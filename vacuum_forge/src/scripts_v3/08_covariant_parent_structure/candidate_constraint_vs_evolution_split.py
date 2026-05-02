# Candidate constraint vs evolution split
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
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/08_covariant_parent_structure/
#   or:
#   scripts_v3/candidate_constraint_vs_evolution_split.py

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
class SectorSplit:
    sector: str
    variable: str
    preferred_type: str
    status: str
    reason: str
    parent_requirement: str


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
    print()
    status_line("consistency risks identified", "RISK",
                "these risks must be handled by parent structure")


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
    case_0_problem_statement()
    splits = build_splits()
    case_2_print_splits(splits)
    case_3_table(splits)
    case_4_status_counts(splits)
    case_5_consistency_risks()
    case_6_parent_target_split()
    case_7_next_study()
    final_interpretation(splits)


if __name__ == "__main__":
    main()
