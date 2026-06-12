# Trial D1: the depletion budget vs the dark matter requirement
#
# Group:
#   004_trial_D_standing_frustration
#
# Script type:
#   LEDGER / ENTRY-GATE KILL TEST
#
# Purpose
# -------
# Entry-gate calculation for the depletion-history-halo mechanism (Trial D,
# mechanisms D-M1/D-M2 in their P6-exchange form):
#
#   vacuum destroyed by P6 exchange during a galaxy's assembly history
#   leaves a Delta_rho < 0 residue that gravitates positively
#   (dark-bridge sign result: effective source = -2*Delta_rho).
#
# Question: integrate the P6 budget over assembly history. Does the residue
# land near the dark matter requirement (~5x baryonic gravitational effect)?
#
# The budget is tied by P6's own statement to KINETIC ENERGY changes:
# "the energy of the vacuum exchanged equals the kinetic energy change."
# The sign-fork branch only changes a factor (eta = 1 in the indefinite
# branch's dynamic-exchange reading, eta = 2 in the positive-J funded
# reading). Galactic dynamics fix the kinetic scale: KE ~ (1/2) M v^2 with
# v the virial velocity. So the entire calculation is parameter-free up to
# the order-unity eta -- exactly the kind of arithmetic an entry gate wants.

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


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="charter_infall_budget_dependency_d1",
        upstream_script_id="000_trial_charter__trial_gate_inventory",
        upstream_derivation_id="trial_traceful_infall_budget_t000",
        expected_record_kind=RecordKind.DERIVATION,
    )
    return archive, ns, invalidated


# =============================================================================
# Case 0
# =============================================================================


def case_0_problem(out: ScriptOutput) -> None:
    header("Case 0: The depletion-budget question")
    print("Mechanism under test: depletion-history halos (Trial D, D-M1/D-M2")
    print("in P6-exchange form). Vacuum destroyed during assembly leaves a")
    print("Delta_rho < 0 residue gravitating as -2*Delta_rho > 0.")
    print()
    print("Requirement: effective gravitating energy ~ 5 x baryonic rest")
    print("energy (the dark matter abundance), roughly flat across systems.")
    print()
    print("Budget law (P6, both sign-fork readings):")
    print("  E_depleted = eta * Delta_KE_assembly,   eta in {1, 2}.")
    print()
    print("Kinetic scale fixed by dynamics: Delta_KE ~ (1/2) M_b v_vir^2.")
    print("Everything below is parameter-free up to eta.")

    with out.governance_assessments():
        out.line("Trial D1 opened", StatusMark.INFO,
                 "entry-gate abundance arithmetic; kill test for the P6-depletion mechanism")


# =============================================================================
# Case 1: the requirement and the budget, symbolically
# =============================================================================


def case_1_symbolic_ledger(out: ScriptOutput):
    header("Case 1: Requirement vs budget (symbolic)")
    M_b, v, c, eta = sp.symbols("M_b v c eta", positive=True)

    # requirement: effective source 5 x baryonic; dark-bridge factor 2 means
    # the depleted energy itself need only be 5/2 x baryonic (generous).
    E_required = sp.Rational(5, 2) * M_b * c**2

    # budget: eta * (1/2) M_b v^2
    E_budget = eta * sp.Rational(1, 2) * M_b * v**2

    ratio = sp.simplify(E_budget / E_required)
    ratio_expected = eta * v**2 / (5 * c**2)

    print(f"  E_required (with -2*Delta_rho generosity) = {sp.sstr(E_required)}")
    print(f"  E_budget   (P6, eta x assembly KE)        = {sp.sstr(E_budget)}")
    print(f"  ratio = {sp.sstr(ratio)}")
    print()
    print("  THE SHAPE RESULT: the predicted 'dark matter fraction' scales as")
    print("  (v/c)^2 -- it is velocity-dependent. The observed ratio is ~5,")
    print("  roughly FLAT from dwarfs to clusters. Wrong magnitude AND wrong")
    print("  shape, before any numbers are inserted.")

    with out.derived_results():
        out.line("budget/requirement = eta v^2 / (5 c^2)",
                 StatusMark.PASS if is_zero(ratio - ratio_expected) else StatusMark.FAIL,
                 "parameter-free up to order-unity eta; scales as (v/c)^2, observed ratio is flat")
    return ratio


# =============================================================================
# Case 2: numbers
# =============================================================================


def case_2_numbers(out: ScriptOutput):
    header("Case 2: Magnitudes (Milky Way and cluster scales)")
    c = 2.998e8
    systems = [
        ("Milky Way (v_vir ~ 200 km/s)", 200e3),
        ("rich cluster (sigma ~ 1000 km/s)", 1000e3),
        ("dwarf galaxy (v ~ 50 km/s)", 50e3),
    ]
    print("  eta = 2 (most generous branch):")
    worst = 0.0
    for name, v in systems:
        ratio = 2 * v**2 / (5 * c**2)
        shortfall = 1.0 / ratio
        worst = max(worst, ratio)
        print(f"    {name}:  budget/requirement = {ratio:.2e}   (shortfall {shortfall:.1e}x)")
    print()
    print("  Even at cluster velocities the budget is ~5e-6 of requirement.")

    ok = worst < 1e-4
    with out.derived_results():
        out.line("virial P6 budget falls short by >= 5 orders of magnitude",
                 StatusMark.PASS if ok else StatusMark.FAIL,
                 "best case (clusters, eta=2): ~ 4e-6 of the requirement")
    return worst


# =============================================================================
# Case 3: generosity sweep -- every plausible depletion channel
# =============================================================================


def case_3_channels(out: ScriptOutput):
    header("Case 3: Channel inventory at maximum generosity")
    print("  Could other assembly-history channels beat the virial budget?")
    print("  Upper bounds on KE-class energy per unit baryonic rest energy:")
    print()
    channels = [
        ("virial assembly / mergers", 4e-7,
         "(v/c)^2 at v ~ 200 km/s; hierarchical sums stay at binding-energy scale"),
        ("supernova kinetic output, cumulative", 1e-5,
         "~1e51 erg x ~1e9 SN vs ~1e65 erg baryonic rest energy"),
        ("compact-object formation (NS/BH binding)", 1e-3,
         "~0.1 c^2 on the ~1% of baryons in compact remnants -- the most generous channel"),
        ("SMBH accretion (0.1 efficiency on ~1e-3 M_b)", 1e-4, ""),
    ]
    total = 0.0
    for name, frac, note in channels:
        total += frac
        print(f"    {name:48s} <= {frac:.0e}  {note}")
    print(f"\n  generous total: <= {total:.1e} of M_b c^2")
    required = 2.5
    shortfall = required / total
    print(f"  requirement:      {required:.1f} of M_b c^2")
    print(f"  shortfall even at maximum generosity: {shortfall:.0e}x")
    print()
    print("  Counter-flow note (makes it worse): photons CLIMBING OUT of the")
    print("  well CREATE vacuum under P6 (T1's ascent bookkeeping), partially")
    print("  refilling the depletion. The residue is smaller than the gross")
    print("  budget. The kill margin above is therefore a lower bound.")

    ok = shortfall > 1e3
    with out.derived_results():
        out.line("all-channel generous budget still short by >= 3 orders",
                 StatusMark.PASS if ok else StatusMark.FAIL,
                 f"sum of channels <= {total:.0e} M_b c^2 vs required 2.5 M_b c^2")
    return total, shortfall


# =============================================================================
# Case 4: verdict
# =============================================================================


def case_4_verdict(out: ScriptOutput) -> None:
    header("Case 4: Trial D1 verdict")
    print("Depletion-history halos (P6-exchange form of D-M1/D-M2):")
    print()
    print("  KILLED at entry gate D-G1 (abundance), parameter-free:")
    print()
    print("  1. Magnitude: the P6 budget is tied to kinetic energy by the")
    print("     postulate's own statement; galactic kinetic scales are")
    print("     (v/c)^2 ~ 1e-7..1e-5 of rest energy; the requirement is 2.5.")
    print("     Shortfall 1e3x at maximum generosity, 1e6x honestly.")
    print("  2. Shape: predicted ratio scales as (v/c)^2; observed ~5, flat.")
    print("  3. Counter-flow: outbound radiation refills; residue < budget.")
    print()
    print("  No parameter rescues it: scaling eta up by 1e6 violates P6's")
    print("  exchange-equals-KE-change statement by definition.")
    print()
    print("SURVIVORS within Trial D (unaffected by this kill):")
    print()
    print("  D-M4 / the w ~ 0 excess branch: abundance set by PRODUCTION")
    print("    physics (how much excess frustration exists), not by P6 KE")
    print("    bookkeeping. The revised entry gate (equation of state +")
    print("    production) stands as Trial D's live route.")
    print("  D-M3 / strain route: dark sector as derived property of")
    print("    K_strain; abundance question deferred to that functional.")
    print()
    print("  The kill also retires the old notes' 'dark matter = passive")
    print("  vacuum depletion at galactic scales' assignment in its")
    print("  energy-bookkeeping form: depletion is real under P6 dynamics")
    print("  but six orders too small to be the dark sector.")

    with out.governance_assessments():
        out.line("Trial D1 verdict: depletion-history mechanism KILLED (abundance)",
                 StatusMark.PASS,
                 "parameter-free: magnitude short >= 1e3x at max generosity; shape wrong ((v/c)^2 vs flat)")
    with out.unresolved_obligations():
        out.line("Trial D continues on the excess/EoS branch only",
                 StatusMark.OBLIGATION,
                 "derive w and production abundance of the frustration excess (revised D-G1)")


# =============================================================================
# Archive recording
# =============================================================================


def record_results(ns, worst_ratio: float, channel_total: float) -> None:
    M_b, v, c, eta = sp.symbols("M_b v c eta", positive=True)

    ns.record_derivation(
        derivation_id="depletion_budget_ratio_d1",
        inputs=[],
        output=eta * v**2 / (5 * c**2),
        method="E_budget/E_required = [eta (1/2) M_b v^2] / [(5/2) M_b c^2]",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="abundance_ratio",
        scope="parameter-free up to eta in {1,2}; includes dark-bridge factor-2 generosity",
    )
    ns.record_derivation(
        derivation_id="depletion_channel_inventory_d1",
        inputs=[],
        output=sp.Float(channel_total),
        method="generous upper bounds: virial, SN kinetic, compact-object binding, SMBH accretion",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="channel_upper_bound",
        scope=f"all channels sum <= {channel_total:.0e} M_b c^2 vs required 2.5; "
              "counter-flow (outbound radiation creates vacuum) makes residue smaller still",
    )

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="kill_depletion_history_halos_d1",
        script_id=SCRIPT_ID,
        branch_id="trial_D_depletion_history_p6_mechanism",
        status=GovernanceStatus.FAILED_BY_WITNESS,
        tier=ClaimTier.EXCLUSION,
        obligation_ids=[],
        description=(
            "Depletion-history halos (P6-exchange form of D-M1/D-M2) killed at the "
            "abundance entry gate: the P6 budget is bound to kinetic energy by the "
            "postulate itself, giving budget/requirement = eta v^2/(5 c^2) ~ 1e-7..1e-5 "
            "-- short by >= 3 orders at maximum channel generosity (compact-object "
            "binding included) and ~6 orders honestly, with the wrong scaling shape "
            "((v/c)^2 vs observed flat ~5) and a vacuum-creating counter-flow from "
            "outbound radiation. No parameter rescues it without violating P6. "
            "Witnesses: depletion_budget_ratio_d1, depletion_channel_inventory_d1."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="trial_D_excess_eos_route_d1",
        script_id=SCRIPT_ID,
        title="Trial D continues on the excess/EoS branch only",
        status=ObligationStatus.OPEN,
        required_by=["trial_D_verdict"],
        description=(
            "Surviving routes: the w ~ 0 transportable excess (abundance from "
            "production physics, not P6 bookkeeping) and the K_strain route (D-M3). "
            "Revised entry gate stands: derive the excess's equation of state, "
            "transport, and production abundance."
        ),
    ))

    ns.record_route(RouteRecord(
        route_id="trial_D2_excess_eos_route_d1",
        script_id=SCRIPT_ID,
        name="Trial D2: equation of state and production of the frustration excess",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=["trial_D_excess_eos_route_d1"],
        activation_conditions=[
            "depletion-history mechanism is closed (this script)",
            "the excess needs a seat in the dynamics before sourcing (P9 fence)",
        ],
    ))

    ns.record_claim(ClaimRecord(
        claim_id="depletion_abundance_kill_d1",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.EXCLUSION,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "Integrating the P6 exchange budget over galactic assembly history "
            "yields a depletion residue of order eta (v/c)^2 / 5 of the dark matter "
            "requirement -- 1e-7 to 1e-5 across dwarfs to clusters, with all "
            "plausible channels (including compact-object formation) summing below "
            "2e-3 of requirement, and the wrong scaling shape. The depletion-history "
            "dark matter mechanism is excluded without free parameters."
        ),
        derivation_ids=["depletion_budget_ratio_d1", "depletion_channel_inventory_d1"],
        obligation_ids=["trial_D_excess_eos_route_d1"],
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Trial D1: Depletion Budget vs the Dark Matter Requirement")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    case_0_problem(out)
    case_1_symbolic_ledger(out)
    worst = case_2_numbers(out)
    channel_total, shortfall = case_3_channels(out)
    case_4_verdict(out)

    record_results(ns, worst, channel_total)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
