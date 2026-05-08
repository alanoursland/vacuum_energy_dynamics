"""CLI subcommands for the project archive.

Implements Milestone 51: ``vf archive list|verify|invalidate|doctor``.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


def cmd_archive(args: Any) -> None:
    """Dispatch archive subcommands."""
    from vacuumforge.archive import ProjectArchive

    archive = ProjectArchive(args.root)

    sub = args.archive_command
    if sub is None:
        print("Usage: vacuumforge archive {list,verify,invalidate,doctor}")
        sys.exit(1)

    if sub == "doctor":
        _cmd_doctor(archive, args)
        return

    # All other subcommands require a script_id.
    ns = archive.script_namespace(args.script_id)

    if sub == "list":
        _cmd_list(ns)
    elif sub == "verify":
        _cmd_verify(ns)
    elif sub == "invalidate":
        _cmd_invalidate(ns)


def _cmd_list(ns) -> None:
    """List derivations and dependencies for a script."""
    derivations = sorted(p.stem for p in ns.derivations_path.glob("*.json"))
    print(f"Derivations ({len(derivations)}):")
    if derivations:
        for d in derivations:
            record = ns.get_derivation(d)
            if record is not None:
                print(f"  {d} [{record.status.value}, {record.method}]")
            else:
                print(f"  {d} [corrupt or unreadable]")
    else:
        print("  (none)")

    deps = ns._load_dependencies()
    print(f"\nDependencies ({len(deps)}):")
    if deps:
        for dep in deps:
            print(f"  {dep.dependency_id}: {dep.upstream_script_id}/{dep.upstream_derivation_id}")
    else:
        print("  (none declared)")

    # Metadata.
    meta_path = ns.path / "last_run_metadata.json"
    if meta_path.exists():
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
            print(f"\nLast run: {meta.get('recorded_at', 'unknown')}")
        except (json.JSONDecodeError, OSError):
            pass

    hash_path = ns.path / "source_hash.json"
    if hash_path.exists():
        try:
            h = json.loads(hash_path.read_text(encoding="utf-8"))
            print(f"Source hash: {h.get('sha256', 'unknown')}")
        except (json.JSONDecodeError, OSError):
            pass


def _cmd_verify(ns) -> None:
    """Verify dependencies for a script."""
    results = ns.verify_dependencies()
    if not results:
        print("No dependencies declared.")
        return

    print(f"Checking {len(results)} dependencies...")
    failed = 0
    for r in results:
        tag = r.status.upper().replace("DEPENDENCY_", "")
        print(f"  {r.dependency.dependency_id} [{tag}]")
        if r.status != "dependency_satisfied":
            print(f"    {r.message}")
            failed += 1

    if failed:
        print(f"\n{failed} of {len(results)} dependencies failed verification.")
        sys.exit(1)
    else:
        print(f"\nAll {len(results)} dependencies satisfied.")


def _cmd_invalidate(ns) -> None:
    """Clear derivations for a script."""
    ns.invalidate()
    print(f"Invalidated archive entries for {ns.script_id}.")


def _cmd_doctor(archive, args) -> None:
    """Scan archive for corruption and report issues."""
    root = Path(args.root)
    if not root.exists():
        print(f"Archive root {root} does not exist.")
        sys.exit(1)

    issues: list[tuple[Path, str]] = []

    for json_path in root.rglob("*.json"):
        try:
            json.loads(json_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            issues.append((json_path, f"malformed JSON: {exc}"))
        except OSError as exc:
            issues.append((json_path, f"read error: {exc}"))

    # Check for source hash mismatches.
    for script_dir in root.iterdir():
        if not script_dir.is_dir():
            continue
        hash_file = script_dir / "source_hash.json"
        if hash_file.exists():
            try:
                h = json.loads(hash_file.read_text(encoding="utf-8"))
                if "sha256" not in h:
                    issues.append((hash_file, "missing sha256 field"))
            except (json.JSONDecodeError, OSError):
                pass  # Already caught above.

    # Check for cycles.
    cycles = archive.detect_cycles()
    if cycles:
        for cycle in cycles:
            cycle_str = " -> ".join(cycle)
            issues.append((root, f"dependency cycle: {cycle_str}"))

    if not issues:
        print("Archive doctor: no issues found.")
    else:
        print(f"Archive doctor: {len(issues)} issue(s) found:")
        for path, msg in issues:
            print(f"  {path}: {msg}")
        print("\nRun 'vf archive invalidate <script_id>' to clear stale entries.")
        sys.exit(1)
