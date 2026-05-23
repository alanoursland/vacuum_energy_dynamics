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
    return sp.factor(sp.Rational(768, 1) / sp.prod(2*s + 2*m + 1 for m in range(5)))

def row_ratio(k):
    k = sp.sympify(k)
    return sp.factor((2*k - 1) / (2*k + 3))

def hierarchy_entry(k, j):
    return sp.factor(beta_moment(k+j) - row_ratio(k) * beta_moment(k+j-1))

def weight(x):
    return (1 - x**2)**4

def trial_phi(j, x):
    return x**(2*j)

def test_psi(k, x):
    return x**(2*k) - row_ratio(k) * x**(2*k-2)

def source_vector_entry(k, source_expr, x):
    return sp.factor(2 * sp.integrate(test_psi(k, x) * source_expr * weight(x), (x, 0, 1)))

DEPENDENCIES = [
    ("g101_problem", "101_residual_source_reconstruction_attempt__candidate_residual_reconstruction_problem", "g101_problem"),
]
MARKER_ID = "g101_projected_profile"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    x = sp.symbols("x", nonnegative=True)
    failures = []
    for N in range(1, 7):
        coeffs = sp.symbols(f"c1:{N+1}")
        fN = sum(coeffs[j-1] * trial_phi(j, x) for j in range(1, N+1))
        for k in range(1, N+1):
            lhs = sum(hierarchy_entry(k, j) * coeffs[j-1] for j in range(1, N+1))
            rhs = sp.factor(2 * sp.integrate(test_psi(k, x) * fN * weight(x), (x, 0, 1)))
            diff = sp.factor(lhs - rhs)
            if diff != 0:
                failures.append((N, k, diff))

    header("Candidate Projected Profile Identity")
    print("Test identity:")
    print("  Σ_j A[k,j] c_j = 2∫psi_k(x) f_N(x) w(x) dx")
    print("where f_N=Σ_j c_j x^(2j).")
    print(f"identity failures for N<=6: {failures}")

    with out.derived_results():
        out.line("projected profile identity failures", StatusMark.PASS if not failures else StatusMark.FAIL, str(failures))
    with out.governance_assessments():
        out.line("matrix action", StatusMark.PASS if not failures else StatusMark.FAIL, "A maps coefficients to weighted test projections of f_N")
        out.line("residual interpretation", StatusMark.INFO, "supports formal residual family R[f]=f-S")
    with out.counterexamples():
        out.line("identity as physical residual", StatusMark.FAIL, "matrix action alone does not define physical R[f]")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=sp.Symbol("projected_profile_identity_derived"),
        method="verify ΣA[k,j]c_j equals weighted projection of f_N for N<=6",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="projected_profile_identity",
        scope="residual source reconstruction",
    )
    record_claim(ns, MARKER_ID, "g101_profile_c1", GovernanceStatus.POLICY_RULE, "The hierarchy matrix action is the weighted projection of the finite profile f_N against row tests.")
    record_obligation(ns, "g101_profile_o1", "Define minimal residual family.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_minimal_residual_family.py")

if __name__ == "__main__":
    main()
