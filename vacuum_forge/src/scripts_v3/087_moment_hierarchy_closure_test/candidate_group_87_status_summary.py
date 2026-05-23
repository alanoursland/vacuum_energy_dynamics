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

def hierarchy_solution(N: int):
    y = sp.symbols("y")
    coeffs = sp.symbols("a1:" + str(N + 1))
    f = (1 - y**2)**3
    w = (1 - y**2)**2
    P = 1 + sum(coeffs[k-1] * y**(2*k) for k in range(1, N + 1))
    J = sp.simplify(w * sp.diff(f * P, y))
    rho = sp.factor(sp.diff(J, y))
    constraints = [
        sp.factor(sp.integrate(sp.expand(y**(2*k) * rho), (y, -1, 1)))
        for k in range(1, N + 1)
    ]
    sol = sp.solve([sp.Eq(m, 0) for m in constraints], coeffs, dict=True)
    return y, coeffs, P, J, rho, constraints, sol

DEPENDENCIES = [
    ("g86_summary", "086_shape_origin_geometry_derivation__candidate_group_86_status_summary", "g86_summary"),
    ("g87_problem", "087_moment_hierarchy_closure_test__candidate_moment_hierarchy_problem", "g87_problem"),
    ("g87_operator", "087_moment_hierarchy_closure_test__candidate_general_even_shape_operator", "g87_operator"),
    ("g87_profiles", "087_moment_hierarchy_closure_test__candidate_hierarchy_profiles_N1_to_N4", "g87_profiles"),
    ("g87_rank_uniqueness", "087_moment_hierarchy_closure_test__candidate_constraint_rank_uniqueness_test", "g87_rank_uniqueness"),
    ("g87_weighted_inheritance", "087_moment_hierarchy_closure_test__candidate_weighted_block_inheritance_theorem", "g87_weighted_inheritance"),
    ("g87_next_obstruction", "087_moment_hierarchy_closure_test__candidate_next_moment_obstruction_test", "g87_next_obstruction"),
    ("g87_route_classifier", "087_moment_hierarchy_closure_test__candidate_moment_hierarchy_route_classifier", "g87_route_classifier"),
]
MARKER_ID = "g87_summary"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Group 87 Status Summary")
    print("Question: Is the Group 86 quartic profile part of a systematic hierarchy?")
    print("Group 87 stable result:")
    print("  general even compact-support operator tested")
    print("  odd moments vanish by parity")
    print("  finite moment hierarchy supported for N=1..4")
    print("  unique normalized even profile per order through N=4")
    print("  quadratic-measure weighted block inheritance derived")
    print("  next even moment M(2N+2) remains nonzero in tested cases")
    print("  local rho remains nonzero")
    print("  all-order closure not proven")
    print("  physical/covariant origin remains open")
    print("  parent divergence identity remains unproven")
    print("  recombination remains blocked")

    with out.governance_assessments():
        out.line("hierarchy", StatusMark.PASS, "finite hierarchy supported N=1..4")
        out.line("uniqueness", StatusMark.PASS, "unique profile per order through N=4")
        out.line("weighted inheritance", StatusMark.PASS, "derived for quadratic measure")
        out.line("next obstruction", StatusMark.WARN, "M(2N+2) remains")
        out.line("all-order closure", StatusMark.OBLIGATION, "not proven")
        out.line("local rho", StatusMark.WARN, "rho remains locally nonzero")
        out.line("physical/covariant origin", StatusMark.OBLIGATION, "remains open")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "recombination remains blocked")
    with out.counterexamples():
        out.line("quartic one-off", StatusMark.FAIL, "hierarchy supported through N=4")
        out.line("all-order inertness", StatusMark.FAIL, "finite hierarchy does not prove all-order inertness")
        out.line("pointwise rho zero", StatusMark.FAIL, "rho remains locally nonzero")
        out.line("parent equation", StatusMark.FAIL, "parent construction remains forbidden")
    with out.unresolved_obligations():
        out.line("general recurrence", StatusMark.OBLIGATION, "derive closed formula or recurrence for profiles")
        out.line("all-order limit", StatusMark.OBLIGATION, "test convergence/closure of hierarchy")
        out.line("covariant lift", StatusMark.OBLIGATION, "lift hierarchy into covariant structure")

    print("\nRecommended next routes:")
    print("  88_hierarchy_formula_derivation")
    print("  88_all_order_limit_obstruction")
    print("  88_covariant_payload_suppression_lift")
    print("  88_shape_variational_physical_origin")
    print("  88_parent_blocker_refresh")

    record_marker(ns, MARKER_ID, "Group 87 summary; finite moment hierarchy test")
    record_claim(ns, MARKER_ID, "g87_summary_c1", GovernanceStatus.POLICY_RULE, "Group 87 supports finite moment hierarchy through N=4.")
    record_claim(ns, MARKER_ID, "g87_summary_c2", GovernanceStatus.POLICY_RULE, "The hierarchy is not all-order closure; next moments/local rho/covariant origin remain open.")
    record_obligation(ns, "g87_summary_o1", "Derive general hierarchy formula or all-order limit next.")
    record_obligation(ns, "g87_summary_o2", "Parent divergence identity remains unproven.")
    ns.write_run_metadata()

if __name__ == "__main__":
    main()
