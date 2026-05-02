# Candidate covariant parent requirements
#
# Purpose
# -------
# The sector bundle inventory organized the reduced theory into:
#
#   A_constraint, A_rad, kappa, W_i, h_ij^TT
#
# This script turns the needed parent structure into explicit requirements.
#
# Unlike many earlier candidate scripts, this one is intentionally stricter:
# it distinguishes:
#
#   SATISFIED_REDUCED  -> demonstrated in reduced scripts
#   PARTIAL            -> partially supported but not derived
#   MISSING            -> required but not yet supplied
#   RISK               -> possible contradiction or danger
#
# The goal is to avoid confusing internal consistency with proof.
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/08_covariant_parent_structure/
#   or:
#   scripts_v3/candidate_covariant_parent_requirements.py

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
class Requirement:
    name: str
    status: str
    current_support: str
    parent_must_supply: str


def print_requirement(req: Requirement) -> None:
    print()
    print("-" * 100)
    print(req.name)
    print("-" * 100)
    status_line(req.name, req.status)
    print(f"Current support: {req.current_support}")
    print(f"Parent must supply: {req.parent_must_supply}")


# =============================================================================
# Case 0: Problem statement
# =============================================================================

def case_0_problem_statement():
    header("Case 0: Covariant parent requirements problem")

    print("Group 08 asks:")
    print()
    print("  Can the reduced sector bundle come from one deeper geometric/covariant")
    print("  parent structure?")
    print()
    print("This script does not try to pass everything.")
    print("It classifies what is satisfied, partial, missing, or risky.")

    status_line("requirements framework posed", "SATISFIED_REDUCED")


# =============================================================================
# Case 1: Build requirements
# =============================================================================

def build_requirements() -> List[Requirement]:
    return [
        Requirement(
            name="R1: Static scalar mass response",
            status="SATISFIED_REDUCED",
            current_support=(
                "A_constraint = 1 - 2GM/(c^2 r) solves source-free exterior "
                "Poisson/Laplace equation and recovers the static scalar channel."
            ),
            parent_must_supply=(
                "A geometric reason why the scalar mass response appears as a "
                "constraint-like lapse/scalar sector."
            ),
        ),
        Requirement(
            name="R2: No unsuppressed scalar radiation",
            status="PARTIAL",
            current_support=(
                "A_rad is explicitly classified as absent or controlled. "
                "Several suppression mechanisms are listed."
            ),
            parent_must_supply=(
                "A real mechanism: projection, constraint, damping/absorption, "
                "mass gap, relaxation, or observationally acceptable weak coupling."
            ),
        ),
        Requirement(
            name="R3: Moving wells without scalar breathing waves",
            status="PARTIAL",
            current_support=(
                "Inventory distinguishes translated scalar wells from free scalar "
                "waves."
            ),
            parent_must_supply=(
                "A retarded/constraint solution concept showing how moving sources "
                "carry moving scalar configurations without producing forbidden "
                "long-range scalar breathing radiation."
            ),
        ),
        Requirement(
            name="R4: Kappa interior/trace response",
            status="PARTIAL",
            current_support=(
                "Kappa is modeled as trace/interior response with exterior "
                "suppression/relaxation."
            ),
            parent_must_supply=(
                "Source law for kappa from stress/pressure/trace matter content and "
                "a derivation of exterior suppression."
            ),
        ),
        Requirement(
            name="R5: Vector current/frame-dragging sector",
            status="PARTIAL",
            current_support=(
                "W_i is identified as the shift/current sector needed for "
                "frame dragging."
            ),
            parent_must_supply=(
                "Field equation, source coupling to mass current/angular momentum, "
                "and constraints on vector radiation."
            ),
        ),
        Requirement(
            name="R6: Tensor TT radiation sector",
            status="SATISFIED_REDUCED",
            current_support=(
                "h_ij^TT basis, wave equation, quadrupole source projection, "
                "amplitude scaling, and action-stiffness toy have been checked "
                "at reduced level."
            ),
            parent_must_supply=(
                "Covariant derivation of TT sector, gauge conditions, coupling, "
                "energy flux, and radiation reaction."
            ),
        ),
        Requirement(
            name="R7: Source coupling consistency",
            status="PARTIAL",
            current_support=(
                "Scalar mass, vector current, tensor quadrupole, and possible "
                "kappa trace sources have been assigned."
            ),
            parent_must_supply=(
                "One stress-energy/vacuum coupling rule that yields all sector "
                "sources in the correct limits."
            ),
        ),
        Requirement(
            name="R8: Gauge structure",
            status="MISSING",
            current_support=(
                "Reduced scripts use gauges such as areal/static/TT but do not "
                "derive full gauge transformations."
            ),
            parent_must_supply=(
                "Gauge freedoms, gauge-invariant diagnostics, and mapping between "
                "coordinate choices."
            ),
        ),
        Requirement(
            name="R9: Constraint/evolution split",
            status="PARTIAL",
            current_support=(
                "A_constraint is classified as elliptic, h_ij^TT as hyperbolic, "
                "and other sectors as TBD."
            ),
            parent_must_supply=(
                "A principled decomposition into constraints and evolution equations."
            ),
        ),
        Requirement(
            name="R10: Metric/geometric recombination",
            status="MISSING",
            current_support=(
                "Sectors are mapped informally to g_tt, g_ti, trace, and TT spatial "
                "parts."
            ),
            parent_must_supply=(
                "A single metric/vacuum structure from which A, kappa, W_i, and "
                "h_ij^TT arise as projections or gauge-fixed components."
            ),
        ),
        Requirement(
            name="R11: Conservation identities",
            status="MISSING",
            current_support=(
                "Reduced scripts use conservation ideas for monopole/dipole and "
                "quadrupole radiation but do not derive parent identities."
            ),
            parent_must_supply=(
                "Bianchi-like or continuity identities ensuring compatible source "
                "conservation across sectors."
            ),
        ),
        Requirement(
            name="R12: Avoid overclaiming GR equivalence",
            status="RISK",
            current_support=(
                "The program recovers several GR-like reduced structures but has "
                "not derived Einstein equations."
            ),
            parent_must_supply=(
                "Clear statement of what is recovered, what is matched, and what is "
                "not yet derived."
            ),
        ),
    ]


# =============================================================================
# Case 2: Print requirements
# =============================================================================

def case_2_print_requirements(requirements: List[Requirement]):
    header("Case 2: Requirement inventory")

    for req in requirements:
        print_requirement(req)


# =============================================================================
# Case 3: Status counts
# =============================================================================

def case_3_status_counts(requirements: List[Requirement]):
    header("Case 3: Status counts")

    counts = {}
    for req in requirements:
        counts[req.status] = counts.get(req.status, 0) + 1

    for status in ["SATISFIED_REDUCED", "PARTIAL", "MISSING", "RISK"]:
        print(f"{status}: {counts.get(status, 0)}")

    print()
    print("Interpretation:")
    print("  SATISFIED_REDUCED means the reduced program has a working toy/result.")
    print("  PARTIAL means there is support but no parent derivation.")
    print("  MISSING means the parent structure has not been supplied.")
    print("  RISK means overclaim or contradiction danger.")

    # This script should not pretend everything is proven.
    if counts.get("MISSING", 0) > 0:
        status_line("parent theory still incomplete", "MISSING",
                    "some required structures are not yet supplied")
    else:
        status_line("parent theory requirements all supplied", "SATISFIED_REDUCED")


# =============================================================================
# Case 4: Blocking requirements
# =============================================================================

def case_4_blocking_requirements(requirements: List[Requirement]):
    header("Case 4: Blocking requirements")

    blocking = [req for req in requirements if req.status in ("MISSING", "RISK")]

    if not blocking:
        print("No blocking requirements.")
        status_line("blocking requirements", "SATISFIED_REDUCED")
        return

    print("Blocking or high-risk requirements:")
    for req in blocking:
        print(f"  - {req.name}: {req.status}")

    print()
    print("These should be handled before claiming a full covariant parent.")

    status_line("blocking requirements identified", "RISK",
                "do not claim full theory yet")


# =============================================================================
# Case 5: Next study recommendation
# =============================================================================

def case_5_next_study():
    header("Case 5: Next study recommendation")

    print("Most important missing piece:")
    print()
    print("  gauge structure and metric/geometric recombination")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_constraint_vs_evolution_split.py")
    print()
    print("Reason:")
    print("  Before gauge/recombination can be solved, we need a clean split between")
    print("  constraint sectors and evolution sectors.")
    print()
    print("Alternative:")
    print("  candidate_gauge_structure_requirements.py")

    status_line("next study selected", "PARTIAL",
                "constraint/evolution split is the next organizing layer")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation(requirements: List[Requirement]):
    header("Final interpretation")

    missing = [req.name for req in requirements if req.status == "MISSING"]
    partial = [req.name for req in requirements if req.status == "PARTIAL"]

    print("The reduced sector program is coherent but not yet a covariant parent.")
    print()
    print("Strong reduced support exists for:")
    print("  A_constraint static scalar response")
    print("  h_ij^TT tensor radiation")
    print()
    print("Partial support exists for:")
    for name in partial:
        print(f"  - {name}")
    print()
    print("Missing parent structures include:")
    for name in missing:
        print(f"  - {name}")
    print()
    print("Possible next artifact:")
    print("  candidate_covariant_parent_requirements.md")
    print()
    print("Possible next script:")
    print("  candidate_constraint_vs_evolution_split.py")


def main():
    header("Candidate Covariant Parent Requirements")
    case_0_problem_statement()
    requirements = build_requirements()
    case_2_print_requirements(requirements)
    case_3_status_counts(requirements)
    case_4_blocking_requirements(requirements)
    case_5_next_study()
    final_interpretation(requirements)


if __name__ == "__main__":
    main()
