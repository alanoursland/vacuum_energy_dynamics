# Candidate kappa exterior suppression condition
#
# Purpose
# -------
# The kappa source-law audit found:
#
#   kappa should not be a second density-sourced scalar potential.
#   best source family: pressure / spatial stress trace / trace-sector exchange.
#
# But the strongest reconstructed sector requires:
#
#   exterior kappa = 0
#
# because the static spherical exterior uses:
#
#   AB = exp(2 kappa)
#   kappa = 0
#   AB = 1
#   B = 1/A
#
# This script tests candidate mechanisms for exterior suppression:
#
#   1. boundary-only condition,
#   2. mass/restoring term,
#   3. constraint projection,
#   4. gauge fixing,
#   5. relaxation,
#   6. source support only inside matter.
#
# It does not derive the final kappa equation.
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/10_kappa_trace_response/
#   or:
#   scripts_v3/candidate_kappa_exterior_suppression_condition.py

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
class SuppressionMechanism:
    name: str
    mechanism: str
    status: str
    reason: str
    risk: str


def print_mechanism(m: SuppressionMechanism) -> None:
    print()
    print("-" * 100)
    print(m.name)
    print("-" * 100)
    status_line(m.name, m.status)
    print(f"Mechanism: {m.mechanism}")
    print(f"Reason: {m.reason}")
    print(f"Risk: {m.risk}")


def case_0_problem_statement():
    header("Case 0: Kappa exterior suppression problem")

    print("Required exterior condition:")
    print()
    print("  kappa -> 0 outside matter")
    print()
    print("Reason:")
    print()
    print("  static exterior reconstruction uses AB = 1 and B = 1/A")
    print()
    print("Question:")
    print()
    print("  What mechanism forces or permits kappa = 0 in exterior vacuum?")

    status_line("exterior suppression problem posed", "CONSTRAINED_BY_IDENTITY")


def case_1_exterior_relation():
    header("Case 1: Exterior relation to Schwarzschild reconstruction")

    A, B, kappa = sp.symbols("A B kappa", positive=True, real=True)

    relation = sp.Eq(A*B, sp.exp(2*kappa))
    exterior = relation.subs(kappa, 0)

    print("Reduced relation:")
    print()
    print(relation)
    print()
    print("Set kappa = 0:")
    print()
    print(exterior)
    print()
    print("Thus:")
    print()
    print("  AB = 1")
    print("  B = 1/A")
    print()
    print("This is required for the reconstructed static exterior.")

    status_line("exterior kappa=0 recovers reciprocal metric factor", "DERIVED_REDUCED")


def build_mechanisms() -> List[SuppressionMechanism]:
    return [
        SuppressionMechanism(
            name="S1: Boundary-only suppression",
            mechanism="S_trace = 0 outside and kappa(infinity)=0",
            status="PLAUSIBLE",
            reason=(
                "For a massless elliptic kappa equation, exterior vacuum plus boundary "
                "conditions may force kappa=0 if no boundary flux is supplied."
            ),
            risk=(
                "Boundary-only suppression may fail if interior matching induces a "
                "1/r kappa tail."
            ),
        ),
        SuppressionMechanism(
            name="S2: Massive/restoring suppression",
            mechanism="-K_k Delta kappa + m_k^2 kappa = alpha_k S_trace",
            status="PLAUSIBLE",
            reason=(
                "A restoring/mass term gives Yukawa-like decay outside matter and can "
                "drive kappa toward zero."
            ),
            risk=(
                "Introduces new scale m_k and may imply an extra scalar mode unless "
                "handled as constrained/relaxational."
            ),
        ),
        SuppressionMechanism(
            name="S3: Constraint projection",
            mechanism="kappa is not an independent exterior degree of freedom",
            status="CONSTRAINED_BY_IDENTITY",
            reason=(
                "This best protects the static exterior: kappa is allowed as an interior "
                "trace response but projected out in source-free exterior."
            ),
            risk=(
                "Requires a parent constraint identity; otherwise it is imposed by hand."
            ),
        ),
        SuppressionMechanism(
            name="S4: Gauge fixing",
            mechanism="exterior areal/static gauge sets kappa = 0",
            status="RISK",
            reason=(
                "Some kappa behavior may be gauge-volume artifact in areal/static reductions."
            ),
            risk=(
                "If kappa is only gauge, interior physical interpretation is weakened. "
                "If it is physical, gauge fixing cannot be the whole mechanism."
            ),
        ),
        SuppressionMechanism(
            name="S5: Relaxation to vacuum minimum",
            mechanism="dot kappa = -Gamma_kappa kappa or damped relaxation",
            status="PLAUSIBLE",
            reason=(
                "Vacuum relaxation can drive trace deviations back to kappa=0 after "
                "matter/source support disappears."
            ),
            risk=(
                "Relaxation law must not introduce propagating scalar radiation or erase "
                "static A_constraint."
            ),
        ),
        SuppressionMechanism(
            name="S6: Compact source support only",
            mechanism="S_trace has compact support inside matter",
            status="PLAUSIBLE",
            reason=(
                "Pressure/stress trace vanishes outside matter, so kappa source naturally "
                "turns off in exterior."
            ),
            risk=(
                "Source compactness alone does not prevent homogeneous exterior tails."
            ),
        ),
    ]


def case_2_print_mechanisms(mechanisms: List[SuppressionMechanism]):
    header("Case 2: Suppression mechanism inventory")
    for m in mechanisms:
        print_mechanism(m)


def case_3_massless_exterior_tail():
    header("Case 3: Massless exterior tail risk")

    r, C0, C1 = sp.symbols("r C0 C1", positive=True, real=True)

    kappa_ext = C0 + C1/r

    print("If exterior equation is massless elliptic:")
    print()
    print("  Delta_areal kappa = 0")
    print()
    print("then:")
    print()
    print(f"kappa_ext = {kappa_ext}")
    print()
    print("Boundary condition kappa(infinity)=0 sets C0 = 0.")
    print("But a 1/r tail remains unless C1 = 0.")
    print()
    print("Therefore boundary-only suppression requires no kappa flux at the surface.")

    status_line("massless exterior permits 1/r tail", "RISK",
                "must set exterior kappa charge/flux to zero")


def case_4_massive_exterior_decay():
    header("Case 4: Massive/restoring exterior decay")

    r, C, m = sp.symbols("r C m", positive=True, real=True)

    kappa_yukawa = C * sp.exp(-m*r) / r

    print("If exterior equation has restoring term:")
    print()
    print("  (-Delta + m_k^2) kappa = 0")
    print()
    print("then a decaying exterior solution is:")
    print()
    print(f"kappa_ext = {kappa_yukawa}")
    print()
    print("This suppresses long-range kappa tails.")
    print()
    print("But m_k is a new scale and must be derived or constrained.")

    status_line("massive/restoring term suppresses exterior tail", "PLAUSIBLE",
                "m_k not derived")


def case_5_constraint_projection_policy():
    header("Case 5: Constraint projection policy")

    print("Strongest exterior-safe policy:")
    print()
    print("  kappa is allowed as an interior trace response.")
    print("  kappa has no independent exterior charge.")
    print("  exterior vacuum projection sets kappa = 0.")
    print()
    print("Symbolically:")
    print()
    print("  S_trace = 0")
    print("  Q_kappa = integral S_trace d^3x = 0 for exterior monopole charge")
    print("  kappa_ext = 0")
    print()
    print("This is clean only if a parent identity enforces it.")

    status_line("constraint projection is exterior-safe", "CONSTRAINED_BY_IDENTITY",
                "parent identity missing")


def case_6_best_current_policy():
    header("Case 6: Best current suppression policy")

    print("Current best policy:")
    print()
    print("1. kappa source is not raw rho.")
    print("2. source family is pressure/spatial trace/trace exchange.")
    print("3. exterior source support vanishes in vacuum.")
    print("4. exterior homogeneous kappa charge must vanish.")
    print("5. suppression may be by constraint projection, restoring term, or both.")
    print("6. gauge contribution must be separated from physical trace response.")
    print()
    print("Most conservative exterior condition:")
    print()
    print("  kappa_ext = 0")
    print("  F_kappa_ext = 4*pi r^2 kappa' = 0")
    print()
    print("This prevents a long-range scalar trace field.")

    status_line("best current suppression policy stated", "CONSTRAINED_BY_IDENTITY",
                "mechanism not fully derived")


def case_7_classification(mechanisms: List[SuppressionMechanism]):
    header("Case 7: Classification table")

    print("| Mechanism | Status |")
    print("|---|---|")
    for m in mechanisms:
        print(f"| {m.name} | {m.status} |")

    print()
    print("Current preferred combination:")
    print()
    print("  compact trace source + zero exterior kappa charge/flux + constraint projection")
    print()
    print("Optional:")
    print()
    print("  massive/restoring suppression if derived")

    status_line("suppression classification produced", "CONSTRAINED_BY_IDENTITY",
                "exterior kappa=0 requires zero charge/flux or projection")


def case_8_failure_controls():
    header("Case 8: Failure controls")

    print("Exterior suppression fails if:")
    print()
    print("1. kappa has a 1/r exterior tail.")
    print("2. kappa is sourced by raw density and duplicates A.")
    print("3. restoring mass m_k is inserted only to hide scalar radiation.")
    print("4. gauge fixing is mistaken for physical suppression.")
    print("5. interior kappa matching creates nonzero exterior kappa flux.")
    print("6. parent identity does not explain why exterior kappa charge vanishes.")

    status_line("suppression failure controls stated", "RISK",
                "must preserve Schwarzschild exterior")


def case_9_next_tests():
    header("Case 9: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_kappa_pressure_trace_model.py")
    print("   Build a simple interior pressure/spatial-trace source model.")
    print()
    print("2. candidate_kappa_gauge_vs_physical_trace.py")
    print("   Separate gauge-volume artifact from physical trace response.")
    print()
    print("3. candidate_kappa_scalar_radiation_leak_check.py")
    print("   Check whether kappa source law leaks scalar radiation.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_kappa_pressure_trace_model.py")
    print()
    print("Reason:")
    print("  After exterior suppression, the next issue is the interior source.")

    status_line("next test selected", "CONSTRAINED_BY_IDENTITY",
                "interior pressure/trace model is next")


def final_interpretation():
    header("Final interpretation")

    print("Exterior kappa suppression is not automatic.")
    print()
    print("A massless exterior kappa equation permits:")
    print()
    print("  kappa = C1/r")
    print()
    print("unless exterior kappa charge/flux vanishes.")
    print()
    print("Best current policy:")
    print()
    print("  kappa is sourced by trace/pressure inside matter")
    print("  exterior source vanishes")
    print("  exterior kappa charge/flux vanishes")
    print("  kappa_ext = 0 by constraint/projection or derived restoring mechanism")
    print()
    print("Possible next artifact:")
    print("  candidate_kappa_exterior_suppression_condition.md")
    print()
    print("Possible next script:")
    print("  candidate_kappa_pressure_trace_model.py")


def main():
    header("Candidate Kappa Exterior Suppression Condition")
    case_0_problem_statement()
    case_1_exterior_relation()
    mechanisms = build_mechanisms()
    case_2_print_mechanisms(mechanisms)
    case_3_massless_exterior_tail()
    case_4_massive_exterior_decay()
    case_5_constraint_projection_policy()
    case_6_best_current_policy()
    case_7_classification(mechanisms)
    case_8_failure_controls()
    case_9_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
