# Candidate kappa gauge versus physical trace
#
# Purpose
# -------
# The compensated-trace test found:
#
#   S_comp = S_trace - <S_trace>
#
# removes the monopole kappa charge, but the subtraction is nonlocal over the
# support. That suggests kappa may be a constrained trace response rather than
# an ordinary local scalar.
#
# This script separates possible meanings of kappa:
#
#   1. gauge / coordinate-volume artifact,
#   2. physical trace / volume response,
#   3. constrained non-propagating trace response,
#   4. dangerous propagating scalar mode.
#
# It tests which interpretation is compatible with:
#
#   exterior kappa = 0,
#   interior trace response,
#   no raw density double-counting,
#   no scalar radiation leak,
#   no arbitrary nonlocal subtraction unless parent-constrained.
#
# This is a classification/control script, not a final derivation.
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/10_kappa_trace_response/
#   or:
#   scripts_v3/candidate_kappa_gauge_vs_physical_trace.py

from dataclasses import dataclass
from typing import List
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


@dataclass
class KappaInterpretation:
    name: str
    meaning: str
    status: str
    compatible_with: str
    risk: str


def print_interpretation(i: KappaInterpretation) -> None:
    print()
    print("-" * 100)
    print(i.name)
    print("-" * 100)
    status_line(i.name, i.status)
    print(f"Meaning: {i.meaning}")
    print(f"Compatible with: {i.compatible_with}")
    print(f"Risk: {i.risk}")


def case_0_problem_statement():
    header("Case 0: Kappa gauge-vs-physical trace problem")

    print("Question:")
    print()
    print("  Is kappa a physical trace response, a gauge-volume artifact,")
    print("  a constrained projection variable, or a dangerous scalar mode?")
    print()
    print("Known relation:")
    print()
    print("  AB = exp(2 kappa)")
    print()
    print("Known requirement:")
    print()
    print("  kappa_ext = 0")
    print()
    print("Known risk:")
    print()
    print("  ordinary scalar kappa dynamics can leak exterior 1/r tails or scalar radiation.")

    status_line("gauge-vs-physical problem posed", "CONSTRAINED_BY_IDENTITY")


def case_1_reduced_diagnostic():
    header("Case 1: Reduced diagnostic relation")

    A, B, kappa = sp.symbols("A B kappa", positive=True, real=True)

    relation = sp.Eq(A*B, sp.exp(2*kappa))
    kappa_expr = sp.Eq(kappa, sp.Rational(1, 2)*sp.log(A*B))

    print("Reduced relation:")
    print()
    print(relation)
    print()
    print("Equivalent diagnostic:")
    print()
    print(kappa_expr)
    print()
    print("This measures departure from reciprocal AB=1 structure.")
    print()
    print("It does not, by itself, decide whether kappa is physical or gauge.")

    status_line("kappa diagnostic relation stated", "DERIVED_REDUCED")


def build_interpretations() -> List[KappaInterpretation]:
    return [
        KappaInterpretation(
            name="I1: Pure gauge / coordinate-volume artifact",
            meaning="kappa measures coordinate or slicing/radial-volume choice rather than physical stress response",
            status="PLAUSIBLE",
            compatible_with=(
                "exterior kappa=0 by gauge fixing; avoids scalar radiation if no physical dynamics"
            ),
            risk=(
                "undermines using kappa as an interior physical response; may demote prior kappa interpretations"
            ),
        ),
        KappaInterpretation(
            name="I2: Physical local trace field",
            meaning="kappa is an ordinary scalar field sourced locally by trace/pressure",
            status="RISK",
            compatible_with=(
                "interior trace response"
            ),
            risk=(
                "generically produces exterior charge/tails or scalar radiation unless screened"
            ),
        ),
        KappaInterpretation(
            name="I3: Constrained non-propagating trace response",
            meaning="kappa is physical in matter but constrained/projected so it has no independent exterior charge",
            status="CONSTRAINED_BY_IDENTITY",
            compatible_with=(
                "interior response, exterior kappa=0, compensated trace, scalar-radiation safety"
            ),
            risk=(
                "requires parent constraint identity; otherwise compensation/projection is imposed by hand"
            ),
        ),
        KappaInterpretation(
            name="I4: Relaxational trace deviation",
            meaning="kappa is a deviation from vacuum minimum that relaxes back to zero outside sources",
            status="PLAUSIBLE",
            compatible_with=(
                "exterior suppression and vacuum absorption intuition"
            ),
            risk=(
                "needs dynamics that do not create observable scalar radiation or erase static A"
            ),
        ),
        KappaInterpretation(
            name="I5: Dangerous propagating scalar mode",
            meaning="kappa is an independent scalar wave/field with trace source",
            status="REJECTED",
            compatible_with=(
                "none of the current exterior/radiation safety requirements without extra suppression"
            ),
            risk=(
                "would introduce scalar gravity radiation and exterior tails"
            ),
        ),
    ]


def case_2_interpretation_inventory(items: List[KappaInterpretation]):
    header("Case 2: Interpretation inventory")
    for i in items:
        print_interpretation(i)


def case_3_gauge_artifact_test():
    header("Case 3: Gauge-artifact test")

    print("If kappa is pure gauge:")
    print()
    print("  exterior kappa=0 can be imposed by coordinate/gauge choice.")
    print("  no scalar radiation is introduced.")
    print("  AB=exp(2kappa) remains a diagnostic, not a physical field equation.")
    print()
    print("But then:")
    print()
    print("  interior kappa cannot be credited as a physical pressure/trace response")
    print("  unless gauge-invariant content is identified.")
    print()
    print("Conclusion:")
    print("  pure-gauge kappa is safe but weak.")

    status_line("pure gauge interpretation is exterior-safe but physically weak",
                "PLAUSIBLE",
                "needs gauge-invariant interior content")


def case_4_physical_local_scalar_test():
    header("Case 4: Physical local scalar test")

    print("If kappa is an ordinary local scalar with source:")
    print()
    print("  -K_k Delta kappa = alpha_k S_trace")
    print()
    print("and:")
    print()
    print("  integral S_trace d^3x != 0")
    print()
    print("then exterior kappa generically has:")
    print()
    print("  kappa_ext ~ 1/r")
    print()
    print("This violates exterior kappa=0 unless screened/projected.")
    print()
    print("Conclusion:")
    print("  ordinary local scalar kappa is dangerous.")

    status_line("local physical scalar kappa leaks without suppression", "RISK",
                "not acceptable as final unscreened interpretation")


def case_5_constrained_trace_test():
    header("Case 5: Constrained trace-response test")

    print("If kappa is a constrained trace response:")
    print()
    print("  it can respond inside matter")
    print("  it can use compensated or projected source")
    print("  it can have zero exterior charge/flux")
    print("  it need not propagate as an exterior scalar wave")
    print()
    print("This best matches current requirements:")
    print()
    print("  interior role")
    print("  exterior kappa=0")
    print("  no duplicate density scalar")
    print("  no scalar radiation leak")
    print()
    print("But a parent identity is required.")

    status_line("constrained trace response is current best interpretation",
                "CONSTRAINED_BY_IDENTITY",
                "parent identity missing")


def case_6_relaxational_test():
    header("Case 6: Relaxational trace-deviation test")

    print("If kappa is relaxational:")
    print()
    print("  dot kappa = -Gamma_kappa kappa + source")
    print()
    print("or:")
    print()
    print("  (-Delta + m_k^2) kappa = source")
    print()
    print("then exterior deviations can decay.")
    print()
    print("This fits the vacuum-minimum intuition.")
    print()
    print("But it introduces:")
    print()
    print("  new scale/rate")
    print("  possible scalar mode")
    print("  need for energy accounting")
    print()
    print("Conclusion:")
    print("  plausible as suppression mechanism, not source identity by itself.")

    status_line("relaxational kappa is plausible but incomplete",
                "PLAUSIBLE",
                "dynamics and energy accounting missing")


def case_7_status_table(items: List[KappaInterpretation]):
    header("Case 7: Status table")

    print("| Interpretation | Status |")
    print("|---|---|")
    for i in items:
        print(f"| {i.name} | {i.status} |")

    print()
    print("Current best interpretation:")
    print()
    print("  kappa is a constrained non-propagating trace response.")
    print()
    print("Secondary possibility:")
    print()
    print("  some part of kappa is gauge-volume diagnostic.")
    print()
    print("Rejected as final:")
    print()
    print("  ordinary unscreened propagating scalar kappa.")

    status_line("kappa interpretation classification produced",
                "CONSTRAINED_BY_IDENTITY",
                "parent constraint still missing")


def case_8_failure_controls():
    header("Case 8: Failure controls")

    print("The kappa interpretation fails if:")
    print()
    print("1. a gauge artifact is treated as physical without invariant content.")
    print("2. physical kappa creates a 1/r exterior tail.")
    print("3. physical kappa creates scalar radiation.")
    print("4. compensation is inserted without parent constraint.")
    print("5. relaxation hides the problem without energy/source accounting.")
    print("6. kappa duplicates the A-sector density response.")

    status_line("gauge-vs-physical failure controls stated",
                "RISK",
                "must protect exterior and scalar-radiation safety")


def case_9_next_tests():
    header("Case 9: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_kappa_constraint_projection_identity.py")
    print("   Try to formalize zero-charge projection as a parent constraint.")
    print()
    print("2. candidate_kappa_scalar_radiation_leak_check.py")
    print("   Check whether trace response leaks scalar radiation dynamically.")
    print()
    print("3. candidate_kappa_relaxation_energy_accounting.py")
    print("   Test whether relaxation can be energy-consistent.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_kappa_constraint_projection_identity.py")
    print()
    print("Reason:")
    print("  Current best interpretation is constrained trace response; the missing")
    print("  piece is the parent projection identity.")

    status_line("next test selected",
                "CONSTRAINED_BY_IDENTITY",
                "constraint projection identity is next")


def final_interpretation():
    header("Final interpretation")

    print("Current best kappa interpretation:")
    print()
    print("  constrained non-propagating trace response")
    print()
    print("not:")
    print()
    print("  ordinary local scalar field")
    print()
    print("and not merely:")
    print()
    print("  arbitrary gauge artifact")
    print()
    print("This interpretation can reconcile:")
    print()
    print("  interior trace response")
    print("  exterior kappa=0")
    print("  compensated zero-charge source")
    print("  scalar-radiation safety")
    print()
    print("But the parent projection identity is missing.")
    print()
    print("Possible next artifact:")
    print("  candidate_kappa_gauge_vs_physical_trace.md")
    print()
    print("Possible next script:")
    print("  candidate_kappa_constraint_projection_identity.py")


def main():
    header("Candidate Kappa Gauge Versus Physical Trace")
    case_0_problem_statement()
    case_1_reduced_diagnostic()
    items = build_interpretations()
    case_2_interpretation_inventory(items)
    case_3_gauge_artifact_test()
    case_4_physical_local_scalar_test()
    case_5_constrained_trace_test()
    case_6_relaxational_test()
    case_7_status_table(items)
    case_8_failure_controls()
    case_9_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
