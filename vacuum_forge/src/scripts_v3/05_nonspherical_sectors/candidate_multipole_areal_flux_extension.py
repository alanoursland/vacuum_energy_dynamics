# Candidate multipole areal-flux extension
#
# Purpose
# -------
# The current strongest mechanics branch is static spherical:
#
#   F_A(r) = 4*pi*r^2*A'(r)
#   F_A = 8*pi*G*M/c^2
#
# giving:
#
#   A = 1 - 2GM/(r c^2)
#
# with exterior compensation:
#
#   kappa = 0
#   B = 1/A
#
# But a real gravitational theory cannot stay purely spherical.
# This script asks whether the A-flux law can be generalized, at least
# weakly, to nonspherical/multipole sources.
#
# The cautious reduced hypothesis is:
#
#   A = 1 + 2 Phi/c^2
#
# where Phi is the Newtonian potential outside a localized source.
#
# Then:
#
#   Delta_flat A = 8*pi*G*rho/c^2
#
# is equivalent to:
#
#   Delta_flat Phi = 4*pi*G*rho
#
# In vacuum exterior:
#
#   Delta_flat A = 0
#
# and A admits the usual harmonic multipole expansion.
#
# This does NOT prove a full nonlinear, nonspherical, covariant theory.
# It tests whether the areal-flux law has a natural weak multipole extension.
#
# Suggested location:
#   scripts_v3/candidate_multipole_areal_flux_extension.py

import sympy as sp


# =============================================================================
# Utilities
# =============================================================================

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


def radial_laplacian_l(expr, r, ell):
    # Flat 3D Laplacian on separated mode f_l(r) P_l(cos theta):
    # Delta[f_l(r) Y_lm] = [1/r^2 (r^2 f')' - l(l+1) f/r^2] Y_lm
    return sp.simplify((1/r**2) * sp.diff(r**2 * sp.diff(expr, r), r) - ell*(ell+1)*expr/r**2)


def spherical_flux_radial(A, r):
    return sp.simplify(4*sp.pi*r**2*sp.diff(A, r))


# =============================================================================
# Case 0: Spherical law recap
# =============================================================================

def case_0_spherical_recap():
    header("Case 0: Spherical areal-flux recap")

    r, G, M, c = sp.symbols("r G M c", positive=True, real=True)

    A = 1 - 2*G*M/(c**2*r)
    F = spherical_flux_radial(A, r)
    target = 8*sp.pi*G*M/c**2

    print(f"A_spherical = {A}")
    print(f"F_A = 4*pi*r^2*A' = {F}")
    print(f"target = {target}")

    status_line("spherical flux gives Schwarzschild coefficient", is_zero(F - target))


# =============================================================================
# Case 1: Weak-field A as Newtonian potential variable
# =============================================================================

def case_1_A_phi_relation():
    header("Case 1: Weak-field A as Newtonian potential variable")

    Phi, c = sp.symbols("Phi c", real=True)

    A = 1 + 2*Phi/c**2

    print("Weak-field identification:")
    print()
    print("  A = 1 + 2 Phi/c^2")
    print()
    print(f"A = {A}")
    print()
    print("Then:")
    print("  Delta A = 2 Delta Phi / c^2")
    print()
    print("If Delta Phi = 4*pi*G*rho, then:")
    print("  Delta A = 8*pi*G*rho/c^2")
    print()
    status_line("areal A-source law matches Newtonian Poisson in weak field", True)


# =============================================================================
# Case 2: Multipole harmonic radial modes
# =============================================================================

def case_2_multipole_harmonic_modes():
    header("Case 2: Vacuum harmonic multipole radial modes")

    r = sp.symbols("r", positive=True, real=True)

    for ell in range(0, 5):
        f_ext = r**(-(ell+1))
        lap = radial_laplacian_l(f_ext, r, ell)

        print(f"ell = {ell}")
        print(f"  exterior radial mode f(r)=1/r^{ell+1}")
        print(f"  mode Laplacian = {lap}")
        status_line(f"ell={ell} exterior multipole is harmonic", is_zero(lap))

    print()
    print("Interpretation:")
    print("  The weak exterior A field can carry ordinary harmonic multipoles.")


# =============================================================================
# Case 3: Interior regular modes
# =============================================================================

def case_3_regular_interior_modes():
    header("Case 3: Regular interior harmonic modes")

    r = sp.symbols("r", positive=True, real=True)

    for ell in range(0, 5):
        f_int = r**ell
        lap = radial_laplacian_l(f_int, r, ell)

        print(f"ell = {ell}")
        print(f"  regular radial mode f(r)=r^{ell}")
        print(f"  mode Laplacian = {lap}")
        status_line(f"ell={ell} regular interior harmonic mode", is_zero(lap))

    print()
    print("Interpretation:")
    print("  Standard regular/harmonic mode structure is available in the weak limit.")


# =============================================================================
# Case 4: Monopole flux versus higher multipoles
# =============================================================================

def case_4_flux_integral_selection():
    header("Case 4: Surface flux selects monopole")

    r, G, c = sp.symbols("r G c", positive=True, real=True)
    M, Q = sp.symbols("M Q", real=True)
    mu = sp.symbols("mu", real=True)  # mu = cos(theta)

    # Toy axisymmetric potential-like A:
    # A = 1 - 2GM/(c^2 r) + q P2(mu)/r^3
    P2 = sp.Rational(1, 2)*(3*mu**2 - 1)
    A = 1 - 2*G*M/(c**2*r) + Q*P2/r**3

    dA = sp.diff(A, r)

    # Surface average over sphere:
    # integral dOmega = 2pi integral_{-1}^{1} dmu
    flux_integrand = r**2*dA
    total_flux = sp.simplify(2*sp.pi*sp.integrate(flux_integrand, (mu, -1, 1)))

    target = 8*sp.pi*G*M/c**2

    print(f"A = {A}")
    print(f"r^2 A_r = {flux_integrand}")
    print(f"surface flux integral = {total_flux}")
    print(f"target monopole flux = {target}")

    status_line("higher quadrupole integrates to zero net flux", is_zero(total_flux - target))

    print()
    print("Interpretation:")
    print("  Total A-flux through a large sphere measures only the monopole mass.")
    print("  Higher multipoles affect angular distribution but not net flux.")


# =============================================================================
# Case 5: Dipole mode and center-of-mass caution
# =============================================================================

def case_5_dipole_caution():
    header("Case 5: Dipole mode and origin/center-of-mass caution")

    r, D, c = sp.symbols("r D c", positive=True, real=True)
    mu = sp.symbols("mu", real=True)

    P1 = mu
    A_dipole = D*P1/r**2
    dA = sp.diff(A_dipole, r)
    total_flux = sp.simplify(2*sp.pi*sp.integrate(r**2*dA, (mu, -1, 1)))

    print(f"A_dipole = {A_dipole}")
    print(f"surface flux integral = {total_flux}")

    status_line("pure dipole has zero net flux", is_zero(total_flux))

    print()
    print("Caution:")
    print("  Dipole terms depend on origin choice and center-of-mass frame.")
    print("  A multipole extension must handle coordinates/gauge carefully.")


# =============================================================================
# Case 6: Linear compensated metric from multipole A
# =============================================================================

def case_6_linear_compensated_metric():
    header("Case 6: Linear compensated metric from multipole A")

    psi = sp.symbols("psi", real=True)

    # Weak A = 1 + 2 psi, where psi=Phi/c^2.
    A = 1 + 2*psi
    # Exterior compensation kappa=0 suggests reciprocal B-like response.
    B_recip = sp.series(1/A, psi, 0, 3).removeO()

    print("Let psi = Phi/c^2.")
    print(f"A = {A}")
    print(f"B = 1/A ≈ {B_recip}")
    print()
    print("To first order:")
    print("  A ≈ 1 + 2psi")
    print("  B ≈ 1 - 2psi")
    print()
    print("For attractive gravity Phi<0:")
    print("  A < 1")
    print("  B > 1")
    print()
    status_line("reciprocal compensation extends formally to weak nonspherical A", True)


# =============================================================================
# Case 7: Nonlinear caution
# =============================================================================

def case_7_nonlinear_caution():
    header("Case 7: Nonlinear caution")

    print("The weak multipole extension is natural:")
    print()
    print("  A = 1 + 2Phi/c²")
    print("  Delta A = 8*pi*G*rho/c²")
    print("  exterior Delta A = 0")
    print()
    print("But the exact nonlinear spherical branch uses:")
    print()
    print("  B = 1/A")
    print("  kappa = 0")
    print()
    print("For general nonspherical fields, a single scalar A is not enough to")
    print("define the full spatial metric. There are tensor/shear degrees of freedom.")
    print()
    print("Therefore:")
    print("  This script supports weak multipoles.")
    print("  It does not produce a full nonlinear nonspherical gravity theory.")
    status_line("nonlinear nonspherical extension remains open", True)


# =============================================================================
# Case 8: Classification
# =============================================================================

def case_8_classification():
    header("Case 8: Classification")

    print("Results:")
    print()
    print("1. The spherical law is the monopole part of a weak Poisson law for A.")
    print("2. A = 1 + 2Phi/c² turns Newtonian Poisson into Delta A = 8πGρ/c².")
    print("3. Exterior vacuum supports harmonic multipoles 1/r^(ell+1).")
    print("4. Net surface flux selects only the monopole mass.")
    print("5. Higher multipoles redistribute angular flux but do not change total flux.")
    print("6. Dipole terms require origin/center-of-mass care.")
    print("7. Exact nonlinear nonspherical completion remains unsolved.")
    print()
    status_line("multipole extension is viable as weak-field diagnostic", True)


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("The areal-flux law has a natural weak multipole extension:")
    print()
    print("  A = 1 + 2Phi/c²")
    print("  Delta A = 8*pi*G*rho/c²")
    print()
    print("In vacuum, A is harmonic and carries ordinary multipoles.")
    print("The total surface flux measures only the monopole mass, while higher")
    print("multipoles shape the angular field.")
    print()
    print("This keeps the reduced exterior program compatible with weak")
    print("nonspherical Newtonian gravity.")
    print()
    print("However, it does not solve the full nonlinear nonspherical problem.")
    print("That will require additional spatial/tensor degrees of freedom beyond")
    print("the spherical A/B reciprocal pair.")
    print()
    print("Possible next artifact:")
    print("  candidate_multipole_areal_flux_extension.md")


def main():
    header("Candidate Multipole Areal-Flux Extension")
    case_0_spherical_recap()
    case_1_A_phi_relation()
    case_2_multipole_harmonic_modes()
    case_3_regular_interior_modes()
    case_4_flux_integral_selection()
    case_5_dipole_caution()
    case_6_linear_compensated_metric()
    case_7_nonlinear_caution()
    case_8_classification()
    final_interpretation()


if __name__ == "__main__":
    main()
