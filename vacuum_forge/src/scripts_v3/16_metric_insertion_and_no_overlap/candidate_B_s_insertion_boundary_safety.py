# Candidate B_s insertion boundary safety
#
# Group:
#   16_metric_insertion_and_no_overlap
#
# Purpose
# -------
# The minimal no-overlap operator audit found:
#
#   O remains unresolved.
#   Residual-kill / insertion exclusivity is the safest convention, not derived O.
#   Non-metric bookkeeping is a useful fence, not O.
#
# Therefore the next gate is boundary safety under the safe convention:
#
#   J_V-driven zeta may enter ordinary metric scalar trace only through B_s,
#   with residual zeta/kappa metric trace killed or non-metric.
#
# Locked-door question:
#
#   Does B_s insertion under residual-kill / non-metric convention create
#   exterior scalar leakage, mass shift, or shell-source behavior?
#
# This script is a boundary-safety sieve, not a derivation.

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
class BoundarySafetyEntry:
    name: str
    rule: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[BoundarySafetyEntry]:
    return [
        BoundarySafetyEntry(
            name="BS1: B_s insertion boundary-safety target",
            rule="B_s insertion under residual-kill creates no exterior scalar leakage, no M_ext shift, no shell source",
            role="core boundary safety theorem target",
            allowed_if="boundary neutrality is structural, not tuned",
            forbidden_if="leakage is canceled by repair current or boundary term",
            status="THEOREM_TARGET",
            missing="boundary safety theorem",
            consequence="decides whether B_s insertion can survive ordinary exterior sector",
        ),
        BoundarySafetyEntry(
            name="BS2: zero exterior zeta/kappa charge",
            rule="Q_ext[zeta,kappa] = 0 outside ordinary static source",
            role="scalar-charge guard",
            allowed_if="zero charge follows from support/projection/residual-kill structure",
            forbidden_if="charge is canceled by R_V or boundary tuning",
            status="REQUIRED",
            missing="zero-charge theorem",
            consequence="prevents scalar exterior gravity",
        ),
        BoundarySafetyEntry(
            name="BS3: no far-zone scalar flux",
            rule="F_scalar_far[zeta,kappa,J_V] = 0",
            role="radiation/exterior guard",
            allowed_if="far-zone scalar flux is structurally absent",
            forbidden_if="B_s insertion creates scalar tail or breathing leakage",
            status="REQUIRED",
            missing="far-zone flux theorem",
            consequence="protects ordinary TT-only radiation target",
        ),
        BoundarySafetyEntry(
            name="BS4: no M_ext shift",
            rule="delta M_ext|B_s/zeta/residual = 0 independent of A-sector mass",
            role="A-sector mass protection",
            allowed_if="metric insertion recombines without changing measured exterior mass",
            forbidden_if="zeta/residual bookkeeping changes M_ext",
            status="REQUIRED",
            missing="mass-accounting theorem",
            consequence="protects strongest reduced A result",
        ),
        BoundarySafetyEntry(
            name="BS5: no boundary shell source",
            rule="B_s/F_zeta support or transition creates no shell-like scalar source",
            role="boundary regularity guard",
            allowed_if="support/matching is smooth or shell term structurally vanishes",
            forbidden_if="sharp support creates unaccounted surface scalar charge",
            status="REQUIRED",
            missing="shell-avoidance theorem",
            consequence="blocks boundary source smuggling",
        ),
        BoundarySafetyEntry(
            name="BS6: compact-support insertion",
            rule="B_s/F_zeta active only inside compact source/interior with zero boundary flux",
            role="candidate safe-support branch",
            allowed_if="compact support follows from insertion law, not after-the-fact repair",
            forbidden_if="support is imposed to hide exterior scalar charge",
            status="CANDIDATE",
            missing="support law and smooth matching",
            consequence="may protect exterior if not decorative",
        ),
        BoundarySafetyEntry(
            name="BS7: smooth transition insertion",
            rule="B_s/F_zeta transitions smoothly to exterior recovery region without shell source",
            role="candidate matching branch",
            allowed_if="transition follows from field/insertion law and preserves zero charge",
            forbidden_if="smoothing function is tuned to pass recovery",
            status="CANDIDATE",
            missing="transition law",
            consequence="possible boundary-safe insertion if coefficient-free",
        ),
        BoundarySafetyEntry(
            name="BS8: zero-flux boundary condition",
            rule="n_i J_V^i = 0 or relevant volume flux vanishes structurally at boundary",
            role="current-boundary safety condition",
            allowed_if="zero flux follows from physical current/support law",
            forbidden_if="zero flux is imposed as repair boundary condition",
            status="CANDIDATE",
            missing="physical J_V/support law",
            consequence="can protect exterior only if J_V becomes real",
        ),
        BoundarySafetyEntry(
            name="BS9: diagnostic elliptic boundary audit",
            rule="solve boundary diagnostic to test leakage, not define physical boundary law",
            role="diagnostic tool",
            allowed_if="kept explicitly diagnostic",
            forbidden_if="elliptic completion becomes physical insertion mechanism",
            status="SAFE_IF",
            missing="physical boundary mechanism",
            consequence="can reveal leakage without becoming ontology",
        ),
        BoundarySafetyEntry(
            name="BS10: boundary repair rejection",
            rule="choose boundary counterterm, R_V, or J_V to cancel leakage after the fact",
            role="rejected repair branch",
            allowed_if="never as mechanism",
            forbidden_if="accepted as boundary neutrality",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents tuned exterior safety",
        ),
        BoundarySafetyEntry(
            name="BS11: exterior areal-kappa diagnostic",
            rule="AB recovery / kappa_areal used only as exterior diagnostic check",
            role="allowed recovery diagnostic",
            allowed_if="diagnostic does not choose insertion or boundary law",
            forbidden_if="areal kappa becomes physical scalar or boundary mechanism",
            status="SAFE_IF",
            missing="not a mechanism",
            consequence="keeps AB check downstream and diagnostic",
        ),
        BoundarySafetyEntry(
            name="BS12: zeta-gradient exterior-tail risk",
            rule="unrestricted grad zeta insertion creates exterior scalar tail",
            role="failure mode",
            allowed_if="only as diagnostic risk",
            forbidden_if="accepted without zero-charge theorem",
            status="RISK",
            missing="zeta support/boundary theorem",
            consequence="can kill unrestricted zeta-gradient insertion",
        ),
        BoundarySafetyEntry(
            name="BS13: source-gradient shell risk",
            rule="source/support-gradient insertion creates shell-like boundary scalar source",
            role="failure mode",
            allowed_if="only as diagnostic risk",
            forbidden_if="accepted without shell-avoidance",
            status="RISK",
            missing="boundary smoothing/source law",
            consequence="can kill source-gradient insertion branch",
        ),
        BoundarySafetyEntry(
            name="BS14: residual-kill boundary consequence",
            rule="killed/non-metric residual produces no exterior charge, no flux, no mass shift",
            role="required consequence of safe convention",
            allowed_if="residual-kill removes exterior metric/source effects",
            forbidden_if="non-metric residual leaks through boundary/accounting",
            status="REQUIRED",
            missing="residual-kill boundary theorem",
            consequence="tests whether residual-kill is safe enough as convention",
        ),
        BoundarySafetyEntry(
            name="BS15: recovery downstream",
            rule="gamma_like and AB checked only after boundary safety is structural",
            role="anti-smuggling guard",
            allowed_if="recovery remains check only",
            forbidden_if="recovery chooses support/smoothing/boundary law",
            status="RECOVERY_TARGET",
            missing="solutions after boundary-safe insertion",
            consequence="keeps recovery from constructing boundary behavior",
        ),
        BoundarySafetyEntry(
            name="BS16: boundary failure",
            rule="B_s insertion creates exterior scalar charge, far flux, M_ext shift, or shell source",
            role="branch-kill condition",
            allowed_if="used to reject unsafe insertion family",
            forbidden_if="patched with boundary repair",
            status="BRANCH_KILLED",
            missing="applies if failure demonstrated",
            consequence="unsafe insertion cannot enter ordinary metric sector",
        ),
        BoundarySafetyEntry(
            name="BS17: recommended next move",
            rule="if boundary safety survives as theorem target, audit recovery without construction",
            role="next local bottleneck",
            allowed_if="boundary safety is not failed but not derived",
            forbidden_if="jumping to parent equation before recovery anti-smuggling audit",
            status="RECOMMENDED",
            missing="recovery audit",
            consequence="next script should be candidate_B_s_insertion_recovery_audit.py",
        ),
    ]


def print_entry(e: BoundarySafetyEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Rule: {e.rule}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: B_s insertion boundary-safety problem")

    print("Question:")
    print()
    print("  Does B_s insertion under residual-kill / non-metric convention create")
    print("  exterior scalar leakage, mass shift, or shell-source behavior?")
    print()
    print("Goal:")
    print()
    print("  test whether the safe insertion convention survives ordinary exterior boundaries")
    print()
    print("Discipline:")
    print()
    print("  no exterior zeta/kappa charge")
    print("  no far-zone scalar flux")
    print("  no M_ext shift")
    print("  no shell source")
    print("  no boundary repair")
    print("  diagnostic elliptic audit only")
    print("  recovery downstream")

    status_line("B_s insertion boundary-safety problem posed", "REQUIRED")


def case_1_inventory(entries: List[BoundarySafetyEntry]):
    header("Case 1: B_s insertion boundary-safety inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[BoundarySafetyEntry]):
    header("Case 2: Compact B_s boundary-safety ledger")

    print("| Entry | Rule | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.rule.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact boundary-safety ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[BoundarySafetyEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Boundary safety is required but not derived.")
    print("  Compact support, smooth transition, and zero-flux boundary are candidate safety routes.")
    print("  Diagnostic elliptic audit is useful but not ontology.")
    print("  Boundary repair is rejected.")
    print("  Zeta-gradient exterior tails and source-gradient shell sources remain major risks.")
    print("  If boundary safety survives, recovery must be audited without construction.")

    status_line("B_s insertion boundary-safety status count produced", "STRUCTURAL")


def case_4_boundary_safety_routes():
    header("Case 4: Boundary-safety routes")

    print("Possible safe routes:")
    print()
    print("1. compact-support insertion")
    print("2. smooth transition insertion")
    print("3. structural zero-flux boundary")
    print("4. residual-kill with proven no exterior consequence")
    print("5. diagnostic elliptic leakage audit")
    print()
    print("Danger routes:")
    print()
    print("1. zeta-gradient exterior tail")
    print("2. source-gradient shell source")
    print("3. boundary counterterm")
    print("4. R_V cancellation")
    print("5. recovery-tuned smoothing")

    status_line("boundary-safety routes listed", "RECOMMENDED")


def case_5_decision_tree():
    header("Case 5: Boundary-safety decision tree")

    print("Decision tree:")
    print()
    print("1. Zero exterior charge / flux / mass shift:")
    print("   mandatory.")
    print()
    print("2. Compact support:")
    print("   candidate only if support is derived.")
    print()
    print("3. Smooth transition:")
    print("   candidate only if not recovery-tuned.")
    print()
    print("4. Zero-flux boundary:")
    print("   candidate only if physical J_V/support law exists.")
    print()
    print("5. Diagnostic elliptic audit:")
    print("   useful for detection, not physical law.")
    print()
    print("6. Boundary repair:")
    print("   rejected.")
    print()
    print("7. If scalar leakage or shell source appears:")
    print("   insertion branch killed for ordinary sector.")

    status_line("boundary-safety decision tree stated", "RECOMMENDED")


def case_6_good_failure():
    header("Case 6: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  B_s insertion under residual-kill creates exterior scalar charge,")
    print("  far-zone scalar flux, M_ext shift, or shell source.")
    print()
    print("Consequence:")
    print()
    print("  That insertion family cannot support ordinary metric sector.")
    print("  Do not patch with boundary repair or recovery-tuned smoothing.")
    print()
    print("Bad failure:")
    print()
    print("  Hide leakage in boundary counterterms or call elliptic completion a mechanism.")

    status_line("B_s insertion boundary-safety good failure stated", "DEFER")


def case_7_failure_controls():
    header("Case 7: Failure controls")

    print("B_s insertion boundary safety fails if:")
    print()
    print("1. exterior zeta/kappa charge appears")
    print("2. far-zone scalar flux appears")
    print("3. M_ext shifts independently of A")
    print("4. boundary shell source appears")
    print("5. compact support is imposed after the fact")
    print("6. smoothing is recovery-tuned")
    print("7. R_V cancels leakage")
    print("8. boundary counterterm cancels leakage")
    print("9. diagnostic elliptic audit becomes ontology")
    print("10. AB/gamma_like chooses boundary behavior")

    status_line("B_s insertion boundary-safety failure controls stated", "RISK")


def case_8_next_tests():
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_B_s_insertion_boundary_safety.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_B_s_insertion_recovery_audit.py")
    print("   Audit gamma_like / AB recovery as tests, not construction.")
    print()
    print("3. candidate_metric_insertion_early_failure_summary.py")
    print("   Use if boundary leakage kills insertion.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_B_s_insertion_recovery_audit.py")
    print()
    print("Reason:")
    print("  If boundary safety is not killed, the next danger is recovery smuggling:")
    print("  gamma_like, AB, Schwarzschild spatial metric, or areal kappa as construction.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("Boundary safety is required and not derived.")
    print()
    print("B_s insertion under residual-kill convention remains alive only if:")
    print()
    print("  no exterior zeta/kappa charge")
    print("  no far-zone scalar flux")
    print("  no M_ext shift")
    print("  no shell source")
    print("  no boundary repair")
    print()
    print("Best next script:")
    print()
    print("  candidate_B_s_insertion_recovery_audit.py")

    status_line("B_s insertion boundary-safety audit complete", "CLOSED")


def main():
    header("Candidate B_s Insertion Boundary Safety")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts()
    case_4_boundary_safety_routes()
    case_5_decision_tree()
    case_6_good_failure()
    case_7_failure_controls()
    case_8_next_tests()
    final_interpretation()


# Fix accidental no-argument case_3 call in main by wrapping after definition.
def case_3_status_counts_wrapper():
    entries = build_entries()
    case_3_status_counts(entries)


if __name__ == "__main__":
    # Use explicit run sequence to avoid accidental stale calls.
    header("Candidate B_s Insertion Boundary Safety")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_boundary_safety_routes()
    case_5_decision_tree()
    case_6_good_failure()
    case_7_failure_controls()
    case_8_next_tests()
    final_interpretation()
