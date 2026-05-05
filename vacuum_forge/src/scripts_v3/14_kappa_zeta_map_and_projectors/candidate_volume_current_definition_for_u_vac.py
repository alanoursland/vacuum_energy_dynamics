# Candidate volume current definition for u_vac
#
# Purpose
# -------
# The vacuum rest frame definition audit found:
#
#   u_vac^mu is not yet defined.
#
# Best surviving candidate:
#
#   u_vac^mu = J_V^mu / sqrt(-J_V^2)
#
# But this only works if J_V is a real vacuum-volume current.
#
# This script attempts to define J_V. If J_V remains unnamed, Group 14 should
# close with u_vac/J_V as the surviving bottleneck.
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
class VolumeCurrentEntry:
    name: str
    current: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[VolumeCurrentEntry]:
    return [
        VolumeCurrentEntry(
            name="JV1: volume-current theorem target",
            current="J_V^mu is a real vacuum-volume flux current; u_vac^mu = J_V^mu / sqrt(-J_V^2)",
            role="core definition target for vacuum rest frame",
            allowed_if="J_V is defined before recovery checks and is timelike where used",
            forbidden_if="J_V is named only to create u_vac",
            status="THEOREM_TARGET",
            missing="explicit J_V^mu",
            consequence="decides whether u_vac can be defined",
        ),
        VolumeCurrentEntry(
            name="JV2: zeta-gradient current",
            current="J_V^mu = beta_z nabla^mu zeta",
            role="simplest scalar-derived current candidate",
            allowed_if="nabla zeta is timelike and beta_z has prior origin",
            forbidden_if="used in static/equilibrium regions where gradient is not a time-flow",
            status="RISK",
            missing="causal character of nabla zeta and beta_z origin",
            consequence="likely insufficient as general vacuum rest frame",
        ),
        VolumeCurrentEntry(
            name="JV3: exchange continuity current",
            current="nabla_mu J_V^mu = Sigma_V - R_V",
            role="volume-balance candidate current",
            allowed_if="Sigma_V and R_V are defined independently",
            forbidden_if="continuity equation is written with unnamed terms",
            status="CANDIDATE",
            missing="Sigma_V, R_V, and boundary conditions",
            consequence="strongest route if volume exchange supplies conservation/balance law",
        ),
        VolumeCurrentEntry(
            name="JV4: source-driven current",
            current="J_V^mu sourced by Sigma_V ~ chi rho a^nu nabla_nu A",
            role="ties volume current to acceleration-gradient source law",
            allowed_if="source creates divergence of J_V, not arbitrary direction",
            forbidden_if="J_V direction is chosen after defining source scalar",
            status="CANDIDATE",
            missing="flux direction law and chi origin",
            consequence="needs more than scalar source; requires transport/flux law",
        ),
        VolumeCurrentEntry(
            name="JV5: equilibrium zero-flux current",
            current="u_vac is rest frame where spatial J_V vanishes locally",
            role="defines vacuum rest frame once J_V exists",
            allowed_if="J_V exists and is timelike/nonzero",
            forbidden_if="zero-flux frame is coordinate rest frame without current",
            status="SAFE_IF",
            missing="J_V itself",
            consequence="useful rest-frame definition but not a current origin",
        ),
        VolumeCurrentEntry(
            name="JV6: density-times-frame circularity",
            current="J_V^mu = n_V u_vac^mu",
            role="circular definition warning",
            allowed_if="u_vac already defined elsewhere",
            forbidden_if="used to define u_vac",
            status="REJECTED",
            missing="not pursued as definition",
            consequence="cannot define the clock using the clock",
        ),
        VolumeCurrentEntry(
            name="JV7: decorative current failure",
            current="J_V is declared as vacuum volume current without flux law",
            role="rejected shortcut",
            allowed_if="never as derivation",
            forbidden_if="used to keep u_vac branch alive",
            status="REJECTED",
            missing="not pursued",
            consequence="triggers Group 14 closure if no current is written",
        ),
        VolumeCurrentEntry(
            name="JV8: timelike/nonzero requirement",
            current="J_V^2 < 0 and J_V != 0 in regimes where u_vac is used",
            role="mathematical viability condition for normalized u_vac",
            allowed_if="proved or domain-limited",
            forbidden_if="normalization used where J_V is null/spacelike/zero",
            status="REQUIRED",
            missing="domain theorem for J_V",
            consequence="prevents invalid frame definition",
        ),
        VolumeCurrentEntry(
            name="JV9: static-source neutrality",
            current="static equilibrium sources do not produce independent exterior J_V/zeta charge",
            role="ordinary-sector safety condition",
            allowed_if="static flux is zero or boundary-neutral",
            forbidden_if="static mass creates scalar volume flux/charge",
            status="REQUIRED",
            missing="static neutrality theorem",
            consequence="kills current definitions that create scalar gravity",
        ),
        VolumeCurrentEntry(
            name="JV10: sign/orientation rule",
            current="orientation of J_V fixes creation/destruction sign",
            role="resolves volume-source sign ambiguity",
            allowed_if="orientation follows from exchange law",
            forbidden_if="sign is chosen from gamma/AB recovery",
            status="UNRESOLVED",
            missing="orientation convention",
            consequence="needed before numerical or recovery claims",
        ),
        VolumeCurrentEntry(
            name="JV11: boundary/no-overlap requirements",
            current="J_V-driven zeta is boundary-neutral and metric insertion occurs only through B_s",
            role="protects exterior neutrality and count-once recombination",
            allowed_if="boundary/no-overlap theorems are attached",
            forbidden_if="J_V creates independent residual metric trace",
            status="REQUIRED",
            missing="boundary neutrality and no-overlap proof",
            consequence="even a real current fails if accounting fails",
        ),
        VolumeCurrentEntry(
            name="JV12: recommended closure move",
            current="if exchange continuity current cannot be specified, close Group 14",
            role="best current governance decision",
            allowed_if="J_V remains undefined after this test",
            forbidden_if="continuing ratio/frame relocation loops",
            status="RECOMMENDED",
            missing="closure summary if J_V remains undefined",
            consequence="next artifact should be Group 14 closure unless J_V becomes explicit",
        ),
    ]


def print_entry(e: VolumeCurrentEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Current: {e.current}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Volume current definition for u_vac problem")

    print("Question:")
    print()
    print("  Can J_V be written, or do we close the cave?")
    print()
    print("Goal:")
    print()
    print("  test whether a real vacuum-volume current can define u_vac")
    print()
    print("Discipline:")
    print()
    print("  do not declare J_V without a flux/balance law")
    print("  do not define J_V using u_vac circularly")
    print("  require timelike/nonzero domain")
    print("  protect static-source neutrality")
    print("  preserve boundary neutrality and no-overlap")
    print("  close Group 14 if J_V remains unnamed")

    status_line("volume current definition problem posed", "REQUIRED")


def case_1_inventory(entries: List[VolumeCurrentEntry]):
    header("Case 1: Volume current definition inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[VolumeCurrentEntry]):
    header("Case 2: Compact volume-current ledger")

    print("| Entry | Current | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.current.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact volume-current ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[VolumeCurrentEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  J_V is not defined by naming it.")
    print("  zeta-gradient current is risky and probably not general.")
    print("  exchange continuity current is the strongest candidate but needs Sigma_V and R_V.")
    print("  source-driven scalar Sigma_V alone does not determine flux direction.")
    print("  if no exchange/transport law is supplied, Group 14 should close.")

    status_line("volume-current status count produced", "STRUCTURAL")


def case_4_current_decision_tree():
    header("Case 4: Volume-current decision tree")

    print("Decision tree:")
    print()
    print("1. Can J_V be defined by exchange continuity?")
    print("   Need: nabla_mu J_V^mu = Sigma_V - R_V with Sigma_V/R_V defined.")
    print()
    print("2. Can J_V be defined by zeta gradient?")
    print("   Only if grad zeta is timelike/nonzero in target regimes.")
    print()
    print("3. Can scalar Sigma_V define J_V direction?")
    print("   No, not by itself; a transport/flux law is needed.")
    print()
    print("4. Can J_V = n_V u_vac define u_vac?")
    print("   No, circular.")
    print()
    print("5. If no real J_V:")
    print("   close Group 14 with u_vac/J_V as bottleneck.")

    status_line("volume-current decision tree stated", "RECOMMENDED")


def case_5_good_failure():
    header("Case 5: Good failure / closure trigger")

    print("Good failure:")
    print()
    print("  no non-circular, timelike, boundary-neutral J_V can be defined from current ingredients.")
    print()
    print("Consequence:")
    print()
    print("  u_vac cannot currently be defined.")
    print("  Acceleration-gradient volume creation remains a theorem target, not a source law.")
    print("  Group 14 should close with J_V/u_vac as the surviving bottleneck.")
    print()
    print("Bad failure:")
    print("  declare J_V and keep going because the next equation needs a clock.")

    status_line("volume-current good failure stated", "DEFER")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("Volume-current definition fails if:")
    print()
    print("1. J_V is named but not defined")
    print("2. J_V is defined using u_vac circularly")
    print("3. zeta-gradient is used where it is not timelike/nonzero")
    print("4. scalar Sigma_V is treated as flux direction")
    print("5. Sigma_V/R_V are unnamed in continuity equation")
    print("6. static sources create independent exterior zeta charge")
    print("7. J_V creates residual metric trace outside B_s")
    print("8. sign/orientation is chosen from recovery")
    print("9. group continues without defining J_V")

    status_line("volume-current failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_volume_current_definition_for_u_vac.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_group_14_closure_summary.py")
    print("   Close Group 14 with J_V/u_vac as surviving bottleneck.")
    print()
    print("3. candidate_exchange_continuity_law_for_volume.py")
    print("   Only if the project wants one final attempt to define Sigma_V/R_V continuity.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_group_14_closure_summary.py")
    print()
    print("Reason:")
    print("  J_V remains dependent on an exchange continuity law not yet available. Close Group 14 and promote J_V/u_vac to next-group bottleneck.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("J_V is the best candidate for defining u_vac, but it is not yet defined.")
    print()
    print("The strongest possible form is an exchange continuity law:")
    print()
    print("  nabla_mu J_V^mu = Sigma_V - R_V")
    print()
    print("But Sigma_V/R_V and flux direction are not yet available.")
    print()
    print("Best next script:")
    print("  candidate_group_14_closure_summary.py")


def main():
    header("Candidate Volume Current Definition For u_vac")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_current_decision_tree()
    case_5_good_failure()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
