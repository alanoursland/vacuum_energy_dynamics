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
    return {
        "N": N,
        "alpha": sp.factor(alpha),
        "correction": sp.factor(correction),
        "schur": sp.factor(schur),
        "pivot": sp.factor(pivot),
        "difference": sp.factor(schur - pivot),
        "alpha_sign": sp.sign(alpha),
        "correction_sign": sp.sign(correction),
        "schur_sign": sp.sign(schur),
        "pivot_sign": sp.sign(pivot),
    }

DEPENDENCIES = [
    ("g93_summary", "093_pivot_sign_theorem_attempt__candidate_group_93_status_summary", "g93_summary"),
    ("g94_problem", "094_schur_complement_positivity_attempt__candidate_schur_repair_problem", "g94_problem"),
    ("g94_schur_identity", "094_schur_complement_positivity_attempt__candidate_schur_identity_repair", "g94_schur_identity"),
    ("g94_schur_balance", "094_schur_complement_positivity_attempt__candidate_schur_term_balance_regimes", "g94_schur_balance"),
    ("g94_schur_ratio", "094_schur_complement_positivity_attempt__candidate_schur_ratio_bound_probe", "g94_schur_ratio"),
    ("g94_classifier", "094_schur_complement_positivity_attempt__candidate_schur_theorem_target_classifier", "g94_classifier"),
]
MARKER_ID = "g94_summary"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Group 94 Status Summary")
    print("Group 94 confirmed the patched Schur complement route and refined its positivity target.")
    print("Stable result:")
    print("  Schur complement pivot identity confirmed through N=15 after the Group 93 patch")
    print("  repaired Schur pivots positive through N=15")
    print("  two-regime alpha/correction balance pattern supported through N=15")
    print("  correction/alpha ratio bound pattern supported through N=15")
    print("  all-order Schur positivity theorem remains open")
    print("  all-order determinant nonzero theorem remains open")
    print("  parent divergence identity remains unproven")
    print("  recombination remains blocked")

    with out.governance_assessments():
        out.line("Schur confirmation", StatusMark.PASS, "completed")
        out.line("Schur positivity", StatusMark.PASS, "finite evidence through N=15")
        out.line("two-regime balance", StatusMark.PASS, "finite pattern identified")
        out.line("ratio theorem", StatusMark.OBLIGATION, "all-order proof open")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "recombination remains blocked")
    with out.counterexamples():
        out.line("Schur identity still failed", StatusMark.FAIL, "patched in Group 93 and confirmed in Group 94")
        out.line("finite evidence as theorem", StatusMark.FAIL, "N=15 is finite")
        out.line("parent equation", StatusMark.FAIL, "parent construction remains forbidden")
    with out.unresolved_obligations():
        out.line("Schur ratio bound", StatusMark.OBLIGATION, "prove two-regime ratio bound")
        out.line("Schur positivity", StatusMark.OBLIGATION, "prove all row-signed leading Schur complements positive")
        out.line("determinant nonzero", StatusMark.OBLIGATION, "prove det(A_N)!=0 for all N")

    print("\nRecommended next routes:")
    print("  95_schur_ratio_bound_theorem_attempt")
    print("  95_biorthogonal_pivot_construction")
    print("  95_hankel_difference_pivot_analysis")
    print("  95_all_order_limit_obstruction")
    print("  95_covariant_payload_suppression_lift")

    record_marker(ns, MARKER_ID, "Group 94 summary; Schur complement repair and positivity attempt")
    record_claim(ns, MARKER_ID, "g94_summary_c1", GovernanceStatus.POLICY_RULE, "Group 94 confirms the patched Schur complement identity and identifies a two-regime ratio-bound theorem target.")
    record_claim(ns, MARKER_ID, "g94_summary_c2", GovernanceStatus.POLICY_RULE, "All-order Schur positivity and determinant nonzero remain open.")
    record_obligation(ns, "g94_summary_o1", "Attempt Schur ratio bound theorem next.")
    record_obligation(ns, "g94_summary_o2", "Parent divergence identity remains unproven.")
    ns.write_run_metadata()

if __name__ == "__main__":
    main()
