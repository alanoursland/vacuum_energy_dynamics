# Candidate relaxation energy accounting identity
#
# Group:
#   12_parent_identity_and_recombination
#
# Script type:
#   INVENTORY

# Purpose
# -------
# The recombination audit found:
#
#   recombination can be constrained,
#   but relaxation energy remains explicitly missing.
#
# Kappa relaxation uses a term like:
#
#   Gamma_relax
#
# or:
#
#   u^mu nabla_mu kappa = -lambda_kappa (kappa - kappa_min)
#
# This is safe only if relaxation is not energy destruction.
#
# This script asks:
#
#   What energy/accounting identity must exist so that relaxation is vacuum
#   configuration exchange rather than dissipation from the total system?
#
# This is a requirement audit, not a derivation.

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


@dataclass
class RelaxationEnergyRequirement:
    name: str
    requirement: str
    candidate_form: str
    forbidden_form: str
    status: str
    risk: str
    missing: str


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="recombination_without_double_counting_marker",
        upstream_script_id="012_parent_identity_and_recombination__candidate_recombination_without_double_counting",
        upstream_derivation_id="recombination_without_double_counting_marker",
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


def build_requirements() -> List[RelaxationEnergyRequirement]:
    return [
        RelaxationEnergyRequirement(
            name="E1: relaxation is exchange, not destruction",
            requirement="Gamma_relax must move imbalance into a vacuum configuration variable.",
            candidate_form="Gamma_relax -> dE_vac_config/dtau",
            forbidden_form="Gamma_relax removes energy with no destination",
            status="REQUIRED",
            risk="Cosmetic damping / energy nonconservation.",
            missing="Definition of E_vac_config.",
        ),
        RelaxationEnergyRequirement(
            name="E2: kappa relaxation has an energy functional",
            requirement="Kappa should relax down a local vacuum configuration energy.",
            candidate_form="E_kappa = 1/2*K_kappa*(kappa-kappa_min)^2",
            forbidden_form="first-order relaxation without stored/free energy",
            status="CANDIDATE",
            risk="Relaxation law becomes phenomenological damping.",
            missing="Derivation of K_kappa and measure/volume element.",
        ),
        RelaxationEnergyRequirement(
            name="E3: monotonic local relaxation but conserved total accounting",
            requirement="Kappa local free energy may decrease, but total vacuum/matter accounting must close.",
            candidate_form="dE_kappa/dtau <= 0, while d(E_total)/dtau = 0 in ordinary closed regime",
            forbidden_form="local damping interpreted as total energy loss",
            status="REQUIRED",
            risk="Energy disappears from the closed system.",
            missing="Destination reservoir and total balance identity.",
        ),
        RelaxationEnergyRequirement(
            name="E4: exterior mass remains fixed under relaxation",
            requirement="Relaxation energy accounting must not alter exterior A-sector mass flux incorrectly.",
            candidate_form="delta M_ext|Gamma_relax = 0 for internal trace relaxation",
            forbidden_form="relaxation changes exterior 1/r coefficient without source flux",
            status="CONSTRAINED",
            risk="Hidden mass tuning through damping.",
            missing="Boundary mass/energy separation theorem.",
        ),
        RelaxationEnergyRequirement(
            name="E5: ordinary closed regime excludes creation",
            requirement="Relaxation must not secretly act as Sigma_creation.",
            candidate_form="Sigma_creation=0; Gamma_relax internal exchange only",
            forbidden_form="Gamma_relax creates/destroys net vacuum energy in ordinary regime",
            status="CONSTRAINED",
            risk="Active-regime leakage.",
            missing="Active/ordinary regime separation.",
        ),
        RelaxationEnergyRequirement(
            name="E6: trace minimum stores configuration displacement",
            requirement="A shift in kappa_min must correspond to a shifted local minimum, not a direct radiative source.",
            candidate_form="kappa_min = chi_kappa*S_trace_effective; E_kappa centered at kappa_min",
            forbidden_form="trace source pumps Box kappa radiation",
            status="STRUCTURAL",
            risk="Trace becomes breathing radiation.",
            missing="Source law for S_trace_effective and chi_kappa.",
        ),
        RelaxationEnergyRequirement(
            name="E7: no kappa momentum reservoir",
            requirement="First-order relaxation must avoid independent kappa kinetic energy unless separately derived.",
            candidate_form="no 1/2*(u^mu nabla_mu kappa)^2 propagating energy term",
            forbidden_form="second-order oscillator/sloshing kappa channel",
            status="CONSTRAINED",
            risk="Hidden breathing wave / scalar radiation.",
            missing="Parent reason for non-inertial kappa.",
        ),
        RelaxationEnergyRequirement(
            name="E8: vacuum configuration variable must be named",
            requirement="The destination of relaxation energy must be a variable or constrained functional.",
            candidate_form="E_vac_config[A,kappa,boundary,q_v] or q_v/J_v balance",
            forbidden_form="unnamed reservoir invoked only when needed",
            status="MISSING",
            risk="Repair reservoir / unfalsifiable accounting.",
            missing="Definition of q_v, E_vac_config, or equivalent.",
        ),
        RelaxationEnergyRequirement(
            name="E9: recombination must not double-count relaxation energy",
            requirement="Energy stored in kappa/trace relaxation must not also be counted as A-sector mass response.",
            candidate_form="rho -> A mass flux; trace displacement -> E_vac_config/kappa sector",
            forbidden_form="same stress energy contributes independently to A mass and kappa stored energy as exterior charge",
            status="REQUIRED",
            risk="Scalar/energy double-counting.",
            missing="Parent source decomposition and recombination accounting.",
        ),
        RelaxationEnergyRequirement(
            name="E10: near-boundary smoothing energy remains diagnostic",
            requirement="Joint-minimum smoothing energy cannot be used as an observational claim until closure.",
            candidate_form="E_joint diagnostic with fixed M_ext and no prediction claim",
            forbidden_form="boundary smoothing energy predicts measurable deviation without weights/recombination",
            status="CONSTRAINED",
            risk="Near-boundary overclaim.",
            missing="Weights, sigma, observable map, closure.",
        ),
    ]


def print_requirement(e: RelaxationEnergyRequirement) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Requirement: {e.requirement}")
    print(f"Candidate form: {e.candidate_form}")
    print(f"Forbidden form: {e.forbidden_form}")
    print(f"[INFO] {e.name}: {e.status}")
    print(f"Risk: {e.risk}")
    print(f"Missing: {e.missing}")


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: Relaxation energy accounting problem")

    print("Question:")
    print()
    print("  Where does relaxation energy go?")
    print()
    print("Goal:")
    print()
    print("  prevent Gamma_relax from becoming hidden energy destruction")
    print()
    print("Discipline:")
    print()
    print("  relaxation is exchange/restoration, not disappearance")
    print("  exterior mass flux remains protected")
    print("  ordinary Sigma_creation remains zero")
    print("  no kappa momentum channel appears by accident")

    with out.unresolved_obligations():
        out.line("relaxation energy accounting problem posed", StatusMark.OBLIGATION, "E_vac_config definition required")


def case_1_requirement_inventory(entries: List[RelaxationEnergyRequirement]):
    header("Case 1: Relaxation energy requirement inventory")
    for entry in entries:
        print_requirement(entry)


def case_2_compact_table(entries: List[RelaxationEnergyRequirement], out: ScriptOutput):
    header("Case 2: Compact relaxation energy ledger")

    print("| Requirement | Candidate form | Forbidden form | Status | Missing |")
    print("|---|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.candidate_form.replace("|", "/")
            + " | "
            + e.forbidden_form.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.missing.replace("|", "/")
            + " |"
        )

    with out.governance_assessments():
        out.line("compact relaxation energy ledger produced", StatusMark.INFO, "10 energy accounting requirements recorded")


def case_3_status_counts(entries: List[RelaxationEnergyRequirement], out: ScriptOutput):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  A kappa free-energy form is plausible but not derived.")
    print("  The missing object is the vacuum configuration energy variable/reservoir.")
    print("  The accounting must preserve exterior mass and ordinary closed-regime conservation.")

    with out.governance_assessments():
        out.line("relaxation energy status count produced", StatusMark.INFO, str(counts))


def case_4_candidate_energy_form(out: ScriptOutput):
    header("Case 4: Candidate relaxation energy form")

    print("Candidate local free-energy form:")
    print()
    print("  E_kappa = 1/2 * K_kappa * (kappa - kappa_min)^2")
    print()
    print("Candidate relaxation:")
    print()
    print("  u^mu nabla_mu kappa = -mu_kappa * dE_kappa/dkappa")
    print()
    print("which gives:")
    print()
    print("  u^mu nabla_mu kappa = -mu_kappa*K_kappa*(kappa-kappa_min)")
    print()
    print("Local monotonicity:")
    print()
    print("  dE_kappa/dtau = -mu_kappa*(dE_kappa/dkappa)^2 <= 0")
    print()
    print("But the lost local free energy must go somewhere:")
    print()
    print("  dE_vac_config/dtau = -dE_kappa/dtau")
    print()
    print("This is candidate accounting, not yet a parent identity.")

    with out.governance_assessments():
        out.line("candidate kappa energy form stated", StatusMark.DEFER, "candidate only; K_kappa and E_vac_config undefined")


def case_5_required_total_balance(out: ScriptOutput):
    header("Case 5: Required total balance")

    print("Ordinary closed regime target:")
    print()
    print("  d/dtau (E_matter + E_A + E_W + E_TT + E_kappa + E_vac_config) = 0")
    print()
    print("with:")
    print()
    print("  Sigma_creation = 0")
    print("  delta M_ext|Gamma_relax = 0 for internal relaxation")
    print("  no A_rad")
    print("  no Box kappa")
    print()
    print("This is a requirement, not a derivation.")

    with out.unresolved_obligations():
        out.line("required total balance stated", StatusMark.OBLIGATION, "total balance identity not yet derived")


def case_6_failure_controls(out: ScriptOutput):
    header("Case 6: Failure controls")

    print("Relaxation energy accounting fails if:")
    print()
    print("1. Gamma_relax removes energy with no destination.")
    print("2. E_vac_config is unnamed or only invoked as a repair reservoir.")
    print("3. Relaxation changes exterior M_ext.")
    print("4. Gamma_relax acts like Sigma_creation in ordinary gravity.")
    print("5. Kappa gains a kinetic/momentum channel and becomes radiative.")
    print("6. Trace minimum energy is counted again as A-sector exterior mass.")
    print("7. Boundary smoothing energy is advertised as prediction before closure.")

    with out.governance_assessments():
        out.line("relaxation energy failure controls stated", StatusMark.DEFER, "failure controls policy-guarded")


def case_7_next_tests(out: ScriptOutput):
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_relaxation_energy_accounting_identity.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_parent_identity_template_v2.py")
    print("   Attempt a tighter parent identity scaffold using exclusions/projectors/recombination/accounting.")
    print()
    print("3. candidate_vacuum_configuration_energy_variable.py")
    print("   Try to define E_vac_config or q_v/J_v accounting.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_parent_identity_template_v2.py")
    print()
    print("Reason:")
    print("  The missing energy variable is named; now update the parent scaffold with all group-12 constraints.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.DEFER, "parent identity template v2 is the next gate")


def final_interpretation():
    header("Final interpretation")

    print("Relaxation energy accounting requires:")
    print()
    print("  Gamma_relax is exchange/restoration, not destruction")
    print("  E_kappa has a local free-energy form")
    print("  local relaxation is monotonic")
    print("  total ordinary closed-regime accounting is conserved")
    print("  exterior M_ext is preserved")
    print("  Sigma_creation remains zero")
    print("  no kappa momentum/radiation channel appears")
    print("  E_vac_config or equivalent must be defined")
    print()
    print("Possible next artifact:")
    print("  candidate_relaxation_energy_accounting_identity.md")
    print()
    print("Possible next script:")
    print("  candidate_parent_identity_template_v2.py")


def main():
    header("Candidate Relaxation Energy Accounting Identity")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement(out)
    entries = build_requirements()
    case_1_requirement_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_candidate_energy_form(out)
    case_5_required_total_balance(out)
    case_6_failure_controls(out)
    case_7_next_tests(out)
    final_interpretation()

    # Proof obligations for missing energy accounting items
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_E_vac_config_definition_E8",
        script_id=SCRIPT_ID,
        title="Define vacuum configuration energy variable E_vac_config (E8)",
        status=ObligationStatus.OPEN,
        description=(
            "The destination of relaxation energy must be a named variable or constrained functional. "
            "E_vac_config[A,kappa,boundary,q_v] or q_v/J_v bookkeeping must be defined. "
            "An unnamed repair reservoir is forbidden."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_K_kappa_and_E_kappa_functional_E2",
        script_id=SCRIPT_ID,
        title="Derive K_kappa and measure/volume element for E_kappa (E2)",
        status=ObligationStatus.OPEN,
        description=(
            "The candidate E_kappa = 1/2*K_kappa*(kappa-kappa_min)^2 requires "
            "K_kappa and a proper measure/volume element to be derived from the parent identity."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_total_closed_regime_balance_E3",
        script_id=SCRIPT_ID,
        title="Derive total ordinary closed-regime energy balance (E3)",
        status=ObligationStatus.OPEN,
        description=(
            "Show that d/dtau(E_matter + E_A + E_W + E_TT + E_kappa + E_vac_config) = 0 "
            "with Sigma_creation=0 and delta M_ext|Gamma_relax=0 in ordinary closed gravity."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_relaxation_source_decomposition_E9",
        script_id=SCRIPT_ID,
        title="Derive parent source decomposition for relaxation vs A-sector (E9)",
        status=ObligationStatus.OPEN,
        description=(
            "Show that trace displacement energy routes to E_vac_config/kappa sector "
            "and does not double-count with A-sector exterior mass response. "
            "Parent source decomposition required."
        ),
    ))

    # Policy claim: unnamed relaxation reservoir is forbidden
    ns.record_claim(ClaimRecord(
        claim_id="unnamed_relaxation_reservoir_forbidden_policy",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Gamma_relax must not remove energy without a named destination variable. "
            "An unnamed reservoir that absorbs any mismatch is a repair reservoir and is forbidden. "
            "E_vac_config or an equivalent must be defined before relaxation energy accounting is licensed."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="kappa_momentum_channel_forbidden_policy",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "First-order kappa relaxation must not carry an independent kinetic energy term "
            "1/2*(u^mu nabla_mu kappa)^2. A second-order kappa oscillator/sloshing channel is forbidden "
            "unless separately and explicitly derived."
        ),
    ))

    # Candidate route: kappa free-energy exchange form
    ns.record_route(RouteRecord(
        route_id="kappa_free_energy_exchange_candidate",
        script_id=SCRIPT_ID,
        name="Candidate kappa free-energy: E_kappa = 1/2*K_kappa*(kappa-kappa_min)^2 with E_vac_config exchange",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[
            "derive_E_vac_config_definition_E8",
            "derive_K_kappa_and_E_kappa_functional_E2",
            "derive_total_closed_regime_balance_E3",
        ],
        activation_conditions=[
            "K_kappa derived from parent vacuum minimum",
            "E_vac_config named and defined",
            "dE_kappa/dtau + dE_vac_config/dtau = 0 demonstrated",
            "Sigma_creation = 0 enforced",
            "delta M_ext|Gamma_relax = 0 enforced",
        ],
    ))

    # Branch decision: relaxation energy accounting deferred
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_relaxation_energy_accounting_derivation",
        script_id=SCRIPT_ID,
        branch_id="relaxation_energy_accounting_derivation",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "derive_E_vac_config_definition_E8",
            "derive_K_kappa_and_E_kappa_functional_E2",
            "derive_total_closed_regime_balance_E3",
            "derive_relaxation_source_decomposition_E9",
        ],
        description=(
            "Relaxation energy accounting cannot be licensed until E_vac_config is defined, "
            "K_kappa is derived, total balance is established, and source decomposition is verified."
        ),
    ))

    ns.record_derivation(
        derivation_id="relaxation_energy_accounting_identity_marker",
        inputs=[],
        output=sp.Symbol("relaxation_energy_accounting_identity_built"),
        method="relaxation_energy_accounting_identity_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
