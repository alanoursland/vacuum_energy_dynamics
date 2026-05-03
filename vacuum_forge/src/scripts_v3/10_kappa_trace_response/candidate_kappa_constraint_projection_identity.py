# Candidate kappa constraint projection identity
#
# Purpose
# -------
# The gauge-vs-physical trace study found the current best interpretation:
#
#   kappa = constrained non-propagating trace response
#
# This can reconcile:
#
#   interior trace response,
#   exterior kappa = 0,
#   compensated zero-charge source,
#   scalar-radiation safety.
#
# But the missing piece is:
#
#   a parent projection identity.
#
# This script tries to formalize a zero-charge projection for kappa:
#
#   S_kappa = P_0 S_trace
#
# where P_0 removes the monopole/support-average charge:
#
#   P_0 S = S - <S>_support
#
# so that:
#
#   integral_support S_kappa d^3x = 0.
#
# This is not yet a derivation from a covariant parent theory.
# It is a formal constraint identity candidate.
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/10_kappa_trace_response/
#   or:
#   scripts_v3/candidate_kappa_constraint_projection_identity.py

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
    header("Case 0: Kappa constraint projection identity problem")

    print("Question:")
    print()
    print("  Can the compensated kappa source be written as a projection identity")
    print("  rather than an arbitrary subtraction?")
    print()
    print("Candidate projection:")
    print()
    print("  P_0 S = S - <S>_support")
    print()
    print("Required identity:")
    print()
    print("  integral_support P_0 S d^3x = 0")

    status_line("constraint projection identity problem posed", "CONSTRAINED_BY_IDENTITY")


def case_1_define_projection_operator():
    header("Case 1: Define zero-charge projection operator")

    print("For a compact support region V:")
    print()
    print("  <S>_V = (1/V) integral_V S d^3x")
    print()
    print("Define:")
    print()
    print("  P_0 S = S - <S>_V")
    print()
    print("Then:")
    print()
    print("  integral_V P_0 S d^3x = 0")
    print()
    print("This removes monopole kappa charge over the support.")

    status_line("zero-charge projection operator defined", "CONSTRAINED_BY_IDENTITY",
                "support/boundary definition required")


def case_2_toy_profile_projection():
    header("Case 2: Toy pressure profile projection")

    r, R, p0 = sp.symbols("r R p0", positive=True, real=True)

    S = 3*p0*(1 - r**2/R**2)
    V = 4*sp.pi*R**3/3
    Q = sp.simplify(4*sp.pi*sp.integrate(r**2*S, (r, 0, R)))
    S_avg = sp.simplify(Q/V)
    P0S = sp.simplify(S - S_avg)
    Q_projected = sp.simplify(4*sp.pi*sp.integrate(r**2*P0S, (r, 0, R)))

    print("Raw source:")
    print()
    print(f"S = {S}")
    print()
    print("Average over support:")
    print()
    print(f"<S> = {S_avg}")
    print()
    print("Projected source:")
    print()
    print(f"P_0 S = {P0S}")
    print()
    print("Projected charge:")
    print()
    print(f"integral P_0 S d^3x = {Q_projected}")

    status_line("toy projection has zero charge",
                "DERIVED_REDUCED" if sp.simplify(Q_projected) == 0 else "RISK")


def case_3_projector_idempotence():
    header("Case 3: Projection idempotence")

    print("A true projection should satisfy:")
    print()
    print("  P_0(P_0 S) = P_0 S")
    print()
    print("Reason:")
    print("  once the support-average is removed, applying the same operation again")
    print("  changes nothing.")
    print()
    print("For compact support with fixed V:")
    print()
    print("  <P_0 S> = 0")
    print("  P_0(P_0 S) = P_0 S - <P_0 S> = P_0 S")
    print()
    print("Thus P_0 is idempotent if the support region is fixed.")

    status_line("zero-charge operator is idempotent for fixed support",
                "DERIVED_REDUCED",
                "moving/dynamical support still unresolved")


def case_4_exterior_tail_control():
    header("Case 4: Exterior tail control")

    alpha_k, K_k, Q_projected, r = sp.symbols("alpha_k K_k Q_projected r", positive=True, real=True)

    tail = alpha_k * Q_projected / (4*sp.pi*K_k*r)

    print("Massless exterior monopole tail:")
    print()
    print("  kappa_ext ~ alpha_k Q_projected/(4*pi K_k r)")
    print()
    print(f"kappa_ext = {tail}")
    print()
    print("If the projection identity enforces:")
    print()
    print("  Q_projected = 0")
    print()
    print("then the exterior monopole tail is removed.")

    status_line("projection removes exterior monopole tail",
                "CONSTRAINED_BY_IDENTITY",
                "higher multipoles/boundary layers not solved")


def case_5_constraint_not_local_law():
    header("Case 5: Constraint, not ordinary local law")

    print("The projection:")
    print()
    print("  P_0 S = S - <S>_V")
    print()
    print("is nonlocal over V.")
    print()
    print("Therefore it should be interpreted as:")
    print()
    print("  a constraint projection")
    print("  or a boundary/matching identity")
    print("  or a consequence of a parent conservation law")
    print()
    print("not as:")
    print()
    print("  an ordinary local scalar source")
    print()
    print("This supports kappa as constrained/non-propagating trace response.")

    status_line("projection is nonlocal and constraint-like",
                "CONSTRAINED_BY_IDENTITY",
                "parent derivation missing")


def case_6_possible_parent_forms():
    header("Case 6: Possible parent identity forms")

    print("Possible parent forms to investigate:")
    print()
    print("1. Zero exterior kappa charge:")
    print("   Q_kappa = integral_V S_kappa d^3x = 0")
    print()
    print("2. Trace balance constraint:")
    print("   accumulation of trace exchange is locally redistributed so net exterior")
    print("   scalar charge vanishes.")
    print()
    print("3. Boundary flux cancellation:")
    print("   F_kappa(R+) = 4*pi R^2 kappa'(R+) = 0")
    print()
    print("4. Projected source equation:")
    print("   L_kappa kappa = alpha_k P_0 S_trace")
    print()
    print("5. Gauge/constraint split:")
    print("   kappa = kappa_phys_constrained + kappa_gauge")
    print()
    print("None is derived yet.")

    status_line("candidate parent identity forms listed",
                "MISSING",
                "must be derived or demoted to formal constraint")


def case_7_schematic_projected_equation():
    header("Case 7: Schematic projected kappa equation")

    print("Candidate constrained equation:")
    print()
    print("  -K_k Delta kappa = alpha_k P_0 S_trace")
    print()
    print("with:")
    print()
    print("  integral P_0 S_trace d^3x = 0")
    print()
    print("Exterior condition:")
    print()
    print("  kappa_ext monopole = 0")
    print()
    print("If additionally boundary/higher multipoles vanish or are confined:")
    print()
    print("  kappa_ext = 0")
    print()
    print("Status:")
    print("  structural candidate only")

    status_line("schematic projected kappa equation stated",
                "CONSTRAINED_BY_IDENTITY",
                "not a final law")


def case_8_failure_controls():
    header("Case 8: Failure controls")

    print("The projection identity fails if:")
    print()
    print("1. support V is arbitrary or observer-dependent.")
    print("2. subtraction is inserted only to kill an unwanted tail.")
    print("3. higher multipoles leak into exterior.")
    print("4. projection violates local energy/source accounting.")
    print("5. no parent identity enforces Q_kappa = 0.")
    print("6. kappa remains gauge-only but is treated as physical.")

    status_line("projection identity failure controls stated",
                "RISK",
                "parent derivation required")


def case_9_next_tests():
    header("Case 9: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_kappa_scalar_radiation_leak_check.py")
    print("   Check whether projected kappa remains non-radiative dynamically.")
    print()
    print("2. candidate_kappa_boundary_flux_cancellation.py")
    print("   Test exterior flux cancellation at the matter boundary.")
    print()
    print("3. candidate_kappa_projection_parent_balance.py")
    print("   Try to connect P_0 to vacuum-substance continuity balance.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_kappa_scalar_radiation_leak_check.py")
    print()
    print("Reason:")
    print("  Projection removes monopole leakage, but scalar radiation safety is still")
    print("  the next hard dynamical check.")

    status_line("next test selected",
                "CONSTRAINED_BY_IDENTITY",
                "scalar-radiation leak check is next")


def final_interpretation():
    header("Final interpretation")

    print("The zero-charge projection:")
    print()
    print("  P_0 S = S - <S>")
    print()
    print("works algebraically:")
    print()
    print("  integral P_0 S d^3x = 0")
    print()
    print("and removes the massless exterior monopole tail.")
    print()
    print("But it is nonlocal over the support and must be interpreted as a")
    print("constraint/projection identity, not an ordinary local source law.")
    print()
    print("Possible next artifact:")
    print("  candidate_kappa_constraint_projection_identity.md")
    print()
    print("Possible next script:")
    print("  candidate_kappa_scalar_radiation_leak_check.py")


def main():
    header("Candidate Kappa Constraint Projection Identity")
    case_0_problem_statement()
    case_1_define_projection_operator()
    case_2_toy_profile_projection()
    case_3_projector_idempotence()
    case_4_exterior_tail_control()
    case_5_constraint_not_local_law()
    case_6_possible_parent_forms()
    case_7_schematic_projected_equation()
    case_8_failure_controls()
    case_9_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
