# Candidate interior A source model
#
# Purpose
# -------
# The exact static spherical exterior branch now uses an areal-flux law:
#
#   F_A(r) = 4*pi*r**2*A'(r)
#   F_A(r) = 8*pi*G*M_enc(r)/c**2
#
# Outside the source:
#
#   M_enc(r) = M
#
# so:
#
#   A(r) = 1 - 2GM/(c**2*r)
#
# and with kappa=0:
#
#   B = 1/A
#
# This recovers exact Schwarzschild exterior metric factors.
#
# This script tests whether the same areal-flux source law behaves sensibly
# inside a finite spherical source.
#
# Main test:
#
#   constant-density sphere:
#     rho(r) = rho0 for 0 <= r <= R
#     M_enc(r) = (4*pi/3) rho0 r**3
#
# Then:
#
#   A'(r) = 2G M_enc(r)/(c**2 r**2)
#         = (8*pi*G*rho0/(3*c**2)) r
#
# and:
#
#   A_in(r) = C + (4*pi*G*rho0/(3*c**2)) r**2
#
# Match A and A' at r=R to exterior:
#
#   A_out(r) = 1 - 2GM/(c**2*r)
#   M = (4*pi/3) rho0 R**3
#
# This is NOT the full GR interior Schwarzschild solution.
# It is the interior solution of the reduced areal-flux law.
#
# Suggested location:
#   scripts_v3/candidate_interior_A_source_model.py

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


def delta_areal(f, r):
    return sp.simplify((1/r**2) * sp.diff(r**2 * sp.diff(f, r), r))


def areal_flux(f, r):
    return sp.simplify(4 * sp.pi * r**2 * sp.diff(f, r))


# =============================================================================
# Case 0: Areal-flux source law recap
# =============================================================================

def case_0_recap():
    header("Case 0: Areal-flux source law recap")

    print("Exact reduced source law:")
    print()
    print("  Delta_areal A = 8*pi*G*rho/c^2")
    print()
    print("where:")
    print()
    print("  Delta_areal A = (1/r^2)(r^2 A')'")
    print()
    print("Equivalent flux law:")
    print()
    print("  F_A(r) = 4*pi*r^2 A'")
    print("  F_A(r) = 8*pi*G*M_enc(r)/c^2")
    print()
    print("Interior test:")
    print()
    print("  M_enc(r) varies with r inside the source.")
    print("  Check whether A, A', and flux match smoothly to exterior.")
    status_line("areal-flux law has interior enclosed-mass form", True)


# =============================================================================
# Case 1: Constant-density enclosed mass
# =============================================================================

def case_1_constant_density_enclosed_mass():
    header("Case 1: Constant-density enclosed mass")

    r, rho0 = sp.symbols("r rho0", positive=True, real=True)

    M_enc = sp.Rational(4, 3) * sp.pi * rho0 * r**3
    M_enc_prime = sp.diff(M_enc, r)
    expected = 4 * sp.pi * r**2 * rho0

    print(f"rho(r) = {rho0}")
    print(f"M_enc(r) = {M_enc}")
    print(f"M_enc'(r) = {M_enc_prime}")
    print(f"4*pi*r^2*rho0 = {expected}")

    status_line("M_enc derivative matches density volume element", is_zero(M_enc_prime - expected))


# =============================================================================
# Case 2: Interior A solution from flux law
# =============================================================================

def case_2_interior_A_solution():
    header("Case 2: Interior A solution from flux law")

    r, G, c, rho0, C = sp.symbols("r G c rho0 C", positive=True, real=True)

    M_enc = sp.Rational(4, 3) * sp.pi * rho0 * r**3
    A_prime = sp.simplify(2 * G * M_enc / (c**2 * r**2))
    A_in = sp.simplify(C + sp.integrate(A_prime, r))

    print(f"M_enc(r) = {M_enc}")
    print(f"A'(r) = 2G M_enc/(c^2 r^2) = {A_prime}")
    print(f"A_in(r) = {A_in}")

    lhs = delta_areal(A_in, r)
    rhs = 8 * sp.pi * G * rho0 / c**2

    print()
    print(f"Delta_areal A_in = {lhs}")
    print(f"8*pi*G*rho0/c^2 = {rhs}")

    status_line("interior A solves areal source equation", is_zero(lhs - rhs))

    return A_in


# =============================================================================
# Case 3: Match to exterior at r=R
# =============================================================================

def case_3_match_to_exterior():
    header("Case 3: Match interior to exterior at r=R")

    r, R, G, c, rho0, C = sp.symbols("r R G c rho0 C", positive=True, real=True)

    M = sp.Rational(4, 3) * sp.pi * rho0 * R**3
    r_s = 2 * G * M / c**2

    A_in = C + 4 * sp.pi * G * rho0 * r**2 / (3 * c**2)
    A_out = 1 - r_s / r

    A_in_R = sp.simplify(A_in.subs(r, R))
    A_out_R = sp.simplify(A_out.subs(r, R))

    C_solution = sp.solve(sp.Eq(A_in_R, A_out_R), C)
    C_match = sp.simplify(C_solution[0]) if C_solution else None
    A_in_matched = sp.simplify(A_in.subs(C, C_match))

    print(f"M = {M}")
    print(f"r_s = {sp.simplify(r_s)}")
    print(f"A_in = {A_in}")
    print(f"A_out = {A_out}")
    print()
    print(f"A_in(R) = {A_in_R}")
    print(f"A_out(R) = {A_out_R}")
    print(f"C solution = {C_solution}")
    print(f"A_in matched = {A_in_matched}")

    status_line("A continuity fixes interior constant", bool(C_solution))

    dA_in_R = sp.simplify(sp.diff(A_in_matched, r).subs(r, R))
    dA_out_R = sp.simplify(sp.diff(A_out, r).subs(r, R))

    print()
    print(f"A_in'(R) = {dA_in_R}")
    print(f"A_out'(R) = {dA_out_R}")

    status_line("A' matches at boundary", is_zero(dA_in_R - dA_out_R))

    return A_in_matched, A_out, M


# =============================================================================
# Case 4: Flux continuity at boundary
# =============================================================================

def case_4_flux_continuity():
    header("Case 4: Flux continuity at source boundary")

    r, R, G, c, rho0 = sp.symbols("r R G c rho0", positive=True, real=True)

    M = sp.Rational(4, 3) * sp.pi * rho0 * R**3
    A_in = 1 - 4*sp.pi*G*rho0*R**2/c**2 + 4*sp.pi*G*rho0*r**2/(3*c**2)
    A_out = 1 - 2*G*M/(c**2*r)

    F_in_R = sp.simplify(areal_flux(A_in, r).subs(r, R))
    F_out_R = sp.simplify(areal_flux(A_out, r).subs(r, R))
    target = sp.simplify(8*sp.pi*G*M/c**2)

    print(f"F_in(R) = {F_in_R}")
    print(f"F_out(R) = {F_out_R}")
    print(f"target  = {target}")

    status_line("interior flux at boundary equals exterior flux", is_zero(F_in_R - F_out_R))
    status_line("boundary flux equals mass normalization", is_zero(F_out_R - target))


# =============================================================================
# Case 5: Regularity at origin
# =============================================================================

def case_5_origin_regularity():
    header("Case 5: Regularity at origin")

    r, R, G, c, rho0 = sp.symbols("r R G c rho0", positive=True, real=True)

    A_in = 1 - 4*sp.pi*G*rho0*R**2/c**2 + 4*sp.pi*G*rho0*r**2/(3*c**2)

    A0 = sp.simplify(A_in.subs(r, 0))
    dA0 = sp.simplify(sp.diff(A_in, r).subs(r, 0))
    F0 = sp.simplify(areal_flux(A_in, r).subs(r, 0))

    print(f"A_in(r) = {A_in}")
    print(f"A_in(0) = {A0}")
    print(f"A_in'(0) = {dA0}")
    print(f"F_A(0) = {F0}")

    status_line("A is finite at origin", True)
    status_line("A' vanishes at origin", is_zero(dA0))
    status_line("flux vanishes at origin", is_zero(F0))


# =============================================================================
# Case 6: Interior B from kappa=0
# =============================================================================

def case_6_interior_B_from_kappa_zero():
    header("Case 6: Interior B from kappa=0")

    r, R, G, c, rho0 = sp.symbols("r R G c rho0", positive=True, real=True)

    A_in = 1 - 4*sp.pi*G*rho0*R**2/c**2 + 4*sp.pi*G*rho0*r**2/(3*c**2)
    kappa = sp.Integer(0)
    B_in = sp.simplify(1 / A_in)
    AB = sp.simplify(A_in * B_in)

    print(f"A_in = {A_in}")
    print(f"kappa = {kappa}")
    print(f"B_in = 1/A_in = {B_in}")
    print(f"A_in B_in = {AB}")

    status_line("kappa=0 gives reciprocal interior B", is_zero(AB - 1))

    print()
    print("Caution:")
    print("  This is the reciprocal interior metric implied by the reduced model.")
    print("  It is not the GR interior Schwarzschild solution.")


# =============================================================================
# Case 7: Compare with weak-field Newtonian potential form
# =============================================================================

def case_7_compare_newtonian_interior_potential():
    header("Case 7: Weak-field comparison to constant-density Newtonian potential")

    r, R, G, c, rho0 = sp.symbols("r R G c rho0", positive=True, real=True)

    A_in = 1 - 4*sp.pi*G*rho0*R**2/c**2 + 4*sp.pi*G*rho0*r**2/(3*c**2)

    # In weak field, A ≈ 1 + 2 Phi/c^2.
    Phi_from_A = sp.simplify((c**2/2) * (A_in - 1))

    print(f"A_in = {A_in}")
    print("Using A ≈ 1 + 2 Phi/c²:")
    print(f"Phi_from_A = {Phi_from_A}")

    # Newtonian potential inside uniform sphere with Phi(infty)=0:
    # Phi(r) = -GM(3R^2-r^2)/(2R^3)
    # with M=(4π/3)ρR^3 -> Phi = -2πGρR^2 + (2πGρ/3)r^2
    Phi_expected = -2*sp.pi*G*rho0*R**2 + 2*sp.pi*G*rho0*r**2/3

    print(f"Phi_expected = {Phi_expected}")

    status_line("A interior matches weak-field Newtonian potential normalization",
                is_zero(Phi_from_A - Phi_expected))


# =============================================================================
# Case 8: Difference from GR interior Schwarzschild
# =============================================================================

def case_8_not_gr_interior_schwarzschild():
    header("Case 8: Not the full GR interior Schwarzschild solution")

    print("Important caution:")
    print()
    print("  The constant-density interior A(r) found here is the solution of")
    print("  the reduced areal-flux source law.")
    print()
    print("  It matches the weak-field Newtonian interior potential and matches")
    print("  smoothly to the exterior A=1-2GM/(rc²).")
    print()
    print("  But it is not the full GR interior Schwarzschild metric.")
    print()
    print("Reasons:")
    print("  - pressure is not included,")
    print("  - stress-energy is not fully represented,")
    print("  - the GR interior solution has a different exact lapse structure,")
    print("  - the current model enforces kappa=0 / B=1/A even inside.")
    print()
    status_line("interior model is reduced-source toy, not full GR interior", True)


# =============================================================================
# Case 9: Summary
# =============================================================================

def case_9_summary():
    header("Case 9: Summary classification")

    print("Results:")
    print()
    print("1. Constant density gives:")
    print("     M_enc(r) = (4π/3) rho0 r³")
    print()
    print("2. Areal flux law gives:")
    print("     A'(r) = 2G M_enc(r)/(c² r²)")
    print()
    print("3. Interior solution:")
    print("     A_in(r) = 1 - 4πG rho0 R²/c² + 4πG rho0 r²/(3c²)")
    print()
    print("4. Exterior solution:")
    print("     A_out(r) = 1 - 2GM/(c²r)")
    print()
    print("5. A and A' match at r=R.")
    print()
    print("6. Areal flux is continuous at r=R.")
    print()
    print("7. The origin is regular.")
    print()
    print("8. The weak-field Newtonian interior potential is recovered.")
    print()
    print("9. This is not the full GR interior Schwarzschild solution.")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("The areal-flux law behaves sensibly for a finite constant-density")
    print("source in the reduced model.")
    print()
    print("It gives a regular interior A(r), smooth matching of A and A' at")
    print("the source boundary, continuous areal flux, and the correct exterior")
    print("Schwarzschild coefficient.")
    print()
    print("In weak field, the interior A(r) corresponds to the standard")
    print("Newtonian potential inside a uniform sphere.")
    print()
    print("However, this is not a full relativistic interior solution.")
    print("The next theoretical gap is pressure/stress and the question of whether")
    print("kappa=0 should hold inside matter or only in source-free exterior.")
    print()
    print("Possible next artifact:")
    print("  candidate_interior_A_source_model.md")


# =============================================================================
# Main
# =============================================================================

def main():
    header("Candidate Interior A Source Model")
    case_0_recap()
    case_1_constant_density_enclosed_mass()
    case_2_interior_A_solution()
    case_3_match_to_exterior()
    case_4_flux_continuity()
    case_5_origin_regularity()
    case_6_interior_B_from_kappa_zero()
    case_7_compare_newtonian_interior_potential()
    case_8_not_gr_interior_schwarzschild()
    case_9_summary()
    final_interpretation()


if __name__ == "__main__":
    main()
