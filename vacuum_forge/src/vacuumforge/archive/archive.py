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
from vacuumforge.archive.serialization import (
    deserialize_enum,
    deserialize_expr,
    deserialize_optional_expr,
    serialize_enum,
    serialize_expr,
    serialize_optional_expr,
)
from vacuumforge.core.simplify import check_equal
from vacuumforge.core.status import Status
from vacuumforge.governance.evidence import EvidenceType, ReasonCode
from vacuumforge.governance.kinds import DerivationRecordQuality, RecordKind
from vacuumforge.governance.records import (
    BranchDecisionRecord,
    ClaimRecord,
    EvidenceRecord,
    HandoffImportRecord,
    ObligationStatus,
    ProofObligationRecord,
    RouteRecord,
    classify_derivation_record,
)
from vacuumforge.governance.statuses import GovernanceStatus
from vacuumforge.governance.tiers import ClaimTier
from vacuumforge.governance.validation import validate_branch_decision, validate_claim_support, validate_route

_log = logging.getLogger(__name__)


class ProjectArchive:
    """Persistent storage of derivation records across scripts."""

    def __init__(self, root_path: str | Path | None = None, *, root: str | Path | None = None) -> None:
        if root_path is None:
            root_path = root
        if root_path is None:
            raise TypeError("ProjectArchive requires root_path or root")
        self.root_path = Path(root_path)
        self.root = self.root_path
        self.root_path.mkdir(parents=True, exist_ok=True)

    def script_namespace(self, script_id: str) -> ScriptNamespace:
        return ScriptNamespace(self, script_id)

    def __enter__(self) -> "ProjectArchive":
        return self

    def __exit__(self, exc_type, exc, tb) -> bool:
        return False

    def query_claims(self, *, status=None, tier=None) -> list[ClaimRecord]:
        claims: list[ClaimRecord] = []
        for ns in self._namespaces():
            for claim in ns.list_claims():
                if status is not None and _value(claim.status) != _value(status):
                    continue
                if tier is not None and claim.tier != _coerce(ClaimTier, tier, tier):
                    continue
                claims.append(claim)
        return claims

    def query_obligations(self, *, status=None) -> list[ProofObligationRecord]:
        items: list[ProofObligationRecord] = []
        status_value = _coerce(ObligationStatus, status, status) if status is not None else None
        for ns in self._namespaces():
            items.extend(ns.list_obligations(status=status_value))
        return items

    def query_evidence(self, *, evidence_type=None, supports=None, challenges=None) -> list[EvidenceRecord]:
        items: list[EvidenceRecord] = []
        expected_type = _coerce(EvidenceType, evidence_type, evidence_type) if evidence_type else None
        for ns in self._namespaces():
            for ev in ns.list_evidence():
                if expected_type is not None and ev.evidence_type != expected_type:
                    continue
                if supports is not None and supports not in ev.supports:
                    continue
                if challenges is not None and challenges not in ev.challenges:
                    continue
                items.append(ev)
        return items

    def query_branch_decisions(self, *, status=None, branch_id=None) -> list[BranchDecisionRecord]:
        items: list[BranchDecisionRecord] = []
        status_value = _coerce(GovernanceStatus, status, status) if status is not None else None
        for ns in self._namespaces():
            for decision in ns.list_branch_decisions(branch_id=branch_id):
                if status_value is not None and decision.status != status_value:
                    continue
                items.append(decision)
        return items

    def _namespaces(self) -> list[ScriptNamespace]:
        if not self.root_path.exists():
            return []
        return [self.script_namespace(p.name) for p in self.root_path.iterdir() if p.is_dir()]

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
        self.evidence_path = self.path / "evidence"
        self.obligations_path = self.path / "obligations"
        self.claims_path = self.path / "claims"
        self.branches_path = self.path / "branches"
        self.routes_path = self.path / "routes"
        self.handoffs_path = self.path / "handoffs"
        for p in (
            self.evidence_path,
            self.obligations_path,
            self.claims_path,
            self.branches_path,
            self.routes_path,
            self.handoffs_path,
        ):
            p.mkdir(parents=True, exist_ok=True)

    # -- Recording -------------------------------------------------------------

    def record_derivation(
        self,
        derivation_id: str,
        inputs: list[sympy.Basic],
        output: sympy.Basic,
        method: str,
        status: Status,
        metadata: dict[str, Any] | None = None,
        record_kind: RecordKind = RecordKind.DERIVATION,
        scope: str | None = None,
        claim_tier: str | None = None,
        result_type: str | None = None,
        superseded_by: str | None = None,
        is_placeholder: bool = False,
    ) -> DerivationRecord:
        record = DerivationRecord(
            derivation_id=derivation_id,
            inputs=inputs,
            output=output,
            method=method,
            status=status,
            metadata=dict(metadata or {}),
            recorded_at=_now(),
            record_kind=record_kind,
            scope=scope,
            claim_tier=claim_tier,
            result_type=result_type,
            superseded_by=superseded_by,
            is_placeholder=is_placeholder,
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
        expected_status: str | None = None,
        expected_record_kind: RecordKind | None = None,
        allow_superseded: bool = False,
    ) -> DependencyDeclaration:
        dep = DependencyDeclaration(
            dependency_id=dependency_id,
            upstream_script_id=upstream_script_id,
            upstream_derivation_id=upstream_derivation_id,
            expected_output=expected_output,
            expected_status=expected_status,
            expected_record_kind=expected_record_kind,
            allow_superseded=allow_superseded,
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
            if record.superseded_by and not dep.allow_superseded:
                results.append(
                    DependencyCheckResult(
                        dep,
                        "dependency_superseded",
                        f"Upstream derivation is superseded by {record.superseded_by}.",
                        dep.expected_output,
                        record.output,
                    )
                )
                continue
            if dep.expected_status is not None and record.status.value != dep.expected_status:
                results.append(
                    DependencyCheckResult(
                        dep,
                        "dependency_status_mismatch",
                        f"Expected status {dep.expected_status}; found {record.status.value}.",
                        dep.expected_output,
                        record.output,
                    )
                )
                continue
            if dep.expected_record_kind is not None and record.record_kind != dep.expected_record_kind:
                results.append(
                    DependencyCheckResult(
                        dep,
                        "dependency_kind_mismatch",
                        f"Expected record kind {dep.expected_record_kind.value}; "
                        f"found {record.record_kind.value}.",
                        dep.expected_output,
                        record.output,
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
                        dep.expected_output,
                        record.output,
                    )
                )
            else:
                residual = None
                try:
                    residual = sympy.simplify(record.output - dep.expected_output)
                except Exception:
                    residual = None
                results.append(
                    DependencyCheckResult(
                        dep,
                        "dependency_changed",
                        f"Expected: {dep.expected_output}; Found: {record.output}.",
                        dep.expected_output,
                        record.output,
                        residual,
                    )
                )
        return results

    # -- Governance records ----------------------------------------------------

    def record_evidence(self, evidence: EvidenceRecord) -> EvidenceRecord:
        if not evidence.created_at:
            evidence.created_at = _now()
        _atomic_write_json(self.evidence_path / f"{evidence.evidence_id}.json", _evidence_to_json(evidence))
        return evidence

    def get_evidence(self, evidence_id: str) -> EvidenceRecord | None:
        return _read_record(self.evidence_path / f"{evidence_id}.json", _evidence_from_json)

    def list_evidence(self) -> list[EvidenceRecord]:
        return _list_records(self.evidence_path, _evidence_from_json)

    def record_obligation(self, obligation: ProofObligationRecord) -> ProofObligationRecord:
        if not obligation.created_at:
            obligation.created_at = _now()
        _atomic_write_json(self.obligations_path / f"{obligation.obligation_id}.json", _obligation_to_json(obligation))
        return obligation

    def get_obligation(self, obligation_id: str) -> ProofObligationRecord | None:
        return _read_record(self.obligations_path / f"{obligation_id}.json", _obligation_from_json)

    def list_obligations(self, status: ObligationStatus | None = None) -> list[ProofObligationRecord]:
        items = _list_records(self.obligations_path, _obligation_from_json)
        if status is None:
            return items
        return [o for o in items if o.status == status]

    def update_obligation_status(
        self,
        obligation_id: str,
        status: ObligationStatus,
        *,
        by: str | None = None,
    ) -> ProofObligationRecord:
        record = self.get_obligation(obligation_id)
        if record is None:
            raise KeyError(obligation_id)
        history = list(record.metadata.get("history", []))
        history.append({"at": _now(), "from": record.status.value, "to": status.value, "by": by})
        record.status = status
        record.metadata["history"] = history
        if by and status == ObligationStatus.SATISFIED and by not in record.satisfied_by:
            record.satisfied_by.append(by)
        self.record_obligation(record)
        return record

    def record_claim(self, claim: ClaimRecord) -> ClaimRecord:
        if not claim.created_at:
            claim.created_at = _now()
        validation = validate_claim_support(claim, resolver=self)
        claim.metadata["validation"] = validation.__dict__
        if not validation.supported:
            claim.status = validation.effective_status
        _atomic_write_json(self.claims_path / f"{claim.claim_id}.json", _claim_to_json(claim))
        return claim

    def get_claim(self, claim_id: str) -> ClaimRecord | None:
        return _read_record(self.claims_path / f"{claim_id}.json", _claim_from_json)

    def list_claims(self, *, tier: ClaimTier | None = None, status: str | None = None) -> list[ClaimRecord]:
        items = _list_records(self.claims_path, _claim_from_json)
        if tier is not None:
            items = [c for c in items if c.tier == tier]
        if status is not None:
            items = [c for c in items if _value(c.status) == status]
        return items

    def record_branch_decision(self, decision: BranchDecisionRecord) -> BranchDecisionRecord:
        if not decision.created_at:
            decision.created_at = _now()
        validation = validate_branch_decision(decision, resolver=self)
        decision.metadata["validation"] = validation.__dict__
        if not validation.supported:
            decision.status = _coerce(GovernanceStatus, validation.effective_status, GovernanceStatus.UNVERIFIED)
        _atomic_write_json(self.branches_path / f"{decision.decision_id}.json", _branch_to_json(decision))
        return decision

    def get_branch_decision(self, decision_id: str) -> BranchDecisionRecord | None:
        return _read_record(self.branches_path / f"{decision_id}.json", _branch_from_json)

    def list_branch_decisions(self, branch_id: str | None = None) -> list[BranchDecisionRecord]:
        items = _list_records(self.branches_path, _branch_from_json)
        if branch_id is not None:
            items = [d for d in items if d.branch_id == branch_id]
        return items

    def record_route(self, route: RouteRecord) -> RouteRecord:
        if not route.created_at:
            route.created_at = _now()
        validation = validate_route(route, resolver=self)
        route.metadata["validation"] = validation.__dict__
        if not validation.supported:
            route.status = _coerce(GovernanceStatus, validation.effective_status, GovernanceStatus.UNVERIFIED)
        _atomic_write_json(self.routes_path / f"{route.route_id}.json", _route_to_json(route))
        return route

    def get_route(self, route_id: str) -> RouteRecord | None:
        return _read_record(self.routes_path / f"{route_id}.json", _route_from_json)

    def list_routes(self, status: GovernanceStatus | None = None) -> list[RouteRecord]:
        items = _list_records(self.routes_path, _route_from_json)
        if status is not None:
            items = [r for r in items if r.status == status]
        return items

    def record_handoff_import(self, handoff: HandoffImportRecord) -> HandoffImportRecord:
        if not handoff.created_at:
            handoff.created_at = _now()
        _atomic_write_json(self.handoffs_path / f"{handoff.handoff_id}.json", _handoff_to_json(handoff))
        return handoff

    def list_handoff_imports(self) -> list[HandoffImportRecord]:
        return _list_records(self.handoffs_path, _handoff_from_json)

    def has_evidence(self, evidence_id: str) -> bool:
        return self.get_evidence(evidence_id) is not None

    def has_derivation(self, derivation_id: str) -> bool:
        return self.get_derivation(derivation_id) is not None

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
        "record_kind": record.record_kind.value,
        "scope": record.scope,
        "claim_tier": record.claim_tier,
        "result_type": record.result_type,
        "superseded_by": record.superseded_by,
        "is_placeholder": record.is_placeholder,
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
        record_kind=_coerce(RecordKind, data.get("record_kind"), RecordKind.DERIVATION),
        scope=data.get("scope") if data.get("scope") is not None else None,
        claim_tier=data.get("claim_tier") if data.get("claim_tier") is not None else None,
        result_type=data.get("result_type") if data.get("result_type") is not None else None,
        superseded_by=data.get("superseded_by") if data.get("superseded_by") is not None else None,
        is_placeholder=bool(data.get("is_placeholder", False)),
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
    if dep.expected_status is not None:
        data["expected_status"] = dep.expected_status
    if dep.expected_record_kind is not None:
        data["expected_record_kind"] = dep.expected_record_kind.value
    data["allow_superseded"] = dep.allow_superseded
    return data


def _dep_from_json(data: dict[str, object]) -> DependencyDeclaration:
    expected = data.get("expected_output")
    return DependencyDeclaration(
        dependency_id=str(data["dependency_id"]),
        upstream_script_id=str(data["upstream_script_id"]),
        upstream_derivation_id=str(data["upstream_derivation_id"]),
        expected_output=deserialize_expr(expected) if isinstance(expected, dict) else None,
        expected_status=str(data["expected_status"]) if data.get("expected_status") is not None else None,
        expected_record_kind=_coerce(RecordKind, data.get("expected_record_kind"), None),
        allow_superseded=bool(data.get("allow_superseded", False)),
        declared_at=str(data.get("declared_at", "")),
    )


def _value(obj: Any) -> str:
    return obj.value if hasattr(obj, "value") else str(obj)


def _coerce(enum_cls, value, default=None):
    return deserialize_enum(enum_cls, value, default)


def _read_record(path: Path, loader):
    if not path.exists():
        return None
    try:
        return loader(json.loads(path.read_text(encoding="utf-8")))
    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        _log.warning("Corrupt archive file %s: %s", path, exc)
        return None


def _list_records(path: Path, loader) -> list:
    records = []
    if not path.exists():
        return records
    for item in sorted(path.glob("*.json")):
        record = _read_record(item, loader)
        if record is not None:
            records.append(record)
    return records


def _evidence_to_json(record: EvidenceRecord) -> dict[str, object]:
    return {
        "evidence_id": record.evidence_id,
        "evidence_type": record.evidence_type.value,
        "script_id": record.script_id,
        "supports": record.supports,
        "challenges": record.challenges,
        "reason_code": serialize_enum(record.reason_code),
        "expression": serialize_optional_expr(record.expression),
        "expected": serialize_optional_expr(record.expected),
        "observed": serialize_optional_expr(record.observed),
        "residual": serialize_optional_expr(record.residual),
        "source_records": record.source_records,
        "status": record.status,
        "created_at": record.created_at,
        "description": record.description,
        "metadata": record.metadata,
    }


def _evidence_from_json(data: dict[str, object]) -> EvidenceRecord:
    return EvidenceRecord(
        evidence_id=str(data["evidence_id"]),
        evidence_type=_coerce(EvidenceType, data["evidence_type"]),
        script_id=str(data["script_id"]),
        supports=list(data.get("supports", [])),
        challenges=list(data.get("challenges", [])),
        reason_code=_coerce(ReasonCode, data.get("reason_code"), None),
        expression=deserialize_optional_expr(data.get("expression")),
        expected=deserialize_optional_expr(data.get("expected")),
        observed=deserialize_optional_expr(data.get("observed")),
        residual=deserialize_optional_expr(data.get("residual")),
        source_records=list(data.get("source_records", [])),
        status=str(data.get("status", "active")),
        created_at=str(data.get("created_at", "")),
        description=data.get("description") if data.get("description") is not None else None,
        metadata=dict(data.get("metadata", {})),
    )


def _obligation_to_json(record: ProofObligationRecord) -> dict[str, object]:
    return {
        "obligation_id": record.obligation_id,
        "script_id": record.script_id,
        "title": record.title,
        "status": record.status.value,
        "required_by": record.required_by,
        "satisfied_by": record.satisfied_by,
        "failed_by": record.failed_by,
        "superseded_by": record.superseded_by,
        "created_at": record.created_at,
        "description": record.description,
        "metadata": record.metadata,
    }


def _obligation_from_json(data: dict[str, object]) -> ProofObligationRecord:
    return ProofObligationRecord(
        obligation_id=str(data["obligation_id"]),
        script_id=str(data["script_id"]),
        title=str(data["title"]),
        status=_coerce(ObligationStatus, data["status"]),
        required_by=list(data.get("required_by", [])),
        satisfied_by=list(data.get("satisfied_by", [])),
        failed_by=list(data.get("failed_by", [])),
        superseded_by=data.get("superseded_by") if data.get("superseded_by") is not None else None,
        created_at=str(data.get("created_at", "")),
        description=data.get("description") if data.get("description") is not None else None,
        metadata=dict(data.get("metadata", {})),
    )


def _claim_to_json(record: ClaimRecord) -> dict[str, object]:
    return {
        "claim_id": record.claim_id,
        "script_id": record.script_id,
        "claim_kind": record.claim_kind.value,
        "tier": record.tier.value,
        "status": _value(record.status),
        "statement": record.statement,
        "reason_code": serialize_enum(record.reason_code),
        "evidence_ids": record.evidence_ids,
        "derivation_ids": record.derivation_ids,
        "obligation_ids": record.obligation_ids,
        "source_claim_ids": record.source_claim_ids,
        "supersedes": record.supersedes,
        "superseded_by": record.superseded_by,
        "created_at": record.created_at,
        "metadata": record.metadata,
    }


def _claim_from_json(data: dict[str, object]) -> ClaimRecord:
    status = _coerce(GovernanceStatus, data.get("status"), data.get("status"))
    return ClaimRecord(
        claim_id=str(data["claim_id"]),
        script_id=str(data["script_id"]),
        claim_kind=_coerce(RecordKind, data["claim_kind"]),
        tier=_coerce(ClaimTier, data["tier"]),
        status=status,
        statement=str(data["statement"]),
        reason_code=_coerce(ReasonCode, data.get("reason_code"), None),
        evidence_ids=list(data.get("evidence_ids", [])),
        derivation_ids=list(data.get("derivation_ids", [])),
        obligation_ids=list(data.get("obligation_ids", [])),
        source_claim_ids=list(data.get("source_claim_ids", [])),
        supersedes=list(data.get("supersedes", [])),
        superseded_by=data.get("superseded_by") if data.get("superseded_by") is not None else None,
        created_at=str(data.get("created_at", "")),
        metadata=dict(data.get("metadata", {})),
    )


def _branch_to_json(record: BranchDecisionRecord) -> dict[str, object]:
    return {
        "decision_id": record.decision_id,
        "script_id": record.script_id,
        "branch_id": record.branch_id,
        "status": record.status.value,
        "tier": record.tier.value,
        "reason_code": serialize_enum(record.reason_code),
        "evidence_ids": record.evidence_ids,
        "obligation_ids": record.obligation_ids,
        "activation_conditions": record.activation_conditions,
        "superseded_by": record.superseded_by,
        "created_at": record.created_at,
        "description": record.description,
        "metadata": record.metadata,
    }


def _branch_from_json(data: dict[str, object]) -> BranchDecisionRecord:
    return BranchDecisionRecord(
        decision_id=str(data["decision_id"]),
        script_id=str(data["script_id"]),
        branch_id=str(data["branch_id"]),
        status=_coerce(GovernanceStatus, data["status"]),
        tier=_coerce(ClaimTier, data["tier"]),
        reason_code=_coerce(ReasonCode, data.get("reason_code"), None),
        evidence_ids=list(data.get("evidence_ids", [])),
        obligation_ids=list(data.get("obligation_ids", [])),
        activation_conditions=list(data.get("activation_conditions", [])),
        superseded_by=data.get("superseded_by") if data.get("superseded_by") is not None else None,
        created_at=str(data.get("created_at", "")),
        description=data.get("description") if data.get("description") is not None else None,
        metadata=dict(data.get("metadata", {})),
    )


def _route_to_json(record: RouteRecord) -> dict[str, object]:
    return {
        "route_id": record.route_id,
        "script_id": record.script_id,
        "name": record.name,
        "status": record.status.value,
        "tier": record.tier.value,
        "witness_ids": record.witness_ids,
        "activation_conditions": record.activation_conditions,
        "required_obligations": record.required_obligations,
        "created_at": record.created_at,
        "description": record.description,
        "metadata": record.metadata,
    }


def _route_from_json(data: dict[str, object]) -> RouteRecord:
    return RouteRecord(
        route_id=str(data["route_id"]),
        script_id=str(data["script_id"]),
        name=str(data["name"]),
        status=_coerce(GovernanceStatus, data["status"]),
        tier=_coerce(ClaimTier, data["tier"]),
        witness_ids=list(data.get("witness_ids", [])),
        activation_conditions=list(data.get("activation_conditions", [])),
        required_obligations=list(data.get("required_obligations", [])),
        created_at=str(data.get("created_at", "")),
        description=data.get("description") if data.get("description") is not None else None,
        metadata=dict(data.get("metadata", {})),
    )


def _handoff_to_json(record: HandoffImportRecord) -> dict[str, object]:
    return {
        "handoff_id": record.handoff_id,
        "script_id": record.script_id,
        "source_record_ref": record.source_record_ref,
        "imported_record_refs": record.imported_record_refs,
        "imported_as": record.imported_as.value,
        "status": _value(record.status),
        "created_at": record.created_at,
        "description": record.description,
        "metadata": record.metadata,
    }


def _handoff_from_json(data: dict[str, object]) -> HandoffImportRecord:
    status = _coerce(GovernanceStatus, data.get("status"), data.get("status"))
    return HandoffImportRecord(
        handoff_id=str(data["handoff_id"]),
        script_id=str(data["script_id"]),
        imported_as=_coerce(RecordKind, data["imported_as"]),
        status=status,
        source_record_ref=str(data.get("source_record_ref", "")),
        imported_record_refs=list(data.get("imported_record_refs", [])),
        created_at=str(data.get("created_at", "")),
        description=data.get("description") if data.get("description") is not None else None,
        metadata=dict(data.get("metadata", {})),
    )
