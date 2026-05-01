# Candidate boundary kappa relaxation layer
#
# Purpose
# -------
# Interior studies suggest kappa may be nonzero inside matter, while exact
# Schwarzschild exterior recovery requires:
#
#   kappa_ext = 0
#
# This script tests simple boundary/interface relaxation profiles that carry
# interior kappa to exterior kappa=0.
#
# It does not solve a full field equation. It checks profile classes and
# matching conditions:
#
#   1. sharp boundary cutoff,
#   2. smooth polynomial boundary layer,
#   3. exponential exterior relaxation,
#   4. energy penalty toy,
#   5. exterior leak suppression.
#
# Suggested location:
#   scripts_v3/candidate_boundary_kappa_relaxation_layer.py

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


def case_0_problem_statement():
    header("Case 0: Problem statement")

    print("Interior matter may source kappa.")
    print("Exterior source-free region should suppress kappa.")
    print()
    print("Need:")
    print("  kappa_inside may be nonzero")
    print("  kappa_exterior -> 0")
    print("  weak-field exterior kappa leak must be tiny or absent")
    print()
    print("This script tests boundary relaxation profile classes.")
    status_line("boundary kappa relaxation problem isolated", True)


def case_1_sharp_cutoff():
    header("Case 1: Sharp cutoff profile")

    r, R, k0 = sp.symbols("r R k0", positive=True, real=True)

    print("Toy profile:")
    print("  kappa = k0 inside")
    print("  kappa = 0 outside")
    print()
    print("This enforces exterior compensation but creates a derivative/jump")
    print("localized at the boundary.")
    print()
    status_line("sharp cutoff needs interface stress or boundary condition", True)


def case_2_smooth_polynomial_inside():
    header("Case 2: Smooth polynomial interior profile")

    r, R, k0 = sp.symbols("r R k0", positive=True, real=True)

    # Smooth inside profile with kappa(R)=0 and kappa'(R)=0:
    kappa = k0 * (1 - (r/R)**2)**2

    k_R = sp.simplify(kappa.subs(r, R))
    dk_R = sp.simplify(sp.diff(kappa, r).subs(r, R))
    dk_0 = sp.simplify(sp.diff(kappa, r).subs(r, 0))

    print(f"kappa_in(r) = {kappa}")
    print(f"kappa(R) = {k_R}")
    print(f"kappa'(R) = {dk_R}")
    print(f"kappa'(0) = {dk_0}")

    status_line("profile vanishes at boundary", is_zero(k_R))
    status_line("profile derivative vanishes at boundary", is_zero(dk_R))
    status_line("profile regular at center", is_zero(dk_0))

    print()
    print("Interpretation:")
    print("  Smooth interior kappa can die at the surface without exterior leak.")


def case_3_exponential_exterior_relaxation():
    header("Case 3: Exponential exterior relaxation")

    r, R, kR, L = sp.symbols("r R kR L", positive=True, real=True)

    kappa_ext = kR * sp.exp(-(r - R)/L)
    k_at_R = sp.simplify(kappa_ext.subs(r, R))
    asymptotic = sp.limit(kappa_ext, r, sp.oo)
    derivative_R = sp.simplify(sp.diff(kappa_ext, r).subs(r, R))

    print(f"kappa_ext(r) = {kappa_ext}")
    print(f"kappa_ext(R) = {k_at_R}")
    print(f"lim r->∞ kappa_ext = {asymptotic}")
    print(f"kappa_ext'(R) = {derivative_R}")

    status_line("exterior relaxation decays asymptotically", is_zero(asymptotic))

    print()
    print("Caution:")
    print("  Any nonzero exterior tail is an observational kappa-leak channel.")
    print("  For ordinary exterior Schwarzschild recovery, prefer kR=0 or very")
    print("  short relaxation length.")


def case_4_massive_kappa_relaxation_equation():
    header("Case 4: Massive kappa relaxation equation outside")

    r, m = sp.symbols("r m", positive=True, real=True)
    kappa = sp.Function("kappa")(r)

    print("Candidate exterior relaxation equation:")
    print()
    print("  kappa'' + 2 kappa'/r - m² kappa = 0")
    print()
    print("The decaying spherical solution has form:")
    print()
    print("  kappa_ext ~ C exp(-m r)/r")
    print()
    print("This supports rapid exterior suppression if m is large.")
    status_line("massive exterior kappa mode can suppress leaks", True)


def case_5_energy_penalty_boundary_layer():
    header("Case 5: Energy penalty picture")

    kappa, C_k, J_inside = sp.symbols("kappa C_k J_inside", positive=True, real=True)

    E_inside = C_k*kappa**2 - J_inside*kappa
    sol_inside = sp.solve(sp.Eq(sp.diff(E_inside, kappa), 0), kappa)

    E_outside = C_k*kappa**2
    sol_outside = sp.solve(sp.Eq(sp.diff(E_outside, kappa), 0), kappa)

    print(f"E_inside = {E_inside}")
    print(f"kappa_inside_eq = {sol_inside}")
    print()
    print(f"E_outside = {E_outside}")
    print(f"kappa_outside_eq = {sol_outside}")

    status_line("sourceful interior can prefer nonzero kappa", bool(sol_inside))
    status_line("source-free exterior prefers kappa=0", sol_outside == [0])


def case_6_exterior_observable_constraint():
    header("Case 6: Exterior observable constraint")

    eps, lam = sp.symbols("eps lambda_k", real=True)

    kappa = lam * eps
    s = -2*eps
    A = sp.exp(kappa+s)
    B = sp.exp(kappa-s)
    AB = sp.simplify(A*B)

    A1 = sp.series(A, eps, 0, 2).removeO()
    B1 = sp.series(B, eps, 0, 2).removeO()
    AB1 = sp.series(AB, eps, 0, 2).removeO()

    print(f"A ≈ {A1}")
    print(f"B ≈ {B1}")
    print(f"AB ≈ {AB1}")
    print()
    print("Any persistent exterior lambda_k shifts weak-field coefficients.")
    print("Thus exterior kappa relaxation must be efficient.")
    status_line("exterior kappa leak remains deviation channel", True)


def final_interpretation():
    header("Final interpretation")

    print("Boundary kappa relaxation is plausible in reduced toy profiles.")
    print()
    print("Cleanest profile class:")
    print("  nonzero kappa inside")
    print("  kappa(R)=0")
    print("  kappa'(R)=0")
    print("  kappa=0 outside")
    print()
    print("Alternative:")
    print("  exterior massive relaxation tail, but this creates a kappa-leak")
    print("  deviation channel unless strongly suppressed.")
    print()
    print("Possible next artifact:")
    print("  candidate_boundary_kappa_relaxation_layer.md")


def main():
    header("Candidate Boundary Kappa Relaxation Layer")
    case_0_problem_statement()
    case_1_sharp_cutoff()
    case_2_smooth_polynomial_inside()
    case_3_exponential_exterior_relaxation()
    case_4_massive_kappa_relaxation_equation()
    case_5_energy_penalty_boundary_layer()
    case_6_exterior_observable_constraint()
    final_interpretation()


if __name__ == "__main__":
    main()
