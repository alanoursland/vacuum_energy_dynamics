# Candidate metric geometric recombination
#
# Group:
#   08_covariant_parent_structure
#
# Script type:
#   REQUIREMENTS
#
# Purpose
# -------
# The gauge requirements study identified coordinate recombination as a missing
# blocker.
#
# This script asks whether the reduced sectors can be placed into one weak-field
# metric-like structure without claiming a full covariant parent:
#
#   A_constraint -> lapse/scalar potential
#   kappa        -> trace/volume scalar response
#   W_i          -> shift/vector sector
#   h_ij^TT      -> spatial tensor radiation
#
# It also keeps A_rad controlled/absent.
#
# The goal is not to derive the metric from first principles. The goal is to
# build a recombination map and identify where gauge issues remain.
#
# Status categories:
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
class RecombinationItem:
    sector: str
    metric_slot: str
    status: str
    current_map: str
    unresolved_issue: str


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="gauge_structure_requirements_marker",
        upstream_script_id="08_covariant_parent_structure__candidate_gauge_structure_requirements",
        upstream_derivation_id="gauge_structure_requirements_marker",
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


def print_item(item: RecombinationItem) -> None:
    print()
    print("-" * 100)
    print(item.sector)
    print("-" * 100)
    status_line(item.sector, item.status)
    print(f"Metric/geometric slot: {item.metric_slot}")
    print(f"Current map: {item.current_map}")
    print(f"Unresolved issue: {item.unresolved_issue}")


# =============================================================================
# Case 0: Problem statement
# =============================================================================

def case_0_problem_statement():
    header("Case 0: Metric/geometric recombination problem")

    print("Question:")
    print()
    print("  Can A, kappa, W_i, and h_ij^TT be assembled into one weak-field")
    print("  metric/geometric structure?")
    print()
    print("Caution:")
    print()
    print("  This is a recombination map, not a derivation.")
    print("  Gauge behavior and conservation identities are still missing.")

    status_line("metric recombination problem posed", "SATISFIED_REDUCED")


# =============================================================================
# Case 1: Proposed weak-field metric structure
# =============================================================================

def case_1_metric_ansatz():
    header("Case 1: Proposed weak-field recombination ansatz")

    print("Proposed schematic weak-field structure:")
    print()
    print("  ds^2 = -(1 + 2 Phi/c^2) c^2 dt^2")
    print("         + 2 W_i dx^i c dt")
    print("         + [(1 - 2 Psi/c^2 + trace/kappa part) delta_ij")
    print("            + h_ij^TT] dx^i dx^j")
    print()
    print("Sector interpretation:")
    print()
    print("  A_constraint ~ 1 + 2 Phi/c^2")
    print("  kappa / trace sector ~ scalar spatial trace or volume response")
    print("  W_i ~ shift/vector/frame-dragging sector")
    print("  h_ij^TT ~ tensor radiation")
    print("  A_rad ~ absent or controlled")
    print()
    status_line("schematic recombination ansatz stated", "PARTIAL",
                "not yet derived from parent structure")


# =============================================================================
# Case 2: Build recombination items
# =============================================================================

def build_items() -> List[RecombinationItem]:
    return [
        RecombinationItem(
            sector="A_constraint scalar lapse sector",
            metric_slot="g_tt / lapse",
            status="SATISFIED_REDUCED",
            current_map="A_constraint controls static scalar potential and exterior lapse.",
            unresolved_issue="Derive lapse normalization and constraint nature from parent theory.",
        ),
        RecombinationItem(
            sector="A_rad scalar radiative hazard",
            metric_slot="possible scalar trace/lapse perturbation",
            status="PARTIAL",
            current_map="A_rad is absent or controlled by policy.",
            unresolved_issue="Determine if A_rad is gauge, constrained, damped, massive, or physical but weak.",
        ),
        RecombinationItem(
            sector="kappa trace/volume sector",
            metric_slot="spatial trace / determinant / volume imbalance",
            status="PARTIAL",
            current_map="kappa is useful in static areal reductions and interior-response toys.",
            unresolved_issue="Separate physical trace response from coordinate volume artifact.",
        ),
        RecombinationItem(
            sector="W_i vector/current sector",
            metric_slot="g_ti / shift",
            status="PARTIAL",
            current_map="W_i is assigned to frame dragging and current response.",
            unresolved_issue="Derive gauge behavior, source coupling, and radiation safety.",
        ),
        RecombinationItem(
            sector="h_ij^TT tensor sector",
            metric_slot="spatial transverse-traceless metric perturbation",
            status="SATISFIED_REDUCED",
            current_map="TT basis, wave equation, and quadrupole source projection established at reduced level.",
            unresolved_issue="Derive TT projection and coupling from parent gauge structure.",
        ),
        RecombinationItem(
            sector="Gauge modes",
            metric_slot="coordinate transformations / nonphysical components",
            status="MISSING",
            current_map="Gauge modes are acknowledged but not derived.",
            unresolved_issue="Identify which components can be transformed away and which diagnostics are invariant.",
        ),
        RecombinationItem(
            sector="Conservation identities",
            metric_slot="source-geometry compatibility",
            status="MISSING",
            current_map="Conservation ideas are used in reduced source arguments.",
            unresolved_issue="Derive Bianchi-like or continuity identities.",
        ),
    ]


# =============================================================================
# Case 3: Print recombination items
# =============================================================================

def case_3_print_items(items: List[RecombinationItem]):
    header("Case 3: Recombination inventory")

    for item in items:
        print_item(item)


# =============================================================================
# Case 4: Recombination table
# =============================================================================

def case_4_recombination_table(items: List[RecombinationItem]):
    header("Case 4: Recombination table")

    print("| Sector | Metric/geometric slot | Status |")
    print("|---|---|---|")
    for item in items:
        print(f"| {item.sector} | {item.metric_slot} | {item.status} |")

    status_line("recombination table produced", "PARTIAL",
                "map exists but parent derivation missing")


# =============================================================================
# Case 5: Double-counting risks
# =============================================================================

def case_5_double_counting_risks():
    header("Case 5: Double-counting and omission risks")

    print("Risks:")
    print()
    print("1. A_rad could double-count scalar trace/lapse perturbations.")
    print("2. kappa could double-count coordinate volume changes.")
    print("3. W_i could double-count shift gauge if not tied to frame-dragging observables.")
    print("4. h_ij^TT is safer, but parent TT projection is still needed.")
    print("5. A_constraint and kappa may mix in non-static or non-areal gauges.")
    print("6. Source coupling may be inconsistent without conservation identities.")


# =============================================================================
# Case 6: Minimal safe recombination policy
# =============================================================================

def case_6_safe_policy():
    header("Case 6: Minimal safe recombination policy")

    print("Until a parent derivation exists, use this conservative policy:")
    print()
    print("1. Treat A_constraint as physical only after boundary/lapse normalization.")
    print("2. Treat A_rad as absent or explicitly controlled.")
    print("3. Treat kappa as gauge-aware, not automatically invariant.")
    print("4. Treat W_i as provisional until frame-dragging observable is derived.")
    print("5. Treat h_ij^TT as the safest physical radiative sector.")
    print("6. Do not claim full metric recombination yet.")
    print()
    status_line("safe recombination policy stated", "PARTIAL",
                "conservative but not a derivation")


# =============================================================================
# Case 7: Status counts
# =============================================================================

def case_7_status_counts(items: List[RecombinationItem]):
    header("Case 7: Status counts")

    counts = {}
    for item in items:
        counts[item.status] = counts.get(item.status, 0) + 1

    for status in ["SATISFIED_REDUCED", "PARTIAL", "MISSING", "RISK"]:
        print(f"{status}: {counts.get(status, 0)}")

    if counts.get("MISSING", 0) > 0:
        status_line("metric recombination incomplete", "MISSING",
                    "gauge and conservation structures are missing")
    else:
        status_line("metric recombination complete", "SATISFIED_REDUCED")

    return counts


# =============================================================================
# Case 8: Next study recommendation
# =============================================================================

def case_8_next_study():
    header("Case 8: Next study recommendation")

    print("Recommended next script:")
    print()
    print("  candidate_gauge_invariant_diagnostics.py")
    print()
    print("Reason:")
    print("  Recombination cannot be trusted until we know which diagnostics are")
    print("  invariant or at least safe under the chosen gauge.")
    print()
    print("Alternative:")
    print("  candidate_conservation_identity_requirements.py")

    status_line("next study selected", "PARTIAL",
                "gauge-invariant diagnostics should come next")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation(items: List[RecombinationItem]):
    header("Final interpretation")

    print("A schematic recombination map exists:")
    print()
    print("  A_constraint -> g_tt / lapse")
    print("  kappa        -> spatial trace / volume response")
    print("  W_i          -> g_ti / shift")
    print("  h_ij^TT      -> spatial TT radiation")
    print()
    print("But this is not yet a covariant parent.")
    print()
    print("The biggest blockers are:")
    print("  gauge modes")
    print("  conservation identities")
    print("  invariant observable set")
    print()
    print("Possible next artifact:")
    print("  candidate_metric_geometric_recombination.md")
    print()
    print("Possible next script:")
    print("  candidate_gauge_invariant_diagnostics.py")


def main():
    header("Candidate Metric Geometric Recombination")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement()
    case_1_metric_ansatz()
    items = build_items()
    case_3_print_items(items)
    case_4_recombination_table(items)
    case_5_double_counting_risks()
    case_6_safe_policy()
    counts = case_7_status_counts(items)
    case_8_next_study()
    final_interpretation(items)

    # --- ProofObligationRecord per MISSING or PARTIAL item ---

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_A_rad_metric_status",
        script_id=SCRIPT_ID,
        title="Derive metric status of A_rad (gauge, constrained, damped, or physical)",
        status=ObligationStatus.OPEN,
        description=(
            "Determine from the parent structure whether A_rad occupies a metric slot "
            "(scalar lapse perturbation) or is absent, constrained, gauge, or damped."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_kappa_physical_metric_slot",
        script_id=SCRIPT_ID,
        title="Derive kappa physical metric slot and separate from coordinate artifact",
        status=ObligationStatus.OPEN,
        description=(
            "Show which part of kappa is a genuine spatial-trace/volume-response "
            "metric slot and which part is a coordinate-volume artifact."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_W_i_recombination_slot_and_gauge_safety",
        script_id=SCRIPT_ID,
        title="Derive W_i recombination slot and gauge safety",
        status=ObligationStatus.OPEN,
        description=(
            "Show that W_i genuinely occupies the g_ti/shift metric slot and is not "
            "a pure gauge artifact, by deriving its source coupling and radiation safety."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_gauge_mode_projections_for_recombination",
        script_id=SCRIPT_ID,
        title="Derive gauge mode projections for metric recombination",
        status=ObligationStatus.OPEN,
        description=(
            "Identify which metric components are pure gauge and derive projections "
            "that remove them, leaving only physical sector content."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_conservation_identities_for_recombination",
        script_id=SCRIPT_ID,
        title="Derive conservation identities needed for metric recombination",
        status=ObligationStatus.OPEN,
        description=(
            "Bianchi-like or continuity identities must be derived to ensure that "
            "the sector source assignments are consistent with the metric recombination."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_A_constraint_lapse_normalization",
        script_id=SCRIPT_ID,
        title="Derive A_constraint lapse normalization condition from parent",
        status=ObligationStatus.OPEN,
        description=(
            "Supply the parent-theory derivation of the asymptotic lapse normalization "
            "A_constraint -> 1 at spatial infinity and its constraint nature."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_tt_projection_for_recombination",
        script_id=SCRIPT_ID,
        title="Derive TT projection for h_ij^TT from parent gauge structure",
        status=ObligationStatus.OPEN,
        description=(
            "Supply the parent-theory derivation of the TT projection conditions "
            "that place h_ij^TT in the spatial tensor metric slot."
        ),
    ))

    # --- Governance claims ---

    ns.record_claim(ClaimRecord(
        claim_id="recombination_map_is_schematic_not_derivation",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "The schematic metric recombination map (A -> g_tt, kappa -> spatial trace, "
            "W_i -> g_ti, h_ij^TT -> TT spatial) is a provisional assignment, not a "
            "derivation. Gauge modes and conservation identities are missing. "
            "The map must not be treated as covariant closure."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="safe_recombination_policy",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Until parent derivations exist: treat A_constraint as physical only after "
            "lapse normalization; treat A_rad as absent or controlled; treat kappa as "
            "gauge-aware; treat W_i as provisional; treat h_ij^TT as safest physical sector. "
            "Do not claim full metric recombination."
        ),
    ))

    # --- Branch decision ---

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_covariant_metric_recombination_claim",
        script_id=SCRIPT_ID,
        branch_id="covariant_metric_recombination",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "derive_gauge_mode_projections_for_recombination",
            "derive_conservation_identities_for_recombination",
        ],
        description=(
            "The covariant metric recombination claim is deferred. "
            "Gauge mode projections and conservation identities are missing."
        ),
    ))

    # --- Routes ---

    ns.record_route(RouteRecord(
        route_id="metric_recombination_completion_route",
        script_id=SCRIPT_ID,
        name="Metric recombination completion route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[
            "derive_gauge_mode_projections_for_recombination",
            "derive_conservation_identities_for_recombination",
            "derive_W_i_recombination_slot_and_gauge_safety",
        ],
        activation_conditions=[
            "gauge modes are projected",
            "conservation identities are derived",
            "all sector slots are genuinely assigned",
        ],
    ))

    # Inventory marker
    ns.record_derivation(
        derivation_id="metric_recombination_marker",
        inputs=[],
        output=sp.Symbol("metric_recombination_map_stated"),
        method="metric_geometric_recombination_inventory",
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
                 "A_constraint g_tt and h_ij^TT TT slot established at reduced level")
        out.line(f"partial: {n_partial}", StatusMark.DEFER,
                 "A_rad, kappa, W_i partial")
        out.line(f"missing: {n_missing}", StatusMark.FAIL,
                 "gauge modes and conservation identities missing")
        out.line("recombination map is schematic not derivation (policy)", StatusMark.FAIL,
                 "must not claim covariant closure")
        out.line("covariant metric recombination deferred", StatusMark.DEFER,
                 "deferred pending gauge projections and conservation identities")

    with out.unresolved_obligations():
        out.line("derive A_rad metric status", StatusMark.OBLIGATION,
                 "open proof obligation recorded")
        out.line("derive kappa physical metric slot", StatusMark.OBLIGATION,
                 "open proof obligation recorded")
        out.line("derive W_i recombination slot and gauge safety", StatusMark.OBLIGATION,
                 "open proof obligation recorded")
        out.line("derive gauge mode projections for recombination", StatusMark.OBLIGATION,
                 "open proof obligation recorded")
        out.line("derive conservation identities for recombination", StatusMark.OBLIGATION,
                 "open proof obligation recorded")
        out.line("derive A_constraint lapse normalization", StatusMark.OBLIGATION,
                 "open proof obligation recorded")
        out.line("derive TT projection for recombination", StatusMark.OBLIGATION,
                 "open proof obligation recorded")


if __name__ == "__main__":
    main()
