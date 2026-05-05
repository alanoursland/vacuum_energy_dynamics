# Candidate parent action stiffness identity
#
# Purpose
# -------
# The linear A_spatial closure coefficient-origin audit found:
#
#   q = -((alpha2 + alpha3)/alpha1)
#
# controls:
#
#   Delta A_spatial = q S_A
#
# The local linear closure branch cannot derive q by itself.
#
# This script tests whether an action/stiffness identity can derive q before
# recovery checks such as gamma_like=1 or AB=1 are applied.
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
class ActionStiffnessEntry:
    name: str
    identity: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[ActionStiffnessEntry]:
    return [
        ActionStiffnessEntry(
            name="ASG1: action/stiffness target",
            identity="S_parent[A,A_spatial,...] whose variation fixes q",
            role="candidate parent coefficient-origin identity",
            allowed_if="functional is specified before recovery checks",
            forbidden_if="functional weights are selected to recover gamma_like=1",
            status="CANDIDATE",
            missing="actual parent functional",
            consequence="could rescue the differential closure branch from coefficient tuning",
        ),
        ActionStiffnessEntry(
            name="ASG2: independent quadratic stiffness terms",
            identity="S ~ c_A |grad A|^2 + c_s |grad A_spatial|^2 + c_m A S_A + ...",
            role="minimal stiffness bookkeeping",
            allowed_if="c_A, c_s, c_m have ontology/normalization origin",
            forbidden_if="c_s/c_A is chosen after checking gamma",
            status="RISK",
            missing="coefficient-origin principle",
            consequence="too easy to become coefficient tuning unless constrained",
        ),
        ActionStiffnessEntry(
            name="ASG3: coupled stiffness term",
            identity="S includes c_cross grad A · grad A_spatial or equivalent coupling",
            role="candidate mechanism for linking A and A_spatial variations",
            allowed_if="cross term follows from parent geometry or exchange identity",
            forbidden_if="cross coefficient is chosen to force q",
            status="CANDIDATE",
            missing="cross-coupling origin",
            consequence="could derive alpha2-like coupling rather than insert it",
        ),
        ActionStiffnessEntry(
            name="ASG4: constrained variation",
            identity="variation of A and A_spatial with constraint C[A,A_spatial,S_A]=0",
            role="action route to differential compatibility",
            allowed_if="constraint is physical/structural, not recovery fitted",
            forbidden_if="constraint is B=1/A or gamma_like=1",
            status="CANDIDATE",
            missing="constraint functional and multiplier status",
            consequence="may connect action route to prior closure shell",
        ),
        ActionStiffnessEntry(
            name="ASG5: volume/zeta stiffness participation",
            identity="S includes zeta-volume stiffness coupled to A_spatial",
            role="ontology-native candidate for spatial trace response",
            allowed_if="zeta is companion or residual by no-overlap identity",
            forbidden_if="zeta supplies A_spatial and remains independent residual",
            status="RISK",
            missing="zeta role decision and no-overlap operator",
            consequence="may shift search toward volume-exchange identity",
        ),
        ActionStiffnessEntry(
            name="ASG6: coefficient-ratio theorem target",
            identity="q = q_action[c_i] fixed before gamma/AB recovery tests",
            role="core theorem target for this branch",
            allowed_if="q follows from variation and coefficient origin",
            forbidden_if="q is chosen from recovery target",
            status="THEOREM_TARGET",
            missing="variation calculation and coefficient origin",
            consequence="decides whether action/stiffness can rescue q",
        ),
        ActionStiffnessEntry(
            name="ASG7: source normalization in action",
            identity="source coupling A S_A and possible A_spatial S_A terms",
            role="determines whether source routing fixes alpha3",
            allowed_if="source couplings follow from matter/vacuum interaction rule",
            forbidden_if="A_spatial source coupling is added to tune gamma",
            status="CANDIDATE",
            missing="matter/source coupling principle",
            consequence="may derive or constrain alpha3",
        ),
        ActionStiffnessEntry(
            name="ASG8: gamma-like recovery check",
            identity="weak-field output after variation gives gamma_like=1",
            role="recovery target",
            allowed_if="checked after functional and q are fixed",
            forbidden_if="used to select stiffness coefficients",
            status="RECOVERY_TARGET",
            missing="weak-field solution from varied equations",
            consequence="tests action/stiffness identity; does not determine it",
        ),
        ActionStiffnessEntry(
            name="ASG9: AB exterior diagnostic check",
            identity="exterior solution after variation yields kappa_areal -> 0 / AB -> 1",
            role="reduced exterior recovery test",
            allowed_if="emerges after solving varied equations",
            forbidden_if="used as constraint term or boundary target in action",
            status="RECOVERY_TARGET",
            missing="exterior solution and boundary class",
            consequence="keeps AB diagnostic-only",
        ),
        ActionStiffnessEntry(
            name="ASG10: no-overlap trace condition",
            identity="variation preserves Trace_A_mass + Trace_residual_neutral, overlap=0",
            role="prevents action from double-counting zeta/kappa trace",
            allowed_if="overlap operator, residual kill, or non-metric residual status is derived",
            forbidden_if="action gives A_spatial and independent zeta/kappa trace",
            status="THEOREM_TARGET",
            missing="overlap operator or residual status theorem",
            consequence="derived q still fails if trace accounting fails",
        ),
        ActionStiffnessEntry(
            name="ASG11: stiffness tuning failure",
            identity="functional coefficients chosen to match gamma_like or Schwarzschild expansion",
            role="branch-kill/defer detector",
            allowed_if="used only as no-go diagnosis",
            forbidden_if="accepted as derivation",
            status="REJECTED",
            missing="not pursued",
            consequence="kills action/stiffness as coefficient-origin route if unavoidable",
        ),
        ActionStiffnessEntry(
            name="ASG12: recommended next test",
            identity="write minimal coupled stiffness functional and variation ledger",
            role="most concrete way to test action/stiffness origin",
            allowed_if="functional is explicit and recovery checks are downstream",
            forbidden_if="functional is merely named",
            status="RECOMMENDED",
            missing="minimal action variation script",
            consequence="next script should test a minimal action ansatz and derive alpha/q if possible",
        ),
    ]


def print_entry(e: ActionStiffnessEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Identity: {e.identity}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Parent action/stiffness identity problem")

    print("Question:")
    print()
    print("  Can an action or stiffness identity fix q without fitting recovery targets?")
    print()
    print("Goal:")
    print()
    print("  test whether coefficient ratios can be derived from a parent functional")
    print()
    print("Discipline:")
    print()
    print("  do not choose stiffness coefficients from gamma_like=1")
    print("  do not use AB=1 as an action constraint")
    print("  do not insert Schwarzschild as variational target")
    print("  do not let zeta double-count residual trace")
    print("  derive q before recovery checks")
    print("  branch-kill if coefficients remain free repair knobs")

    status_line("parent action/stiffness problem posed", "REQUIRED")


def case_1_inventory(entries: List[ActionStiffnessEntry]):
    header("Case 1: Action/stiffness identity inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[ActionStiffnessEntry]):
    header("Case 2: Compact action/stiffness ledger")

    print("| Entry | Identity | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.identity.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact action/stiffness ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[ActionStiffnessEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Action/stiffness is a legitimate q-origin candidate only if the functional is explicit.")
    print("  Independent quadratic stiffness terms are not enough if coefficients remain free.")
    print("  Coupled stiffness or constrained variation are stronger candidates.")
    print("  Zeta participation is possible but risks leaving the A-local branch.")
    print("  Recovery checks must remain downstream.")

    status_line("action/stiffness status count produced", "STRUCTURAL")


def case_4_minimal_functional_targets():
    header("Case 4: Minimal functional targets")

    print("Minimal functional families to test next:")
    print()
    print("1. Independent stiffness:")
    print("   S ~ c_A |grad A|^2 + c_s |grad A_spatial|^2 + c_m A S_A")
    print()
    print("2. Coupled stiffness:")
    print("   S ~ c_A |grad A|^2 + c_s |grad A_spatial|^2 + c_x grad A · grad A_spatial + c_m A S_A")
    print()
    print("3. Constrained variation:")
    print("   S + lambda C[A,A_spatial,S_A]")
    print()
    print("4. Zeta-coupled stiffness:")
    print("   S[A,A_spatial,zeta] with overlap(A_spatial,zeta_residual)=0")
    print()
    print("Each must derive q before gamma_like or AB checks.")

    status_line("minimal functional targets stated", "CANDIDATE")


def case_5_good_failure():
    header("Case 5: Good failure / branch defer")

    print("Good failure:")
    print()
    print("  every minimal action/stiffness functional leaves q as a free ratio")
    print("  unless coefficients are chosen from recovery targets.")
    print()
    print("Consequence:")
    print()
    print("  action/stiffness does not rescue local coefficient origin by itself.")
    print("  Search should move to conservation-current or volume-exchange identity.")
    print()
    print("Bad failure:")
    print("  choose stiffness weights to fit gamma_like=1 and call it derivation.")

    status_line("action/stiffness good failure stated", "DEFER")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("Action/stiffness identity fails if:")
    print()
    print("1. coefficients are chosen after gamma_like check")
    print("2. AB=1 is inserted as a constraint term")
    print("3. Schwarzschild form is used as variational target")
    print("4. cross-coupling coefficient is tuned to produce q")
    print("5. source coupling is added only to fix q")
    print("6. zeta supplies spatial stiffness and remains independent residual")
    print("7. no-overlap theorem is ignored")
    print("8. functional is named but not written")

    status_line("action/stiffness failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_parent_action_stiffness_identity.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_minimal_coupled_stiffness_variation.py")
    print("   Write minimal coupled stiffness functional and vary it symbolically.")
    print()
    print("3. candidate_conservation_current_coefficient_origin.py")
    print("   Test conservation-current origin if stiffness leaves q free.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_minimal_coupled_stiffness_variation.py")
    print()
    print("Reason:")
    print("  The action/stiffness branch only becomes meaningful when a concrete functional is varied. Test coupled stiffness first.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("Action/stiffness is a legitimate q-origin candidate only if it writes a functional and derives q before recovery checks.")
    print()
    print("Best next test:")
    print("  candidate_minimal_coupled_stiffness_variation.py")
    print()
    print("Reason:")
    print("  coupled stiffness is the minimal action route that can relate A and A_spatial without setting q by hand.")


def main():
    header("Candidate Parent Action Stiffness Identity")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_minimal_functional_targets()
    case_5_good_failure()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
