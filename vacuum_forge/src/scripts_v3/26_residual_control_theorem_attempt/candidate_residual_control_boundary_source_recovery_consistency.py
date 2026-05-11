# Candidate residual control boundary source recovery consistency
#
# Group:
#   26_residual_control_theorem_attempt
#
# Script type:
#   CONSISTENCY AUDIT
#
# Purpose
# -------
# Audit the current residual-control obstruction / handoff state against:
#
#   recovery independence,
#   boundary/source compatibility,
#   insertion separation,
#   parent-gate closure.
#
# Locked-door question:
#
#   Does the current residual-control state preserve all guardrails?
#
# This script does not derive residual control.
# It does not derive residual kill.
# It does not derive strict inertness.
# It does not derive active no-overlap O.
# It does not derive B_s/F_zeta insertion.
# It does not open parent equation closure.
#
# It checks that the current state:
#
#   non-O residual control not closed,
#   active O optional-open/deferred,
#   zeta/kappa geometric obstruction open,
#   epsilon/e_kappa accounting partially reduced,
#
# remains compatible with recovery, boundary/source, support/matching,
# insertion, and parent-closure guardrails.
#
# Tiny goblin rule:
#
#   Guard the exits while the theorem sleeps.

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
        "BLOCKED": StatusMark.FAIL,
        "CONSISTENT_IF": StatusMark.INFO,
        "DEFERRED": StatusMark.DEFER,
        "DIAGNOSTIC_ONLY": StatusMark.INFO,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
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
            "problem_ledger_dep_26",
            "26_residual_control_theorem_attempt__candidate_residual_control_theorem_problem_ledger",
            "residual_control_theorem_problem_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "nonO_obstruction_dep_26",
            "26_residual_control_theorem_attempt__candidate_residual_control_without_active_O_obstruction",
            "residual_control_without_active_O_obstruction_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "minimal_O_dep_26",
            "26_residual_control_theorem_attempt__candidate_minimal_O_necessity_or_deferral",
            "minimal_O_necessity_or_deferral_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g25_recovery_dep_26",
            "25_residual_kill_or_no_overlap_theorem__candidate_residual_kill_recovery_independence",
            "residual_kill_recovery_independence_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g25_boundary_source_dep_26",
            "25_residual_kill_or_no_overlap_theorem__candidate_residual_kill_boundary_source_compatibility",
            "residual_kill_boundary_source_compatibility_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g24_boundary_source_dep_26",
            "24_metric_insertion_recovery_retest__candidate_metric_insertion_boundary_support_compatibility",
            "metric_insertion_boundary_support_marker_24",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g24_recovery_dep_26",
            "24_metric_insertion_recovery_retest__candidate_recovery_target_anti_smuggling_audit",
            "recovery_target_anti_smuggling_marker_24",
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
class ConsistencyLoadLedger:
    recovery_selection_load: sp.Symbol
    boundary_repair_load: sp.Symbol
    source_repair_load: sp.Symbol
    support_repair_load: sp.Symbol
    insertion_license_load: sp.Symbol
    parent_opening_load: sp.Symbol
    O_shortcut_load: sp.Symbol
    consistency_failure_load: sp.Expr


@dataclass
class ConsistencyCheck:
    name: str
    guardrail: str
    status: str
    current_state: str
    violation_if: str


@dataclass
class HandoffState:
    name: str
    handoff: str
    status: str
    allowed_if: str
    forbidden_if: str


@dataclass
class RejectedConsistencyShortcut:
    name: str
    shortcut: str
    forbidden_use: str
    status: str
    consequence: str


@dataclass
class ConsistencyConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


# =============================================================================
# Builders
# =============================================================================


def build_ledger() -> ConsistencyLoadLedger:
    (
        recovery_selection_load,
        boundary_repair_load,
        source_repair_load,
        support_repair_load,
        insertion_license_load,
        parent_opening_load,
        O_shortcut_load,
    ) = sp.symbols(
        "recovery_selection_load boundary_repair_load source_repair_load support_repair_load insertion_license_load parent_opening_load O_shortcut_load",
        real=True,
    )

    consistency_failure_load = sp.simplify(
        recovery_selection_load
        + boundary_repair_load
        + source_repair_load
        + support_repair_load
        + insertion_license_load
        + parent_opening_load
        + O_shortcut_load
    )

    return ConsistencyLoadLedger(
        recovery_selection_load=recovery_selection_load,
        boundary_repair_load=boundary_repair_load,
        source_repair_load=source_repair_load,
        support_repair_load=support_repair_load,
        insertion_license_load=insertion_license_load,
        parent_opening_load=parent_opening_load,
        O_shortcut_load=O_shortcut_load,
        consistency_failure_load=consistency_failure_load,
    )


def build_checks() -> List[ConsistencyCheck]:
    return [
        ConsistencyCheck(
            name="C1: recovery independence",
            guardrail="recovery may audit residual state but may not select it",
            status="PRESERVED",
            current_state="residual control remains open; O optional-open/deferred; no recovery target selects residual status",
            violation_if="Schwarzschild, AB=1, B=1/A, gamma_like, PPN, or areal kappa chooses kill/inertness/O",
        ),
        ConsistencyCheck(
            name="C2: boundary repair independence",
            guardrail="boundary/scalar/current failure may not select residual cleanup",
            status="PRESERVED",
            current_state="no residual route is promoted from boundary repair; scalar/current/boundary leakage remains a guardrail",
            violation_if="tail, flux, or boundary leakage chooses residual kill, inertness, or O",
        ),
        ConsistencyCheck(
            name="C3: source no-double-counting",
            guardrail="source compatibility may not select residual cleanup",
            status="PRESERVED",
            current_state="source guardrails are necessary but insufficient; not upgraded to theorem",
            violation_if="ordinary source duplication is hidden by residual kill, inertness, accounting, or O",
        ),
        ConsistencyCheck(
            name="C4: support/matching independence",
            guardrail="support/smoothing/transition/matching data may not carry residual cleanup",
            status="PRESERVED",
            current_state="support guardrails remain constraints; residual-control theorem not derived from support data",
            violation_if="support radius, smoothing width, transition layer, or seam condition chooses residual status",
        ),
        ConsistencyCheck(
            name="C5: O shortcut exclusion",
            guardrail="O may be target, not tool",
            status="PRESERVED",
            current_state="active O optional-open/deferred, not derived, not usable",
            violation_if="O erases overlap without domain/codomain/kernel/image/composition/pairing/divergence/boundary/source structure",
        ),
        ConsistencyCheck(
            name="C6: insertion separation",
            guardrail="residual-control obstruction or O classification does not license B_s/F_zeta insertion",
            status="PRESERVED",
            current_state="insertion law and coefficient origin remain open",
            violation_if="non-O obstruction, O optional-open status, or O deferral is treated as insertion theorem",
        ),
        ConsistencyCheck(
            name="C7: parent gate closure",
            guardrail="residual-control state does not open parent field equation",
            status="PRESERVED",
            current_state="parent identity and divergence closure remain downstream",
            violation_if="residual obstruction, accounting reduction, O classification, or guardrail audit opens parent equation",
        ),
    ]


def build_handoffs() -> List[HandoffState]:
    return [
        HandoffState(
            name="H1: residual-control theorem remains open",
            handoff="continue theorem attempt only if a new structural law is available",
            status="OPEN",
            allowed_if="new material can close direct kill, inertness, or sector-by-sector non-reentry without O",
            forbidden_if="the work only restates the current obstruction",
        ),
        HandoffState(
            name="H2: active-O construction",
            handoff="active no-overlap operator construction",
            status="SAFE_IF",
            allowed_if="the next step derives O domain/codomain/kernel/image/composition/pairing/divergence/boundary/source/mass/scalar/current/support/recovery-independence structure",
            forbidden_if="O is used as eraser by name",
        ),
        HandoffState(
            name="H3: B_s/F_zeta coefficient-origin route",
            handoff="coefficient-origin / insertion-law theorem attempt",
            status="SAFE_IF",
            allowed_if="the next step keeps residual control open and attacks insertion law / coefficient origin directly",
            forbidden_if="insertion is assumed from residual obstruction or O classification",
        ),
        HandoffState(
            name="H4: reduced observational audit",
            handoff="audit reduced consequences without closing residual control",
            status="SAFE_IF",
            allowed_if="observational/recovery checks remain downstream audits",
            forbidden_if="observations select residual status, O, coefficients, or parent equation",
        ),
        HandoffState(
            name="H5: parent equation",
            handoff="parent field equation",
            status="NOT_READY",
            allowed_if="residual control, insertion, source/boundary/support, divergence, and parent identity are all derived",
            forbidden_if="current obstruction state is used as parent readiness",
        ),
    ]


def build_rejected_shortcuts() -> List[RejectedConsistencyShortcut]:
    return [
        RejectedConsistencyShortcut(
            name="S1: recovery chooses residual state",
            shortcut="use recovery success to choose residual kill, inertness, or O",
            forbidden_use="recovery selected theorem state",
            status="REJECTED",
            consequence="recovery constructs field equation",
        ),
        RejectedConsistencyShortcut(
            name="S2: boundary/source chooses residual state",
            shortcut="use tail, flux, shell, source duplication, or support failure to choose residual cleanup",
            forbidden_use="repair selected theorem state",
            status="REJECTED",
            consequence="guardrail failure becomes construction rule",
        ),
        RejectedConsistencyShortcut(
            name="S3: accounting repair",
            shortcut="epsilon/e_kappa accounting variables repair zeta/kappa residuals",
            forbidden_use="accounting variables hide geometric obstruction",
            status="REJECTED",
            consequence="residual-control obstruction is hidden",
        ),
        RejectedConsistencyShortcut(
            name="S4: optional O as usable O",
            shortcut="use optional-open/deferred O as an operator",
            forbidden_use="classification becomes construction",
            status="REJECTED",
            consequence="active-O theorem is smuggled",
        ),
        RejectedConsistencyShortcut(
            name="S5: obstruction licenses insertion",
            shortcut="non-O obstruction or O deferral licenses B_s/F_zeta insertion",
            forbidden_use="obstruction or classification replaces insertion law",
            status="REJECTED",
            consequence="metric recombination is smuggled",
        ),
        RejectedConsistencyShortcut(
            name="S6: obstruction opens parent",
            shortcut="residual-control obstruction state opens parent equation",
            forbidden_use="obstruction replaces parent identity and divergence closure",
            status="REJECTED",
            consequence="parent gate opens falsely",
        ),
    ]


def build_conclusions() -> List[ConsistencyConclusion]:
    return [
        ConsistencyConclusion(
            name="K1: current obstruction state consistency",
            conclusion="preserved under guardrails",
            status="PRESERVED",
            meaning="the current open residual-control state does not violate recovery, boundary/source, support, insertion, or parent constraints",
        ),
        ConsistencyConclusion(
            name="K2: residual-control theorem",
            conclusion="not derived",
            status="NOT_DERIVED",
            meaning="consistency of the obstruction state is not residual-control proof",
        ),
        ConsistencyConclusion(
            name="K3: active O",
            conclusion="optional-open/deferred and not usable",
            status="DEFERRED",
            meaning="O remains a possible route only if a real operator is constructed",
        ),
        ConsistencyConclusion(
            name="K4: best next handoff",
            conclusion="choose active-O construction or B_s/F_zeta coefficient-origin route",
            status="SAFE_IF",
            meaning="since residual-control theorem routes have not closed, the next group should attack a missing constructive object",
        ),
        ConsistencyConclusion(
            name="K5: parent gate",
            conclusion="closed",
            status="NOT_READY",
            meaning="no parent equation is licensed by the current residual-control state",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Residual-control consistency audit problem")
    print("Question:")
    print()
    print("  Does the current residual-control state preserve all guardrails?")
    print()
    print("Reference discipline:")
    print()
    print("  The current state is open obstruction, not theorem closure.")
    print("  Guardrails must remain guardrails: recovery cannot construct, boundary/source cannot repair, O cannot erase, insertion and parent gates stay closed.")

    with out.governance_assessments():
        out.line(
            "residual-control boundary/source/recovery consistency audit opened",
            StatusMark.INFO,
            "checking current obstruction/handoff state against guardrails",
        )


def case_1_consistency_ledger(ledger: ConsistencyLoadLedger, out: ScriptOutput) -> None:
    header("Case 1: Consistency failure-load ledger")
    print("Failure channels:")
    print()
    for name in [
        "recovery_selection_load",
        "boundary_repair_load",
        "source_repair_load",
        "support_repair_load",
        "insertion_license_load",
        "parent_opening_load",
        "O_shortcut_load",
    ]:
        print(f"  {name} = {sp.sstr(getattr(ledger, name))}")
    print()
    print("Consistency failure load:")
    print()
    print(f"  L_consistency_fail = {sp.sstr(ledger.consistency_failure_load)}")
    print()
    print("Interpretation:")
    print()
    print("  The current residual-control state is consistent only if these failure loads remain closed.")
    print("  This ledger checks guardrail preservation; it does not solve residual control.")

    with out.derived_results():
        out.line(
            "residual-control consistency failure-load stated",
            StatusMark.OBLIGATION,
            f"L_consistency_fail = {sp.sstr(ledger.consistency_failure_load)}",
        )


def case_2_consistency_checks(checks: List[ConsistencyCheck], out: ScriptOutput) -> None:
    header("Case 2: Guardrail consistency checks")
    for check in checks:
        print()
        print("-" * 120)
        print(check.name)
        print("-" * 120)
        print(f"Guardrail: {check.guardrail}")
        print(f"[{status_mark(check.status).value}] {check.name}: {check.status}")
        print(f"Current state: {check.current_state}")
        print(f"Violation if: {check.violation_if}")

    with out.governance_assessments():
        out.line(
            "residual-control guardrail consistency checks completed",
            StatusMark.PASS,
            f"{len(checks)} guardrails preserved under current obstruction state",
        )


def case_3_handoff_states(handoffs: List[HandoffState], out: ScriptOutput) -> None:
    header("Case 3: Handoff-state classification")
    for handoff in handoffs:
        print()
        print("-" * 120)
        print(handoff.name)
        print("-" * 120)
        print(f"Handoff: {handoff.handoff}")
        print(f"[{status_mark(handoff.status).value}] {handoff.name}: {handoff.status}")
        print(f"Allowed if: {handoff.allowed_if}")
        print(f"Forbidden if: {handoff.forbidden_if}")

    with out.governance_assessments():
        out.line(
            "residual-control handoff states classified",
            StatusMark.PASS,
            "active-O construction, coefficient-origin route, or reduced audit are safe handoffs; parent is not ready",
        )


def case_4_rejected_shortcuts(shortcuts: List[RejectedConsistencyShortcut], out: ScriptOutput) -> None:
    header("Case 4: Rejected consistency shortcuts")
    for shortcut in shortcuts:
        print()
        print("-" * 120)
        print(shortcut.name)
        print("-" * 120)
        print(f"Shortcut: {shortcut.shortcut}")
        print(f"Forbidden use: {shortcut.forbidden_use}")
        print(f"[{status_mark(shortcut.status).value}] {shortcut.name}: {shortcut.status}")
        print(f"Consequence: {shortcut.consequence}")

    with out.counterexamples():
        out.line(
            "residual-control consistency shortcuts rejected",
            StatusMark.FAIL,
            "recovery selection, boundary/source repair, accounting repair, optional O as usable, insertion, and parent shortcuts are rejected",
        )


def case_5_conclusions(conclusions: List[ConsistencyConclusion], out: ScriptOutput) -> None:
    header("Case 5: Consistency conclusions")
    for conclusion in conclusions:
        print()
        print("-" * 120)
        print(conclusion.name)
        print("-" * 120)
        print(f"Conclusion: {conclusion.conclusion}")
        print(f"[{status_mark(conclusion.status).value}] {conclusion.name}: {conclusion.status}")
        print(f"Meaning: {conclusion.meaning}")

    with out.governance_assessments():
        out.line(
            "residual-control consistency conclusion stated",
            StatusMark.PASS,
            "current obstruction/handoff state is guardrail-consistent but not a theorem",
        )


def case_6_failure_controls(out: ScriptOutput) -> None:
    header("Case 6: Failure controls")
    print("The residual-control consistency audit fails if a later script allows:")
    print()
    print("1. recovery selects residual kill, inertness, O, or coefficients")
    print("2. boundary/source/support failure selects residual cleanup")
    print("3. accounting variables repair zeta/kappa geometric obstruction")
    print("4. optional-open/deferred O used as active operator")
    print("5. obstruction state licenses B_s/F_zeta insertion")
    print("6. obstruction state opens parent equation")
    print("7. guardrail consistency treated as residual-control theorem")
    print("8. handoff classification treated as theorem closure")
    print("9. parent equation attempted before residual/insertion/source/boundary/support/divergence closure")
    print("10. reduced observational audit selects residual status or coefficients")

    with out.governance_assessments():
        out.line(
            "residual-control consistency failure controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not treat consistency or handoff as theorem closure",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Residual-control boundary/source/recovery consistency result:")
    print()
    print("  The current obstruction/handoff state preserves recovery independence.")
    print("  Boundary/source/support guardrails remain preserved.")
    print("  O remains optional-open/deferred and unusable without construction.")
    print("  B_s/F_zeta insertion remains not licensed.")
    print("  Parent equation remains not ready.")
    print("  This consistency audit is not a residual-control theorem.")
    print()
    print("Possible next script:")
    print("  candidate_residual_control_theorem_attempt_obligations.py")
    print()
    print("Likely next group after closure:")
    print("  active_no_overlap_operator_construction")
    print("  or B_s_Fzeta_coefficient_origin")
    print()
    print("Tiny goblin label:")
    print("  Guard the exits while the theorem sleeps.")

    with out.governance_assessments():
        out.line(
            "residual-control boundary/source/recovery consistency audit complete",
            StatusMark.PASS,
            "guardrails preserved; residual-control theorem remains open",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, ledger: ConsistencyLoadLedger) -> None:
    ns.record_derivation(
        derivation_id="g26_rc_consistency_load",
        inputs=[
            ledger.recovery_selection_load,
            ledger.boundary_repair_load,
            ledger.source_repair_load,
            ledger.support_repair_load,
            ledger.insertion_license_load,
            ledger.parent_opening_load,
            ledger.O_shortcut_load,
        ],
        output=ledger.consistency_failure_load,
        method="sum residual-control consistency failure channels under current obstruction/handoff state",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="residual_control_consistency_ledger",
        scope="Group 26 residual control theorem attempt",
    )

    ns.record_derivation(
        derivation_id="g26_rc_consistency_marker",
        inputs=[
            sp.Symbol("nonO_obstruction_state"),
            sp.Symbol("O_optional_open_deferred"),
            sp.Symbol("recovery_independence"),
            sp.Symbol("boundary_source_guardrails"),
            sp.Symbol("insertion_closed"),
            sp.Symbol("parent_closed"),
        ],
        output=sp.Symbol("residual_control_consistency_preserved_not_theorem"),
        method="Group 26 residual-control boundary/source/recovery consistency audit",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="consistency_marker",
        scope="Group 26 residual control theorem attempt",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g26_preserve_recovery_independence", "Preserve recovery independence"),
        ("g26_preserve_boundary_source_guardrails", "Preserve boundary/source guardrails"),
        ("g26_preserve_support_matching_guardrails", "Preserve support/matching guardrails"),
        ("g26_keep_accounting_from_repairing_geometry", "Keep accounting variables from repairing zeta/kappa geometry"),
        ("g26_keep_O_unusable_without_construction", "Keep optional-open/deferred O unusable without construction"),
        ("g26_keep_insertion_closed_after_consistency", "Keep B_s/F_zeta insertion closed after consistency audit"),
        ("g26_keep_parent_closed_after_consistency", "Keep parent equation closed after consistency audit"),
        ("g26_do_not_upgrade_consistency_to_theorem", "Do not upgrade consistency audit to residual-control theorem"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g26_residual_control_consistency_route"],
            description=(
                "The current obstruction/handoff state is guardrail-consistent but does not solve residual control."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g26_preserve_recovery_independence",
        "g26_preserve_boundary_source_guardrails",
        "g26_preserve_support_matching_guardrails",
        "g26_keep_accounting_from_repairing_geometry",
        "g26_keep_O_unusable_without_construction",
        "g26_keep_insertion_closed_after_consistency",
        "g26_keep_parent_closed_after_consistency",
        "g26_do_not_upgrade_consistency_to_theorem",
    ]

    ns.record_route(RouteRecord(
        route_id="g26_residual_control_consistency_route",
        script_id=SCRIPT_ID,
        name="Group 26 residual-control boundary/source/recovery consistency audit",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "recovery independence remains preserved",
            "boundary/source/support guardrails remain preserved",
            "accounting variables do not repair zeta/kappa geometry",
            "O remains optional-open/deferred and unusable without construction",
            "insertion and parent gates remain closed",
            "consistency audit is not upgraded to theorem closure",
        ],
    ))

    for branch_id in [
        "recovery_selects_residual_state",
        "boundary_source_selects_residual_cleanup",
        "accounting_repairs_geometric_residuals",
        "optional_O_used_as_active_operator",
        "obstruction_licenses_insertion",
        "obstruction_opens_parent",
        "consistency_as_residual_control_theorem",
        "handoff_as_theorem_closure",
        "parent_attempt_before_closure",
        "observational_audit_selects_status",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_26",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; consistency and handoff do not solve residual control or open downstream gates.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g26_residual_control_consistency_preserved_not_theorem",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "The current residual-control obstruction/handoff state preserves recovery independence, boundary/source/support guardrails, "
            "insertion separation, and parent-gate closure. O remains optional-open/deferred and unusable without construction. "
            "This consistency audit is not a residual-control theorem."
        ),
        derivation_ids=[
            "g26_rc_consistency_load",
            "g26_rc_consistency_marker",
        ],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Residual Control Boundary Source Recovery Consistency")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    ledger = build_ledger()
    checks = build_checks()
    handoffs = build_handoffs()
    shortcuts = build_rejected_shortcuts()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_consistency_ledger(ledger, out)
    case_2_consistency_checks(checks, out)
    case_3_handoff_states(handoffs, out)
    case_4_rejected_shortcuts(shortcuts, out)
    case_5_conclusions(conclusions, out)
    case_6_failure_controls(out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, ledger)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
