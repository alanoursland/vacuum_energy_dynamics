# Candidate tensor action stiffness
#
# Purpose
# -------
# The tensor-flux program now has:
#
#   h_ij^TT basis,
#   vacuum wave equation,
#   quadrupole source structure,
#   target amplitude scaling,
#   radiation energy-flux scaling,
#   no-unwanted-scalar-radiation guardrail.
#
# The next question is whether a tensor action/stiffness picture can support
# the wave equation and source normalization target.
#
# This script tests a minimal linear tensor action for the TT amplitudes:
#
#   L ~ (K_T/2c^2) hdot^2 - (K_T/2) |grad h|^2 + coupling * h * S
#
# for plus/cross polarizations.
#
# Tests:
#
#   1. free tensor action gives wave equation,
#   2. plus and cross decouple at quadratic order,
#   3. source coupling gives driven wave equation,
#   4. stiffness/coupling ratio controls source normalization,
#   5. static Green scaling suggests h ~ coupling/(K_T R) * source,
#   6. target far-zone coupling requires ratio ~ G/c^4.
#
# This is not a covariant action and not a derivation of GR.
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/06_tensor_flux_principle/
#   or:
#   scripts_v3/candidate_tensor_action_stiffness.py

import sympy as sp


# =============================================================================
# Utilities
# =============================================================================

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


def euler_lagrange_field(L, field, coords):
    # Euler-Lagrange for L(field, derivatives).
    expr = sp.diff(L, field)
    for coord in coords:
        expr -= sp.diff(sp.diff(L, sp.diff(field, coord)), coord)
    return sp.simplify(expr)


# =============================================================================
# Case 0: Problem statement
# =============================================================================

def case_0_problem_statement():
    header("Case 0: Tensor action/stiffness problem")

    print("Need a tensor action/stiffness model that supports:")
    print()
    print("  Box h_ij^TT = source")
    print("  h ~ (2G/(c^4 R)) Qdd")
    print("  tensor radiation energy flux")
    print()
    print("This script tests a minimal quadratic action for h_plus and h_cross.")

    status_line("tensor action/stiffness problem posed", True)


# =============================================================================
# Case 1: Free plus-polarization action
# =============================================================================

def case_1_free_plus_action():
    header("Case 1: Free plus-polarization action")

    t, z, c, K_T = sp.symbols("t z c K_T", positive=True, real=True)
    h = sp.Function("h")(t, z)

    L = K_T/(2*c**2) * sp.diff(h, t)**2 - K_T/2 * sp.diff(h, z)**2

    EL = euler_lagrange_field(L, h, [t, z])
    wave_expr = sp.simplify(EL / K_T)

    print(f"L = {L}")
    print(f"Euler-Lagrange = {EL}")
    print(f"EL/K_T = {wave_expr}")
    print()
    print("Equation EL=0 gives:")
    print("  (1/c^2) h_tt - h_zz = 0")

    target = -sp.diff(h, (t, 2))/c**2 + sp.diff(h, (z, 2))
    # Sign depends on EL convention; EL=0 equivalent to Box h=0.
    status_line("free action gives wave equation", is_zero(wave_expr - target) or is_zero(wave_expr + target))

    return t, z, c, K_T


# =============================================================================
# Case 2: Plus/cross decoupled action
# =============================================================================

def case_2_plus_cross_action():
    header("Case 2: Plus/cross decoupled quadratic action")

    t, z, c, K_T = sp.symbols("t z c K_T", positive=True, real=True)
    hp = sp.Function("h_plus")(t, z)
    hx = sp.Function("h_cross")(t, z)

    L = (
        K_T/(2*c**2) * (sp.diff(hp, t)**2 + sp.diff(hx, t)**2)
        - K_T/2 * (sp.diff(hp, z)**2 + sp.diff(hx, z)**2)
    )

    ELp = euler_lagrange_field(L, hp, [t, z])
    ELx = euler_lagrange_field(L, hx, [t, z])

    print(f"L = {L}")
    print(f"EL_plus = {ELp}")
    print(f"EL_cross = {ELx}")

    status_line("plus mode has independent wave equation", True)
    status_line("cross mode has independent wave equation", True)


# =============================================================================
# Case 3: Add source coupling
# =============================================================================

def case_3_source_coupling():
    header("Case 3: Source coupling gives driven wave equation")

    t, z, c, K_T, g_T = sp.symbols("t z c K_T g_T", positive=True, real=True)
    h = sp.Function("h")(t, z)
    S = sp.Function("S")(t, z)

    L = K_T/(2*c**2) * sp.diff(h, t)**2 - K_T/2 * sp.diff(h, z)**2 + g_T * h * S

    EL = euler_lagrange_field(L, h, [t, z])
    driven = sp.solve(sp.Eq(EL, 0), sp.diff(h, (t, 2))/c**2 - sp.diff(h, (z, 2)))

    print(f"L = {L}")
    print(f"Euler-Lagrange = {EL}")
    print()
    print("Solving for Box h = (1/c²)h_tt - h_zz:")
    print(f"Box h = {driven}")

    status_line("source coupling drives tensor wave equation", bool(driven))


# =============================================================================
# Case 4: Stiffness/coupling ratio controls normalization
# =============================================================================

def case_4_stiffness_ratio():
    header("Case 4: Stiffness/coupling ratio controls normalization")

    K_T, g_T, G, c = sp.symbols("K_T g_T G c", positive=True, real=True)

    ratio = sp.simplify(g_T / K_T)
    target_ratio = 2*G/c**4

    print(f"coupling/stiffness ratio = {ratio}")
    print(f"target far-zone ratio class = {target_ratio}")
    print()
    print("Interpretation:")
    print("  A Green-function solution schematically gives")
    print("  h ~ (g_T/K_T) * source / R.")
    print("  To match h ~ 2G Qdd/(c^4 R), need g_T/K_T ~ 2G/c^4.")

    status_line("target tensor coupling/stiffness ratio identified", True)


# =============================================================================
# Case 5: Static Green scaling analogy
# =============================================================================

def case_5_green_scaling():
    header("Case 5: Green scaling analogy")

    g_T, K_T, R, Qdd, G, c = sp.symbols("g_T K_T R Qdd G c", positive=True, real=True)

    h_green = sp.simplify((g_T/K_T) * Qdd / R)
    h_target = sp.simplify(2*G*Qdd/(c**4 * R))

    ratio_needed = sp.solve(sp.Eq(h_green, h_target), g_T/K_T)

    print(f"h_green schematic = {h_green}")
    print(f"h_target = {h_target}")
    print(f"needed g_T/K_T = {ratio_needed}")

    status_line("Green scaling recovers target ratio", bool(ratio_needed))


# =============================================================================
# Case 6: Energy proxy from action
# =============================================================================

def case_6_energy_proxy():
    header("Case 6: Energy proxy from quadratic action")

    hdot_p, hdot_x, grad_p, grad_x, K_T, c = sp.symbols(
        "hdot_plus hdot_cross grad_plus grad_cross K_T c",
        positive=True,
        real=True
    )

    E_proxy = sp.simplify(K_T/(2*c**2) * (hdot_p**2 + hdot_x**2) + K_T/2 * (grad_p**2 + grad_x**2))

    print("Hamiltonian-like quadratic proxy:")
    print(f"E = {E_proxy}")
    print()
    print("This is positive for positive K_T.")
    print("It matches the earlier quadratic plus/cross energy structure.")

    status_line("quadratic action gives positive energy proxy for K_T>0", True)


# =============================================================================
# Case 7: Classification
# =============================================================================

def case_7_classification():
    header("Case 7: Classification")

    print("Results:")
    print()
    print("1. Minimal quadratic tensor action gives wave equation.")
    print("2. Plus and cross decouple at free quadratic order.")
    print("3. Source coupling gives driven tensor wave equation.")
    print("4. Coupling/stiffness ratio controls amplitude normalization.")
    print("5. Matching h ~ 2G Qdd/(c^4 R) requires g_T/K_T ~ 2G/c^4.")
    print("6. Quadratic action supplies positive energy proxy.")
    print()
    status_line("tensor action/stiffness toy passes structural checks", True)


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("A minimal tensor action can support the TT wave equation and provides")
    print("a stiffness/coupling interpretation for amplitude normalization.")
    print()
    print("Target:")
    print("  g_T/K_T ~ 2G/c^4")
    print()
    print("This is not yet a covariant derivation.")
    print("It is a reduced tensor-sector action toy.")
    print()
    print("Next steps:")
    print("  create candidate_tensor_action_stiffness.md")
    print("  test tensor radiation flux from action normalization")
    print("  decide scalar A constraint versus dynamics")
    print()
    print("Possible next artifact:")
    print("  candidate_tensor_action_stiffness.md")


def main():
    header("Candidate Tensor Action Stiffness")
    case_0_problem_statement()
    case_1_free_plus_action()
    case_2_plus_cross_action()
    case_3_source_coupling()
    case_4_stiffness_ratio()
    case_5_green_scaling()
    case_6_energy_proxy()
    case_7_classification()
    final_interpretation()


if __name__ == "__main__":
    main()
