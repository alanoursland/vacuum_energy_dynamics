# Group:
#   14_kappa_zeta_map_and_projectors
#
# Script type:
#   INVENTORY
#
# Candidate volume current definition for u_vac
#
# Purpose
# -------
# The vacuum rest frame definition audit found:
#
#   u_vac^mu is not yet defined.
#
# Best surviving candidate:
#
#   u_vac^mu = J_V^mu / sqrt(-J_V^2)
#
# But this only works if J_V is a real vacuum-volume current.
#
# This script attempts to define J_V. If J_V remains unnamed, Group 14 should
# close with u_vac/J_V as the surviving bottleneck.
#
# It is not a derivation.

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
    ReasonCode,
    RecordKind,
    RouteRecord,
    ScriptOutput,
    StatusMark,
)


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"



def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


@dataclass
class VolumeCurrentEntry:
    name: str
    current: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[VolumeCurrentEntry]:
    return [
        VolumeCurrentEntry(
            name="JV1: volume-current theorem target",
            current="J_V^mu is a real vacuum-volume flux current; u_vac^mu = J_V^mu / sqrt(-J_V^2)",
            role="core definition target for vacuum rest frame",
            allowed_if="J_V is defined before recovery checks and is timelike where used",
            forbidden_if="J_V is named only to create u_vac",
            status="THEOREM_TARGET",
            missing="explicit J_V^mu",
            consequence="decides whether u_vac can be defined",
        ),
        VolumeCurrentEntry(
            name="JV2: zeta-gradient current",
            current="J_V^mu = beta_z nabla^mu zeta",
            role="simplest scalar-derived current candidate",
            allowed_if="nabla zeta is timelike and beta_z has prior origin",
            forbidden_if="used in static/equilibrium regions where gradient is not a time-flow",
            status="RISK",
            missing="causal character of nabla zeta and beta_z origin",
            consequence="likely insufficient as general vacuum rest frame",
        ),
        VolumeCurrentEntry(
            name="JV3: exchange continuity current",
            current="nabla_mu J_V^mu = Sigma_V - R_V",
            role="volume-balance candidate current",
            allowed_if="Sigma_V and R_V are defined independently",
            forbidden_if="continuity equation is written with unnamed terms",
            status="CANDIDATE",
            missing="Sigma_V, R_V, and boundary conditions",
            consequence="strongest route if volume exchange supplies conservation/balance law",
        ),
        VolumeCurrentEntry(
            name="JV4: source-driven current",
            current="J_V^mu sourced by Sigma_V ~ chi rho a^nu nabla_nu A",
            role="ties volume current to acceleration-gradient source law",
            allowed_if="source creates divergence of J_V, not arbitrary direction",
            forbidden_if="J_V direction is chosen after defining source scalar",
            status="CANDIDATE",
            missing="flux direction law and chi origin",
            consequence="needs more than scalar source; requires transport/flux law",
        ),
        VolumeCurrentEntry(
            name="JV5: equilibrium zero-flux current",
            current="u_vac is rest frame where spatial J_V vanishes locally",
            role="defines vacuum rest frame once J_V exists",
            allowed_if="J_V exists and is timelike/nonzero",
            forbidden_if="zero-flux frame is coordinate rest frame without current",
            status="SAFE_IF",
            missing="J_V itself",
            consequence="useful rest-frame definition but not a current origin",
        ),
        VolumeCurrentEntry(
            name="JV6: density-times-frame circularity",
            current="J_V^mu = n_V u_vac^mu",
            role="circular definition warning",
            allowed_if="u_vac already defined elsewhere",
            forbidden_if="used to define u_vac",
            status="REJECTED",
            missing="not pursued as definition",
            consequence="cannot define the clock using the clock",
        ),
        VolumeCurrentEntry(
            name="JV7: decorative current failure",
            current="J_V is declared as vacuum volume current without flux law",
            role="rejected shortcut",
            allowed_if="never as derivation",
            forbidden_if="used to keep u_vac branch alive",
            status="REJECTED",
            missing="not pursued",
            consequence="triggers Group 14 closure if no current is written",
        ),
        VolumeCurrentEntry(
            name="JV8: timelike/nonzero requirement",
            current="J_V^2 < 0 and J_V != 0 in regimes where u_vac is used",
            role="mathematical viability condition for normalized u_vac",
            allowed_if="proved or domain-limited",
            forbidden_if="normalization used where J_V is null/spacelike/zero",
            status="REQUIRED",
            missing="domain theorem for J_V",
            consequence="prevents invalid frame definition",
        ),
        VolumeCurrentEntry(
            name="JV9: static-source neutrality",
            current="static equilibrium sources do not produce independent exterior J_V/zeta charge",
            role="ordinary-sector safety condition",
            allowed_if="static flux is zero or boundary-neutral",
            forbidden_if="static mass creates scalar volume flux/charge",
            status="REQUIRED",
            missing="static neutrality theorem",
            consequence="kills current definitions that create scalar gravity",
        ),
        VolumeCurrentEntry(
            name="JV10: sign/orientation rule",
            current="orientation of J_V fixes creation/destruction sign",
            role="resolves volume-source sign ambiguity",
            allowed_if="orientation follows from exchange law",
            forbidden_if="sign is chosen from gamma/AB recovery",
            status="UNRESOLVED",
            missing="orientation convention",
            consequence="needed before numerical or recovery claims",
        ),
        VolumeCurrentEntry(
            name="JV11: boundary/no-overlap requirements",
            current="J_V-driven zeta is boundary-neutral and metric insertion occurs only through B_s",
            role="protects exterior neutrality and count-once recombination",
            allowed_if="boundary/no-overlap theorems are attached",
            forbidden_if="J_V creates independent residual metric trace",
            status="REQUIRED",
            missing="boundary neutrality and no-overlap proof",
            consequence="even a real current fails if accounting fails",
        ),
        VolumeCurrentEntry(
            name="JV12: recommended closure move",
            current="if exchange continuity current cannot be specified, close Group 14",
            role="best current governance decision",
            allowed_if="J_V remains undefined after this test",
            forbidden_if="continuing ratio/frame relocation loops",
            status="RECOMMENDED",
            missing="closure summary if J_V remains undefined",
            consequence="next artifact should be Group 14 closure unless J_V becomes explicit",
        ),
    ]


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="vacuum_rest_frame_definition_marker",
        upstream_script_id="014_kappa_zeta_map_and_projectors__candidate_vacuum_rest_frame_definition",
        upstream_derivation_id="vacuum_rest_frame_definition_marker",
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


def print_entry(e: VolumeCurrentEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Current: {e.current}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    print(f"Status: {e.status}")
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Volume current definition for u_vac problem")

    print("Question:")
    print()
    print("  Can J_V be written, or do we close the cave?")
    print()
    print("Goal:")
    print()
    print("  test whether a real vacuum-volume current can define u_vac")
    print()
    print("Discipline:")
    print()
    print("  do not declare J_V without a flux/balance law")
    print("  do not define J_V using u_vac circularly")
    print("  require timelike/nonzero domain")
    print("  protect static-source neutrality")
    print("  preserve boundary neutrality and no-overlap")
    print("  close Group 14 if J_V remains unnamed")

    out = ScriptOutput()
    with out.unresolved_obligations():
        out.line("volume current definition problem posed", StatusMark.OBLIGATION, "requires real J_V flux law, not decoration")


def case_1_inventory(entries: List[VolumeCurrentEntry]):
    header("Case 1: Volume current definition inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[VolumeCurrentEntry]):
    header("Case 2: Compact volume-current ledger")

    print("| Entry | Current | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.current.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("compact volume-current ledger produced", StatusMark.INFO, "inventory only")


def case_3_status_counts(entries: List[VolumeCurrentEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  J_V is not defined by naming it.")
    print("  zeta-gradient current is risky and probably not general.")
    print("  exchange continuity current is the strongest candidate but needs Sigma_V and R_V.")
    print("  source-driven scalar Sigma_V alone does not determine flux direction.")
    print("  if no exchange/transport law is supplied, Group 14 should close.")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("volume-current status count produced", StatusMark.INFO, "inventory only")


def case_4_current_decision_tree():
    header("Case 4: Volume-current decision tree")

    print("Decision tree:")
    print()
    print("1. Can J_V be defined by exchange continuity?")
    print("   Need: nabla_mu J_V^mu = Sigma_V - R_V with Sigma_V/R_V defined.")
    print()
    print("2. Can J_V be defined by zeta gradient?")
    print("   Only if grad zeta is timelike/nonzero in target regimes.")
    print()
    print("3. Can scalar Sigma_V define J_V direction?")
    print("   No, not by itself; a transport/flux law is needed.")
    print()
    print("4. Can J_V = n_V u_vac define u_vac?")
    print("   No, circular.")
    print()
    print("5. If no real J_V:")
    print("   close Group 14 with u_vac/J_V as bottleneck.")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("volume-current decision tree stated", StatusMark.INFO, "candidates ranked")


def case_5_good_failure():
    header("Case 5: Good failure / closure trigger")

    print("Good failure:")
    print()
    print("  no non-circular, timelike, boundary-neutral J_V can be defined from current ingredients.")
    print()
    print("Consequence:")
    print()
    print("  u_vac cannot currently be defined.")
    print("  Acceleration-gradient volume creation remains a theorem target, not a source law.")
    print("  Group 14 should close with J_V/u_vac as the surviving bottleneck.")
    print()
    print("Bad failure:")
    print("  declare J_V and keep going because the next equation needs a clock.")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("volume-current good failure stated", StatusMark.DEFER, "deferred: J_V/u_vac is surviving Group 14 bottleneck")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("Volume-current definition fails if:")
    print()
    print("1. J_V is named but not defined")
    print("2. J_V is defined using u_vac circularly")
    print("3. zeta-gradient is used where it is not timelike/nonzero")
    print("4. scalar Sigma_V is treated as flux direction")
    print("5. Sigma_V/R_V are unnamed in continuity equation")
    print("6. static sources create independent exterior zeta charge")
    print("7. J_V creates residual metric trace outside B_s")
    print("8. sign/orientation is chosen from recovery")
    print("9. group continues without defining J_V")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("volume-current failure controls stated", StatusMark.INFO, "guardrails recorded")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_volume_current_definition_for_u_vac.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_group_14_closure_summary.py")
    print("   Close Group 14 with J_V/u_vac as surviving bottleneck.")
    print()
    print("3. candidate_exchange_continuity_law_for_volume.py")
    print("   Only if the project wants one final attempt to define Sigma_V/R_V continuity.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_group_14_closure_summary.py")
    print()
    print("Reason:")
    print("  J_V remains dependent on an exchange continuity law not yet available. Close Group 14 and promote J_V/u_vac to next-group bottleneck.")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("next test selected", StatusMark.INFO, "candidate_group_14_closure_summary.py")


def final_interpretation():
    header("Final interpretation")

    print("J_V is the best candidate for defining u_vac, but it is not yet defined.")
    print()
    print("The strongest possible form is an exchange continuity law:")
    print()
    print("  nabla_mu J_V^mu = Sigma_V - R_V")
    print()
    print("But Sigma_V/R_V and flux direction are not yet available.")
    print()
    print("Best next script:")
    print("  candidate_group_14_closure_summary.py")


def main():
    header("Candidate Volume Current Definition For u_vac")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_current_decision_tree()
    case_5_good_failure()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_J_V_flux_law",
        script_id=SCRIPT_ID,
        title="Derive J_V flux direction law for vacuum-volume current",
        status=ObligationStatus.OPEN,
        description=(
            "J_V must have an independent physical flux or transport law — not just a divergence "
            "equation — before u_vac^mu = J_V^mu / sqrt(-J_V^2) can define the vacuum rest frame."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_J_V_domain_theorem",
        script_id=SCRIPT_ID,
        title="Derive timelike/nonzero domain theorem for J_V",
        status=ObligationStatus.OPEN,
        description=(
            "J_V^2 < 0 and J_V != 0 must be proved or the domain explicitly restricted "
            "to regimes where these conditions hold, to prevent invalid frame normalization."
        ),
    ))
    ns.record_route(RouteRecord(
        route_id="exchange_continuity_J_V_route",
        script_id=SCRIPT_ID,
        name="Exchange continuity J_V route: nabla_mu J_V^mu = Sigma_V - R_V",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[
            "derive_J_V_flux_law",
            "derive_J_V_domain_theorem",
            "derive_Sigma_V_source_law",
            "derive_boundary_neutrality_for_Sigma_V",
        ],
        activation_conditions=[
            "Sigma_V and R_V are independently defined",
            "J_V has a non-circular transport/flux direction",
            "J_V^2 < 0 and J_V != 0 in target domain",
        ],
    ))
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_decorative_J_V",
        script_id=SCRIPT_ID,
        branch_id="decorative_J_V_current",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        reason_code=ReasonCode.RECOVERY_SELECTED_PARAMETER,
        description=(
            "J_V declared as vacuum-volume current without a flux law is rejected. "
            "Naming J_V does not define it; a real transport/balance law is required."
        ),
    ))
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_circular_J_V_n_V_u_vac",
        script_id=SCRIPT_ID,
        branch_id="circular_J_V_n_V_u_vac",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        reason_code=ReasonCode.RECOVERY_SELECTED_PARAMETER,
        description=(
            "J_V^mu = n_V u_vac^mu used to define u_vac is rejected as a circular definition. "
            "The clock cannot be defined using the clock."
        ),
    ))
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_volume_current_and_u_vac_definition",
        script_id=SCRIPT_ID,
        branch_id="volume_current_J_V_and_u_vac",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "derive_J_V_flux_law",
            "derive_J_V_domain_theorem",
            "derive_Sigma_V_source_law",
        ],
        description=(
            "J_V/u_vac definition is deferred pending an independent flux direction law, "
            "a domain theorem, and defined Sigma_V/R_V operators. "
            "Group 14 closes with J_V/u_vac as the surviving bottleneck."
        ),
    ))
    ns.record_derivation(
        derivation_id="volume_current_definition_for_u_vac_marker",
        inputs=[],
        output=sp.Symbol("volume_current_definition_for_u_vac_audited"),
        method="volume_current_definition_for_u_vac_audit",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
