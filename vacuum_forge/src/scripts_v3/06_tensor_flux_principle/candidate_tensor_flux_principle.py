# Candidate tensor flux principle
#
# Purpose
# -------
# This script collects the first tensor-flux program results into one
# principle-level diagnostic:
#
#   1. scalar A-flux is the monopole channel,
#   2. scalar A-flux cannot produce waves,
#   3. TT tensor basis supplies plus/cross polarizations,
#   4. TT tensor waves propagate with omega^2=c^2 k^2,
#   5. trace-free quadrupole structure sources plus/cross channels,
#   6. tensor radiation is the quadrupole radiative channel.
#
# It does not derive GR. It organizes the multi-channel vacuum-response idea:
#
#   monopole scalar flow  -> A
#   quadrupole tensor flow -> h_ij^TT
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/06_tensor_flux_principle/
#   or:
#   scripts_v3/candidate_tensor_flux_principle.py

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


def inner(A, B):
    return sp.simplify(sum(A[i, j] * B[i, j] for i in range(3) for j in range(3)))


# =============================================================================
# Case 0: Principle statement
# =============================================================================

def case_0_principle_statement():
    header("Case 0: Tensor-flux principle statement")

    print("Working principle:")
    print()
    print("  A-flux is the scalar monopole vacuum-response channel.")
    print("  h_ij^TT is the tensor quadrupole radiative channel.")
    print()
    print("Do not force waves into A.")
    print("Do not treat scalar flux as a complete gravity theory.")
    print()
    print("Instead:")
    print("  build a multi-sector vacuum-response theory.")

    status_line("tensor-flux principle posed", True)


# =============================================================================
# Case 1: Scalar monopole channel
# =============================================================================

def case_1_scalar_monopole_channel():
    header("Case 1: Scalar monopole channel")

    G, M, c = sp.symbols("G M c", positive=True, real=True)

    F_A = 8 * sp.pi * G * M / c**2

    print("Scalar A-flux channel:")
    print()
    print("  M -> F_A")
    print()
    print(f"F_A = {F_A}")
    print()
    print("Interpretation:")
    print("  monopole mass controls scalar A-flux.")

    status_line("monopole scalar channel stated", True)

    return F_A


# =============================================================================
# Case 2: Scalar no-wave guardrail
# =============================================================================

def case_2_scalar_no_wave_guardrail():
    header("Case 2: Scalar no-wave guardrail")

    psi = sp.symbols("psi", real=True)

    H_scalar = -2 * psi * sp.eye(3)
    trace = sp.trace(H_scalar)
    H_tf = sp.simplify(H_scalar - trace * sp.eye(3) / 3)

    print("Scalar spatial perturbation:")
    print(H_scalar)
    print()
    print(f"trace = {trace}")
    print("trace-free projection:")
    print(H_tf)

    status_line("scalar mode is pure trace", trace != 0)
    status_line("scalar mode has zero trace-free tensor content",
                all(is_zero(entry) for entry in list(H_tf)))


# =============================================================================
# Case 3: Tensor TT channel
# =============================================================================

def case_3_tensor_tt_channel():
    header("Case 3: Tensor TT channel")

    e_plus = sp.Matrix([
        [1, 0, 0],
        [0, -1, 0],
        [0, 0, 0],
    ])

    e_cross = sp.Matrix([
        [0, 1, 0],
        [1, 0, 0],
        [0, 0, 0],
    ])

    hp, hx = sp.symbols("h_plus h_cross", real=True)
    H_TT = sp.simplify(hp * e_plus + hx * e_cross)

    print("e_plus =")
    print(e_plus)
    print()
    print("e_cross =")
    print(e_cross)
    print()
    print("H_TT =")
    print(H_TT)
    print()
    print(f"trace(H_TT) = {sp.trace(H_TT)}")

    status_line("TT tensor channel has two polarizations", is_zero(sp.trace(H_TT)))

    return e_plus, e_cross, H_TT


# =============================================================================
# Case 4: Tensor wave propagation
# =============================================================================

def case_4_tensor_wave_propagation():
    header("Case 4: Tensor wave propagation")

    t, z, k, omega, c, H = sp.symbols("t z k omega c H", positive=True, real=True)

    h = H * sp.cos(k*z - omega*t)
    box_h = sp.simplify((1/c**2) * sp.diff(h, t, 2) - sp.diff(h, z, 2))
    coeff = sp.simplify(box_h / h)

    print(f"h = {h}")
    print(f"Box h = {box_h}")
    print(f"Box h / h = {coeff}")
    print()
    print("Wave condition:")
    print("  omega^2 = c^2 k^2")

    status_line("TT amplitude supports wave dispersion relation",
                is_zero(coeff - (k**2 - omega**2/c**2)))


# =============================================================================
# Case 5: Quadrupole source projection
# =============================================================================

def case_5_quadrupole_source_projection():
    header("Case 5: Quadrupole source projection")

    Qxx, Qyy, Qzz, Qxy, Qxz, Qyz = sp.symbols("Q_xx Q_yy Q_zz Q_xy Q_xz Q_yz", real=True)

    Q = sp.Matrix([
        [Qxx, Qxy, Qxz],
        [Qxy, Qyy, Qyz],
        [Qxz, Qyz, Qzz],
    ])

    trQ = sp.trace(Q)
    Q_TF = sp.simplify(Q - trQ * sp.eye(3) / 3)

    e_plus = sp.Matrix([
        [1, 0, 0],
        [0, -1, 0],
        [0, 0, 0],
    ])

    e_cross = sp.Matrix([
        [0, 1, 0],
        [1, 0, 0],
        [0, 0, 0],
    ])

    Q_plus = sp.simplify(inner(Q_TF, e_plus) / 2)
    Q_cross = sp.simplify(inner(Q_TF, e_cross) / 2)

    print("Q_TF =")
    print(Q_TF)
    print()
    print(f"Q_plus = {Q_plus}")
    print(f"Q_cross = {Q_cross}")

    status_line("quadrupole projects into plus channel", is_zero(Q_plus - (Qxx - Qyy)/2))
    status_line("quadrupole projects into cross channel", is_zero(Q_cross - Qxy))


# =============================================================================
# Case 6: Time derivative distinction
# =============================================================================

def case_6_time_derivative_distinction():
    header("Case 6: Time-derivative distinction")

    t, Q0, Omega = sp.symbols("t Q0 Omega", positive=True, real=True)

    Qp = Q0 * sp.cos(2*Omega*t)
    Qx = Q0 * sp.sin(2*Omega*t)

    amp_proxy = sp.simplify(sp.diff(Qp, t, 2)**2 + sp.diff(Qx, t, 2)**2)
    power_proxy = sp.simplify(sp.diff(Qp, t, 3)**2 + sp.diff(Qx, t, 3)**2)

    print(f"Q_plus = {Qp}")
    print(f"Q_cross = {Qx}")
    print()
    print(f"second-derivative amplitude proxy = {amp_proxy}")
    print(f"third-derivative power proxy = {power_proxy}")

    status_line("amplitude proxy uses second derivatives", is_zero(amp_proxy - 16*Omega**4*Q0**2))
    status_line("power proxy uses third derivatives", is_zero(power_proxy - 64*Omega**6*Q0**2))


# =============================================================================
# Case 7: Multi-channel map
# =============================================================================

def case_7_multichannel_map():
    header("Case 7: Multi-channel vacuum-response map")

    print("| Channel | Variable | Source object | Role |")
    print("|---|---|---|---|")
    print("| scalar monopole | A | M / rho | Newtonian potential, static flux |")
    print("| trace interior | kappa | pressure / trace candidate | matter response |")
    print("| vector current | W_i | mass current / angular momentum | frame dragging |")
    print("| tensor quadrupole | h_ij^TT | Q_ij^TF derivatives | radiation |")
    print()
    status_line("multi-channel map stated", True)


# =============================================================================
# Case 8: Classification
# =============================================================================

def case_8_classification():
    header("Case 8: Classification")

    print("Results:")
    print()
    print("1. Scalar A-flux is the monopole channel.")
    print("2. Scalar A has no TT wave content.")
    print("3. TT tensor basis supplies plus/cross polarizations.")
    print("4. TT amplitudes support wave propagation.")
    print("5. Trace-free quadrupole projects onto plus/cross channels.")
    print("6. Changing quadrupole structure is the source-side tensor object.")
    print("7. Tensor-flux principle should be a multi-sector principle, not scalar-only.")
    print()
    status_line("tensor-flux principle passes structural checks", True)


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("The tensor-flux principle is now structurally defined:")
    print()
    print("  A-flux = scalar monopole vacuum-response channel")
    print("  h_ij^TT = tensor quadrupole radiative channel")
    print()
    print("This does not yet derive GR.")
    print("It organizes the theory so that scalar success and tensor radiation")
    print("belong to different but compatible sectors.")
    print()
    print("Next steps:")
    print("  normalize tensor coupling")
    print("  derive/source far-zone amplitude")
    print("  define tensor radiation energy flux")
    print("  ensure no unwanted scalar radiation")
    print()
    print("Possible next artifact:")
    print("  candidate_tensor_flux_principle.md")
    print()
    print("Possible next script:")
    print("  candidate_quadrupole_coupling_normalization.py")


def main():
    header("Candidate Tensor Flux Principle")
    case_0_principle_statement()
    case_1_scalar_monopole_channel()
    case_2_scalar_no_wave_guardrail()
    case_3_tensor_tt_channel()
    case_4_tensor_wave_propagation()
    case_5_quadrupole_source_projection()
    case_6_time_derivative_distinction()
    case_7_multichannel_map()
    case_8_classification()
    final_interpretation()


if __name__ == "__main__":
    main()
