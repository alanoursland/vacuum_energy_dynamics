# Candidate kappa second derivative boundary stress
#
# Purpose
# -------
# The kappa boundary-layer model found a compact profile:
#
#   kappa(r) = kappa_0 (1 - r^2/R^2)^2
#
# with:
#
#   kappa(R) = 0
#   kappa'(R) = 0
#   F_kappa(R) = 0
#
# so it can match to exterior kappa = 0 without exporting first-derivative flux.
#
# But the next trap is hidden interface stress:
#
#   Does kappa'' jump at R?
#   Does Delta kappa jump?
#   Does a shell source appear?
#
# This script checks second-derivative and effective-source behavior at the
# boundary, and compares the simple C1 profile to a smoother C2 compact profile.
#
# This is a boundary regularity test, not a final interface derivation.
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/10_kappa_trace_response/
#   or:
#   scripts_v3/candidate_kappa_second_derivative_boundary_stress.py

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


def areal_laplacian(expr, r):
    return sp.simplify(sp.diff(expr, r, 2) + 2*sp.diff(expr, r)/r)


def case_0_problem_statement():
    header("Case 0: Kappa second-derivative boundary stress problem")

    print("Question:")
    print()
    print("  Does a compact interior kappa profile create hidden boundary stress")
    print("  through second-derivative or effective-source jumps?")
    print()
    print("Known from previous model:")
    print()
    print("  kappa(R)=0")
    print("  kappa'(R)=0")
    print("  exterior kappa=0")
    print()
    print("Need now:")
    print()
    print("  check kappa''(R)")
    print("  check Delta kappa(R)")
    print("  decide whether smoother compact profile is required")

    status_line("second derivative boundary stress problem posed",
                "CONSTRAINED_BY_IDENTITY")


def case_1_C1_profile_second_derivatives():
    header("Case 1: C1 compact profile second derivatives")

    r, R, k0 = sp.symbols("r R kappa_0", positive=True, real=True)

    x = r/R
    kappa = k0*(1 - x**2)**2
    dk = sp.simplify(sp.diff(kappa, r))
    d2k = sp.simplify(sp.diff(kappa, r, 2))
    lap = areal_laplacian(kappa, r)

    print("Profile:")
    print()
    print("  kappa = k0 (1 - r^2/R^2)^2")
    print()
    print(f"kappa = {kappa}")
    print()
    print("Boundary values:")
    print()
    print(f"kappa(R) = {sp.simplify(kappa.subs(r, R))}")
    print(f"kappa'(R) = {sp.simplify(dk.subs(r, R))}")
    print(f"kappa''(R-) = {sp.simplify(d2k.subs(r, R))}")
    print(f"Delta kappa(R-) = {sp.simplify(lap.subs(r, R))}")
    print()
    print("Exterior kappa=0 has:")
    print()
    print("  kappa''(R+) = 0")
    print("  Delta kappa(R+) = 0")
    print()
    print("Thus the second derivative/effective source jumps at R.")

    jump_d2 = sp.simplify(d2k.subs(r, R))
    jump_lap = sp.simplify(lap.subs(r, R))

    status_line("C1 profile has second-derivative/effective-source jump",
                "RISK" if jump_d2 != 0 or jump_lap != 0 else "DERIVED_REDUCED",
                "may imply boundary layer or hidden interface stress")

    return r, R, k0


def case_2_C2_profile_candidate(r, R, k0):
    header("Case 2: C2 smoother compact profile candidate")

    x = r/R

    # Higher-power compact profile. This makes value, first derivative, and
    # second derivative vanish at R.
    kappa = k0*(1 - x**2)**3
    dk = sp.simplify(sp.diff(kappa, r))
    d2k = sp.simplify(sp.diff(kappa, r, 2))
    lap = areal_laplacian(kappa, r)

    print("Smoother profile:")
    print()
    print("  kappa = k0 (1 - r^2/R^2)^3")
    print()
    print(f"kappa = {kappa}")
    print()
    print("Boundary values:")
    print()
    print(f"kappa(R) = {sp.simplify(kappa.subs(r, R))}")
    print(f"kappa'(R) = {sp.simplify(dk.subs(r, R))}")
    print(f"kappa''(R-) = {sp.simplify(d2k.subs(r, R))}")
    print(f"Delta kappa(R-) = {sp.simplify(lap.subs(r, R))}")
    print()
    print("This profile matches exterior zero through second derivative/effective source.")

    ok = (
        sp.simplify(kappa.subs(r, R)) == 0
        and sp.simplify(dk.subs(r, R)) == 0
        and sp.simplify(d2k.subs(r, R)) == 0
        and sp.simplify(lap.subs(r, R)) == 0
    )

    status_line("C2 profile removes second-derivative/effective-source jump",
                "DERIVED_REDUCED" if ok else "RISK")

    return kappa, lap


def case_3_flux_and_charge_for_C2(r, R, kappa):
    header("Case 3: Flux and charge for C2 profile")

    dk = sp.simplify(sp.diff(kappa, r))
    flux = sp.simplify(4*sp.pi*r**2*dk)
    flux_R = sp.simplify(flux.subs(r, R))
    lap = areal_laplacian(kappa, r)
    source_integral = sp.simplify(4*sp.pi*sp.integrate(r**2*lap, (r, 0, R)))

    print("Flux:")
    print()
    print(f"F_kappa(r) = {flux}")
    print(f"F_kappa(R) = {flux_R}")
    print()
    print("Integrated effective source:")
    print()
    print(f"integral Delta kappa d^3x = {source_integral}")
    print()
    print("C2 profile keeps zero flux and zero net source.")

    ok = sp.simplify(flux_R) == 0 and sp.simplify(source_integral) == 0

    status_line("C2 profile has zero flux and zero net effective source",
                "DERIVED_REDUCED" if ok else "RISK")


def case_4_regular_center_check(r, R, k0, kappa):
    header("Case 4: Regular center check")

    dk = sp.simplify(sp.diff(kappa, r))
    d2k = sp.simplify(sp.diff(kappa, r, 2))
    lap = areal_laplacian(kappa, r)

    print("Center values for C2 profile:")
    print()
    print(f"kappa(0) = {sp.simplify(kappa.subs(r, 0))}")
    print(f"kappa'(0) = {sp.simplify(dk.subs(r, 0))}")
    print(f"kappa''(0) = {sp.simplify(d2k.subs(r, 0))}")
    print(f"Delta kappa(0) = {sp.simplify(lap.subs(r, 0))}")
    print()
    print("The profile is regular at the center.")

    status_line("C2 profile is center-regular",
                "DERIVED_REDUCED",
                "source sign/compatibility still needs checking")


def case_5_effective_source_shape(r, R, kappa):
    header("Case 5: Effective source shape for C2 profile")

    lap = sp.factor(areal_laplacian(kappa, r))

    print("Effective source shape:")
    print()
    print("  S_eff ~ Delta kappa")
    print()
    print(f"S_eff = {lap}")
    print()
    print("This source shape has positive and negative regions so that net charge")
    print("vanishes.")
    print()
    print("It resembles a compensated trace source rather than raw positive pressure.")

    status_line("C2 effective source is compensated-like",
                "CONSTRAINED_BY_IDENTITY",
                "must be derived from trace/minimum law")


def case_6_interface_interpretation():
    header("Case 6: Interface interpretation")

    print("The C1 profile:")
    print()
    print("  matches value and first derivative")
    print("  but jumps in second derivative/effective source")
    print()
    print("The C2 profile:")
    print()
    print("  matches value, first derivative, and second derivative")
    print("  has zero boundary flux")
    print("  has zero net effective source")
    print()
    print("Interpretation:")
    print("  if hidden shell stress is forbidden, use at least C2 compact profile")
    print("  or derive an allowed boundary layer/interface stress explicitly")

    status_line("C2 smoothness preferred if no shell stress is allowed",
                "CONSTRAINED_BY_IDENTITY",
                "physical interface derivation missing")


def case_7_failure_controls():
    header("Case 7: Failure controls")

    print("Boundary stress control fails if:")
    print()
    print("1. kappa'' jumps and no interface stress accounts for it.")
    print("2. Delta kappa jumps and implies an unmodeled shell source.")
    print("3. smoother profile cannot be sourced by matter trace/minimum shift.")
    print("4. compensated effective source is inserted by hand.")
    print("5. higher derivative terms in the true action require even higher smoothness.")
    print("6. boundary smoothness hides rather than explains scalar confinement.")

    status_line("boundary stress failure controls stated",
                "RISK",
                "true action determines required smoothness")


def case_8_classification():
    header("Case 8: Classification")

    print("| Item | Status |")
    print("|---|---|")
    print("| C1 profile value/first derivative match | DERIVED_REDUCED |")
    print("| C1 profile second derivative jump | RISK |")
    print("| C2 profile value/first/second derivative match | DERIVED_REDUCED |")
    print("| C2 boundary flux zero | DERIVED_REDUCED |")
    print("| C2 net effective source zero | DERIVED_REDUCED |")
    print("| C2 source shape derived from matter trace | MISSING |")
    print("| physical interface law | MISSING |")
    print("| required smoothness from true action | MISSING |")

    status_line("second-derivative boundary stress classification produced",
                "CONSTRAINED_BY_IDENTITY",
                "C2 solves toy stress jump, derivation missing")


def case_9_next_tests():
    header("Case 9: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_kappa_boundary_layer_source_compatibility.py")
    print("   Check whether plausible pressure/trace/minimum shift can produce C2 source.")
    print()
    print("2. candidate_kappa_trace_response_status_summary.md")
    print("   Summarize group 10.")
    print()
    print("3. candidate_kappa_action_smoothness_requirement.py")
    print("   Determine smoothness required by candidate kappa action.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_kappa_boundary_layer_source_compatibility.py")
    print()
    print("Reason:")
    print("  C2 compactness works mathematically; now source compatibility is the issue.")

    status_line("next test selected",
                "CONSTRAINED_BY_IDENTITY",
                "source compatibility is next")


def final_interpretation():
    header("Final interpretation")

    print("The previous C1 compact profile avoids exterior flux but has a second")
    print("derivative/effective-source jump at the boundary.")
    print()
    print("A smoother C2 profile:")
    print()
    print("  kappa = k0 (1 - r^2/R^2)^3")
    print()
    print("matches exterior zero through second derivative, keeps boundary flux zero,")
    print("and has zero net effective source.")
    print()
    print("This removes the hidden shell-stress trap at toy level.")
    print()
    print("But source compatibility remains missing.")
    print()
    print("Possible next artifact:")
    print("  candidate_kappa_second_derivative_boundary_stress.md")
    print()
    print("Possible next script:")
    print("  candidate_kappa_boundary_layer_source_compatibility.py")


def main():
    header("Candidate Kappa Second Derivative Boundary Stress")
    case_0_problem_statement()
    r, R, k0 = case_1_C1_profile_second_derivatives()
    kappa_c2, lap_c2 = case_2_C2_profile_candidate(r, R, k0)
    case_3_flux_and_charge_for_C2(r, R, kappa_c2)
    case_4_regular_center_check(r, R, k0, kappa_c2)
    case_5_effective_source_shape(r, R, kappa_c2)
    case_6_interface_interpretation()
    case_7_failure_controls()
    case_8_classification()
    case_9_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
