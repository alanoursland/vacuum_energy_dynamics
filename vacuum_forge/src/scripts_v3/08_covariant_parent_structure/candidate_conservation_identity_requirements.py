# Candidate conservation identity requirements
#
# Group:
#   08_covariant_parent_structure
#
# Script type:
#   REQUIREMENTS
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
    HandoffImportRecord,
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
class ConservationRequirement:
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
        dependency_id="gauge_invariant_diagnostics_marker",
        upstream_script_id="08_covariant_parent_structure__candidate_gauge_invariant_diagnostics",
        upstream_derivation_id="gauge_invariant_diagnostics_marker",
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

    return counts


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
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement()
    reqs = build_requirements()
    case_2_print_requirements(reqs)
    case_3_source_table()
    counts = case_4_status_counts(reqs)
    case_5_blocking_identities(reqs)
    case_6_minimal_safe_policy()
    case_7_next_study()
    final_interpretation(reqs)

    # --- ProofObligationRecord per MISSING or PARTIAL requirement ---

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_C1_mass_continuity_equation",
        script_id=SCRIPT_ID,
        title="C1: Derive mass continuity equation for scalar sector source",
        status=ObligationStatus.OPEN,
        description=(
            "Supply a continuity equation relating mass density and current "
            "in the appropriate limit for A_constraint source coupling."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_C2_current_conservation_for_W_i",
        script_id=SCRIPT_ID,
        title="C2: Derive current conservation identity for W_i source",
        status=ObligationStatus.OPEN,
        description=(
            "Derive the relation between W_i source, mass current, angular momentum, "
            "and continuity identities so that the vector sector is compatible with "
            "source conservation."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_C3_stress_trace_identity_for_kappa",
        script_id=SCRIPT_ID,
        title="C3: Derive stress/trace conservation identity for kappa source",
        status=ObligationStatus.OPEN,
        description=(
            "Supply a stress/trace identity showing when kappa is sourced and why it "
            "vanishes in exterior vacuum."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_C4_quadrupole_source_from_conserved_stress_energy",
        script_id=SCRIPT_ID,
        title="C4: Derive quadrupole source for h_ij^TT from conserved stress-energy",
        status=ObligationStatus.OPEN,
        description=(
            "Derive the h_ij^TT quadrupole radiation source from conserved stress-energy "
            "or vacuum-source identities rather than matching."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_C5_constraint_propagation",
        script_id=SCRIPT_ID,
        title="C5: Derive constraint propagation (constraints preserved by evolution)",
        status=ObligationStatus.OPEN,
        description=(
            "Show that if the constraint equations hold on an initial slice, they "
            "remain satisfied under the evolution equations."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_C6_vacuum_identity_for_exterior",
        script_id=SCRIPT_ID,
        title="C6: Derive vacuum identity defining which sectors are active in exterior",
        status=ObligationStatus.OPEN,
        description=(
            "Supply a unified vacuum identity stating which sectors may remain active "
            "in source-free regions and which must vanish."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_C7_bianchi_like_geometric_identity",
        script_id=SCRIPT_ID,
        title="C7: Derive Bianchi-like geometric identity for covariant parent",
        status=ObligationStatus.OPEN,
        description=(
            "Supply a geometric identity analogous in role to Bianchi conservation, "
            "ensuring that sector source-geometry coupling is consistent and that "
            "the sector equations can close."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_C8_energy_flux_balance_law",
        script_id=SCRIPT_ID,
        title="C8: Derive energy flux balance law for radiation sector",
        status=ObligationStatus.OPEN,
        description=(
            "Supply an energy balance law connecting source energy loss to tensor "
            "radiation flux and explicitly excluding uncontrolled scalar/vector energy losses."
        ),
    ))

    # --- Governance claims ---

    ns.record_claim(ClaimRecord(
        claim_id="source_couplings_are_reduced_assignments_not_final_laws",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Current source couplings (A_constraint <- rho, W_i <- mass current, "
            "kappa <- stress/trace, h_ij^TT <- quadrupole) are reduced-sector assignments, "
            "not final parent-theory laws. They must not be claimed as derived until "
            "conservation identities C1-C8 are supplied."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="bianchi_identity_required_for_covariant_closure",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "C7 (Bianchi-like geometric identity) is a prerequisite for claiming "
            "covariant closure of the parent field equations. Without it, sector "
            "equations may not close consistently."
        ),
    ))

    # --- Branch decision ---

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_covariant_closure_claim",
        script_id=SCRIPT_ID,
        branch_id="covariant_closure_of_parent_field_equations",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "derive_C7_bianchi_like_geometric_identity",
            "derive_C2_current_conservation_for_W_i",
            "derive_C3_stress_trace_identity_for_kappa",
            "derive_C5_constraint_propagation",
        ],
        description=(
            "Covariant closure of the parent field equations is deferred. "
            "C2 (W_i), C3 (kappa), C5 (constraint propagation), and C7 (Bianchi) "
            "are missing. The reduced program may proceed but must not claim covariant closure."
        ),
    ))

    # --- Routes ---

    ns.record_route(RouteRecord(
        route_id="conservation_identity_completion_route",
        script_id=SCRIPT_ID,
        name="Conservation identity completion route for covariant parent",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[
            "derive_C7_bianchi_like_geometric_identity",
            "derive_C2_current_conservation_for_W_i",
            "derive_C3_stress_trace_identity_for_kappa",
            "derive_C5_constraint_propagation",
        ],
        activation_conditions=[
            "Bianchi-like geometric identity is derived",
            "current/W_i continuity identity is derived",
            "kappa stress/trace identity is derived",
            "constraint propagation is verified",
        ],
    ))

    # --- Group 08 handoff import ---
    # This is the last script in group 08; record what downstream groups may import.

    ns.record_handoff_import(HandoffImportRecord(
        handoff_id="group_08_covariant_parent_handoff",
        script_id=SCRIPT_ID,
        imported_as=RecordKind.SUMMARY_CLAIM,
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        imported_record_refs=[
            "obligation:derive_C7_bianchi_like_geometric_identity",
            "obligation:derive_C2_current_conservation_for_W_i",
            "obligation:derive_C3_stress_trace_identity_for_kappa",
            "obligation:derive_C5_constraint_propagation",
            "obligation:derive_G4_W_i_gauge_transformation",
            "obligation:derive_G7_gauge_invariant_observable_set",
            "obligation:derive_G8_coordinate_recombination_map",
            "obligation:satisfy_R8_gauge_structure",
            "obligation:satisfy_R10_metric_recombination",
            "obligation:satisfy_R11_conservation_identities",
            "claim:covariant_parent_not_yet_established",
            "claim:sector_split_map_partial",
            "claim:recombination_map_is_schematic_not_derivation",
            "claim:safe_diagnostic_policy",
            "claim:source_couplings_are_reduced_assignments_not_final_laws",
            "claim:bianchi_identity_required_for_covariant_closure",
            "route:conservation_identity_completion_route",
            "route:gauge_structure_completion_route",
            "route:metric_recombination_completion_route",
        ],
        description=(
            "Group 08 handoff to downstream groups. "
            "The reduced sector program is coherent but not yet a covariant parent. "
            "Key open obligations: gauge structure (G4, G7, G8), conservation identities (C2, C3, C5, C7), "
            "and metric recombination. "
            "Key provisional claims: sector split map is partial; recombination map is schematic. "
            "Key routes: conservation identity completion, gauge structure completion, recombination completion. "
            "Downstream groups must not assume covariant closure, GR equivalence, or licensed route status "
            "for anything listed here as deferred or open."
        ),
    ))

    # Inventory marker
    ns.record_derivation(
        derivation_id="conservation_identity_requirements_marker",
        inputs=[],
        output=sp.Symbol("conservation_identity_blockers_identified"),
        method="conservation_identity_requirement_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )

    ns.write_run_metadata()

    n_missing = counts.get("MISSING", 0)
    n_partial = counts.get("PARTIAL", 0)

    with out.governance_assessments():
        out.line(f"partial: {n_partial}", StatusMark.DEFER,
                 "C1 mass continuity, C4 quadrupole source, C6 vacuum identity, C8 energy flux")
        out.line(f"missing: {n_missing}", StatusMark.FAIL,
                 "C2 W_i current, C3 kappa stress/trace, C5 constraint propagation, C7 Bianchi")
        out.line("source couplings are reduced assignments (policy)", StatusMark.FAIL,
                 "must not claim derived until C1-C8 supplied")
        out.line("Bianchi identity required for covariant closure (policy)", StatusMark.FAIL,
                 "C7 is a prerequisite for covariant closure")
        out.line("covariant closure deferred", StatusMark.DEFER,
                 "deferred pending C2, C3, C5, C7")
        out.line("group 08 handoff recorded", StatusMark.PASS,
                 "handoff import record recorded for downstream groups")

    with out.unresolved_obligations():
        for req in build_requirements():
            if req.status in ("MISSING", "PARTIAL"):
                out.line(f"derive {req.name}", StatusMark.OBLIGATION,
                         "open proof obligation recorded")

    out.print_summary()


if __name__ == "__main__":
    main()
