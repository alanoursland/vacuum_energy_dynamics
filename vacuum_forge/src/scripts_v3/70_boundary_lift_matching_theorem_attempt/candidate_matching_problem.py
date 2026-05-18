
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
    ("g69_summary", "69_boundary_covariant_cancellation_attempt__candidate_group_69_status_summary", "g69_summary"),
]
MARKER_ID = "g70_problem"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Boundary-Lift Matching Problem")
    print("Question:")
    print("  Can L_boundary = -(D_jump + D_layer + D_tail) be derived from common geometry?")
    with out.governance_assessments():
        out.line("Group 70 opened", StatusMark.PASS, "boundary-lift matching theorem attempt opened")
        out.line("parent status", StatusMark.DEFER, "parent equation remains blocked")
        out.line("transition status", StatusMark.PASS, "diagnostic transition remains non-insertable")
    with out.counterexamples():
        out.line("chosen matching", StatusMark.FAIL, "choosing L_boundary to cancel boundary sum is repair-like")
        out.line("parent construction", StatusMark.FAIL, "do not write parent equation during theorem attempt")
        out.line("active O escape", StatusMark.FAIL, "active O remains unconstructed")

    record_marker(ns, MARKER_ID, "Group 70 opening; no parent equation")
    record_claim(ns, MARKER_ID, "g70_problem_c1", GovernanceStatus.UNVERIFIED, "Group 70 opens the boundary-lift matching theorem attempt.")
    record_obligation(ns, "g70_problem_o1", "Attempt to derive common-generator anti-match relation.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_common_generator_ansatz.py")

if __name__ == "__main__":
    main()
