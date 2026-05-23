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
    return sp.factor(sp.Rational(768, 1) / denom)

def hierarchy_entry(k, j):
    k = sp.sympify(k)
    j = sp.sympify(j)
    return sp.factor(beta_moment(k+j) - ((2*k - 1) / (2*k + 3)) * beta_moment(k+j-1))

def hierarchy_matrix(N: int):
    A = sp.zeros(N, N)
    for k in range(1, N + 1):
        for j in range(1, N + 1):
            A[k-1, j-1] = hierarchy_entry(k, j)
    return A

DEPENDENCIES = [
    ("g099_origin_matrix", "099_hierarchy_source_origin_audit__candidate_origin_route_evidence_matrix", "g099_origin_matrix"),
]
MARKER_ID = "g099_moment_probe"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    s = sp.symbols("s", integer=True, positive=True)
    x = sp.symbols("x", positive=True)

    # Try to represent beta_moment(s) as a beta integral.
    # Integral_0^1 x^(2s) (1-x^2)^4 dx = 1/2 * Beta(s+1/2, 5)
    # = 12*sqrt(pi)*Gamma(s+1/2)/Gamma(s+11/2)
    # For half-integer ratios this becomes rational with five odd factors.
    integral_expr = sp.integrate(x**(2*s) * (1 - x**2)**4, (x, 0, 1))
    candidate_scaled = sp.factor(2 * integral_expr)
    target = beta_moment(s)
    ratio = sp.factor(target / candidate_scaled)

    # Verify constant ratio for sample s.
    sample_ratios = [sp.factor(beta_moment(n) / (2 * sp.integrate(x**(2*n) * (1 - x**2)**4, (x, 0, 1)))) for n in range(1, 8)]
    constant_ratio = all(sp.factor(r - sample_ratios[0]) == 0 for r in sample_ratios)

    # Derive exact identity from product form.
    product_integral_formula = sp.factor(sp.Rational(384, 1) / sp.prod(2*s + 2*m + 1 for m in range(5)))
    # Integral itself equals 384/product? Check samples. Then beta_moment is 2*integral.
    sample_integral_checks = []
    for n in range(1, 8):
        integ = sp.integrate(x**(2*n) * (1 - x**2)**4, (x, 0, 1))
        sample_integral_checks.append(sp.factor(integ - product_integral_formula.subs(s, n)))

    header("Candidate Moment Projection Plausibility Probe")
    print("Test beta_moment as a beta-type moment.")
    print("Candidate integral:")
    print("  I_s = ∫_0^1 x^(2s) (1-x^2)^4 dx")
    print(f"Sympy integral expression: {integral_expr}")
    print(f"Target beta_moment(s): {target}")
    print(f"target / (2*I_s): {ratio}")
    print(f"sample ratios: {sample_ratios}")
    print(f"constant ratio across samples: {constant_ratio}")
    print(f"sample integral checks against 384/product: {sample_integral_checks}")
    print()
    print("Interpretation:")
    print("  beta_moment(s) has a beta-integral moment representation up to a constant normalization.")
    print("  This supports a moment/projection origin as mathematically plausible.")
    print("  It does not derive the physical residual, basis, source vector, or boundary conditions.")

    failures = [c for c in sample_integral_checks if c != 0]
    with out.derived_results():
        out.line("sample ratio constant", StatusMark.PASS if constant_ratio else StatusMark.FAIL, str(constant_ratio))
        out.line("integral check failures", StatusMark.PASS if not failures else StatusMark.FAIL, str(failures))
        out.line("target over 2I", StatusMark.INFO, str(ratio))
    with out.governance_assessments():
        out.line("moment structure", StatusMark.PASS, "beta_moment has beta-integral moment representation in tested/symbolic form")
        out.line("projection origin", StatusMark.INFO, "mathematically plausible but physically underderived")
        out.line("physical source", StatusMark.OBLIGATION, "residual/basis/source/boundary still missing")
    with out.counterexamples():
        out.line("moment representation as field equation", StatusMark.FAIL, "integral identity is not a physical derivation")
        out.line("moment origin as burden ledger", StatusMark.FAIL, "no ledger assignment follows")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[s],
        output=sp.Symbol("beta_moment_integral_supported"),
        method="probe beta_moment(s) as beta-type moment integral with weight (1-x^2)^4",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="moment_projection_plausibility_probe",
        scope="hierarchy source-origin audit",
    )
    record_claim(ns, MARKER_ID, "g099_moment_c1", GovernanceStatus.POLICY_RULE, "The beta_moment sequence has a plausible moment-integral structure, but physical projection origin is not derived.")
    record_obligation(ns, "g099_moment_o1", "Classify source-origin decision surface.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_source_origin_decision_surface.py")

if __name__ == "__main__":
    main()
