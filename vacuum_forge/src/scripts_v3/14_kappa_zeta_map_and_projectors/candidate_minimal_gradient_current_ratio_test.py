# Candidate minimal gradient-current ratio test
#
# Purpose
# -------
# The conservation-current coefficient-origin audit found:
#
#   Minimal current:
#     J_A^i = a grad^i A + b grad^i B_s
#
#   gives:
#     q = -a/b
#
# This is useful only if a/b is fixed before recovery checks.
#
# This script tests whether the minimal gradient current genuinely fixes q or
# merely moves the ratio problem from c_x/c_s to a/b.
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
class GradientCurrentEntry:
    name: str
    statement: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[GradientCurrentEntry]:
    return [
        GradientCurrentEntry(
            name="GC1: minimal gradient current",
            statement="J_A^i = a grad^i A + b grad^i B_s",
            role="least decorated local current tying A and A_spatial variable",
            allowed_if="a and b have pre-recovery origin",
            forbidden_if="a:b is chosen to fit gamma_like",
            status="STRUCTURAL",
            missing="origin of a:b",
            consequence="current is explicit but ratio remains exposed",
        ),
        GradientCurrentEntry(
            name="GC2: divergence calculation",
            statement="div J_A = a Delta A + b Delta B_s = (a + b q) S_A",
            role="shows how current fixes q if div J_A=0",
            allowed_if="Delta A=S_A and Delta B_s=q S_A are the intended reduced equations",
            forbidden_if="divergence relation is used after choosing q",
            status="THEOREM_TARGET",
            missing="current-origin justification",
            consequence="with nonzero S_A, div J_A=0 implies q=-a/b",
        ),
        GradientCurrentEntry(
            name="GC3: ratio relocation",
            statement="q = -a/b",
            role="tests whether conservation solved or relocated coefficient origin",
            allowed_if="a/b is derived independently",
            forbidden_if="a/b remains free but q is claimed derived",
            status="DEFER",
            missing="pre-recovery origin of a/b",
            consequence="minimal current relocates the problem unless a/b is fixed",
        ),
        GradientCurrentEntry(
            name="GC4: free current ratio",
            statement="choose a/b freely",
            role="repair knob",
            allowed_if="never as derivation",
            forbidden_if="used to save conservation-current branch",
            status="REJECTED",
            missing="not pursued",
            consequence="turns conservation into coefficient tuning",
        ),
        GradientCurrentEntry(
            name="GC5: stiffness-current equivalence",
            statement="a:b maps to c_x:c_s or Noether current of coupled stiffness",
            role="checks whether current gives new information",
            allowed_if="mapping imposes additional identity beyond q=-c_x/c_s",
            forbidden_if="current merely restates stiffness ratio",
            status="CONSTRAINED",
            missing="Noether / stiffness-current map",
            consequence="may collapse conservation route back into stiffness-ratio problem",
        ),
        GradientCurrentEntry(
            name="GC6: field-space metric origin",
            statement="a/b fixed by metric on (A,B_s) field space",
            role="possible symmetry / normalization origin for current ratio",
            allowed_if="field-space metric is specified before recovery",
            forbidden_if="metric is chosen to fit q",
            status="CANDIDATE",
            missing="field-space metric or symmetry",
            consequence="could rescue local current if concrete",
        ),
        GradientCurrentEntry(
            name="GC7: source-balance origin",
            statement="a/b fixed by matching current divergence to source routing",
            role="possible source-routing route",
            allowed_if="source routing is derived from matter/vacuum coupling",
            forbidden_if="source balance is invented to repair gamma_like",
            status="RISK",
            missing="source-routing identity",
            consequence="may require parent balance identity rather than local current",
        ),
        GradientCurrentEntry(
            name="GC8: parent balance origin",
            statement="a/b fixed by Div E_parent = B_closed[T] + B_relax",
            role="broader nonlocal/parent route",
            allowed_if="parent operator and balance terms are explicit",
            forbidden_if="parent balance is named but undefined",
            status="CANDIDATE",
            missing="E_parent, B_closed, B_relax",
            consequence="likely next route if local current ratio remains free",
        ),
        GradientCurrentEntry(
            name="GC9: gamma-like recovery check",
            statement="after a/b fixed, weak-field output gives gamma_like=1",
            role="downstream recovery target",
            allowed_if="checked after ratio derivation",
            forbidden_if="used to choose a/b",
            status="RECOVERY_TARGET",
            missing="weak-field map from current-fixed q",
            consequence="tests but does not determine a/b",
        ),
        GradientCurrentEntry(
            name="GC10: AB diagnostic check",
            statement="after a/b fixed, exterior solution gives AB -> 1 diagnostic",
            role="downstream exterior recovery target",
            allowed_if="checked after solving equations",
            forbidden_if="used to choose current coefficients",
            status="RECOVERY_TARGET",
            missing="exterior solution",
            consequence="keeps AB diagnostic-only",
        ),
        GradientCurrentEntry(
            name="GC11: no-overlap trace condition",
            statement="current-fixed B_s must not overlap zeta/kappa residual trace",
            role="protects count-once theorem",
            allowed_if="overlap operator or residual theorem is present",
            forbidden_if="current fixes q but double-counts scalar trace",
            status="THEOREM_TARGET",
            missing="overlap operator / residual status",
            consequence="current route still fails if trace accounting overlaps",
        ),
        GradientCurrentEntry(
            name="GC12: recommended next move",
            statement="if a/b has no local origin, move to parent balance or volume-exchange origin",
            role="best current branch decision",
            allowed_if="free ratio and recovery-tuned ratio are rejected",
            forbidden_if="pretending local current derived q",
            status="RECOMMENDED",
            missing="parent balance or volume-exchange script",
            consequence="next script should test parent balance identity or volume-exchange stiffness ratio origin",
        ),
    ]


def print_entry(e: GradientCurrentEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Statement: {e.statement}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Minimal gradient-current ratio test problem")

    print("Question:")
    print()
    print("  Is a/b real structure, or just c_x/c_s wearing a conservation cloak?")
    print()
    print("Goal:")
    print()
    print("  test whether the minimal local current genuinely fixes q")
    print()
    print("Discipline:")
    print()
    print("  do not choose a/b from gamma_like")
    print("  do not choose a/b from AB=1")
    print("  do not claim q is derived while a/b is free")
    print("  do not let current merely restate stiffness ratio")
    print("  preserve no-overlap trace condition")
    print("  move to parent balance or volume-exchange if local current ratio remains free")

    status_line("minimal gradient-current ratio problem posed", "REQUIRED")


def case_1_inventory(entries: List[GradientCurrentEntry]):
    header("Case 1: Gradient-current ratio inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[GradientCurrentEntry]):
    header("Case 2: Compact gradient-current ledger")

    print("| Entry | Statement | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.statement.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact gradient-current ledger produced", "STRUCTURAL")


def case_3_minimal_calculation():
    header("Case 3: Minimal gradient-current calculation")

    print("Current:")
    print()
    print("  J_A^i = a grad^i A + b grad^i B_s")
    print()
    print("Divergence:")
    print()
    print("  div J_A = a Delta A + b Delta B_s")
    print()
    print("Using:")
    print()
    print("  Delta A = S_A")
    print("  Delta B_s = q S_A")
    print()
    print("gives:")
    print()
    print("  div J_A = (a + b q) S_A")
    print()
    print("If div J_A = 0 and S_A != 0:")
    print()
    print("  q = -a/b")
    print()
    print("Interpretation:")
    print("  This fixes q only if a/b is fixed independently.")

    status_line("minimal gradient-current calculation produced", "THEOREM_TARGET")


def case_4_status_counts(entries: List[GradientCurrentEntry]):
    header("Case 4: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  The minimal current is explicit but does not derive q unless a/b has an origin.")
    print("  Free a/b is rejected.")
    print("  Field-space metric and parent balance are the main surviving origins.")
    print("  Local conservation likely defers to parent balance or volume-exchange identity.")

    status_line("gradient-current status count produced", "STRUCTURAL")


def case_5_good_failure():
    header("Case 5: Good failure / defer outcome")

    print("Good failure:")
    print()
    print("  minimal current gives q=-a/b, but a/b has no local pre-recovery origin.")
    print()
    print("Consequence:")
    print()
    print("  local conservation current does not derive q.")
    print("  Move to parent balance identity or volume-exchange stiffness-ratio origin.")
    print()
    print("Bad failure:")
    print("  choose a/b from gamma_like=1 and call it a conservation law.")

    status_line("gradient-current good failure stated", "DEFER")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("Gradient-current ratio test fails if:")
    print()
    print("1. a/b is chosen from gamma_like")
    print("2. a/b is chosen from AB=1")
    print("3. a/b is declared by normalization without a field-space metric")
    print("4. current is just Noether restatement of coupled stiffness with no new identity")
    print("5. source-balance origin is invented to repair recovery")
    print("6. parent balance terms are named but undefined")
    print("7. no-overlap trace theorem is ignored")
    print("8. q is claimed derived while a/b remains free")

    status_line("gradient-current failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_minimal_gradient_current_ratio_test.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_parent_balance_identity_for_A_spatial.py")
    print("   Test whether a parent balance identity can fix the current ratio.")
    print()
    print("3. candidate_volume_exchange_stiffness_ratio_origin.py")
    print("   Test whether vacuum-volume exchange fixes the ratio.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_parent_balance_identity_for_A_spatial.py")
    print()
    print("Reason:")
    print("  Local gradient current relocates q to a/b. A parent balance identity is the next non-decorative route for fixing a/b.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("Minimal gradient current gives:")
    print()
    print("  q = -a/b")
    print()
    print("This is not a q derivation unless a/b is derived.")
    print()
    print("Best next test:")
    print("  candidate_parent_balance_identity_for_A_spatial.py")


def main():
    header("Candidate Minimal Gradient-Current Ratio Test")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_minimal_calculation()
    case_4_status_counts(entries)
    case_5_good_failure()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
