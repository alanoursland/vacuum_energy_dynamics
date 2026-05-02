# Candidate conservation identity requirements
#
# Purpose
# -------
# The diagnostics study identified conservation/source compatibility as a
# missing blocker.
#
# A parent theory cannot assign sources independently by hand:
#
#   A_constraint <- mass density
#   kappa        <- pressure/stress/trace candidate
#   W_i          <- mass current/angular momentum
#   h_ij^TT      <- trace-free quadrupole derivatives
#
# These source assignments must be compatible with conservation identities.
#
# This script inventories required conservation/Bianchi-like identities and
# classifies current support.
#
# Status categories:
#
#   SATISFIED_REDUCED
#   PARTIAL
#   MISSING
#   RISK
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/08_covariant_parent_structure/
#   or:
#   scripts_v3/candidate_conservation_identity_requirements.py

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
class ConservationRequirement:
    name: str
    status: str
    current_support: str
    parent_must_supply: str
    risk_if_missing: str


def print_req(req: ConservationRequirement) -> None:
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
    header("Case 0: Conservation identity requirements problem")

    print("Problem:")
    print()
    print("  Sector sources cannot be independent hand assignments.")
    print()
    print("Need identities tying together:")
    print()
    print("  mass density")
    print("  mass current")
    print("  pressure/stress/trace")
    print("  quadrupole moments")
    print("  field constraints/evolution")
    print()
    print("A parent theory needs Bianchi-like or continuity-like compatibility.")

    status_line("conservation identity problem posed", "SATISFIED_REDUCED")


# =============================================================================
# Case 1: Build requirements
# =============================================================================

def build_requirements() -> List[ConservationRequirement]:
    return [
        ConservationRequirement(
            name="C1: Mass continuity for scalar source",
            status="PARTIAL",
            current_support=(
                "Scalar A_constraint uses mass density rho or total mass M. "
                "Binary guardrails used conserved M."
            ),
            parent_must_supply=(
                "Continuity equation relating mass density and current, e.g. "
                "partial_t rho + div j = 0 in the appropriate limit."
            ),
            risk_if_missing=(
                "A_constraint source could change inconsistently with matter flow."
            ),
        ),
        ConservationRequirement(
            name="C2: Current conservation for W_i",
            status="MISSING",
            current_support=(
                "W_i is assigned to mass current/angular momentum, but no equation "
                "or conservation identity has been derived."
            ),
            parent_must_supply=(
                "Relation between W_i source, mass current, angular momentum, and "
                "continuity identities."
            ),
            risk_if_missing=(
                "Frame-dragging sector could violate source conservation or double-count gauge shift."
            ),
        ),
        ConservationRequirement(
            name="C3: Stress/pressure consistency for kappa",
            status="MISSING",
            current_support=(
                "Kappa is assigned to pressure/stress/trace candidate response."
            ),
            parent_must_supply=(
                "A stress/trace identity showing when kappa is sourced and why it "
                "is suppressed in exterior vacuum."
            ),
            risk_if_missing=(
                "Kappa may be arbitrary or conflict with scalar/tensor sectors."
            ),
        ),
        ConservationRequirement(
            name="C4: Quadrupole source consistency for h_ij^TT",
            status="PARTIAL",
            current_support=(
                "Tensor studies use trace-free quadrupole derivatives and conservation "
                "kills monopole/dipole scalar radiation proxies."
            ),
            parent_must_supply=(
                "Derive quadrupole radiation source from conserved stress-energy or "
                "vacuum-source identities."
            ),
            risk_if_missing=(
                "Quadrupole source may be matched rather than derived."
            ),
        ),
        ConservationRequirement(
            name="C5: Constraint propagation",
            status="MISSING",
            current_support=(
                "A_constraint is treated as elliptic and h_ij^TT as hyperbolic."
            ),
            parent_must_supply=(
                "Show that if constraints hold initially, evolution preserves them."
            ),
            risk_if_missing=(
                "Constraint equations could become inconsistent over time."
            ),
        ),
        ConservationRequirement(
            name="C6: No-source exterior consistency",
            status="PARTIAL",
            current_support=(
                "Exterior scripts set rho=0, kappa suppressed, A_rad controlled, "
                "and h_ij^TT source-free except radiation."
            ),
            parent_must_supply=(
                "A unified vacuum identity defining which sectors may remain active "
                "in source-free regions."
            ),
            risk_if_missing=(
                "Exterior vacuum could contain incompatible leftover sector sources."
            ),
        ),
        ConservationRequirement(
            name="C7: Bianchi-like geometric identity",
            status="MISSING",
            current_support=(
                "No parent geometric identity exists yet."
            ),
            parent_must_supply=(
                "A geometric identity analogous in role to Bianchi conservation, "
                "ensuring source-geometry compatibility."
            ),
            risk_if_missing=(
                "The theory cannot be a covariant parent; sector equations may not close."
            ),
        ),
        ConservationRequirement(
            name="C8: Energy flux balance",
            status="PARTIAL",
            current_support=(
                "Tensor radiation energy-flux scaling was checked at reduced level."
            ),
            parent_must_supply=(
                "Energy balance law connecting source energy loss to tensor radiation "
                "and excluding uncontrolled scalar/vector losses."
            ),
            risk_if_missing=(
                "Radiation sector may not conserve energy or may miss extra channels."
            ),
        ),
    ]


# =============================================================================
# Case 2: Print requirements
# =============================================================================

def case_2_print_requirements(reqs: List[ConservationRequirement]):
    header("Case 2: Conservation requirement inventory")

    for req in reqs:
        print_req(req)


# =============================================================================
# Case 3: Source-sector table
# =============================================================================

def case_3_source_table():
    header("Case 3: Source-sector compatibility table")

    print("| Sector | Source object | Required identity | Status |")
    print("|---|---|---|---|")
    print("| A_constraint | rho / M | mass continuity | PARTIAL |")
    print("| W_i | mass current / angular momentum | current continuity / angular momentum relation | MISSING |")
    print("| kappa | pressure / stress / trace | stress/trace consistency | MISSING |")
    print("| h_ij^TT | Q_ij^TF derivatives | conserved quadrupole source derivation | PARTIAL |")
    print("| constraints | initial data | constraint propagation | MISSING |")
    print("| radiation | energy flux | source energy balance | PARTIAL |")

    status_line("source-sector table stated", "PARTIAL",
                "several identities missing")


# =============================================================================
# Case 4: Status counts
# =============================================================================

def case_4_status_counts(reqs: List[ConservationRequirement]):
    header("Case 4: Status counts")

    counts = {}
    for req in reqs:
        counts[req.status] = counts.get(req.status, 0) + 1

    for status in ["SATISFIED_REDUCED", "PARTIAL", "MISSING", "RISK"]:
        print(f"{status}: {counts.get(status, 0)}")

    if counts.get("MISSING", 0) > 0:
        status_line("conservation identities incomplete", "MISSING",
                    "parent source-geometry compatibility is missing")
    else:
        status_line("conservation identities complete", "SATISFIED_REDUCED")


# =============================================================================
# Case 5: Blocking identities
# =============================================================================

def case_5_blocking_identities(reqs: List[ConservationRequirement]):
    header("Case 5: Blocking identity gaps")

    blocking = [req for req in reqs if req.status == "MISSING"]

    print("Blocking missing identities:")
    for req in blocking:
        print(f"  - {req.name}")

    print()
    print("These must be supplied before claiming a closed parent field equation.")

    status_line("blocking identity gaps identified", "MISSING",
                "source compatibility remains unresolved")


# =============================================================================
# Case 6: Minimal safe policy
# =============================================================================

def case_6_minimal_safe_policy():
    header("Case 6: Minimal safe policy")

    print("Until parent identities exist:")
    print()
    print("1. Treat source couplings as reduced-sector assignments, not final laws.")
    print("2. Do not claim full stress-energy coupling.")
    print("3. Keep A_rad and vector radiation controlled unless energy balance permits them.")
    print("4. Treat tensor quadrupole power scaling as matched/reduced, not derived.")
    print("5. Mark kappa source law as open.")
    print("6. Do not claim covariant closure.")
    print()
    status_line("minimal conservation policy stated", "PARTIAL",
                "safe but incomplete")


# =============================================================================
# Case 7: Next study recommendation
# =============================================================================

def case_7_next_study():
    header("Case 7: Next study recommendation")

    print("Recommended next file:")
    print()
    print("  covariant_parent_structure_summary.md")
    print()
    print("Reason:")
    print("  Group 08 has now identified its main blockers:")
    print("    gauge structure")
    print("    recombination")
    print("    invariant diagnostics")
    print("    conservation identities")
    print()
    print("A summary should close the group and state the parent-theory gap clearly.")
    print()
    print("Alternative:")
    print("  candidate_metric_parent_gap_summary.py")

    status_line("next file selected", "PARTIAL",
                "group 08 is ready for summary unless more depth is desired")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation(reqs: List[ConservationRequirement]):
    header("Final interpretation")

    print("Conservation/source identities are not solved.")
    print()
    print("Partial reduced support exists for:")
    print("  mass continuity assumptions")
    print("  quadrupole source structure")
    print("  tensor radiation energy scaling")
    print()
    print("Missing parent identities include:")
    print("  current/W_i identity")
    print("  kappa stress/trace identity")
    print("  constraint propagation")
    print("  Bianchi-like geometric identity")
    print()
    print("Possible next artifact:")
    print("  candidate_conservation_identity_requirements.md")
    print()
    print("Possible next file:")
    print("  covariant_parent_structure_summary.md")


def main():
    header("Candidate Conservation Identity Requirements")
    case_0_problem_statement()
    reqs = build_requirements()
    case_2_print_requirements(reqs)
    case_3_source_table()
    case_4_status_counts(reqs)
    case_5_blocking_identities(reqs)
    case_6_minimal_safe_policy()
    case_7_next_study()
    final_interpretation(reqs)


if __name__ == "__main__":
    main()
