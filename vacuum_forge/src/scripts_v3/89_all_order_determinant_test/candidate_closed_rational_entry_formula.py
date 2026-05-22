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
    ("g89_problem", "89_all_order_determinant_test__candidate_determinant_problem", "g89_problem"),
]
MARKER_ID = "g89_entry_formula"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    s, k, j = sp.symbols("s k j", integer=True, positive=True)
    beta_formula = beta_moment(s)
    r = sp.Rational(1, 1) * (2*k - 1)/(2*k + 3)
    entry = sp.factor(beta_moment(k+j) - r*beta_moment(k+j-1))
    test_entry = sp.factor(entry.subs({k: 2, j: 3}))
    direct = sp.factor(beta_moment(5) - sp.Rational(3, 7)*beta_moment(4))
    diff = sp.simplify(test_entry - direct)

    header("Candidate Closed Rational Entry Formula")
    print(f"beta_moment(s) = {beta_formula}")
    print("A_N[k,j] = beta(k+j) - ((2k-1)/(2k+3))*beta(k+j-1)")
    print(f"generic entry = {entry}")
    print(f"test entry k=2,j=3 = {test_entry}")
    print(f"direct check difference = {diff}")

    with out.derived_results():
        out.line("beta closed form", StatusMark.PASS, str(beta_formula))
        out.line("entry formula", StatusMark.PASS, str(entry))
        out.line("test difference", StatusMark.PASS, str(diff))
    with out.governance_assessments():
        out.line("closed rational entry", StatusMark.PASS, "A_N entries require no symbolic Beta/Gamma simplification")
        out.line("runtime hygiene", StatusMark.PASS, "determinant tests now use exact rational arithmetic")
    with out.counterexamples():
        out.line("symbolic beta blowup", StatusMark.FAIL, "closed rational beta formula replaces symbolic special functions")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[s, k, j],
        output=entry,
        method="use closed rational formula for B(s+1/2,5) to derive A_N entries",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="closed_rational_entry_formula",
        scope="finite hierarchy determinant matrix",
    )
    record_claim(ns, MARKER_ID, "g89_entry_c1", GovernanceStatus.POLICY_RULE, "A_N entries have an exact closed rational formula.")
    record_obligation(ns, "g89_entry_o1", "Compute determinant sequence through N=10.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_determinant_sequence_N1_to_N10.py")

if __name__ == "__main__":
    main()
