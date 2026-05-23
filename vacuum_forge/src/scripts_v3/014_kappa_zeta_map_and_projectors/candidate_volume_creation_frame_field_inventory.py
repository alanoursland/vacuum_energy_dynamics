# Group:
#   14_kappa_zeta_map_and_projectors
#
# Script type:
#   INVENTORY
#
# Candidate volume creation frame field inventory
#
# Purpose
# -------
# The acceleration-gradient volume creation audit found:
#
#   Sigma_V = chi rho a^mu nabla_mu A
#
# is the best postulate-facing source law candidate.
#
# But the bottleneck is the frame:
#
#   what is u^mu, and what projection defines a^mu nabla_mu A?
#
# This script inventories matter-flow, vacuum-flow, and projected-frame choices.
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
class FrameFieldEntry:
    name: str
    frame_choice: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[FrameFieldEntry]:
    return [
        FrameFieldEntry(
            name="FF1: frame-field target",
            frame_choice="choose physical u^mu/u_vac^mu for Sigma_V = chi rho a^mu nabla_mu A",
            role="core prerequisite for acceleration-gradient source law",
            allowed_if="frame is defined by matter flow, vacuum substance, or explicit ontology",
            forbidden_if="frame is selected to fit recovery checks",
            status="THEOREM_TARGET",
            missing="physical frame definition",
            consequence="decides whether acceleration-gradient candidate can be covariant",
        ),
        FrameFieldEntry(
            name="FF2: matter congruence frame",
            frame_choice="u^mu = u_m^mu from matter flow; a_m^mu = u_m^nu nabla_nu u_m^mu",
            role="source-local matter-frame candidate",
            allowed_if="matter current/congruence is well-defined and not coordinate velocity",
            forbidden_if="used for static matter as coordinate artifact",
            status="CANDIDATE",
            missing="matter model and current definition",
            consequence="works best for fluid/dust sources but may be source-dependent",
        ),
        FrameFieldEntry(
            name="FF3: vacuum rest frame",
            frame_choice="u^mu = u_vac^mu from local rest frame of vacuum substance / zeta flow",
            role="ontology-native frame candidate",
            allowed_if="u_vac follows from vacuum volume configuration or exchange law",
            forbidden_if="invented to make Sigma_V nonzero/zero as convenient",
            status="CANDIDATE",
            missing="definition of u_vac^mu",
            consequence="best aligned with vacuum ontology but currently missing",
        ),
        FrameFieldEntry(
            name="FF4: projected matter acceleration",
            frame_choice="Sigma_V = chi rho (P_vac a_m)^mu (P_vac nabla A)_mu",
            role="hybrid frame: matter acceleration measured relative to vacuum frame",
            allowed_if="both u_m and u_vac are defined",
            forbidden_if="projection is chosen from gamma/AB recovery",
            status="RISK",
            missing="u_vac, projection convention, sign",
            consequence="may express mass accelerating across vacuum gradient, but adds structure",
        ),
        FrameFieldEntry(
            name="FF5: vacuum acceleration of vacuum flow",
            frame_choice="Sigma_V = chi rho a_vac^mu nabla_mu A",
            role="vacuum-flow acceleration candidate",
            allowed_if="rho coupling to vacuum acceleration is justified",
            forbidden_if="matter source disappears or coupling is arbitrary",
            status="RISK",
            missing="rho-vacuum coupling rule",
            consequence="may shift source law away from matter acceleration",
        ),
        FrameFieldEntry(
            name="FF6: hypersurface normal frame",
            frame_choice="u^mu = n^mu normal to chosen slicing",
            role="mathematically convenient frame",
            allowed_if="slicing is physically defined by vacuum ontology",
            forbidden_if="pure gauge slicing is treated as physical",
            status="CONSTRAINED",
            missing="physical slicing rule",
            consequence="likely diagnostic only unless tied to vacuum rest frame",
        ),
        FrameFieldEntry(
            name="FF7: coordinate velocity frame",
            frame_choice="u^mu from coordinate velocity v^i",
            role="toy / reduced diagnostic only",
            allowed_if="used only in simulations or reduced intuition",
            forbidden_if="accepted as parent law",
            status="REJECTED",
            missing="not pursued as parent frame",
            consequence="prevents rho v dot grad A from becoming field equation",
        ),
        FrameFieldEntry(
            name="FF8: static-source safety",
            frame_choice="frame choice makes Sigma_V static-neutral unless physical acceleration/exchange exists",
            role="ordinary-sector safety requirement",
            allowed_if="static equilibrium source has no independent exterior zeta charge",
            forbidden_if="static density in a gradient creates scalar charge",
            status="REQUIRED",
            missing="static neutrality theorem",
            consequence="kills frame choices that make static matter source scalar volume charge",
        ),
        FrameFieldEntry(
            name="FF9: sign/orientation rule",
            frame_choice="frame/projection fixes sign of a·grad A as creation/destruction",
            role="resolves unresolved orientation ambiguity",
            allowed_if="sign follows from postulate/exchange convention before recovery",
            forbidden_if="sign chosen to match gamma/AB",
            status="UNRESOLVED",
            missing="creation/destruction orientation convention",
            consequence="needed before numerical or recovery claims",
        ),
        FrameFieldEntry(
            name="FF10: chi-origin dependency",
            frame_choice="frame choice does not fix chi by recovery; chi still needs ontology/source coupling",
            role="prevents frame from hiding coefficient tuning",
            allowed_if="chi remains separately constrained by postulate/exchange law",
            forbidden_if="frame/projection absorbs chi fit",
            status="REQUIRED",
            missing="chi origin",
            consequence="frame field alone cannot complete Sigma_V derivation",
        ),
        FrameFieldEntry(
            name="FF11: boundary/no-overlap requirements",
            frame_choice="source-driven zeta is boundary-neutral and enters metric only through B_s",
            role="protects exterior neutrality and count-once recombination",
            allowed_if="boundary and overlap theorems are attached",
            forbidden_if="frame choice creates exterior scalar charge or residual overlap",
            status="REQUIRED",
            missing="boundary neutrality and no-overlap proofs",
            consequence="frame-safe source still fails if accounting fails",
        ),
        FrameFieldEntry(
            name="FF12: recommended next move",
            frame_choice="test vacuum rest frame vs matter congruence frame before hybrid projection",
            role="best current branch decision",
            allowed_if="each branch has static-source and no-overlap checks",
            forbidden_if="jumping to hybrid frame to patch failures",
            status="RECOMMENDED",
            missing="frame branch comparison script",
            consequence="next script should compare u_matter and u_vac branches directly",
        ),
    ]


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="acceleration_gradient_volume_creation_marker",
        upstream_script_id="14_kappa_zeta_map_and_projectors__candidate_acceleration_gradient_volume_creation",
        upstream_derivation_id="acceleration_gradient_volume_creation_marker",
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


def print_entry(e: FrameFieldEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Frame choice: {e.frame_choice}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    print(f"Status: {e.status}")
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Volume creation frame-field inventory problem")

    print("Question:")
    print()
    print("  Who gets to say what accelerating across the gradient means?")
    print()
    print("Goal:")
    print()
    print("  inventory frame choices for Sigma_V = chi rho a^mu nabla_mu A")
    print()
    print("Discipline:")
    print()
    print("  do not use coordinate velocity as parent frame")
    print("  do not invent vacuum frame to fit recovery")
    print("  do not use gauge slicing as physical frame unless ontology defines it")
    print("  protect static-source neutrality")
    print("  keep chi-origin separate")
    print("  preserve boundary neutrality and no-overlap")

    out = ScriptOutput()
    with out.unresolved_obligations():
        out.line("volume creation frame-field problem posed", StatusMark.OBLIGATION, "requires physical u^mu/u_vac^mu definition")


def case_1_inventory(entries: List[FrameFieldEntry]):
    header("Case 1: Frame-field inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[FrameFieldEntry]):
    header("Case 2: Compact frame-field ledger")

    print("| Entry | Frame choice | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.frame_choice.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("compact frame-field ledger produced", StatusMark.INFO, "inventory only")


def case_3_status_counts(entries: List[FrameFieldEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Matter congruence and vacuum rest frame are the two clean branches.")
    print("  Hybrid projection is possible but risky unless both frames are defined.")
    print("  Hypersurface normal is diagnostic unless physically tied to vacuum ontology.")
    print("  Coordinate velocity is rejected as parent frame.")
    print("  Static neutrality, chi-origin, boundary neutrality, and no-overlap remain mandatory.")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("frame-field status count produced", StatusMark.INFO, "inventory only")


def case_4_frame_decision_tree():
    header("Case 4: Frame decision tree")

    print("Decision tree:")
    print()
    print("1. Matter frame u_m?")
    print("   Good for source-local acceleration but source-model dependent.")
    print()
    print("2. Vacuum frame u_vac?")
    print("   Best ontology match, but currently missing.")
    print()
    print("3. Hybrid projection?")
    print("   Only after u_m and u_vac are both defined.")
    print()
    print("4. Hypersurface normal?")
    print("   Diagnostic unless slicing is physically defined.")
    print()
    print("5. Coordinate velocity?")
    print("   Rejected as parent law.")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("frame decision tree stated", StatusMark.INFO, "candidates ranked")


def case_5_good_failure():
    header("Case 5: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  no matter/vacuum frame can define acceleration-gradient volume creation")
    print("  while preserving static neutrality, chi-origin, boundary neutrality, and no-overlap.")
    print()
    print("Consequence:")
    print()
    print("  acceleration-gradient source law fails for now.")
    print("  Return to Sigma_V theorem target or test broader tensor candidates.")
    print()
    print("Bad failure:")
    print("  choose a convenient frame and proceed as if it were physical.")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("frame-field good failure stated", StatusMark.DEFER, "deferred pending physical frame definition")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("Frame-field inventory fails if:")
    print()
    print("1. coordinate velocity becomes parent frame")
    print("2. vacuum frame is invented to fit recovery")
    print("3. hypersurface normal is treated as physical without ontology")
    print("4. hybrid projection is used before both frames are defined")
    print("5. static source creates independent exterior zeta charge")
    print("6. frame choice hides chi tuning")
    print("7. boundary neutrality is absent")
    print("8. no-overlap theorem is absent")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("frame-field failure controls stated", StatusMark.INFO, "guardrails recorded")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_volume_creation_frame_field_inventory.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_matter_vs_vacuum_frame_branch_test.py")
    print("   Compare u_matter and u_vac frame branches directly.")
    print()
    print("3. candidate_vacuum_rest_frame_definition.py")
    print("   Try to define u_vac from zeta/vacuum substance ontology.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_matter_vs_vacuum_frame_branch_test.py")
    print()
    print("Reason:")
    print("  The next bottleneck is choosing between matter-flow and vacuum-flow frames before adding hybrid projections.")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("next test selected", StatusMark.INFO, "candidate_matter_vs_vacuum_frame_branch_test.py")


def final_interpretation():
    header("Final interpretation")

    print("The frame inventory reduces the branch to two clean candidates:")
    print()
    print("  matter congruence u_m^mu")
    print("  vacuum rest frame u_vac^mu")
    print()
    print("Hybrid projection should wait until both are defined.")
    print()
    print("Best next test:")
    print("  candidate_matter_vs_vacuum_frame_branch_test.py")


def main():
    header("Candidate Volume Creation Frame Field Inventory")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_frame_decision_tree()
    case_5_good_failure()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_physical_frame_for_accel_gradient",
        script_id=SCRIPT_ID,
        title="Derive physical frame field u^mu/u_vac^mu for acceleration-gradient source law",
        status=ObligationStatus.OPEN,
        description=(
            "A physical frame (matter congruence u_m or vacuum rest frame u_vac) must be "
            "defined before Sigma_V = chi rho a^mu nabla_mu A can be made covariant and frame-safe."
        ),
    ))
    ns.record_route(RouteRecord(
        route_id="matter_congruence_frame_route",
        script_id=SCRIPT_ID,
        name="Matter congruence frame u_m^mu for acceleration-gradient source law",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[
            "derive_physical_frame_for_accel_gradient",
            "derive_static_source_neutrality_for_accel_gradient",
        ],
        activation_conditions=[
            "matter current/congruence is well-defined and not coordinate velocity",
            "static matter does not create independent exterior zeta charge",
        ],
    ))
    ns.record_route(RouteRecord(
        route_id="vacuum_rest_frame_route",
        script_id=SCRIPT_ID,
        name="Vacuum rest frame u_vac^mu for acceleration-gradient source law",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[
            "derive_physical_frame_for_accel_gradient",
            "derive_static_source_neutrality_for_accel_gradient",
        ],
        activation_conditions=[
            "u_vac follows from vacuum volume configuration or exchange law",
            "not invented to make Sigma_V nonzero/zero as convenient",
        ],
    ))
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_coordinate_velocity_frame",
        script_id=SCRIPT_ID,
        branch_id="coordinate_velocity_frame",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        reason_code=ReasonCode.RECOVERY_SELECTED_PARAMETER,
        description=(
            "Coordinate velocity frame u^mu from v^i is rejected as parent frame; "
            "it is diagnostic only and prevents rho v dot grad A from becoming a field equation."
        ),
    ))
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_hybrid_projection_frame",
        script_id=SCRIPT_ID,
        branch_id="hybrid_projection_frame",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=["derive_physical_frame_for_accel_gradient"],
        description=(
            "Hybrid projection (P_vac a_m) is deferred until both u_m and u_vac are "
            "independently defined. It must not be used to patch failures of either branch."
        ),
    ))
    ns.record_derivation(
        derivation_id="volume_creation_frame_field_inventory_marker",
        inputs=[],
        output=sp.Symbol("volume_creation_frame_field_inventory_audited"),
        method="volume_creation_frame_field_inventory_audit",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
