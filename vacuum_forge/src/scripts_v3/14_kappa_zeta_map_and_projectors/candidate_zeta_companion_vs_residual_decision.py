# Candidate zeta companion versus residual decision
#
# Purpose
# -------
# The minimal volume-exchange operator ansatz found:
#
#   Minimal V shells can be written, but the decisive issue is zeta status.
#
# If zeta fixes B_s:
#
#   it cannot remain independent residual trace.
#
# If zeta remains residual:
#
#   it probably does not fix q.
#
# This script decides whether zeta can be B_s companion or residual, but not both.
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
        "THEOREM_TARGET": "WARN",
        "RECOVERY_TARGET": "WARN",
        "BRANCH_KILLED": "FAIL",
        "DEFER": "WARN",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class ZetaStatusEntry:
    name: str
    status_branch: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[ZetaStatusEntry]:
    return [
        ZetaStatusEntry(
            name="ZS1: zeta as B_s companion",
            status_branch="zeta supplies the A_spatial volume response / B_s companion",
            role="possible solution to q-origin through volume exchange",
            allowed_if="zeta residual metric trace is killed or made non-metric",
            forbidden_if="zeta also remains independent residual trace",
            status="CANDIDATE",
            missing="zeta-B_s identity and coefficient origin",
            consequence="could solve A_spatial branch but collapses residual-zeta convention",
        ),
        ZetaStatusEntry(
            name="ZS2: zeta as residual only",
            status_branch="zeta remains boundary-neutral residual / relaxation variable",
            role="preserves previous residual convention",
            allowed_if="zeta is not used to fix B_s or q",
            forbidden_if="zeta also supplies A_spatial companion",
            status="SAFE_IF",
            missing="separate A_spatial q-origin",
            consequence="does not solve A_spatial ratio; A_spatial remains theorem target or needs another origin",
        ),
        ZetaStatusEntry(
            name="ZS3: zeta as both companion and residual",
            status_branch="zeta fixes B_s and remains independent residual trace",
            role="forbidden double-counting branch",
            allowed_if="never in current architecture",
            forbidden_if="used to solve q while preserving residual trace",
            status="REJECTED",
            missing="not pursued",
            consequence="violates count-once recombination",
        ),
        ZetaStatusEntry(
            name="ZS4: zeta as non-metric bookkeeping",
            status_branch="zeta tracks vacuum configuration but does not enter metric trace independently",
            role="possible compromise if zeta participates in exchange but not residual metric trace",
            allowed_if="metric insertion is through B_s only",
            forbidden_if="zeta also appears as separate scalar metric component",
            status="CANDIDATE",
            missing="bookkeeping-to-metric map",
            consequence="may allow volume exchange without exterior scalar charge",
        ),
        ZetaStatusEntry(
            name="ZS5: zeta companion coefficient theorem target",
            status_branch="B_s = F_zeta[A,zeta] fixes q before recovery checks",
            role="core theorem target if zeta becomes companion",
            allowed_if="F_zeta is derived from volume exchange operator",
            forbidden_if="F_zeta coefficient is chosen from gamma_like or AB",
            status="THEOREM_TARGET",
            missing="F_zeta / V operator derivation",
            consequence="decides whether zeta companion branch solves A_spatial",
        ),
        ZetaStatusEntry(
            name="ZS6: no-overlap requirement",
            status_branch="O[B_s,zeta_residual/kappa_residual] = 0 or residual killed",
            role="protects count-once trace theorem",
            allowed_if="operator is explicit or residual is non-metric",
            forbidden_if="overlap is asserted without consequence",
            status="REQUIRED",
            missing="overlap operator or residual kill theorem",
            consequence="required for either companion or residual branch",
        ),
        ZetaStatusEntry(
            name="ZS7: boundary neutrality requirement",
            status_branch="zeta residual has Q_ext=0; companion contribution absorbed into B_s",
            role="prevents exterior scalar charge",
            allowed_if="neutrality theorem or absorption into A_spatial is explicit",
            forbidden_if="zeta creates exterior scalar charge",
            status="REQUIRED",
            missing="boundary neutrality theorem",
            consequence="protects no scalar gravity / exterior mass result",
        ),
        ZetaStatusEntry(
            name="ZS8: kappa residual consequence",
            status_branch="if zeta becomes companion, kappa residual must be diagnostic/non-metric or separately neutral",
            role="downstream cleanup for kappa status",
            allowed_if="kappa does not reintroduce overlapping scalar trace",
            forbidden_if="kappa restores the killed residual zeta trace",
            status="CONSTRAINED",
            missing="kappa after zeta status decision",
            consequence="likely triggers kappa_diagnostic_or_residual_after_zeta script",
        ),
        ZetaStatusEntry(
            name="ZS9: P_relax consequence",
            status_branch="if zeta remains residual, P_relax may own its first-order relaxation",
            role="keeps relaxation separate from A_spatial q-origin",
            allowed_if="P_relax is boundary-neutral and non-radiative",
            forbidden_if="relaxation is used as coefficient patch for B_s",
            status="SAFE_IF",
            missing="P_relax definition",
            consequence="preserves residual track but leaves A_spatial unresolved",
        ),
        ZetaStatusEntry(
            name="ZS10: recovery checks downstream",
            status_branch="after zeta status and q-origin are fixed, test gamma_like and AB",
            role="ordinary-regime recovery tests",
            allowed_if="checked after structural choice",
            forbidden_if="used to choose zeta status",
            status="RECOVERY_TARGET",
            missing="solutions after zeta status decision",
            consequence="keeps recovery from becoming construction",
        ),
        ZetaStatusEntry(
            name="ZS11: zeta patch failure",
            status_branch="zeta selected as companion only because it can fit recovery targets",
            role="rejected shortcut",
            allowed_if="used only as no-go diagnosis",
            forbidden_if="accepted as ontology",
            status="REJECTED",
            missing="not pursued",
            consequence="kills zeta-companion route if no exchange law derives it",
        ),
        ZetaStatusEntry(
            name="ZS12: recommended provisional decision",
            status_branch="zeta cannot be both; provisional fork must be explicit before more V work",
            role="best current governance rule",
            allowed_if="next scripts carry branch labels companion/residual/non-metric",
            forbidden_if="continuing with ambiguous zeta status",
            status="RECOMMENDED",
            missing="branch selection by later derivation",
            consequence="next script should test the companion branch first or return A_spatial to theorem target",
        ),
    ]


def print_entry(e: ZetaStatusEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Status branch: {e.status_branch}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Zeta companion versus residual decision problem")

    print("Question:")
    print()
    print("  Can zeta be B_s companion or residual, but not both?")
    print()
    print("Goal:")
    print()
    print("  split zeta status before adding more volume-exchange structure")
    print()
    print("Discipline:")
    print()
    print("  do not let zeta fix B_s and remain residual")
    print("  do not choose zeta status from gamma_like or AB")
    print("  preserve boundary neutrality")
    print("  preserve count-once no-overlap")
    print("  expose consequences for kappa and P_relax")
    print("  keep A_spatial as theorem target if zeta remains residual")

    status_line("zeta companion/residual decision problem posed", "REQUIRED")


def case_1_inventory(entries: List[ZetaStatusEntry]):
    header("Case 1: Zeta status inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[ZetaStatusEntry]):
    header("Case 2: Compact zeta-status ledger")

    print("| Entry | Status branch | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.status_branch.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact zeta-status ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[ZetaStatusEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Zeta as both companion and residual is rejected.")
    print("  Zeta as companion could solve A_spatial, but kills/respecifies residual zeta trace.")
    print("  Zeta as residual preserves accounting but probably does not solve q-origin.")
    print("  Boundary neutrality and no-overlap are mandatory either way.")

    status_line("zeta-status count produced", "STRUCTURAL")


def case_4_decision_tree():
    header("Case 4: Zeta status decision tree")

    print("Decision tree:")
    print()
    print("1. Does zeta fix B_s/q through V?")
    print("   If yes: zeta is companion or non-metric bookkeeping, not independent residual trace.")
    print()
    print("2. Does zeta remain residual?")
    print("   If yes: it cannot be used to fix B_s/q.")
    print()
    print("3. Does zeta need to carry relaxation?")
    print("   If yes: relaxation belongs to P_relax, not A_spatial q-origin.")
    print()
    print("4. Does either branch create exterior scalar charge?")
    print("   If yes: reject ordinary-sector branch.")
    print()
    print("5. Does either branch overlap B_s and residual trace?")
    print("   If yes: reject or kill residual metric trace.")

    status_line("zeta decision tree stated", "RECOMMENDED")


def case_5_good_failure():
    header("Case 5: Good failure / fork result")

    print("Good failure:")
    print()
    print("  zeta cannot derive B_s/q without becoming the B_s companion,")
    print("  and keeping zeta residual-only leaves A_spatial unresolved.")
    print()
    print("Consequence:")
    print()
    print("  A_spatial remains recovery theorem target,")
    print("  or zeta companion branch must be pursued with residual zeta killed/non-metric.")
    print()
    print("Bad failure:")
    print("  keep zeta ambiguous and use it whenever convenient.")

    status_line("zeta fork good failure stated", "DEFER")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("Zeta status decision fails if:")
    print()
    print("1. zeta fixes B_s and remains independent residual trace")
    print("2. zeta status is chosen from gamma_like")
    print("3. zeta status is chosen from AB diagnostic")
    print("4. boundary neutrality is ignored")
    print("5. no-overlap theorem is ignored")
    print("6. kappa reintroduces killed zeta residual trace")
    print("7. P_relax is used as coefficient patch")
    print("8. A_spatial is claimed derived while zeta status remains ambiguous")

    status_line("zeta-status failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_zeta_companion_vs_residual_decision.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_zeta_companion_branch_test.py")
    print("   Test the branch where zeta becomes B_s companion and residual trace is killed/non-metric.")
    print()
    print("3. candidate_A_spatial_theorem_target_after_zeta_residual.py")
    print("   If zeta remains residual, return A_spatial to theorem target status.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_zeta_companion_branch_test.py")
    print()
    print("Reason:")
    print("  The only branch that might solve q-origin is zeta as companion. Test it explicitly, with residual zeta trace killed or made non-metric.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("Zeta cannot be both companion and residual.")
    print()
    print("If zeta is companion:")
    print("  residual zeta trace must be killed or made non-metric.")
    print()
    print("If zeta is residual:")
    print("  A_spatial/q-origin remains unresolved.")
    print()
    print("Best next test:")
    print("  candidate_zeta_companion_branch_test.py")


def main():
    header("Candidate Zeta Companion Versus Residual Decision")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_decision_tree()
    case_5_good_failure()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
