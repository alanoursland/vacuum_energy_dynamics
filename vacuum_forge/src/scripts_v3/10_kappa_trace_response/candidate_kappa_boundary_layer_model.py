# Candidate kappa boundary layer model
#
# Purpose
# -------
# The non-inertial kappa relaxation model found:
#
#   kappa is not a wave,
#   kappa is a non-inertial trace/volume relaxation coordinate,
#   matter trace shifts the local vacuum-curvature minimum,
#   kappa relaxes monotonically toward that minimum,
#   there is no independent kappa momentum channel.
#
# This fits the earlier rule:
#
#   propagating breathing waves are not allowed.
#
# The next concrete issue is the boundary:
#
#   interior kappa may exist,
#   exterior kappa must vanish,
#   exterior flux must vanish.
#
# This script builds toy boundary-layer profiles that satisfy:
#
#   kappa(R+) = 0
#   partial_r kappa(R+) = 0
#
# while allowing interior trace response.
#
# This is not a derived matter/vacuum interface theory.
# It is a boundary-control model.
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/10_kappa_trace_response/
#   or:
#   scripts_v3/candidate_kappa_boundary_layer_model.py

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
    header("Case 0: Kappa boundary-layer problem")

    print("Question:")
    print()
    print("  Can interior kappa exist while exterior kappa and exterior flux vanish?")
    print()
    print("Boundary requirements:")
    print()
    print("  kappa(R+) = 0")
    print("  partial_r kappa(R+) = 0")
    print()
    print("Goal:")
    print()
    print("  allow interior trace/volume response")
    print("  forbid exterior kappa tail")
    print("  forbid propagating breathing leakage")

    status_line("boundary-layer problem posed", "CONSTRAINED_BY_IDENTITY")


def case_1_simple_profile():
    header("Case 1: Smooth compact interior profile")

    r, R, k0 = sp.symbols("r R kappa_0", positive=True, real=True)

    # Smooth profile with kappa(R)=0 and kappa'(R)=0.
    x = r/R
    kappa = k0 * (1 - x**2)**2
    dk = sp.simplify(sp.diff(kappa, r))

    kappa_R = sp.simplify(kappa.subs(r, R))
    dk_R = sp.simplify(dk.subs(r, R))
    kappa_0_val = sp.simplify(kappa.subs(r, 0))
    dk_0 = sp.simplify(dk.subs(r, 0))

    print("Toy compact interior profile:")
    print()
    print("  kappa(r) = kappa_0 (1 - r^2/R^2)^2")
    print()
    print(f"kappa(r) = {kappa}")
    print()
    print("Boundary values:")
    print()
    print(f"kappa(R) = {kappa_R}")
    print(f"kappa'(R) = {dk_R}")
    print()
    print("Center values:")
    print()
    print(f"kappa(0) = {kappa_0_val}")
    print(f"kappa'(0) = {dk_0}")

    ok = sp.simplify(kappa_R) == 0 and sp.simplify(dk_R) == 0

    status_line("smooth compact profile has zero value and flux at boundary",
                "DERIVED_REDUCED" if ok else "RISK")

    return r, R, k0, kappa, dk


def case_2_boundary_flux(r, R, kappa, dk):
    header("Case 2: Boundary flux diagnostic")

    flux = sp.simplify(4*sp.pi*r**2*dk)
    flux_R = sp.simplify(flux.subs(r, R))

    print("Flux diagnostic:")
    print()
    print("  F_kappa(r) = 4*pi r^2 kappa'(r)")
    print()
    print(f"F_kappa(r) = {flux}")
    print()
    print("At boundary:")
    print()
    print(f"F_kappa(R) = {flux_R}")

    status_line("boundary flux vanishes",
                "DERIVED_REDUCED" if sp.simplify(flux_R) == 0 else "RISK")


def case_3_no_exterior_tail():
    header("Case 3: Exterior extension")

    print("Define exterior:")
    print()
    print("  kappa_ext(r>R) = 0")
    print()
    print("Since the interior profile satisfies:")
    print()
    print("  kappa(R-) = 0")
    print("  kappa'(R-) = 0")
    print()
    print("and exterior satisfies:")
    print()
    print("  kappa(R+) = 0")
    print("  kappa'(R+) = 0")
    print()
    print("there is no jump in value or first derivative.")
    print()
    print("Thus no exterior 1/r tail is required by matching.")

    status_line("zero exterior kappa extension is smooth to first derivative",
                "CONSTRAINED_BY_IDENTITY",
                "second derivative / stress layer not yet checked")


def case_4_effective_source_from_profile(r, R, k0, kappa):
    header("Case 4: Effective source implied by profile")

    lap = sp.simplify(sp.diff(kappa, r, 2) + 2*sp.diff(kappa, r)/r)

    print("If a schematic elliptic operator is used:")
    print()
    print("  Delta_areal kappa = kappa'' + 2 kappa'/r")
    print()
    print("then the toy profile implies:")
    print()
    print(f"Delta kappa = {lap}")
    print()
    print("This is the effective source shape needed to support the boundary-confined profile.")
    print()
    print("It is not derived from matter trace yet.")

    status_line("effective source shape computed",
                "DERIVED_REDUCED",
                "source law not derived")


def case_5_source_integral_check(r, R, kappa):
    header("Case 5: Effective source integral check")

    lap = sp.simplify(sp.diff(kappa, r, 2) + 2*sp.diff(kappa, r)/r)
    integral = sp.simplify(4*sp.pi*sp.integrate(r**2*lap, (r, 0, R)))

    print("Integrated Laplacian source:")
    print()
    print("  integral Delta kappa d^3x")
    print()
    print(f"= {integral}")
    print()
    print("By divergence theorem this equals boundary flux.")
    print("Since boundary flux is zero, the integrated source is zero.")
    print()
    print("This matches the zero-charge projection idea.")

    status_line("effective source has zero net charge",
                "DERIVED_REDUCED" if sp.simplify(integral) == 0 else "RISK")


def case_6_boundary_layer_interpretation():
    header("Case 6: Boundary-layer interpretation")

    print("The toy profile shows a possible pattern:")
    print()
    print("  kappa can be nonzero inside matter")
    print("  kappa can relax to zero at the boundary")
    print("  kappa' can also vanish at the boundary")
    print("  exterior kappa can be identically zero")
    print()
    print("Interpretation:")
    print("  trace/volume response is interior-confined")
    print("  no scalar charge is exported")
    print("  no exterior breathing field is launched")
    print()
    print("But:")
    print("  the profile is chosen, not derived.")

    status_line("boundary-confined kappa is structurally possible",
                "CONSTRAINED_BY_IDENTITY",
                "interface physics missing")


def case_7_noninertial_compatibility():
    header("Case 7: Compatibility with non-inertial relaxation")

    print("The profile is compatible with non-inertial relaxation if:")
    print()
    print("  kappa_min(r) is nonzero inside matter")
    print("  kappa_min(R) = 0")
    print("  kappa_min'(R) = 0")
    print("  exterior kappa_min = 0")
    print()
    print("Then kappa can relax locally toward kappa_min without carrying")
    print("momentum through the boundary.")
    print()
    print("This realizes:")
    print()
    print("  local trace relaxation")
    print("  no propagating breathing wave")

    status_line("boundary profile fits non-inertial relaxation picture",
                "PLAUSIBLE",
                "kappa_min source law missing")


def case_8_failure_controls():
    header("Case 8: Failure controls")

    print("The boundary-layer model fails if:")
    print()
    print("1. kappa'(R+) is nonzero and exports flux.")
    print("2. profile requires an unphysical shell source at R.")
    print("3. second derivative jump creates hidden boundary stress.")
    print("4. chosen profile cannot be produced by trace/pressure source.")
    print("5. boundary confinement is inserted only to hide scalar radiation.")
    print("6. non-inertial relaxation secretly includes a second-order wave channel.")

    status_line("boundary-layer failure controls stated",
                "RISK",
                "interface/source derivation needed")


def case_9_classification():
    header("Case 9: Classification")

    print("| Item | Status |")
    print("|---|---|")
    print("| compact profile kappa = k0(1-r^2/R^2)^2 | PLAUSIBLE toy model |")
    print("| kappa(R)=0 | DERIVED_REDUCED |")
    print("| kappa'(R)=0 | DERIVED_REDUCED |")
    print("| boundary flux F_kappa(R)=0 | DERIVED_REDUCED |")
    print("| exterior kappa=0 extension | CONSTRAINED_BY_IDENTITY |")
    print("| effective source integral zero | DERIVED_REDUCED |")
    print("| source/interface derivation | MISSING |")
    print("| hidden boundary stress check | MISSING |")

    status_line("boundary-layer classification produced",
                "CONSTRAINED_BY_IDENTITY",
                "toy confinement works, derivation missing")


def case_10_next_tests():
    header("Case 10: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_kappa_boundary_layer_source_compatibility.py")
    print("   Check whether plausible pressure/trace source can produce the compact profile.")
    print()
    print("2. candidate_kappa_trace_response_status_summary.md")
    print("   Summarize group 10 current status.")
    print()
    print("3. candidate_kappa_second_derivative_boundary_stress.py")
    print("   Check hidden shell/boundary stress from derivative jumps.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_kappa_second_derivative_boundary_stress.py")
    print()
    print("Reason:")
    print("  Value and flux match, but second derivative/interface stress is the next trap.")

    status_line("next test selected",
                "CONSTRAINED_BY_IDENTITY",
                "hidden boundary stress check is next")


def final_interpretation():
    header("Final interpretation")

    print("A toy compact kappa profile can allow:")
    print()
    print("  interior kappa response")
    print("  kappa(R)=0")
    print("  kappa'(R)=0")
    print("  F_kappa(R)=0")
    print("  exterior kappa=0")
    print()
    print("This supports the idea that kappa can be an interior, non-propagating")
    print("trace relaxation variable rather than a breathing wave.")
    print()
    print("Possible next artifact:")
    print("  candidate_kappa_boundary_layer_model.md")
    print()
    print("Possible next script:")
    print("  candidate_kappa_second_derivative_boundary_stress.py")


def main():
    header("Candidate Kappa Boundary Layer Model")
    case_0_problem_statement()
    r, R, k0, kappa, dk = case_1_simple_profile()
    case_2_boundary_flux(r, R, kappa, dk)
    case_3_no_exterior_tail()
    case_4_effective_source_from_profile(r, R, k0, kappa)
    case_5_source_integral_check(r, R, kappa)
    case_6_boundary_layer_interpretation()
    case_7_noninertial_compatibility()
    case_8_failure_controls()
    case_9_classification()
    case_10_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
