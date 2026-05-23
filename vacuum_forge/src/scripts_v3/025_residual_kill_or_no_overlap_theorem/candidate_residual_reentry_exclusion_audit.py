# Candidate residual reentry exclusion audit
#
# Group:
#   25_residual_kill_or_no_overlap_theorem
#
# Script type:
#   REQUIREMENTS / DIAGNOSTIC
#
# Purpose
# -------
# Audit all possible residual reentry paths.
#
# Locked-door question:
#
#   Can residuals re-enter through another name?
#
# This script does not derive residual non-reentry.
# It does not derive residual kill.
# It does not derive non-metric inertness.
# It does not derive active no-overlap O.
# It does not derive B_s/F_zeta insertion.
# It does not open parent equation closure.
#
# It records that residual non-reentry must be sector-by-sector, not total
# cancellation.

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
            "025_residual_kill_or_no_overlap_theorem__candidate_residual_kill_problem_ledger",
            "residual_kill_problem_ledger_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "classification_dep_25",
            "025_residual_kill_or_no_overlap_theorem__candidate_metric_trace_residual_classification",
            "metric_trace_residual_classification_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "inertness_dep_25",
            "025_residual_kill_or_no_overlap_theorem__candidate_nonmetric_inertness_conditions",
            "nonmetric_inertness_conditions_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g24_boundary_support_dep_25",
            "024_metric_insertion_recovery_retest__candidate_metric_insertion_boundary_support_compatibility",
            "metric_insertion_boundary_support_marker_24",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g24_source_dep_25",
            "024_metric_insertion_recovery_retest__candidate_metric_insertion_source_compatibility",
            "metric_insertion_source_compatibility_marker_24",
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
class ReentryLedger:
    metric_trace: sp.Symbol
    source_load: sp.Symbol
    boundary_flux: sp.Symbol
    scalar_tail: sp.Symbol
    current_flux: sp.Symbol
    A_tail_mass: sp.Symbol
    shell_source: sp.Symbol
    support_radius: sp.Symbol
    smoothing_width: sp.Symbol
    transition_layer: sp.Symbol
    recovery_coeff: sp.Symbol
    gamma_AB_diag: sp.Symbol
    O_eraser: sp.Symbol
    H_insert: sp.Symbol
    dark_label: sp.Symbol
    exchange_label: sp.Symbol
    curvature_label: sp.Symbol
    current_label: sp.Symbol
    parent_placeholder: sp.Symbol
    total_reentry_load: sp.Expr


@dataclass
class ReentryPath:
    name: str
    path: str
    status: str
    forbidden_use: str
    consequence: str


@dataclass
class ReentryExclusionRule:
    name: str
    rule: str
    status: str
    failure_if: str


@dataclass
class ReentryBranch:
    name: str
    branch: str
    status: str
    allowed_if: str
    rejected_if: str


def build_ledger() -> ReentryLedger:
    names = (
        "metric_trace source_load boundary_flux scalar_tail current_flux A_tail_mass shell_source "
        "support_radius smoothing_width transition_layer recovery_coeff gamma_AB_diag O_eraser "
        "H_insert dark_label exchange_label curvature_label current_label parent_placeholder"
    )
    (
        metric_trace,
        source_load,
        boundary_flux,
        scalar_tail,
        current_flux,
        A_tail_mass,
        shell_source,
        support_radius,
        smoothing_width,
        transition_layer,
        recovery_coeff,
        gamma_AB_diag,
        O_eraser,
        H_insert,
        dark_label,
        exchange_label,
        curvature_label,
        current_label,
        parent_placeholder,
    ) = sp.symbols(names, real=True)

    total_reentry_load = sp.simplify(
        metric_trace
        + source_load
        + boundary_flux
        + scalar_tail
        + current_flux
        + A_tail_mass
        + shell_source
        + support_radius
        + smoothing_width
        + transition_layer
        + recovery_coeff
        + gamma_AB_diag
        + O_eraser
        + H_insert
        + dark_label
        + exchange_label
        + curvature_label
        + current_label
        + parent_placeholder
    )

    return ReentryLedger(
        metric_trace=metric_trace,
        source_load=source_load,
        boundary_flux=boundary_flux,
        scalar_tail=scalar_tail,
        current_flux=current_flux,
        A_tail_mass=A_tail_mass,
        shell_source=shell_source,
        support_radius=support_radius,
        smoothing_width=smoothing_width,
        transition_layer=transition_layer,
        recovery_coeff=recovery_coeff,
        gamma_AB_diag=gamma_AB_diag,
        O_eraser=O_eraser,
        H_insert=H_insert,
        dark_label=dark_label,
        exchange_label=exchange_label,
        curvature_label=curvature_label,
        current_label=current_label,
        parent_placeholder=parent_placeholder,
        total_reentry_load=total_reentry_load,
    )


def build_paths() -> List[ReentryPath]:
    return [
        ReentryPath(
            name="P1: metric trace reentry",
            path="residual -> ordinary metric scalar trace",
            status="REJECTED",
            forbidden_use="residual zeta/kappa contributes metric trace after B_s insertion",
            consequence="count-once fails",
        ),
        ReentryPath(
            name="P2: source load reentry",
            path="residual -> ordinary source load / source-loaded coefficient",
            status="REJECTED",
            forbidden_use="residual carries rho/T or source-like load",
            consequence="source no-double-counting fails",
        ),
        ReentryPath(
            name="P3: boundary flux reentry",
            path="residual -> boundary flux / leakage",
            status="REJECTED",
            forbidden_use="residual exports boundary flux",
            consequence="boundary neutrality fails",
        ),
        ReentryPath(
            name="P4: scalar-tail reentry",
            path="residual -> C/r exterior scalar tail",
            status="REJECTED",
            forbidden_use="residual leaves exterior scalar tail",
            consequence="scalar silence fails",
        ),
        ReentryPath(
            name="P5: current-flux reentry",
            path="residual -> non-A current flux",
            status="REJECTED",
            forbidden_use="residual exports current flux",
            consequence="neutral current transport remains unsolved",
        ),
        ReentryPath(
            name="P6: A-tail mass reentry",
            path="residual -> q/r A-tail mass shift",
            status="REJECTED",
            forbidden_use="residual shifts protected A-sector mass",
            consequence="A-sector mass protection fails",
        ),
        ReentryPath(
            name="P7: shell/source seam reentry",
            path="residual -> shell/source seam load",
            status="REJECTED",
            forbidden_use="residual creates shell or finite-width source disguise",
            consequence="no-shell and source compatibility fail",
        ),
        ReentryPath(
            name="P8: support/matching reentry",
            path="residual -> support radius / smoothing width / matching condition",
            status="REJECTED",
            forbidden_use="residual hides in support, smoothing, transition layer, or matching data",
            consequence="smooth-support/matching guardrails fail",
        ),
        ReentryPath(
            name="P9: recovery diagnostic reentry",
            path="residual -> recovery coefficient / gamma-AB diagnostic parameter",
            status="REJECTED",
            forbidden_use="residual status or coefficient chosen from Schwarzschild/gamma/AB/B=1/A/PPN",
            consequence="recovery constructs residual control",
        ),
        ReentryPath(
            name="P10: O/H/dark/exchange/curvature/current repair reentry",
            path="residual -> repair label",
            status="REJECTED",
            forbidden_use="repair label supplies missing residual law",
            consequence="repair theorem is smuggled",
        ),
        ReentryPath(
            name="P11: parent placeholder reentry",
            path="residual -> parent identity placeholder",
            status="REJECTED",
            forbidden_use="residual cleanup opens or fills parent equation",
            consequence="parent closure is smuggled",
        ),
    ]


def build_rules() -> List[ReentryExclusionRule]:
    return [
        ReentryExclusionRule(
            name="R1: sector-by-sector zero",
            rule="each residual reentry path must vanish or be separately theorem-routed",
            status="REQUIRED",
            failure_if="unsafe paths cancel only in total",
        ),
        ReentryExclusionRule(
            name="R2: no renaming",
            rule="residual cannot re-enter by another name",
            status="REQUIRED",
            failure_if="metric/source/boundary/support/recovery/repair labels disguise residual load",
        ),
        ReentryExclusionRule(
            name="R3: no recovery selection",
            rule="reentry exclusion must be fixed before recovery diagnostics",
            status="REQUIRED",
            failure_if="residual status changes to pass recovery",
        ),
        ReentryExclusionRule(
            name="R4: no repair labels",
            rule="O/H/dark/exchange/curvature/current labels cannot supply missing residual non-reentry",
            status="REQUIRED",
            failure_if="repair object closes residual-control gap",
        ),
        ReentryExclusionRule(
            name="R5: no insertion/parent licensing",
            rule="reentry exclusion audit does not prove B_s/F_zeta insertion or parent equation",
            status="REQUIRED",
            failure_if="audit result opens insertion or parent gate",
        ),
    ]


def build_branches() -> List[ReentryBranch]:
    return [
        ReentryBranch(
            name="B1: strict residual non-reentry",
            branch="all reentry paths zero sector-by-sector or theorem-routed",
            status="THEOREM_TARGET",
            allowed_if="metric/source/boundary/support/recovery/repair/parent reentry is derived absent",
            rejected_if="any path is merely ignored or canceled in total",
        ),
        ReentryBranch(
            name="B2: diagnostic-only non-reentry audit",
            branch="residual reentry paths are listed without claiming theorem",
            status="SAFE_IF",
            allowed_if="used only as requirements audit",
            rejected_if="used to license residual kill or insertion",
        ),
        ReentryBranch(
            name="B3: total cancellation non-reentry",
            branch="multiple unsafe reentry paths cancel only in aggregate",
            status="REJECTED",
            allowed_if="never as non-reentry theorem",
            rejected_if="sector-by-sector zero is replaced by sum zero",
        ),
        ReentryBranch(
            name="B4: repair non-reentry",
            branch="O/H/dark/exchange/curvature/current labels erase residual paths",
            status="REJECTED",
            allowed_if="never without the relevant theorem",
            rejected_if="repair label is invoked by name",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Residual reentry exclusion problem")
    print("Question:")
    print()
    print("  Can residuals re-enter through another name?")
    print()
    print("Reference discipline:")
    print()
    print("  Residual non-reentry must be sector-by-sector.")
    print("  Total cancellation is not non-reentry.")
    print("  Renaming residual load as metric, source, boundary, support, recovery, repair, or parent data is rejected.")

    with out.governance_assessments():
        out.line(
            "residual reentry exclusion audit opened",
            StatusMark.INFO,
            "auditing residual reentry paths under every known label",
        )


def case_1_reentry_ledger(ledger: ReentryLedger, out: ScriptOutput) -> None:
    header("Case 1: Residual reentry load ledger")
    print("Representative reentry channels:")
    print()
    for name in [
        "metric_trace",
        "source_load",
        "boundary_flux",
        "scalar_tail",
        "current_flux",
        "A_tail_mass",
        "shell_source",
        "support_radius",
        "smoothing_width",
        "transition_layer",
        "recovery_coeff",
        "gamma_AB_diag",
        "O_eraser",
        "H_insert",
        "dark_label",
        "exchange_label",
        "curvature_label",
        "current_label",
        "parent_placeholder",
    ]:
        print(f"  {name} = {sp.sstr(getattr(ledger, name))}")
    print()
    print("Total reentry load:")
    print()
    print(f"  L_reentry = {sp.sstr(ledger.total_reentry_load)}")
    print()
    print("Interpretation:")
    print()
    print("  L_reentry = 0 by total cancellation is not enough.")
    print("  Each channel must vanish sector-by-sector or be theorem-routed.")

    with out.derived_results():
        out.line(
            "residual reentry load ledger stated",
            StatusMark.OBLIGATION,
            f"L_reentry = {sp.sstr(ledger.total_reentry_load)}",
        )


def case_2_paths(paths: List[ReentryPath], out: ScriptOutput) -> None:
    header("Case 2: Residual reentry paths")
    for path in paths:
        print()
        print("-" * 120)
        print(path.name)
        print("-" * 120)
        print(f"Path: {path.path}")
        print(f"Forbidden use: {path.forbidden_use}")
        print(f"[{status_mark(path.status).value}] {path.name}: {path.status}")
        print(f"Consequence: {path.consequence}")

    with out.counterexamples():
        out.line(
            "residual reentry paths rejected",
            StatusMark.FAIL,
            f"{len(paths)} residual reentry paths rejected as control routes",
        )


def case_3_rules(rules: List[ReentryExclusionRule], out: ScriptOutput) -> None:
    header("Case 3: Residual reentry exclusion rules")
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
            "residual reentry exclusion rules populated",
            StatusMark.OBLIGATION,
            f"{len(rules)} rules constrain residual non-reentry",
        )


def case_4_branches(branches: List[ReentryBranch], out: ScriptOutput) -> None:
    header("Case 4: Residual non-reentry branches")
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
            "residual non-reentry branches classified",
            StatusMark.PASS,
            f"{len(branches)} non-reentry branches classified",
        )


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("The residual reentry exclusion audit fails if a later script allows:")
    print()
    print("1. residual metric trace reentry")
    print("2. residual source-load reentry")
    print("3. residual boundary/scalar/current reentry")
    print("4. residual A-tail mass shift")
    print("5. residual shell/source load")
    print("6. residual support/smoothing/transition/matching reentry")
    print("7. residual recovery/gamma/AB diagnostic reentry")
    print("8. residual O/H/dark/exchange/curvature/current repair reentry")
    print("9. residual parent-placeholder reentry")
    print("10. total cancellation treated as non-reentry")
    print("11. insertion or parent gate opened from reentry audit alone")

    with out.governance_assessments():
        out.line(
            "residual reentry exclusion failure controls stated",
            StatusMark.OBLIGATION,
            "future scripts must reject residual reentry under every known name",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Residual reentry exclusion result:")
    print()
    print("  Residuals cannot re-enter through metric, source, boundary, scalar-tail, current-flux, A-tail, shell/source, support, smoothing, transition, recovery, gamma/AB, O, H, dark, exchange, curvature, current, or parent-placeholder language.")
    print("  Non-reentry must be sector-by-sector.")
    print("  Total cancellation is not non-reentry.")
    print("  This remains a theorem burden.")
    print()
    print("Possible next script:")
    print("  candidate_no_overlap_operator_minimum_burden.py")
    print()
    print("Tiny goblin label:")
    print("  Every pocket checked. No renamed ghost.")

    with out.governance_assessments():
        out.line(
            "residual reentry exclusion audit complete",
            StatusMark.PASS,
            "reentry paths explicit; non-reentry theorem remains open",
        )


def record_derivations(ns, ledger: ReentryLedger) -> None:
    ns.record_derivation(
        derivation_id="residual_reentry_load_25",
        inputs=[
            ledger.metric_trace,
            ledger.source_load,
            ledger.boundary_flux,
            ledger.scalar_tail,
            ledger.current_flux,
            ledger.A_tail_mass,
            ledger.shell_source,
            ledger.support_radius,
            ledger.smoothing_width,
            ledger.transition_layer,
            ledger.recovery_coeff,
            ledger.gamma_AB_diag,
            ledger.O_eraser,
            ledger.H_insert,
            ledger.dark_label,
            ledger.exchange_label,
            ledger.curvature_label,
            ledger.current_label,
            ledger.parent_placeholder,
        ],
        output=ledger.total_reentry_load,
        method="sum representative residual reentry channels for audit only",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="residual_reentry_ledger",
        scope="Group 25 residual kill or no-overlap theorem",
    )

    ns.record_derivation(
        derivation_id="residual_reentry_exclusion_marker_25",
        inputs=[
            sp.Symbol("metric_reentry_zero"),
            sp.Symbol("source_reentry_zero"),
            sp.Symbol("boundary_reentry_zero"),
            sp.Symbol("support_reentry_zero"),
            sp.Symbol("recovery_reentry_zero"),
            sp.Symbol("repair_reentry_zero"),
            sp.Symbol("parent_reentry_zero"),
        ],
        output=sp.Symbol("residual_reentry_exclusion_conditions_stated"),
        method="Group 25 residual reentry exclusion audit",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="requirements_marker",
        scope="Group 25 residual kill or no-overlap theorem",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g25_derive_no_metric_reentry", "Derive no residual metric reentry"),
        ("g25_derive_no_source_reentry", "Derive no residual source reentry"),
        ("g25_derive_no_boundary_scalar_current_reentry", "Derive no residual boundary/scalar/current reentry"),
        ("g25_derive_no_A_tail_shell_reentry", "Derive no residual A-tail or shell/source reentry"),
        ("g25_derive_no_support_layer_reentry", "Derive no residual support/layer reentry"),
        ("g25_derive_no_recovery_reentry", "Derive no residual recovery diagnostic reentry"),
        ("g25_derive_no_repair_reentry", "Derive no residual repair-label reentry"),
        ("g25_derive_no_parent_reentry", "Derive no residual parent-placeholder reentry"),
        ("g25_derive_sector_by_sector_nonreentry", "Derive sector-by-sector non-reentry"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g25_residual_reentry_exclusion_route"],
            description=(
                "Residual non-reentry remains theorem-targeted until each reentry path is closed sector-by-sector."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g25_derive_no_metric_reentry",
        "g25_derive_no_source_reentry",
        "g25_derive_no_boundary_scalar_current_reentry",
        "g25_derive_no_A_tail_shell_reentry",
        "g25_derive_no_support_layer_reentry",
        "g25_derive_no_recovery_reentry",
        "g25_derive_no_repair_reentry",
        "g25_derive_no_parent_reentry",
        "g25_derive_sector_by_sector_nonreentry",
    ]

    ns.record_route(RouteRecord(
        route_id="g25_reentry_exclusion_route",
        script_id=SCRIPT_ID,
        name="Group 25 residual reentry exclusion theorem target",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "metric/source/boundary/support/recovery/repair/parent reentry paths are closed sector-by-sector",
            "total cancellation is not used",
            "residual reentry is not renamed",
            "insertion and parent gates remain closed",
        ],
    ))

    for branch_id in [
        "residual_metric_reentry",
        "residual_source_reentry",
        "residual_boundary_current_reentry",
        "residual_A_tail_shell_reentry",
        "residual_support_layer_reentry",
        "residual_recovery_reentry",
        "residual_repair_reentry",
        "residual_parent_reentry",
        "residual_total_cancellation_nonreentry",
        "insertion_parent_from_reentry_audit",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_25",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; residual non-reentry must be sector-by-sector and theorem-routed.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g25_residual_nonreentry_sector_by_sector",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Residuals cannot re-enter through metric, source, boundary, scalar-tail, current-flux, A-tail, shell/source, "
            "support, smoothing, transition, recovery, gamma/AB, O, H, dark, exchange, curvature, current, or parent-placeholder language. "
            "Non-reentry must be sector-by-sector, not total cancellation."
        ),
        derivation_ids=[
            "residual_reentry_load_25",
            "residual_reentry_exclusion_marker_25",
        ],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Residual Reentry Exclusion Audit")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    ledger = build_ledger()
    paths = build_paths()
    rules = build_rules()
    branches = build_branches()

    case_0_problem_statement(out)
    case_1_reentry_ledger(ledger, out)
    case_2_paths(paths, out)
    case_3_rules(rules, out)
    case_4_branches(branches, out)
    case_5_failure_controls(out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, ledger)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
