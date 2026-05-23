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
    ("g92_normalized_pivots", "92_determinant_sign_recurrence_search__candidate_sign_normalized_pivot_sequence", "g92_normalized_pivots"),
]
MARKER_ID = "g92_recurrence_search"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    rows = det_pivot_rows(30)
    pis = {N: normalized_pivot(N, pivot) for N, detA, det_sign, pivot, pivot_sign in rows}
    ratio_data = [(N, sp.factor(pis[N] / pis[N-1])) for N in range(2, 31)]

    found = []
    max_degree = 4
    for deg_num in range(0, max_degree + 1):
        for deg_den in range(0, max_degree + 1):
            needed = deg_num + 1 + deg_den
            if needed > len(ratio_data):
                continue
            candidate = fit_rational_function(ratio_data, deg_num, deg_den)
            if candidate is None:
                continue
            train_end = min(12, len(ratio_data))
            train_ok = all(sp.simplify(candidate.subs(sp.Symbol("n"), N) - y) == 0 for N, y in ratio_data[:train_end])
            holdout_ok = all(sp.simplify(candidate.subs(sp.Symbol("n"), N) - y) == 0 for N, y in ratio_data[train_end:])
            if train_ok and holdout_ok:
                found.append((deg_num, deg_den, candidate))
                break
        if found:
            break

    header("Candidate Low-Degree Rational Recurrence Search")
    print("Search target: pi_N/pi_(N-1) = R(N), R rational with numerator/denominator degrees <= 4.")
    print(f"candidate found: {found}")
    if not found:
        print("No low-degree rational recurrence found under the tested bounds.")

    with out.derived_results():
        out.line("candidate found", StatusMark.PASS if found else StatusMark.WARN, str(found))
    with out.governance_assessments():
        if found:
            out.line("low-degree recurrence", StatusMark.PASS, "candidate passed finite holdout")
        else:
            out.line("low-degree recurrence", StatusMark.WARN, "no degree<=4 rational recurrence found")
        out.line("search scope", StatusMark.INFO, "bounded finite search, not proof of nonexistence")
    with out.counterexamples():
        out.line("assume easy recurrence", StatusMark.FAIL, "bounded search did not justify easy recurrence" if not found else "candidate still finite")
        out.line("finite recurrence fit as theorem", StatusMark.FAIL, "finite fit cannot prove all-order recurrence")

    record_marker(ns, MARKER_ID, "low-degree rational recurrence search for normalized pivot ratios")
    if found:
        record_claim(ns, MARKER_ID, "g92_rec_c1", GovernanceStatus.UNVERIFIED, "A low-degree rational recurrence candidate was found but remains finite-test only.")
    else:
        record_claim(ns, MARKER_ID, "g92_rec_c1", GovernanceStatus.POLICY_RULE, "No degree<=4 rational recurrence for normalized pivot ratios was found in the tested finite search.")
    record_obligation(ns, "g92_rec_o1", "Test recurrence candidate or record obstruction.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_recurrence_candidate_holdout_test.py")

if __name__ == "__main__":
    main()
