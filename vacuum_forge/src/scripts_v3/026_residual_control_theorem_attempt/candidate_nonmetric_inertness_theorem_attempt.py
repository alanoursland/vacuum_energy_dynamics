# Candidate nonmetric inertness theorem attempt
#
# Group:
#   26_residual_control_theorem_attempt
#
# Script type:
#   THEOREM ATTEMPT
#
# Purpose
# -------
# Attempt the strict non-metric / inert residual-control route.
#
# Locked-door question:
#
#   Can residuals be proven strictly non-metric / inert instead of killed?
#
# This script does not derive B_s/F_zeta insertion.
# It does not derive active no-overlap O.
# It does not derive parent equation closure.
#
# It tests whether each residual double-count entry can satisfy a strict
# inertness predicate:
#
#   I(X) = no metric trace,
#          no source role,
#          no boundary flux,
#          no scalar tail,
#          no current flux,
#          no A-tail mass shift,
#          no shell/source load,
#          no support/layer role,
#          no recovery-selected status,
#          no repair role,
#          no parent placeholder role.
#
# Tiny goblin rule:
#
#   Inert means no pockets.

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
            "g25_inertness_dep_26",
            "025_residual_kill_or_no_overlap_theorem__candidate_nonmetric_inertness_conditions",
            "nonmetric_inertness_conditions_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g25_reentry_dep_26",
            "025_residual_kill_or_no_overlap_theorem__candidate_residual_reentry_exclusion_audit",
            "residual_reentry_exclusion_marker_25",
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
class InertnessPredicateLedger:
    metric_trace: sp.Symbol
    source_role: sp.Symbol
    boundary_flux: sp.Symbol
    scalar_tail: sp.Symbol
    current_flux: sp.Symbol
    A_tail_mass_shift: sp.Symbol
    shell_source_load: sp.Symbol
    support_layer_role: sp.Symbol
    recovery_selected_status: sp.Symbol
    repair_role: sp.Symbol
    parent_placeholder_role: sp.Symbol
    I_fail: sp.Expr


@dataclass
class ResidualInertnessAttempt:
    name: str
    residual: str
    candidate_support: str
    inertness_status: str
    reason: str
    next_reduction: str


@dataclass
class InertnessChannelTest:
    name: str
    channel: str
    status: str
    passes_if: str
    current_result: str


@dataclass
class RejectedInertnessShortcut:
    name: str
    shortcut: str
    forbidden_use: str
    status: str
    consequence: str


@dataclass
class InertnessConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


# =============================================================================
# Builders
# =============================================================================


def build_predicate_ledger() -> InertnessPredicateLedger:
    (
        metric_trace,
        source_role,
        boundary_flux,
        scalar_tail,
        current_flux,
        A_tail_mass_shift,
        shell_source_load,
        support_layer_role,
        recovery_selected_status,
        repair_role,
        parent_placeholder_role,
    ) = sp.symbols(
        "metric_trace source_role boundary_flux scalar_tail current_flux A_tail_mass_shift shell_source_load support_layer_role recovery_selected_status repair_role parent_placeholder_role",
        real=True,
    )

    I_fail = sp.simplify(
        metric_trace
        + source_role
        + boundary_flux
        + scalar_tail
        + current_flux
        + A_tail_mass_shift
        + shell_source_load
        + support_layer_role
        + recovery_selected_status
        + repair_role
        + parent_placeholder_role
    )

    return InertnessPredicateLedger(
        metric_trace=metric_trace,
        source_role=source_role,
        boundary_flux=boundary_flux,
        scalar_tail=scalar_tail,
        current_flux=current_flux,
        A_tail_mass_shift=A_tail_mass_shift,
        shell_source_load=shell_source_load,
        support_layer_role=support_layer_role,
        recovery_selected_status=recovery_selected_status,
        repair_role=repair_role,
        parent_placeholder_role=parent_placeholder_role,
        I_fail=I_fail,
    )


def build_residual_attempts() -> List[ResidualInertnessAttempt]:
    return [
        ResidualInertnessAttempt(
            name="I1: zeta residual inertness",
            residual="zeta_residual_metric",
            candidate_support="count-once requirement and B_s/F_zeta target",
            inertness_status="NOT_DERIVED",
            reason="count-once blocks reentry but does not prove zeta residual has no metric/source/boundary/support/recovery/repair/parent role",
            next_reduction="requires zeta non-reentry theorem, insertion law, coefficient-origin theorem, or active O",
        ),
        ResidualInertnessAttempt(
            name="I2: kappa residual inertness",
            residual="kappa_metric",
            candidate_support="diagnostic-only / areal-kappa guardrail",
            inertness_status="NOT_DERIVED",
            reason="diagnostic-only status constrains construction use but does not prove strict inertness across all channels",
            next_reduction="requires kappa non-reentry theorem or active O",
        ),
        ResidualInertnessAttempt(
            name="I3: epsilon_vac accounting inertness",
            residual="epsilon_vac_metric",
            candidate_support="configuration accounting and no extra metric/source channel guardrail",
            inertness_status="PARTIAL_REDUCTION",
            reason="accounting guardrail supports a narrower inertness target, but full no-reentry is not derived",
            next_reduction="requires accounting-only theorem: no metric/source/support/boundary/recovery/repair/parent role",
        ),
        ResidualInertnessAttempt(
            name="I4: e_kappa accounting inertness",
            residual="e_kappa_metric",
            candidate_support="kappa accounting and no source-channel guardrail",
            inertness_status="PARTIAL_REDUCTION",
            reason="accounting guardrail supports a narrower inertness target, but e_kappa could still re-enter without a theorem",
            next_reduction="requires kappa accounting-only theorem: no trace restoration, no source role, no recovery tuning",
        ),
    ]


def build_channel_tests() -> List[InertnessChannelTest]:
    return [
        InertnessChannelTest(
            name="C1: no metric trace",
            channel="metric_trace",
            status="NOT_DERIVED",
            passes_if="each residual entry is proven absent from ordinary metric scalar trace",
            current_result="not derived for zeta_residual_metric or kappa_metric",
        ),
        InertnessChannelTest(
            name="C2: no source role",
            channel="source_role",
            status="CONDITIONALLY_REDUCED",
            passes_if="source no-double-counting is upgraded into no residual source channel for each entry",
            current_result="guardrail exists, but theorem not derived",
        ),
        InertnessChannelTest(
            name="C3: no boundary flux",
            channel="boundary_flux",
            status="NOT_DERIVED",
            passes_if="residual entries are proven boundary-neutral",
            current_result="boundary guardrail exists, but residual inertness theorem is not derived",
        ),
        InertnessChannelTest(
            name="C4: no scalar tail",
            channel="scalar_tail",
            status="NOT_DERIVED",
            passes_if="residual entries are proven to leave no C/r tail",
            current_result="scalar silence requirement exists, but no residual inertness theorem is derived",
        ),
        InertnessChannelTest(
            name="C5: no current flux",
            channel="current_flux",
            status="NOT_DERIVED",
            passes_if="residual entries are proven not to export non-A current",
            current_result="current silence remains a guardrail, not an inertness theorem",
        ),
        InertnessChannelTest(
            name="C6: no A-tail mass shift",
            channel="A_tail_mass_shift",
            status="CONDITIONALLY_REDUCED",
            passes_if="A-sector mass protection is lifted to residual no-mass-shift theorem",
            current_result="mass protection guardrail exists, but residual inertness theorem is not derived",
        ),
        InertnessChannelTest(
            name="C7: no shell/source load",
            channel="shell_source_load",
            status="NOT_DERIVED",
            passes_if="residual entries are proven no-shell/no-source at seams",
            current_result="matching guardrails exist, but no residual theorem is derived",
        ),
        InertnessChannelTest(
            name="C8: no support/layer role",
            channel="support_layer_role",
            status="NOT_DERIVED",
            passes_if="residual entries are proven independent of support radius, smoothing width, and transition layer",
            current_result="support/matching requirements exist, but residual no-layer role is not derived",
        ),
        InertnessChannelTest(
            name="C9: no recovery-selected status",
            channel="recovery_selected_status",
            status="CONDITIONALLY_REDUCED",
            passes_if="residual status is fixed structurally before recovery",
            current_result="anti-smuggling rule exists, but structural origin is not yet derived",
        ),
        InertnessChannelTest(
            name="C10: no repair role",
            channel="repair_role",
            status="CONDITIONALLY_REDUCED",
            passes_if="residual inertness is independent of O/H/dark/exchange/curvature/current repair labels",
            current_result="repair routes are rejected, but inertness theorem is not derived",
        ),
        InertnessChannelTest(
            name="C11: no parent placeholder",
            channel="parent_placeholder_role",
            status="CONDITIONALLY_REDUCED",
            passes_if="residual inertness is independent of parent closure",
            current_result="parent closure is blocked, but residual inertness theorem is not derived",
        ),
    ]


def build_rejected_shortcuts() -> List[RejectedInertnessShortcut]:
    return [
        RejectedInertnessShortcut(
            name="S1: inert by label",
            shortcut="call residuals inert",
            forbidden_use="label substitutes for no-reentry theorem",
            status="REJECTED",
            consequence="residual can still re-enter",
        ),
        RejectedInertnessShortcut(
            name="S2: non-metric by label",
            shortcut="call residuals non-metric",
            forbidden_use="vocabulary substitutes for metric-trace proof",
            status="REJECTED",
            consequence="metric trace may still survive",
        ),
        RejectedInertnessShortcut(
            name="S3: accounting-only by preference",
            shortcut="call epsilon_vac/e_kappa accounting-only",
            forbidden_use="accounting label substitutes for no metric/source/support/boundary role",
            status="REJECTED",
            consequence="hidden channel remains possible",
        ),
        RejectedInertnessShortcut(
            name="S4: inert by total cancellation",
            shortcut="residual channels cancel in total",
            forbidden_use="total cancellation substitutes for sector-by-sector no-reentry",
            status="REJECTED",
            consequence="unsafe reentry is hidden",
        ),
        RejectedInertnessShortcut(
            name="S5: inert by recovery",
            shortcut="choose inertness because recovery requires it",
            forbidden_use="recovery diagnostic selects residual status",
            status="REJECTED",
            consequence="recovery constructs residual control",
        ),
        RejectedInertnessShortcut(
            name="S6: inert by repair",
            shortcut="choose inertness to fix boundary/source/support failure",
            forbidden_use="repair need selects residual status",
            status="REJECTED",
            consequence="residual cleanup becomes repair route",
        ),
        RejectedInertnessShortcut(
            name="S7: inertness licenses insertion",
            shortcut="strict inertness attempt licenses B_s/F_zeta insertion",
            forbidden_use="inertness theorem replaces insertion law",
            status="REJECTED",
            consequence="metric insertion is smuggled",
        ),
        RejectedInertnessShortcut(
            name="S8: inertness opens parent",
            shortcut="strict inertness attempt opens parent equation",
            forbidden_use="inertness theorem replaces parent identity",
            status="REJECTED",
            consequence="parent equation is smuggled",
        ),
    ]


def build_conclusions() -> List[InertnessConclusion]:
    return [
        InertnessConclusion(
            name="C1: full strict inertness",
            conclusion="not derived for all L_double entries",
            status="NOT_DERIVED",
            meaning="strict non-metric inertness cannot yet control the full double-count load",
        ),
        InertnessConclusion(
            name="C2: accounting residuals",
            conclusion="epsilon_vac_metric and e_kappa_metric are partially reduced to accounting-only inertness targets",
            status="PARTIAL_REDUCTION",
            meaning="these entries are better candidates for an accounting inertness theorem than direct kill",
        ),
        InertnessConclusion(
            name="C3: geometric residuals",
            conclusion="zeta_residual_metric and kappa_metric remain unresolved",
            status="THEOREM_TARGET",
            meaning="the dangerous geometric residuals still need sector-by-sector non-reentry, insertion law, or active O",
        ),
        InertnessConclusion(
            name="C4: next route",
            conclusion="test zeta/kappa non-reentry sector-by-sector",
            status="SAFE_IF",
            meaning="the next script should focus on the geometric residual reentry channels",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Nonmetric inertness theorem attempt problem")
    print("Question:")
    print()
    print("  Can residuals be proven strictly non-metric / inert instead of killed?")
    print()
    print("Reference discipline:")
    print()
    print("  Inertness requires no pockets: no metric, source, boundary, scalar, current, mass, shell, support, recovery, repair, or parent role.")
    print("  Accounting and diagnostic labels are not inertness theorems.")

    with out.governance_assessments():
        out.line(
            "nonmetric inertness theorem attempt opened",
            StatusMark.INFO,
            "testing strict inertness / no-reentry route after direct kill was not derived",
        )


def case_1_predicate_ledger(ledger: InertnessPredicateLedger, out: ScriptOutput) -> None:
    header("Case 1: Strict inertness predicate ledger")
    print("Inertness failure channels:")
    print()
    for name in [
        "metric_trace",
        "source_role",
        "boundary_flux",
        "scalar_tail",
        "current_flux",
        "A_tail_mass_shift",
        "shell_source_load",
        "support_layer_role",
        "recovery_selected_status",
        "repair_role",
        "parent_placeholder_role",
    ]:
        print(f"  {name} = {sp.sstr(getattr(ledger, name))}")
    print()
    print("Strict inertness failure load:")
    print()
    print(f"  I_fail = {sp.sstr(ledger.I_fail)}")
    print()
    print("Interpretation:")
    print()
    print("  Strict inertness requires I_fail = 0 sector-by-sector.")
    print("  A residual is not inert if any pocket remains.")

    with out.derived_results():
        out.line(
            "strict inertness failure-load ledger stated",
            StatusMark.OBLIGATION,
            f"I_fail = {sp.sstr(ledger.I_fail)}",
        )


def case_2_residual_attempts(attempts: List[ResidualInertnessAttempt], out: ScriptOutput) -> None:
    header("Case 2: Residual-entry inertness attempt")
    for attempt in attempts:
        print()
        print("-" * 120)
        print(attempt.name)
        print("-" * 120)
        print(f"Residual: {attempt.residual}")
        print(f"Candidate support: {attempt.candidate_support}")
        print(f"[{status_mark(attempt.inertness_status).value}] {attempt.name}: {attempt.inertness_status}")
        print(f"Reason: {attempt.reason}")
        print(f"Next reduction: {attempt.next_reduction}")

    with out.unresolved_obligations():
        out.line(
            "residual-entry inertness attempts classified",
            StatusMark.OBLIGATION,
            f"{len(attempts)} residual entries tested; full inertness not derived",
        )


def case_3_channel_tests(tests: List[InertnessChannelTest], out: ScriptOutput) -> None:
    header("Case 3: Inertness channel tests")
    for test in tests:
        print()
        print("-" * 120)
        print(test.name)
        print("-" * 120)
        print(f"Channel: {test.channel}")
        print(f"[{status_mark(test.status).value}] {test.name}: {test.status}")
        print(f"Passes if: {test.passes_if}")
        print(f"Current result: {test.current_result}")

    with out.governance_assessments():
        out.line(
            "strict inertness channel tests completed",
            StatusMark.PASS,
            f"{len(tests)} channels evaluated; full inertness not derived",
        )


def case_4_rejected_shortcuts(shortcuts: List[RejectedInertnessShortcut], out: ScriptOutput) -> None:
    header("Case 4: Rejected inertness shortcuts")
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
            "strict inertness shortcuts rejected",
            StatusMark.FAIL,
            "labels, accounting preference, total cancellation, recovery, repair, insertion, and parent shortcuts are rejected",
        )


def case_5_conclusions(conclusions: List[InertnessConclusion], out: ScriptOutput) -> None:
    header("Case 5: Strict inertness theorem-attempt conclusions")
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
            "strict inertness theorem-attempt conclusion stated",
            StatusMark.DEFER,
            "full inertness not derived; zeta/kappa non-reentry should be tested next",
        )


def case_6_failure_controls(out: ScriptOutput) -> None:
    header("Case 6: Failure controls")
    print("The nonmetric inertness theorem attempt fails if a later script allows:")
    print()
    print("1. inertness by label")
    print("2. non-metric status by vocabulary")
    print("3. accounting-only status by preference")
    print("4. diagnostic-only status used as construction data")
    print("5. total cancellation treated as sector-by-sector no-reentry")
    print("6. recovery diagnostic selects inertness")
    print("7. boundary/source/support failure selects inertness")
    print("8. O/H/dark/exchange/curvature/current label supplies inertness")
    print("9. inertness licenses B_s/F_zeta insertion")
    print("10. inertness opens parent equation")

    with out.governance_assessments():
        out.line(
            "strict inertness failure controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not convert labels or guardrails into inertness theorem",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Strict nonmetric inertness theorem attempt result:")
    print()
    print("  Full strict inertness is not derived for all L_double entries.")
    print("  epsilon_vac_metric and e_kappa_metric are partially reduced to accounting-only inertness theorem targets.")
    print("  zeta_residual_metric and kappa_metric remain unresolved geometric residuals.")
    print("  Strict inertness requires sector-by-sector no reentry through every channel.")
    print("  B_s/F_zeta insertion and parent closure remain not ready.")
    print()
    print("Possible next script:")
    print("  candidate_zeta_kappa_nonreentry_theorem_attempt.py")
    print()
    print("Tiny goblin label:")
    print("  Inert means no pockets.")

    with out.governance_assessments():
        out.line(
            "nonmetric inertness theorem attempt complete",
            StatusMark.PASS,
            "full inertness not derived; zeta/kappa non-reentry route remains next",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, ledger: InertnessPredicateLedger) -> None:
    ns.record_derivation(
        derivation_id="nonmetric_inertness_theorem_attempt_failure_load_26",
        inputs=[
            ledger.metric_trace,
            ledger.source_role,
            ledger.boundary_flux,
            ledger.scalar_tail,
            ledger.current_flux,
            ledger.A_tail_mass_shift,
            ledger.shell_source_load,
            ledger.support_layer_role,
            ledger.recovery_selected_status,
            ledger.repair_role,
            ledger.parent_placeholder_role,
        ],
        output=ledger.I_fail,
        method="sum strict inertness failure channels for theorem attempt",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="nonmetric_inertness_theorem_attempt_ledger",
        scope="Group 26 residual control theorem attempt",
    )

    ns.record_derivation(
        derivation_id="nonmetric_inertness_theorem_attempt_marker_26",
        inputs=[
            sp.Symbol("zeta_residual_metric"),
            sp.Symbol("kappa_metric"),
            sp.Symbol("epsilon_vac_metric"),
            sp.Symbol("e_kappa_metric"),
            sp.Symbol("strict_inertness_channels"),
        ],
        output=sp.Symbol("nonmetric_inertness_theorem_not_derived"),
        method="Group 26 strict nonmetric inertness theorem attempt",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="theorem_attempt_marker",
        scope="Group 26 residual control theorem attempt",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g26_inertness_zeta_residual", "Derive strict inertness for zeta residual metric trace"),
        ("g26_inertness_kappa_metric", "Derive strict inertness for kappa metric trace"),
        ("g26_inertness_epsilon_metric", "Derive strict accounting inertness for epsilon_vac metric channel"),
        ("g26_inertness_e_kappa_metric", "Derive strict accounting inertness for e_kappa metric channel"),
        ("g26_inertness_no_metric_source_channels", "Derive no metric/source channels"),
        ("g26_inertness_no_boundary_support_channels", "Derive no boundary/support channels"),
        ("g26_inertness_no_recovery_repair_parent_channels", "Derive no recovery/repair/parent channels"),
        ("g26_keep_insertion_parent_closed_after_inertness_attempt", "Keep insertion and parent gates closed after inertness attempt"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g26_nonmetric_inertness_theorem_attempt_route"],
            description=(
                "Strict nonmetric inertness is not derived here. Future work must prove no-reentry sector-by-sector for each residual entry."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g26_inertness_zeta_residual",
        "g26_inertness_kappa_metric",
        "g26_inertness_epsilon_metric",
        "g26_inertness_e_kappa_metric",
        "g26_inertness_no_metric_source_channels",
        "g26_inertness_no_boundary_support_channels",
        "g26_inertness_no_recovery_repair_parent_channels",
        "g26_keep_insertion_parent_closed_after_inertness_attempt",
    ]

    ns.record_route(RouteRecord(
        route_id="g26_nonmetric_inertness_theorem_attempt_route",
        script_id=SCRIPT_ID,
        name="Group 26 strict nonmetric inertness theorem attempt",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "each residual entry is proven no metric/source/boundary/support/recovery/repair/parent role",
            "accounting residuals are formalized as strictly inert if used",
            "zeta/kappa geometric residuals are not assumed inert",
            "total cancellation is not used",
            "insertion and parent gates remain closed",
        ],
    ))

    for branch_id in [
        "inertness_by_label",
        "nonmetric_by_vocabulary",
        "accounting_by_preference",
        "diagnostic_status_as_construction",
        "total_cancellation_as_inertness",
        "recovery_selected_inertness",
        "boundary_source_selected_inertness",
        "repair_label_supplies_inertness",
        "inertness_licenses_insertion",
        "inertness_opens_parent",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_26",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; inertness requires sector-by-sector no-reentry theorem.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g26_strict_nonmetric_inertness_not_derived",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Full strict nonmetric inertness is not derived for all L_double entries. epsilon_vac_metric and e_kappa_metric are partially reduced "
            "to accounting-only inertness theorem targets, while zeta_residual_metric and kappa_metric remain unresolved geometric residuals. "
            "Inertness requires sector-by-sector no reentry and does not license B_s/F_zeta insertion or parent closure."
        ),
        derivation_ids=[
            "nonmetric_inertness_theorem_attempt_failure_load_26",
            "nonmetric_inertness_theorem_attempt_marker_26",
        ],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Nonmetric Inertness Theorem Attempt")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    ledger = build_predicate_ledger()
    attempts = build_residual_attempts()
    tests = build_channel_tests()
    shortcuts = build_rejected_shortcuts()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_predicate_ledger(ledger, out)
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
