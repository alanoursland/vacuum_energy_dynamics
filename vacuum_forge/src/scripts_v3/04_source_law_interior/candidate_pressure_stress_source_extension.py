# Candidate pressure/stress source extension
#
# Purpose
# -------
# The reduced static spherical program currently has:
#
#   A-flux law:
#     F_A(r) = 4*pi*r**2*A'(r)
#     F_A(r) = 8*pi*G*M_enc(r)/c**2
#
# and:
#
#   exterior kappa = 0
#
# This works for the exact Schwarzschild exterior. But interior comparison
# with the GR constant-density Schwarzschild solution shows missing
# second-order structure inside matter.
#
# The likely missing physics is pressure/stress and/or traceful interior
# kappa response.
#
# This script tests simple source-channel hypotheses:
#
#   H1. pressure modifies A-flux source directly,
#   H2. pressure/stress sources kappa inside,
#   H3. pressure corrections vanish at boundary and preserve exterior flux,
#   H4. GR interior residual can be shaped by a pressure-like profile.
#
# IMPORTANT:
# This is a reduced diagnostic script. It does not derive the TOV equation
# or a full relativistic matter coupling.
#
# Suggested location:
#   scripts_v3/candidate_pressure_stress_source_extension.py

import sympy as sp


def header(title: str) -> None:
    print()
    print("=" * 112)
    print(title)
    print("=" * 112)


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


def series_u(expr, u, order):
    return sp.simplify(sp.series(expr, u, 0, order).removeO())


def case_0_problem_statement():
    header("Case 0: Problem statement")

    print("Current reduced source law:")
    print()
    print("  F_A(r) = 4*pi*r^2*A'(r)")
    print("  F_A(r) = 8*pi*G*M_enc(r)/c^2")
    print()
    print("This captures exterior Schwarzschild and weak-field interior potential.")
    print()
    print("But GR interior comparison shows missing second-order structure.")
    print("Candidate missing channels:")
    print("  pressure/stress source for A-flux")
    print("  pressure/stress source for interior kappa")
    print("  nonlinear interior self-field correction")
    print()
    status_line("pressure/stress source question isolated", True)


def case_1_gr_pressure_profile_weak_order():
    header("Case 1: GR constant-density pressure profile expansion")

    x, u, rho0, c = sp.symbols("x u rho0 c", positive=True, real=True)

    # Exact GR interior Schwarzschild pressure:
    # p/(rho c^2) = [sqrt(1-u x^2) - sqrt(1-u)] /
    #               [3 sqrt(1-u) - sqrt(1-u x^2)]
    p_over_rhoc2 = (sp.sqrt(1-u*x**2) - sp.sqrt(1-u)) / (
        3*sp.sqrt(1-u) - sp.sqrt(1-u*x**2)
    )

    p_series = series_u(p_over_rhoc2, u, 3)

    print("Dimensionless pressure profile for GR constant-density interior:")
    print("  p/(rho c^2) = [sqrt(1-u x²)-sqrt(1-u)] /")
    print("                 [3sqrt(1-u)-sqrt(1-u x²)]")
    print()
    print(f"p/(rho c^2) series through u² = {p_series}")

    leading = series_u(p_over_rhoc2, u, 2)
    print(f"leading pressure ratio = {leading}")

    status_line("pressure begins at order u", not is_zero(leading))
    status_line("pressure vanishes at surface x=1", is_zero(sp.simplify(p_over_rhoc2.subs(x, 1))))


def case_2_A_residual_vs_pressure_shape():
    header("Case 2: A residual versus pressure-like shape")

    x, u = sp.symbols("x u", real=True)

    A_red = 1 - sp.Rational(3, 2)*u + sp.Rational(1, 2)*u*x**2
    A_gr = sp.Rational(1, 4) * (3*sp.sqrt(1-u) - sp.sqrt(1-u*x**2))**2

    residual = sp.simplify(A_gr - A_red)
    residual_leading = sp.simplify(series_u(residual, u, 3).coeff(u, 2) * u**2)

    # Leading GR pressure shape p/(rho c^2) ~ u(1-x^2)/4.
    # A residual leading is ~ 3 u^2 (1-x^2)^2 / 16.
    pressure_shape = u*(1-x**2)/4
    pressure_squared_shape = sp.simplify(3 * pressure_shape**2)

    print(f"A_GR - A_red leading = {residual_leading}")
    print(f"leading pressure shape = {pressure_shape}")
    print(f"3 * pressure_shape^2 = {pressure_squared_shape}")
    print(f"difference = {sp.simplify(residual_leading - pressure_squared_shape)}")

    status_line("A residual has pressure-squared-like boundary shape",
                is_zero(residual_leading - pressure_squared_shape))

    print()
    print("Interpretation:")
    print("  The A residual begins at order u^2 and has shape (1-x^2)^2.")
    print("  This resembles a second-order pressure/self-field correction.")


def case_3_pressure_direct_A_flux_hypothesis():
    header("Case 3: Pressure as direct A-flux source hypothesis")

    r, G, c, rho, p, chi = sp.symbols("r G c rho p chi", positive=True, real=True)

    # Hypothesis:
    #   Delta_areal A = 8*pi*G/c^2 * (rho + chi*p/c^2)
    source = 8*sp.pi*G/c**2 * (rho + chi*p/c**2)

    print("Hypothesis H1:")
    print()
    print("  Delta_areal A = 8*pi*G/c^2 * (rho + chi p/c^2)")
    print()
    print(f"source = {source}")
    print()
    print("Consequences:")
    print("  pressure changes A-flux directly.")
    print("  if pressure vanishes at boundary, exterior flux can still be set by")
    print("  integrated effective source.")
    print()
    status_line("direct pressure A-source hypothesis formulated", True)


def case_4_pressure_as_kappa_source_hypothesis():
    header("Case 4: Pressure/stress as kappa-source hypothesis")

    kappa, C_k, rho, p, a, b, c = sp.symbols("kappa C_k rho p a b c", real=True)

    # Toy trace-like source:
    # J_k = a*rho*c^2 + b*p
    # In units-free reduced form, use J_k as a linear source.
    J_k = a*rho*c**2 + b*p
    E = C_k*kappa**2 - J_k*kappa

    eq = sp.Eq(sp.diff(E, kappa), 0)
    sol = sp.solve(eq, kappa)

    print("Hypothesis H2:")
    print()
    print("  pressure/stress sources interior kappa")
    print()
    print(f"J_k = {J_k}")
    print(f"E = {E}")
    print(f"stationary equation = {eq}")
    print(f"kappa_eq = {sol}")
    print()
    print("If J_k vanishes in exterior, kappa relaxes to zero outside.")
    status_line("pressure/stress kappa-source hypothesis formulated", bool(sol))


def case_5_boundary_preservation_conditions():
    header("Case 5: Boundary preservation conditions")

    x, u = sp.symbols("x u", real=True)

    pressure_shape = u*(1-x**2)/4
    kappa_shape = -3*u*(1-x**2)/4
    A_residual_shape = 3*u**2*(1-x**2)**2/16

    print(f"pressure leading shape ~ {pressure_shape}")
    print(f"kappa leading GR diagnostic shape ~ {kappa_shape}")
    print(f"A residual leading shape ~ {A_residual_shape}")
    print()
    print(f"pressure at boundary = {sp.simplify(pressure_shape.subs(x, 1))}")
    print(f"kappa at boundary = {sp.simplify(kappa_shape.subs(x, 1))}")
    print(f"A residual at boundary = {sp.simplify(A_residual_shape.subs(x, 1))}")
    print(f"A residual derivative at boundary = {sp.simplify(sp.diff(A_residual_shape, x).subs(x, 1))}")

    status_line("pressure-like corrections vanish at boundary", is_zero(pressure_shape.subs(x, 1)))
    status_line("kappa-like corrections vanish at boundary", is_zero(kappa_shape.subs(x, 1)))
    status_line("A residual is boundary-smooth", is_zero(sp.diff(A_residual_shape, x).subs(x, 1)))

    print()
    print("Interpretation:")
    print("  Interior pressure/stress corrections can be boundary-contained.")
    print("  This lets exterior A-flux and kappa=0 remain intact.")


def case_6_channel_classification():
    header("Case 6: Source-channel classification")

    print("Candidate source channels:")
    print()
    print("1. Density -> A-flux")
    print("   F_A = 8*pi*G*M_enc/c^2")
    print("   controls exterior mass field")
    print()
    print("2. Pressure/stress -> interior kappa")
    print("   traceful matter response")
    print("   should vanish or relax at boundary")
    print()
    print("3. Pressure/self-field -> second-order A residual")
    print("   interior-supported correction")
    print("   boundary-smooth so exterior Schwarzschild remains")
    print()
    print("4. Exterior source-free vacuum")
    print("   kappa -> 0")
    print("   A-flux conserved")
    print("   B = 1/A")
    print()
    status_line("source-channel map separated", True)


def final_interpretation():
    header("Final interpretation")

    print("Pressure/stress likely belongs to the interior problem, not the")
    print("ordinary exterior mass-flux law.")
    print()
    print("The cleanest current hypothesis is:")
    print()
    print("  density / total mass fixes exterior A-flux,")
    print("  pressure and stress source interior kappa and/or boundary-smooth")
    print("  second-order A corrections,")
    print("  source-free exterior suppresses kappa and conserves A-flux.")
    print()
    print("Possible next artifact:")
    print("  candidate_pressure_stress_source_extension.md")


def main():
    header("Candidate Pressure/Stress Source Extension")
    case_0_problem_statement()
    case_1_gr_pressure_profile_weak_order()
    case_2_A_residual_vs_pressure_shape()
    case_3_pressure_direct_A_flux_hypothesis()
    case_4_pressure_as_kappa_source_hypothesis()
    case_5_boundary_preservation_conditions()
    case_6_channel_classification()
    final_interpretation()


if __name__ == "__main__":
    main()
