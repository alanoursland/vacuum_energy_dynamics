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
        method="route/governance marker; no physical derivation",
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
    ("g73_summary", "073_layer_generator_construction__candidate_group_73_status_summary", "g73_summary"),
]
MARKER_ID = "g74_problem"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Boundary-Lift Route Split Decision Problem")
    print("Question:")
    print("  Should the boundary-lift route remain monolithic, split into theorem targets, downgrade, or jump to active O?")
    print()
    print("Imported Group 73 status:")
    print("  geometric D_layer generator not derived")
    print("  D_layer legitimacy unresolved")
    print("  signed-distance / measure scaffolds retained only as theorem inputs")
    print("  L_bulk/L_gauge lift cleanliness remains open")
    print("  parent divergence identity unproven")
    print("  recombination blocked")

    with out.governance_assessments():
        out.line("group opened", StatusMark.PASS, "boundary-lift route split decision opened")
        out.line("starting state", StatusMark.INFO, "Groups 71-73 produced controlled obstruction, not theorem closure")
        out.line("parent status", StatusMark.DEFER, "parent equation remains blocked")
        out.line("recombination", StatusMark.DEFER, "parent recombination remains blocked")
    with out.counterexamples():
        out.line("monolithic closure", StatusMark.FAIL, "cannot close full boundary-lift route while D_layer and lift cleanliness remain open")
        out.line("hard route kill", StatusMark.FAIL, "controlled obstruction is not no-go theorem")
        out.line("active O jump", StatusMark.FAIL, "active O is not forced by unresolved O-free subtargets")
        out.line("parent construction", StatusMark.FAIL, "do not write parent equation during route decision")
    with out.unresolved_obligations():
        out.line("route ledger", StatusMark.OBLIGATION, "inventory retained, deferred, blocked, and rejected routes")
        out.line("split decision", StatusMark.OBLIGATION, "decide whether to split theorem targets")

    record_marker(ns, MARKER_ID, "Group 74 opening; route management only")
    record_claim(ns, MARKER_ID, "g74_problem_c1", GovernanceStatus.POLICY_RULE, "Group 74 opens a route-management decision after controlled obstruction.")
    record_claim(ns, MARKER_ID, "g74_problem_c2", GovernanceStatus.REJECTED_ROUTE, "Parent construction, active-O jump, monolithic closure, and hard route kill are not licensed here.")
    record_obligation(ns, "g74_problem_o1", "Classify boundary-lift route status after Groups 71-73.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_route_status_ledger.py")

if __name__ == "__main__":
    main()
