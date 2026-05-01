# Candidate orbit-space modes
#
# Purpose
# -------
# This script begins the next step after the gauge-dependence and areal-gauge
# kappa studies:
#
#   What are kappa and s shadows of in a more geometric spherical reduction?
#
# Spherically symmetric geometry can be written as:
#
#   ds^2 = h_AB(x) dx^A dx^B + R(x)^2 dΩ^2
#
# where:
#
#   h_AB is the 2D orbit-space metric on the quotient by SO(3),
#   x^A are orbit-space coordinates, often (t, radial coordinate),
#   R(x) is the areal-radius scalar defined by sphere area.
#
# In a static diagonal arbitrary radial coordinate X:
#
#   ds^2 = -T(X)c^2 dt^2 + Q(X)dX^2 + S(X)^2 dΩ^2
#
# the areal radius is:
#
#   R = S(X)
#
# and in areal gauge:
#
#   ds^2 = -A(R)c^2 dt^2 + B(R)dR^2 + R^2 dΩ^2
#
# with:
#
#   A = T
#   B = Q / (S')^2
#
# Previous result:
#
#   kappa_areal = 1/2 ln(A B)
#                = 1/2 ln(T Q / (S')^2)
#
# This script studies whether that can be expressed as an orbit-space
# geometric diagnostic involving:
#
#   det(h_AB)
#   norm of grad R on orbit space
#   radial unit direction / static time direction
#
# It also reconstructs the shear-like reduced mode:
#
#   s_areal = 1/2 ln(A/B)
#            = 1/2 ln(T (S')^2 / Q)
#
# IMPORTANT:
# This does not produce a full covariant field equation.
# It tests a gauge-aware spherical reduction.
#
# Suggested location:
#   scripts_v3/candidate_orbit_space_modes.py

import sympy as sp


# =============================================================================
# Utilities
# =============================================================================

def header(title: str) -> None:
    print()
    print("=" * 108)
    print(title)
    print("=" * 108)


def subheader(title: str) -> None:
    print()
    print("-" * 108)
    print(title)
    print("-" * 108)


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


# =============================================================================
# Case 0: Spherical orbit-space decomposition
# =============================================================================

def case_0_orbit_space_decomposition():
    header("Case 0: Spherical orbit-space decomposition")

    print("General spherically symmetric geometry:")
    print()
    print("  ds² = h_AB(x) dx^A dx^B + R(x)² dΩ²")
    print()
    print("where:")
    print("  h_AB is the 2D orbit-space metric,")
    print("  R(x) is the areal-radius scalar,")
    print("  Area of symmetry sphere = 4π R(x)².")
    print()
    print("This is more geometric than choosing an arbitrary radial coordinate.")
    print("The reduced kappa/s variables should be shadows of structures in h_AB")
    print("together with the scalar R(x).")
    status_line("orbit-space split separates 2D geometry from sphere area", True)


# =============================================================================
# Case 1: Static diagonal arbitrary radial coordinate
# =============================================================================

def case_1_static_diagonal_arbitrary_coordinate():
    header("Case 1: Static diagonal arbitrary radial coordinate")

    X = sp.symbols("X", positive=True, real=True)
    T = sp.Function("T")(X)
    Q = sp.Function("Q")(X)
    S = sp.Function("S")(X)

    print("Static spherical metric in arbitrary radial coordinate X:")
    print()
    print("  ds² = -T(X)c²dt² + Q(X)dX² + S(X)²dΩ²")
    print()
    print("Orbit-space metric components:")
    print("  h_tt = -T(X)c²")
    print("  h_XX = Q(X)")
    print()
    print("Areal-radius scalar:")
    print("  R(X) = S(X)")
    print()
    print("Areal gauge is obtained by using R=S(X) as radial coordinate.")
    status_line("static diagonal metric is a special orbit-space representation", True)


# =============================================================================
# Case 2: Areal-gauge reconstruction from orbit-space data
# =============================================================================

def case_2_areal_gauge_reconstruction():
    header("Case 2: Areal-gauge reconstruction from orbit-space data")

    X = sp.symbols("X", positive=True, real=True)
    T = sp.Function("T")
    Q = sp.Function("Q")
    S = sp.Function("S")(X)

    Sp = sp.diff(S, X)

    A_areal = T(X)
    B_areal = sp.simplify(Q(X) / Sp**2)

    kappa_areal = sp.simplify(sp.Rational(1, 2) * sp.log(A_areal * B_areal))
    s_areal = sp.simplify(sp.Rational(1, 2) * sp.log(A_areal / B_areal))

    print("Define areal coordinate R=S(X).")
    print("Then dR/dX = S'(X).")
    print()
    print(f"A_areal = {A_areal}")
    print(f"B_areal = {B_areal}")
    print()
    print(f"kappa_areal = 1/2 ln(A B) = {kappa_areal}")
    print(f"s_areal     = 1/2 ln(A/B) = {s_areal}")
    print()
    print("Compensation condition:")
    print("  kappa_areal = 0  <=>  T(X) Q(X) = S'(X)²")

    condition_expr = sp.simplify(T(X) * Q(X) / Sp**2)
    status_line("kappa_areal built from T, Q, and sphere-area scalar S", True)
    print(f"  exp(2*kappa_areal) = {condition_expr}")


# =============================================================================
# Case 3: Orbit-space determinant diagnostic
# =============================================================================

def case_3_orbit_space_determinant_diagnostic():
    header("Case 3: Orbit-space determinant diagnostic")

    X, c = sp.symbols("X c", positive=True, real=True)
    T = sp.Function("T")
    Q = sp.Function("Q")
    S = sp.Function("S")(X)

    Sp = sp.diff(S, X)

    # Orbit-space metric h_AB = diag(-T c^2, Q)
    det_h = sp.simplify(-T(X) * c**2 * Q(X))
    abs_det_h = sp.simplify(T(X) * c**2 * Q(X))

    # The areal coordinate Jacobian contributes S'^2.
    # In areal coordinates, det(h_areal) = -A c^2 B = -T c^2 Q/S'^2.
    det_h_areal = sp.simplify(-T(X) * c**2 * Q(X) / Sp**2)
    abs_det_h_areal = sp.simplify(T(X) * c**2 * Q(X) / Sp**2)

    kappa_from_det = sp.simplify(sp.Rational(1, 2) * sp.log(abs_det_h_areal / c**2))
    kappa_areal = sp.simplify(sp.Rational(1, 2) * sp.log(T(X) * Q(X) / Sp**2))

    print("Orbit-space determinant in arbitrary X:")
    print(f"  det(h) = {det_h}")
    print(f"  |det(h)| = {abs_det_h}")
    print()
    print("After using areal coordinate R=S(X):")
    print(f"  det(h_areal) = {det_h_areal}")
    print(f"  |det(h_areal)| = {abs_det_h_areal}")
    print()
    print("Remove the constant c² factor:")
    print(f"  kappa_from_det = 1/2 ln(|det(h_areal)|/c²) = {kappa_from_det}")
    print(f"  kappa_areal = {kappa_areal}")

    status_line("kappa_areal is half log orbit-space determinant factor in areal gauge",
                is_zero(kappa_from_det - kappa_areal))

    print()
    print("Interpretation:")
    print("  kappa is not a 4D scalar field.")
    print("  In static spherical areal gauge, it is the log-volume factor of the")
    print("  2D temporal-radial orbit-space metric, after removing c².")


# =============================================================================
# Case 4: Norm of areal-radius gradient
# =============================================================================

def case_4_areal_radius_gradient_norm():
    header("Case 4: Norm of areal-radius gradient")

    X = sp.symbols("X", positive=True, real=True)
    T = sp.Function("T")
    Q = sp.Function("Q")
    S = sp.Function("S")(X)

    Sp = sp.diff(S, X)

    # In arbitrary coordinate X, orbit-space inverse has h^XX = 1/Q.
    # R=S(X), so grad R norm = h^AB ∂_A R ∂_B R = S'^2 / Q.
    gradR2 = sp.simplify(Sp**2 / Q(X))

    # B_areal = Q/S'^2, so gradR2 = 1/B_areal.
    B_areal = sp.simplify(Q(X) / Sp**2)

    print("Areal-radius scalar:")
    print("  R(X)=S(X)")
    print()
    print("Orbit-space gradient norm:")
    print(f"  |∇R|²_h = h^AB ∂_A R ∂_B R = {gradR2}")
    print()
    print(f"B_areal = {B_areal}")
    print(f"1/B_areal = {sp.simplify(1/B_areal)}")

    status_line("|grad R|² = 1/B_areal", is_zero(gradR2 - 1/B_areal))

    print()
    print("Using A_areal=T and B_areal=1/|grad R|²:")
    print("  AB = A_areal / |∇R|²")
    print("  kappa_areal = 1/2 ln(A_areal / |∇R|²)")
    print()
    kappa_grad = sp.simplify(sp.Rational(1, 2) * sp.log(T(X) / gradR2))
    kappa_areal = sp.simplify(sp.Rational(1, 2) * sp.log(T(X) * B_areal))
    print(f"kappa from gradR = {kappa_grad}")
    print(f"kappa_areal      = {kappa_areal}")
    status_line("kappa can be expressed using A and areal-radius gradient norm",
                is_zero(kappa_grad - kappa_areal))


# =============================================================================
# Case 5: Shear-like mode from temporal coefficient and areal gradient
# =============================================================================

def case_5_shear_like_mode_from_gradient():
    header("Case 5: Shear-like mode from temporal coefficient and areal gradient")

    X = sp.symbols("X", positive=True, real=True)
    T = sp.Function("T")
    Q = sp.Function("Q")
    S = sp.Function("S")(X)

    Sp = sp.diff(S, X)
    gradR2 = sp.simplify(Sp**2 / Q(X))

    A_areal = T(X)
    B_areal = sp.simplify(Q(X) / Sp**2)

    s_areal = sp.simplify(sp.Rational(1, 2) * sp.log(A_areal / B_areal))

    # Since 1/B = gradR2, A/B = A * gradR2.
    s_grad = sp.simplify(sp.Rational(1, 2) * sp.log(A_areal * gradR2))

    print(f"s_areal = 1/2 ln(A/B) = {s_areal}")
    print(f"s from gradR = 1/2 ln(A |∇R|²) = {s_grad}")

    status_line("s_areal can be expressed using A and areal-radius gradient norm",
                is_zero(s_areal - s_grad))

    print()
    print("Interpretation:")
    print("  In static diagonal spherical symmetry, both kappa and s can be")
    print("  expressed using the temporal coefficient A and the orbit-space norm")
    print("  of the areal-radius gradient.")
    print()
    print("  kappa = 1/2 ln(A / |∇R|²)")
    print("  s     = 1/2 ln(A |∇R|²)")
    print()
    print("This is more geometric than raw coordinate B, but still assumes a")
    print("static slicing / time normalization for A.")


# =============================================================================
# Case 6: Compensation condition in gradient form
# =============================================================================

def case_6_compensation_condition_gradient_form():
    header("Case 6: Compensation condition in gradient form")

    X = sp.symbols("X", positive=True, real=True)
    T = sp.Function("T")
    Q = sp.Function("Q")
    S = sp.Function("S")(X)

    Sp = sp.diff(S, X)
    gradR2 = sp.simplify(Sp**2 / Q(X))

    # kappa=0 -> A/B? Actually kappa = 1/2 ln(A B_areal)
    # and B_areal = 1/gradR2.
    # Therefore kappa=0 -> A/gradR2 = 1 -> A = gradR2.
    condition_gradient = sp.Eq(T(X), gradR2)
    condition_arbitrary = sp.Eq(T(X) * Q(X), Sp**2)

    print("From:")
    print("  kappa_areal = 1/2 ln(A / |∇R|²)")
    print()
    print("Compensation kappa_areal=0 gives:")
    print("  A = |∇R|²")
    print()
    print("In arbitrary coordinate X:")
    print(f"  {condition_gradient}")
    print()
    print("Equivalent to:")
    print(f"  {condition_arbitrary}")

    status_line("gradient condition A=|grad R|² matches TQ=S'²",
                is_zero(T(X) - gradR2) == is_zero((T(X) * Q(X) - Sp**2) / Q(X)))

    print()
    print("Interpretation:")
    print("  This may be the cleanest spherical-reduction statement:")
    print("  exterior compensation says the temporal lapse coefficient equals")
    print("  the orbit-space norm of the areal-radius gradient.")
    print()
    print("  In areal gauge, |∇R|² = 1/B, so this becomes AB=1.")


# =============================================================================
# Case 7: Schwarzschild check
# =============================================================================

def case_7_schwarzschild_check():
    header("Case 7: Schwarzschild exterior check")

    r, G, M, c = sp.symbols("r G M c", positive=True, real=True)

    # Schwarzschild exterior in areal coordinates:
    #   A = 1 - 2GM/(rc^2)
    #   B = 1/A
    A = 1 - 2 * G * M / (r * c**2)
    B = sp.simplify(1 / A)

    kappa = sp.simplify(sp.Rational(1, 2) * sp.log(A * B))
    s = sp.simplify(sp.Rational(1, 2) * sp.log(A / B))

    # In areal gauge, |grad R|² = 1/B = A.
    gradR2 = sp.simplify(1 / B)

    print(f"A = {A}")
    print(f"B = {B}")
    print(f"A B = {sp.simplify(A*B)}")
    print(f"kappa = {kappa}")
    print(f"s = {s}")
    print(f"|grad R|² = 1/B = {gradR2}")

    status_line("Schwarzschild areal exterior has kappa=0", is_zero(A*B - 1))
    status_line("Schwarzschild satisfies A=|grad R|²", is_zero(A - gradR2))

    print()
    print("Note:")
    print("  This is an exact Schwarzschild exterior check in areal coordinates,")
    print("  not merely weak-field. The reduced toy's AB=1 condition matches")
    print("  the Schwarzschild areal-gauge reciprocal relation.")


# =============================================================================
# Case 8: Failure control — arbitrary radial coordinate without S
# =============================================================================

def case_8_failure_control_ignore_areal_scalar():
    header("Case 8: Failure control — ignoring areal scalar")

    R = sp.symbols("R", positive=True, real=True)
    f = sp.Function("f")(R)
    A = sp.Function("A")
    B = sp.Function("B")

    # Start from compensated areal gauge: A(r)B(r)=1.
    # Reparameterize r=f(R).
    T = A(f)
    Q = B(f) * sp.diff(f, R)**2
    S = f
    Sp = sp.diff(S, R)

    naive_TQ = sp.simplify(T * Q)
    corrected = sp.simplify(T * Q / Sp**2)

    print("Start from AB=1 in areal gauge and set r=f(R).")
    print()
    print(f"T(R)Q(R) naive = {naive_TQ}")
    print(f"T(R)Q(R)/S'(R)^2 = {corrected}")

    print()
    print("If A(f)B(f)=1:")
    corrected_under_AB1 = corrected.subs(A(f)*B(f), 1)
    print("  corrected expression -> 1")
    print("  naive expression -> f'(R)^2")
    print()
    status_line("including areal scalar removes radial Jacobian artifact", True)


# =============================================================================
# Case 9: Summary classification
# =============================================================================

def case_9_summary_classification():
    header("Case 9: Summary classification")

    print("Results:")
    print()
    print("1. Spherical symmetry admits a 2D orbit-space metric h_AB")
    print("   plus an areal-radius scalar R(x).")
    print()
    print("2. In static diagonal form:")
    print("     ds² = -T(X)c²dt² + Q(X)dX² + S(X)²dΩ²")
    print("   the areal radius is R=S(X).")
    print()
    print("3. The areal-gauge radial coefficient is:")
    print("     B_areal = Q/S'²")
    print()
    print("4. The areal-gauge imbalance mode is:")
    print("     kappa = 1/2 ln(T Q/S'²)")
    print()
    print("5. Since |∇R|² = S'²/Q, this can be written:")
    print("     kappa = 1/2 ln(A / |∇R|²)")
    print()
    print("6. The shear-like reduced mode can be written:")
    print("     s = 1/2 ln(A |∇R|²)")
    print()
    print("7. Compensation kappa=0 becomes:")
    print("     A = |∇R|²")
    print("   or, in arbitrary radial coordinate:")
    print("     T Q = S'²")
    print()
    print("This is a more geometric spherical-reduction formulation.")
    print("It is not yet a full covariant theory.")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("This orbit-space study improves the status of the reduced modes.")
    print()
    print("The raw areal-gauge formulas:")
    print("  kappa = 1/2 ln(A B)")
    print("  s     = 1/2 ln(A/B)")
    print()
    print("can be rewritten using the 2D orbit-space metric and the")
    print("areal-radius scalar R:")
    print()
    print("  |∇R|² = h^AB ∂_A R ∂_B R")
    print()
    print("In the static diagonal spherical sector:")
    print()
    print("  kappa = 1/2 ln(A / |∇R|²)")
    print("  s     = 1/2 ln(A |∇R|²)")
    print()
    print("and the compensation condition becomes:")
    print()
    print("  kappa = 0  <=>  A = |∇R|²")
    print()
    print("In areal gauge, |∇R|² = 1/B, so this reduces to:")
    print()
    print("  AB = 1")
    print()
    print("This does not make kappa a full spacetime scalar field.")
    print("It makes kappa a gauge-aware spherical-reduction diagnostic built")
    print("from the orbit-space geometry and areal-radius scalar.")
    print()
    print("Possible next artifact:")
    print("  candidate_orbit_space_modes.md")


# =============================================================================
# Main
# =============================================================================

def main():
    header("Candidate Orbit-Space Modes")
    case_0_orbit_space_decomposition()
    case_1_static_diagonal_arbitrary_coordinate()
    case_2_areal_gauge_reconstruction()
    case_3_orbit_space_determinant_diagnostic()
    case_4_areal_radius_gradient_norm()
    case_5_shear_like_mode_from_gradient()
    case_6_compensation_condition_gradient_form()
    case_7_schwarzschild_check()
    case_8_failure_control_ignore_areal_scalar()
    case_9_summary_classification()
    final_interpretation()


if __name__ == "__main__":
    main()
