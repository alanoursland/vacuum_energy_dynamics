# Candidate A_spatial versus zeta trace counting
#
# Purpose
# -------
# The recombination projector audit found:
#
#   P_recombination is the count-once gate:
#
#     g_tt <- A
#     g_0i <- W_i
#     g_ij <- A_spatial_once + trace_volume_residual_once + h_TT
#
# The major unresolved issue is:
#
#   What spatial trace belongs to A,
#   and what remains for zeta/kappa?
#
# This script tests the counting branches for A_spatial versus zeta/kappa
# trace-volume response.
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
class TraceCountingEntry:
    name: str
    branch: str
    interpretation: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[TraceCountingEntry]:
    return [
        TraceCountingEntry(
            name="C1: A_spatial consumes all scalar spatial trace",
            branch="g_ij scalar trace is fully fixed by A-sector recovery",
            interpretation="zeta/kappa cannot add independent scalar spatial trace",
            allowed_if="A-sector parent identity derives both lapse and spatial scalar trace",
            forbidden_if="zeta/kappa also add volume trace as independent geometry",
            status="SAFE_IF",
            missing="A-sector spatial recovery theorem",
            consequence="kappa likely diagnostic/residual only; zeta volume energy cannot be inserted as independent metric trace",
        ),
        TraceCountingEntry(
            name="C2: A_spatial consumes only mass-sector trace",
            branch="A_spatial accounts for exterior mass geometry, leaving compensated residual trace/volume freedom",
            interpretation="zeta/kappa may survive as boundary-neutral residual",
            allowed_if="residual has zero exterior charge and does not alter M_ext",
            forbidden_if="residual changes exterior mass or creates scalar tail",
            status="CANDIDATE",
            missing="projector separating mass-sector trace from residual trace",
            consequence="P_boundary P_trace residual can enter recombination once",
        ),
        TraceCountingEntry(
            name="C3: A_spatial and zeta are the same trace variable",
            branch="zeta is the volume expression of the A-sector spatial response",
            interpretation="epsilon_vac_config may describe A-sector spatial volume configuration, not extra trace",
            allowed_if="energy accounting is rewritten so zeta does not add independent geometry",
            forbidden_if="A_spatial and zeta both inserted separately",
            status="RISK",
            missing="identity connecting A_spatial trace to zeta",
            consequence="zeta may become diagnostic/energy bookkeeping for A_spatial, kappa residual remains separate or diagnostic",
        ),
        TraceCountingEntry(
            name="C4: kappa is only residual after A_spatial and zeta",
            branch="A_spatial and zeta define volume geometry; kappa tracks mismatch/relaxation only",
            interpretation="kappa does not enter g_ij as independent trace",
            allowed_if="kappa energy is residual and recombination excludes duplicate kappa trace",
            forbidden_if="kappa adds separate spatial trace",
            status="CANDIDATE",
            missing="kappa-zeta residual map",
            consequence="supports kappa diagnostic/first-order residual role",
        ),
        TraceCountingEntry(
            name="C5: zeta/kappa boundary residual only",
            branch="zeta/kappa enter only through compact or boundary-neutral residual correction",
            interpretation="ordinary exterior metric is A-sector; volume residual is interior/boundary-neutral",
            allowed_if="P_boundary enforces zero charge/flux and delta M_ext=0",
            forbidden_if="boundary residual leaks into exterior scalar charge",
            status="CANDIDATE",
            missing="boundary mass preservation theorem",
            consequence="preserves group-13 volume accounting while minimizing GR-smuggling risk",
        ),
        TraceCountingEntry(
            name="C6: no independent A_spatial derivation",
            branch="A_spatial is currently recovery bookkeeping, not derived",
            interpretation="do not assume GR spatial metric form",
            allowed_if="A_spatial labeled recovery constraint / theorem target",
            forbidden_if="GR spatial response is imported as field equation",
            status="UNRESOLVED",
            missing="parent identity deriving A_spatial companion",
            consequence="recombination remains bookkeeping until A_spatial is derived",
        ),
        TraceCountingEntry(
            name="C7: duplicate scalar spatial trace",
            branch="g_ij includes A_spatial + zeta + kappa as independent trace terms",
            interpretation="triple-counts scalar volume response",
            allowed_if="never in ordinary branch",
            forbidden_if="used as recombination map",
            status="FORBIDDEN",
            missing="not pursued",
            consequence="kills the branch unless projection removes two of the three contributions",
        ),
        TraceCountingEntry(
            name="C8: exterior scalar tail from residual",
            branch="trace_volume_residual_once produces zeta_ext or kappa_ext ~ 1/r",
            interpretation="residual becomes scalar gravity",
            allowed_if="never in ordinary exterior",
            forbidden_if="residual has nonzero exterior charge",
            status="FORBIDDEN",
            missing="not pursued",
            consequence="requires P_boundary or branch rejection",
        ),
        TraceCountingEntry(
            name="C9: energy accounting mismatch",
            branch="metric count-once but epsilon/e_kappa count twice, or metric double-counts while energy counts once",
            interpretation="geometry and accounting disagree",
            allowed_if="energy convention and metric recombination are matched",
            forbidden_if="epsilon_zeta and e_kappa describe same metric trace independently",
            status="REQUIRED",
            missing="degree-of-freedom accounting rule",
            consequence="forces either kappa diagnostic status or absorbed/unified energy convention",
        ),
        TraceCountingEntry(
            name="C10: areal diagnostic caution",
            branch="kappa = 1/2 ln(AB) used as reduced diagnostic only",
            interpretation="spherical relation can diagnose A/B mismatch but cannot be silently promoted",
            allowed_if="kept as reduced gauge diagnostic until covariant map is derived",
            forbidden_if="AB diagnostic is treated as physical kappa trace in general recombination",
            status="CONSTRAINED",
            missing="areal diagnostic versus physical variable split",
            consequence="suggests a later diagnostic-vs-physical kappa script remains useful",
        ),
        TraceCountingEntry(
            name="C11: best provisional counting convention",
            branch="A_spatial_once + boundary-neutral trace_volume_residual_once",
            interpretation="A owns mass-sector spatial response; zeta/kappa may only supply a compensated residual once",
            allowed_if="declared provisional and tested against exterior neutrality / energy accounting",
            forbidden_if="treated as derived covariant metric law",
            status="RECOMMENDED",
            missing="A_spatial derivation and residual projector",
            consequence="use as working recombination convention until A_spatial theorem is derived",
        ),
        TraceCountingEntry(
            name="C12: theorem target",
            branch="Trace[g_ij scalar] = Trace_A_mass + Trace_residual_neutral, with no overlap",
            interpretation="desired count-once theorem for scalar spatial trace",
            allowed_if="parent identity yields orthogonal/projected scalar trace pieces",
            forbidden_if="overlap remains nonzero",
            status="THEOREM_TARGET",
            missing="parent recombination identity",
            consequence="defines the central future recombination theorem",
        ),
    ]


def print_entry(e: TraceCountingEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Branch: {e.branch}")
    print(f"Interpretation: {e.interpretation}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: A_spatial versus zeta trace counting problem")

    print("Question:")
    print()
    print("  What spatial trace is already consumed by A, and what remains for zeta/kappa?")
    print()
    print("Goal:")
    print()
    print("  classify counting branches without assuming GR spatial recombination")
    print()
    print("Discipline:")
    print()
    print("  do not import GR spatial metric as derivation")
    print("  do not triple-count scalar trace")
    print("  do not let zeta/kappa become exterior scalar gravity")
    print("  do not let kappa be both diagnostic and physical trace")
    print("  metric recombination must match epsilon/e_kappa accounting")

    status_line("A_spatial versus zeta trace counting problem posed", "REQUIRED")


def case_1_inventory(entries: List[TraceCountingEntry]):
    header("Case 1: Trace-counting branch inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[TraceCountingEntry]):
    header("Case 2: Compact trace-counting ledger")

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

    status_line("compact trace-counting ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[TraceCountingEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  The recombination search now turns on A_spatial.")
    print("  If A_spatial consumes all scalar spatial trace, zeta/kappa must become diagnostic or residual only.")
    print("  If A_spatial consumes only mass-sector trace, a boundary-neutral zeta/kappa residual may survive.")
    print("  Triple scalar trace insertion is forbidden.")

    status_line("trace-counting status count produced", "STRUCTURAL")


def case_4_provisional_counting_rule():
    header("Case 4: Provisional count-once rule")

    print("Recommended provisional rule:")
    print()
    print("  g_ij scalar trace = A_spatial_once + trace_volume_residual_once")
    print()
    print("where:")
    print()
    print("  A_spatial_once = mass-sector spatial trace required by A-sector recovery")
    print()
    print("  trace_volume_residual_once = boundary-neutral zeta/kappa residual, if any")
    print()
    print("and:")
    print()
    print("  overlap(A_spatial_once, trace_volume_residual_once) = 0")
    print()
    print("This is a theorem target, not a derived recombination law.")

    status_line("provisional count-once rule stated", "RECOMMENDED")


def case_5_failure_controls():
    header("Case 5: Failure controls")

    print("Trace counting fails if:")
    print()
    print("1. A_spatial, zeta, and kappa are all inserted as independent scalar traces")
    print("2. zeta/kappa residual has exterior 1/r charge")
    print("3. A_spatial is copied from GR and called derived")
    print("4. kappa = 1/2 ln(AB) is promoted from diagnostic without proof")
    print("5. metric recombination and epsilon/e_kappa accounting disagree")
    print("6. boundary-neutral residual changes M_ext")
    print("7. overlap between A_spatial and residual trace remains nonzero")

    status_line("trace-counting failure controls stated", "RISK")


def case_6_next_tests():
    header("Case 6: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_A_spatial_vs_zeta_trace_counting.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_areal_kappa_diagnostic_vs_physical_variable.py")
    print("   Separate kappa=1/2 ln(AB) diagnostic from physical kappa/zeta response.")
    print()
    print("3. candidate_A_spatial_recovery_constraint.py")
    print("   Identify what A_spatial is required to recover without importing GR.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_areal_kappa_diagnostic_vs_physical_variable.py")
    print()
    print("Reason:")
    print("  The current counting problem depends on not silently promoting kappa=1/2 ln(AB) from reduced diagnostic to physical scalar.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("The safest current recombination counting rule is:")
    print()
    print("  scalar trace in g_ij = A_spatial_once + boundary-neutral trace_volume_residual_once")
    print()
    print("with:")
    print()
    print("  no overlap")
    print("  no exterior scalar charge")
    print("  no GR spatial metric import")
    print("  no kappa diagnostic promotion")
    print()
    print("Possible next artifact:")
    print("  candidate_A_spatial_vs_zeta_trace_counting.md")
    print()
    print("Possible next script:")
    print("  candidate_areal_kappa_diagnostic_vs_physical_variable.py")


def main():
    header("Candidate A_spatial Versus Zeta Trace Counting")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_provisional_counting_rule()
    case_5_failure_controls()
    case_6_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
