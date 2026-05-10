# Candidate gauge structure requirements
#
# Group:
#   08_covariant_parent_structure
#
# Script type:
#   REQUIREMENTS
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

from dataclasses import dataclass
from pathlib import Path
from typing import List

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    BranchDecisionRecord,
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    RecordKind,
    RouteRecord,
    ScriptOutput,
    StatusMark,
)


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"


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


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="constraint_evolution_split_marker",
        upstream_script_id="08_covariant_parent_structure__candidate_constraint_vs_evolution_split",
        upstream_derivation_id="constraint_evolution_split_marker",
    )
    return archive, ns, invalidated


def print_archive_status(ns, invalidated: bool) -> None:
    if invalidated:
        print("[INFO] Archive invalidated due to source change.")
    checks = ns.verify_dependencies()
    if not checks:
        print("[INFO] Archive dependencies: none declared.")
        return
    print("[INFO] Archive dependency check:")
    for check in checks:
        print(f"  - {check.dependency.dependency_id}: {check.status} ({check.message})")


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

    return counts


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
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement()
    reqs = build_requirements()
    case_2_print_requirements(reqs)
    counts = case_3_status_counts(reqs)
    case_4_classification_table()
    case_5_blocking_gaps(reqs)
    case_6_next_study()
    final_interpretation(reqs)

    # --- ProofObligationRecord for each MISSING or PARTIAL requirement ---

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_G1_areal_gauge_transformation_law",
        script_id=SCRIPT_ID,
        title="G1: Derive areal-radius gauge transformation law",
        status=ObligationStatus.OPEN,
        description=(
            "Supply the transformation law of kappa and other sector variables under "
            "radial coordinate changes, and identify which areal-gauge quantities are "
            "genuine invariants."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_G2_lapse_time_reparameterization_law",
        script_id=SCRIPT_ID,
        title="G2: Derive lapse/A transformation under time reparameterization",
        status=ObligationStatus.OPEN,
        description=(
            "Show how A transforms under time-slicing changes and derive the asymptotic "
            "normalization condition A -> 1 at infinity."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_G3_kappa_gauge_invariant_meaning",
        script_id=SCRIPT_ID,
        title="G3: Derive gauge-invariant or gauge-fixed meaning of kappa",
        status=ObligationStatus.OPEN,
        description=(
            "Separate physical trace response from coordinate-volume artifact in kappa, "
            "and supply its source law."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_G4_W_i_gauge_transformation",
        script_id=SCRIPT_ID,
        title="G4: Derive W_i gauge transformation and gauge-invariant frame-dragging observable",
        status=ObligationStatus.OPEN,
        description=(
            "Supply the transformation of W_i under spatial diffeomorphisms and time "
            "slicing, and construct a gauge-invariant frame-dragging observable."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_G5_tt_projection_from_parent_gauge",
        script_id=SCRIPT_ID,
        title="G5: Derive TT projection and physical mode count from parent gauge",
        status=ObligationStatus.OPEN,
        description=(
            "Derive the TT projection from parent gauge conditions and establish the "
            "physical mode count for h_ij^TT."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_G6_A_rad_physical_or_gauge_status",
        script_id=SCRIPT_ID,
        title="G6: Determine physical vs gauge status of A_rad",
        status=ObligationStatus.OPEN,
        description=(
            "Establish whether A_rad is a physical field, a gauge artifact, a constrained "
            "mode, a damped mode, or projected out in the parent theory."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_G7_gauge_invariant_observable_set",
        script_id=SCRIPT_ID,
        title="G7: Derive gauge-invariant observable set",
        status=ObligationStatus.OPEN,
        description=(
            "Construct a list of observables or invariant diagnostics: redshift/lapse "
            "normalization, areal radius, frame dragging, TT strain, curvature-like quantities."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_G8_coordinate_recombination_map",
        script_id=SCRIPT_ID,
        title="G8: Derive coordinate recombination map",
        status=ObligationStatus.OPEN,
        description=(
            "Supply a metric/geometric reconstruction rule and gauge conditions for "
            "combining A, kappa, W_i, and h_ij^TT into one consistent geometry."
        ),
    ))

    # --- Governance claims ---

    ns.record_claim(ClaimRecord(
        claim_id="gauge_structure_is_parent_blocker",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Gauge structure is a missing blocker for the covariant parent. "
            "G4 (W_i gauge), G7 (observable set), and G8 (recombination map) are missing. "
            "The theory must not compare gauge-dependent sector variables to observations "
            "until these are resolved."
        ),
    ))

    # --- Branch decision ---

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_full_gauge_derived_parent",
        script_id=SCRIPT_ID,
        branch_id="gauge_derived_covariant_parent",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "derive_G4_W_i_gauge_transformation",
            "derive_G7_gauge_invariant_observable_set",
            "derive_G8_coordinate_recombination_map",
        ],
        description=(
            "The claim to a fully gauge-derived covariant parent is deferred. "
            "G4, G7, and G8 are missing. The reduced program may proceed within "
            "reduced gauge choices but must not claim a covariant gauge derivation."
        ),
    ))

    # --- Routes ---

    ns.record_route(RouteRecord(
        route_id="gauge_structure_completion_route",
        script_id=SCRIPT_ID,
        name="Gauge structure completion route for covariant parent",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[
            "derive_G4_W_i_gauge_transformation",
            "derive_G7_gauge_invariant_observable_set",
            "derive_G8_coordinate_recombination_map",
        ],
        activation_conditions=[
            "W_i gauge transformation is derived",
            "gauge-invariant observable set is established",
            "coordinate recombination map is derived",
        ],
    ))

    # Inventory marker
    ns.record_derivation(
        derivation_id="gauge_structure_requirements_marker",
        inputs=[],
        output=sp.Symbol("gauge_structure_blockers_identified"),
        method="gauge_structure_requirement_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )

    ns.write_run_metadata()

    n_missing = counts.get("MISSING", 0)
    n_partial = counts.get("PARTIAL", 0)
    n_satisfied = counts.get("SATISFIED_REDUCED", 0)

    with out.governance_assessments():
        out.line(f"satisfied reduced: {n_satisfied}", StatusMark.PASS,
                 "G5 TT plus/cross basis established in reduced")
        out.line(f"partial: {n_partial}", StatusMark.DEFER,
                 "G1 areal, G2 lapse, G3 kappa, G6 A_rad partial")
        out.line(f"missing: {n_missing}", StatusMark.FAIL,
                 "G4 W_i gauge, G7 observable set, G8 recombination map missing")
        out.line("gauge structure is parent blocker (policy)", StatusMark.FAIL,
                 "must not compare gauge-dependent variables to observations")
        out.line("gauge-derived parent deferred", StatusMark.DEFER,
                 "deferred pending G4, G7, G8")

    with out.unresolved_obligations():
        for req in build_requirements():
            if req.status in ("MISSING", "PARTIAL"):
                out.line(f"derive {req.name}", StatusMark.OBLIGATION,
                         "open proof obligation recorded")

    out.print_summary()


if __name__ == "__main__":
    main()
