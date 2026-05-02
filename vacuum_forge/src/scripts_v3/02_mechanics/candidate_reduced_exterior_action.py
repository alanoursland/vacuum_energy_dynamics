# Candidate reduced exterior action
#
# Purpose
# -------
# This script tests whether one reduced variational toy can unify the two
# successful reduced exterior mechanisms:
#
#   1. kappa suppression:
#        kappa = 0  ->  AB = 1
#
#   2. shear source law:
#        ∇²s = 8πG rho / c²
#        spherical exterior -> s(r) = -2GM/(r c²)
#
# This follows the reduced exterior mode program:
#
#   a = ln A
#   b = ln B
#
#   kappa = (a + b)/2
#   s     = (a - b)/2
#
#   A = exp(kappa + s)
#   B = exp(kappa - s)
#   AB = exp(2*kappa)
#
# Candidate reduced energy/action density:
#
#   L = K_k |∇kappa|² + M_k² kappa²
#       + K_s |∇s|²
#       + alpha rho s
#
# The sign of alpha is chosen so that variation gives:
#
#   ∇²s = 8πG rho / c²
#
# depending on the normalization of K_s.
#
# IMPORTANT:
# This is NOT the full theory, not a covariant action, and not a theorem.
# It is a reduced-sector variational toy.
#
# Suggested location:
#   scripts_v3/candidate_reduced_exterior_action.py

import sympy as sp


def header(title: str) -> None:
    print()
    print("=" * 96)
    print(title)
    print("=" * 96)


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


def euler_lagrange_density(L, field, coord):
    f = field
    fp = sp.diff(f, coord)
    return sp.simplify(sp.diff(L, f) - sp.diff(sp.diff(L, fp), coord))


def radial_laplacian(expr, r):
    return sp.simplify((1 / r**2) * sp.diff(r**2 * sp.diff(expr, r), r))


def series_in_epsilon(expr, epsilon, order=3):
    return sp.series(expr, epsilon, 0, order).removeO()


def case_0_log_scale_algebra():
    header("Case 0: Log-scale algebra")

    kappa, s = sp.symbols("kappa s", real=True)

    A = sp.exp(kappa + s)
    B = sp.exp(kappa - s)
    AB = sp.simplify(A * B)

    print(f"A  = {A}")
    print(f"B  = {B}")
    print(f"AB = {AB}")

    status_line("AB = exp(2*kappa)", is_zero(AB - sp.exp(2 * kappa)))
    status_line("kappa=0 gives AB=1", is_zero(AB.subs(kappa, 0) - 1))


def case_1_reduced_el_equations_1d():
    header("Case 1: Reduced Euler-Lagrange equations in one coordinate")

    x = sp.symbols("x", real=True)
    Kk, Mk, Ks, alpha = sp.symbols("K_k M_k K_s alpha", positive=True, real=True)
    rho = sp.Function("rho")(x)

    kappa = sp.Function("kappa")(x)
    s = sp.Function("s")(x)

    L = Kk * sp.diff(kappa, x)**2 + Mk**2 * kappa**2 + Ks * sp.diff(s, x)**2 + alpha * rho * s

    EL_k = euler_lagrange_density(L, kappa, x)
    EL_s = euler_lagrange_density(L, s, x)

    print(f"L = {L}")
    print()
    print("Euler-Lagrange equations:")
    print(f"  EL_kappa = {EL_k} = 0")
    print(f"  EL_s     = {EL_s} = 0")

    EL_k_ext = sp.simplify(EL_k.subs({
        kappa: 0,
        sp.diff(kappa, x): 0,
        sp.diff(kappa, (x, 2)): 0,
    }))

    print()
    print(f"EL_kappa | kappa=0 = {EL_k_ext}")
    status_line("kappa=0 solves source-free kappa equation", is_zero(EL_k_ext))

    print()
    print("Shear equation rearranged:")
    print("  alpha*rho - 2*K_s*s'' = 0")
    print("  s'' = alpha*rho/(2*K_s)")
    print()
    print("To match the reduced Poisson normalization in Cartesian form, choose:")
    print("  alpha/(2*K_s) = 8πG/c²")


def case_2_3d_variation_target():
    header("Case 2: 3D reduced variation target and normalization")

    G, c, Ks, alpha = sp.symbols("G c K_s alpha", positive=True, real=True)

    alpha_solution = sp.solve(sp.Eq(alpha / (2 * Ks), 8 * sp.pi * G / c**2), alpha)

    print("Variation of:")
    print("  E_s = ∫ [K_s |∇s|² + alpha rho s] d³x")
    print("gives:")
    print("  ∇²s = alpha rho/(2K_s)")
    print()
    print("Desired:")
    print("  ∇²s = 8πG rho/c²")
    print()
    print(f"alpha solution = {alpha_solution}")

    ok = bool(alpha_solution) and is_zero(alpha_solution[0] - 16 * sp.pi * G * Ks / c**2)
    status_line("normalization alpha = 16πG K_s/c²", ok)


def case_3_exterior_spherical_solution():
    header("Case 3: Exterior spherical solution from reduced source law")

    r, G, M, c = sp.symbols("r G M c", positive=True, real=True)
    C = sp.symbols("C", real=True)

    s_expr = C / r
    lap = radial_laplacian(s_expr, r)

    print(f"s(r) = {s_expr}")
    print(f"∇²s for r>0 = {lap}")
    status_line("C/r is harmonic outside source", is_zero(lap))

    flux = sp.simplify(4 * sp.pi * r**2 * sp.diff(s_expr, r))
    target_flux = 8 * sp.pi * G * M / c**2
    C_solution = sp.solve(sp.Eq(flux, target_flux), C)

    print()
    print(f"4πr²s'(r) = {flux}")
    print(f"target flux = {target_flux}")
    print(f"C solution = {C_solution}")

    if C_solution:
        C_val = sp.simplify(C_solution[0])
        s_fixed = sp.simplify(s_expr.subs(C, C_val))
        print(f"s_fixed(r) = {s_fixed}")
        status_line("source flux fixes s=-2GM/(rc²)", is_zero(s_fixed + 2 * G * M / (r * c**2)))


def case_4_metric_recovery():
    header("Case 4: Metric recovery")

    eps = sp.symbols("eps", positive=True, real=True)

    kappa = sp.Integer(0)
    s = -2 * eps

    A = sp.exp(kappa + s)
    B = sp.exp(kappa - s)
    AB = sp.simplify(A * B)

    A_series = series_in_epsilon(A, eps, 3)
    B_series = series_in_epsilon(B, eps, 3)

    print(f"kappa = {kappa}")
    print(f"s = {s}")
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"AB = {AB}")
    print()
    print(f"A series = {A_series}")
    print(f"B series = {B_series}")

    status_line("A = 1 - 2eps + 2eps² + ...", is_zero(A_series - (1 - 2 * eps + 2 * eps**2)))
    status_line("B = 1 + 2eps + 2eps² + ...", is_zero(B_series - (1 + 2 * eps + 2 * eps**2)))
    status_line("AB = 1 exactly", is_zero(AB - 1))


def case_5_kappa_source_failure_control():
    header("Case 5: Failure control — direct kappa source")

    x = sp.symbols("x", real=True)
    Kk, Mk, Jk = sp.symbols("K_k M_k J_k", positive=True, real=True)

    kappa = sp.Function("kappa")(x)

    Lk = Kk * sp.diff(kappa, x)**2 + Mk**2 * kappa**2 - Jk * kappa
    EL_k = euler_lagrange_density(Lk, kappa, x)

    print(f"L_k = {Lk}")
    print(f"EL_kappa = {EL_k} = 0")

    k0 = sp.symbols("k0", real=True)
    algebraic = sp.simplify(EL_k.subs({
        kappa: k0,
        sp.diff(kappa, x): 0,
        sp.diff(kappa, (x, 2)): 0,
    }))
    k0_solution = sp.solve(sp.Eq(algebraic, 0), k0)

    print()
    print(f"constant equilibrium equation = {algebraic} = 0")
    print(f"kappa constant solutions = {k0_solution}")

    if k0_solution:
        k_eq = sp.simplify(k0_solution[0])
        AB = sp.simplify(sp.exp(2 * k_eq))
        print(f"kappa_eq = {k_eq}")
        print(f"AB = {AB}")
        status_line("kappa source makes kappa nonzero generically", k_eq != 0)
        status_line("reciprocal scaling fails generically", not is_zero(AB - 1))


def case_6_wrong_shear_coefficient_control():
    header("Case 6: Failure control — wrong shear coefficient")

    eps, lam = sp.symbols("eps lambda", real=True)

    s = -lam * eps
    A = sp.exp(s)
    A_series = series_in_epsilon(A, eps, 2)

    print(f"s = {s}")
    print(f"A series = {A_series}")

    sol = sp.solve(sp.Eq(A_series, 1 - 2 * eps), lam)
    print(f"lambda solution = {sol}")

    status_line("weak-field temporal coefficient fixes lambda=2", sol == [2])


def final_interpretation():
    header("Final interpretation")

    print("This reduced action toy unifies the previous two mechanisms:")
    print()
    print("1. Kappa suppression:")
    print("   K_k |∇kappa|² + M_k² kappa²")
    print("   gives kappa=0 as the relaxed source-free exterior solution.")
    print()
    print("2. Shear source law:")
    print("   K_s |∇s|² + alpha rho s")
    print("   gives ∇²s = alpha rho/(2K_s).")
    print()
    print("Choosing:")
    print("   alpha = 16πG K_s/c²")
    print("gives:")
    print("   ∇²s = 8πG rho/c².")
    print()
    print("For a spherical mass M:")
    print("   s(r) = -2GM/(r c²).")
    print()
    print("With kappa=0:")
    print("   A = exp(s), B = exp(-s), AB = 1.")
    print()
    print("Weak field:")
    print("   A ≈ 1 - 2GM/(r c²)")
    print("   B ≈ 1 + 2GM/(r c²)")
    print()
    print("This is still only a reduced-sector variational toy.")
    print("The next theoretical step is to find the covariant parent of this action")
    print("and explain the origin of the kappa suppression and shear-source coupling.")


def main():
    header("Candidate Reduced Exterior Action")
    case_0_log_scale_algebra()
    case_1_reduced_el_equations_1d()
    case_2_3d_variation_target()
    case_3_exterior_spherical_solution()
    case_4_metric_recovery()
    case_5_kappa_source_failure_control()
    case_6_wrong_shear_coefficient_control()
    final_interpretation()


if __name__ == "__main__":
    main()
