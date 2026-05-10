# Group:
#   10_kappa_trace_response
#
# Script type:
#   INVENTORY
#
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

from dataclasses import dataclass
from pathlib import Path
from typing import List
import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    BranchDecisionRecord,
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    RecordKind,
    ReasonCode,
    ScriptOutput,
    StatusMark,
)


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


@dataclass
class KappaDynamicsOption:
    name: str
    equation_type: str
    status: str
    radiation_behavior: str
    risk: str


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="kappa_constraint_projection_identity_marker",
        upstream_script_id="10_kappa_trace_response__candidate_kappa_constraint_projection_identity",
        upstream_derivation_id="kappa_constraint_projection_identity_marker",
    )
    return archive, ns, invalidated


def print_archive_status(ns, invalidated: bool) -> None:
    if invalidated:
        print("[INFO] Archive invalidated due to source change.")
    checks = ns.verify_dependencies()
    if not checks:
        print("[INFO] Archive dependencies: none declared.")
        return
    print("[INFO] Archive dependency check:")
    for check in checks:
        print(f"  - {check.dependency.dependency_id}: {check.status} ({check.message})")


def print_option(o: KappaDynamicsOption) -> None:
    print()
    print("-" * 100)
    print(o.name)
    print("-" * 100)
    print(f"Status: {o.status}")
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

    return dispersion


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

    return dispersion


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

    return kappa_t


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
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement()
    options = build_options()
    case_1_option_inventory(options)
    dispersion_massless = case_2_massless_wave_hazard()
    case_3_elliptic_constraint_safety()
    dispersion_massive = case_4_massive_dispersion()
    kappa_t = case_5_relaxation_safety()
    case_6_projected_time_dependent_source_warning()
    case_7_classification(options)
    case_8_failure_controls()
    case_9_next_tests()
    final_interpretation()

    ns.record_derivation(
        derivation_id="kappa_scalar_radiation_leak_check_marker",
        inputs=[],
        output=sp.Symbol("kappa_scalar_radiation_leak_options_classified"),
        method="kappa_scalar_radiation_leak_check_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_hyperbolic_massless_kappa_wave_branch",
        script_id=SCRIPT_ID,
        branch_id="hyperbolic_massless_kappa_wave",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        reason_code=ReasonCode.MISSING_BOUNDARY_NEUTRALITY_THEOREM,
        obligation_ids=["derive_kappa_parent_constraint_projection_in_10_kappa_trace"],
        description=(
            "A massless hyperbolic kappa (Box kappa = source) allows scalar radiation "
            "even with zero monopole charge. This branch is deferred: it is not accepted "
            "as a safe kappa dynamics option pending derivation of a suppression mechanism."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_kappa_dynamic_scalar_radiation_safety_in_10_kappa_trace",
        script_id=SCRIPT_ID,
        title="Derive dynamical scalar radiation safety for kappa",
        status=ObligationStatus.OPEN,
        description=(
            "Static zero-monopole charge is not sufficient. A time-dependent kappa "
            "equation must be shown to be non-radiative dynamically. This requires "
            "either elliptic/constrained dynamics, a relaxation law with energy accounting, "
            "or a massive suppression with derived scale m_k."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="kappa_safe_dynamics_must_be_non_wave",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "Safe kappa dynamics must be elliptic/constrained, relaxational/non-wave, "
            "or massive/restoring with derived scale. Ordinary massless hyperbolic kappa "
            "introduces a scalar breathing wave channel incompatible with current requirements."
        ),
    ))

    with out.governance_assessments():
        out.line("massless hyperbolic kappa", StatusMark.FAIL, "deferred - creates breathing wave channel")
        out.line("elliptic constrained kappa", StatusMark.DEFER, "safe structurally, parent identity missing")
        out.line("relaxational kappa", StatusMark.DEFER, "plausible, energy accounting missing")
        out.line("dynamic scalar radiation safety", StatusMark.OBLIGATION, "not yet proven")

    with out.unresolved_obligations():
        out.line("derive dynamical scalar radiation safety", StatusMark.OBLIGATION, "open")

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
