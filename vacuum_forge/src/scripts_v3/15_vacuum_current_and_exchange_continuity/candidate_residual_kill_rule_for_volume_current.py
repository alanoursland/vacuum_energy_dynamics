# Candidate residual-kill rule for volume current
#
# Purpose
# -------
# The Group 15 current-subchain status summary found:
#
#   The safest provisional convention is residual-kill / non-metric residual
#   if J_V-driven zeta enters B_s.
#
# This script tests that cleanest safe convention:
#
#   if J_V-driven zeta enters B_s,
#   then residual zeta/kappa metric trace is killed or made non-metric.
#
# It is not a derivation of residual-kill.
# It is a safety convention audit.

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
        "CLOSED": "PASS",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class ResidualKillEntry:
    name: str
    rule: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[ResidualKillEntry]:
    return [
        ResidualKillEntry(
            name="RK1: residual-kill target",
            rule="If J_V-driven zeta enters B_s, residual zeta/kappa metric trace is killed or made non-metric",
            role="core clean no-overlap convention",
            allowed_if="used as provisional safety convention until O is derived",
            forbidden_if="treated as derived field equation",
            status="THEOREM_TARGET",
            missing="residual-kill theorem",
            consequence="prevents J_V-driven zeta from double-counting scalar trace",
        ),
        ResidualKillEntry(
            name="RK2: zeta residual metric killed",
            rule="zeta_residual_metric = 0 after B_s insertion",
            role="direct zeta count-once rule",
            allowed_if="zeta remains metric-active only through B_s/A_spatial channel",
            forbidden_if="zeta also appears as independent residual metric scalar",
            status="SAFE_IF",
            missing="derivation of kill/non-metric transition",
            consequence="demotes residual zeta from metric correction to bookkeeping or inactive residual",
        ),
        ResidualKillEntry(
            name="RK3: kappa residual metric killed / diagnostic",
            rule="kappa_residual_metric = 0 or kappa remains reduced diagnostic / non-metric",
            role="prevents kappa from restoring killed trace",
            allowed_if="kappa is diagnostic, separately neutral, or non-metric",
            forbidden_if="kappa becomes substitute scalar metric trace",
            status="REQUIRED",
            missing="kappa cleanup theorem",
            consequence="protects Group 14 areal-kappa fence and count-once recombination",
        ),
        ResidualKillEntry(
            name="RK4: non-metric bookkeeping branch",
            rule="zeta/kappa residual may remain as configuration bookkeeping but not direct metric trace",
            role="preserves ontology without metric double-counting",
            allowed_if="bookkeeping-to-metric insertion is only through B_s or other explicit map",
            forbidden_if="bookkeeping terms become hidden source reservoir",
            status="CANDIDATE",
            missing="bookkeeping status and accounting law",
            consequence="keeps residual variables useful without scalar-gravity behavior",
        ),
        ResidualKillEntry(
            name="RK5: P_relax-only residual branch",
            rule="residual belongs only to first-order non-radiative relaxation, not metric scalar trace",
            role="possible safe dynamic residual role",
            allowed_if="P_relax is first-order, boundary-neutral, and non-radiative",
            forbidden_if="P_relax becomes Box zeta / Box kappa or scalar radiation",
            status="CANDIDATE",
            missing="P_relax mechanism and non-wave theorem",
            consequence="may preserve residual dynamics without ordinary scalar wave",
        ),
        ResidualKillEntry(
            name="RK6: B_s-only metric insertion",
            rule="Trace[g_ij^scalar] receives J_V-driven zeta only through B_s",
            role="metric recombination rule",
            allowed_if="B_s/F_zeta insertion law is explicit",
            forbidden_if="same zeta variation enters both B_s and residual metric trace",
            status="REQUIRED",
            missing="B_s/F_zeta map",
            consequence="central condition for safe ordinary metric entry",
        ),
        ResidualKillEntry(
            name="RK7: energy/accounting consequence",
            rule="epsilon_vac_config / e_kappa do not count killed residual as extra source energy",
            role="prevents coefficient reservoir behavior",
            allowed_if="energy/accounting terms are diagnostic or recombine once",
            forbidden_if="killed residual reappears as physical energy source",
            status="REQUIRED",
            missing="energy/accounting rule",
            consequence="prevents hidden double-counting through vacuum bookkeeping",
        ),
        ResidualKillEntry(
            name="RK8: neutral residual alternative",
            rule="residual metric trace survives only if O=0, boundary-neutral, no mass overlap",
            role="alternative theorem-heavy branch",
            allowed_if="orthogonality, boundary neutrality, and no A-sector overlap are derived",
            forbidden_if="neutral residual is assumed to avoid residual-kill",
            status="RISK",
            missing="full no-overlap operator and boundary theorem",
            consequence="keeps residual branch alive only at high proof burden",
        ),
        ResidualKillEntry(
            name="RK9: residual restoration forbidden",
            rule="kappa or zeta residual restores killed metric trace after B_s insertion",
            role="rejected regression",
            allowed_if="never in ordinary branch",
            forbidden_if="accepted as recombination",
            status="REJECTED",
            missing="not pursued",
            consequence="kills branches that undo residual-kill by relabeling",
        ),
        ResidualKillEntry(
            name="RK10: boundary-neutral killed residual",
            rule="killed/non-metric residual creates no exterior scalar charge or far-zone scalar flux",
            role="ordinary-sector safety guard",
            allowed_if="residual-kill also removes exterior scalar tail",
            forbidden_if="non-metric residual still sources exterior metric behavior",
            status="REQUIRED",
            missing="boundary consequence theorem",
            consequence="links residual-kill to exterior safety",
        ),
        ResidualKillEntry(
            name="RK11: no M_ext shift",
            rule="residual-kill / non-metric residual does not alter A-sector exterior mass",
            role="A-sector mass protection",
            allowed_if="B_s/J_V recombination preserves M_ext accounting",
            forbidden_if="residual bookkeeping shifts measured mass",
            status="REQUIRED",
            missing="mass-accounting proof",
            consequence="keeps volume accounting from becoming mass reservoir",
        ),
        ResidualKillEntry(
            name="RK12: recovery downstream",
            rule="gamma_like and AB tested only after residual-kill convention is fixed",
            role="ordinary-regime recovery target",
            allowed_if="kept downstream",
            forbidden_if="used to decide which residual to kill",
            status="RECOVERY_TARGET",
            missing="solutions after residual-kill convention",
            consequence="keeps recovery from choosing the safety convention",
        ),
        ResidualKillEntry(
            name="RK13: residual-kill not derivation warning",
            rule="residual-kill is provisional convention unless derived from O or parent identity",
            role="anti-hardening warning",
            allowed_if="explicitly marked provisional",
            forbidden_if="treated as postulate or field equation without derivation",
            status="REQUIRED",
            missing="parent derivation",
            consequence="prevents scaffold from hardening into assumption",
        ),
        ResidualKillEntry(
            name="RK14: branch failure",
            rule="residual cannot be killed/non-metric, and O cannot be defined",
            role="ordinary metric branch failure condition",
            allowed_if="used to keep J_V-driven zeta out of metric sector",
            forbidden_if="patched by neutral-residual assertion",
            status="BRANCH_KILLED",
            missing="applies if no safe residual branch survives",
            consequence="J_V-driven zeta cannot enter ordinary metric scalar sector",
        ),
        ResidualKillEntry(
            name="RK15: recommended next move",
            rule="if residual-kill is only provisional, update Group 15 status and field-equation status",
            role="best next checkpoint",
            allowed_if="residual-kill audit does not derive a theorem",
            forbidden_if="continuing into field equations as if residual-kill were derived",
            status="RECOMMENDED",
            missing="status update",
            consequence="next script should summarize Group 15 with residual-kill as provisional convention",
        ),
    ]


def print_entry(e: ResidualKillEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Rule: {e.rule}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Residual-kill rule problem")

    print("Question:")
    print()
    print("  If J_V-driven zeta enters B_s, can residual zeta/kappa metric trace be killed")
    print("  or made non-metric as the cleanest safe convention?")
    print()
    print("Goal:")
    print()
    print("  test residual-kill / non-metric residual as provisional count-once convention")
    print()
    print("Discipline:")
    print()
    print("  do not treat residual-kill as derived")
    print("  do not let kappa restore killed trace")
    print("  do not move killed residual into energy/accounting source")
    print("  preserve boundary neutrality")
    print("  preserve no M_ext shift")
    print("  keep recovery downstream")

    status_line("residual-kill rule problem posed", "REQUIRED")


def case_1_inventory(entries: List[ResidualKillEntry]):
    header("Case 1: Residual-kill inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[ResidualKillEntry]):
    header("Case 2: Compact residual-kill ledger")

    print("| Entry | Rule | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.rule.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact residual-kill ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[ResidualKillEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Residual-kill is the cleanest safe convention but not derived.")
    print("  Kappa must remain diagnostic/non-metric or separately neutral.")
    print("  Non-metric bookkeeping and P_relax-only residual are candidate residual roles.")
    print("  Neutral residual remains risky and theorem-heavy.")
    print("  If residual-kill cannot be kept provisional and safe, J_V-driven zeta cannot enter the ordinary metric sector.")

    status_line("residual-kill status count produced", "STRUCTURAL")


def case_4_decision_tree():
    header("Case 4: Residual-kill decision tree")

    print("Decision tree:")
    print()
    print("1. Residual-kill:")
    print("   safest count-once branch if J_V-driven zeta enters B_s.")
    print()
    print("2. Non-metric bookkeeping:")
    print("   preserves variables but removes direct metric scalar trace.")
    print()
    print("3. P_relax-only residual:")
    print("   possible if first-order, non-radiative, and boundary-neutral.")
    print()
    print("4. Neutral residual:")
    print("   possible only if O, boundary neutrality, and no mass overlap are derived.")
    print()
    print("5. Kappa diagnostic:")
    print("   required unless kappa is separately derived.")
    print()
    print("6. If residual metric trace persists without O:")
    print("   J_V-driven zeta cannot enter ordinary metric sector.")

    status_line("residual-kill decision tree stated", "RECOMMENDED")


def case_5_good_failure():
    header("Case 5: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  residual-kill cannot be justified, and neutral residual lacks O.")
    print()
    print("Consequence:")
    print()
    print("  J_V-driven zeta must stay non-metric or theorem-target only.")
    print("  Do not insert it into ordinary metric scalar trace.")
    print()
    print("Bad failure:")
    print("  kill residual by declaration and then use it as hidden source/accounting reservoir.")

    status_line("residual-kill good failure stated", "DEFER")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("Residual-kill rule fails if:")
    print()
    print("1. residual-kill is treated as derived")
    print("2. zeta residual remains metric-active after B_s insertion")
    print("3. kappa restores killed residual trace")
    print("4. killed residual reappears as physical energy source")
    print("5. P_relax becomes Box zeta / Box kappa or scalar radiation")
    print("6. non-metric bookkeeping shifts M_ext")
    print("7. neutral residual is assumed without O")
    print("8. recovery checks decide residual status")

    status_line("residual-kill failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_residual_kill_rule_for_volume_current.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_group_15_status_after_residual_kill.py")
    print("   Update Group 15 status with residual-kill as provisional convention.")
    print()
    print("3. candidate_nonmetric_residual_bookkeeping.py")
    print("   Test non-metric bookkeeping role if more detail is needed.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_group_15_status_after_residual_kill.py")
    print()
    print("Reason:")
    print("  Residual-kill is a provisional safety convention, not a derivation. The next useful step is a status update before any field-equation attempt.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("Residual-kill / non-metric residual is the cleanest safe convention.")
    print()
    print("But it remains provisional.")
    print()
    print("Best current convention:")
    print()
    print("  If J_V-driven zeta enters B_s, residual zeta/kappa metric trace is killed or made non-metric.")
    print()
    print("Best next test:")
    print("  candidate_group_15_status_after_residual_kill.py")


def main():
    header("Candidate Residual-Kill Rule For Volume Current")
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
