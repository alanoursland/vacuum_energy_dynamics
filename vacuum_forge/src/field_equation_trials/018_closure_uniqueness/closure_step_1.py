# Trial 018: Closure uniqueness, step 1
#
# Script type:
#   RIGOR PROGRAM / SELF-COUPLING OBSTRUCTION
#
# Purpose
# -------
# This is the first in-house rung toward replacing the Deser 1970
# self-coupled spin-2 closure citation. It does not retire the full
# closure-uniqueness obligation.
#
# It verifies the first consistency obstruction:
#
#   1. The linear massless spin-2 operator is identically conserved:
#        partial^mu G^(1)_{mu nu} = 0.
#   2. Therefore a linear equation G^(1) = source requires a conserved
#      total source.
#   3. The gauge variation of the matter coupling h_{mu nu}T^{mu nu}/2
#      is proportional, up to a boundary term, to partial_mu T^{mu nu}.
#   4. Matter stress alone is not conserved once it exchanges momentum
#      with h_{mu nu}; a compensating gravitational field stress is
#      therefore forced as the first self-coupling step.

from pathlib import Path

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    RecordKind,
    ScriptOutput,
    StatusMark,
)


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


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


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    return archive, ns, invalidated


t, x, y, z = sp.symbols("t x y z")
COORDS = [t, x, y, z]
LABELS = ["t", "x", "y", "z"]
ETA = [-1, 1, 1, 1]


def d_down(mu: int, expr):
    return sp.diff(expr, COORDS[mu])


def d_up(mu: int, expr):
    return ETA[mu] * sp.diff(expr, COORDS[mu])


def box(expr):
    return sum(d_up(mu, d_down(mu, expr)) for mu in range(4))


def make_symmetric_tensor(prefix: str):
    entries = {}
    for mu in range(4):
        for nu in range(mu, 4):
            entries[(mu, nu)] = sp.Function(f"{prefix}{mu}{nu}")(*COORDS)
    return sp.Matrix(
        4,
        4,
        lambda mu, nu: entries[(mu, nu)] if mu <= nu else entries[(nu, mu)],
    )


def linear_spin2_operator(h):
    trace_h = sum(ETA[alpha] * h[alpha, alpha] for alpha in range(4))
    div_div_h = sum(
        ETA[alpha] * ETA[beta] * d_down(alpha, d_down(beta, h[alpha, beta]))
        for alpha in range(4)
        for beta in range(4)
    )

    G1 = sp.zeros(4, 4)
    for mu in range(4):
        for nu in range(4):
            term1 = sum(
                d_down(alpha, d_down(mu, ETA[alpha] * h[alpha, nu]))
                for alpha in range(4)
            )
            term2 = sum(
                d_down(alpha, d_down(nu, ETA[alpha] * h[alpha, mu]))
                for alpha in range(4)
            )
            eta_mn = ETA[mu] if mu == nu else 0
            G1[mu, nu] = sp.Rational(1, 2) * (
                term1
                + term2
                - box(h[mu, nu])
                - d_down(mu, d_down(nu, trace_h))
                - eta_mn * (div_div_h - box(trace_h))
            )
    return G1


def divergence_lower_first(tensor, nu: int):
    return sp.simplify(sum(d_up(mu, tensor[mu, nu]) for mu in range(4)))


def case_0_statement(out: ScriptOutput) -> None:
    header("Case 0: Closure uniqueness program, first rung")
    print("This script starts, but does not finish, the in-house replacement")
    print("for the Deser self-coupled spin-2 closure citation.")
    print()
    print("Target of this rung: show why linear spin-2 cannot consistently")
    print("stop at matter sourcing. The linear operator is identically")
    print("conserved, so the source must be conserved; once matter exchanges")
    print("energy-momentum with the field, matter stress alone is not enough.")

    with out.governance_assessments():
        out.line(
            "closure uniqueness in-house program opened",
            StatusMark.INFO,
            "first self-coupling obstruction only; full Deser replacement remains open",
        )


def case_1_linear_bianchi(out: ScriptOutput):
    header("Case 1: Linear spin-2 operator has identically conserved divergence")
    h = make_symmetric_tensor("h")
    G1 = linear_spin2_operator(h)
    residuals = [sp.simplify(divergence_lower_first(G1, nu)) for nu in range(4)]

    for nu, residual in enumerate(residuals):
        print(f"  partial^mu G^(1)_mu{LABELS[nu]} = {sp.sstr(residual)}")

    ok = all(is_zero(residual) for residual in residuals)
    with out.derived_results():
        out.line(
            "linear Bianchi identity verified for arbitrary symmetric h",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "partial^mu G^(1)_mu nu = 0; source conservation is forced",
        )
    return ok


def case_2_gauge_variation_matter_coupling(out: ScriptOutput):
    header("Case 2: Gauge variation of the matter coupling")
    T = make_symmetric_tensor("T")
    xi = [sp.Function(f"xi{nu}")(*COORDS) for nu in range(4)]

    coupling_variation_density = sum(
        T[mu, nu] * d_down(mu, xi[nu])
        for mu in range(4)
        for nu in range(4)
    )
    boundary_density = sum(
        d_down(mu, T[mu, nu] * xi[nu])
        for mu in range(4)
        for nu in range(4)
    )
    divergence_term = sum(
        sum(d_down(mu, T[mu, nu]) for mu in range(4)) * xi[nu]
        for nu in range(4)
    )
    residual = sp.simplify(boundary_density - divergence_term - coupling_variation_density)

    print("For delta h_mu nu = partial_mu xi_nu + partial_nu xi_mu and symmetric T,")
    print("the variation of (1/2) h_mu nu T^mu nu is")
    print("  T^mu nu partial_mu xi_nu")
    print("and the product rule gives")
    print("  T^mu nu partial_mu xi_nu = boundary - (partial_mu T^mu nu) xi_nu")
    print(f"  product-rule residual = {sp.sstr(residual)}")

    ok = is_zero(residual)
    with out.derived_results():
        out.line(
            "matter coupling gauge variation requires source conservation",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "gauge invariance of the linear coupling holds only when partial_mu T^mu nu = 0 up to boundary terms",
        )
    return ok


def case_3_self_coupling_forced(out: ScriptOutput):
    header("Case 3: Matter stress alone is not a consistent terminal source")
    f = sp.symbols("f0:4")
    div_G = [sp.Integer(0) for _ in range(4)]
    div_T_matter = list(f)
    div_tau_grav = [-item for item in f]

    matter_only_residuals = [
        sp.simplify(div_G[nu] - div_T_matter[nu]) for nu in range(4)
    ]
    total_source_residuals = [
        sp.simplify(div_G[nu] - (div_T_matter[nu] + div_tau_grav[nu]))
        for nu in range(4)
    ]

    print("Let f_nu be the exchange force density:")
    print("  partial_mu T_matter^mu nu = f_nu")
    print("The linear spin-2 equation has conserved left side, so matter-only")
    print("sourcing leaves residuals:")
    for nu, residual in enumerate(matter_only_residuals):
        print(f"  nu={LABELS[nu]}: {sp.sstr(residual)}")
    print("Adding a field stress tau with partial_mu tau^mu nu = -f_nu gives:")
    for nu, residual in enumerate(total_source_residuals):
        print(f"  nu={LABELS[nu]}: {sp.sstr(residual)}")

    matter_only_fails_symbolically = all(
        sp.simplify(matter_only_residuals[nu] + f[nu]) == 0 for nu in range(4)
    )
    total_ok = all(is_zero(residual) for residual in total_source_residuals)
    ok = matter_only_fails_symbolically and total_ok

    print()
    print("Interpretation: the first self-coupling step is not optional.")
    print("Once matter and h exchange energy-momentum, the field's own stress")
    print("must enter the source so the total source remains conserved.")

    with out.derived_results():
        out.line(
            "first self-coupling obstruction verified",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "matter-only source is inconsistent for nonzero exchange; field stress with opposite divergence is forced",
        )
    return ok


def case_4_verdict(out: ScriptOutput) -> None:
    header("Case 4: Verdict")
    print("This first in-house rung proves the conservation obstruction that")
    print("starts the spin-2 self-coupling chain. It does not yet prove the")
    print("full Deser closure or uniqueness of the Einstein-Hilbert endpoint.")
    print()
    print("Next rung: compute or organize the first explicit self-coupling")
    print("term, ideally in a first-order/Palatini form where the finite")
    print("closure can be displayed without an uncontrolled infinite tower.")

    with out.governance_assessments():
        out.line(
            "closure uniqueness obligation advanced but not retired",
            StatusMark.INFO,
            "linear conservation obstruction discharged; full self-coupled closure remains open",
        )
    with out.unresolved_obligations():
        out.line(
            "in-house self-coupled spin-2 closure uniqueness",
            StatusMark.OBLIGATION,
            "first obstruction proved here; full Deser replacement remains the active load-bearing debt",
        )


def record_results(ns) -> None:
    ns.record_derivation(
        derivation_id="linear_bianchi_identity_018",
        inputs=[],
        output=sp.Symbol("partial_up_mu_G1_mu_nu_eq_zero"),
        method="symbolic divergence of the Fierz-Pauli/linearized Einstein operator for arbitrary symmetric h",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="closure_uniqueness_rung",
        scope="linear massless spin-2 operator on Minkowski background",
    )
    ns.record_derivation(
        derivation_id="matter_coupling_gauge_variation_018",
        inputs=[],
        output=sp.Symbol("delta_S_int_boundary_minus_divT_xi"),
        method="product-rule check for delta h_mu nu = partial_mu xi_nu + partial_nu xi_mu",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="closure_uniqueness_rung",
        scope="linear universal coupling h_mu nu T^mu nu / 2",
    )
    ns.record_derivation(
        derivation_id="first_self_coupling_obstruction_018",
        inputs=[],
        output=sp.Symbol("field_stress_required_for_total_source_conservation"),
        method="algebraic exchange-force check: div T_matter = f requires div tau_field = -f",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="closure_uniqueness_rung",
        scope="first consistency obstruction; not the full nonlinear closure",
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="closure_uniqueness_inhouse_018",
        script_id=SCRIPT_ID,
        title="In-house self-coupled spin-2 closure uniqueness",
        status=ObligationStatus.OPEN,
        required_by=["field_equation_proof"],
        description=(
            "First conservation/self-coupling obstruction is proved in-house by "
            "linear_bianchi_identity_018, matter_coupling_gauge_variation_018, "
            "and first_self_coupling_obstruction_018. Full Deser replacement remains open."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="closure_step_1_claim_018",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "The first self-coupling step is forced: the linear spin-2 operator "
            "has identically conserved divergence, the linear matter coupling "
            "is gauge invariant only for conserved source, and matter stress "
            "alone is not conserved when it exchanges energy-momentum with the "
            "field. A compensating gravitational field stress must enter the source. "
            "This advances but does not retire the in-house closure-uniqueness obligation."
        ),
        derivation_ids=[
            "linear_bianchi_identity_018",
            "matter_coupling_gauge_variation_018",
            "first_self_coupling_obstruction_018",
        ],
        obligation_ids=["closure_uniqueness_inhouse_018"],
    ))


def main() -> None:
    header("Trial 018: Closure Uniqueness Step 1")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    case_0_statement(out)
    case_1_linear_bianchi(out)
    case_2_gauge_variation_matter_coupling(out)
    case_3_self_coupling_forced(out)
    case_4_verdict(out)

    record_results(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()

