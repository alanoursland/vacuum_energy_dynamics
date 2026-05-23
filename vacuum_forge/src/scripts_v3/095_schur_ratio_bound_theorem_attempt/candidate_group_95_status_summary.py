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
    ("g94_summary", "094_schur_complement_positivity_attempt__candidate_group_94_status_summary", "g94_summary"),
    ("g95_problem", "095_schur_ratio_bound_theorem_attempt__candidate_ratio_bound_problem", "g95_problem"),
    ("g95_ratio_equivalence", "095_schur_ratio_bound_theorem_attempt__candidate_ratio_bound_equivalence", "g95_ratio_equivalence"),
    ("g95_post_transition_evidence", "095_schur_ratio_bound_theorem_attempt__candidate_post_transition_ratio_evidence_N11_to_N25", "g95_post_transition_evidence"),
    ("g95_gap_probe", "095_schur_ratio_bound_theorem_attempt__candidate_ratio_gap_structure_probe", "g95_gap_probe"),
    ("g95_route_audit", "095_schur_ratio_bound_theorem_attempt__candidate_ratio_route_simplification_audit", "g95_route_audit"),
]
MARKER_ID = "g95_summary"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Group 95 Status Summary")
    print("Group 95 attempts to sharpen the Group 94 Schur ratio-bound target.")
    print("Stable result:")
    print("  ratio-bound equivalence derived")
    print("  for alpha>0, 0<correction/alpha<1 is equivalent to correction>0 and schur>0")
    print("  post-transition ratio-bound evidence extended through N=25")
    print("  Schur gap g_N=1-r_N=schur/alpha positive through N=25")
    print("  ratio route is mostly a repackaging of Schur positivity as gap positivity under alpha>0")
    print("  all-order ratio-bound theorem remains open")
    print("  all-order Schur positivity theorem remains open")
    print("  all-order determinant nonzero theorem remains open")
    print("  parent divergence identity remains unproven")
    print("  recombination remains blocked")

    with out.governance_assessments():
        out.line("ratio equivalence", StatusMark.PASS, "derived")
        out.line("post-transition evidence", StatusMark.PASS, "extended through N=25")
        out.line("gap positivity", StatusMark.PASS, "supported through N=25")
        out.line("route simplification", StatusMark.INFO, "ratio route reduces to gap/sign theorem")
        out.line("all-order theorem", StatusMark.OBLIGATION, "not proven")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "recombination remains blocked")
    with out.counterexamples():
        out.line("ratio proof closed", StatusMark.FAIL, "not proven")
        out.line("finite evidence as theorem", StatusMark.FAIL, "N=25 is finite")
        out.line("parent equation", StatusMark.FAIL, "parent construction remains forbidden")
    with out.unresolved_obligations():
        out.line("alpha positivity", StatusMark.OBLIGATION, "prove alpha_N>0 post-transition")
        out.line("correction positivity", StatusMark.OBLIGATION, "prove correction_N>0 post-transition")
        out.line("gap positivity", StatusMark.OBLIGATION, "prove schur_N/alpha_N>0 post-transition")

    print("\nRecommended next routes:")
    print("  96_post_transition_schur_sign_theorem_attempt")
    print("  96_alpha_correction_sign_theorem_attempt")
    print("  96_schur_gap_positivity_theorem_attempt")
    print("  96_biorthogonal_pivot_construction")
    print("  96_hankel_difference_pivot_analysis")

    record_marker(ns, MARKER_ID, "Group 95 summary; Schur ratio-bound theorem attempt")
    record_claim(ns, MARKER_ID, "g95_summary_c1", GovernanceStatus.POLICY_RULE, "Group 95 derives the ratio-bound equivalence and extends post-transition evidence through N=25.")
    record_claim(ns, MARKER_ID, "g95_summary_c2", GovernanceStatus.POLICY_RULE, "The ratio route is mostly a gap/sign reformulation; all-order proof remains open.")
    record_obligation(ns, "g95_summary_o1", "Attempt post-transition Schur sign/gap theorem next.")
    record_obligation(ns, "g95_summary_o2", "Parent divergence identity remains unproven.")
    ns.write_run_metadata()

if __name__ == "__main__":
    main()
