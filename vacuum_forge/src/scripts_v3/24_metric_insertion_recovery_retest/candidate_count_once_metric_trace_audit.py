# Candidate count once metric trace audit
#
# Group:
#   24_metric_insertion_recovery_retest
#
# Script type:
#   REQUIREMENTS / DIAGNOSTIC
#
# Purpose
# -------
# Audit whether the candidate metric-insertion route counts scalar spatial trace
# exactly once.
#
# Locked-door question:
#
#   Does the insertion route count scalar spatial trace exactly once?
#
# This script does not derive count-once recombination.
# It does not derive residual-kill.
# It does not derive no-overlap O.
# It does not derive B_s/F_zeta insertion.
# It does not open parent equation closure.
#
# It records the current safe convention:
#
#   zeta may enter ordinary metric scalar trace through B_s only if
#   residual zeta_metric = 0 or is strictly non-metric/inert.
#
#   kappa_metric must be 0, diagnostic-only, or strictly non-metric/inert.
#
#   epsilon_vac_config and e_kappa must not become extra metric/source channels.
#
#   O cannot erase overlap by name.

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
        "ALLOWED_AUDIT": StatusMark.INFO,
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
            "metric_retest_dep_24",
            "24_metric_insertion_recovery_retest__candidate_metric_insertion_retest_ledger",
            "metric_insertion_retest_ledger_marker_24",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "recovery_antismuggle_dep_24",
            "24_metric_insertion_recovery_retest__candidate_recovery_target_anti_smuggling_audit",
            "recovery_target_anti_smuggling_marker_24",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g20_summary_dep_24",
            "20_no_overlap_and_projection_operators__candidate_no_overlap_projection_group_status_summary",
            "no_overlap_projection_group_status_summary_marker",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g22_nonmetric_dep_24",
            "22_boundary_neutrality_and_scalar_silence__candidate_diagnostic_residual_nonmetric_conditions",
            "diagnostic_residual_nonmetric_conditions_marker_22",
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
class CountOnceTraceLedger:
    zeta_to_Bs: sp.Symbol
    zeta_residual_metric: sp.Symbol
    kappa_metric: sp.Symbol
    epsilon_vac_metric: sp.Symbol
    e_kappa_metric: sp.Symbol
    trace_total: sp.Expr
    double_count_load: sp.Expr
    safe_trace_target: sp.Expr


@dataclass
class CountOnceCondition:
    name: str
    condition: str
    status: str
    failure_if: str
    consequence: str


@dataclass
class TraceRoute:
    name: str
    route: str
    status: str
    allowed_if: str
    rejected_if: str


@dataclass
class RejectedTraceRoute:
    name: str
    route: str
    forbidden_use: str
    status: str
    consequence: str


# =============================================================================
# Builders
# =============================================================================


def build_trace_ledger() -> CountOnceTraceLedger:
    zeta_to_Bs, zeta_residual_metric, kappa_metric, epsilon_vac_metric, e_kappa_metric = sp.symbols(
        "zeta_to_Bs zeta_residual_metric kappa_metric epsilon_vac_metric e_kappa_metric",
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
        zeta_residual_metric + kappa_metric + epsilon_vac_metric + e_kappa_metric
    )
    safe_trace_target = zeta_to_Bs

    return CountOnceTraceLedger(
        zeta_to_Bs=zeta_to_Bs,
        zeta_residual_metric=zeta_residual_metric,
        kappa_metric=kappa_metric,
        epsilon_vac_metric=epsilon_vac_metric,
        e_kappa_metric=e_kappa_metric,
        trace_total=trace_total,
        double_count_load=double_count_load,
        safe_trace_target=safe_trace_target,
    )


def build_conditions() -> List[CountOnceCondition]:
    return [
        CountOnceCondition(
            name="C1: zeta enters metric trace once",
            condition="zeta may enter ordinary metric scalar trace through B_s only once",
            status="REQUIRED",
            failure_if="zeta enters both B_s and residual metric trace",
            consequence="scalar spatial trace is double-counted",
        ),
        CountOnceCondition(
            name="C2: residual zeta metric trace killed or inert",
            condition="zeta_residual_metric = 0, or strictly non-metric/inert with no re-entry",
            status="REQUIRED",
            failure_if="residual zeta_metric survives after zeta is inserted into B_s",
            consequence="count-once recombination fails",
        ),
        CountOnceCondition(
            name="C3: kappa metric trace killed or diagnostic-only",
            condition="kappa_metric = 0, diagnostic-only, or strictly non-metric/inert",
            status="REQUIRED",
            failure_if="kappa restores killed residual trace or becomes physical scalar by areal diagnostic",
            consequence="areal kappa promotion sneaks metric trace back in",
        ),
        CountOnceCondition(
            name="C4: epsilon_vac_config not extra metric source",
            condition="epsilon_vac_config must not become additional ordinary metric/source channel",
            status="REQUIRED",
            failure_if="epsilon_vac_config contributes metric trace independently of B_s",
            consequence="hidden residual metric source appears",
        ),
        CountOnceCondition(
            name="C5: e_kappa not extra metric source",
            condition="e_kappa must not become additional ordinary metric/source channel",
            status="REQUIRED",
            failure_if="e_kappa contributes metric trace independently of B_s",
            consequence="kappa residual re-enters through energy label",
        ),
        CountOnceCondition(
            name="C6: no active O by name",
            condition="O may enforce no-overlap only if real operator structure is derived",
            status="REQUIRED",
            failure_if="O erases overlap, residual trace, or duplicate insertion by name",
            consequence="projection theorem is smuggled",
        ),
        CountOnceCondition(
            name="C7: no recovery-selected residual status",
            condition="residual-kill/nonmetric status must be fixed before recovery audit",
            status="REQUIRED",
            failure_if="residual status changes to pass AB/gamma/Schwarzschild recovery",
            consequence="count-once convention becomes recovery tuning",
        ),
    ]


def build_trace_routes() -> List[TraceRoute]:
    return [
        TraceRoute(
            name="R1: count-once B_s route",
            route="zeta -> B_s, residual zeta/kappa metric trace killed or non-metric",
            status="SAFE_IF",
            allowed_if="residual trace, epsilon_vac_config, e_kappa, and kappa_metric are zero/inert and non-reentering",
            rejected_if="any residual metric trace survives or re-enters",
        ),
        TraceRoute(
            name="R2: diagnostic kappa route",
            route="kappa_areal used as reduced diagnostic only",
            status="SAFE_IF",
            allowed_if="kappa does not become physical scalar or extra metric source",
            rejected_if="kappa restores residual trace or constructs B_s",
        ),
        TraceRoute(
            name="R3: active no-overlap route",
            route="O enforces count-once projection",
            status="THEOREM_TARGET",
            allowed_if="domain, kernel, image, divergence, boundary, and source compatibility are derived",
            rejected_if="O is invoked as eraser without operator structure",
        ),
        TraceRoute(
            name="R4: double-counted trace route",
            route="zeta enters B_s and residual metric trace",
            status="REJECTED",
            allowed_if="never in ordinary metric recombination",
            rejected_if="used to pass recovery or parent closure",
        ),
    ]


def build_rejected_routes() -> List[RejectedTraceRoute]:
    return [
        RejectedTraceRoute(
            name="D1: zeta double insertion",
            route="zeta_Bs_plus_zeta_residual_metric",
            forbidden_use="zeta contributes through B_s and through residual metric trace",
            status="REJECTED",
            consequence="ordinary scalar spatial trace counted twice",
        ),
        RejectedTraceRoute(
            name="D2: kappa residual restoration",
            route="kappa_restores_killed_trace",
            forbidden_use="kappa metric trace restores residual killed by count-once convention",
            status="REJECTED",
            consequence="residual-kill is undone through kappa",
        ),
        RejectedTraceRoute(
            name="D3: areal kappa ontology",
            route="areal_kappa_as_physical_scalar",
            forbidden_use="kappa_areal = 1/2 ln(AB) promoted to physical scalar insertion law",
            status="REJECTED",
            consequence="diagnostic relation becomes false metric ontology",
        ),
        RejectedTraceRoute(
            name="D4: epsilon_vac metric source",
            route="epsilon_vac_config_extra_metric_source",
            forbidden_use="epsilon_vac_config becomes independent ordinary metric/source trace",
            status="REJECTED",
            consequence="hidden metric source channel appears",
        ),
        RejectedTraceRoute(
            name="D5: e_kappa metric source",
            route="e_kappa_extra_metric_source",
            forbidden_use="e_kappa becomes independent ordinary metric/source trace",
            status="REJECTED",
            consequence="kappa energy label becomes metric insertion patch",
        ),
        RejectedTraceRoute(
            name="D6: O eraser",
            route="O_erases_trace_overlap_by_name",
            forbidden_use="O removes overlap without derived operator structure",
            status="REJECTED",
            consequence="no-overlap theorem is smuggled",
        ),
        RejectedTraceRoute(
            name="D7: recovery-selected residual kill",
            route="recovery_selected_residual_kill",
            forbidden_use="residual status chosen to pass AB/gamma/Schwarzschild checks",
            status="REJECTED",
            consequence="recovery becomes count-once construction",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Count-once metric trace audit problem")
    print("Question:")
    print()
    print("  Does the insertion route count scalar spatial trace exactly once?")
    print()
    print("Reference discipline:")
    print()
    print("  zeta may enter B_s only if residual zeta metric trace is killed or non-metric/inert.")
    print("  kappa must remain diagnostic/non-metric/inert unless derived.")
    print("  epsilon_vac_config and e_kappa must not become extra metric/source channels.")
    print("  O cannot erase overlap by name.")
    print("  This script audits the count-once burden; it does not derive it.")

    with out.governance_assessments():
        out.line(
            "count-once metric trace audit opened",
            StatusMark.INFO,
            "auditing whether scalar spatial trace is counted exactly once",
        )


def case_1_trace_ledger(ledger: CountOnceTraceLedger, out: ScriptOutput) -> None:
    header("Case 1: Count-once trace ledger")
    print("Metric trace entries:")
    print()
    print(f"  zeta_to_Bs = {sp.sstr(ledger.zeta_to_Bs)}")
    print(f"  zeta_residual_metric = {sp.sstr(ledger.zeta_residual_metric)}")
    print(f"  kappa_metric = {sp.sstr(ledger.kappa_metric)}")
    print(f"  epsilon_vac_metric = {sp.sstr(ledger.epsilon_vac_metric)}")
    print(f"  e_kappa_metric = {sp.sstr(ledger.e_kappa_metric)}")
    print()
    print("Total trace ledger:")
    print()
    print(f"  trace_total = {sp.sstr(ledger.trace_total)}")
    print()
    print("Double-count load:")
    print()
    print(f"  double_count_load = {sp.sstr(ledger.double_count_load)}")
    print()
    print("Safe count-once target:")
    print()
    print(f"  safe_trace_target = {sp.sstr(ledger.safe_trace_target)}")
    print()
    print("For count-once insertion, double_count_load must vanish or remain strictly inert/non-metric/non-reentering.")

    with out.derived_results():
        out.line(
            "count-once trace total ledger stated",
            StatusMark.PASS,
            f"trace_total = {sp.sstr(ledger.trace_total)}",
        )
        out.line(
            "double-count residual load ledger stated",
            StatusMark.OBLIGATION,
            f"double_count_load = {sp.sstr(ledger.double_count_load)}",
        )


def case_2_conditions(conditions: List[CountOnceCondition], out: ScriptOutput) -> None:
    header("Case 2: Count-once conditions")
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
            "count-once conditions populated",
            StatusMark.OBLIGATION,
            f"{len(conditions)} count-once conditions remain required",
        )


def case_3_trace_routes(routes: List[TraceRoute], out: ScriptOutput) -> None:
    header("Case 3: Trace route ledger")
    for route in routes:
        print()
        print("-" * 120)
        print(route.name)
        print("-" * 120)
        print(f"Route: {route.route}")
        print(f"[{status_mark(route.status).value}] {route.name}: {route.status}")
        print(f"Allowed if: {route.allowed_if}")
        print(f"Rejected if: {route.rejected_if}")

    with out.governance_assessments():
        out.line(
            "trace route ledger populated",
            StatusMark.PASS,
            f"{len(routes)} trace routes classified",
        )


def case_4_rejected_routes(routes: List[RejectedTraceRoute], out: ScriptOutput) -> None:
    header("Case 4: Rejected trace double-count routes")
    for route in routes:
        print()
        print("-" * 120)
        print(route.name)
        print("-" * 120)
        print(f"Route: {route.route}")
        print(f"Forbidden use: {route.forbidden_use}")
        print(f"[{status_mark(route.status).value}] {route.name}: {route.status}")
        print(f"Consequence: {route.consequence}")

    with out.counterexamples():
        out.line(
            "trace double-count routes rejected",
            StatusMark.FAIL,
            "zeta double insertion, kappa restoration, areal kappa ontology, epsilon/e_kappa metric sources, O eraser, and recovery-selected residual kill remain rejected",
        )


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("The count-once metric trace audit fails if a later script allows:")
    print()
    print("1. zeta enters both B_s and residual metric trace")
    print("2. residual zeta_metric survives after B_s insertion")
    print("3. kappa restores killed residual trace")
    print("4. areal kappa becomes physical scalar insertion law")
    print("5. epsilon_vac_config becomes extra metric/source channel")
    print("6. e_kappa becomes extra metric/source channel")
    print("7. residual relaxation becomes Box zeta / Box kappa by another name")
    print("8. O erases overlap without derived operator structure")
    print("9. residual-kill/nonmetric status selected by recovery failure")
    print("10. parent equation opened from count-once convention alone")

    with out.governance_assessments():
        out.line(
            "count-once trace failure controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not double-count scalar spatial trace or smuggle no-overlap",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Count-once metric trace result:")
    print()
    print("  zeta may enter ordinary metric scalar trace through B_s only once.")
    print("  residual zeta metric trace must be zero or strictly non-metric/inert/non-reentering.")
    print("  kappa metric trace must be zero, diagnostic-only, or strictly non-metric/inert.")
    print("  epsilon_vac_config and e_kappa must not become extra metric/source channels.")
    print("  O cannot erase overlap by name.")
    print("  recovery may not choose residual-kill/nonmetric status.")
    print()
    print("This is still a convention / theorem target, not a derived no-overlap law.")
    print()
    print("Possible next script:")
    print("  candidate_gamma_AB_recovery_diagnostics.py")
    print()
    print("Tiny goblin label:")
    print("  One trace coin. No pocket echo.")

    with out.governance_assessments():
        out.line(
            "count-once metric trace audit complete",
            StatusMark.PASS,
            "count-once trace burden explicit; no-overlap theorem remains open",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, ledger: CountOnceTraceLedger) -> None:
    ns.record_derivation(
        derivation_id="count_once_metric_trace_total_24",
        inputs=[
            ledger.zeta_to_Bs,
            ledger.zeta_residual_metric,
            ledger.kappa_metric,
            ledger.epsilon_vac_metric,
            ledger.e_kappa_metric,
        ],
        output=ledger.trace_total,
        method="sum representative scalar spatial metric trace channels",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="count_once_trace_ledger",
        scope="Group 24 metric insertion recovery retest",
    )

    ns.record_derivation(
        derivation_id="count_once_metric_trace_marker_24",
        inputs=[
            sp.Symbol("zeta_to_Bs"),
            sp.Symbol("zeta_residual_metric"),
            sp.Symbol("kappa_metric"),
            sp.Symbol("epsilon_vac_metric"),
            sp.Symbol("e_kappa_metric"),
            sp.Symbol("O_no_overlap_target"),
        ],
        output=sp.Symbol("count_once_metric_trace_conditions_stated"),
        method="Group 24 count-once metric trace audit",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="requirements_marker",
        scope="Group 24 metric insertion recovery retest",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g24_derive_zeta_count_once", "Derive zeta count-once trace insertion"),
        ("g24_derive_residual_zeta_inert", "Derive residual zeta metric inertness or kill"),
        ("g24_derive_kappa_metric_inert", "Derive kappa metric inertness or diagnostic-only status"),
        ("g24_derive_no_epsilon_extra_metric", "Derive epsilon_vac_config non-metric/source inertness"),
        ("g24_derive_no_ekappa_extra_metric", "Derive e_kappa non-metric/source inertness"),
        ("g24_derive_no_overlap_operator_or_keep_closed", "Derive no-overlap operator or keep O closed"),
        ("g24_derive_residual_status_recovery_independent", "Derive recovery-independent residual status"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g24_count_once_trace_route"],
            description=(
                "Count-once metric trace remains theorem-targeted until residual zeta/kappa, epsilon_vac_config, e_kappa, "
                "no-overlap, and recovery-independent residual status are derived or kept inert."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g24_derive_zeta_count_once",
        "g24_derive_residual_zeta_inert",
        "g24_derive_kappa_metric_inert",
        "g24_derive_no_epsilon_extra_metric",
        "g24_derive_no_ekappa_extra_metric",
        "g24_derive_no_overlap_operator_or_keep_closed",
        "g24_derive_residual_status_recovery_independent",
    ]

    ns.record_route(RouteRecord(
        route_id="g24_count_once_trace_route",
        script_id=SCRIPT_ID,
        name="Group 24 count-once metric trace theorem target",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "zeta enters B_s once",
            "residual zeta metric trace is zero/inert",
            "kappa metric trace is zero/diagnostic/inert",
            "epsilon_vac_config and e_kappa are not metric/source channels",
            "O is not used unless derived",
            "residual status is recovery-independent",
        ],
    ))

    for branch_id in [
        "zeta_double_insertion",
        "kappa_restores_trace",
        "areal_kappa_ontology",
        "epsilon_vac_metric_source",
        "e_kappa_metric_source",
        "O_trace_eraser",
        "recovery_selected_residual_kill",
        "parent_from_count_once_convention",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_24",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; count-once trace discipline is not a derived no-overlap theorem.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g24_count_once_trace_convention_not_theorem",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "zeta may enter ordinary metric scalar trace through B_s only if residual zeta/kappa metric trace is killed, "
            "diagnostic-only, or strictly non-metric/inert/non-reentering. epsilon_vac_config and e_kappa must not become extra metric/source channels. "
            "This is a convention/theorem target, not a derived no-overlap operator."
        ),
        derivation_ids=[
            "count_once_metric_trace_total_24",
            "count_once_metric_trace_marker_24",
        ],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Count Once Metric Trace Audit")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    ledger = build_trace_ledger()
    conditions = build_conditions()
    routes = build_trace_routes()
    rejected = build_rejected_routes()

    case_0_problem_statement(out)
    case_1_trace_ledger(ledger, out)
    case_2_conditions(conditions, out)
    case_3_trace_routes(routes, out)
    case_4_rejected_routes(rejected, out)
    case_5_failure_controls(out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, ledger)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
