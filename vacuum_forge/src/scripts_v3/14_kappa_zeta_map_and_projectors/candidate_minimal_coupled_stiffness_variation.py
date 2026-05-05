# Candidate minimal coupled stiffness variation
#
# Purpose
# -------
# The parent action/stiffness identity audit found:
#
#   Action/stiffness is a legitimate q-origin candidate only if it writes a
#   functional and derives q before recovery checks.
#
# The best next test is a minimal coupled stiffness functional:
#
#   S ~ c_A |grad A|^2
#     + c_s |grad A_spatial|^2
#     + c_x grad A · grad A_spatial
#     + c_m A S_A
#
# This script varies that functional symbolically and audits whether the
# coefficient ratio q is derived or merely moved into stiffness coefficients.
#
# It is not a final action.

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
class CoupledVariationEntry:
    name: str
    statement: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[CoupledVariationEntry]:
    return [
        CoupledVariationEntry(
            name="CV1: minimal coupled functional",
            statement="S = ∫ [1/2 c_A |grad A|^2 + 1/2 c_s |grad B_s|^2 + c_x grad A·grad B_s + c_m A S_A] dV",
            role="concrete action/stiffness test; B_s denotes A_spatial variable",
            allowed_if="coefficients have pre-recovery origin",
            forbidden_if="coefficients are selected to pass gamma_like recovery",
            status="STRUCTURAL",
            missing="coefficient origin and boundary class",
            consequence="functional can be varied, but coefficient freedom remains visible",
        ),
        CoupledVariationEntry(
            name="CV2: variation with respect to B_s",
            statement="δS/δB_s -> -c_s ΔB_s - c_x ΔA = 0",
            role="spatial companion equation from coupled stiffness",
            allowed_if="sign conventions and boundary terms are fixed",
            forbidden_if="interpreted before coefficient origin is known",
            status="CANDIDATE",
            missing="boundary conditions and normalization",
            consequence="gives ΔB_s = -(c_x/c_s) ΔA",
        ),
        CoupledVariationEntry(
            name="CV3: using A constraint",
            statement="with ΔA = S_A, variation gives ΔB_s = q_action S_A where q_action = -(c_x/c_s)",
            role="candidate derivation of q from stiffness ratio",
            allowed_if="c_x/c_s is derived before recovery checks",
            forbidden_if="c_x/c_s is chosen to make gamma_like=1",
            status="THEOREM_TARGET",
            missing="origin of c_x/c_s",
            consequence="q is reduced to stiffness-ratio origin, not fully derived yet",
        ),
        CoupledVariationEntry(
            name="CV4: variation with respect to A",
            statement="δS/δA -> -c_A ΔA - c_x ΔB_s + c_m S_A = 0",
            role="checks consistency with pre-existing A constraint",
            allowed_if="recovers or renormalizes ΔA=S_A without tuning",
            forbidden_if="A equation is overwritten to force recovery",
            status="RISK",
            missing="compatibility with existing A-sector normalization",
            consequence="coupled action may disturb the existing A constraint unless constrained",
        ),
        CoupledVariationEntry(
            name="CV5: independent stiffness failure",
            statement="if c_x=0 then B_s has no sourced spatial companion equation",
            role="no-go for independent stiffness as q-origin",
            allowed_if="used as branch-kill result",
            forbidden_if="source coupling to B_s is added solely to repair q",
            status="BRANCH_KILLED",
            missing="none for this minimal independent case",
            consequence="independent stiffness alone cannot derive A_spatial from A",
        ),
        CoupledVariationEntry(
            name="CV6: direct B_s source coupling",
            statement="add c_b B_s S_A",
            role="alternative way to source spatial companion",
            allowed_if="source coupling follows from matter/vacuum rule",
            forbidden_if="added to fit gamma_like=1",
            status="RISK",
            missing="source-coupling principle",
            consequence="could derive q only if c_b/c_s has prior origin",
        ),
        CoupledVariationEntry(
            name="CV7: stiffness-ratio free parameter problem",
            statement="q_action = -(c_x/c_s)",
            role="core problem exposed by variation",
            allowed_if="c_x/c_s follows from ontology, symmetry, conservation, or parent identity",
            forbidden_if="ratio remains free and is fixed by recovery target",
            status="DEFER",
            missing="stiffness-ratio origin",
            consequence="action variation moves the problem to coefficient origin unless c_x/c_s is constrained",
        ),
        CoupledVariationEntry(
            name="CV8: gamma-like recovery check",
            statement="weak-field output checks whether q_action produces gamma_like=1",
            role="downstream recovery target",
            allowed_if="checked after c_x/c_s is fixed",
            forbidden_if="used to choose c_x/c_s",
            status="RECOVERY_TARGET",
            missing="weak-field map from q_action to gamma_like",
            consequence="tests but does not determine stiffness ratio",
        ),
        CoupledVariationEntry(
            name="CV9: AB exterior diagnostic check",
            statement="exterior solution checks kappa_areal -> 0 / AB -> 1",
            role="downstream exterior recovery diagnostic",
            allowed_if="checked after solving varied equations",
            forbidden_if="inserted as boundary condition or action constraint",
            status="RECOVERY_TARGET",
            missing="exterior solution and boundary class",
            consequence="keeps AB diagnostic-only",
        ),
        CoupledVariationEntry(
            name="CV10: no-overlap trace condition",
            statement="O[B_s, trace_residual] = 0 or residual killed/non-metric",
            role="prevents coupled action from double-counting zeta/kappa trace",
            allowed_if="overlap operator or residual status theorem is defined",
            forbidden_if="B_s and zeta/kappa both enter as independent trace",
            status="THEOREM_TARGET",
            missing="overlap operator / residual status",
            consequence="derived q still fails if trace accounting overlaps",
        ),
        CoupledVariationEntry(
            name="CV11: stiffness tuning failure",
            statement="choose c_x/c_s after checking gamma_like or Schwarzschild expansion",
            role="rejected shortcut",
            allowed_if="used only as no-go diagnosis",
            forbidden_if="accepted as derivation",
            status="REJECTED",
            missing="not pursued",
            consequence="kills coupled stiffness as q-origin if unavoidable",
        ),
        CoupledVariationEntry(
            name="CV12: recommended next move",
            statement="test whether c_x/c_s can be fixed by symmetry, normalization, or conservation; otherwise defer to conservation-current identity",
            role="best current branch decision",
            allowed_if="variation result is treated honestly as ratio-origin problem",
            forbidden_if="pretending q is fully derived by variation alone",
            status="RECOMMENDED",
            missing="stiffness-ratio origin inventory",
            consequence="next script should audit c_x/c_s origin or move to conservation-current origin",
        ),
    ]


def print_entry(e: CoupledVariationEntry) -> None:
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
    header("Case 0: Minimal coupled stiffness variation problem")

    print("Question:")
    print()
    print("  Does coupled stiffness derive q, or only move the tuning knob?")
    print()
    print("Goal:")
    print()
    print("  vary a concrete minimal coupled stiffness functional and expose whether q is derived")
    print()
    print("Notation:")
    print("  B_s denotes the A_spatial scalar variable in this reduced symbolic test.")
    print()
    print("Discipline:")
    print("  do not choose c_x/c_s from gamma_like")
    print("  do not insert AB=1 as boundary/action constraint")
    print("  preserve the existing A constraint")
    print("  do not double-count zeta/kappa residual trace")
    print("  admit defer outcome if stiffness ratio remains free")

    status_line("minimal coupled stiffness variation problem posed", "REQUIRED")


def case_1_inventory(entries: List[CoupledVariationEntry]):
    header("Case 1: Coupled stiffness variation inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[CoupledVariationEntry]):
    header("Case 2: Compact coupled-variation ledger")

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

    status_line("compact coupled-variation ledger produced", "STRUCTURAL")


def case_3_variation_calculation():
    header("Case 3: Minimal variation calculation")

    print("Functional:")
    print()
    print("  S = ∫ [1/2 c_A |grad A|^2 + 1/2 c_s |grad B_s|^2 + c_x grad A·grad B_s + c_m A S_A] dV")
    print()
    print("Variation with respect to B_s:")
    print()
    print("  -c_s ΔB_s - c_x ΔA = 0")
    print()
    print("Therefore:")
    print()
    print("  ΔB_s = -(c_x/c_s) ΔA")
    print()
    print("Using ΔA = S_A:")
    print()
    print("  ΔB_s = q_action S_A")
    print()
    print("where:")
    print()
    print("  q_action = -(c_x/c_s)")
    print()
    print("Interpretation:")
    print("  Variation derives q only if c_x/c_s is itself derived.")
    print("  Otherwise it moves the tuning knob from q to stiffness ratio.")

    status_line("minimal variation calculation produced", "THEOREM_TARGET")


def case_4_status_counts(entries: List[CoupledVariationEntry]):
    header("Case 4: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Coupled stiffness can produce the A_spatial equation form.")
    print("  It does not by itself derive the stiffness ratio c_x/c_s.")
    print("  Independent stiffness alone is killed as a q-origin.")
    print("  The branch must now find a ratio origin or defer to conservation/current identity.")

    status_line("coupled-variation status count produced", "STRUCTURAL")


def case_5_good_failure():
    header("Case 5: Good failure / defer outcome")

    print("Good failure:")
    print()
    print("  coupled variation yields q_action = -(c_x/c_s), but no pre-recovery principle fixes c_x/c_s.")
    print()
    print("Consequence:")
    print()
    print("  coupled stiffness does not fully derive q.")
    print("  It exposes the next bottleneck: stiffness-ratio origin.")
    print("  Search should test symmetry/normalization/conservation origin or defer to conservation-current identity.")
    print()
    print("Bad failure:")
    print("  choose c_x/c_s to make gamma_like=1 and call the action derived.")

    status_line("coupled stiffness good failure stated", "DEFER")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("Coupled stiffness variation fails if:")
    print()
    print("1. c_x/c_s is chosen from gamma_like=1")
    print("2. c_x/c_s is chosen from Schwarzschild expansion")
    print("3. AB=1 is used as action constraint or boundary condition")
    print("4. A variation destroys the existing A constraint without explanation")
    print("5. B_s source coupling is added only to repair q")
    print("6. zeta/kappa residual trace overlaps with B_s")
    print("7. variation result is claimed to derive q while c_x/c_s remains free")

    status_line("coupled stiffness failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_minimal_coupled_stiffness_variation.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_stiffness_ratio_origin_inventory.py")
    print("   Test whether c_x/c_s can come from symmetry, normalization, conservation, or ontology.")
    print()
    print("3. candidate_conservation_current_coefficient_origin.py")
    print("   Move to conservation/current identity if stiffness ratio remains free.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_stiffness_ratio_origin_inventory.py")
    print()
    print("Reason:")
    print("  Coupled variation produces q_action = -c_x/c_s. The next bottleneck is whether c_x/c_s has a pre-recovery origin.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("Coupled stiffness variation produces the right form:")
    print()
    print("  ΔB_s = q_action S_A")
    print("  q_action = -(c_x/c_s)")
    print()
    print("But it does not fully derive q unless c_x/c_s is derived.")
    print()
    print("Best next test:")
    print("  candidate_stiffness_ratio_origin_inventory.py")


def main():
    header("Candidate Minimal Coupled Stiffness Variation")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_variation_calculation()
    case_4_status_counts(entries)
    case_5_good_failure()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
