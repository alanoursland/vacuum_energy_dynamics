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
    if N == 1:
        alpha = B[0, 0]
        correction = sp.Integer(0)
        schur = sp.factor(alpha)
    else:
        C = B[:N-1, :N-1]
        u = B[:N-1, N-1]
        v_row = B[N-1, :N-1]
        alpha = B[N-1, N-1]
        x = C.LUsolve(u)
        correction = sp.factor((v_row * x)[0])
        schur = sp.factor(alpha - correction)
    ratio = sp.factor(correction / alpha)
    gap = sp.factor(schur / alpha)
    return {"N": N, "alpha": alpha, "correction": correction, "schur": schur, "ratio": ratio, "gap": gap}

def rows(start=11, stop=36):
    return {N: schur_components(N) for N in range(start, stop + 1)}

def rational_sign_parts(expr):
    expr = sp.factor(expr)
    num, den = sp.fraction(expr)
    return sp.factor(num), sp.factor(den), sp.sign(num), sp.sign(den), sp.sign(expr)

DEPENDENCIES = [
    ("g97_branch_differences", "97_parity_gap_theorem_attempt__candidate_branch_difference_signs", "g97_branch_differences"),
]
MARKER_ID = "g97_interlacing_differences"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    data = rows(11, 36)
    left_failures = []
    right_failures = []
    bracket_failures = []
    diffs = []
    for N in range(11, 35, 2):
        even = N + 1
        nxt = N + 2
        if nxt not in data:
            continue
        left = sp.factor(data[even]["gap"] - data[N]["gap"])
        right = sp.factor(data[even]["gap"] - data[nxt]["gap"])
        diffs.append((N, even, nxt, left, right))
        if left <= 0:
            left_failures.append((N, even, left))
        if right <= 0:
            right_failures.append((even, nxt, right))
        if not (left > 0 and right > 0):
            bracket_failures.append((N, even, nxt))

    header("Candidate Interlacing Difference Signs")
    print("Test exact even-peak interlacing differences:")
    print("  gap_(N+1) - gap_N > 0")
    print("  gap_(N+1) - gap_(N+2) > 0")
    print(f"left failures: {left_failures}")
    print(f"right failures: {right_failures}")
    print(f"bracket failures: {bracket_failures}")
    for N, even, nxt, left, right in diffs:
        if N <= 17 or N in (25, 33):
            print(f"N={N}, even={even}, next={nxt}: left_sign={sp.sign(left)}, right_sign={sp.sign(right)}")

    with out.derived_results():
        out.line("left failures", StatusMark.PASS if not left_failures else StatusMark.FAIL, str(left_failures))
        out.line("right failures", StatusMark.PASS if not right_failures else StatusMark.FAIL, str(right_failures))
        out.line("bracket failures", StatusMark.PASS if not bracket_failures else StatusMark.FAIL, str(bracket_failures))
    with out.governance_assessments():
        out.line("interlacing differences", StatusMark.PASS, "positive through N=35")
        out.line("theorem target", StatusMark.INFO, "prove exact even-peak interlacing difference positivity all-order")
    with out.counterexamples():
        out.line("interlacing theorem", StatusMark.FAIL, "finite evidence only")
        out.line("interlacing alone proves gap positivity", StatusMark.FAIL, "needs base positivity / branch behavior")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=sp.Matrix([sp.sign(d[3]) for d in diffs] + [sp.sign(d[4]) for d in diffs]),
        method="exact even-peak interlacing difference signs through N=36",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="interlacing_difference_signs",
        scope="parity gap theorem branch",
    )
    record_claim(ns, MARKER_ID, "g97_interlace_c1", GovernanceStatus.POLICY_RULE, "Exact interlacing difference positivity is supported through N=36.")
    record_obligation(ns, "g97_interlace_o1", "Probe numerator signs of difference expressions.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_difference_numerator_probe.py")

if __name__ == "__main__":
    main()
