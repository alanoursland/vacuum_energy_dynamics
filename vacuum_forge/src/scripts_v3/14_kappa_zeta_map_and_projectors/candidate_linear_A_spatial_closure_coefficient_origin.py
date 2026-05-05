# Candidate linear A_spatial closure coefficient origin
#
# Purpose
# -------
# The differential A_spatial closure operator inventory found that the least
# decorated linear closure:
#
#   alpha1 Delta A_spatial + alpha2 Delta A + alpha3 S_A = 0
#
# together with:
#
#   Delta A = S_A
#
# collapses to:
#
#   Delta A_spatial = -((alpha2 + alpha3)/alpha1) S_A
#
# This is useful only if the ratio is derived, not chosen.
#
# This script audits possible origins for that coefficient ratio.
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
class CoefficientOriginEntry:
    name: str
    origin: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[CoefficientOriginEntry]:
    return [
        CoefficientOriginEntry(
            name="CO1: linear closure ratio",
            origin="q = -((alpha2 + alpha3)/alpha1)",
            role="controls Delta A_spatial = q S_A",
            allowed_if="q is derived before recovery checks",
            forbidden_if="q is selected to force gamma_like=1",
            status="STRUCTURAL",
            missing="origin of alpha ratios",
            consequence="the linear branch lives or dies on q",
        ),
        CoefficientOriginEntry(
            name="CO2: free-fit q",
            origin="choose q to match gamma_like=1",
            role="repair knob",
            allowed_if="never as derivation",
            forbidden_if="used to save the linear closure branch",
            status="REJECTED",
            missing="not pursued",
            consequence="turns differential closure into observational tuning",
        ),
        CoefficientOriginEntry(
            name="CO3: action/stiffness origin",
            origin="alpha ratios follow from variation of a stiffness/action functional",
            role="candidate legitimate coefficient origin",
            allowed_if="functional is specified before fitting recovery targets",
            forbidden_if="functional weights are chosen to reproduce gamma_like=1",
            status="CANDIDATE",
            missing="action/stiffness functional",
            consequence="may defer linear branch to parent_action_stiffness_identity",
        ),
        CoefficientOriginEntry(
            name="CO4: conservation-current origin",
            origin="alpha ratios fixed by div J_A = 0 or source-balance closure",
            role="candidate constraint/conservation origin",
            allowed_if="current J_A and balance law are explicit",
            forbidden_if="conservation language is decorative",
            status="CANDIDATE",
            missing="J_A and balance operator",
            consequence="may move branch toward conservation/Bianchi-like identity",
        ),
        CoefficientOriginEntry(
            name="CO5: source normalization origin",
            origin="alpha3 fixed by same source routing that fixes Delta A = S_A",
            role="possible internal normalization route",
            allowed_if="source routing identity fixes alpha3 relative to alpha1/alpha2",
            forbidden_if="source normalization is adjusted after checking gamma",
            status="CANDIDATE",
            missing="source routing identity",
            consequence="could keep branch local if source normalization derives q",
        ),
        CoefficientOriginEntry(
            name="CO6: elliptic operator normalization",
            origin="alpha1 fixed by normalization of L1 and boundary-admissible elliptic problem",
            role="operator normalization candidate",
            allowed_if="normalization is mathematical/variational, not recovery-tuned",
            forbidden_if="boundary data impose Schwarzschild or AB=1",
            status="SAFE_IF",
            missing="operator normalization rule and boundary class",
            consequence="helps only if alpha2/alpha3 are also derived",
        ),
        CoefficientOriginEntry(
            name="CO7: zeta participation origin",
            origin="q fixed by volume/curvature exchange relation involving zeta",
            role="ontology-native but risky coefficient origin",
            allowed_if="zeta becomes companion or residual by no-overlap identity",
            forbidden_if="zeta supplies q while remaining independent residual trace",
            status="RISK",
            missing="zeta-A_spatial no-overlap identity",
            consequence="may leave A-local branch and become volume-exchange branch",
        ),
        CoefficientOriginEntry(
            name="CO8: gamma-like recovery check",
            origin="linearized solution yields gamma_like=1",
            role="observational recovery test",
            allowed_if="checked only after q is derived",
            forbidden_if="used to choose q",
            status="RECOVERY_TARGET",
            missing="linearized recovery calculation",
            consequence="tests q; does not determine q",
        ),
        CoefficientOriginEntry(
            name="CO9: AB exterior diagnostic check",
            origin="exterior solution yields kappa_areal -> 0 / AB -> 1",
            role="reduced exterior recovery test",
            allowed_if="emerges from solved closure",
            forbidden_if="used as boundary or coefficient condition",
            status="RECOVERY_TARGET",
            missing="exterior solution with derived q",
            consequence="keeps AB diagnostic-only",
        ),
        CoefficientOriginEntry(
            name="CO10: no-overlap compatibility",
            origin="q must not force overlapping A_spatial and zeta/kappa residual trace",
            role="protects count-once theorem",
            allowed_if="overlap operator or residual-kill theorem is present",
            forbidden_if="metric trace is counted twice",
            status="THEOREM_TARGET",
            missing="overlap operator O",
            consequence="derived q still fails if trace accounting fails",
        ),
        CoefficientOriginEntry(
            name="CO11: coefficient-origin failure",
            origin="no pre-recovery principle fixes q",
            role="good failure / branch defer",
            allowed_if="used to defer to action/stiffness or conservation parent identity",
            forbidden_if="q is then chosen by hand anyway",
            status="DEFER",
            missing="coefficient principle",
            consequence="linear differential branch is not killed absolutely, but cannot stand locally",
        ),
        CoefficientOriginEntry(
            name="CO12: recommended next move",
            origin="defer q-origin to parent action/stiffness unless source/conservation origin can be made explicit",
            role="best current search move",
            allowed_if="local coefficient tuning is rejected",
            forbidden_if="pretending q is derived locally",
            status="RECOMMENDED",
            missing="parent coefficient-origin script",
            consequence="next script should test action/stiffness coefficient origin or conservation current origin",
        ),
    ]


def print_entry(e: CoefficientOriginEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Origin: {e.origin}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Linear A_spatial closure coefficient-origin problem")

    print("Question:")
    print()
    print("  Can the linear closure coefficient ratio q be derived rather than fitted?")
    print()
    print("Goal:")
    print()
    print("  determine whether the local differential closure branch has a legitimate coefficient origin")
    print()
    print("Discipline:")
    print()
    print("  do not choose q to make gamma_like=1")
    print("  do not use AB=1 as coefficient condition")
    print("  do not hide q inside source normalization")
    print("  do not let zeta fix q while remaining independent residual")
    print("  if q has no local origin, defer to parent identity")

    status_line("linear coefficient-origin problem posed", "REQUIRED")


def case_1_inventory(entries: List[CoefficientOriginEntry]):
    header("Case 1: Coefficient-origin inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[CoefficientOriginEntry]):
    header("Case 2: Compact coefficient-origin ledger")

    print("| Entry | Origin | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.origin.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact coefficient-origin ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[CoefficientOriginEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  The local linear closure cannot use gamma_like recovery to choose q.")
    print("  Legitimate q origins are action/stiffness, conservation-current, source-routing, or volume-exchange identities.")
    print("  If none is explicit, the linear closure branch must defer to a parent coefficient-origin identity.")
    print("  This is a useful narrowing result, not a failure of the whole theory.")

    status_line("coefficient-origin status count produced", "STRUCTURAL")


def case_4_linear_ratio_statement():
    header("Case 4: Linear ratio statement")

    print("Minimal linear closure:")
    print()
    print("  alpha1 Delta A_spatial + alpha2 Delta A + alpha3 S_A = 0")
    print()
    print("Using:")
    print()
    print("  Delta A = S_A")
    print()
    print("gives:")
    print()
    print("  Delta A_spatial = q S_A")
    print()
    print("where:")
    print()
    print("  q = -((alpha2 + alpha3)/alpha1)")
    print()
    print("Allowed:")
    print("  derive q from a prior identity.")
    print()
    print("Forbidden:")
    print("  choose q from gamma_like=1, AB=1, or Schwarzschild matching.")

    status_line("linear q statement produced", "REQUIRED")


def case_5_good_failure():
    header("Case 5: Good failure / defer outcome")

    print("Good failure:")
    print()
    print("  no local pre-recovery principle fixes q.")
    print()
    print("Consequence:")
    print()
    print("  the linear differential closure branch cannot stand alone.")
    print("  It must defer to:")
    print("    parent action/stiffness identity,")
    print("    conservation-current identity,")
    print("    or volume-exchange identity.")
    print()
    print("Bad failure:")
    print("  choose q by matching gamma_like=1 and call it closure.")

    status_line("linear coefficient-origin good failure stated", "DEFER")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("Coefficient-origin test fails if:")
    print()
    print("1. q is chosen to recover gamma_like=1")
    print("2. q is chosen to recover AB=1")
    print("3. q is hidden inside source normalization after recovery checks")
    print("4. q is hidden inside boundary data")
    print("5. q is attributed to action/stiffness without a functional")
    print("6. q is attributed to conservation without a current")
    print("7. zeta fixes q while also remaining independent residual")
    print("8. no-overlap theorem is ignored after q is chosen")

    status_line("coefficient-origin failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_linear_A_spatial_closure_coefficient_origin.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_parent_action_stiffness_identity.py")
    print("   Test whether an action/stiffness functional can derive q.")
    print()
    print("3. candidate_conservation_current_coefficient_origin.py")
    print("   Test whether a conserved current can derive q.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_parent_action_stiffness_identity.py")
    print()
    print("Reason:")
    print("  The local branch reduced to coefficient origin. The cleanest next source of coefficient ratios is an action/stiffness identity.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("The local linear closure branch does not derive q by itself.")
    print()
    print("q = -((alpha2 + alpha3)/alpha1)")
    print()
    print("is acceptable only if derived before recovery checks.")
    print()
    print("Best next test:")
    print("  candidate_parent_action_stiffness_identity.py")


def main():
    header("Candidate Linear A_spatial Closure Coefficient Origin")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_linear_ratio_statement()
    case_5_good_failure()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
