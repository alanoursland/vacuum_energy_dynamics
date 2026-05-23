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

def q_poly(k, t):
    return t**k - sp.Rational(2*k - 1, 2*k + 3)*t**(k-1)

DEPENDENCIES = [
    ("g90_derivative_factorization", "090_determinant_positivity_theorem_attempt__candidate_derivative_factorization", "g90_derivative_factorization"),
    ("g90_andreief", "090_determinant_positivity_theorem_attempt__candidate_andreief_representation", "g90_andreief"),
    ("g90_chebyshev_sign", "090_determinant_positivity_theorem_attempt__candidate_chebyshev_sign_route_test", "g90_chebyshev_sign"),
    ("g90_hankel_difference", "090_determinant_positivity_theorem_attempt__candidate_hankel_difference_structure", "g90_hankel_difference"),
    ("g90_pivot_extension", "090_determinant_positivity_theorem_attempt__candidate_pivot_evidence_extension_N1_to_N12", "g90_pivot_extension"),
]
MARKER_ID = "g90_route_classifier"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    classifications = [
        ("DERIVATIVE_FACTORIZATION_DERIVED", "stable", "q_k mu has weighted derivative/Sturm-like factorization"),
        ("ANDREIEF_REPRESENTATION_DERIVED", "stable", "det(A_N) has integral determinant representation"),
        ("SIMPLE_CHEBYSHEV_SIGN_ROUTE_BLOCKED", "stable", "q determinant not sign-definite in naive form"),
        ("HANKEL_DIFFERENCE_STRUCTURE_DERIVED", "stable", "A=H1-RH0 derived"),
        ("PIVOT_EVIDENCE_EXTENDED_N1_TO_N12", "stable", "determinants and pivots positive through N=12"),
        ("ALL_ORDER_DETERMINANT_THEOREM_NOT_PROVEN", "stable", "no all-order positivity proof closed"),
        ("PROOF_TARGET_REFINED", "stable", "future proof should use derivative/Hankel/biorthogonal route, not naive Chebyshev route"),
        ("ALL_ORDER_LIMIT_OPEN", "stable", "convergence/local inertness limit remains open"),
        ("PARENT_DIVERGENCE_UNPROVEN", "stable", "parent identity remains blocked"),
        ("RECOMBINATION_BLOCKED", "stable", "no recombination license"),
    ]

    header("Candidate Determinant Positivity Route Classifier")
    for name, status, reason in classifications:
        print(f"{name}: {status}; {reason}")

    with out.governance_assessments():
        out.line("derivative factorization", StatusMark.PASS, "derived")
        out.line("Andreief representation", StatusMark.PASS, "derived")
        out.line("Chebyshev route", StatusMark.WARN, "simple sign route blocked")
        out.line("Hankel difference", StatusMark.PASS, "derived")
        out.line("pivot evidence", StatusMark.PASS, "extended through N=12")
        out.line("all-order theorem", StatusMark.OBLIGATION, "not proven")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "recombination remains blocked")
    with out.counterexamples():
        out.line("all-order determinant proven", StatusMark.FAIL, "no full theorem closed")
        out.line("naive Chebyshev proof", StatusMark.FAIL, "q determinant sign route fails in simple form")
        out.line("finite as infinity", StatusMark.FAIL, "N=12 evidence is still finite")
        out.line("parent equation", StatusMark.FAIL, "parent construction remains forbidden")
    with out.unresolved_obligations():
        out.line("biorthogonal route", StatusMark.OBLIGATION, "construct biorthogonal polynomials or recurrence")
        out.line("Hankel/Christoffel route", StatusMark.OBLIGATION, "turn H1-RH0 into positivity theorem if possible")
        out.line("pivot recurrence", StatusMark.OBLIGATION, "derive all-order pivot formula")

    record_marker(ns, MARKER_ID, "determinant positivity theorem route classifier")
    record_claim(ns, MARKER_ID, "g90_class_c1", GovernanceStatus.POLICY_RULE, "Group 90 refines determinant proof routes but does not prove all-order positivity.")
    record_claim(ns, MARKER_ID, "g90_class_c2", GovernanceStatus.POLICY_RULE, "Simple Chebyshev sign route is blocked; derivative/Hankel/biorthogonal routes remain.")
    record_obligation(ns, "g90_class_o1", "Attempt biorthogonal polynomial construction or pivot recurrence next.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_group_90_status_summary.py")

if __name__ == "__main__":
    main()
