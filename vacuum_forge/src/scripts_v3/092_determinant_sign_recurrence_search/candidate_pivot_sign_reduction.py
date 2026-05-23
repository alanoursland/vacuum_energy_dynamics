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
    ("g92_problem", "092_determinant_sign_recurrence_search__candidate_sign_recurrence_problem", "g92_problem"),
]
MARKER_ID = "g92_pivot_reduction"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    rows = det_pivot_rows(30)
    derived_signs = []
    product_sign = sp.Integer(1)
    failures = []
    for N, detA, det_sign, pivot, pivot_sign in rows:
        product_sign *= pivot_sign
        expected = sp.Integer(1) if N <= 10 else sp.Integer(-1 if N % 2 else 1)
        derived_signs.append((N, product_sign, det_sign, expected))
        if product_sign != det_sign or det_sign != expected:
            failures.append((N, product_sign, det_sign, expected))

    header("Candidate Pivot Sign Reduction")
    print("D_N = det(A_N), p_N = D_N/D_(N-1), D_0=1")
    print("Therefore sign(D_N)=product_{m=1}^N sign(p_m).")
    print("If pivot signs are + through N=10 and - after N=11, then sign(D_N)=+ through N=10 and (-1)^N after.")
    print(f"finite reduction failures through N=30: {failures}")
    for N, product_sign, det_sign, expected in derived_signs:
        print(f"N={N}: product_sign={product_sign}, det_sign={det_sign}, expected={expected}")

    with out.derived_results():
        out.line("reduction failures", StatusMark.PASS if not failures else StatusMark.FAIL, str(failures))
    with out.governance_assessments():
        out.line("pivot-sign reduction", StatusMark.PASS, "determinant sign theorem reduces to pivot sign theorem")
        out.line("theorem target", StatusMark.INFO, "prove p_N positive through 10 and negative thereafter, or equivalent normalized pivot positivity")
    with out.counterexamples():
        out.line("det sign independent of pivots", StatusMark.FAIL, "det sign is product of pivot signs")
        out.line("finite reduction as proof", StatusMark.FAIL, "finite pivot check still not all-order proof")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=sp.Matrix([row[1] for row in derived_signs]),
        method="derive determinant signs as product of pivot signs and verify through N=30",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="pivot_sign_reduction",
        scope="determinant sign recurrence search",
    )
    record_claim(ns, MARKER_ID, "g92_pivot_c1", GovernanceStatus.POLICY_RULE, "The determinant sign pattern reduces to the pivot sign pattern.")
    record_obligation(ns, "g92_pivot_o1", "Compute sign-normalized pivot sequence.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_sign_normalized_pivot_sequence.py")

if __name__ == "__main__":
    main()
