# Candidate gauge structure requirements
#
# Purpose
# -------
# The constraint/evolution split identified gauge structure as a missing blocker.
#
# This script does not derive the full gauge structure.
# It inventories what a parent theory must supply:
#
#   1. coordinate/gauge modes must not be counted as physical sectors,
#   2. A, kappa, W_i, h_ij^TT need gauge behavior,
#   3. physical diagnostics should be gauge-invariant or gauge-fixed with care,
#   4. reduced gauges such as areal gauge, static gauge, and TT gauge must be
#      related to a parent transformation structure.
#
# The script uses strict statuses:
#
#   SATISFIED_REDUCED
#   PARTIAL
#   MISSING
#   RISK
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/08_covariant_parent_structure/
#   or:
#   scripts_v3/candidate_gauge_structure_requirements.py

from dataclasses import dataclass
from typing import List


# =============================================================================
# Utilities
# =============================================================================

def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_line(label: str, status: str, detail: str = "") -> None:
    marks = {
        "SATISFIED_REDUCED": "PASS",
        "PARTIAL": "WARN",
        "MISSING": "FAIL",
        "RISK": "WARN",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class GaugeRequirement:
    name: str
    status: str
    current_support: str
    parent_must_supply: str
    risk_if_missing: str


def print_req(req: GaugeRequirement) -> None:
    print()
    print("-" * 100)
    print(req.name)
    print("-" * 100)
    status_line(req.name, req.status)
    print(f"Current support: {req.current_support}")
    print(f"Parent must supply: {req.parent_must_supply}")
    print(f"Risk if missing: {req.risk_if_missing}")


# =============================================================================
# Case 0: Problem statement
# =============================================================================

def case_0_problem_statement():
    header("Case 0: Gauge structure requirements problem")

    print("Gauge structure is a missing blocker.")
    print()
    print("The parent theory must identify:")
    print()
    print("  physical variables")
    print("  coordinate artifacts")
    print("  allowed gauge choices")
    print("  gauge-invariant diagnostics")
    print("  how reduced gauges map into one parent structure")

    status_line("gauge requirements problem posed", "SATISFIED_REDUCED")


# =============================================================================
# Case 1: Build gauge requirements
# =============================================================================

def build_requirements() -> List[GaugeRequirement]:
    return [
        GaugeRequirement(
            name="G1: Areal-radius gauge behavior",
            status="PARTIAL",
            current_support=(
                "Orbit-space studies identified the areal radius R and showed "
                "that kappa in areal gauge depends on A and |grad R|."
            ),
            parent_must_supply=(
                "Transformation law under radial coordinate changes and a clear "
                "statement of which areal-gauge quantities are invariant diagnostics."
            ),
            risk_if_missing=(
                "Radial coordinate artifacts may be mistaken for physical kappa or B behavior."
            ),
        ),
        GaugeRequirement(
            name="G2: Static slicing / lapse behavior",
            status="PARTIAL",
            current_support=(
                "A is used as a static lapse/scalar potential in reduced exterior studies."
            ),
            parent_must_supply=(
                "How A transforms under time reparameterization and slicing changes, "
                "and how to normalize A asymptotically."
            ),
            risk_if_missing=(
                "The scalar A channel may include gauge normalization artifacts."
            ),
        ),
        GaugeRequirement(
            name="G3: Kappa physical versus gauge component",
            status="PARTIAL",
            current_support=(
                "Kappa is interpreted as trace/volume imbalance, especially in areal/static settings."
            ),
            parent_must_supply=(
                "Gauge-invariant or gauge-fixed meaning of kappa and its source law."
            ),
            risk_if_missing=(
                "Kappa deviations may be coordinate volume effects rather than physical response."
            ),
        ),
        GaugeRequirement(
            name="G4: Vector W_i gauge behavior",
            status="MISSING",
            current_support=(
                "W_i is identified as a shift/current/frame-dragging candidate."
            ),
            parent_must_supply=(
                "Transformation of W_i under spatial diffeomorphisms and time slicing, "
                "plus gauge-invariant frame-dragging observables."
            ),
            risk_if_missing=(
                "Vector sector may double-count gauge shift or miss physical frame dragging."
            ),
        ),
        GaugeRequirement(
            name="G5: TT gauge and tensor physical modes",
            status="SATISFIED_REDUCED",
            current_support=(
                "h_ij^TT plus/cross basis is trace-free and transverse in reduced wave studies."
            ),
            parent_must_supply=(
                "Parent derivation of TT projection, gauge conditions, and physical mode count."
            ),
            risk_if_missing=(
                "The TT sector may remain a reduced gauge choice rather than a derived physical sector."
            ),
        ),
        GaugeRequirement(
            name="G6: Scalar A_rad versus gauge artifact",
            status="PARTIAL",
            current_support=(
                "A_rad is classified as absent/controlled and distinct from moving constraint wells."
            ),
            parent_must_supply=(
                "Determine whether A_rad is physical, gauge, constrained, damped, or projected out."
            ),
            risk_if_missing=(
                "A_rad could be overcounted as physical radiation or undercounted if real."
            ),
        ),
        GaugeRequirement(
            name="G7: Gauge-invariant observable set",
            status="MISSING",
            current_support=(
                "Reduced scripts use diagnostics like AB, TT traces, fluxes, and projections."
            ),
            parent_must_supply=(
                "A list of observables or invariant diagnostics: redshift/lapse normalization, "
                "areal radius, frame dragging, TT strain, curvature-like quantities."
            ),
            risk_if_missing=(
                "The theory may compare gauge-dependent variables to observations."
            ),
        ),
        GaugeRequirement(
            name="G8: Coordinate recombination map",
            status="MISSING",
            current_support=(
                "Sectors are informally mapped to g_tt, g_ti, trace, and TT spatial parts."
            ),
            parent_must_supply=(
                "A metric/geometric reconstruction rule and gauge conditions for combining sectors."
            ),
            risk_if_missing=(
                "The reduced sectors may not assemble into one consistent geometry."
            ),
        ),
    ]


# =============================================================================
# Case 2: Print requirements
# =============================================================================

def case_2_print_requirements(reqs: List[GaugeRequirement]):
    header("Case 2: Gauge requirement inventory")

    for req in reqs:
        print_req(req)


# =============================================================================
# Case 3: Status counts
# =============================================================================

def case_3_status_counts(reqs: List[GaugeRequirement]):
    header("Case 3: Status counts")

    counts = {}
    for req in reqs:
        counts[req.status] = counts.get(req.status, 0) + 1

    for status in ["SATISFIED_REDUCED", "PARTIAL", "MISSING", "RISK"]:
        print(f"{status}: {counts.get(status, 0)}")

    if counts.get("MISSING", 0) > 0:
        status_line("gauge structure incomplete", "MISSING",
                    "several gauge requirements are not yet supplied")
    else:
        status_line("gauge structure complete", "SATISFIED_REDUCED")


# =============================================================================
# Case 4: Physical/gauge classification table
# =============================================================================

def case_4_classification_table():
    header("Case 4: Physical versus gauge classification table")

    print("| Object | Current classification | Gauge concern |")
    print("|---|---|---|")
    print("| A_constraint | physical after boundary normalization | time slicing/lapse normalization |")
    print("| A_rad | controlled hazard | may be physical, gauge, or constrained |")
    print("| kappa | trace/interior diagnostic | may include coordinate-volume artifact |")
    print("| W_i | vector/current response | may mix with shift gauge |")
    print("| h_ij^TT | physical tensor radiation in TT gauge | parent TT projection needed |")
    print("| areal radius R | geometric scalar in spherical reduction | must anchor radial gauge |")
    print("| AB / kappa_areal | useful diagnostic | gauge-aware, not automatic scalar invariant |")

    status_line("physical/gauge classification table stated", "PARTIAL",
                "classification needs parent derivation")


# =============================================================================
# Case 5: Blocking gauge gaps
# =============================================================================

def case_5_blocking_gaps(reqs: List[GaugeRequirement]):
    header("Case 5: Blocking gauge gaps")

    blocking = [req for req in reqs if req.status == "MISSING"]

    print("Blocking missing gauge structures:")
    for req in blocking:
        print(f"  - {req.name}")

    print()
    print("These should be addressed before claiming a covariant parent.")

    status_line("blocking gauge gaps identified", "MISSING",
                "gauge structure remains a parent-theory blocker")


# =============================================================================
# Case 6: Next study recommendation
# =============================================================================

def case_6_next_study():
    header("Case 6: Next study recommendation")

    print("Recommended next script:")
    print()
    print("  candidate_metric_geometric_recombination.py")
    print()
    print("Reason:")
    print("  Gauge requirements point directly at the recombination problem:")
    print("  how A, kappa, W_i, and h_ij^TT assemble into one metric/geometric object.")
    print()
    print("Alternative:")
    print("  candidate_gauge_invariant_diagnostics.py")

    status_line("next study selected", "PARTIAL",
                "metric/geometric recombination is the next blocker")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation(reqs: List[GaugeRequirement]):
    header("Final interpretation")

    print("Gauge structure is not solved yet.")
    print()
    print("Reduced support exists for:")
    print("  areal-radius awareness")
    print("  static lapse normalization")
    print("  TT plus/cross basis")
    print()
    print("Missing or partial structures remain for:")
    print("  W_i gauge behavior")
    print("  gauge-invariant observable set")
    print("  coordinate recombination map")
    print("  physical versus gauge status of kappa and A_rad")
    print()
    print("Possible next artifact:")
    print("  candidate_gauge_structure_requirements.md")
    print()
    print("Possible next script:")
    print("  candidate_metric_geometric_recombination.py")


def main():
    header("Candidate Gauge Structure Requirements")
    case_0_problem_statement()
    reqs = build_requirements()
    case_2_print_requirements(reqs)
    case_3_status_counts(reqs)
    case_4_classification_table()
    case_5_blocking_gaps(reqs)
    case_6_next_study()
    final_interpretation(reqs)


if __name__ == "__main__":
    main()
