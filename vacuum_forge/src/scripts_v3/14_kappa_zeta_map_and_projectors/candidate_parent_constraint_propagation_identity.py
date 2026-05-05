# Candidate parent constraint propagation identity
#
# Purpose
# -------
# The A-sector parent identity inventory narrowed the search.
#
# Rejected:
#
#   GR rewrite,
#   B=1/A identity,
#   gamma=1 coefficient fit.
#
# Surviving identity classes:
#
#   action/stiffness,
#   constraint propagation,
#   conservation/Bianchi-like,
#   volume-exchange,
#   recombination/no-overlap identity.
#
# The nearest route from the existing A-sector success is constraint propagation:
#
#   can the A constraint force a compatible A_spatial companion without GR import?
#
# This script tests that route.
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
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class ConstraintPropagationEntry:
    name: str
    branch: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[ConstraintPropagationEntry]:
    return [
        ConstraintPropagationEntry(
            name="CP1: A constraint with propagation closure",
            branch="Delta_A A = source plus closure condition forces A_spatial",
            role="primary candidate route from existing A-sector success",
            allowed_if="closure equation derives spatial companion and preserves source conservation",
            forbidden_if="A_spatial is appended after solving A",
            status="CANDIDATE",
            missing="explicit propagation/closure law",
            consequence="would keep A/A_spatial in one scalar constraint family",
        ),
        ConstraintPropagationEntry(
            name="CP2: source conservation compatibility",
            branch="A constraint plus continuity/conservation determines spatial response consistency",
            role="candidate non-decorative closure condition",
            allowed_if="conserved source/current is defined and links lapse/spatial response",
            forbidden_if="conservation is invoked without a current/operator",
            status="CANDIDATE",
            missing="conserved current and closure operator",
            consequence="may connect to broader Bianchi-like parent identity",
        ),
        ConstraintPropagationEntry(
            name="CP3: elliptic constraint propagation",
            branch="spatial companion follows from elliptic constraint compatibility rather than evolution",
            role="keeps A_spatial non-radiative and constraint-like",
            allowed_if="elliptic compatibility fixes spatial trace without B=1/A decree",
            forbidden_if="elliptic solution simply inserts Schwarzschild spatial metric",
            status="CANDIDATE",
            missing="compatibility condition and boundary data rule",
            consequence="could derive static spatial companion without scalar wave modes",
        ),
        ConstraintPropagationEntry(
            name="CP4: weak-field gamma recovery as check",
            branch="constraint propagation recovers gamma=1-like weak-field behavior",
            role="recovery target for acceptable propagation identity",
            allowed_if="gamma-like result follows from closure, not coefficient tuning",
            forbidden_if="gamma=1 is selected by hand",
            status="RECOVERY_TARGET",
            missing="weak-field limit of closure identity",
            consequence="tests propagation identity without using gamma=1 as construction",
        ),
        ConstraintPropagationEntry(
            name="CP5: exterior AB diagnostic as check",
            branch="recovered exterior passes kappa_areal -> 0 / AB -> 1 diagnostic",
            role="exterior recovery check",
            allowed_if="AB relation emerges after deriving A_spatial",
            forbidden_if="AB=1 is imposed to define A_spatial",
            status="RECOVERY_TARGET",
            missing="derived exterior solution",
            consequence="keeps areal kappa fenced as diagnostic",
        ),
        ConstraintPropagationEntry(
            name="CP6: no-overlap trace theorem",
            branch="Trace[g_ij scalar] = Trace_A_mass + Trace_residual_neutral with overlap=0",
            role="recombination compatibility requirement for propagation identity",
            allowed_if="closure either derives residual-neutral split or kills residual trace",
            forbidden_if="A_spatial and zeta/kappa residual overlap",
            status="THEOREM_TARGET",
            missing="overlap operator and residual projector",
            consequence="decides what remains for zeta/kappa after A_spatial closure",
        ),
        ConstraintPropagationEntry(
            name="CP7: zeta as closure participant",
            branch="zeta participates in propagation closure as A_spatial companion",
            role="possible ontology-native completion of A_spatial",
            allowed_if="zeta is not also independent residual and preserves exterior neutrality",
            forbidden_if="zeta patches A_spatial while remaining separate residual trace",
            status="RISK",
            missing="zeta-A_spatial identity and accounting revision",
            consequence="may force revisit of zeta primary/residual convention",
        ),
        ConstraintPropagationEntry(
            name="CP8: kappa residual after closure",
            branch="kappa remains residual/diagnostic after A_spatial closure",
            role="possible surviving role for kappa",
            allowed_if="closure leaves non-overlapping boundary-neutral residual",
            forbidden_if="kappa adds independent scalar trace",
            status="SAFE_IF",
            missing="residual map after closure",
            consequence="may trigger kappa_diagnostic_or_residual_after_A_spatial script",
        ),
        ConstraintPropagationEntry(
            name="CP9: A-only closure failure",
            branch="A constraint cannot force A_spatial without additional parent structure",
            role="good branch-killed outcome",
            allowed_if="used to move search to action/stiffness or Bianchi-like identity",
            forbidden_if="failure is patched by GR metric import",
            status="BRANCH_KILLED",
            missing="decisive no-go proof",
            consequence="kills A-sector-local constraint propagation branch if proven",
        ),
        ConstraintPropagationEntry(
            name="CP10: GR rewrite closure",
            branch="constraint propagation is just Einstein constraint equations rewritten",
            role="none",
            allowed_if="never as derivation in current branch",
            forbidden_if="used as closure proof",
            status="REJECTED",
            missing="not pursued",
            consequence="would smuggle GR as parent closure",
        ),
        ConstraintPropagationEntry(
            name="CP11: B=1/A closure shortcut",
            branch="closure condition is AB=1 or B=1/A",
            role="shortcut",
            allowed_if="only as exterior diagnostic after derivation",
            forbidden_if="used as closure condition",
            status="REJECTED",
            missing="not pursued",
            consequence="repeats rejected construction shortcut",
        ),
        ConstraintPropagationEntry(
            name="CP12: recommended next route",
            branch="test whether a non-GR closure law can be written for A constraint propagation",
            role="best current field-equation narrowing target",
            allowed_if="closure has explicit mechanism and failure criteria",
            forbidden_if="closure is merely named",
            status="RECOMMENDED",
            missing="candidate closure law",
            consequence="next script should attempt a minimal symbolic closure/no-go test",
        ),
    ]


def print_entry(e: ConstraintPropagationEntry) -> None:
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
    header("Case 0: Parent constraint propagation identity problem")

    print("Question:")
    print()
    print("  Can the A constraint force a compatible A_spatial companion without GR import?")
    print()
    print("Goal:")
    print()
    print("  test constraint propagation as the nearest bridge from existing A-sector success to A_spatial")
    print()
    print("Discipline:")
    print()
    print("  do not append A_spatial after solving A")
    print("  do not impose B=1/A")
    print("  do not tune gamma=1")
    print("  do not rewrite Einstein constraints")
    print("  do not patch failure with zeta/kappa without no-overlap proof")
    print("  define closure or kill the branch")

    status_line("parent constraint propagation problem posed", "REQUIRED")


def case_1_inventory(entries: List[ConstraintPropagationEntry]):
    header("Case 1: Constraint propagation branch inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[ConstraintPropagationEntry]):
    header("Case 2: Compact constraint-propagation ledger")

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

    status_line("compact constraint-propagation ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[ConstraintPropagationEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Constraint propagation is viable only if it supplies an explicit closure law.")
    print("  Recovery checks remain gamma-like weak-field behavior and exterior AB diagnostic.")
    print("  If no non-GR closure law exists, the A-sector-local propagation branch is killed.")
    print("  Zeta can participate only if it stops being an independent overlapping residual.")

    status_line("constraint-propagation status count produced", "STRUCTURAL")


def case_4_minimal_closure_requirements():
    header("Case 4: Minimal closure requirements")

    print("A legitimate constraint propagation identity must provide:")
    print()
    print("1. A scalar constraint for A.")
    print("2. A propagation/closure condition.")
    print("3. A derived A_spatial companion.")
    print("4. Source/current conservation compatibility.")
    print("5. Weak-field gamma-like recovery as output, not tuning.")
    print("6. Exterior AB diagnostic as output, not assumption.")
    print("7. Count-once trace compatibility.")
    print("8. A branch-killed outcome if closure cannot be written.")
    print()
    print("Missing one of these makes the identity decorative.")

    status_line("minimal closure requirements stated", "REQUIRED")


def case_5_good_failure():
    header("Case 5: Good failure")

    print("Good failure:")
    print()
    print("  No non-GR local closure law can force A_spatial from the A constraint alone.")
    print()
    print("Consequence:")
    print()
    print("  The A-sector-local constraint propagation branch is insufficient.")
    print("  Search must move to action/stiffness, conservation/Bianchi-like, or volume-exchange parent identities.")
    print()
    print("Bad failure:")
    print()
    print("  Use GR spatial metric, B=1/A, or gamma tuning as patch.")

    status_line("constraint-propagation good failure stated", "BRANCH_KILLED")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("Constraint propagation fails if:")
    print()
    print("1. A_spatial is appended after solving A")
    print("2. closure is B=1/A")
    print("3. closure is gamma=1 coefficient tuning")
    print("4. closure is Einstein constraints renamed")
    print("5. conservation is invoked without current/operator")
    print("6. zeta/kappa patch closure while remaining independent residual")
    print("7. no-overlap trace theorem is ignored")
    print("8. exterior matching is used as local propagation law")
    print("9. closure has no branch-killed criterion")

    status_line("constraint-propagation failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_parent_constraint_propagation_identity.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_minimal_A_constraint_closure_no_go.py")
    print("   Try to write a minimal non-GR closure form; kill branch if only GR shortcuts work.")
    print()
    print("3. candidate_parent_action_stiffness_identity.py")
    print("   Move to action/stiffness route if constraint closure cannot be made concrete.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_minimal_A_constraint_closure_no_go.py")
    print()
    print("Reason:")
    print("  The propagation branch is now narrowed enough to test concretely: can a minimal closure be written without B=1/A, GR rewrite, or gamma tuning?")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("Constraint propagation is the nearest surviving bridge from A to A_spatial.")
    print()
    print("It survives only if:")
    print("  a real closure law can be written,")
    print("  source/current compatibility is defined,")
    print("  gamma-like and AB recovery emerge as checks,")
    print("  and the count-once trace theorem is preserved.")
    print()
    print("Best next test:")
    print("  candidate_minimal_A_constraint_closure_no_go.py")


def main():
    header("Candidate Parent Constraint Propagation Identity")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_minimal_closure_requirements()
    case_5_good_failure()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
