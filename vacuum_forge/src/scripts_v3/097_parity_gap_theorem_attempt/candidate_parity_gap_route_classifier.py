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
    ("g97_interlacing_differences", "97_parity_gap_theorem_attempt__candidate_interlacing_difference_signs", "g97_interlacing_differences"),
    ("g97_numerator_probe", "97_parity_gap_theorem_attempt__candidate_difference_numerator_probe", "g97_numerator_probe"),
]
MARKER_ID = "g97_classifier"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    classifications = [
        ("BRANCH_GAP_DIFFERENCES_POSITIVE_TESTED_RANGE", "stable", "gap_N-gap_N+2 positive through N=36"),
        ("BRANCH_RATIO_DIFFERENCES_POSITIVE_TESTED_RANGE", "stable", "ratio_N+2-ratio_N positive through N=36"),
        ("INTERLACING_DIFFERENCES_POSITIVE_TESTED_RANGE", "stable", "even-peak differences positive through N=36"),
        ("DIFFERENCE_NUMERATOR_POSITIVITY_TARGET_IDENTIFIED", "stable", "positive rational numerator/denominator signs probed through N=30"),
        ("SIMPLE_ONE_STEP_MONOTONICITY_BLOCKED", "stable", "unsplit monotonicity remains false target"),
        ("ALL_ORDER_PARITY_GAP_THEOREM_OPEN", "stable", "finite difference evidence is not theorem"),
        ("ALL_ORDER_RATIO_BOUND_THEOREM_OPEN", "stable", "ratio bound remains open"),
        ("ALL_ORDER_SCHUR_POSITIVITY_THEOREM_OPEN", "stable", "Schur positivity remains open"),
        ("ALL_ORDER_DETERMINANT_NONZERO_OPEN", "stable", "determinant nonzero remains open"),
        ("PARENT_DIVERGENCE_UNPROVEN", "stable", "parent identity remains blocked"),
        ("RECOMBINATION_BLOCKED", "stable", "no recombination license"),
    ]

    header("Candidate Parity Gap Route Classifier")
    for name, status, reason in classifications:
        print(f"{name}: {status}; {reason}")

    with out.governance_assessments():
        out.line("branch differences", StatusMark.PASS, "positive in tested range")
        out.line("interlacing differences", StatusMark.PASS, "positive in tested range")
        out.line("numerator target", StatusMark.PASS, "identified")
        out.line("all-order parity theorem", StatusMark.OBLIGATION, "not proven")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "recombination remains blocked")
    with out.counterexamples():
        out.line("finite differences as theorem", StatusMark.FAIL, "finite tests are not all-order proof")
        out.line("parent equation", StatusMark.FAIL, "parent construction remains forbidden")
    with out.unresolved_obligations():
        out.line("difference numerator theorem", StatusMark.OBLIGATION, "factor/prove positivity of exact difference numerators")
        out.line("parity gap theorem", StatusMark.OBLIGATION, "prove branch monotonicity and interlacing all-order")
        out.line("structural proof", StatusMark.OBLIGATION, "connect difference numerators to matrix/Hankel structure")

    record_marker(ns, MARKER_ID, "parity gap route classifier")
    record_claim(ns, MARKER_ID, "g97_class_c1", GovernanceStatus.POLICY_RULE, "Group 97 reduces parity gap structure to exact positive rational difference targets in the tested range.")
    record_claim(ns, MARKER_ID, "g97_class_c2", GovernanceStatus.POLICY_RULE, "All-order parity gap theorem remains open.")
    record_obligation(ns, "g97_class_o1", "Attempt difference numerator factorization/positivity next.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_group_97_status_summary.py")

if __name__ == "__main__":
    main()
