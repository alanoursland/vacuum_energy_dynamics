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
    ("g91_problem", "91_determinant_sign_pattern_and_nonzero_audit__candidate_sign_pattern_problem", "g91_problem"),
]
MARKER_ID = "g91_n11_counterexample"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    rows = det_sequence(12)
    selected = [row for row in rows if row[0] in (10, 11, 12)]

    header("Candidate N11 Counterexample Verification")
    for N, detA, det_sign, pivot, pivot_sign in selected:
        print(f"N={N}")
        print(f"  det sign = {det_sign}; det = {detA}")
        print(f"  pivot sign = {pivot_sign}; pivot = {pivot}")

    n11 = selected[1]
    positivity_counterexample = (n11[2] < 0 and n11[4] < 0)

    with out.derived_results():
        for N, detA, det_sign, pivot, pivot_sign in selected:
            out.line(f"N={N} det sign", StatusMark.PASS if detA != 0 else StatusMark.FAIL, str(det_sign))
            out.line(f"N={N} pivot sign", StatusMark.PASS if pivot != 0 else StatusMark.FAIL, str(pivot_sign))
        out.line("N=11 positivity counterexample", StatusMark.PASS if positivity_counterexample else StatusMark.FAIL, str(positivity_counterexample))
    with out.governance_assessments():
        out.line("positivity theorem", StatusMark.FAIL, "det(A_11)<0, so det(A_N)>0 for all N is false")
        out.line("pivot positivity", StatusMark.FAIL, "pivot_11<0, so positive pivot theorem is false")
        out.line("nonzero determinant", StatusMark.PASS, "N=10..12 determinants remain nonzero")
    with out.counterexamples():
        out.line("all-order positivity", StatusMark.FAIL, "N=11 is explicit counterexample")
        out.line("sign flip kills invertibility", StatusMark.FAIL, "det(A_11) is negative but nonzero")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=sp.Matrix([n11[1], n11[3]]),
        method="exact determinant and pivot recomputation for N=10,11,12",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="n11_counterexample_verification",
        scope="determinant sign audit",
    )
    record_claim(ns, MARKER_ID, "g91_n11_c1", GovernanceStatus.POLICY_RULE, "determinant positivity is disproven by det(A_11)<0.")
    record_claim(ns, MARKER_ID, "g91_n11_c2", GovernanceStatus.POLICY_RULE, "nonzero determinant remains intact through N=12.")
    record_obligation(ns, "g91_n11_o1", "Compute determinant sign sequence through N=30.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_determinant_sign_sequence_N1_to_N30.py")

if __name__ == "__main__":
    main()
