# Candidate parent balance identity for A_spatial
#
# Purpose
# -------
# The minimal gradient-current ratio test found:
#
#   J_A^i = a grad^i A + b grad^i B_s
#   div J_A = 0
#   q = -a/b
#
# This is not a q derivation unless a/b is derived.
#
# This script tests whether a parent balance identity can fix the current ratio
# rather than merely naming a conservation law.
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
class ParentBalanceEntry:
    name: str
    balance: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[ParentBalanceEntry]:
    return [
        ParentBalanceEntry(
            name="PB1: parent balance target",
            balance="Div E_parent[A,B_s,zeta,...] = B_closed[T] + B_relax",
            role="candidate broad identity that could fix current ratio a/b",
            allowed_if="E_parent and balance terms are explicit",
            forbidden_if="Bianchi-like language replaces an operator",
            status="CANDIDATE",
            missing="E_parent, B_closed, B_relax definitions",
            consequence="could rescue current-ratio origin if non-decorative",
        ),
        ParentBalanceEntry(
            name="PB2: E_parent operator",
            balance="E_parent contains coupled A/B_s field response",
            role="defines what is being balanced",
            allowed_if="operator is written before recovery checks",
            forbidden_if="operator is Einstein tensor with new labels",
            status="CANDIDATE",
            missing="explicit parent operator",
            consequence="without E_parent, balance identity is only a name",
        ),
        ParentBalanceEntry(
            name="PB3: B_closed[T] source balance",
            balance="B_closed[T] routes matter/source response into A and B_s sectors",
            role="possible origin of current/source coefficients",
            allowed_if="source routing is defined from matter/vacuum coupling",
            forbidden_if="source balance is invented to fit gamma_like",
            status="RISK",
            missing="source-routing law",
            consequence="could fix a/b but high hidden-tuning risk",
        ),
        ParentBalanceEntry(
            name="PB4: B_relax residual balance",
            balance="B_relax accounts for residual trace/relaxation without double-counting",
            role="connects balance identity to zeta/kappa residual status",
            allowed_if="residual is boundary-neutral and no-overlap is enforced",
            forbidden_if="relaxation term patches coefficient mismatch",
            status="RISK",
            missing="residual/relaxation operator",
            consequence="may move branch toward volume-exchange or P_relax identity",
        ),
        ParentBalanceEntry(
            name="PB5: current-ratio theorem target",
            balance="a/b = r_balance[E_parent,B_closed,B_relax]",
            role="core theorem target for parent balance branch",
            allowed_if="ratio follows from balance structure before recovery checks",
            forbidden_if="ratio chosen from gamma/AB targets",
            status="THEOREM_TARGET",
            missing="ratio derivation from balance identity",
            consequence="decides whether parent balance rescues q-origin",
        ),
        ParentBalanceEntry(
            name="PB6: no decorative Bianchi-like identity",
            balance="Div E_parent is named but not defined",
            role="rejected shortcut",
            allowed_if="never as derivation",
            forbidden_if="used to save current-ratio origin",
            status="REJECTED",
            missing="not pursued",
            consequence="kills parent balance route if no operator can be written",
        ),
        ParentBalanceEntry(
            name="PB7: GR rewrite danger",
            balance="E_parent is Einstein tensor or GR constraint rewrite",
            role="forbidden shortcut family",
            allowed_if="used only as recovery comparison",
            forbidden_if="used as parent balance derivation",
            status="REJECTED",
            missing="not pursued",
            consequence="would smuggle GR into parent balance",
        ),
        ParentBalanceEntry(
            name="PB8: volume-exchange balance",
            balance="parent balance fixed by vacuum-volume/curvature exchange with zeta",
            role="ontology-native candidate but branch-shifting",
            allowed_if="zeta role and no-overlap are explicit",
            forbidden_if="zeta fixes balance while remaining independent residual trace",
            status="CANDIDATE",
            missing="volume-exchange identity",
            consequence="may be the next route if abstract balance remains undefined",
        ),
        ParentBalanceEntry(
            name="PB9: gamma-like recovery check",
            balance="after balance-fixed a/b, weak-field output gives gamma_like=1",
            role="downstream recovery target",
            allowed_if="checked after ratio derivation",
            forbidden_if="used to select balance terms",
            status="RECOVERY_TARGET",
            missing="weak-field map from balance-fixed ratio",
            consequence="tests but does not define parent balance",
        ),
        ParentBalanceEntry(
            name="PB10: AB diagnostic check",
            balance="after balance-fixed a/b, exterior output gives AB -> 1 diagnostic",
            role="downstream exterior recovery check",
            allowed_if="checked after solving balance equations",
            forbidden_if="used as balance condition",
            status="RECOVERY_TARGET",
            missing="exterior solution from balance identity",
            consequence="keeps AB diagnostic-only",
        ),
        ParentBalanceEntry(
            name="PB11: no-overlap trace theorem",
            balance="balance-fixed B_s must not overlap zeta/kappa residual trace",
            role="protects count-once recombination",
            allowed_if="overlap operator or residual status theorem is present",
            forbidden_if="balance fixes ratio but double-counts scalar trace",
            status="THEOREM_TARGET",
            missing="overlap operator / residual theorem",
            consequence="parent balance still fails if trace accounting overlaps",
        ),
        ParentBalanceEntry(
            name="PB12: recommended next move",
            balance="if E_parent cannot be written, move to volume-exchange balance explicitly",
            role="best current branch decision",
            allowed_if="decorative balance is rejected",
            forbidden_if="continuing with undefined parent balance",
            status="RECOMMENDED",
            missing="explicit balance or volume-exchange script",
            consequence="next script should either write E_parent candidates or move to volume-exchange origin",
        ),
    ]


def print_entry(e: ParentBalanceEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Balance: {e.balance}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Parent balance identity for A_spatial problem")

    print("Question:")
    print()
    print("  Can parent balance fix a/b, or is balance just another painted tunnel?")
    print()
    print("Goal:")
    print()
    print("  test whether a parent balance identity can fix the current ratio")
    print()
    print("Discipline:")
    print()
    print("  define E_parent before using Div E_parent")
    print("  do not rewrite GR as parent balance")
    print("  do not choose balance terms from gamma_like or AB")
    print("  do not use relaxation as coefficient patch")
    print("  preserve no-overlap trace theorem")
    print("  move to volume-exchange if balance remains unnamed")

    status_line("parent balance identity problem posed", "REQUIRED")


def case_1_inventory(entries: List[ParentBalanceEntry]):
    header("Case 1: Parent balance identity inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[ParentBalanceEntry]):
    header("Case 2: Compact parent-balance ledger")

    print("| Entry | Balance | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.balance.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact parent-balance ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[ParentBalanceEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Parent balance is promising only if E_parent is explicit.")
    print("  Source and relaxation balances are high-risk coefficient patches unless derived.")
    print("  GR rewrite and decorative Bianchi-like balance are rejected.")
    print("  Volume-exchange may be the next concrete route if abstract balance cannot be written.")

    status_line("parent-balance status count produced", "STRUCTURAL")


def case_4_balance_requirements():
    header("Case 4: Minimal parent-balance requirements")

    print("A legitimate parent balance identity must provide:")
    print()
    print("1. explicit E_parent operator")
    print("2. explicit B_closed[T] source-routing term")
    print("3. explicit B_relax or proof it is absent")
    print("4. derivation of a/b or proof no local ratio is fixed")
    print("5. no GR rewrite")
    print("6. gamma-like and AB recovery as downstream checks")
    print("7. no-overlap trace compatibility")
    print()
    print("Missing any of these makes parent balance decorative.")

    status_line("minimal parent-balance requirements stated", "REQUIRED")


def case_5_good_failure():
    header("Case 5: Good failure / branch move")

    print("Good failure:")
    print()
    print("  no explicit non-GR E_parent can be written that fixes a/b.")
    print()
    print("Consequence:")
    print()
    print("  abstract parent balance cannot rescue q-origin.")
    print("  Move to volume-exchange identity, where the ontology may supply real balance structure.")
    print()
    print("Bad failure:")
    print("  call the balance Bianchi-like and keep going without an operator.")

    status_line("parent-balance good failure stated", "DEFER")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("Parent balance identity fails if:")
    print()
    print("1. E_parent is not defined")
    print("2. E_parent is Einstein tensor with new labels")
    print("3. B_closed[T] is source routing invented to fix gamma")
    print("4. B_relax is coefficient patching")
    print("5. a/b is claimed derived without ratio formula")
    print("6. gamma_like or AB are used to select balance terms")
    print("7. zeta/kappa residual double-counts B_s")
    print("8. balance remains abstract after this script")

    status_line("parent-balance failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_parent_balance_identity_for_A_spatial.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_parent_balance_operator_inventory.py")
    print("   Try to write explicit E_parent operator classes.")
    print()
    print("3. candidate_volume_exchange_stiffness_ratio_origin.py")
    print("   Move to ontology-native volume-exchange balance.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_parent_balance_operator_inventory.py")
    print()
    print("Reason:")
    print("  Parent balance remains viable only if E_parent can be made explicit. Test operator classes before jumping to volume-exchange.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("Parent balance can rescue the current ratio only if it writes an operator.")
    print()
    print("Core target:")
    print("  a/b = r_balance[E_parent, B_closed, B_relax]")
    print()
    print("Best next test:")
    print("  candidate_parent_balance_operator_inventory.py")


def main():
    header("Candidate Parent Balance Identity For A_spatial")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_balance_requirements()
    case_5_good_failure()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
