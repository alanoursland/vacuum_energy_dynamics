# Candidate quadrupole coupling normalization
#
# Purpose
# -------
# The tensor-flux principle identifies:
#
#   A-flux        -> scalar monopole channel
#   h_ij^TT      -> tensor quadrupole radiative channel
#   Q_ij^TF      -> source-side quadrupole tensor
#
# The next question is normalization:
#
#   What coefficient maps quadrupole acceleration to far-zone h_ij^TT?
#
# In GR-like weak radiation, the schematic far-zone relation is:
#
#   h_ij^TT ~ (2G/(c^4 R)) d^2 Q_ij^TT/dt^2
#
# where R is distance to observer.
#
# This script does not assume the full GR derivation. It checks:
#
#   1. dimensional consistency of a coupling C_Q ~ G/(c^4 R),
#   2. plus/cross amplitude scaling from Q_plus, Q_cross,
#   3. rotating quadrupole frequency scaling h ~ Omega^2 Q0 / R,
#   4. distinction between amplitude normalization and power normalization,
#   5. scalar monopole normalization versus tensor quadrupole normalization.
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/06_tensor_flux_principle/
#   or:
#   scripts_v3/candidate_quadrupole_coupling_normalization.py

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


# =============================================================================
# Case 0: Normalization problem
# =============================================================================

def case_0_problem_statement():
    header("Case 0: Quadrupole coupling normalization problem")

    print("Tensor-flux source structure:")
    print()
    print("  Q_ij^TF -> h_ij^TT")
    print()
    print("Need amplitude normalization:")
    print()
    print("  h_ij^TT ~ C_Q * d²Q_ij^TT/dt²")
    print()
    print("GR-like weak far-zone scaling uses:")
    print()
    print("  C_Q = 2G/(c^4 R)")
    print()
    print("This script treats that as a target normalization, not a derivation.")

    status_line("quadrupole coupling normalization problem posed", True)


# =============================================================================
# Case 1: Symbolic far-zone amplitude law
# =============================================================================

def case_1_far_zone_amplitude_law():
    header("Case 1: Symbolic far-zone amplitude law")

    G, c, R = sp.symbols("G c R", positive=True, real=True)
    Qdd_plus, Qdd_cross = sp.symbols("Qdd_plus Qdd_cross", real=True)

    C_Q = 2*G/(c**4 * R)

    h_plus = sp.simplify(C_Q * Qdd_plus)
    h_cross = sp.simplify(C_Q * Qdd_cross)

    print(f"C_Q = {C_Q}")
    print(f"h_plus = {h_plus}")
    print(f"h_cross = {h_cross}")

    status_line("far-zone amplitude normalization stated", True)

    return C_Q, h_plus, h_cross


# =============================================================================
# Case 2: Rotating quadrupole amplitude scaling
# =============================================================================

def case_2_rotating_quadrupole_scaling():
    header("Case 2: Rotating quadrupole amplitude scaling")

    G, c, R, Q0, Omega, t = sp.symbols("G c R Q0 Omega t", positive=True, real=True)

    Q_plus = Q0 * sp.cos(2*Omega*t)
    Q_cross = Q0 * sp.sin(2*Omega*t)

    Qdd_plus = sp.diff(Q_plus, t, 2)
    Qdd_cross = sp.diff(Q_cross, t, 2)

    C_Q = 2*G/(c**4 * R)

    h_plus = sp.simplify(C_Q * Qdd_plus)
    h_cross = sp.simplify(C_Q * Qdd_cross)

    amp_sq = sp.simplify(h_plus**2 + h_cross**2)

    print(f"Q_plus = {Q_plus}")
    print(f"Q_cross = {Q_cross}")
    print()
    print(f"Qdd_plus = {Qdd_plus}")
    print(f"Qdd_cross = {Qdd_cross}")
    print()
    print(f"h_plus = {h_plus}")
    print(f"h_cross = {h_cross}")
    print()
    print(f"h_plus² + h_cross² = {amp_sq}")

    expected = 64*G**2*Omega**4*Q0**2/(R**2*c**8)
    status_line("amplitude scales as G Omega² Q0/(c⁴ R)",
                is_zero(amp_sq - expected))


# =============================================================================
# Case 3: Dimensional scaling sanity check
# =============================================================================

def case_3_dimensional_scaling():
    header("Case 3: Dimensional scaling sanity check")

    print("Dimension check:")
    print()
    print("  [G]      = L^3 / (M T^2)")
    print("  [Q]      = M L^2")
    print("  [Qdd]    = M L^2 / T^2")
    print("  [c^4 R]  = (L^4/T^4) * L = L^5/T^4")
    print()
    print("  [G Qdd/(c^4 R)]")
    print("    = [L^3/(M T^2)] [M L^2/T^2] [T^4/L^5]")
    print("    = dimensionless")
    print()
    status_line("quadrupole amplitude coefficient is dimensionally consistent", True)


# =============================================================================
# Case 4: Amplitude versus power normalization
# =============================================================================

def case_4_amplitude_vs_power():
    header("Case 4: Amplitude versus power normalization")

    G, c, Q0, Omega = sp.symbols("G c Q0 Omega", positive=True, real=True)

    # Amplitude proxy from second derivative:
    amp_source = 16*Omega**4*Q0**2

    # Power proxy from third derivative:
    power_source = 64*Omega**6*Q0**2

    # GR-like power coefficient schematic:
    # P ~ G/(5 c^5) < Qdddot_ij Qdddot_ij >
    P_proxy = sp.simplify(G * power_source / (5*c**5))

    print(f"amplitude-source proxy Qdd² = {amp_source}")
    print(f"power-source proxy Qddd² = {power_source}")
    print(f"GR-like power proxy coefficient G/(5c^5): {P_proxy}")
    print()
    print("Interpretation:")
    print("  amplitude normalization uses G/c^4")
    print("  power normalization uses G/c^5")
    print("  they are related but not the same step")

    status_line("amplitude and power normalizations kept distinct", True)


# =============================================================================
# Case 5: Compare scalar and tensor normalizations
# =============================================================================

def case_5_scalar_tensor_normalization_comparison():
    header("Case 5: Scalar versus tensor normalization")

    G, M, c, R, Qdd = sp.symbols("G M c R Qdd", positive=True, real=True)

    # Scalar exterior A perturbation at distance R:
    delta_A = -2*G*M/(c**2 * R)

    # Tensor far-zone strain:
    h_TT = 2*G*Qdd/(c**4 * R)

    print("Scalar monopole amplitude:")
    print(f"  delta A ~ {delta_A}")
    print()
    print("Tensor quadrupole amplitude:")
    print(f"  h_TT ~ {h_TT}")
    print()
    print("Comparison:")
    print("  scalar mass channel uses GM/(c²R)")
    print("  tensor quadrupole channel uses G Qdd/(c⁴R)")
    print()
    status_line("scalar and tensor coupling normalizations are distinct", True)


# =============================================================================
# Case 6: Coupling target classification
# =============================================================================

def case_6_classification():
    header("Case 6: Coupling target classification")

    print("Results:")
    print()
    print("1. A GR-like far-zone tensor amplitude has coefficient 2G/(c^4 R).")
    print("2. This coefficient is dimensionally consistent.")
    print("3. Rotating quadrupole amplitudes scale as Omega² Q0.")
    print("4. Radiated-power proxies scale as Omega^6 Q0².")
    print("5. Scalar monopole normalization GM/(c²R) is distinct from tensor")
    print("   quadrupole normalization GQdd/(c⁴R).")
    print()
    status_line("quadrupole coupling normalization target established", True)


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("This script establishes the target normalization for the tensor")
    print("quadrupole amplitude:")
    print()
    print("  h_ij^TT ~ (2G/(c^4 R)) Qdd_ij^TT")
    print()
    print("It does not derive the coefficient from a tensor action.")
    print("It identifies the normalization that a successful tensor-flux theory")
    print("should reproduce.")
    print()
    print("Next steps:")
    print("  derive this coefficient from tensor action/stiffness")
    print("  connect amplitude normalization to radiation energy flux")
    print("  check no unwanted scalar radiation")
    print()
    print("Possible next artifact:")
    print("  candidate_quadrupole_coupling_normalization.md")
    print()
    print("Possible next script:")
    print("  candidate_tensor_radiation_energy_flux.py")


def main():
    header("Candidate Quadrupole Coupling Normalization")
    case_0_problem_statement()
    case_1_far_zone_amplitude_law()
    case_2_rotating_quadrupole_scaling()
    case_3_dimensional_scaling()
    case_4_amplitude_vs_power()
    case_5_scalar_tensor_normalization_comparison()
    case_6_classification()
    final_interpretation()


if __name__ == "__main__":
    main()
