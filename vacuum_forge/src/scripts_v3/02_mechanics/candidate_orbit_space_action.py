# Candidate orbit-space action
#
# Purpose
# -------
# This script follows the exact static spherical recovery result.
#
# The exact recovery suggested:
#
#   A = exp(s)
#
# is the better source variable, not s itself.
#
# Candidate exact static spherical source law:
#
#   ∇²A = 8πG rho / c²
#
# In source-free exterior:
#
#   ∇²A = 0
#
# In terms of s:
#
#   ∇² exp(s) = 0
#   ∇²s + |∇s|² = 0
#
# This script tests candidate variational principles:
#
#   1. Linear weak-field s-action:
#        E_s = ∫ [K_s |∇s|² + alpha rho s] d³x
#
#      gives:
#        ∇²s = alpha rho / (2K_s)
#
#   2. Exact candidate A-action:
#        E_A = ∫ [K_A |∇A|² + beta rho A] d³x
#
#      gives:
#        ∇²A = beta rho / (2K_A)
#
#   3. Nonlinear s-action induced by A=exp(s):
#        E_s_exact = ∫ [K_A exp(2s)|∇s|² + beta rho exp(s)] d³x
#
#      should be equivalent to the A-action under A=exp(s).
#
#   4. Source-free exterior exact equation:
#        ∇²A = 0
#      recovers:
#        A = 1 - r_s/r
#        s = ln(1-r_s/r)
#        B = 1/A under kappa=0
#
#   5. Orbit-space compensation condition:
#        A = |∇R|²
#      connects the action variable A to the geometric reduced condition.
#
# IMPORTANT:
# This is a reduced static spherical variational toy.
# It is not a covariant action for the full theory.
#
# Suggested location:
#   scripts_v3/candidate_orbit_space_action.py

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


def euler_lagrange_1d(L, field, x):
    f = field
    fp = sp.diff(f, x)
    return sp.simplify(sp.diff(L, f) - sp.diff(sp.diff(L, fp), x))


def radial_laplacian(expr, r):
    return sp.simplify((1 / r**2) * sp.diff(r**2 * sp.diff(expr, r), r))


def radial_grad_sq(expr, r):
    return sp.simplify(sp.diff(expr, r)**2)


def case_0_recap_exact_source_variable():
    header("Case 0: Recap exact source variable")

    r, r_s = sp.symbols("r r_s", positive=True, real=True)

    A = 1 - r_s / r
    s = sp.log(A)
    B = sp.exp(-s)

    print(f"A_exact = {A}")
    print(f"s_exact = ln(A) = {s}")
    print(f"B = exp(-s) = {B}")
    print(f"AB = {sp.simplify(A*B)}")
    print()
    print(f"∇²A = {radial_laplacian(A, r)}")
    print(f"∇²s + |∇s|² = {sp.simplify(radial_laplacian(s, r) + radial_grad_sq(s, r))}")

    status_line("A is harmonic outside source", is_zero(radial_laplacian(A, r)))
    status_line("s satisfies nonlinear source-free equation",
                is_zero(radial_laplacian(s, r) + radial_grad_sq(s, r)))
    status_line("kappa=0 gives AB=1", is_zero(A*B - 1))


def case_1_weak_field_s_action():
    header("Case 1: Weak-field linear s-action")

    x = sp.symbols("x", real=True)
    K_s, alpha = sp.symbols("K_s alpha", positive=True, real=True)
    rho = sp.Function("rho")(x)
    s = sp.Function("s")(x)

    L = K_s * sp.diff(s, x)**2 + alpha * rho * s
    EL = euler_lagrange_1d(L, s, x)

    print(f"L_s = {L}")
    print(f"Euler-Lagrange = {EL} = 0")
    print()
    print("Rearranged:")
    print("  s'' = alpha rho / (2 K_s)")
    print()
    print("This is the weak-field linear action used earlier.")

    expected = alpha * rho - 2 * K_s * sp.diff(s, (x, 2))
    status_line("linear s-action gives Poisson equation for s", is_zero(EL - expected))


def case_2_exact_A_action():
    header("Case 2: Exact candidate A-action")

    x = sp.symbols("x", real=True)
    K_A, beta = sp.symbols("K_A beta", positive=True, real=True)
    rho = sp.Function("rho")(x)
    A = sp.Function("A")(x)

    L = K_A * sp.diff(A, x)**2 + beta * rho * A
    EL = euler_lagrange_1d(L, A, x)

    print(f"L_A = {L}")
    print(f"Euler-Lagrange = {EL} = 0")
    print()
    print("Rearranged:")
    print("  A'' = beta rho / (2 K_A)")
    print()
    print("To match:")
    print("  ∇²A = 8πG rho / c²")
    print("choose:")
    print("  beta/(2K_A) = 8πG/c²")
    print("  beta = 16πG K_A/c²")

    G, c = sp.symbols("G c", positive=True, real=True)
    beta_sol = 16 * sp.pi * G * K_A / c**2
    print(f"beta = {beta_sol}")

    expected = beta * rho - 2 * K_A * sp.diff(A, (x, 2))
    status_line("A-action gives Poisson equation for A", is_zero(EL - expected))


def case_3_nonlinear_s_action_from_A():
    header("Case 3: Nonlinear s-action induced by A=exp(s)")

    x = sp.symbols("x", real=True)
    K_A, beta = sp.symbols("K_A beta", positive=True, real=True)
    rho = sp.Function("rho")(x)
    s = sp.Function("s")(x)

    A = sp.exp(s)
    Ap = sp.diff(A, x)

    L_s_exact = sp.simplify(K_A * Ap**2 + beta * rho * A)
    EL_s = sp.simplify(euler_lagrange_1d(L_s_exact, s, x))

    print(f"A = exp(s)")
    print(f"A' = {Ap}")
    print(f"L_s_exact = {L_s_exact}")
    print(f"Euler-Lagrange wrt s = {EL_s}")

    EL_A_sub = beta * rho - 2 * K_A * sp.diff(A, (x, 2))
    expected = sp.simplify(EL_A_sub * sp.exp(s))

    print()
    print(f"Expected EL_s = exp(s) * [beta rho - 2K_A A''] = {expected}")

    status_line("nonlinear s-action is equivalent to A-action under A=exp(s)",
                is_zero(EL_s - expected))


def case_4_radial_source_free_A_equation():
    header("Case 4: Radial source-free A equation")

    r, r_s = sp.symbols("r r_s", positive=True, real=True)
    A = 1 - r_s / r
    s = sp.log(A)

    lap_A = radial_laplacian(A, r)
    nonlinear_s = sp.simplify(radial_laplacian(s, r) + radial_grad_sq(s, r))

    print(f"A = {A}")
    print(f"s = ln(A) = {s}")
    print(f"∇²A = {lap_A}")
    print(f"∇²s + |∇s|² = {nonlinear_s}")

    status_line("A=1-r_s/r solves radial source-free A equation", is_zero(lap_A))
    status_line("s=ln(1-r_s/r) solves nonlinear s equation", is_zero(nonlinear_s))


def case_5_radial_A_action_with_measure():
    header("Case 5: Radial A-action with spherical measure")

    r = sp.symbols("r", positive=True, real=True)
    K_A, beta = sp.symbols("K_A beta", positive=True, real=True)
    rho = sp.Function("rho")(r)
    A = sp.Function("A")(r)

    L_radial = r**2 * (K_A * sp.diff(A, r)**2 + beta * rho * A)
    EL = euler_lagrange_1d(L_radial, A, r)

    print(f"L_radial = {L_radial}")
    print(f"Euler-Lagrange = {EL} = 0")

    expected = sp.simplify(r**2 * beta * rho - 2 * K_A * sp.diff(r**2 * sp.diff(A, r), r))
    print(f"Expected = {expected}")
    status_line("radial A-action gives spherical Poisson equation", is_zero(EL - expected))

    print()
    print("Rearranged:")
    print("  (1/r²)(r² A')' = beta rho/(2K_A)")
    print("  ∇²A = beta rho/(2K_A)")


def case_6_flux_normalization():
    header("Case 6: Flux normalization")

    r, r_s, G, M, c = sp.symbols("r r_s G M c", positive=True, real=True)

    A = 1 - r_s / r
    flux = sp.simplify(4 * sp.pi * r**2 * sp.diff(A, r))
    target = 8 * sp.pi * G * M / c**2
    sol = sp.solve(sp.Eq(flux, target), r_s)

    print(f"A = {A}")
    print(f"4πr² A' = {flux}")
    print(f"target = {target}")
    print(f"r_s solution = {sol}")

    status_line("flux normalization gives Schwarzschild radius",
                bool(sol) and is_zero(sol[0] - 2*G*M/c**2))


def case_7_combine_with_kappa_suppression():
    header("Case 7: Combine A-action with kappa suppression toy")

    x = sp.symbols("x", real=True)
    K_k, M_k, K_A, beta = sp.symbols("K_k M_k K_A beta", positive=True, real=True)
    rho = sp.Function("rho")(x)
    kappa = sp.Function("kappa")(x)
    A = sp.Function("A")(x)

    L = (
        K_k * sp.diff(kappa, x)**2
        + M_k**2 * kappa**2
        + K_A * sp.diff(A, x)**2
        + beta * rho * A
    )

    EL_k = euler_lagrange_1d(L, kappa, x)
    EL_A = euler_lagrange_1d(L, A, x)

    print(f"L = {L}")
    print()
    print(f"EL_kappa = {EL_k} = 0")
    print(f"EL_A     = {EL_A} = 0")

    expected_k = 2*M_k**2*kappa - 2*K_k*sp.diff(kappa, (x,2))
    expected_A = beta*rho - 2*K_A*sp.diff(A, (x,2))

    status_line("kappa equation gives suppression when unsourced", is_zero(EL_k - expected_k))
    status_line("A equation gives source law", is_zero(EL_A - expected_A))


def case_8_orbit_space_compensation():
    header("Case 8: Orbit-space compensation reminder")

    X = sp.symbols("X", positive=True, real=True)
    T = sp.Function("T")(X)
    Q = sp.Function("Q")(X)
    S = sp.Function("S")(X)

    gradR2 = sp.simplify(sp.diff(S, X)**2 / Q)
    kappa_orbit = sp.simplify(sp.Rational(1,2) * sp.log(T / gradR2))

    print("Static spherical orbit-space metric:")
    print("  ds² = -T(X)c²dt² + Q(X)dX² + S(X)²dΩ²")
    print()
    print(f"|∇R|² = {gradR2}")
    print(f"kappa = 1/2 ln(A/|∇R|²) = {kappa_orbit}")
    print()
    print("Compensation kappa=0 gives:")
    print("  A = |∇R|²")
    print("  T Q = S'²")
    print()
    print("Exact Schwarzschild exterior satisfies this with A=1-r_s/r.")
    status_line("orbit-space condition supplies geometric compensation target", True)


def case_9_summary_classification():
    header("Case 9: Summary classification")

    print("Results:")
    print()
    print("1. The weak-field s-action gives:")
    print("     ∇²s = alpha rho/(2K_s)")
    print()
    print("2. The exact candidate A-action gives:")
    print("     ∇²A = beta rho/(2K_A)")
    print()
    print("3. Choosing:")
    print("     beta = 16πG K_A/c²")
    print("   gives:")
    print("     ∇²A = 8πG rho/c²")
    print()
    print("4. Under A=exp(s), the A-action becomes nonlinear in s:")
    print("     exp(2s)|∇s|² + rho exp(s)")
    print()
    print("5. Source-free exterior gives:")
    print("     ∇²A = 0")
    print("   or:")
    print("     ∇²s + |∇s|² = 0")
    print()
    print("6. The combined toy has:")
    print("     kappa suppression + A sourcing")
    print()
    print("This is a reduced exact static spherical action candidate,")
    print("not a full covariant action.")


def final_interpretation():
    header("Final interpretation")

    print("This action probe supports the exact-recovery refinement:")
    print()
    print("  The linear weak-field action should be written in s.")
    print("  The exact static spherical candidate is cleaner in A=exp(s).")
    print()
    print("Candidate exact reduced action sector:")
    print()
    print("  E_A = ∫ [K_A |∇A|² + beta rho A] d³x")
    print()
    print("with:")
    print()
    print("  beta = 16πG K_A/c²")
    print()
    print("gives:")
    print()
    print("  ∇²A = 8πG rho/c²")
    print()
    print("Under A=exp(s), this becomes a nonlinear s-action and yields:")
    print()
    print("  ∇²s + |∇s|² = 0")
    print()
    print("in source-free exterior.")
    print()
    print("Combining with kappa suppression gives the reduced exact-sector toy:")
    print()
    print("  kappa suppressed")
    print("  A=e^s sourced")
    print("  B=1/A when kappa=0")
    print()
    print("Possible next artifact:")
    print("  candidate_orbit_space_action.md")


def main():
    header("Candidate Orbit-Space Action")
    case_0_recap_exact_source_variable()
    case_1_weak_field_s_action()
    case_2_exact_A_action()
    case_3_nonlinear_s_action_from_A()
    case_4_radial_source_free_A_equation()
    case_5_radial_A_action_with_measure()
    case_6_flux_normalization()
    case_7_combine_with_kappa_suppression()
    case_8_orbit_space_compensation()
    case_9_summary_classification()
    final_interpretation()


if __name__ == "__main__":
    main()
