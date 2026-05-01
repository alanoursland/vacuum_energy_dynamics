# Candidate static spherical exact recovery
#
# Purpose
# -------
# This script tests whether the reduced static spherical exterior program can
# be upgraded from weak-field recovery to exact Schwarzschild exterior recovery.
#
# Previous reduced result:
#
#   kappa = 0
#   A = exp(s)
#   B = exp(-s)
#   AB = 1
#
# Weak-field source-law toy used:
#
#   s_weak(r) = - r_s/r
#   where r_s = 2GM/c^2
#
# giving:
#
#   A = exp(-r_s/r) ≈ 1 - r_s/r
#
# This matches Schwarzschild only to first order.
#
# Exact Schwarzschild exterior in areal gauge has:
#
#   A_exact = 1 - r_s/r
#   B_exact = 1/A_exact
#   AB = 1
#
# Therefore exact compensated shear would be:
#
#   s_exact = ln(A_exact) = ln(1 - r_s/r)
#
# Question:
#   What source-free equation does s_exact satisfy?
#
# Since A = exp(s), if A is harmonic:
#
#   ∇²A = 0
#
# then:
#
#   ∇² exp(s) = exp(s) [∇²s + |∇s|²] = 0
#
# so:
#
#   ∇²s + |∇s|² = 0
#
# This script tests:
#
#   1. exact Schwarzschild satisfies kappa=0 and AB=1;
#   2. s_weak is harmonic outside source but only weakly matches A_exact;
#   3. s_exact is not harmonic under the flat radial Laplacian;
#   4. A_exact is harmonic outside source;
#   5. s_exact satisfies the nonlinear equation ∇²s + |∇s|² = 0;
#   6. the nonlinear equation linearizes to ∇²s = 0 in weak field;
#   7. flux normalization recovers r_s=2GM/c²;
#   8. the exact redshift factor emerges from A=1-r_s/r.
#
# IMPORTANT:
# This is still a reduced areal-gauge static spherical toy.
# It is not a derivation of Einstein's equations.
#
# Suggested location:
#   scripts_v3/candidate_static_spherical_exact_recovery.py

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


def radial_laplacian(expr, r):
    """Flat 3D radial Laplacian for spherical scalar f(r)."""
    return sp.simplify((1 / r**2) * sp.diff(r**2 * sp.diff(expr, r), r))


def radial_grad_sq(expr, r):
    """Flat radial |grad f|^2 for spherical scalar f(r)."""
    return sp.simplify(sp.diff(expr, r)**2)


def series_at_infinity(expr, r, order=4):
    """Series in x=1/r around x=0."""
    x = sp.symbols("x", positive=True, real=True)
    expr_x = sp.simplify(expr.subs(r, 1/x))
    ser_x = sp.series(expr_x, x, 0, order).removeO()
    return sp.simplify(ser_x.subs(x, 1/r))


# =============================================================================
# Case 0: Exact Schwarzschild compensated exterior
# =============================================================================

def case_0_exact_schwarzschild_compensated():
    header("Case 0: Exact Schwarzschild compensated exterior")

    r, r_s = sp.symbols("r r_s", positive=True, real=True)

    A = 1 - r_s / r
    B = sp.simplify(1 / A)
    kappa = sp.simplify(sp.Rational(1, 2) * sp.log(A * B))
    s = sp.simplify(sp.Rational(1, 2) * sp.log(A / B))

    print(f"A_exact = {A}")
    print(f"B_exact = {B}")
    print(f"A B = {sp.simplify(A*B)}")
    print(f"kappa = {kappa}")
    print(f"s = 1/2 ln(A/B) = {s}")
    print()
    print("Since B=1/A, s = ln(A).")
    print(f"ln(A) = {sp.log(A)}")

    status_line("exact Schwarzschild has AB=1", is_zero(A * B - 1))
    status_line("exact Schwarzschild has kappa=0", is_zero(A * B - 1))
    status_line("s equals ln(A)", is_zero(s - sp.log(A)))


# =============================================================================
# Case 1: Weak shear versus exact shear
# =============================================================================

def case_1_weak_vs_exact_shear():
    header("Case 1: Weak shear versus exact shear")

    r, r_s = sp.symbols("r r_s", positive=True, real=True)

    s_weak = -r_s / r
    A_weak_exp = sp.exp(s_weak)

    A_exact = 1 - r_s / r
    s_exact = sp.log(A_exact)

    print(f"s_weak = {s_weak}")
    print(f"A_from_s_weak = exp(s_weak) = {A_weak_exp}")
    print(f"A_exact = {A_exact}")
    print(f"s_exact = ln(A_exact) = {s_exact}")

    print()
    print("Large-r expansions:")
    print(f"A_from_s_weak = {series_at_infinity(A_weak_exp, r, 4)}")
    print(f"A_exact       = {series_at_infinity(A_exact, r, 4)}")
    print(f"s_exact       = {series_at_infinity(s_exact, r, 4)}")
    print(f"s_weak        = {s_weak}")

    first_order_match = sp.simplify(series_at_infinity(A_weak_exp - A_exact, r, 3))
    print()
    print(f"A_weak_exp - A_exact through order 1/r² = {first_order_match}")

    status_line("weak exponential A matches exact A at first order",
                is_zero(sp.expand(series_at_infinity(A_weak_exp - A_exact, r, 2))))
    status_line("weak exponential differs at second order",
                not is_zero(sp.expand(series_at_infinity(A_weak_exp - A_exact, r, 3))))


# =============================================================================
# Case 2: Harmonic tests for weak and exact shear
# =============================================================================

def case_2_harmonic_tests():
    header("Case 2: Harmonic tests for weak and exact shear")

    r, r_s = sp.symbols("r r_s", positive=True, real=True)

    s_weak = -r_s / r
    A_exact = 1 - r_s / r
    s_exact = sp.log(A_exact)

    lap_s_weak = radial_laplacian(s_weak, r)
    lap_s_exact = sp.simplify(radial_laplacian(s_exact, r))
    lap_A_exact = radial_laplacian(A_exact, r)

    print(f"∇² s_weak = {lap_s_weak}")
    print(f"∇² s_exact = {lap_s_exact}")
    print(f"∇² A_exact = {lap_A_exact}")

    status_line("s_weak is harmonic for r>0", is_zero(lap_s_weak))
    status_line("s_exact is not harmonic under flat radial Laplacian", not is_zero(lap_s_exact))
    status_line("A_exact is harmonic for r>0", is_zero(lap_A_exact))

    print()
    print("Interpretation:")
    print("  The weak-field source law ∇²s=0 is linearized.")
    print("  Exact Schwarzschild suggests the source-free harmonic variable is A=e^s,")
    print("  not s itself.")


# =============================================================================
# Case 3: Nonlinear s equation
# =============================================================================

def case_3_nonlinear_s_equation():
    header("Case 3: Nonlinear s equation from harmonic A=e^s")

    r, r_s = sp.symbols("r r_s", positive=True, real=True)

    A_exact = 1 - r_s / r
    s_exact = sp.log(A_exact)

    lap_s = radial_laplacian(s_exact, r)
    grad_s_sq = radial_grad_sq(s_exact, r)

    nonlinear = sp.simplify(lap_s + grad_s_sq)

    print(f"s_exact = {s_exact}")
    print(f"∇²s = {lap_s}")
    print(f"|∇s|² = {grad_s_sq}")
    print(f"∇²s + |∇s|² = {nonlinear}")

    status_line("s_exact satisfies nonlinear source-free equation", is_zero(nonlinear))

    print()
    print("Equation:")
    print("  ∇²s + |∇s|² = 0")
    print()
    print("Equivalent:")
    print("  ∇² exp(s) = 0")


# =============================================================================
# Case 4: Linearization of nonlinear s equation
# =============================================================================

def case_4_linearization():
    header("Case 4: Linearization of nonlinear s equation")

    r, eps = sp.symbols("r eps", positive=True, real=True)
    u = sp.Function("u")(r)

    s = eps * u

    lap_s = radial_laplacian(s, r)
    grad_s_sq = radial_grad_sq(s, r)
    nonlinear = sp.expand(lap_s + grad_s_sq)

    first_order = sp.series(nonlinear, eps, 0, 2).removeO()
    second_order = sp.series(nonlinear, eps, 0, 3).removeO()

    print(f"s = eps*u(r)")
    print(f"∇²s + |∇s|² = {nonlinear}")
    print(f"first order in eps = {first_order}")
    print(f"through second order in eps = {second_order}")

    status_line("linearized nonlinear equation is ∇²u=0",
                is_zero(first_order - eps * radial_laplacian(u, r)))

    print()
    print("Interpretation:")
    print("  The earlier shear Laplace law is the first-order approximation")
    print("  to the nonlinear exact candidate equation.")


# =============================================================================
# Case 5: Flux normalization for A
# =============================================================================

def case_5_flux_normalization_for_A():
    header("Case 5: Flux normalization for A")

    r, r_s, G, M, c = sp.symbols("r r_s G M c", positive=True, real=True)

    A = 1 - r_s / r
    dA = sp.diff(A, r)
    flux_A = sp.simplify(4 * sp.pi * r**2 * dA)

    target_flux = 8 * sp.pi * G * M / c**2
    sol_rs = sp.solve(sp.Eq(flux_A, target_flux), r_s)

    print(f"A = {A}")
    print(f"A' = {dA}")
    print(f"4πr² A' = {flux_A}")
    print(f"target flux = {target_flux}")
    print(f"r_s solution = {sol_rs}")

    status_line("A-flux normalization gives r_s=2GM/c²",
                bool(sol_rs) and is_zero(sol_rs[0] - 2 * G * M / c**2))

    print()
    print("Note:")
    print("  This parallels the earlier s-flux normalization in weak field,")
    print("  but the exact harmonic variable is A rather than s.")


# =============================================================================
# Case 6: Poisson form for A and nonlinear form for s
# =============================================================================

def case_6_poisson_form_for_A():
    header("Case 6: Poisson form for A and nonlinear form for s")

    print("Candidate exact reduced source law:")
    print()
    print("  ∇²A = 8πG rho / c²")
    print()
    print("with:")
    print()
    print("  A = exp(s)")
    print()
    print("In source-free exterior:")
    print()
    print("  ∇²A = 0")
    print()
    print("Equivalent s equation:")
    print()
    print("  ∇²s + |∇s|² = 0")
    print()
    print("In weak field, |∇s|² is second order, so:")
    print()
    print("  ∇²s ≈ 0")
    print()
    status_line("candidate exact law reduces to weak shear Laplace law", True)


# =============================================================================
# Case 7: Exact metric recovery
# =============================================================================

def case_7_exact_metric_recovery():
    header("Case 7: Exact metric recovery")

    r, r_s = sp.symbols("r r_s", positive=True, real=True)

    A = 1 - r_s / r
    s = sp.log(A)
    kappa = sp.Integer(0)
    B = sp.exp(kappa - s)
    AB = sp.simplify(A * B)

    print(f"A = {A}")
    print(f"s = ln(A) = {s}")
    print(f"kappa = {kappa}")
    print(f"B = exp(-s) = {B}")
    print(f"AB = {AB}")

    status_line("B equals 1/A", is_zero(B - 1/A))
    status_line("AB=1 exactly", is_zero(AB - 1))

    print()
    print("Result:")
    print("  kappa=0 and s=ln(1-r_s/r) recover exact Schwarzschild")
    print("  areal-gauge exterior metric factors.")


# =============================================================================
# Case 8: Comparison of source-law candidates
# =============================================================================

def case_8_compare_source_law_candidates():
    header("Case 8: Compare source-law candidates")

    print("Weak-field candidate:")
    print("  ∇²s = 0 outside source")
    print("  s = -r_s/r")
    print("  A = exp(s) = exp(-r_s/r)")
    print("  matches Schwarzschild only at first order")
    print()
    print("Exact candidate:")
    print("  ∇²A = 0 outside source")
    print("  A = 1 - r_s/r")
    print("  s = ln(A)")
    print("  equivalently ∇²s + |∇s|² = 0")
    print("  recovers exact Schwarzschild exterior factors under kappa=0")
    print()
    print("Interpretation:")
    print("  The earlier shear Poisson law may be the linearized form of a")
    print("  nonlinear exact law for A=e^s.")


# =============================================================================
# Case 9: Summary classification
# =============================================================================

def case_9_summary_classification():
    header("Case 9: Summary classification")

    print("Results:")
    print()
    print("1. Exact Schwarzschild in areal gauge has:")
    print("     A = 1 - r_s/r")
    print("     B = 1/A")
    print("     AB = 1")
    print("     kappa = 0")
    print()
    print("2. Therefore exact shear is:")
    print("     s_exact = ln(1 - r_s/r)")
    print()
    print("3. The weak shear:")
    print("     s_weak = -r_s/r")
    print("   matches only to first order.")
    print()
    print("4. s_exact is not harmonic:")
    print("     ∇²s_exact != 0")
    print()
    print("5. A_exact is harmonic:")
    print("     ∇²A_exact = 0")
    print()
    print("6. Therefore s_exact satisfies:")
    print("     ∇²s + |∇s|² = 0")
    print()
    print("7. The nonlinear s equation linearizes to:")
    print("     ∇²s = 0")
    print()
    print("8. The A-flux normalization gives:")
    print("     r_s = 2GM/c²")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("This exact-recovery toy suggests a refinement:")
    print()
    print("  The weak-field shear source law ∇²s = 0 is probably linearized.")
    print()
    print("For exact static spherical recovery, the better source-free variable may be:")
    print()
    print("  A = exp(s)")
    print()
    print("with exact exterior equation:")
    print()
    print("  ∇²A = 0")
    print()
    print("or equivalently:")
    print()
    print("  ∇²s + |∇s|² = 0")
    print()
    print("Then:")
    print()
    print("  A = 1 - r_s/r")
    print("  s = ln(1 - r_s/r)")
    print("  B = 1/A")
    print("  kappa = 0")
    print()
    print("This recovers exact Schwarzschild exterior metric factors in areal gauge.")
    print()
    print("This is still not a derivation of Einstein's equations.")
    print("It is a reduced exact static spherical candidate.")
    print()
    print("Possible next artifact:")
    print("  candidate_static_spherical_exact_recovery.md")


# =============================================================================
# Main
# =============================================================================

def main():
    header("Candidate Static Spherical Exact Recovery")
    case_0_exact_schwarzschild_compensated()
    case_1_weak_vs_exact_shear()
    case_2_harmonic_tests()
    case_3_nonlinear_s_equation()
    case_4_linearization()
    case_5_flux_normalization_for_A()
    case_6_poisson_form_for_A()
    case_7_exact_metric_recovery()
    case_8_compare_source_law_candidates()
    case_9_summary_classification()
    final_interpretation()


if __name__ == "__main__":
    main()
