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
    ("g94_schur_identity", "094_schur_complement_positivity_attempt__candidate_schur_identity_repair", "g94_schur_identity"),
    ("g94_schur_balance", "094_schur_complement_positivity_attempt__candidate_schur_term_balance_regimes", "g94_schur_balance"),
    ("g94_schur_ratio", "094_schur_complement_positivity_attempt__candidate_schur_ratio_bound_probe", "g94_schur_ratio"),
]
MARKER_ID = "g94_classifier"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    classifications = [
        ("SCHUR_COMPLEMENT_IDENTITY_REPAIRED", "stable", "dimension-safe Schur calculation verified through N=15"),
        ("SCHUR_PIVOTS_POSITIVE_N1_TO_N15", "stable", "repaired Schur pivots positive through N=15"),
        ("TWO_REGIME_SCHUR_BALANCE_SUPPORTED_N1_TO_N15", "stable", "alpha/correction dominance pattern found"),
        ("SCHUR_RATIO_BOUND_SUPPORTED_N2_TO_N15", "stable", "correction/alpha ratio follows two-regime bounds"),
        ("ALL_ORDER_SCHUR_POSITIVITY_THEOREM_OPEN", "stable", "finite Schur evidence is not theorem"),
        ("ALL_ORDER_RATIO_BOUND_THEOREM_OPEN", "stable", "ratio bounds need proof"),
        ("ALL_ORDER_DETERMINANT_NONZERO_OPEN", "stable", "determinant nonzero remains open"),
        ("PARENT_DIVERGENCE_UNPROVEN", "stable", "parent identity remains blocked"),
        ("RECOMBINATION_BLOCKED", "stable", "no recombination license"),
    ]

    header("Candidate Schur Theorem Target Classifier")
    for name, status, reason in classifications:
        print(f"{name}: {status}; {reason}")

    with out.governance_assessments():
        out.line("Schur identity", StatusMark.PASS, "repaired")
        out.line("Schur positivity", StatusMark.PASS, "finite evidence through N=15")
        out.line("ratio theorem", StatusMark.INFO, "candidate two-regime theorem target")
        out.line("all-order Schur theorem", StatusMark.OBLIGATION, "not proven")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "recombination remains blocked")
    with out.counterexamples():
        out.line("Group 93 Schur failure carry-forward", StatusMark.FAIL, "repaired here")
        out.line("finite Schur positivity as theorem", StatusMark.FAIL, "N=15 is finite")
        out.line("parent equation", StatusMark.FAIL, "parent construction remains forbidden")
    with out.unresolved_obligations():
        out.line("ratio theorem", StatusMark.OBLIGATION, "prove two-regime correction/alpha bounds")
        out.line("Schur positivity theorem", StatusMark.OBLIGATION, "prove all leading Schur complements positive")
        out.line("biorthogonal route", StatusMark.OBLIGATION, "try structural proof if ratio route stalls")

    record_marker(ns, MARKER_ID, "Schur theorem target classifier")
    record_claim(ns, MARKER_ID, "g94_class_c1", GovernanceStatus.POLICY_RULE, "Group 94 repairs the Schur identity and identifies a two-regime Schur ratio theorem target.")
    record_claim(ns, MARKER_ID, "g94_class_c2", GovernanceStatus.POLICY_RULE, "All-order Schur positivity remains open.")
    record_obligation(ns, "g94_class_o1", "Attempt two-regime Schur ratio bound theorem next.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_group_94_status_summary.py")

if __name__ == "__main__":
    main()
