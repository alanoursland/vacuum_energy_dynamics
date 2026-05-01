# Candidate GR residual as kappa response
#
# Purpose
# -------
# The reduced constant-density interior A model matches GR interior
# Schwarzschild at the boundary and through first weak-field order, but
# differs at second order inside matter.
#
# The GR interior Schwarzschild solution also generally has:
#
#   A_GR B_GR != 1
#
# inside matter, while:
#
#   A_GR B_GR = 1
#
# at the exterior boundary.
#
# This script asks whether the missing interior structure can be represented
# as an effective interior kappa profile:
#
#   kappa_GR(r) = 1/2 ln(A_GR B_GR)
#
# using dimensionless variables:
#
#   x = r/R
#   u = r_s/R = 2GM/(c^2 R)
#
# Main tests:
#
#   1. kappa_GR is generally nonzero inside.
#   2. kappa_GR(1)=0 at the boundary.
#   3. leading weak-field kappa_GR shape.
#   4. kappa_GR derivative at boundary.
#   5. whether the residual A_GR - A_red has the same boundary behavior.
#
# IMPORTANT:
# This is a diagnostic comparison to GR interior Schwarzschild, not a
# derivation of GR and not a commitment that the model must match GR exactly.
#
# Suggested location:
#   scripts_v3/candidate_gr_residual_as_kappa_response.py

import sympy as sp


def header(title: str) -> None:
    print()
    print("=" * 108)
    print(title)
    print("=" * 108)


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


def case_0_define_gr_kappa():
    header("Case 0: Define GR interior kappa diagnostic")

    x, u = sp.symbols("x u", real=True)

    A_gr = sp.Rational(1, 4) * (3*sp.sqrt(1-u) - sp.sqrt(1-u*x**2))**2
    B_gr = 1 / (1 - u*x**2)
    AB_gr = sp.simplify(A_gr * B_gr)
    kappa_gr = sp.simplify(sp.Rational(1, 2) * sp.log(AB_gr))

    print("Dimensionless variables:")
    print("  x = r/R")
    print("  u = r_s/R = 2GM/(c²R)")
    print()
    print(f"A_GR = {A_gr}")
    print(f"B_GR = {B_gr}")
    print(f"A_GR B_GR = {AB_gr}")
    print(f"kappa_GR = 1/2 ln(A_GR B_GR) = {kappa_gr}")

    status_line("GR interior has nontrivial AB diagnostic", not is_zero(AB_gr - 1))

    return x, u, A_gr, B_gr, AB_gr, kappa_gr


def case_1_boundary_behavior(x, u, AB_gr, kappa_gr):
    header("Case 1: Boundary behavior")

    AB_boundary = sp.simplify(AB_gr.subs(x, 1))
    kappa_boundary = sp.simplify(kappa_gr.subs(x, 1))

    dAB_boundary = sp.simplify(sp.diff(AB_gr, x).subs(x, 1))
    dkappa_boundary = sp.simplify(sp.diff(kappa_gr, x).subs(x, 1))

    print(f"A_GR B_GR at x=1 = {AB_boundary}")
    print(f"kappa_GR(1) = {kappa_boundary}")
    print(f"d/dx(A_GR B_GR)|1 = {dAB_boundary}")
    print(f"kappa_GR'(1) = {dkappa_boundary}")

    status_line("AB returns to 1 at boundary", is_zero(AB_boundary - 1))
    status_line("kappa returns to zero at boundary", is_zero(kappa_boundary))
    status_line("kappa derivative generally nonzero at boundary", not is_zero(dkappa_boundary))

    print()
    print("Interpretation:")
    print("  GR interior restores exterior compensation at the boundary,")
    print("  but the derivative can carry boundary/interface information.")


def case_2_weak_field_kappa_shape(x, u, AB_gr, kappa_gr):
    header("Case 2: Weak-field kappa shape")

    AB_series = series_u(AB_gr, u, 3)
    kappa_series = series_u(kappa_gr, u, 3)

    print(f"A_GR B_GR series through u² = {AB_series}")
    print(f"kappa_GR series through u² = {kappa_series}")

    leading_kappa = sp.simplify(series_u(kappa_gr, u, 2))
    second_order_kappa = sp.simplify(series_u(kappa_gr, u, 3))

    print()
    print(f"leading kappa = {leading_kappa}")
    print(f"through second order = {second_order_kappa}")

    status_line("kappa has first-order interior contribution", not is_zero(leading_kappa))
    status_line("kappa vanishes at boundary to this order",
                is_zero(sp.simplify(second_order_kappa.subs(x, 1))))


def case_3_center_behavior(x, u, kappa_gr):
    header("Case 3: Center behavior")

    kappa_center = sp.simplify(kappa_gr.subs(x, 0))
    dkappa_center = sp.simplify(sp.diff(kappa_gr, x).subs(x, 0))

    print(f"kappa_GR(0) = {kappa_center}")
    print(f"kappa_GR'(0) = {dkappa_center}")
    print(f"kappa_GR(0) series = {series_u(kappa_center, u, 4)}")

    status_line("kappa is regular at center", is_zero(dkappa_center))
    status_line("center kappa is generally nonzero", not is_zero(kappa_center))


def case_4_compare_A_residual(x, u, A_gr):
    header("Case 4: Compare A residual")

    A_red = 1 - sp.Rational(3, 2)*u + sp.Rational(1, 2)*u*x**2
    residual_A = sp.simplify(A_gr - A_red)

    residual_series = series_u(residual_A, u, 4)
    residual_boundary = sp.simplify(residual_A.subs(x, 1))
    dresidual_boundary = sp.simplify(sp.diff(residual_A, x).subs(x, 1))

    print(f"A_red = {A_red}")
    print(f"A_GR - A_red = {residual_A}")
    print(f"residual series through u³ = {residual_series}")
    print()
    print(f"residual at x=1 = {residual_boundary}")
    print(f"residual derivative at x=1 = {dresidual_boundary}")

    status_line("A residual vanishes at boundary", is_zero(residual_boundary))
    status_line("A residual derivative vanishes at boundary", is_zero(dresidual_boundary))

    print()
    print("Interpretation:")
    print("  The A-lapse residual is interior-supported and boundary-smooth.")
    print("  This makes it a plausible pressure/stress/interior-response correction.")


def case_5_effective_kappa_profile_fit(x, u, kappa_gr):
    header("Case 5: Toy effective kappa profile fit")

    eta = sp.symbols("eta", real=True)

    # Fit leading GR kappa to a simple shape eta*u*(1-x^2)
    kappa_leading = series_u(kappa_gr, u, 2)
    toy = eta * u * (1 - x**2)

    # Fit at center x=0.
    eta_solution = sp.solve(sp.Eq(toy.subs(x, 0), kappa_leading.subs(x, 0)), eta)
    toy_fit = sp.simplify(toy.subs(eta, eta_solution[0])) if eta_solution else toy

    print(f"kappa_GR leading = {kappa_leading}")
    print(f"toy profile = eta*u*(1-x²)")
    print(f"eta from center fit = {eta_solution}")
    print(f"toy fit = {toy_fit}")
    print(f"difference = {sp.simplify(kappa_leading - toy_fit)}")

    status_line("simple (1-x²) shape can capture leading kappa if fit succeeds",
                bool(eta_solution))


def case_6_interpretation_summary():
    header("Case 6: Interpretation summary")

    print("Results:")
    print()
    print("1. GR interior has A_GR B_GR != 1 inside matter.")
    print("2. Therefore kappa_GR = 1/2 ln(A_GR B_GR) is nonzero inside.")
    print("3. At the boundary x=1, A_GR B_GR = 1 and kappa_GR=0.")
    print("4. The derivative of kappa at the boundary can be nonzero.")
    print("5. The A residual relative to the reduced flux model is boundary-smooth.")
    print()
    print("Interpretation:")
    print("  This supports treating kappa=0 as an exterior/source-free condition,")
    print("  while matter interiors may carry traceful kappa response.")
    print()
    print("Possible next artifact:")
    print("  candidate_gr_residual_as_kappa_response.md")


def main():
    header("Candidate GR Residual as Kappa Response")
    x, u, A_gr, B_gr, AB_gr, kappa_gr = case_0_define_gr_kappa()
    case_1_boundary_behavior(x, u, AB_gr, kappa_gr)
    case_2_weak_field_kappa_shape(x, u, AB_gr, kappa_gr)
    case_3_center_behavior(x, u, kappa_gr)
    case_4_compare_A_residual(x, u, A_gr)
    case_5_effective_kappa_profile_fit(x, u, kappa_gr)
    case_6_interpretation_summary()


if __name__ == "__main__":
    main()
