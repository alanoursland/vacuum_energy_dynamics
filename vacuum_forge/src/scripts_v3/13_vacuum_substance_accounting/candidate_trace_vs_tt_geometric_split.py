# Candidate trace versus TT geometric split
#
# Purpose
# -------
# The volume-form configuration audit found:
#
#   zeta = ln sqrt(gamma)
#
# as the best current geometric candidate for vacuum-spacetime configuration.
#
# At linear order:
#
#   delta zeta = 1/2 gamma^ij delta gamma_ij
#
# and for TT perturbations:
#
#   gamma^ij h_ij^TT = 0
#
# therefore:
#
#   delta zeta|TT = 0
#
# This script tests the geometric split:
#
#   trace / scalar / longitudinal modes change volume form and are conversion-limited.
#   TT modes are volume-preserving shear and may propagate.
#
# This is not a proof of full TT-only radiation.
# It is a theorem-target audit.

from dataclasses import dataclass
from typing import List


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_line(label: str, status: str, detail: str = "") -> None:
    marks = {
        "CANDIDATE": "WARN",
        "STRUCTURAL": "WARN",
        "CONSTRAINED": "WARN",
        "REQUIRED": "WARN",
        "MISSING": "FAIL",
        "UNRESOLVED": "FAIL",
        "RISK": "WARN",
        "FORBIDDEN": "PASS",
        "REJECTED": "WARN",
        "DERIVED_REDUCED": "PASS",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class SplitEntry:
    name: str
    mode: str
    geometric_effect: str
    candidate_rule: str
    forbidden_interpretation: str
    status: str
    missing: str


def build_entries() -> List[SplitEntry]:
    return [
        SplitEntry(
            name="T1: volume strain variable",
            mode="trace/volume scalar",
            geometric_effect="zeta = ln sqrt(gamma) measures local volume-form strain in a chosen slice",
            candidate_rule="delta zeta = 1/2 gamma^ij delta gamma_ij",
            forbidden_interpretation="zeta as fully covariant observable without frame/foliation",
            status="CANDIDATE",
            missing="frame/foliation or covariant volume current",
        ),
        SplitEntry(
            name="T2: pure trace perturbation",
            mode="h_ij = (1/3) gamma_ij h",
            geometric_effect="changes volume form: delta zeta = h/2",
            candidate_rule="trace perturbation routes to P_trace / volume conversion",
            forbidden_interpretation="trace perturbation propagates as ordinary far-zone scalar radiation",
            status="STRUCTURAL",
            missing="parent P_trace and conversion law",
        ),
        SplitEntry(
            name="T3: TT perturbation",
            mode="h_ij^TT with gamma^ij h_ij^TT=0 and div h^TT=0",
            geometric_effect="preserves volume at linear order: delta zeta|TT=0",
            candidate_rule="TT shear may propagate without vacuum creation/destruction",
            forbidden_interpretation="TT mode treated as volume-changing scalar conversion",
            status="CANDIDATE",
            missing="nonlinear/covariant TT statement and source coefficient",
        ),
        SplitEntry(
            name="T4: scalar A-sector",
            mode="scalar mass constraint",
            geometric_effect="controls exterior mass response through A_flux, not volume-form charge",
            candidate_rule="rho -> A_flux; not rho -> zeta exterior charge",
            forbidden_interpretation="A-sector mass duplicated as volume-form exterior scalar tail",
            status="CONSTRAINED",
            missing="parent scalar constraint propagation",
        ),
        SplitEntry(
            name="T5: kappa trace/volume mismatch",
            mode="kappa",
            geometric_effect="candidate mismatch between zeta and local equilibrium zeta_min",
            candidate_rule="kappa ~ zeta - zeta_min or reduced kappa = 1/2 ln(AB)",
            forbidden_interpretation="kappa as independent rho-sourced scalar field",
            status="CANDIDATE",
            missing="precise kappa-zeta map",
        ),
        SplitEntry(
            name="T6: scalar/trace conversion",
            mode="would-be scalar wave",
            geometric_effect="conversion into vacuum-spacetime configuration rather than far-zone propagation",
            candidate_rule="trace/volume disturbance changes zeta and relaxes/exchanges with epsilon_vac_config",
            forbidden_interpretation="Box A, A_rad, or Box kappa as ordinary radiation",
            status="CONSTRAINED",
            missing="conversion operator / parent projector",
        ),
        SplitEntry(
            name="T7: longitudinal current",
            mode="P_L j",
            geometric_effect="updates scalar constraint / density redistribution, not transverse shear",
            candidate_rule="P_L j -> scalar continuity and A constraint propagation",
            forbidden_interpretation="P_L j sources W_i or TT radiation",
            status="CONSTRAINED",
            missing="scalar constraint propagation identity",
        ),
        SplitEntry(
            name="T8: transverse current",
            mode="P_T j",
            geometric_effect="sources vector shear/frame-dragging response",
            candidate_rule="P_T j -> W_i",
            forbidden_interpretation="transverse vector response treated as volume creation",
            status="STRUCTURAL",
            missing="normalization alpha_W/K_c and recombination map",
        ),
        SplitEntry(
            name="T9: nonlinear volume preservation caveat",
            mode="finite-amplitude TT/shear",
            geometric_effect="linear trace-free does not automatically prove nonlinear determinant preservation",
            candidate_rule="TT-only radiation theorem needs nonlinear/covariant extension",
            forbidden_interpretation="linear result advertised as full theorem",
            status="RISK",
            missing="nonlinear determinant/shear analysis",
        ),
        SplitEntry(
            name="T10: far-zone radiation rule",
            mode="ordinary radiation",
            geometric_effect="far-zone propagating radiation should be volume-preserving TT shear only",
            candidate_rule="ordinary far-zone radiation = h_ij^TT",
            forbidden_interpretation="scalar/trace conversion leaks into far-zone scalar flux",
            status="CANDIDATE",
            missing="binary-radiation scalar conversion safety check",
        ),
    ]


def print_entry(e: SplitEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Mode: {e.mode}")
    print(f"Geometric effect: {e.geometric_effect}")
    print(f"Candidate rule: {e.candidate_rule}")
    print(f"Forbidden interpretation: {e.forbidden_interpretation}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")


def case_0_problem_statement():
    header("Case 0: Trace versus TT geometric split problem")

    print("Question:")
    print()
    print("  Can the trace/TT split explain scalar conversion and TT-only radiation?")
    print()
    print("Goal:")
    print()
    print("  formalize the geometric difference between volume-changing modes and volume-preserving shear")
    print()
    print("Discipline:")
    print()
    print("  do not claim full theorem from linear trace-free identity")
    print("  do not let trace modes source TT radiation")
    print("  do not let scalar conversion become far-zone scalar radiation")
    print("  keep A-sector mass separate from volume-form charge")

    status_line("trace versus TT split problem posed", "REQUIRED")


def case_1_split_inventory(entries: List[SplitEntry]):
    header("Case 1: Trace/TT split inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[SplitEntry]):
    header("Case 2: Compact trace/TT ledger")

    print("| Entry | Mode | Candidate rule | Status | Missing |")
    print("|---|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.mode.replace("|", "/")
            + " | "
            + e.candidate_rule.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.missing.replace("|", "/")
            + " |"
        )

    status_line("compact trace/TT ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[SplitEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  The trace/TT split is structurally promising.")
    print("  The linear TT volume-preservation result is strong but not a full theorem.")
    print("  The next danger is scalar conversion leaking into far-zone radiation.")

    status_line("trace/TT status count produced", "STRUCTURAL")


def case_4_minimal_geometric_split():
    header("Case 4: Minimal geometric split")

    print("Let:")
    print()
    print("  zeta = ln sqrt(gamma)")
    print()
    print("Then:")
    print()
    print("  delta zeta = 1/2 gamma^ij delta gamma_ij")
    print()
    print("Trace perturbation:")
    print()
    print("  h_ij = (1/3) gamma_ij h")
    print("  gamma^ij h_ij = h")
    print("  delta zeta = h/2")
    print()
    print("TT perturbation:")
    print()
    print("  gamma^ij h_ij^TT = 0")
    print("  delta zeta|TT = 0")
    print()
    print("Interpretation:")
    print()
    print("  trace changes vacuum-spacetime amount")
    print("  TT shear preserves vacuum-spacetime amount at linear order")

    status_line("minimal trace/TT split stated", "CANDIDATE")


def case_5_theorem_target():
    header("Case 5: TT-only radiation theorem target")

    print("Possible theorem target:")
    print()
    print("  Ordinary far-zone radiation is TT-only because")
    print("  volume-changing trace/scalar modes convert into vacuum-spacetime configuration,")
    print("  while volume-preserving TT shear propagates.")
    print()
    print("Required pieces:")
    print()
    print("1. zeta or equivalent volume-form variable.")
    print("2. P_trace conversion law.")
    print("3. P_TT propagation law.")
    print("4. scalar conversion not damping model.")
    print("5. binary radiation scalar-conversion safety.")
    print("6. nonlinear/covariant extension.")
    print()
    print("Current status:")
    print("  theorem target, not theorem.")

    status_line("TT-only theorem target stated", "CANDIDATE")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("The trace/TT split fails if:")
    print()
    print("1. Trace modes propagate as ordinary far-zone scalar radiation.")
    print("2. TT modes change zeta / volume at the relevant order.")
    print("3. A-sector mass is duplicated as volume-form exterior charge.")
    print("4. Kappa and zeta become independent scalar charges.")
    print("5. Linear trace-free identity is overclaimed as full covariance.")
    print("6. Binary systems acquire extra scalar energy loss.")
    print("7. P_trace and P_TT are not actually independent projectors.")

    status_line("trace/TT failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_trace_vs_tt_geometric_split.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_scalar_conversion_not_damping.py")
    print("   Replace damping language with conversion-limited scalar dynamics.")
    print()
    print("3. candidate_binary_radiation_scalar_conversion_safety.py")
    print("   Check if scalar conversion introduces extra orbital-energy loss.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_scalar_conversion_not_damping.py")
    print()
    print("Reason:")
    print("  The trace/TT split suggests scalar modes convert; now define conversion versus damping.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("The trace/TT geometric split says:")
    print()
    print("  trace modes change zeta = ln sqrt(gamma)")
    print("  TT modes preserve zeta at linear order")
    print("  scalar/trace modes are candidates for conversion into vacuum-spacetime configuration")
    print("  TT modes are candidates for propagating volume-preserving shear")
    print()
    print("This is a strong theorem target, not a completed theorem.")
    print()
    print("Possible next artifact:")
    print("  candidate_trace_vs_tt_geometric_split.md")
    print()
    print("Possible next script:")
    print("  candidate_scalar_conversion_not_damping.py")


def main():
    header("Candidate Trace Versus TT Geometric Split")
    case_0_problem_statement()
    entries = build_entries()
    case_1_split_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_minimal_geometric_split()
    case_5_theorem_target()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
