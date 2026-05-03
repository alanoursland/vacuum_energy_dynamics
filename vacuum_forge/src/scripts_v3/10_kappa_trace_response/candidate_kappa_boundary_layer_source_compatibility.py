# Candidate kappa boundary layer source compatibility
#
# Purpose
# -------
# The second-derivative boundary stress test found:
#
#   C1 profile: kappa = k0 (1 - r^2/R^2)^2
#     value and first derivative match exterior zero,
#     but second derivative/effective source jumps at R.
#
#   C2 profile: kappa = k0 (1 - r^2/R^2)^3
#     value, first derivative, second derivative, and effective source match
#     exterior zero at R,
#     boundary flux is zero,
#     net effective source is zero.
#
# But C2's effective source is compensated-like, not raw positive pressure.
#
# This script checks whether plausible pressure/trace/minimum-shift physics can
# produce or interpret the C2 effective source.
#
# Candidate interpretations:
#
#   1. raw pressure trace source,
#   2. compensated trace source,
#   3. source-shifted local minimum kappa_min(r),
#   4. boundary/interface response,
#   5. hand-chosen smoothing.
#
# This is a compatibility audit, not a final source derivation.
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/10_kappa_trace_response/
#   or:
#   scripts_v3/candidate_kappa_boundary_layer_source_compatibility.py

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
    header("Case 0: Kappa boundary-layer source compatibility problem")

    print("Question:")
    print()
    print("  Can the smooth C2 compact kappa profile be produced by plausible")
    print("  trace/pressure/minimum-shift physics?")
    print()
    print("Profile:")
    print()
    print("  kappa = k0 (1 - r^2/R^2)^3")
    print()
    print("Known:")
    print()
    print("  zero boundary value")
    print("  zero boundary flux")
    print("  zero second-derivative boundary jump")
    print("  zero net effective source")
    print()
    print("Now test source compatibility.")

    status_line("boundary-layer source compatibility problem posed",
                "CONSTRAINED_BY_IDENTITY")


def case_1_effective_source_for_C2():
    header("Case 1: C2 effective source")

    r, R, k0 = sp.symbols("r R kappa_0", positive=True, real=True)

    x = r/R
    kappa = k0*(1 - x**2)**3
    S_eff = sp.factor(areal_laplacian(kappa, r))

    print("C2 profile:")
    print()
    print(f"kappa = {kappa}")
    print()
    print("Effective source:")
    print()
    print("  S_eff ~ Delta kappa")
    print()
    print(f"S_eff = {S_eff}")

    Q_eff = sp.simplify(4*sp.pi*sp.integrate(r**2*S_eff, (r, 0, R)))

    print()
    print("Integrated effective source:")
    print()
    print(f"Q_eff = {Q_eff}")

    status_line("C2 effective source computed",
                "DERIVED_REDUCED",
                "source interpretation pending")

    return r, R, k0, kappa, S_eff


def case_2_sign_structure(r, R, S_eff):
    header("Case 2: Sign structure")

    roots = sp.solve(sp.Eq(S_eff, 0), r)

    print("Zeros of effective source:")
    print()
    print(roots)
    print()
    print("Nontrivial physical root inside support:")
    print()
    print("  r = sqrt(3/7) R")
    print()
    print("Interpretation:")
    print("  S_eff changes sign inside the matter support.")
    print("  Therefore it is not a raw positive pressure source.")

    status_line("C2 effective source changes sign",
                "CONSTRAINED_BY_IDENTITY",
                "raw pressure trace cannot directly produce it")


def case_3_compare_raw_pressure():
    header("Case 3: Raw pressure trace comparison")

    r, R, p0 = sp.symbols("r R p0", positive=True, real=True)

    p = p0*(1 - r**2/R**2)
    S_raw = 3*p

    print("Toy raw pressure trace:")
    print()
    print(f"S_raw = {S_raw}")
    print()
    print("For p0 > 0 and 0 <= r <= R:")
    print()
    print("  S_raw >= 0")
    print()
    print("But C2 S_eff changes sign.")
    print()
    print("Conclusion:")
    print("  raw pressure trace alone is incompatible with the C2 effective source.")

    status_line("raw pressure trace incompatible as sole source",
                "REJECTED",
                "unless projected/combined with compensation")


def case_4_compensated_trace_comparison(r, R, S_eff):
    header("Case 4: Compensated trace comparison")

    p0 = sp.symbols("p0", positive=True, real=True)

    S_raw = 3*p0*(1 - r**2/R**2)
    V = 4*sp.pi*R**3/3
    Q_raw = sp.simplify(4*sp.pi*sp.integrate(r**2*S_raw, (r, 0, R)))
    avg = sp.simplify(Q_raw/V)
    S_comp = sp.factor(S_raw - avg)

    print("Compensated pressure trace:")
    print()
    print(f"S_comp = {S_comp}")
    print()
    print("C2 effective source:")
    print()
    print(f"S_eff = {S_eff}")
    print()
    print("Both have zero net integral and sign-changing structure.")
    print("They are not identical shapes, but they are in the same compensated-source family.")

    status_line("C2 source resembles compensated trace family",
                "PLAUSIBLE",
                "exact source law not derived")


def case_5_shifted_minimum_interpretation(r, R, k0, kappa):
    header("Case 5: Shifted local minimum interpretation")

    chi = sp.symbols("chi_k", positive=True, real=True)

    # If relaxation drives kappa -> kappa_min, then a static relaxed profile
    # can be interpreted as kappa_min(r) = kappa(r).
    kappa_min = sp.simplify(kappa)
    S_trace_required = sp.simplify(kappa_min / chi)

    print("If non-inertial relaxation reaches local equilibrium:")
    print()
    print("  kappa = kappa_min")
    print()
    print("and:")
    print()
    print("  kappa_min = chi_k S_trace_effective")
    print()
    print("then required effective trace source is:")
    print()
    print(f"S_trace_effective = {S_trace_required}")
    print()
    print("This source is compact, positive for k0/chi_k > 0, and vanishes smoothly at R.")
    print()
    print("Important:")
    print("  this is different from the elliptic effective source Delta kappa.")
    print("  in the non-inertial model, trace shifts the minimum rather than acting")
    print("  as a Poisson charge.")

    status_line("shifted-minimum interpretation can produce compact kappa directly",
                "PLAUSIBLE",
                "chi_k and source law not derived")


def case_6_operator_dependence_warning():
    header("Case 6: Operator-dependence warning")

    print("Source compatibility depends on which equation kappa obeys.")
    print()
    print("If kappa is elliptic:")
    print()
    print("  source ~ Delta kappa")
    print("  C2 implies compensated/sign-changing source")
    print()
    print("If kappa is non-inertial relaxation:")
    print()
    print("  source shifts kappa_min")
    print("  C2 can come from a compact positive shifted minimum")
    print()
    print("Therefore the non-inertial model is more compatible with ordinary")
    print("interior trace response than a Poisson-source kappa model.")

    status_line("source compatibility depends on kappa dynamics",
                "CONSTRAINED_BY_IDENTITY",
                "supports non-inertial minimum-shift picture")


def case_7_boundary_interface_source():
    header("Case 7: Boundary/interface interpretation")

    print("The smooth compact C2 profile may reflect:")
    print()
    print("  matter trace source in the interior")
    print("  plus vacuum-interface restoration near the boundary")
    print()
    print("Rather than:")
    print()
    print("  raw pressure source alone")
    print()
    print("This suggests a two-part source/minimum:")
    print()
    print("  kappa_min(r) = interior trace shift * boundary cutoff")
    print()
    print("where the boundary cutoff enforces:")
    print()
    print("  kappa_min(R)=0")
    print("  kappa_min'(R)=0")
    print("  kappa_min''(R)=0")
    print()
    print("This is plausible but not derived.")

    status_line("boundary cutoff/minimum-shift interpretation is plausible",
                "PLAUSIBLE",
                "interface law missing")


def case_8_classification():
    header("Case 8: Classification")

    print("| Interpretation | Status |")
    print("|---|---|")
    print("| raw pressure trace as elliptic source | REJECTED as sole source |")
    print("| compensated trace as elliptic source | PLAUSIBLE / needs parent identity |")
    print("| C2 source as Delta kappa | DERIVED_REDUCED shape, source law missing |")
    print("| shifted local minimum kappa_min | PLAUSIBLE |")
    print("| boundary cutoff/interface restoration | PLAUSIBLE |")
    print("| hand-chosen smoothing | RISK |")
    print("| final source compatibility | UNFINISHED |")

    status_line("source compatibility classification produced",
                "CONSTRAINED_BY_IDENTITY",
                "non-inertial shifted-minimum picture preferred")


def case_9_failure_controls():
    header("Case 9: Failure controls")

    print("Source compatibility fails if:")
    print()
    print("1. raw pressure is claimed to produce sign-changing Delta kappa directly.")
    print("2. compensation is inserted with no parent identity.")
    print("3. boundary cutoff is chosen only to hide exterior kappa.")
    print("4. shifted-minimum source is not connected to trace/volume physics.")
    print("5. interface restoration conflicts with A-sector mass flux.")
    print("6. kappa dynamics are mixed inconsistently between Poisson and relaxation pictures.")

    status_line("source compatibility failure controls stated",
                "RISK",
                "avoid mixing incompatible source interpretations")


def case_10_next_tests():
    header("Case 10: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_kappa_minimum_shift_source_model.py")
    print("   Formalize trace source as shifted kappa_min with boundary cutoff.")
    print()
    print("2. candidate_kappa_trace_response_status_summary.md")
    print("   Summarize group 10.")
    print()
    print("3. candidate_kappa_action_smoothness_requirement.py")
    print("   Determine smoothness required by candidate action.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_kappa_minimum_shift_source_model.py")
    print()
    print("Reason:")
    print("  Source compatibility favors non-inertial minimum-shift over Poisson source.")

    status_line("next test selected",
                "CONSTRAINED_BY_IDENTITY",
                "minimum-shift source model is next")


def final_interpretation():
    header("Final interpretation")

    print("The C2 compact profile is not naturally produced by raw pressure as")
    print("an elliptic Poisson source.")
    print()
    print("Its Delta-kappa source is compensated/sign-changing.")
    print()
    print("However, in the non-inertial relaxation picture, matter trace does not")
    print("need to equal Delta kappa.")
    print()
    print("Instead it can shift the local minimum:")
    print()
    print("  kappa_min = chi_k S_trace_effective")
    print()
    print("Then a smooth compact kappa_min can produce a smooth compact kappa")
    print("without treating trace as a radiative scalar charge.")
    print()
    print("Possible next artifact:")
    print("  candidate_kappa_boundary_layer_source_compatibility.md")
    print()
    print("Possible next script:")
    print("  candidate_kappa_minimum_shift_source_model.py")


def main():
    header("Candidate Kappa Boundary Layer Source Compatibility")
    case_0_problem_statement()
    r, R, k0, kappa, S_eff = case_1_effective_source_for_C2()
    case_2_sign_structure(r, R, S_eff)
    case_3_compare_raw_pressure()
    case_4_compensated_trace_comparison(r, R, S_eff)
    case_5_shifted_minimum_interpretation(r, R, k0, kappa)
    case_6_operator_dependence_warning()
    case_7_boundary_interface_source()
    case_8_classification()
    case_9_failure_controls()
    case_10_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
