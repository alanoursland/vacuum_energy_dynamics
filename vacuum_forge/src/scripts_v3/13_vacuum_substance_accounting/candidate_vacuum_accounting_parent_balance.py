# Candidate vacuum accounting parent balance
#
# Purpose
# -------
# The vacuum transport current constraints audit allowed J_v only as:
#
#   absent/local exchange,
#   compact support current,
#   constraint redistribution with zero exterior flux,
#   causal transport if separately derived.
#
# It forbade J_v as:
#
#   acausal repair current,
#   far-zone scalar radiation current,
#   coefficient tuning knob,
#   exterior mass-changing current.
#
# The next target is a concrete balance skeleton:
#
#   u^mu nabla_mu epsilon_vac_config + nabla_mu J_v^mu
#     = Sigma_exchange - Gamma_relax
#
# with ordinary closed conditions:
#
#   Sigma_creation = 0
#   boundary J_v flux = 0
#   Q_volume = 0
#   delta M_ext = 0
#   F_scalar_far = 0
#
# This script audits that parent-balance skeleton.
#
# It is not a derivation.

from dataclasses import dataclass
from typing import List


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_line(label: str, status: str, detail: str = "") -> None:
    marks = {
        "SAFE_IF": "WARN",
        "CANDIDATE": "WARN",
        "STRUCTURAL": "WARN",
        "CONSTRAINED": "WARN",
        "REQUIRED": "WARN",
        "MISSING": "FAIL",
        "UNRESOLVED": "FAIL",
        "RISK": "WARN",
        "FORBIDDEN": "PASS",
        "REJECTED": "WARN",
        "DANGER": "FAIL",
        "THEOREM_TARGET": "WARN",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class BalanceEntry:
    name: str
    term: str
    role: str
    required_condition: str
    forbidden_failure: str
    status: str
    missing: str


def build_entries() -> List[BalanceEntry]:
    return [
        BalanceEntry(
            name="PB1: volume configuration density",
            term="epsilon_vac_config",
            role="local geometric vacuum-spacetime configuration variable, likely built from zeta=ln sqrt(gamma)",
            required_condition="geometric definition, not thermodynamic bucket",
            forbidden_failure="repair reservoir or coefficient tuning functional",
            status="CANDIDATE",
            missing="functional definition from zeta/kappa/volume form",
        ),
        BalanceEntry(
            name="PB2: flow derivative",
            term="u^mu nabla_mu epsilon_vac_config",
            role="local rate of vacuum-configuration change along chosen frame/flow",
            required_condition="u^mu defined or replaced by covariant/constraint operator",
            forbidden_failure="bare coordinate time derivative with hidden frame",
            status="UNRESOLVED",
            missing="u^mu or foliation/volume current",
        ),
        BalanceEntry(
            name="PB3: vacuum configuration current",
            term="nabla_mu J_v^mu",
            role="optional compact/constrained/causal redistribution term",
            required_condition="zero exterior flux and no far-zone scalar energy",
            forbidden_failure="acausal repair current or scalar radiation current",
            status="CANDIDATE",
            missing="J_v class selection and support law",
        ),
        BalanceEntry(
            name="PB4: exchange source",
            term="Sigma_exchange",
            role="matter/vacuum-spacetime configuration coupling",
            required_condition="geometric/projector-derived, not free knob",
            forbidden_failure="duplicates A-sector mass source or acts as arbitrary source",
            status="UNRESOLVED",
            missing="mass-acceleration-gradient or trace-volume coupling expression",
        ),
        BalanceEntry(
            name="PB5: relaxation term",
            term="Gamma_relax",
            role="internal restoration/conversion between e_kappa and epsilon_vac_config",
            required_condition="exchange/restoration, not destruction",
            forbidden_failure="damping sink or Sigma_creation in ordinary gravity",
            status="CONSTRAINED",
            missing="sign convention and relation to e_kappa",
        ),
        BalanceEntry(
            name="PB6: active creation exclusion",
            term="Sigma_creation = 0",
            role="ordinary closed-regime condition",
            required_condition="no nonconservative creation/destruction in ordinary gravity",
            forbidden_failure="active-regime leakage into ordinary sector",
            status="REQUIRED",
            missing="active-regime trigger/exclusion law",
        ),
        BalanceEntry(
            name="PB7: boundary flux zero",
            term="surface integral J_v dot dS at R+ = 0",
            role="prevents vacuum configuration current from leaking into exterior scalar charge",
            required_condition="zero exterior boundary flux",
            forbidden_failure="zeta/kappa exterior 1/r tail",
            status="REQUIRED",
            missing="boundary/interface law",
        ),
        BalanceEntry(
            name="PB8: zero volume charge",
            term="Q_volume = 0",
            role="prevents exterior volume scalar monopole",
            required_condition="compact support or compensated source",
            forbidden_failure="uncompensated scalar charge",
            status="REQUIRED",
            missing="S_volume and compensation law",
        ),
        BalanceEntry(
            name="PB9: A-sector mass protected",
            term="delta M_ext = 0",
            role="keeps exterior mass tied to A_flux, not volume accounting",
            required_condition="volume/kappa/J_v terms do not alter A exterior coefficient",
            forbidden_failure="boundary/vacuum transport tunes measured mass",
            status="REQUIRED",
            missing="boundary mass preservation theorem",
        ),
        BalanceEntry(
            name="PB10: no far-zone scalar flux",
            term="F_scalar_far = 0",
            role="binary-radiation safety condition",
            required_condition="ordinary far-zone energy loss remains TT-only",
            forbidden_failure="scalar orbital damping or scalar radiation",
            status="REQUIRED",
            missing="radiation flux proof after coupling selection",
        ),
        BalanceEntry(
            name="PB11: recombination separation",
            term="P_recombination",
            role="keeps A mass response, volume zeta/kappa, W_i, and h_TT counted once",
            required_condition="no scalar double-counting",
            forbidden_failure="zeta/kappa duplicates A-sector mass",
            status="MISSING",
            missing="recombination projector identity",
        ),
        BalanceEntry(
            name="PB12: parent identity embedding",
            term="Div E_parent = B_closed + B_relax",
            role="eventual embedding of accounting balance in field-equation parent structure",
            required_condition="balance is derived from parent identity rather than appended",
            forbidden_failure="decorative balance law",
            status="MISSING",
            missing="E_parent, B_closed, B_relax definitions",
        ),
    ]


def print_entry(e: BalanceEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Term: {e.term}")
    print(f"Role: {e.role}")
    print(f"Required condition: {e.required_condition}")
    print(f"Forbidden failure: {e.forbidden_failure}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")


def case_0_problem_statement():
    header("Case 0: Vacuum accounting parent balance problem")

    print("Question:")
    print()
    print("  Can we write a concrete vacuum-substance accounting balance skeleton?")
    print()
    print("Candidate skeleton:")
    print()
    print("  u^mu nabla_mu epsilon_vac_config + nabla_mu J_v^mu")
    print("    = Sigma_exchange - Gamma_relax")
    print()
    print("Ordinary closed conditions:")
    print()
    print("  Sigma_creation = 0")
    print("  boundary J_v flux = 0")
    print("  Q_volume = 0")
    print("  delta M_ext = 0")
    print("  F_scalar_far = 0")
    print()
    print("Discipline:")
    print()
    print("  no repair reservoir")
    print("  no free Sigma_exchange knob")
    print("  no scalar far-zone radiation")
    print("  no exterior mass change")
    print("  no decorative parent balance")

    status_line("vacuum accounting parent balance problem posed", "REQUIRED")


def case_1_inventory(entries: List[BalanceEntry]):
    header("Case 1: Parent balance term inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[BalanceEntry]):
    header("Case 2: Compact parent balance ledger")

    print("| Entry | Term | Status | Required condition | Missing |")
    print("|---|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.term.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.required_condition.replace("|", "/")
            + " | "
            + e.missing.replace("|", "/")
            + " |"
        )

    status_line("compact parent balance ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[BalanceEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  The balance skeleton is now explicit enough to audit.")
    print("  Most boundary/safety conditions are required.")
    print("  The central missing definitions are epsilon_vac_config, Sigma_exchange, u^mu, and parent embedding.")

    status_line("parent balance status count produced", "STRUCTURAL")


def case_4_balance_skeleton():
    header("Case 4: Candidate balance skeleton")

    print("Candidate local/constrained balance:")
    print()
    print("  u^mu nabla_mu epsilon_vac_config + nabla_mu J_v^mu")
    print("    = Sigma_exchange - Gamma_relax")
    print()
    print("with:")
    print()
    print("  epsilon_vac_config ~ F(zeta, zeta_min, kappa, ...)")
    print("  zeta = ln sqrt(gamma)")
    print("  Gamma_relax exchanges with e_kappa")
    print("  J_v absent, compact, constrained, or causal if derived")
    print()
    print("ordinary closed regime:")
    print()
    print("  Sigma_creation = 0")
    print()
    print("exterior safety:")
    print()
    print("  surface J_v dot dS = 0")
    print("  Q_volume = 0")
    print("  delta M_ext = 0")
    print("  F_scalar_far = 0")

    status_line("candidate balance skeleton stated", "CANDIDATE")


def case_5_sign_interpretation():
    header("Case 5: Sign interpretation")

    print("One possible sign convention:")
    print()
    print("  Gamma_relax > 0:")
    print("    relaxation consumes kappa imbalance and deposits into epsilon_vac_config")
    print()
    print("  Sigma_exchange > 0:")
    print("    matter/geometry coupling increases epsilon_vac_config")
    print()
    print("But signs are not fixed yet.")
    print()
    print("Required:")
    print()
    print("  curvature excess/deficit exchange must be geometric accounting")
    print("  not energy deletion")
    print("  not active creation in ordinary gravity")

    status_line("sign interpretation stated", "CANDIDATE")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("The parent balance skeleton fails if:")
    print()
    print("1. epsilon_vac_config remains undefined.")
    print("2. u^mu is a hidden preferred frame.")
    print("3. J_v becomes acausal repair transport.")
    print("4. Sigma_exchange becomes a free knob.")
    print("5. Gamma_relax becomes energy destruction.")
    print("6. Sigma_creation leaks into ordinary gravity.")
    print("7. boundary J_v flux is nonzero.")
    print("8. Q_volume becomes nonzero.")
    print("9. M_ext changes under vacuum accounting.")
    print("10. scalar far-zone flux appears.")
    print("11. parent embedding remains decorative.")

    status_line("parent balance failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_vacuum_accounting_parent_balance.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_epsilon_vac_config_functional.py")
    print("   Try a concrete functional epsilon_vac_config = F(zeta, zeta_min, gradients, kappa).")
    print()
    print("3. vacuum_substance_accounting_summary.md")
    print("   Summarize group 13 so far.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_epsilon_vac_config_functional.py")
    print()
    print("Reason:")
    print("  The balance skeleton now depends explicitly on epsilon_vac_config; define the functional next.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("The first concrete vacuum-accounting skeleton is:")
    print()
    print("  u^mu nabla_mu epsilon_vac_config + nabla_mu J_v^mu")
    print("    = Sigma_exchange - Gamma_relax")
    print()
    print("with ordinary constraints:")
    print()
    print("  Sigma_creation = 0")
    print("  boundary J_v flux = 0")
    print("  Q_volume = 0")
    print("  delta M_ext = 0")
    print("  F_scalar_far = 0")
    print()
    print("The next missing object is:")
    print("  epsilon_vac_config = F(zeta, zeta_min, gradients, kappa, ...)")
    print()
    print("Possible next artifact:")
    print("  candidate_vacuum_accounting_parent_balance.md")
    print()
    print("Possible next script:")
    print("  candidate_epsilon_vac_config_functional.py")


def main():
    header("Candidate Vacuum Accounting Parent Balance")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_balance_skeleton()
    case_5_sign_interpretation()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
