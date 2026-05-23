from __future__ import annotations
from pathlib import Path
import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    ClaimRecord, ClaimTier, GovernanceStatus, ObligationStatus,
    ProofObligationRecord, RecordKind, ScriptOutput, StatusMark,
)

ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"

def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)

def prepare_archive(dependencies):
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    for dep_id, upstream_script_id, upstream_derivation_id in dependencies:
        ns.declare_dependency(
            dependency_id=dep_id,
            upstream_script_id=upstream_script_id,
            upstream_derivation_id=upstream_derivation_id,
        )
    return archive, ns, invalidated

def print_archive_status(ns, invalidated: bool) -> None:
    if invalidated:
        print("[INFO] Archive invalidated due to source change.")
    checks = ns.verify_dependencies()
    if not checks:
        print("[INFO] Archive dependencies: none declared.")
        return
    print("[INFO] Archive dependency check:")
    for check in checks:
        print(f"  - {check.dependency.dependency_id}: {check.status} ({check.message})")

def record_marker(ns, marker_id: str, scope: str) -> None:
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[],
        output=sp.Symbol(marker_id),
        method="inventory marker; no physical derivation",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
        scope=scope,
    )

def record_claim(ns, marker_id: str, claim_id: str, status: GovernanceStatus, statement: str) -> None:
    ns.record_claim(
        ClaimRecord(
            claim_id=claim_id,
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=status,
            statement=statement,
            derivation_ids=[marker_id],
            obligation_ids=[],
        )
    )

def record_obligation(ns, obligation_id: str, statement: str, status: ObligationStatus = ObligationStatus.OPEN) -> None:
    ns.record_obligation(
        ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=obligation_id,
            status=status,
            required_by=[SCRIPT_ID],
            description=statement,
        )
    )

DEPENDENCIES = [
    ("g77_summary", "077_remainder_obstruction_audit__candidate_group_77_status_summary", "g77_summary"),
]
MARKER_ID = "g78_problem"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Boundary-Lift Split Obligation Ledger Problem")
    print("Question:")
    print("  What remains owed after the boundary-lift route split and rho audit?")
    print()
    print("Imported Group 77 status:")
    print("  rho status remains unresolved")
    print("  zero/gauge-exact/boundary-exact/inert routes are theorem targets only")
    print("  shared lift identity remains not closed")
    print("  D_layer remains separate unresolved theorem target")
    print("  parent divergence identity unproven")
    print("  recombination blocked")

    with out.governance_assessments():
        out.line("group opened", StatusMark.PASS, "split obligation ledger opened")
        out.line("route management", StatusMark.INFO, "this group records obligations; it is not a theorem attempt")
        out.line("parent status", StatusMark.DEFER, "parent equation remains blocked")
        out.line("recombination", StatusMark.DEFER, "parent recombination remains blocked")
    with out.counterexamples():
        out.line("summary as theorem", StatusMark.FAIL, "ledger cannot be treated as derivation")
        out.line("abstract rerun", StatusMark.FAIL, "do not repeat broad audits without concrete input")
        out.line("active O escape", StatusMark.FAIL, "active O remains unconstructed and out of scope")
        out.line("parent construction", StatusMark.FAIL, "do not write parent equation during ledger group")
    with out.unresolved_obligations():
        out.line("ledger", StatusMark.OBLIGATION, "inventory open, retained, deferred, blocked, and rejected routes")
        out.line("readiness gates", StatusMark.OBLIGATION, "state what concrete input is required for future groups")

    record_marker(ns, MARKER_ID, "Group 78 opening; no parent equation")
    record_claim(ns, MARKER_ID, "g78_problem_c1", GovernanceStatus.UNVERIFIED, "Group 78 opens boundary-lift split obligation ledger.")
    record_obligation(ns, "g78_problem_o1", "Inventory split obligations and readiness gates.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_split_target_inventory.py")

if __name__ == "__main__":
    main()
