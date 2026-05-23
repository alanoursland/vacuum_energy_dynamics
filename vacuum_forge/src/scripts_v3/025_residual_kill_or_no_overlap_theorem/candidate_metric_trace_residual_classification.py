# Candidate metric trace residual classification
#
# Group:
#   25_residual_kill_or_no_overlap_theorem
#
# Script type:
#   REQUIREMENTS / DIAGNOSTIC
#
# Purpose
# -------
# Classify possible residual statuses for zeta/kappa trace after B_s/F_zeta
# insertion.
#
# Locked-door question:
#
#   What statuses can residual zeta/kappa trace honestly have?
#
# This script does not derive residual kill.
# It does not derive non-metric inertness.
# It does not derive active no-overlap O.
# It does not derive B_s/F_zeta insertion.
# It does not open parent equation closure.
#
# It classifies safe-if / theorem-targeted statuses versus unsafe reentry routes.

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
        "UNSAFE": StatusMark.FAIL,
        "UNRESOLVED": StatusMark.OBLIGATION,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "residual_problem_dep_25",
            "025_residual_kill_or_no_overlap_theorem__candidate_residual_kill_problem_ledger",
            "residual_kill_problem_ledger_marker_25",
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
class ResidualStatusClass:
    name: str
    status_class: str
    classification: str
    allowed_if: str
    rejected_if: str
    consequence: str


@dataclass
class ResidualClassificationLedger:
    killed: sp.Symbol
    nonmetric: sp.Symbol
    diagnostic_only: sp.Symbol
    inert_bookkeeping: sp.Symbol
    projected_by_O: sp.Symbol
    metric_reentry: sp.Symbol
    source_reentry: sp.Symbol
    recovery_selected: sp.Symbol
    boundary_support_reentry: sp.Symbol
    safe_status_load: sp.Expr
    unsafe_status_load: sp.Expr


@dataclass
class ClassificationRule:
    name: str
    rule: str
    status: str
    failure_if: str


@dataclass
class RejectedStatusRoute:
    name: str
    route: str
    forbidden_use: str
    status: str
    consequence: str


# =============================================================================
# Builders
# =============================================================================


def build_classification_ledger() -> ResidualClassificationLedger:
    (
        killed,
        nonmetric,
        diagnostic_only,
        inert_bookkeeping,
        projected_by_O,
        metric_reentry,
        source_reentry,
        recovery_selected,
        boundary_support_reentry,
    ) = sp.symbols(
        "killed nonmetric diagnostic_only inert_bookkeeping projected_by_O metric_reentry source_reentry recovery_selected boundary_support_reentry",
        real=True,
    )

    safe_status_load = sp.simplify(killed + nonmetric + diagnostic_only + inert_bookkeeping + projected_by_O)
    unsafe_status_load = sp.simplify(metric_reentry + source_reentry + recovery_selected + boundary_support_reentry)

    return ResidualClassificationLedger(
        killed=killed,
        nonmetric=nonmetric,
        diagnostic_only=diagnostic_only,
        inert_bookkeeping=inert_bookkeeping,
        projected_by_O=projected_by_O,
        metric_reentry=metric_reentry,
        source_reentry=source_reentry,
        recovery_selected=recovery_selected,
        boundary_support_reentry=boundary_support_reentry,
        safe_status_load=safe_status_load,
        unsafe_status_load=unsafe_status_load,
    )


def build_status_classes() -> List[ResidualStatusClass]:
    return [
        ResidualStatusClass(
            name="S1: killed residual",
            status_class="killed",
            classification="THEOREM_TARGET",
            allowed_if="structural residual-kill law is derived before recovery and preserves all guardrails",
            rejected_if="residual is set to zero by declaration",
            consequence="potentially safe only if derived",
        ),
        ResidualStatusClass(
            name="S2: strictly non-metric residual",
            status_class="nonmetric",
            classification="THEOREM_TARGET",
            allowed_if="no metric, source, boundary, support, recovery, repair, or parent reentry is proven",
            rejected_if="nonmetric means merely ignored",
            consequence="potentially safe only with no-reentry theorem",
        ),
        ResidualStatusClass(
            name="S3: diagnostic-only residual",
            status_class="diagnostic_only",
            classification="SAFE_IF",
            allowed_if="diagnostic residual has no metric/source/boundary/support/recovery role and cannot re-enter",
            rejected_if="diagnostic later becomes construction, source, or recovery parameter",
            consequence="safe only as inert audit label",
        ),
        ResidualStatusClass(
            name="S4: inert bookkeeping residual",
            status_class="inert_bookkeeping",
            classification="THEOREM_TARGET",
            allowed_if="bookkeeping variable is proven non-dynamical, non-sourcing, non-boundary, and non-reentering",
            rejected_if="bookkeeping label carries hidden trace/source/load",
            consequence="requires explicit inertness conditions",
        ),
        ResidualStatusClass(
            name="S5: active no-overlap projected residual",
            status_class="projected_by_O",
            classification="THEOREM_TARGET",
            allowed_if="O has derived domain, kernel, image, idempotence, divergence, boundary, source, mass, and scalar-tail behavior",
            rejected_if="O is invoked as eraser by name",
            consequence="active O remains unavailable until derived",
        ),
        ResidualStatusClass(
            name="S6: unsafe metric reentry",
            status_class="metric_reentry",
            classification="REJECTED",
            allowed_if="never for count-once metric insertion",
            rejected_if="residual zeta/kappa enters ordinary metric trace after B_s insertion",
            consequence="scalar spatial trace is double-counted",
        ),
        ResidualStatusClass(
            name="S7: unsafe source reentry",
            status_class="source_reentry",
            classification="REJECTED",
            allowed_if="never for ordinary source no-double-counting",
            rejected_if="residual becomes source channel or source-loaded parameter",
            consequence="ordinary source routing is duplicated",
        ),
        ResidualStatusClass(
            name="S8: unsafe recovery-selected silence",
            status_class="recovery_selected",
            classification="REJECTED",
            allowed_if="never",
            rejected_if="residual status is chosen from Schwarzschild, gamma, AB, B=1/A, PPN, or parent-fit recovery",
            consequence="recovery constructs residual control",
        ),
        ResidualStatusClass(
            name="S9: unsafe boundary/support reentry",
            status_class="boundary_support_reentry",
            classification="REJECTED",
            allowed_if="never as residual control",
            rejected_if="residual re-enters through scalar tail, current flux, shell, support, smoothing, or transition layer",
            consequence="residual cleanup becomes boundary/support repair",
        ),
    ]


def build_rules() -> List[ClassificationRule]:
    return [
        ClassificationRule(
            name="R1: safe status requires derivation",
            rule="killed, nonmetric, inert, or projected status is not safe by declaration",
            status="REQUIRED",
            failure_if="a safe label is assigned without a theorem burden",
        ),
        ClassificationRule(
            name="R2: diagnostic-only means no reentry",
            rule="diagnostic residuals must have no metric, source, boundary, support, recovery, repair, or parent role",
            status="REQUIRED",
            failure_if="diagnostic residual later becomes construction data",
        ),
        ClassificationRule(
            name="R3: projected means real O",
            rule="active no-overlap projected status requires actual O structure",
            status="REQUIRED",
            failure_if="O erases overlap by name",
        ),
        ClassificationRule(
            name="R4: unsafe statuses rejected sector-by-sector",
            rule="metric, source, recovery, and boundary/support reentry routes are rejected sector-by-sector",
            status="REQUIRED",
            failure_if="unsafe residual loads cancel only in total",
        ),
        ClassificationRule(
            name="R5: classification does not license insertion",
            rule="residual classification does not by itself prove B_s/F_zeta insertion",
            status="REQUIRED",
            failure_if="classification audit opens insertion or parent gate",
        ),
    ]


def build_rejected_routes() -> List[RejectedStatusRoute]:
    return [
        RejectedStatusRoute(
            name="U1: metric reentry",
            route="residual_metric_reentry",
            forbidden_use="residual zeta/kappa enters ordinary metric trace after B_s insertion",
            status="REJECTED",
            consequence="count-once trace fails",
        ),
        RejectedStatusRoute(
            name="U2: source reentry",
            route="residual_source_reentry",
            forbidden_use="residual becomes ordinary source channel, source reservoir, or source-loaded seam parameter",
            status="REJECTED",
            consequence="source no-double-counting fails",
        ),
        RejectedStatusRoute(
            name="U3: recovery-selected silence",
            route="recovery_selected_residual_silence",
            forbidden_use="residual status chosen to pass Schwarzschild/gamma/AB/B=1/A/PPN/parent-fit checks",
            status="REJECTED",
            consequence="recovery constructs residual control",
        ),
        RejectedStatusRoute(
            name="U4: boundary scalar reentry",
            route="residual_boundary_scalar_reentry",
            forbidden_use="residual re-enters as scalar tail, boundary flux, current flux, A-tail, or shell/source load",
            status="REJECTED",
            consequence="boundary/scalar silence is bypassed",
        ),
        RejectedStatusRoute(
            name="U5: support/layer reentry",
            route="residual_support_layer_reentry",
            forbidden_use="residual hides in support radius, smoothing width, transition layer, or matching condition",
            status="REJECTED",
            consequence="smooth-support/matching guardrails are bypassed",
        ),
        RejectedStatusRoute(
            name="U6: repair-label reentry",
            route="residual_repair_label_reentry",
            forbidden_use="residual re-enters through O/H/dark/exchange/curvature/current labels",
            status="REJECTED",
            consequence="repair object supplies missing residual law",
        ),
        RejectedStatusRoute(
            name="U7: parent-placeholder reentry",
            route="residual_parent_placeholder_reentry",
            forbidden_use="residual status used to open parent equation or fill parent identity",
            status="REJECTED",
            consequence="parent closure is smuggled",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Metric trace residual classification problem")
    print("Question:")
    print()
    print("  What statuses can residual zeta/kappa trace honestly have?")
    print()
    print("Reference discipline:")
    print()
    print("  Killed, non-metric, inert, diagnostic-only, and projected statuses are not automatic.")
    print("  They require theorem support or strict no-reentry controls.")
    print("  Unsafe metric/source/recovery/boundary/support reentry routes are rejected.")

    with out.governance_assessments():
        out.line(
            "metric trace residual classification opened",
            StatusMark.INFO,
            "classifying residual statuses without deriving residual kill or no-overlap",
        )


def case_1_classification_ledger(ledger: ResidualClassificationLedger, out: ScriptOutput) -> None:
    header("Case 1: Residual status classification ledger")
    print("Potentially safe status labels:")
    print()
    print(f"  killed = {sp.sstr(ledger.killed)}")
    print(f"  nonmetric = {sp.sstr(ledger.nonmetric)}")
    print(f"  diagnostic_only = {sp.sstr(ledger.diagnostic_only)}")
    print(f"  inert_bookkeeping = {sp.sstr(ledger.inert_bookkeeping)}")
    print(f"  projected_by_O = {sp.sstr(ledger.projected_by_O)}")
    print()
    print("Unsafe status labels:")
    print()
    print(f"  metric_reentry = {sp.sstr(ledger.metric_reentry)}")
    print(f"  source_reentry = {sp.sstr(ledger.source_reentry)}")
    print(f"  recovery_selected = {sp.sstr(ledger.recovery_selected)}")
    print(f"  boundary_support_reentry = {sp.sstr(ledger.boundary_support_reentry)}")
    print()
    print("Safe-status burden:")
    print()
    print(f"  safe_status_load = {sp.sstr(ledger.safe_status_load)}")
    print()
    print("Unsafe-status burden:")
    print()
    print(f"  unsafe_status_load = {sp.sstr(ledger.unsafe_status_load)}")
    print()
    print("Interpretation:")
    print()
    print("  Safe labels are only labels unless their conditions are derived.")
    print("  Unsafe labels are rejected as residual-control statuses.")

    with out.derived_results():
        out.line(
            "residual safe-status ledger stated",
            StatusMark.OBLIGATION,
            f"safe_status_load = {sp.sstr(ledger.safe_status_load)}",
        )
        out.line(
            "residual unsafe-status ledger stated",
            StatusMark.FAIL,
            f"unsafe_status_load = {sp.sstr(ledger.unsafe_status_load)}",
        )


def case_2_status_classes(classes: List[ResidualStatusClass], out: ScriptOutput) -> None:
    header("Case 2: Residual status classes")
    for cls in classes:
        print()
        print("-" * 120)
        print(cls.name)
        print("-" * 120)
        print(f"Status class: {cls.status_class}")
        print(f"[{status_mark(cls.classification).value}] {cls.name}: {cls.classification}")
        print(f"Allowed if: {cls.allowed_if}")
        print(f"Rejected if: {cls.rejected_if}")
        print(f"Consequence: {cls.consequence}")

    with out.governance_assessments():
        out.line(
            "residual status classes populated",
            StatusMark.PASS,
            f"{len(classes)} residual statuses classified",
        )


def case_3_rules(rules: List[ClassificationRule], out: ScriptOutput) -> None:
    header("Case 3: Residual classification rules")
    for rule in rules:
        print()
        print("-" * 120)
        print(rule.name)
        print("-" * 120)
        print(f"Rule: {rule.rule}")
        print(f"[{status_mark(rule.status).value}] {rule.name}: {rule.status}")
        print(f"Failure if: {rule.failure_if}")

    with out.unresolved_obligations():
        out.line(
            "residual classification rules populated",
            StatusMark.OBLIGATION,
            f"{len(rules)} classification rules constrain residual statuses",
        )


def case_4_rejected_routes(routes: List[RejectedStatusRoute], out: ScriptOutput) -> None:
    header("Case 4: Rejected residual status routes")
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
            "unsafe residual status routes rejected",
            StatusMark.FAIL,
            "metric, source, recovery, boundary/support, repair-label, and parent-placeholder reentry remain rejected",
        )


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("The residual classification audit fails if a later script allows:")
    print()
    print("1. killed status assigned without structural kill law")
    print("2. non-metric status assigned without no-reentry theorem")
    print("3. diagnostic-only status later used as construction data")
    print("4. inert bookkeeping label carries hidden trace/source/load")
    print("5. O-projected status without real O structure")
    print("6. residual metric reentry after B_s insertion")
    print("7. residual source reentry")
    print("8. residual status selected by recovery")
    print("9. residual reentry through boundary/support/layer language")
    print("10. residual reentry through repair labels")
    print("11. parent equation opened from classification ledger")

    with out.governance_assessments():
        out.line(
            "residual classification failure controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not turn labels into solved residual control",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Residual classification result:")
    print()
    print("  Killed, non-metric, diagnostic-only, inert, and O-projected statuses are potentially safe only with their own theorem burden.")
    print("  Metric reentry, source reentry, recovery-selected silence, and boundary/support reentry are rejected.")
    print("  Classification does not derive residual kill, active O, B_s/F_zeta insertion, or parent closure.")
    print()
    print("Possible next script:")
    print("  candidate_nonmetric_inertness_conditions.py")
    print()
    print("Tiny goblin label:")
    print("  A label is not a lock.")

    with out.governance_assessments():
        out.line(
            "metric trace residual classification complete",
            StatusMark.PASS,
            "residual statuses classified; theorem burden remains open",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, ledger: ResidualClassificationLedger) -> None:
    ns.record_derivation(
        derivation_id="metric_trace_residual_classification_ledger_25",
        inputs=[
            ledger.killed,
            ledger.nonmetric,
            ledger.diagnostic_only,
            ledger.inert_bookkeeping,
            ledger.projected_by_O,
            ledger.metric_reentry,
            ledger.source_reentry,
            ledger.recovery_selected,
            ledger.boundary_support_reentry,
        ],
        output=sp.Tuple(ledger.safe_status_load, ledger.unsafe_status_load),
        method="classify possible residual statuses into safe-if/theorem-targeted and rejected reentry categories",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="residual_status_classification",
        scope="Group 25 residual kill or no-overlap theorem",
    )

    ns.record_derivation(
        derivation_id="metric_trace_residual_classification_marker_25",
        inputs=[
            sp.Symbol("killed"),
            sp.Symbol("nonmetric"),
            sp.Symbol("diagnostic_only"),
            sp.Symbol("inert_bookkeeping"),
            sp.Symbol("projected_by_O"),
            sp.Symbol("unsafe_reentry"),
        ],
        output=sp.Symbol("metric_trace_residual_classification_stated"),
        method="Group 25 metric trace residual classification ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="requirements_marker",
        scope="Group 25 residual kill or no-overlap theorem",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g25_derive_killed_status", "Derive killed residual status if used"),
        ("g25_derive_nonmetric_status", "Derive non-metric residual status if used"),
        ("g25_derive_diagnostic_no_reentry", "Derive diagnostic-only no-reentry"),
        ("g25_derive_inert_bookkeeping", "Derive inert bookkeeping status"),
        ("g25_derive_projected_by_O_status", "Derive projected-by-O status if used"),
        ("g25_reject_unsafe_reentry_statuses", "Reject unsafe residual reentry statuses"),
        ("g25_keep_insertion_parent_closed", "Keep insertion and parent gates closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g25_residual_classification_route"],
            description=(
                "Residual status classification remains theorem-targeted until killed, nonmetric, diagnostic-only, inert, or O-projected "
                "status is derived with no reentry. Unsafe statuses remain rejected."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g25_derive_killed_status",
        "g25_derive_nonmetric_status",
        "g25_derive_diagnostic_no_reentry",
        "g25_derive_inert_bookkeeping",
        "g25_derive_projected_by_O_status",
        "g25_reject_unsafe_reentry_statuses",
        "g25_keep_insertion_parent_closed",
    ]

    ns.record_route(RouteRecord(
        route_id="g25_residual_classification_route",
        script_id=SCRIPT_ID,
        name="Group 25 residual status classification route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "safe residual status labels carry theorem burdens",
            "diagnostic-only status cannot re-enter",
            "O-projected status requires real O structure",
            "unsafe metric/source/recovery/boundary/support reentry statuses remain rejected",
            "insertion and parent gates remain closed",
        ],
    ))

    for branch_id in [
        "residual_metric_reentry",
        "residual_source_reentry",
        "recovery_selected_residual_silence",
        "residual_boundary_scalar_reentry",
        "residual_support_layer_reentry",
        "residual_repair_label_reentry",
        "residual_parent_placeholder_reentry",
        "classification_opens_insertion_or_parent",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_25",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; residual classification cannot become reentry, insertion, or parent closure.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g25_residual_status_classification_not_control",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Killed, non-metric, diagnostic-only, inert, and O-projected residual statuses are only safe if their no-reentry burdens are derived. "
            "Metric, source, recovery-selected, boundary/support, repair-label, and parent-placeholder reentry statuses are rejected. "
            "This classification does not derive residual kill, no-overlap, B_s/F_zeta insertion, or parent closure."
        ),
        derivation_ids=[
            "metric_trace_residual_classification_ledger_25",
            "metric_trace_residual_classification_marker_25",
        ],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Metric Trace Residual Classification")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    ledger = build_classification_ledger()
    classes = build_status_classes()
    rules = build_rules()
    routes = build_rejected_routes()

    case_0_problem_statement(out)
    case_1_classification_ledger(ledger, out)
    case_2_status_classes(classes, out)
    case_3_rules(rules, out)
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
