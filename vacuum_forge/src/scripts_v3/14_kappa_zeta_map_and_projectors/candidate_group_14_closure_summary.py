# Group:
#   14_kappa_zeta_map_and_projectors
#
# Script type:
#   SUMMARY
#
# Candidate Group 14 closure summary
#
# Purpose
# -------
# Group 14 began as kappa/zeta map and projector work.
#
# It became a controlled search for the origin of A_spatial / spatial-trace response.
#
# The final live branch reduced to:
#
#   source-driven volume creation
#     -> acceleration-gradient source law
#     -> vacuum rest frame u_vac
#     -> vacuum-volume current J_V
#
# The volume-current test found:
#
#   J_V is not yet defined.
#
# Therefore Group 14 should close with J_V/u_vac as the surviving bottleneck.
#
# This script is a closure ledger, not a new candidate mechanism.

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
class ClosureEntry:
    name: str
    finding: str
    status: str
    consequence: str


def build_entries() -> List[ClosureEntry]:
    return [
        ClosureEntry(
            name="G14-1: original group purpose",
            finding="map kappa/zeta/projector responsibilities and prevent scalar double-counting",
            status="STRUCTURAL",
            consequence="projector accounting was sharpened into spatial-trace origin search",
        ),
        ClosureEntry(
            name="G14-2: A_spatial origin target",
            finding="derive A_spatial/spatial trace without GR smuggling or gamma tuning",
            status="THEOREM_TARGET",
            consequence="became the central field-equation narrowing problem of the group",
        ),
        ClosureEntry(
            name="G14-3: local differential closure",
            finding="local closure produces q but does not derive q",
            status="DEFER",
            consequence="coefficient origin became the bottleneck",
        ),
        ClosureEntry(
            name="G14-4: coupled stiffness route",
            finding="coupled stiffness yields q = -c_x/c_s",
            status="DEFER",
            consequence="moved coefficient problem to stiffness ratio",
        ),
        ClosureEntry(
            name="G14-5: conservation-current route",
            finding="minimal gradient current yields q = -a/b",
            status="DEFER",
            consequence="moved coefficient problem to current ratio",
        ),
        ClosureEntry(
            name="G14-6: parent balance route",
            finding="parent balance requires explicit E_parent and otherwise relocates ratio",
            status="DEFER",
            consequence="decorative balance and GR rewrite were rejected",
        ),
        ClosureEntry(
            name="G14-7: volume-exchange route",
            finding="volume exchange is ontology-native but requires explicit V[A,B_s,zeta]",
            status="CANDIDATE",
            consequence="forced zeta companion-versus-residual decision",
        ),
        ClosureEntry(
            name="G14-8: zeta status",
            finding="zeta cannot be both B_s companion and independent residual trace",
            status="REQUIRED",
            consequence="companion branch requires residual zeta trace killed or non-metric",
        ),
        ClosureEntry(
            name="G14-9: F_zeta map",
            finding="algebraic F_zeta maps are high-risk; source-driven maps need Sigma_V[A,T]",
            status="DEFER",
            consequence="moved live branch to source-driven volume creation",
        ),
        ClosureEntry(
            name="G14-10: source-driven volume creation",
            finding="best candidate is Sigma_V ~ chi rho a^mu nabla_mu A",
            status="CANDIDATE",
            consequence="requires frame/projection, chi-origin, neutrality, and no-overlap",
        ),
        ClosureEntry(
            name="G14-11: frame field",
            finding="matter frame is concrete but risky; vacuum frame is ontology-native but undefined",
            status="DEFER",
            consequence="moved live branch to u_vac definition",
        ),
        ClosureEntry(
            name="G14-12: vacuum current",
            finding="u_vac best candidate is normalized J_V, but J_V is not defined",
            status="UNRESOLVED",
            consequence="final surviving bottleneck is J_V/u_vac",
        ),
        ClosureEntry(
            name="G14-13: closure decision",
            finding="Group 14 should stop rather than continue ratio/frame relocation loops",
            status="CLOSED",
            consequence="promote J_V/u_vac and exchange continuity to next group",
        ),
    ]


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="volume_current_definition_for_u_vac_marker",
        upstream_script_id="14_kappa_zeta_map_and_projectors__candidate_volume_current_definition_for_u_vac",
        upstream_derivation_id="volume_current_definition_for_u_vac_marker",
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


def print_entry(e: ClosureEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Finding: {e.finding}")
    print(f"Status: {e.status}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Group 14 closure problem")

    print("Question:")
    print()
    print("  What did Group 14 accomplish, what did it kill, and what bottleneck survives?")
    print()
    print("Goal:")
    print()
    print("  close the group without pretending the final field equations were derived")
    print()
    print("Discipline:")
    print()
    print("  do not open another ratio-relocation loop")
    print("  do not promote J_V or u_vac before definition")
    print("  keep gamma/AB recovery downstream")
    print("  preserve no-overlap and boundary-neutrality guardrails")
    print("  name the surviving bottleneck explicitly")

    out = ScriptOutput()
    with out.unresolved_obligations():
        out.line("Group 14 closure problem posed", StatusMark.OBLIGATION, "J_V/u_vac surviving bottleneck must be named")
    out.print()


def case_1_closure_inventory(entries: List[ClosureEntry]):
    header("Case 1: Closure inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[ClosureEntry]):
    header("Case 2: Compact closure ledger")

    print("| Entry | Finding | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.finding.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("compact closure ledger produced", StatusMark.INFO, "summary inventory")
    out.print()


def case_3_killed_branches():
    header("Case 3: Killed or rejected branches")

    rejected = [
        "free q chosen from gamma_like or AB",
        "copy GR spatial metric or impose B=1/A by decree",
        "raw kappa/Box kappa/Box zeta scalar radiation branches",
        "zeta as both B_s companion and residual metric trace",
        "coordinate velocity rho v dot grad A as parent source law",
        "arbitrary preferred vacuum frame",
        "decorative J_V or decorative Div E_parent",
        "J_V = n_V u_vac used to define u_vac circularly",
    ]

    for item in rejected:
        print(f"- {item}")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("rejected branch list stated", StatusMark.INFO, "branches rejected or deferred")
    out.print()


def case_4_surviving_bottleneck():
    header("Case 4: Surviving bottleneck")

    print("Surviving bottleneck:")
    print()
    print("  define a real vacuum-volume current J_V^mu")
    print()
    print("Needed for:")
    print()
    print("  u_vac^mu = J_V^mu / sqrt(-J_V^2)")
    print()
    print("Strongest possible structure:")
    print()
    print("  nabla_mu J_V^mu = Sigma_V - R_V")
    print()
    print("Missing:")
    print()
    print("  Sigma_V complete source law")
    print("  R_V relaxation/exchange term")
    print("  flux/transport direction")
    print("  timelike/nonzero domain")
    print("  boundary neutrality")
    print("  no-overlap / residual-kill theorem")
    print("  sign/orientation")
    print("  chi-origin")

    out = ScriptOutput()
    with out.unresolved_obligations():
        out.line("surviving bottleneck named", StatusMark.OPEN, "J_V/u_vac definition unresolved")
    out.print()


def case_5_provisional_conventions():
    header("Case 5: Provisional conventions to carry forward")

    conventions = [
        "A_spatial remains a recovery theorem target, not a derived equation.",
        "zeta may become B_s companion only if residual zeta trace is killed or non-metric.",
        "if zeta remains residual, it does not solve A_spatial/q-origin.",
        "kappa remains diagnostic/non-metric unless later branch proves otherwise.",
        "gamma_like and AB are recovery checks, not construction tools.",
        "boundary neutrality and no-overlap remain mandatory.",
        "J_V/u_vac is the next-group bottleneck.",
    ]

    for item in conventions:
        print(f"- {item}")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("provisional conventions stated", StatusMark.INFO, "carried forward as provisional")
    out.print()


def case_6_next_group():
    header("Case 6: Recommended next group")

    print("Recommended next group:")
    print()
    print("  15_vacuum_current_and_exchange_continuity")
    print()
    print("Locked door:")
    print()
    print("  Can a real exchange continuity law define J_V?")
    print()
    print("First script:")
    print()
    print("  candidate_exchange_continuity_law_for_volume.py")
    print()
    print("Reason:")
    print()
    print("  Group 14 reached J_V/u_vac as bottleneck.")
    print("  The next group should derive or kill the volume-current route directly.")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("next group selected", StatusMark.INFO, "15_vacuum_current_and_exchange_continuity")
    out.print()


def final_interpretation():
    header("Final interpretation")

    print("Group 14 is closed.")
    print()
    print("It did not derive A_spatial.")
    print("It did something useful instead:")
    print()
    print("  it reduced the spatial-trace origin problem to J_V/u_vac.")
    print()
    print("Final bottleneck:")
    print()
    print("  define a real vacuum-volume current J_V^mu,")
    print("  or keep acceleration-gradient volume creation as a theorem target only.")


def main():
    header("Candidate Group 14 Closure Summary")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    entries = build_entries()
    case_1_closure_inventory(entries)
    case_2_compact_table(entries)
    case_3_killed_branches()
    case_4_surviving_bottleneck()
    case_5_provisional_conventions()
    case_6_next_group()
    final_interpretation()

    with archive:
        # Summary claim for Group 14 closure
        ns.record_claim(ClaimRecord(
            claim_id="group_14_A_spatial_not_derived",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.SUMMARY_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.NOT_INSERTABLE_YET,
            statement=(
                "Group 14 did not derive A_spatial or the spatial-trace q-origin. "
                "The problem was reduced to J_V/u_vac definition, which remains a theorem target."
            ),
            obligation_ids=[
                "derive_J_V_flux_law",
                "derive_Sigma_V_source_law",
                "derive_boundary_neutrality_for_Sigma_V",
                "derive_residual_kill_no_overlap_for_Sigma_V",
            ],
        ))
        ns.record_claim(ClaimRecord(
            claim_id="group_14_recovery_downstream_convention",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.POLICY_RULE,
            statement=(
                "gamma_like and AB are recovery checks, not construction tools. "
                "They must remain downstream of source law derivation in all successor groups."
            ),
        ))
        ns.record_claim(ClaimRecord(
            claim_id="group_14_zeta_companion_requires_residual_kill",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.POLICY_RULE,
            statement=(
                "zeta may become a B_s companion only if the residual zeta trace is killed or "
                "proven non-metric. If zeta remains residual, it does not solve the A_spatial/q-origin."
            ),
        ))

        # Rejected branch decisions for the closure record
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id="reject_free_q_from_gamma_AB",
            script_id=SCRIPT_ID,
            branch_id="free_q_from_gamma_AB",
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            reason_code=ReasonCode.RECOVERY_SELECTED_PARAMETER,
            description="Choosing q from gamma_like or AB is rejected as recovery-tuning.",
        ))
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id="reject_zeta_dual_role_branch",
            script_id=SCRIPT_ID,
            branch_id="zeta_companion_and_residual_trace",
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            reason_code=ReasonCode.RECOVERY_SELECTED_PARAMETER,
            description=(
                "zeta cannot simultaneously be a B_s companion and an independent residual metric trace. "
                "This branch is rejected; the companion route requires residual-kill."
            ),
        ))
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id="defer_group_14_source_driven_branch",
            script_id=SCRIPT_ID,
            branch_id="group_14_source_driven_volume_creation",
            status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=[
                "derive_J_V_flux_law",
                "derive_Sigma_V_source_law",
                "derive_u_vac_from_vacuum_ontology",
                "derive_boundary_neutrality_for_Sigma_V",
                "derive_residual_kill_no_overlap_for_Sigma_V",
            ],
            description=(
                "The source-driven volume creation branch (Sigma_V -> J_V -> u_vac -> B_s companion) "
                "is deferred pending J_V flux law, Sigma_V source law, u_vac definition, boundary "
                "neutrality, and no-overlap theorem. Group 14 closes here."
            ),
        ))

        # Handoff import record: what Group 15 may import from Group 14
        ns.record_handoff_import(HandoffImportRecord(
            handoff_id="group_14_to_15_handoff",
            script_id=SCRIPT_ID,
            imported_as=RecordKind.SUMMARY_CLAIM,
            status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
            imported_record_refs=[
                # Open obligations Group 15 must address or carry forward
                "obligation:derive_Sigma_V_source_law",
                "obligation:derive_chi_origin_for_Sigma_V",
                "obligation:derive_residual_kill_no_overlap_for_Sigma_V",
                "obligation:derive_boundary_neutrality_for_Sigma_V",
                "obligation:derive_J_V_flux_law",
                "obligation:derive_J_V_domain_theorem",
                "obligation:derive_u_vac_from_vacuum_ontology",
                "obligation:derive_u_vac_static_neutrality",
                "obligation:derive_covariant_acceleration_for_Sigma_V",
                "obligation:derive_static_source_neutrality_for_accel_gradient",
                # Candidate routes Group 15 may build on
                "route:exchange_continuity_J_V_route",
                "route:acceleration_gradient_Sigma_V_candidate_route",
                # Rejected branches Group 15 must not reopen
                "decision:reject_free_q_from_gamma_AB",
                "decision:reject_zeta_dual_role_branch",
                "decision:reject_coordinate_velocity_accel_gradient",
                "decision:reject_arbitrary_preferred_frame",
                "decision:reject_decorative_J_V",
                "decision:reject_circular_J_V_n_V_u_vac",
                # Policy rules Group 15 must preserve
                "claim:group_14_recovery_downstream_convention",
                "claim:group_14_zeta_companion_requires_residual_kill",
                # Summary closure claim
                "claim:group_14_A_spatial_not_derived",
            ],
            description=(
                "Group 15 (vacuum_current_and_exchange_continuity) may import the following from Group 14:\n"
                "OPEN OBLIGATIONS: Sigma_V source law, chi-origin, residual-kill/no-overlap, boundary neutrality, "
                "J_V flux law, J_V domain theorem, u_vac definition, u_vac static neutrality, "
                "covariant acceleration, static-source safety.\n"
                "CANDIDATE ROUTES: exchange continuity J_V route, acceleration-gradient Sigma_V route.\n"
                "REJECTED BRANCHES: free-q tuning, zeta dual-role, coordinate velocity frame, "
                "arbitrary preferred frame, decorative J_V, circular J_V = n_V u_vac.\n"
                "POLICY RULES: recovery downstream, zeta companion requires residual-kill.\n"
                "GROUP CLOSURE: A_spatial was not derived; J_V/u_vac is the surviving bottleneck."
            ),
        ))

        ns.record_derivation(
            derivation_id="group_14_closure_summary_marker",
            inputs=[],
            output=sp.Symbol("group_14_closure_summary_audited"),
            method="group_14_closure_summary_audit",
            status=Status.DERIVED,
            record_kind=RecordKind.INVENTORY_MARKER,
            is_placeholder=True,
        )
        ns.write_run_metadata()


if __name__ == "__main__":
    main()
