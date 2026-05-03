# Candidate relaxation energy accounting identity
#
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
from typing import List


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_line(label: str, status: str, detail: str = "") -> None:
    marks = {
        "DERIVED_REDUCED": "PASS",
        "STRUCTURAL": "WARN",
        "CONSTRAINED": "WARN",
        "REQUIRED": "WARN",
        "MISSING": "FAIL",
        "UNRESOLVED": "FAIL",
        "RISK": "WARN",
        "FORBIDDEN": "PASS",
        "CANDIDATE": "WARN",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class RelaxationEnergyRequirement:
    name: str
    requirement: str
    candidate_form: str
    forbidden_form: str
    status: str
    risk: str
    missing: str


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
    status_line(e.name, e.status)
    print(f"Risk: {e.risk}")
    print(f"Missing: {e.missing}")


def case_0_problem_statement():
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

    status_line("relaxation energy accounting problem posed", "REQUIRED")


def case_1_requirement_inventory(entries: List[RelaxationEnergyRequirement]):
    header("Case 1: Relaxation energy requirement inventory")
    for entry in entries:
        print_requirement(entry)


def case_2_compact_table(entries: List[RelaxationEnergyRequirement]):
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

    status_line("compact relaxation energy ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[RelaxationEnergyRequirement]):
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

    status_line("relaxation energy status count produced", "STRUCTURAL")


def case_4_candidate_energy_form():
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

    status_line("candidate kappa energy form stated", "CANDIDATE")


def case_5_required_total_balance():
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

    status_line("required total balance stated", "REQUIRED")


def case_6_failure_controls():
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

    status_line("relaxation energy failure controls stated", "RISK")


def case_7_next_tests():
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

    status_line("next test selected", "STRUCTURAL")


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
    case_0_problem_statement()
    entries = build_requirements()
    case_1_requirement_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_candidate_energy_form()
    case_5_required_total_balance()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
