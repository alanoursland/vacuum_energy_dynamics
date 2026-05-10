# Candidate constraint vs evolution split
#
# Group:
#   08_covariant_parent_structure
#
# Script type:
#   REQUIREMENTS
#
# Purpose
# -------
# The covariant parent requirements study identified the next organizing layer:
#
#   Which sectors are constraints?
#   Which sectors are dynamical/evolution fields?
#   Which sectors are relaxation/response modes?
#   Which sectors are controlled hazards?
#
# This script classifies each sector:
#
#   A_constraint
#   A_rad
#   kappa
#   W_i
#   h_ij^TT
#
# using stricter statuses:
#
#   SATISFIED_REDUCED
#   PARTIAL
#   MISSING
#   RISK
#
# Goal:
#   Produce a constraint/evolution map that future gauge and covariant-parent
#   studies can use.

from dataclasses import dataclass
from pathlib import Path
from typing import List

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
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
class SectorSplit:
    sector: str
    variable: str
    preferred_type: str
    status: str
    reason: str
    parent_requirement: str


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="covariant_parent_requirements_marker",
        upstream_script_id="08_covariant_parent_structure__candidate_covariant_parent_requirements",
        upstream_derivation_id="covariant_parent_requirements_marker",
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


def print_split(split: SectorSplit) -> None:
    print()
    print("-" * 100)
    print(f"{split.sector}: {split.variable}")
    print("-" * 100)
    status_line(split.sector, split.status)
    print(f"Preferred equation type: {split.preferred_type}")
    print(f"Reason: {split.reason}")
    print(f"Parent requirement: {split.parent_requirement}")


# =============================================================================
# Case 0: Problem statement
# =============================================================================

def case_0_problem_statement():
    header("Case 0: Constraint/evolution split problem")

    print("A covariant parent must know which reduced sectors are:")
    print()
    print("  constraints")
    print("  dynamical evolution fields")
    print("  relaxation/response modes")
    print("  controlled hazards")
    print("  unknown")
    print()
    print("This script classifies the current sector bundle.")

    status_line("constraint/evolution split problem posed", "SATISFIED_REDUCED")


# =============================================================================
# Case 1: Build split inventory
# =============================================================================

def build_splits() -> List[SectorSplit]:
    return [
        SectorSplit(
            sector="Scalar static sector",
            variable="A_constraint",
            preferred_type="CONSTRAINT / ELLIPTIC",
            status="SATISFIED_REDUCED",
            reason=(
                "Poisson-like A supports static exterior gravity and does not "
                "produce scalar wave dispersion."
            ),
            parent_requirement=(
                "Derive why the lapse/scalar mass response is constrained rather "
                "than an independent long-range radiative scalar."
            ),
        ),
        SectorSplit(
            sector="Scalar radiative hazard",
            variable="A_rad",
            preferred_type="ABSENT OR CONTROLLED",
            status="PARTIAL",
            reason=(
                "A_rad is identified as dangerous if unsuppressed; mechanisms "
                "include projection, damping, absorption, mass gap, relaxation, "
                "or weak coupling."
            ),
            parent_requirement=(
                "Supply the actual mechanism that removes or suppresses A_rad."
            ),
        ),
        SectorSplit(
            sector="Trace/interior response",
            variable="kappa",
            preferred_type="RELAXATION / SOURCED RESPONSE",
            status="PARTIAL",
            reason=(
                "Kappa has been modeled as interior trace/volume response with "
                "exterior suppression, but the source law is not derived."
            ),
            parent_requirement=(
                "Derive stress/pressure/trace source coupling and exterior "
                "relaxation or constraint."
            ),
        ),
        SectorSplit(
            sector="Vector current sector",
            variable="W_i",
            preferred_type="CONSTRAINT OR SLOW VECTOR RESPONSE TBD",
            status="PARTIAL",
            reason=(
                "W_i is needed for frame dragging and current response, but its "
                "equation type is not yet known."
            ),
            parent_requirement=(
                "Derive whether W_i is constraint-like, hyperbolic, or mixed, "
                "and determine vector radiation safety."
            ),
        ),
        SectorSplit(
            sector="Tensor radiation sector",
            variable="h_ij^TT",
            preferred_type="EVOLUTION / HYPERBOLIC",
            status="SATISFIED_REDUCED",
            reason=(
                "TT basis, wave equation, quadrupole source projection, and "
                "action-stiffness toy support a reduced dynamical wave sector."
            ),
            parent_requirement=(
                "Derive the TT evolution equation, gauge restrictions, coupling, "
                "and energy flux from parent structure."
            ),
        ),
        SectorSplit(
            sector="Gauge sector",
            variable="coordinate/gauge modes",
            preferred_type="GAUGE / NONPHYSICAL",
            status="MISSING",
            reason=(
                "Reduced scripts use gauge choices but do not derive full gauge "
                "freedoms or gauge-invariant combinations."
            ),
            parent_requirement=(
                "Identify gauge variables, gauge transformations, and physical "
                "gauge-invariant diagnostics."
            ),
        ),
        SectorSplit(
            sector="Conservation/identity sector",
            variable="source identities",
            preferred_type="CONSTRAINT IDENTITY",
            status="MISSING",
            reason=(
                "Conservation is used in reduced arguments but not derived as a "
                "parent identity."
            ),
            parent_requirement=(
                "Supply Bianchi-like or continuity identities linking source "
                "conservation to field equations."
            ),
        ),
    ]


# =============================================================================
# Case 2: Print split inventory
# =============================================================================

def case_2_print_splits(splits: List[SectorSplit]):
    header("Case 2: Sector split inventory")

    for split in splits:
        print_split(split)


# =============================================================================
# Case 3: Constraint/evolution table
# =============================================================================

def case_3_table(splits: List[SectorSplit]):
    header("Case 3: Constraint/evolution table")

    print("| Sector | Variable | Preferred type | Status |")
    print("|---|---|---|---|")
    for s in splits:
        print(f"| {s.sector} | {s.variable} | {s.preferred_type} | {s.status} |")

    status_line("constraint/evolution table produced", "SATISFIED_REDUCED")


# =============================================================================
# Case 4: Status counts
# =============================================================================

def case_4_status_counts(splits: List[SectorSplit]):
    header("Case 4: Status counts")

    counts = {}
    for s in splits:
        counts[s.status] = counts.get(s.status, 0) + 1

    for status in ["SATISFIED_REDUCED", "PARTIAL", "MISSING", "RISK"]:
        print(f"{status}: {counts.get(status, 0)}")

    if counts.get("MISSING", 0) > 0:
        status_line("constraint/evolution split incomplete", "MISSING",
                    "gauge and conservation identities are missing")
    else:
        status_line("constraint/evolution split complete", "SATISFIED_REDUCED")

    return counts


# =============================================================================
# Case 5: Consistency risks
# =============================================================================

def case_5_consistency_risks():
    header("Case 5: Consistency risks")

    print("Key risks:")
    print()
    print("1. If A_rad is hyperbolic and unsuppressed, extra scalar radiation appears.")
    print("2. If W_i is hyperbolic and unsuppressed, extra vector radiation may appear.")
    print("3. If kappa is not suppressed exterior, weak-field constraints may fail.")
    print("4. If gauge modes are mistaken for physical modes, the sector count is wrong.")
    print("5. If conservation identities are missing, source coupling may be inconsistent.")


# =============================================================================
# Case 6: Parent target split
# =============================================================================

def case_6_parent_target_split():
    header("Case 6: Parent target split")

    print("Desired parent split:")
    print()
    print("Constraints:")
    print("  A_constraint")
    print("  source/conservation identities")
    print("  some gauge restrictions")
    print()
    print("Controlled response:")
    print("  A_rad absent/suppressed")
    print("  kappa sourced/relaxed")
    print("  W_i frame-dragging response TBD")
    print()
    print("Evolution:")
    print("  h_ij^TT tensor waves")
    print()
    print("Gauge:")
    print("  coordinate artifacts projected out")
    print()
    status_line("parent target split stated", "PARTIAL",
                "still needs derivation")


# =============================================================================
# Case 7: Next study recommendation
# =============================================================================

def case_7_next_study():
    header("Case 7: Next study recommendation")

    print("Recommended next script:")
    print()
    print("  candidate_gauge_structure_requirements.py")
    print()
    print("Reason:")
    print("  The split exposes gauge structure as a missing blocking requirement.")
    print("  The next step is to identify which variables are physical and which are")
    print("  gauge shadows.")
    print()
    print("Alternative:")
    print("  candidate_metric_geometric_recombination.py")

    status_line("next study selected", "PARTIAL",
                "gauge structure is the next blocker")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation(splits: List[SectorSplit]):
    header("Final interpretation")

    print("The constraint/evolution split is now clearer:")
    print()
    print("  A_constraint -> constraint / elliptic")
    print("  A_rad        -> absent or controlled")
    print("  kappa        -> relaxation / interior response")
    print("  W_i          -> vector response, equation type TBD")
    print("  h_ij^TT      -> evolution / hyperbolic")
    print("  gauge modes  -> nonphysical / to be projected")
    print()
    print("Strong reduced support exists for A_constraint and h_ij^TT.")
    print("The missing blockers are gauge structure and conservation identities.")
    print()
    print("Possible next artifact:")
    print("  candidate_constraint_vs_evolution_split.md")
    print()
    print("Possible next script:")
    print("  candidate_gauge_structure_requirements.py")


def main():
    header("Candidate Constraint vs Evolution Split")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement()
    splits = build_splits()
    case_2_print_splits(splits)
    case_3_table(splits)
    counts = case_4_status_counts(splits)
    case_5_consistency_risks()
    case_6_parent_target_split()
    case_7_next_study()
    final_interpretation(splits)

    # --- ProofObligationRecord for each MISSING or PARTIAL sector ---

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_A_rad_suppression_mechanism_for_split",
        script_id=SCRIPT_ID,
        title="Derive A_rad suppression mechanism (constraint/evolution split level)",
        status=ObligationStatus.OPEN,
        description=(
            "Show from parent structure why A_rad is absent or suppressed, establishing "
            "its sector type (absent, projected, damped, massive, or relaxed)."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_kappa_source_and_exterior_suppression",
        script_id=SCRIPT_ID,
        title="Derive kappa source law and exterior suppression for split",
        status=ObligationStatus.OPEN,
        description=(
            "Supply stress/pressure/trace source coupling for kappa and derive "
            "why kappa is suppressed in exterior vacuum."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_W_i_equation_type",
        script_id=SCRIPT_ID,
        title="Derive W_i equation type (constraint or hyperbolic)",
        status=ObligationStatus.OPEN,
        description=(
            "Determine whether W_i obeys a constraint equation, a hyperbolic "
            "evolution equation, or a mixed system, and check vector radiation safety."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_gauge_sector_variables_and_transformations",
        script_id=SCRIPT_ID,
        title="Derive gauge sector variables and transformation laws",
        status=ObligationStatus.OPEN,
        description=(
            "Identify which degrees of freedom are gauge artifacts, derive their "
            "transformation laws, and construct physical gauge-invariant combinations."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_conservation_identity_for_split",
        script_id=SCRIPT_ID,
        title="Derive conservation identity for sector split",
        status=ObligationStatus.OPEN,
        description=(
            "Supply Bianchi-like or continuity identities linking source conservation "
            "to the constraint and evolution equations."
        ),
    ))

    # --- Governance claims ---

    ns.record_claim(ClaimRecord(
        claim_id="sector_split_map_partial",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "The current constraint/evolution split is: A_constraint (constraint), "
            "A_rad (absent or controlled), kappa (relaxation/response), W_i (TBD), "
            "h_ij^TT (hyperbolic evolution), gauge modes (nonphysical). "
            "This map is provisional and incomplete pending gauge and conservation derivations."
        ),
    ))

    # --- Routes ---

    ns.record_route(RouteRecord(
        route_id="complete_constraint_evolution_split_route",
        script_id=SCRIPT_ID,
        name="Complete constraint/evolution split with gauge and conservation",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[
            "derive_gauge_sector_variables_and_transformations",
            "derive_conservation_identity_for_split",
            "derive_W_i_equation_type",
        ],
        activation_conditions=[
            "gauge sector is identified and projected",
            "conservation identities are derived",
            "W_i equation type is known",
            "all sector types are classified",
        ],
    ))

    # Inventory marker
    ns.record_derivation(
        derivation_id="constraint_evolution_split_marker",
        inputs=[],
        output=sp.Symbol("constraint_evolution_map_established"),
        method="constraint_evolution_split_inventory",
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
                 "A_constraint and h_ij^TT have strong reduced support")
        out.line(f"partial: {n_partial}", StatusMark.DEFER,
                 "A_rad, kappa, W_i partial only")
        out.line(f"missing: {n_missing}", StatusMark.FAIL,
                 "gauge sector and conservation identities missing")
        out.line("sector split map provisional", StatusMark.DEFER,
                 "pending gauge and conservation derivations")

    with out.unresolved_obligations():
        out.line("derive A_rad suppression mechanism for split", StatusMark.OBLIGATION,
                 "open proof obligation recorded")
        out.line("derive kappa source and exterior suppression", StatusMark.OBLIGATION,
                 "open proof obligation recorded")
        out.line("derive W_i equation type", StatusMark.OBLIGATION,
                 "open proof obligation recorded")
        out.line("derive gauge sector variables and transformations", StatusMark.OBLIGATION,
                 "open proof obligation recorded")
        out.line("derive conservation identity for split", StatusMark.OBLIGATION,
                 "open proof obligation recorded")

    out.print_summary()


if __name__ == "__main__":
    main()
