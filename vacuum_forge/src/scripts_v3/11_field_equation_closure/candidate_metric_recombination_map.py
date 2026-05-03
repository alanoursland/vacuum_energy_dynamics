# Candidate metric recombination map
#
# Purpose
# -------
# The field-equation closure inventory found that the next major trap is metric
# recombination:
#
#   how do A, W_i, h_ij^TT, and kappa become one metric-like object?
#
# This script states a reduced recombination map and labels each piece:
#
#   derived,
#   structural,
#   constrained,
#   missing,
#   risk.
#
# It does not derive the covariant parent metric.
# It is a recombination audit.
#
# Key dangers:
#
#   silently importing GR,
#   double-counting scalar trace response,
#   letting kappa become a repair knob,
#   mixing gauge diagnostics with physical fields.
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/11_field_equation_closure/
#   or:
#   scripts_v3/candidate_metric_recombination_map.py

from dataclasses import dataclass
from typing import List


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_line(label: str, status: str, detail: str = "") -> None:
    marks = {
        "DERIVED": "PASS",
        "DERIVED_REDUCED": "PASS",
        "STRUCTURAL": "WARN",
        "CONSTRAINED": "WARN",
        "MATCHED": "WARN",
        "MISSING": "FAIL",
        "RISK": "WARN",
        "REJECTED": "WARN",
        "UNFINISHED": "FAIL",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class MetricPiece:
    component: str
    schematic_form: str
    sector_source: str
    status: str
    risk: str
    missing: str


def build_pieces() -> List[MetricPiece]:
    return [
        MetricPiece(
            component="g_tt",
            schematic_form="-A c^2",
            sector_source="A-sector scalar monopole / lapse response",
            status="DERIVED_REDUCED",
            risk="Overextending static spherical scalar result into all regimes.",
            missing="Full nonlinear nonspherical parent map.",
        ),
        MetricPiece(
            component="g_rr / radial scalar piece",
            schematic_form="B = exp(2 kappa)/A in reduced areal gauge",
            sector_source="A plus kappa diagnostic",
            status="DERIVED_REDUCED",
            risk="Treating areal-gauge relation as fully covariant.",
            missing="Gauge-invariant interpretation of kappa and B.",
        ),
        MetricPiece(
            component="g_0i",
            schematic_form="proportional to W_i",
            sector_source="transverse vector current sector",
            status="STRUCTURAL",
            risk="Normalization and sign may be imported from GR.",
            missing="Observable coupling and covariant shift-vector map.",
        ),
        MetricPiece(
            component="g_ij scalar trace",
            schematic_form="scalar spatial response tied to A plus constrained kappa trace role",
            sector_source="A-sector spatial response plus kappa trace relaxation",
            status="CONSTRAINED",
            risk="Double-counting scalar trace response or turning kappa into scalar gravity.",
            missing="No-double-counting rule and parent decomposition.",
        ),
        MetricPiece(
            component="g_ij TT",
            schematic_form="delta_ij + h_ij^TT in weak radiation limit",
            sector_source="tensor TT radiation sector",
            status="STRUCTURAL",
            risk="Correct TT form but coupling/source identity not derived.",
            missing="Tensor coupling normalization and action stiffness.",
        ),
        MetricPiece(
            component="forbidden scalar radiation",
            schematic_form="no ordinary long-range A_rad or kappa breathing wave",
            sector_source="scalar radiation safety constraint",
            status="CONSTRAINED",
            risk="Hidden scalar mode reappears through recombination.",
            missing="Parent mechanism enforcing scalar-radiation absence.",
        ),
    ]


def print_piece(p: MetricPiece) -> None:
    print()
    print("-" * 120)
    print(f"Component: {p.component}")
    print("-" * 120)
    print(f"Schematic form: {p.schematic_form}")
    print(f"Sector source: {p.sector_source}")
    status_line(p.component, p.status)
    print(f"Risk: {p.risk}")
    print(f"Missing: {p.missing}")


def case_0_problem_statement():
    header("Case 0: Metric recombination map problem")

    print("Question:")
    print()
    print("  How do A, W_i, h_ij^TT, and kappa recombine into one metric-like object?")
    print()
    print("Goal:")
    print()
    print("  state a reduced recombination map without pretending it is covariantly derived")
    print()
    print("Discipline:")
    print()
    print("  mark gauge-conditioned pieces")
    print("  mark structural pieces")
    print("  prevent scalar double-counting")
    print("  prevent hidden breathing radiation")
    print("  do not silently import GR")

    status_line("metric recombination problem posed", "CONSTRAINED")


def case_1_reduced_metric_ansatz():
    header("Case 1: Reduced metric ansatz")

    print("Schematic weak/reduced recombination:")
    print()
    print("  ds^2 = -A c^2 dt^2 + 2 W_i c dt dx^i + spatial_metric_ij dx^i dx^j")
    print()
    print("with:")
    print()
    print("  spatial_metric_ij = scalar_spatial_response(A,kappa)_ij + h_ij^TT")
    print()
    print("Current status:")
    print()
    print("  This is a bookkeeping ansatz, not a covariant parent derivation.")

    status_line("reduced metric ansatz stated", "STRUCTURAL",
                "normalizations and signs not final")


def case_2_metric_pieces(pieces: List[MetricPiece]):
    header("Case 2: Metric component ledger")
    for piece in pieces:
        print_piece(piece)


def case_3_kappa_recombination_rule():
    header("Case 3: Kappa recombination rule")

    print("Kappa may enter recombination as:")
    print()
    print("  AB = exp(2 kappa)")
    print()
    print("and as a constrained trace/volume relaxation response.")
    print()
    print("But kappa must not be treated as:")
    print()
    print("  an independent long-range scalar potential")
    print("  an ordinary massless breathing-wave field")
    print("  a duplicate source of rho")
    print()
    print("Preferred rule:")
    print()
    print("  kappa modifies trace/volume matching and interior/boundary relaxation")
    print("  while exterior kappa -> 0 and F_kappa(R+) = 0.")

    status_line("kappa recombination constrained", "CONSTRAINED",
                "parent/gauge split missing")


def case_4_no_double_counting_rules():
    header("Case 4: Recombination no-double-counting rules")

    print("Rules:")
    print()
    print("1. A carries the long-range scalar mass response from rho.")
    print("2. kappa does not carry an independent long-range rho-sourced scalar field.")
    print("3. W_i carries transverse current response; longitudinal current remains scalar continuity.")
    print("4. h_ij^TT carries trace-free tensor radiation.")
    print("5. trace/pressure may shift kappa_min but must not source propagating scalar radiation.")
    print("6. spatial scalar response tied to A must not be duplicated by kappa.")
    print("7. near-boundary kappa smoothing must not change total exterior mass flux by hand.")

    status_line("recombination no-double-counting rules stated", "CONSTRAINED")


def case_5_gr_import_risks():
    header("Case 5: GR import risks")

    print("High-risk imports:")
    print()
    print("  g_0i normalization from frame dragging")
    print("  tensor coupling 16*pi*G/c^4")
    print("  radiation energy coefficient c^3/(32*pi*G)")
    print("  spatial gamma=1 beyond weak scalar derivation")
    print("  Bianchi/conservation identity")
    print()
    print("These may be targets, but should not be claimed as ontology-derived yet.")

    status_line("GR import risks listed", "RISK",
                "targets are not derivations")


def case_6_classification(pieces: List[MetricPiece]):
    header("Case 6: Recombination classification")

    print("| Component | Status |")
    print("|---|---|")
    for p in pieces:
        print(f"| {p.component} | {p.status} |")

    print()
    print("Current recombination status:")
    print()
    print("  useful reduced ansatz")
    print("  not covariantly derived")
    print("  scalar double-counting controlled by rules")
    print("  parent map missing")

    status_line("recombination classification produced", "STRUCTURAL")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_metric_recombination_map.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_source_decomposition_ledger.py")
    print("   Separate rho, j_T, trace, pressure, and TT stress source roles.")
    print()
    print("3. candidate_no_double_counting_constraints.py")
    print("   Expand recombination constraints into explicit source-sector rules.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_source_decomposition_ledger.py")
    print()
    print("Reason:")
    print("  Recombination depends on a clean source split; source roles are the next trap.")

    status_line("next test selected", "CONSTRAINED")


def final_interpretation():
    header("Final interpretation")

    print("The current recombination map is a reduced bookkeeping ansatz:")
    print()
    print("  g_tt from A")
    print("  g_0i from W_i")
    print("  g_ij from scalar spatial response, constrained kappa trace role, and h_ij^TT")
    print()
    print("It is not yet a covariant parent derivation.")
    print()
    print("The two key risks are:")
    print("  scalar double-counting")
    print("  silent GR import")
    print()
    print("Possible next artifact:")
    print("  candidate_metric_recombination_map.md")
    print()
    print("Possible next script:")
    print("  candidate_source_decomposition_ledger.py")


def main():
    header("Candidate Metric Recombination Map")
    case_0_problem_statement()
    case_1_reduced_metric_ansatz()
    pieces = build_pieces()
    case_2_metric_pieces(pieces)
    case_3_kappa_recombination_rule()
    case_4_no_double_counting_rules()
    case_5_gr_import_risks()
    case_6_classification(pieces)
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
