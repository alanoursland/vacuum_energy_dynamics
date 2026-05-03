# Candidate kappa joint minimum energy functional
#
# Purpose
# -------
# The joint minimum spline model found:
#
#   interior quadratic tendency + exterior reciprocal tendency can be blended
#   smoothly with a C2 transition layer.
#
# User expectation:
#
#   the near-boundary gravity prediction may deviate from GR,
#   probably hardest near the surface,
#   likely not directly measured.
#
# This script makes the spline idea more variational.
#
# It defines a toy energy:
#
#   E[f] = integral [
#       W_int(r) (f - f_int)^2
#     + W_ext(r) (f - f_ext)^2
#     + lambda1 (f')^2
#     + lambda2 (f'')^2
#   ] dr
#
# and computes the Euler-Lagrange equation for a functional with f, f', and f''.
#
# It also defines a deviation diagnostic:
#
#   delta_GR_like = f_joint - f_GR_reference
#
# near the boundary.
#
# This is not a final physical derivation or observational claim.
# It is a variational toy model and prediction-discipline check.

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
        "PLAUSIBLE": "WARN",
        "MISSING": "FAIL",
        "RISK": "WARN",
        "REJECTED": "WARN",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


def case_0_problem_statement():
    header("Case 0: Joint minimum energy-functional problem")

    print("Question:")
    print()
    print("  Can the interior/exterior spline be interpreted as the minimizer of")
    print("  a joint vacuum-curvature energy rather than hand smoothing?")
    print()
    print("Motivation:")
    print()
    print("  near-boundary curvature may deviate from naive GR/Newtonian matching")
    print("  if interior quadratic and exterior reciprocal tendencies co-minimize.")
    print()
    print("Discipline:")
    print()
    print("  do not claim observability yet")
    print("  define a deviation diagnostic only")

    status_line("joint minimum energy-functional problem posed",
                "CONSTRAINED_BY_IDENTITY")


def case_1_define_energy_density():
    header("Case 1: Define toy energy density")

    r = sp.symbols("r", positive=True, real=True)
    f = sp.Function("f")(r)

    W_int = sp.Function("W_int")(r)
    W_ext = sp.Function("W_ext")(r)
    f_int = sp.Function("f_int")(r)
    f_ext = sp.Function("f_ext")(r)
    lam1, lam2 = sp.symbols("lambda_1 lambda_2", positive=True, real=True)

    L = (
        W_int*(f - f_int)**2
        + W_ext*(f - f_ext)**2
        + lam1*sp.diff(f, r)**2
        + lam2*sp.diff(f, r, 2)**2
    )

    print("Toy energy density:")
    print()
    print("  L = W_int (f-f_int)^2 + W_ext (f-f_ext)^2")
    print("      + lambda_1 (f')^2 + lambda_2 (f'')^2")
    print()
    print(f"L = {L}")
    print()
    print("Interpretation:")
    print("  W_int anchors to interior tendency")
    print("  W_ext anchors to exterior tendency")
    print("  lambda_1 penalizes slope strain")
    print("  lambda_2 penalizes curvature jumps / sharp bending")

    status_line("toy energy density defined",
                "PLAUSIBLE",
                "weights not derived")

    return r, f, W_int, W_ext, f_int, f_ext, lam1, lam2, L


def case_2_euler_lagrange_fourth_order(r, f, L):
    header("Case 2: Euler-Lagrange equation with second-derivative term")

    dL_df = sp.diff(L, f)
    dL_dfp = sp.diff(L, sp.diff(f, r))
    dL_dfpp = sp.diff(L, sp.diff(f, r, 2))

    EL = sp.simplify(dL_df - sp.diff(dL_dfp, r) + sp.diff(dL_dfpp, r, 2))

    print("Euler-Lagrange equation for L depending on f, f_prime, f_double_prime:")
    print()
    print("  dL/df - d/dr(dL/df_prime) + d^2/dr^2(dL/df_double_prime) = 0")
    print()
    print("Computed structure:")
    print()
    print(EL)
    print()
    print("The lambda_2 term makes the toy minimizer fourth-order.")
    print("That is expected for curvature-smoothing energy.")
    print()
    print("Boundary conditions must therefore be handled carefully.")

    status_line("Euler-Lagrange equation computed",
                "DERIVED_REDUCED",
                "toy variational structure only")


def case_3_simplified_constant_weights():
    header("Case 3: Simplified constant-weight equation")

    r = sp.symbols("r", positive=True, real=True)
    f = sp.Function("f")(r)

    Wi, We, lam1, lam2 = sp.symbols("W_i W_e lambda_1 lambda_2", positive=True, real=True)
    f_int = sp.Function("f_int")(r)
    f_ext = sp.Function("f_ext")(r)

    eq = sp.Eq(
        Wi*(f - f_int) + We*(f - f_ext) - lam1*sp.diff(f, r, 2) + lam2*sp.diff(f, r, 4),
        0,
    )

    print("For constant weights, the schematic equation is:")
    print()
    print(eq)
    print()
    print("Equivalent:")
    print()
    print("  lambda_2 fourth_derivative(f) - lambda_1 second_derivative(f)")
    print("  + (W_i+W_e) f = W_i f_int + W_e f_ext")
    print()
    print("This shows the minimizer is pulled toward both tendencies while")
    print("smoothness terms distribute the mismatch.")

    status_line("constant-weight minimizer equation stated",
                "DERIVED_REDUCED",
                "still toy model")


def case_4_tendencies_and_transition():
    header("Case 4: Interior/exterior tendencies")

    r, R, M, a0, a2 = sp.symbols("r R M a0 a2", positive=True, real=True)

    f_int = a0 + a2*r**2
    f_ext = 1 - M/r

    print("Interior tendency:")
    print()
    print(f"f_int = {f_int}")
    print()
    print("Exterior tendency:")
    print()
    print(f"f_ext = {f_ext}")
    print()
    print("In the energy model, these are not manually spliced.")
    print("They are competing attractors/minima with radial weights.")

    status_line("interior/exterior attractors stated",
                "PLAUSIBLE",
                "physical identification still open")

    return r, R, M, a0, a2, f_int, f_ext


def case_5_weight_functions():
    header("Case 5: Weight functions")

    print("A smooth model needs radial weights such as:")
    print()
    print("  W_int(r): large inside, fades near/outside surface")
    print("  W_ext(r): small inside, dominates outside")
    print()
    print("A possible smooth transition variable:")
    print()
    print("  x = (r - R)/sigma")
    print()
    print("A possible logistic weight:")
    print()
    print("  W_ext = 1/(1 + exp(-x))")
    print("  W_int = 1 - W_ext")
    print()
    print("This avoids a hard seam but introduces sigma.")
    print()
    print("sigma would control the near-boundary deviation width.")

    status_line("smooth radial weights proposed",
                "PLAUSIBLE",
                "sigma/weights not derived")


def case_6_deviation_diagnostic():
    header("Case 6: Deviation diagnostic")

    r = sp.symbols("r", positive=True, real=True)
    f_joint = sp.Function("f_joint")(r)
    f_ref = sp.Function("f_GR_ref")(r)

    delta = sp.simplify(f_joint - f_ref)

    print("Define a near-boundary deviation diagnostic:")
    print()
    print("  delta_GR_like(r) = f_joint(r) - f_GR_ref(r)")
    print()
    print(f"delta = {delta}")
    print()
    print("Possible derived diagnostics later:")
    print()
    print("  delta_f")
    print("  delta_f_prime")
    print("  delta_f_double_prime")
    print("  deviation in local acceleration")
    print("  deviation in redshift / time dilation")
    print()
    print("Current status:")
    print("  diagnostic named, not predicted.")

    status_line("near-boundary deviation diagnostic defined",
                "CONSTRAINED_BY_IDENTITY",
                "no magnitude prediction yet")


def case_7_measurement_caution():
    header("Case 7: Measurement caution")

    print("A near-boundary deviation is plausible in the toy model, but not yet")
    print("an observational prediction.")
    print()
    print("Reasons:")
    print()
    print("  no derived energy weights")
    print("  no derived transition width")
    print("  no selected observable")
    print("  no magnitude estimate")
    print("  interior curvature is hard to measure directly")
    print("  exterior far field must remain GR-like/1/r")
    print()
    print("Likely location of largest deviation:")
    print()
    print("  near the material surface / interface")
    print()
    print("Likely status:")
    print()
    print("  theoretical effect first, possible niche experimental target later")

    status_line("measurement caution stated",
                "CONSTRAINED_BY_IDENTITY",
                "do not overclaim")


def case_8_gr_deviation_hierarchy():
    header("Case 8: GR-deviation hierarchy")

    print("| Region | Expected deviation status |")
    print("|---|---|")
    print("| deep interior | possible, model-dependent |")
    print("| near boundary/interface | most likely largest deviation |")
    print("| exterior near surface | possible small smoothing correction |")
    print("| far exterior | should recover 1/r / GR-like behavior |")
    print("| radiation sector | no breathing wave from kappa |")
    print()
    print("This hierarchy keeps the model from claiming broad GR violation.")

    status_line("GR-deviation hierarchy stated",
                "PLAUSIBLE",
                "requires quantitative model")


def case_9_failure_controls():
    header("Case 9: Failure controls")

    print("The variational joint-minimum model fails if:")
    print()
    print("1. weights are arbitrary curve-fitting.")
    print("2. far exterior 1/r behavior is spoiled.")
    print("3. transition width sigma is unconstrained.")
    print("4. predicted deviations conflict with existing tests.")
    print("5. kappa and A variables are mixed without a recombination rule.")
    print("6. fourth-order smoothing introduces unphysical boundary modes.")
    print("7. near-boundary deviation is claimed without observable definition.")

    status_line("energy-functional failure controls stated",
                "RISK",
                "quantitative discipline required")


def case_10_classification():
    header("Case 10: Classification")

    print("| Item | Status |")
    print("|---|---|")
    print("| energy density template | PLAUSIBLE |")
    print("| Euler-Lagrange structure | DERIVED_REDUCED |")
    print("| fourth-order smoothing equation | DERIVED_REDUCED toy result |")
    print("| radial weights | PLAUSIBLE / not derived |")
    print("| transition width sigma | MISSING |")
    print("| near-boundary deviation diagnostic | CONSTRAINED_BY_IDENTITY |")
    print("| observability | UNKNOWN |")
    print("| final prediction | UNFINISHED |")

    status_line("joint minimum energy-functional classification produced",
                "CONSTRAINED_BY_IDENTITY",
                "variational toy model, not prediction")


def case_11_next_tests():
    header("Case 11: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_kappa_near_boundary_deviation_diagnostic.py")
    print("   Define concrete acceleration/redshift/deviation diagnostics.")
    print()
    print("2. candidate_kappa_trace_response_status_summary.md")
    print("   Summarize group 10 current state.")
    print()
    print("3. candidate_kappa_joint_minimum_numerical_toy.py")
    print("   Solve a simple weighted variational problem numerically.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_kappa_near_boundary_deviation_diagnostic.py")
    print()
    print("Reason:")
    print("  If deviation from GR is possible, define what would deviate before")
    print("  claiming magnitude or measurability.")

    status_line("next test selected",
                "CONSTRAINED_BY_IDENTITY",
                "diagnostic before prediction")


def final_interpretation():
    header("Final interpretation")

    print("A variational joint-minimum model can make the spline idea less ad hoc.")
    print()
    print("It suggests the largest deviation from naive GR/Newtonian interior matching")
    print("would occur near the material boundary.")
    print()
    print("But no measurement claim is justified yet.")
    print()
    print("Needed next:")
    print("  define concrete deviation diagnostics")
    print("  then estimate magnitude only after weights/scale are specified")
    print()
    print("Possible next artifact:")
    print("  candidate_kappa_joint_minimum_energy_functional.md")
    print()
    print("Possible next script:")
    print("  candidate_kappa_near_boundary_deviation_diagnostic.py")


def main():
    header("Candidate Kappa Joint Minimum Energy Functional")
    case_0_problem_statement()
    r, f, W_int, W_ext, f_int, f_ext, lam1, lam2, L = case_1_define_energy_density()
    case_2_euler_lagrange_fourth_order(r, f, L)
    case_3_simplified_constant_weights()
    case_4_tendencies_and_transition()
    case_5_weight_functions()
    case_6_deviation_diagnostic()
    case_7_measurement_caution()
    case_8_gr_deviation_hierarchy()
    case_9_failure_controls()
    case_10_classification()
    case_11_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
