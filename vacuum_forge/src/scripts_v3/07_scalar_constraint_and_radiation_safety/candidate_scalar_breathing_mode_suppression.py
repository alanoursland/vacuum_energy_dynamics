# Candidate scalar breathing mode suppression
#
# Group:
#   07_scalar_constraint_and_radiation_safety
#
# Script type:
#   INVENTORY
#
# Purpose
# -------
# The scalar constraint mechanism showed:
#
#   safe:      Delta A = 8*pi*G*rho/c^2
#   dangerous: Box A = source
#
# If A has a radiative component, it can produce scalar breathing modes. Those
# modes are non-TT and would be an extra polarization/radiation channel.
#
# This script classifies possible suppression mechanisms:
#
#   1. constraint projection: A_rad = 0
#   2. mass gap / short range: Box a + m_A^2 a = source
#   3. damping / absorption: Box a + gamma a_t + m_A^2 a = source
#   4. relaxation to vacuum minimum: da/dtau = -Gamma dE/da
#   5. weak coupling: scalar source coupling epsilon_s is small
#
# The user's vacuum-absorption intuition is represented by mechanisms 3 and 4:
#
#   scalar perturbations may be generated locally but relax back into the
#   vacuum minimum before surviving as long-range radiation.
#
# This is not an observational bound calculation and not a proof. It is a
# mechanism inventory / algebraic safety test.

from pathlib import Path

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
    RouteRecord,
    ScriptOutput,
    StatusMark,
)


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"


# =============================================================================
# Utilities
# =============================================================================

def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="scalar_constraint_architecture_marker",
        upstream_script_id="07_scalar_constraint_and_radiation_safety__candidate_scalar_constraint_mechanism",
        upstream_derivation_id="scalar_constraint_architecture_marker",
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


# =============================================================================
# Case 0: Problem statement
# =============================================================================

def case_0_problem_statement():
    header("Case 0: Scalar breathing suppression problem")

    print("Problem:")
    print()
    print("  A is needed for scalar/static mass response.")
    print("  But radiative A modes can produce non-TT scalar breathing waves.")
    print()
    print("Goal:")
    print()
    print("  Identify mechanisms that make scalar breathing absent, short-ranged,")
    print("  damped, absorbed, relaxed, or weakly coupled.")
    print()
    print("Preferred architecture:")
    print()
    print("  A        -> scalar constraint/static channel")
    print("  h_ij^TT -> tensor radiation channel")


# =============================================================================
# Case 1: Constraint projection
# =============================================================================

def case_1_constraint_projection():
    header("Case 1: Constraint projection A_rad = 0")

    A_constraint, A_rad = sp.symbols("A_constraint A_rad", real=True)

    A_total = A_constraint + A_rad
    A_safe = A_total.subs(A_rad, 0)

    print("Split:")
    print("  A = A_constraint + A_rad")
    print()
    print(f"A_total = {A_total}")
    print(f"constraint projection A_rad=0 gives A = {A_safe}")
    print()
    print("Interpretation:")
    print("  The cleanest mechanism is that A has no independent radiative mode.")

    return A_total, A_safe, A_constraint


# =============================================================================
# Case 2: Massive scalar suppression
# =============================================================================

def case_2_massive_suppression():
    header("Case 2: Massive / short-range scalar suppression")

    k, omega, c, m = sp.symbols("k omega c m", positive=True, real=True)

    # Massive scalar dispersion in units where m has inverse-length dimension:
    # omega^2/c^2 = k^2 + m^2
    dispersion = sp.Eq(omega**2/c**2, k**2 + m**2)

    print("Massive scalar mode dispersion:")
    print(f"  {dispersion}")
    print()
    print("Static Green behavior:")
    print("  a(r) ~ exp(-m r)/r")
    print()
    print("If m is large, scalar breathing is short-ranged and suppressed far away.")

    return dispersion


# =============================================================================
# Case 3: Damping / absorption
# =============================================================================

def case_3_damping_absorption():
    header("Case 3: Damping / vacuum absorption")

    t, gamma, omega0, a0 = sp.symbols("t gamma omega0 a0", positive=True, real=True)

    # Underdamped schematic amplitude envelope.
    a = a0 * sp.exp(-gamma*t/2) * sp.cos(omega0*t)

    envelope = a0 * sp.exp(-gamma*t/2)

    print("Candidate damped scalar perturbation:")
    print(f"a(t) = {a}")
    print(f"envelope = {envelope}")
    print()
    print("Interpretation:")
    print("  Scalar perturbations may be generated locally but damp back into the")
    print("  vacuum minimum instead of surviving as long-range radiation.")

    return a, envelope, t, gamma


# =============================================================================
# Case 4: Relaxation to vacuum minimum
# =============================================================================

def case_4_relaxation_minimum():
    header("Case 4: Relaxation to vacuum minimum")

    tau, Gamma, mu, a0 = sp.symbols("tau Gamma mu a0", positive=True, real=True)
    a = sp.Function("a")(tau)

    E = sp.Rational(1, 2) * mu**2 * a**2
    gradE = sp.diff(E, a)

    # Relaxation equation da/dtau = -Gamma mu^2 a.
    solution = a0 * sp.exp(-Gamma*mu**2*tau)

    print("Vacuum minimum energy:")
    print(f"E(a) = {E}")
    print(f"dE/da = {gradE}")
    print()
    print("Relaxation law:")
    print("  da/dtau = -Gamma dE/da = -Gamma mu^2 a")
    print()
    print(f"solution = {solution}")

    return E, gradE, solution, tau, Gamma, mu, a0


# =============================================================================
# Case 5: Weak scalar coupling
# =============================================================================

def case_5_weak_coupling():
    header("Case 5: Weak scalar coupling")

    eps_s, S, K = sp.symbols("epsilon_s S K", positive=True, real=True)

    amplitude = sp.simplify(eps_s*S/K)
    power_proxy = sp.simplify(amplitude**2)

    print("Scalar source coupling:")
    print("  source strength ~ epsilon_s S")
    print()
    print(f"amplitude proxy = {amplitude}")
    print(f"power proxy = {power_proxy}")
    print()
    print("If epsilon_s is small, scalar radiation is weak.")
    print("This is less clean than constraint projection and requires bounds.")

    return amplitude, power_proxy


# =============================================================================
# Case 6: Tensor radiation remains unsuppressed
# =============================================================================

def case_6_tensor_channel_preserved():
    header("Case 6: Tensor radiation channel remains active")

    Q0, Omega = sp.symbols("Q0 Omega", positive=True, real=True)

    tensor_power_proxy = 64*Omega**6*Q0**2

    print("Tensor quadrupole power proxy:")
    print(f"Qdddot² proxy = {tensor_power_proxy}")
    print()
    print("Suppression mechanisms should target scalar breathing modes,")
    print("not the h_ij^TT tensor channel.")

    return tensor_power_proxy


# =============================================================================
# Case 7: Mechanism classification table
# =============================================================================

def case_7_classification_table():
    header("Case 7: Mechanism classification")

    print("| Mechanism | Scalar radiation status | Risk |")
    print("|---|---|---|")
    print("| constraint projection | absent | cleanest but must be derived |")
    print("| mass gap | short-ranged | must preserve static A response |")
    print("| damping / absorption | decays in time | must not damp static gravity |")
    print("| relaxation to minimum | returns to vacuum minimum | needs dynamical law |")
    print("| weak coupling | small but nonzero | needs observational bounds |")
    print("| unsuppressed scalar wave | present | dangerous |")


# =============================================================================
# Case 8: Classification
# =============================================================================

def case_8_results():
    header("Case 8: Results")

    print("Results:")
    print()
    print("1. Constraint projection removes A_rad directly.")
    print("2. A mass gap makes scalar waves short-ranged.")
    print("3. Damping/absorption can make scalar perturbations decay.")
    print("4. Relaxation can return scalar perturbations to the vacuum minimum.")
    print("5. Weak coupling can reduce scalar radiation but needs bounds.")
    print("6. Tensor h_ij^TT radiation should remain active.")
    print("7. The best current target is constraint-like A plus tensor radiation.")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("Scalar breathing modes are not automatically fatal if the theory supplies")
    print("a suppression mechanism.")
    print()
    print("The cleanest option remains:")
    print()
    print("  A_rad = 0")
    print("  A is constraint-like")
    print()
    print("A plausible fallback is vacuum absorption/relaxation:")
    print()
    print("  scalar perturbations are generated locally but damp or relax back into")
    print("  the vacuum minimum before becoming long-range observable radiation.")
    print()
    print("Any such mechanism must preserve static A gravity.")
    print()
    print("Possible next artifact:")
    print("  candidate_scalar_breathing_mode_suppression.md")
    print()
    print("Possible next script:")
    print("  candidate_binary_scalar_radiation_guardrail.py")


def main():
    header("Candidate Scalar Breathing Mode Suppression")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement()
    A_total, A_safe, A_constraint = case_1_constraint_projection()
    dispersion = case_2_massive_suppression()
    a_damped, envelope, t_sym, gamma_sym = case_3_damping_absorption()
    E_relax, gradE, solution_relax, tau_sym, Gamma_sym, mu_sym, a0_sym = case_4_relaxation_minimum()
    amplitude_wk, power_proxy_wk = case_5_weak_coupling()
    tensor_power = case_6_tensor_channel_preserved()
    case_7_classification_table()
    case_8_results()
    final_interpretation()

    # --- Derived results ---

    # Case 1: constraint projection algebraic check
    ns.record_derivation(
        derivation_id="constraint_projection_removes_A_rad",
        inputs=[A_total],
        output=A_safe,
        method="symbolic substitution A_rad = 0 in A = A_constraint + A_rad",
        status=Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
        result_type="constraint_projection",
        scope="algebraic identity, not physical derivation of mechanism",
    )

    # Case 3: damping envelope diagnostic
    ns.record_derivation(
        derivation_id="scalar_damping_envelope_decay",
        inputs=[a_damped],
        output=envelope,
        method="underdamped amplitude envelope a0 * exp(-gamma*t/2)",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="decay_envelope",
    )

    # Case 4: relaxation gradient
    ns.record_derivation(
        derivation_id="vacuum_relaxation_gradient_sample",
        inputs=[E_relax],
        output=gradE,
        method="dE/da for E = (1/2) mu^2 a^2; relaxation law da/dtau = -Gamma mu^2 a",
        status=Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
        result_type="relaxation_gradient",
        scope="quadratic potential toy only",
    )

    # --- Routes for each suppression mechanism ---

    ns.record_route(RouteRecord(
        route_id="constraint_projection_suppression_route",
        script_id=SCRIPT_ID,
        name="Constraint projection: A_rad = 0",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=["derive_constraint_projection_mechanism"],
        activation_conditions=[
            "A has no independent radiative mode",
            "A_rad is projected out by construction",
        ],
    ))

    ns.record_route(RouteRecord(
        route_id="vacuum_absorption_relaxation_route",
        script_id=SCRIPT_ID,
        name="Vacuum absorption / relaxation route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=["derive_vacuum_absorption_dynamical_law"],
        activation_conditions=[
            "scalar perturbations are generated locally",
            "perturbations relax back to vacuum minimum before becoming long-range radiation",
            "static A gravity is preserved",
        ],
    ))

    ns.record_route(RouteRecord(
        route_id="mass_gap_suppression_route",
        script_id=SCRIPT_ID,
        name="Mass gap / short-range scalar suppression route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=["derive_mass_gap_compatible_with_static_A"],
        activation_conditions=[
            "A_rad has a mass gap m > 0",
            "scalar breathing is short-ranged ~ exp(-m r)/r",
            "A_constraint long-range response is preserved",
        ],
    ))

    # --- Governance claims ---

    ns.record_claim(ClaimRecord(
        claim_id="scalar_breathing_suppression_required",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Any scalar breathing mode arising from A_rad must be absent, short-ranged, "
            "damped, absorbed, relaxed to the vacuum minimum, or weakly coupled with "
            "observational bounds. An unsuppressed massless scalar wave is not allowed."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="static_gravity_must_survive_suppression",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Any suppression mechanism applied to A_rad must preserve the static "
            "long-range A_constraint gravity. Suppression must not damp the static "
            "scalar mass response."
        ),
    ))

    # --- Proof obligations ---

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_constraint_projection_mechanism",
        script_id=SCRIPT_ID,
        title="Derive constraint projection mechanism for A_rad = 0",
        status=ObligationStatus.OPEN,
        description=(
            "Supply a geometric or structural derivation showing why A has no "
            "independent radiative mode. A_rad = 0 must follow from the parent "
            "structure rather than being imposed by hand."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_vacuum_absorption_dynamical_law",
        script_id=SCRIPT_ID,
        title="Derive vacuum absorption or relaxation dynamical law for scalar perturbations",
        status=ObligationStatus.OPEN,
        description=(
            "Show that scalar perturbations generated locally damp or relax to the "
            "vacuum minimum before becoming long-range radiation. Requires a dynamical "
            "law with clear timescale and a proof that static A gravity is unaffected."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_mass_gap_compatible_with_static_A",
        script_id=SCRIPT_ID,
        title="Derive mass gap for A_rad compatible with long-range static A_constraint",
        status=ObligationStatus.OPEN,
        description=(
            "Show that A_rad can have a mass gap m while A_constraint remains long-ranged. "
            "Requires explaining why the two components have different mass parameters."
        ),
    ))

    # Inventory marker
    ns.record_derivation(
        derivation_id="scalar_breathing_suppression_marker",
        inputs=[],
        output=sp.Symbol("scalar_breathing_control_required"),
        method="scalar_breathing_suppression_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )

    ns.write_run_metadata()

    with out.sample_results():
        out.line("constraint projection A_rad=0 algebraic check", StatusMark.PASS,
                 "A = A_constraint after substitution; mechanism not yet derived")
        out.line("relaxation gradient for quadratic potential", StatusMark.PASS,
                 "dE/da = mu^2 a; sample only")

    with out.governance_assessments():
        out.line("scalar breathing suppression required (policy)", StatusMark.PASS,
                 "any A_rad must be absent/short-ranged/damped/absorbed/weak")
        out.line("static gravity must survive suppression (policy)", StatusMark.PASS,
                 "A_constraint long-range response must be preserved")
        out.line("constraint projection route", StatusMark.PASS, "candidate route recorded")
        out.line("vacuum absorption/relaxation route", StatusMark.PASS, "candidate route recorded")
        out.line("mass gap route", StatusMark.PASS, "candidate route recorded")

    with out.unresolved_obligations():
        out.line("derive constraint projection mechanism", StatusMark.OBLIGATION,
                 "open proof obligation recorded")
        out.line("derive vacuum absorption dynamical law", StatusMark.OBLIGATION,
                 "open proof obligation recorded")
        out.line("derive mass gap compatible with static A", StatusMark.OBLIGATION,
                 "open proof obligation recorded")

    out.print_summary()


if __name__ == "__main__":
    main()
