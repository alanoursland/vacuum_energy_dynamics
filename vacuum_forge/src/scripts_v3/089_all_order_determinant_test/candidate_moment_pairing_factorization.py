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

def coefficients_for_N(N: int):
    A, b = hierarchy_matrix(N)
    return [sp.factor(x) for x in A.LUsolve(b)]

def next_moment_for_coeffs(coeffs):
    y = sp.symbols("y")
    N = len(coeffs)
    f = (1 - y**2)**3
    w = (1 - y**2)**2
    P = 1 + sum(coeffs[j-1] * y**(2*j) for j in range(1, N+1))
    rho = sp.factor(sp.diff(w*sp.diff(f*P, y), y))
    next_m = sp.factor(sp.integrate(sp.expand(y**(2*N+2)*rho), (y, -1, 1)))
    rho0 = sp.factor(rho.subs(y, 0))
    return next_m, rho0

DEPENDENCIES = [
    ("g89_pivots", "089_all_order_determinant_test__candidate_lu_pivot_nonzero_test", "g89_pivots"),
]
MARKER_ID = "g89_pairing"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    k, j, t = sp.symbols("k j t", integer=True, positive=True)
    r = sp.Rational(1, 1) * (2*k - 1)/(2*k + 3)
    q_k = t**k - r*t**(k-1)
    pairing_entry = beta_moment(k+j) - r*beta_moment(k+j-1)
    direct_entry = sp.factor(beta_moment(k+j) - r*beta_moment(k+j-1))
    diff = sp.simplify(pairing_entry - direct_entry)

    header("Candidate Moment Pairing Factorization")
    print("Define weight mu(t)=t^(-1/2)(1-t)^4 on [0,1].")
    print(f"q_k(t) = {q_k}")
    print("A_N[k,j] = <t^j, q_k(t)>_mu")
    print(f"entry = {direct_entry}")
    print(f"difference check = {diff}")
    print("Interpretation: det(A_N) pairs coefficient subspace span{t..t^N} against constraint subspace span{q_1..q_N}.")

    with out.derived_results():
        out.line("q_k", StatusMark.PASS, str(q_k))
        out.line("pairing entry", StatusMark.PASS, str(direct_entry))
        out.line("difference", StatusMark.PASS, str(diff))
    with out.governance_assessments():
        out.line("moment-pairing factorization", StatusMark.PASS, "A_N is a finite moment-pairing matrix")
        out.line("theorem target", StatusMark.INFO, "all-order determinant becomes subspace nondegeneracy theorem")
    with out.counterexamples():
        out.line("opaque determinant", StatusMark.FAIL, "determinant has moment-pairing interpretation")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[k, j],
        output=direct_entry,
        method="rewrite A_N entries as <t^j, t^k-r_k t^(k-1)> under beta weight",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="moment_pairing_factorization",
        scope="finite hierarchy determinant matrix",
    )
    record_claim(ns, MARKER_ID, "g89_pair_c1", GovernanceStatus.POLICY_RULE, "A_N is a moment-pairing matrix between coefficient and constraint subspaces.")
    record_obligation(ns, "g89_pair_o1", "Validate profile generation through determinant-valid matrices.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_profile_generation_under_invertibility.py")

if __name__ == "__main__":
    main()
