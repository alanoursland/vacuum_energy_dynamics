# Candidate vector boundary coefficient from action
#
# Purpose
# -------
# The vector boundary-value problem gave the exterior shape:
#
#   W_phi = C_J J sin(theta)/r^2
#
# and:
#
#   B_W = curl W ~ C_W J/r^3
#
# but left the boundary coefficient C_b / C_J / C_W missing.
#
# This script asks whether the coefficient can be related to the curl-energy
# source equation:
#
#   curl curl W = - alpha_W j_T/(2K_c)
#
# or, in a magnetostatic-like Green-function form:
#
#   W(x) ~ lambda_W integral j_T(x') / |x-x'| d^3x'
#
# with:
#
#   lambda_W = alpha_W/(8*pi*K_c)   up to convention
#
# The goal is not to set the GR coefficient.
# The goal is to show that the boundary/far-field coefficient is controlled by
# the same missing ratio alpha_W/K_c, not a new arbitrary number.
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/09_vacuum_identity_and_source_coupling/
#   or:
#   scripts_v3/candidate_vector_boundary_coefficient_from_action.py

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
    header("Case 0: Vector boundary coefficient from action problem")

    print("Question:")
    print()
    print("  Can the exterior/boundary coefficient be tied to the curl-energy")
    print("  source ratio alpha_W/(2K_c)?")
    print()
    print("Rules:")
    print()
    print("  keep all coefficients symbolic")
    print("  do not insert Lense-Thirring normalization")
    print("  check whether C_b is a new free coefficient or controlled by alpha_W/K_c")

    status_line("boundary coefficient problem posed", "CONSTRAINED_BY_IDENTITY")


def case_1_field_equation_ratio():
    header("Case 1: Curl-energy source ratio")

    alpha_W, K_c = sp.symbols("alpha_W K_c", positive=True, real=True)

    ratio = alpha_W/(2*K_c)

    print("Curl-energy equation:")
    print()
    print("  curl curl W = - alpha_W j_T/(2K_c)")
    print()
    print("Coefficient ratio:")
    print()
    print(f"lambda_eq = {ratio}")
    print()
    print("This ratio is still missing, but it should control the exterior amplitude.")

    status_line("field-equation coefficient ratio identified", "MISSING",
                "alpha_W/(2K_c) not derived")


def case_2_green_function_amplitude():
    header("Case 2: Green-function amplitude")

    alpha_W, K_c = sp.symbols("alpha_W K_c", positive=True, real=True)

    # If Delta W = lambda_eq j, the Poisson Green function gives 1/(4pi).
    lambda_eq = alpha_W/(2*K_c)
    lambda_green = lambda_eq/(4*sp.pi)

    print("Under transverse gauge:")
    print()
    print("  Delta W = alpha_W j_T/(2K_c)")
    print()
    print("Poisson Green-function amplitude conventionally introduces 1/(4*pi):")
    print()
    print("  W ~ [alpha_W/(8*pi K_c)] integral j_T/|x-x'| d^3x'")
    print()
    print(f"lambda_green = {lambda_green}")
    print()
    print("This is not a GR coefficient.")
    print("It only relates exterior amplitude to the missing action ratio.")

    status_line("Green-function amplitude tied to alpha_W/K_c", "CONSTRAINED_BY_IDENTITY",
                "absolute ratio still missing")


def case_3_far_field_multipole_relation():
    header("Case 3: Far-field relation to angular momentum")

    alpha_W, K_c, J = sp.symbols("alpha_W K_c J", positive=True, real=True)

    lambda_green = alpha_W/(8*sp.pi*K_c)

    C_shape = sp.symbols("C_shape", positive=True, real=True)
    C_J = sp.simplify(C_shape * lambda_green)

    print("For a compact rotating source, the far-field vector amplitude should be:")
    print()
    print("  C_J J")
    print()
    print("where:")
    print()
    print("  C_J = C_shape * alpha_W/(8*pi K_c)")
    print()
    print(f"C_J = {C_J}")
    print()
    print("C_shape depends on angular conventions and source model.")
    print("alpha_W/K_c remains the physical missing ratio.")

    status_line("far-field coefficient tied to action ratio times shape factor",
                "CONSTRAINED_BY_IDENTITY",
                "shape factor and action ratio not fully derived")


def case_4_boundary_coefficient_relation():
    header("Case 4: Boundary coefficient relation")

    C_b, C_shape, alpha_W, K_c = sp.symbols("C_b C_shape alpha_W K_c", positive=True, real=True)

    Cb_expr = C_shape * alpha_W/(8*sp.pi*K_c)

    print("Boundary coefficient can be parameterized as:")
    print()
    print("  C_b = C_shape * alpha_W/(8*pi K_c)")
    print()
    print(f"C_b = {Cb_expr}")
    print()
    print("This means C_b should not be an independent new knob if the action")
    print("and source model are specified.")
    print()
    print("But C_shape and alpha_W/K_c are still missing.")

    status_line("boundary coefficient reduced to action ratio plus shape factor",
                "CONSTRAINED_BY_IDENTITY",
                "not a final normalization")


def case_5_precession_coefficient_separation():
    header("Case 5: Precession coefficient separation")

    beta_W, C_shape, alpha_W, K_c = sp.symbols("beta_W C_shape alpha_W K_c", positive=True, real=True)

    C_total = sp.simplify(beta_W * C_shape * alpha_W/(8*sp.pi*K_c))

    print("Observable precession coefficient separates into:")
    print()
    print("  C_total = beta_W * C_shape * alpha_W/(8*pi K_c)")
    print()
    print(f"C_total = {C_total}")
    print()
    print("Meaning:")
    print("  vector field normalization and precession coupling are separate.")
    print()
    print("Missing:")
    print("  beta_W")
    print("  C_shape")
    print("  alpha_W/K_c")

    status_line("precession coefficient separated into missing factors", "MISSING",
                "observable normalization not derived")


def case_6_no_new_free_boundary_knob():
    header("Case 6: No new free boundary knob")

    print("Important result:")
    print()
    print("  C_b should not be treated as an independent free coefficient once")
    print("  the vector action, source coupling, and boundary/source model are fixed.")
    print()
    print("Instead:")
    print()
    print("  C_b is controlled by alpha_W/K_c and geometry/source shape factors.")
    print()
    print("Remaining danger:")
    print()
    print("  if alpha_W/K_c, beta_W, and C_shape are all independently fitted,")
    print("  the vector sector becomes a fit machine.")

    status_line("boundary knob reduced but not eliminated", "CONSTRAINED_BY_IDENTITY",
                "main action ratio remains missing")


def case_7_classification():
    header("Case 7: Classification")

    print("| Item | Status |")
    print("|---|---|")
    print("| curl-energy equation ratio alpha_W/(2K_c) | MISSING |")
    print("| Green-function amplitude alpha_W/(8pi K_c) | CONSTRAINED_BY_IDENTITY |")
    print("| boundary coefficient C_b from action ratio | CONSTRAINED_BY_IDENTITY |")
    print("| source/shape factor C_shape | MISSING |")
    print("| precession coupling beta_W | MISSING |")
    print("| Lense-Thirring normalization | HAND_ASSIGNED if inserted now |")
    print()
    status_line("boundary coefficient classification produced", "CONSTRAINED_BY_IDENTITY",
                "C_b tied to missing action ratio, not solved")


def case_8_next_tests():
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_vector_source_shape_factor.py")
    print("   Compute source/shape factor for a simple rotating sphere symbolically.")
    print()
    print("2. candidate_kappa_source_law_from_trace_exchange.py")
    print("   Work missing kappa source law.")
    print()
    print("3. candidate_tensor_source_from_exchange_identity.py")
    print("   Work hand-assigned tensor coupling.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_vector_source_shape_factor.py")

    status_line("next test selected", "CONSTRAINED_BY_IDENTITY",
                "source shape factor is next local vector cleanup")


def final_interpretation():
    header("Final interpretation")

    print("The boundary coefficient is not a totally new free knob.")
    print()
    print("It can be related structurally to:")
    print()
    print("  alpha_W/K_c")
    print("  source geometry / shape factor")
    print()
    print("But the actual normalization is still missing because:")
    print()
    print("  alpha_W/K_c is missing")
    print("  C_shape is missing")
    print("  beta_W is missing")
    print()
    print("Possible next artifact:")
    print("  candidate_vector_boundary_coefficient_from_action.md")
    print()
    print("Possible next script:")
    print("  candidate_vector_source_shape_factor.py")


def main():
    header("Candidate Vector Boundary Coefficient From Action")
    case_0_problem_statement()
    case_1_field_equation_ratio()
    case_2_green_function_amplitude()
    case_3_far_field_multipole_relation()
    case_4_boundary_coefficient_relation()
    case_5_precession_coefficient_separation()
    case_6_no_new_free_boundary_knob()
    case_7_classification()
    case_8_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
