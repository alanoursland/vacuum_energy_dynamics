"""Persistent derivation archive.

Implements Milestones 49-50 from the validation-hardening technical design.
"""

from __future__ import annotations

import datetime as _dt
import json
import logging
import os
from pathlib import Path
from typing import Any

import sympy

from vacuumforge.archive.records import (
    DependencyCheckResult,
    DependencyDeclaration,
    DerivationRecord,
)
from vacuumforge.archive.serialization import deserialize_expr, serialize_expr
from vacuumforge.core.simplify import check_equal
from vacuumforge.core.status import Status

_log = logging.getLogger(__name__)


class ProjectArchive:
    """Persistent storage of derivation records across scripts."""

    def __init__(self, root_path: str | Path) -> None:
        self.root_path = Path(root_path)
        self.root_path.mkdir(parents=True, exist_ok=True)

    def script_namespace(self, script_id: str) -> ScriptNamespace:
        return ScriptNamespace(self, script_id)

    def detect_cycles(self) -> list[list[str]]:
        """Return a list of dependency cycles across all scripts.

        Each cycle is a list of script_ids forming the loop.
        """
        import networkx as nx

        graph = nx.DiGraph()
        for script_dir in self.root_path.iterdir():
            if not script_dir.is_dir():
                continue
            script_id = script_dir.name
            deps_file = script_dir / "dependencies.json"
            if not deps_file.exists():
                continue
            try:
                data = json.loads(deps_file.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                continue
            for item in data:
                upstream = item.get("upstream_script_id", "")
                if upstream:
                    graph.add_edge(upstream, script_id)

        cycles: list[list[str]] = []
        try:
            cycles = list(nx.simple_cycles(graph))
        except nx.NetworkXError:
            pass
        return cycles


class ScriptNamespace:
    """Archive namespace for one script."""

    def __init__(self, archive: ProjectArchive, script_id: str) -> None:
        self.archive = archive
        self.script_id = script_id
        self.path = archive.root_path / script_id
        self.derivations_path = self.path / "derivations"
        self.derivations_path.mkdir(parents=True, exist_ok=True)

    # -- Recording -------------------------------------------------------------

    def record_derivation(
        self,
        derivation_id: str,
        inputs: list[sympy.Basic],
        output: sympy.Basic,
        method: str,
        status: Status,
        metadata: dict[str, Any] | None = None,
    ) -> DerivationRecord:
        record = DerivationRecord(
            derivation_id=derivation_id,
            inputs=inputs,
            output=output,
            method=method,
            status=status,
            metadata=dict(metadata or {}),
            recorded_at=_now(),
        )
        _atomic_write_json(self._derivation_file(derivation_id), _record_to_json(record))
        return record

    def get_derivation(self, derivation_id: str) -> DerivationRecord | None:
        path = self._derivation_file(derivation_id)
        if not path.exists():
            return None
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            return _record_from_json(data)
        except (json.JSONDecodeError, KeyError, TypeError) as exc:
            _log.warning("Corrupt derivation file %s: %s", path, exc)
            return None

    # -- Dependencies ----------------------------------------------------------

    def declare_dependency(
        self,
        dependency_id: str,
        upstream_script_id: str,
        upstream_derivation_id: str,
        expected_output: sympy.Basic | None = None,
    ) -> DependencyDeclaration:
        dep = DependencyDeclaration(
            dependency_id=dependency_id,
            upstream_script_id=upstream_script_id,
            upstream_derivation_id=upstream_derivation_id,
            expected_output=expected_output,
            declared_at=_now(),
        )
        deps = self._load_dependencies()
        deps = [d for d in deps if d.dependency_id != dependency_id]
        deps.append(dep)
        _atomic_write_json(self.path / "dependencies.json", [_dep_to_json(d) for d in deps])
        return dep

    def verify_dependencies(self, ctx=None) -> list[DependencyCheckResult]:
        """Verify all declared dependencies.

        Returns a list of results with statuses:
        - dependency_satisfied
        - dependency_changed
        - dependency_missing
        - dependency_cycle
        """
        # Check for cycles first.
        cycles = self.archive.detect_cycles()
        involved_scripts = set()
        for cycle in cycles:
            involved_scripts.update(cycle)

        results: list[DependencyCheckResult] = []
        for dep in self._load_dependencies():
            # Report cycle if this dependency is part of one.
            if (
                self.script_id in involved_scripts
                and dep.upstream_script_id in involved_scripts
            ):
                cycle_strs = [" -> ".join(c) for c in cycles
                              if self.script_id in c and dep.upstream_script_id in c]
                results.append(
                    DependencyCheckResult(
                        dep, "dependency_cycle",
                        f"Cycle detected: {'; '.join(cycle_strs) or 'circular dependency'}.",
                    )
                )
                continue

            upstream = self.archive.script_namespace(dep.upstream_script_id)
            record = upstream.get_derivation(dep.upstream_derivation_id)
            if record is None:
                results.append(
                    DependencyCheckResult(
                        dep, "dependency_missing",
                        f"Upstream derivation '{dep.upstream_derivation_id}' "
                        f"not found in archive for script '{dep.upstream_script_id}'.",
                    )
                )
                continue
            if dep.expected_output is None:
                results.append(
                    DependencyCheckResult(
                        dep,
                        "dependency_satisfied",
                        "Upstream derivation exists; output not verified "
                        "(no expected_output declared).",
                    )
                )
                continue
            if check_equal(record.output, dep.expected_output):
                results.append(
                    DependencyCheckResult(
                        dep, "dependency_satisfied",
                        "Upstream derivation matches expected output.",
                    )
                )
            else:
                results.append(
                    DependencyCheckResult(
                        dep,
                        "dependency_changed",
                        f"Expected: {dep.expected_output}; Found: {record.output}.",
                    )
                )
        return results

    # -- Invalidation ----------------------------------------------------------

    def invalidate(self) -> None:
        """Clear all derivation entries for this script."""
        for path in self.derivations_path.glob("*.json"):
            path.unlink()

    def check_source_invalidation(self, script_path: str | Path) -> bool:
        """Compare the script's current source hash against the stored one.

        If the hash has changed, invalidates all derivation entries and
        stores the new hash.  Returns True if invalidation occurred.
        """
        from vacuumforge.archive.invalidation import check_and_invalidate

        return check_and_invalidate(self.path, script_path, self.derivations_path)

    # -- Metadata --------------------------------------------------------------

    def write_run_metadata(self, **extra: Any) -> None:
        """Write last-run metadata to the namespace directory."""
        import vacuumforge

        metadata: dict[str, Any] = {
            "script_id": self.script_id,
            "vacuumforge_version": getattr(vacuumforge, "__version__", "0.1.0"),
            "recorded_at": _now(),
        }
        metadata.update(extra)
        _atomic_write_json(self.path / "last_run_metadata.json", metadata)

    # -- Internal --------------------------------------------------------------

    def _derivation_file(self, derivation_id: str) -> Path:
        return self.derivations_path / f"{derivation_id}.json"

    def _load_dependencies(self) -> list[DependencyDeclaration]:
        path = self.path / "dependencies.json"
        if not path.exists():
            return []
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            return [_dep_from_json(item) for item in data]
        except (json.JSONDecodeError, KeyError, TypeError) as exc:
            _log.warning("Corrupt dependencies file %s: %s", path, exc)
            return []


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _now() -> str:
    return _dt.datetime.now(tz=_dt.timezone.utc).isoformat()


def _atomic_write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2), encoding="utf-8")
    os.replace(tmp, path)


def _record_to_json(record: DerivationRecord) -> dict[str, object]:
    return {
        "derivation_id": record.derivation_id,
        "inputs": [serialize_expr(expr) for expr in record.inputs],
        "output": serialize_expr(record.output),
        "method": record.method,
        "status": record.status.value,
        "metadata": record.metadata,
        "recorded_at": record.recorded_at,
        "vacuumforge_version": record.vacuumforge_version,
    }


def _record_from_json(data: dict[str, object]) -> DerivationRecord:
    return DerivationRecord(
        derivation_id=str(data["derivation_id"]),
        inputs=[deserialize_expr(expr) for expr in data.get("inputs", [])],
        output=deserialize_expr(data["output"]),
        method=str(data["method"]),
        status=Status(str(data["status"])),
        metadata=dict(data.get("metadata", {})),
        recorded_at=str(data.get("recorded_at", "")),
        vacuumforge_version=str(data.get("vacuumforge_version", "0.1.0")),
    )


def _dep_to_json(dep: DependencyDeclaration) -> dict[str, object]:
    data: dict[str, object] = {
        "dependency_id": dep.dependency_id,
        "upstream_script_id": dep.upstream_script_id,
        "upstream_derivation_id": dep.upstream_derivation_id,
        "declared_at": dep.declared_at,
    }
    if dep.expected_output is not None:
        data["expected_output"] = serialize_expr(dep.expected_output)
    return data


def _dep_from_json(data: dict[str, object]) -> DependencyDeclaration:
    expected = data.get("expected_output")
    return DependencyDeclaration(
        dependency_id=str(data["dependency_id"]),
        upstream_script_id=str(data["upstream_script_id"]),
        upstream_derivation_id=str(data["upstream_derivation_id"]),
        expected_output=deserialize_expr(expected) if isinstance(expected, dict) else None,
        declared_at=str(data.get("declared_at", "")),
    )
