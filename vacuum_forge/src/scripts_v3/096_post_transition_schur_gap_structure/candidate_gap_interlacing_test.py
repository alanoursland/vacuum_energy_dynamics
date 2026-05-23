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

def row_epsilon(k: int):
    return sp.Integer(1 if k <= 10 else -1)

def row_signed_matrix(N: int):
    A = hierarchy_matrix(N)
    B = sp.zeros(N, N)
    for k in range(1, N + 1):
        eps = row_epsilon(k)
        for j in range(1, N + 1):
            B[k-1, j-1] = eps * A[k-1, j-1]
    return B

def schur_components(N: int):
    B = row_signed_matrix(N)
    detB = sp.factor(B.det(method="bareiss"))
    if N == 1:
        alpha = B[0, 0]
        correction = sp.Integer(0)
        schur = sp.factor(alpha)
        previous_det = sp.Integer(1)
    else:
        C = B[:N-1, :N-1]
        u = B[:N-1, N-1]
        v_row = B[N-1, :N-1]
        alpha = B[N-1, N-1]
        x = C.LUsolve(u)
        correction = sp.factor((v_row * x)[0])
        schur = sp.factor(alpha - correction)
        previous_det = sp.factor(C.det(method="bareiss"))
    pivot = sp.factor(detB / previous_det)
    ratio = None if alpha == 0 else sp.factor(correction / alpha)
    gap = None if alpha == 0 else sp.factor(schur / alpha)
    return {
        "N": N,
        "alpha": sp.factor(alpha),
        "correction": sp.factor(correction),
        "schur": sp.factor(schur),
        "pivot": sp.factor(pivot),
        "ratio": ratio,
        "gap": gap,
        "alpha_sign": sp.sign(alpha),
        "correction_sign": sp.sign(correction),
        "schur_sign": sp.sign(schur),
        "ratio_sign": None if ratio is None else sp.sign(ratio),
        "gap_sign": None if gap is None else sp.sign(gap),
    }

def post_rows(start=11, stop=30):
    return [schur_components(N) for N in range(start, stop + 1)]

def branch(rows, parity):
    return [row for row in rows if row["N"] % 2 == parity]

def increasing(values):
    failures = []
    for a, b in zip(values, values[1:]):
        if not (b[1] > a[1]):
            failures.append((a[0], b[0], sp.factor(b[1] - a[1])))
    return failures

def decreasing(values):
    failures = []
    for a, b in zip(values, values[1:]):
        if not (b[1] < a[1]):
            failures.append((a[0], b[0], sp.factor(b[1] - a[1])))
    return failures

DEPENDENCIES = [
    ("g96_parity_monotonicity", "096_post_transition_schur_gap_structure__candidate_parity_monotonicity_test", "g96_parity_monotonicity"),
]
MARKER_ID = "g96_gap_interlacing"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    rows = post_rows(11, 30)
    by_n = {r["N"]: r for r in rows}

    # Test zig-zag pattern suggested by Group 95:
    # odd -> even caused gap increase, so gap_even(N+1) > gap_odd(N)
    # even -> next odd should then decrease, so gap_even(N) > gap_odd(N+1)
    odd_to_even_fail = []
    even_to_odd_fail = []
    for N in range(11, 30):
        if N % 2 == 1 and N + 1 in by_n:
            if not (by_n[N + 1]["gap"] > by_n[N]["gap"]):
                odd_to_even_fail.append((N, N+1, sp.factor(by_n[N + 1]["gap"] - by_n[N]["gap"])))
        if N % 2 == 0 and N + 1 in by_n:
            if not (by_n[N]["gap"] > by_n[N + 1]["gap"]):
                even_to_odd_fail.append((N, N+1, sp.factor(by_n[N]["gap"] - by_n[N + 1]["gap"])))

    # Stronger nested interlacing: odd_N < even_(N+1) and odd_(N+2) < even_(N+1)
    bracket_fail = []
    for odd_n in range(11, 29, 2):
        even_n = odd_n + 1
        next_odd = odd_n + 2
        if next_odd in by_n:
            even_gap = by_n[even_n]["gap"]
            if not (even_gap > by_n[odd_n]["gap"] and even_gap > by_n[next_odd]["gap"]):
                bracket_fail.append((odd_n, even_n, next_odd))

    header("Candidate Gap Interlacing Test")
    print("Test zig-zag/interlacing structure for gap_N.")
    print(f"odd->even increase failures: {odd_to_even_fail}")
    print(f"even->odd decrease failures: {even_to_odd_fail}")
    print(f"even peak bracket failures: {bracket_fail}")

    interlace_pass = not (odd_to_even_fail or even_to_odd_fail or bracket_fail)

    with out.derived_results():
        out.line("odd->even increase failures", StatusMark.PASS if not odd_to_even_fail else StatusMark.WARN, str(odd_to_even_fail))
        out.line("even->odd decrease failures", StatusMark.PASS if not even_to_odd_fail else StatusMark.WARN, str(even_to_odd_fail))
        out.line("even peak bracket failures", StatusMark.PASS if not bracket_fail else StatusMark.WARN, str(bracket_fail))
    with out.governance_assessments():
        out.line("gap interlacing", StatusMark.PASS if interlace_pass else StatusMark.WARN, "supported through N=30" if interlace_pass else "not cleanly established")
        out.line("structure target", StatusMark.INFO, "interlacing may explain one-step monotonicity failures")
    with out.counterexamples():
        out.line("interlacing theorem", StatusMark.FAIL, "finite evidence only")
        out.line("gap positivity follows from interlacing alone", StatusMark.FAIL, "interlacing needs base positivity and branch behavior")

    record_marker(ns, MARKER_ID, "post-transition gap interlacing test")
    if interlace_pass:
        record_claim(ns, MARKER_ID, "g96_interlace_c1", GovernanceStatus.POLICY_RULE, "Gap interlacing/zig-zag structure is supported through N=30.")
    else:
        record_claim(ns, MARKER_ID, "g96_interlace_c1", GovernanceStatus.POLICY_RULE, "Simple gap interlacing is not cleanly established through N=30.")
    record_obligation(ns, "g96_interlace_o1", "Classify parity gap theorem target.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_parity_theorem_target_classifier.py")

if __name__ == "__main__":
    main()
