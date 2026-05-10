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
    if sub == "query":
        _cmd_query(archive, args)
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

    print("\nGovernance records:")
    print(f"  Evidence: {len(ns.list_evidence())}")
    print(f"  Obligations: {len(ns.list_obligations())}")
    print(f"  Claims: {len(ns.list_claims())}")
    print(f"  Branch decisions: {len(ns.list_branch_decisions())}")
    print(f"  Routes: {len(ns.list_routes())}")
    if hasattr(ns, "list_handoff_imports"):
        print(f"  Handoff imports: {len(ns.list_handoff_imports())}")

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
    claim_failures = []

    # Governance verification is intentionally lightweight here. Record-time
    # validation stores downgrade details in metadata; CLI verify surfaces them.
    for claim in ns.list_claims():
        validation = claim.metadata.get("validation", {})
        if validation and not validation.get("supported", True):
            claim_failures.append(("claim", claim.claim_id, validation))
    for decision in ns.list_branch_decisions():
        validation = decision.metadata.get("validation", {})
        if validation and not validation.get("supported", True):
            claim_failures.append(("branch", decision.decision_id, validation))
    for route in ns.list_routes():
        validation = route.metadata.get("validation", {})
        if validation and not validation.get("supported", True):
            claim_failures.append(("route", route.route_id, validation))

    if not results:
        print("No dependencies declared.")

    failed = 0
    if results:
        print(f"Checking {len(results)} dependencies...")
        for r in results:
            tag = r.status.upper().replace("DEPENDENCY_", "")
            print(f"  {r.dependency.dependency_id} [{tag}]")
            if r.status != "dependency_satisfied":
                print(f"    {r.message}")
                failed += 1

    if claim_failures:
        print(f"\nUnsupported or downgraded governance records ({len(claim_failures)}):")
        for kind, record_id, validation in claim_failures:
            print(
                f"  {kind}:{record_id} "
                f"[{validation.get('requested_status')} -> {validation.get('effective_status')}]"
            )
            for msg in validation.get("messages", []):
                print(f"    {msg}")
        failed += len(claim_failures)

    if failed:
        print(f"\n{failed} verification issue(s).")
        sys.exit(1)
    elif results:
        print(f"\nAll {len(results)} dependencies satisfied.")
    else:
        print("\nNo verification issues found.")


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

    # Governance consistency checks.
    for script_dir in root.iterdir():
        if not script_dir.is_dir():
            continue
        ns = archive.script_namespace(script_dir.name)
        evidence_ids = {ev.evidence_id for ev in ns.list_evidence()}
        for claim in ns.list_claims():
            for evidence_id in claim.evidence_ids:
                if evidence_id not in evidence_ids:
                    issues.append((script_dir, f"claim {claim.claim_id} references missing evidence {evidence_id}"))
            validation = claim.metadata.get("validation", {})
            if validation and not validation.get("supported", True):
                issues.append((script_dir, f"claim {claim.claim_id} downgraded to {validation.get('effective_status')}"))
        for decision in ns.list_branch_decisions():
            for evidence_id in decision.evidence_ids:
                if evidence_id not in evidence_ids:
                    issues.append((script_dir, f"branch {decision.decision_id} references missing evidence {evidence_id}"))
            validation = decision.metadata.get("validation", {})
            if validation and not validation.get("supported", True):
                issues.append((script_dir, f"branch {decision.decision_id} downgraded to {validation.get('effective_status')}"))

    if not issues:
        print("Archive doctor: no issues found.")
    else:
        print(f"Archive doctor: {len(issues)} issue(s) found:")
        for path, msg in issues:
            print(f"  {path}: {msg}")
        print("\nRun 'vf archive invalidate <script_id>' to clear stale entries.")
        sys.exit(1)


def _cmd_query(archive, args) -> None:
    kind = args.query_kind
    if kind == "obligations":
        items = archive.query_obligations(status=args.status)
        for item in items:
            print(f"{item.script_id}:{item.obligation_id} [{item.status.value}] {item.title}")
    elif kind == "claims":
        items = archive.query_claims(status=args.status, tier=args.tier)
        for item in items:
            status = item.status.value if hasattr(item.status, "value") else str(item.status)
            print(f"{item.script_id}:{item.claim_id} [{status}] {item.statement}")
    elif kind == "evidence":
        items = archive.query_evidence(evidence_type=args.type)
        for item in items:
            print(f"{item.script_id}:{item.evidence_id} [{item.evidence_type.value}]")
    elif kind == "branches":
        items = archive.query_branch_decisions(status=args.status)
        for item in items:
            print(f"{item.script_id}:{item.decision_id} [{item.status.value}] {item.branch_id}")
