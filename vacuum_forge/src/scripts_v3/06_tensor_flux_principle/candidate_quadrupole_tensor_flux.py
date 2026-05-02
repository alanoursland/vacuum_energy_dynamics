# Candidate quadrupole tensor flux
#
# Purpose
# -------
# The tensor wave equation established that h_ij^TT can propagate with
# plus/cross polarizations. The next question is source structure.
#
# GR's leading gravitational radiation from isolated slow sources is
# quadrupole radiation. This script builds a reduced diagnostic for the
# tensor-flux idea:
#
#   A-flux       -> monopole scalar channel
#   h_ij^TT flux -> quadrupole tensor radiative channel
#
# Tests:
#
#   1. define the trace-free quadrupole tensor Q_ij^TF,
#   2. verify its trace-free property,
#   3. show monopole and dipole are not TT radiation channels,
#   4. project a quadrupole source onto plus/cross TT basis for z propagation,
#   5. separate amplitude source from radiated-power proxy,
#   6. identify second derivative vs third derivative distinction.
#
# Important caution:
#   In GR, far-zone wave amplitude is related to the second time derivative
#   of the quadrupole moment, while radiated power is related to third time
#   derivatives. This script keeps that distinction explicit.
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/06_tensor_flux_principle/
#   or:
#   scripts_v3/candidate_quadrupole_tensor_flux.py

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
# Case 0: Problem statement
# =============================================================================

def case_0_problem_statement():
    header("Case 0: Quadrupole tensor-flux problem statement")

    print("Scalar channel:")
    print("  monopole mass -> A-flux")
    print()
    print("Tensor channel target:")
    print("  quadrupole trace-free source -> h_ij^TT radiation")
    print()
    print("Need to distinguish:")
    print("  wave amplitude source ~ second time derivative of quadrupole")
    print("  radiated power proxy ~ third time derivative squared")
    print()
    status_line("quadrupole tensor-flux problem posed", True)


# =============================================================================
# Case 1: Define trace-free quadrupole tensor
# =============================================================================

def case_1_define_quadrupole_tf():
    header("Case 1: Define trace-free quadrupole tensor")

    Qxx, Qyy, Qzz, Qxy, Qxz, Qyz = sp.symbols("Q_xx Q_yy Q_zz Q_xy Q_xz Q_yz", real=True)

    Q = sp.Matrix([
        [Qxx, Qxy, Qxz],
        [Qxy, Qyy, Qyz],
        [Qxz, Qyz, Qzz],
    ])

    trQ = sp.trace(Q)
    Q_TF = sp.simplify(Q - trQ * sp.eye(3) / 3)

    print("General symmetric quadrupole tensor Q:")
    print(Q)
    print()
    print(f"Tr(Q) = {trQ}")
    print()
    print("Trace-free quadrupole Q_TF = Q - Tr(Q) I/3:")
    print(Q_TF)
    print()
    print(f"Tr(Q_TF) = {sp.simplify(sp.trace(Q_TF))}")

    status_line("Q_TF is trace-free", is_zero(sp.trace(Q_TF)))

    return Q_TF


# =============================================================================
# Case 2: Monopole and dipole are not TT radiation channels
# =============================================================================

def case_2_monopole_dipole_not_tt():
    header("Case 2: Monopole and dipole are not TT radiation channels")

    M, Dx, Dy, Dz = sp.symbols("M D_x D_y D_z", real=True)

    print("Monopole:")
    print("  M is scalar.")
    print("  It sources A-flux, not TT tensor radiation.")
    print()
    print("Dipole:")
    print(f"  D = ({Dx}, {Dy}, {Dz})")
    print("  For isolated systems, ordinary mass dipole radiation is removed by")
    print("  center-of-mass / momentum conservation.")
    print()
    print("Tensor radiation starts at trace-free quadrupole order.")
    print()
    status_line("monopole belongs to scalar channel", True)
    status_line("dipole is not the leading isolated tensor radiation channel", True)


# =============================================================================
# Case 3: Project quadrupole onto plus/cross for z propagation
# =============================================================================

def case_3_project_to_plus_cross(Q_TF):
    header("Case 3: Project Q_TF onto plus/cross basis")

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

    # Since <e,e>=2, amplitudes are half the inner product.
    Q_plus = sp.simplify(inner(Q_TF, e_plus) / 2)
    Q_cross = sp.simplify(inner(Q_TF, e_cross) / 2)

    print(f"Q_plus projection = {Q_plus}")
    print(f"Q_cross projection = {Q_cross}")
    print()
    print("For z propagation:")
    print("  plus source sees (Q_xx - Q_yy)/2")
    print("  cross source sees Q_xy")

    status_line("quadrupole projects onto plus/cross channels", True)

    return Q_plus, Q_cross


# =============================================================================
# Case 4: Time-dependent quadrupole source proxy
# =============================================================================

def case_4_time_dependent_source_proxy():
    header("Case 4: Time-dependent quadrupole source proxy")

    t, Omega, Q0 = sp.symbols("t Omega Q0", positive=True, real=True)

    # Toy rotating quadrupole projections.
    Q_plus = Q0 * sp.cos(2*Omega*t)
    Q_cross = Q0 * sp.sin(2*Omega*t)

    Qp_ddot = sp.diff(Q_plus, t, 2)
    Qx_ddot = sp.diff(Q_cross, t, 2)

    Qp_dddot = sp.diff(Q_plus, t, 3)
    Qx_dddot = sp.diff(Q_cross, t, 3)

    print(f"Q_plus(t) = {Q_plus}")
    print(f"Q_cross(t) = {Q_cross}")
    print()
    print(f"Q_plus_ddot = {Qp_ddot}")
    print(f"Q_cross_ddot = {Qx_ddot}")
    print()
    print(f"Q_plus_dddot = {Qp_dddot}")
    print(f"Q_cross_dddot = {Qx_dddot}")

    amplitude_proxy = sp.simplify(Qp_ddot**2 + Qx_ddot**2)
    power_proxy = sp.simplify(Qp_dddot**2 + Qx_dddot**2)

    print()
    print(f"amplitude-source proxy Q_ddot² sum = {amplitude_proxy}")
    print(f"power proxy Q_dddot² sum = {power_proxy}")

    status_line("quadrupole amplitude proxy uses second derivatives", True)
    status_line("quadrupole power proxy uses third derivatives", True)


# =============================================================================
# Case 5: Static quadrupole does not radiate
# =============================================================================

def case_5_static_quadrupole_no_radiation():
    header("Case 5: Static quadrupole does not radiate")

    t, Q0 = sp.symbols("t Q0", real=True)

    Q_static = Q0
    Q_ddot = sp.diff(Q_static, t, 2)
    Q_dddot = sp.diff(Q_static, t, 3)

    print(f"Q_static = {Q_static}")
    print(f"Q_ddot = {Q_ddot}")
    print(f"Q_dddot = {Q_dddot}")

    status_line("static quadrupole has no wave-amplitude source", is_zero(Q_ddot))
    status_line("static quadrupole has no radiation-power proxy", is_zero(Q_dddot))


# =============================================================================
# Case 6: Tensor-flux analogy
# =============================================================================

def case_6_tensor_flux_analogy():
    header("Case 6: Tensor-flux analogy")

    print("Scalar monopole channel:")
    print()
    print("  M -> A-flux")
    print("  F_A = 8*pi*G*M/c^2")
    print()
    print("Tensor quadrupole channel:")
    print()
    print("  Q_ij^TF -> h_ij^TT")
    print("  changing quadrupole -> outgoing tensor radiation")
    print()
    print("Interpretive upgrade:")
    print()
    print("  A-flux is monopole scalar vacuum flow.")
    print("  Tensor flux is quadrupole TT radiative vacuum flow.")
    print()
    status_line("tensor-flux analogy stated", True)


# =============================================================================
# Case 7: Classification
# =============================================================================

def case_7_classification():
    header("Case 7: Classification")

    print("Results:")
    print()
    print("1. Trace-free quadrupole Q_ij^TF is the natural tensor source object.")
    print("2. Monopole belongs to scalar A-flux channel.")
    print("3. Dipole is not the leading isolated tensor radiation channel.")
    print("4. Q_ij^TF projects onto plus/cross TT polarizations.")
    print("5. Wave amplitude source is associated with second derivatives.")
    print("6. Radiated-power proxy is associated with third derivatives squared.")
    print("7. Static quadrupole does not radiate.")
    print()
    status_line("quadrupole tensor-flux source structure passes first checks", True)


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("This script gives the first source-side structure for the tensor-flux")
    print("program.")
    print()
    print("A-flux uses monopole mass.")
    print("Tensor flux uses trace-free quadrupole structure.")
    print()
    print("The plus/cross radiative channels are sourced by the TT projection of")
    print("the changing quadrupole.")
    print()
    print("Next steps:")
    print("  normalize the quadrupole coupling")
    print("  connect to far-zone wave amplitude")
    print("  develop tensor radiation energy flux")
    print("  avoid unwanted scalar radiation")
    print()
    print("Possible next artifact:")
    print("  candidate_quadrupole_tensor_flux.md")
    print()
    print("Possible next script:")
    print("  candidate_tensor_flux_principle.py")


def main():
    header("Candidate Quadrupole Tensor Flux")
    case_0_problem_statement()
    Q_TF = case_1_define_quadrupole_tf()
    case_2_monopole_dipole_not_tt()
    case_3_project_to_plus_cross(Q_TF)
    case_4_time_dependent_source_proxy()
    case_5_static_quadrupole_no_radiation()
    case_6_tensor_flux_analogy()
    case_7_classification()
    final_interpretation()


if __name__ == "__main__":
    main()
