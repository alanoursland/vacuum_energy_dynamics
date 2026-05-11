# Candidate residual control theorem attempt obligations
#
# Group:
#   26_residual_control_theorem_attempt
#
# Script type:
#   OBLIGATION / HANDOFF SUMMARY
#
# Purpose
# -------
# Consolidate what the residual-control theorem attempt closed, what remains
# open, and what handoff is now licensed.
#
# Locked-door question:
#
#   What did the theorem attempt close, and what remains open?
#
# This script does not derive residual control.
# It does not derive residual kill.
# It does not derive strict inertness.
# It does not derive zeta/kappa non-reentry.
# It does not derive epsilon/e_kappa accounting inertness.
# It does not derive active no-overlap O.
# It does not derive B_s/F_zeta insertion.
# It does not open parent equation closure.
#
# Tiny goblin rule:
#
#   Count the locked doors before choosing the next tunnel.

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
        "CONTROLLED_OBSTRUCTION": StatusMark.DEFER,
        "DEFERRED": StatusMark.DEFER,
        "HANDOFF_READY": StatusMark.PASS,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "OPTIONAL_OPEN": StatusMark.INFO,
        "PARTIAL_REDUCTION": StatusMark.INFO,
        "PRESERVED": StatusMark.PASS,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "SAFE_IF": StatusMark.INFO,
        "THEOREM_TARGET": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "problem_dep_26",
            "26_residual_control_theorem_attempt__candidate_residual_control_theorem_problem_ledger",
            "residual_control_theorem_problem_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "kill_dep_26",
            "26_residual_control_theorem_attempt__candidate_structural_residual_kill_law_attempt",
            "structural_residual_kill_law_attempt_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "inert_dep_26",
            "26_residual_control_theorem_attempt__candidate_nonmetric_inertness_theorem_attempt",
            "nonmetric_inertness_theorem_attempt_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "zk_dep_26",
            "26_residual_control_theorem_attempt__candidate_zeta_kappa_nonreentry_theorem_attempt",
            "zeta_kappa_nonreentry_theorem_attempt_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "acct_dep_26",
            "26_residual_control_theorem_attempt__candidate_epsilon_ekappa_inertness_theorem_attempt",
            "epsilon_ekappa_inertness_theorem_attempt_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "nonO_dep_26",
            "26_residual_control_theorem_attempt__candidate_residual_control_without_active_O_obstruction",
            "residual_control_without_active_O_obstruction_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "O_dep_26",
            "26_residual_control_theorem_attempt__candidate_minimal_O_necessity_or_deferral",
            "minimal_O_necessity_or_deferral_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "consistency_dep_26",
            "26_residual_control_theorem_attempt__candidate_residual_control_boundary_source_recovery_consistency",
            "g26_rc_consistency_marker",
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
class AttemptStatusEntry:
    name: str
    result: str
    status: str
    consequence: str
    handoff_effect: str


@dataclass
class OpenObligation:
    name: str
    obligation: str
    status: str
    blocks: str
    next_route: str


@dataclass
class HandoffRecommendation:
    name: str
    route: str
    status: str
    why: str
    caution: str


@dataclass
class RejectedUpgrade:
    name: str
    upgrade: str
    status: str
    reason: str


@dataclass
class ClosureGate:
    name: str
    gate: str
    status: str
    opens_if: str


# =============================================================================
# Builders
# =============================================================================


def build_status_entries() -> List[AttemptStatusEntry]:
    return [
        AttemptStatusEntry(
            name="S1: theorem target ledger",
            result="L_double target and admissible theorem routes are explicit",
            status="CLOSED_DIAGNOSTIC",
            consequence="theorem bar is defined",
            handoff_effect="future work cannot count labels, recovery, repair, O-by-name, insertion, or parent shortcuts",
        ),
        AttemptStatusEntry(
            name="S2: direct residual kill",
            result="direct structural L_double = 0 not derived",
            status="NOT_DERIVED",
            consequence="residual kill remains theorem target",
            handoff_effect="do not claim residual kill unless a new structural law appears",
        ),
        AttemptStatusEntry(
            name="S3: strict inertness",
            result="full strict non-metric inertness not derived",
            status="NOT_DERIVED",
            consequence="sector-by-sector no-reentry remains open",
            handoff_effect="do not claim inertness from labels or total cancellation",
        ),
        AttemptStatusEntry(
            name="S4: zeta/kappa non-reentry",
            result="zeta and kappa geometric residual non-reentry not derived",
            status="NOT_DERIVED",
            consequence="geometric residuals remain the sharp obstruction",
            handoff_effect="active O or insertion/coefficient origin may be needed",
        ),
        AttemptStatusEntry(
            name="S5: epsilon/e_kappa accounting inertness",
            result="accounting pair partially reduced but not derived",
            status="PARTIAL_REDUCTION",
            consequence="accounting pair is narrower but cannot close geometry",
            handoff_effect="may remain an accounting theorem target but not full residual control",
        ),
        AttemptStatusEntry(
            name="S6: non-O obstruction",
            result="no non-O residual-control route closes under current licensed objects",
            status="CONTROLLED_OBSTRUCTION",
            consequence="controlled obstruction, not mathematical impossibility",
            handoff_effect="active O classification and insertion/coefficient route become live",
        ),
        AttemptStatusEntry(
            name="S7: minimal O classifier",
            result="O optional-open/deferred, not derived, not proven necessary",
            status="OPTIONAL_OPEN",
            consequence="O is target, not tool",
            handoff_effect="active-O construction is a valid handoff if it derives real structure",
        ),
        AttemptStatusEntry(
            name="S8: consistency audit",
            result="current obstruction/handoff state preserves guardrails",
            status="PRESERVED",
            consequence="recovery, boundary/source/support, insertion, and parent gates remain protected",
            handoff_effect="active-O construction, coefficient-origin route, or reduced audit are safe; parent is not ready",
        ),
    ]


def build_obligations() -> List[OpenObligation]:
    return [
        OpenObligation(
            name="O1: direct residual-kill law",
            obligation="derive L_double = 0 structurally",
            status="OPEN",
            blocks="residual kill and count-once recombination",
            next_route="new structural law only; otherwise do not continue this route",
        ),
        OpenObligation(
            name="O2: strict inertness theorem",
            obligation="derive every L_double entry strictly non-metric, non-sourcing, boundary-neutral, support-neutral, recovery-independent, repair-independent, and parent-independent",
            status="OPEN",
            blocks="non-metric residual survival",
            next_route="sector-by-sector no-reentry theorem or active O",
        ),
        OpenObligation(
            name="O3: zeta residual non-reentry",
            obligation="derive zeta residual cannot re-enter after zeta_to_Bs insertion",
            status="OPEN",
            blocks="count-once scalar trace",
            next_route="B_s/F_zeta insertion law, coefficient origin, or active O",
        ),
        OpenObligation(
            name="O4: kappa residual non-reentry",
            obligation="derive kappa cannot restore residual metric trace or source role",
            status="OPEN",
            blocks="kappa diagnostic/non-metric discipline",
            next_route="kappa non-reentry theorem or active O",
        ),
        OpenObligation(
            name="O5: epsilon/e_kappa accounting inertness",
            obligation="derive accounting-only status with no hidden metric/source/support/boundary/recovery/repair/parent role",
            status="OPEN",
            blocks="clean accounting discipline",
            next_route="accounting theorem target; not sufficient for full residual control",
        ),
        OpenObligation(
            name="O6: active O construction",
            obligation="derive O domain, codomain, kernel, image, composition, pairing/no-overlap, divergence, boundary/source/mass/scalar/current/support behavior, and recovery independence",
            status="OPEN",
            blocks="active no-overlap route",
            next_route="active_no_overlap_operator_construction",
        ),
        OpenObligation(
            name="O7: B_s/F_zeta insertion law",
            obligation="derive insertion law and coefficient origin without selecting residual status",
            status="OPEN",
            blocks="metric recombination and possible O deferral decision",
            next_route="B_s_Fzeta_coefficient_origin",
        ),
        OpenObligation(
            name="O8: parent equation",
            obligation="derive residual control, insertion, source/boundary/support, divergence, and parent identity before parent closure",
            status="NOT_READY",
            blocks="parent field equation",
            next_route="not a valid next group",
        ),
    ]


def build_handoffs() -> List[HandoffRecommendation]:
    return [
        HandoffRecommendation(
            name="H1: active-O construction",
            route="27_active_no_overlap_operator_construction",
            status="HANDOFF_READY",
            why="non-O residual control did not close and O is optional-open/deferred; constructing O would attack the sharp missing operator route",
            caution="must derive real O structure; O by name remains rejected",
        ),
        HandoffRecommendation(
            name="H2: B_s/F_zeta coefficient-origin",
            route="27_Bs_Fzeta_coefficient_origin",
            status="HANDOFF_READY",
            why="zeta residual non-reentry and O deferral may depend on insertion law / coefficient origin",
            caution="must keep residual control open; insertion cannot be assumed from obstruction",
        ),
        HandoffRecommendation(
            name="H3: reduced observational audit",
            route="27_reduced_observational_audit",
            status="SAFE_IF",
            why="could audit consequences without solving residual control",
            caution="observations may not select residual status, O, coefficients, insertion, or parent closure",
        ),
        HandoffRecommendation(
            name="H4: continue residual-control theorem attempt",
            route="continue_26_only_if_new_structural_law",
            status="SAFE_IF",
            why="valid only if genuinely new material can close kill, inertness, or non-reentry",
            caution="do not keep restating the controlled obstruction",
        ),
        HandoffRecommendation(
            name="H5: parent field equation",
            route="parent_field_equation",
            status="NOT_READY",
            why="parent closure requires residual control, insertion, source/boundary/support, divergence, and parent identity",
            caution="not licensed by this theorem attempt",
        ),
    ]


def build_rejected_upgrades() -> List[RejectedUpgrade]:
    return [
        RejectedUpgrade(
            name="R1: theorem attempt becomes residual-control theorem",
            upgrade="treating Group 26 attempt as solved residual control",
            status="REJECTED",
            reason="all major theorem routes remain not derived or only partially reduced",
        ),
        RejectedUpgrade(
            name="R2: non-O obstruction becomes no-go theorem",
            upgrade="claiming active O mathematically necessary",
            status="REJECTED",
            reason="the obstruction is under current licensed objects, not a formal impossibility theorem",
        ),
        RejectedUpgrade(
            name="R3: optional-open O becomes usable O",
            upgrade="using O as an active operator",
            status="REJECTED",
            reason="O structure is not derived",
        ),
        RejectedUpgrade(
            name="R4: accounting partial reduction becomes residual control",
            upgrade="using epsilon/e_kappa accounting reduction to close zeta/kappa geometry",
            status="REJECTED",
            reason="accounting pair does not close the geometric residual obstruction",
        ),
        RejectedUpgrade(
            name="R5: consistency audit becomes theorem",
            upgrade="using guardrail consistency as residual-control proof",
            status="REJECTED",
            reason="consistency only preserves exits; it does not solve the theorem",
        ),
        RejectedUpgrade(
            name="R6: handoff becomes insertion",
            upgrade="using coefficient-origin handoff as B_s/F_zeta insertion law",
            status="REJECTED",
            reason="handoff is not theorem closure",
        ),
        RejectedUpgrade(
            name="R7: handoff becomes parent readiness",
            upgrade="using handoff classification to open parent equation",
            status="REJECTED",
            reason="parent gate remains not ready",
        ),
    ]


def build_closure_gates() -> List[ClosureGate]:
    return [
        ClosureGate(
            name="G1: residual-control theorem gate",
            gate="residual kill / inertness / non-reentry",
            status="NOT_READY",
            opens_if="direct kill, strict inertness, sector-by-sector non-reentry, or active O is actually derived",
        ),
        ClosureGate(
            name="G2: active O gate",
            gate="real no-overlap operator",
            status="NOT_READY",
            opens_if="full operator structure and compatibility behavior are derived",
        ),
        ClosureGate(
            name="G3: B_s/F_zeta insertion gate",
            gate="metric insertion / coefficient origin",
            status="NOT_READY",
            opens_if="insertion law and coefficient origin are derived without selecting residual status",
        ),
        ClosureGate(
            name="G4: count-once recombination gate",
            gate="safe scalar trace recombination",
            status="NOT_READY",
            opens_if="residual control and insertion law are both derived",
        ),
        ClosureGate(
            name="G5: parent field equation gate",
            gate="parent equation closure",
            status="NOT_READY",
            opens_if="residual control, insertion, source/boundary/support, divergence, and parent identity are derived",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Residual-control theorem attempt obligations problem")
    print("Question:")
    print()
    print("  What did the theorem attempt close, and what remains open?")
    print()
    print("Reference discipline:")
    print()
    print("  This is an obligation/handoff summary, not theorem closure.")
    print("  It should choose the next tunnel without pretending a locked door opened.")

    with out.governance_assessments():
        out.line(
            "residual-control theorem-attempt obligations audit opened",
            StatusMark.INFO,
            "summarizing what closed, what remains open, and which handoffs are licensed",
        )


def case_1_status_entries(entries: List[AttemptStatusEntry], out: ScriptOutput) -> None:
    header("Case 1: Theorem-attempt status ledger")
    for entry in entries:
        print()
        print("-" * 120)
        print(entry.name)
        print("-" * 120)
        print(f"Result: {entry.result}")
        print(f"[{status_mark(entry.status).value}] {entry.name}: {entry.status}")
        print(f"Consequence: {entry.consequence}")
        print(f"Handoff effect: {entry.handoff_effect}")

    with out.governance_assessments():
        out.line(
            "residual-control theorem-attempt status ledger populated",
            StatusMark.PASS,
            f"{len(entries)} theorem-attempt statuses summarized",
        )


def case_2_open_obligations(obligations: List[OpenObligation], out: ScriptOutput) -> None:
    header("Case 2: Open residual-control obligations")
    for obligation in obligations:
        print()
        print("-" * 120)
        print(obligation.name)
        print("-" * 120)
        print(f"Obligation: {obligation.obligation}")
        print(f"[{status_mark(obligation.status).value}] {obligation.name}: {obligation.status}")
        print(f"Blocks: {obligation.blocks}")
        print(f"Next route: {obligation.next_route}")

    with out.unresolved_obligations():
        out.line(
            "residual-control open obligations summarized",
            StatusMark.OBLIGATION,
            f"{len(obligations)} obligations remain open or not ready",
        )


def case_3_handoffs(handoffs: List[HandoffRecommendation], out: ScriptOutput) -> None:
    header("Case 3: Handoff recommendations")
    for handoff in handoffs:
        print()
        print("-" * 120)
        print(handoff.name)
        print("-" * 120)
        print(f"Route: {handoff.route}")
        print(f"[{status_mark(handoff.status).value}] {handoff.name}: {handoff.status}")
        print(f"Why: {handoff.why}")
        print(f"Caution: {handoff.caution}")

    with out.governance_assessments():
        out.line(
            "residual-control handoff recommendations stated",
            StatusMark.PASS,
            "active-O construction and B_s/F_zeta coefficient-origin are the main licensed constructive handoffs",
        )


def case_4_rejected_upgrades(upgrades: List[RejectedUpgrade], out: ScriptOutput) -> None:
    header("Case 4: Rejected theorem-attempt upgrades")
    for upgrade in upgrades:
        print()
        print("-" * 120)
        print(upgrade.name)
        print("-" * 120)
        print(f"Rejected upgrade: {upgrade.upgrade}")
        print(f"[{status_mark(upgrade.status).value}] {upgrade.name}: {upgrade.status}")
        print(f"Reason: {upgrade.reason}")

    with out.counterexamples():
        out.line(
            "residual-control theorem-attempt upgrades rejected",
            StatusMark.FAIL,
            "theorem attempt, obstruction, O classification, accounting reduction, consistency audit, and handoffs are not theorem closure",
        )


def case_5_closure_gates(gates: List[ClosureGate], out: ScriptOutput) -> None:
    header("Case 5: Closure gates after theorem attempt")
    for gate in gates:
        print()
        print("-" * 120)
        print(gate.name)
        print("-" * 120)
        print(f"Gate: {gate.gate}")
        print(f"[{status_mark(gate.status).value}] {gate.name}: {gate.status}")
        print(f"Opens if: {gate.opens_if}")

    with out.governance_assessments():
        out.line(
            "residual-control closure gates remain not ready",
            StatusMark.DEFER,
            "residual-control, active O, insertion, count-once, and parent gates remain closed",
        )


def case_6_failure_controls(out: ScriptOutput) -> None:
    header("Case 6: Failure controls")
    print("The residual-control theorem-attempt obligations audit fails if a later script allows:")
    print()
    print("1. theorem attempt treated as residual-control theorem")
    print("2. controlled obstruction treated as mathematical no-go theorem")
    print("3. optional-open/deferred O treated as usable operator")
    print("4. accounting partial reduction treated as full residual control")
    print("5. consistency audit treated as theorem closure")
    print("6. active-O handoff treated as active-O construction")
    print("7. coefficient-origin handoff treated as B_s/F_zeta insertion")
    print("8. reduced observational audit selects residual status or coefficients")
    print("9. handoff classification opens parent equation")
    print("10. parent equation attempted before residual/insertion/source/boundary/support/divergence closure")

    with out.governance_assessments():
        out.line(
            "residual-control theorem-attempt obligation failure controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not treat handoff or obstruction as theorem closure",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Residual-control theorem attempt obligations result:")
    print()
    print("  Direct residual kill did not close.")
    print("  Full strict inertness did not close.")
    print("  Zeta/kappa geometric non-reentry did not close.")
    print("  epsilon/e_kappa accounting inertness only partially reduced.")
    print("  No non-O residual-control route closed under current licensed objects.")
    print("  Active O is optional-open/deferred, not derived, and not proven necessary.")
    print("  The current obstruction/handoff state preserves guardrails.")
    print("  B_s/F_zeta insertion remains not ready.")
    print("  Parent equation remains not ready.")
    print()
    print("Best next group options:")
    print("  27_active_no_overlap_operator_construction")
    print("  27_Bs_Fzeta_coefficient_origin")
    print()
    print("Preferred next group if choosing a constructive route:")
    print("  27_active_no_overlap_operator_construction")
    print()
    print("Tiny goblin label:")
    print("  Count the locked doors before choosing the next tunnel.")

    with out.governance_assessments():
        out.line(
            "residual-control theorem-attempt obligations audit complete",
            StatusMark.PASS,
            "theorem attempt summarized; constructive handoff is active-O construction or B_s/F_zeta coefficient origin",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns) -> None:
    ns.record_derivation(
        derivation_id="g26_obligation_status",
        inputs=[
            sp.Symbol("direct_kill_not_derived"),
            sp.Symbol("strict_inertness_not_derived"),
            sp.Symbol("zeta_kappa_nonreentry_not_derived"),
            sp.Symbol("accounting_partial_only"),
            sp.Symbol("nonO_controlled_obstruction"),
            sp.Symbol("O_optional_open_deferred"),
            sp.Symbol("consistency_preserved"),
        ],
        output=sp.Symbol("g26_residual_control_attempt_obligations_open"),
        method="Group 26 residual-control theorem attempt obligation and handoff summary",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="obligation_summary_marker",
        scope="Group 26 residual control theorem attempt",
        is_placeholder=True,
    )

    ns.record_derivation(
        derivation_id="g26_handoff_status",
        inputs=[
            sp.Symbol("active_O_construction"),
            sp.Symbol("Bs_Fzeta_coefficient_origin"),
            sp.Symbol("reduced_observational_audit"),
            sp.Symbol("parent_not_ready"),
        ],
        output=sp.Symbol("g26_constructive_handoff_ready"),
        method="Classify Group 26 handoff options after residual-control theorem attempt",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="handoff_summary",
        scope="Group 26 residual control theorem attempt",
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g26_o1_kill_law", "Residual kill law remains open"),
        ("g26_o2_inert_law", "Strict inertness theorem remains open"),
        ("g26_o3_zeta_reentry", "Zeta residual non-reentry remains open"),
        ("g26_o4_kappa_reentry", "Kappa residual non-reentry remains open"),
        ("g26_o5_accounting", "epsilon/e_kappa accounting inertness remains open"),
        ("g26_o6_active_O", "Active O construction remains open"),
        ("g26_o7_Bs_coeff", "B_s/F_zeta insertion law and coefficient origin remain open"),
        ("g26_o8_parent_closed", "Parent equation remains not ready"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g26_obligation_route"],
            description=(
                "Group 26 theorem attempt did not close this obligation. Future constructive work must close it directly or keep the gate closed."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g26_o1_kill_law",
        "g26_o2_inert_law",
        "g26_o3_zeta_reentry",
        "g26_o4_kappa_reentry",
        "g26_o5_accounting",
        "g26_o6_active_O",
        "g26_o7_Bs_coeff",
        "g26_o8_parent_closed",
    ]

    ns.record_route(RouteRecord(
        route_id="g26_obligation_route",
        script_id=SCRIPT_ID,
        name="Group 26 residual-control theorem-attempt obligation summary",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "Group 26 theorem attempt is treated as obligation/handoff summary, not theorem closure",
            "direct kill, inertness, zeta/kappa non-reentry, accounting inertness, active O, and insertion remain open",
            "parent gate remains closed",
            "constructive handoff targets active-O construction or B_s/F_zeta coefficient origin",
        ],
    ))

    for branch_id in [
        "attempt_as_theorem",
        "obstruction_as_no_go",
        "optional_O_as_operator",
        "accounting_as_control",
        "consistency_as_theorem",
        "active_O_handoff_as_constructed",
        "coeff_handoff_as_insertion",
        "observation_selects_status",
        "handoff_opens_parent",
        "parent_before_closure",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; Group 26 obligation/handoff summary does not close residual control or downstream gates.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g26_obligations_open_handoff_ready",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Group 26 theorem attempt did not derive residual control. Direct kill, strict inertness, zeta/kappa non-reentry, accounting inertness, "
            "active O, and B_s/F_zeta insertion remain open; parent equation remains not ready. "
            "The constructive handoff is active-O construction or B_s/F_zeta coefficient-origin work, while reduced observational audit remains safe if downstream-only."
        ),
        derivation_ids=[
            "g26_obligation_status",
            "g26_handoff_status",
        ],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Residual Control Theorem Attempt Obligations")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    entries = build_status_entries()
    obligations = build_obligations()
    handoffs = build_handoffs()
    upgrades = build_rejected_upgrades()
    gates = build_closure_gates()

    case_0_problem_statement(out)
    case_1_status_entries(entries, out)
    case_2_open_obligations(obligations, out)
    case_3_handoffs(handoffs, out)
    case_4_rejected_upgrades(upgrades, out)
    case_5_closure_gates(gates, out)
    case_6_failure_controls(out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
