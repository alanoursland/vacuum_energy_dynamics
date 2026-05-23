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
    for k in range(1, N + 1):
        r = sp.Rational(2*k - 1, 2*k + 3)
        for j in range(1, N + 1):
            A[k-1, j-1] = beta_moment(k+j) - r*beta_moment(k+j-1)
    return A

def det_pivot_rows(max_n: int):
    rows = []
    prev = sp.Integer(1)
    for N in range(1, max_n + 1):
        A = hierarchy_matrix(N)
        detA = sp.factor(A.det(method="bareiss"))
        pivot = sp.factor(detA / prev)
        rows.append((N, detA, sp.sign(detA), pivot, sp.sign(pivot)))
        prev = detA
    return rows

def normalized_pivot(N: int, pivot):
    return sp.factor(pivot if N <= 10 else -pivot)

def fit_rational_function(data, deg_num: int, deg_den: int):
    # Fit y = P(n) / Q(n), with Q(0)=1:
    #   P(n)=a0+a1*n+...
    #   Q(n)=1+b1*n+...
    # Use SymPy Integers so deg_den=0 still supports .subs().
    n = sp.Symbol("n")
    a = sp.symbols(f"a0:{deg_num + 1}")
    b = sp.symbols(f"b1:{deg_den + 1}") if deg_den else tuple()
    P = sp.Integer(0) + sum(a[i] * n**i for i in range(deg_num + 1))
    Q = sp.Integer(1) + sum(b[i-1] * n**i for i in range(1, deg_den + 1))
    unknowns = list(a) + list(b)
    if len(data) < len(unknowns):
        return None
    equations = []
    for N, y_value in data[:len(unknowns)]:
        equations.append(sp.Eq(P.subs(n, N) - y_value * Q.subs(n, N), 0))
    sol = sp.solve(equations, unknowns, dict=True, rational=True)
    if not sol:
        return None
    expr = sp.factor((P / Q).subs(sol[0]))
    # Guard against poles on the provided data.
    for N, _ in data:
        if sp.simplify(Q.subs(sol[0]).subs(n, N)) == 0:
            return None
    return expr

DEPENDENCIES = [
    ("g91_summary", "91_determinant_sign_pattern_and_nonzero_audit__candidate_group_91_status_summary", "g91_summary"),
    ("g92_problem", "92_determinant_sign_recurrence_search__candidate_sign_recurrence_problem", "g92_problem"),
    ("g92_pivot_reduction", "92_determinant_sign_recurrence_search__candidate_pivot_sign_reduction", "g92_pivot_reduction"),
    ("g92_normalized_pivots", "92_determinant_sign_recurrence_search__candidate_sign_normalized_pivot_sequence", "g92_normalized_pivots"),
    ("g92_recurrence_search", "92_determinant_sign_recurrence_search__candidate_low_degree_rational_recurrence_search", "g92_recurrence_search"),
    ("g92_recurrence_holdout", "92_determinant_sign_recurrence_search__candidate_recurrence_candidate_holdout_test", "g92_recurrence_holdout"),
    ("g92_theorem_target", "92_determinant_sign_recurrence_search__candidate_sign_recurrence_theorem_target", "g92_theorem_target"),
]
MARKER_ID = "g92_summary"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Group 92 Status Summary")
    print("Question: can the Group 91 sign pattern be explained by pivot recurrence?")
    print("Group 92 stable result:")
    print("  determinant sign pattern reduces to pivot sign pattern")
    print("  sign-normalized pivots pi_N are positive through N=30")
    print("  raw determinant positivity remains false")
    print("  bounded low-degree rational recurrence search completed")
    print("  no all-order recurrence theorem established")
    print("  all-order pivot sign theorem remains open")
    print("  all-order determinant nonzero theorem remains open")
    print("  sign-pattern theorem remains open")
    print("  parent divergence identity remains unproven")
    print("  recombination remains blocked")

    with out.governance_assessments():
        out.line("pivot sign reduction", StatusMark.PASS, "derived")
        out.line("normalized pivots", StatusMark.PASS, "positive through N=30")
        out.line("low-degree recurrence search", StatusMark.WARN, "does not close theorem")
        out.line("all-order pivot theorem", StatusMark.OBLIGATION, "not proven")
        out.line("all-order nonzero", StatusMark.OBLIGATION, "not proven")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "recombination remains blocked")
    with out.counterexamples():
        out.line("raw positivity", StatusMark.FAIL, "determinant positivity was disproven by N=11")
        out.line("finite recurrence as theorem", StatusMark.FAIL, "bounded search cannot prove all-order recurrence")
        out.line("parent equation", StatusMark.FAIL, "parent construction remains forbidden")
    with out.unresolved_obligations():
        out.line("pivot sign theorem", StatusMark.OBLIGATION, "prove pi_N>0 for all N")
        out.line("nonzero theorem", StatusMark.OBLIGATION, "prove det(A_N)!=0 for all N")
        out.line("structural proof", StatusMark.OBLIGATION, "use Hankel/biorthogonal/pivot recurrence route")

    print("\nRecommended next routes:")
    print("  93_pivot_sign_theorem_attempt")
    print("  93_biorthogonal_pivot_construction")
    print("  93_hankel_difference_pivot_analysis")
    print("  93_all_order_limit_obstruction")
    print("  93_covariant_payload_suppression_lift")

    record_marker(ns, MARKER_ID, "Group 92 summary; determinant sign recurrence search")
    record_claim(ns, MARKER_ID, "g92_summary_c1", GovernanceStatus.POLICY_RULE, "Group 92 reduces determinant sign pattern to sign-normalized pivot positivity.")
    record_claim(ns, MARKER_ID, "g92_summary_c2", GovernanceStatus.POLICY_RULE, "Bounded low-degree recurrence search does not close the all-order theorem.")
    record_obligation(ns, "g92_summary_o1", "Attempt structural pivot sign theorem next.")
    record_obligation(ns, "g92_summary_o2", "Parent divergence identity remains unproven.")
    ns.write_run_metadata()

if __name__ == "__main__":
    main()
