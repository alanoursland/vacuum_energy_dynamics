# Candidate vacuum rest frame definition
#
# Purpose
# -------
# The matter versus vacuum frame branch test found:
#
#   u_vac is the ontology-native frame,
#   but it must be defined or killed.
#
# This script inventories possible definitions of u_vac from zeta, vacuum
# substance, volume configuration, or equilibrium structure.
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
class VacuumFrameEntry:
    name: str
    definition: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[VacuumFrameEntry]:
    return [
        VacuumFrameEntry(
            name="VF1: vacuum frame theorem target",
            definition="u_vac^mu is derived from vacuum substance / zeta / volume configuration",
            role="core ontology-native frame target",
            allowed_if="definition is independent of recovery checks",
            forbidden_if="u_vac is invented to make Sigma_V work",
            status="THEOREM_TARGET",
            missing="actual definition of u_vac^mu",
            consequence="decides whether acceleration-gradient source law can proceed",
        ),
        VacuumFrameEntry(
            name="VF2: zeta-gradient normal candidate",
            definition="u_vac^mu parallel to normalized timelike gradient of zeta, if grad zeta is timelike",
            role="local scalar-clock candidate",
            allowed_if="nabla_mu zeta is timelike and nonzero in the regime of interest",
            forbidden_if="used where zeta gradient is spacelike/null/zero or gauge-dependent",
            status="RISK",
            missing="causal character and slicing/gauge status of zeta",
            consequence="may fail in static or equilibrium regions where zeta has no usable time gradient",
        ),
        VacuumFrameEntry(
            name="VF3: vacuum volume current candidate",
            definition="u_vac^mu = J_V^mu / sqrt(-J_V^2), with J_V a vacuum-volume flux current",
            role="best physical-flow candidate if J_V exists",
            allowed_if="J_V is defined by volume exchange law before recovery checks",
            forbidden_if="J_V is invented after choosing u_vac",
            status="CANDIDATE",
            missing="explicit J_V^mu",
            consequence="strongest route if volume exchange supplies a real current",
        ),
        VacuumFrameEntry(
            name="VF4: local equilibrium frame candidate",
            definition="u_vac is frame in which local vacuum volume flux vanishes / zeta configuration is at rest",
            role="rest-frame-by-equilibrium definition",
            allowed_if="vacuum equilibrium condition is defined invariantly",
            forbidden_if="equilibrium frame is just chosen coordinates",
            status="CANDIDATE",
            missing="invariant rest/equilibrium criterion",
            consequence="may define u_vac in static regions without scalar time gradient",
        ),
        VacuumFrameEntry(
            name="VF5: hypersurface-normal diagnostic",
            definition="u_vac^mu = n^mu normal to preferred zeta/vacuum-volume foliation",
            role="mathematical diagnostic candidate",
            allowed_if="foliation is physically defined by vacuum ontology",
            forbidden_if="n^mu is arbitrary ADM/gauge slicing",
            status="CONSTRAINED",
            missing="physical foliation rule",
            consequence="diagnostic only unless vacuum ontology picks the slices",
        ),
        VacuumFrameEntry(
            name="VF6: matter-comoving fallback",
            definition="u_vac^mu = u_m^mu in tightly coupled matter/vacuum equilibrium",
            role="fallback branch where vacuum is dragged by matter",
            allowed_if="matter-vacuum locking is derived and not assumed generally",
            forbidden_if="used to choose matter frame by convenience",
            status="RISK",
            missing="matter-vacuum locking law",
            consequence="may collapse back to matter-frame source-model dependence",
        ),
        VacuumFrameEntry(
            name="VF7: arbitrary preferred frame",
            definition="u_vac chosen as convenient background rest frame",
            role="forbidden shortcut",
            allowed_if="never as parent definition",
            forbidden_if="used to make acceleration-gradient branch work",
            status="REJECTED",
            missing="not pursued",
            consequence="would introduce an unsupported preferred frame",
        ),
        VacuumFrameEntry(
            name="VF8: static-source neutrality requirement",
            definition="u_vac definition yields Sigma_V static-neutral or boundary-neutral around equilibrium sources",
            role="ordinary-sector safety requirement",
            allowed_if="static source does not create independent exterior zeta charge",
            forbidden_if="vacuum frame creates scalar charge around static mass",
            status="REQUIRED",
            missing="static neutrality theorem",
            consequence="kills u_vac definitions that create ordinary scalar gravity",
        ),
        VacuumFrameEntry(
            name="VF9: sign/orientation rule",
            definition="u_vac and projection fix sign of a_vac dot grad A as creation/destruction",
            role="resolves source-law orientation ambiguity",
            allowed_if="sign follows from vacuum-volume exchange convention",
            forbidden_if="sign is chosen from gamma/AB recovery",
            status="UNRESOLVED",
            missing="creation/destruction orientation rule",
            consequence="needed before numerical or recovery claims",
        ),
        VacuumFrameEntry(
            name="VF10: chi-origin dependency",
            definition="u_vac definition does not determine chi by recovery fitting",
            role="prevents frame from hiding coefficient origin",
            allowed_if="chi remains separately derived from exchange/source coupling",
            forbidden_if="normalization of u_vac/J_V absorbs chi tuning",
            status="REQUIRED",
            missing="chi origin",
            consequence="u_vac alone does not complete Sigma_V",
        ),
        VacuumFrameEntry(
            name="VF11: boundary/no-overlap requirements",
            definition="source-driven zeta is boundary-neutral and enters metric only through B_s",
            role="protects exterior neutrality and count-once recombination",
            allowed_if="boundary neutrality and residual-kill/no-overlap theorems are attached",
            forbidden_if="u_vac route creates independent residual metric trace",
            status="REQUIRED",
            missing="boundary/no-overlap proof",
            consequence="even a defined u_vac fails if accounting fails",
        ),
        VacuumFrameEntry(
            name="VF12: recommended next move",
            definition="try volume-current J_V definition first; otherwise closure summary",
            role="best current branch decision",
            allowed_if="J_V is treated as required structure, not decoration",
            forbidden_if="continuing with unnamed vacuum frame",
            status="RECOMMENDED",
            missing="volume-current definition or group closure",
            consequence="next script should either define J_V or close Group 14 with u_vac as bottleneck",
        ),
    ]


def print_entry(e: VacuumFrameEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Definition: {e.definition}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Vacuum rest frame definition problem")
    print("Question:")
    print()
    print("  Is u_vac a real ontology object, or just a clock drawn on the cave wall?")
    print()
    print("Goal:")
    print()
    print("  attempt to define u_vac from zeta, vacuum substance, volume flow, or equilibrium")
    print()
    print("Discipline:")
    print()
    print("  do not invent a preferred frame")
    print("  do not choose u_vac from gamma_like or AB")
    print("  do not use arbitrary slicing as ontology")
    print("  protect static-source neutrality")
    print("  keep chi-origin separate")
    print("  preserve boundary neutrality and no-overlap")
    print("  close the group if u_vac cannot be defined")

    status_line("vacuum rest frame definition problem posed", "REQUIRED")


def case_1_inventory(entries: List[VacuumFrameEntry]):
    header("Case 1: Vacuum rest frame definition inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[VacuumFrameEntry]):
    header("Case 2: Compact vacuum-frame ledger")

    print("| Entry | Definition | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.definition.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact vacuum-frame ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[VacuumFrameEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  u_vac cannot be an arbitrary preferred frame.")
    print("  zeta-gradient normal is risky because zeta may not provide a timelike clock.")
    print("  volume-current J_V is the strongest candidate if the exchange law supplies it.")
    print("  equilibrium-frame definition may work in static regions if defined invariantly.")
    print("  if neither J_V nor equilibrium frame can be defined, Group 14 should close with u_vac as the bottleneck.")

    status_line("vacuum-frame status count produced", "STRUCTURAL")


def case_4_definition_decision_tree():
    header("Case 4: Vacuum-frame definition decision tree")

    print("Decision tree:")
    print()
    print("1. Does volume exchange define a current J_V?")
    print("   If yes: define u_vac = normalized J_V.")
    print()
    print("2. If no J_V, does zeta define a timelike gradient?")
    print("   If yes: zeta-gradient normal may define local vacuum clock.")
    print()
    print("3. If no zeta clock, does vacuum equilibrium define a rest frame?")
    print("   If yes: use invariant zero-flux/equilibrium frame.")
    print()
    print("4. If only arbitrary slicing remains:")
    print("   reject u_vac as parent frame.")
    print()
    print("5. If u_vac cannot be defined:")
    print("   close Group 14 with u_vac as surviving bottleneck.")

    status_line("vacuum-frame definition decision tree stated", "RECOMMENDED")


def case_5_good_failure():
    header("Case 5: Good failure / group closure trigger")

    print("Good failure:")
    print()
    print("  no J_V, zeta-clock, or invariant equilibrium criterion defines u_vac.")
    print()
    print("Consequence:")
    print()
    print("  acceleration-gradient volume creation cannot currently be promoted.")
    print("  Group 14 should close with u_vac / volume-current definition as the surviving bottleneck.")
    print()
    print("Bad failure:")
    print("  choose a convenient preferred frame and continue as if u_vac were derived.")

    status_line("vacuum-frame good failure stated", "DEFER")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("Vacuum-frame definition fails if:")
    print()
    print("1. u_vac is arbitrary preferred frame")
    print("2. u_vac is chosen from gamma_like or AB")
    print("3. zeta-gradient is used where not timelike/nonzero")
    print("4. hypersurface normal is arbitrary gauge slicing")
    print("5. J_V is named but not defined")
    print("6. equilibrium frame is coordinate rest frame")
    print("7. static source creates independent exterior zeta charge")
    print("8. boundary neutrality or no-overlap is dropped")
    print("9. chi tuning is hidden in normalization")

    status_line("vacuum-frame failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_vacuum_rest_frame_definition.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_volume_current_definition_for_u_vac.py")
    print("   Try to define J_V and u_vac = normalized J_V.")
    print()
    print("3. candidate_group_14_closure_summary.py")
    print("   Close Group 14 if J_V cannot be defined immediately.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_volume_current_definition_for_u_vac.py")
    print()
    print("Reason:")
    print("  J_V is the strongest non-arbitrary u_vac candidate. Test it once, then close the group if it remains unnamed.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("u_vac is not yet defined.")
    print()
    print("Best surviving candidate:")
    print("  u_vac^mu = J_V^mu / sqrt(-J_V^2)")
    print()
    print("But this only works if J_V is a real vacuum-volume current.")
    print()
    print("Best next test:")
    print("  candidate_volume_current_definition_for_u_vac.py")
    print()
    print("Group closure note:")
    print("  If J_V cannot be defined, close Group 14 with u_vac/J_V as the surviving bottleneck.")


def main():
    header("Candidate Vacuum Rest Frame Definition")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_definition_decision_tree()
    case_5_good_failure()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
