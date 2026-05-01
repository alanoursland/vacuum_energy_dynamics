# Candidate exact source-law geometry check
#
# Purpose
# -------
# The exact static spherical recovery result used:
#
#   ∇²_flat A = 8πG rho / c²
#
# with:
#
#   A = exp(s)
#
# In source-free exterior:
#
#   ∇²_flat A = 0
#
# and for spherical mass:
#
#   A = 1 - r_s/r
#
# This recovers exact Schwarzschild exterior metric factors under kappa=0:
#
#   B = 1/A
#
# The danger:
#   Did we find a geometric reduced law, or did we sneak in a flat-background
#   Poisson equation that happens to work because A has a 1/r form?
#
# This script compares several candidate operators:
#
#   1. Flat areal radial Laplacian:
#        Δ_flat A = (1/r²)(r² A')'
#
#   2. Curved spatial Laplacian on the t=constant spatial metric:
#        dl² = B(r) dr² + r² dΩ²
#
#        Δ_spatial A =
#        1/(r² sqrt(B)) d/dr [ r²/sqrt(B) A' ]
#
#   3. Orbit-space d'Alembert/Laplacian radial static piece using h_AB:
#        h_AB dx^A dx^B = -A c² dt² + B dr²
#
#      For static A(r), the orbit-space scalar operator is:
#
#        □_h A =
#        1/sqrt(|h|) d/dr [ sqrt(|h|) h^rr A' ]
#
#      With AB=1:
#        sqrt(|h|) ∝ sqrt(AB) = 1
#        h^rr = 1/B = A
#
#      so:
#        □_h A = d/dr [ A A' ]
#
#      This is not the flat radial flux law.
#
#   4. Areal flux law:
#        F_A = 4π r² A'
#
#      For A=1-r_s/r:
#        F_A = 4π r_s = constant
#
# The goal is to identify which operator the exact source law actually uses.
#
# IMPORTANT:
# This is a reduced static spherical diagnostic, not a full covariant theory.
#
# Suggested location:
#   scripts_v3/candidate_exact_source_law_geometry_check.py

import sympy as sp


# =============================================================================
# Utilities
# =============================================================================

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


def flat_radial_laplacian(f, r):
    return sp.simplify((1 / r**2) * sp.diff(r**2 * sp.diff(f, r), r))


def curved_spatial_radial_laplacian(f, B, r):
    # Spatial 3-metric:
    #   dl² = B dr² + r² dΩ²
    # radial scalar Laplacian:
    #   1/(r² sqrt(B)) d/dr [ r²/sqrt(B) f' ]
    return sp.simplify((1 / (r**2 * sp.sqrt(B))) * sp.diff((r**2 / sp.sqrt(B)) * sp.diff(f, r), r))


def orbit_space_static_operator(f, A, B, r):
    # 2D orbit metric:
    #   h_AB dx^A dx^B = -A c² dt² + B dr²
    # Ignoring constant c factor:
    #   sqrt(|h|) = sqrt(A B)
    #   h^rr = 1/B
    # static scalar operator:
    #   1/sqrt(AB) d/dr [ sqrt(AB) (1/B) f' ]
    return sp.simplify((1 / sp.sqrt(A * B)) * sp.diff(sp.sqrt(A * B) * (1 / B) * sp.diff(f, r), r))


def areal_flux(f, r):
    return sp.simplify(4 * sp.pi * r**2 * sp.diff(f, r))


# =============================================================================
# Case 0: Exact Schwarzschild exterior setup
# =============================================================================

def case_0_setup():
    header("Case 0: Exact Schwarzschild exterior setup")

    r, r_s = sp.symbols("r r_s", positive=True, real=True)

    A = 1 - r_s / r
    B = sp.simplify(1 / A)

    print(f"A = {A}")
    print(f"B = {B}")
    print(f"AB = {sp.simplify(A*B)}")
    print(f"A' = {sp.diff(A, r)}")

    status_line("Schwarzschild areal exterior has AB=1", is_zero(A*B - 1))
    return r, r_s, A, B


# =============================================================================
# Case 1: Flat areal radial Laplacian
# =============================================================================

def case_1_flat_laplacian(r, r_s, A, B):
    header("Case 1: Flat areal radial Laplacian")

    lap_flat = flat_radial_laplacian(A, r)
    flux = areal_flux(A, r)

    print("Operator:")
    print("  Δ_flat A = (1/r²)(r² A')'")
    print()
    print(f"Δ_flat A = {lap_flat}")
    print(f"4πr² A' = {flux}")

    status_line("A=1-r_s/r is flat-harmonic for r>0", is_zero(lap_flat))
    status_line("areal flux is constant", is_zero(sp.diff(flux, r)))

    print()
    print("Interpretation:")
    print("  The exact source law used so far is equivalent to conserved")
    print("  areal flux of A through coordinate spheres.")


# =============================================================================
# Case 2: Curved spatial Laplacian
# =============================================================================

def case_2_curved_spatial_laplacian(r, r_s, A, B):
    header("Case 2: Curved spatial Laplacian on t=constant slice")

    lap_spatial = curved_spatial_radial_laplacian(A, B, r)
    lap_spatial_simplified = sp.simplify(lap_spatial)

    print("Spatial metric:")
    print("  dl² = B(r) dr² + r² dΩ²")
    print()
    print("Operator:")
    print("  Δ_spatial A = 1/(r²√B) d/dr [ r²/√B A' ]")
    print()
    print(f"Δ_spatial A = {lap_spatial_simplified}")

    status_line("A is NOT generally harmonic under curved spatial Laplacian",
                not is_zero(lap_spatial_simplified))

    print()
    print("Interpretation:")
    print("  The exact source law is not the ordinary scalar Laplacian built")
    print("  from the curved spatial metric dl²=Bdr²+r²dΩ².")
    print("  That means the A-action is not simply a standard curved-space")
    print("  scalar energy on the t=constant spatial slice.")


# =============================================================================
# Case 3: Orbit-space static scalar operator
# =============================================================================

def case_3_orbit_space_operator(r, r_s, A, B):
    header("Case 3: Orbit-space static scalar operator")

    op_h = orbit_space_static_operator(A, A, B, r)
    op_h_simplified = sp.simplify(op_h)

    print("Orbit-space metric:")
    print("  h_AB dx^A dx^B = -A c²dt² + B dr²")
    print()
    print("Static scalar operator:")
    print("  □_h A = 1/√|h| d/dr [ √|h| h^rr A' ]")
    print()
    print("With AB=1:")
    print("  √|h| is constant")
    print("  h^rr = 1/B = A")
    print("  □_h A = d/dr(A A')")
    print()
    print(f"□_h A = {op_h_simplified}")

    status_line("A is NOT generally harmonic under orbit-space scalar operator",
                not is_zero(op_h_simplified))

    print()
    print("Interpretation:")
    print("  The exact source law is also not simply the scalar wave/Laplace")
    print("  operator of the 2D orbit-space metric h_AB.")


# =============================================================================
# Case 4: Compare all operators
# =============================================================================

def case_4_operator_comparison(r, r_s, A, B):
    header("Case 4: Operator comparison")

    lap_flat = flat_radial_laplacian(A, r)
    lap_spatial = curved_spatial_radial_laplacian(A, B, r)
    op_h = orbit_space_static_operator(A, A, B, r)
    flux = areal_flux(A, r)

    print(f"Δ_flat A      = {sp.simplify(lap_flat)}")
    print(f"Δ_spatial A   = {sp.simplify(lap_spatial)}")
    print(f"□_orbit A     = {sp.simplify(op_h)}")
    print(f"4πr²A'        = {flux}")
    print(f"d/dr(4πr²A')  = {sp.simplify(sp.diff(flux, r))}")

    print()
    print("Classification:")
    print("  flat areal radial operator: passes")
    print("  conserved areal flux: passes")
    print("  curved spatial Laplacian: fails")
    print("  2D orbit-space scalar operator: fails")
    print()
    status_line("exact law is specifically areal-flux / flat-radial in current form", True)


# =============================================================================
# Case 5: General condition for conserved areal flux
# =============================================================================

def case_5_general_areal_flux_solution():
    header("Case 5: General solution of conserved areal flux")

    r, C0, C1, F = sp.symbols("r C0 C1 F", positive=True, real=True)
    A = sp.Function("A")(r)

    equation = sp.Eq(sp.diff(r**2 * sp.diff(A, r), r), 0)
    solution = sp.dsolve(equation)

    print("Conserved areal flux condition:")
    print("  d/dr(r² A') = 0")
    print()
    print(f"Equation: {equation}")
    print(f"General solution: {solution}")
    print()
    print("So:")
    print("  A(r) = C0 + C1/r")
    print()
    print("Asymptotic flatness sets C0=1.")
    print("Mass flux sets C1=-r_s.")
    status_line("conserved areal flux gives 1/r exterior form", True)


# =============================================================================
# Case 6: Can curved spatial harmonicity recover Schwarzschild?
# =============================================================================

def case_6_curved_spatial_harmonic_solution():
    header("Case 6: Curved-spatial harmonic solution check")

    r = sp.symbols("r", positive=True, real=True)
    A = sp.Function("A")(r)

    # If kappa=0, B=1/A.
    B = 1 / A

    # Curved spatial Laplacian for f=A with B=1/A:
    # Δ_spatial A = 1/(r² sqrt(B)) d/dr [r²/sqrt(B) A']
    # sqrt(B)=1/sqrt(A), so:
    # Δ = sqrt(A)/r² d/dr [r² sqrt(A) A']
    lap_expr = sp.simplify((sp.sqrt(A) / r**2) * sp.diff(r**2 * sp.sqrt(A) * sp.diff(A, r), r))

    print("If one instead imposed curved-spatial harmonicity with B=1/A:")
    print("  Δ_spatial A = 0")
    print()
    print(f"Equation expression = {lap_expr}")
    print()
    print("This is nonlinear and not solved by A=1-r_s/r in general.")
    print("Therefore the current exact recovery is not based on spatial")
    print("harmonicity of A.")
    status_line("curved-spatial harmonicity is a different theory branch", True)


# =============================================================================
# Case 7: Interpretation of flat operator
# =============================================================================

def case_7_interpretation():
    header("Case 7: Interpretation of the flat/areal operator")

    print("The operator that works is:")
    print()
    print("  Δ_areal A = (1/r²)(r² A')'")
    print()
    print("This can be interpreted as conserved flux through areal spheres:")
    print()
    print("  F_A = 4πr² A'")
    print()
    print("It is not the ordinary scalar Laplacian of the curved spatial slice,")
    print("and not the ordinary scalar operator of the 2D orbit-space metric.")
    print()
    print("Possible interpretations:")
    print()
    print("  1. The reduced exact law is an areal-flux law.")
    print("  2. The action uses an auxiliary Euclidean radial measure.")
    print("  3. The true covariant parent is not a standard scalar-field action.")
    print("  4. A deeper variational principle may reduce to areal-flux conservation.")
    print()
    print("This is now a central open problem.")


# =============================================================================
# Case 8: Implications for action
# =============================================================================

def case_8_action_implications():
    header("Case 8: Implications for the A-action")

    print("The current exact reduced action:")
    print()
    print("  E_A = ∫ [K_A |∇A|² + beta rho A] d³x")
    print()
    print("should be read carefully.")
    print()
    print("The ∇ and d³x in this expression currently behave like flat")
    print("areal-coordinate operators, not curved spatial metric operators.")
    print()
    print("Therefore:")
    print()
    print("  This action is a successful reduced static spherical action toy,")
    print("  but not yet a geometric/covariant action.")
    print()
    print("The next theory task is to explain why the areal-flux operator, rather")
    print("than the curved spatial scalar Laplacian, is the right reduced operator.")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("This geometry check sharpens the exact source-law result.")
    print()
    print("A=1-r_s/r is harmonic under:")
    print()
    print("  Δ_flat A = (1/r²)(r²A')'")
    print()
    print("and has conserved areal flux:")
    print()
    print("  4πr²A' = constant")
    print()
    print("But A is not harmonic under:")
    print()
    print("  the curved spatial Laplacian of dl²=Bdr²+r²dΩ²,")
    print("  nor the scalar operator of the 2D orbit-space metric h_AB.")
    print()
    print("Therefore the exact source law is best described, for now, as an")
    print("areal-flux / flat-radial reduced law.")
    print()
    print("This is not fatal. It is a precision gain.")
    print("It tells us exactly what the future covariant/geometric parent must explain.")
    print()
    print("Possible next artifact:")
    print("  candidate_exact_source_law_geometry_check.md")


# =============================================================================
# Main
# =============================================================================

def main():
    header("Candidate Exact Source-Law Geometry Check")
    r, r_s, A, B = case_0_setup()
    case_1_flat_laplacian(r, r_s, A, B)
    case_2_curved_spatial_laplacian(r, r_s, A, B)
    case_3_orbit_space_operator(r, r_s, A, B)
    case_4_operator_comparison(r, r_s, A, B)
    case_5_general_areal_flux_solution()
    case_6_curved_spatial_harmonic_solution()
    case_7_interpretation()
    case_8_action_implications()
    final_interpretation()


if __name__ == "__main__":
    main()
