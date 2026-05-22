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
    ("g91_n11_counterexample", "91_determinant_sign_pattern_and_nonzero_audit__candidate_n11_counterexample_verification", "g91_n11_counterexample"),
    ("g91_sign_sequence", "91_determinant_sign_pattern_and_nonzero_audit__candidate_determinant_sign_sequence_N1_to_N30", "g91_sign_sequence"),
    ("g91_sign_normalization", "91_determinant_sign_pattern_and_nonzero_audit__candidate_sign_normalization_hypothesis_test", "g91_sign_normalization"),
    ("g91_post_signflip_invertibility", "91_determinant_sign_pattern_and_nonzero_audit__candidate_post_signflip_invertibility_validation", "g91_post_signflip_invertibility"),
]
MARKER_ID = "g91_retarget"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    classifications = [
        ("POSITIVITY_THEOREM_DISPROVEN_BY_N11", "stable", "det(A_11)<0"),
        ("PIVOT_POSITIVITY_DISPROVEN_BY_N11", "stable", "pivot_11<0 and later pivots stay negative in tested range"),
        ("DETERMINANT_NONZERO_VERIFIED_N1_TO_N30", "stable", "no zero determinants found through N=30"),
        ("SIGN_PATTERN_SUPPORTED_N1_TO_N30", "stable", "det positive through N=10 and sign(det)=(-1)^N for N>=11 in tested range"),
        ("SIGN_NORMALIZATION_SUPPORTED_N1_TO_N30", "stable", "normalized determinant positive through N=30"),
        ("PROFILE_GENERATION_SURVIVES_SIGN_FLIP", "stable", "N=11 and N=12 systems solve with zero residuals"),
        ("NONZERO_INVERTIBILITY_THEOREM_OPEN", "stable", "finite nonzero evidence is not all-order proof"),
        ("SIGN_PATTERN_THEOREM_OPEN", "stable", "finite sign pattern is not all-order proof"),
        ("PARENT_DIVERGENCE_UNPROVEN", "stable", "parent identity remains blocked"),
        ("RECOMBINATION_BLOCKED", "stable", "no recombination license"),
    ]

    header("Candidate Nonzero Theorem Retarget")
    for name, status, reason in classifications:
        print(f"{name}: {status}; {reason}")

    with out.governance_assessments():
        out.line("positivity theorem", StatusMark.FAIL, "disproven by N=11")
        out.line("nonzero theorem", StatusMark.OBLIGATION, "retained as open all-order target")
        out.line("sign pattern", StatusMark.INFO, "supported through N=30")
        out.line("profile generation", StatusMark.PASS, "survives sign flip")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "recombination remains blocked")
    with out.counterexamples():
        out.line("determinant positivity carry-forward", StatusMark.FAIL, "must not carry forward")
        out.line("negative determinant as singular", StatusMark.FAIL, "negative is nonzero")
        out.line("finite nonzero as theorem", StatusMark.FAIL, "N=30 is not all N")
    with out.unresolved_obligations():
        out.line("sign recurrence", StatusMark.OBLIGATION, "derive determinant/pivot sign recurrence")
        out.line("nonzero theorem", StatusMark.OBLIGATION, "prove det(A_N)!=0 for all N")
        out.line("limit behavior", StatusMark.OBLIGATION, "study all-order hierarchy limit")

    record_marker(ns, MARKER_ID, "retarget determinant theorem from positivity to nonzero/sign-pattern")
    record_claim(ns, MARKER_ID, "g91_retarget_c1", GovernanceStatus.POLICY_RULE, "determinant positivity is disproven; determinant nonzero/invertibility remains the correct theorem target.")
    record_claim(ns, MARKER_ID, "g91_retarget_c2", GovernanceStatus.POLICY_RULE, "sign pattern and nonzero determinant are supported through N=30 but not proven all-order.")
    record_obligation(ns, "g91_retarget_o1", "Derive determinant sign recurrence or nonzero theorem next.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_group_91_status_summary.py")

if __name__ == "__main__":
    main()
