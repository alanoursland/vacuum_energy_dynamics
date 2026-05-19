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
    ("g70_summary", "70_boundary_lift_matching_theorem_attempt__candidate_group_70_status_summary", "g70_summary"),
]
MARKER_ID = "g71_problem"


def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Common Boundary Generator Search Problem")
    print("Question:")
    print("  Is there a common boundary/covariant generator that forces the Group 70 matching package?")
    print()
    print("Imported Group 70 compatibility package:")
    print("  sigma = 1")
    print("  a_jump = a_layer = a_tail = -1")
    print("  L_bulk = 0")
    print("  L_gauge = 0")
    print()
    print("Group 71 target:")
    print("  Separate derived common-generator anti-match from selected cancellation / repair paint.")

    with out.governance_assessments():
        out.line("group opened", StatusMark.PASS, "common boundary generator search opened")
        out.line("starting state", StatusMark.INFO, "Group 70 compatibility known; theorem not proven")
        out.line("parent status", StatusMark.DEFER, "parent equation remains blocked")
        out.line("recombination", StatusMark.DEFER, "parent recombination remains blocked")
    with out.counterexamples():
        out.line("B-with-hat", StatusMark.FAIL, "renaming D_jump + D_layer + D_tail is not a generator")
        out.line("chosen signs", StatusMark.FAIL, "choosing signs or coefficients to cancel is repair-like")
        out.line("diagnostic layer", StatusMark.FAIL, "diagnostic transition remains non-insertable")
        out.line("active O escape", StatusMark.FAIL, "active O remains unconstructed")
    with out.unresolved_obligations():
        out.line("generator criteria", StatusMark.OBLIGATION, "state what a legal common generator must force")
        out.line("candidate family tests", StatusMark.OBLIGATION, "test orientation, components, bulk/gauge leakage, and generator classes")

    record_marker(ns, MARKER_ID, "Group 71 opening; no parent equation")
    record_claim(ns, MARKER_ID, "g71_problem_c1", GovernanceStatus.UNVERIFIED, "Group 71 opens a search for a real common boundary/covariant generator.")
    record_claim(ns, MARKER_ID, "g71_problem_c2", GovernanceStatus.REJECTED_ROUTE, "Renaming the boundary sum, choosing signs, diagnostic layer insertion, and active-O escape are rejected.")
    record_obligation(ns, "g71_problem_o1", "Define legal generator requirements before testing candidate families.")
    record_obligation(ns, "g71_problem_o2", "Preserve compatibility-vs-theorem boundary throughout Group 71.")
    ns.write_run_metadata()

    print("\nPossible next script:")
    print("  candidate_boundary_generator_requirements.py")


if __name__ == "__main__":
    main()
