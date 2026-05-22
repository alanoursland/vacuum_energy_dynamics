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

def beta_moment(s):
    """Exact B(s+1/2, 5) for integer or rational s.

    Using B(x,5)=24/[x(x+1)(x+2)(x+3)(x+4)] avoids slow symbolic
    beta/gamma simplification. For x=s+1/2 this is:
      768 / Π_{m=0}^4 (2s + 2m + 1).
    """
    s = sp.Rational(s) if isinstance(s, int) else sp.sympify(s)
    denom = sp.prod(2*s + 2*m + 1 for m in range(5))
    return sp.Rational(768, 1) / denom

def hierarchy_matrix(N: int):
    A = sp.zeros(N, N)
    b = sp.zeros(N, 1)
    for k in range(1, N + 1):
        r = sp.Rational(2*k - 1, 2*k + 3)
        for j in range(1, N + 1):
            A[k-1, j-1] = beta_moment(k+j) - r*beta_moment(k+j-1)
        b[k-1, 0] = r*beta_moment(k-1) - beta_moment(k)
    return A, b

def beta_formula_coefficients(N: int):
    A, b = hierarchy_matrix(N)
    sol_vec = A.LUsolve(b)
    return [sp.factor(sol_vec[i, 0]) for i in range(N)]

def moment_value(k: int, coeffs):
    """Return M_(2k) from the Beta moment identity for P=1+Σ a_j t^j."""
    all_coeffs = [sp.Integer(1)] + list(coeffs)
    def I(index: int):
        return sum(all_coeffs[j] * beta_moment(index + j) for j in range(len(all_coeffs)))
    return sp.factor(2*k * ((2*k - 1)*I(k-1) - (2*k + 3)*I(k)))

def rho_at_zero(coeffs):
    """rho(0) for Xi=(1-y^2)^3 P(y^2), J=(1-y^2)^2 Xi'."""
    a1 = coeffs[0] if coeffs else sp.Integer(0)
    return sp.factor(2*(a1 - 3))

def profile_from_coeffs(coeffs):
    t = sp.symbols("t")
    return sp.expand(1 + sum(coeffs[j-1] * t**j for j in range(1, len(coeffs)+1)))

DEPENDENCIES = [
    ("g87_summary", "87_moment_hierarchy_closure_test__candidate_group_87_status_summary", "g87_summary"),
    ("g88_problem", "88_hierarchy_formula_derivation__candidate_hierarchy_formula_problem", "g88_problem"),
    ("g88_moment_ratio", "88_hierarchy_formula_derivation__candidate_moment_ratio_identity", "g88_moment_ratio"),
    ("g88_beta_system", "88_hierarchy_formula_derivation__candidate_beta_linear_system_formula", "g88_beta_system"),
    ("g88_cramer", "88_hierarchy_formula_derivation__candidate_cramer_coefficient_formula", "g88_cramer"),
    ("g88_validation", "88_hierarchy_formula_derivation__candidate_formula_validation_N1_to_N6", "g88_validation"),
    ("g88_next_sequence", "88_hierarchy_formula_derivation__candidate_next_obstruction_sequence", "g88_next_sequence"),
    ("g88_route_classifier", "88_hierarchy_formula_derivation__candidate_hierarchy_formula_route_classifier", "g88_route_classifier"),
]
MARKER_ID = "g88_summary"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Group 88 Status Summary")
    print("Question: Can the finite hierarchy be generated by a general formula?")
    print("Group 88 stable result:")
    print("  integration-by-parts moment-ratio identity derived")
    print("  M2k=0 equivalent to I_k=((2k-1)/(2k+3))I_(k-1)")
    print("  Beta-function linear system A_N a=b_N derived")
    print("  Cramer determinant formula for finite coefficients derived")
    print("  formula validated for N=1..6")
    print("  formula extends Group 87 beyond N=4 to N=5,N=6")
    print("  next obstruction moments remain nonzero through N=6")
    print("  local rho remains nonzero")
    print("  all-order determinant nonzero remains open")
    print("  all-order limit/convergence remains open")
    print("  physical/covariant origin remains open")
    print("  parent divergence identity remains unproven")
    print("  recombination remains blocked")

    with out.governance_assessments():
        out.line("formula derivation", StatusMark.PASS, "finite-N coefficient generator derived")
        out.line("validation", StatusMark.PASS, "N=1..6")
        out.line("next obstruction", StatusMark.WARN, "next moments remain")
        out.line("all-order determinant", StatusMark.OBLIGATION, "not proven")
        out.line("all-order limit", StatusMark.OBLIGATION, "not proven")
        out.line("local rho", StatusMark.WARN, "rho remains nonzero")
        out.line("physical/covariant origin", StatusMark.OBLIGATION, "open")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "recombination remains blocked")
    with out.counterexamples():
        out.line("examples without formula", StatusMark.FAIL, "Beta/Cramer generator derived")
        out.line("formula as closure", StatusMark.FAIL, "all-order determinant and limit remain open")
        out.line("rho inertness", StatusMark.FAIL, "local rho and next moments remain")
        out.line("parent equation", StatusMark.FAIL, "parent construction remains forbidden")
    with out.unresolved_obligations():
        out.line("determinant theorem", StatusMark.OBLIGATION, "prove det(A_N) nonzero for all N")
        out.line("recurrence", StatusMark.OBLIGATION, "derive coefficient recurrence or orthogonal-polynomial form")
        out.line("limit", StatusMark.OBLIGATION, "test all-order convergence/closure")

    print("\nRecommended next routes:")
    print("  89_all_order_determinant_test")
    print("  89_hierarchy_recurrence_search")
    print("  89_all_order_limit_obstruction")
    print("  89_covariant_payload_suppression_lift")
    print("  89_parent_blocker_refresh")

    record_marker(ns, MARKER_ID, "Group 88 summary; hierarchy formula derivation")
    record_claim(ns, MARKER_ID, "g88_summary_c1", GovernanceStatus.POLICY_RULE, "Group 88 derives a finite-N Beta/Cramer coefficient formula for the moment hierarchy.")
    record_claim(ns, MARKER_ID, "g88_summary_c2", GovernanceStatus.POLICY_RULE, "All-order determinant, recurrence/limit, local inertness, and covariant origin remain open.")
    record_obligation(ns, "g88_summary_o1", "Prove determinant nonzero or derive recurrence/limit next.")
    record_obligation(ns, "g88_summary_o2", "Parent divergence identity remains unproven.")
    ns.write_run_metadata()

if __name__ == "__main__":
    main()
