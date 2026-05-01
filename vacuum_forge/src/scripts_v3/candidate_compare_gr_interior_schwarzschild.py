# Candidate compare GR interior Schwarzschild
#
# Purpose
# -------
# Compare the reduced constant-density interior A model to the exact GR
# interior Schwarzschild solution for a uniform-density sphere.
#
# This is a diagnostic comparison, not an attempt to derive GR.
#
# Reduced areal-flux interior:
#
#   A_red(r) = 1 - 4*pi*G*rho0*R^2/c^2 + 4*pi*G*rho0*r^2/(3*c^2)
#
# GR interior Schwarzschild lapse factor:
#
#   A_GR(r) = [1/4] [3 sqrt(1-r_s/R) - sqrt(1-r_s*r^2/R^3)]^2
#
# with:
#
#   r_s = 2GM/c^2
#   M = (4*pi/3) rho0 R^3
#
# Exterior boundary:
#   A_GR(R) = A_red(R) = 1-r_s/R
#
# Weak-field:
#   A_GR and A_red agree at first order in compactness.
#
# Suggested location:
#   scripts_v3/candidate_compare_gr_interior_schwarzschild.py

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


def series(expr, var, order=3):
    return sp.series(expr, var, 0, order).removeO()


def case_0_define_models():
    header("Case 0: Define reduced and GR interior models")

    x, u = sp.symbols("x u", real=True)

    # Dimensionless radius x=r/R.
    # Compactness u = r_s/R = 2GM/(c^2 R).
    A_red = 1 - sp.Rational(3, 2)*u + sp.Rational(1, 2)*u*x**2
    A_gr = sp.Rational(1, 4) * (3*sp.sqrt(1-u) - sp.sqrt(1-u*x**2))**2
    A_ext_boundary = 1 - u

    print("Dimensionless variables:")
    print("  x = r/R")
    print("  u = r_s/R = 2GM/(c²R)")
    print()
    print(f"A_red(x) = {A_red}")
    print(f"A_GR(x)  = {A_gr}")
    print(f"A_boundary = {A_ext_boundary}")

    status_line("both models match exterior A at x=1",
                is_zero(A_red.subs(x, 1) - A_ext_boundary)
                and is_zero(A_gr.subs(x, 1) - A_ext_boundary))

    return x, u, A_red, A_gr


def case_1_boundary_derivatives(x, u, A_red, A_gr):
    header("Case 1: Boundary derivative comparison")

    d_red = sp.diff(A_red, x)
    d_gr = sp.simplify(sp.diff(A_gr, x))

    d_red_1 = sp.simplify(d_red.subs(x, 1))
    d_gr_1 = sp.simplify(d_gr.subs(x, 1))

    print(f"dA_red/dx = {d_red}")
    print(f"dA_GR/dx  = {d_gr}")
    print()
    print(f"dA_red/dx at x=1 = {d_red_1}")
    print(f"dA_GR/dx at x=1  = {d_gr_1}")

    status_line("boundary derivatives match", is_zero(d_red_1 - d_gr_1))


def case_2_weak_field_series(x, u, A_red, A_gr):
    header("Case 2: Weak-field compactness series")

    A_gr_series = sp.simplify(series(A_gr, u, 3))
    A_red_series = sp.simplify(series(A_red, u, 3))
    diff_series = sp.simplify(series(A_gr - A_red, u, 3))

    print(f"A_red series = {A_red_series}")
    print(f"A_GR series  = {A_gr_series}")
    print(f"A_GR - A_red through u² = {diff_series}")

    first_order_diff = sp.simplify(series(A_gr - A_red, u, 2))
    second_order_diff = sp.simplify(series(A_gr - A_red, u, 3))

    status_line("models agree through first order in compactness", is_zero(first_order_diff))
    status_line("models differ at second order", not is_zero(second_order_diff))


def case_3_residual_shape(x, u, A_red, A_gr):
    header("Case 3: Residual shape")

    residual = sp.simplify(A_gr - A_red)
    residual_series = sp.simplify(series(residual, u, 4))

    print(f"Residual exact = {residual}")
    print(f"Residual series through u³ = {residual_series}")

    center_residual = sp.simplify(residual.subs(x, 0))
    boundary_residual = sp.simplify(residual.subs(x, 1))

    print()
    print(f"Residual at center x=0 = {center_residual}")
    print(f"Residual at boundary x=1 = {boundary_residual}")

    status_line("residual vanishes at boundary", is_zero(boundary_residual))
    status_line("residual is generally nonzero inside", not is_zero(center_residual))


def case_4_center_values(x, u, A_red, A_gr):
    header("Case 4: Center lapse comparison")

    A_red_0 = sp.simplify(A_red.subs(x, 0))
    A_gr_0 = sp.simplify(A_gr.subs(x, 0))

    print(f"A_red(0) = {A_red_0}")
    print(f"A_GR(0)  = {A_gr_0}")
    print()
    print(f"A_red(0) series = {series(A_red_0, u, 4)}")
    print(f"A_GR(0) series  = {series(A_gr_0, u, 4)}")
    print(f"center difference series = {series(A_gr_0 - A_red_0, u, 4)}")

    status_line("center values agree at first order", is_zero(series(A_gr_0 - A_red_0, u, 2)))
    status_line("center values differ beyond first order", not is_zero(series(A_gr_0 - A_red_0, u, 4)))


def case_5_B_comparison():
    header("Case 5: Radial metric comparison")

    x, u = sp.symbols("x u", real=True)

    A_red = 1 - sp.Rational(3, 2)*u + sp.Rational(1, 2)*u*x**2
    B_red = sp.simplify(1/A_red)

    # GR constant-density interior radial metric:
    B_gr = sp.simplify(1 / (1 - u*x**2))

    print(f"B_red = 1/A_red = {B_red}")
    print(f"B_GR  = {B_gr}")

    diff_series = sp.simplify(series(B_gr - B_red, u, 3))
    print(f"B_GR - B_red through u² = {diff_series}")

    status_line("B differs already at first order generically",
                not is_zero(series(B_gr - B_red, u, 2)))

    print()
    print("Interpretation:")
    print("  Forcing kappa=0 inside gives B_red=1/A_red.")
    print("  GR interior does not generally have AB=1 inside matter.")


def case_6_kappa_gr_inside():
    header("Case 6: GR interior kappa diagnostic")

    x, u = sp.symbols("x u", real=True)

    A_gr = sp.Rational(1, 4) * (3*sp.sqrt(1-u) - sp.sqrt(1-u*x**2))**2
    B_gr = 1 / (1 - u*x**2)

    AB_gr = sp.simplify(A_gr * B_gr)
    kappa_gr = sp.simplify(sp.Rational(1, 2) * sp.log(AB_gr))

    print(f"A_GR * B_GR = {AB_gr}")
    print(f"kappa_GR = 1/2 ln(A_GR B_GR) = {kappa_gr}")

    AB_boundary = sp.simplify(AB_gr.subs(x, 1))
    AB_series = sp.simplify(series(AB_gr, u, 3))

    print()
    print(f"A_GR B_GR at x=1 = {AB_boundary}")
    print(f"A_GR B_GR series = {AB_series}")

    status_line("GR interior has AB=1 at boundary", is_zero(AB_boundary - 1))
    status_line("GR interior does not generally have AB=1 inside", not is_zero(AB_gr - 1))


def final_interpretation():
    header("Final interpretation")

    print("The reduced interior A model and GR interior Schwarzschild agree")
    print("at the exterior boundary and at first weak-field order for A.")
    print()
    print("They differ at higher order inside the source.")
    print()
    print("The largest structural difference is that the reduced model, when")
    print("forced to kappa=0 inside, has B=1/A everywhere.")
    print()
    print("The GR interior Schwarzschild solution does not generally have AB=1")
    print("inside matter, although AB=1 is recovered at the exterior boundary.")
    print()
    print("Interpretation:")
    print("  kappa=0 may be an exterior/source-free condition, not an interior")
    print("  matter condition.")
    print()
    print("Possible next artifact:")
    print("  candidate_compare_gr_interior_schwarzschild.md")


def main():
    header("Candidate Compare GR Interior Schwarzschild")
    x, u, A_red, A_gr = case_0_define_models()
    case_1_boundary_derivatives(x, u, A_red, A_gr)
    case_2_weak_field_series(x, u, A_red, A_gr)
    case_3_residual_shape(x, u, A_red, A_gr)
    case_4_center_values(x, u, A_red, A_gr)
    case_5_B_comparison()
    case_6_kappa_gr_inside()
    final_interpretation()


if __name__ == "__main__":
    main()
