# Candidate residual kill problem ledger
#
# Group:
#   25_residual_kill_or_no_overlap_theorem
#
# Script type:
#   REQUIREMENTS / DIAGNOSTIC
#
# Purpose
# -------
# Open Group 25 by collecting the residual objects and inherited count-once
# burden from Group 24.
#
# Locked-door question:
#
#   What exactly must be killed, made inert, or projected out?
#
# This script does not derive residual kill.
# It does not derive non-metric inertness.
# It does not derive active no-overlap O.
# It does not derive B_s/F_zeta insertion.
# It does not prove boundary neutrality, scalar silence, source compatibility,
# smooth support, no-shell matching, or parent closure.
#
# It records that residual kill / inertness / no-overlap is a theorem target,
# not current construction.

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
        "DIAGNOSTIC_ONLY": StatusMark.INFO,
        "NOT_READY": StatusMark.DEFER,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "SAFE_IF": StatusMark.INFO,
        "THEOREM_TARGET": StatusMark.DEFER,
        "UNRESOLVED": StatusMark.OBLIGATION,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g20_summary_dep_25",
            "020_no_overlap_and_projection_operators__candidate_no_overlap_projection_group_status_summary",
            "no_overlap_projection_group_status_summary_marker",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g21_summary_dep_25",
            "021_source_routing_and_mass_neutrality__candidate_group_21_source_routing_status_summary",
            "group21_source_routing_status_summary_marker_21",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g22_summary_dep_25",
            "022_boundary_neutrality_and_scalar_silence__candidate_group_22_boundary_neutrality_status_summary",
            "group22_boundary_neutrality_status_summary_marker_22",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g23_summary_dep_25",
            "023_smooth_support_and_matching_laws__candidate_group_23_matching_laws_status_summary",
            "group23_matching_laws_status_summary_marker_23",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g24_count_once_dep_25",
            "024_metric_insertion_recovery_retest__candidate_count_once_metric_trace_audit",
            "count_once_metric_trace_marker_24",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g24_summary_dep_25",
            "024_metric_insertion_recovery_retest__candidate_group_24_metric_insertion_status_summary",
            "group24_metric_insertion_status_summary_marker_24",
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
class ResidualProblemLedger:
    zeta_to_Bs: sp.Symbol
    zeta_residual_metric: sp.Symbol
    kappa_metric: sp.Symbol
    epsilon_vac_metric: sp.Symbol
    e_kappa_metric: sp.Symbol
    O_target: sp.Symbol
    trace_total: sp.Expr
    double_count_load: sp.Expr
    safe_trace_target: sp.Expr
    residual_control_gap: sp.Expr


@dataclass
class ResidualObject:
    name: str
    symbol: str
    role: str
    status: str
    required_control: str
    forbidden_use: str


@dataclass
class ResidualControlRoute:
    name: str
    route: str
    status: str
    allowed_if: str
    blocked_if: str


@dataclass
class RejectedResidualShortcut:
    name: str
    shortcut: str
    forbidden_use: str
    status: str
    consequence: str


# =============================================================================
# Builders
# =============================================================================


def build_problem_ledger() -> ResidualProblemLedger:
    zeta_to_Bs, zeta_residual_metric, kappa_metric, epsilon_vac_metric, e_kappa_metric, O_target = sp.symbols(
        "zeta_to_Bs zeta_residual_metric kappa_metric epsilon_vac_metric e_kappa_metric O_target",
        real=True,
    )

    trace_total = sp.simplify(
        zeta_to_Bs
        + zeta_residual_metric
        + kappa_metric
        + epsilon_vac_metric
        + e_kappa_metric
    )
    double_count_load = sp.simplify(
        zeta_residual_metric
        + kappa_metric
        + epsilon_vac_metric
        + e_kappa_metric
    )
    safe_trace_target = zeta_to_Bs

    # Representative gap ledger:
    # O_target does not automatically cancel double_count_load.
    # The residual control theorem must either make double_count_load zero,
    # prove it inert/non-metric/non-reentering, or derive a real O action.
    residual_control_gap = sp.simplify(double_count_load - O_target)

    return ResidualProblemLedger(
        zeta_to_Bs=zeta_to_Bs,
        zeta_residual_metric=zeta_residual_metric,
        kappa_metric=kappa_metric,
        epsilon_vac_metric=epsilon_vac_metric,
        e_kappa_metric=e_kappa_metric,
        O_target=O_target,
        trace_total=trace_total,
        double_count_load=double_count_load,
        safe_trace_target=safe_trace_target,
        residual_control_gap=residual_control_gap,
    )


def build_residual_objects() -> List[ResidualObject]:
    return [
        ResidualObject(
            name="R0: inserted scalar spatial trace",
            symbol="zeta_to_Bs",
            role="portion of zeta allowed to enter ordinary metric scalar trace through B_s/F_zeta",
            status="THEOREM_TARGET",
            required_control="allowed only as count-once insertion target",
            forbidden_use="must not coexist with residual zeta/kappa metric trace unless no-overlap is derived",
        ),
        ResidualObject(
            name="R1: residual zeta metric trace",
            symbol="zeta_residual_metric",
            role="leftover zeta-like metric trace after B_s insertion",
            status="UNRESOLVED",
            required_control="must be zero, strictly non-metric/inert/non-reentering, or removed by derived O",
            forbidden_use="must not survive as ordinary metric trace",
        ),
        ResidualObject(
            name="R2: kappa metric trace",
            symbol="kappa_metric",
            role="kappa-like trace channel that could restore killed residual trace",
            status="UNRESOLVED",
            required_control="must be zero, diagnostic-only, strictly non-metric/inert/non-reentering, or removed by derived O",
            forbidden_use="must not restore killed residual trace or become physical scalar by areal diagnostic",
        ),
        ResidualObject(
            name="R3: epsilon_vac_config metric/source channel",
            symbol="epsilon_vac_metric",
            role="configuration residual that could become hidden metric/source channel",
            status="UNRESOLVED",
            required_control="must be absent from ordinary metric/source trace or proven strictly inert",
            forbidden_use="must not become extra metric/source channel",
        ),
        ResidualObject(
            name="R4: e_kappa metric/source channel",
            symbol="e_kappa_metric",
            role="kappa energy-like label that could become hidden metric/source channel",
            status="UNRESOLVED",
            required_control="must be absent from ordinary metric/source trace or proven strictly inert",
            forbidden_use="must not reintroduce kappa trace through energy/source language",
        ),
        ResidualObject(
            name="R5: no-overlap operator target",
            symbol="O",
            role="possible future operator that removes or separates overlap",
            status="THEOREM_TARGET",
            required_control="requires domain, codomain, kernel, image, idempotence/composition, divergence, boundary, source, mass, and scalar-tail behavior",
            forbidden_use="must not erase overlap by name",
        ),
    ]


def build_control_routes() -> List[ResidualControlRoute]:
    return [
        ResidualControlRoute(
            name="C1: derived residual kill",
            route="L_double = 0 by structural residual-kill law",
            status="THEOREM_TARGET",
            allowed_if="kill law is derived before recovery and preserves boundary/source/support guardrails",
            blocked_if="residuals are set to zero by declaration",
        ),
        ResidualControlRoute(
            name="C2: strict non-metric / inert residual status",
            route="entries in L_double are non-metric, inert, and non-reentering",
            status="THEOREM_TARGET",
            allowed_if="no metric, source, boundary, support, recovery, repair, or parent reentry is proven",
            blocked_if="non-metric means merely ignored",
        ),
        ResidualControlRoute(
            name="C3: active no-overlap operator",
            route="O projects/removes overlap through derived operator structure",
            status="THEOREM_TARGET",
            allowed_if="full O structure and compatibility laws are derived",
            blocked_if="O is used as eraser by name",
        ),
        ResidualControlRoute(
            name="C4: diagnostic-only residual bookkeeping",
            route="residuals remain diagnostic and do not enter ordinary metric/source equations",
            status="SAFE_IF",
            allowed_if="diagnostic status is fixed before recovery and no reentry paths exist",
            blocked_if="diagnostics later become metric/source/support/recovery parameters",
        ),
        ResidualControlRoute(
            name="C5: recovery-selected residual silence",
            route="residuals are killed or made inert because recovery would otherwise fail",
            status="REJECTED",
            allowed_if="never",
            blocked_if="Schwarzschild, gamma, AB, B=1/A, PPN, or parent-fit selects residual status",
        ),
    ]


def build_rejected_shortcuts() -> List[RejectedResidualShortcut]:
    return [
        RejectedResidualShortcut(
            name="S1: residual kill by declaration",
            shortcut="declare zeta_residual_metric = 0",
            forbidden_use="residual is set to zero without a structural law",
            status="REJECTED",
            consequence="count-once theorem is smuggled",
        ),
        RejectedResidualShortcut(
            name="S2: kappa kill by declaration",
            shortcut="declare kappa_metric = 0",
            forbidden_use="kappa trace is killed without diagnostic/inertness/no-overlap proof",
            status="REJECTED",
            consequence="kappa may later restore residual trace",
        ),
        RejectedResidualShortcut(
            name="S3: epsilon / e_kappa ignored",
            shortcut="ignore epsilon_vac_config or e_kappa",
            forbidden_use="configuration or energy labels are treated as inert without no-reentry conditions",
            status="REJECTED",
            consequence="hidden metric/source channel remains possible",
        ),
        RejectedResidualShortcut(
            name="S4: O eraser",
            shortcut="use O to erase overlap by name",
            forbidden_use="O removes residual load without domain/kernel/image/divergence/boundary/source structure",
            status="REJECTED",
            consequence="active no-overlap theorem is smuggled",
        ),
        RejectedResidualShortcut(
            name="S5: recovery-selected residual status",
            shortcut="choose residual kill/inertness from recovery target",
            forbidden_use="AB, B=1/A, gamma_like, PPN, Schwarzschild, or parent-fit determines residual status",
            status="REJECTED",
            consequence="recovery constructs residual control",
        ),
        RejectedResidualShortcut(
            name="S6: boundary/source repair residual status",
            shortcut="choose residual status to cancel boundary/source failure",
            forbidden_use="residual kill hides scalar tail, current flux, A-tail, shell, or source duplication",
            status="REJECTED",
            consequence="residual cleanup becomes repair route",
        ),
        RejectedResidualShortcut(
            name="S7: parent closure from residual cleanup",
            shortcut="open parent equation after residual ledger is stated",
            forbidden_use="residual-control audit is treated as parent identity",
            status="REJECTED",
            consequence="parent equation is smuggled",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Residual kill / no-overlap problem")
    print("Question:")
    print()
    print("  What exactly must be killed, made inert, or projected out?")
    print()
    print("Reference discipline:")
    print()
    print("  Group 25 attacks the count-once bottleneck from Group 24.")
    print("  zeta may enter B_s only if residual zeta/kappa metric trace does not re-enter.")
    print("  residual kill, inertness, and active O remain theorem targets.")
    print("  This script opens the ledger and proves none of them.")

    with out.governance_assessments():
        out.line(
            "residual kill / no-overlap problem ledger opened",
            StatusMark.INFO,
            "collecting residual trace objects and inherited count-once burden",
        )


def case_1_trace_ledger(ledger: ResidualProblemLedger, out: ScriptOutput) -> None:
    header("Case 1: Residual trace ledger")
    print("Trace entries:")
    print()
    print(f"  zeta_to_Bs = {sp.sstr(ledger.zeta_to_Bs)}")
    print(f"  zeta_residual_metric = {sp.sstr(ledger.zeta_residual_metric)}")
    print(f"  kappa_metric = {sp.sstr(ledger.kappa_metric)}")
    print(f"  epsilon_vac_metric = {sp.sstr(ledger.epsilon_vac_metric)}")
    print(f"  e_kappa_metric = {sp.sstr(ledger.e_kappa_metric)}")
    print(f"  O_target = {sp.sstr(ledger.O_target)}")
    print()
    print("Total ordinary metric trace ledger:")
    print()
    print(f"  T_total = {sp.sstr(ledger.trace_total)}")
    print()
    print("Double-count load:")
    print()
    print(f"  L_double = {sp.sstr(ledger.double_count_load)}")
    print()
    print("Safe target:")
    print()
    print(f"  T_safe = {sp.sstr(ledger.safe_trace_target)}")
    print()
    print("Residual-control gap:")
    print()
    print(f"  gap = {sp.sstr(ledger.residual_control_gap)}")
    print()
    print("Interpretation:")
    print()
    print("  O_target does not automatically cancel L_double.")
    print("  The group must derive kill, inertness, or real no-overlap before the gap can close.")

    with out.derived_results():
        out.line(
            "residual trace total ledger stated",
            StatusMark.PASS,
            f"T_total = {sp.sstr(ledger.trace_total)}",
        )
        out.line(
            "double-count load ledger stated",
            StatusMark.OBLIGATION,
            f"L_double = {sp.sstr(ledger.double_count_load)}",
        )
        out.line(
            "residual-control gap stated",
            StatusMark.OBLIGATION,
            f"gap = {sp.sstr(ledger.residual_control_gap)}",
        )


def case_2_residual_objects(objects: List[ResidualObject], out: ScriptOutput) -> None:
    header("Case 2: Residual object inventory")
    for obj in objects:
        print()
        print("-" * 120)
        print(obj.name)
        print("-" * 120)
        print(f"Symbol: {obj.symbol}")
        print(f"Role: {obj.role}")
        print(f"[{status_mark(obj.status).value}] {obj.name}: {obj.status}")
        print(f"Required control: {obj.required_control}")
        print(f"Forbidden use: {obj.forbidden_use}")

    with out.governance_assessments():
        out.line(
            "residual object inventory populated",
            StatusMark.PASS,
            f"{len(objects)} residual objects classified",
        )


def case_3_control_routes(routes: List[ResidualControlRoute], out: ScriptOutput) -> None:
    header("Case 3: Residual control route ledger")
    for route in routes:
        print()
        print("-" * 120)
        print(route.name)
        print("-" * 120)
        print(f"Route: {route.route}")
        print(f"[{status_mark(route.status).value}] {route.name}: {route.status}")
        print(f"Allowed if: {route.allowed_if}")
        print(f"Blocked if: {route.blocked_if}")

    with out.governance_assessments():
        out.line(
            "residual control routes classified",
            StatusMark.PASS,
            f"{len(routes)} residual control routes classified",
        )


def case_4_rejected_shortcuts(shortcuts: List[RejectedResidualShortcut], out: ScriptOutput) -> None:
    header("Case 4: Rejected residual-control shortcuts")
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
            "residual-control shortcuts rejected",
            StatusMark.FAIL,
            "kill by declaration, ignored residuals, O eraser, recovery-selected status, boundary/source repair, and parent shortcut remain rejected",
        )


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("The residual kill problem ledger fails if a later script allows:")
    print()
    print("1. residual zeta_metric killed by declaration")
    print("2. kappa_metric killed by declaration")
    print("3. epsilon_vac_config or e_kappa treated as inert without conditions")
    print("4. O erases overlap by name")
    print("5. residual status chosen from recovery")
    print("6. residual status chosen from boundary/scalar failure")
    print("7. residual status chosen from source compatibility needs")
    print("8. residual re-enters through support/matching/layer language")
    print("9. residual re-enters through source language")
    print("10. H/dark/exchange/curvature/current object supplies residual kill")
    print("11. parent equation opens from residual cleanup")

    with out.governance_assessments():
        out.line(
            "residual kill problem failure controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not pretend residuals are gone without law, inertness, or real O",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Group 25 opening result:")
    print()
    print("  The residual objects that must be controlled are explicit.")
    print("  The double-count load is explicit.")
    print("  The safe trace target is zeta_to_Bs alone.")
    print("  Residual kill remains theorem-targeted.")
    print("  Non-metric / inert residual status remains theorem-targeted.")
    print("  Active no-overlap O remains theorem-targeted.")
    print("  B_s/F_zeta insertion remains blocked unless residual control is derived or explicitly left open.")
    print("  Parent equation remains not ready.")
    print()
    print("Possible next script:")
    print("  candidate_metric_trace_residual_classification.py")
    print()
    print("Tiny goblin label:")
    print("  No echo coin. No ghost trace. No fake eraser.")

    with out.governance_assessments():
        out.line(
            "residual kill problem ledger complete",
            StatusMark.PASS,
            "residual-control target explicit; kill/inertness/O theorem remains open",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, ledger: ResidualProblemLedger) -> None:
    ns.record_derivation(
        derivation_id="residual_kill_trace_ledger_25",
        inputs=[
            ledger.zeta_to_Bs,
            ledger.zeta_residual_metric,
            ledger.kappa_metric,
            ledger.epsilon_vac_metric,
            ledger.e_kappa_metric,
        ],
        output=ledger.trace_total,
        method="sum residual trace channels after possible zeta-to-Bs insertion",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="residual_trace_ledger",
        scope="Group 25 residual kill or no-overlap theorem",
    )

    ns.record_derivation(
        derivation_id="residual_kill_double_count_load_25",
        inputs=[
            ledger.zeta_residual_metric,
            ledger.kappa_metric,
            ledger.epsilon_vac_metric,
            ledger.e_kappa_metric,
        ],
        output=ledger.double_count_load,
        method="sum non-Bs residual trace entries that must be killed, inert, or projected",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="double_count_load",
        scope="Group 25 residual kill or no-overlap theorem",
    )

    ns.record_derivation(
        derivation_id="residual_kill_problem_ledger_marker_25",
        inputs=[
            sp.Symbol("zeta_to_Bs"),
            sp.Symbol("zeta_residual_metric"),
            sp.Symbol("kappa_metric"),
            sp.Symbol("epsilon_vac_metric"),
            sp.Symbol("e_kappa_metric"),
            sp.Symbol("O_target"),
        ],
        output=sp.Symbol("residual_kill_problem_ledger_stated"),
        method="Group 25 residual kill / no-overlap opening ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="requirements_marker",
        scope="Group 25 residual kill or no-overlap theorem",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g25_derive_residual_kill_law", "Derive residual-kill law"),
        ("g25_derive_nonmetric_inertness", "Derive strict non-metric / inert residual status"),
        ("g25_derive_zeta_residual_nonreentry", "Derive zeta residual non-reentry"),
        ("g25_derive_kappa_residual_nonreentry", "Derive kappa residual non-reentry"),
        ("g25_derive_epsilon_ekappa_inertness", "Derive epsilon_vac_config and e_kappa inertness"),
        ("g25_derive_active_O_or_keep_closed", "Derive active no-overlap O or keep O closed"),
        ("g25_derive_recovery_independent_residual_status", "Derive recovery-independent residual status"),
        ("g25_preserve_boundary_source_guardrails", "Preserve boundary/source guardrails under residual cleanup"),
        ("g25_keep_parent_closed", "Keep parent equation closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g25_residual_control_route"],
            description=(
                "Residual control remains theorem-targeted until kill, inertness, non-reentry, active-O structure, "
                "recovery independence, boundary/source compatibility, and parent-closure discipline are derived."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g25_derive_residual_kill_law",
        "g25_derive_nonmetric_inertness",
        "g25_derive_zeta_residual_nonreentry",
        "g25_derive_kappa_residual_nonreentry",
        "g25_derive_epsilon_ekappa_inertness",
        "g25_derive_active_O_or_keep_closed",
        "g25_derive_recovery_independent_residual_status",
        "g25_preserve_boundary_source_guardrails",
        "g25_keep_parent_closed",
    ]

    ns.record_route(RouteRecord(
        route_id="g25_residual_control_route",
        script_id=SCRIPT_ID,
        name="Group 25 residual kill / no-overlap theorem target",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "residual double-count load is killed, inert, or projected by derived law",
            "zeta residual does not re-enter metric/source/boundary/support/recovery language",
            "kappa residual does not restore killed trace",
            "epsilon_vac_config and e_kappa remain non-metric/source inert",
            "active O is derived if used",
            "residual status is recovery-independent",
            "boundary/source guardrails are preserved",
            "parent equation remains closed",
        ],
    ))

    for branch_id in [
        "residual_kill_by_declaration",
        "kappa_kill_by_declaration",
        "epsilon_ekappa_ignored",
        "O_overlap_eraser",
        "recovery_selected_residual_status",
        "boundary_source_repair_residual_status",
        "residual_support_layer_reentry",
        "residual_source_reentry",
        "H_dark_exchange_curvature_residual_repair",
        "parent_from_residual_cleanup",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_25",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; residual control must be derived, not declared or repaired.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g25_residual_control_target_not_solved",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Group 25 opens the residual kill / no-overlap theorem target. "
            "The double-count load from residual zeta/kappa, epsilon_vac_config, and e_kappa must be killed, proven inert, "
            "or removed by a real no-overlap operator before B_s/F_zeta metric insertion can be licensed. "
            "No residual kill, non-metric inertness, active O, or parent closure is derived here."
        ),
        derivation_ids=[
            "residual_kill_trace_ledger_25",
            "residual_kill_double_count_load_25",
            "residual_kill_problem_ledger_marker_25",
        ],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Residual Kill Problem Ledger")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    ledger = build_problem_ledger()
    objects = build_residual_objects()
    routes = build_control_routes()
    shortcuts = build_rejected_shortcuts()

    case_0_problem_statement(out)
    case_1_trace_ledger(ledger, out)
    case_2_residual_objects(objects, out)
    case_3_control_routes(routes, out)
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
