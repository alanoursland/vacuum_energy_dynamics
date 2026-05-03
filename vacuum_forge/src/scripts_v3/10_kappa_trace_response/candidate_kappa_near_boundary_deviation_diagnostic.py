# Candidate kappa near-boundary deviation diagnostic
#
# Purpose
# -------
# The joint-minimum energy functional found:
#
#   a variational toy model can represent competition between
#   interior quadratic tendency, exterior reciprocal tendency,
#   and smoothness penalties.
#
# It suggests:
#
#   the largest deviation from naive GR/Newtonian interior matching may occur
#   near the material boundary.
#
# But:
#
#   no measurement claim is justified yet.
#
# This script defines concrete symbolic diagnostics for a possible near-boundary
# deviation before estimating any magnitude.
#
# Candidate diagnostics:
#
#   delta_f        = f_joint - f_ref
#   delta_g        = -d(delta_f)/dr
#   delta_curv     = d2(delta_f)/dr2
#   delta_redshift = approximate lapse/redshift deviation
#   width scaling  = dependence on transition width sigma
#
# This is a diagnostic inventory, not a prediction.
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/10_kappa_trace_response/
#   or:
#   scripts_v3/candidate_kappa_near_boundary_deviation_diagnostic.py

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
    header("Case 0: Near-boundary deviation diagnostic problem")

    print("Question:")
    print()
    print("  If the joint-minimum model deviates from GR near a material boundary,")
    print("  what exactly would deviate?")
    print()
    print("Discipline:")
    print()
    print("  define diagnostics before estimating magnitude")
    print("  do not claim measurement/observability yet")
    print()
    print("Likely region:")
    print()
    print("  near surface / matter-vacuum interface")

    status_line("near-boundary deviation diagnostic problem posed",
                "CONSTRAINED_BY_IDENTITY")


def case_1_define_reference_and_joint_profiles():
    header("Case 1: Reference and joint profiles")

    r = sp.symbols("r", positive=True, real=True)

    f_ref = sp.Function("f_GR_ref")(r)
    f_joint = sp.Function("f_joint")(r)

    delta_f = sp.simplify(f_joint - f_ref)

    print("Reference profile:")
    print()
    print("  f_GR_ref(r)")
    print()
    print("Joint-minimum profile:")
    print()
    print("  f_joint(r)")
    print()
    print("Profile deviation:")
    print()
    print("  delta_f = f_joint - f_GR_ref")
    print()
    print(f"delta_f = {delta_f}")

    status_line("profile deviation diagnostic defined",
                "CONSTRAINED_BY_IDENTITY",
                "reference profile must be specified")

    return r, f_ref, f_joint, delta_f


def case_2_acceleration_diagnostic(r, delta_f):
    header("Case 2: Acceleration diagnostic")

    delta_g = sp.simplify(-sp.diff(delta_f, r))

    print("If f behaves like a potential/lapse-like scalar, local radial")
    print("acceleration deviation is proportional to:")
    print()
    print("  delta_g = -d(delta_f)/dr")
    print()
    print(f"delta_g = {delta_g}")
    print()
    print("This would likely peak where the transition layer bends fastest.")

    status_line("acceleration deviation diagnostic defined",
                "CONSTRAINED_BY_IDENTITY",
                "normalization/recombination missing")

    return delta_g


def case_3_curvature_diagnostic(r, delta_f):
    header("Case 3: Curvature diagnostic")

    delta_curv = sp.simplify(sp.diff(delta_f, r, 2))
    delta_lap = sp.simplify(sp.diff(delta_f, r, 2) + 2*sp.diff(delta_f, r)/r)

    print("Second-derivative curvature-like deviation:")
    print()
    print("  delta_curv = d2(delta_f)/dr2")
    print()
    print(f"delta_curv = {delta_curv}")
    print()
    print("Areal Laplacian-like deviation:")
    print()
    print("  delta_lap = delta_f'' + 2 delta_f'/r")
    print()
    print(f"delta_lap = {delta_lap}")

    status_line("curvature deviation diagnostics defined",
                "CONSTRAINED_BY_IDENTITY",
                "metric mapping still needed")

    return delta_curv, delta_lap


def case_4_redshift_lapse_diagnostic():
    header("Case 4: Redshift/lapse diagnostic")

    A_ref, delta_A = sp.symbols("A_ref delta_A", positive=True, real=True)

    # For small delta_A, sqrt(A_ref+delta_A)/sqrt(A_ref) - 1
    exact = sp.sqrt(A_ref + delta_A)/sp.sqrt(A_ref) - 1
    linear = sp.simplify(delta_A/(2*A_ref))

    print("If the deviation enters a lapse-like factor A:")
    print()
    print("  A_joint = A_ref + delta_A")
    print()
    print("Fractional clock/redshift deviation:")
    print()
    print("  sqrt(A_joint/A_ref) - 1")
    print()
    print(f"exact = {exact}")
    print()
    print("Linearized for small delta_A:")
    print()
    print(f"approx = {linear}")

    status_line("redshift/lapse diagnostic defined",
                "CONSTRAINED_BY_IDENTITY",
                "requires recombination map")


def case_5_transition_width_scaling():
    header("Case 5: Transition width scaling")

    sigma, eps = sp.symbols("sigma epsilon", positive=True, real=True)

    print("Let epsilon be a characteristic profile deviation amplitude and sigma")
    print("the transition width.")
    print()
    print("Scaling estimates:")
    print()
    print("  delta_f ~ epsilon")
    print("  delta_g ~ epsilon / sigma")
    print("  delta_curv ~ epsilon / sigma^2")
    print()
    print("Thus curvature-like deviations are most sensitive to narrow transition")
    print("layers.")
    print()
    print("But sigma is not derived, so this is only scaling discipline.")

    status_line("transition-width scaling stated",
                "PLAUSIBLE",
                "epsilon and sigma not derived")


def case_6_regions_hierarchy():
    header("Case 6: Region hierarchy")

    print("| Region | Diagnostic expectation |")
    print("|---|---|")
    print("| deep interior | delta may be small if quadratic tendency dominates |")
    print("| inner transition side | delta_g and delta_curv may grow |")
    print("| material boundary | likely largest curvature-like diagnostic |")
    print("| near exterior | possible small relaxation back to 1/r |")
    print("| far exterior | delta should decay / vanish |")
    print()
    print("This keeps the expected deviation localized.")

    status_line("near-boundary region hierarchy stated",
                "PLAUSIBLE",
                "magnitude unknown")


def case_7_possible_observable_channels():
    header("Case 7: Possible observable channels")

    print("Candidate observable channels:")
    print()
    print("1. local acceleration near a dense body's surface")
    print("2. clock/redshift gradient near a surface")
    print("3. pressure/interior-equilibrium inference in compact objects")
    print("4. thin-shell laboratory density-interface tests")
    print("5. astrophysical surface matching effects")
    print()
    print("Caution:")
    print("  no channel is claimed viable yet.")
    print("  these are diagnostic buckets only.")

    status_line("observable channel inventory stated",
                "PLAUSIBLE",
                "no viability assessment")


def case_8_measurement_caution():
    header("Case 8: Measurement caution")

    print("Why this may be unmeasured or hard to measure:")
    print()
    print("  interior curvature is not directly accessible in ordinary bodies")
    print("  near-surface Newtonian backgrounds dominate")
    print("  material systematics may swamp tiny deviations")
    print("  exterior far field must agree with GR")
    print("  compact-object interiors are model-dependent")
    print()
    print("Therefore:")
    print()
    print("  possible deviation != practical test yet")

    status_line("measurement caution retained",
                "CONSTRAINED_BY_IDENTITY",
                "avoid overclaim")


def case_9_failure_controls():
    header("Case 9: Failure controls")

    print("Deviation diagnostic program fails if:")
    print()
    print("1. f_joint and f_ref are not mapped to observables.")
    print("2. delta is nonzero only by arbitrary spline choice.")
    print("3. far exterior delta does not vanish.")
    print("4. predicted acceleration/redshift deviation is already excluded.")
    print("5. kappa-sector deviation is confused with A-sector mass flux.")
    print("6. magnitude is claimed before sigma/weights are derived.")

    status_line("deviation diagnostic failure controls stated",
                "RISK",
                "diagnostic before prediction")


def case_10_classification():
    header("Case 10: Classification")

    print("| Diagnostic | Status |")
    print("|---|---|")
    print("| profile deviation delta_f | CONSTRAINED_BY_IDENTITY |")
    print("| acceleration deviation delta_g | CONSTRAINED_BY_IDENTITY |")
    print("| curvature deviation delta_curv | CONSTRAINED_BY_IDENTITY |")
    print("| redshift/lapse deviation | CONSTRAINED_BY_IDENTITY |")
    print("| transition width scaling | PLAUSIBLE |")
    print("| observable channels | PLAUSIBLE inventory only |")
    print("| magnitude prediction | MISSING |")
    print("| measurement claim | NOT MADE |")

    status_line("near-boundary diagnostic classification produced",
                "CONSTRAINED_BY_IDENTITY",
                "no prediction yet")


def case_11_next_tests():
    header("Case 11: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_kappa_joint_minimum_numerical_toy.py")
    print("   Solve a simple weighted variational problem numerically.")
    print()
    print("2. candidate_kappa_trace_response_status_summary.md")
    print("   Summarize group 10.")
    print()
    print("3. candidate_kappa_deviation_observability_scan.py")
    print("   Later: rough observability categories.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_kappa_trace_response_status_summary.md")
    print()
    print("Reason:")
    print("  Group 10 has reached a natural boundary: kappa status is now clear enough")
    print("  to summarize before pushing numerical/observational speculation.")

    status_line("next test selected",
                "CONSTRAINED_BY_IDENTITY",
                "summary is recommended")


def final_interpretation():
    header("Final interpretation")

    print("Near-boundary deviation should be discussed only through diagnostics:")
    print()
    print("  delta_f")
    print("  delta_g")
    print("  delta_curv")
    print("  delta_redshift")
    print()
    print("No magnitude claim is justified until:")
    print()
    print("  weights are derived")
    print("  transition width is derived")
    print("  recombination map is fixed")
    print("  observable is selected")
    print()
    print("Possible next artifact:")
    print("  candidate_kappa_near_boundary_deviation_diagnostic.md")
    print()
    print("Recommended next:")
    print("  candidate_kappa_trace_response_status_summary.md")


def main():
    header("Candidate Kappa Near-Boundary Deviation Diagnostic")
    r, f_ref, f_joint, delta_f = case_1_define_reference_and_joint_profiles()
    case_0_problem_statement()
    delta_g = case_2_acceleration_diagnostic(r, delta_f)
    case_3_curvature_diagnostic(r, delta_f)
    case_4_redshift_lapse_diagnostic()
    case_5_transition_width_scaling()
    case_6_regions_hierarchy()
    case_7_possible_observable_channels()
    case_8_measurement_caution()
    case_9_failure_controls()
    case_10_classification()
    case_11_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
