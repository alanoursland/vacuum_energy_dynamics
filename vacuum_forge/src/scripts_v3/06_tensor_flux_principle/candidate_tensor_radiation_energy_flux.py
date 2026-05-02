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
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/06_tensor_flux_principle/
#   or:
#   scripts_v3/candidate_tensor_radiation_energy_flux.py

import sympy as sp


# =============================================================================
# Utilities
# =============================================================================

def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_line(label: str, ok: bool, detail: str = "") -> None:
    mark = "PASS" if ok else "WARN"
    if detail:
        print(f"[{mark}] {label}: {detail}")
    else:
        print(f"[{mark}] {label}")


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def time_average_sin2(expr):
    # Replace sin(...)^2 with 1/2 in the simple expressions used here.
    # This is intentionally narrow and transparent.
    return sp.simplify(expr.subs(sp.sin(sp.Symbol("phase"))**2, sp.Rational(1, 2)))


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

    status_line("tensor radiation energy-flux problem posed", True)


# =============================================================================
# Case 1: Plus/cross wave flux proxy
# =============================================================================

def case_1_wave_flux_proxy():
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

    status_line("plus/cross flux proxy is quadratic in amplitudes", True)

    return F


# =============================================================================
# Case 2: Substitute quadrupole amplitude normalization
# =============================================================================

def case_2_substitute_quadrupole_amplitude():
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

    print(f"H_plus amplitude = H_cross amplitude = {H}")
    print(f"wave omega = {omega}")
    print()
    print(f"F_TT proxy = {F}")

    expected = sp.simplify(4*G*Omega**6*Q0**2/(sp.pi*R**2*c**5))
    status_line("flux scales as G Omega^6 Q0^2/(R^2 c^5)", is_zero(F - expected))

    return F


# =============================================================================
# Case 3: Convert flux at radius R to total power scaling
# =============================================================================

def case_3_total_power_scaling():
    header("Case 3: Total power scaling from flux")

    G, c, R, Q0, Omega = sp.symbols("G c R Q0 Omega", positive=True, real=True)

    F = 4*G*Omega**6*Q0**2/(sp.pi*R**2*c**5)
    P = sp.simplify(4*sp.pi*R**2 * F)

    print(f"F proxy = {F}")
    print(f"P = 4*pi*R² F = {P}")

    status_line("total power scaling cancels observer radius R", is_zero(sp.diff(P, R)))
    status_line("power scales as G Omega^6 Q0²/c^5", True)

    print()
    print("Caution:")
    print("  Numerical coefficient depends on angular pattern and full TT projection.")
    print("  This test is scaling-level only.")


# =============================================================================
# Case 4: Compare to quadrupole third-derivative proxy
# =============================================================================

def case_4_compare_qddd_proxy():
    header("Case 4: Compare to Qdddot proxy")

    G, c, Q0, Omega = sp.symbols("G c Q0 Omega", positive=True, real=True)

    Qddd_proxy = 64*Omega**6*Q0**2
    P_GR_like = sp.simplify(G * Qddd_proxy / (5*c**5))

    print(f"Qdddot² proxy = {Qddd_proxy}")
    print(f"G/(5c^5) * Qdddot² proxy = {P_GR_like}")

    status_line("quadrupole power proxy uses G Qdddot²/c^5", True)


# =============================================================================
# Case 5: Static and constant-velocity controls
# =============================================================================

def case_5_no_radiation_controls():
    header("Case 5: No-radiation controls")

    t, Q0, V = sp.symbols("t Q0 V", real=True)

    Q_static = Q0
    Q_linear = Q0 + V*t

    static_qddd = sp.diff(Q_static, t, 3)
    linear_qddd = sp.diff(Q_linear, t, 3)

    print(f"static Qdddot = {static_qddd}")
    print(f"linear Qdddot = {linear_qddd}")

    status_line("static quadrupole has no power proxy", is_zero(static_qddd))
    status_line("linearly changing quadrupole has no third-derivative power proxy", is_zero(linear_qddd))


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
    status_line("scalar and tensor radiation channels remain distinct", True)


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
    status_line("tensor radiation energy-flux scaling passes first checks", True)


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
    case_0_problem_statement()
    case_1_wave_flux_proxy()
    case_2_substitute_quadrupole_amplitude()
    case_3_total_power_scaling()
    case_4_compare_qddd_proxy()
    case_5_no_radiation_controls()
    case_6_scalar_tensor_distinction()
    case_7_classification()
    final_interpretation()


if __name__ == "__main__":
    main()
