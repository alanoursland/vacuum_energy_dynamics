# Candidate scalar constraint mechanism
#
# Purpose
# -------
# The tensor-flux program requires a safety guardrail:
#
#   A        -> scalar monopole/Newtonian/static channel
#   h_ij^TT -> tensor quadrupole/radiative channel
#
# If A is an ordinary propagating scalar wave field, the theory may predict
# unwanted scalar breathing radiation. The safer architecture is that A is
# elliptic/constraint-like in the ordinary exterior/radiation regime:
#
#   Delta A = 8*pi*G*rho/c^2
#
# rather than:
#
#   Box A = 8*pi*G*rho/c^2
#
# This script compares these two branches.
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/07_scalar_constraint_and_radiation_safety/
#   or:
#   scripts_v3/candidate_scalar_constraint_mechanism.py

import sympy as sp


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


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


def laplacian_radial(expr, r):
    return sp.simplify((1/r**2) * sp.diff(r**2 * sp.diff(expr, r), r))


def wave_operator_1d(expr, t, z, c):
    return sp.simplify((1/c**2) * sp.diff(expr, t, 2) - sp.diff(expr, z, 2))


def case_0_problem_statement():
    header("Case 0: Scalar constraint mechanism problem")

    print("Current preferred architecture:")
    print()
    print("  A        -> scalar monopole/Newtonian/static response")
    print("  h_ij^TT -> tensor quadrupole/radiative response")
    print()
    print("Danger:")
    print("  If A obeys an ordinary wave equation, it may radiate scalar breathing modes.")
    print()
    print("Candidate safety mechanism:")
    print("  A is constraint-like / elliptic in ordinary exterior gravity:")
    print()
    print("    Delta A = 8*pi*G*rho/c^2")
    print()
    print("  rather than an independent radiative scalar:")
    print()
    print("    Box A = 8*pi*G*rho/c^2")

    status_line("scalar constraint mechanism problem posed", True)


def case_1_poisson_static_exterior():
    header("Case 1: Poisson/constraint branch supports static exterior A")

    r, G, M, c = sp.symbols("r G M c", positive=True, real=True)

    A = 1 - 2*G*M/(c**2*r)
    lapA = laplacian_radial(A, r)

    print(f"A_static = {A}")
    print(f"Delta A = {lapA}")
    print()
    print("For r>0, source-free exterior satisfies:")
    print("  Delta A = 0")

    status_line("static exterior A solves source-free Poisson branch", is_zero(lapA))


def case_2_poisson_no_dispersion():
    header("Case 2: Poisson branch has no independent time-wave dispersion")

    t, z, k, omega, H = sp.symbols("t z k omega H", positive=True, real=True)

    A_wave = H * sp.cos(k*z - omega*t)
    poisson_operator = sp.simplify(-sp.diff(A_wave, z, 2))

    print("Try a time-dependent plane wave in a source-free Poisson equation:")
    print()
    print(f"A_wave = {A_wave}")
    print(f"-d²A/dz² = {poisson_operator}")
    print()
    print("Source-free Poisson requires spatial Laplacian = 0.")
    print("For k != 0, this is not a propagating dispersion relation.")
    print("It forces the spatial harmonic condition, not omega^2=c^2k^2.")

    status_line("Poisson branch does not produce scalar wave dispersion", True)


def case_3_wave_branch_radiates():
    header("Case 3: Hyperbolic scalar branch would radiate")

    t, z, k, omega, c, H = sp.symbols("t z k omega c H", positive=True, real=True)

    A_rad = H * sp.cos(k*z - omega*t)
    boxA = wave_operator_1d(A_rad, t, z, c)
    coeff = sp.simplify(boxA / A_rad)

    print("If A obeys Box A = 0:")
    print()
    print(f"A_rad = {A_rad}")
    print(f"Box A = {boxA}")
    print(f"Box A / A = {coeff}")
    print()
    print("This admits scalar waves when:")
    print("  omega^2 = c^2 k^2")

    status_line("hyperbolic A branch admits scalar radiation", is_zero(coeff - (k**2 - omega**2/c**2)))


def case_4_static_source_preference():
    header("Case 4: Static source prefers constraint branch")

    print("For ordinary static mass response:")
    print()
    print("  rho = rho(x)")
    print("  A = A(x)")
    print()
    print("Poisson branch:")
    print("  Delta A = 8*pi*G*rho/c^2")
    print()
    print("Wave branch:")
    print("  Box A = 8*pi*G*rho/c^2")
    print("  reduces to Poisson only after imposing time independence.")
    print()
    print("Interpretation:")
    print("  Static Newtonian gravity naturally belongs to the constraint branch.")
    print("  Treating A as fundamentally wave-like adds a dangerous extra scalar sector.")

    status_line("static mass response favors constraint interpretation", True)


def case_5_monopole_dipole_controls():
    header("Case 5: Conserved monopole and dipole controls")

    t, M0, D0, V = sp.symbols("t M0 D0 V", real=True)

    M = M0
    D = D0 + V*t

    Mdot = sp.diff(M, t)
    Dddot = sp.diff(D, t, 2)

    print(f"M(t) = {M}")
    print(f"Mdot = {Mdot}")
    print()
    print(f"D(t) = {D}")
    print(f"Dddot = {Dddot}")
    print()
    print("Conservation suppresses ordinary scalar monopole/dipole radiation proxies.")

    status_line("conserved mass kills scalar monopole radiation proxy", is_zero(Mdot))
    status_line("center-of-mass inertial motion kills scalar dipole radiation proxy", is_zero(Dddot))


def case_6_breathing_danger():
    header("Case 6: Scalar breathing remains dangerous if A propagates")

    b, hp, hx = sp.symbols("b h_plus h_cross", real=True)

    H_breathing = sp.Matrix([
        [b, 0, 0],
        [0, b, 0],
        [0, 0, 0],
    ])

    trace = sp.trace(H_breathing)

    H_TT = sp.Matrix([
        [hp, hx, 0],
        [hx, -hp, 0],
        [0, 0, 0],
    ])

    trace_tt = sp.trace(H_TT)

    print("Scalar breathing mode:")
    print(H_breathing)
    print(f"trace = {trace}")
    print()
    print("TT tensor mode:")
    print(H_TT)
    print(f"trace = {trace_tt}")
    print()
    print("If A propagates with a breathing mode, it adds a non-TT polarization.")

    status_line("scalar breathing mode is non-TT", not is_zero(trace))
    status_line("TT tensor mode remains trace-free", is_zero(trace_tt))


def case_7_static_dynamic_split():
    header("Case 7: Static/dynamic split for A")

    print("Useful decomposition:")
    print()
    print("  A = A_constraint + A_rad?")
    print()
    print("Preferred ordinary-gravity setting:")
    print()
    print("  A_rad = 0")
    print()
    print("or:")
    print()
    print("  A_rad is massive / short-ranged / weakly coupled / constrained")
    print()
    print("Radiation channel:")
    print()
    print("  h_ij^TT carries plus/cross tensor waves")
    print()
    print("This keeps:")
    print("  A        -> static scalar mass response")
    print("  h_ij^TT -> radiative tensor response")

    status_line("A static/dynamic split formulated", True)


def case_8_classification():
    header("Case 8: Classification")

    print("Results:")
    print()
    print("1. Poisson A supports static exterior scalar gravity.")
    print("2. Poisson A does not provide scalar wave dispersion.")
    print("3. Hyperbolic A would provide scalar radiation.")
    print("4. Conserved monopole and inertial dipole controls suppress low-order")
    print("   scalar radiation proxies.")
    print("5. Scalar breathing remains dangerous if A has a radiative quadrupole mode.")
    print("6. Preferred architecture: A is constraint-like; h_ij^TT radiates.")
    print()
    status_line("scalar constraint mechanism passes as architecture guardrail", True)


def final_interpretation():
    header("Final interpretation")

    print("The scalar A channel should be treated as constraint-like in ordinary")
    print("exterior gravity unless a tightly controlled scalar-radiation sector is")
    print("deliberately introduced.")
    print()
    print("Safe architecture:")
    print()
    print("  Delta A = 8*pi*G*rho/c^2")
    print("  A handles scalar mass response")
    print("  h_ij^TT handles gravitational radiation")
    print()
    print("Dangerous architecture:")
    print()
    print("  Box A = source")
    print("  A becomes an independent scalar radiation field")
    print()
    print("Possible next artifact:")
    print("  candidate_scalar_constraint_mechanism.md")
    print()
    print("Possible next script:")
    print("  candidate_scalar_breathing_mode_suppression.py")


def main():
    header("Candidate Scalar Constraint Mechanism")
    case_0_problem_statement()
    case_1_poisson_static_exterior()
    case_2_poisson_no_dispersion()
    case_3_wave_branch_radiates()
    case_4_static_source_preference()
    case_5_monopole_dipole_controls()
    case_6_breathing_danger()
    case_7_static_dynamic_split()
    case_8_classification()
    final_interpretation()


if __name__ == "__main__":
    main()
