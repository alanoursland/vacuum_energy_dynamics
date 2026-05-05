# Candidate areal kappa diagnostic versus physical variable
#
# Purpose
# -------
# The A_spatial versus zeta trace-counting audit found:
#
#   The safest current recombination counting rule is:
#
#     scalar trace in g_ij = A_spatial_once + boundary-neutral trace_volume_residual_once
#
#   with:
#
#     no overlap,
#     no exterior scalar charge,
#     no GR spatial metric import,
#     no kappa diagnostic promotion.
#
# The next bottleneck is:
#
#   kappa = 1/2 ln(A B)
#
# This relation is powerful in reduced spherical areal gauge, but dangerous:
#
#   it may be silently promoted from reduced diagnostic to physical trace/volume scalar.
#
# This script fences the areal-kappa diagnostic before A_spatial recovery uses it.
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
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class ArealKappaEntry:
    name: str
    branch: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[ArealKappaEntry]:
    return [
        ArealKappaEntry(
            name="K1: areal kappa as reduced diagnostic only",
            branch="kappa_areal = 1/2 ln(A B)",
            role="diagnoses A/B mismatch in static spherical areal reduction",
            allowed_if="kept explicitly reduced, gauge-conditioned, and diagnostic",
            forbidden_if="treated as covariant physical scalar field",
            status="RECOMMENDED",
            missing="covariant physical kappa, if any",
            consequence="safe to use as test instrument, not as field-equation building block",
        ),
        ArealKappaEntry(
            name="K2: exterior recovery diagnostic",
            branch="kappa_areal -> 0 corresponds to A B -> 1 in recovered exterior",
            role="checks Schwarzschild-like exterior recovery",
            allowed_if="used as recovery check, not construction principle",
            forbidden_if="AB=1 is imposed as unexplained metric law",
            status="SAFE_IF",
            missing="parent derivation of exterior recovery",
            consequence="AB=1 remains target/diagnostic, not derivation",
        ),
        ArealKappaEntry(
            name="K3: areal kappa as physical trace variable",
            branch="kappa_phys := 1/2 ln(A B)",
            role="promotes reduced diagnostic to physical trace/volume scalar",
            allowed_if="a covariant map to zeta/projected trace is derived",
            forbidden_if="promotion happens by notation or convenience",
            status="RISK",
            missing="covariant map, frame/slicing rule, projector identity",
            consequence="unsafe until derived; risks GR smuggling and scalar double-counting",
        ),
        ArealKappaEntry(
            name="K4: areal kappa as proxy for zeta-zeta_min",
            branch="kappa_areal ~ zeta - zeta_min in spherical reduction",
            role="possible reduced comparison between AB mismatch and volume-form strain",
            allowed_if="treated as reduced diagnostic relation only",
            forbidden_if="used as general kappa-zeta identity",
            status="CANDIDATE",
            missing="explicit calculation of zeta in the same reduction/gauge",
            consequence="may guide kappa-zeta map but cannot define it yet",
        ),
        ArealKappaEntry(
            name="K5: residual/relaxation kappa distinct from areal diagnostic",
            branch="kappa_residual != kappa_areal unless mapped",
            role="keeps physical/residual kappa separate from reduced AB diagnostic",
            allowed_if="residual kappa remains first-order, projected, boundary-neutral",
            forbidden_if="residual kappa inherits AB diagnostic status automatically",
            status="CANDIDATE",
            missing="residual map P_relax P_trace(zeta-zeta_min)",
            consequence="allows e_kappa to remain provisional if residual variable survives",
        ),
        ArealKappaEntry(
            name="K6: silent covariant promotion",
            branch="use kappa=1/2 ln(AB) as general scalar in parent equation",
            role="none",
            allowed_if="never in current branch",
            forbidden_if="used to define parent kappa without derivation",
            status="FORBIDDEN",
            missing="not pursued",
            consequence="would smuggle reduced spherical metric structure into the parent theory",
        ),
        ArealKappaEntry(
            name="K7: e_kappa if kappa is diagnostic only",
            branch="e_kappa = 1/2 K_kappa(kappa-kappa_min)^2 with diagnostic kappa",
            role="potentially invalid physical energy for a diagnostic variable",
            allowed_if="e_kappa is reinterpreted as diagnostic cost or residual variable is separately defined",
            forbidden_if="physical energy is assigned to pure gauge/reduced diagnostic",
            status="UNRESOLVED",
            missing="decision whether physical residual kappa survives",
            consequence="e_kappa may need retirement, reinterpretation, or residual-variable relabeling",
        ),
        ArealKappaEntry(
            name="K8: recombination use of areal kappa",
            branch="kappa_areal used in recombination diagnostics",
            role="checks whether reduced A/B recombination is consistent",
            allowed_if="diagnostic only and not inserted as independent trace",
            forbidden_if="g_ij receives an independent kappa_areal trace contribution",
            status="CONSTRAINED",
            missing="P_recombination relation to reduced areal variables",
            consequence="areal kappa can test recombination but not define physical trace insertion",
        ),
        ArealKappaEntry(
            name="K9: A_spatial recovery dependency",
            branch="A_spatial recovery uses kappa_areal to diagnose AB mismatch",
            role="helps test exterior/interior A-B consistency",
            allowed_if="used after explicit diagnostic labeling",
            forbidden_if="A_spatial theorem assumes kappa_areal is physical",
            status="SAFE_IF",
            missing="A_spatial recovery theorem",
            consequence="fencing areal kappa now makes A_spatial recovery safer next",
        ),
        ArealKappaEntry(
            name="K10: count-once theorem preservation",
            branch="Trace[g_ij scalar] = Trace_A_mass + Trace_residual_neutral with no overlap",
            role="global recombination constraint that areal kappa must not violate",
            allowed_if="areal kappa remains diagnostic or maps to only one trace channel",
            forbidden_if="areal kappa adds third scalar trace",
            status="REQUIRED",
            missing="parent recombination identity",
            consequence="preserves previous trace-counting theorem target",
        ),
        ArealKappaEntry(
            name="K11: diagnostic failure outcome",
            branch="no clean map from kappa_areal to zeta without gauge/slicing assumptions",
            role="good failure mode",
            allowed_if="failure is used to keep areal kappa diagnostic-only",
            forbidden_if="map failure is ignored and kappa is promoted anyway",
            status="SAFE_IF",
            missing="explicit zeta comparison test",
            consequence="forces physical kappa, if any, to be separately defined",
        ),
        ArealKappaEntry(
            name="K12: recommended convention",
            branch="areal kappa is reduced diagnostic; physical/residual kappa remains unresolved",
            role="best current convention for avoiding GR smuggling",
            allowed_if="declared provisional and revisited after A_spatial recovery",
            forbidden_if="hardened into parent field variable without derivation",
            status="RECOMMENDED",
            missing="future physical kappa decision",
            consequence="use kappa_areal as test instrument, not building block",
        ),
    ]


def print_entry(e: ArealKappaEntry) -> None:
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
    header("Case 0: Areal kappa diagnostic versus physical variable problem")

    print("Question:")
    print()
    print("  How do we keep kappa = 1/2 ln(A B) useful without letting it become a smuggled physical scalar?")
    print()
    print("Goal:")
    print()
    print("  separate reduced areal diagnostic kappa from any physical/residual kappa")
    print()
    print("Discipline:")
    print()
    print("  use areal kappa as test instrument, not building block")
    print("  do not import GR spatial structure through AB=1")
    print("  do not assign physical e_kappa to a pure diagnostic")
    print("  do not insert areal kappa as independent spatial trace")
    print("  preserve count-once recombination theorem target")

    status_line("areal kappa diagnostic problem posed", "REQUIRED")


def case_1_inventory(entries: List[ArealKappaEntry]):
    header("Case 1: Areal kappa branch inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[ArealKappaEntry]):
    header("Case 2: Compact areal-kappa ledger")

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

    status_line("compact areal-kappa ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[ArealKappaEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Areal kappa is valuable as a reduced diagnostic.")
    print("  Silent promotion to a physical/covariant scalar is forbidden.")
    print("  Physical or residual kappa remains unresolved and must be separately defined.")
    print("  e_kappa remains provisional until residual kappa survives as more than a diagnostic.")

    status_line("areal-kappa status count produced", "STRUCTURAL")


def case_4_recommended_convention():
    header("Case 4: Recommended convention")

    print("Recommended for now:")
    print()
    print("  kappa_areal = 1/2 ln(A B)")
    print()
    print("is:")
    print()
    print("  a reduced spherical areal-gauge diagnostic")
    print("  an exterior recovery check")
    print("  a test instrument for A/B mismatch")
    print()
    print("It is not:")
    print()
    print("  a covariant physical scalar")
    print("  an independent spatial trace insertion")
    print("  a sufficient basis for physical e_kappa")
    print("  a parent field-equation building block")
    print()
    print("Physical/residual kappa remains unresolved.")

    status_line("recommended areal-kappa convention stated", "RECOMMENDED")


def case_5_recovery_not_construction():
    header("Case 5: AB=1 recovery, not construction")

    print("Safe phrasing:")
    print()
    print("  In the recovered static spherical exterior, kappa_areal -> 0 corresponds to A B -> 1.")
    print("  This is a diagnostic of exterior recovery.")
    print("  It is not a derivation of the parent metric structure.")
    print()
    print("Unsafe phrasing:")
    print()
    print("  Set kappa = 0, therefore A B = 1, therefore the exterior metric is fixed.")
    print()
    print("Rule:")
    print()
    print("  AB=1 is a recovery target/check, not a construction principle.")

    status_line("AB=1 recovery language stated", "CONSTRAINED")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("The areal-kappa branch fails if:")
    print()
    print("1. kappa = 1/2 ln(A B) is used as a covariant scalar without derivation")
    print("2. AB=1 is used as construction rather than recovery check")
    print("3. e_kappa is physical energy of a pure diagnostic variable")
    print("4. areal kappa is inserted as independent g_ij trace")
    print("5. areal kappa and zeta/kappa residual both count the same trace")
    print("6. failure to map areal kappa to zeta is ignored")
    print("7. A_spatial recovery assumes physical kappa before kappa is fenced")

    status_line("areal-kappa failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_areal_kappa_diagnostic_vs_physical_variable.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_A_spatial_recovery_constraint.py")
    print("   Identify what A_spatial is required to recover without importing GR.")
    print()
    print("3. candidate_kappa_diagnostic_or_residual_after_A_spatial.py")
    print("   Decide whether kappa remains diagnostic or residual after A_spatial is constrained.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_A_spatial_recovery_constraint.py")
    print()
    print("Reason:")
    print("  Areal kappa is now fenced as diagnostic. Next identify A_spatial recovery requirements without using kappa as hidden physical scalar.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("Areal kappa is useful but dangerous:")
    print()
    print("  kappa_areal = 1/2 ln(A B)")
    print()
    print("Use it as:")
    print("  reduced diagnostic")
    print("  exterior recovery check")
    print("  A/B mismatch test instrument")
    print()
    print("Do not use it as:")
    print("  covariant physical scalar")
    print("  independent trace insertion")
    print("  physical e_kappa basis")
    print("  parent field-equation building block")
    print()
    print("Possible next artifact:")
    print("  candidate_areal_kappa_diagnostic_vs_physical_variable.md")
    print()
    print("Possible next script:")
    print("  candidate_A_spatial_recovery_constraint.py")


def main():
    header("Candidate Areal Kappa Diagnostic Versus Physical Variable")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_recommended_convention()
    case_5_recovery_not_construction()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
