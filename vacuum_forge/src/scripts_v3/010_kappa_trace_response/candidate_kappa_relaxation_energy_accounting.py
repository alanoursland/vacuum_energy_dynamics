# Group:
#   10_kappa_trace_response
#
# Script type:
#   DERIVATION
#
# Candidate kappa relaxation energy accounting
#
# Purpose
# -------
# Boundary-flux cancellation found:
#
#   preferred: no ordinary breathing radiation
#   rejected: persistent massless breathing radiation
#   possible fallback: damped / absorbed / critically damped trace response
#
# But damping cannot be used as a hand-wave.
#
# This script asks whether a relaxational kappa response can be interpreted as
# controlled energy dissipation into the vacuum minimum rather than as an ad hoc
# way to hide scalar radiation.
#
# It tests:
#
#   1. undamped oscillator: energy conserved, can radiate if coupled outward.
#   2. damped oscillator: energy decreases at a definite rate.
#   3. critical damping: no oscillatory far-field breathing if overdamped/critical.
#   4. relaxation sink: lost trace energy must enter a vacuum sink term.
#   5. static A constraint must remain unaffected.
#
# This is a control script, not a final derivation.

from pathlib import Path

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    RecordKind,
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


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="kappa_boundary_flux_cancellation_marker",
        upstream_script_id="010_kappa_trace_response__candidate_kappa_boundary_flux_cancellation",
        upstream_derivation_id="kappa_boundary_flux_cancellation_marker",
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


def case_0_problem_statement():
    header("Case 0: Kappa relaxation energy-accounting problem")

    print("Question:")
    print()
    print("  If a kappa breathing/trace response exists, can it be damped or")
    print("  absorbed consistently rather than becoming long-range scalar radiation?")
    print()
    print("Rule:")
    print()
    print("  damping is not allowed as a cosmetic fix.")
    print()
    print("It must correspond to:")
    print()
    print("  energy transfer into a vacuum sink / restoring minimum")
    print("  or a constrained non-wave relaxation law")
    print()
    print("Preferred outcome:")
    print()
    print("  no ordinary breathing radiation")


def case_1_undamped_oscillator_energy():
    header("Case 1: Undamped trace oscillator energy")

    kappa, v, omega0 = sp.symbols("kappa v omega_0", positive=True, real=True)

    E = sp.Rational(1, 2)*v**2 + sp.Rational(1, 2)*omega0**2*kappa**2

    print("Toy undamped trace oscillator:")
    print()
    print("  kappa_dot = v")
    print("  v_dot = -omega0^2 kappa")
    print()
    print("Energy:")
    print()
    print(f"E = {E}")
    print()
    print("This energy is conserved in the toy oscillator.")
    print("If coupled to exterior wave modes, it can support breathing radiation.")

    return kappa, v, omega0, E


def case_2_damped_energy_derivative():
    header("Case 2: Damped oscillator energy derivative")

    kappa, v, omega0, Gamma = sp.symbols("kappa v omega_0 Gamma", positive=True, real=True)

    E = sp.Rational(1, 2)*v**2 + sp.Rational(1, 2)*omega0**2*kappa**2

    # equation: kappa_dot = v, v_dot = -Gamma v - omega0^2 kappa
    dE_dt = sp.simplify(v*(-Gamma*v - omega0**2*kappa) + omega0**2*kappa*v)

    print("Damped trace oscillator:")
    print()
    print("  kappa_dot = v")
    print("  v_dot = -Gamma v - omega0^2 kappa")
    print()
    print("Energy:")
    print()
    print(f"E = {E}")
    print()
    print("Energy derivative:")
    print()
    print(f"dE/dt = {dE_dt}")
    print()
    print("For Gamma > 0:")
    print()
    print("  dE/dt <= 0")
    print()
    print("The lost energy must be accounted for as vacuum absorption/dissipation.")

    return kappa, v, omega0, Gamma, E, dE_dt


def case_3_critical_damping_condition():
    header("Case 3: Critical damping condition")

    Gamma, omega0 = sp.symbols("Gamma omega_0", positive=True, real=True)

    critical = sp.Eq(Gamma**2, 4*omega0**2)

    print("For toy equation:")
    print()
    print("  kappa_ddot + Gamma kappa_dot + omega0^2 kappa = 0")
    print()
    print("Critical damping condition:")
    print()
    print(critical)
    print()
    print("Regimes:")
    print()
    print("  Gamma^2 < 4 omega0^2  -> underdamped oscillatory trace response")
    print("  Gamma^2 = 4 omega0^2  -> critically damped")
    print("  Gamma^2 > 4 omega0^2  -> overdamped")
    print()
    print("Cleanest fallback if breathing is forced:")
    print()
    print("  critical/overdamped, not underdamped propagating.")

    return Gamma, omega0, critical


def case_4_relaxation_sink_balance():
    header("Case 4: Relaxation sink balance")

    Gamma, v = sp.symbols("Gamma v", positive=True, real=True)

    P_loss = Gamma*v**2

    print("Damping power lost from kappa oscillator:")
    print()
    print("  P_loss = Gamma kappa_dot^2")
    print()
    print(f"P_loss = {P_loss}")
    print()
    print("Vacuum balance must include a sink term:")
    print()
    print("  Gamma_relax = P_loss")
    print()
    print("or an equivalent positive-definite absorption term.")
    print()
    print("Without this, damping is just a hand-wave.")

    return P_loss


def case_5_static_A_constraint_guard():
    header("Case 5: Static A-constraint guard")

    print("Relaxation must not erase static scalar gravity.")
    print()
    print("Allowed:")
    print()
    print("  damp kappa trace/breathing deviations")
    print("  absorb scalar radiative trace perturbations")
    print()
    print("Not allowed:")
    print()
    print("  damp the static A_constraint mass field")
    print("  remove areal flux")
    print("  alter A = 1 - 2GM/(c^2 r)")
    print()
    print("Therefore relaxation must act on:")
    print()
    print("  kappa_rad / trace deviation")
    print()
    print("not on:")
    print()
    print("  A_constraint")


def case_6_safe_vs_unsafe_breathing():
    header("Case 6: Safe versus unsafe breathing")

    print("| Breathing/trace behavior | Status |")
    print("|---|---|")
    print("| no breathing mode | preferred / cleanest |")
    print("| constrained non-propagating trace response | acceptable if parent identity derived |")
    print("| critically damped local trace response | plausible fallback if energy-accounted |")
    print("| overdamped relaxation | plausible fallback if energy-accounted |")
    print("| underdamped but rapidly absorbed | risky, requires attenuation length |")
    print("| massless long-range breathing radiation | rejected |")
    print("| damping inserted only to hide scalar waves | rejected |")


def case_7_attenuation_length():
    header("Case 7: Attenuation length criterion")

    c, Gamma = sp.symbols("c Gamma", positive=True, real=True)

    L_att = sp.simplify(c/Gamma)

    print("For a disturbance moving at characteristic speed c with damping Gamma:")
    print()
    print("  attenuation length L_att ~ c/Gamma")
    print()
    print(f"L_att = {L_att}")
    print()
    print("To avoid long-range breathing radiation:")
    print()
    print("  L_att must be short compared with observational propagation scales")
    print()
    print("or the mode must be non-propagating/constrained.")
    print()
    print("This gives a future phenomenological bound if damping is used.")

    return c, Gamma, L_att


def case_8_classification():
    header("Case 8: Classification")

    print("| Item | Status |")
    print("|---|---|")
    print("| undamped kappa oscillator | RISK |")
    print("| damped oscillator energy loss | DERIVED_REDUCED |")
    print("| critical damping condition | CONSTRAINED_BY_IDENTITY |")
    print("| positive vacuum sink term | CONSTRAINED_BY_IDENTITY / MISSING ontology |")
    print("| A-sector preservation guard | CONSTRAINED_BY_IDENTITY |")
    print("| attenuation length criterion | PLAUSIBLE |")
    print("| final relaxation law | MISSING |")


def case_9_next_tests():
    header("Case 9: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_kappa_projection_parent_balance.py")
    print("   Connect P_0, F_kappa=0, and relaxation sink to vacuum-substance balance.")
    print()
    print("2. candidate_kappa_boundary_layer_model.py")
    print("   Model confined interior kappa with boundary layer and zero exterior flux.")
    print()
    print("3. candidate_kappa_trace_response_status_summary.py")
    print("   Summarize group 10 status if we are near the natural stopping point.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_kappa_projection_parent_balance.py")
    print()
    print("Reason:")
    print("  relaxation and projection both need the parent balance identity.")


def final_interpretation():
    header("Final interpretation")

    print("Breathing radiation remains disfavored.")
    print()
    print("If math forces a trace/breathing response, acceptable forms are:")
    print()
    print("  constrained non-wave")
    print("  critically damped")
    print("  overdamped")
    print("  strongly absorbed with short attenuation length")
    print()
    print("But damping requires:")
    print()
    print("  dE/dt = -Gamma kappa_dot^2")
    print("  positive vacuum sink/accounting")
    print("  preservation of static A_constraint")
    print()
    print("Possible next artifact:")
    print("  candidate_kappa_relaxation_energy_accounting.md")
    print()
    print("Possible next script:")
    print("  candidate_kappa_projection_parent_balance.py")


def main():
    header("Candidate Kappa Relaxation Energy Accounting")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement()
    kappa, v, omega0, E = case_1_undamped_oscillator_energy()
    kappa, v, omega0, Gamma, E_dmp, dE_dt = case_2_damped_energy_derivative()
    Gamma, omega0, critical = case_3_critical_damping_condition()
    P_loss = case_4_relaxation_sink_balance()
    case_5_static_A_constraint_guard()
    case_6_safe_vs_unsafe_breathing()
    c, Gamma2, L_att = case_7_attenuation_length()
    case_8_classification()
    case_9_next_tests()
    final_interpretation()

    # Real algebraic computation: dE/dt = -Gamma*v^2
    ns.record_derivation(
        derivation_id="damped_kappa_oscillator_energy_derivative",
        inputs=[E_dmp],
        output=dE_dt,
        method=(
            "compute d/dt[1/2 v^2 + 1/2 omega0^2 kappa^2] using "
            "kappa_dot=v, v_dot=-Gamma*v-omega0^2*kappa"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
    )

    ns.record_derivation(
        derivation_id="kappa_relaxation_energy_accounting_marker",
        inputs=[],
        output=sp.Symbol("kappa_relaxation_energy_accounting_classified"),
        method="kappa_relaxation_energy_accounting_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_kappa_relaxation_vacuum_sink_in_10_kappa_trace",
        script_id=SCRIPT_ID,
        title="Derive the vacuum sink term that accounts for kappa relaxation energy",
        status=ObligationStatus.OPEN,
        description=(
            "If kappa damping is used, dE/dt = -Gamma*v^2 shows energy is lost. "
            "The destination of this energy (vacuum configuration sink) must be "
            "derived rather than assumed to prevent hiding scalar radiation."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_kappa_damping_rate_Gamma_in_10_kappa_trace",
        script_id=SCRIPT_ID,
        title="Derive the kappa damping rate Gamma from first principles",
        status=ObligationStatus.OPEN,
        description=(
            "The attenuation length L_att ~ c/Gamma and critical damping condition "
            "Gamma^2 = 4*omega0^2 are only meaningful if Gamma is derived. "
            "Gamma must not be inserted by hand to hide scalar radiation."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="kappa_damping_requires_positive_vacuum_sink",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.OPEN_RISK,
        statement=(
            "If a kappa damping term Gamma is introduced, the energy loss rate "
            "dE/dt = -Gamma*v^2 must be accounted for by a derived positive-definite "
            "vacuum absorption/sink term. Inserting Gamma without this accounting "
            "is rejected as a cosmetic fix for scalar radiation."
        ),
    ))

    with out.derived_results():
        out.line("damped oscillator dE/dt = -Gamma*kappa_dot^2", StatusMark.PASS, "algebraic derivation")

    with out.governance_assessments():
        out.line("undamped kappa oscillator", StatusMark.FAIL, "can radiate if coupled externally")
        out.line("damped kappa with vacuum sink", StatusMark.DEFER, "plausible fallback; Gamma not derived")
        out.line("A-sector preservation guard", StatusMark.PASS, "sector split required")

    with out.unresolved_obligations():
        out.line("derive vacuum sink for kappa relaxation energy", StatusMark.OBLIGATION, "open")
        out.line("derive Gamma from first principles", StatusMark.OBLIGATION, "open")

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
