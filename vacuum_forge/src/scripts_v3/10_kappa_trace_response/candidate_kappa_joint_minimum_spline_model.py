# Candidate kappa joint minimum spline model
#
# Purpose
# -------
# The boundary-layer source compatibility study found:
#
#   raw pressure trace is not compatible with the smooth C2 compact profile
#   as an elliptic Poisson source.
#
#   the non-inertial minimum-shift picture is preferred:
#     matter trace shifts a local vacuum-curvature minimum,
#     kappa relaxes toward that minimum,
#     no propagating breathing mode is produced.
#
# User refinement:
#
#   The interior curvature may not be exactly the Newtonian quadratic profile.
#   The mass creates a quadratic interior tendency, but the exterior 1/r minimum
#   configuration modifies the boundary region to be smooth.
#
# This script builds a toy joint-minimum spline model:
#
#   interior tendency: regular quadratic-like profile,
#   exterior tendency: reciprocal 1/r-like profile,
#   transition layer: smooth spline enforcing value/slope/curvature matching.
#
# Goal:
#
#   show that the actual minimum can deviate from naive interior parabola near
#   the surface while preserving smooth connection to exterior reciprocal falloff.
#
# This is not a final physical derivation.
# It is a basis/modeling test.
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/10_kappa_trace_response/
#   or:
#   scripts_v3/candidate_kappa_joint_minimum_spline_model.py

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
    header("Case 0: Joint minimum spline problem")

    print("Question:")
    print()
    print("  Can interior quadratic tendency and exterior reciprocal tendency be")
    print("  represented as one smooth vacuum-curvature minimum curve?")
    print()
    print("Idea:")
    print()
    print("  interior is regular and approximately quadratic")
    print("  exterior tends toward 1/r")
    print("  boundary region adjusts so the total configuration is smooth")
    print()
    print("Goal:")
    print()
    print("  allow interior deviation from naive parabola near the surface")
    print("  preserve exterior smoothness")
    print("  avoid propagating kappa/breathing wave")

    status_line("joint minimum spline problem posed", "CONSTRAINED_BY_IDENTITY")


def case_1_define_interior_and_exterior_tendencies():
    header("Case 1: Interior and exterior tendencies")

    r, R, a0, a2, M = sp.symbols("r R a0 a2 M", positive=True, real=True)

    interior = a0 + a2*r**2
    exterior = 1 - M/r

    print("Interior regular quadratic tendency:")
    print()
    print(f"f_int(r) = {interior}")
    print()
    print("Exterior reciprocal tendency:")
    print()
    print(f"f_ext(r) = {exterior}")
    print()
    print("These are not asserted as final metric functions here.")
    print("They are basis tendencies for a joint minimum model.")

    status_line("quadratic and reciprocal basis tendencies stated",
                "PLAUSIBLE",
                "coefficients/source relation not derived")

    return r, R, a0, a2, M, interior, exterior


def case_2_hermite_transition_layer():
    header("Case 2: Hermite transition layer setup")

    x = sp.symbols("x", real=True)

    # Cubic Hermite basis functions on x in [0,1].
    H00 = 2*x**3 - 3*x**2 + 1
    H10 = x**3 - 2*x**2 + x
    H01 = -2*x**3 + 3*x**2
    H11 = x**3 - x**2

    print("Use a cubic Hermite transition basis on x in [0,1]:")
    print()
    print(f"H00 = {H00}")
    print(f"H10 = {H10}")
    print(f"H01 = {H01}")
    print(f"H11 = {H11}")
    print()
    print("This can match value and first derivative across a transition layer.")
    print("For curvature matching, a quintic smoothstep or higher spline is better.")

    status_line("Hermite transition basis stated",
                "PLAUSIBLE",
                "C1 smooth; C2 requires quintic/higher")


def case_3_quintic_smoothstep():
    header("Case 3: Quintic smoothstep for C2 matching")

    x = sp.symbols("x", real=True)

    s = 6*x**5 - 15*x**4 + 10*x**3
    ds0 = sp.simplify(sp.diff(s, x).subs(x, 0))
    ds1 = sp.simplify(sp.diff(s, x).subs(x, 1))
    d2s0 = sp.simplify(sp.diff(s, x, 2).subs(x, 0))
    d2s1 = sp.simplify(sp.diff(s, x, 2).subs(x, 1))

    print("Quintic smoothstep:")
    print()
    print(f"s(x) = {s}")
    print()
    print("Endpoint derivative checks:")
    print()
    print(f"s'(0) = {ds0}")
    print(f"s'(1) = {ds1}")
    print(f"s''(0) = {d2s0}")
    print(f"s''(1) = {d2s1}")
    print()
    print("This basis can splice tendencies without value/slope/curvature jumps.")

    ok = ds0 == 0 and ds1 == 0 and d2s0 == 0 and d2s1 == 0

    status_line("quintic smoothstep supports C2 transition",
                "DERIVED_REDUCED" if ok else "RISK")


def case_4_blended_joint_minimum():
    header("Case 4: Blended joint minimum model")

    r, R, w, a0, a2, M = sp.symbols("r R w a0 a2 M", positive=True, real=True)

    # Transition coordinate: x=(r-(R-w))/w. In actual use clamp x to [0,1].
    x = (r - (R - w))/w
    s = 6*x**5 - 15*x**4 + 10*x**3

    interior = a0 + a2*r**2
    exterior = 1 - M/r
    blend = sp.simplify((1 - s)*interior + s*exterior)

    print("Transition coordinate:")
    print()
    print("  x = (r - (R-w))/w")
    print()
    print("Smooth blend:")
    print()
    print("  f_joint = (1-s) f_int + s f_ext")
    print()
    print("where:")
    print()
    print(f"f_int = {interior}")
    print(f"f_ext = {exterior}")
    print()
    print("The blended expression is large, so not expanded by default.")
    print()
    print("Interpretation:")
    print("  near inner side, interior tendency dominates")
    print("  near outer side, exterior reciprocal tendency dominates")
    print("  transition region modifies naive interior parabola near surface")

    status_line("joint interior/exterior blend defined",
                "PLAUSIBLE",
                "energy functional not derived")

    return r, R, w, a0, a2, M, x, s, interior, exterior, blend


def case_5_boundary_matching_equations():
    header("Case 5: Boundary matching equations")

    R, a0, a2, M = sp.symbols("R a0 a2 M", positive=True, real=True)
    r = sp.symbols("r", positive=True, real=True)

    interior = a0 + a2*r**2
    exterior = 1 - M/r

    equations = [
        sp.Eq(interior.subs(r, R), exterior.subs(r, R)),
        sp.Eq(sp.diff(interior, r).subs(r, R), sp.diff(exterior, r).subs(r, R)),
    ]

    print("If directly matching at R without a transition layer, C1 matching gives:")
    print()
    for eq in equations:
        print(eq)

    sol = sp.solve(equations, (a0, a2), dict=True)

    print()
    print("Solution for interior coefficients:")
    print(sol)
    print()
    print("This shows exterior 1/r boundary conditions can determine the best")
    print("quadratic interior coefficients if direct matching is imposed.")
    print()
    print("With a transition layer, the interior can remain more Newtonian in the")
    print("bulk while the boundary region absorbs the smoothing.")

    status_line("direct C1 matching equations solved",
                "DERIVED_REDUCED",
                "toy coefficient relation only")


def case_6_curvature_deviation_near_surface():
    header("Case 6: Curvature deviation near surface")

    print("Interpretation of the spline model:")
    print()
    print("  The interior bulk may look approximately quadratic.")
    print("  Near the surface, the exterior reciprocal minimum pulls the curve away")
    print("  from the naive parabola.")
    print("  The transition layer distributes that correction smoothly.")
    print()
    print("This implies:")
    print()
    print("  internal curvature is not exactly the Newtonian parabolic prediction.")
    print("  exterior may also be slightly adjusted near the surface in a full")
    print("  joint-minimum model.")
    print()
    print("But exterior far field should recover the reciprocal 1/r behavior.")

    status_line("near-surface curvature deviation identified",
                "PLAUSIBLE",
                "observable consequences not assessed")


def case_7_energy_functional_placeholder():
    header("Case 7: Energy functional placeholder")

    print("A real joint-minimum model needs an energy functional, for example:")
    print()
    print("  E[f] = integral [")
    print("       W_int(r) (f - f_int)^2")
    print("     + W_ext(r) (f - f_ext)^2")
    print("     + lambda_1 (f')^2")
    print("     + lambda_2 (f'')^2")
    print("    ] dr")
    print()
    print("The minimizer would naturally compromise between interior and exterior")
    print("tendencies while penalizing sharp boundary curvature.")
    print()
    print("This is the more principled version of spline blending.")

    status_line("joint minimum energy functional sketched",
                "PLAUSIBLE",
                "weights and variational derivation missing")


def case_8_kappa_relation():
    header("Case 8: Relation to kappa")

    print("The spline variable may represent:")
    print()
    print("  A-like scalar response")
    print("  kappa_min")
    print("  an effective curvature/volume profile")
    print()
    print("For kappa specifically:")
    print()
    print("  matter trace shifts kappa_min in the interior")
    print("  exterior vacuum requires kappa_min -> 0")
    print("  boundary smoothing gives compact kappa response")
    print()
    print("This supports non-propagating trace relaxation rather than breathing waves.")

    status_line("spline model supports kappa minimum-shift interpretation",
                "CONSTRAINED_BY_IDENTITY",
                "variable identification must be fixed")


def case_9_failure_controls():
    header("Case 9: Failure controls")

    print("Spline/joint-minimum model fails if:")
    print()
    print("1. spline is used only as curve-fitting with no energy principle.")
    print("2. exterior 1/r far field is spoiled.")
    print("3. transition creates hidden shell stress.")
    print("4. interior deviation conflicts with known matching constraints.")
    print("5. kappa and A profiles are mixed inconsistently.")
    print("6. smoothing hides rather than explains scalar confinement.")

    status_line("joint-minimum failure controls stated",
                "RISK",
                "must derive energy/weights")


def case_10_classification():
    header("Case 10: Classification")

    print("| Item | Status |")
    print("|---|---|")
    print("| interior quadratic tendency | PLAUSIBLE basis |")
    print("| exterior reciprocal tendency | PLAUSIBLE / required far field |")
    print("| Hermite C1 splice | PLAUSIBLE |")
    print("| quintic C2 smoothstep | DERIVED_REDUCED smoothness |")
    print("| direct C1 coefficient matching | DERIVED_REDUCED toy relation |")
    print("| near-surface interior deviation | PLAUSIBLE |")
    print("| joint energy functional | PLAUSIBLE / missing derivation |")
    print("| final physical spline model | UNFINISHED |")

    status_line("joint minimum spline classification produced",
                "CONSTRAINED_BY_IDENTITY",
                "useful model, not derivation")


def case_11_next_tests():
    header("Case 11: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_kappa_joint_minimum_energy_functional.py")
    print("   Make the spline model variational instead of hand-blended.")
    print()
    print("2. candidate_kappa_trace_response_status_summary.md")
    print("   Summarize group 10.")
    print()
    print("3. candidate_kappa_minimum_shift_source_model.py")
    print("   Return to local minimum-shift source law.")
    print()
    print("Recommended next artifact:")
    print()
    print("  candidate_kappa_joint_minimum_spline_model.md")
    print()
    print("Recommended next script:")
    print("  candidate_kappa_joint_minimum_energy_functional.py")

    status_line("next test selected",
                "CONSTRAINED_BY_IDENTITY",
                "energy functional is next if continuing")


def final_interpretation():
    header("Final interpretation")

    print("A joint-minimum spline model can represent:")
    print()
    print("  interior quadratic tendency")
    print("  exterior reciprocal 1/r tendency")
    print("  smooth near-surface compromise")
    print()
    print("This supports the idea that interior curvature need not be exactly")
    print("Newtonian/parabolic near the surface.")
    print()
    print("The real version should be variational:")
    print()
    print("  minimize a combined interior/exterior/smoothness energy")
    print()
    print("Possible next artifact:")
    print("  candidate_kappa_joint_minimum_spline_model.md")
    print()
    print("Possible next script:")
    print("  candidate_kappa_joint_minimum_energy_functional.py")


def main():
    header("Candidate Kappa Joint Minimum Spline Model")
    case_0_problem_statement()
    case_1_define_interior_and_exterior_tendencies()
    case_2_hermite_transition_layer()
    case_3_quintic_smoothstep()
    case_4_blended_joint_minimum()
    case_5_boundary_matching_equations()
    case_6_curvature_deviation_near_surface()
    case_7_energy_functional_placeholder()
    case_8_kappa_relation()
    case_9_failure_controls()
    case_10_classification()
    case_11_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
