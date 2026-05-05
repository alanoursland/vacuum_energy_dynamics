# Candidate stiffness ratio origin inventory
#
# Purpose
# -------
# The minimal coupled stiffness variation found:
#
#   Delta B_s = q_action S_A
#   q_action = -(c_x/c_s)
#
# Coupled stiffness produces the right equation shape but does not fully derive q
# unless c_x/c_s has a pre-recovery origin.
#
# This script inventories possible origins for c_x/c_s.
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
class RatioOriginEntry:
    name: str
    origin: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[RatioOriginEntry]:
    return [
        RatioOriginEntry(
            name="SR1: stiffness ratio target",
            origin="r_s = c_x/c_s, q_action = -r_s",
            role="core coefficient-ratio bottleneck exposed by coupled variation",
            allowed_if="r_s is fixed before gamma/AB recovery checks",
            forbidden_if="r_s is selected to pass recovery targets",
            status="STRUCTURAL",
            missing="pre-recovery origin of r_s",
            consequence="coupled stiffness lives or defers on r_s",
        ),
        RatioOriginEntry(
            name="SR2: free stiffness ratio",
            origin="choose c_x/c_s freely",
            role="repair knob",
            allowed_if="never as derivation",
            forbidden_if="used to save coupled stiffness branch",
            status="REJECTED",
            missing="not pursued",
            consequence="turns action/stiffness into coefficient tuning",
        ),
        RatioOriginEntry(
            name="SR3: symmetry origin",
            origin="c_x/c_s fixed by field-space symmetry or diagonalization constraint",
            role="candidate legitimate ratio origin",
            allowed_if="symmetry is specified before recovery checks",
            forbidden_if="symmetry is invented to force q",
            status="CANDIDATE",
            missing="actual symmetry / field-space metric",
            consequence="could keep action/stiffness branch alive if concrete",
        ),
        RatioOriginEntry(
            name="SR4: normalization origin",
            origin="c_s and c_x fixed by canonical normalization of coupled modes",
            role="possible mathematical coefficient origin",
            allowed_if="normalization follows from kinetic/stiffness metric, not recovery",
            forbidden_if="normalization chosen after gamma_like check",
            status="CANDIDATE",
            missing="canonical variable choice and stiffness metric",
            consequence="may reduce ratio freedom but risks gauge/convention dependence",
        ),
        RatioOriginEntry(
            name="SR5: conservation-current origin",
            origin="c_x/c_s fixed by div J_A = 0 or parent source-balance identity",
            role="candidate conservation route",
            allowed_if="current and balance law are explicit",
            forbidden_if="conservation language is decorative",
            status="CANDIDATE",
            missing="J_A and balance operator",
            consequence="may move next branch to conservation-current coefficient origin",
        ),
        RatioOriginEntry(
            name="SR6: source-coupling origin",
            origin="source interaction fixes c_x/c_s through matter/vacuum coupling",
            role="possible ontology/source-routing origin",
            allowed_if="coupling rule is specified before recovery checks",
            forbidden_if="source coupling is added to repair gamma_like",
            status="RISK",
            missing="matter/vacuum coupling rule",
            consequence="could rescue ratio, but high risk of hidden tuning",
        ),
        RatioOriginEntry(
            name="SR7: volume/zeta exchange origin",
            origin="c_x/c_s fixed by vacuum-volume / curvature-exchange identity",
            role="ontology-native but branch-shifting ratio origin",
            allowed_if="zeta is companion or residual by no-overlap identity",
            forbidden_if="zeta fixes ratio while remaining independent residual trace",
            status="RISK",
            missing="zeta exchange identity and no-overlap theorem",
            consequence="likely leaves pure A-local stiffness branch for volume-exchange branch",
        ),
        RatioOriginEntry(
            name="SR8: constrained-variation origin",
            origin="Lagrange constraint C[A,B_s,S_A]=0 fixes effective c_x/c_s",
            role="candidate route connecting closure shell to action",
            allowed_if="constraint is structural and not B=1/A/gamma_like",
            forbidden_if="constraint is recovery target in disguise",
            status="CANDIDATE",
            missing="constraint origin and multiplier status",
            consequence="may rescue ratio only if constraint itself is derived",
        ),
        RatioOriginEntry(
            name="SR9: gamma-like recovery check",
            origin="weak-field output after r_s fixed gives gamma_like=1",
            role="downstream recovery target",
            allowed_if="checked after r_s is fixed",
            forbidden_if="used to choose r_s",
            status="RECOVERY_TARGET",
            missing="weak-field mapping from r_s to gamma_like",
            consequence="tests but does not determine stiffness ratio",
        ),
        RatioOriginEntry(
            name="SR10: AB exterior diagnostic check",
            origin="exterior solution after r_s fixed gives kappa_areal -> 0 / AB -> 1",
            role="downstream exterior diagnostic",
            allowed_if="checked after solving varied equations",
            forbidden_if="used as boundary/action constraint",
            status="RECOVERY_TARGET",
            missing="exterior solution with fixed r_s",
            consequence="keeps AB diagnostic-only",
        ),
        RatioOriginEntry(
            name="SR11: no-overlap compatibility",
            origin="r_s must not produce overlapping B_s and zeta/kappa residual trace",
            role="protects count-once theorem",
            allowed_if="overlap operator or residual status theorem is available",
            forbidden_if="derived ratio still double-counts trace",
            status="THEOREM_TARGET",
            missing="overlap operator / residual theorem",
            consequence="ratio origin still fails if trace accounting fails",
        ),
        RatioOriginEntry(
            name="SR12: recommended next move",
            origin="if no symmetry/normalization origin is concrete, move to conservation-current origin",
            role="best current branch decision",
            allowed_if="free ratio and recovery-tuned ratio are rejected",
            forbidden_if="pretending action/stiffness has derived r_s without origin",
            status="RECOMMENDED",
            missing="symmetry/normalization/conservation comparison",
            consequence="next script should compare symmetry/normalization against conservation-current route",
        ),
    ]


def print_entry(e: RatioOriginEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Origin: {e.origin}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Stiffness ratio origin inventory problem")

    print("Question:")
    print()
    print("  Who fixed c_x/c_s before gamma looked at it?")
    print()
    print("Goal:")
    print()
    print("  inventory possible pre-recovery origins of the stiffness ratio")
    print()
    print("Discipline:")
    print()
    print("  do not choose c_x/c_s from gamma_like")
    print("  do not choose c_x/c_s from AB=1")
    print("  do not invent symmetry after recovery")
    print("  do not hide tuning in normalization or source coupling")
    print("  do not let zeta fix ratio while remaining independent residual")
    print("  move to conservation-current route if action/stiffness ratio remains free")

    status_line("stiffness ratio origin problem posed", "REQUIRED")


def case_1_inventory(entries: List[RatioOriginEntry]):
    header("Case 1: Stiffness ratio origin inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[RatioOriginEntry]):
    header("Case 2: Compact stiffness-ratio ledger")

    print("| Entry | Origin | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.origin.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact stiffness-ratio ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[RatioOriginEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Free stiffness ratio is rejected.")
    print("  Symmetry and normalization are possible but must be specified concretely.")
    print("  Conservation-current origin is the strongest next alternative if stiffness ratio remains free.")
    print("  Zeta/volume exchange is plausible but likely leaves the pure A-local stiffness branch.")
    print("  Recovery checks remain downstream.")

    status_line("stiffness-ratio status count produced", "STRUCTURAL")


def case_4_ratio_decision_tree():
    header("Case 4: Ratio-origin decision tree")

    print("Decision tree:")
    print()
    print("1. Is there a real field-space symmetry fixing c_x/c_s?")
    print("   If yes: test recovery downstream.")
    print()
    print("2. Is there a canonical normalization that fixes c_x/c_s before recovery?")
    print("   If yes: check whether it is physical or convention-only.")
    print()
    print("3. Does a conservation-current identity fix c_x/c_s?")
    print("   If yes: move to current/balance derivation.")
    print()
    print("4. Does zeta/volume exchange fix c_x/c_s?")
    print("   If yes: leave pure A-local branch and revisit zeta role.")
    print()
    print("5. If none:")
    print("   action/stiffness does not derive q; defer to conservation-current or volume-exchange branch.")

    status_line("stiffness-ratio decision tree stated", "RECOMMENDED")


def case_5_good_failure():
    header("Case 5: Good failure / defer outcome")

    print("Good failure:")
    print()
    print("  no symmetry, normalization, source-routing, or ontology rule fixes c_x/c_s before recovery.")
    print()
    print("Consequence:")
    print()
    print("  action/stiffness has exposed but not solved q-origin.")
    print("  Move to conservation-current coefficient origin or volume-exchange identity.")
    print()
    print("Bad failure:")
    print("  choose c_x/c_s from gamma_like=1 and call it symmetry or normalization.")

    status_line("stiffness ratio good failure stated", "DEFER")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("Stiffness-ratio origin test fails if:")
    print()
    print("1. ratio is chosen from gamma_like=1")
    print("2. ratio is chosen from AB=1 or Schwarzschild expansion")
    print("3. symmetry is invented after recovery")
    print("4. normalization is convention-only but treated as physical")
    print("5. conservation is invoked without a current")
    print("6. source coupling hides a fit")
    print("7. zeta fixes ratio while remaining independent residual")
    print("8. no-overlap theorem is ignored after ratio selection")

    status_line("stiffness-ratio failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_stiffness_ratio_origin_inventory.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_conservation_current_coefficient_origin.py")
    print("   Test whether a conserved current/balance law fixes c_x/c_s.")
    print()
    print("3. candidate_volume_exchange_stiffness_ratio_origin.py")
    print("   Test whether zeta/vacuum-volume exchange fixes c_x/c_s.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_conservation_current_coefficient_origin.py")
    print()
    print("Reason:")
    print("  Symmetry/normalization are currently unspecified. Conservation-current origin is the strongest next non-tuning route.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("Coupled stiffness reduced q-origin to:")
    print()
    print("  c_x/c_s origin")
    print()
    print("No free ratio is allowed.")
    print()
    print("If symmetry/normalization are not concrete, the next real route is:")
    print("  conservation-current coefficient origin.")
    print()
    print("Best next test:")
    print("  candidate_conservation_current_coefficient_origin.py")


def main():
    header("Candidate Stiffness Ratio Origin Inventory")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_ratio_decision_tree()
    case_5_good_failure()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
