# Candidate covariant parent requirements
#
# Group:
#   08_covariant_parent_structure
#
# Script type:
#   REQUIREMENTS
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
class Requirement:
    name: str
    status: str
    current_support: str
    parent_must_supply: str


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="sector_bundle_inventory_marker",
        upstream_script_id="08_covariant_parent_structure__candidate_sector_bundle_inventory",
        upstream_derivation_id="sector_bundle_inventory_marker",
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

    return counts


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
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement()
    requirements = build_requirements()
    case_2_print_requirements(requirements)
    counts = case_3_status_counts(requirements)
    case_4_blocking_requirements(requirements)
    case_5_next_study()
    final_interpretation(requirements)

    # --- Record one ProofObligationRecord per MISSING or PARTIAL requirement ---

    ns.record_obligation(ProofObligationRecord(
        obligation_id="satisfy_R2_no_unsuppressed_scalar_radiation",
        script_id=SCRIPT_ID,
        title="R2: Derive scalar radiation suppression mechanism (parent level)",
        status=ObligationStatus.OPEN,
        description=(
            "The parent structure must supply a real suppression mechanism for A_rad: "
            "projection, constraint, damping/absorption, mass gap, relaxation, or "
            "observationally acceptable weak coupling."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="satisfy_R3_moving_wells_no_breathing_waves",
        script_id=SCRIPT_ID,
        title="R3: Derive retarded/constraint concept for moving wells without scalar breathing",
        status=ObligationStatus.OPEN,
        description=(
            "The parent must show how moving sources carry moving scalar constraint "
            "configurations without producing forbidden long-range scalar breathing radiation."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="satisfy_R4_kappa_source_law",
        script_id=SCRIPT_ID,
        title="R4: Derive kappa source law from parent structure",
        status=ObligationStatus.OPEN,
        description=(
            "Supply a derivation of the kappa source from stress/pressure/trace matter "
            "content and a derivation of exterior suppression."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="satisfy_R5_vector_field_equation",
        script_id=SCRIPT_ID,
        title="R5: Derive W_i field equation and vector radiation constraints",
        status=ObligationStatus.OPEN,
        description=(
            "Supply the W_i field equation from mass current/angular momentum coupling "
            "and determine vector radiation safety."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="satisfy_R7_source_coupling_consistency",
        script_id=SCRIPT_ID,
        title="R7: Derive one unified source coupling rule for all sectors",
        status=ObligationStatus.OPEN,
        description=(
            "The parent must supply one stress-energy/vacuum coupling rule that yields "
            "all sector sources in the correct limits."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="satisfy_R8_gauge_structure",
        script_id=SCRIPT_ID,
        title="R8: Derive gauge structure from parent theory",
        status=ObligationStatus.OPEN,
        description=(
            "The parent must supply gauge freedoms, gauge-invariant diagnostics, and "
            "the mapping between coordinate choices."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="satisfy_R9_constraint_evolution_split",
        script_id=SCRIPT_ID,
        title="R9: Derive principled constraint/evolution split from parent",
        status=ObligationStatus.OPEN,
        description=(
            "The parent must supply a principled decomposition into constraints and "
            "evolution equations for all sectors."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="satisfy_R10_metric_recombination",
        script_id=SCRIPT_ID,
        title="R10: Derive metric/geometric recombination from parent structure",
        status=ObligationStatus.OPEN,
        description=(
            "A single metric/vacuum structure from which A, kappa, W_i, and h_ij^TT "
            "arise as projections or gauge-fixed components must be derived."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="satisfy_R11_conservation_identities",
        script_id=SCRIPT_ID,
        title="R11: Derive Bianchi-like or continuity conservation identities",
        status=ObligationStatus.OPEN,
        description=(
            "The parent must supply conservation identities ensuring compatible source "
            "conservation across all sectors."
        ),
    ))

    # --- Governance claims ---

    ns.record_claim(ClaimRecord(
        claim_id="covariant_parent_not_yet_established",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "The reduced sector program is coherent as an architecture but does not "
            "yet constitute a covariant parent theory. R8 (gauge), R10 (recombination), "
            "and R11 (conservation identities) are missing. Do not claim covariant "
            "closure until these are supplied."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="no_gr_equivalence_claim",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "R12 risk: The program recovers GR-like reduced structures but has not "
            "derived Einstein equations. Claims of GR equivalence must not be made "
            "until a clear statement of what is recovered, matched, and unresolved is supplied."
        ),
    ))

    # --- Branch decision ---

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_full_covariant_parent_claim",
        script_id=SCRIPT_ID,
        branch_id="full_covariant_parent_theory",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "satisfy_R8_gauge_structure",
            "satisfy_R10_metric_recombination",
            "satisfy_R11_conservation_identities",
        ],
        description=(
            "The full covariant parent theory claim is deferred. R8, R10, and R11 "
            "are missing. The reduced program may proceed but must not claim covariant "
            "closure yet."
        ),
    ))

    # Inventory marker
    ns.record_derivation(
        derivation_id="covariant_parent_requirements_marker",
        inputs=[],
        output=sp.Symbol("covariant_parent_requirements_classified"),
        method="covariant_parent_requirement_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )

    ns.write_run_metadata()

    n_missing = counts.get("MISSING", 0)
    n_risk = counts.get("RISK", 0)
    n_partial = counts.get("PARTIAL", 0)
    n_satisfied = counts.get("SATISFIED_REDUCED", 0)

    with out.governance_assessments():
        out.line(f"satisfied reduced: {n_satisfied}", StatusMark.PASS,
                 "strong reduced support for R1, R6")
        out.line(f"partial: {n_partial}", StatusMark.DEFER,
                 "R2, R3, R4, R5, R7, R9 have support but no parent derivation")
        out.line(f"missing: {n_missing}", StatusMark.FAIL,
                 "R8 gauge, R10 recombination, R11 conservation identities")
        out.line(f"risk: {n_risk}", StatusMark.FAIL,
                 "R12 GR overclaim risk")
        out.line("covariant parent not yet established", StatusMark.DEFER,
                 "deferred pending R8, R10, R11")

    with out.unresolved_obligations():
        for req in build_requirements():
            if req.status in ("MISSING", "PARTIAL"):
                out.line(f"satisfy {req.name}", StatusMark.OBLIGATION,
                         "open proof obligation recorded")


if __name__ == "__main__":
    main()
