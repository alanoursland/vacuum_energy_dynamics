# Candidate source coupling normalization
#
# Purpose
# -------
# The boundary flux action found that a source/interface coupling:
#
#   E_boundary = -q A(R)
#
# produces the boundary condition:
#
#   2 K_A R^2 A'(R) = q
#
# Therefore:
#
#   F_A(R) = 4*pi*R^2 A'(R) = 2*pi*q/K_A
#
# To recover Schwarzschild exterior:
#
#   F_A = 8*pi*G*M/c^2
#
# so:
#
#   q_M = 4 K_A G M / c^2
#
# This script checks how that normalization follows from:
#
#   1. weak-field Newtonian matching,
#   2. Schwarzschild radius coefficient,
#   3. boundary momentum normalization,
#   4. dimensional reduced charge structure,
#   5. additivity in mass.
#
# It does not derive K_A from first principles.
#
# Suggested location:
#   scripts_v3/candidate_source_coupling_normalization.py

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


def case_0_boundary_relation():
    header("Case 0: Boundary relation recap")

    R, K_A, q = sp.symbols("R K_A q", positive=True, real=True)

    Aprime = q/(2*K_A*R**2)
    flux = sp.simplify(4*sp.pi*R**2*Aprime)

    print("Boundary condition from action:")
    print()
    print("  2 K_A R^2 A'(R) = q")
    print()
    print(f"A'(R) = {Aprime}")
    print(f"F_A = 4*pi*R^2*A'(R) = {flux}")

    status_line("boundary charge q fixes A-flux", True)


def case_1_newtonian_matching():
    header("Case 1: Weak-field Newtonian matching")

    r, G, M, c, F = sp.symbols("r G M c F", positive=True, real=True)

    # Exterior conserved flux:
    #   4π r² A' = F
    # so A' = F/(4πr²)
    # with A(∞)=1:
    #   A = 1 - F/(4π r)
    # Weak field requires:
    #   A = 1 + 2 Phi/c² = 1 - 2GM/(c²r)
    A_from_flux = 1 - F/(4*sp.pi*r)
    A_target = 1 - 2*G*M/(c**2*r)

    F_solution = sp.solve(sp.Eq(A_from_flux, A_target), F)

    print(f"A_from_flux = {A_from_flux}")
    print(f"A_target Newtonian = {A_target}")
    print(f"F solution = {F_solution}")

    status_line("Newtonian matching fixes F_A=8πGM/c²",
                bool(F_solution) and is_zero(F_solution[0] - 8*sp.pi*G*M/c**2))


def case_2_boundary_charge_from_flux():
    header("Case 2: Boundary charge from flux")

    K_A, G, M, c = sp.symbols("K_A G M c", positive=True, real=True)

    F_target = 8*sp.pi*G*M/c**2
    q_from_flux = sp.simplify(K_A * F_target / (2*sp.pi))
    q_target = 4*K_A*G*M/c**2

    print(f"F_target = {F_target}")
    print("Since F_A = 2*pi*q/K_A:")
    print(f"q = K_A*F/(2*pi) = {q_from_flux}")
    print(f"q_target = {q_target}")

    status_line("boundary charge normalization follows from Newtonian flux",
                is_zero(q_from_flux - q_target))


def case_3_schwarzschild_radius_matching():
    header("Case 3: Schwarzschild radius coefficient matching")

    r, r_s, G, M, c, F = sp.symbols("r r_s G M c F", positive=True, real=True)

    A = 1 - r_s/r
    flux = sp.simplify(4*sp.pi*r**2*sp.diff(A, r))
    F_target = 8*sp.pi*G*M/c**2

    rs_solution = sp.solve(sp.Eq(flux, F_target), r_s)

    print(f"A = {A}")
    print(f"F_A = {flux}")
    print(f"F_target = {F_target}")
    print(f"r_s solution = {rs_solution}")

    status_line("flux normalization fixes r_s=2GM/c²",
                bool(rs_solution) and is_zero(rs_solution[0] - 2*G*M/c**2))


def case_4_additivity():
    header("Case 4: Additivity in mass")

    K_A, G, c, M1, M2 = sp.symbols("K_A G c M1 M2", positive=True, real=True)

    q = lambda M: 4*K_A*G*M/c**2
    F = lambda M: 8*sp.pi*G*M/c**2

    q_total = sp.simplify(q(M1 + M2))
    q_sum = sp.simplify(q(M1) + q(M2))

    F_total = sp.simplify(F(M1 + M2))
    F_sum = sp.simplify(F(M1) + F(M2))

    print(f"q(M1+M2) = {q_total}")
    print(f"q(M1)+q(M2) = {q_sum}")
    print()
    print(f"F(M1+M2) = {F_total}")
    print(f"F(M1)+F(M2) = {F_sum}")

    status_line("boundary charge is additive in mass", is_zero(q_total - q_sum))
    status_line("flux is additive in mass", is_zero(F_total - F_sum))


def case_5_energy_coupling_interpretation():
    header("Case 5: Energy coupling interpretation")

    K_A, G, M, c, A_R = sp.symbols("K_A G M c A_R", positive=True, real=True)

    q_M = 4*K_A*G*M/c**2
    E_boundary = -q_M*A_R

    print("Boundary coupling:")
    print()
    print(f"q_M = {q_M}")
    print(f"E_boundary = {E_boundary}")
    print()
    print("Interpretation:")
    print("  q_M has length-like mass coupling GM/c² multiplied by K_A.")
    print("  The exact coefficient is fixed by Newtonian/Schwarzschild matching.")
    print("  K_A remains a reduced stiffness/normalization parameter.")
    print()
    status_line("source coupling can be normalized by weak-field matching", True)


def case_6_what_is_not_derived():
    header("Case 6: What remains underived")

    print("The script fixes q_M from required weak-field/exterior matching.")
    print()
    print("It does NOT derive:")
    print("  K_A from vacuum microphysics,")
    print("  why matter couples to A rather than another variable,")
    print("  why the boundary action is exactly -q A(R),")
    print("  how pressure/stress modifies q or sources kappa,")
    print("  a full covariant source action.")
    print()
    status_line("normalization is matched, not fundamental yet", True)


def final_interpretation():
    header("Final interpretation")

    print("The boundary charge normalization is not arbitrary once the")
    print("weak-field Newtonian limit is imposed.")
    print()
    print("Exterior flux gives:")
    print("  A = 1 - F_A/(4*pi*r)")
    print()
    print("Newtonian matching requires:")
    print("  F_A = 8*pi*G*M/c^2")
    print()
    print("The boundary relation F_A = 2*pi*q/K_A then requires:")
    print("  q_M = 4*K_A*G*M/c^2")
    print()
    print("This explains the coefficient at the reduced matching level,")
    print("but does not yet derive the coupling from deeper principles.")
    print()
    print("Possible next artifact:")
    print("  candidate_source_coupling_normalization.md")


def main():
    header("Candidate Source Coupling Normalization")
    case_0_boundary_relation()
    case_1_newtonian_matching()
    case_2_boundary_charge_from_flux()
    case_3_schwarzschild_radius_matching()
    case_4_additivity()
    case_5_energy_coupling_interpretation()
    case_6_what_is_not_derived()
    final_interpretation()


if __name__ == "__main__":
    main()
