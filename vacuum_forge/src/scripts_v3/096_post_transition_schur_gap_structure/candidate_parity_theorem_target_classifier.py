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
    ("g96_parity_sequences", "96_post_transition_schur_gap_structure__candidate_parity_gap_sequence_probe", "g96_parity_sequences"),
    ("g96_parity_monotonicity", "96_post_transition_schur_gap_structure__candidate_parity_monotonicity_test", "g96_parity_monotonicity"),
    ("g96_gap_interlacing", "96_post_transition_schur_gap_structure__candidate_gap_interlacing_test", "g96_gap_interlacing"),
]
MARKER_ID = "g96_classifier"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    classifications = [
        ("POST_TRANSITION_GAP_POSITIVE_N11_TO_N30", "stable", "gap positive and ratio in (0,1) through N=30"),
        ("PARITY_BRANCHES_ISOLATED", "stable", "odd/even post-transition sequences separated"),
        ("PARITY_MONOTONICITY_TESTED_N11_TO_N30", "stable", "within-branch monotonicity tested exactly"),
        ("GAP_INTERLACING_TESTED_N11_TO_N30", "stable", "zig-zag/interlacing tested exactly"),
        ("SIMPLE_ONE_STEP_MONOTONICITY_BLOCKED", "stable", "Group 95 one-step monotonicity failures preserved"),
        ("ALL_ORDER_PARITY_GAP_THEOREM_OPEN", "stable", "finite parity evidence is not theorem"),
        ("ALL_ORDER_RATIO_BOUND_THEOREM_OPEN", "stable", "ratio bound remains open"),
        ("ALL_ORDER_SCHUR_POSITIVITY_THEOREM_OPEN", "stable", "Schur positivity remains open"),
        ("ALL_ORDER_DETERMINANT_NONZERO_OPEN", "stable", "determinant nonzero remains open"),
        ("PARENT_DIVERGENCE_UNPROVEN", "stable", "parent identity remains blocked"),
        ("RECOMBINATION_BLOCKED", "stable", "no recombination license"),
    ]

    header("Candidate Parity Theorem Target Classifier")
    for name, status, reason in classifications:
        print(f"{name}: {status}; {reason}")

    with out.governance_assessments():
        out.line("gap positivity", StatusMark.PASS, "extended through N=30")
        out.line("parity structure", StatusMark.PASS, "tested and classified")
        out.line("all-order parity theorem", StatusMark.OBLIGATION, "not proven")
        out.line("ratio theorem", StatusMark.OBLIGATION, "not proven")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "recombination remains blocked")
    with out.counterexamples():
        out.line("finite parity evidence as theorem", StatusMark.FAIL, "N=30 is finite")
        out.line("parent equation", StatusMark.FAIL, "parent construction remains forbidden")
    with out.unresolved_obligations():
        out.line("parity theorem", StatusMark.OBLIGATION, "prove or reject parity-split gap structure all-order")
        out.line("post-transition signs", StatusMark.OBLIGATION, "prove alpha/correction/gap positivity post-transition")
        out.line("structural proof", StatusMark.OBLIGATION, "connect gap behavior to matrix/Hankel structure")

    record_marker(ns, MARKER_ID, "parity gap theorem target classifier")
    record_claim(ns, MARKER_ID, "g96_class_c1", GovernanceStatus.POLICY_RULE, "Group 96 isolates and tests post-transition parity gap structure.")
    record_claim(ns, MARKER_ID, "g96_class_c2", GovernanceStatus.POLICY_RULE, "All-order parity gap theorem remains open.")
    record_obligation(ns, "g96_class_o1", "Attempt parity gap theorem or post-transition sign theorem next.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_group_96_status_summary.py")

if __name__ == "__main__":
    main()
