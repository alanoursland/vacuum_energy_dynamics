# Candidate zeta companion branch test
#
# Purpose
# -------
# The zeta companion/residual decision found:
#
#   zeta cannot be both companion and residual.
#
# If zeta is companion:
#
#   residual zeta trace must be killed or made non-metric.
#
# If zeta is residual:
#
#   A_spatial/q-origin remains unresolved.
#
# This script tests the companion branch explicitly.
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
class ZetaCompanionEntry:
    name: str
    branch: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[ZetaCompanionEntry]:
    return [
        ZetaCompanionEntry(
            name="ZC1: companion branch target",
            branch="B_s = F_zeta[A,zeta] fixes A_spatial/q-origin before recovery checks",
            role="core theorem target for zeta companion branch",
            allowed_if="F_zeta is derived from volume-exchange law",
            forbidden_if="F_zeta coefficient is chosen from gamma_like or AB",
            status="THEOREM_TARGET",
            missing="explicit F_zeta / V derivation",
            consequence="decides whether zeta companion branch solves A_spatial",
        ),
        ZetaCompanionEntry(
            name="ZC2: algebraic companion map",
            branch="B_s = lambda_z zeta + G[A]",
            role="minimal test map from volume variable to spatial companion",
            allowed_if="lambda_z and G are derived before recovery checks",
            forbidden_if="lambda_z is tuned to gamma_like",
            status="RISK",
            missing="lambda_z origin and gauge status",
            consequence="can easily become coefficient patch unless derived",
        ),
        ZetaCompanionEntry(
            name="ZC3: derivative companion map",
            branch="Delta B_s = r_z Delta zeta + H[A,S_A]",
            role="differential version of zeta companion relation",
            allowed_if="r_z follows from exchange operator",
            forbidden_if="r_z chosen to match q",
            status="CANDIDATE",
            missing="exchange operator and r_z origin",
            consequence="may connect volume dynamics to A_spatial without direct algebraic identification",
        ),
        ZetaCompanionEntry(
            name="ZC4: source-driven companion map",
            branch="Sigma_V[A,T] drives zeta, and zeta drives B_s",
            role="postulate-facing branch tied to source-driven volume creation",
            allowed_if="Sigma_V is expressed before recovery checks",
            forbidden_if="source term is added to repair A_spatial",
            status="CANDIDATE",
            missing="source-driven volume creation law",
            consequence="connects to mass/source coupling but remains underdefined",
        ),
        ZetaCompanionEntry(
            name="ZC5: residual zeta trace killed",
            branch="zeta has no independent residual metric trace after becoming B_s companion",
            role="mandatory no-double-counting consequence",
            allowed_if="residual zeta is killed, non-metric, or pure bookkeeping",
            forbidden_if="zeta remains separate scalar metric residual",
            status="REQUIRED",
            missing="residual kill/non-metric theorem",
            consequence="collapses or revises previous residual-zeta convention",
        ),
        ZetaCompanionEntry(
            name="ZC6: non-metric zeta bookkeeping",
            branch="zeta remains vacuum configuration variable but metric insertion occurs only through B_s",
            role="possible safe version of companion branch",
            allowed_if="bookkeeping-to-metric map is explicit",
            forbidden_if="zeta also appears as metric trace",
            status="CANDIDATE",
            missing="bookkeeping-to-metric map",
            consequence="preserves ontology while avoiding exterior scalar charge",
        ),
        ZetaCompanionEntry(
            name="ZC7: no-overlap requirement",
            branch="O[B_s,zeta_residual/kappa_residual] = 0 or residual killed",
            role="protects count-once recombination",
            allowed_if="operator exists or residual is killed/non-metric",
            forbidden_if="overlap is asserted without consequence",
            status="REQUIRED",
            missing="overlap operator / residual status theorem",
            consequence="branch fails if B_s and residual trace overlap",
        ),
        ZetaCompanionEntry(
            name="ZC8: boundary neutrality requirement",
            branch="companion contribution absorbed into B_s; no independent zeta exterior charge",
            role="protects exterior no-scalar-charge result",
            allowed_if="zeta charge is absent or not independent of A_spatial",
            forbidden_if="zeta companion creates separate exterior scalar charge",
            status="REQUIRED",
            missing="boundary neutrality theorem",
            consequence="prevents zeta companion from becoming scalar gravity",
        ),
        ZetaCompanionEntry(
            name="ZC9: kappa consequence",
            branch="kappa must remain diagnostic/non-metric or separately neutral after zeta companion choice",
            role="prevents kappa from restoring killed residual trace",
            allowed_if="kappa does not become independent overlapping scalar trace",
            forbidden_if="kappa becomes residual substitute for killed zeta trace",
            status="CONSTRAINED",
            missing="post-zeta kappa status",
            consequence="requires later kappa cleanup script",
        ),
        ZetaCompanionEntry(
            name="ZC10: recovery checks downstream",
            branch="after F_zeta/q-origin fixed, test gamma_like and AB",
            role="ordinary-regime recovery targets",
            allowed_if="checked after companion map is derived",
            forbidden_if="used to choose zeta map coefficients",
            status="RECOVERY_TARGET",
            missing="solutions after companion map",
            consequence="tests but does not define the companion branch",
        ),
        ZetaCompanionEntry(
            name="ZC11: zeta companion patch failure",
            branch="zeta selected as companion only because it can fit recovery targets",
            role="rejected shortcut",
            allowed_if="used only as no-go diagnosis",
            forbidden_if="accepted as derivation",
            status="REJECTED",
            missing="not pursued",
            consequence="kills companion branch if no exchange law derives F_zeta",
        ),
        ZetaCompanionEntry(
            name="ZC12: recommended next move",
            branch="test minimal F_zeta maps and residual-kill theorem together",
            role="best current concrete test",
            allowed_if="companion and residual-kill requirements are tested as one package",
            forbidden_if="testing F_zeta while leaving residual trace ambiguous",
            status="RECOMMENDED",
            missing="minimal F_zeta map inventory",
            consequence="next script should inventory F_zeta candidate maps and branch-kill criteria",
        ),
    ]


def print_entry(e: ZetaCompanionEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Branch: {e.branch}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Zeta companion branch test problem")

    print("Question:")
    print()
    print("  Can zeta become the B_s companion without leaving residual trace-gremlins behind?")
    print()
    print("Goal:")
    print()
    print("  test the only branch that might solve A_spatial/q-origin")
    print()
    print("Discipline:")
    print()
    print("  derive F_zeta before recovery checks")
    print("  kill or make non-metric residual zeta trace")
    print("  preserve no-overlap")
    print("  preserve boundary neutrality")
    print("  expose consequences for kappa")
    print("  reject zeta as recovery patch")

    status_line("zeta companion branch problem posed", "REQUIRED")


def case_1_inventory(entries: List[ZetaCompanionEntry]):
    header("Case 1: Zeta companion branch inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[ZetaCompanionEntry]):
    header("Case 2: Compact zeta-companion ledger")

    print("| Entry | Branch | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.branch.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact zeta-companion ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[ZetaCompanionEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Zeta companion branch is viable only if F_zeta is derived.")
    print("  Residual zeta metric trace must be killed or made non-metric.")
    print("  Algebraic maps are risky because coefficients can become recovery patches.")
    print("  Differential/source-driven maps are candidates but need explicit exchange law.")
    print("  Kappa cleanup becomes mandatory if zeta residual trace is killed.")

    status_line("zeta-companion status count produced", "STRUCTURAL")


def case_4_companion_requirements():
    header("Case 4: Companion branch requirements")

    print("A valid zeta companion branch must provide:")
    print()
    print("1. explicit F_zeta[A,zeta] or differential companion map")
    print("2. coefficient origin before gamma/AB checks")
    print("3. residual zeta trace killed or non-metric")
    print("4. boundary neutrality")
    print("5. no-overlap with kappa/residual sectors")
    print("6. kappa status cleanup")
    print("7. recovery checks downstream")
    print()
    print("Missing any of these leaves zeta as a patch, not a companion.")

    status_line("zeta companion requirements stated", "REQUIRED")


def case_5_good_failure():
    header("Case 5: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  no F_zeta map can be derived without tuning,")
    print("  or F_zeta requires residual zeta trace to remain metric-active.")
    print()
    print("Consequence:")
    print()
    print("  zeta companion branch fails.")
    print("  A_spatial returns to recovery theorem target status,")
    print("  while zeta may remain residual under P_relax if neutral and non-radiative.")
    print()
    print("Bad failure:")
    print("  use zeta as companion but quietly keep residual trace.")

    status_line("zeta companion good failure stated", "DEFER")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("Zeta companion branch fails if:")
    print()
    print("1. F_zeta is not written")
    print("2. F_zeta coefficient is chosen from gamma_like")
    print("3. AB diagnostic chooses F_zeta")
    print("4. residual zeta trace remains metric-active")
    print("5. boundary neutrality is absent")
    print("6. no-overlap theorem is absent")
    print("7. kappa restores killed residual trace")
    print("8. source-driven volume creation remains unnamed")

    status_line("zeta companion failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_zeta_companion_branch_test.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_F_zeta_companion_map_inventory.py")
    print("   Inventory possible F_zeta[A,zeta] maps and coefficient-origin constraints.")
    print()
    print("3. candidate_kappa_diagnostic_or_residual_after_zeta.py")
    print("   Clean up kappa after zeta residual trace is killed/non-metric.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_F_zeta_companion_map_inventory.py")
    print()
    print("Reason:")
    print("  The companion branch now depends on deriving F_zeta. Inventory map forms before kappa cleanup.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("Zeta companion branch is the only live branch that might solve q-origin.")
    print()
    print("It survives only if:")
    print("  F_zeta is derived,")
    print("  residual zeta trace is killed/non-metric,")
    print("  boundary neutrality and no-overlap hold.")
    print()
    print("Best next test:")
    print("  candidate_F_zeta_companion_map_inventory.py")


def main():
    header("Candidate Zeta Companion Branch Test")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_companion_requirements()
    case_5_good_failure()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
