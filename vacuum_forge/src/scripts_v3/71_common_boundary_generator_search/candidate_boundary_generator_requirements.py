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


def record_claim(ns, derivation_id: str, claim_id: str, status: GovernanceStatus, statement: str) -> None:
    ns.record_claim(
        ClaimRecord(
            claim_id=claim_id,
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=status,
            statement=statement,
            derivation_ids=[derivation_id],
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
    ("g71_problem", "71_common_boundary_generator_search__candidate_generator_search_problem", "g71_problem"),
]
DERIVATION_ID = "g71_requirements"


def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    D_jump, D_layer, D_tail, L_bulk, L_gauge = sp.symbols("D_jump D_layer D_tail L_bulk L_gauge")
    B = sp.simplify(D_jump + D_layer + D_tail)
    D_boundary = B
    L_boundary = -B
    o_free_residual = sp.simplify(D_boundary + L_boundary + L_bulk + L_gauge)

    header("Candidate Boundary Generator Requirements")
    print(f"B = {B}")
    print(f"D_boundary = +B = {D_boundary}")
    print(f"L_boundary = -B = {L_boundary}")
    print(f"O-free residual under ideal boundary anti-match = {o_free_residual}")
    print()
    print("Legal generator criteria:")
    print("  1. supply a boundary object before the signs are chosen")
    print("  2. produce D_boundary and L_boundary as opposite orientations of that object")
    print("  3. account for jump/layer/tail components without diagnostic transition insertion")
    print("  4. leave no uncontrolled repair current, active-O patch, or hidden bulk/gauge leak")

    with out.derived_results():
        out.line("boundary sum", StatusMark.PASS, f"B={B}")
        out.line("ideal anti-match residual", StatusMark.PASS, str(o_free_residual))
    with out.governance_assessments():
        out.line("requirement", StatusMark.INFO, "generator must force signs/cofficients, not merely reproduce them")
        out.line("bulk/gauge", StatusMark.OBLIGATION, "ideal boundary anti-match still leaves L_bulk + L_gauge")
    with out.counterexamples():
        out.line("renamed B", StatusMark.FAIL, "B alone is the boundary sum, not the origin of the sum")
        out.line("repair current", StatusMark.FAIL, "adding a cancellation current after leakage is not a generator")
        out.line("active O", StatusMark.FAIL, "projection-like object is out of scope unless constructed")

    ns.record_derivation(
        derivation_id=DERIVATION_ID,
        inputs=[],
        output=o_free_residual,
        method="state generator anti-match requirements and compute ideal residual",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="generator_requirements",
        scope="requirements and compatibility; not generator theorem",
    )
    record_claim(ns, DERIVATION_ID, "g71_req_c1", GovernanceStatus.POLICY_RULE, "A legal common generator must produce opposite boundary/lift orientations before signs are selected.")
    record_claim(ns, DERIVATION_ID, "g71_req_c2", GovernanceStatus.REJECTED_ROUTE, "Renaming B, adding repair currents, or invoking active O by label is rejected.")
    record_obligation(ns, "g71_req_o1", "Test whether orientation anti-match can be forced rather than selected.")
    record_obligation(ns, "g71_req_o2", "Resolve or preserve L_bulk and L_gauge as lift-cleanliness obligations.")
    ns.write_run_metadata()

    print("\nPossible next script:")
    print("  candidate_orientation_forcing_test.py")


if __name__ == "__main__":
    main()
