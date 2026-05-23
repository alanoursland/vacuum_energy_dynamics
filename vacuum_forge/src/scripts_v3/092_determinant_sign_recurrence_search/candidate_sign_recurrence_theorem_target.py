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
    ("g92_pivot_reduction", "92_determinant_sign_recurrence_search__candidate_pivot_sign_reduction", "g92_pivot_reduction"),
    ("g92_normalized_pivots", "92_determinant_sign_recurrence_search__candidate_sign_normalized_pivot_sequence", "g92_normalized_pivots"),
    ("g92_recurrence_search", "92_determinant_sign_recurrence_search__candidate_low_degree_rational_recurrence_search", "g92_recurrence_search"),
    ("g92_recurrence_holdout", "92_determinant_sign_recurrence_search__candidate_recurrence_candidate_holdout_test", "g92_recurrence_holdout"),
]
MARKER_ID = "g92_theorem_target"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    classifications = [
        ("PIVOT_SIGN_REDUCTION_DERIVED", "stable", "determinant sign is product of pivot signs"),
        ("SIGN_NORMALIZED_PIVOTS_POSITIVE_N1_TO_N30", "stable", "pi_N positive through N=30"),
        ("LOW_DEGREE_RATIONAL_RECURRENCE_SEARCH_COMPLETED", "stable", "degree<=4 normalized-pivot ratio search performed"),
        ("LOW_DEGREE_RATIONAL_RECURRENCE_NOT_ESTABLISHED", "stable", "no recurrence theorem closed by bounded search"),
        ("ALL_ORDER_PIVOT_SIGN_THEOREM_OPEN", "stable", "prove pi_N>0 for all N"),
        ("ALL_ORDER_NONZERO_THEOREM_OPEN", "stable", "prove det(A_N)!=0 for all N"),
        ("SIGN_PATTERN_THEOREM_OPEN", "stable", "finite sign pattern not all-order theorem"),
        ("PARENT_DIVERGENCE_UNPROVEN", "stable", "parent identity remains blocked"),
        ("RECOMBINATION_BLOCKED", "stable", "no recombination license"),
    ]

    header("Candidate Sign Recurrence Theorem Target")
    for name, status, reason in classifications:
        print(f"{name}: {status}; {reason}")

    with out.governance_assessments():
        out.line("pivot reduction", StatusMark.PASS, "derived")
        out.line("normalized pivots", StatusMark.PASS, "positive through N=30")
        out.line("low-degree recurrence", StatusMark.WARN, "not established as theorem")
        out.line("pivot sign theorem", StatusMark.OBLIGATION, "open")
        out.line("nonzero determinant", StatusMark.OBLIGATION, "open")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "recombination remains blocked")
    with out.counterexamples():
        out.line("revived positivity", StatusMark.FAIL, "raw determinant positivity remains false")
        out.line("finite recurrence as theorem", StatusMark.FAIL, "bounded recurrence search cannot prove all-order")
        out.line("parent equation", StatusMark.FAIL, "parent construction remains forbidden")
    with out.unresolved_obligations():
        out.line("pivot theorem", StatusMark.OBLIGATION, "prove sign-normalized pivots positive for all N")
        out.line("structural recurrence", StatusMark.OBLIGATION, "derive pivot recurrence from determinant/Hankel structure")
        out.line("biorthogonal route", StatusMark.OBLIGATION, "try biorthogonal pivot construction if recurrence search stalls")

    record_marker(ns, MARKER_ID, "sign recurrence theorem target")
    record_claim(ns, MARKER_ID, "g92_target_c1", GovernanceStatus.POLICY_RULE, "Determinant sign theorem reduces to sign-normalized pivot positivity.")
    record_claim(ns, MARKER_ID, "g92_target_c2", GovernanceStatus.POLICY_RULE, "No all-order recurrence theorem is established by the bounded search.")
    record_obligation(ns, "g92_target_o1", "Attempt structural pivot sign theorem next.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_group_92_status_summary.py")

if __name__ == "__main__":
    main()
