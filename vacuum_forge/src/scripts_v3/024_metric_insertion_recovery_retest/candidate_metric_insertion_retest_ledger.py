# Candidate metric insertion retest ledger
#
# Group:
#   24_metric_insertion_recovery_retest
#
# Script type:
#   REQUIREMENTS / DIAGNOSTIC
#
# Purpose
# -------
# Open Group 24 by collecting the metric-insertion objects and guardrails.
#
# Locked-door question:
#
#   What exactly is being retested in B_s/F_zeta metric insertion?
#
# This script does not derive B_s/F_zeta insertion.
# It does not prove gamma-like recovery.
# It does not prove AB=1 as a parent law.
# It does not prove residual-kill or no-overlap.
# It does not prove boundary neutrality, scalar silence, compact support,
# no-shell matching, source compatibility, H insertability, or parent closure.
#
# It records that metric insertion is a retest target, not a solved construction.

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
        "STRUCTURAL": StatusMark.INFO,
        "THEOREM_TARGET": StatusMark.DEFER,
        "VIABLE_IF": StatusMark.INFO,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g20_no_overlap_dep_24",
            "20_no_overlap_and_projection_operators__candidate_no_overlap_projection_group_status_summary",
            "no_overlap_projection_group_status_summary_marker",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g21_summary_dep_24",
            "21_source_routing_and_mass_neutrality__candidate_group_21_source_routing_status_summary",
            "group21_source_routing_status_summary_marker_21",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g22_summary_dep_24",
            "22_boundary_neutrality_and_scalar_silence__candidate_group_22_boundary_neutrality_status_summary",
            "group22_boundary_neutrality_status_summary_marker_22",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g23_summary_dep_24",
            "23_smooth_support_and_matching_laws__candidate_group_23_matching_laws_status_summary",
            "group23_matching_laws_status_summary_marker_23",
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
class MetricInsertionObject:
    name: str
    symbol: str
    role: str
    status: str
    allowed_use: str
    forbidden_use: str


@dataclass
class RetestGuardrail:
    name: str
    source_group: str
    rule: str
    status: str
    failure_if: str


@dataclass
class MetricInsertionRisk:
    name: str
    risk: str
    status: str
    consequence: str


@dataclass
class ReducedDiagnosticLedger:
    A_ext: sp.Expr
    B_s_target: sp.Symbol
    zeta: sp.Symbol
    kappa_areal: sp.Expr
    AB_product: sp.Expr
    residual_trace_load: sp.Expr
    recovery_smuggling_load: sp.Expr


# =============================================================================
# Builders
# =============================================================================


def build_reduced_diagnostics() -> ReducedDiagnosticLedger:
    r = sp.Symbol("r", positive=True)
    G = sp.Symbol("G", positive=True)
    M = sp.Symbol("M", positive=True)
    c = sp.Symbol("c", positive=True)
    B_s_target = sp.Symbol("B_s_target", real=True)
    zeta = sp.Symbol("zeta", real=True)
    zeta_residual_metric, kappa_residual_metric = sp.symbols(
        "zeta_residual_metric kappa_residual_metric",
        real=True,
    )
    alpha_gamma, alpha_AB, alpha_Schw, alpha_support = sp.symbols(
        "alpha_gamma alpha_AB alpha_Schw alpha_support",
        real=True,
    )

    A_ext = sp.simplify(1 - 2 * G * M / (c**2 * r))
    B_diag = sp.simplify(1 / A_ext)
    AB_product = sp.simplify(A_ext * B_diag)
    kappa_areal = sp.simplify(sp.Rational(1, 2) * sp.log(AB_product))

    residual_trace_load = sp.simplify(zeta_residual_metric + kappa_residual_metric)
    recovery_smuggling_load = sp.simplify(alpha_gamma + alpha_AB + alpha_Schw + alpha_support)

    return ReducedDiagnosticLedger(
        A_ext=A_ext,
        B_s_target=B_s_target,
        zeta=zeta,
        kappa_areal=kappa_areal,
        AB_product=AB_product,
        residual_trace_load=residual_trace_load,
        recovery_smuggling_load=recovery_smuggling_load,
    )


def build_metric_insertion_objects() -> List[MetricInsertionObject]:
    return [
        MetricInsertionObject(
            name="M1: A-sector temporal response",
            symbol="A",
            role="reduced scalar temporal / mass-response field",
            status="DERIVED_REDUCED",
            allowed_use="ordinary exterior mass reference and recovery audit anchor",
            forbidden_use="not a license to construct B_s by copying GR spatial metric",
        ),
        MetricInsertionObject(
            name="M2: scalar spatial response target",
            symbol="B_s / A_spatial",
            role="candidate scalar spatial metric response companion",
            status="THEOREM_TARGET",
            allowed_use="metric insertion target to be audited",
            forbidden_use="not derived by B=1/A, gamma_like fitting, or GR copying",
        ),
        MetricInsertionObject(
            name="M3: candidate insertion map",
            symbol="B_s = F_zeta[A, zeta, J_V, Sigma_V, R_V]",
            role="candidate route connecting volume response to scalar spatial trace",
            status="THEOREM_TARGET",
            allowed_use="future theorem target if coefficient origin and constraints are derived",
            forbidden_use="not a current field law or construction rule",
        ),
        MetricInsertionObject(
            name="M4: zeta volume-form candidate",
            symbol="zeta = ln sqrt(gamma)",
            role="spatial volume-form candidate",
            status="STRUCTURAL",
            allowed_use="candidate geometric input to F_zeta",
            forbidden_use="must not enter B_s and residual metric trace simultaneously",
        ),
        MetricInsertionObject(
            name="M5: kappa areal diagnostic",
            symbol="kappa_areal = 1/2 ln(AB)",
            role="reduced areal-gauge diagnostic",
            status="DIAGNOSTIC_ONLY",
            allowed_use="static exterior recovery check",
            forbidden_use="not a physical scalar or parent construction law unless derived",
        ),
        MetricInsertionObject(
            name="M6: residual-kill / non-metric convention",
            symbol="zeta_residual_metric = 0; kappa_residual_metric = 0 or non-metric",
            role="count-once provisional convention",
            status="SAFE_IF",
            allowed_use="safest current metric recombination convention",
            forbidden_use="not a derived no-overlap theorem",
        ),
        MetricInsertionObject(
            name="M7: no-overlap operator target",
            symbol="O[B_s, zeta_residual/kappa_residual, J_V]",
            role="future active no-overlap / projection theorem target",
            status="THEOREM_TARGET",
            allowed_use="future route only if domain/kernel/image/divergence/boundary/source laws are derived",
            forbidden_use="not an eraser by name",
        ),
        MetricInsertionObject(
            name="M8: recovery targets",
            symbol="Schwarzschild, gamma_like, AB, B=1/A, PPN-like checks",
            role="downstream diagnostics",
            status="RECOVERY_TARGET",
            allowed_use="audit after insertion data are structurally fixed",
            forbidden_use="must not choose insertion coefficients, support, residual status, or boundary data",
        ),
    ]


def build_guardrails() -> List[RetestGuardrail]:
    return [
        RetestGuardrail(
            name="G20: no active O by declaration",
            source_group="Group 20",
            rule="No universal active O is defined; role-specific projectors require full operator structure.",
            status="REQUIRED",
            failure_if="O erases metric overlap, boundary leakage, source duplication, or scalar tails by name",
        ),
        RetestGuardrail(
            name="G21: A-sector source/mass protection",
            source_group="Group 21",
            rule="ordinary rho/M_enc remains A-routed; non-A sectors may not shift exterior mass or duplicate source load",
            status="REQUIRED",
            failure_if="B_s/F_zeta coefficient becomes ordinary source reservoir or non-A mass route",
        ),
        RetestGuardrail(
            name="G22: boundary/scalar silence",
            source_group="Group 22",
            rule="delta F_A|boundary,non-A = 0; C_i = 0; I_nonA = 0; no shell; no recovery smoothing; no O/H repair",
            status="REQUIRED",
            failure_if="metric insertion leaves scalar tail, current flux, A-tail, shell source, or repair route",
        ),
        RetestGuardrail(
            name="G23: smooth support and matching",
            source_group="Group 23",
            rule="support origin, value/slope matching, shell absence, transition neutrality, recovery independence, source compatibility remain required",
            status="REQUIRED",
            failure_if="metric insertion uses toy support, smoothness, recovery-selected seam data, or source seam pockets",
        ),
        RetestGuardrail(
            name="R1: recovery downstream only",
            source_group="Recovery audit",
            rule="Schwarzschild, AB, B=1/A, gamma_like, and PPN-like checks may audit only after insertion data are fixed",
            status="REQUIRED",
            failure_if="recovery target chooses F_zeta coefficients, support radius, smoothing width, or residual status",
        ),
        RetestGuardrail(
            name="R2: parent gate closed",
            source_group="Parent closure guard",
            rule="metric insertion retest cannot open parent equation without insertion, divergence, source, boundary, support, and no-overlap theorems",
            status="REQUIRED",
            failure_if="parent equation is written from retest ledger alone",
        ),
    ]


def build_risks() -> List[MetricInsertionRisk]:
    return [
        MetricInsertionRisk(
            name="K1: GR spatial metric copy",
            risk="B_s copied from Schwarzschild or GR spatial metric",
            status="REJECTED",
            consequence="silent GR import replaces insertion theorem",
        ),
        MetricInsertionRisk(
            name="K2: B=1/A construction",
            risk="static exterior diagnostic B=1/A promoted to parent construction rule",
            status="REJECTED",
            consequence="recovery check becomes smuggled dynamics",
        ),
        MetricInsertionRisk(
            name="K3: gamma-like coefficient fit",
            risk="coefficient chosen to make gamma_like or PPN response pass",
            status="REJECTED",
            consequence="recovery chooses the branch",
        ),
        MetricInsertionRisk(
            name="K4: areal kappa promotion",
            risk="kappa_areal treated as physical scalar insertion law",
            status="REJECTED",
            consequence="reduced diagnostic becomes false ontology",
        ),
        MetricInsertionRisk(
            name="K5: scalar trace double-counting",
            risk="zeta enters B_s while residual zeta/kappa metric trace survives",
            status="REJECTED",
            consequence="scalar spatial trace is counted twice",
        ),
        MetricInsertionRisk(
            name="K6: support / boundary smuggling",
            risk="metric insertion uses compact support, smoothing, or boundary data selected from recovery",
            status="REJECTED",
            consequence="Group 22/23 seam guardrails are bypassed",
        ),
        MetricInsertionRisk(
            name="K7: source seam pocket",
            risk="B_s/F_zeta coefficient, support radius, or layer parameter hides ordinary source load",
            status="REJECTED",
            consequence="ordinary source no-double-counting fails",
        ),
        MetricInsertionRisk(
            name="K8: H or dark insertion patch",
            risk="H_curv/H_exch or dark labels patch insertion failure",
            status="REJECTED",
            consequence="non-insertable repair object enters metric branch",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Metric insertion retest ledger problem")
    print("Question:")
    print()
    print("  What exactly is being retested in B_s/F_zeta metric insertion?")
    print()
    print("Reference discipline:")
    print()
    print("  Group 24 retests metric insertion under Group 20-23 guardrails.")
    print("  B_s/F_zeta is a theorem target, not a solved construction.")
    print("  Recovery may audit but not construct.")
    print("  No O eraser, no H patch, no dark patch, no recovery-selected support, and no parent equation are used.")

    with out.governance_assessments():
        out.line(
            "metric insertion retest ledger opened",
            StatusMark.INFO,
            "collecting B_s/F_zeta retest objects and inherited guardrails",
        )


def case_1_reduced_diagnostics(ledger: ReducedDiagnosticLedger, out: ScriptOutput) -> None:
    header("Case 1: Reduced diagnostic anchors")
    print("Reduced A-sector exterior:")
    print()
    print(f"  A_ext = {sp.sstr(ledger.A_ext)}")
    print()
    print("Static exterior AB diagnostic if B_diag = 1/A_ext:")
    print()
    print(f"  AB_product = {sp.sstr(ledger.AB_product)}")
    print(f"  kappa_areal = 1/2 ln(AB_product) = {sp.sstr(ledger.kappa_areal)}")
    print()
    print("Count-once residual trace load:")
    print()
    print(f"  residual_trace_load = {sp.sstr(ledger.residual_trace_load)}")
    print()
    print("Recovery-smuggling load:")
    print()
    print(f"  recovery_smuggling_load = {sp.sstr(ledger.recovery_smuggling_load)}")
    print()
    print("Interpretation:")
    print()
    print("  AB=1 and kappa_areal=0 are reduced exterior diagnostics.")
    print("  They do not construct B_s/F_zeta as a parent law.")
    print("  residual_trace_load and recovery_smuggling_load must vanish or remain theorem-targeted before insertion is licensed.")

    with out.derived_results():
        out.line(
            "static exterior AB diagnostic stated",
            StatusMark.PASS,
            f"AB = {sp.sstr(ledger.AB_product)}, kappa_areal = {sp.sstr(ledger.kappa_areal)}",
        )
        out.line(
            "count-once residual trace ledger stated",
            StatusMark.OBLIGATION,
            f"residual_trace_load = {sp.sstr(ledger.residual_trace_load)}",
        )
        out.line(
            "recovery-smuggling ledger stated",
            StatusMark.OBLIGATION,
            f"recovery_smuggling_load = {sp.sstr(ledger.recovery_smuggling_load)}",
        )


def case_2_object_inventory(objects: List[MetricInsertionObject], out: ScriptOutput) -> None:
    header("Case 2: Metric insertion object inventory")
    for obj in objects:
        print()
        print("-" * 120)
        print(obj.name)
        print("-" * 120)
        print(f"Symbol: {obj.symbol}")
        print(f"Role: {obj.role}")
        print(f"[{status_mark(obj.status).value}] {obj.name}: {obj.status}")
        print(f"Allowed use: {obj.allowed_use}")
        print(f"Forbidden use: {obj.forbidden_use}")

    with out.governance_assessments():
        out.line(
            "metric insertion object inventory populated",
            StatusMark.PASS,
            f"{len(objects)} metric-insertion objects classified",
        )


def case_3_guardrail_ledger(guardrails: List[RetestGuardrail], out: ScriptOutput) -> None:
    header("Case 3: Retest guardrail ledger")
    for guardrail in guardrails:
        print()
        print("-" * 120)
        print(guardrail.name)
        print("-" * 120)
        print(f"Source group: {guardrail.source_group}")
        print(f"Rule: {guardrail.rule}")
        print(f"[{status_mark(guardrail.status).value}] {guardrail.name}: {guardrail.status}")
        print(f"Failure if: {guardrail.failure_if}")

    with out.unresolved_obligations():
        out.line(
            "metric insertion guardrails imported",
            StatusMark.OBLIGATION,
            f"{len(guardrails)} inherited guardrails constrain B_s/F_zeta retest",
        )


def case_4_risk_ledger(risks: List[MetricInsertionRisk], out: ScriptOutput) -> None:
    header("Case 4: Metric insertion risk ledger")
    for risk in risks:
        print()
        print("-" * 120)
        print(risk.name)
        print("-" * 120)
        print(f"Risk: {risk.risk}")
        print(f"[{status_mark(risk.status).value}] {risk.name}: {risk.status}")
        print(f"Consequence: {risk.consequence}")

    with out.counterexamples():
        out.line(
            "metric insertion false construction routes rejected",
            StatusMark.FAIL,
            "GR copying, B=1/A construction, gamma fitting, kappa promotion, trace double-counting, seam smuggling, source pockets, and H/dark patches remain rejected",
        )


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("The metric insertion retest ledger fails if a later script allows:")
    print()
    print("1. B_s copied from Schwarzschild / GR spatial metric")
    print("2. B=1/A used as a general construction rule")
    print("3. gamma_like or PPN response used to choose coefficients")
    print("4. AB=1 used as a parent insertion law")
    print("5. areal kappa promoted to physical scalar")
    print("6. zeta inserted into both B_s and residual metric trace")
    print("7. kappa restores killed residual trace")
    print("8. O erases overlap by name")
    print("9. H or dark label patches insertion failure")
    print("10. compact support, smoothing, layer, or boundary data chosen from recovery")
    print("11. ordinary source load hidden in insertion/support/layer coefficients")
    print("12. parent equation opened from retest ledger alone")

    with out.governance_assessments():
        out.line(
            "metric insertion retest overclaim controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not turn recovery diagnostics into construction rules",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Group 24 opening result:")
    print()
    print("  B_s/F_zeta metric insertion is a retest target.")
    print("  A-sector exterior recovery is an anchor, not a spatial metric construction.")
    print("  AB=1, B=1/A, gamma_like, and areal kappa remain recovery diagnostics.")
    print("  Count-once residual handling remains provisional.")
    print("  No active O is available.")
    print("  No H insertion is available.")
    print("  Group 22 boundary/scalar and Group 23 matching/support guardrails remain active.")
    print("  Parent equation remains not ready.")
    print()
    print("Possible next script:")
    print("  candidate_recovery_target_anti_smuggling_audit.py")
    print()
    print("Tiny goblin label:")
    print("  Check the mirror. Do not let it hold the knife.")

    with out.governance_assessments():
        out.line(
            "metric insertion retest ledger complete",
            StatusMark.PASS,
            "B_s/F_zeta retest objects and guardrails explicit; insertion theorem remains open",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, ledger: ReducedDiagnosticLedger) -> None:
    ns.record_derivation(
        derivation_id="metric_insertion_retest_reduced_AB_diagnostic_24",
        inputs=[ledger.A_ext],
        output=sp.Tuple(ledger.AB_product, ledger.kappa_areal),
        method="evaluate reduced exterior AB diagnostic with B_diag = 1/A_ext",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="metric_insertion_recovery_diagnostic",
        scope="Group 24 metric insertion recovery retest",
    )

    ns.record_derivation(
        derivation_id="metric_insertion_retest_residual_trace_ledger_24",
        inputs=[ledger.residual_trace_load],
        output=ledger.residual_trace_load,
        method="represent count-once residual zeta/kappa trace load",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="count_once_residual_trace_ledger",
        scope="Group 24 metric insertion recovery retest",
    )

    ns.record_derivation(
        derivation_id="metric_insertion_retest_ledger_marker_24",
        inputs=[
            sp.Symbol("A_ext"),
            sp.Symbol("B_s_target"),
            sp.Symbol("F_zeta"),
            sp.Symbol("zeta"),
            sp.Symbol("kappa_areal"),
            sp.Symbol("residual_kill"),
            sp.Symbol("recovery_downstream"),
        ],
        output=sp.Symbol("metric_insertion_retest_ledger_stated"),
        method="Group 24 metric insertion retest ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="requirements_marker",
        scope="Group 24 metric insertion recovery retest",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g24_define_F_zeta_target", "Define the F_zeta insertion target without claiming it as a law"),
        ("g24_keep_recovery_downstream", "Keep recovery downstream of insertion construction"),
        ("g24_preserve_count_once_trace", "Preserve count-once scalar trace discipline"),
        ("g24_preserve_no_active_O", "Preserve no-active-O discipline"),
        ("g24_preserve_boundary_support_guards", "Preserve boundary/scalar and support/matching guardrails"),
        ("g24_preserve_source_compatibility", "Preserve ordinary source no-double-counting"),
        ("g24_keep_parent_closed", "Keep parent equation closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g24_metric_insertion_retest_route"],
            description=(
                "Metric insertion retest remains theorem-targeted until F_zeta coefficient origin, count-once recombination, "
                "recovery independence, boundary/support compatibility, source compatibility, and no-repair constraints are derived."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g24_define_F_zeta_target",
        "g24_keep_recovery_downstream",
        "g24_preserve_count_once_trace",
        "g24_preserve_no_active_O",
        "g24_preserve_boundary_support_guards",
        "g24_preserve_source_compatibility",
        "g24_keep_parent_closed",
    ]

    ns.record_route(RouteRecord(
        route_id="g24_metric_insertion_retest_route",
        script_id=SCRIPT_ID,
        name="Group 24 B_s/F_zeta metric insertion retest target",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "F_zeta insertion is treated as theorem target",
            "recovery is downstream audit only",
            "count-once residual trace discipline is preserved",
            "no active O or H insertion is assumed",
            "boundary/support and source guardrails remain active",
            "parent equation remains closed",
        ],
    ))

    for branch_id in [
        "GR_spatial_metric_copy",
        "B_inverse_A_construction",
        "gamma_like_coefficient_fit",
        "AB_parent_law",
        "areal_kappa_physical_scalar",
        "scalar_trace_double_counting",
        "support_boundary_smuggling",
        "source_seam_pocket",
        "H_dark_insertion_patch",
        "parent_from_metric_retest",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_24",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; metric insertion retest cannot become recovery-selected construction or parent closure.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g24_metric_insertion_retest_not_construction",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "B_s/F_zeta metric insertion is a retest target, not a solved construction. "
            "A-sector recovery, AB, B=1/A, gamma_like, and areal kappa may audit only after insertion data are structurally fixed. "
            "No active O, H insertion, recovery-selected seam data, source seam pocket, or parent equation is licensed."
        ),
        derivation_ids=[
            "metric_insertion_retest_reduced_AB_diagnostic_24",
            "metric_insertion_retest_residual_trace_ledger_24",
            "metric_insertion_retest_ledger_marker_24",
        ],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Metric Insertion Retest Ledger")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    diagnostics = build_reduced_diagnostics()
    objects = build_metric_insertion_objects()
    guardrails = build_guardrails()
    risks = build_risks()

    case_0_problem_statement(out)
    case_1_reduced_diagnostics(diagnostics, out)
    case_2_object_inventory(objects, out)
    case_3_guardrail_ledger(guardrails, out)
    case_4_risk_ledger(risks, out)
    case_5_failure_controls(out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, diagnostics)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
