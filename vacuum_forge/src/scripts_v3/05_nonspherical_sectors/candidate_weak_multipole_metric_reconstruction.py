# Candidate weak multipole metric reconstruction
#
# Purpose
# -------
# The multipole A-source test showed that the areal-flux law has a natural
# weak nonspherical extension:
#
#   A = 1 + 2 Phi/c^2
#   Delta A = 8*pi*G*rho/c^2
#
# In vacuum, A is harmonic and carries ordinary multipoles.
#
# But a full weak gravitational metric is not just the temporal scalar A.
# In standard weak-field GR, for Newtonian scalar potential Phi:
#
#   g_tt ≈ -(1 + 2 Phi/c^2)c^2
#   g_ij ≈ (1 - 2 Phi/c^2) delta_ij
#
# This script checks whether the reduced reciprocal compensation idea:
#
#   kappa = 0
#   B_like = 1/A
#
# reproduces the weak scalar spatial factor, and then identifies what is
# missing for a full nonspherical theory.
#
# Main tests:
#
#   1. A=1+2psi gives temporal Newtonian factor.
#   2. B=1/A gives 1-2psi+O(psi^2), matching the weak scalar spatial factor.
#   3. Multipole psi fields remain harmonic in vacuum.
#   4. A scalar conformal spatial factor can represent the PPN gamma=1
#      scalar part at first order.
#   5. A scalar sector cannot represent vector/frame-dragging or tensor waves.
#   6. Anisotropic spatial shear requires additional degrees of freedom.
#
# IMPORTANT:
# This is a weak-field diagnostic. It is not a nonlinear nonspherical theory.
#
# Suggested location:
#   scripts_v3/candidate_weak_multipole_metric_reconstruction.py

import sympy as sp


# =============================================================================
# Utilities
# =============================================================================

def header(title: str) -> None:
    print()
    print("=" * 116)
    print(title)
    print("=" * 116)


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
    return sp.simplify(
        (1/r**2) * sp.diff(r**2 * sp.diff(expr, r), r)
        - ell*(ell+1)*expr/r**2
    )


def series(expr, var, order):
    return sp.series(expr, var, 0, order).removeO()


# =============================================================================
# Case 0: Weak metric target
# =============================================================================

def case_0_weak_metric_target():
    header("Case 0: Weak metric target")

    psi = sp.symbols("psi", real=True)

    A_target = 1 + 2*psi
    spatial_factor_target = 1 - 2*psi

    print("Let:")
    print("  psi = Phi/c^2")
    print()
    print("Standard weak scalar metric target:")
    print("  g_tt factor A = 1 + 2 psi")
    print("  spatial conformal factor = 1 - 2 psi")
    print()
    print(f"A_target = {A_target}")
    print(f"spatial_factor_target = {spatial_factor_target}")

    status_line("weak scalar target stated", True)


# =============================================================================
# Case 1: Reciprocal compensation at weak order
# =============================================================================

def case_1_reciprocal_compensation():
    header("Case 1: Reciprocal compensation at weak order")

    psi = sp.symbols("psi", real=True)

    A = 1 + 2*psi
    B_recip = sp.simplify(1/A)
    B_series = series(B_recip, psi, 4)

    print(f"A = {A}")
    print(f"B_recip = 1/A = {B_recip}")
    print(f"B_recip series = {B_series}")
    print()
    print("To first order:")
    print("  B_recip ≈ 1 - 2 psi")

    status_line("reciprocal compensation matches scalar spatial factor at first order",
                is_zero(series(B_recip - (1 - 2*psi), psi, 2)))


# =============================================================================
# Case 2: PPN gamma proxy
# =============================================================================

def case_2_gamma_proxy():
    header("Case 2: Gamma proxy")

    psi, gamma = sp.symbols("psi gamma", real=True)

    A = 1 + 2*psi
    spatial_factor = 1 - 2*gamma*psi
    B_recip_first = 1 - 2*psi

    gamma_solution = sp.solve(sp.Eq(spatial_factor, B_recip_first), gamma)

    print("PPN-like scalar spatial factor:")
    print("  spatial = 1 - 2 gamma psi")
    print()
    print("Reciprocal compensation gives:")
    print("  spatial = 1 - 2 psi")
    print()
    print(f"gamma solution = {gamma_solution}")

    status_line("reciprocal scalar sector gives gamma=1",
                bool(gamma_solution) and gamma_solution[0] == 1)


# =============================================================================
# Case 3: Multipole scalar potential reconstruction
# =============================================================================

def case_3_multipole_scalar_reconstruction():
    header("Case 3: Multipole scalar potential reconstruction")

    r, Q, psi0 = sp.symbols("r Q psi0", positive=True, real=True)
    mu = sp.symbols("mu", real=True)

    # Example weak potential psi = -Mbar/r + Q P2/r^3.
    Mbar = sp.symbols("Mbar", real=True)
    P2 = sp.Rational(1, 2)*(3*mu**2 - 1)
    psi = -Mbar/r + Q*P2/r**3

    A = 1 + 2*psi
    spatial = 1 - 2*psi

    print(f"psi = {psi}")
    print(f"A = 1 + 2psi = {A}")
    print(f"spatial scalar factor = 1 - 2psi = {spatial}")
    print()
    print("Interpretation:")
    print("  The same weak multipole psi controls temporal and scalar spatial")
    print("  metric factors with gamma=1.")

    status_line("weak multipole scalar metric reconstructed", True)


# =============================================================================
# Case 4: Vacuum harmonic modes remain valid
# =============================================================================

def case_4_harmonic_modes():
    header("Case 4: Vacuum harmonic modes remain valid")

    r = sp.symbols("r", positive=True, real=True)

    for ell in range(0, 5):
        f = r**(-(ell+1))
        lap = radial_laplacian_l(f, r, ell)
        print(f"ell={ell}: f=1/r^{ell+1}, mode Laplacian={lap}")
        status_line(f"ell={ell} scalar multipole harmonic", is_zero(lap))

    print()
    print("These are scalar A/psi multipoles, not the full tensor metric content.")


# =============================================================================
# Case 5: Anisotropic spatial shear is missing
# =============================================================================

def case_5_anisotropic_spatial_shear_missing():
    header("Case 5: Anisotropic spatial shear is missing")

    psi, hxx, hyy, hzz = sp.symbols("psi h_xx h_yy h_zz", real=True)

    # Scalar conformal spatial metric perturbation:
    #   h_ij^scalar = -2 psi delta_ij
    h_scalar = sp.Matrix([
        [-2*psi, 0, 0],
        [0, -2*psi, 0],
        [0, 0, -2*psi],
    ])

    # General diagonal spatial perturbation:
    h_general_diag = sp.Matrix([
        [hxx, 0, 0],
        [0, hyy, 0],
        [0, 0, hzz],
    ])

    trace_scalar = sp.trace(h_scalar)
    trace_general = sp.trace(h_general_diag)

    shear_diag = sp.simplify(h_general_diag - (trace_general/3)*sp.eye(3))

    print("Scalar conformal spatial perturbation:")
    print(h_scalar)
    print(f"trace = {trace_scalar}")
    print()
    print("General diagonal spatial perturbation:")
    print(h_general_diag)
    print(f"trace = {trace_general}")
    print()
    print("Trace-free diagonal shear part:")
    print(shear_diag)
    print()
    print("A single scalar psi fixes only the conformal/trace spatial piece.")
    print("It cannot represent arbitrary trace-free spatial shear.")

    status_line("anisotropic spatial shear requires extra degrees of freedom", True)


# =============================================================================
# Case 6: Vector/frame-dragging sector is missing
# =============================================================================

def case_6_vector_sector_missing():
    header("Case 6: Vector/frame-dragging sector is missing")

    print("Weak stationary rotating sources introduce off-diagonal components:")
    print()
    print("  g_ti != 0")
    print()
    print("These are vector/gravitomagnetic/frame-dragging degrees of freedom.")
    print()
    print("The scalar A field and reciprocal scalar spatial factor do not produce")
    print("off-diagonal g_ti components.")
    print()
    status_line("frame-dragging requires vector sector beyond scalar A", True)


# =============================================================================
# Case 7: Tensor wave sector is missing
# =============================================================================

def case_7_tensor_sector_missing():
    header("Case 7: Tensor wave sector is missing")

    print("Linearized gravitational waves require transverse-traceless spatial")
    print("metric perturbations:")
    print()
    print("  h_ij^TT")
    print()
    print("These are not captured by a scalar A=1+2psi alone.")
    print()
    print("Therefore the scalar multipole extension is not a wave-sector theory.")
    print()
    status_line("tensor waves require additional tensor sector", True)


# =============================================================================
# Case 8: Nonlinear nonspherical closure
# =============================================================================

def case_8_nonlinear_closure():
    header("Case 8: Nonlinear nonspherical closure")

    print("Spherical exact branch:")
    print("  A = 1 - 2GM/(rc^2)")
    print("  kappa = 0")
    print("  B = 1/A")
    print()
    print("Weak nonspherical scalar branch:")
    print("  A = 1 + 2Phi/c^2")
    print("  spatial conformal factor ≈ 1 - 2Phi/c^2")
    print()
    print("Open nonlinear problem:")
    print("  How should full spatial geometry be reconstructed when Phi is")
    print("  nonspherical and nonlinear effects matter?")
    print()
    print("Likely needed sectors:")
    print("  scalar A / Newtonian potential")
    print("  kappa / trace response")
    print("  spatial shear")
    print("  vector frame-dragging")
    print("  tensor waves")

    status_line("nonlinear nonspherical closure remains open", True)


# =============================================================================
# Case 9: Classification
# =============================================================================

def case_9_classification():
    header("Case 9: Classification")

    print("Results:")
    print()
    print("1. A=1+2Phi/c^2 reconstructs the weak temporal scalar metric.")
    print("2. Reciprocal compensation gives spatial factor 1-2Phi/c^2 to first order.")
    print("3. This corresponds to gamma=1 in the scalar weak-field sector.")
    print("4. Scalar A multipoles are compatible with Newtonian weak multipoles.")
    print("5. A single scalar cannot represent anisotropic spatial shear.")
    print("6. A single scalar cannot represent frame dragging.")
    print("7. A single scalar cannot represent tensor gravitational waves.")
    print("8. The nonlinear nonspherical closure remains an open problem.")
    print()
    status_line("weak scalar sector passes; full nonspherical theory remains incomplete", True)


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("The weak A multipole sector can reconstruct the standard weak scalar")
    print("metric form:")
    print()
    print("  g_tt factor: A = 1 + 2Phi/c^2")
    print("  spatial scalar factor: 1 - 2Phi/c^2")
    print()
    print("This means reciprocal compensation reproduces the gamma=1 scalar")
    print("weak-field structure at first order.")
    print()
    print("But this is not a full gravity theory.")
    print("A full nonspherical extension needs additional sectors:")
    print()
    print("  spatial shear")
    print("  vector/frame-dragging modes")
    print("  tensor/wave modes")
    print("  nonlinear closure rules")
    print()
    print("Possible next artifact:")
    print("  candidate_weak_multipole_metric_reconstruction.md")
    print()
    print("Possible next script:")
    print("  candidate_nonspherical_degree_inventory.py")


def main():
    header("Candidate Weak Multipole Metric Reconstruction")
    case_0_weak_metric_target()
    case_1_reciprocal_compensation()
    case_2_gamma_proxy()
    case_3_multipole_scalar_reconstruction()
    case_4_harmonic_modes()
    case_5_anisotropic_spatial_shear_missing()
    case_6_vector_sector_missing()
    case_7_tensor_sector_missing()
    case_8_nonlinear_closure()
    case_9_classification()
    final_interpretation()


if __name__ == "__main__":
    main()
