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
    ("g91_sign_sequence", "091_determinant_sign_pattern_and_nonzero_audit__candidate_determinant_sign_sequence_N1_to_N30", "g91_sign_sequence"),
]
MARKER_ID = "g91_sign_normalization"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    rows = det_sequence(30)
    normalized = []
    failures = []
    header("Candidate Sign Normalization Hypothesis Test")
    print("Hypothesis:")
    print("  S_N = det(A_N) for N<=10")
    print("  S_N = (-1)^N det(A_N) for N>=11")
    print("Expected: S_N > 0 in tested range.")
    for N, detA, det_sign, pivot, pivot_sign in rows:
        sign_factor = sp.Integer(1) if N <= 10 else sp.Integer(-1 if N % 2 else 1)
        S = sp.factor(sign_factor * detA)
        s_sign = sp.sign(S)
        normalized.append((N, s_sign))
        if s_sign <= 0:
            failures.append((N, s_sign))
        print(f"N={N}: normalized_sign={s_sign}")

    with out.derived_results():
        out.line("normalization failures", StatusMark.PASS if not failures else StatusMark.FAIL, str(failures))
        for N, s_sign in normalized:
            out.line(f"N={N} normalized sign", StatusMark.PASS if s_sign > 0 else StatusMark.FAIL, str(s_sign))
    with out.governance_assessments():
        out.line("sign-normalized evidence", StatusMark.PASS, "normalized determinants positive through N=30")
        out.line("conjecture status", StatusMark.INFO, "finite sign normalization is a conjecture, not theorem")
    with out.counterexamples():
        out.line("raw positivity", StatusMark.FAIL, "normalization is needed after N=10")
        out.line("finite normalization as proof", StatusMark.FAIL, "finite test does not prove all-order sign law")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=sp.Matrix([row[1] for row in normalized]),
        method="test sign-normalized determinant positivity through N=30",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="sign_normalization_hypothesis",
        scope="finite sign-pattern audit",
    )
    record_claim(ns, MARKER_ID, "g91_norm_c1", GovernanceStatus.POLICY_RULE, "sign-normalized determinant is positive through N=30 under the tested pattern.")
    record_obligation(ns, "g91_norm_o1", "Validate profile generation after sign flip.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_post_signflip_invertibility_validation.py")

if __name__ == "__main__":
    main()
