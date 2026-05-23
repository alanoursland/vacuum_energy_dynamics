# Candidate metric insertion source compatibility
#
# Group:
#   24_metric_insertion_recovery_retest
#
# Script type:
#   REQUIREMENTS / DIAGNOSTIC
#
# Purpose
# -------
# Audit whether B_s/F_zeta insertion can preserve ordinary source
# no-double-counting.
#
# Locked-door question:
#
#   Can B_s/F_zeta insertion preserve ordinary source no-double-counting?
#
# This script does not derive B_s/F_zeta insertion.
# It does not derive source compatibility.
# It does not derive ordinary source routing from the parent theory.
# It does not prove boundary neutrality or scalar silence.
# It does not open the parent field equation.
#
# It records that metric insertion cannot duplicate A-sector source load or
# hide ordinary source load inside insertion coefficients, residuals,
# support/layer parameters, curvature/H/exchange/dark labels, or cancellation
# ledgers.

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
            "boundary_support_dep_24",
            "24_metric_insertion_recovery_retest__candidate_metric_insertion_boundary_support_compatibility",
            "metric_insertion_boundary_support_marker_24",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g21_source_dep_24",
            "21_source_routing_and_mass_neutrality__candidate_source_routing_no_double_counting",
            "source_routing_no_double_counting_marker_21",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g23_source_dep_24",
            "23_smooth_support_and_matching_laws__candidate_matching_law_source_compatibility",
            "matching_law_source_compatibility_marker_23",
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
class SourceCompatibilityLedger:
    rho_A: sp.Symbol
    rho_Bs_coeff: sp.Symbol
    rho_zeta_residual: sp.Symbol
    rho_kappa_residual: sp.Symbol
    rho_support_layer: sp.Symbol
    rho_curv: sp.Symbol
    rho_H: sp.Symbol
    rho_exch: sp.Symbol
    rho_dark: sp.Symbol
    rho_cancel: sp.Symbol
    duplicate_source_load: sp.Expr


@dataclass
class SourceCompatibilityCondition:
    name: str
    condition: str
    status: str
    failure_if: str
    consequence: str


@dataclass
class SourceCompatibilityBranch:
    name: str
    branch: str
    status: str
    allowed_if: str
    rejected_if: str


@dataclass
class RejectedSourceRoute:
    name: str
    route: str
    forbidden_use: str
    status: str
    consequence: str


# =============================================================================
# Builders
# =============================================================================


def build_ledger() -> SourceCompatibilityLedger:
    (
        rho_A,
        rho_Bs_coeff,
        rho_zeta_residual,
        rho_kappa_residual,
        rho_support_layer,
        rho_curv,
        rho_H,
        rho_exch,
        rho_dark,
        rho_cancel,
    ) = sp.symbols(
        "rho_A rho_Bs_coeff rho_zeta_residual rho_kappa_residual rho_support_layer rho_curv rho_H rho_exch rho_dark rho_cancel",
        real=True,
    )

    duplicate_source_load = sp.simplify(
        rho_Bs_coeff
        + rho_zeta_residual
        + rho_kappa_residual
        + rho_support_layer
        + rho_curv
        + rho_H
        + rho_exch
        + rho_dark
        + rho_cancel
    )

    return SourceCompatibilityLedger(
        rho_A=rho_A,
        rho_Bs_coeff=rho_Bs_coeff,
        rho_zeta_residual=rho_zeta_residual,
        rho_kappa_residual=rho_kappa_residual,
        rho_support_layer=rho_support_layer,
        rho_curv=rho_curv,
        rho_H=rho_H,
        rho_exch=rho_exch,
        rho_dark=rho_dark,
        rho_cancel=rho_cancel,
        duplicate_source_load=duplicate_source_load,
    )


def build_conditions() -> List[SourceCompatibilityCondition]:
    return [
        SourceCompatibilityCondition(
            name="S1: ordinary source remains A-routed",
            condition="rho/M_enc remains routed to A-sector mass charge",
            status="REQUIRED",
            failure_if="ordinary source is used to determine B_s/F_zeta insertion coefficient",
            consequence="A-sector source coin is duplicated",
        ),
        SourceCompatibilityCondition(
            name="S2: insertion coefficient not source reservoir",
            condition="rho_Bs_coeff = 0",
            status="REQUIRED",
            failure_if="B_s/F_zeta coefficient carries ordinary source load",
            consequence="metric insertion becomes hidden source channel",
        ),
        SourceCompatibilityCondition(
            name="S3: zeta residual not source channel",
            condition="rho_zeta_residual = 0",
            status="REQUIRED",
            failure_if="residual zeta becomes source reservoir after insertion",
            consequence="count-once and source no-double-counting fail together",
        ),
        SourceCompatibilityCondition(
            name="S4: kappa residual not source channel",
            condition="rho_kappa_residual = 0",
            status="REQUIRED",
            failure_if="kappa residual restores ordinary source load",
            consequence="diagnostic kappa becomes hidden source route",
        ),
        SourceCompatibilityCondition(
            name="S5: support/layer parameters not source-loaded",
            condition="rho_support_layer = 0",
            status="REQUIRED",
            failure_if="support radius, smoothing width, boundary data, or transition layer coefficient carries ordinary source load",
            consequence="Group 23 seam pockets return",
        ),
        SourceCompatibilityCondition(
            name="S6: no curvature/H/exchange/dark repair source",
            condition="rho_curv = rho_H = rho_exch = rho_dark = 0",
            status="REQUIRED",
            failure_if="repair labels absorb ordinary source load for metric insertion",
            consequence="repair exclusions are bypassed",
        ),
        SourceCompatibilityCondition(
            name="S7: no source cancellation ledger",
            condition="rho_cancel = 0 and duplicate loads vanish sector-by-sector",
            status="REQUIRED",
            failure_if="source loads cancel only in a total ledger",
            consequence="total cancellation is mistaken for source compatibility",
        ),
    ]


def build_branches() -> List[SourceCompatibilityBranch]:
    return [
        SourceCompatibilityBranch(
            name="B1: source-compatible insertion candidate",
            branch="B_s/F_zeta candidate with no duplicate source loads",
            status="THEOREM_TARGET",
            allowed_if="A-sector source remains protected and all duplicate loads vanish or are theorem-routed sector-by-sector",
            rejected_if="candidate claims insertion while source loads remain unhandled",
        ),
        SourceCompatibilityBranch(
            name="B2: diagnostic-only source audit",
            branch="candidate audited against source no-double-counting ledger without claiming theorem",
            status="SAFE_IF",
            allowed_if="used only to classify source risks and obligations",
            rejected_if="used to license metric insertion",
        ),
        SourceCompatibilityBranch(
            name="B3: source-loaded insertion coefficient",
            branch="ordinary rho/T hidden in B_s/F_zeta coefficient",
            status="REJECTED",
            allowed_if="never as metric insertion construction",
            rejected_if="used to fit recovery or boundary/support conditions",
        ),
        SourceCompatibilityBranch(
            name="B4: source-loaded seam",
            branch="ordinary rho/T hidden in support/layer/boundary parameter",
            status="REJECTED",
            allowed_if="never as matching/support construction",
            rejected_if="used to repair seam or recovery",
        ),
        SourceCompatibilityBranch(
            name="B5: source cancellation ledger",
            branch="duplicate source loads cancel only after summing",
            status="REJECTED",
            allowed_if="never as source compatibility",
            rejected_if="used instead of sector-by-sector zero",
        ),
    ]


def build_rejected_routes() -> List[RejectedSourceRoute]:
    return [
        RejectedSourceRoute(
            name="R1: source-loaded insertion coefficient",
            route="rho_to_Bs_Fzeta_coefficient",
            forbidden_use="ordinary rho/T determines or hides inside B_s/F_zeta coefficient",
            status="REJECTED",
            consequence="metric insertion duplicates A-sector source routing",
        ),
        RejectedSourceRoute(
            name="R2: zeta residual source channel",
            route="rho_to_zeta_residual",
            forbidden_use="ordinary rho/T survives in residual zeta after insertion",
            status="REJECTED",
            consequence="count-once and source compatibility both fail",
        ),
        RejectedSourceRoute(
            name="R3: kappa residual source channel",
            route="rho_to_kappa_residual",
            forbidden_use="ordinary rho/T survives in kappa residual or e_kappa label",
            status="REJECTED",
            consequence="diagnostic kappa becomes hidden source",
        ),
        RejectedSourceRoute(
            name="R4: source-loaded support/layer parameter",
            route="rho_to_support_layer_parameter",
            forbidden_use="ordinary rho/T hidden in support radius, smoothing width, transition layer, or boundary data",
            status="REJECTED",
            consequence="seam pockets return",
        ),
        RejectedSourceRoute(
            name="R5: repair-label source insertion",
            route="rho_to_curv_H_exch_dark_repair",
            forbidden_use="ordinary rho/T absorbed into curvature, H, exchange, or dark labels",
            status="REJECTED",
            consequence="repair labels become source reservoirs",
        ),
        RejectedSourceRoute(
            name="R6: source cancellation ledger",
            route="source_total_cancellation",
            forbidden_use="duplicate source loads cancel only in total",
            status="REJECTED",
            consequence="total cancellation is not source compatibility",
        ),
        RejectedSourceRoute(
            name="R7: parent source shortcut",
            route="parent_source_shortcut_from_insertion",
            forbidden_use="metric insertion source audit treated as parent source derivation",
            status="REJECTED",
            consequence="parent source law is smuggled",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Metric insertion source compatibility problem")
    print("Question:")
    print()
    print("  Can B_s/F_zeta insertion preserve ordinary source no-double-counting?")
    print()
    print("Reference discipline:")
    print()
    print("  Ordinary rho/M_enc remains A-routed.")
    print("  Metric insertion coefficients, residuals, seam parameters, and repair labels cannot carry duplicate ordinary source load.")
    print("  This script audits source compatibility burdens; it does not derive them.")

    with out.governance_assessments():
        out.line(
            "metric insertion source compatibility audit opened",
            StatusMark.INFO,
            "auditing B_s/F_zeta against ordinary source no-double-counting",
        )


def case_1_source_ledger(ledger: SourceCompatibilityLedger, out: ScriptOutput) -> None:
    header("Case 1: Metric insertion source duplicate-load ledger")
    print("Protected source route:")
    print()
    print(f"  rho_A = {sp.sstr(ledger.rho_A)}")
    print()
    print("Forbidden duplicate source loads:")
    print()
    print(f"  rho_Bs_coeff = {sp.sstr(ledger.rho_Bs_coeff)}")
    print(f"  rho_zeta_residual = {sp.sstr(ledger.rho_zeta_residual)}")
    print(f"  rho_kappa_residual = {sp.sstr(ledger.rho_kappa_residual)}")
    print(f"  rho_support_layer = {sp.sstr(ledger.rho_support_layer)}")
    print(f"  rho_curv = {sp.sstr(ledger.rho_curv)}")
    print(f"  rho_H = {sp.sstr(ledger.rho_H)}")
    print(f"  rho_exch = {sp.sstr(ledger.rho_exch)}")
    print(f"  rho_dark = {sp.sstr(ledger.rho_dark)}")
    print(f"  rho_cancel = {sp.sstr(ledger.rho_cancel)}")
    print()
    print("Duplicate source load:")
    print()
    print(f"  L_source_dup = {sp.sstr(ledger.duplicate_source_load)}")
    print()
    print("Metric insertion is not source-compatible while any duplicate load remains unproved, unneutralized, or not theorem-routed sector-by-sector.")

    with out.derived_results():
        out.line(
            "metric insertion source duplicate-load ledger stated",
            StatusMark.OBLIGATION,
            f"L_source_dup = {sp.sstr(ledger.duplicate_source_load)}",
        )


def case_2_conditions(conditions: List[SourceCompatibilityCondition], out: ScriptOutput) -> None:
    header("Case 2: Metric insertion source compatibility conditions")
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
            "metric insertion source compatibility conditions populated",
            StatusMark.OBLIGATION,
            f"{len(conditions)} source compatibility conditions remain required",
        )


def case_3_branches(branches: List[SourceCompatibilityBranch], out: ScriptOutput) -> None:
    header("Case 3: Source compatibility branches")
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
            "metric insertion source compatibility branches classified",
            StatusMark.PASS,
            f"{len(branches)} branches classified",
        )


def case_4_rejected_routes(routes: List[RejectedSourceRoute], out: ScriptOutput) -> None:
    header("Case 4: Rejected metric insertion source shortcuts")
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
            "metric insertion source shortcuts rejected",
            StatusMark.FAIL,
            "source-loaded coefficients, residuals, seam parameters, repair labels, cancellation ledgers, and parent source shortcuts remain rejected",
        )


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("The metric insertion source compatibility audit fails if a later script allows:")
    print()
    print("1. ordinary rho/T determines or hides in B_s/F_zeta coefficient")
    print("2. residual zeta becomes source channel after insertion")
    print("3. kappa residual or e_kappa becomes source channel")
    print("4. support radius, smoothing width, transition layer, or boundary data carries ordinary source load")
    print("5. curvature/H/exchange/dark labels absorb ordinary source load")
    print("6. duplicate source loads cancel only in total")
    print("7. source compatibility assumed from recovery success")
    print("8. source compatibility assumed from boundary/support audit")
    print("9. parent source law opened from metric insertion source audit alone")

    with out.governance_assessments():
        out.line(
            "metric insertion source compatibility failure controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not hide ordinary source load inside insertion routes",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Metric insertion source compatibility result:")
    print()
    print("  rho/M_enc remains A-routed.")
    print("  B_s/F_zeta coefficients cannot carry ordinary source load.")
    print("  zeta/kappa residuals cannot become source channels.")
    print("  support/layer/boundary parameters cannot become source reservoirs.")
    print("  curvature/H/exchange/dark labels cannot become repair source routes.")
    print("  cancellation ledgers are not source compatibility.")
    print()
    print("Metric insertion source compatibility remains theorem-targeted.")
    print()
    print("Possible next script:")
    print("  candidate_metric_insertion_theorem_obligations.py")
    print()
    print("Tiny goblin label:")
    print("  Source coin stays in A. No metric pocket.")

    with out.governance_assessments():
        out.line(
            "metric insertion source compatibility audit complete",
            StatusMark.PASS,
            "source no-double-counting guardrails imported; insertion theorem remains open",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, ledger: SourceCompatibilityLedger) -> None:
    ns.record_derivation(
        derivation_id="metric_insertion_source_duplicate_load_24",
        inputs=[
            ledger.rho_Bs_coeff,
            ledger.rho_zeta_residual,
            ledger.rho_kappa_residual,
            ledger.rho_support_layer,
            ledger.rho_curv,
            ledger.rho_H,
            ledger.rho_exch,
            ledger.rho_dark,
            ledger.rho_cancel,
        ],
        output=ledger.duplicate_source_load,
        method="sum representative forbidden duplicate source loads for metric insertion",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="metric_insertion_source_duplicate_load_ledger",
        scope="Group 24 metric insertion recovery retest",
    )

    ns.record_derivation(
        derivation_id="metric_insertion_source_compatibility_marker_24",
        inputs=[
            sp.Symbol("rho_A"),
            sp.Symbol("rho_Bs_coeff"),
            sp.Symbol("rho_zeta_residual"),
            sp.Symbol("rho_kappa_residual"),
            sp.Symbol("rho_support_layer"),
            sp.Symbol("rho_repair_labels"),
            sp.Symbol("rho_cancel"),
        ],
        output=sp.Symbol("metric_insertion_source_compatibility_conditions_stated"),
        method="Group 24 metric insertion source compatibility ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="requirements_marker",
        scope="Group 24 metric insertion recovery retest",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g24_derive_A_source_protected_in_insertion", "Derive A-sector source protection under insertion"),
        ("g24_derive_no_source_loaded_Bs_coeff", "Derive no source-loaded B_s/F_zeta coefficient"),
        ("g24_derive_no_zeta_source_residual", "Derive no zeta residual source channel"),
        ("g24_derive_no_kappa_source_residual", "Derive no kappa residual source channel"),
        ("g24_derive_no_source_loaded_seam", "Derive no source-loaded support/layer/boundary parameter"),
        ("g24_derive_no_repair_label_source_insertion", "Derive no repair-label source insertion"),
        ("g24_derive_no_source_cancellation_insertion", "Derive no source cancellation ledger for insertion"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g24_insertion_source_route"],
            description=(
                "Metric insertion source compatibility remains theorem-targeted until ordinary source no-double-counting is preserved "
                "across coefficients, residuals, support/layer parameters, repair labels, and cancellation ledgers."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g24_derive_A_source_protected_in_insertion",
        "g24_derive_no_source_loaded_Bs_coeff",
        "g24_derive_no_zeta_source_residual",
        "g24_derive_no_kappa_source_residual",
        "g24_derive_no_source_loaded_seam",
        "g24_derive_no_repair_label_source_insertion",
        "g24_derive_no_source_cancellation_insertion",
    ]

    ns.record_route(RouteRecord(
        route_id="g24_insertion_source_route",
        script_id=SCRIPT_ID,
        name="Group 24 metric insertion source compatibility route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "ordinary rho/M_enc remains A-routed",
            "B_s/F_zeta coefficient carries no ordinary source load",
            "zeta/kappa residuals carry no ordinary source load",
            "support/layer/boundary parameters carry no ordinary source load",
            "curvature/H/exchange/dark labels carry no ordinary source load",
            "no source cancellation ledger is used",
        ],
    ))

    for branch_id in [
        "source_loaded_Bs_coefficient",
        "zeta_residual_source_channel",
        "kappa_residual_source_channel",
        "source_loaded_support_layer_parameter",
        "repair_label_source_insertion",
        "source_cancellation_ledger",
        "parent_source_shortcut_from_insertion",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_24",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; metric insertion cannot duplicate ordinary source routing.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g24_insertion_preserves_source_no_double_counting",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "B_s/F_zeta metric insertion cannot be source-compatible unless ordinary rho/M_enc remains A-routed and no duplicate source load "
            "appears in insertion coefficients, zeta/kappa residuals, support/layer/boundary parameters, repair labels, or cancellation ledgers."
        ),
        derivation_ids=[
            "metric_insertion_source_duplicate_load_24",
            "metric_insertion_source_compatibility_marker_24",
        ],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Metric Insertion Source Compatibility")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    ledger = build_ledger()
    conditions = build_conditions()
    branches = build_branches()
    routes = build_rejected_routes()

    case_0_problem_statement(out)
    case_1_source_ledger(ledger, out)
    case_2_conditions(conditions, out)
    case_3_branches(branches, out)
    case_4_rejected_routes(routes, out)
    case_5_failure_controls(out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, ledger)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
