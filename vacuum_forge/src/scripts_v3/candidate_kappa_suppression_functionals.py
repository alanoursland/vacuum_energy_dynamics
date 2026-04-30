# Candidate kappa-suppression functionals
#
# Purpose
# -------
# This script is a reduced-sector VacuumForge / SymPy development experiment.
#
# It follows candidate_log_scale_modes_test_v2.py and tests toy exterior
# functionals that may suppress the conformal / uncompensated mode kappa
# while allowing the compensated / shear mode s.
#
# This is NOT a field equation and NOT a theorem.
#
# It is a toy laboratory for the P7-style target:
#
#   static source-free exterior compensation:
#       kappa -> 0
#       s remains active
#
# Log-scale exterior modes:
#
#   a = ln A
#   b = ln B
#
#   kappa = (a + b)/2
#   s     = (a - b)/2
#
# Then:
#
#   A = exp(kappa + s)
#   B = exp(kappa - s)
#   AB = exp(2*kappa)
#
# So kappa = 0 gives reciprocal exterior scaling:
#
#   AB = 1.
#
# This script tests whether several toy exterior functionals drive kappa=0
# without directly assuming AB=1 and without forcing s=0.
#
# Cases
# -----
# Case 0: Algebraic spine
#   Verify AB=exp(2*kappa).
#
# Case 1: Algebraic local potential
#   E = M_k^2 kappa^2 + M_s^2 (s - S_b)^2
#   Expected: kappa=0, s=S_b.
#
# Case 2: Kappa-sourced control
#   E = M_k^2 kappa^2 - J_k kappa + M_s^2 (s - S_b)^2
#   Expected: kappa=J_k/(2 M_k^2), so AB != 1 generically.
#
# Case 3: Two-shell exterior relaxation
#   Two radial shell variables kappa1,kappa2 and s1,s2.
#   Kappa has mass + gradient stiffness. Boundary condition kappa(infty)=0.
#   Shear has boundary source S_b at inner shell.
#   Expected: kappa1=kappa2=0, s active.
#
# Case 4: Two-shell kappa boundary-source control
#   Same as Case 3 but with an inner kappa boundary source K_b.
#   Expected: kappa becomes nonzero; reciprocal scaling fails unless K_b=0
#   or exterior dynamics suppresses it infinitely.
#
# Case 5: Exterior-only kappa suppression with interface shear
#   Similar to Case 3, interpreted as:
#       source/interface seeds shear
#       source-free exterior has no kappa source
#   Expected: kappa=0 and s active.
#
# Suggested location:
#   scripts_v3/candidate_kappa_suppression_functionals.py

import sympy as sp


# =============================================================================
# Utilities
# =============================================================================

def header(title: str) -> None:
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


def subheader(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


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


def solve_stationary(energy, variables):
    equations = [sp.Eq(sp.diff(energy, v), 0) for v in variables]
    solutions = sp.solve(equations, variables, dict=True, simplify=True)
    return equations, solutions


def print_energy_result(name, energy, variables):
    print(f"{name} energy:")
    print(f"  E = {sp.simplify(energy)}")
    equations, solutions = solve_stationary(energy, variables)
    print("Stationary equations:")
    for eq in equations:
        print(f"  {eq}")
    print("Solutions:")
    for sol in solutions:
        print(f"  {sol}")
    if not solutions:
        print("  (none)")
    return equations, solutions


def ab_from_kappa(kappa_expr):
    return sp.simplify(sp.exp(2 * kappa_expr))


def reciprocal_status(kappa_expr):
    AB = ab_from_kappa(kappa_expr)
    return AB, is_zero(AB - 1)


# =============================================================================
# Case 0: Algebraic spine
# =============================================================================

def case_0_algebraic_spine():
    header("Case 0: Algebraic spine")

    kappa, s = sp.symbols("kappa s", real=True)

    A = sp.exp(kappa + s)
    B = sp.exp(kappa - s)
    AB = sp.simplify(A * B)

    print(f"A  = {A}")
    print(f"B  = {B}")
    print(f"AB = {AB}")

    status_line("AB = exp(2*kappa)", is_zero(AB - sp.exp(2 * kappa)))
    status_line("kappa=0 implies AB=1", is_zero(AB.subs(kappa, 0) - 1))


# =============================================================================
# Case 1: Algebraic local potential suppresses kappa, allows shear
# =============================================================================

def case_1_local_potential():
    header("Case 1: Local potential suppresses kappa, allows shear")

    kappa, s = sp.symbols("kappa s", real=True)
    M_k, M_s, S_b = sp.symbols("M_k M_s S_b", positive=True, real=True)

    # Kappa is minimized at 0.
    # Shear is minimized at boundary/interface amplitude S_b.
    E = M_k**2 * kappa**2 + M_s**2 * (s - S_b)**2

    _, sols = print_energy_result("Case 1", E, [kappa, s])
    if sols:
        sol = sols[0]
        k_eq = sp.simplify(sol[kappa])
        s_eq = sp.simplify(sol[s])
        AB, recip = reciprocal_status(k_eq)

        print()
        print(f"kappa_eq = {k_eq}")
        print(f"s_eq     = {s_eq}")
        print(f"AB       = {AB}")

        status_line("kappa suppressed", k_eq == 0)
        status_line("shear remains available", sp.simplify(s_eq - S_b) == 0)
        status_line("reciprocal scaling follows", recip)


# =============================================================================
# Case 2: Kappa-sourced control
# =============================================================================

def case_2_kappa_sourced_control():
    header("Case 2: Kappa-sourced control")

    kappa, s = sp.symbols("kappa s", real=True)
    M_k, M_s, S_b, J_k = sp.symbols("M_k M_s S_b J_k", positive=True, real=True)

    # Control: add a direct kappa source.
    # This should pull kappa away from zero and break reciprocal scaling.
    E = M_k**2 * kappa**2 - J_k * kappa + M_s**2 * (s - S_b)**2

    _, sols = print_energy_result("Case 2", E, [kappa, s])
    if sols:
        sol = sols[0]
        k_eq = sp.simplify(sol[kappa])
        s_eq = sp.simplify(sol[s])
        AB, recip = reciprocal_status(k_eq)

        print()
        print(f"kappa_eq = {k_eq}")
        print(f"s_eq     = {s_eq}")
        print(f"AB       = {AB}")

        status_line("kappa is nonzero generically", k_eq != 0)
        status_line("shear remains available", sp.simplify(s_eq - S_b) == 0)
        status_line("reciprocal scaling fails generically", not recip)


# =============================================================================
# Case 3: Two-shell exterior relaxation, kappa has mass + stiffness
# =============================================================================

def case_3_two_shell_exterior_relaxation():
    header("Case 3: Two-shell exterior relaxation")

    k1, k2, s1, s2 = sp.symbols("kappa_1 kappa_2 s_1 s_2", real=True)
    M_k, K_k, M_s, K_s, S_b = sp.symbols("M_k K_k M_s K_s S_b", positive=True, real=True)

    # Two-shell toy:
    #   k1, s1 = inner exterior shell
    #   k2, s2 = outer exterior shell
    #
    # Kappa:
    #   mass term suppresses kappa in source-free exterior
    #   gradient term smooths shell-to-shell variation
    #   outer boundary effectively prefers kappa2=0 through mass term
    #
    # Shear:
    #   inner shell is seeded by boundary/interface shear S_b
    #   gradient term lets shear propagate outward
    #   small mass term keeps solution finite in toy model
    E_k = M_k**2 * (k1**2 + k2**2) + K_k * (k2 - k1)**2
    E_s = M_s**2 * ((s1 - S_b)**2 + s2**2) + K_s * (s2 - s1)**2
    E = E_k + E_s

    _, sols = print_energy_result("Case 3", E, [k1, k2, s1, s2])
    if sols:
        sol = sols[0]
        k1_eq = sp.simplify(sol[k1])
        k2_eq = sp.simplify(sol[k2])
        s1_eq = sp.simplify(sol[s1])
        s2_eq = sp.simplify(sol[s2])

        AB1, recip1 = reciprocal_status(k1_eq)
        AB2, recip2 = reciprocal_status(k2_eq)

        print()
        print(f"kappa_1_eq = {k1_eq}")
        print(f"kappa_2_eq = {k2_eq}")
        print(f"s_1_eq     = {s1_eq}")
        print(f"s_2_eq     = {s2_eq}")
        print(f"AB_1       = {AB1}")
        print(f"AB_2       = {AB2}")

        status_line("inner exterior kappa suppressed", k1_eq == 0)
        status_line("outer exterior kappa suppressed", k2_eq == 0)
        status_line("inner reciprocal scaling follows", recip1)
        status_line("outer reciprocal scaling follows", recip2)
        status_line("shear is active at inner shell", not is_zero(s1_eq))
        status_line("shear can propagate to outer shell", not is_zero(s2_eq))


# =============================================================================
# Case 4: Two-shell kappa boundary-source control
# =============================================================================

def case_4_kappa_boundary_source_control():
    header("Case 4: Two-shell kappa boundary-source control")

    k1, k2, s1, s2 = sp.symbols("kappa_1 kappa_2 s_1 s_2", real=True)
    M_k, K_k, M_s, K_s, S_b, K_b = sp.symbols(
        "M_k K_k M_s K_s S_b K_b", positive=True, real=True
    )

    # Control: same as Case 3 but the interface/source also pulls kappa_1
    # toward nonzero K_b. This should break reciprocal scaling unless
    # K_b=0 or the exterior suppression M_k is taken to an infinite limit.
    E_k = M_k**2 * ((k1 - K_b)**2 + k2**2) + K_k * (k2 - k1)**2
    E_s = M_s**2 * ((s1 - S_b)**2 + s2**2) + K_s * (s2 - s1)**2
    E = E_k + E_s

    _, sols = print_energy_result("Case 4", E, [k1, k2, s1, s2])
    if sols:
        sol = sols[0]
        k1_eq = sp.simplify(sol[k1])
        k2_eq = sp.simplify(sol[k2])
        s1_eq = sp.simplify(sol[s1])
        s2_eq = sp.simplify(sol[s2])

        AB1, recip1 = reciprocal_status(k1_eq)
        AB2, recip2 = reciprocal_status(k2_eq)

        print()
        print(f"kappa_1_eq = {k1_eq}")
        print(f"kappa_2_eq = {k2_eq}")
        print(f"s_1_eq     = {s1_eq}")
        print(f"s_2_eq     = {s2_eq}")
        print(f"AB_1       = {AB1}")
        print(f"AB_2       = {AB2}")

        status_line("inner kappa becomes nonzero generically", k1_eq != 0)
        status_line("outer kappa becomes nonzero generically", k2_eq != 0)
        status_line("inner reciprocal scaling fails generically", not recip1)
        status_line("outer reciprocal scaling fails generically", not recip2)
        print()
        print("Interpretation:")
        print("  If the source/interface directly seeds kappa into the exterior toy,")
        print("  reciprocal scaling is lost unless a further exterior constraint or")
        print("  boundary condition removes that kappa source.")


# =============================================================================
# Case 5: Interface shear source, exterior kappa source absent
# =============================================================================

def case_5_interface_shear_exterior_kappa_absent():
    header("Case 5: Interface shear source with exterior kappa source absent")

    k1, k2, s1, s2 = sp.symbols("kappa_1 kappa_2 s_1 s_2", real=True)
    M_k, K_k, K_s, S_b = sp.symbols("M_k K_k K_s S_b", positive=True, real=True)

    # This is the sharpest P7-style toy:
    #
    #   - Kappa has suppression and smoothing but no source.
    #   - Shear is seeded at the inner boundary/interface.
    #   - Shear has no mass term here, only boundary seed + gradient;
    #     to avoid a flat zero-mode degeneracy, pin the outer shear weakly to 0
    #     using the same boundary term K_s*s2^2.
    #
    # This is still a toy; it simply checks that source/interface shear can
    # coexist with exterior kappa=0.
    E_k = M_k**2 * (k1**2 + k2**2) + K_k * (k2 - k1)**2
    E_s = K_s * ((s1 - S_b)**2 + (s2 - s1)**2 + s2**2)
    E = E_k + E_s

    _, sols = print_energy_result("Case 5", E, [k1, k2, s1, s2])
    if sols:
        sol = sols[0]
        k1_eq = sp.simplify(sol[k1])
        k2_eq = sp.simplify(sol[k2])
        s1_eq = sp.simplify(sol[s1])
        s2_eq = sp.simplify(sol[s2])

        AB1, recip1 = reciprocal_status(k1_eq)
        AB2, recip2 = reciprocal_status(k2_eq)

        print()
        print(f"kappa_1_eq = {k1_eq}")
        print(f"kappa_2_eq = {k2_eq}")
        print(f"s_1_eq     = {s1_eq}")
        print(f"s_2_eq     = {s2_eq}")
        print(f"AB_1       = {AB1}")
        print(f"AB_2       = {AB2}")

        status_line("inner exterior kappa suppressed", k1_eq == 0)
        status_line("outer exterior kappa suppressed", k2_eq == 0)
        status_line("inner reciprocal scaling follows", recip1)
        status_line("outer reciprocal scaling follows", recip2)
        status_line("interface shear remains active", not is_zero(s1_eq))
        status_line("shear reaches outer shell", not is_zero(s2_eq))


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("This toy suite supports the following reduced-sector conclusions:")
    print()
    print("1. Kappa is the reciprocal-scaling control mode:")
    print("      AB = exp(2*kappa).")
    print()
    print("2. A source-free exterior functional can suppress kappa while allowing")
    print("   the shear/compensated mode s to remain active.")
    print()
    print("3. If kappa is directly sourced, reciprocal scaling fails generically.")
    print()
    print("4. The best P7-style toy is not 'all exchange is trace-free everywhere'.")
    print("   It is:")
    print("      source/interface physics may seed shear or boundary conditions,")
    print("      while the source-free exterior has no kappa source and relaxes")
    print("      kappa to zero.")
    print()
    print("5. This script still does not provide a covariant field equation.")
    print("   It only sharpens what such an equation must accomplish:")
    print()
    print("      derive exterior kappa suppression without imposing AB=1 directly,")
    print("      while allowing compensated shear to encode the exterior field.")


# =============================================================================
# Main
# =============================================================================

def main():
    header("Candidate Kappa-Suppression Functionals")
    case_0_algebraic_spine()
    case_1_local_potential()
    case_2_kappa_sourced_control()
    case_3_two_shell_exterior_relaxation()
    case_4_kappa_boundary_source_control()
    case_5_interface_shear_exterior_kappa_absent()
    final_interpretation()


if __name__ == "__main__":
    main()
