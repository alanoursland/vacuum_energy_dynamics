# Candidate vector boundary value problem
#
# Purpose
# -------
# The vector global rotation mode study found:
#
#   J = integral r x j d^3x
#
# as the global angular-momentum source, and suggested the symbolic far-field:
#
#   B_W ~ C_W J/r^3
#
# This script solves a symbolic exterior vector boundary-value model that
# produces a dipole-like vector potential and curl field.
#
# It keeps all coefficients symbolic.
# It does NOT insert the Lense-Thirring coefficient.

import sympy as sp


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_line(label: str, status: str, detail: str = "") -> None:
    marks = {
        "DERIVED_REDUCED": "PASS",
        "CONSTRAINED_BY_IDENTITY": "WARN",
        "MISSING": "FAIL",
        "RISK": "WARN",
        "HAND_ASSIGNED": "WARN",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


def case_0_problem_statement():
    header("Case 0: Vector boundary value problem")

    print("Question:")
    print()
    print("  Can boundary angular momentum J produce an exterior vector field")
    print("  with curl diagnostic B_W ~ J/r^3?")
    print()
    print("Rules:")
    print()
    print("  keep all coefficients symbolic")
    print("  do not insert Lense-Thirring normalization")
    print("  solve only the structural exterior shape")

    status_line("vector boundary-value problem posed", "CONSTRAINED_BY_IDENTITY")


def case_1_boundary_data():
    header("Case 1: Boundary angular momentum data")

    J, R, Cb = sp.symbols("J R C_b", positive=True, real=True)

    boundary_data = Cb * J / R**2

    print("Compact rotating source:")
    print()
    print("  radius: R")
    print("  angular momentum: J")
    print()
    print("Symbolic boundary amplitude:")
    print()
    print("  W_phi(R, pi/2) = C_b J/R^2")
    print()
    print(f"boundary_data = {boundary_data}")
    print()
    print("C_b is not derived.")

    status_line("boundary data stated symbolically", "CONSTRAINED_BY_IDENTITY",
                "boundary coefficient missing")


def case_2_exterior_ansatz():
    header("Case 2: Exterior dipole-like vector ansatz")

    r, theta, J, Cj = sp.symbols("r theta J C_J", positive=True, real=True)

    W_phi = Cj * J * sp.sin(theta) / r**2

    print("Exterior ansatz:")
    print()
    print("  W_phi(r, theta) = C_J J sin(theta)/r^2")
    print()
    print(f"W_phi = {W_phi}")
    print()
    print("Interpretation:")
    print("  This is the axial/vector dipole-like exterior shape.")
    print("  C_J is symbolic and not derived.")

    status_line("exterior vector ansatz stated", "CONSTRAINED_BY_IDENTITY",
                "coefficient missing")

    return r, theta, J, Cj, W_phi


def case_3_curl_scaling(r, theta, J, Cj, W_phi):
    header("Case 3: Curl diagnostic scaling")

    B_r = sp.simplify((1/(r*sp.sin(theta))) * sp.diff(sp.sin(theta)*W_phi, theta))
    B_theta = sp.simplify(-(1/r) * sp.diff(r*W_phi, r))

    print("For W = W_phi e_phi:")
    print()
    print("B_r = (curl W)_r =")
    print(B_r)
    print()
    print("B_theta = (curl W)_theta =")
    print(B_theta)
    print()
    print("Both scale as J/r^3.")

    scale_r = sp.simplify(B_r * r**3 / J)
    scale_t = sp.simplify(B_theta * r**3 / J)
    ok = (not scale_r.has(r)) and (not scale_t.has(r))

    status_line("curl diagnostic has J/r^3 scaling",
                "DERIVED_REDUCED" if ok else "RISK")


def case_4_boundary_matching_relation():
    header("Case 4: Boundary matching relation")

    J, R, Cb, Cj = sp.symbols("J R C_b C_J", positive=True, real=True)

    W_boundary_from_ansatz = Cj * J / R**2
    W_boundary_target = Cb * J / R**2

    solution = sp.solve(sp.Eq(W_boundary_from_ansatz, W_boundary_target), Cj)

    print("At equator theta = pi/2:")
    print()
    print("  ansatz gives W_phi(R) = C_J J/R^2")
    print("  boundary target is W_phi(R) = C_b J/R^2")
    print()
    print(f"C_J solution = {solution}")
    print()
    print("Thus C_J is fixed by boundary coefficient C_b.")
    print("But C_b is still missing.")

    status_line("boundary matching fixes exterior coefficient from boundary coefficient",
                "CONSTRAINED_BY_IDENTITY",
                "boundary coefficient still missing")


def case_5_precession_chain():
    header("Case 5: Precession chain remains symbolic")

    J, r, Cw, beta_W = sp.symbols("J r C_W beta_W", positive=True, real=True)

    B_W = Cw * J / r**3
    Omega_drag = beta_W * B_W

    print("Curl diagnostic:")
    print()
    print(f"B_W = {B_W}")
    print()
    print("Symbolic precession relation:")
    print()
    print(f"Omega_drag = {Omega_drag}")
    print()
    print("Combined coefficient:")
    print()
    print("  C_total = beta_W C_W")
    print()
    print("C_total is not derived.")

    status_line("precession chain symbolic", "MISSING",
                "observable coefficient not derived")


def case_6_no_gr_matching():
    header("Case 6: No GR matching discipline")

    print("Forbidden:")
    print()
    print("  choose C_b, C_J, C_W, beta_W, or C_total to match Lense-Thirring")
    print()
    print("Allowed:")
    print()
    print("  derive boundary coefficient from vector action/source model")
    print("  derive beta_W from observable/precession coupling")
    print("  declare coefficient phenomenological")
    print()
    print("Current status:")
    print()
    print("  shape: derived/reduced")
    print("  normalization: missing")

    status_line("GR matching forbidden", "RISK",
                "normalization must not be inserted")


def case_7_classification():
    header("Case 7: Classification")

    print("| Item | Status |")
    print("|---|---|")
    print("| boundary angular momentum J | CONSTRAINED_BY_IDENTITY |")
    print("| W_phi ~ J sin(theta)/r^2 ansatz | CONSTRAINED_BY_IDENTITY |")
    print("| curl B_W ~ J/r^3 scaling | DERIVED_REDUCED |")
    print("| C_J from boundary C_b | CONSTRAINED_BY_IDENTITY |")
    print("| boundary coefficient C_b | MISSING |")
    print("| precession coefficient beta_W | MISSING |")
    print("| Lense-Thirring normalization | HAND_ASSIGNED if inserted now |")

    status_line("boundary-value classification produced", "CONSTRAINED_BY_IDENTITY",
                "shape derived, normalization missing")


def case_8_next_tests():
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_vector_boundary_coefficient_from_action.py")
    print("   Try to relate C_b to alpha_W/(2K_c) and source angular momentum.")
    print()
    print("2. candidate_kappa_source_law_from_trace_exchange.py")
    print("   Work missing kappa source law.")
    print()
    print("3. candidate_tensor_source_from_exchange_identity.py")
    print("   Work hand-assigned tensor coupling.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_vector_boundary_coefficient_from_action.py")

    status_line("next test selected", "CONSTRAINED_BY_IDENTITY",
                "boundary coefficient is the remaining vector gap")


def final_interpretation():
    header("Final interpretation")

    print("A symbolic exterior vector boundary-value model gives:")
    print()
    print("  W_phi ~ J sin(theta)/r^2")
    print()
    print("and therefore:")
    print()
    print("  B_W = curl W ~ J/r^3")
    print()
    print("This recovers the expected angular-momentum far-field shape.")
    print()
    print("But the normalization is still missing:")
    print()
    print("  C_b, C_J, C_W, beta_W")
    print()
    print("Possible next artifact:")
    print("  candidate_vector_boundary_value_problem.md")
    print()
    print("Possible next script:")
    print("  candidate_vector_boundary_coefficient_from_action.py")


def main():
    header("Candidate Vector Boundary Value Problem")
    case_0_problem_statement()
    case_1_boundary_data()
    r, theta, J, Cj, W_phi = case_2_exterior_ansatz()
    case_3_curl_scaling(r, theta, J, Cj, W_phi)
    case_4_boundary_matching_relation()
    case_5_precession_chain()
    case_6_no_gr_matching()
    case_7_classification()
    case_8_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
