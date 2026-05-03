# Candidate source coupling from vacuum exchange
#
# Purpose
# -------
# The vacuum-substance continuity identity proposed:
#
#   partial_t q_v + div J_v = Sigma_exchange + Sigma_creation - Gamma_relax
#
# This script asks whether the sector source couplings can be interpreted as
# projections of Sigma_exchange and related vacuum-balance terms:
#
#   density rho                  -> A_constraint scalar source
#   current j_i = rho v_i        -> W_i vector source
#   stress/pressure/trace        -> kappa trace/interior source
#   time-varying quadrupole      -> h_ij^TT tensor source
#   relaxation term              -> A_rad suppression
#   creation term                -> special nonconservative regimes
#
# The goal is to classify each coupling as:
#
#   DERIVED_REDUCED
#   CONSTRAINED_BY_IDENTITY
#   HAND_ASSIGNED
#   MISSING
#   RISK
#
# This is not a covariant source law. It is a source-coupling audit from the
# vacuum-exchange ontology.
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/09_vacuum_identity_and_source_coupling/
#   or:
#   scripts_v3/candidate_source_coupling_from_vacuum_exchange.py

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
        "DERIVED_REDUCED": "PASS",
        "CONSTRAINED_BY_IDENTITY": "WARN",
        "HAND_ASSIGNED": "WARN",
        "MISSING": "FAIL",
        "RISK": "WARN",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class SourceCoupling:
    sector: str
    source_object: str
    exchange_projection: str
    status: str
    current_support: str
    missing_piece: str


def print_coupling(c: SourceCoupling) -> None:
    print()
    print("-" * 100)
    print(c.sector)
    print("-" * 100)
    status_line(c.sector, c.status)
    print(f"Source object: {c.source_object}")
    print(f"Exchange projection: {c.exchange_projection}")
    print(f"Current support: {c.current_support}")
    print(f"Missing piece: {c.missing_piece}")


# =============================================================================
# Case 0: Problem statement
# =============================================================================

def case_0_problem_statement():
    header("Case 0: Source coupling from vacuum exchange problem")

    print("Question:")
    print()
    print("  Can the sector sources be interpreted as projections of one")
    print("  vacuum-exchange balance law?")
    print()
    print("Candidate balance:")
    print()
    print("  partial_t q_v + div J_v = Sigma_exchange + Sigma_creation - Gamma_relax")
    print()
    print("Goal:")
    print()
    print("  reduce hand-assigned couplings and identify what remains missing.")

    status_line("source coupling audit posed", "CONSTRAINED_BY_IDENTITY")


# =============================================================================
# Case 1: Build couplings
# =============================================================================

def build_couplings() -> List[SourceCoupling]:
    return [
        SourceCoupling(
            sector="A_constraint scalar source",
            source_object="mass density rho / enclosed mass M",
            exchange_projection="scalar part of Sigma_exchange",
            status="DERIVED_REDUCED",
            current_support=(
                "Areal flux law gives Delta_areal A = 8*pi*G*rho/c^2 and "
                "recovers static exterior A = 1 - 2GM/(c^2 r)."
            ),
            missing_piece=(
                "Derive the 8*pi*G/c^2 coefficient from vacuum exchange ontology, "
                "not just reduced flux normalization."
            ),
        ),
        SourceCoupling(
            sector="W_i vector/current source",
            source_object="mass current j_i = rho v_i / angular momentum",
            exchange_projection="vector/current part of vacuum transport J_v",
            status="CONSTRAINED_BY_IDENTITY",
            current_support=(
                "Continuity bookkeeping points from density to current, suggesting "
                "W_i should couple to transport rather than be assigned only by analogy."
            ),
            missing_piece=(
                "Derive W_i field equation, coefficient, gauge behavior, and frame-dragging observable."
            ),
        ),
        SourceCoupling(
            sector="kappa trace/interior source",
            source_object="pressure, stress trace, volume exchange candidate",
            exchange_projection="trace/compressive part of exchange or relaxation",
            status="MISSING",
            current_support=(
                "Kappa is interpreted as trace/interior response, but no source identity exists."
            ),
            missing_piece=(
                "Derive whether kappa couples to pressure, stress trace, density gradients, "
                "relaxation, or creation-like terms."
            ),
        ),
        SourceCoupling(
            sector="h_ij^TT tensor source",
            source_object="time-varying trace-free quadrupole derivatives",
            exchange_projection="trace-free shear/tensor part of conserved source motion",
            status="HAND_ASSIGNED",
            current_support=(
                "Tensor studies established TT basis, quadrupole projection, and target scaling."
            ),
            missing_piece=(
                "Derive quadrupole coupling and 2G/c^4 normalization from the exchange identity "
                "or a parent action."
            ),
        ),
        SourceCoupling(
            sector="A_rad scalar radiative hazard",
            source_object="scalar breathing perturbation",
            exchange_projection="relaxation/deviation term Gamma_relax",
            status="CONSTRAINED_BY_IDENTITY",
            current_support=(
                "Relaxation term can represent vacuum absorption of scalar radiative perturbations."
            ),
            missing_piece=(
                "Show relaxation suppresses A_rad without erasing A_constraint or violating energy balance."
            ),
        ),
        SourceCoupling(
            sector="Creation regime",
            source_object="Sigma_creation",
            exchange_projection="nonconservative vacuum amount change",
            status="RISK",
            current_support=(
                "Creation is classified as special-regime behavior, not ordinary exterior gravity."
            ),
            missing_piece=(
                "Define when creation is allowed and prevent it from becoming a free knob."
            ),
        ),
    ]


# =============================================================================
# Case 2: Print couplings
# =============================================================================

def case_2_print_couplings(couplings: List[SourceCoupling]):
    header("Case 2: Source coupling inventory")

    for c in couplings:
        print_coupling(c)


# =============================================================================
# Case 3: Coupling table
# =============================================================================

def case_3_coupling_table(couplings: List[SourceCoupling]):
    header("Case 3: Coupling status table")

    print("| Sector | Source object | Status |")
    print("|---|---|---|")
    for c in couplings:
        print(f"| {c.sector} | {c.source_object} | {c.status} |")

    status_line("coupling table produced", "CONSTRAINED_BY_IDENTITY",
                "several couplings remain missing or hand-assigned")


# =============================================================================
# Case 4: Status counts
# =============================================================================

def case_4_status_counts(couplings: List[SourceCoupling]):
    header("Case 4: Status counts")

    counts = {}
    for c in couplings:
        counts[c.status] = counts.get(c.status, 0) + 1

    for status in ["DERIVED_REDUCED", "CONSTRAINED_BY_IDENTITY", "HAND_ASSIGNED", "MISSING", "RISK"]:
        print(f"{status}: {counts.get(status, 0)}")

    if counts.get("MISSING", 0) or counts.get("HAND_ASSIGNED", 0) or counts.get("RISK", 0):
        status_line("source coupling incomplete", "MISSING",
                    "some sector sources are not derived from ontology")
    else:
        status_line("source coupling complete", "DERIVED_REDUCED")


# =============================================================================
# Case 5: Ontology work versus GR matching
# =============================================================================

def case_5_ontology_vs_matching():
    header("Case 5: Ontology work versus GR matching")

    print("Ontology is doing work when:")
    print()
    print("  density naturally sources scalar exchange")
    print("  current naturally sources vector transport")
    print("  relaxation naturally suppresses radiative scalar deviations")
    print()
    print("Ontology is not yet doing enough work when:")
    print()
    print("  tensor coefficient is set to 2G/c^4 by target matching")
    print("  W_i coefficient is chosen to match frame dragging")
    print("  kappa source is left as pressure/stress/trace placeholder")
    print("  creation is invoked to solve mismatches")
    print()
    status_line("ontology-vs-matching boundary stated", "RISK",
                "future scripts should reduce matching by deriving couplings")


# =============================================================================
# Case 6: Next tests
# =============================================================================

def case_6_next_tests():
    header("Case 6: Next tests")

    print("Most useful next tests:")
    print()
    print("1. candidate_vector_current_from_continuity.py")
    print("   Derive or fail to derive W_i source form from current continuity.")
    print()
    print("2. candidate_kappa_source_law_from_trace_exchange.py")
    print("   Force kappa into one primary source role.")
    print()
    print("3. candidate_tensor_source_from_exchange_identity.py")
    print("   Ask whether quadrupole tensor coupling can follow from conserved exchange.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_vector_current_from_continuity.py")
    print()
    print("Reason:")
    print("  W_i is the nearest sector where continuity gives a concrete new source object: j_i.")

    status_line("next test selected", "CONSTRAINED_BY_IDENTITY",
                "vector current is the most direct identity-derived next step")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation(couplings: List[SourceCoupling]):
    header("Final interpretation")

    print("The vacuum-exchange picture begins to constrain source coupling:")
    print()
    print("  density -> A_constraint")
    print("  current -> W_i")
    print("  relaxation -> A_rad suppression")
    print()
    print("But major pieces remain underived:")
    print()
    print("  kappa source")
    print("  tensor coupling coefficient")
    print("  W_i field equation and coefficient")
    print("  closure identity")
    print()
    print("Possible next artifact:")
    print("  candidate_source_coupling_from_vacuum_exchange.md")
    print()
    print("Possible next script:")
    print("  candidate_vector_current_from_continuity.py")


def main():
    header("Candidate Source Coupling From Vacuum Exchange")
    case_0_problem_statement()
    couplings = build_couplings()
    case_2_print_couplings(couplings)
    case_3_coupling_table(couplings)
    case_4_status_counts(couplings)
    case_5_ontology_vs_matching()
    case_6_next_tests()
    final_interpretation(couplings)


if __name__ == "__main__":
    main()
