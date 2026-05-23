# Candidate group 26 status summary
#
# Group:
#   26_residual_control_theorem_attempt
#
# Script type:
#   SUMMARY
#
# Purpose
# -------
# Close Group 26 by summarizing the residual-control theorem attempt.
#
# Locked-door question:
#
#   What did the residual-control theorem attempt establish?
#
# This script is not a residual-control theorem.
# It is not residual kill.
# It is not strict inertness.
# It is not zeta/kappa non-reentry.
# It is not epsilon/e_kappa accounting inertness.
# It is not active no-overlap O.
# It is not B_s/F_zeta insertion.
# It is not parent equation closure.
#
# Tiny goblin rule:
#
#   The tunnel is chosen. The treasure is not claimed.

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


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_mark(status: str) -> StatusMark:
    return {
        "CLOSED_DIAGNOSTIC": StatusMark.PASS,
        "CONTROLLED_OBSTRUCTION": StatusMark.DEFER,
        "DEFERRED": StatusMark.DEFER,
        "HANDOFF_READY": StatusMark.PASS,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPTIONAL_OPEN": StatusMark.INFO,
        "PARTIAL_REDUCTION": StatusMark.INFO,
        "PRESERVED": StatusMark.PASS,
        "REJECTED": StatusMark.FAIL,
        "SUMMARY": StatusMark.PASS,
        "THEOREM_TARGET": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "problem_dep_26",
            "026_residual_control_theorem_attempt__candidate_residual_control_theorem_problem_ledger",
            "residual_control_theorem_problem_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "kill_dep_26",
            "026_residual_control_theorem_attempt__candidate_structural_residual_kill_law_attempt",
            "structural_residual_kill_law_attempt_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "inert_dep_26",
            "026_residual_control_theorem_attempt__candidate_nonmetric_inertness_theorem_attempt",
            "nonmetric_inertness_theorem_attempt_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "zk_dep_26",
            "026_residual_control_theorem_attempt__candidate_zeta_kappa_nonreentry_theorem_attempt",
            "zeta_kappa_nonreentry_theorem_attempt_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "acct_dep_26",
            "026_residual_control_theorem_attempt__candidate_epsilon_ekappa_inertness_theorem_attempt",
            "epsilon_ekappa_inertness_theorem_attempt_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "nonO_dep_26",
            "026_residual_control_theorem_attempt__candidate_residual_control_without_active_O_obstruction",
            "residual_control_without_active_O_obstruction_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "O_dep_26",
            "026_residual_control_theorem_attempt__candidate_minimal_O_necessity_or_deferral",
            "minimal_O_necessity_or_deferral_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "consistency_dep_26",
            "026_residual_control_theorem_attempt__candidate_residual_control_boundary_source_recovery_consistency",
            "g26_rc_consistency_marker",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "obligation_dep_26",
            "026_residual_control_theorem_attempt__candidate_residual_control_theorem_attempt_obligations",
            "g26_obligation_status",
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


@dataclass
class SummaryEntry:
    name: str
    result: str
    status: str
    consequence: str


@dataclass
class Handoff:
    name: str
    route: str
    status: str
    reason: str
    guardrail: str


@dataclass
class FinalGate:
    name: str
    status: str
    reason: str


@dataclass
class RejectedSummaryUpgrade:
    name: str
    rejected_upgrade: str
    status: str
    reason: str


def build_summary_entries() -> List[SummaryEntry]:
    return [
        SummaryEntry(
            name="G26-1: theorem target",
            result="L_double target and admissible theorem routes are explicit",
            status="CLOSED_DIAGNOSTIC",
            consequence="the theorem attempt bar is clear",
        ),
        SummaryEntry(
            name="G26-2: direct residual kill",
            result="direct structural L_double = 0 was not derived",
            status="NOT_DERIVED",
            consequence="residual kill remains theorem-targeted",
        ),
        SummaryEntry(
            name="G26-3: strict inertness",
            result="full strict non-metric inertness was not derived",
            status="NOT_DERIVED",
            consequence="sector-by-sector no-reentry remains open",
        ),
        SummaryEntry(
            name="G26-4: zeta/kappa non-reentry",
            result="zeta/kappa geometric residual non-reentry was not derived",
            status="NOT_DERIVED",
            consequence="geometric residuals remain the sharp obstruction",
        ),
        SummaryEntry(
            name="G26-5: epsilon/e_kappa accounting",
            result="accounting pair partially reduced but not derived",
            status="PARTIAL_REDUCTION",
            consequence="accounting discipline is narrower but not full residual control",
        ),
        SummaryEntry(
            name="G26-6: non-O obstruction",
            result="no non-O residual-control route closes under current licensed objects",
            status="CONTROLLED_OBSTRUCTION",
            consequence="obstruction is controlled but not a mathematical no-go theorem",
        ),
        SummaryEntry(
            name="G26-7: active O",
            result="O is optional-open/deferred, not derived, and not proven necessary",
            status="OPTIONAL_OPEN",
            consequence="O is target, not tool",
        ),
        SummaryEntry(
            name="G26-8: guardrail consistency",
            result="current obstruction/handoff state preserves recovery, boundary/source/support, insertion, and parent guardrails",
            status="PRESERVED",
            consequence="handoff is safe but not theorem closure",
        ),
        SummaryEntry(
            name="G26-9: downstream gates",
            result="residual-control, active O, insertion, count-once, and parent gates remain not ready",
            status="NOT_READY",
            consequence="constructive next group is needed",
        ),
    ]


def build_handoffs() -> List[Handoff]:
    return [
        Handoff(
            name="H1: preferred constructive route",
            route="027_active_no_overlap_operator_construction",
            status="HANDOFF_READY",
            reason="non-O residual control did not close, O is optional-open/deferred, and the missing operator route is now the sharp constructive target",
            guardrail="must derive real O structure; O by name remains rejected",
        ),
        Handoff(
            name="H2: alternate constructive route",
            route="027_Bs_Fzeta_coefficient_origin",
            status="HANDOFF_READY",
            reason="zeta residual non-reentry and O deferral may depend on insertion law / coefficient origin",
            guardrail="must keep residual control open; insertion cannot be assumed",
        ),
        Handoff(
            name="H3: safe audit route",
            route="027_reduced_observational_audit",
            status="SAFE_IF",
            reason="can audit consequences without theorem closure",
            guardrail="observations may not select status, O, coefficients, insertion, or parent closure",
        ),
        Handoff(
            name="H4: parent route",
            route="parent_field_equation",
            status="NOT_READY",
            reason="parent closure requires residual control, insertion, source/boundary/support, divergence, and parent identity",
            guardrail="not licensed",
        ),
    ]


def build_gates() -> List[FinalGate]:
    return [
        FinalGate(
            name="residual-control theorem",
            status="NOT_READY",
            reason="direct kill, inertness, and non-reentry did not close",
        ),
        FinalGate(
            name="active O",
            status="NOT_READY",
            reason="optional-open/deferred but not derived",
        ),
        FinalGate(
            name="B_s/F_zeta insertion",
            status="NOT_READY",
            reason="insertion law and coefficient origin remain open",
        ),
        FinalGate(
            name="count-once recombination",
            status="NOT_READY",
            reason="requires residual control and insertion law",
        ),
        FinalGate(
            name="parent equation",
            status="NOT_READY",
            reason="requires residual control, insertion, source/boundary/support, divergence, and parent identity",
        ),
    ]


def build_rejected_upgrades() -> List[RejectedSummaryUpgrade]:
    return [
        RejectedSummaryUpgrade(
            name="U1: summary as theorem",
            rejected_upgrade="treating this summary as residual-control theorem",
            status="REJECTED",
            reason="major theorem routes remain open",
        ),
        RejectedSummaryUpgrade(
            name="U2: controlled obstruction as no-go",
            rejected_upgrade="claiming non-O residual control is mathematically impossible",
            status="REJECTED",
            reason="the obstruction is under current licensed objects only",
        ),
        RejectedSummaryUpgrade(
            name="U3: O optional-open as O derived",
            rejected_upgrade="using O as active operator",
            status="REJECTED",
            reason="O structure is not derived",
        ),
        RejectedSummaryUpgrade(
            name="U4: handoff as construction",
            rejected_upgrade="treating active-O handoff or coefficient-origin handoff as theorem closure",
            status="REJECTED",
            reason="handoff is a route, not result",
        ),
        RejectedSummaryUpgrade(
            name="U5: parent readiness",
            rejected_upgrade="opening parent equation from Group 26",
            status="REJECTED",
            reason="parent gate remains not ready",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Group 26 summary problem")
    print("Question:")
    print()
    print("  What did the residual-control theorem attempt establish?")
    print()
    print("Discipline:")
    print()
    print("  This is a summary, not theorem closure.")
    print("  The summary chooses a next constructive tunnel without claiming the treasure.")

    with out.governance_assessments():
        out.line(
            "Group 26 status summary opened",
            StatusMark.INFO,
            "summarizing residual-control theorem attempt and handoff status",
        )


def case_1_summary_entries(entries: List[SummaryEntry], out: ScriptOutput) -> None:
    header("Case 1: Group 26 status entries")
    for entry in entries:
        print()
        print("-" * 120)
        print(entry.name)
        print("-" * 120)
        print(f"Result: {entry.result}")
        print(f"[{status_mark(entry.status).value}] {entry.name}: {entry.status}")
        print(f"Consequence: {entry.consequence}")

    with out.governance_assessments():
        out.line(
            "Group 26 status entries summarized",
            StatusMark.PASS,
            f"{len(entries)} status entries summarized",
        )


def case_2_handoffs(handoffs: List[Handoff], out: ScriptOutput) -> None:
    header("Case 2: Handoff recommendations")
    for handoff in handoffs:
        print()
        print("-" * 120)
        print(handoff.name)
        print("-" * 120)
        print(f"Route: {handoff.route}")
        print(f"[{status_mark(handoff.status).value}] {handoff.name}: {handoff.status}")
        print(f"Reason: {handoff.reason}")
        print(f"Guardrail: {handoff.guardrail}")

    with out.governance_assessments():
        out.line(
            "Group 26 handoff recommendations summarized",
            StatusMark.PASS,
            "preferred constructive route is active-O construction; coefficient-origin route is also handoff-ready",
        )


def case_3_closure_gates(gates: List[FinalGate], out: ScriptOutput) -> None:
    header("Case 3: Final closure gates")
    for gate in gates:
        print()
        print("-" * 120)
        print(gate.name)
        print("-" * 120)
        print(f"[{status_mark(gate.status).value}] {gate.name}: {gate.status}")
        print(f"Reason: {gate.reason}")

    with out.governance_assessments():
        out.line(
            "Group 26 closure gates remain closed",
            StatusMark.DEFER,
            "residual-control, active O, insertion, count-once, and parent gates remain not ready",
        )


def case_4_rejected_upgrades(upgrades: List[RejectedSummaryUpgrade], out: ScriptOutput) -> None:
    header("Case 4: Rejected summary upgrades")
    for upgrade in upgrades:
        print()
        print("-" * 120)
        print(upgrade.name)
        print("-" * 120)
        print(f"Rejected upgrade: {upgrade.rejected_upgrade}")
        print(f"[{status_mark(upgrade.status).value}] {upgrade.name}: {upgrade.status}")
        print(f"Reason: {upgrade.reason}")

    with out.counterexamples():
        out.line(
            "Group 26 summary upgrades rejected",
            StatusMark.FAIL,
            "summary, obstruction, O classification, handoff, and parent readiness upgrades are rejected",
        )


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("The Group 26 summary fails if a later script allows:")
    print()
    print("1. Group 26 summary treated as residual-control theorem")
    print("2. non-O obstruction treated as mathematical no-go theorem")
    print("3. O optional-open/deferred treated as active O")
    print("4. accounting partial reduction treated as full residual control")
    print("5. active-O handoff treated as O construction")
    print("6. coefficient-origin handoff treated as insertion law")
    print("7. reduced observational audit selects residual status or coefficients")
    print("8. parent equation opened from Group 26")
    print("9. recovery/boundary/source/support selects residual status")
    print("10. O used before full structure is derived")

    with out.governance_assessments():
        out.line(
            "Group 26 summary failure controls stated",
            StatusMark.OBLIGATION,
            "future work must not upgrade summary or handoff to theorem closure",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Group 26 result:")
    print()
    print("  Residual-control theorem attempt did not close residual control.")
    print("  Direct residual kill, strict inertness, and zeta/kappa non-reentry remain not derived.")
    print("  epsilon/e_kappa accounting inertness is only partially reduced.")
    print("  No non-O route closes under current licensed objects.")
    print("  Active O is optional-open/deferred, not derived, and not proven necessary.")
    print("  Current obstruction/handoff state preserves guardrails.")
    print("  Best constructive handoff: 27_active_no_overlap_operator_construction.")
    print("  Alternate constructive handoff: 27_Bs_Fzeta_coefficient_origin.")
    print("  Parent equation remains not ready.")
    print()
    print("Tiny goblin label:")
    print("  The tunnel is chosen. The treasure is not claimed.")

    with out.governance_assessments():
        out.line(
            "Group 26 residual-control theorem attempt summary complete",
            StatusMark.PASS,
            "Group 26 closes as theorem attempt / controlled obstruction with constructive handoff",
        )


def record_derivations(ns) -> None:
    ns.record_derivation(
        derivation_id="g26_status_summary",
        inputs=[
            sp.Symbol("residual_control_not_closed"),
            sp.Symbol("O_optional_open_deferred"),
            sp.Symbol("active_O_handoff_ready"),
            sp.Symbol("Bs_Fzeta_coeff_handoff_ready"),
            sp.Symbol("parent_not_ready"),
        ],
        output=sp.Symbol("g26_summary_complete"),
        method="Group 26 residual-control theorem attempt status summary",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="summary_marker",
        scope="Group 26 residual control theorem attempt",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g26_sum_residual_control_open", "Residual control remains open"),
        ("g26_sum_active_O_open", "Active O construction remains open"),
        ("g26_sum_Bs_coeff_open", "B_s/F_zeta coefficient origin remains open"),
        ("g26_sum_count_once_open", "Count-once recombination remains open"),
        ("g26_sum_parent_closed", "Parent equation remains closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g26_summary_route"],
            description=(
                "Group 26 closes as theorem attempt / controlled obstruction. This obligation remains open for future constructive work."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g26_sum_residual_control_open",
        "g26_sum_active_O_open",
        "g26_sum_Bs_coeff_open",
        "g26_sum_count_once_open",
        "g26_sum_parent_closed",
    ]

    ns.record_route(RouteRecord(
        route_id="g26_summary_route",
        script_id=SCRIPT_ID,
        name="Group 26 residual-control theorem attempt summary",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "Group 26 is treated as theorem attempt / controlled obstruction, not theorem closure",
            "active-O construction and B_s/F_zeta coefficient-origin are handoff-ready",
            "parent equation remains not ready",
        ],
    ))

    for branch_id in [
        "summary_as_theorem",
        "obstruction_as_no_go",
        "O_optional_as_active",
        "accounting_as_control",
        "handoff_as_construction",
        "coeff_handoff_as_insertion",
        "observations_select_status",
        "parent_opened_from_summary",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; Group 26 summary is not theorem closure.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g26_summary_not_theorem",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Group 26 did not derive residual control. It closes as a theorem attempt / controlled obstruction: non-O residual control did not close, "
            "active O is optional-open/deferred and not derived, B_s/F_zeta coefficient origin remains open, and parent equation remains not ready. "
            "The constructive handoff is active-O construction or B_s/F_zeta coefficient-origin work."
        ),
        derivation_ids=["g26_status_summary"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Group 26 Status Summary")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    entries = build_summary_entries()
    handoffs = build_handoffs()
    gates = build_gates()
    upgrades = build_rejected_upgrades()

    case_0_problem_statement(out)
    case_1_summary_entries(entries, out)
    case_2_handoffs(handoffs, out)
    case_3_closure_gates(gates, out)
    case_4_rejected_upgrades(upgrades, out)
    case_5_failure_controls(out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
