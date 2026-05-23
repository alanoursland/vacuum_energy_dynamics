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
            A[k-1, j-1] = sp.factor(beta_moment(k+j) - r*beta_moment(k+j-1))
        b[k-1, 0] = sp.factor(r*beta_moment(k-1) - beta_moment(k))
    return A, b

def q_poly(k, t):
    return t**k - sp.Rational(2*k - 1, 2*k + 3)*t**(k-1)

DEPENDENCIES = [
    ("g90_chebyshev_sign", "090_determinant_positivity_theorem_attempt__candidate_chebyshev_sign_route_test", "g90_chebyshev_sign"),
]
MARKER_ID = "g90_hankel_difference"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    N = 4
    H0 = sp.zeros(N, N)
    H1 = sp.zeros(N, N)
    R = sp.zeros(N, N)
    for k in range(1, N+1):
        R[k-1, k-1] = sp.Rational(2*k - 1, 2*k + 3)
        for j in range(1, N+1):
            H0[k-1, j-1] = beta_moment(k+j-1)
            H1[k-1, j-1] = beta_moment(k+j)
    A, _ = hierarchy_matrix(N)
    diff = sp.simplify(H1 - R*H0 - A)
    det_H0 = sp.factor(H0.det(method="bareiss"))
    det_H1 = sp.factor(H1.det(method="bareiss"))

    header("Candidate Hankel Difference Structure")
    print("A = H1 - R H0")
    print("H0[k,j]=beta(k+j-1), H1[k,j]=beta(k+j), R=diag((2k-1)/(2k+3))")
    print(f"N=4 difference H1-RH0-A = {diff}")
    print(f"det(H0) for N=4 = {det_H0}")
    print(f"det(H1) for N=4 = {det_H1}")
    print("Interpretation: A is a row-dependent Hankel/Christoffel difference, not a plain positive Hankel Gram matrix.")

    with out.derived_results():
        out.line("difference", StatusMark.PASS, str(diff))
        out.line("det H0", StatusMark.PASS, str(det_H0))
        out.line("det H1", StatusMark.PASS, str(det_H1))
    with out.governance_assessments():
        out.line("Hankel difference", StatusMark.PASS, "A=H1-RH0 derived")
        out.line("proof route", StatusMark.INFO, "suggests generalized eigenvalue/Christoffel transform route")
        out.line("not Gram", StatusMark.WARN, "A is not a standard positive Gram matrix")
    with out.counterexamples():
        out.line("A as simple Hankel Gram", StatusMark.FAIL, "row-dependent R prevents direct Gram positivity proof")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=diff,
        method="decompose A_N as H1 - R H0",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="hankel_difference_structure",
        scope="determinant positivity theorem route",
    )
    record_claim(ns, MARKER_ID, "g90_hankel_c1", GovernanceStatus.POLICY_RULE, "A_N is a row-dependent Hankel difference H1-RH0, not a plain positive Gram matrix.")
    record_obligation(ns, "g90_hankel_o1", "Extend determinant/pivot evidence.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_pivot_evidence_extension_N1_to_N12.py")

if __name__ == "__main__":
    main()
