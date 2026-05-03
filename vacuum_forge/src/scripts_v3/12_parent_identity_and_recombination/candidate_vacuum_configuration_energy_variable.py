# Candidate vacuum configuration energy variable
#
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

from dataclasses import dataclass
from typing import List


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_line(label: str, status: str, detail: str = "") -> None:
    marks = {
        "CANDIDATE": "WARN",
        "STRUCTURAL": "WARN",
        "CONSTRAINED": "WARN",
        "REQUIRED": "WARN",
        "MISSING": "FAIL",
        "UNRESOLVED": "FAIL",
        "RISK": "WARN",
        "FORBIDDEN": "PASS",
        "REJECTED": "WARN",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


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
    status_line(v.name, v.status)
    print(f"Risk: {v.risk}")
    print(f"Missing: {v.missing}")


def case_0_problem_statement():
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

    status_line("vacuum configuration variable problem posed", "REQUIRED")


def case_1_candidate_inventory(entries: List[VacuumVariableCandidate]):
    header("Case 1: Vacuum variable candidate inventory")
    for entry in entries:
        print_candidate(entry)


def case_2_compact_table(entries: List[VacuumVariableCandidate]):
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

    status_line("compact vacuum variable ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[VacuumVariableCandidate]):
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

    status_line("vacuum variable status count produced", "STRUCTURAL")


def case_4_candidate_minimal_accounting():
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

    status_line("candidate minimal vacuum accounting stated", "CANDIDATE")


def case_5_repair_reservoir_tests():
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

    status_line("no-repair-reservoir tests stated", "RISK")


def case_6_best_current_choice():
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

    status_line("best current vacuum variable choice stated", "STRUCTURAL")


def case_7_next_tests():
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

    status_line("next test selected", "STRUCTURAL")


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
    case_0_problem_statement()
    entries = build_candidates()
    case_1_candidate_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_candidate_minimal_accounting()
    case_5_repair_reservoir_tests()
    case_6_best_current_choice()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
