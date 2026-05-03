# Candidate kappa pressure trace model
#
# Purpose
# -------
# The kappa exterior suppression study found:
#
#   kappa_ext = 0 is required for the reconstructed static exterior.
#   A massless exterior kappa equation permits kappa = C1/r unless exterior
#   kappa charge/flux vanishes.
#
# This script builds a simple interior pressure/spatial-trace source model.
#
# It asks:
#
#   1. if S_trace = 3p for a uniform-density hydrostatic toy sphere,
#   2. whether the resulting integrated kappa charge is generically nonzero,
#   3. whether that would create an exterior kappa tail if kappa is massless,
#   4. what extra condition is needed to avoid exterior leakage.
#
# This is a toy model, not a GR interior solution.

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
    header("Case 0: Kappa pressure/trace model problem")

    print("Question:")
    print()
    print("  If kappa is sourced by pressure or spatial stress trace, does an")
    print("  interior matter body generate forbidden exterior kappa charge?")
    print()
    print("Toy source:")
    print()
    print("  S_trace = 3p")
    print()
    print("Goal:")
    print()
    print("  determine whether pressure trace requires projection/screening to avoid")
    print("  an exterior 1/r kappa tail.")

    status_line("pressure trace model problem posed", "CONSTRAINED_BY_IDENTITY")


def case_1_pressure_profile():
    header("Case 1: Simple pressure profile")

    r, R, p0 = sp.symbols("r R p0", positive=True, real=True)

    p = p0 * (1 - r**2/R**2)
    S_trace = 3*p

    print("Toy pressure profile:")
    print()
    print("  p(r) = p0 (1 - r^2/R^2)")
    print()
    print(f"p(r) = {p}")
    print()
    print("Spatial trace source:")
    print()
    print("  S_trace = 3p")
    print()
    print(f"S_trace = {S_trace}")
    print()
    print("This is a toy interior source, not a GR pressure profile.")

    status_line("toy pressure trace source defined", "PLAUSIBLE",
                "not derived from hydrostatic equilibrium")

    return r, R, p0, p, S_trace


def case_2_integrated_trace_charge(r, R, p0, S_trace):
    header("Case 2: Integrated trace charge")

    Q = sp.simplify(4*sp.pi*sp.integrate(r**2*S_trace, (r, 0, R)))

    print("Integrated trace charge:")
    print()
    print("  Q_kappa = 4*pi integral_0^R r^2 S_trace dr")
    print()
    print(f"Q_kappa = {Q}")
    print()
    print("For p0 > 0, Q_kappa is nonzero.")
    print()
    print("If massless kappa uses this as ordinary charge, exterior kappa gets a 1/r tail.")

    status_line("pressure trace has nonzero integrated charge", "RISK",
                "massless kappa would leak outside")

    return Q


def case_3_massless_flux_consequence():
    header("Case 3: Massless exterior flux consequence")

    alpha_k, K_k, Q_kappa = sp.symbols("alpha_k K_k Q_kappa", positive=True, real=True)
    r = sp.symbols("r", positive=True, real=True)

    F_kappa = -alpha_k * Q_kappa / K_k
    kappa_tail = alpha_k * Q_kappa / (4*sp.pi*K_k*r)

    print("Schematic massless equation:")
    print()
    print("  -K_k Delta kappa = alpha_k S_trace")
    print()
    print("Exterior flux proportional to integrated trace charge:")
    print()
    print(f"F_kappa ~ {F_kappa}")
    print()
    print("Exterior tail:")
    print()
    print(f"kappa_ext ~ {kappa_tail}")
    print()
    print("Thus a positive pressure trace source generically creates exterior leakage.")

    status_line("massless pressure-sourced kappa leaks outside", "RISK",
                "requires projection, screening, or zero-charge construction")


def case_4_zero_charge_requirement():
    header("Case 4: Zero-charge requirement")

    print("To preserve exterior kappa = 0 with massless kappa:")
    print()
    print("  Q_kappa = integral S_trace d^3x must vanish")
    print()
    print("But for ordinary positive pressure:")
    print()
    print("  integral 3p d^3x > 0")
    print()
    print("Therefore a raw pressure-trace Poisson law is not exterior-safe.")
    print()
    print("Needed:")
    print()
    print("  constraint projection that removes monopole kappa charge")
    print("  or restoring/massive suppression")
    print("  or source defined as compensated trace exchange with zero net charge")

    status_line("zero-charge condition conflicts with raw positive pressure", "RISK",
                "raw S_trace=3p not enough")


def case_5_compensated_trace_source():
    header("Case 5: Compensated trace source option")

    r, R, p0 = sp.symbols("r R p0", positive=True, real=True)

    p = p0 * (1 - r**2/R**2)
    S_raw = 3*p
    volume = 4*sp.pi*R**3/3
    Q_raw = sp.simplify(4*sp.pi*sp.integrate(r**2*S_raw, (r, 0, R)))
    S_avg = sp.simplify(Q_raw / volume)

    S_comp = sp.simplify(S_raw - S_avg)
    Q_comp = sp.simplify(4*sp.pi*sp.integrate(r**2*S_comp, (r, 0, R)))

    print("Compensated source idea:")
    print()
    print("  S_comp = S_trace - <S_trace>")
    print()
    print(f"<S_trace> = {S_avg}")
    print()
    print(f"S_comp = {S_comp}")
    print()
    print("Integrated compensated charge:")
    print()
    print(f"Q_comp = {Q_comp}")
    print()
    print("This removes monopole kappa charge by construction.")
    print("But it must be derived from a parent constraint, not inserted arbitrarily.")

    status_line("compensated trace source can enforce zero charge", "CONSTRAINED_BY_IDENTITY",
                "needs parent identity")


def case_6_massive_trace_response_option():
    header("Case 6: Massive/restoring trace response option")

    r, Q, alpha_k, K_k, m_k = sp.symbols("r Q alpha_k K_k m_k", positive=True, real=True)

    kappa_ext = alpha_k * Q * sp.exp(-m_k*r) / (4*sp.pi*K_k*r)

    print("If kappa has a restoring/mass scale:")
    print()
    print("  (-Delta + m_k^2) kappa = source")
    print()
    print("then exterior tail is Yukawa-suppressed:")
    print()
    print(f"kappa_ext ~ {kappa_ext}")
    print()
    print("This allows nonzero integrated trace charge but avoids long-range leakage.")
    print()
    print("However m_k must be derived or constrained.")

    status_line("massive trace response can suppress leakage", "PLAUSIBLE",
                "new scale m_k missing")


def case_7_classification():
    header("Case 7: Classification")

    print("| Model | Status |")
    print("|---|---|")
    print("| S_trace = 3p | PLAUSIBLE interior source |")
    print("| integrated Q_kappa from positive pressure | RISK / nonzero |")
    print("| massless kappa with Q_kappa != 0 | RISK / exterior 1/r leak |")
    print("| compensated trace source | CONSTRAINED_BY_IDENTITY if parent-derived |")
    print("| massive/restoring kappa | PLAUSIBLE if m_k derived |")
    print("| raw pressure Poisson law as final equation | REJECTED unless screened/projected |")

    status_line("pressure trace classification produced", "RISK",
                "raw pressure source leaks unless constrained")


def case_8_next_tests():
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_kappa_gauge_vs_physical_trace.py")
    print("   Separate gauge-volume artifact from physical trace response.")
    print()
    print("2. candidate_kappa_compensated_trace_constraint.py")
    print("   Test zero-net-trace source construction.")
    print()
    print("3. candidate_kappa_scalar_radiation_leak_check.py")
    print("   Check whether trace response leaks scalar radiation dynamically.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_kappa_compensated_trace_constraint.py")
    print()
    print("Reason:")
    print("  Raw pressure source creates nonzero kappa charge; compensation/projection is the")
    print("  immediate issue.")

    status_line("next test selected", "CONSTRAINED_BY_IDENTITY",
                "compensated trace constraint is next")


def final_interpretation():
    header("Final interpretation")

    print("A raw pressure/spatial-trace source is plausible for the interior, but")
    print("dangerous for the exterior.")
    print()
    print("For positive pressure:")
    print()
    print("  Q_kappa = integral 3p d^3x != 0")
    print()
    print("A massless kappa equation would then produce:")
    print()
    print("  kappa_ext ~ 1/r")
    print()
    print("Therefore raw pressure trace cannot be the final unscreened kappa source.")
    print()
    print("Need one of:")
    print()
    print("  compensated/zero-charge trace constraint")
    print("  massive/restoring suppression")
    print("  parent projection that removes exterior kappa charge")
    print()
    print("Possible next artifact:")
    print("  candidate_kappa_pressure_trace_model.md")
    print()
    print("Possible next script:")
    print("  candidate_kappa_compensated_trace_constraint.py")


def main():
    header("Candidate Kappa Pressure Trace Model")
    case_0_problem_statement()
    r, R, p0, p, S_trace = case_1_pressure_profile()
    case_2_integrated_trace_charge(r, R, p0, S_trace)
    case_3_massless_flux_consequence()
    case_4_zero_charge_requirement()
    case_5_compensated_trace_source()
    case_6_massive_trace_response_option()
    case_7_classification()
    case_8_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
