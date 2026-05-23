# Candidate vacuum configuration energy variable
#
# Group:
#   12_parent_identity_and_recombination
#
# Script type:
#   INVENTORY

# Purpose
# -------
# Parent identity template v2 now depends explicitly on:
#
#   E_vac_config
#
# or an equivalent vacuum-substance accounting variable:
#
#   q_v / J_v
#
# The relaxation-energy audit interpreted Gamma_relax as exchange:
#
#   curvature excess deposits into vacuum-substance configuration,
#   curvature deficit pulls from vacuum-substance configuration,
#   and ordinary closed-regime total accounting is conserved.
#
# This script asks:
#
#   What could E_vac_config be?
#
# It is not a definition yet.
# It is a variable audit and no-repair-reservoir test.
#
# This script is also the final summary script for Group 12.
# It records a HandoffImportRecord for what Group 13 may import.

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
    HandoffImportRecord,
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
class VacuumVariableCandidate:
    name: str
    candidate: str
    role: str
    required_exchange: str
    forbidden_use: str
    status: str
    risk: str
    missing: str


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="parent_identity_template_v2_marker",
        upstream_script_id="012_parent_identity_and_recombination__candidate_parent_identity_template_v2",
        upstream_derivation_id="parent_identity_template_v2_marker",
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


def build_candidates() -> List[VacuumVariableCandidate]:
    return [
        VacuumVariableCandidate(
            name="V1: local vacuum configuration energy density",
            candidate="epsilon_vac_config(x)",
            role="Local destination/source for kappa relaxation imbalance.",
            required_exchange="u^mu nabla_mu epsilon_vac_config = -u^mu nabla_mu E_kappa_density",
            forbidden_use="unnamed reservoir that absorbs any mismatch.",
            status="CANDIDATE",
            risk="Can become a repair reservoir if not tied to measurable/configurational variables.",
            missing="Definition, units, measure, coupling to kappa.",
        ),
        VacuumVariableCandidate(
            name="V2: vacuum charge density proxy",
            candidate="q_v",
            role="Ontology-native substance-density or configuration charge.",
            required_exchange="partial_t q_v + div J_v = Sigma_exchange - Gamma_relax in ordinary regime",
            forbidden_use="q_v changes exterior mass or acts as Sigma_creation.",
            status="STRUCTURAL",
            risk="May duplicate A-sector mass density if not separated.",
            missing="Physical meaning and relation to curvature/volume.",
        ),
        VacuumVariableCandidate(
            name="V3: vacuum transport current",
            candidate="J_v",
            role="Flux of vacuum-substance configuration between regions.",
            required_exchange="balances local curvature excess/deficit through divergence of J_v",
            forbidden_use="instantaneous nonlocal repair current.",
            status="STRUCTURAL",
            risk="Could hide acausal transfer if support/speed is undefined.",
            missing="Transport law and causal/constraint status.",
        ),
        VacuumVariableCandidate(
            name="V4: constrained global vacuum reservoir",
            candidate="E_vac_config_global",
            role="Global constraint reservoir for non-propagating relaxation bookkeeping.",
            required_exchange="integral dE_vac_config = -integral dE_kappa for closed system",
            forbidden_use="arbitrary global energy sink/source.",
            status="RISK",
            risk="Looks like an unfalsifiable reservoir unless derived as a constraint.",
            missing="Constraint origin and locality/observability rules.",
        ),
        VacuumVariableCandidate(
            name="V5: boundary/interface configuration energy",
            candidate="E_boundary_config",
            role="Energy associated with boundary smoothing or trace/volume matching near interfaces.",
            required_exchange="boundary smoothing energy changes while M_ext remains fixed",
            forbidden_use="changes exterior 1/r coefficient or predicts deviation before closure",
            status="CANDIDATE",
            risk="Boundary overclaim or mass tuning.",
            missing="Boundary mass theorem, weights, sigma, observable map.",
        ),
        VacuumVariableCandidate(
            name="V6: kappa minimum displacement energy",
            candidate="E_min_shift = E_vac_config[kappa_min]",
            role="Stores energy associated with shifting the local kappa minimum.",
            required_exchange="trace/pressure shifts minimum; relaxation moves kappa toward that shifted minimum",
            forbidden_use="trace source pumps scalar radiation or exterior kappa charge.",
            status="CANDIDATE",
            risk="Double-counting trace energy with matter stress.",
            missing="S_trace_effective, chi_kappa, source accounting.",
        ),
        VacuumVariableCandidate(
            name="V7: A-sector excluded from vacuum reservoir",
            candidate="E_A not included as relaxable vacuum reservoir",
            role="Protect exterior mass flux from relaxation bookkeeping.",
            required_exchange="rho -> A mass flux; kappa exchange does not alter M_ext",
            forbidden_use="vacuum reservoir adjusts A mass charge.",
            status="CONSTRAINED",
            risk="Relaxation tunes measured mass.",
            missing="Parent separation of A flux and vacuum configuration energy.",
        ),
        VacuumVariableCandidate(
            name="V8: active creation variable excluded in ordinary regime",
            candidate="Sigma_creation not part of E_vac_config exchange",
            role="Protect ordinary closure.",
            required_exchange="Sigma_creation=0; Gamma_relax internal only",
            forbidden_use="E_vac_config creates/destroys net energy in ordinary gravity.",
            status="CONSTRAINED",
            risk="Active-regime leakage.",
            missing="Active-regime trigger/exclusion law.",
        ),
        VacuumVariableCandidate(
            name="V9: recombination accounting variable",
            candidate="E_recombination_accounting",
            role="Ensures scalar response is counted once when geometry is assembled.",
            required_exchange="A mass energy and kappa trace energy remain distinct in recombination",
            forbidden_use="same scalar stress counted in A and kappa sectors.",
            status="UNRESOLVED",
            risk="Energy/scalar double-counting in metric map.",
            missing="P_recombination and source accounting.",
        ),
        VacuumVariableCandidate(
            name="V10: coefficient/action stiffness source",
            candidate="E_action_stiffness",
            role="Could derive K_kappa, C_T, K_T, alpha_W/K_c from a shared stiffness principle.",
            required_exchange="coefficients come from action/stiffness, not GR matching",
            forbidden_use="using E_vac_config to tune coefficients after the fact.",
            status="MISSING",
            risk="Coefficient repair knob.",
            missing="Action/stiffness principle.",
        ),
    ]


def print_candidate(v: VacuumVariableCandidate) -> None:
    print()
    print("-" * 120)
    print(v.name)
    print("-" * 120)
    print(f"Candidate: {v.candidate}")
    print(f"Role: {v.role}")
    print(f"Required exchange: {v.required_exchange}")
    print(f"Forbidden use: {v.forbidden_use}")
    print(f"[INFO] {v.name}: {v.status}")
    print(f"Risk: {v.risk}")
    print(f"Missing: {v.missing}")


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: Vacuum configuration energy variable problem")

    print("Question:")
    print()
    print("  What could E_vac_config be?")
    print()
    print("Goal:")
    print()
    print("  name possible vacuum-substance accounting variables without making them repair reservoirs")
    print()
    print("Discipline:")
    print()
    print("  E_vac_config must not change exterior mass")
    print("  E_vac_config must not act as Sigma_creation")
    print("  E_vac_config must not hide arbitrary damping")
    print("  E_vac_config must not double-count scalar response")

    with out.unresolved_obligations():
        out.line("vacuum configuration variable problem posed", StatusMark.OBLIGATION, "E_vac_config definition required")


def case_1_candidate_inventory(entries: List[VacuumVariableCandidate]):
    header("Case 1: Vacuum variable candidate inventory")
    for entry in entries:
        print_candidate(entry)


def case_2_compact_table(entries: List[VacuumVariableCandidate], out: ScriptOutput):
    header("Case 2: Compact vacuum variable ledger")

    print("| Candidate | Role | Status | Risk | Missing |")
    print("|---|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.candidate.replace("|", "/")
            + " | "
            + e.role.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.risk.replace("|", "/")
            + " | "
            + e.missing.replace("|", "/")
            + " |"
        )

    with out.governance_assessments():
        out.line("compact vacuum variable ledger produced", StatusMark.INFO, "10 E_vac_config candidates audited")


def case_3_status_counts(entries: List[VacuumVariableCandidate], out: ScriptOutput):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Several candidates are plausible, but none are derived.")
    print("  The safest immediate interpretation is local vacuum configuration energy")
    print("  plus q_v/J_v bookkeeping, while excluding A-sector mass and Sigma_creation.")

    with out.governance_assessments():
        out.line("vacuum variable status count produced", StatusMark.INFO, str(counts))


def case_4_candidate_minimal_accounting(out: ScriptOutput):
    header("Case 4: Candidate minimal accounting")

    print("Minimal candidate accounting:")
    print()
    print("  e_kappa = 1/2*K_kappa*(kappa-kappa_min)^2")
    print()
    print("  u^mu nabla_mu e_kappa <= 0")
    print()
    print("  u^mu nabla_mu epsilon_vac_config = -u^mu nabla_mu e_kappa")
    print()
    print("Ordinary closed regime:")
    print()
    print("  Sigma_creation = 0")
    print("  delta M_ext = 0")
    print("  no A_rad")
    print("  no Box kappa")
    print()
    print("Interpretation:")
    print()
    print("  curvature excess deposits into vacuum-substance configuration")
    print("  curvature deficit pulls from vacuum-substance configuration")
    print("  total local accounting closes")
    print()
    print("This is candidate bookkeeping, not a derivation.")

    with out.governance_assessments():
        out.line("candidate minimal vacuum accounting stated", StatusMark.DEFER, "candidate only; not derived")


def case_5_repair_reservoir_tests(out: ScriptOutput):
    header("Case 5: No-repair-reservoir tests")

    print("E_vac_config fails if:")
    print()
    print("1. It is invoked only after contradictions appear.")
    print("2. It can absorb arbitrary energy without a state variable.")
    print("3. It changes exterior M_ext.")
    print("4. It acts like Sigma_creation in ordinary regime.")
    print("5. It duplicates A-sector mass energy.")
    print("6. It tunes kappa, vector, or tensor coefficients.")
    print("7. It allows acausal nonlocal vacuum transport without being declared a constraint.")
    print("8. It makes near-boundary predictions before recombination/observables are derived.")

    with out.governance_assessments():
        out.line("no-repair-reservoir tests stated", StatusMark.DEFER, "8 repair-reservoir tests policy-guarded")


def case_6_best_current_choice(out: ScriptOutput):
    header("Case 6: Best current choice")

    print("Best current minimal interpretation:")
    print()
    print("  epsilon_vac_config:")
    print("    local vacuum-substance configuration energy density")
    print()
    print("  q_v, J_v:")
    print("    optional ontology-native density/current bookkeeping variables")
    print()
    print("  E_boundary_config:")
    print("    possible interface contribution, diagnostic only")
    print()
    print("Excluded from this variable:")
    print()
    print("  A-sector exterior mass charge")
    print("  Sigma_creation in ordinary regime")
    print("  coefficient tuning reservoir")
    print()
    print("This is still structural, not derived.")

    with out.governance_assessments():
        out.line("best current vacuum variable choice stated", StatusMark.DEFER, "structural only; not derived")


def case_7_next_tests(out: ScriptOutput):
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_vacuum_configuration_energy_variable.md")
    print("   Artifact for this script.")
    print()
    print("2. parent_identity_and_recombination_summary.md")
    print("   Summarize group 12 so far.")
    print()
    print("3. candidate_parent_identity_template_v3.py")
    print("   Attempt a third scaffold after E_vac_config choices.")
    print()
    print("Recommended next:")
    print()
    print("  parent_identity_and_recombination_summary.md")
    print()
    print("Reason:")
    print("  Group 12 has reached a natural summary point after exclusions, implications, projectors, scalar/kappa/boundary/recombination/accounting, and E_vac_config.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.DEFER, "group 12 summary and group 13 handoff is the next step")


def case_8_group12_summary_and_group13_handoff(out: ScriptOutput):
    header("Case 8: Group 12 summary and Group 13 handoff")

    print("Group 12 has established:")
    print()
    print("  14 parent identity exclusion constraints")
    print("  15 reduced-sector implication tests")
    print("  10 projector structure entries (P_L and P_T symbolically verified)")
    print("  scalar constraint-not-radiation policy (3 policy rules)")
    print("  10 kappa covariant relaxation requirements")
    print("  10 boundary mass preservation requirements")
    print("  10 recombination no-double-counting entries")
    print("  10 relaxation energy accounting requirements")
    print("  13 parent identity template v2 clauses")
    print("  10 vacuum configuration energy variable candidates")
    print()
    print("What Group 13 may import from Group 12:")
    print()
    print("  policy rules: scalar constraint, box kappa, rho-kappa, GR coefficients")
    print("  proof obligations: scalar propagation, P_scalar, P_recombination, E_vac_config")
    print("  candidate route: kappa covariantized relaxation form")
    print("  candidate route: reduced recombination map")
    print("  candidate route: kappa free-energy exchange")
    print("  branch decisions: deferred until prerequisites met")
    print()
    print("Group 13 (vacuum substance accounting) should:")
    print()
    print("  define q_v and J_v properly")
    print("  derive or constrain E_vac_config from q_v/J_v ontology")
    print("  close the ordinary closed-regime total energy balance")
    print("  not reopen exclusions established in Group 12")

    with out.governance_assessments():
        out.line("group 12 summary stated; group 13 handoff prepared", StatusMark.INFO, "handoff recorded below")


def final_interpretation():
    header("Final interpretation")

    print("E_vac_config should currently be treated as:")
    print()
    print("  a local vacuum-substance configuration energy density,")
    print("  possibly with q_v/J_v bookkeeping,")
    print("  excluding A-sector mass charge and Sigma_creation.")
    print()
    print("It must support:")
    print("  curvature excess depositing into vacuum substance")
    print("  curvature deficit pulling from vacuum substance")
    print("  ordinary closed-regime accounting")
    print("  exterior mass preservation")
    print()
    print("Possible next artifact:")
    print("  candidate_vacuum_configuration_energy_variable.md")
    print()
    print("Recommended next:")
    print("  parent_identity_and_recombination_summary.md")


def main():
    header("Candidate Vacuum Configuration Energy Variable")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement(out)
    entries = build_candidates()
    case_1_candidate_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_candidate_minimal_accounting(out)
    case_5_repair_reservoir_tests(out)
    case_6_best_current_choice(out)
    case_7_next_tests(out)
    case_8_group12_summary_and_group13_handoff(out)
    final_interpretation()

    # Proof obligations for vacuum variable definition
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_epsilon_vac_config_definition_V1",
        script_id=SCRIPT_ID,
        title="Define local vacuum configuration energy density epsilon_vac_config (V1)",
        status=ObligationStatus.OPEN,
        description=(
            "epsilon_vac_config must be defined with units, measure, and coupling to kappa. "
            "It must not become a repair reservoir. "
            "Group 13 (vacuum substance accounting) is responsible for this derivation."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_q_v_J_v_transport_law_V2_V3",
        script_id=SCRIPT_ID,
        title="Define q_v and J_v vacuum substance density and transport law (V2, V3)",
        status=ObligationStatus.OPEN,
        description=(
            "q_v and J_v must satisfy partial_t q_v + div J_v = Sigma_exchange - Gamma_relax in ordinary regime. "
            "Transport law must be causal/local or declared as a constraint with stated support. "
            "Group 13 is responsible for this derivation."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_E_vac_config_not_A_sector_separation_V7",
        script_id=SCRIPT_ID,
        title="Derive parent separation of A-sector flux and vacuum configuration energy (V7)",
        status=ObligationStatus.OPEN,
        description=(
            "E_vac_config must be separated from the A-sector exterior mass charge. "
            "rho routes to A; kappa exchange must not alter M_ext. "
            "Parent separation identity required."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_P_recombination_accounting_variable_V9",
        script_id=SCRIPT_ID,
        title="Derive recombination accounting variable ensuring scalar counted once (V9)",
        status=ObligationStatus.OPEN,
        description=(
            "A mass energy and kappa trace energy must remain distinct in recombination. "
            "E_recombination_accounting must follow from P_recombination derivation."
        ),
    ))

    # Policy claim: E_vac_config as repair reservoir is forbidden
    ns.record_claim(ClaimRecord(
        claim_id="E_vac_config_repair_reservoir_forbidden_policy",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "E_vac_config must not function as an unnamed repair reservoir. "
            "It must not change exterior M_ext, act as Sigma_creation, "
            "duplicate A-sector mass energy, tune coefficients, or absorb arbitrary energy "
            "without a defined state variable. An invocable-only-after-contradiction reservoir is forbidden."
        ),
    ))

    # Candidate route: local epsilon_vac_config with q_v/J_v bookkeeping
    ns.record_route(RouteRecord(
        route_id="epsilon_vac_config_local_with_q_v_J_v_candidate",
        script_id=SCRIPT_ID,
        name="Candidate E_vac_config: local epsilon_vac_config with optional q_v/J_v bookkeeping",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[
            "derive_epsilon_vac_config_definition_V1",
            "derive_q_v_J_v_transport_law_V2_V3",
            "derive_E_vac_config_not_A_sector_separation_V7",
        ],
        activation_conditions=[
            "epsilon_vac_config defined with units and measure",
            "q_v/J_v transport law is causal or constraint-declared",
            "A-sector flux separated from E_vac_config",
            "Sigma_creation excluded from E_vac_config exchange",
            "no coefficient tuning by E_vac_config",
        ],
    ))

    # Branch decision: E_vac_config full definition deferred to Group 13
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_E_vac_config_full_definition_to_group13",
        script_id=SCRIPT_ID,
        branch_id="E_vac_config_full_definition",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "derive_epsilon_vac_config_definition_V1",
            "derive_q_v_J_v_transport_law_V2_V3",
            "derive_E_vac_config_not_A_sector_separation_V7",
            "derive_P_recombination_accounting_variable_V9",
        ],
        description=(
            "Full definition of E_vac_config is deferred to Group 13 (vacuum substance accounting). "
            "Group 12 has established the constraints and requirements that E_vac_config must satisfy, "
            "but the derivation is a Group 13 responsibility."
        ),
    ))

    # HandoffImportRecord: what Group 13 may import from Group 12
    ns.record_handoff_import(HandoffImportRecord(
        handoff_id="group12_to_group13_handoff",
        script_id=SCRIPT_ID,
        imported_as=RecordKind.INVENTORY_MARKER,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        source_record_ref="vacuum_configuration_energy_variable_marker",
        imported_record_refs=[
            "parent_identity_exclusion_constraints_marker",
            "parent_identity_reduced_implications_marker",
            "projector_structure_for_parent_identity_marker",
            "scalar_constraint_not_radiation_identity_marker",
            "kappa_covariant_relaxation_requirement_marker",
            "boundary_mass_preservation_identity_marker",
            "recombination_without_double_counting_marker",
            "relaxation_energy_accounting_identity_marker",
            "parent_identity_template_v2_marker",
            "vacuum_configuration_energy_variable_marker",
        ],
        description=(
            "Group 13 (vacuum substance accounting) may import from Group 12: "
            "policy rules for scalar constraint, Box kappa, rho-kappa separation, GR coefficient insertion. "
            "Open proof obligations: scalar constraint propagation, P_scalar, P_recombination, "
            "E_vac_config definition, boundary mass preservation theorem. "
            "Candidate routes: kappa covariantized relaxation, reduced recombination map, kappa free-energy exchange. "
            "Branch decisions: all positive parent identity routes are deferred pending prerequisites. "
            "Group 13 must not reopen exclusions established in Group 12."
        ),
    ))

    ns.record_derivation(
        derivation_id="vacuum_configuration_energy_variable_marker",
        inputs=[],
        output=sp.Symbol("vacuum_configuration_energy_variable_audited"),
        method="vacuum_configuration_energy_variable_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
