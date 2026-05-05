# Candidate minimal volume-exchange operator ansatz
#
# Purpose
# -------
# The volume-exchange stiffness-ratio origin audit found:
#
#   Volume exchange is the next ontology-native candidate.
#
# It only helps if:
#
#   V[A,B_s,zeta] is explicit,
#   it fixes the ratio before recovery checks,
#   and zeta does not double-count residual trace.
#
# This script attempts minimal explicit exchange-operator shells.
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
class VolumeOperatorEntry:
    name: str
    ansatz: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[VolumeOperatorEntry]:
    return [
        VolumeOperatorEntry(
            name="VO1: minimal exchange target",
            ansatz="V[A,B_s,zeta] enters A/B_s balance and fixes r_V before recovery checks",
            role="core explicit volume-exchange goal",
            allowed_if="operator is written and coefficient-fixed internally",
            forbidden_if="V is named but not specified",
            status="THEOREM_TARGET",
            missing="explicit V operator",
            consequence="decides whether volume exchange can end ratio relocation",
        ),
        VolumeOperatorEntry(
            name="VO2: algebraic companion ansatz",
            ansatz="B_s = F_V[zeta,A] or B_s - lambda zeta = G[A]",
            role="direct zeta-to-spatial companion shell",
            allowed_if="lambda or F_V is derived before recovery checks",
            forbidden_if="lambda is chosen to fit gamma_like or AB",
            status="RISK",
            missing="derivation of F_V/lambda and gauge status",
            consequence="likely makes zeta an A_spatial companion, not residual",
        ),
        VolumeOperatorEntry(
            name="VO3: derivative exchange ansatz",
            ansatz="V ~ eta1 grad B_s·grad zeta + eta2 grad A·grad zeta + eta3 grad A·grad B_s",
            role="coupled stiffness extension with volume variable",
            allowed_if="eta ratios have ontology origin",
            forbidden_if="eta ratios are chosen to repair q",
            status="CANDIDATE",
            missing="eta-ratio origin",
            consequence="may still relocate coefficient problem unless exchange fixes eta ratios",
        ),
        VolumeOperatorEntry(
            name="VO4: volume-current ansatz",
            ansatz="J_V^i = u grad^i zeta + v grad^i B_s + w grad^i A",
            role="current-route volume exchange candidate",
            allowed_if="u:v:w fixed by volume flux law",
            forbidden_if="current coefficients chosen from recovery checks",
            status="CANDIDATE",
            missing="volume flux law",
            consequence="could fix current ratio if vacuum-volume flux is real",
        ),
        VolumeOperatorEntry(
            name="VO5: source-coupled volume creation ansatz",
            ansatz="Sigma_V = chi S_A or Sigma_V = chi rho a·grad A",
            role="routes source/mass response into volume creation",
            allowed_if="chi and source form follow from postulates before recovery checks",
            forbidden_if="Sigma_V is added to force gamma_like",
            status="CANDIDATE",
            missing="covariant source-driven volume creation law",
            consequence="connects to mass accelerating across gradient coupling",
        ),
        VolumeOperatorEntry(
            name="VO6: relaxation-to-volume ansatz",
            ansatz="R_V = -lambda_relax (zeta - zeta_min) coupled to B_s",
            role="possible first-order residual/relaxation channel",
            allowed_if="relaxation is boundary-neutral and not coefficient patching",
            forbidden_if="relaxation term repairs missing q-origin",
            status="RISK",
            missing="relaxation frame and boundary theorem",
            consequence="may belong to P_relax rather than A_spatial q-origin",
        ),
        VolumeOperatorEntry(
            name="VO7: zeta companion status",
            ansatz="zeta becomes B_s companion if V fixes B_s ratio",
            role="status consequence, not optional decoration",
            allowed_if="residual zeta trace is killed or made non-metric",
            forbidden_if="zeta remains independent residual trace",
            status="REQUIRED",
            missing="zeta companion-vs-residual decision",
            consequence="forces revisit of zeta primary/residual convention",
        ),
        VolumeOperatorEntry(
            name="VO8: zeta residual-only status",
            ansatz="zeta remains residual; V does not fix B_s ratio",
            role="safe accounting branch but no q-origin",
            allowed_if="separate q-origin exists or A_spatial remains theorem target",
            forbidden_if="zeta residual is also used to fix B_s",
            status="SAFE_IF",
            missing="separate q-origin",
            consequence="preserves residual convention but does not solve A_spatial",
        ),
        VolumeOperatorEntry(
            name="VO9: boundary neutrality requirement",
            ansatz="Q_ext[V] = 0 unless V is absorbed into A_spatial companion",
            role="protects no exterior scalar charge",
            allowed_if="boundary neutrality theorem is stated or residual is non-metric",
            forbidden_if="V creates exterior zeta/kappa charge",
            status="REQUIRED",
            missing="boundary neutrality theorem",
            consequence="prevents volume exchange from becoming scalar gravity",
        ),
        VolumeOperatorEntry(
            name="VO10: no-overlap operator",
            ansatz="O[B_s,zeta_residual/kappa_residual] = 0",
            role="protects count-once recombination",
            allowed_if="O is explicit or residual killed",
            forbidden_if="B_s and residual trace overlap",
            status="THEOREM_TARGET",
            missing="overlap operator / residual kill theorem",
            consequence="volume exchange fails if it double-counts trace",
        ),
        VolumeOperatorEntry(
            name="VO11: recovery checks downstream",
            ansatz="after V fixes ratio, test gamma_like=1 and AB->1",
            role="ordinary-regime recovery targets",
            allowed_if="checked after V is fixed",
            forbidden_if="used to choose V coefficients",
            status="RECOVERY_TARGET",
            missing="solutions from exchange operator",
            consequence="tests but does not define V",
        ),
        VolumeOperatorEntry(
            name="VO12: recommended next move",
            ansatz="test derivative/current/source-coupled V shells; then decide zeta companion vs residual",
            role="best current concrete path",
            allowed_if="each shell has branch-kill criteria",
            forbidden_if="leaving V as unnamed ontology",
            status="RECOMMENDED",
            missing="operator test / zeta status script",
            consequence="next script should decide whether zeta can be companion or residual after V shells",
        ),
    ]


def print_entry(e: VolumeOperatorEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Ansatz: {e.ansatz}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Minimal volume-exchange operator ansatz problem")

    print("Question:")
    print()
    print("  Can V[A,B_s,zeta] be written, or is volume exchange just a shiny missing equation?")
    print()
    print("Goal:")
    print()
    print("  attempt explicit volume-exchange operator shells")
    print()
    print("Discipline:")
    print()
    print("  do not leave V unnamed")
    print("  do not choose exchange coefficients from gamma_like or AB")
    print("  do not let zeta be both B_s companion and residual")
    print("  preserve boundary neutrality")
    print("  preserve no-overlap trace theorem")
    print("  allow branch-defer if V only relocates coefficients")

    status_line("minimal volume-exchange operator problem posed", "REQUIRED")


def case_1_inventory(entries: List[VolumeOperatorEntry]):
    header("Case 1: Minimal volume-exchange operator inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[VolumeOperatorEntry]):
    header("Case 2: Compact volume-operator ledger")

    print("| Entry | Ansatz | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.ansatz.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact volume-operator ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[VolumeOperatorEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Explicit V shells can be named, but coefficient origin remains unresolved unless a volume law fixes the ratios.")
    print("  If zeta fixes B_s, zeta cannot remain independent residual trace.")
    print("  Boundary neutrality and no-overlap are mandatory.")
    print("  The next decision is zeta companion versus residual after the V-shell inventory.")

    status_line("volume-operator status count produced", "STRUCTURAL")


def case_4_operator_shells():
    header("Case 4: Operator shells to test")

    print("Minimal shells:")
    print()
    print("1. Algebraic companion:")
    print("   B_s = F_V[zeta,A]")
    print()
    print("2. Derivative exchange:")
    print("   V ~ eta1 grad B_s·grad zeta + eta2 grad A·grad zeta + eta3 grad A·grad B_s")
    print()
    print("3. Volume current:")
    print("   J_V^i = u grad^i zeta + v grad^i B_s + w grad^i A")
    print()
    print("4. Source-coupled volume creation:")
    print("   Sigma_V = chi S_A")
    print("   or Sigma_V = chi rho a·grad A")
    print()
    print("5. Relaxation-to-volume:")
    print("   R_V = -lambda_relax (zeta - zeta_min)")
    print()
    print("Each must fix ratios before recovery checks or be treated as decorative.")

    status_line("volume-exchange operator shells stated", "CANDIDATE")


def case_5_good_failure():
    header("Case 5: Good failure / decision")

    print("Good failure:")
    print()
    print("  all explicit V shells either leave free coefficients or make zeta double-count residual trace.")
    print()
    print("Consequence:")
    print()
    print("  volume exchange does not yet derive q.")
    print("  Next work must decide zeta companion versus residual, or return A_spatial to recovery theorem target status.")
    print()
    print("Bad failure:")
    print("  keep saying vacuum volume fixes q while V is still unnamed.")

    status_line("volume-operator good failure stated", "DEFER")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("Minimal volume-exchange operator test fails if:")
    print()
    print("1. V remains unnamed")
    print("2. exchange coefficients are chosen from gamma_like")
    print("3. AB diagnostic fixes exchange coefficients")
    print("4. zeta fixes B_s and remains independent residual")
    print("5. boundary neutrality is not enforced")
    print("6. no-overlap theorem is absent")
    print("7. source-driven volume creation has no covariant/source expression")
    print("8. V only relocates coefficient freedom")

    status_line("volume-operator failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_minimal_volume_exchange_operator_ansatz.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_zeta_companion_vs_residual_decision.py")
    print("   Decide whether zeta can be B_s companion or residual, but not both.")
    print()
    print("3. candidate_source_driven_volume_creation_law.py")
    print("   Test source-coupled vacuum creation expression.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_zeta_companion_vs_residual_decision.py")
    print()
    print("Reason:")
    print("  Every useful V shell forces zeta status. Decide companion versus residual before adding more exchange structure.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("Minimal V shells can be written, but the decisive issue is zeta status.")
    print()
    print("If zeta fixes B_s:")
    print("  it cannot remain independent residual trace.")
    print()
    print("If zeta remains residual:")
    print("  it probably does not fix q.")
    print()
    print("Best next test:")
    print("  candidate_zeta_companion_vs_residual_decision.py")


def main():
    header("Candidate Minimal Volume-Exchange Operator Ansatz")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_operator_shells()
    case_5_good_failure()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
