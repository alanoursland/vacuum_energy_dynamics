# Candidate matter versus vacuum frame branch test
#
# Purpose
# -------
# The volume creation frame-field inventory found:
#
#   matter congruence u_m^mu
#   vacuum rest frame u_vac^mu
#
# are the two clean branches for defining:
#
#   Sigma_V = chi rho a^mu nabla_mu A
#
# Hybrid projection should wait until both are defined.
#
# This script compares the matter-flow and vacuum-flow frame branches directly.
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
class FrameBranchEntry:
    name: str
    branch: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[FrameBranchEntry]:
    return [
        FrameBranchEntry(
            name="MV1: branch comparison target",
            branch="choose whether Sigma_V uses matter frame u_m or vacuum frame u_vac",
            role="core frame decision for acceleration-gradient source law",
            allowed_if="choice is physically/ontologically defined before recovery checks",
            forbidden_if="choice is made to fit gamma_like, AB, or static safety",
            status="THEOREM_TARGET",
            missing="physical frame criterion",
            consequence="decides whether acceleration-gradient branch can proceed",
        ),
        FrameBranchEntry(
            name="MV2: matter congruence branch",
            branch="Sigma_V = chi rho a_m^mu nabla_mu A, a_m^mu = u_m^nu nabla_nu u_m^mu",
            role="source-local acceleration across A-gradient",
            allowed_if="u_m is defined by matter current/fluid flow and not coordinate velocity",
            forbidden_if="static equilibrium acceleration is coordinate/gauge artifact",
            status="CANDIDATE",
            missing="matter model and static equilibrium handling",
            consequence="physically local but source-model dependent",
        ),
        FrameBranchEntry(
            name="MV3: vacuum rest-frame branch",
            branch="Sigma_V = chi rho a_vac^mu nabla_mu A, a_vac^mu = u_vac^nu nabla_nu u_vac^mu",
            role="ontology-native vacuum-substance acceleration branch",
            allowed_if="u_vac is derived from zeta/vacuum configuration or exchange law",
            forbidden_if="u_vac is invented to control Sigma_V",
            status="CANDIDATE",
            missing="definition of u_vac^mu",
            consequence="best ontology match but currently missing its core object",
        ),
        FrameBranchEntry(
            name="MV4: hybrid projection deferred",
            branch="Sigma_V = chi rho (P_vac a_m)^mu (P_vac nabla A)_mu",
            role="possible later synthesis of matter acceleration relative to vacuum",
            allowed_if="u_m and u_vac are both independently defined first",
            forbidden_if="used now to patch failures of either branch",
            status="DEFER",
            missing="independent matter and vacuum frame definitions",
            consequence="hybrid projection waits; goblin not allowed to glue clocks together yet",
        ),
        FrameBranchEntry(
            name="MV5: static-source safety for matter frame",
            branch="matter-frame Sigma_V vanishes or is boundary-neutral for static equilibrium sources",
            role="tests whether matter acceleration creates forbidden scalar charge",
            allowed_if="static matter has no independent zeta exterior charge",
            forbidden_if="support/pressure acceleration generates exterior scalar gravity",
            status="REQUIRED",
            missing="static-source neutrality proof",
            consequence="major risk for matter congruence branch",
        ),
        FrameBranchEntry(
            name="MV6: static-source safety for vacuum frame",
            branch="vacuum-frame Sigma_V is neutral for static vacuum/source equilibrium",
            role="tests whether vacuum frame prevents scalar charge",
            allowed_if="u_vac equilibrium makes source-driven zeta boundary-neutral",
            forbidden_if="vacuum acceleration around static source generates independent charge",
            status="REQUIRED",
            missing="vacuum equilibrium / neutrality theorem",
            consequence="major risk for vacuum rest-frame branch",
        ),
        FrameBranchEntry(
            name="MV7: source-model dependence",
            branch="matter branch depends on dust/fluid/stress model",
            role="tracks whether Sigma_V becomes matter-model-specific",
            allowed_if="source law is valid for intended matter class or generalized cleanly",
            forbidden_if="different source models require fitted source terms",
            status="RISK",
            missing="matter class scope",
            consequence="may make matter branch too narrow for parent law",
        ),
        FrameBranchEntry(
            name="MV8: ontology-native vacuum frame requirement",
            branch="u_vac must arise from vacuum substance, zeta flow, or volume configuration",
            role="prevents arbitrary preferred frame",
            allowed_if="u_vac is derived before source law uses it",
            forbidden_if="u_vac is a gauge/slicing choice",
            status="REQUIRED",
            missing="u_vac derivation",
            consequence="vacuum branch cannot proceed without defining vacuum rest frame",
        ),
        FrameBranchEntry(
            name="MV9: sign/orientation rule",
            branch="branch choice fixes creation/destruction sign of a·grad A",
            role="resolves orientation ambiguity",
            allowed_if="sign follows from branch ontology before recovery",
            forbidden_if="sign chosen to fit gamma/AB",
            status="UNRESOLVED",
            missing="sign convention from postulate/exchange law",
            consequence="required before numerical or recovery claims",
        ),
        FrameBranchEntry(
            name="MV10: chi-origin dependency",
            branch="neither matter nor vacuum frame may hide chi tuning",
            role="prevents coefficient fitting through frame choice",
            allowed_if="chi origin remains separately specified",
            forbidden_if="frame/projection absorbs coefficient choice",
            status="REQUIRED",
            missing="chi origin",
            consequence="frame branch decision does not complete Sigma_V derivation alone",
        ),
        FrameBranchEntry(
            name="MV11: boundary/no-overlap requirements",
            branch="source-driven zeta is boundary-neutral and metric insertion occurs only through B_s",
            role="protects exterior neutrality and count-once recombination",
            allowed_if="boundary neutrality and residual-kill/no-overlap theorems are attached",
            forbidden_if="either frame creates independent exterior zeta charge or residual overlap",
            status="REQUIRED",
            missing="boundary/no-overlap proof",
            consequence="even a physical frame fails if accounting fails",
        ),
        FrameBranchEntry(
            name="MV12: recommended next move",
            branch="try defining u_vac from zeta/vacuum substance before adopting matter-frame branch",
            role="best current branch decision",
            allowed_if="vacuum ontology is upstream of source coupling",
            forbidden_if="choosing matter frame only because u_vac is hard",
            status="RECOMMENDED",
            missing="vacuum rest-frame definition script",
            consequence="next script should attempt u_vac definition directly",
        ),
    ]


def print_entry(e: FrameBranchEntry) -> None:
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
    header("Case 0: Matter versus vacuum frame branch problem")

    print("Question:")
    print()
    print("  Does matter carry the clock, or does vacuum?")
    print()
    print("Goal:")
    print()
    print("  compare u_matter and u_vac frame branches before hybrid projection")
    print()
    print("Discipline:")
    print()
    print("  do not pick frame from recovery")
    print("  do not use coordinate velocity")
    print("  do not invent u_vac as convenient preferred frame")
    print("  do not use hybrid projection before both frames are defined")
    print("  protect static-source neutrality")
    print("  keep chi-origin, boundary neutrality, and no-overlap attached")

    status_line("matter/vacuum frame branch problem posed", "REQUIRED")


def case_1_inventory(entries: List[FrameBranchEntry]):
    header("Case 1: Matter versus vacuum frame branch inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[FrameBranchEntry]):
    header("Case 2: Compact matter-vacuum frame ledger")

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

    status_line("compact matter-vacuum frame ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[FrameBranchEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Matter frame is concrete but source-model dependent and static-source risky.")
    print("  Vacuum frame is ontologically preferred but missing its definition.")
    print("  Hybrid projection remains deferred.")
    print("  The next constructive step is to attempt u_vac definition from zeta/vacuum substance.")

    status_line("matter-vacuum frame status count produced", "STRUCTURAL")


def case_4_branch_decision():
    header("Case 4: Branch decision")

    print("Matter frame:")
    print("  Pros: concrete for fluids/dust; source-local.")
    print("  Risks: source-model dependence; static pressure/support artifacts.")
    print()
    print("Vacuum frame:")
    print("  Pros: ontology-native; natural for vacuum substance and zeta.")
    print("  Risks: currently undefined; can become arbitrary preferred frame.")
    print()
    print("Hybrid projection:")
    print("  Pros: may express matter acceleration relative to vacuum.")
    print("  Risks: only valid after both frames are independently defined.")
    print()
    print("Decision:")
    print("  Try to define u_vac before adopting matter frame as parent law.")

    status_line("matter-vacuum branch decision stated", "RECOMMENDED")


def case_5_good_failure():
    header("Case 5: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  u_vac cannot be defined from vacuum substance/zeta,")
    print("  and matter frame is too source-model-dependent or static-source unsafe.")
    print()
    print("Consequence:")
    print()
    print("  acceleration-gradient source law fails for now.")
    print("  Return Sigma_V to theorem target status or test broader tensor candidate.")
    print()
    print("Bad failure:")
    print("  choose matter frame because it is easy, or invent vacuum frame because it is needed.")

    status_line("matter-vacuum frame good failure stated", "DEFER")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("Matter/vacuum frame branch test fails if:")
    print()
    print("1. frame is selected from gamma_like or AB")
    print("2. coordinate velocity enters parent law")
    print("3. u_vac is arbitrary gauge/slicing")
    print("4. hybrid projection is used before both frames are defined")
    print("5. matter-frame branch creates static scalar charge")
    print("6. vacuum-frame branch invents preferred frame")
    print("7. chi-origin is hidden in frame choice")
    print("8. boundary neutrality or no-overlap is dropped")

    status_line("matter-vacuum frame failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_matter_vs_vacuum_frame_branch_test.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_vacuum_rest_frame_definition.py")
    print("   Try to define u_vac from zeta/vacuum substance ontology.")
    print()
    print("3. candidate_matter_frame_static_safety.py")
    print("   Test static-source safety for the matter-frame branch.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_vacuum_rest_frame_definition.py")
    print()
    print("Reason:")
    print("  Vacuum frame is ontologically preferred and currently missing. Define or kill it before falling back to matter-frame source law.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("The branch comparison does not choose matter frame by convenience.")
    print()
    print("Best next test:")
    print("  candidate_vacuum_rest_frame_definition.py")
    print()
    print("Reason:")
    print("  u_vac is the ontology-native frame, but it must be defined or killed.")


def main():
    header("Candidate Matter Versus Vacuum Frame Branch Test")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_branch_decision()
    case_5_good_failure()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
