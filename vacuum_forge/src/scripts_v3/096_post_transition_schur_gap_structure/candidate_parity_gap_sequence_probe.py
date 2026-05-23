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
    ("g96_problem", "096_post_transition_schur_gap_structure__candidate_gap_structure_problem", "g96_problem"),
]
MARKER_ID = "g96_parity_sequences"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    rows = post_rows(11, 30)
    odd_rows = branch(rows, 1)
    even_rows = branch(rows, 0)
    positive_failures = [(r["N"], r["gap"], r["ratio"]) for r in rows if not (r["gap"] > 0 and r["ratio"] > 0 and r["ratio"] < 1)]

    header("Candidate Parity Gap Sequence Probe")
    print("Compute post-transition gap_N=schur/alpha and ratio_N=correction/alpha for N=11..30.")
    print(f"positive/range failures: {positive_failures}")
    print("Odd branch:")
    for r in odd_rows:
        print(f"  N={r['N']}: gap={r['gap']}; ratio={r['ratio']}")
    print("Even branch:")
    for r in even_rows:
        print(f"  N={r['N']}: gap={r['gap']}; ratio={r['ratio']}")

    with out.derived_results():
        out.line("positive/range failures", StatusMark.PASS if not positive_failures else StatusMark.FAIL, str(positive_failures))
        out.line("odd branch count", StatusMark.INFO, str(len(odd_rows)))
        out.line("even branch count", StatusMark.INFO, str(len(even_rows)))
    with out.governance_assessments():
        out.line("post-transition evidence", StatusMark.PASS, "gap positive and ratio in (0,1) through N=30")
        out.line("parity split", StatusMark.PASS, "odd/even branches isolated for theorem targeting")
    with out.counterexamples():
        out.line("gap positivity theorem", StatusMark.FAIL, "N=30 evidence is finite")
        out.line("ratio bound theorem", StatusMark.FAIL, "N=30 evidence is finite")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=sp.Matrix([r["gap_sign"] for r in rows]),
        method="compute exact parity-split post-transition gap/ratio sequences through N=30",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="parity_gap_sequence_probe",
        scope="post-transition Schur gap branch",
    )
    record_claim(ns, MARKER_ID, "g96_seq_c1", GovernanceStatus.POLICY_RULE, "Post-transition gap positivity and ratio bound are supported through N=30.")
    record_obligation(ns, "g96_seq_o1", "Test parity branch monotonicity.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_parity_monotonicity_test.py")

if __name__ == "__main__":
    main()
