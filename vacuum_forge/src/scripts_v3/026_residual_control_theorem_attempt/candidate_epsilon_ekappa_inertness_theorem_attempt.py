# Candidate epsilon e_kappa inertness theorem attempt
#
# Group:
#   26_residual_control_theorem_attempt
#
# Script type:
#   THEOREM ATTEMPT
#
# Purpose
# -------
# Test whether epsilon_vac_metric and e_kappa_metric can be proven
# accounting-only / inert under current guardrails.
#
# Locked-door question:
#
#   Can epsilon_vac_config and e_kappa be kept as accounting-only objects?
#
# This script does not derive B_s/F_zeta insertion.
# It does not derive active no-overlap O.
# It does not derive parent equation closure.
#
# It focuses on the accounting pair:
#
#   epsilon_vac_metric
#   e_kappa_metric
#
# because the prior direct-kill and strict-inertness attempts found partial
# reductions for these entries, while zeta/kappa remain the sharper geometric
# obstruction.
#
# Tiny goblin rule:
#
#   Accounting is not a secret purse.

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
        "ACCOUNTING_TARGET": StatusMark.OBLIGATION,
        "BLOCKED": StatusMark.FAIL,
        "CONDITIONALLY_REDUCED": StatusMark.INFO,
        "CONDITIONALLY_SAFE": StatusMark.INFO,
        "DIAGNOSTIC_ONLY": StatusMark.INFO,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "PARTIAL_REDUCTION": StatusMark.INFO,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "SAFE_IF": StatusMark.INFO,
        "THEOREM_ATTEMPT": StatusMark.DEFER,
        "THEOREM_TARGET": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "problem_ledger_dep_26",
            "026_residual_control_theorem_attempt__candidate_residual_control_theorem_problem_ledger",
            "residual_control_theorem_problem_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "structural_kill_dep_26",
            "026_residual_control_theorem_attempt__candidate_structural_residual_kill_law_attempt",
            "structural_residual_kill_law_attempt_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "inertness_attempt_dep_26",
            "026_residual_control_theorem_attempt__candidate_nonmetric_inertness_theorem_attempt",
            "nonmetric_inertness_theorem_attempt_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "zeta_kappa_dep_26",
            "026_residual_control_theorem_attempt__candidate_zeta_kappa_nonreentry_theorem_attempt",
            "zeta_kappa_nonreentry_theorem_attempt_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g25_boundary_source_dep_26",
            "025_residual_kill_or_no_overlap_theorem__candidate_residual_kill_boundary_source_compatibility",
            "residual_kill_boundary_source_compatibility_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g25_summary_dep_26",
            "025_residual_kill_or_no_overlap_theorem__candidate_group_25_residual_kill_status_summary",
            "group25_residual_kill_status_summary_marker_25",
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
class AccountingInertnessLedger:
    epsilon_metric_role: sp.Symbol
    epsilon_source_role: sp.Symbol
    epsilon_boundary_role: sp.Symbol
    epsilon_support_role: sp.Symbol
    epsilon_recovery_role: sp.Symbol
    epsilon_repair_role: sp.Symbol
    epsilon_parent_role: sp.Symbol
    e_kappa_metric_role: sp.Symbol
    e_kappa_source_role: sp.Symbol
    e_kappa_trace_restore_role: sp.Symbol
    e_kappa_boundary_role: sp.Symbol
    e_kappa_support_role: sp.Symbol
    e_kappa_recovery_role: sp.Symbol
    e_kappa_repair_role: sp.Symbol
    e_kappa_parent_role: sp.Symbol
    epsilon_accounting_failure: sp.Expr
    e_kappa_accounting_failure: sp.Expr
    accounting_failure_total: sp.Expr


@dataclass
class AccountingResidualAttempt:
    name: str
    residual: str
    target: str
    status: str
    current_support: str
    missing_theorem: str


@dataclass
class AccountingChannelTest:
    name: str
    channel: str
    epsilon_status: str
    e_kappa_status: str
    epsilon_result: str
    e_kappa_result: str


@dataclass
class RejectedAccountingShortcut:
    name: str
    shortcut: str
    forbidden_use: str
    status: str
    consequence: str


@dataclass
class AccountingInertnessConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


# =============================================================================
# Builders
# =============================================================================


def build_ledger() -> AccountingInertnessLedger:
    (
        epsilon_metric_role,
        epsilon_source_role,
        epsilon_boundary_role,
        epsilon_support_role,
        epsilon_recovery_role,
        epsilon_repair_role,
        epsilon_parent_role,
        e_kappa_metric_role,
        e_kappa_source_role,
        e_kappa_trace_restore_role,
        e_kappa_boundary_role,
        e_kappa_support_role,
        e_kappa_recovery_role,
        e_kappa_repair_role,
        e_kappa_parent_role,
    ) = sp.symbols(
        "epsilon_metric_role epsilon_source_role epsilon_boundary_role epsilon_support_role epsilon_recovery_role epsilon_repair_role epsilon_parent_role "
        "e_kappa_metric_role e_kappa_source_role e_kappa_trace_restore_role e_kappa_boundary_role e_kappa_support_role e_kappa_recovery_role e_kappa_repair_role e_kappa_parent_role",
        real=True,
    )

    epsilon_accounting_failure = sp.simplify(
        epsilon_metric_role
        + epsilon_source_role
        + epsilon_boundary_role
        + epsilon_support_role
        + epsilon_recovery_role
        + epsilon_repair_role
        + epsilon_parent_role
    )

    e_kappa_accounting_failure = sp.simplify(
        e_kappa_metric_role
        + e_kappa_source_role
        + e_kappa_trace_restore_role
        + e_kappa_boundary_role
        + e_kappa_support_role
        + e_kappa_recovery_role
        + e_kappa_repair_role
        + e_kappa_parent_role
    )

    accounting_failure_total = sp.simplify(epsilon_accounting_failure + e_kappa_accounting_failure)

    return AccountingInertnessLedger(
        epsilon_metric_role=epsilon_metric_role,
        epsilon_source_role=epsilon_source_role,
        epsilon_boundary_role=epsilon_boundary_role,
        epsilon_support_role=epsilon_support_role,
        epsilon_recovery_role=epsilon_recovery_role,
        epsilon_repair_role=epsilon_repair_role,
        epsilon_parent_role=epsilon_parent_role,
        e_kappa_metric_role=e_kappa_metric_role,
        e_kappa_source_role=e_kappa_source_role,
        e_kappa_trace_restore_role=e_kappa_trace_restore_role,
        e_kappa_boundary_role=e_kappa_boundary_role,
        e_kappa_support_role=e_kappa_support_role,
        e_kappa_recovery_role=e_kappa_recovery_role,
        e_kappa_repair_role=e_kappa_repair_role,
        e_kappa_parent_role=e_kappa_parent_role,
        epsilon_accounting_failure=epsilon_accounting_failure,
        e_kappa_accounting_failure=e_kappa_accounting_failure,
        accounting_failure_total=accounting_failure_total,
    )


def build_residual_attempts() -> List[AccountingResidualAttempt]:
    return [
        AccountingResidualAttempt(
            name="A1: epsilon_vac accounting-only inertness",
            residual="epsilon_vac_metric",
            target="epsilon_vac_config remains configuration/accounting only and carries no metric/source/support/boundary/recovery/repair/parent role",
            status="PARTIAL_REDUCTION",
            current_support="energy/accounting guardrail and no extra metric/source channel rule",
            missing_theorem="formal accounting-only theorem that removes all ordinary metric/source/support/boundary/recovery/repair/parent roles",
        ),
        AccountingResidualAttempt(
            name="A2: e_kappa accounting-only inertness",
            residual="e_kappa_metric",
            target="e_kappa remains kappa accounting only and cannot restore trace, carry source, tune recovery, or fill parent role",
            status="PARTIAL_REDUCTION",
            current_support="kappa accounting guardrail and no source-channel rule",
            missing_theorem="formal kappa-accounting theorem: no trace restoration, no source reservoir, no recovery tuning, no repair/parent role",
        ),
        AccountingResidualAttempt(
            name="A3: accounting pair separation from zeta/kappa geometry",
            residual="epsilon_vac_metric + e_kappa_metric",
            target="accounting residuals do not repair or hide the unresolved zeta/kappa geometric residuals",
            status="NOT_DERIVED",
            current_support="guardrails reject accounting as hidden source/metric reservoir",
            missing_theorem="separation theorem between accounting variables and geometric trace residuals",
        ),
    ]


def build_channel_tests() -> List[AccountingChannelTest]:
    return [
        AccountingChannelTest(
            name="C1: metric role",
            channel="metric",
            epsilon_status="NOT_DERIVED",
            e_kappa_status="NOT_DERIVED",
            epsilon_result="extra metric-channel role is rejected, but epsilon metric absence is not derived",
            e_kappa_result="e_kappa metric-channel role is rejected, but e_kappa metric absence is not derived",
        ),
        AccountingChannelTest(
            name="C2: source role",
            channel="source",
            epsilon_status="CONDITIONALLY_REDUCED",
            e_kappa_status="CONDITIONALLY_REDUCED",
            epsilon_result="source reservoir use is rejected, but no-source theorem is not derived",
            e_kappa_result="source reservoir use is rejected, but no-source theorem is not derived",
        ),
        AccountingChannelTest(
            name="C3: trace restoration role",
            channel="trace_restore",
            epsilon_status="CONDITIONALLY_REDUCED",
            e_kappa_status="NOT_DERIVED",
            epsilon_result="epsilon should not restore trace, but no formal theorem is derived",
            e_kappa_result="e_kappa cannot be allowed to restore kappa/zeta trace, but theorem is not derived",
        ),
        AccountingChannelTest(
            name="C4: boundary / scalar / current role",
            channel="boundary_scalar_current",
            epsilon_status="NOT_DERIVED",
            e_kappa_status="NOT_DERIVED",
            epsilon_result="boundary repair use is rejected, but epsilon boundary silence is not derived",
            e_kappa_result="boundary repair use is rejected, but e_kappa boundary silence is not derived",
        ),
        AccountingChannelTest(
            name="C5: support / layer role",
            channel="support_layer",
            epsilon_status="NOT_DERIVED",
            e_kappa_status="NOT_DERIVED",
            epsilon_result="support/layer hiding is rejected, but support-neutral theorem is not derived",
            e_kappa_result="support/layer hiding is rejected, but support-neutral theorem is not derived",
        ),
        AccountingChannelTest(
            name="C6: recovery tuning role",
            channel="recovery",
            epsilon_status="CONDITIONALLY_REDUCED",
            e_kappa_status="CONDITIONALLY_REDUCED",
            epsilon_result="recovery selection is rejected, but structural accounting status is not derived",
            e_kappa_result="recovery selection is rejected, but structural accounting status is not derived",
        ),
        AccountingChannelTest(
            name="C7: repair role",
            channel="repair",
            epsilon_status="CONDITIONALLY_REDUCED",
            e_kappa_status="CONDITIONALLY_REDUCED",
            epsilon_result="repair-label use is rejected, but repair-independence theorem is not derived",
            e_kappa_result="repair-label use is rejected, but repair-independence theorem is not derived",
        ),
        AccountingChannelTest(
            name="C8: parent placeholder role",
            channel="parent",
            epsilon_status="CONDITIONALLY_REDUCED",
            e_kappa_status="CONDITIONALLY_REDUCED",
            epsilon_result="parent placeholder use is rejected, but non-parent theorem is not derived",
            e_kappa_result="parent placeholder use is rejected, but non-parent theorem is not derived",
        ),
    ]


def build_rejected_shortcuts() -> List[RejectedAccountingShortcut]:
    return [
        RejectedAccountingShortcut(
            name="S1: accounting label as theorem",
            shortcut="call epsilon_vac/e_kappa accounting-only",
            forbidden_use="accounting vocabulary substitutes for inertness theorem",
            status="REJECTED",
            consequence="hidden metric/source/support role remains possible",
        ),
        RejectedAccountingShortcut(
            name="S2: accounting reservoir",
            shortcut="use epsilon_vac/e_kappa as hidden energy, source, or metric reservoir",
            forbidden_use="accounting variable carries ordinary physical load",
            status="REJECTED",
            consequence="source and metric no-double-counting fail",
        ),
        RejectedAccountingShortcut(
            name="S3: e_kappa trace restoration",
            shortcut="use e_kappa to restore killed kappa/zeta trace",
            forbidden_use="accounting object reintroduces geometric residual",
            status="REJECTED",
            consequence="residual-control theorem is bypassed",
        ),
        RejectedAccountingShortcut(
            name="S4: epsilon_vac configuration repair",
            shortcut="use epsilon_vac_config to repair boundary/source/support failure",
            forbidden_use="configuration accounting becomes repair object",
            status="REJECTED",
            consequence="boundary/source compatibility is smuggled",
        ),
        RejectedAccountingShortcut(
            name="S5: recovery-tuned accounting",
            shortcut="choose accounting inertness from recovery success",
            forbidden_use="recovery selects accounting status",
            status="REJECTED",
            consequence="recovery constructs residual control",
        ),
        RejectedAccountingShortcut(
            name="S6: accounting hides geometric residuals",
            shortcut="use epsilon/e_kappa cancellation to hide zeta/kappa reentry",
            forbidden_use="accounting pair cancels geometric residuals only in total",
            status="REJECTED",
            consequence="unsafe geometric reentry remains",
        ),
        RejectedAccountingShortcut(
            name="S7: accounting licenses insertion",
            shortcut="accounting inertness licenses B_s/F_zeta insertion",
            forbidden_use="accounting theorem replaces insertion law or coefficient origin",
            status="REJECTED",
            consequence="metric insertion is smuggled",
        ),
        RejectedAccountingShortcut(
            name="S8: accounting opens parent",
            shortcut="accounting inertness opens parent equation",
            forbidden_use="accounting theorem replaces parent identity and divergence closure",
            status="REJECTED",
            consequence="parent equation is smuggled",
        ),
    ]


def build_conclusions() -> List[AccountingInertnessConclusion]:
    return [
        AccountingInertnessConclusion(
            name="C1: epsilon_vac accounting inertness",
            conclusion="partially reduced but not derived",
            status="PARTIAL_REDUCTION",
            meaning="epsilon_vac_metric is a plausible accounting-only theorem target, but no full no-role theorem is derived",
        ),
        AccountingInertnessConclusion(
            name="C2: e_kappa accounting inertness",
            conclusion="partially reduced but not derived",
            status="PARTIAL_REDUCTION",
            meaning="e_kappa_metric is a plausible accounting-only theorem target, but no trace/source/recovery no-role theorem is derived",
        ),
        AccountingInertnessConclusion(
            name="C3: accounting pair does not close residual control",
            conclusion="accounting inertness, even if later derived, would not close zeta/kappa geometric non-reentry by itself",
            status="SAFE_IF",
            meaning="the sharper obstruction remains geometric unless zeta/kappa or active O is solved",
        ),
        AccountingInertnessConclusion(
            name="C4: non-O residual control status",
            conclusion="direct kill, full inertness, and zeta/kappa non-reentry are not derived; accounting pair only partially reduces",
            status="NOT_READY",
            meaning="the next script should test whether any non-O residual-control route closes under current licensed objects",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Epsilon/e_kappa accounting inertness theorem attempt problem")
    print("Question:")
    print()
    print("  Can epsilon_vac_config and e_kappa be kept as accounting-only objects?")
    print()
    print("Reference discipline:")
    print()
    print("  Accounting is not a secret purse.")
    print("  epsilon_vac and e_kappa may not restore trace, carry source, repair boundary/support failure, tune recovery, or fill parent placeholders.")
    print("  Even successful accounting inertness would not by itself close zeta/kappa geometric residual non-reentry.")

    with out.governance_assessments():
        out.line(
            "epsilon/e_kappa accounting inertness theorem attempt opened",
            StatusMark.INFO,
            "testing whether accounting residuals can be isolated after geometric non-reentry remained open",
        )


def case_1_accounting_ledger(ledger: AccountingInertnessLedger, out: ScriptOutput) -> None:
    header("Case 1: Accounting inertness failure ledger")
    print("epsilon_vac accounting failure load:")
    print()
    print(f"  L_epsilon_accounting_fail = {sp.sstr(ledger.epsilon_accounting_failure)}")
    print()
    print("e_kappa accounting failure load:")
    print()
    print(f"  L_e_kappa_accounting_fail = {sp.sstr(ledger.e_kappa_accounting_failure)}")
    print()
    print("Total accounting failure load:")
    print()
    print(f"  L_accounting_fail = {sp.sstr(ledger.accounting_failure_total)}")
    print()
    print("Interpretation:")
    print()
    print("  Accounting-only status requires every role load to vanish sector-by-sector.")
    print("  Accounting labels do not close these loads by themselves.")

    with out.derived_results():
        out.line(
            "epsilon_vac accounting failure load stated",
            StatusMark.OBLIGATION,
            f"L_epsilon_accounting_fail = {sp.sstr(ledger.epsilon_accounting_failure)}",
        )
        out.line(
            "e_kappa accounting failure load stated",
            StatusMark.OBLIGATION,
            f"L_e_kappa_accounting_fail = {sp.sstr(ledger.e_kappa_accounting_failure)}",
        )
        out.line(
            "total accounting failure load stated",
            StatusMark.OBLIGATION,
            f"L_accounting_fail = {sp.sstr(ledger.accounting_failure_total)}",
        )


def case_2_residual_attempts(attempts: List[AccountingResidualAttempt], out: ScriptOutput) -> None:
    header("Case 2: Accounting residual inertness attempts")
    for attempt in attempts:
        print()
        print("-" * 120)
        print(attempt.name)
        print("-" * 120)
        print(f"Residual: {attempt.residual}")
        print(f"Target: {attempt.target}")
        print(f"[{status_mark(attempt.status).value}] {attempt.name}: {attempt.status}")
        print(f"Current support: {attempt.current_support}")
        print(f"Missing theorem: {attempt.missing_theorem}")

    with out.unresolved_obligations():
        out.line(
            "accounting residual inertness attempts classified",
            StatusMark.OBLIGATION,
            f"{len(attempts)} accounting residual attempts tested; full accounting inertness not derived",
        )


def case_3_channel_tests(tests: List[AccountingChannelTest], out: ScriptOutput) -> None:
    header("Case 3: Accounting role channel tests")
    for test in tests:
        print()
        print("-" * 120)
        print(test.name)
        print("-" * 120)
        print(f"Channel: {test.channel}")
        print(f"[{status_mark(test.epsilon_status).value}] epsilon_vac: {test.epsilon_status}")
        print(f"  epsilon result: {test.epsilon_result}")
        print(f"[{status_mark(test.e_kappa_status).value}] e_kappa: {test.e_kappa_status}")
        print(f"  e_kappa result: {test.e_kappa_result}")

    with out.governance_assessments():
        out.line(
            "accounting role channels tested",
            StatusMark.PASS,
            f"{len(tests)} accounting channels evaluated; full accounting inertness remains open",
        )


def case_4_rejected_shortcuts(shortcuts: List[RejectedAccountingShortcut], out: ScriptOutput) -> None:
    header("Case 4: Rejected accounting inertness shortcuts")
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
            "accounting inertness shortcuts rejected",
            StatusMark.FAIL,
            "accounting label, reservoir use, trace restoration, repair, recovery tuning, geometric cancellation, insertion, and parent shortcuts are rejected",
        )


def case_5_conclusions(conclusions: List[AccountingInertnessConclusion], out: ScriptOutput) -> None:
    header("Case 5: Accounting inertness conclusions")
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
            "accounting inertness theorem-attempt conclusion stated",
            StatusMark.DEFER,
            "accounting entries partially reduced; full residual control remains open",
        )


def case_6_failure_controls(out: ScriptOutput) -> None:
    header("Case 6: Failure controls")
    print("The epsilon/e_kappa accounting inertness theorem attempt fails if a later script allows:")
    print()
    print("1. accounting-only status by vocabulary")
    print("2. epsilon_vac or e_kappa as hidden metric/source reservoir")
    print("3. e_kappa restores kappa/zeta trace")
    print("4. epsilon_vac_config repairs boundary/source/support failure")
    print("5. accounting status selected from recovery")
    print("6. accounting variables hide zeta/kappa geometric residuals")
    print("7. accounting total cancellation treated as non-reentry")
    print("8. accounting inertness licenses B_s/F_zeta insertion")
    print("9. accounting inertness opens parent equation")
    print("10. accounting inertness treated as full residual control while zeta/kappa remain unresolved")

    with out.governance_assessments():
        out.line(
            "accounting inertness failure controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not convert accounting labels into residual-control theorem",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("epsilon/e_kappa accounting inertness theorem attempt result:")
    print()
    print("  epsilon_vac_metric is partially reduced to an accounting-only inertness theorem target, but not derived.")
    print("  e_kappa_metric is partially reduced to an accounting-only inertness theorem target, but not derived.")
    print("  Accounting labels cannot carry hidden metric/source/support/boundary/recovery/repair/parent roles.")
    print("  Accounting inertness, even if later derived, would not close zeta/kappa geometric non-reentry by itself.")
    print("  Non-O residual control remains open.")
    print("  B_s/F_zeta insertion and parent closure remain not ready.")
    print()
    print("Possible next script:")
    print("  candidate_residual_control_without_active_O_obstruction.py")
    print()
    print("Tiny goblin label:")
    print("  Accounting is not a secret purse.")

    with out.governance_assessments():
        out.line(
            "epsilon/e_kappa accounting inertness theorem attempt complete",
            StatusMark.PASS,
            "accounting pair partially reduced; non-O residual-control obstruction should be tested next",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, ledger: AccountingInertnessLedger) -> None:
    ns.record_derivation(
        derivation_id="epsilon_ekappa_accounting_failure_load_26",
        inputs=[
            ledger.epsilon_accounting_failure,
            ledger.e_kappa_accounting_failure,
        ],
        output=ledger.accounting_failure_total,
        method="sum accounting-role failure channels for epsilon_vac and e_kappa",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="epsilon_ekappa_accounting_inertness_attempt_ledger",
        scope="Group 26 residual control theorem attempt",
    )

    ns.record_derivation(
        derivation_id="epsilon_ekappa_inertness_theorem_attempt_marker_26",
        inputs=[
            sp.Symbol("epsilon_vac_metric"),
            sp.Symbol("e_kappa_metric"),
            sp.Symbol("accounting_role_channels"),
        ],
        output=sp.Symbol("epsilon_ekappa_accounting_inertness_not_derived"),
        method="Group 26 epsilon/e_kappa accounting inertness theorem attempt",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="theorem_attempt_marker",
        scope="Group 26 residual control theorem attempt",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g26_epsilon_no_metric_source_role", "Derive epsilon_vac no metric/source role"),
        ("g26_epsilon_no_boundary_support_role", "Derive epsilon_vac no boundary/support role"),
        ("g26_epsilon_no_recovery_repair_parent_role", "Derive epsilon_vac no recovery/repair/parent role"),
        ("g26_ekappa_no_metric_source_trace_restore", "Derive e_kappa no metric/source/trace-restoration role"),
        ("g26_ekappa_no_boundary_support_role", "Derive e_kappa no boundary/support role"),
        ("g26_ekappa_no_recovery_repair_parent_role", "Derive e_kappa no recovery/repair/parent role"),
        ("g26_accounting_not_geometric_residual_repair", "Keep accounting variables from repairing zeta/kappa residuals"),
        ("g26_keep_insertion_parent_closed_after_accounting_attempt", "Keep insertion and parent gates closed after accounting attempt"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g26_epsilon_ekappa_accounting_inertness_attempt_route"],
            description=(
                "epsilon/e_kappa accounting inertness is only partially reduced here. Future work must prove no hidden roles sector-by-sector."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g26_epsilon_no_metric_source_role",
        "g26_epsilon_no_boundary_support_role",
        "g26_epsilon_no_recovery_repair_parent_role",
        "g26_ekappa_no_metric_source_trace_restore",
        "g26_ekappa_no_boundary_support_role",
        "g26_ekappa_no_recovery_repair_parent_role",
        "g26_accounting_not_geometric_residual_repair",
        "g26_keep_insertion_parent_closed_after_accounting_attempt",
    ]

    ns.record_route(RouteRecord(
        route_id="g26_epsilon_ekappa_accounting_inertness_attempt_route",
        script_id=SCRIPT_ID,
        name="Group 26 epsilon/e_kappa accounting inertness theorem attempt",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "epsilon_vac carries no metric/source/boundary/support/recovery/repair/parent role",
            "e_kappa carries no metric/source/trace-restoration/boundary/support/recovery/repair/parent role",
            "accounting variables do not repair zeta/kappa geometric residuals",
            "accounting variables do not license insertion or parent closure",
        ],
    ))

    for branch_id in [
        "accounting_label_as_theorem",
        "epsilon_ekappa_hidden_reservoir",
        "ekappa_trace_restoration",
        "epsilon_boundary_source_repair",
        "recovery_tuned_accounting",
        "accounting_hides_geometric_residuals",
        "accounting_total_cancellation",
        "accounting_licenses_insertion",
        "accounting_opens_parent",
        "accounting_as_full_residual_control",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_26",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; accounting variables cannot become hidden residual-control reservoirs.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g26_epsilon_ekappa_accounting_inertness_partially_reduced_not_derived",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "epsilon_vac_metric and e_kappa_metric are partially reduced to accounting-only inertness theorem targets, but no full accounting inertness theorem is derived. "
            "Accounting variables cannot carry hidden metric/source/support/boundary/recovery/repair/parent roles, cannot repair zeta/kappa geometric residuals, and cannot license insertion or parent closure."
        ),
        derivation_ids=[
            "epsilon_ekappa_accounting_failure_load_26",
            "epsilon_ekappa_inertness_theorem_attempt_marker_26",
        ],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Epsilon E_kappa Inertness Theorem Attempt")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    ledger = build_ledger()
    attempts = build_residual_attempts()
    tests = build_channel_tests()
    shortcuts = build_rejected_shortcuts()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_accounting_ledger(ledger, out)
    case_2_residual_attempts(attempts, out)
    case_3_channel_tests(tests, out)
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
