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
    b = sp.zeros(N, 1)
    for k in range(1, N + 1):
        r = sp.Rational(2*k - 1, 2*k + 3)
        for j in range(1, N + 1):
            A[k-1, j-1] = beta_moment(k+j) - r*beta_moment(k+j-1)
        b[k-1, 0] = r*beta_moment(k-1) - beta_moment(k)
    return A, b

def det_sequence(max_n: int):
    rows = []
    prev = sp.Integer(1)
    for N in range(1, max_n + 1):
        A, _ = hierarchy_matrix(N)
        detA = sp.factor(A.det(method="bareiss"))
        pivot = sp.factor(detA / prev)
        rows.append((N, detA, sp.sign(detA), pivot, sp.sign(pivot)))
        prev = detA
    return rows

def expected_det_sign(N: int):
    if N <= 10:
        return sp.Integer(1)
    return sp.Integer(-1 if N % 2 else 1)

def expected_pivot_sign(N: int):
    if N <= 10:
        return sp.Integer(1)
    return sp.Integer(-1)

DEPENDENCIES = [
    ("g90_pivot_extension", "090_determinant_positivity_theorem_attempt__candidate_pivot_evidence_extension_N1_to_N12", "g90_pivot_extension"),
    ("g91_problem", "091_determinant_sign_pattern_and_nonzero_audit__candidate_sign_pattern_problem", "g91_problem"),
    ("g91_n11_counterexample", "091_determinant_sign_pattern_and_nonzero_audit__candidate_n11_counterexample_verification", "g91_n11_counterexample"),
    ("g91_sign_sequence", "091_determinant_sign_pattern_and_nonzero_audit__candidate_determinant_sign_sequence_N1_to_N30", "g91_sign_sequence"),
    ("g91_sign_normalization", "091_determinant_sign_pattern_and_nonzero_audit__candidate_sign_normalization_hypothesis_test", "g91_sign_normalization"),
    ("g91_post_signflip_invertibility", "091_determinant_sign_pattern_and_nonzero_audit__candidate_post_signflip_invertibility_validation", "g91_post_signflip_invertibility"),
    ("g91_retarget", "091_determinant_sign_pattern_and_nonzero_audit__candidate_nonzero_theorem_retarget", "g91_retarget"),
]
MARKER_ID = "g91_summary"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Group 91 Status Summary")
    print("Question: after positivity fails, what determinant theorem remains?")
    print("Group 91 stable result:")
    print("  N=11 determinant positivity counterexample verified")
    print("  determinant positivity theorem disproven")
    print("  pivot positivity theorem disproven")
    print("  determinant nonzero verified through N=30")
    print("  sign pattern supported through N=30:")
    print("    positive determinant for N=1..10")
    print("    sign(det(A_N))=(-1)^N for N=11..30")
    print("    pivot sign negative for N=11..30")
    print("  sign-normalized determinant positive through N=30")
    print("  N=11 and N=12 profile generation survives sign flip")
    print("  nonzero/invertibility theorem remains open")
    print("  determinant sign-pattern theorem remains open")
    print("  parent divergence identity remains unproven")
    print("  recombination remains blocked")

    with out.governance_assessments():
        out.line("positivity", StatusMark.FAIL, "disproven by N=11")
        out.line("nonzero evidence", StatusMark.PASS, "verified through N=30")
        out.line("sign pattern", StatusMark.PASS, "supported through N=30")
        out.line("profile generation", StatusMark.PASS, "survives sign flip")
        out.line("all-order nonzero", StatusMark.OBLIGATION, "not proven")
        out.line("all-order sign pattern", StatusMark.OBLIGATION, "not proven")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "recombination remains blocked")
    with out.counterexamples():
        out.line("carry positivity forward", StatusMark.FAIL, "N=11 counterexample forbids it")
        out.line("negative determinant as singular", StatusMark.FAIL, "negative determinant is not singular")
        out.line("finite audit as theorem", StatusMark.FAIL, "N=30 is finite")
        out.line("parent equation", StatusMark.FAIL, "parent construction remains forbidden")
    with out.unresolved_obligations():
        out.line("sign recurrence", StatusMark.OBLIGATION, "derive determinant/pivot sign recurrence")
        out.line("nonzero theorem", StatusMark.OBLIGATION, "prove det(A_N)!=0 for all N")
        out.line("all-order limit", StatusMark.OBLIGATION, "study hierarchy limit/convergence")

    print("\nRecommended next routes:")
    print("  92_determinant_sign_recurrence_search")
    print("  92_nonzero_invertibility_theorem_attempt")
    print("  92_biorthogonal_polynomial_construction")
    print("  92_all_order_limit_obstruction")
    print("  92_covariant_payload_suppression_lift")

    record_marker(ns, MARKER_ID, "Group 91 summary; determinant sign-pattern and nonzero retarget")
    record_claim(ns, MARKER_ID, "g91_summary_c1", GovernanceStatus.POLICY_RULE, "Group 91 verifies the N=11 positivity counterexample and retargets determinant work to nonzero/sign-pattern.")
    record_claim(ns, MARKER_ID, "g91_summary_c2", GovernanceStatus.POLICY_RULE, "det(A_N) nonzero and the corrected sign pattern are supported through N=30, but not proven all-order.")
    record_obligation(ns, "g91_summary_o1", "Derive determinant sign recurrence or all-order nonzero theorem next.")
    record_obligation(ns, "g91_summary_o2", "Parent divergence identity remains unproven.")
    ns.write_run_metadata()

if __name__ == "__main__":
    main()
