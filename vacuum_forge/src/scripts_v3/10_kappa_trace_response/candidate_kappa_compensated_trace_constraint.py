# Candidate kappa compensated trace constraint
#
# Purpose
# -------
# The pressure-trace model found:
#
#   S_trace = 3p is plausible inside matter,
#   but Q_kappa = integral S_trace d^3x is generically nonzero,
#   so a massless kappa equation leaks as kappa_ext ~ 1/r.
#
# This script tests a compensated trace construction:
#
#   S_comp = S_trace - <S_trace>_support
#
# so that:
#
#   integral S_comp d^3x = 0
#
# It asks whether this can remove exterior monopole kappa leakage while keeping
# an interior trace/volume response.
#
# This is not yet a derived parent constraint.
# It is a zero-charge control test.
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/10_kappa_trace_response/
#   or:
#   scripts_v3/candidate_kappa_compensated_trace_constraint.py

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
    header("Case 0: Kappa compensated trace constraint problem")

    print("Problem:")
    print()
    print("  Raw pressure trace source has nonzero integrated kappa charge.")
    print()
    print("Candidate fix:")
    print()
    print("  S_comp = S_trace - <S_trace>_support")
    print()
    print("Goal:")
    print()
    print("  remove exterior monopole leakage while retaining interior trace response.")

    status_line("compensated trace problem posed", "CONSTRAINED_BY_IDENTITY")


def case_1_define_raw_and_compensated_source():
    header("Case 1: Define raw and compensated source")

    r, R, p0 = sp.symbols("r R p0", positive=True, real=True)

    p = p0 * (1 - r**2/R**2)
    S_raw = 3*p

    volume = 4*sp.pi*R**3/3
    Q_raw = sp.simplify(4*sp.pi*sp.integrate(r**2*S_raw, (r, 0, R)))
    S_avg = sp.simplify(Q_raw / volume)
    S_comp = sp.simplify(S_raw - S_avg)

    print("Raw source:")
    print()
    print(f"S_raw = {S_raw}")
    print()
    print("Support average:")
    print()
    print(f"<S_raw> = {S_avg}")
    print()
    print("Compensated source:")
    print()
    print(f"S_comp = {S_comp}")

    status_line("compensated source defined", "CONSTRAINED_BY_IDENTITY",
                "subtraction needs parent identity")

    return r, R, p0, S_raw, S_comp, Q_raw


def case_2_zero_charge_check(r, R, S_raw, S_comp, Q_raw):
    header("Case 2: Zero-charge check")

    Q_comp = sp.simplify(4*sp.pi*sp.integrate(r**2*S_comp, (r, 0, R)))

    print("Raw charge:")
    print()
    print(f"Q_raw = {Q_raw}")
    print()
    print("Compensated charge:")
    print()
    print(f"Q_comp = {Q_comp}")
    print()
    print("Therefore the compensated source removes monopole kappa charge.")

    status_line("compensated source has zero integrated charge",
                "DERIVED_REDUCED" if sp.simplify(Q_comp) == 0 else "RISK")

    return Q_comp


def case_3_interior_source_not_zero(r, R, p0, S_comp):
    header("Case 3: Interior source remains nontrivial")

    S_center = sp.simplify(S_comp.subs(r, 0))
    S_surface = sp.simplify(S_comp.subs(r, R))
    zero_crossings = sp.solve(sp.Eq(S_comp, 0), r)

    print("Compensated source values:")
    print()
    print(f"S_comp(0) = {S_center}")
    print(f"S_comp(R) = {S_surface}")
    print()
    print("Zero crossing(s):")
    print(zero_crossings)
    print()
    print("Interpretation:")
    print("  compensation does not erase kappa interior structure.")
    print("  it creates positive and negative regions with zero net charge.")

    status_line("compensated source retains interior structure", "CONSTRAINED_BY_IDENTITY",
                "physical meaning of negative compensation must be derived")


def case_4_massless_exterior_consequence():
    header("Case 4: Massless exterior consequence")

    alpha_k, K_k, Q_comp, r = sp.symbols("alpha_k K_k Q_comp r", positive=True, real=True)

    kappa_tail = alpha_k * Q_comp / (4*sp.pi*K_k*r)

    print("For massless kappa:")
    print()
    print("  kappa_ext ~ alpha_k Q_comp/(4*pi K_k r)")
    print()
    print(f"kappa_ext = {kappa_tail}")
    print()
    print("If Q_comp = 0, the monopole 1/r tail vanishes.")
    print()
    print("Higher multipoles or boundary-layer effects may remain, depending on source shape.")

    status_line("zero compensated charge removes monopole tail", "CONSTRAINED_BY_IDENTITY",
                "higher multipoles/boundary behavior not solved")


def case_5_parent_identity_requirement():
    header("Case 5: Parent identity requirement")

    print("Compensation is mathematically useful but physically dangerous.")
    print()
    print("It is acceptable only if a parent identity demands something like:")
    print()
    print("  integral S_kappa d^3x = 0")
    print()
    print("or:")
    print()
    print("  kappa responds only to deviations from mean trace inside a constrained support")
    print()
    print("or:")
    print()
    print("  exterior kappa charge is projected out by a constraint equation")
    print()
    print("Otherwise the subtraction is just a hand-tuned fix.")

    status_line("parent identity required for compensation", "MISSING",
                "zero-charge rule not derived")


def case_6_locality_warning():
    header("Case 6: Locality warning")

    print("The subtraction:")
    print()
    print("  S_comp = S_trace - <S_trace>_support")
    print()
    print("is nonlocal over the support region.")
    print()
    print("That may be acceptable for a constraint projection, but not for a local")
    print("dynamical source law unless derived from a constrained variable.")
    print()
    print("Thus compensation points toward kappa as a constrained/non-propagating")
    print("trace response, not an ordinary local scalar field.")

    status_line("compensation is nonlocal over support", "RISK",
                "suggests constraint projection rather than local scalar dynamics")


def case_7_classification():
    header("Case 7: Classification")

    print("| Item | Status |")
    print("|---|---|")
    print("| raw pressure trace source | PLAUSIBLE interior source |")
    print("| raw integrated charge | RISK / nonzero |")
    print("| compensated source | CONSTRAINED_BY_IDENTITY |")
    print("| zero integrated charge | DERIVED_REDUCED |")
    print("| interior structure retained | CONSTRAINED_BY_IDENTITY |")
    print("| parent identity for compensation | MISSING |")
    print("| locality of support-average subtraction | RISK |")
    print("| final kappa source law | UNFINISHED |")

    status_line("compensated trace classification produced", "CONSTRAINED_BY_IDENTITY",
                "works algebraically, needs parent identity")


def case_8_next_tests():
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_kappa_gauge_vs_physical_trace.py")
    print("   Separate gauge-volume artifact from physical trace response.")
    print()
    print("2. candidate_kappa_scalar_radiation_leak_check.py")
    print("   Check whether compensated trace response leaks scalar radiation dynamically.")
    print()
    print("3. candidate_kappa_constraint_projection_identity.py")
    print("   Try to formalize the zero-charge projection as a parent identity.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_kappa_gauge_vs_physical_trace.py")
    print()
    print("Reason:")
    print("  Compensation looks nonlocal/constraint-like; before promoting it, separate")
    print("  physical trace from gauge-volume artifact.")

    status_line("next test selected", "CONSTRAINED_BY_IDENTITY",
                "gauge-vs-physical trace is next")


def final_interpretation():
    header("Final interpretation")

    print("Compensated trace source:")
    print()
    print("  S_comp = S_trace - <S_trace>")
    print()
    print("does remove the monopole kappa charge:")
    print()
    print("  integral S_comp d^3x = 0")
    print()
    print("and therefore removes the massless exterior 1/r monopole leak.")
    print()
    print("But the subtraction is nonlocal over the source support and must be")
    print("derived from a parent constraint/projection identity.")
    print()
    print("Possible next artifact:")
    print("  candidate_kappa_compensated_trace_constraint.md")
    print()
    print("Possible next script:")
    print("  candidate_kappa_gauge_vs_physical_trace.py")


def main():
    header("Candidate Kappa Compensated Trace Constraint")
    case_0_problem_statement()
    r, R, p0, S_raw, S_comp, Q_raw = case_1_define_raw_and_compensated_source()
    case_2_zero_charge_check(r, R, S_raw, S_comp, Q_raw)
    case_3_interior_source_not_zero(r, R, p0, S_comp)
    case_4_massless_exterior_consequence()
    case_5_parent_identity_requirement()
    case_6_locality_warning()
    case_7_classification()
    case_8_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
