# Candidate trace projector definition
#
# Purpose
# -------
# The projected kappa-zeta map audit found:
#
#   kappa = P_trace(zeta - zeta_min)
#
# is plausible only if P_trace does much more than raw trace extraction.
#
# It must:
#
#   extract trace/volume mismatch,
#   remove or compensate exterior monopole,
#   exclude A-sector mass charge,
#   annihilate TT modes,
#   cooperate with P_boundary,
#   avoid becoming a wave operator,
#   support first-order relaxation if P_relax is included,
#   leave recombination with only one trace/volume contribution.
#
# This script defines the required roles of P_trace.
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
class TraceProjectorEntry:
    name: str
    requirement: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str


def build_entries() -> List[TraceProjectorEntry]:
    return [
        TraceProjectorEntry(
            name="T1: linear metric trace extraction",
            requirement="P_trace h_ij = (1/3) gamma_ij gamma^ab h_ab",
            role="extracts spatial trace / volume perturbation at linear reduced level",
            allowed_if="used as local linear diagnostic only",
            forbidden_if="mistaken for full covariant source projector",
            status="STRUCTURAL",
            missing="nonlinear/covariant extension",
        ),
        TraceProjectorEntry(
            name="T2: zeta variation relation",
            requirement="delta zeta = 1/2 gamma^ij delta gamma_ij",
            role="ties trace projection to volume-form variation",
            allowed_if="frame/foliation is specified",
            forbidden_if="treated as gauge-invariant without u^mu or slicing",
            status="STRUCTURAL",
            missing="frame or covariant volume variable",
        ),
        TraceProjectorEntry(
            name="T3: TT annihilation",
            requirement="P_trace h_TT = 0 and P_TT P_trace = 0",
            role="prevents trace/volume sector from contaminating TT radiation",
            allowed_if="orthogonality holds at least in reduced/linear sector",
            forbidden_if="trace source leaks into h_TT or TT changes zeta",
            status="REQUIRED",
            missing="nonlinear/covariant projector proof",
        ),
        TraceProjectorEntry(
            name="T4: A-sector mass exclusion",
            requirement="P_trace excludes A_flux / rho exterior mass charge",
            role="prevents zeta/kappa from duplicating scalar mass response",
            allowed_if="rho routes to A-sector and trace/volume routes only to residual/equilibrium response",
            forbidden_if="rho becomes A mass plus kappa/zeta exterior charge",
            status="REQUIRED",
            missing="scalar constraint propagation and source routing identity",
        ),
        TraceProjectorEntry(
            name="T5: compensation / zero monopole",
            requirement="integral P_trace S_volume d^3x = 0 or Q_kappa=Q_volume=0",
            role="prevents exterior scalar monopole",
            allowed_if="compensation follows from parent projector, boundary law, or constraint",
            forbidden_if="projection requires hand-tuned subtraction per source",
            status="REQUIRED",
            missing="parent origin of compensation",
        ),
        TraceProjectorEntry(
            name="T6: boundary cooperation",
            requirement="P_boundary P_trace enforces F_zeta(R+)=F_kappa(R+)=0",
            role="prevents boundary leakage into exterior scalar tail",
            allowed_if="P_trace and P_boundary are explicitly separated or jointly defined",
            forbidden_if="P_trace alone hides boundary conditions",
            status="REQUIRED",
            missing="P_boundary definition",
        ),
        TraceProjectorEntry(
            name="T7: no wave operator",
            requirement="P_trace is not Box, not hyperbolic propagation",
            role="keeps scalar/trace conversion non-radiative",
            allowed_if="projection is algebraic/elliptic/constraint-like",
            forbidden_if="P_trace creates Box kappa or Box zeta",
            status="FORBIDDEN",
            missing="parent proof of no scalar inertia",
        ),
        TraceProjectorEntry(
            name="T8: relaxation compatibility",
            requirement="P_relax P_trace may feed first-order kappa relaxation",
            role="allows kappa to track projected residual without scalar sloshing",
            allowed_if="P_relax is first-order/non-inertial",
            forbidden_if="P_relax becomes second-order oscillator",
            status="CANDIDATE",
            missing="P_relax and Gamma_relax relation",
        ),
        TraceProjectorEntry(
            name="T9: diagnostic versus energetic status",
            requirement="P_trace output must be labeled diagnostic, constraint, or energetic",
            role="prevents same projection from being counted twice",
            allowed_if="energy convention is explicit",
            forbidden_if="P_trace output is both kappa identity and physical energy term",
            status="UNRESOLVED",
            missing="degree-of-freedom and energy-accounting rule",
        ),
        TraceProjectorEntry(
            name="T10: recombination compatibility",
            requirement="P_recombination counts A/zeta/kappa trace response once",
            role="prevents spatial metric trace double/triple-counting",
            allowed_if="P_trace output is inserted into geometry through a single channel",
            forbidden_if="g_ij independently adds scalar_spatial_response(A), zeta, and kappa trace",
            status="REQUIRED",
            missing="P_recombination definition",
        ),
        TraceProjectorEntry(
            name="T11: raw pressure/trace source rejection",
            requirement="P_trace[T] is not raw T, raw p, or Delta kappa = alpha T",
            role="prevents exterior charge and scalar double-counting",
            allowed_if="raw trace is compensated/projected and boundary-neutral",
            forbidden_if="ordinary positive pressure produces kappa_ext ~ 1/r",
            status="REJECTED",
            missing="not pursued as raw source",
        ),
        TraceProjectorEntry(
            name="T12: recommended provisional P_trace definition",
            requirement="P_trace = trace extraction + A-sector exclusion + compensation + TT annihilation, with boundary cooperation",
            role="best current operational definition",
            allowed_if="declared as requirement bundle, not a derived operator",
            forbidden_if="treated as finished parent projector",
            status="RECOMMENDED",
            missing="actual parent-derived mathematical operator",
        ),
    ]


def print_entry(e: TraceProjectorEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Requirement: {e.requirement}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")


def case_0_problem_statement():
    header("Case 0: Trace projector definition problem")

    print("Question:")
    print()
    print("  What must P_trace do for projected kappa to be safe?")
    print()
    print("Goal:")
    print()
    print("  define P_trace requirements without pretending the parent projector is derived")
    print()
    print("Discipline:")
    print()
    print("  P_trace is not raw trace source")
    print("  P_trace is not Box kappa or Box zeta")
    print("  P_trace must annihilate TT")
    print("  P_trace must exclude A-sector mass")
    print("  P_trace must support exterior neutrality")
    print("  P_trace must not create energy double-counting")

    status_line("trace projector problem posed", "REQUIRED")


def case_1_inventory(entries: List[TraceProjectorEntry]):
    header("Case 1: P_trace requirement inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[TraceProjectorEntry]):
    header("Case 2: Compact P_trace ledger")

    print("| Entry | Requirement | Status | Missing |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.requirement.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.missing.replace("|", "/")
            + " |"
        )

    status_line("compact P_trace ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[TraceProjectorEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  P_trace is not a single simple operation yet.")
    print("  It is currently a requirement bundle:")
    print("    trace extraction, A-exclusion, compensation, TT annihilation, and boundary cooperation.")
    print("  The next likely split is P_trace versus P_boundary versus P_recombination.")

    status_line("P_trace status count produced", "STRUCTURAL")


def case_4_minimal_projector_bundle():
    header("Case 4: Minimal P_trace requirement bundle")

    print("Current operational bundle:")
    print()
    print("  P_trace =")
    print("    trace extraction")
    print("    + A-sector mass exclusion")
    print("    + compensation / zero monopole")
    print("    + TT annihilation")
    print("    + boundary cooperation")
    print()
    print("Not yet decided:")
    print()
    print("  which pieces belong to P_trace itself")
    print("  which belong to P_boundary")
    print("  which belong to P_recombination")
    print("  which belong to P_relax")
    print()
    print("Therefore:")
    print()
    print("  P_trace is a requirement bundle, not a derived operator.")

    status_line("minimal P_trace bundle stated", "RECOMMENDED")


def case_5_failure_controls():
    header("Case 5: Failure controls")

    print("P_trace fails if:")
    print()
    print("1. it is raw pressure/trace source")
    print("2. it duplicates A-sector mass")
    print("3. it allows kappa/zeta exterior 1/r charge")
    print("4. it contaminates TT radiation")
    print("5. it becomes Box kappa or Box zeta")
    print("6. it hides boundary conditions")
    print("7. it creates e_kappa / epsilon_zeta double-counting")
    print("8. it is treated as parent-derived before derivation")

    status_line("P_trace failure controls stated", "RISK")


def case_6_next_tests():
    header("Case 6: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_trace_projector_definition.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_boundary_projector_for_volume_neutrality.py")
    print("   Split off boundary/exterior neutrality duties.")
    print()
    print("3. candidate_recombination_projector_for_trace_volume.py")
    print("   Split off metric assembly / no-double-counting duties.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_boundary_projector_for_volume_neutrality.py")
    print()
    print("Reason:")
    print("  P_trace currently carries boundary neutrality duties. Split P_boundary next.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("P_trace is currently best understood as a requirement bundle:")
    print()
    print("  trace extraction")
    print("  A-sector exclusion")
    print("  compensation / zero monopole")
    print("  TT annihilation")
    print("  boundary cooperation")
    print()
    print("It is not yet a derived operator.")
    print()
    print("Possible next artifact:")
    print("  candidate_trace_projector_definition.md")
    print()
    print("Possible next script:")
    print("  candidate_boundary_projector_for_volume_neutrality.py")


def main():
    header("Candidate Trace Projector Definition")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_minimal_projector_bundle()
    case_5_failure_controls()
    case_6_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
