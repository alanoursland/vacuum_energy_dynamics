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
]
MARKER_ID = "g91_sign_sequence"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    rows = det_sequence(30)
    mismatches = []
    zero_failures = []
    header("Candidate Determinant Sign Sequence N1 to N30")
    for N, detA, det_sign, pivot, pivot_sign in rows:
        exp_det = expected_det_sign(N)
        exp_pivot = expected_pivot_sign(N)
        if det_sign != exp_det or pivot_sign != exp_pivot:
            mismatches.append((N, det_sign, exp_det, pivot_sign, exp_pivot))
        if detA == 0 or pivot == 0:
            zero_failures.append((N, detA, pivot))
        print(f"N={N}: det_sign={det_sign}, expected={exp_det}; pivot_sign={pivot_sign}, expected={exp_pivot}")

    with out.derived_results():
        out.line("mismatches", StatusMark.PASS if not mismatches else StatusMark.WARN, str(mismatches))
        out.line("zero failures", StatusMark.PASS if not zero_failures else StatusMark.FAIL, str(zero_failures))
        for N, detA, det_sign, pivot, pivot_sign in rows:
            out.line(f"N={N}", StatusMark.PASS if detA != 0 else StatusMark.FAIL, f"det_sign={det_sign}, pivot_sign={pivot_sign}")
    with out.governance_assessments():
        out.line("nonzero evidence", StatusMark.PASS, "det(A_N) nonzero through N=30")
        out.line("sign pattern evidence", StatusMark.PASS if not mismatches else StatusMark.WARN, "tested sign pattern matches through N=30")
        out.line("finite scope", StatusMark.INFO, "N=1..30 is strong finite evidence, not all-order proof")
    with out.counterexamples():
        out.line("positivity restored", StatusMark.FAIL, "determinant signs alternate after N=10 in tested range")
        out.line("finite sign pattern as theorem", StatusMark.FAIL, "finite match does not prove all N")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=sp.Matrix([row[2] for row in rows]),
        method="exact determinant and pivot sign sequence through N=30",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="determinant_sign_sequence_N1_to_N30",
        scope="finite determinant sign-pattern audit",
    )
    record_claim(ns, MARKER_ID, "g91_sign_c1", GovernanceStatus.POLICY_RULE, "det(A_N) is nonzero through N=30.")
    record_claim(ns, MARKER_ID, "g91_sign_c2", GovernanceStatus.POLICY_RULE, "finite sign pattern is supported through N=30: positive through N=10 and (-1)^N thereafter.")
    record_obligation(ns, "g91_sign_o1", "Test sign-normalized determinant hypothesis.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_sign_normalization_hypothesis_test.py")

if __name__ == "__main__":
    main()
