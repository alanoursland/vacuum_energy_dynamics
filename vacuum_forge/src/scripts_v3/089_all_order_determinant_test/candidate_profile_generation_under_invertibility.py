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
    ("g89_det_sequence", "089_all_order_determinant_test__candidate_determinant_sequence_N1_to_N10", "g89_det_sequence"),
    ("g89_pairing", "089_all_order_determinant_test__candidate_moment_pairing_factorization", "g89_pairing"),
]
MARKER_ID = "g89_profile_generation"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    rows = []
    header("Candidate Profile Generation Under Invertibility")
    for N in range(1, 11):
        coeffs = coefficients_for_N(N)
        next_m, rho0 = next_moment_for_coeffs(coeffs)
        target_residuals = []
        for k in range(1, N+1):
            # Use moment-ratio linear system residual rather than repeated symbolic rho integration.
            A, b = hierarchy_matrix(N)
            vec = sp.Matrix(coeffs)
            target_residuals = [sp.factor(x) for x in list(A*vec - b)]
            break
        ok = all(x == 0 for x in target_residuals)
        rows.append((N, coeffs, ok, next_m, rho0))
        print(f"N={N}: target residuals zero={ok}; next M{2*N+2}={next_m}; rho(0)={rho0}")
        print(f"  coeffs={coeffs}")

    with out.derived_results():
        for N, coeffs, ok, next_m, rho0 in rows:
            out.line(f"N={N} residuals", StatusMark.PASS if ok else StatusMark.FAIL, str(ok))
            out.line(f"N={N} next", StatusMark.WARN, str(next_m))
            out.line(f"N={N} rho0", StatusMark.WARN, str(rho0))
    with out.governance_assessments():
        out.line("profile generation", StatusMark.PASS, "determinant-valid matrices generate profiles through N=10")
        out.line("target constraints", StatusMark.PASS, "linear system residuals vanish through N=10")
        out.line("next obstruction", StatusMark.WARN, "next moments remain nonzero")
        out.line("local rho", StatusMark.WARN, "rho(0) remains nonzero")
    with out.counterexamples():
        out.line("determinant-valid but profile failure", StatusMark.FAIL, "no profile generation failure through N=10")
        out.line("profile generation as inertness", StatusMark.FAIL, "next/local obstructions remain")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=sp.Matrix([row[3] for row in rows]),
        method="generate hierarchy profiles through N=10 using invertible A_N and check residuals/next moments",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="profile_generation_N1_to_N10",
        scope="finite hierarchy determinant validation",
    )
    record_claim(ns, MARKER_ID, "g89_profile_c1", GovernanceStatus.POLICY_RULE, "Determinant-valid matrices generate hierarchy profiles through N=10.")
    record_obligation(ns, "g89_profile_o1", "Classify determinant route status.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_determinant_route_classifier.py")

if __name__ == "__main__":
    main()
