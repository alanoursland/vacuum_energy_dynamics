# Candidate vector transverse current projection
#
# Purpose
# -------
# The vector curl-energy field equation gave:
#
#   curl curl W = - alpha_W j / (2 K_c)
#
# and under div W = 0:
#
#   Delta W = alpha_W j / (2 K_c)
#
# But curl-energy naturally describes transverse vector content.
#
# This script asks how current should split into:
#
#   j = j_T + j_L
#
# where:
#
#   div j_T = 0
#   curl j_L = 0
#
# Hypothesis:
#
#   j_T sources W_i.
#   j_L is handled by scalar constraint / continuity structure.
#
# This is structural. It does not set the vector coefficient.
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/09_vacuum_identity_and_source_coupling/
#   or:
#   scripts_v3/candidate_vector_transverse_current_projection.py

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


def grad(f, coords):
    return sp.Matrix([sp.diff(f, q) for q in coords])


def case_0_problem_statement():
    header("Case 0: Transverse current projection problem")

    print("Curl-energy vector sector naturally couples to transverse vector content.")
    print()
    print("Need current split:")
    print()
    print("  j = j_T + j_L")
    print("  div j_T = 0")
    print("  curl j_L = 0")
    print()
    print("Hypothesis:")
    print()
    print("  j_T sources W_i")
    print("  j_L belongs to scalar continuity/constraint handling")

    status_line("transverse current projection problem posed", "CONSTRAINED_BY_IDENTITY")


def case_1_helmholtz_split_statement():
    header("Case 1: Helmholtz-style split statement")

    print("For suitable boundary conditions, a vector current can be decomposed as:")
    print()
    print("  j = j_T + grad chi")
    print()
    print("where:")
    print()
    print("  div j_T = 0")
    print("  curl grad chi = 0")
    print()
    print("This is the natural split for vector curl-energy.")

    status_line("current split stated", "CONSTRAINED_BY_IDENTITY",
                "requires boundary conditions")


def case_2_gradient_current_is_longitudinal():
    header("Case 2: Gradient current is longitudinal")

    x, y, z = sp.symbols("x y z", real=True)
    coords = (x, y, z)
    chi = sp.Function("chi")(x, y, z)

    j_L = grad(chi, coords)
    curl_jL = sp.simplify(curl(j_L, coords))

    print("Longitudinal current:")
    print("  j_L = grad chi")
    print()
    print("curl j_L =")
    print(curl_jL)

    ok = all(is_zero(e) for e in curl_jL)
    status_line("gradient current has zero curl", "DERIVED_REDUCED" if ok else "RISK")


def case_3_rotational_current_is_transverse():
    header("Case 3: Rotational current is transverse")

    x, y, z, J0 = sp.symbols("x y z J0", real=True)
    coords = (x, y, z)

    j_T = sp.Matrix([-J0*y, J0*x, 0])
    div_jT = div(j_T, coords)
    curl_jT = sp.simplify(curl(j_T, coords))

    print("Rotational current:")
    print(j_T)
    print()
    print(f"div j_T = {div_jT}")
    print("curl j_T =")
    print(curl_jT)

    status_line("rotational current is divergence-free", "DERIVED_REDUCED" if is_zero(div_jT) else "RISK")


def case_4_continuity_allocation():
    header("Case 4: Continuity allocation")

    print("Mass continuity:")
    print()
    print("  partial_t rho + div j = 0")
    print()
    print("If j = j_T + j_L and div j_T = 0, then:")
    print()
    print("  partial_t rho + div j_L = 0")
    print()
    print("Interpretation:")
    print()
    print("  j_T carries circulation/rotation and sources W_i.")
    print("  j_L carries compression/accumulation and belongs with scalar constraint.")
    print()
    print("This prevents the vector sector from swallowing scalar continuity.")

    status_line("continuity allocates longitudinal current to scalar sector", "CONSTRAINED_BY_IDENTITY",
                "formal projection/boundary conditions still needed")


def case_5_vector_field_equation_with_projection():
    header("Case 5: Projected vector field equation")

    alpha_W, K_c = sp.symbols("alpha_W K_c", positive=True, real=True)

    print("Curl-energy vector equation:")
    print()
    print("  curl curl W = - alpha_W j / (2 K_c)")
    print()
    print("Projected source policy:")
    print()
    print("  curl curl W = - alpha_W j_T / (2 K_c)")
    print()
    print("Under div W = 0:")
    print()
    print("  Delta W = alpha_W j_T / (2 K_c)")
    print()
    print("Coefficient still missing:")
    print()
    print(f"  alpha_W/(2 K_c) = {alpha_W/(2*K_c)}")

    status_line("projected vector equation stated", "CONSTRAINED_BY_IDENTITY",
                "coefficient and projection operator missing")


def case_6_projection_safety_table():
    header("Case 6: Projection safety table")

    print("| Current piece | Property | Sector assignment | Status |")
    print("|---|---|---|---|")
    print("| j_T | div j_T = 0 | W_i vector/curl sector | CONSTRAINED_BY_IDENTITY |")
    print("| j_L | curl j_L = 0 | scalar continuity / A_constraint | CONSTRAINED_BY_IDENTITY |")
    print("| full j | continuity source | split required | PARTIAL |")
    print("| time-dependent split | needs projection operator | MISSING |")
    print("| coefficient alpha_W/(2K_c) | normalization | MISSING |")

    status_line("projection safety table produced", "CONSTRAINED_BY_IDENTITY",
                "projection structure helps sector allocation")


def case_7_failure_controls():
    header("Case 7: Failure controls")

    print("This projection fails if:")
    print()
    print("1. j_L is allowed to source W_i directly.")
    print("2. j_T is disconnected from angular momentum/current circulation.")
    print("3. projection depends on arbitrary gauge choices without boundary rules.")
    print("4. coefficient is inserted from GR matching.")
    print("5. time-dependent longitudinal pieces violate scalar constraint propagation.")
    print()
    status_line("projection failure controls stated", "RISK",
                "requires boundary/gauge discipline")


def case_8_next_tests():
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_vector_current_projection_operator.py")
    print("   Write the formal transverse projector and test simple examples.")
    print()
    print("2. candidate_kappa_source_law_from_trace_exchange.py")
    print("   Work the missing kappa source sector.")
    print()
    print("3. candidate_tensor_source_from_exchange_identity.py")
    print("   Work the hand-assigned tensor coupling.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_vector_current_projection_operator.py")

    status_line("next test selected", "CONSTRAINED_BY_IDENTITY",
                "formal projector is the next vector cleanup")


def final_interpretation():
    header("Final interpretation")

    print("The current should not feed the vector sector raw.")
    print()
    print("The natural policy is:")
    print()
    print("  j_T -> W_i vector/curl sector")
    print("  j_L -> scalar continuity/constraint sector")
    print()
    print("Projected vector equation:")
    print()
    print("  curl curl W = - alpha_W j_T / (2K_c)")
    print()
    print("Under div W = 0:")
    print()
    print("  Delta W = alpha_W j_T / (2K_c)")
    print()
    print("Possible next artifact:")
    print("  candidate_vector_transverse_current_projection.md")
    print()
    print("Possible next script:")
    print("  candidate_vector_current_projection_operator.py")


def main():
    header("Candidate Vector Transverse Current Projection")
    case_0_problem_statement()
    case_1_helmholtz_split_statement()
    case_2_gradient_current_is_longitudinal()
    case_3_rotational_current_is_transverse()
    case_4_continuity_allocation()
    case_5_vector_field_equation_with_projection()
    case_6_projection_safety_table()
    case_7_failure_controls()
    case_8_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
