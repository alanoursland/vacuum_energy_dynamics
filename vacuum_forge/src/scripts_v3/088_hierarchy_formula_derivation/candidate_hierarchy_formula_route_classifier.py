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
    ("g88_moment_ratio", "088_hierarchy_formula_derivation__candidate_moment_ratio_identity", "g88_moment_ratio"),
    ("g88_beta_system", "088_hierarchy_formula_derivation__candidate_beta_linear_system_formula", "g88_beta_system"),
    ("g88_cramer", "088_hierarchy_formula_derivation__candidate_cramer_coefficient_formula", "g88_cramer"),
    ("g88_validation", "088_hierarchy_formula_derivation__candidate_formula_validation_N1_to_N6", "g88_validation"),
    ("g88_next_sequence", "088_hierarchy_formula_derivation__candidate_next_obstruction_sequence", "g88_next_sequence"),
]
MARKER_ID = "g88_route_classifier"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    classifications = [
        ("MOMENT_RATIO_IDENTITY_DERIVED", "stable", "M2k=0 reduced to I_k=r_k I_(k-1)"),
        ("BETA_LINEAR_SYSTEM_DERIVED", "stable", "finite coefficients generated by A_N a=b_N"),
        ("CRAMER_COEFFICIENT_FORMULA_DERIVED", "stable", "coefficients have determinant formula when det(A_N)!=0"),
        ("FORMULA_VALIDATED_N1_TO_N6", "stable", "formula reproduces direct solves and extends beyond N=4"),
        ("NEXT_OBSTRUCTION_PERSISTS_N1_TO_N6", "stable", "next moments nonzero through N=6"),
        ("FINITE_HIERARCHY_FORMULA_STRENGTHENED", "stable", "finite hierarchy now has generator formula"),
        ("ALL_ORDER_DETERMINANT_NONZERO_OPEN", "stable", "det(A_N) nonzero for all N not proven"),
        ("ALL_ORDER_LIMIT_OPEN", "stable", "no convergence/closure theorem"),
        ("LOCAL_RHO_NONZERO_REMAINS", "stable", "rho(0) nonzero in tested generated profiles"),
        ("PHYSICAL_COVARIANT_ORIGIN_OPEN", "stable", "reduced formula not covariant physics"),
        ("PARENT_DIVERGENCE_UNPROVEN", "stable", "parent identity remains blocked"),
        ("RECOMBINATION_BLOCKED", "stable", "no recombination license"),
    ]

    header("Candidate Hierarchy Formula Route Classifier")
    for name, status, reason in classifications:
        print(f"{name}: {status}; {reason}")

    with out.governance_assessments():
        out.line("moment ratio", StatusMark.PASS, "derived")
        out.line("Beta system", StatusMark.PASS, "derived")
        out.line("Cramer formula", StatusMark.PASS, "derived")
        out.line("validation", StatusMark.PASS, "N=1..6")
        out.line("next obstruction", StatusMark.WARN, "persists")
        out.line("all-order determinant", StatusMark.OBLIGATION, "not proven")
        out.line("all-order limit", StatusMark.OBLIGATION, "not proven")
        out.line("local rho", StatusMark.WARN, "nonzero remains")
        out.line("physical/covariant origin", StatusMark.OBLIGATION, "open")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "recombination remains blocked")
    with out.counterexamples():
        out.line("finite examples only", StatusMark.FAIL, "formula now generates finite profiles")
        out.line("formula as all-order closure", StatusMark.FAIL, "determinant and limit still open")
        out.line("payload inertness", StatusMark.FAIL, "next obstruction/local rho remain")
        out.line("parent equation", StatusMark.FAIL, "parent construction remains forbidden")
    with out.unresolved_obligations():
        out.line("determinant theorem", StatusMark.OBLIGATION, "prove or reject det(A_N) nonzero for all N")
        out.line("limit theorem", StatusMark.OBLIGATION, "test all-order limit/convergence")
        out.line("recurrence", StatusMark.OBLIGATION, "seek coefficient recurrence or closed orthogonal-polynomial form")

    record_marker(ns, MARKER_ID, "hierarchy formula route classifier")
    record_claim(ns, MARKER_ID, "g88_class_c1", GovernanceStatus.POLICY_RULE, "Group 88 derives a finite-N Beta/Cramer formula for hierarchy coefficients.")
    record_claim(ns, MARKER_ID, "g88_class_c2", GovernanceStatus.POLICY_RULE, "All-order determinant, limit, and covariant origin remain open.")
    record_obligation(ns, "g88_class_o1", "Test all-order determinant or derive recurrence/limit next.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_group_88_status_summary.py")

if __name__ == "__main__":
    main()
