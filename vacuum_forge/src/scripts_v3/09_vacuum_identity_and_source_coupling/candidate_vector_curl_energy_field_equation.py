# Candidate vector curl-energy field equation
#
# Purpose
# -------
# The vector stiffness study identified the most gauge-aware vector path:
#
#   E_W = integral [ K_c |curl W|^2 + alpha_W j_i W_i ] d^3x
#
# This script derives the schematic field equation:
#
#   curl curl W = source
#
# and shows that under a transverse gauge div W = 0, this reduces to:
#
#   -Delta W = source
#
# The coefficient alpha_W/K_c remains symbolic.
#
# This is a structural derivation, not a coefficient derivation.
# It does NOT insert Lense-Thirring normalization.
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/09_vacuum_identity_and_source_coupling/
#   or:
#   scripts_v3/candidate_vector_curl_energy_field_equation.py

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


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def curl(V, coords):
    x, y, z = coords
    return sp.Matrix([
        sp.diff(V[2], y) - sp.diff(V[1], z),
        sp.diff(V[0], z) - sp.diff(V[2], x),
        sp.diff(V[1], x) - sp.diff(V[0], y),
    ])


def div(V, coords):
    return sp.simplify(sum(sp.diff(V[i], coords[i]) for i in range(3)))


def lap_vec(V, coords):
    return sp.Matrix([
        sp.simplify(sum(sp.diff(V[i], q, 2) for q in coords))
        for i in range(3)
    ])


def grad_scalar(f, coords):
    return sp.Matrix([sp.diff(f, q) for q in coords])


def case_0_problem_statement():
    header("Case 0: Vector curl-energy field equation problem")

    print("Candidate vector energy:")
    print()
    print("  E_W = integral [ K_c |curl W|^2 + alpha_W j.W ] d^3x")
    print()
    print("Question:")
    print()
    print("  What field equation follows from curl-energy?")
    print()
    print("Expected structure:")
    print()
    print("  curl curl W = source")
    print()
    print("Under div W = 0:")
    print()
    print("  -Delta W = source")
    print()
    print("Coefficient remains symbolic.")

    status_line("curl-energy field-equation problem posed", "CONSTRAINED_BY_IDENTITY")


def case_1_vector_identity():
    header("Case 1: Vector identity curl curl W")

    x, y, z = sp.symbols("x y z", real=True)
    coords = (x, y, z)

    Wx = sp.Function("W_x")(x, y, z)
    Wy = sp.Function("W_y")(x, y, z)
    Wz = sp.Function("W_z")(x, y, z)
    W = sp.Matrix([Wx, Wy, Wz])

    curlcurl = sp.simplify(curl(curl(W, coords), coords))
    graddiv_minus_lap = sp.simplify(grad_scalar(div(W, coords), coords) - lap_vec(W, coords))

    diff = sp.simplify(curlcurl - graddiv_minus_lap)

    print("Identity:")
    print()
    print("  curl curl W = grad(div W) - Delta W")
    print()
    print("Check curlcurl - [grad div W - Delta W] =")
    print(diff)

    ok = all(is_zero(e) for e in diff)
    status_line("curl-curl identity verified", "DERIVED_REDUCED" if ok else "RISK")


def case_2_transverse_reduction():
    header("Case 2: Transverse reduction")

    print("If the vector sector is placed in transverse gauge:")
    print()
    print("  div W = 0")
    print()
    print("then:")
    print()
    print("  curl curl W = -Delta W")
    print()
    print("This recovers a Poisson-like vector equation from curl-energy:")
    print()
    print("  Delta W_i ~ source_i")
    print()
    print("Interpretation:")
    print("  curl-energy naturally favors transverse/vector content.")

    status_line("transverse reduction gives vector Poisson form", "CONSTRAINED_BY_IDENTITY",
                "requires gauge condition div W=0")


def case_3_variational_structure():
    header("Case 3: Variational field-equation structure")

    K_c, alpha_W = sp.symbols("K_c alpha_W", positive=True, real=True)

    print("Energy:")
    print()
    print("  E = integral [ K_c |curl W|^2 + alpha_W j.W ] d^3x")
    print()
    print("Variation gives boundary + bulk terms.")
    print("After integrating by parts, the schematic bulk equation is:")
    print()
    print("  2 K_c curl curl W + alpha_W j = 0")
    print()
    print("Therefore:")
    print()
    print("  curl curl W = - alpha_W j / (2 K_c)")
    print()
    print("Under div W = 0:")
    print()
    print("  Delta W = alpha_W j / (2 K_c)")
    print()
    print("Coefficient target:")
    print()
    print("  alpha_W / (2 K_c)")

    status_line("curl-energy variation gives source equation", "CONSTRAINED_BY_IDENTITY",
                "coefficient remains symbolic")


def case_4_pure_gradient_null_mode():
    header("Case 4: Pure-gradient null mode")

    x, y, z = sp.symbols("x y z", real=True)
    coords = (x, y, z)
    phi = sp.Function("phi")(x, y, z)

    W_grad = grad_scalar(phi, coords)
    curl_grad = sp.simplify(curl(W_grad, coords))

    print("For W = grad phi:")
    print()
    print("curl W =")
    print(curl_grad)
    print()
    print("Thus |curl W|^2 does not penalize pure-gradient pieces.")
    print("This is gauge-like behavior and requires gauge fixing or boundary conditions.")

    ok = all(is_zero(e) for e in curl_grad)
    status_line("curl-energy has pure-gradient null mode", "CONSTRAINED_BY_IDENTITY" if ok else "RISK",
                "gauge fixing required")


def case_5_current_transversality():
    header("Case 5: Current transversality condition")

    print("Curl-energy with transverse W naturally couples most cleanly to")
    print("transverse current:")
    print()
    print("  div j = 0")
    print()
    print("For stationary incompressible currents, this is compatible with")
    print("mass continuity:")
    print()
    print("  partial_t rho = 0")
    print("  div j = 0")
    print()
    print("For time-dependent sources, longitudinal/current-continuity pieces")
    print("must be handled by scalar constraint or gauge structure.")

    status_line("stationary transverse current compatibility stated", "CONSTRAINED_BY_IDENTITY",
                "time-dependent split still missing")


def case_6_coefficient_status():
    header("Case 6: Coefficient status")

    alpha_W, K_c = sp.symbols("alpha_W K_c", positive=True, real=True)
    ratio = alpha_W/(2*K_c)

    print("The curl-energy field equation identifies the coefficient ratio:")
    print()
    print(f"alpha_W/(2 K_c) = {ratio}")
    print()
    print("But this script does not derive alpha_W or K_c.")
    print()
    print("Current status:")
    print()
    print("  equation structure: derived from candidate curl-energy")
    print("  coefficient: missing")
    print("  GR normalization: not inserted")

    status_line("coefficient ratio identified but not derived", "MISSING",
                "normalization still absent")


def case_7_classification():
    header("Case 7: Classification")

    print("| Item | Status |")
    print("|---|---|")
    print("| curl curl W identity | DERIVED_REDUCED |")
    print("| transverse reduction to Delta W | CONSTRAINED_BY_IDENTITY |")
    print("| curl-energy field equation | CONSTRAINED_BY_IDENTITY |")
    print("| pure-gradient null mode | CONSTRAINED_BY_IDENTITY / gauge issue |")
    print("| coefficient alpha_W/(2K_c) | MISSING |")
    print("| full time-dependent current split | MISSING |")
    print("| GR frame-dragging normalization | HAND_ASSIGNED if inserted now |")

    status_line("curl-energy classification produced", "CONSTRAINED_BY_IDENTITY",
                "structure derived, coefficient missing")


def case_8_next_tests():
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_vector_transverse_current_projection.py")
    print("   Split current into transverse and longitudinal parts.")
    print()
    print("2. candidate_kappa_source_law_from_trace_exchange.py")
    print("   Work the missing kappa trace/interior source.")
    print()
    print("3. candidate_tensor_source_from_exchange_identity.py")
    print("   Work the hand-assigned tensor coupling.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_vector_transverse_current_projection.py")

    status_line("next test selected", "CONSTRAINED_BY_IDENTITY",
                "curl-energy needs transverse current projection")


def final_interpretation():
    header("Final interpretation")

    print("Curl-energy gives a real structural vector equation:")
    print()
    print("  curl curl W = - alpha_W j / (2 K_c)")
    print()
    print("Under div W = 0:")
    print()
    print("  Delta W = alpha_W j / (2 K_c)")
    print()
    print("This supports the vector-current sector structurally.")
    print()
    print("But the coefficient remains missing:")
    print()
    print("  alpha_W/(2K_c)")
    print()
    print("Possible next artifact:")
    print("  candidate_vector_curl_energy_field_equation.md")
    print()
    print("Possible next script:")
    print("  candidate_vector_transverse_current_projection.py")


def main():
    header("Candidate Vector Curl-Energy Field Equation")
    case_0_problem_statement()
    case_1_vector_identity()
    case_2_transverse_reduction()
    case_3_variational_structure()
    case_4_pure_gradient_null_mode()
    case_5_current_transversality()
    case_6_coefficient_status()
    case_7_classification()
    case_8_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
