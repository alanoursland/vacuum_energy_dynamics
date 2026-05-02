# Candidate no-extra-polarization policy
#
# Purpose
# -------
# The A-channel split established:
#
#   A = A_constraint + A_rad
#
# with:
#
#   A_constraint allowed as static scalar gravity,
#   A_rad dangerous unless zero/suppressed/absorbed/short-ranged/weak.
#
# This script states a polarization policy:
#
#   Ordinary long-range gravitational radiation should contain only the
#   tensor plus/cross TT modes unless additional modes are deliberately
#   introduced and tightly constrained.
#
# Tests:
#
#   1. TT plus/cross modes are trace-free and transverse.
#   2. Scalar breathing mode is non-TT.
#   3. Longitudinal scalar mode is non-transverse.
#   4. Vector-like radiation is outside current allowed radiation channel.
#   5. Allowed radiation set = {h_plus, h_cross}.
#   6. Extra modes require suppression flags.
#
# This is a policy/architecture guardrail, not an observational analysis.
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/07_scalar_constraint_and_radiation_safety/
#   or:
#   scripts_v3/candidate_no_extra_polarization_policy.py

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


def matrix_is_zero(M) -> bool:
    return all(is_zero(entry) for entry in list(M))


# =============================================================================
# Case 0: Problem statement
# =============================================================================

def case_0_problem_statement():
    header("Case 0: No-extra-polarization policy problem")

    print("Current radiation target:")
    print()
    print("  allowed ordinary long-range radiation: h_plus, h_cross")
    print()
    print("Dangerous extra modes:")
    print()
    print("  scalar breathing")
    print("  scalar longitudinal")
    print("  unsuppressed vector modes")
    print()
    print("Policy:")
    print()
    print("  Extra modes must be absent, projected out, damped, absorbed,")
    print("  massive/short-ranged, weakly coupled, or observationally constrained.")

    status_line("no-extra-polarization policy posed", True)


# =============================================================================
# Case 1: TT plus/cross allowed modes
# =============================================================================

def case_1_allowed_tt_modes():
    header("Case 1: Allowed TT plus/cross modes")

    hp, hx, k = sp.symbols("h_plus h_cross k", real=True)

    H_TT = sp.Matrix([
        [hp, hx, 0],
        [hx, -hp, 0],
        [0, 0, 0],
    ])

    trace = sp.trace(H_TT)
    kvec = sp.Matrix([0, 0, k])
    trans = sp.simplify(kvec.T * H_TT)

    print("H_TT =")
    print(H_TT)
    print(f"trace = {trace}")
    print("k^i H_ij =")
    print(trans)

    status_line("plus/cross modes are trace-free", is_zero(trace))
    status_line("plus/cross modes are transverse for z propagation", matrix_is_zero(trans))


# =============================================================================
# Case 2: Scalar breathing is extra
# =============================================================================

def case_2_scalar_breathing_extra():
    header("Case 2: Scalar breathing is an extra non-TT mode")

    b, k = sp.symbols("b k", real=True)

    H_breathing = sp.Matrix([
        [b, 0, 0],
        [0, b, 0],
        [0, 0, 0],
    ])

    trace = sp.trace(H_breathing)
    kvec = sp.Matrix([0, 0, k])
    trans = sp.simplify(kvec.T * H_breathing)

    print("H_breathing =")
    print(H_breathing)
    print(f"trace = {trace}")
    print("k^i H_ij =")
    print(trans)

    status_line("breathing mode may be transverse", matrix_is_zero(trans))
    status_line("breathing mode is not traceless", not is_zero(trace))
    status_line("breathing mode must be suppressed unless deliberately allowed", True)


# =============================================================================
# Case 3: Longitudinal scalar is extra
# =============================================================================

def case_3_longitudinal_extra():
    header("Case 3: Longitudinal scalar is an extra non-TT mode")

    l, k = sp.symbols("ell k", real=True)

    H_long = sp.Matrix([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, l],
    ])

    trace = sp.trace(H_long)
    kvec = sp.Matrix([0, 0, k])
    trans = sp.simplify(kvec.T * H_long)

    print("H_longitudinal =")
    print(H_long)
    print(f"trace = {trace}")
    print("k^i H_ij =")
    print(trans)

    status_line("longitudinal mode is not transverse", not matrix_is_zero(trans))
    status_line("longitudinal mode is not allowed as ordinary radiation", True)


# =============================================================================
# Case 4: Vector-like modes are separate sector
# =============================================================================

def case_4_vector_modes_separate():
    header("Case 4: Vector-like modes are separate sector")

    Vx, Vy, Vz = sp.symbols("V_x V_y V_z", real=True)
    W = sp.Matrix([Vx, Vy, Vz])

    print("Vector/current sector candidate:")
    print(f"W_i = {W}")
    print()
    print("Interpretation:")
    print("  W_i may be needed for frame dragging.")
    print("  It is not the ordinary TT radiation channel.")
    print("  Any long-range vector radiation would require separate derivation and constraints.")

    status_line("vector modes are outside current allowed radiation set", True)


# =============================================================================
# Case 5: Allowed / forbidden mode policy
# =============================================================================

def case_5_policy_table():
    header("Case 5: Allowed / controlled mode policy")

    print("| Mode | Status | Required condition |")
    print("|---|---|---|")
    print("| h_plus | allowed | TT tensor radiation |")
    print("| h_cross | allowed | TT tensor radiation |")
    print("| scalar breathing | controlled | zero/suppressed/absorbed/massive/weak |")
    print("| scalar longitudinal | controlled | projected out/suppressed |")
    print("| vector radiation | controlled | separate derivation and constraints |")
    print()
    status_line("polarization policy table stated", True)


# =============================================================================
# Case 6: A_rad flag policy
# =============================================================================

def case_6_A_rad_flags():
    header("Case 6: A_rad suppression flags")

    print("For A_rad, allowed safety flags are:")
    print()
    print("  absent")
    print("  projected_out")
    print("  damped_absorbed")
    print("  relaxes_to_minimum")
    print("  massive_short_ranged")
    print("  weakly_coupled")
    print("  observationally_constrained")
    print()
    print("Unsafe flag:")
    print()
    print("  unsuppressed_massless_scalar_wave")

    status_line("A_rad requires explicit safety flag", True)


# =============================================================================
# Case 7: Classification
# =============================================================================

def case_7_classification():
    header("Case 7: Classification")

    print("Results:")
    print()
    print("1. h_plus and h_cross are allowed ordinary long-range radiation modes.")
    print("2. Scalar breathing is non-TT and must be controlled.")
    print("3. Scalar longitudinal is non-TT and must be controlled.")
    print("4. Vector radiation is outside the current ordinary radiation channel.")
    print("5. A_rad must carry a suppression/absence flag.")
    print("6. The theory's ordinary radiation claim should remain TT-only for now.")
    print()
    status_line("no-extra-polarization policy established", True)


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("The current radiation policy is:")
    print()
    print("  Ordinary long-range gravitational radiation = h_plus + h_cross.")
    print()
    print("Extra scalar/vector polarizations are not allowed unless separately")
    print("derived and suppressed/constrained.")
    print()
    print("This protects the scalar A channel from becoming an unwanted")
    print("scalar-radiation theory.")
    print()
    print("Possible next artifact:")
    print("  candidate_no_extra_polarization_policy.md")
    print()
    print("Possible next file:")
    print("  scalar_constraint_and_radiation_safety_summary.md")


def main():
    header("Candidate No Extra Polarization Policy")
    case_0_problem_statement()
    case_1_allowed_tt_modes()
    case_2_scalar_breathing_extra()
    case_3_longitudinal_extra()
    case_4_vector_modes_separate()
    case_5_policy_table()
    case_6_A_rad_flags()
    case_7_classification()
    final_interpretation()


if __name__ == "__main__":
    main()
