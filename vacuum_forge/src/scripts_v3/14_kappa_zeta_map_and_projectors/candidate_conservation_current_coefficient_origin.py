# Candidate conservation-current coefficient origin
#
# Purpose
# -------
# The stiffness-ratio origin inventory found:
#
#   r_s = c_x/c_s
#   q_action = -r_s
#
# Free stiffness ratio is rejected.
#
# Symmetry and normalization are possible but currently unspecified.
# Conservation-current origin is the strongest next non-tuning route.
#
# This script tests whether a conserved current / balance law can fix c_x/c_s.
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
class ConservationOriginEntry:
    name: str
    current: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[ConservationOriginEntry]:
    return [
        ConservationOriginEntry(
            name="CC1: conservation-current target",
            current="div J_A[A,B_s,T] = 0 fixes r_s = c_x/c_s",
            role="candidate non-tuning origin for stiffness ratio",
            allowed_if="J_A is explicitly defined before recovery checks",
            forbidden_if="current is decorative or retrofitted to gamma_like",
            status="CANDIDATE",
            missing="explicit J_A and balance law",
            consequence="could rescue stiffness-ratio origin if non-decorative",
        ),
        ConservationOriginEntry(
            name="CC2: gradient current",
            current="J_A^i = a grad^i A + b grad^i B_s",
            role="minimal local current tying A and B_s gradients",
            allowed_if="a:b is fixed by source routing or identity before recovery",
            forbidden_if="a:b is chosen to force r_s",
            status="CANDIDATE",
            missing="origin of a:b",
            consequence="risks moving ratio problem from c_x/c_s to a:b",
        ),
        ConservationOriginEntry(
            name="CC3: source-balance current",
            current="div J_A = S_A - S_spatial or equivalent balance equation",
            role="routes source response between A and B_s",
            allowed_if="both source terms are defined from same matter/vacuum coupling",
            forbidden_if="S_spatial is invented to repair gamma_like",
            status="RISK",
            missing="definition of S_spatial and coupling rule",
            consequence="may derive ratio if source balance is real, but high tuning risk",
        ),
        ConservationOriginEntry(
            name="CC4: parent balance identity",
            current="Div E_parent = B_closed[T] + B_relax",
            role="broader conservation/Bianchi-like route",
            allowed_if="E_parent, B_closed, and B_relax are defined",
            forbidden_if="Bianchi-like words replace an actual operator",
            status="CANDIDATE",
            missing="parent operator and balance terms",
            consequence="likely necessary if local current is insufficient",
        ),
        ConservationOriginEntry(
            name="CC5: stiffness-current equivalence",
            current="J_A derived from variation of coupled stiffness functional",
            role="checks whether current adds new information or restates action",
            allowed_if="current imposes an additional identity beyond Euler-Lagrange equations",
            forbidden_if="current merely restates q = -c_x/c_s",
            status="CONSTRAINED",
            missing="Noether/source-balance relation",
            consequence="prevents conservation route from duplicating stiffness ratio problem",
        ),
        ConservationOriginEntry(
            name="CC6: current fixes ratio theorem target",
            current="r_s = r_J[J_A] before gamma/AB checks",
            role="core theorem target for conservation-current branch",
            allowed_if="ratio follows from current/balance identity",
            forbidden_if="ratio is selected after recovery checks",
            status="THEOREM_TARGET",
            missing="derivation of r_J",
            consequence="decides whether conservation route rescues q-origin",
        ),
        ConservationOriginEntry(
            name="CC7: decorative conservation failure",
            current="declare div J_A=0 without defining J_A",
            role="rejected shortcut",
            allowed_if="never as derivation",
            forbidden_if="used to save coefficient origin",
            status="REJECTED",
            missing="not pursued",
            consequence="kills conservation-current route if no current can be written",
        ),
        ConservationOriginEntry(
            name="CC8: gamma-like recovery check",
            current="weak-field output after r_s fixed gives gamma_like=1",
            role="downstream recovery target",
            allowed_if="checked after current fixes r_s",
            forbidden_if="used to define J_A or r_s",
            status="RECOVERY_TARGET",
            missing="weak-field map from current-fixed ratio",
            consequence="tests but does not determine the current",
        ),
        ConservationOriginEntry(
            name="CC9: AB exterior diagnostic check",
            current="exterior solution after current-fixed r_s gives AB -> 1 diagnostic",
            role="downstream exterior recovery test",
            allowed_if="checked after solving equations",
            forbidden_if="used as current constraint",
            status="RECOVERY_TARGET",
            missing="exterior solution with current-fixed ratio",
            consequence="keeps AB diagnostic-only",
        ),
        ConservationOriginEntry(
            name="CC10: no-overlap compatibility",
            current="current-fixed B_s must not overlap zeta/kappa residual trace",
            role="protects count-once theorem",
            allowed_if="overlap operator or residual status theorem is present",
            forbidden_if="current fixes ratio but creates trace double-counting",
            status="THEOREM_TARGET",
            missing="overlap operator or residual theorem",
            consequence="conservation-derived ratio still fails if trace accounting fails",
        ),
        ConservationOriginEntry(
            name="CC11: conservation route failure",
            current="no explicit current/balance law fixes r_s before recovery",
            role="good failure / branch defer",
            allowed_if="used to move search to volume-exchange or parent identity",
            forbidden_if="patched by fitted current",
            status="DEFER",
            missing="explicit current/balance law",
            consequence="action/stiffness plus conservation cannot derive q locally",
        ),
        ConservationOriginEntry(
            name="CC12: recommended next move",
            current="attempt minimal gradient-current ledger before volume-exchange branch",
            role="best current concrete conservation test",
            allowed_if="a:b origin and shortcut checks are explicit",
            forbidden_if="current is only symbolic decoration",
            status="RECOMMENDED",
            missing="minimal current ansatz script",
            consequence="next script should test gradient-current ansatz and whether it merely relocates the ratio",
        ),
    ]


def print_entry(e: ConservationOriginEntry) -> None:
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
    header("Case 0: Conservation-current coefficient-origin problem")

    print("Question:")
    print()
    print("  Can a real conserved current fix c_x/c_s before recovery checks?")
    print()
    print("Goal:")
    print()
    print("  test whether conservation-current origin is more than decorative balance language")
    print()
    print("Discipline:")
    print()
    print("  define J_A before using it")
    print("  do not choose current coefficients from gamma_like")
    print("  do not use AB=1 as current constraint")
    print("  do not invent source balance to patch recovery")
    print("  do not ignore no-overlap trace theorem")
    print("  defer if conservation only relocates the ratio problem")

    status_line("conservation-current coefficient-origin problem posed", "REQUIRED")


def case_1_inventory(entries: List[ConservationOriginEntry]):
    header("Case 1: Conservation-current origin inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[ConservationOriginEntry]):
    header("Case 2: Compact conservation-current ledger")

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

    status_line("compact conservation-current ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[ConservationOriginEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Conservation-current origin is viable only if J_A is explicit.")
    print("  Minimal gradient currents risk moving the ratio from c_x/c_s to a:b.")
    print("  A parent balance identity may be needed if local current is insufficient.")
    print("  Decorative conservation is rejected.")

    status_line("conservation-current status count produced", "STRUCTURAL")


def case_4_minimal_current_shape():
    header("Case 4: Minimal current shape")

    print("Minimal local current ansatz:")
    print()
    print("  J_A^i = a grad^i A + b grad^i B_s")
    print()
    print("Then:")
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
    print("For div J_A = 0 with nonzero S_A:")
    print()
    print("  q = -a/b")
    print()
    print("Interpretation:")
    print("  conservation fixes q only if a/b is itself derived.")
    print("  Otherwise the ratio problem has merely moved from c_x/c_s to a/b.")

    status_line("minimal current shape stated", "THEOREM_TARGET")


def case_5_good_failure():
    header("Case 5: Good failure / defer outcome")

    print("Good failure:")
    print()
    print("  minimal current gives q = -a/b, but no pre-recovery principle fixes a/b.")
    print()
    print("Consequence:")
    print()
    print("  local conservation current does not solve q-origin.")
    print("  Move to broader parent balance or volume-exchange identity.")
    print()
    print("Bad failure:")
    print("  choose a/b from gamma_like=1 and call it conservation.")

    status_line("conservation-current good failure stated", "DEFER")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("Conservation-current origin fails if:")
    print()
    print("1. J_A is not defined")
    print("2. current coefficients are chosen from gamma_like")
    print("3. current coefficients are chosen from AB=1")
    print("4. source-balance term is invented to repair recovery")
    print("5. current merely restates stiffness ratio")
    print("6. a/b remains free but q is claimed derived")
    print("7. no-overlap theorem is ignored after current fixes q")
    print("8. parent balance terms are named but not defined")

    status_line("conservation-current failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_conservation_current_coefficient_origin.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_minimal_gradient_current_ratio_test.py")
    print("   Test whether J_A^i = a grad A + b grad B_s genuinely fixes q or moves the ratio.")
    print()
    print("3. candidate_volume_exchange_stiffness_ratio_origin.py")
    print("   Move to zeta/vacuum-volume exchange if current route remains free.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_minimal_gradient_current_ratio_test.py")
    print()
    print("Reason:")
    print("  The conservation route must now test the minimal current shape explicitly before claiming q-origin.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("Conservation current can fix q only if the current coefficient ratio is derived.")
    print()
    print("Minimal current:")
    print("  J_A^i = a grad^i A + b grad^i B_s")
    print()
    print("gives:")
    print("  q = -a/b")
    print()
    print("This is useful only if a/b is fixed before recovery checks.")
    print()
    print("Best next test:")
    print("  candidate_minimal_gradient_current_ratio_test.py")


def main():
    header("Candidate Conservation-Current Coefficient Origin")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_minimal_current_shape()
    case_5_good_failure()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
