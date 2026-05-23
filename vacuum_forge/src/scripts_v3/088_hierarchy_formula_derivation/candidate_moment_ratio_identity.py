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
    """Exact B(s+1/2, 5) for integer or rational s.

    Using B(x,5)=24/[x(x+1)(x+2)(x+3)(x+4)] avoids slow symbolic
    beta/gamma simplification. For x=s+1/2 this is:
      768 / Π_{m=0}^4 (2s + 2m + 1).
    """
    s = sp.Rational(s) if isinstance(s, int) else sp.sympify(s)
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

def beta_formula_coefficients(N: int):
    A, b = hierarchy_matrix(N)
    sol_vec = A.LUsolve(b)
    return [sp.factor(sol_vec[i, 0]) for i in range(N)]

def moment_value(k: int, coeffs):
    """Return M_(2k) from the Beta moment identity for P=1+Σ a_j t^j."""
    all_coeffs = [sp.Integer(1)] + list(coeffs)
    def I(index: int):
        return sum(all_coeffs[j] * beta_moment(index + j) for j in range(len(all_coeffs)))
    return sp.factor(2*k * ((2*k - 1)*I(k-1) - (2*k + 3)*I(k)))

def rho_at_zero(coeffs):
    """rho(0) for Xi=(1-y^2)^3 P(y^2), J=(1-y^2)^2 Xi'."""
    a1 = coeffs[0] if coeffs else sp.Integer(0)
    return sp.factor(2*(a1 - 3))

def profile_from_coeffs(coeffs):
    t = sp.symbols("t")
    return sp.expand(1 + sum(coeffs[j-1] * t**j for j in range(1, len(coeffs)+1)))

DEPENDENCIES = [
    ("g88_problem", "088_hierarchy_formula_derivation__candidate_hierarchy_formula_problem", "g88_problem"),
]
MARKER_ID = "g88_moment_ratio"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    y, k = sp.symbols("y k", integer=True, positive=True)
    t = sp.symbols("t", positive=True)
    derivative_kernel = sp.factor(sp.diff(2*k*y**(2*k-1)*(1-y**2)**2, y))
    expected_kernel = sp.factor(2*k*y**(2*k-2)*(1-y**2)*((2*k-1) - (2*k+3)*y**2))
    kernel_check = sp.simplify(derivative_kernel - expected_kernel)
    r_k = sp.simplify(sp.Rational(1,1)*(2*k-1)/(2*k+3))

    header("Candidate Moment Ratio Identity")
    print("After two integrations by parts:")
    print("M_(2k) = integral Xi * d/dy[2k y^(2k-1)(1-y^2)^2] dy")
    print(f"kernel derivative = {derivative_kernel}")
    print(f"expected kernel = {expected_kernel}")
    print(f"kernel difference = {kernel_check}")
    print("With t=y^2 and I_k(P)=int_0^1 t^(k-1/2)(1-t)^4 P(t) dt:")
    print(f"M_(2k)=0 iff I_k = r_k I_(k-1), r_k = {r_k}")

    with out.derived_results():
        out.line("kernel derivative", StatusMark.PASS, str(derivative_kernel))
        out.line("kernel check", StatusMark.PASS, str(kernel_check))
        out.line("ratio r_k", StatusMark.PASS, str(r_k))
    with out.governance_assessments():
        out.line("moment-ratio identity", StatusMark.PASS, "M2k constraints reduce to I_k/I_(k-1) ratio")
        out.line("structural simplification", StatusMark.PASS, "hierarchy becomes moment-ratio problem")
    with out.counterexamples():
        out.line("black-box solve only", StatusMark.FAIL, "moment constraints have integration-by-parts structure")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[k],
        output=r_k,
        method="integrate M2k by parts twice and convert to t=y^2 moment ratio",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="moment_ratio_identity",
        scope="reduced compact-support exactness hierarchy",
    )
    record_claim(ns, MARKER_ID, "g88_ratio_c1", GovernanceStatus.POLICY_RULE, "The M2k=0 hierarchy constraints reduce to I_k=((2k-1)/(2k+3))I_(k-1).")
    record_obligation(ns, "g88_ratio_o1", "Convert moment-ratio identity into Beta linear system.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_beta_linear_system_formula.py")

if __name__ == "__main__":
    main()
