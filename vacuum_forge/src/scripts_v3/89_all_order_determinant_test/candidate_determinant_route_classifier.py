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
    s = sp.sympify(s)
    denom = sp.prod(2*s + 2*m + 1 for m in range(5))
    return sp.Rational(768, 1) / denom

def hierarchy_matrix(N: int):
    A = sp.zeros(N, N)
    b = sp.zeros(N, 1)
    for k in range(1, N + 1):
        r = sp.Rational(2*k - 1, 2*k + 3)
        for j in range(1, N + 1):
            A[k-1, j-1] = sp.factor(beta_moment(k+j) - r*beta_moment(k+j-1))
        b[k-1, 0] = sp.factor(r*beta_moment(k-1) - beta_moment(k))
    return A, b

def coefficients_for_N(N: int):
    A, b = hierarchy_matrix(N)
    return [sp.factor(x) for x in A.LUsolve(b)]

def next_moment_for_coeffs(coeffs):
    y = sp.symbols("y")
    N = len(coeffs)
    f = (1 - y**2)**3
    w = (1 - y**2)**2
    P = 1 + sum(coeffs[j-1] * y**(2*j) for j in range(1, N+1))
    rho = sp.factor(sp.diff(w*sp.diff(f*P, y), y))
    next_m = sp.factor(sp.integrate(sp.expand(y**(2*N+2)*rho), (y, -1, 1)))
    rho0 = sp.factor(rho.subs(y, 0))
    return next_m, rho0

DEPENDENCIES = [
    ("g89_entry_formula", "89_all_order_determinant_test__candidate_closed_rational_entry_formula", "g89_entry_formula"),
    ("g89_det_sequence", "89_all_order_determinant_test__candidate_determinant_sequence_N1_to_N10", "g89_det_sequence"),
    ("g89_pivots", "89_all_order_determinant_test__candidate_lu_pivot_nonzero_test", "g89_pivots"),
    ("g89_pairing", "89_all_order_determinant_test__candidate_moment_pairing_factorization", "g89_pairing"),
    ("g89_profile_generation", "89_all_order_determinant_test__candidate_profile_generation_under_invertibility", "g89_profile_generation"),
]
MARKER_ID = "g89_route_classifier"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    classifications = [
        ("CLOSED_RATIONAL_ENTRY_FORMULA_DERIVED", "stable", "A_N entries use exact rational beta formula"),
        ("DETERMINANT_NONZERO_VERIFIED_N1_TO_N10", "stable", "det(A_N)>0 through N=10"),
        ("PIVOTS_NONZERO_VERIFIED_N1_TO_N10", "stable", "leading determinant pivots nonzero through N=10"),
        ("MOMENT_PAIRING_FACTORIZATION_DERIVED", "stable", "A_N=<t^j,q_k>_mu"),
        ("PROFILE_GENERATION_VALIDATED_N1_TO_N10", "stable", "profiles generated and target residuals vanish through N=10"),
        ("NEXT_OBSTRUCTION_PERSISTS_N1_TO_N10", "stable", "next moments/local rho remain"),
        ("ALL_ORDER_DETERMINANT_THEOREM_OPEN", "stable", "finite checks do not prove all N"),
        ("ALL_ORDER_LIMIT_OPEN", "stable", "convergence/local inertness limit not proven"),
        ("PHYSICAL_COVARIANT_ORIGIN_OPEN", "stable", "determinant test remains reduced"),
        ("PARENT_DIVERGENCE_UNPROVEN", "stable", "parent identity remains blocked"),
        ("RECOMBINATION_BLOCKED", "stable", "no recombination license"),
    ]

    header("Candidate Determinant Route Classifier")
    for name, status, reason in classifications:
        print(f"{name}: {status}; {reason}")

    with out.governance_assessments():
        out.line("entry formula", StatusMark.PASS, "derived")
        out.line("determinants", StatusMark.PASS, "nonzero through N=10")
        out.line("pivots", StatusMark.PASS, "nonzero through N=10")
        out.line("pairing", StatusMark.PASS, "moment-pairing factorization derived")
        out.line("profiles", StatusMark.PASS, "validated through N=10")
        out.line("next obstruction", StatusMark.WARN, "persists")
        out.line("all-order determinant", StatusMark.OBLIGATION, "not proven")
        out.line("all-order limit", StatusMark.OBLIGATION, "not proven")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "recombination remains blocked")
    with out.counterexamples():
        out.line("early determinant failure", StatusMark.FAIL, "none found through N=10")
        out.line("finite determinant as theorem", StatusMark.FAIL, "finite checks cannot prove all-order positivity")
        out.line("profile generation as inertness", StatusMark.FAIL, "next obstructions remain")
        out.line("parent equation", StatusMark.FAIL, "parent construction remains forbidden")
    with out.unresolved_obligations():
        out.line("determinant theorem", StatusMark.OBLIGATION, "prove det(A_N) nonzero/positive for all N")
        out.line("subspace nondegeneracy", StatusMark.OBLIGATION, "prove moment-pairing subspace nondegeneracy for all N")
        out.line("recurrence", StatusMark.OBLIGATION, "derive recurrence or orthogonal-polynomial structure")

    record_marker(ns, MARKER_ID, "determinant route classifier")
    record_claim(ns, MARKER_ID, "g89_class_c1", GovernanceStatus.POLICY_RULE, "det(A_N)>0 and profile generation are verified through N=10.")
    record_claim(ns, MARKER_ID, "g89_class_c2", GovernanceStatus.POLICY_RULE, "All-order determinant theorem remains open and is now sharply localized.")
    record_obligation(ns, "g89_class_o1", "Attempt determinant positivity theorem or recurrence next.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_group_89_status_summary.py")

if __name__ == "__main__":
    main()
