# Candidate group 23 matching laws status summary
#
# Group:
#   23_smooth_support_and_matching_laws
#
# Script type:
#   SUMMARY
#
# Purpose
# -------
# Close Group 23 by summarizing:
#
#   matching regularity ladder,
#   distributional shell audit,
#   compact-support admissibility,
#   transition-layer mass/flux audit,
#   boundary-parameter independence,
#   source compatibility,
#   theorem obligations,
#   handoff options.
#
# This script is not a matching/support theorem.
# It is not compact support, no-shell matching, boundary neutrality,
# scalar silence, or parent equation readiness.
#
# Locked-door question:
#
#   What did Group 23 establish, and what remains theorem-targeted?

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


def status_mark(status: str) -> StatusMark:
    return {
        "CLOSED_DIAGNOSTIC": StatusMark.PASS,
        "DIAGNOSTIC_ONLY": StatusMark.INFO,
        "NOT_READY": StatusMark.DEFER,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "SAFE_IF": StatusMark.INFO,
        "SUMMARY": StatusMark.PASS,
        "THEOREM_TARGET": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "ladder_dep_23",
            "23_smooth_support_and_matching_laws__candidate_matching_regularization_ladder",
            "matching_regularization_ladder_marker_23",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "shell_dep_23",
            "23_smooth_support_and_matching_laws__candidate_distributional_shell_source_audit",
            "distributional_shell_source_audit_marker_23",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "support_dep_23",
            "23_smooth_support_and_matching_laws__candidate_compact_support_admissibility_conditions",
            "compact_support_admissibility_marker_23",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "layer_dep_23",
            "23_smooth_support_and_matching_laws__candidate_transition_layer_mass_flux_audit",
            "transition_layer_mass_flux_marker_23",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "param_dep_23",
            "23_smooth_support_and_matching_laws__candidate_boundary_parameter_independence",
            "boundary_parameter_independence_marker_23",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "source_dep_23",
            "23_smooth_support_and_matching_laws__candidate_matching_law_source_compatibility",
            "matching_law_source_compatibility_marker_23",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "obligation_dep_23",
            "23_smooth_support_and_matching_laws__candidate_matching_law_theorem_obligations",
            "matching_law_theorem_obligations_marker_23",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g22_summary_dep_23",
            "22_boundary_neutrality_and_scalar_silence__candidate_group_22_boundary_neutrality_status_summary",
            "group22_boundary_neutrality_status_summary_marker_22",
            RecordKind.INVENTORY_MARKER,
        ),
    ]

    for dependency_id, upstream_script_id, upstream_derivation_id, expected_record_kind in dependencies:
        ns.declare_dependency(
            dependency_id=dependency_id,
            upstream_script_id=upstream_script_id,
            upstream_derivation_id=upstream_derivation_id,
            expected_record_kind=expected_record_kind,
        )

    return archive, ns, invalidated


def ensure_archive_write_dirs(ns) -> None:
    for attr in (
        "routes_path",
        "branch_decisions_path",
        "claims_path",
        "obligations_path",
        "derivations_path",
        "governance_path",
    ):
        path_obj = getattr(ns, attr, None)
        if path_obj is not None:
            path_obj.mkdir(parents=True, exist_ok=True)


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


# =============================================================================
# Data models
# =============================================================================


@dataclass
class Group23StatusEntry:
    name: str
    result: str
    status: str
    consequence: str
    handoff: str


@dataclass
class ClosureOutcome:
    name: str
    statement: str
    status: str
    consequence: str


@dataclass
class HandoffOption:
    name: str
    route: str
    allowed_if: str
    caution: str
    status: str


# =============================================================================
# Builders
# =============================================================================


def build_status_entries() -> List[Group23StatusEntry]:
    return [
        Group23StatusEntry(
            name="G23-1: matching regularity ladder",
            result="value jump rejected; value matching alone risky; value+slope matching necessary diagnostically; smooth compact toy profiles remain diagnostics",
            status="CLOSED_DIAGNOSTIC",
            consequence="regularity ladder is explicit but not a support theorem",
            handoff="future work must derive support origin and no-shell matching",
        ),
        Group23StatusEntry(
            name="G23-2: distributional shell audit",
            result="cutoff profiles f(r)*Theta(R-r) can create delta-shell diagnostics from f(R) and slope/flux diagnostics from f'(R)",
            status="CLOSED_DIAGNOSTIC",
            consequence="sharp support and value-only matching remain unsafe",
            handoff="distributional shell absence remains theorem-targeted",
        ),
        Group23StatusEntry(
            name="G23-3: compact-support admissibility",
            result="compact support requires structural origin, f(R)=0, f'(R)=0/no-flux, shell absence, recovery independence, no hidden tuning, no A-tail, no scalar tail, and source compatibility",
            status="REQUIRED",
            consequence="compact support is constrained but not derived",
            handoff="support law remains theorem-targeted",
        ),
        Group23StatusEntry(
            name="G23-4: transition-layer mass/flux audit",
            result="smooth transition layers must have zero C_layer, q_layer, I_layer, sigma_layer, alpha_recovery, and source_load, with structural origin",
            status="REQUIRED",
            consequence="smoothness is not neutrality",
            handoff="transition-layer neutrality remains theorem-targeted",
        ),
        Group23StatusEntry(
            name="G23-5: boundary-parameter independence",
            result="support radius, smoothing width, AB/gamma coefficients, residual tail status, and boundary data must not be selected from recovery targets",
            status="REQUIRED",
            consequence="recovery remains downstream audit, not construction",
            handoff="recovery independence remains theorem-targeted",
        ),
        Group23StatusEntry(
            name="G23-6: source compatibility",
            result="matching/support/layer laws must preserve A-sector source routing and create no duplicate shell/scalar/current/repair/parameter source loads",
            status="REQUIRED",
            consequence="the source coin stays in A; no seam pockets",
            handoff="source compatibility remains theorem-targeted",
        ),
        Group23StatusEntry(
            name="G23-7: theorem obligations",
            result="nine matching/support obligations are explicit: support origin, value matching, slope/no-flux matching, shell absence, transition neutrality, recovery independence, source compatibility, residual non-reentry, no repair route",
            status="THEOREM_TARGET",
            consequence="real matching/support law remains not solved",
            handoff="Group 23 closes as requirements/diagnostic audit",
        ),
        Group23StatusEntry(
            name="G23-8: boundary/scalar and parent gates",
            result="compact support, no-shell matching, transition neutrality, boundary/scalar silence, and parent equation gates remain not ready",
            status="NOT_READY",
            consequence="do not open parent closure from Group 23 alone",
            handoff="next group should choose metric insertion retest, projector law, source-compatible boundary law, or reduced observational audit",
        ),
    ]


def build_outcomes() -> List[ClosureOutcome]:
    return [
        ClosureOutcome(
            name="Outcome A: matching ladder explicit",
            statement="Boundary regularity levels are classified from value jump through derived support law.",
            status="SUMMARY",
            consequence="future scripts have a seam-regularity checklist",
        ),
        ClosureOutcome(
            name="Outcome B: shell dangers explicit",
            statement="Sharp support, value-only matching, and slope/flux shell diagnostics are visible.",
            status="CLOSED_DIAGNOSTIC",
            consequence="fake no-shell claims are blocked",
        ),
        ClosureOutcome(
            name="Outcome C: compact support constrained",
            statement="Compact support is admissible only with structural origin, matching, no shell, no tails, recovery independence, and source compatibility.",
            status="REQUIRED",
            consequence="support by declaration remains rejected",
        ),
        ClosureOutcome(
            name="Outcome D: transition layers constrained",
            statement="Smooth transition layers cannot hide mass, scalar flux, current flux, shell/source load, recovery tuning, or source load.",
            status="REQUIRED",
            consequence="smoothness is not neutrality",
        ),
        ClosureOutcome(
            name="Outcome E: matching/support theorem still open",
            statement="Group 23 made obligations explicit but did not derive the matching/support theorem.",
            status="THEOREM_TARGET",
            consequence="boundary/scalar silence remains downstream",
        ),
        ClosureOutcome(
            name="Outcome F: parent equation still not ready",
            statement="Group 23 does not open the parent equation gate.",
            status="NOT_READY",
            consequence="parent closure remains downstream",
        ),
    ]


def build_handoffs() -> List[HandoffOption]:
    return [
        HandoffOption(
            name="Handoff 1: metric insertion recovery retest",
            route="24_metric_insertion_recovery_retest",
            allowed_if="the next step tests B_s/F_zeta insertion against Group 22 and Group 23 guardrails",
            caution="recovery may audit but may not choose boundary/support/layer data",
            status="CANDIDATE",
        ),
        HandoffOption(
            name="Handoff 2: role-specific boundary/source projectors",
            route="24_role_specific_boundary_projectors",
            allowed_if="the next step attempts real projector routes with domain, kernel, image, divergence, and boundary law",
            caution="active O remains unavailable unless actually derived",
            status="CANDIDATE",
        ),
        HandoffOption(
            name="Handoff 3: source-compatible boundary laws",
            route="24_source_compatible_boundary_laws",
            allowed_if="source compatibility becomes the bottleneck for matching/support law",
            caution="ordinary rho/M_enc must remain A-routed; no seam pockets",
            status="CANDIDATE",
        ),
        HandoffOption(
            name="Handoff 4: reduced observational audit",
            route="24_reduced_observational_audit",
            allowed_if="the project wants reduced tests without claiming parent closure",
            caution="observational checks must not choose boundary/scalar/current/support data",
            status="CANDIDATE",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Group 23 status summary problem")
    print("Question:")
    print()
    print("  What did Group 23 establish, and what remains theorem-targeted?")
    print()
    print("Discipline:")
    print()
    print("  This is a group summary, not a matching/support theorem.")
    print("  Compact support, no-shell matching, transition neutrality, boundary/scalar silence, and parent closure remain not ready.")
    print("  Group 23 closes as requirements and diagnostic audit.")

    with out.governance_assessments():
        out.line(
            "Group 23 status summary opened",
            StatusMark.INFO,
            "summarizing matching/support requirements without upgrading them to theorems",
        )


def case_1_status_entries(entries: List[Group23StatusEntry], out: ScriptOutput) -> None:
    header("Case 1: Group 23 status entries")
    for entry in entries:
        print()
        print("-" * 120)
        print(entry.name)
        print("-" * 120)
        print(f"Result: {entry.result}")
        print(f"[{status_mark(entry.status).value}] {entry.name}: {entry.status}")
        print(f"Consequence: {entry.consequence}")
        print(f"Handoff: {entry.handoff}")

    with out.governance_assessments():
        out.line(
            "Group 23 status ledger populated",
            StatusMark.PASS,
            f"{len(entries)} status entries summarized from the Group 23 chain",
        )


def case_2_closure_outcomes(outcomes: List[ClosureOutcome], out: ScriptOutput) -> None:
    header("Case 2: Closure outcomes")
    for outcome in outcomes:
        print()
        print("-" * 120)
        print(outcome.name)
        print("-" * 120)
        print(f"Statement: {outcome.statement}")
        print(f"[{status_mark(outcome.status).value}] {outcome.name}: {outcome.status}")
        print(f"Consequence: {outcome.consequence}")

    with out.governance_assessments():
        out.line(
            "Group 23 closure outcomes stated",
            StatusMark.PASS,
            "matching/support burdens explicit; theorem burden remains open",
        )


def case_3_known_unknowns(out: ScriptOutput) -> None:
    header("Case 3: Known unknowns preserved")
    unknowns = [
        "structural support origin theorem",
        "value matching theorem",
        "slope / no-flux matching theorem",
        "distributional shell absence theorem",
        "transition layer neutrality theorem",
        "recovery-independent boundary data theorem",
        "source-compatible matching law",
        "diagnostic residual non-reentry through support/matching",
        "no-repair support law",
        "boundary neutrality theorem",
        "exterior scalar silence theorem",
        "neutral transport theorem",
        "active no-overlap O",
        "H_curv/H_exch insertability",
        "parent field equation",
    ]
    for item in unknowns:
        print(f"  - {item}")

    with out.unresolved_obligations():
        out.line(
            "Group 23 known unknowns preserved",
            StatusMark.OBLIGATION,
            "Group 23 made matching/support obligations explicit but did not close them",
        )


def case_4_handoffs(options: List[HandoffOption], out: ScriptOutput) -> None:
    header("Case 4: Handoff options")
    for option in options:
        print()
        print("-" * 120)
        print(option.name)
        print("-" * 120)
        print(f"Route: {option.route}")
        print(f"Allowed if: {option.allowed_if}")
        print(f"Caution: {option.caution}")
        print(f"[{status_mark(option.status).value}] {option.name}: {option.status}")

    with out.governance_assessments():
        out.line(
            "Group 23 handoff options recorded",
            StatusMark.PASS,
            "next group should remain narrower than parent closure",
        )


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("The Group 23 summary fails if a later script treats it as proving:")
    print()
    print("1. compact support")
    print("2. no-shell matching")
    print("3. structural support origin")
    print("4. transition layer neutrality")
    print("5. recovery independence")
    print("6. source compatibility")
    print("7. boundary neutrality")
    print("8. scalar silence")
    print("9. active no-overlap O")
    print("10. H insertability")
    print("11. parent equation readiness")
    print()
    print("The summary only licenses this governance result:")
    print()
    print("  matching/support obligations explicit; diagnostics closed; theorems open.")

    with out.governance_assessments():
        out.line(
            "Group 23 overclaim controls stated",
            StatusMark.OBLIGATION,
            "summary must not upgrade requirements into solved matching/support claims",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Group 23 result:")
    print()
    print("  Matching regularity ladder is explicit.")
    print("  Distributional shell dangers are explicit.")
    print("  Compact support admissibility conditions are explicit.")
    print("  Transition layer mass/flux/source/recovery burdens are explicit.")
    print("  Recovery-selected boundary/support/layer parameters remain rejected.")
    print("  Matching/support/layer laws must preserve ordinary source no-double-counting.")
    print("  Matching/support theorem obligations are explicit.")
    print("  Compact support, no-shell matching, transition neutrality, boundary/scalar silence, and parent equation remain not ready.")
    print()
    print("Tiny goblin label:")
    print()
    print("  Seam mapped. Crumbs counted. Door still locked.")

    with out.governance_assessments():
        out.line(
            "Group 23 matching laws status summary complete",
            StatusMark.PASS,
            "Group 23 closes as explicit requirements/diagnostic audit; theorem burden remains open",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_inventory_marker(ns, entries: List[Group23StatusEntry]) -> None:
    ns.record_derivation(
        derivation_id="group23_matching_laws_status_summary_marker_23",
        inputs=[sp.Symbol(entry.name.split(":", 1)[0].replace("-", "_").replace(" ", "_")) for entry in entries],
        output=sp.Symbol("group23_matching_laws_status_summary_stated"),
        method="Group 23 smooth support and matching laws status summary",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="summary_marker",
        scope="Group 23 smooth support and matching laws",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g23_close_support_origin", "Close structural support origin theorem"),
        ("g23_close_value_slope", "Close value/slope matching theorem"),
        ("g23_close_no_shell", "Close distributional shell absence theorem"),
        ("g23_close_layer_neutrality", "Close transition layer neutrality theorem"),
        ("g23_close_recovery_independence", "Close recovery-independent boundary data theorem"),
        ("g23_close_source_compat", "Close source-compatible matching law"),
        ("g23_close_no_repair", "Close no-repair matching/support law"),
        ("g23_keep_parent_closed", "Keep parent equation closed until prerequisites are derived"),
    ]
    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g23_matching_status_summary"],
            description=(
                "Group 23 closes as a requirements/diagnostic audit. This obligation remains open for future theorem work."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g23_close_support_origin",
        "g23_close_value_slope",
        "g23_close_no_shell",
        "g23_close_layer_neutrality",
        "g23_close_recovery_independence",
        "g23_close_source_compat",
        "g23_close_no_repair",
        "g23_keep_parent_closed",
    ]

    ns.record_route(RouteRecord(
        route_id="g23_matching_status_summary",
        script_id=SCRIPT_ID,
        name="Group 23 smooth support and matching laws status summary",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "Group 23 requirements are treated as open theorem obligations",
            "diagnostic results are not upgraded to support laws",
            "repair routes remain rejected",
            "parent equation remains closed",
        ],
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_g23_as_matching_theorem",
        script_id=SCRIPT_ID,
        branch_id="group23_as_matching_theorem",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=obligation_ids,
        description=(
            "Reject treating Group 23 summary as a matching/support, compact-support, or no-shell theorem."
        ),
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_parent_after_g23",
        script_id=SCRIPT_ID,
        branch_id="parent_equation_after_group23",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=obligation_ids,
        description=(
            "Parent equation remains not ready after Group 23 because matching/support obligations remain open."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="g23_summary_requirements_not_theorems",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Group 23 makes smooth support and matching-law requirements explicit, rejects support/matching repair upgrades, "
            "and preserves theorem obligations. It does not prove compact support, no-shell matching, transition neutrality, "
            "boundary neutrality, scalar silence, active O, H insertability, or parent equation readiness."
        ),
        derivation_ids=["group23_matching_laws_status_summary_marker_23"],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Group 23 Matching Laws Status Summary")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    entries = build_status_entries()
    outcomes = build_outcomes()
    options = build_handoffs()

    case_0_problem_statement(out)
    case_1_status_entries(entries, out)
    case_2_closure_outcomes(outcomes, out)
    case_3_known_unknowns(out)
    case_4_handoffs(options, out)
    case_5_failure_controls(out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_inventory_marker(ns, entries)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
