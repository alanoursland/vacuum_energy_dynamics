# Candidate recovery target anti-smuggling audit
#
# Group:
#   24_metric_insertion_recovery_retest
#
# Script type:
#   REQUIREMENTS / DIAGNOSTIC
#
# Purpose
# -------
# Separate recovery tests from metric-insertion construction rules.
#
# Locked-door question:
#
#   Which recovery targets may audit B_s/F_zeta, and which may not construct it?
#
# This script does not derive B_s/F_zeta insertion.
# It does not prove gamma-like recovery.
# It does not prove AB=1 as a parent law.
# It does not prove B=1/A as a construction rule.
# It does not promote areal kappa to a physical scalar.
# It does not open the parent field equation.
#
# It records that recovery may test only after insertion data are structurally fixed.

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
            "024_metric_insertion_recovery_retest__candidate_metric_insertion_retest_ledger",
            "metric_insertion_retest_ledger_marker_24",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g23_summary_dep_24",
            "023_smooth_support_and_matching_laws__candidate_group_23_matching_laws_status_summary",
            "group23_matching_laws_status_summary_marker_23",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g22_summary_dep_24",
            "022_boundary_neutrality_and_scalar_silence__candidate_group_22_boundary_neutrality_status_summary",
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
class RecoveryAuditTarget:
    name: str
    target: str
    allowed_role: str
    status: str
    forbidden_construction: str


@dataclass
class RecoverySmugglingRoute:
    name: str
    route: str
    status: str
    forbidden_use: str
    consequence: str


@dataclass
class RecoveryDisciplineCondition:
    name: str
    condition: str
    status: str
    failure_if: str


@dataclass
class RecoveryDiagnosticLedger:
    gamma_like_target: sp.Symbol
    AB_target: sp.Integer
    kappa_areal_target: sp.Integer
    alpha_gamma_fit: sp.Symbol
    alpha_AB_fit: sp.Symbol
    alpha_BinvA_fit: sp.Symbol
    alpha_support_fit: sp.Symbol
    smuggling_load: sp.Expr


# =============================================================================
# Builders
# =============================================================================


def build_diagnostics() -> RecoveryDiagnosticLedger:
    gamma_like_target = sp.Symbol("gamma_like_target", real=True)
    alpha_gamma_fit, alpha_AB_fit, alpha_BinvA_fit, alpha_support_fit = sp.symbols(
        "alpha_gamma_fit alpha_AB_fit alpha_BinvA_fit alpha_support_fit",
        real=True,
    )
    AB_target = sp.Integer(1)
    kappa_areal_target = sp.Integer(0)
    smuggling_load = sp.simplify(alpha_gamma_fit + alpha_AB_fit + alpha_BinvA_fit + alpha_support_fit)

    return RecoveryDiagnosticLedger(
        gamma_like_target=gamma_like_target,
        AB_target=AB_target,
        kappa_areal_target=kappa_areal_target,
        alpha_gamma_fit=alpha_gamma_fit,
        alpha_AB_fit=alpha_AB_fit,
        alpha_BinvA_fit=alpha_BinvA_fit,
        alpha_support_fit=alpha_support_fit,
        smuggling_load=smuggling_load,
    )


def build_audit_targets() -> List[RecoveryAuditTarget]:
    return [
        RecoveryAuditTarget(
            name="T1: Schwarzschild exterior",
            target="A=1-2GM/(c^2 r), B=1/A in reduced static exterior",
            allowed_role="downstream reduced exterior audit",
            status="ALLOWED_AUDIT",
            forbidden_construction="copying GR spatial metric into B_s/F_zeta",
        ),
        RecoveryAuditTarget(
            name="T2: AB diagnostic",
            target="AB=1 in reduced exterior diagnostic branch",
            allowed_role="reduced areal diagnostic after branch data are fixed",
            status="ALLOWED_AUDIT",
            forbidden_construction="using AB=1 as parent insertion law",
        ),
        RecoveryAuditTarget(
            name="T3: B=1/A diagnostic",
            target="B=1/A in static spherical exterior",
            allowed_role="recovered exterior relation",
            status="ALLOWED_AUDIT",
            forbidden_construction="using B=1/A to construct B_s generally",
        ),
        RecoveryAuditTarget(
            name="T4: gamma-like weak-field response",
            target="gamma_like or PPN-like scalar spatial response",
            allowed_role="weak-field recovery audit",
            status="ALLOWED_AUDIT",
            forbidden_construction="choosing coefficient or insertion form to make gamma_like pass",
        ),
        RecoveryAuditTarget(
            name="T5: areal kappa diagnostic",
            target="kappa_areal = 1/2 ln(AB)",
            allowed_role="reduced gauge-conditioned diagnostic",
            status="DIAGNOSTIC_ONLY",
            forbidden_construction="promoting areal kappa to physical scalar insertion law",
        ),
        RecoveryAuditTarget(
            name="T6: boundary/support compatibility checks",
            target="no shell, no tail, no recovery-selected smoothing/support",
            allowed_role="downstream guardrail audit",
            status="ALLOWED_AUDIT",
            forbidden_construction="choosing support radius, smoothing width, or boundary data to pass recovery",
        ),
    ]


def build_smuggling_routes() -> List[RecoverySmugglingRoute]:
    return [
        RecoverySmugglingRoute(
            name="S1: GR metric copy",
            route="copy_Schwarzschild_or_GR_spatial_metric",
            status="REJECTED",
            forbidden_use="B_s/F_zeta is set equal to the known GR spatial response",
            consequence="recovery target becomes hidden construction",
        ),
        RecoverySmugglingRoute(
            name="S2: AB product fit",
            route="AB_product_fit",
            status="REJECTED",
            forbidden_use="coefficient selected so AB=1",
            consequence="AB diagnostic becomes parent law by tuning",
        ),
        RecoverySmugglingRoute(
            name="S3: B inverse A fit",
            route="B_inverse_A_fit",
            status="REJECTED",
            forbidden_use="B=1/A imposed outside reduced exterior recovery",
            consequence="static exterior relation becomes false general construction",
        ),
        RecoverySmugglingRoute(
            name="S4: gamma-like fit",
            route="gamma_like_fit",
            status="REJECTED",
            forbidden_use="insertion coefficient selected to make gamma_like or PPN response pass",
            consequence="weak-field recovery constructs the branch",
        ),
        RecoverySmugglingRoute(
            name="S5: areal kappa promotion",
            route="areal_kappa_promotion",
            status="REJECTED",
            forbidden_use="kappa_areal = 1/2 ln(AB) treated as physical scalar dynamics",
            consequence="diagnostic relation becomes ontology",
        ),
        RecoverySmugglingRoute(
            name="S6: recovery-selected seam",
            route="recovery_selected_support_smoothing_boundary",
            status="REJECTED",
            forbidden_use="support radius, smoothing width, transition layer, or boundary data chosen to pass recovery",
            consequence="Group 23 seam guardrails are bypassed",
        ),
        RecoverySmugglingRoute(
            name="S7: recovery-selected residual status",
            route="recovery_selected_residual_status",
            status="REJECTED",
            forbidden_use="residual-kill/nonmetric status chosen after recovery failure appears",
            consequence="count-once convention becomes tuning",
        ),
    ]


def build_conditions() -> List[RecoveryDisciplineCondition]:
    return [
        RecoveryDisciplineCondition(
            name="C1: insertion data fixed before recovery",
            condition="F_zeta form and coefficients must be structural or theorem-targeted before recovery tests",
            status="REQUIRED",
            failure_if="recovery target chooses insertion form or coefficient",
        ),
        RecoveryDisciplineCondition(
            name="C2: support data fixed before recovery",
            condition="support radius, smoothing width, transition layer, and boundary data must be independent of recovery",
            status="REQUIRED",
            failure_if="Schwarzschild/PPN/AB/gamma_like chooses seam data",
        ),
        RecoveryDisciplineCondition(
            name="C3: residual status fixed before recovery",
            condition="residual-kill/nonmetric status must not be selected from recovery outcomes",
            status="REQUIRED",
            failure_if="zeta/kappa residual status changes to make recovery pass",
        ),
        RecoveryDisciplineCondition(
            name="C4: recovery may reject",
            condition="recovery tests may reject or classify a candidate branch",
            status="ALLOWED_AUDIT",
            failure_if="rejection is converted into parameter tuning",
        ),
        RecoveryDisciplineCondition(
            name="C5: parent gate remains closed",
            condition="successful reduced recovery audit does not itself open parent equation",
            status="REQUIRED",
            failure_if="parent equation is written from recovery success alone",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Recovery target anti-smuggling problem")
    print("Question:")
    print()
    print("  Which recovery targets may audit B_s/F_zeta, and which may not construct it?")
    print()
    print("Reference discipline:")
    print()
    print("  Group 24 retests metric insertion.")
    print("  Recovery may audit after insertion data are structurally fixed.")
    print("  Recovery may not choose coefficients, support, smoothing, residual status, or boundary data.")

    with out.governance_assessments():
        out.line(
            "recovery target anti-smuggling audit opened",
            StatusMark.INFO,
            "separating allowed recovery diagnostics from forbidden construction rules",
        )


def case_1_diagnostics(ledger: RecoveryDiagnosticLedger, out: ScriptOutput) -> None:
    header("Case 1: Recovery-smuggling diagnostic ledger")
    print("Recovery target diagnostics:")
    print()
    print(f"  gamma_like_target = {sp.sstr(ledger.gamma_like_target)}")
    print(f"  AB_target = {sp.sstr(ledger.AB_target)}")
    print(f"  kappa_areal_target = {sp.sstr(ledger.kappa_areal_target)}")
    print()
    print("Forbidden fit coefficients:")
    print()
    print(f"  alpha_gamma_fit = {sp.sstr(ledger.alpha_gamma_fit)}")
    print(f"  alpha_AB_fit = {sp.sstr(ledger.alpha_AB_fit)}")
    print(f"  alpha_BinvA_fit = {sp.sstr(ledger.alpha_BinvA_fit)}")
    print(f"  alpha_support_fit = {sp.sstr(ledger.alpha_support_fit)}")
    print()
    print("Recovery-smuggling load:")
    print()
    print(f"  smuggling_load = {sp.sstr(ledger.smuggling_load)}")
    print()
    print("All fit coefficients must vanish or remain blocked; recovery targets may audit but not select them.")

    with out.derived_results():
        out.line(
            "recovery-smuggling load ledger stated",
            StatusMark.OBLIGATION,
            f"smuggling_load = {sp.sstr(ledger.smuggling_load)}",
        )


def case_2_audit_targets(targets: List[RecoveryAuditTarget], out: ScriptOutput) -> None:
    header("Case 2: Allowed recovery audit targets")
    for target in targets:
        print()
        print("-" * 120)
        print(target.name)
        print("-" * 120)
        print(f"Target: {target.target}")
        print(f"Allowed role: {target.allowed_role}")
        print(f"[{status_mark(target.status).value}] {target.name}: {target.status}")
        print(f"Forbidden construction: {target.forbidden_construction}")

    with out.governance_assessments():
        out.line(
            "recovery audit target ledger populated",
            StatusMark.PASS,
            f"{len(targets)} recovery targets classified as audit-only or diagnostic-only",
        )


def case_3_smuggling_routes(routes: List[RecoverySmugglingRoute], out: ScriptOutput) -> None:
    header("Case 3: Rejected recovery-smuggling routes")
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
            "recovery-smuggling routes rejected",
            StatusMark.FAIL,
            "GR copy, AB/B=1/A/gamma fits, kappa promotion, seam selection, and residual-status selection remain rejected",
        )


def case_4_conditions(conditions: List[RecoveryDisciplineCondition], out: ScriptOutput) -> None:
    header("Case 4: Recovery discipline conditions")
    for condition in conditions:
        print()
        print("-" * 120)
        print(condition.name)
        print("-" * 120)
        print(f"Condition: {condition.condition}")
        print(f"[{status_mark(condition.status).value}] {condition.name}: {condition.status}")
        print(f"Failure if: {condition.failure_if}")

    with out.unresolved_obligations():
        out.line(
            "recovery discipline conditions populated",
            StatusMark.OBLIGATION,
            f"{len(conditions)} recovery-discipline conditions constrain metric insertion",
        )


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("The recovery anti-smuggling audit fails if a later script allows:")
    print()
    print("1. GR spatial metric copied into B_s")
    print("2. AB=1 used to choose insertion coefficient")
    print("3. B=1/A used as a general B_s construction rule")
    print("4. gamma_like or PPN response used to select coefficient")
    print("5. areal kappa promoted to physical scalar insertion law")
    print("6. support radius chosen from Schwarzschild recovery")
    print("7. smoothing width or transition layer chosen from PPN/gamma/AB recovery")
    print("8. residual-kill or nonmetric status chosen from recovery failure")
    print("9. recovery success opens parent equation")

    with out.governance_assessments():
        out.line(
            "recovery anti-smuggling failure controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not convert recovery diagnostics into construction rules",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Recovery targets may audit B_s/F_zeta only after insertion data are fixed.")
    print()
    print("Allowed as audit:")
    print()
    print("  Schwarzschild exterior")
    print("  AB diagnostic")
    print("  B=1/A reduced exterior relation")
    print("  gamma_like / PPN-like response")
    print("  areal kappa diagnostic")
    print("  boundary/support compatibility checks")
    print()
    print("Rejected as construction:")
    print()
    print("  GR spatial metric copy")
    print("  AB coefficient fit")
    print("  B=1/A construction")
    print("  gamma-like coefficient fit")
    print("  areal kappa promotion")
    print("  recovery-selected seam")
    print("  recovery-selected residual status")
    print()
    print("Possible next script:")
    print("  candidate_count_once_metric_trace_audit.py")
    print()
    print("Tiny goblin label:")
    print("  The mirror judges. It does not forge.")

    with out.governance_assessments():
        out.line(
            "recovery target anti-smuggling audit complete",
            StatusMark.PASS,
            "recovery is downstream audit only; metric insertion theorem remains open",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, ledger: RecoveryDiagnosticLedger) -> None:
    ns.record_derivation(
        derivation_id="recovery_anti_smuggling_load_24",
        inputs=[
            ledger.alpha_gamma_fit,
            ledger.alpha_AB_fit,
            ledger.alpha_BinvA_fit,
            ledger.alpha_support_fit,
        ],
        output=ledger.smuggling_load,
        method="sum representative forbidden recovery-selected fit coefficients",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="recovery_smuggling_ledger",
        scope="Group 24 metric insertion recovery retest",
    )

    ns.record_derivation(
        derivation_id="recovery_target_anti_smuggling_marker_24",
        inputs=[
            sp.Symbol("Schwarzschild_audit"),
            sp.Symbol("AB_audit"),
            sp.Symbol("B_inverse_A_audit"),
            sp.Symbol("gamma_like_audit"),
            sp.Symbol("areal_kappa_audit"),
            sp.Symbol("support_boundary_audit"),
        ],
        output=sp.Symbol("recovery_target_anti_smuggling_conditions_stated"),
        method="Group 24 recovery target anti-smuggling audit",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="requirements_marker",
        scope="Group 24 metric insertion recovery retest",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g24_derive_insertion_before_recovery", "Derive insertion data before recovery audit"),
        ("g24_derive_no_recovery_coeff_fit", "Derive no recovery-selected coefficient fit"),
        ("g24_derive_no_recovery_seam_fit", "Derive no recovery-selected support/smoothing/boundary data"),
        ("g24_derive_no_recovery_residual_fit", "Derive no recovery-selected residual status"),
        ("g24_keep_parent_closed_after_recovery", "Keep parent equation closed after recovery audit"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g24_recovery_antismuggle_route"],
            description=(
                "Recovery may audit metric insertion only after insertion coefficients, seam data, and residual status are fixed structurally."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g24_derive_insertion_before_recovery",
        "g24_derive_no_recovery_coeff_fit",
        "g24_derive_no_recovery_seam_fit",
        "g24_derive_no_recovery_residual_fit",
        "g24_keep_parent_closed_after_recovery",
    ]

    ns.record_route(RouteRecord(
        route_id="g24_recovery_antismuggle_route",
        script_id=SCRIPT_ID,
        name="Group 24 recovery target anti-smuggling route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "recovery targets are audit-only",
            "insertion form and coefficients are not selected by recovery",
            "support/smoothing/boundary data are not selected by recovery",
            "residual status is not selected by recovery",
            "parent equation remains closed",
        ],
    ))

    for branch_id in [
        "GR_metric_copy",
        "AB_product_fit",
        "B_inverse_A_fit",
        "gamma_like_fit",
        "areal_kappa_promotion",
        "recovery_selected_seam",
        "recovery_selected_residual_status",
        "parent_from_recovery_success",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_24",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; recovery diagnostics cannot construct metric insertion.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g24_recovery_audit_not_construction",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Schwarzschild, AB, B=1/A, gamma_like, PPN-like, areal-kappa, and boundary/support checks may audit B_s/F_zeta "
            "only after insertion data are structurally fixed. They may not choose coefficients, seam data, residual status, or parent closure."
        ),
        derivation_ids=[
            "recovery_anti_smuggling_load_24",
            "recovery_target_anti_smuggling_marker_24",
        ],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Recovery Target Anti-Smuggling Audit")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    diagnostics = build_diagnostics()
    targets = build_audit_targets()
    routes = build_smuggling_routes()
    conditions = build_conditions()

    case_0_problem_statement(out)
    case_1_diagnostics(diagnostics, out)
    case_2_audit_targets(targets, out)
    case_3_smuggling_routes(routes, out)
    case_4_conditions(conditions, out)
    case_5_failure_controls(out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, diagnostics)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
