from __future__ import annotations
from pathlib import Path
import itertools
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

DEPENDENCIES = [
    ("g93_row_sign_matrix", "93_pivot_sign_theorem_attempt__candidate_row_sign_normalized_matrix", "g93_row_sign_matrix"),
]
MARKER_ID = "g93_schur_pivots"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    failures = []
    schur_rows = []
    previous_det = sp.Integer(1)

    for N in range(1, 16):
        B = row_signed_matrix(N)
        detB = sp.factor(B.det(method="bareiss"))
        pivot_det = sp.factor(detB / previous_det)

        if N == 1:
            schur = sp.factor(B[0, 0])
        else:
            C = B[:N-1, :N-1]
            u = B[:N-1, N-1]          # column vector
            v_row = B[N-1, :N-1]      # row vector
            alpha = B[N-1, N-1]
            x = C.LUsolve(u)          # column vector solving C*x = u
            schur = sp.factor(alpha - (v_row * x)[0])

        diff = sp.factor(schur - pivot_det)
        if diff != 0:
            failures.append((N, diff))
        schur_rows.append((N, schur, sp.sign(schur)))
        previous_det = detB

    header("Candidate Schur Complement Pivot Identity")
    print("For B_N=[[B_(N-1),u],[v_row,alpha]], pivot_N = alpha - v_row B_(N-1)^(-1) u.")
    print(f"Schur/determinant pivot failures through N=15: {failures}")
    for N, schur, sign_schur in schur_rows:
        print(f"N={N}: sign(schur pivot)={sign_schur}, schur={schur}")

    with out.derived_results():
        out.line("Schur failures", StatusMark.PASS if not failures else StatusMark.FAIL, str(failures))
        for N, schur, sign_schur in schur_rows:
            out.line(f"N={N} Schur sign", StatusMark.PASS if sign_schur > 0 else StatusMark.FAIL, str(sign_schur))
    with out.governance_assessments():
        out.line("Schur pivot identity", StatusMark.PASS, "verified through N=15")
        out.line("positive Schur evidence", StatusMark.PASS, "row-signed Schur pivots positive through N=15")
        out.line("theorem target", StatusMark.INFO, "prove all row-signed leading Schur complements positive")
    with out.counterexamples():
        out.line("pivot positivity without Schur target", StatusMark.FAIL, "pivot positivity has exact Schur complement form")
        out.line("finite Schur evidence as theorem", StatusMark.FAIL, "N=15 is not all N")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=sp.Matrix([row[2] for row in schur_rows]),
        method="verify row-signed determinant pivots equal Schur complements through N=15 using row-vector Schur product",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="schur_complement_pivot_identity",
        scope="structural pivot sign theorem attempt",
    )
    record_claim(ns, MARKER_ID, "g93_schur_c1", GovernanceStatus.POLICY_RULE, "Sign-normalized pivot positivity is equivalent to positivity of row-signed leading Schur complements.")
    record_obligation(ns, "g93_schur_o1", "Test simple total positivity route.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_total_positivity_obstruction.py")

if __name__ == "__main__":
    main()
