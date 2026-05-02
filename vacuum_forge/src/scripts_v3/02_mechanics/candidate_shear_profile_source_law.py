# Candidate shear profile source law
#
# Purpose
# -------
# This script begins the shear/source-law development unit after the
# log-scale and kappa-suppression studies.
#
# Previous unit:
#   kappa = (ln A + ln B)/2 controls reciprocal scaling.
#   kappa = 0 -> AB = 1.
#
# Current unit:
#   Given kappa = 0 in the static source-free exterior,
#   determine the remaining compensated/shear mode s(r).
#
# Log-scale convention used here:
#
#   a = ln A
#   b = ln B
#
#   kappa = (a + b)/2
#   s     = (a - b)/2
#
# If kappa = 0:
#
#   a = s
#   b = -s
#
# so:
#
#   A = exp(s)
#   B = exp(-s)
#   AB = 1 exactly.
#
# Weak-field target:
#
#   A = 1 - 2U/c^2 + O(c^-4)
#   B = 1 + 2U/c^2 + O(c^-4)
#   U = GM/r
#
# Therefore:
#
#   s(r) = ln A ~= -2U/c^2 = -2GM/(r c^2)
#
# This script tests the simplest reduced exterior source-law toy:
#
#   source-free exterior:
#       ∇² s = 0
#
# In spherical symmetry:
#
#   (1/r^2) d/dr (r^2 ds/dr) = 0
#
# with asymptotic flatness:
#
#   s(infinity) = 0
#
# and mass/interface flux condition:
#
#   4π r² s'(r) = 8π GM/c²
#
# which fixes:
#
#   s(r) = -2GM/(r c²)
#
# This is NOT a full field equation and NOT a theorem.
# It is a reduced-sector source-law toy.

import sympy as sp


def header(title: str) -> None:
    print()
    print("=" * 92)
    print(title)
    print("=" * 92)


def subheader(title: str) -> None:
    print()
    print("-" * 92)
    print(title)
    print("-" * 92)


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


def series_in_epsilon(expr, epsilon, order=3):
    return sp.series(expr, epsilon, 0, order).removeO()


def case_0_convention_check():
    header("Case 0: Convention check")

    kappa, s = sp.symbols("kappa s", real=True)

    a = kappa + s
    b = kappa - s
    A = sp.exp(a)
    B = sp.exp(b)
    AB = sp.simplify(A * B)

    print(f"a = {a}")
    print(f"b = {b}")
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"AB = {AB}")

    A_k0 = sp.simplify(A.subs(kappa, 0))
    B_k0 = sp.simplify(B.subs(kappa, 0))
    AB_k0 = sp.simplify(AB.subs(kappa, 0))

    print()
    print("With kappa = 0:")
    print(f"A = {A_k0}")
    print(f"B = {B_k0}")
    print(f"AB = {AB_k0}")

    status_line("kappa=0 gives A=exp(s)", is_zero(A_k0 - sp.exp(s)))
    status_line("kappa=0 gives B=exp(-s)", is_zero(B_k0 - sp.exp(-s)))
    status_line("kappa=0 gives AB=1", is_zero(AB_k0 - 1))


def case_1_radial_laplace_solution():
    header("Case 1: Source-free radial Laplace equation")

    r = sp.symbols("r", positive=True, real=True)
    s = sp.Function("s")

    equation = sp.Eq((1 / r**2) * sp.diff(r**2 * sp.diff(s(r), r), r), 0)

    print("Radial source-free equation:")
    print(f"  {equation}")

    sol = sp.dsolve(equation)
    print()
    print("General solution:")
    print(f"  {sol}")

    C1, C2 = sp.symbols("C1 C2")
    candidate = C1 + C2 / r
    lap_candidate = sp.simplify((1 / r**2) * sp.diff(r**2 * sp.diff(candidate, r), r))

    print()
    print(f"Candidate s(r) = {candidate}")
    print(f"∇²s = {lap_candidate}")

    status_line("C1 + C2/r solves source-free radial Laplace equation", is_zero(lap_candidate))


def case_2_flux_fixes_coefficient():
    header("Case 2: Mass/interface flux fixes coefficient")

    r, G, M, c = sp.symbols("r G M c", positive=True, real=True)
    C = sp.symbols("C", real=True)

    s_expr = C / r
    ds_dr = sp.diff(s_expr, r)
    flux = sp.simplify(4 * sp.pi * r**2 * ds_dr)

    print(f"s(r) = {s_expr}")
    print(f"s'(r) = {ds_dr}")
    print(f"4π r² s'(r) = {flux}")

    target_flux = 8 * sp.pi * G * M / c**2
    C_solution = sp.solve(sp.Eq(flux, target_flux), C)

    print()
    print(f"Target flux = {target_flux}")
    print(f"C solution = {C_solution}")

    if C_solution:
        C_val = sp.simplify(C_solution[0])
        s_fixed = sp.simplify(s_expr.subs(C, C_val))
        print(f"C = {C_val}")
        print(f"s_fixed(r) = {s_fixed}")

        target_s = -2 * G * M / (r * c**2)
        status_line("flux condition fixes s(r) = -2GM/(r c^2)", is_zero(s_fixed - target_s))

        fixed_flux = sp.simplify(4 * sp.pi * r**2 * sp.diff(s_fixed, r))
        print(f"fixed flux = {fixed_flux}")
        status_line("fixed solution has desired outward flux", is_zero(fixed_flux - target_flux))


def case_3_metric_recovery_from_s():
    header("Case 3: Weak-field metric recovery from shear profile")

    eps = sp.symbols("eps", positive=True, real=True)

    s = -2 * eps
    A = sp.exp(s)
    B = sp.exp(-s)
    AB = sp.simplify(A * B)

    A_series = series_in_epsilon(A, eps, order=3)
    B_series = series_in_epsilon(B, eps, order=3)
    AB_series = sp.simplify(series_in_epsilon(AB, eps, order=3))

    print(f"s = {s}")
    print(f"A = exp(s) = {A}")
    print(f"B = exp(-s) = {B}")
    print(f"AB = {AB}")
    print()
    print(f"A series = {A_series}")
    print(f"B series = {B_series}")
    print(f"AB series = {AB_series}")

    print()
    status_line("A recovers temporal series through O(eps^2)", is_zero(sp.expand(A_series - (1 - 2 * eps + 2 * eps**2))))
    status_line("B recovers reciprocal spatial series through O(eps^2)", is_zero(sp.expand(B_series - (1 + 2 * eps + 2 * eps**2))))
    status_line("AB is exactly 1", is_zero(AB - 1))

    print()
    print("First-order targets:")
    print(f"  A = {1 - 2 * eps} + O(eps^2)")
    print(f"  B = {1 + 2 * eps} + O(eps^2)")


def case_4_poisson_source_form():
    header("Case 4: Poisson source form and sign check")

    r, G, M, c = sp.symbols("r G M c", positive=True, real=True)

    print("Distributional sign check:")
    print("  ∇²(1/r) = -4π δ³(r)")
    print("  s = -2GM/(c² r)")
    print("  ∇²s = (+8πGM/c²) δ³(r)")
    print()
    print("Candidate reduced Poisson equation:")
    print("  ∇²s = 8πG rho / c²")
    print()
    print("Outside the source:")
    print("  rho = 0")
    print("  ∇²s = 0")

    s_expr = -2 * G * M / (r * c**2)
    lap = sp.simplify((1 / r**2) * sp.diff(r**2 * sp.diff(s_expr, r), r))

    print()
    print(f"Exterior s(r) = {s_expr}")
    print(f"Ordinary radial ∇²s for r>0 = {lap}")
    status_line("exterior solution is harmonic away from source", is_zero(lap))


def case_5_failure_controls():
    header("Case 5: Failure controls")

    r, C0, C1, eps = sp.symbols("r C0 C1 eps", positive=True, real=True)

    subheader("Failure control A: nonzero asymptotic constant")
    s_const = C0 + C1 / r

    print(f"s(r) = {s_const}")
    print("If C0 != 0, then s(infinity) != 0.")
    print("This violates asymptotic flatness unless C0 = 0.")
    status_line("asymptotic flatness requires C0=0", True)

    subheader("Failure control B: wrong coefficient")
    lam = sp.symbols("lambda", real=True)
    s_wrong = -lam * eps
    A_wrong = sp.exp(s_wrong)
    A_wrong_series = series_in_epsilon(A_wrong, eps, order=2)
    print(f"s = {s_wrong}")
    print(f"A series = {A_wrong_series}")
    print("Weak-field temporal target requires coefficient lambda = 2.")
    lambda_solution = sp.solve(sp.Eq(A_wrong_series, 1 - 2 * eps), lam)
    print(f"lambda solution = {lambda_solution}")
    status_line("weak-field temporal coefficient fixes lambda=2", lambda_solution == [2])


def final_interpretation():
    header("Final interpretation")

    print("This source-law toy establishes the reduced exterior chain:")
    print()
    print("  kappa = 0")
    print("    -> A = exp(s), B = exp(-s), AB = 1")
    print()
    print("  source-free exterior shear equation:")
    print("    ∇²s = 0")
    print()
    print("  spherical solution plus asymptotic flatness:")
    print("    s(r) = C/r")
    print()
    print("  mass/interface flux condition:")
    print("    4πr²s'(r) = 8πGM/c²")
    print()
    print("  coefficient:")
    print("    C = -2GM/c²")
    print()
    print("  result:")
    print("    s(r) = -2GM/(r c²)")
    print()
    print("  metric:")
    print("    A = exp(s) ≈ 1 - 2GM/(r c²)")
    print("    B = exp(-s) ≈ 1 + 2GM/(r c²)")
    print("    AB = 1 exactly")
    print()
    print("This does NOT yet derive the field equation or the mass/interface flux law.")
    print("It shows that if the shear mode obeys a Laplace/Poisson source law with")
    print("the stated normalization, then the weak-field exterior profile follows.")
    print()
    print("Next theoretical target:")
    print("  Explain why the vacuum configuration functional gives this shear equation")
    print("  and why the source/interface flux is fixed by M as 8πGM/c².")


def main():
    header("Candidate Shear Profile Source Law")
    case_0_convention_check()
    case_1_radial_laplace_solution()
    case_2_flux_fixes_coefficient()
    case_3_metric_recovery_from_s()
    case_4_poisson_source_form()
    case_5_failure_controls()
    final_interpretation()


if __name__ == "__main__":
    main()
