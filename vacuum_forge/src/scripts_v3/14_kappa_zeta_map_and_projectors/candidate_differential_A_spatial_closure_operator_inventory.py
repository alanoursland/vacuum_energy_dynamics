# Candidate differential A_spatial closure operator inventory
#
# Purpose
# -------
# The minimal A-constraint closure ansatz audit found the most local survivor:
#
#   C[A,A_spatial,S_A]
#     = alpha1 L1[A_spatial] + alpha2 L2[A] + alpha3 S_A = 0
#
# But this is only an ansatz shell.
#
# This script inventories possible L1/L2 operators and coefficient constraints
# to decide whether the differential compatibility branch is real or just
# GR in a mask.
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
class OperatorEntry:
    name: str
    operator: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[OperatorEntry]:
    return [
        OperatorEntry(
            name="DO1: differential closure shell",
            operator="C = alpha1 L1[A_spatial] + alpha2 L2[A] + alpha3 S_A = 0",
            role="starting differential compatibility family",
            allowed_if="operators and coefficients are separately justified",
            forbidden_if="used as decorative notation for missing A_spatial equation",
            status="STRUCTURAL",
            missing="L1, L2, alpha constraints",
            consequence="branch remains open only if operator content is non-decorative",
        ),
        OperatorEntry(
            name="DO2: Laplacian-like L1 on A_spatial",
            operator="L1[A_spatial] = Delta A_spatial",
            role="minimal elliptic local operator for spatial companion",
            allowed_if="operator follows from non-radiative constraint structure",
            forbidden_if="chosen only because it reproduces Poisson/GR-like spatial response",
            status="CANDIDATE",
            missing="constraint/stiffness origin of L1",
            consequence="could make A_spatial elliptic and non-radiative",
        ),
        OperatorEntry(
            name="DO3: mass-source coupling through S_A",
            operator="alpha3 S_A[rho]",
            role="routes A-sector source into closure",
            allowed_if="source placement follows from same A constraint/source routing",
            forbidden_if="source coefficient is tuned to force gamma_like=1",
            status="CANDIDATE",
            missing="source normalization principle",
            consequence="determines whether gamma-like recovery is output or tuning",
        ),
        OperatorEntry(
            name="DO4: A-derivative L2 operator",
            operator="L2[A] = Delta A or radial compatibility derivative of A",
            role="couples lapse scalar response to spatial companion",
            allowed_if="operator is not equivalent to imposing B=1/A",
            forbidden_if="L2 secretly encodes Schwarzschild/AB relation",
            status="RISK",
            missing="non-GR compatibility origin",
            consequence="danger junction for GR smuggling",
        ),
        OperatorEntry(
            name="DO5: gradient-square nonlinear correction",
            operator="L2[A] includes |grad A|^2 or nonlinear derivative terms",
            role="possible nonlinear correction beyond weak field",
            allowed_if="coefficient derives from action/stiffness or closure",
            forbidden_if="term is chosen to match Schwarzschild expansion",
            status="CANDIDATE",
            missing="nonlinear coefficient origin",
            consequence="may be deferred until linear closure is understood",
        ),
        OperatorEntry(
            name="DO6: coefficient-origin constraint",
            operator="alpha1:alpha2:alpha3 fixed by identity, not fit",
            role="prevents gamma tuning",
            allowed_if="ratio follows from conservation/action/constraint closure",
            forbidden_if="ratio is selected to make gamma_like=1",
            status="REQUIRED",
            missing="coefficient principle",
            consequence="without this, differential closure is tuning not derivation",
        ),
        OperatorEntry(
            name="DO7: gamma-like weak-field check",
            operator="linearized closure output gives gamma_like=1",
            role="recovery test",
            allowed_if="emerges from operator/coefficient principle",
            forbidden_if="used to choose alpha ratios",
            status="RECOVERY_TARGET",
            missing="linearized solution of closure",
            consequence="tests closure after operator inventory",
        ),
        OperatorEntry(
            name="DO8: AB exterior diagnostic check",
            operator="exterior solution yields kappa_areal -> 0 / AB -> 1",
            role="reduced exterior recovery test",
            allowed_if="emerges from solved closure",
            forbidden_if="used as boundary condition or closure equation",
            status="RECOVERY_TARGET",
            missing="exterior solution and boundary data rule",
            consequence="keeps AB diagnostic-only",
        ),
        OperatorEntry(
            name="DO9: no-overlap operator",
            operator="O[A_spatial, trace_residual] = 0",
            role="ensures differential closure does not double-count zeta/kappa trace",
            allowed_if="O is defined or residual is killed/non-metric",
            forbidden_if="overlap=0 is asserted without operator or consequence",
            status="THEOREM_TARGET",
            missing="operator O or residual-kill theorem",
            consequence="decides whether zeta/kappa survive as metric residuals",
        ),
        OperatorEntry(
            name="DO10: zeta-dependent operator",
            operator="L2[A,zeta] or C[A,A_spatial,zeta]",
            role="possible volume-assisted compatibility",
            allowed_if="zeta becomes companion or residual by no-overlap identity",
            forbidden_if="zeta both supplies A_spatial and remains independent residual",
            status="RISK",
            missing="zeta role decision and accounting revision",
            consequence="may move branch from A-local to volume-exchange identity",
        ),
        OperatorEntry(
            name="DO11: GR shortcut collapse",
            operator="operator choice equivalent to B=1/A, copied GR metric, Einstein constraint, or tuned gamma",
            role="branch-kill detector",
            allowed_if="used as no-go diagnosis only",
            forbidden_if="accepted as closure",
            status="REJECTED",
            missing="not pursued",
            consequence="if all operator choices collapse here, differential branch dies",
        ),
        OperatorEntry(
            name="DO12: recommended operator test",
            operator="test linear elliptic L1/L2/source closure before nonlinear or zeta-assisted branches",
            role="least decorated local test",
            allowed_if="coefficient-origin and shortcut checks are explicit",
            forbidden_if="linear test is tuned to pass recovery targets",
            status="RECOMMENDED",
            missing="minimal linear operator closure script",
            consequence="next script should test linear closure algebra and branch-kill criteria",
        ),
    ]


def print_entry(e: OperatorEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Operator: {e.operator}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Differential A_spatial closure operator inventory problem")

    print("Question:")
    print()
    print("  What L1/L2 operators can make differential compatibility real rather than decorative?")
    print()
    print("Goal:")
    print()
    print("  inventory operator choices and expose coefficient / shortcut risks")
    print()
    print("Discipline:")
    print()
    print("  do not tune alpha ratios to gamma=1")
    print("  do not encode B=1/A in L2")
    print("  do not copy GR spatial metric")
    print("  do not assert overlap=0 without operator/consequence")
    print("  do not let zeta be both A_spatial companion and residual")
    print("  require branch-kill if all operators are shortcuts")

    status_line("differential operator inventory problem posed", "REQUIRED")


def case_1_inventory(entries: List[OperatorEntry]):
    header("Case 1: Differential operator inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[OperatorEntry]):
    header("Case 2: Compact differential-operator ledger")

    print("| Entry | Operator | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.operator.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact differential-operator ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[OperatorEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  A linear elliptic closure is the least decorated local test.")
    print("  The danger is coefficient tuning: without alpha origin, gamma-like recovery is not derived.")
    print("  L2[A] is the GR-smuggling danger junction.")
    print("  Zeta-dependent operators likely leave the A-local branch and move toward volume-exchange identity.")

    status_line("differential-operator status count produced", "STRUCTURAL")


def case_4_minimal_linear_operator_test():
    header("Case 4: Minimal linear operator test")

    print("Least decorated test form:")
    print()
    print("  alpha1 Delta A_spatial + alpha2 Delta A + alpha3 S_A = 0")
    print()
    print("Using the A constraint:")
    print()
    print("  Delta A = S_A")
    print()
    print("This collapses to:")
    print()
    print("  alpha1 Delta A_spatial + (alpha2 + alpha3) S_A = 0")
    print()
    print("Therefore:")
    print()
    print("  Delta A_spatial = -((alpha2 + alpha3)/alpha1) S_A")
    print()
    print("Danger:")
    print("  choosing the ratio to recover gamma_like=1 is coefficient tuning unless alpha ratios are derived.")

    status_line("minimal linear operator test stated", "CANDIDATE")


def case_5_branch_kill_or_defer():
    header("Case 5: Branch-kill or defer criteria")

    print("Kill or defer the differential branch if:")
    print()
    print("1. the only viable L1/L2 pair is Laplacian with tuned coefficient ratio")
    print("2. L2[A] encodes B=1/A or Schwarzschild expansion")
    print("3. source placement is chosen only to force gamma_like=1")
    print("4. overlap with zeta/kappa residual is unresolved")
    print("5. no coefficient-origin principle is available")
    print()
    print("If killed/deferred, move to:")
    print("  parent action/stiffness identity for coefficient origin,")
    print("  conservation/Bianchi-like identity for closure origin,")
    print("  or volume-exchange identity for zeta participation.")

    status_line("differential branch-kill/defer criteria stated", "BRANCH_KILLED")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("Differential operator inventory fails if:")
    print()
    print("1. operator inventory pretends alpha ratios are derived")
    print("2. gamma_like=1 is used to pick coefficients")
    print("3. AB=1 appears inside L2 or boundary data")
    print("4. L1 is just copied from GR constraint form")
    print("5. nonlinear terms are tuned to Schwarzschild expansion")
    print("6. zeta-dependent closure keeps zeta as independent residual")
    print("7. no-overlap theorem is not represented")
    print("8. branch cannot be killed or deferred despite coefficient-origin failure")

    status_line("differential operator failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_differential_A_spatial_closure_operator_inventory.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_linear_A_spatial_closure_coefficient_origin.py")
    print("   Test whether alpha ratios can be derived or whether the branch is tuning.")
    print()
    print("3. candidate_parent_action_stiffness_identity.py")
    print("   Move to action/stiffness for coefficient origin.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_linear_A_spatial_closure_coefficient_origin.py")
    print()
    print("Reason:")
    print("  The minimal linear closure reduces to a coefficient-ratio problem. Test whether that ratio can be derived, not fit.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("The differential closure branch reduces quickly to coefficient origin.")
    print()
    print("Minimal form:")
    print("  alpha1 Delta A_spatial + alpha2 Delta A + alpha3 S_A = 0")
    print()
    print("With Delta A = S_A:")
    print("  Delta A_spatial = -((alpha2 + alpha3)/alpha1) S_A")
    print()
    print("This is useful only if the ratio is derived, not chosen.")
    print()
    print("Best next test:")
    print("  candidate_linear_A_spatial_closure_coefficient_origin.py")


def main():
    header("Candidate Differential A_spatial Closure Operator Inventory")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_minimal_linear_operator_test()
    case_5_branch_kill_or_defer()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
