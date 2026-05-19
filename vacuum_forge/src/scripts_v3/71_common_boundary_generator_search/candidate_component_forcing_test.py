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
    ("g70_coefficients", "70_boundary_lift_matching_theorem_attempt__candidate_component_coefficient_matching", "g70_coefficients"),
    ("g71_orientation", "71_common_boundary_generator_search__candidate_orientation_forcing_test", "g71_orientation_forcing"),
]
DERIVATION_ID = "g71_component_forcing"


def residual_for(coeffs):
    D_jump, D_layer, D_tail = sp.symbols("D_jump D_layer D_tail")
    a_jump, a_layer, a_tail = coeffs
    return sp.simplify((a_jump + 1) * D_jump + (a_layer + 1) * D_layer + (a_tail + 1) * D_tail)


def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    D_jump, D_layer, D_tail = sp.symbols("D_jump D_layer D_tail")
    a_jump, a_layer, a_tail = sp.symbols("a_jump a_layer a_tail")
    L_boundary = sp.simplify(a_jump * D_jump + a_layer * D_layer + a_tail * D_tail)
    residual = sp.simplify(L_boundary + D_jump + D_layer + D_tail)
    equations = [
        sp.Eq(sp.diff(residual, D_jump), 0),
        sp.Eq(sp.diff(residual, D_layer), 0),
        sp.Eq(sp.diff(residual, D_tail), 0),
    ]
    solution = sp.solve(equations, [a_jump, a_layer, a_tail], dict=True)

    fixed_common = residual_for((-1, -1, -1))
    missing_layer = residual_for((-1, 0, -1))
    jump_only = residual_for((-1, 0, 0))
    same_sign = residual_for((1, 1, 1))

    header("Candidate Component Forcing Test")
    print(f"L_boundary = {L_boundary}")
    print(f"residual = {residual}")
    print(f"coefficient equations = {equations}")
    print(f"solution = {solution}")
    print()
    print("Candidate component patterns:")
    print(f"  common all-components anti-match residual: {fixed_common}")
    print(f"  missing layer residual: {missing_layer}")
    print(f"  jump-only residual: {jump_only}")
    print(f"  same-sign residual: {same_sign}")

    with out.derived_results():
        out.line("component residual", StatusMark.PASS, str(residual))
        out.line("component solution", StatusMark.PASS, str(solution))
    with out.governance_assessments():
        out.line("all-component route", StatusMark.INFO, "retained only if the generator covers jump/layer/tail as one boundary object")
        out.line("layer burden", StatusMark.OBLIGATION, "a_layer=-1 is dangerous unless D_layer is legitimate and not diagnostic insertion")
    with out.counterexamples():
        out.line("free coefficients", StatusMark.FAIL, "manual coefficient solving is compatibility, not generator theorem")
        out.line("missing layer", StatusMark.FAIL, f"residual={missing_layer}")
        out.line("jump only", StatusMark.FAIL, f"residual={jump_only}")
        out.line("same sign", StatusMark.FAIL, f"residual={same_sign}")
    with out.unresolved_obligations():
        out.line("component theorem", StatusMark.OBLIGATION, "derive a_jump=a_layer=a_tail=-1 from one shared boundary/lift geometry")
        out.line("layer legitimacy", StatusMark.OBLIGATION, "show D_layer is a legitimate boundary component, not old diagnostic transition insertion")

    ns.record_derivation(
        derivation_id=DERIVATION_ID,
        inputs=[],
        output=sp.Tuple(-1, -1, -1),
        method="solve independent component anti-match conditions and test failed component patterns",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="component_forcing_requirement",
        scope="component compatibility; not generator theorem",
    )
    record_claim(ns, DERIVATION_ID, "g71_component_c1", GovernanceStatus.POLICY_RULE, "Component anti-match requires jump, layer, and tail coefficients all equal -1.")
    record_claim(ns, DERIVATION_ID, "g71_component_c2", GovernanceStatus.REJECTED_ROUTE, "Missing-layer, jump-only, same-sign, and free-coefficient routes are rejected as theorem substitutes.")
    record_obligation(ns, "g71_component_o1", "Derive component coefficients from a shared boundary/lift generator.")
    record_obligation(ns, "g71_component_o2", "Audit D_layer legitimacy before treating it as part of any generator.")
    ns.write_run_metadata()

    print("\nPossible next script:")
    print("  candidate_bulk_gauge_leakage_test.py")


if __name__ == "__main__":
    main()
