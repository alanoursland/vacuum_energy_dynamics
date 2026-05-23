# Candidate matching law source compatibility
#
# Group:
#   23_smooth_support_and_matching_laws
#
# Script type:
#   REQUIREMENTS / DIAGNOSTIC
#
# Purpose
# -------
# Audit whether matching/support/layer laws can coexist with ordinary source
# routing and no-double-counting.
#
# Locked-door question:
#
#   Can matching conditions coexist with ordinary source routing and no-double-counting?
#
# This script does not derive source compatibility.
# It does not prove compact support.
# It does not prove no-shell matching.
# It does not prove boundary neutrality or scalar silence.
#
# It records that matching/support/layer laws must not reroute ordinary matter
# into boundary shells, scalar tails, non-A current flux, curvature rescue,
# H counterterms, exchange repair, dark patches, or support/layer parameters.

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
        "DIAGNOSTIC_ONLY": StatusMark.INFO,
        "FORBIDDEN": StatusMark.FAIL,
        "PROVISIONAL": StatusMark.INFO,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "RISK": StatusMark.WARN,
        "SAFE_IF": StatusMark.INFO,
        "THEOREM_TARGET": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "compact_support_dep_23",
            "023_smooth_support_and_matching_laws__candidate_compact_support_admissibility_conditions",
            "compact_support_admissibility_marker_23",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "transition_layer_dep_23",
            "023_smooth_support_and_matching_laws__candidate_transition_layer_mass_flux_audit",
            "transition_layer_mass_flux_marker_23",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "parameter_independence_dep_23",
            "023_smooth_support_and_matching_laws__candidate_boundary_parameter_independence",
            "boundary_parameter_independence_marker_23",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g21_source_dep_23",
            "021_source_routing_and_mass_neutrality__candidate_source_routing_no_double_counting",
            "source_routing_no_double_counting_marker_21",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g22_repair_dep_23",
            "022_boundary_neutrality_and_scalar_silence__candidate_boundary_repair_route_exclusion",
            "boundary_repair_route_exclusion_inventory_marker_22",
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
    rho_shell: sp.Symbol
    rho_scalar: sp.Symbol
    rho_current: sp.Symbol
    rho_curv: sp.Symbol
    rho_H: sp.Symbol
    rho_exch: sp.Symbol
    rho_dark: sp.Symbol
    rho_layer_param: sp.Symbol
    duplicate_source_load: sp.Expr
    protected_A_load: sp.Expr


@dataclass
class SourceCompatibilityCondition:
    name: str
    condition: str
    status: str
    failure_if: str
    consequence: str


@dataclass
class SourceRoutingBranch:
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
    rho_A, rho_shell, rho_scalar, rho_current, rho_curv, rho_H, rho_exch, rho_dark, rho_layer_param = sp.symbols(
        "rho_A rho_shell rho_scalar rho_current rho_curv rho_H rho_exch rho_dark rho_layer_param",
        real=True,
    )

    duplicate_source_load = sp.simplify(
        rho_shell
        + rho_scalar
        + rho_current
        + rho_curv
        + rho_H
        + rho_exch
        + rho_dark
        + rho_layer_param
    )

    return SourceCompatibilityLedger(
        rho_A=rho_A,
        rho_shell=rho_shell,
        rho_scalar=rho_scalar,
        rho_current=rho_current,
        rho_curv=rho_curv,
        rho_H=rho_H,
        rho_exch=rho_exch,
        rho_dark=rho_dark,
        rho_layer_param=rho_layer_param,
        duplicate_source_load=duplicate_source_load,
        protected_A_load=rho_A,
    )


def build_conditions() -> List[SourceCompatibilityCondition]:
    return [
        SourceCompatibilityCondition(
            name="S1: ordinary source remains A-routed",
            condition="rho/M_enc remains routed to A-sector mass charge",
            status="REQUIRED",
            failure_if="ordinary matter is rerouted into boundary/support/layer repair",
            consequence="A-sector mass coin remains protected",
        ),
        SourceCompatibilityCondition(
            name="S2: no boundary shell source from ordinary matter",
            condition="rho_shell = 0 for duplicate support/boundary shell load",
            status="REQUIRED",
            failure_if="matching/support law creates shell source from ordinary rho/T",
            consequence="no-shell matching must preserve source routing",
        ),
        SourceCompatibilityCondition(
            name="S3: no residual scalar source reroute",
            condition="rho_scalar = 0 for duplicate scalar-tail support source",
            status="REQUIRED",
            failure_if="ordinary matter creates C/r residual tail through matching law",
            consequence="scalar silence cannot be source-rerouted",
        ),
        SourceCompatibilityCondition(
            name="S4: no non-A current repair source",
            condition="rho_current = 0 for duplicate current-flux load",
            status="REQUIRED",
            failure_if="ordinary matter is routed into I/(4*pi*r^2) repair current",
            consequence="current flux silence remains protected",
        ),
        SourceCompatibilityCondition(
            name="S5: no curvature/H/exchange/dark repair source",
            condition="rho_curv = rho_H = rho_exch = rho_dark = 0 for duplicate ordinary load",
            status="REQUIRED",
            failure_if="ordinary matter is absorbed into curvature, H, exchange, or dark boundary patch",
            consequence="repair routes remain rejected",
        ),
        SourceCompatibilityCondition(
            name="S6: no support/layer parameter source load",
            condition="rho_layer_param = 0 for ordinary source hidden in support/layer parameter",
            status="REQUIRED",
            failure_if="support radius, smoothing width, or layer coefficient carries ordinary source load by tuning",
            consequence="parameter independence and source no-double-counting remain tied",
        ),
        SourceCompatibilityCondition(
            name="S7: no cancellation ledger",
            condition="duplicate_source_load must vanish sector-by-sector, not only in total",
            status="REQUIRED",
            failure_if="non-A source pockets cancel only after summing",
            consequence="total cancellation is not source compatibility",
        ),
    ]


def build_branches() -> List[SourceRoutingBranch]:
    return [
        SourceRoutingBranch(
            name="B1: protected A-sector routing",
            branch="ordinary rho/M_enc -> A-sector mass charge",
            status="SAFE_IF",
            allowed_if="used as the protected reduced ordinary source route",
            rejected_if="duplicated into non-A repair channels",
        ),
        SourceRoutingBranch(
            name="B2: boundary shell from source",
            branch="ordinary source creates boundary shell support load",
            status="REJECTED",
            allowed_if="never as silent matching law",
            rejected_if="used to satisfy support/no-shell conditions",
        ),
        SourceRoutingBranch(
            name="B3: scalar/current repair source",
            branch="ordinary source routed into scalar tail or current flux cancellation",
            status="REJECTED",
            allowed_if="never as boundary/scalar silence",
            rejected_if="used to cancel C_i or I_i coefficients",
        ),
        SourceRoutingBranch(
            name="B4: structural source-compatible matching law",
            branch="matching/support law preserves A routing and has zero duplicate loads",
            status="THEOREM_TARGET",
            allowed_if="all source compatibility conditions are derived",
            rejected_if="any support/layer/source coefficient is chosen after leakage appears",
        ),
    ]


def build_rejected_routes() -> List[RejectedSourceRoute]:
    return [
        RejectedSourceRoute(
            name="R1: ordinary source to boundary shell",
            route="rho_to_boundary_shell",
            forbidden_use="ordinary rho/T supplies shell or support seam source",
            status="REJECTED",
            consequence="no-shell behavior cannot be sourced by ordinary matter reroute",
        ),
        RejectedSourceRoute(
            name="R2: ordinary source to scalar tail",
            route="rho_to_scalar_tail",
            forbidden_use="ordinary rho/T supplies residual C/r scalar tail",
            status="REJECTED",
            consequence="scalar silence cannot be patched by source reroute",
        ),
        RejectedSourceRoute(
            name="R3: ordinary source to current flux",
            route="rho_to_current_flux",
            forbidden_use="ordinary rho/T supplies non-A I/(4*pi*r^2) current flux",
            status="REJECTED",
            consequence="current flux cannot be source repair",
        ),
        RejectedSourceRoute(
            name="R4: ordinary source to curvature/H/exchange/dark",
            route="rho_to_repair_labels",
            forbidden_use="ordinary rho/T absorbed into curvature, H, exchange, or dark repair labels",
            status="REJECTED",
            consequence="repair labels cannot carry duplicate ordinary source load",
        ),
        RejectedSourceRoute(
            name="R5: source-loaded support parameter",
            route="source_loaded_support_parameter",
            forbidden_use="ordinary source hidden in support radius, smoothing width, or layer coefficient",
            status="REJECTED",
            consequence="support parameters must not become source reservoirs",
        ),
        RejectedSourceRoute(
            name="R6: source cancellation ledger",
            route="source_cancellation_ledger",
            forbidden_use="non-A source loads cancel only after summing",
            status="REJECTED",
            consequence="cancellation is not source compatibility",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Matching law source compatibility problem")
    print("Question:")
    print()
    print("  Can matching conditions coexist with ordinary source routing and no-double-counting?")
    print()
    print("Reference discipline:")
    print()
    print("  Group 21 protected ordinary rho/M_enc -> A-sector mass charge.")
    print("  Groups 22-23 reject boundary/scalar/current/support repair routes.")
    print("  This script checks that matching/support/layer laws do not duplicate ordinary source load.")
    print("  It does not derive source compatibility.")

    with out.governance_assessments():
        out.line(
            "matching law source compatibility audit opened",
            StatusMark.INFO,
            "auditing whether matching/support/layer laws preserve ordinary source no-double-counting",
        )


def case_1_source_ledger(ledger: SourceCompatibilityLedger, out: ScriptOutput) -> None:
    header("Case 1: Source compatibility ledger")
    print("Protected ordinary source route:")
    print()
    print(f"  rho_A = {sp.sstr(ledger.protected_A_load)}")
    print()
    print("Forbidden duplicate source loads:")
    print()
    print(f"  rho_shell = {sp.sstr(ledger.rho_shell)}")
    print(f"  rho_scalar = {sp.sstr(ledger.rho_scalar)}")
    print(f"  rho_current = {sp.sstr(ledger.rho_current)}")
    print(f"  rho_curv = {sp.sstr(ledger.rho_curv)}")
    print(f"  rho_H = {sp.sstr(ledger.rho_H)}")
    print(f"  rho_exch = {sp.sstr(ledger.rho_exch)}")
    print(f"  rho_dark = {sp.sstr(ledger.rho_dark)}")
    print(f"  rho_layer_param = {sp.sstr(ledger.rho_layer_param)}")
    print()
    print("Duplicate source load ledger:")
    print()
    print(f"  duplicate_source_load = {sp.sstr(ledger.duplicate_source_load)}")
    print()
    print("Source compatibility requires these duplicate loads to vanish sector-by-sector.")

    with out.derived_results():
        out.line(
            "source compatibility duplicate-load ledger stated",
            StatusMark.PASS,
            f"duplicate load = {sp.sstr(ledger.duplicate_source_load)}",
        )


def case_2_condition_ledger(conditions: List[SourceCompatibilityCondition], out: ScriptOutput) -> None:
    header("Case 2: Source compatibility condition ledger")
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
            "source compatibility conditions populated",
            StatusMark.OBLIGATION,
            f"{len(conditions)} source compatibility conditions remain required",
        )


def case_3_branch_ledger(branches: List[SourceRoutingBranch], out: ScriptOutput) -> None:
    header("Case 3: Source-routing branch ledger")
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
            "source-routing branch ledger populated",
            StatusMark.PASS,
            f"{len(branches)} source-routing branches classified",
        )


def case_4_rejected_routes(routes: List[RejectedSourceRoute], out: ScriptOutput) -> None:
    header("Case 4: Rejected source-rerouting routes")
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
            "source-rerouting routes rejected",
            StatusMark.FAIL,
            "boundary shell, scalar tail, current flux, repair labels, support parameters, and cancellation ledgers remain rejected",
        )


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("The matching law source compatibility audit fails if a later script allows:")
    print()
    print("1. ordinary rho/T rerouted into boundary shell")
    print("2. ordinary rho/T rerouted into scalar tail")
    print("3. ordinary rho/T rerouted into non-A current flux")
    print("4. ordinary rho/T rerouted into curvature/H/exchange/dark repair")
    print("5. ordinary rho/T hidden in support radius, smoothing width, or layer coefficient")
    print("6. source cancellation ledger to replace sector-by-sector zero")
    print("7. matching law to duplicate A-sector source load")
    print("8. boundary/source compatibility to be assumed instead of derived")
    print("9. parent equation opened from source compatibility diagnostics alone")

    with out.governance_assessments():
        out.line(
            "source compatibility overclaim controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not let matching/support/layer laws duplicate ordinary source routing",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Matching/support/layer laws are source-compatible only if:")
    print()
    print("  rho/M_enc remains routed to A-sector mass charge")
    print("  rho_shell = 0")
    print("  rho_scalar = 0")
    print("  rho_current = 0")
    print("  rho_curv = rho_H = rho_exch = rho_dark = 0")
    print("  rho_layer_param = 0")
    print("  no cancellation ledger replaces sector-by-sector zero")
    print()
    print("This script does not derive source compatibility.")
    print("It records the source no-double-counting burden for matching/support/layer laws.")
    print()
    print("Possible next script:")
    print("  candidate_matching_law_theorem_obligations.py")
    print()
    print("Tiny goblin label:")
    print("  The source coin stays in A. No seam pockets.")

    with out.governance_assessments():
        out.line(
            "matching law source compatibility audit complete",
            StatusMark.PASS,
            "matching/support/layer laws must preserve ordinary source no-double-counting",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, ledger: SourceCompatibilityLedger) -> None:
    ns.record_derivation(
        derivation_id="matching_source_duplicate_load_ledger_23",
        inputs=[
            ledger.rho_shell,
            ledger.rho_scalar,
            ledger.rho_current,
            ledger.rho_curv,
            ledger.rho_H,
            ledger.rho_exch,
            ledger.rho_dark,
            ledger.rho_layer_param,
        ],
        output=ledger.duplicate_source_load,
        method="sum representative forbidden duplicate ordinary source loads",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="source_duplicate_load_ledger",
        scope="Group 23 matching law source compatibility",
    )

    ns.record_derivation(
        derivation_id="matching_law_source_compatibility_marker_23",
        inputs=[
            sp.Symbol("rho_A"),
            sp.Symbol("rho_shell"),
            sp.Symbol("rho_scalar"),
            sp.Symbol("rho_current"),
            sp.Symbol("rho_repair"),
            sp.Symbol("rho_layer_param"),
        ],
        output=sp.Symbol("matching_law_source_compatibility_conditions_stated"),
        method="Group 23 matching law source compatibility ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="requirements_marker",
        scope="Group 23 smooth support and matching laws",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g23_derive_A_source_preservation", "Derive A-sector source preservation"),
        ("g23_derive_no_boundary_shell_source", "Derive no boundary shell source"),
        ("g23_derive_no_scalar_source_reroute", "Derive no scalar source reroute"),
        ("g23_derive_no_current_source_reroute", "Derive no current source reroute"),
        ("g23_derive_no_repair_label_source", "Derive no repair-label source reroute"),
        ("g23_derive_no_source_loaded_parameters", "Derive no source-loaded support/layer parameters"),
        ("g23_derive_no_source_cancellation_ledger", "Derive no source cancellation ledger"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g23_source_compat_route"],
            description=(
                "Matching/support/layer laws remain source-compatible only if ordinary rho/M_enc remains A-routed "
                "and no duplicate boundary, scalar, current, repair-label, dark, or parameter source load is created."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g23_derive_A_source_preservation",
        "g23_derive_no_boundary_shell_source",
        "g23_derive_no_scalar_source_reroute",
        "g23_derive_no_current_source_reroute",
        "g23_derive_no_repair_label_source",
        "g23_derive_no_source_loaded_parameters",
        "g23_derive_no_source_cancellation_ledger",
    ]

    ns.record_route(RouteRecord(
        route_id="g23_source_compat_route",
        script_id=SCRIPT_ID,
        name="Group 23 matching law source compatibility theorem target",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "ordinary rho/M_enc remains A-routed",
            "boundary shell source load vanishes",
            "scalar tail source load vanishes",
            "non-A current source load vanishes",
            "curvature/H/exchange/dark repair-label source loads vanish",
            "support/layer parameters carry no ordinary source load",
            "no source cancellation ledger is used",
        ],
    ))

    for branch_id in [
        "rho_to_boundary_shell",
        "rho_to_scalar_tail",
        "rho_to_current_flux",
        "rho_to_repair_labels",
        "source_loaded_support_parameter",
        "source_cancellation_ledger",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_23",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; matching/support/layer laws must not duplicate ordinary source routing.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g23_matching_support_preserve_source_routing",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Matching/support/layer laws must preserve ordinary source no-double-counting: rho/M_enc remains A-routed, "
            "and no boundary shell, scalar tail, current flux, repair label, dark label, or support/layer parameter may carry duplicate ordinary source load."
        ),
        derivation_ids=[
            "matching_source_duplicate_load_ledger_23",
            "matching_law_source_compatibility_marker_23",
        ],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Matching Law Source Compatibility")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    ledger = build_ledger()
    conditions = build_conditions()
    branches = build_branches()
    routes = build_rejected_routes()

    case_0_problem_statement(out)
    case_1_source_ledger(ledger, out)
    case_2_condition_ledger(conditions, out)
    case_3_branch_ledger(branches, out)
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
