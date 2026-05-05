# Candidate boundary/no-overlap for volume current
#
# Purpose
# -------
# The static-source neutrality run found:
#
#   static zero-current or compact/balanced exchange may be safe,
#   but any exterior scalar charge kills the current family.
#
# If static neutrality survives, the next gate is whether J_V-driven zeta:
#
#   leaks through the boundary,
#   creates exterior zeta/kappa charge,
#   shifts M_ext,
#   or double-counts B_s / residual trace.
#
# This script inventories boundary neutrality and no-overlap requirements.
#
# It is not a derivation of the boundary projector or overlap operator.

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
class BoundaryOverlapEntry:
    name: str
    test: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[BoundaryOverlapEntry]:
    return [
        BoundaryOverlapEntry(
            name="BO1: boundary/no-overlap target",
            test="J_V-driven zeta has zero exterior leakage and no overlap with B_s/residual trace",
            role="core safety condition for surviving volume-current families",
            allowed_if="boundary neutrality and no-overlap are structural, not tuned",
            forbidden_if="boundary terms or residual trace are adjusted to hide leakage",
            status="THEOREM_TARGET",
            missing="boundary theorem and no-overlap operator",
            consequence="decides whether volume current can survive ordinary recombination",
        ),
        BoundaryOverlapEntry(
            name="BO2: zero exterior J_V flux",
            test="n_mu J_V^mu | boundary = 0 or exterior flux integrates to zero structurally",
            role="boundary flux neutrality condition",
            allowed_if="zero flux follows from support, symmetry, or exchange law",
            forbidden_if="boundary flux is canceled by fitted counterterm",
            status="REQUIRED",
            missing="boundary flux theorem",
            consequence="kills current laws that leak scalar volume flux",
        ),
        BoundaryOverlapEntry(
            name="BO3: zero exterior zeta/kappa charge",
            test="Q_ext[zeta,kappa,J_V] = 0 for ordinary static exterior",
            role="exterior scalar-charge guard",
            allowed_if="charge vanishes by projection/boundary mechanism",
            forbidden_if="exterior scalar charge is canceled by R_V tuning",
            status="REQUIRED",
            missing="charge definition and zero-charge theorem",
            consequence="prevents volume current from becoming scalar gravity",
        ),
        BoundaryOverlapEntry(
            name="BO4: no far-zone scalar flux",
            test="F_scalar_far[J_V,zeta,kappa] = 0",
            role="ordinary radiation/exterior guard",
            allowed_if="far-zone scalar flux is structurally absent",
            forbidden_if="J_V sources ordinary scalar radiation or tail",
            status="REQUIRED",
            missing="far-zone flux theorem",
            consequence="protects TT-only ordinary radiation target",
        ),
        BoundaryOverlapEntry(
            name="BO5: no exterior mass shift",
            test="delta M_ext|volume = 0",
            role="A-sector mass protection",
            allowed_if="volume exchange recombines without changing exterior A mass",
            forbidden_if="J_V/Sigma/R shifts M_ext independently",
            status="REQUIRED",
            missing="mass-accounting theorem",
            consequence="kills volume-current families that alter A-sector mass",
        ),
        BoundaryOverlapEntry(
            name="BO6: B_s-only metric insertion",
            test="J_V-driven zeta affects metric scalar trace only through B_s / A_spatial companion channel",
            role="safe companion accounting branch",
            allowed_if="residual zeta trace is killed or non-metric",
            forbidden_if="zeta also appears as independent residual metric trace",
            status="CANDIDATE",
            missing="F_zeta/B_s insertion rule",
            consequence="may preserve volume-current branch without scalar duplicate",
        ),
        BoundaryOverlapEntry(
            name="BO7: residual zeta/kappa killed or non-metric",
            test="zeta_residual_metric = 0 or non-metric; kappa remains diagnostic/non-metric/separately neutral",
            role="residual-kill condition",
            allowed_if="residual status is explicit",
            forbidden_if="residual sector restores the same scalar trace",
            status="REQUIRED",
            missing="residual-kill theorem and kappa cleanup",
            consequence="prevents trace double-counting",
        ),
        BoundaryOverlapEntry(
            name="BO8: no-overlap operator theorem",
            test="O[B_s, zeta_residual/kappa_residual, J_V] = 0",
            role="count-once theorem target",
            allowed_if="overlap operator is defined or residuals are killed",
            forbidden_if="overlap is asserted without mechanism",
            status="THEOREM_TARGET",
            missing="overlap operator definition",
            consequence="central missing theorem for recombination safety",
        ),
        BoundaryOverlapEntry(
            name="BO9: compact-support current",
            test="J_V support compact inside source/interior with smooth zero boundary flux",
            role="candidate boundary-safe current family",
            allowed_if="support and smoothness follow from exchange law",
            forbidden_if="compact support is imposed to hide scalar charge",
            status="CANDIDATE",
            missing="support law and smooth matching theorem",
            consequence="may satisfy boundary neutrality but still needs no-overlap",
        ),
        BoundaryOverlapEntry(
            name="BO10: boundary shell-source risk",
            test="sharp support or source-gradient boundary creates shell-like scalar source",
            role="boundary failure mode",
            allowed_if="only as diagnostic risk",
            forbidden_if="accepted without shell-avoidance theorem",
            status="RISK",
            missing="shell-source avoidance theorem",
            consequence="can kill compact/source-gradient current families",
        ),
        BoundaryOverlapEntry(
            name="BO11: elliptic boundary completion diagnostic",
            test="solve boundary-value problem for J_V diagnostically, not ontologically",
            role="diagnostic elliptic completion",
            allowed_if="clearly marked diagnostic and not physical flux law",
            forbidden_if="promoted to exchange ontology",
            status="SAFE_IF",
            missing="separate physical flux law",
            consequence="may help audit boundary leakage but cannot define J_V",
        ),
        BoundaryOverlapEntry(
            name="BO12: forbidden boundary repair",
            test="choose boundary counterterm / R_V / J_V nonlocally to cancel leakage",
            role="forbidden shortcut",
            allowed_if="never as ordinary branch",
            forbidden_if="used as boundary neutrality mechanism",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents boundary tuning from replacing field equation",
        ),
        BoundaryOverlapEntry(
            name="BO13: static zero-current branch",
            test="J_V=0 exterior/static equilibrium, with no residual metric insertion",
            role="safe exterior branch",
            allowed_if="frame not required from J_V there or equilibrium fallback exists",
            forbidden_if="J_V=0 is normalized or residual trace remains active",
            status="SAFE_IF",
            missing="equilibrium-frame fallback if needed",
            consequence="protects exterior but may not define u_vac globally",
        ),
        BoundaryOverlapEntry(
            name="BO14: recovery downstream",
            test="gamma_like and AB tested only after boundary/no-overlap structure is fixed",
            role="ordinary-regime recovery target",
            allowed_if="kept downstream",
            forbidden_if="used to choose boundary cancellation or overlap split",
            status="RECOVERY_TARGET",
            missing="solutions after safe recombination",
            consequence="keeps recovery from choosing boundary/no-overlap mechanism",
        ),
        BoundaryOverlapEntry(
            name="BO15: branch kill on leakage or overlap",
            test="boundary leakage, exterior charge, M_ext shift, or trace overlap appears",
            role="branch-kill condition",
            allowed_if="used to reject unsafe current family",
            forbidden_if="patched by boundary repair or residual relabeling",
            status="BRANCH_KILLED",
            missing="applies when failure demonstrated",
            consequence="unsafe current family cannot support ordinary sector",
        ),
        BoundaryOverlapEntry(
            name="BO16: recommended next move",
            test="if boundary/no-overlap survives only as theorem target, summarize Group 15 current status",
            role="best next bottleneck",
            allowed_if="boundary/no-overlap remains unresolved after audit",
            forbidden_if="continuing into field equations with unresolved overlap",
            status="RECOMMENDED",
            missing="Group 15 status summary or no-overlap operator script",
            consequence="next script should either define no-overlap operator or close current subchain with bottleneck",
        ),
    ]


def print_entry(e: BoundaryOverlapEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Test: {e.test}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Boundary/no-overlap problem")

    print("Question:")
    print()
    print("  Does surviving J_V-driven volume exchange leak through the boundary")
    print("  or double-count B_s / residual trace?")
    print()
    print("Goal:")
    print()
    print("  audit boundary neutrality and count-once recombination for volume current")
    print()
    print("Discipline:")
    print()
    print("  do not tune boundary terms to hide leakage")
    print("  do not let J_V shift M_ext")
    print("  do not let zeta/kappa residual duplicate B_s trace")
    print("  distinguish diagnostic elliptic completion from physical flux law")
    print("  preserve no far-zone scalar flux")
    print("  keep gamma/AB recovery downstream")

    status_line("boundary/no-overlap problem posed", "REQUIRED")


def case_1_inventory(entries: List[BoundaryOverlapEntry]):
    header("Case 1: Boundary/no-overlap inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[BoundaryOverlapEntry]):
    header("Case 2: Compact boundary/no-overlap ledger")

    print("| Entry | Test | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.test.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact boundary/no-overlap ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[BoundaryOverlapEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Boundary neutrality requires zero exterior flux, zero scalar charge, no far-zone scalar flux, and no M_ext shift.")
    print("  No-overlap requires B_s-only insertion or killed/non-metric residual zeta/kappa trace.")
    print("  Compact support and static zero-current branches are conditionally safe.")
    print("  Boundary shell sources and nonlocal boundary repair are dangerous.")
    print("  The no-overlap operator remains the central missing theorem if no failure is demonstrated.")

    status_line("boundary/no-overlap status count produced", "STRUCTURAL")


def case_4_decision_tree():
    header("Case 4: Boundary/no-overlap decision tree")

    print("Decision tree:")
    print()
    print("1. Zero exterior flux / zero exterior charge:")
    print("   mandatory for ordinary sector.")
    print()
    print("2. B_s-only metric insertion:")
    print("   allowed if residual zeta/kappa metric trace is killed or non-metric.")
    print()
    print("3. Compact-support current:")
    print("   candidate if smooth boundary flux vanishes structurally.")
    print()
    print("4. Elliptic boundary completion:")
    print("   diagnostic only, not physical flux ontology.")
    print()
    print("5. Boundary repair / R_V cancellation:")
    print("   rejected if used to hide leakage.")
    print()
    print("6. If leakage or overlap appears:")
    print("   current family is killed for ordinary sector.")

    status_line("boundary/no-overlap decision tree stated", "RECOMMENDED")


def case_5_good_failure():
    header("Case 5: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  a candidate current leaks scalar flux through the boundary,")
    print("  shifts M_ext, or double-counts B_s/residual trace.")
    print()
    print("Consequence:")
    print()
    print("  reject that current family for ordinary sector.")
    print("  Do not patch with boundary repair or residual relabeling.")
    print()
    print("Bad failure:")
    print("  call an elliptic boundary solution a physical current law.")

    status_line("boundary/no-overlap good failure stated", "DEFER")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("Boundary/no-overlap test fails if:")
    print()
    print("1. exterior J_V flux is nonzero")
    print("2. exterior zeta/kappa scalar charge appears")
    print("3. far-zone scalar flux appears")
    print("4. volume exchange shifts M_ext independently of A")
    print("5. zeta enters metric through both B_s and residual trace")
    print("6. kappa restores killed residual trace")
    print("7. boundary shell source appears")
    print("8. elliptic completion is promoted to physical current")
    print("9. recovery checks choose boundary/no-overlap mechanism")

    status_line("boundary/no-overlap failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_boundary_no_overlap_for_volume_current.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_no_overlap_operator_for_volume_current.py")
    print("   Try to define O[B_s, zeta_residual/kappa_residual, J_V] = 0.")
    print()
    print("3. candidate_group_15_intermediate_status_summary.py")
    print("   Use if no-overlap remains a theorem target and current families remain conditional.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_no_overlap_operator_for_volume_current.py")
    print()
    print("Reason:")
    print("  Boundary neutrality reduces the next missing mechanism to the no-overlap operator for B_s versus residual trace.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("Boundary neutrality and no-overlap are now the surviving safety gate.")
    print()
    print("Best current interpretation:")
    print()
    print("  J_V-driven zeta is allowed only if it has no exterior leakage")
    print("  and does not double-count B_s / residual trace.")
    print()
    print("Best next test:")
    print("  candidate_no_overlap_operator_for_volume_current.py")


def main():
    header("Candidate Boundary/No-Overlap For Volume Current")
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
