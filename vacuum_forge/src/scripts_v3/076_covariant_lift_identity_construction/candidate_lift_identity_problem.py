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
    ("g75_summary", "75_covariant_lift_neutrality_attempt__candidate_group_75_status_summary", "g75_summary"),
]
MARKER_ID = "g76_problem"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Covariant Lift Identity Problem")
    print("Question:")
    print("  Can a shared lift identity derive L_bulk + L_gauge = 0 without repair cancellation?")
    print()
    print("Imported Group 75 status:")
    print("  independent lift neutrality not derived")
    print("  shared lift identity not derived")
    print("  repair-style mutual cancellation rejected")
    print("  D_layer remains separate")
    print("  parent divergence identity unproven")
    print("  recombination blocked")

    with out.governance_assessments():
        out.line("group opened", StatusMark.PASS, "shared covariant lift-identity construction attempt opened")
        out.line("D_layer separation", StatusMark.INFO, "D_layer remains separate theorem target")
        out.line("parent status", StatusMark.DEFER, "parent equation remains blocked")
        out.line("recombination", StatusMark.DEFER, "parent recombination remains blocked")
    with out.counterexamples():
        out.line("repair cancellation", StatusMark.FAIL, "choosing L_bulk=-L_gauge after leakage appears remains repair-like")
        out.line("drop remainder", StatusMark.FAIL, "rho cannot be dropped by prose")
        out.line("active O escape", StatusMark.FAIL, "active O remains unconstructed and out of scope")
        out.line("parent construction", StatusMark.FAIL, "do not write parent equation during lift-identity attempt")
    with out.unresolved_obligations():
        out.line("identity requirements", StatusMark.OBLIGATION, "state exact-pair and remainder requirements")
        out.line("candidate identity tests", StatusMark.OBLIGATION, "test exact pair, remainder, and gauge-exact routes")

    record_marker(ns, MARKER_ID, "Group 76 opening; no parent equation")
    record_claim(ns, MARKER_ID, "g76_problem_c1", GovernanceStatus.UNVERIFIED, "Group 76 opens shared covariant lift-identity construction attempt.")
    record_obligation(ns, "g76_problem_o1", "State shared lift identity requirements.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_shared_identity_requirements.py")

if __name__ == "__main__":
    main()
