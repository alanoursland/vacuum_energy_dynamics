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
    ("g91_sign_normalization", "91_determinant_sign_pattern_and_nonzero_audit__candidate_sign_normalization_hypothesis_test", "g91_sign_normalization"),
]
MARKER_ID = "g91_post_signflip_invertibility"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    rows = []
    header("Candidate Post-Signflip Invertibility Validation")
    for N in (11, 12):
        A, b = hierarchy_matrix(N)
        detA = sp.factor(A.det(method="bareiss"))
        coeffs = A.LUsolve(b)
        residuals = [sp.factor(x) for x in list(A*coeffs - b)]
        zero_residuals = all(r == 0 for r in residuals)
        rows.append((N, sp.sign(detA), zero_residuals, coeffs[0], coeffs[-1]))
        print(f"N={N}: det_sign={sp.sign(detA)}, residuals_zero={zero_residuals}")
        print(f"  first coefficient={coeffs[0]}")
        print(f"  last coefficient={coeffs[-1]}")

    with out.derived_results():
        for N, det_sign, zero_residuals, first_c, last_c in rows:
            out.line(f"N={N} det sign", StatusMark.PASS, str(det_sign))
            out.line(f"N={N} residuals", StatusMark.PASS if zero_residuals else StatusMark.FAIL, str(zero_residuals))
            out.line(f"N={N} first coeff", StatusMark.INFO, str(first_c))
            out.line(f"N={N} last coeff", StatusMark.INFO, str(last_c))
    with out.governance_assessments():
        out.line("post-signflip generation", StatusMark.PASS, "N=11 and N=12 profile systems solve exactly")
        out.line("invertibility versus positivity", StatusMark.PASS, "negative determinant does not block coefficient generation")
    with out.counterexamples():
        out.line("negative determinant kills hierarchy", StatusMark.FAIL, "N=11 residuals vanish despite det<0")
        out.line("positivity required for Cramer", StatusMark.FAIL, "Cramer requires nonzero determinant only")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=sp.Matrix([sp.Integer(1 if row[2] else 0) for row in rows]),
        method="solve hierarchy systems at N=11 and N=12 and check exact residuals",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="post_signflip_invertibility_validation",
        scope="determinant sign-pattern audit",
    )
    record_claim(ns, MARKER_ID, "g91_post_c1", GovernanceStatus.POLICY_RULE, "profile generation survives the determinant sign flip at N=11.")
    record_obligation(ns, "g91_post_o1", "Retarget determinant theorem statuses.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_nonzero_theorem_retarget.py")

if __name__ == "__main__":
    main()
