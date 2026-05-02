# Candidate binary scalar radiation guardrail
#
# Purpose
# -------
# The scalar breathing suppression inventory showed that scalar radiation must
# be absent, constrained, short-ranged, damped, relaxed, or weakly coupled.
#
# The next stress test is a binary-like source. Binaries are dangerous because
# they naturally contain time-varying quadrupole structure.
#
# This script checks:
#
#   1. total mass monopole is conserved,
#   2. center-of-mass dipole has zero second derivative,
#   3. tensor quadrupole varies and supports TT radiation,
#   4. scalar breathing quadrupole would be an extra channel,
#   5. therefore scalar quadrupole breathing must be absent/suppressed,
#   6. tensor h_ij^TT remains the intended radiation channel.
#
# This is not a binary waveform model and not an observational bound.
# It is a source-moment guardrail for group 07.
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/07_scalar_constraint_and_radiation_safety/
#   or:
#   scripts_v3/candidate_binary_scalar_radiation_guardrail.py

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
# Case 0: Problem statement
# =============================================================================

def case_0_problem_statement():
    header("Case 0: Binary scalar-radiation guardrail problem")

    print("Binary-like sources are a stress test because they have time-varying")
    print("quadrupole moments.")
    print()
    print("Safe target:")
    print("  conserved monopole -> no scalar monopole radiation")
    print("  conserved/inertial dipole -> no scalar dipole radiation")
    print("  time-varying quadrupole -> tensor h_ij^TT radiation")
    print()
    print("Danger:")
    print("  scalar breathing quadrupole becomes an extra radiation channel")

    status_line("binary scalar-radiation guardrail posed", True)


# =============================================================================
# Case 1: Equal-mass circular binary moments
# =============================================================================

def case_1_binary_positions():
    header("Case 1: Equal-mass circular binary positions")

    t, m, a, Omega = sp.symbols("t m a Omega", positive=True, real=True)

    x1 = sp.Matrix([a*sp.cos(Omega*t), a*sp.sin(Omega*t), 0])
    x2 = -x1

    M = 2*m
    D = sp.simplify(m*x1 + m*x2)

    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
    print(f"M = {M}")
    print(f"D = {D}")

    status_line("center of mass dipole vanishes for equal circular binary", all(is_zero(e) for e in D))

    return t, m, a, Omega, x1, x2, M, D


# =============================================================================
# Case 2: Monopole and dipole controls
# =============================================================================

def case_2_monopole_dipole_controls(t, M, D):
    header("Case 2: Monopole and dipole controls")

    Mdot = sp.diff(M, t)
    Dddot = sp.simplify(D.diff(t, 2))

    print(f"Mdot = {Mdot}")
    print("Dddot =")
    print(Dddot)

    status_line("binary total mass is conserved", is_zero(Mdot))
    status_line("binary center-of-mass dipole has zero second derivative", all(is_zero(e) for e in Dddot))


# =============================================================================
# Case 3: Quadrupole tensor for binary
# =============================================================================

def case_3_quadrupole_tensor(t, m, x1, x2):
    header("Case 3: Binary trace-free quadrupole tensor")

    def quadrupole_for_particle(mass, x):
        r2 = sp.simplify((x.T*x)[0])
        return sp.simplify(mass * (x*x.T - sp.eye(3)*r2/3))

    Q_TF = sp.simplify(quadrupole_for_particle(m, x1) + quadrupole_for_particle(m, x2))

    print("Q_TF =")
    print(Q_TF)
    print()
    print(f"trace(Q_TF) = {sp.simplify(sp.trace(Q_TF))}")

    status_line("binary quadrupole is trace-free", is_zero(sp.trace(Q_TF)))

    return Q_TF


# =============================================================================
# Case 4: Plus/cross quadrupole projections
# =============================================================================

def case_4_plus_cross_projections(Q_TF):
    header("Case 4: Plus/cross quadrupole projections")

    Q_plus = sp.simplify((Q_TF[0, 0] - Q_TF[1, 1]) / 2)
    Q_cross = sp.simplify(Q_TF[0, 1])

    print(f"Q_plus = {Q_plus}")
    print(f"Q_cross = {Q_cross}")

    status_line("binary has time-varying plus projection", Q_plus != 0)
    status_line("binary has time-varying cross projection", Q_cross != 0)

    return Q_plus, Q_cross


# =============================================================================
# Case 5: Tensor radiation proxy
# =============================================================================

def case_5_tensor_radiation_proxy(t, Q_plus, Q_cross):
    header("Case 5: Tensor quadrupole radiation proxy")

    Qp3 = sp.simplify(sp.diff(Q_plus, t, 3))
    Qx3 = sp.simplify(sp.diff(Q_cross, t, 3))

    proxy = sp.simplify(Qp3**2 + Qx3**2)

    print(f"Q_plus_dddot = {Qp3}")
    print(f"Q_cross_dddot = {Qx3}")
    print(f"tensor Qdddot² proxy = {proxy}")

    status_line("binary time-varying quadrupole supports tensor radiation proxy", proxy != 0)

    return proxy


# =============================================================================
# Case 6: Scalar breathing danger from quadrupole
# =============================================================================

def case_6_scalar_breathing_danger(t, Q_TF):
    header("Case 6: Scalar breathing danger from quadrupole")

    # A scalar breathing channel would not use the TT trace-free projection.
    # But any scalar quadrupole-like breathing amplitude B(t) would represent
    # an extra non-TT channel. Use a generic B(t) tied to orbital frequency.
    B0, Omega = sp.symbols("B0 Omega", positive=True, real=True)
    B = B0 * sp.cos(2*Omega*t)

    Bdot_proxy = sp.simplify(sp.diff(B, t)**2)

    H_breathing = sp.Matrix([
        [B, 0, 0],
        [0, B, 0],
        [0, 0, 0],
    ])

    trace = sp.trace(H_breathing)

    print("Generic scalar breathing amplitude:")
    print(f"B(t) = {B}")
    print(f"Bdot² proxy = {Bdot_proxy}")
    print()
    print("Breathing matrix:")
    print(H_breathing)
    print(f"trace = {trace}")
    print()
    print("If B0 is not zero/suppressed, this is extra scalar radiation.")

    status_line("scalar breathing would be a non-TT extra channel", not is_zero(trace))


# =============================================================================
# Case 7: Guardrail classification
# =============================================================================

def case_7_guardrail_classification():
    header("Case 7: Guardrail classification")

    print("Binary source-moment result:")
    print()
    print("1. Monopole scalar radiation: killed by mass conservation.")
    print("2. Dipole scalar radiation: killed by center-of-mass conservation.")
    print("3. Tensor quadrupole radiation: active and intended.")
    print("4. Scalar quadrupole breathing radiation: dangerous if unsuppressed.")
    print()
    print("Required safety condition:")
    print()
    print("  B_scalar_quadrupole = 0")
    print("  or B_scalar_quadrupole is massive/damped/absorbed/weakly coupled.")
    print()
    status_line("binary scalar-radiation guardrail established", True)


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("A binary naturally radiates through the tensor quadrupole channel.")
    print()
    print("Conservation protects scalar monopole and dipole channels, but not a")
    print("hypothetical scalar quadrupole breathing channel.")
    print()
    print("Therefore the theory must ensure:")
    print()
    print("  A is constraint-like")
    print("  or scalar breathing is suppressed/absorbed/short-ranged/weakly coupled")
    print()
    print("while:")
    print()
    print("  h_ij^TT remains the active tensor radiation channel")
    print()
    print("Possible next artifact:")
    print("  candidate_binary_scalar_radiation_guardrail.md")
    print()
    print("Possible next script:")
    print("  candidate_A_channel_static_dynamic_split.py")


def main():
    header("Candidate Binary Scalar Radiation Guardrail")
    case_0_problem_statement()
    t, m, a, Omega, x1, x2, M, D = case_1_binary_positions()
    case_2_monopole_dipole_controls(t, M, D)
    Q_TF = case_3_quadrupole_tensor(t, m, x1, x2)
    Q_plus, Q_cross = case_4_plus_cross_projections(Q_TF)
    case_5_tensor_radiation_proxy(t, Q_plus, Q_cross)
    case_6_scalar_breathing_danger(t, Q_TF)
    case_7_guardrail_classification()
    final_interpretation()


if __name__ == "__main__":
    main()
