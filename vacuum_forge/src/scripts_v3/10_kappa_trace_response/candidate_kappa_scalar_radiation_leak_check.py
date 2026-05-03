# Candidate kappa scalar radiation leak check
#
# Purpose
# -------
# The kappa constraint projection identity found:
#
#   P_0 S = S - <S>
#   integral P_0 S d^3x = 0
#
# This removes the massless exterior monopole tail.
#
# But removing the static exterior monopole is not enough.
#
# This script asks whether kappa can still behave as a propagating scalar
# radiation channel.
#
# It tests four interpretations:
#
#   1. elliptic constrained kappa,
#   2. hyperbolic massless kappa,
#   3. massive/restoring kappa,
#   4. relaxational non-wave kappa.
#
# Goal:
#
#   preserve interior trace response and exterior kappa=0
#   without introducing a long-range scalar gravitational wave.
#
# This is a classification/control script, not a final dynamical derivation.
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/10_kappa_trace_response/
#   or:
#   scripts_v3/candidate_kappa_scalar_radiation_leak_check.py

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
class KappaDynamicsOption:
    name: str
    equation_type: str
    status: str
    radiation_behavior: str
    risk: str


def print_option(o: KappaDynamicsOption) -> None:
    print()
    print("-" * 100)
    print(o.name)
    print("-" * 100)
    status_line(o.name, o.status)
    print(f"Equation type: {o.equation_type}")
    print(f"Radiation behavior: {o.radiation_behavior}")
    print(f"Risk: {o.risk}")


def case_0_problem_statement():
    header("Case 0: Kappa scalar-radiation leak problem")

    print("Question:")
    print()
    print("  Does kappa create a scalar radiation channel even if its static")
    print("  exterior monopole charge is projected away?")
    print()
    print("Required:")
    print()
    print("  interior trace response allowed")
    print("  exterior kappa = 0")
    print("  no ordinary long-range scalar radiation")
    print()
    print("Danger:")
    print()
    print("  a hyperbolic kappa equation would introduce breathing/trace waves.")

    status_line("scalar radiation leak problem posed", "CONSTRAINED_BY_IDENTITY")


def build_options() -> List[KappaDynamicsOption]:
    return [
        KappaDynamicsOption(
            name="D1: Elliptic constrained kappa",
            equation_type="L_kappa kappa = alpha P_0 S_trace with no independent time evolution",
            status="CONSTRAINED_BY_IDENTITY",
            radiation_behavior="No independent propagating scalar wave by construction.",
            risk="Requires parent constraint identity and consistent time-dependent support/projection.",
        ),
        KappaDynamicsOption(
            name="D2: Hyperbolic massless kappa",
            equation_type="Box kappa = alpha P_0 S_trace",
            status="REJECTED",
            radiation_behavior="Allows massless scalar radiation even when monopole charge is zero.",
            risk="Introduces breathing/trace gravitational wave channel.",
        ),
        KappaDynamicsOption(
            name="D3: Massive/restoring kappa",
            equation_type="(Box - m_k^2) kappa = alpha P_0 S_trace or (-Delta + m_k^2) kappa = source",
            status="PLAUSIBLE",
            radiation_behavior="Suppresses long-range radiation if massive or non-propagating in relevant regime.",
            risk="Introduces scale m_k and possible massive scalar mode.",
        ),
        KappaDynamicsOption(
            name="D4: Relaxational kappa",
            equation_type="dot kappa = -Gamma_k kappa + source/projection",
            status="PLAUSIBLE",
            radiation_behavior="Non-wave relaxation can absorb trace perturbations back to vacuum minimum.",
            risk="Needs energy accounting and must not erase static A_constraint.",
        ),
    ]


def case_1_option_inventory(options: List[KappaDynamicsOption]):
    header("Case 1: Kappa dynamics options")
    for o in options:
        print_option(o)


def case_2_massless_wave_hazard():
    header("Case 2: Massless hyperbolic wave hazard")

    omega, c, k = sp.symbols("omega c k", positive=True, real=True)

    dispersion = sp.Eq(omega**2, c**2*k**2)

    print("For a massless scalar wave equation:")
    print()
    print("  Box kappa = 0")
    print()
    print("plane-wave modes obey:")
    print()
    print(dispersion)
    print()
    print("Even if the monopole source is projected out, time-dependent trace")
    print("structure can excite propagating scalar modes.")
    print()
    print("This is not acceptable as an ordinary long-range gravity wave channel.")

    status_line("massless hyperbolic kappa allows scalar radiation", "REJECTED",
                "would create breathing/trace mode")


def case_3_elliptic_constraint_safety():
    header("Case 3: Elliptic constraint safety")

    print("If kappa is elliptic/constrained:")
    print()
    print("  L_kappa kappa = alpha_k P_0 S_trace")
    print()
    print("with no independent second time derivative:")
    print()
    print("  no Box kappa term")
    print()
    print("then kappa is determined instantaneously/constraint-wise by source and")
    print("boundary/projection data.")
    print()
    print("This avoids an independent scalar radiation channel.")
    print()
    print("But it requires a parent constraint identity to be legitimate.")

    status_line("elliptic constrained kappa is radiation-safe structurally",
                "CONSTRAINED_BY_IDENTITY",
                "parent identity missing")


def case_4_massive_dispersion():
    header("Case 4: Massive/restoring dispersion")

    omega, c, k, m = sp.symbols("omega c k m", positive=True, real=True)

    dispersion = sp.Eq(omega**2, c**2*k**2 + m**2)

    print("A massive/restoring scalar mode would have schematic dispersion:")
    print()
    print(dispersion)
    print()
    print("This suppresses long-range low-frequency propagation if m is large enough")
    print("or if kappa is not freely radiative.")
    print()
    print("But it still introduces a scalar mode unless the dynamics are constrained")
    print("or strongly damped.")

    status_line("massive/restoring kappa may suppress but not eliminate scalar mode",
                "PLAUSIBLE",
                "m_k and dynamics not derived")


def case_5_relaxation_safety():
    header("Case 5: Relaxation safety")

    t, Gamma, k0 = sp.symbols("t Gamma kappa_0", positive=True, real=True)

    kappa_t = k0 * sp.exp(-Gamma*t)

    print("Relaxational trace deviation:")
    print()
    print("  dot kappa = -Gamma kappa")
    print()
    print("solution:")
    print()
    print(f"kappa(t) = {kappa_t}")
    print()
    print("This absorbs scalar trace perturbations rather than propagating them.")
    print()
    print("But relaxation requires energy accounting and a source/restoring basis.")

    status_line("relaxation can absorb kappa perturbations", "PLAUSIBLE",
                "energy accounting missing")


def case_6_projected_time_dependent_source_warning():
    header("Case 6: Time-dependent projection warning")

    print("Projection:")
    print()
    print("  P_0 S = S - <S>_support")
    print()
    print("For time-dependent sources:")
    print()
    print("  support V(t)")
    print("  average <S(t)>")
    print("  moving boundary terms")
    print()
    print("can introduce extra terms.")
    print()
    print("Therefore scalar-radiation safety requires more than static zero charge.")
    print()
    print("Need:")
    print()
    print("  time-dependent constraint propagation")
    print("  boundary flux cancellation")
    print("  or relaxation law with energy accounting")

    status_line("time-dependent projection may create extra terms", "RISK",
                "dynamic support/projection not solved")


def case_7_classification(options: List[KappaDynamicsOption]):
    header("Case 7: Classification")

    print("| Dynamics option | Status |")
    print("|---|---|")
    for o in options:
        print(f"| {o.name} | {o.status} |")

    print()
    print("Current best dynamical policy:")
    print()
    print("  kappa should be elliptic/constrained or relaxational, not massless hyperbolic.")
    print()
    print("Rejected:")
    print()
    print("  ordinary massless scalar wave kappa.")
    print()
    print("Open:")
    print()
    print("  parent constraint propagation")
    print("  relaxation energy accounting")
    print("  massive scalar scale if used")

    status_line("scalar radiation leak classification produced",
                "CONSTRAINED_BY_IDENTITY",
                "safe path is constrained/non-wave kappa")


def case_8_failure_controls():
    header("Case 8: Failure controls")

    print("Kappa scalar-radiation safety fails if:")
    print()
    print("1. Box kappa appears as an ordinary massless wave equation.")
    print("2. time-dependent projected sources radiate trace waves.")
    print("3. relaxation violates energy/source accounting.")
    print("4. massive kappa introduces an observable fifth/scalar mode unintentionally.")
    print("5. projection is static only and does not propagate consistently.")
    print("6. kappa suppression erases the static A constraint.")

    status_line("scalar-radiation failure controls stated", "RISK",
                "dynamic safety not yet proven")


def case_9_next_tests():
    header("Case 9: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_kappa_boundary_flux_cancellation.py")
    print("   Test exterior flux cancellation at the moving/static boundary.")
    print()
    print("2. candidate_kappa_projection_parent_balance.py")
    print("   Connect P_0 to vacuum-substance continuity balance.")
    print()
    print("3. candidate_kappa_relaxation_energy_accounting.py")
    print("   Test whether relaxation can be energy-consistent.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_kappa_boundary_flux_cancellation.py")
    print()
    print("Reason:")
    print("  Static projection removes monopole charge; next check is boundary flux.")

    status_line("next test selected", "CONSTRAINED_BY_IDENTITY",
                "boundary flux cancellation is next")


def final_interpretation():
    header("Final interpretation")

    print("Projection removes static monopole leakage, but not automatically scalar")
    print("radiation.")
    print()
    print("Safe kappa policies:")
    print()
    print("  elliptic/constrained")
    print("  relaxational/non-wave")
    print("  massive/restoring only if derived and controlled")
    print()
    print("Rejected:")
    print()
    print("  ordinary massless hyperbolic kappa")
    print()
    print("Possible next artifact:")
    print("  candidate_kappa_scalar_radiation_leak_check.md")
    print()
    print("Possible next script:")
    print("  candidate_kappa_boundary_flux_cancellation.py")


def main():
    header("Candidate Kappa Scalar Radiation Leak Check")
    case_0_problem_statement()
    options = build_options()
    case_1_option_inventory(options)
    case_2_massless_wave_hazard()
    case_3_elliptic_constraint_safety()
    case_4_massive_dispersion()
    case_5_relaxation_safety()
    case_6_projected_time_dependent_source_warning()
    case_7_classification(options)
    case_8_failure_controls()
    case_9_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
