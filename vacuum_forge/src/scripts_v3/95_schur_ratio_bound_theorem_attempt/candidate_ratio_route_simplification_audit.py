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
    ("g95_ratio_equivalence", "95_schur_ratio_bound_theorem_attempt__candidate_ratio_bound_equivalence", "g95_ratio_equivalence"),
    ("g95_post_transition_evidence", "95_schur_ratio_bound_theorem_attempt__candidate_post_transition_ratio_evidence_N11_to_N25", "g95_post_transition_evidence"),
    ("g95_gap_probe", "95_schur_ratio_bound_theorem_attempt__candidate_ratio_gap_structure_probe", "g95_gap_probe"),
]
MARKER_ID = "g95_route_audit"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    classifications = [
        ("RATIO_BOUND_EQUIVALENCE_DERIVED", "stable", "under alpha>0, 0<correction/alpha<1 is equivalent to correction>0 and schur>0"),
        ("POST_TRANSITION_RATIO_BOUND_SUPPORTED_N11_TO_N25", "stable", "alpha, correction, schur, ratio, and gap signs pass through N=25"),
        ("SCHUR_GAP_POSITIVE_N11_TO_N25", "stable", "gap=schur/alpha positive through N=25"),
        ("RATIO_ROUTE_IS_REPACKAGING_PLUS_GAP_TARGET", "stable", "ratio bound does not bypass Schur positivity; it expresses it as positive gap under alpha>0"),
        ("ALL_ORDER_RATIO_BOUND_THEOREM_OPEN", "stable", "finite ratio/gap evidence is not theorem"),
        ("ALL_ORDER_SCHUR_POSITIVITY_THEOREM_OPEN", "stable", "Schur positivity remains open"),
        ("ALL_ORDER_DETERMINANT_NONZERO_OPEN", "stable", "determinant nonzero remains open"),
        ("PARENT_DIVERGENCE_UNPROVEN", "stable", "parent identity remains blocked"),
        ("RECOMBINATION_BLOCKED", "stable", "no recombination license"),
    ]

    header("Candidate Ratio Route Simplification Audit")
    for name, status, reason in classifications:
        print(f"{name}: {status}; {reason}")

    with out.governance_assessments():
        out.line("ratio equivalence", StatusMark.PASS, "derived")
        out.line("post-transition evidence", StatusMark.PASS, "extended through N=25")
        out.line("route simplification", StatusMark.INFO, "ratio route mostly repackages Schur positivity as gap positivity under alpha>0")
        out.line("all-order ratio theorem", StatusMark.OBLIGATION, "not proven")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "recombination remains blocked")
    with out.counterexamples():
        out.line("ratio route proves theorem", StatusMark.FAIL, "only finite evidence plus equivalence")
        out.line("ratio route independent of Schur positivity", StatusMark.FAIL, "ratio<1 is schur/alpha>0")
        out.line("parent equation", StatusMark.FAIL, "parent construction remains forbidden")
    with out.unresolved_obligations():
        out.line("post-transition alpha sign", StatusMark.OBLIGATION, "prove alpha_N>0 for N>=11")
        out.line("post-transition correction sign", StatusMark.OBLIGATION, "prove correction_N>0 for N>=11")
        out.line("post-transition gap sign", StatusMark.OBLIGATION, "prove gap_N=schur_N/alpha_N>0 for N>=11")

    record_marker(ns, MARKER_ID, "Schur ratio route simplification audit")
    record_claim(ns, MARKER_ID, "g95_audit_c1", GovernanceStatus.POLICY_RULE, "The ratio route is equivalent to Schur gap positivity under post-transition alpha/correction sign assumptions.")
    record_claim(ns, MARKER_ID, "g95_audit_c2", GovernanceStatus.POLICY_RULE, "Post-transition ratio-bound evidence is extended through N=25, but all-order theorem remains open.")
    record_obligation(ns, "g95_audit_o1", "Attempt post-transition alpha/correction/gap sign theorem next.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_group_95_status_summary.py")

if __name__ == "__main__":
    main()
