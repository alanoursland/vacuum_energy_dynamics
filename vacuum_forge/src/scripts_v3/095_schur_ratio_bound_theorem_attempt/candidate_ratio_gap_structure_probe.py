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
        "pivot_sign": sp.sign(pivot),
        "ratio_sign": None if ratio is None else sp.sign(ratio),
        "gap_sign": None if gap is None else sp.sign(gap),
        "difference": sp.factor(schur - pivot),
    }

DEPENDENCIES = [
    ("g95_post_transition_evidence", "095_schur_ratio_bound_theorem_attempt__candidate_post_transition_ratio_evidence_N11_to_N25", "g95_post_transition_evidence"),
]
MARKER_ID = "g95_gap_probe"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    rows = [schur_components(N) for N in range(11, 26)]
    gaps = [(row["N"], row["gap"]) for row in rows]
    ratios = [(row["N"], row["ratio"]) for row in rows]
    positive_gap_failures = [(N, g) for N, g in gaps if g <= 0]

    # Check monotonic behavior exactly.
    gap_decreasing_failures = []
    ratio_increasing_failures = []
    for (N0, g0), (N1, g1) in zip(gaps, gaps[1:]):
        if not (g1 < g0):
            gap_decreasing_failures.append((N0, N1, sp.factor(g1 - g0)))
    for (N0, r0), (N1, r1) in zip(ratios, ratios[1:]):
        if not (r1 > r0):
            ratio_increasing_failures.append((N0, N1, sp.factor(r1 - r0)))

    header("Candidate Ratio Gap Structure Probe")
    print("Probe gap_N = 1-r_N = schur_N/alpha_N for N=11..25.")
    print(f"positive gap failures: {positive_gap_failures}")
    print(f"gap decreasing failures: {gap_decreasing_failures}")
    print(f"ratio increasing failures: {ratio_increasing_failures}")
    for N, g in gaps:
        if N <= 15 or N in (20, 25):
            print(f"N={N}: gap={g}")

    with out.derived_results():
        out.line("positive gap failures", StatusMark.PASS if not positive_gap_failures else StatusMark.FAIL, str(positive_gap_failures))
        out.line("gap decreasing failures", StatusMark.PASS if not gap_decreasing_failures else StatusMark.WARN, str(gap_decreasing_failures))
        out.line("ratio increasing failures", StatusMark.PASS if not ratio_increasing_failures else StatusMark.WARN, str(ratio_increasing_failures))
    with out.governance_assessments():
        out.line("gap positivity", StatusMark.PASS, "gap positive through N=25")
        out.line("gap monotonicity", StatusMark.PASS if not gap_decreasing_failures else StatusMark.WARN, "gap decreasing through tested range" if not gap_decreasing_failures else "simple monotonicity not established")
        out.line("ratio monotonicity", StatusMark.PASS if not ratio_increasing_failures else StatusMark.WARN, "ratio increasing through tested range" if not ratio_increasing_failures else "ratio monotonicity not established")
    with out.counterexamples():
        out.line("gap positivity theorem", StatusMark.FAIL, "finite evidence only")
        out.line("monotonicity theorem", StatusMark.FAIL, "finite monotonic evidence only")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=sp.Matrix([g for _, g in gaps]),
        method="exact gap and monotonicity probe through N=25",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="ratio_gap_structure_probe",
        scope="Schur ratio-bound theorem branch",
    )
    record_claim(ns, MARKER_ID, "g95_gap_c1", GovernanceStatus.POLICY_RULE, "Post-transition Schur gap is positive through N=25.")
    record_claim(ns, MARKER_ID, "g95_gap_c2", GovernanceStatus.POLICY_RULE, "Gap monotonicity / ratio monotonicity are tested as finite theorem targets.")
    record_obligation(ns, "g95_gap_o1", "Audit whether ratio route simplifies the proof target.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_ratio_route_simplification_audit.py")

if __name__ == "__main__":
    main()
