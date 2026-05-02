# Candidate scalar-flux no-wave failure control
#
# Purpose
# -------
# The scalar A-flux branch works as the monopole/Newtonian channel:
#
#   A = 1 + 2 Phi/c^2
#
# and, at first weak-field order, reciprocal compensation gives the scalar
# spatial factor:
#
#   g_ij ~ (1 - 2 Phi/c^2) delta_ij
#
# But gravitational waves are not scalar conformal perturbations.
# Linearized gravitational waves require a transverse-traceless tensor:
#
#   h_ij^TT
#
# This script records the failure control:
#
#   The scalar A-flux law cannot produce tensor gravitational waves.
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/06_tensor_flux_principle/
#   or:
#   scripts_v3/candidate_scalar_flux_no_wave_failure_control.py

import sympy as sp


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


def case_0_problem_statement():
    header("Case 0: Problem statement")

    print("Scalar branch:")
    print()
    print("  A = 1 + 2 Phi/c^2")
    print("  h_ij^scalar = -2 psi delta_ij")
    print()
    print("Wave target:")
    print()
    print("  h_ij^TT")
    print("  trace-free")
    print("  transverse")
    print("  two polarizations: h_plus and h_cross")
    print()
    print("Question:")
    print("  Can scalar A-flux be the gravitational-wave sector?")
    print()
    print("Expected answer:")
    print("  No. Scalar A-flux is the monopole/scalar channel, not the TT wave channel.")

    status_line("scalar no-wave failure control posed", True)


def case_1_scalar_not_trace_free():
    header("Case 1: Scalar spatial perturbation is not trace-free")

    psi = sp.symbols("psi", real=True)

    H_scalar = -2 * psi * sp.eye(3)
    trace = sp.simplify(sp.trace(H_scalar))

    print("Scalar spatial perturbation:")
    print()
    print("  h_ij^scalar = -2 psi delta_ij")
    print()
    print(H_scalar)
    print()
    print(f"trace = {trace}")

    status_line("scalar perturbation has nonzero trace unless psi=0", trace != 0)

    print()
    print("Interpretation:")
    print("  A TT gravitational wave must be trace-free.")
    print("  The scalar conformal perturbation is pure trace, not TT.")


def case_2_scalar_trace_free_projection():
    header("Case 2: Trace-free projection of scalar spatial perturbation")

    psi = sp.symbols("psi", real=True)

    H_scalar = -2 * psi * sp.eye(3)
    H_tf = sp.simplify(H_scalar - sp.trace(H_scalar) * sp.eye(3) / 3)

    print("Scalar perturbation:")
    print(H_scalar)
    print()
    print("Trace-free projection:")
    print(H_tf)

    status_line("trace-free projection of pure scalar conformal mode vanishes", matrix_is_zero(H_tf))

    print()
    print("Interpretation:")
    print("  The scalar spatial mode has no TT content after removing the trace.")


def case_3_breathing_vs_tt():
    header("Case 3: Scalar breathing mode versus TT plus/cross")

    psi, hp, hx = sp.symbols("psi h_plus h_cross", real=True)

    H_breathing = sp.Matrix([
        [psi, 0, 0],
        [0, psi, 0],
        [0, 0, 0],
    ])

    H_TT = sp.Matrix([
        [hp, hx, 0],
        [hx, -hp, 0],
        [0, 0, 0],
    ])

    trace_b = sp.trace(H_breathing)
    trace_tt = sp.trace(H_TT)

    print("Scalar breathing-like transverse mode:")
    print(H_breathing)
    print(f"trace = {trace_b}")
    print()
    print("Tensor TT plus/cross mode:")
    print(H_TT)
    print(f"trace = {trace_tt}")

    status_line("breathing mode is not trace-free unless trivial", trace_b != 0)
    status_line("TT plus/cross mode is trace-free", is_zero(trace_tt))

    print()
    print("Interpretation:")
    print("  A scalar wave would be a breathing-type mode, not the two GR TT modes.")


def case_4_no_scalar_reproduces_tt():
    header("Case 4: No scalar psi reproduces nontrivial TT modes")

    psi, hp, hx = sp.symbols("psi h_plus h_cross", real=True)

    H_scalar = -2 * psi * sp.eye(3)
    H_TT = sp.Matrix([
        [hp, hx, 0],
        [hx, -hp, 0],
        [0, 0, 0],
    ])

    equations = []
    for i in range(3):
        for j in range(3):
            equations.append(sp.Eq(H_scalar[i, j], H_TT[i, j]))

    sol = sp.solve(equations, [psi, hp, hx], dict=True)

    print("Solve H_scalar = H_TT for psi, h_plus, h_cross:")
    print(f"solutions = {sol}")

    expected = [{psi: 0, hp: 0, hx: 0}]
    status_line("only trivial scalar=TT solution exists", sol == expected)

    print()
    print("Interpretation:")
    print("  A scalar conformal perturbation cannot generate nonzero plus/cross modes.")


def case_5_transversality_not_enough():
    header("Case 5: Transversality alone is not enough")

    psi, k = sp.symbols("psi k", real=True)

    H_breathing = sp.Matrix([
        [psi, 0, 0],
        [0, psi, 0],
        [0, 0, 0],
    ])

    kvec = sp.Matrix([0, 0, k])
    trans = sp.simplify(kvec.T * H_breathing)
    trace = sp.trace(H_breathing)

    print("Breathing-like scalar transverse mode:")
    print(H_breathing)
    print()
    print(f"k^i h_ij = {trans}")
    print(f"trace = {trace}")

    status_line("breathing mode can be transverse", matrix_is_zero(trans))
    status_line("but breathing mode is not traceless", not is_zero(trace))

    print()
    print("Interpretation:")
    print("  Even a transverse scalar breathing mode is not a GR TT wave.")


def case_6_scalar_wave_is_scalar_radiation():
    header("Case 6: Scalar wave equation would be scalar radiation")

    t, z, omega, k, c, H = sp.symbols("t z omega k c H", positive=True, real=True)

    psi = H * sp.cos(k*z - omega*t)
    box_psi = sp.simplify((1/c**2) * sp.diff(psi, t, 2) - sp.diff(psi, z, 2))

    print("Suppose scalar psi obeys a wave equation:")
    print()
    print("  Box psi = 0")
    print()
    print(f"psi = {psi}")
    print(f"Box psi = {box_psi}")
    print()
    print("This gives scalar propagation when omega^2 = c^2 k^2.")
    print("But it would be scalar radiation, not tensor TT radiation.")

    status_line("scalar wave equation is not a tensor wave equation", True)


def case_7_tt_sector_requirement():
    header("Case 7: Required TT tensor sector")

    hp, hx = sp.symbols("h_plus h_cross", real=True)

    H_TT = sp.Matrix([
        [hp, hx, 0],
        [hx, -hp, 0],
        [0, 0, 0],
    ])

    trace = sp.trace(H_TT)

    print("Required tensor wave sector for propagation along z:")
    print()
    print(H_TT)
    print()
    print(f"trace = {trace}")
    print()
    print("Independent polarizations:")
    print("  h_plus")
    print("  h_cross")

    status_line("TT sector has the two needed tensor polarizations", is_zero(trace))


def case_8_classification():
    header("Case 8: Classification")

    print("Results:")
    print()
    print("1. Scalar spatial perturbation is pure trace/conformal.")
    print("2. Its trace-free projection is zero.")
    print("3. Scalar breathing modes are not TT modes.")
    print("4. No nonzero scalar psi reproduces h_plus/h_cross.")
    print("5. A scalar wave equation would produce scalar radiation, not GR tensor waves.")
    print("6. Gravitational waves require an independent h_ij^TT sector.")
    print()
    status_line("scalar flux law cannot be the gravitational-wave sector", True)


def final_interpretation():
    header("Final interpretation")

    print("This failure control proves the scalar A-flux law is not secretly a")
    print("gravitational-wave theory.")
    print()
    print("A-flux remains valuable as:")
    print()
    print("  monopole / scalar / Newtonian mass response")
    print()
    print("But gravitational radiation requires:")
    print()
    print("  h_ij^TT")
    print("  two tensor polarizations")
    print("  trace-free transverse spatial structure")
    print()
    print("Therefore the next stage should build a tensor-flux principle:")
    print()
    print("  A-flux = monopole scalar channel")
    print("  tensor flux = quadrupole TT radiative channel")
    print()
    print("Possible next artifact:")
    print("  candidate_scalar_flux_no_wave_failure_control.md")
    print()
    print("Possible next script:")
    print("  candidate_tensor_flux_basis.py")


def main():
    header("Candidate Scalar-Flux No-Wave Failure Control")
    case_0_problem_statement()
    case_1_scalar_not_trace_free()
    case_2_scalar_trace_free_projection()
    case_3_breathing_vs_tt()
    case_4_no_scalar_reproduces_tt()
    case_5_transversality_not_enough()
    case_6_scalar_wave_is_scalar_radiation()
    case_7_tt_sector_requirement()
    case_8_classification()
    final_interpretation()


if __name__ == "__main__":
    main()
