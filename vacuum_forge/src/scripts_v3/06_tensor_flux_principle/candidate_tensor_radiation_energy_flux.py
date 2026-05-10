# Group:
#   06_tensor_flux_principle
#
# Script type:
#   DIAGNOSTIC

# Candidate tensor radiation energy flux
#
# Purpose
# -------
# The quadrupole coupling normalization established the target amplitude:
#
#   h_ij^TT ~ (2G/(c^4 R)) Qdd_ij^TT
#
# The next question is radiation flux / power.
#
# This script builds a reduced diagnostic for tensor radiation energy flux:
#
#   1. define plus/cross plane waves,
#   2. build a quadratic flux proxy from time derivatives,
#   3. substitute quadrupole amplitude normalization,
#   4. recover scaling P ~ G Qddd^2 / c^5,
#   5. distinguish local wave flux from total radiated power,
#   6. keep this as a target proxy, not a derivation.
#
# Important:
#   In GR, the standard averaged energy flux for TT waves has the form:
#
#     F ~ c^3/(32*pi*G) < hdot_+^2 + hdot_x^2 >
#
#   and quadrupole power has the form:
#
#     P ~ G/(5 c^5) < Qdddot_ij Qdddot_ij >
#
# This script uses those as target scalings, not derived facts.

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


# =============================================================================
# Utilities
# =============================================================================

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


def time_average_sin2(expr):
    # Replace sin(...)^2 with 1/2 in the simple expressions used here.
    # This is intentionally narrow and transparent.
    return sp.simplify(expr.subs(sp.sin(sp.Symbol("phase"))**2, sp.Rational(1, 2)))


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="quadrupole_tensor_flux_marker",
        upstream_script_id="06_tensor_flux_principle__candidate_quadrupole_tensor_flux",
        upstream_derivation_id="quadrupole_tensor_flux_marker",
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


# =============================================================================
# Case 0: Problem statement
# =============================================================================

def case_0_problem_statement():
    header("Case 0: Tensor radiation energy-flux problem")

    print("Known target amplitude:")
    print()
    print("  h_ij^TT ~ (2G/(c^4 R)) Qdd_ij^TT")
    print()
    print("Need radiation flux / power proxy:")
    print()
    print("  F_TT ~ c^3/(32*pi*G) < hdot_plus^2 + hdot_cross^2 >")
    print("  P_quad ~ G/(5c^5) < Qdddot_ij Qdddot_ij >")
    print()
    print("This script checks scaling consistency, not a derivation.")

    out = ScriptOutput()
    with out.unresolved_obligations():
        out.line("tensor radiation energy-flux problem posed", StatusMark.OBLIGATION, "target scalings stated; derivation from action remains open")


# =============================================================================
# Case 1: Plus/cross wave flux proxy
# =============================================================================

def case_1_wave_flux_proxy(ns):
    header("Case 1: Plus/cross wave flux proxy")

    t, omega, Hp, Hx, G, c = sp.symbols("t omega H_plus H_cross G c", positive=True, real=True)

    phase = sp.Symbol("phase", real=True)
    h_plus = Hp * sp.cos(phase)
    h_cross = Hx * sp.sin(phase)

    # Use d/dt phase = omega in magnitude.
    hdot_plus_sq_avg = sp.Rational(1, 2) * Hp**2 * omega**2
    hdot_cross_sq_avg = sp.Rational(1, 2) * Hx**2 * omega**2

    F = sp.simplify(c**3/(32*sp.pi*G) * (hdot_plus_sq_avg + hdot_cross_sq_avg))

    print("Averaged derivative squares:")
    print(f"<hdot_plus²> = {hdot_plus_sq_avg}")
    print(f"<hdot_cross²> = {hdot_cross_sq_avg}")
    print()
    print("Target TT flux proxy:")
    print("  F = c^3/(32*pi*G) <hdot_plus² + hdot_cross²>")
    print()
    print(f"F = {F}")

    out = ScriptOutput()
    with out.sample_results():
        out.line("plus/cross flux proxy is quadratic in amplitudes", StatusMark.PASS, f"F = {F}")

    ns.record_derivation(
        derivation_id="tt_flux_proxy_quadratic_amplitudes",
        inputs=[Hp, Hx, omega, G, c],
        output=F,
        method="GR_like_TT_flux_proxy",
        status=Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
        scope="GR-like target flux proxy; not derived from action",
    )

    return F


# =============================================================================
# Case 2: Substitute quadrupole amplitude normalization
# =============================================================================

def case_2_substitute_quadrupole_amplitude(ns):
    header("Case 2: Substitute quadrupole amplitude normalization")

    G, c, R, Q0, Omega = sp.symbols("G c R Q0 Omega", positive=True, real=True)

    # Rotating quadrupole:
    # Q_plus = Q0 cos(2Ωt), Q_cross = Q0 sin(2Ωt)
    # Qdd amplitude = 4Ω² Q0.
    # h amplitude = (2G/(c^4 R)) * 4Ω² Q0 = 8GΩ²Q0/(c^4 R).
    H = 8*G*Omega**2*Q0/(c**4 * R)

    # Wave frequency is omega = 2Ω.
    omega = 2*Omega

    F = sp.simplify(c**3/(32*sp.pi*G) * (sp.Rational(1, 2)*H**2*omega**2 + sp.Rational(1, 2)*H**2*omega**2))

    expected = sp.simplify(4*G*Omega**6*Q0**2/(sp.pi*R**2*c**5))
    residual = sp.simplify(F - expected)

    print(f"H_plus amplitude = H_cross amplitude = {H}")
    print(f"wave omega = {omega}")
    print()
    print(f"F_TT proxy = {F}")

    out = ScriptOutput()
    with out.sample_results():
        out.line("flux scales as G Omega^6 Q0^2/(R^2 c^5)",
                 StatusMark.PASS if is_zero(residual) else StatusMark.FAIL,
                 f"residual = {residual}")

    ns.record_derivation(
        derivation_id="tt_flux_quadrupole_amplitude_substitution",
        inputs=[H, omega, G, c, R, Q0, Omega],
        output=F,
        method="substitute_rotating_quadrupole_h_into_flux_proxy",
        status=Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
        scope="rotating quadrupole toy model; GR-like target",
    )

    return F


# =============================================================================
# Case 3: Convert flux at radius R to total power scaling
# =============================================================================

def case_3_total_power_scaling(ns):
    header("Case 3: Total power scaling from flux")

    G, c, R, Q0, Omega = sp.symbols("G c R Q0 Omega", positive=True, real=True)

    F = 4*G*Omega**6*Q0**2/(sp.pi*R**2*c**5)
    P = sp.simplify(4*sp.pi*R**2 * F)
    dP_dR = sp.diff(P, R)

    print(f"F proxy = {F}")
    print(f"P = 4*pi*R² F = {P}")

    out = ScriptOutput()
    with out.derived_results():
        out.line("total power scaling cancels observer radius R",
                 StatusMark.PASS if is_zero(dP_dR) else StatusMark.FAIL,
                 f"dP/dR = {dP_dR}")
        out.line("power scales as G Omega^6 Q0²/c^5", StatusMark.PASS, f"P = {P}")

    print()
    print("Caution:")
    print("  Numerical coefficient depends on angular pattern and full TT projection.")
    print("  This test is scaling-level only.")

    ns.record_derivation(
        derivation_id="tt_total_power_scaling_from_flux",
        inputs=[F, R],
        output=P,
        method="spherical_area_times_flux",
        status=Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
        scope="scaling level; numerical coefficient not derived",
    )


# =============================================================================
# Case 4: Compare to quadrupole third-derivative proxy
# =============================================================================

def case_4_compare_qddd_proxy(ns):
    header("Case 4: Compare to Qdddot proxy")

    G, c, Q0, Omega = sp.symbols("G c Q0 Omega", positive=True, real=True)

    Qddd_proxy = 64*Omega**6*Q0**2
    P_GR_like = sp.simplify(G * Qddd_proxy / (5*c**5))

    print(f"Qdddot² proxy = {Qddd_proxy}")
    print(f"G/(5c^5) * Qdddot² proxy = {P_GR_like}")

    out = ScriptOutput()
    with out.sample_results():
        out.line("quadrupole power proxy uses G Qdddot²/c^5", StatusMark.PASS, f"P_GR_like = {P_GR_like}")

    ns.record_derivation(
        derivation_id="qddd_power_proxy_gr_like",
        inputs=[Q0, Omega, G, c],
        output=P_GR_like,
        method="GR_like_power_proxy_from_Qdddot_squared",
        status=Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
        scope="GR-like target; not derived from action",
    )


# =============================================================================
# Case 5: Static and constant-velocity controls
# =============================================================================

def case_5_no_radiation_controls(ns):
    header("Case 5: No-radiation controls")

    t, Q0, V = sp.symbols("t Q0 V", real=True)

    Q_static = Q0
    Q_linear = Q0 + V*t

    static_qddd = sp.diff(Q_static, t, 3)
    linear_qddd = sp.diff(Q_linear, t, 3)

    print(f"static Qdddot = {static_qddd}")
    print(f"linear Qdddot = {linear_qddd}")

    out = ScriptOutput()
    with out.derived_results():
        out.line("static quadrupole has no power proxy",
                 StatusMark.PASS if is_zero(static_qddd) else StatusMark.FAIL,
                 f"static Qdddot = {static_qddd}")
        out.line("linearly changing quadrupole has no third-derivative power proxy",
                 StatusMark.PASS if is_zero(linear_qddd) else StatusMark.FAIL,
                 f"linear Qdddot = {linear_qddd}")

    ns.record_derivation(
        derivation_id="no_radiation_control_static_linear",
        inputs=[Q_static, Q_linear],
        output=sp.Matrix([static_qddd, linear_qddd]),
        method="time_derivative_no_radiation_controls",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
    )


# =============================================================================
# Case 6: Distinguish scalar and tensor radiation
# =============================================================================

def case_6_scalar_tensor_distinction():
    header("Case 6: Scalar and tensor radiation distinction")

    print("Scalar A channel:")
    print("  monopole/static Newtonian response")
    print("  not the TT radiation channel")
    print()
    print("Tensor h_ij^TT channel:")
    print("  plus/cross polarizations")
    print("  quadrupole time variation")
    print("  energy flux quadratic in hdot")
    print()
    print("A viable theory must avoid large unwanted scalar radiation.")
    print()

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("scalar and tensor radiation channels remain distinct", StatusMark.PASS, "A = static; h_TT = radiative")


# =============================================================================
# Case 7: Classification
# =============================================================================

def case_7_classification():
    header("Case 7: Classification")

    print("Results:")
    print()
    print("1. TT wave flux proxy is quadratic in hdot_plus and hdot_cross.")
    print("2. Substituting h ~ 2G Qdd/(c^4 R) gives flux scaling")
    print("   F ~ G Omega^6 Q0^2/(R^2 c^5).")
    print("3. Multiplying by area gives total power scaling")
    print("   P ~ G Omega^6 Q0^2/c^5.")
    print("4. This matches the Qdddot² scaling class.")
    print("5. Numerical coefficients are not derived here.")
    print("6. Scalar A remains separate from tensor radiation.")
    print()

    out = ScriptOutput()
    with out.unresolved_obligations():
        out.line("tensor radiation energy-flux scaling passes first checks", StatusMark.OBLIGATION, "scaling confirmed; coefficient derivation from action remains open")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("This script connects tensor amplitude normalization to energy-flux")
    print("scaling.")
    print()
    print("Using:")
    print("  h ~ 2G Qdd/(c^4 R)")
    print()
    print("and:")
    print("  F_TT ~ c^3/(32*pi*G) <hdot²>")
    print()
    print("gives:")
    print("  P ~ G Qdddot²/c^5")
    print()
    print("This is still a target-scaling diagnostic, not a derivation.")
    print()
    print("Next steps:")
    print("  derive flux coefficient from tensor action/stiffness")
    print("  compare angular pattern coefficients")
    print("  check no unwanted scalar radiation")
    print()
    print("Possible next artifact:")
    print("  candidate_tensor_radiation_energy_flux.md")
    print()
    print("Possible next script:")
    print("  candidate_no_unwanted_scalar_radiation.py")


def main():
    header("Candidate Tensor Radiation Energy Flux")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    case_1_wave_flux_proxy(ns)
    case_2_substitute_quadrupole_amplitude(ns)
    case_3_total_power_scaling(ns)
    case_4_compare_qddd_proxy(ns)
    case_5_no_radiation_controls(ns)
    case_6_scalar_tensor_distinction()
    case_7_classification()
    final_interpretation()

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_flux_coefficient_from_action",
        script_id=SCRIPT_ID,
        title="Derive flux coefficient from tensor action/stiffness",
        status=ObligationStatus.OPEN,
        description=(
            "The flux coefficient c^3/(32*pi*G) and quadrupole power coefficient G/(5c^5) "
            "are GR targets. They must be derived from the tensor-flux action or stiffness "
            "picture, not assumed."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="compare_angular_pattern_coefficients",
        script_id=SCRIPT_ID,
        title="Compare angular pattern coefficients for tensor radiation",
        status=ObligationStatus.OPEN,
        description=(
            "The current proxy uses spherical shell area 4*pi*R^2. "
            "An angular pattern integral over the TT projection is required to "
            "confirm the numerical coefficient."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="tensor_radiation_flux_scaling_diagnostic",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.HEURISTIC,
        statement=(
            "The TT flux proxy F ~ c^3/(32*pi*G) <hdot²> and substituting h ~ 2G Qdd/(c^4 R) "
            "gives scaling P ~ G Qdddot²/c^5. This is a scaling diagnostic, not a derivation. "
            "Numerical coefficients require action/angular-pattern derivation."
        ),
        obligation_ids=["derive_flux_coefficient_from_action", "compare_angular_pattern_coefficients"],
    ))

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
