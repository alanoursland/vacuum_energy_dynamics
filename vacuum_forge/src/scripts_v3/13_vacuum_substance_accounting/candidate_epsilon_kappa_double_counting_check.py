# Candidate epsilon-kappa double-counting check
#
# Purpose
# -------
# The epsilon_vac_config functional audit proposed:
#
#   epsilon_vac_config =
#     1/2 K_zeta (zeta-zeta_min)^2
#     + 1/2 L_zeta |grad zeta|^2
#     + 1/2 K_lock (kappa-(zeta-zeta_min))^2
#
# Existing kappa relaxation accounting also uses:
#
#   e_kappa = 1/2 K_kappa (kappa-kappa_min)^2
#
# Potential problem:
#
#   If epsilon_vac_config contains kappa mismatch energy,
#   and e_kappa is also counted separately,
#   the same trace/volume imbalance may be counted twice.
#
# This script audits whether e_kappa should be inside or outside
# epsilon_vac_config.
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
        "RECOMMENDED": "PASS",
        "REQUIRED": "WARN",
        "MISSING": "FAIL",
        "UNRESOLVED": "FAIL",
        "RISK": "WARN",
        "FORBIDDEN": "PASS",
        "REJECTED": "WARN",
        "DANGER": "FAIL",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class DoubleCountingEntry:
    name: str
    option: str
    accounting_rule: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str


def build_entries() -> List[DoubleCountingEntry]:
    return [
        DoubleCountingEntry(
            name="D1: e_kappa outside epsilon_vac_config",
            option="epsilon_vac_config contains zeta geometry; e_kappa is separate sector relaxation energy",
            accounting_rule="E_total includes epsilon_vac_config + e_kappa once each",
            allowed_if="kappa is an independent relaxation diagnostic not already included in epsilon",
            forbidden_if="epsilon includes K_lock or kappa mismatch representing same energy",
            status="SAFE_IF",
            missing="whether kappa is independent or just zeta mismatch",
        ),
        DoubleCountingEntry(
            name="D2: e_kappa inside epsilon_vac_config",
            option="epsilon_vac_config includes kappa mismatch energy",
            accounting_rule="E_total includes epsilon_vac_config only; do not add e_kappa separately",
            allowed_if="kappa mismatch is part of vacuum configuration energy",
            forbidden_if="e_kappa is also counted as separate energy",
            status="SAFE_IF",
            missing="how Gamma_relax is written when e_kappa is internal",
        ),
        DoubleCountingEntry(
            name="D3: kappa-zeta locking as constraint, not energy",
            option="K_lock -> constraint enforcing kappa = zeta-zeta_min",
            accounting_rule="locking term not counted as physical energy if it is a Lagrange constraint",
            allowed_if="parent/projector defines kappa as diagnostic projection of zeta",
            forbidden_if="finite K_lock counted while also enforcing equality exactly",
            status="CANDIDATE",
            missing="constraint versus penalty interpretation",
        ),
        DoubleCountingEntry(
            name="D4: kappa-zeta locking as penalty energy",
            option="finite K_lock penalty energy included in epsilon_vac_config",
            accounting_rule="locking energy counted inside epsilon; no duplicate e_kappa for same mismatch",
            allowed_if="kappa and zeta can differ physically",
            forbidden_if="creates extra scalar degree of freedom",
            status="RISK",
            missing="degree-of-freedom count and projector identity",
        ),
        DoubleCountingEntry(
            name="D5: Gamma_relax with external e_kappa",
            option="Gamma_relax transfers from e_kappa to epsilon_vac_config",
            accounting_rule="d e_kappa/dtau + d epsilon_vac_config/dtau = 0",
            allowed_if="e_kappa is outside epsilon_vac_config",
            forbidden_if="epsilon already contains e_kappa",
            status="CANDIDATE",
            missing="sign convention and source of relaxation rate",
        ),
        DoubleCountingEntry(
            name="D6: Gamma_relax with internal e_kappa",
            option="Gamma_relax is internal redistribution within epsilon_vac_config",
            accounting_rule="d epsilon_vac_config/dtau accounts for kappa relaxation internally",
            allowed_if="e_kappa included in epsilon_vac_config",
            forbidden_if="additional transfer equation adds same change again",
            status="CANDIDATE",
            missing="internal bookkeeping decomposition",
        ),
        DoubleCountingEntry(
            name="D7: forbidden duplicate total energy",
            option="E_total = epsilon_vac_config + e_kappa when epsilon already includes kappa mismatch",
            accounting_rule="do not do this",
            allowed_if="never",
            forbidden_if="same trace/volume mismatch counted twice",
            status="FORBIDDEN",
            missing="not pursued",
        ),
        DoubleCountingEntry(
            name="D8: forbidden duplicate source response",
            option="rho or trace response creates A mass, zeta charge, and kappa charge independently",
            accounting_rule="source response must be routed once by projectors",
            allowed_if="never unless parent identity forces distinct channels",
            forbidden_if="scalar mass/volume response double-counted",
            status="FORBIDDEN",
            missing="P_recombination and source projector identity",
        ),
        DoubleCountingEntry(
            name="D9: recommended provisional convention",
            option="treat e_kappa outside epsilon_vac_config for now; keep epsilon purely zeta-volume until kappa-zeta map is derived",
            accounting_rule="epsilon_vac_config = zeta displacement + gradient/interface terms; e_kappa separate; no K_lock energy counted yet",
            allowed_if="we label K_lock as diagnostic/constraint target, not physical energy",
            forbidden_if="we need kappa-zeta locking energy to enforce consistency",
            status="RECOMMENDED",
            missing="later revisit after kappa-zeta map",
        ),
        DoubleCountingEntry(
            name="D10: later unified convention",
            option="after kappa-zeta map, absorb e_kappa into epsilon_vac_config or eliminate kappa as independent energy",
            accounting_rule="single trace/volume energy functional",
            allowed_if="parent projector shows kappa is not independent",
            forbidden_if="done before derivation",
            status="STRUCTURAL",
            missing="parent projector / recombination derivation",
        ),
    ]


def print_entry(e: DoubleCountingEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Option: {e.option}")
    print(f"Accounting rule: {e.accounting_rule}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")


def case_0_problem_statement():
    header("Case 0: epsilon-kappa double-counting problem")

    print("Question:")
    print()
    print("  Should e_kappa be inside or outside epsilon_vac_config?")
    print()
    print("Goal:")
    print()
    print("  prevent the same trace/volume mismatch from being counted twice")
    print()
    print("Discipline:")
    print()
    print("  count scalar/trace energy once")
    print("  do not count K_lock twice")
    print("  do not duplicate source response")
    print("  do not treat constraint penalties as physical energy unless derived")
    print("  keep provisional conventions explicit")

    status_line("epsilon-kappa double-counting problem posed", "REQUIRED")


def case_1_inventory(entries: List[DoubleCountingEntry]):
    header("Case 1: Double-counting inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[DoubleCountingEntry]):
    header("Case 2: Compact double-counting ledger")

    print("| Entry | Option | Status | Accounting rule | Missing |")
    print("|---|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.option.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.accounting_rule.replace("|", "/")
            + " | "
            + e.missing.replace("|", "/")
            + " |"
        )

    status_line("compact double-counting ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[DoubleCountingEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Both inside and outside conventions are possible.")
    print("  The safest provisional convention is to keep e_kappa outside epsilon_vac_config.")
    print("  K_lock should remain diagnostic/constraint-like until the kappa-zeta map is derived.")

    status_line("double-counting status count produced", "STRUCTURAL")


def case_4_recommended_convention():
    header("Case 4: Recommended provisional convention")

    print("Recommended for now:")
    print()
    print("  epsilon_vac_config contains:")
    print("    1/2 K_zeta (zeta-zeta_min)^2")
    print("    1/2 L_zeta |grad zeta|^2")
    print()
    print("  e_kappa remains separate:")
    print("    e_kappa = 1/2 K_kappa (kappa-kappa_min)^2")
    print()
    print("  K_lock is not counted as physical energy yet.")
    print("  Treat K_lock as a diagnostic/constraint target.")
    print()
    print("Reason:")
    print("  the kappa-zeta map is not derived, so combining them risks double-counting.")

    status_line("recommended provisional convention stated", "RECOMMENDED")


def case_5_forbidden_patterns():
    header("Case 5: Forbidden patterns")

    print("Forbidden:")
    print()
    print("1. epsilon includes kappa mismatch and E_total also adds e_kappa.")
    print("2. K_lock enforces equality exactly and is also counted as finite energy.")
    print("3. rho contributes to A mass, zeta exterior charge, and kappa exterior charge.")
    print("4. Gamma_relax transfers energy between two terms that are already the same term.")
    print("5. Recombination counts zeta and kappa as independent scalar gravity sectors.")

    status_line("forbidden double-counting patterns stated", "FORBIDDEN")


def case_6_updated_functional():
    header("Case 6: Updated provisional functional")

    print("Provisional epsilon_vac_config:")
    print()
    print("  epsilon_vac_config =")
    print("    1/2 K_zeta (zeta-zeta_min)^2")
    print("    + 1/2 L_zeta |grad zeta|^2")
    print()
    print("Separate kappa relaxation energy:")
    print()
    print("  e_kappa = 1/2 K_kappa (kappa-kappa_min)^2")
    print()
    print("Provisional exchange accounting:")
    print()
    print("  d e_kappa/dtau + d epsilon_vac_config/dtau = 0")
    print()
    print("Constraint target:")
    print()
    print("  kappa ~ zeta - zeta_min")
    print()
    print("but no K_lock energy counted until derived.")

    status_line("updated provisional functional stated", "CANDIDATE")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_epsilon_kappa_double_counting_check.md")
    print("   Artifact for this script.")
    print()
    print("2. vacuum_substance_accounting_summary.md")
    print("   Summarize group 13 after resolving provisional accounting.")
    print()
    print("3. candidate_kappa_zeta_map.py")
    print("   Directly test whether kappa equals/proxies zeta-zeta_min.")
    print()
    print("Recommended next:")
    print()
    print("  vacuum_substance_accounting_summary.md")
    print()
    print("Reason:")
    print("  Group 13 has reached a natural summary point with a provisional accounting convention.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("To avoid double-counting:")
    print()
    print("  keep e_kappa outside epsilon_vac_config for now")
    print("  keep epsilon_vac_config as zeta displacement plus gradient/interface terms")
    print("  treat K_lock as diagnostic/constraint target, not physical energy")
    print("  revisit after the kappa-zeta map is derived")
    print()
    print("Possible next artifact:")
    print("  candidate_epsilon_kappa_double_counting_check.md")
    print()
    print("Recommended next:")
    print("  vacuum_substance_accounting_summary.md")


def main():
    header("Candidate Epsilon Kappa Double Counting Check")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_recommended_convention()
    case_5_forbidden_patterns()
    case_6_updated_functional()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
