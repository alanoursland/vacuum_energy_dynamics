# Candidate nonmetric inertness conditions
#
# Group:
#   25_residual_kill_or_no_overlap_theorem
#
# Script type:
#   REQUIREMENTS / DIAGNOSTIC
#
# Purpose
# -------
# Define the necessary conditions for residuals to be considered non-metric
# or inert.
#
# Locked-door question:
#
#   What must non-metric / inert residual status actually mean?
#
# This script does not derive non-metric inertness.
# It does not derive residual kill.
# It does not derive active no-overlap O.
# It does not derive B_s/F_zeta insertion.
# It does not open parent equation closure.
#
# It records that "non-metric" does not mean ignored. It requires a
# no-reentry theorem burden.

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
        "BLOCKED": StatusMark.FAIL,
        "DIAGNOSTIC_ONLY": StatusMark.INFO,
        "NOT_READY": StatusMark.DEFER,
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
            "residual_problem_dep_25",
            "25_residual_kill_or_no_overlap_theorem__candidate_residual_kill_problem_ledger",
            "residual_kill_problem_ledger_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "classification_dep_25",
            "25_residual_kill_or_no_overlap_theorem__candidate_metric_trace_residual_classification",
            "metric_trace_residual_classification_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g22_nonmetric_dep_25",
            "22_boundary_neutrality_and_scalar_silence__candidate_diagnostic_residual_nonmetric_conditions",
            "diagnostic_residual_nonmetric_conditions_marker_22",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g24_count_once_dep_25",
            "24_metric_insertion_recovery_retest__candidate_count_once_metric_trace_audit",
            "count_once_metric_trace_marker_24",
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
class InertnessLoadLedger:
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
    nonmetric_failure_load: sp.Expr


@dataclass
class InertnessCondition:
    name: str
    condition: str
    status: str
    failure_if: str
    consequence: str


@dataclass
class InertnessBranch:
    name: str
    branch: str
    status: str
    allowed_if: str
    rejected_if: str


@dataclass
class RejectedInertnessShortcut:
    name: str
    shortcut: str
    forbidden_use: str
    status: str
    consequence: str


def build_ledger() -> InertnessLoadLedger:
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

    nonmetric_failure_load = sp.simplify(
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

    return InertnessLoadLedger(
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
        nonmetric_failure_load=nonmetric_failure_load,
    )


def build_conditions() -> List[InertnessCondition]:
    return [
        InertnessCondition(
            name="N1: no metric trace",
            condition="metric_trace = 0",
            status="REQUIRED",
            failure_if="residual enters ordinary metric scalar trace",
            consequence="count-once recombination fails",
        ),
        InertnessCondition(
            name="N2: no source role",
            condition="source_role = 0",
            status="REQUIRED",
            failure_if="residual becomes ordinary source channel or source-loaded coefficient",
            consequence="source no-double-counting fails",
        ),
        InertnessCondition(
            name="N3: no boundary flux",
            condition="boundary_flux = 0",
            status="REQUIRED",
            failure_if="residual creates boundary flux or current leakage",
            consequence="boundary neutrality fails",
        ),
        InertnessCondition(
            name="N4: no exterior scalar tail",
            condition="scalar_tail = 0",
            status="REQUIRED",
            failure_if="residual leaves C/r exterior scalar tail",
            consequence="scalar silence fails",
        ),
        InertnessCondition(
            name="N5: no current flux",
            condition="current_flux = 0",
            status="REQUIRED",
            failure_if="residual exports non-A current flux",
            consequence="current silence fails",
        ),
        InertnessCondition(
            name="N6: no A-tail mass shift",
            condition="A_tail_mass_shift = 0",
            status="REQUIRED",
            failure_if="residual shifts protected A-sector exterior mass",
            consequence="A-sector mass protection fails",
        ),
        InertnessCondition(
            name="N7: no shell/source load",
            condition="shell_source_load = 0",
            status="REQUIRED",
            failure_if="residual creates shell/source seam load",
            consequence="no-shell and source compatibility fail",
        ),
        InertnessCondition(
            name="N8: no support/layer role",
            condition="support_layer_role = 0",
            status="REQUIRED",
            failure_if="residual hides in support radius, smoothing width, transition layer, or matching condition",
            consequence="smooth support guardrails fail",
        ),
        InertnessCondition(
            name="N9: no recovery-selected status",
            condition="recovery_selected_status = 0",
            status="REQUIRED",
            failure_if="residual inertness is selected from Schwarzschild/gamma/AB/B=1/A/PPN/parent-fit recovery",
            consequence="recovery constructs residual control",
        ),
        InertnessCondition(
            name="N10: no repair role",
            condition="repair_role = 0",
            status="REQUIRED",
            failure_if="residual inertness depends on O/H/dark/exchange/curvature/current repair labels",
            consequence="repair route supplies missing theorem",
        ),
        InertnessCondition(
            name="N11: no parent placeholder role",
            condition="parent_placeholder_role = 0",
            status="REQUIRED",
            failure_if="residual inertness is used to fill or open parent equation",
            consequence="parent closure is smuggled",
        ),
    ]


def build_branches() -> List[InertnessBranch]:
    return [
        InertnessBranch(
            name="B1: strict non-metric inert residual",
            branch="residual has zero metric/source/boundary/support/recovery/repair/parent roles",
            status="THEOREM_TARGET",
            allowed_if="all inertness conditions are derived sector-by-sector",
            rejected_if="non-metric is merely asserted",
        ),
        InertnessBranch(
            name="B2: diagnostic-only inert residual",
            branch="residual is audit-only and cannot construct, source, recover, or repair",
            status="SAFE_IF",
            allowed_if="diagnostic-only status is fixed before recovery and all reentry paths are closed",
            rejected_if="diagnostic label later becomes construction data",
        ),
        InertnessBranch(
            name="B3: inert by naming",
            branch="residual is called non-metric or inert without no-reentry conditions",
            status="REJECTED",
            allowed_if="never",
            rejected_if="used to close count-once burden",
        ),
        InertnessBranch(
            name="B4: inert by recovery",
            branch="residual becomes inert because recovery requires it",
            status="REJECTED",
            allowed_if="never",
            rejected_if="Schwarzschild/gamma/AB/B=1/A/PPN/parent-fit chooses status",
        ),
    ]


def build_rejected_shortcuts() -> List[RejectedInertnessShortcut]:
    return [
        RejectedInertnessShortcut(
            name="S1: nonmetric by label",
            shortcut="declare residual non-metric",
            forbidden_use="non-metric label used without no-reentry proof",
            status="REJECTED",
            consequence="residual may still re-enter",
        ),
        RejectedInertnessShortcut(
            name="S2: inert by bookkeeping",
            shortcut="declare residual bookkeeping-only",
            forbidden_use="bookkeeping label carries hidden trace/source/load",
            status="REJECTED",
            consequence="hidden ordinary channel remains possible",
        ),
        RejectedInertnessShortcut(
            name="S3: diagnostic becomes construction",
            shortcut="diagnostic residual later used as B_s/F_zeta, support, boundary, source, or recovery parameter",
            forbidden_use="diagnostic label used as construction data",
            status="REJECTED",
            consequence="diagnostic-only status collapses",
        ),
        RejectedInertnessShortcut(
            name="S4: inertness by cancellation",
            shortcut="residual loads cancel only in total",
            forbidden_use="sector-by-sector zero is replaced by total cancellation",
            status="REJECTED",
            consequence="unsafe reentry is hidden",
        ),
        RejectedInertnessShortcut(
            name="S5: inertness opens parent",
            shortcut="non-metric/inertness ledger opens parent equation",
            forbidden_use="requirements audit treated as parent identity",
            status="REJECTED",
            consequence="parent gate is smuggled",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Nonmetric inertness conditions problem")
    print("Question:")
    print()
    print("  What must non-metric / inert residual status actually mean?")
    print()
    print("Reference discipline:")
    print()
    print("  Non-metric does not mean ignored.")
    print("  Inert does not mean harmless by label.")
    print("  Residual inertness requires no reentry through metric, source, boundary, support, recovery, repair, or parent placeholders.")

    with out.governance_assessments():
        out.line(
            "nonmetric inertness conditions audit opened",
            StatusMark.INFO,
            "defining no-reentry conditions for non-metric / inert residual status",
        )


def case_1_inertness_ledger(ledger: InertnessLoadLedger, out: ScriptOutput) -> None:
    header("Case 1: Nonmetric inertness failure-load ledger")
    print("Residual inertness failure channels:")
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
    print("Nonmetric failure load:")
    print()
    print(f"  L_nonmetric_fail = {sp.sstr(ledger.nonmetric_failure_load)}")
    print()
    print("All channels must vanish or be theorem-routed before non-metric / inert status is honest.")

    with out.derived_results():
        out.line(
            "nonmetric inertness failure-load ledger stated",
            StatusMark.OBLIGATION,
            f"L_nonmetric_fail = {sp.sstr(ledger.nonmetric_failure_load)}",
        )


def case_2_conditions(conditions: List[InertnessCondition], out: ScriptOutput) -> None:
    header("Case 2: Nonmetric inertness conditions")
    for condition in conditions:
        print()
        print("-" * 120)
        print(condition.name)
        print("-" * 120)
        print(f"Condition: {condition.condition}")
        print(f"[{status_mark(condition.status).value}] {condition.name}: {condition.status}")
        print(f"Failure if: {condition.failure_if}")
        print(f"Consequence: {condition.consequence}")

    with out.unresolved_obligations():
        out.line(
            "nonmetric inertness conditions populated",
            StatusMark.OBLIGATION,
            f"{len(conditions)} no-reentry conditions required for honest inertness",
        )


def case_3_branches(branches: List[InertnessBranch], out: ScriptOutput) -> None:
    header("Case 3: Nonmetric inertness branches")
    for branch in branches:
        print()
        print("-" * 120)
        print(branch.name)
        print("-" * 120)
        print(f"Branch: {branch.branch}")
        print(f"[{status_mark(branch.status).value}] {branch.name}: {branch.status}")
        print(f"Allowed if: {branch.allowed_if}")
        print(f"Rejected if: {branch.rejected_if}")

    with out.governance_assessments():
        out.line(
            "nonmetric inertness branches classified",
            StatusMark.PASS,
            f"{len(branches)} inertness branches classified",
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
            "inertness shortcuts rejected",
            StatusMark.FAIL,
            "nonmetric by label, inert bookkeeping, diagnostic construction, total cancellation, and parent shortcut remain rejected",
        )


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("The nonmetric inertness conditions audit fails if a later script allows:")
    print()
    print("1. non-metric label without no metric trace proof")
    print("2. non-metric label with source role")
    print("3. non-metric label with boundary flux or scalar tail")
    print("4. non-metric label with current flux or A-tail mass shift")
    print("5. non-metric label with shell/source load")
    print("6. residual hidden in support/smoothing/transition/matching language")
    print("7. residual inertness chosen from recovery")
    print("8. residual inertness supplied by O/H/dark/exchange/curvature/current repair")
    print("9. total cancellation replaces sector-by-sector no-reentry")
    print("10. parent equation opened from inertness conditions alone")

    with out.governance_assessments():
        out.line(
            "nonmetric inertness failure controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not use nonmetric/inert labels as residual cleanup",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Nonmetric / inertness result:")
    print()
    print("  Non-metric does not mean ignored.")
    print("  Inert does not mean harmless by label.")
    print("  Honest non-metric / inert residual status requires no metric, source, boundary, scalar-tail, current-flux, A-tail, shell/source, support/layer, recovery, repair, or parent reentry.")
    print("  This remains a theorem burden.")
    print()
    print("Possible next script:")
    print("  candidate_residual_reentry_exclusion_audit.py")
    print()
    print("Tiny goblin label:")
    print("  No reentry, or no inertness.")

    with out.governance_assessments():
        out.line(
            "nonmetric inertness conditions audit complete",
            StatusMark.PASS,
            "inertness conditions explicit; nonmetric theorem remains open",
        )


def record_derivations(ns, ledger: InertnessLoadLedger) -> None:
    ns.record_derivation(
        derivation_id="nonmetric_inertness_failure_load_25",
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
        output=ledger.nonmetric_failure_load,
        method="sum representative reentry channels that invalidate non-metric / inert residual status",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="nonmetric_inertness_failure_ledger",
        scope="Group 25 residual kill or no-overlap theorem",
    )

    ns.record_derivation(
        derivation_id="nonmetric_inertness_conditions_marker_25",
        inputs=[
            sp.Symbol("metric_trace_zero"),
            sp.Symbol("source_role_zero"),
            sp.Symbol("boundary_flux_zero"),
            sp.Symbol("scalar_tail_zero"),
            sp.Symbol("current_flux_zero"),
            sp.Symbol("support_layer_zero"),
            sp.Symbol("recovery_independent"),
            sp.Symbol("no_repair_role"),
            sp.Symbol("no_parent_placeholder"),
        ],
        output=sp.Symbol("nonmetric_inertness_conditions_stated"),
        method="Group 25 nonmetric inertness conditions ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="requirements_marker",
        scope="Group 25 residual kill or no-overlap theorem",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g25_derive_no_metric_trace_for_inertness", "Derive no metric trace for inert residuals"),
        ("g25_derive_no_source_role_for_inertness", "Derive no source role for inert residuals"),
        ("g25_derive_no_boundary_scalar_current_tail", "Derive no boundary/scalar/current tail for inert residuals"),
        ("g25_derive_no_A_tail_shell_load", "Derive no A-tail or shell/source load for inert residuals"),
        ("g25_derive_no_support_layer_role", "Derive no support/layer role for inert residuals"),
        ("g25_derive_recovery_independent_inertness", "Derive recovery-independent inertness"),
        ("g25_derive_no_repair_parent_role", "Derive no repair or parent placeholder role for inert residuals"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g25_nonmetric_inertness_route"],
            description=(
                "Non-metric / inert residual status remains theorem-targeted until all reentry channels are closed sector-by-sector."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g25_derive_no_metric_trace_for_inertness",
        "g25_derive_no_source_role_for_inertness",
        "g25_derive_no_boundary_scalar_current_tail",
        "g25_derive_no_A_tail_shell_load",
        "g25_derive_no_support_layer_role",
        "g25_derive_recovery_independent_inertness",
        "g25_derive_no_repair_parent_role",
    ]

    ns.record_route(RouteRecord(
        route_id="g25_nonmetric_inertness_route",
        script_id=SCRIPT_ID,
        name="Group 25 nonmetric inertness theorem target",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "no metric trace",
            "no source role",
            "no boundary/scalar/current/A-tail/shell load",
            "no support/layer role",
            "residual status is recovery-independent",
            "no repair or parent placeholder role",
        ],
    ))

    for branch_id in [
        "nonmetric_by_label",
        "inert_bookkeeping_hidden_load",
        "diagnostic_becomes_construction",
        "inertness_by_total_cancellation",
        "inertness_opens_parent",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_25",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; nonmetric/inert status requires no-reentry theorem burden.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g25_nonmetric_inertness_requires_no_reentry",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Non-metric / inert residual status requires no metric, source, boundary, scalar-tail, current-flux, A-tail, "
            "shell/source, support/layer, recovery, repair, or parent reentry. A nonmetric label alone does not solve residual control."
        ),
        derivation_ids=[
            "nonmetric_inertness_failure_load_25",
            "nonmetric_inertness_conditions_marker_25",
        ],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Nonmetric Inertness Conditions")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    ledger = build_ledger()
    conditions = build_conditions()
    branches = build_branches()
    shortcuts = build_rejected_shortcuts()

    case_0_problem_statement(out)
    case_1_inertness_ledger(ledger, out)
    case_2_conditions(conditions, out)
    case_3_branches(branches, out)
    case_4_rejected_shortcuts(shortcuts, out)
    case_5_failure_controls(out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, ledger)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
