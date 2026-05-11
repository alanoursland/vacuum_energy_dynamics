# Candidate diagnostic residual nonmetric conditions
#
# Group:
#   22_boundary_neutrality_and_scalar_silence
#
# Script type:
#   REQUIREMENTS / DIAGNOSTIC
#
# Purpose
# -------
# Clarify when a residual may survive as diagnostic / non-metric without
# affecting mass, scalar silence, source routing, or boundary behavior.
#
# Locked-door question:
#
#   When can a residual survive as diagnostic/non-metric without affecting
#   mass or boundary behavior?
#
# This script does not derive residual-kill.
# It does not derive no-overlap O.
# It does not prove scalar silence.
# It does not prove boundary neutrality.
#
# It records the no-reentry conditions for residual diagnostic labels.

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
        "DIAGNOSTIC_ONLY": StatusMark.INFO,
        "FORBIDDEN": StatusMark.FAIL,
        "PROVISIONAL": StatusMark.INFO,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "RISK": StatusMark.WARN,
        "ROLE_LEVEL": StatusMark.INFO,
        "SAFE_IF": StatusMark.INFO,
        "THEOREM_TARGET": StatusMark.DEFER,
        "UNRESOLVED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "boundary_scalar_silence_target_ledger_dependency_22",
            "22_boundary_neutrality_and_scalar_silence__candidate_boundary_scalar_silence_targets",
            "boundary_scalar_silence_target_ledger_marker_22",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "sector_scalar_silence_dependency_22",
            "22_boundary_neutrality_and_scalar_silence__candidate_scalar_tail_silence_sector_conditions",
            "scalar_tail_silence_sector_inventory_marker_22",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "smooth_compact_no_shell_dependency_22",
            "22_boundary_neutrality_and_scalar_silence__candidate_smooth_compact_support_no_shell_conditions",
            "smooth_compact_support_no_shell_inventory_marker_22",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "boundary_repair_exclusion_dependency_22",
            "22_boundary_neutrality_and_scalar_silence__candidate_boundary_repair_route_exclusion",
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
class ResidualLeakDiagnostic:
    C_metric: sp.Symbol
    C_source: sp.Symbol
    q_boundary: sp.Symbol
    I_far: sp.Symbol
    E_account: sp.Symbol
    total_reentry_load: sp.Expr
    scalar_flux: sp.Expr
    boundary_mass_shift: sp.Expr
    current_flux: sp.Expr


@dataclass
class NonmetricConditionEntry:
    name: str
    condition: str
    status: str
    failure_if: str
    consequence: str


@dataclass
class ResidualReentryRoute:
    name: str
    route: str
    forbidden_use: str
    status: str
    consequence: str


def build_diagnostics() -> ResidualLeakDiagnostic:
    C_metric, C_source, q_boundary, I_far, E_account = sp.symbols(
        "C_metric C_source q_boundary I_far E_account",
        real=True,
    )
    G = sp.Symbol("G", positive=True)
    c = sp.Symbol("c", positive=True)

    return ResidualLeakDiagnostic(
        C_metric=C_metric,
        C_source=C_source,
        q_boundary=q_boundary,
        I_far=I_far,
        E_account=E_account,
        total_reentry_load=sp.simplify(C_metric + C_source + q_boundary + I_far + E_account),
        scalar_flux=sp.simplify(-4 * sp.pi * C_metric),
        boundary_mass_shift=sp.simplify(-c**2 * q_boundary / (2 * G)),
        current_flux=I_far,
    )


def build_conditions() -> List[NonmetricConditionEntry]:
    return [
        NonmetricConditionEntry(
            name="N1: no metric trace effect",
            condition="residual does not enter g_ij scalar trace, A, B_s, zeta metric trace, or kappa metric trace",
            status="REQUIRED",
            failure_if="diagnostic residual becomes metric scalar tail or spatial trace component",
            consequence="residual remains bookkeeping, not geometry",
        ),
        NonmetricConditionEntry(
            name="N2: no source role",
            condition="residual does not source A, zeta, kappa, J_V, curvature, H, exchange, dark, or ordinary matter routing",
            status="REQUIRED",
            failure_if="diagnostic label becomes source reservoir or coefficient supply",
            consequence="residual cannot become hidden source energy",
        ),
        NonmetricConditionEntry(
            name="N3: no boundary flux",
            condition="residual creates no boundary A-tail, scalar flux, derivative jump, or shell source",
            status="REQUIRED",
            failure_if="diagnostic residual changes boundary behavior or hides shell flux",
            consequence="residual cannot be boundary purse",
        ),
        NonmetricConditionEntry(
            name="N4: no far-zone tail",
            condition="residual has no exterior 1/r scalar coefficient and no 1/r^2 current flux coefficient",
            status="REQUIRED",
            failure_if="residual leaves C/r or I/(4*pi*r^2) far-zone residue",
            consequence="residual remains exterior-silent",
        ),
        NonmetricConditionEntry(
            name="N5: no coefficient reservoir",
            condition="residual accounting terms do not supply recovery, stiffness, smoothing, mass, or support coefficients",
            status="REQUIRED",
            failure_if="epsilon/e/residual label becomes parameter bank",
            consequence="residual cannot tune recovery or boundary behavior",
        ),
        NonmetricConditionEntry(
            name="N6: no later re-entry",
            condition="residual cannot re-enter through H, O, dark label, curvature, exchange, source projector, or parent equation placeholder",
            status="REQUIRED",
            failure_if="residual is demoted now but reintroduced later through a patch object",
            consequence="diagnostic/non-metric status must be stable under later bookkeeping",
        ),
        NonmetricConditionEntry(
            name="N7: recovery independence",
            condition="diagnostic/non-metric status is not chosen from Schwarzschild/PPN/gamma_like/AB/B=1/A recovery",
            status="REQUIRED",
            failure_if="residual status is selected to pass a recovery check",
            consequence="recovery remains downstream diagnostic, not construction",
        ),
        NonmetricConditionEntry(
            name="N8: explicit theorem target if residual survives",
            condition="any residual survival beyond inert diagnostics is marked theorem-targeted",
            status="REQUIRED",
            failure_if="surviving residual is treated as licensed by nonmetric vocabulary",
            consequence="nonmetric labels do not prove no-overlap",
        ),
    ]


def build_reentry_routes() -> List[ResidualReentryRoute]:
    return [
        ResidualReentryRoute(
            name="R1: metric trace re-entry",
            route="residual_to_metric_trace",
            forbidden_use="residual returns as g_ij scalar trace after being called non-metric",
            status="REJECTED",
            consequence="violates count-once / scalar silence discipline",
        ),
        ResidualReentryRoute(
            name="R2: source reservoir re-entry",
            route="residual_to_source_reservoir",
            forbidden_use="residual supplies A, kappa, zeta, curvature, H, exchange, or dark source coefficient",
            status="REJECTED",
            consequence="diagnostic residual becomes hidden source energy",
        ),
        ResidualReentryRoute(
            name="R3: boundary repair re-entry",
            route="residual_to_boundary_repair",
            forbidden_use="residual adjusts boundary slope, support, smoothing, or shell behavior",
            status="REJECTED",
            consequence="residual becomes boundary purse",
        ),
        ResidualReentryRoute(
            name="R4: H/O patch re-entry",
            route="residual_to_H_or_O_patch",
            forbidden_use="H or O reintroduces a killed/nonmetric residual as correction or projection remainder",
            status="REJECTED",
            consequence="undefined patch objects cannot license residual survival",
        ),
        ResidualReentryRoute(
            name="R5: recovery-selected nonmetric status",
            route="recovery_selected_nonmetric_status",
            forbidden_use="residual is declared non-metric only because recovery requires it",
            status="REJECTED",
            consequence="recovery may audit residual status but cannot construct it",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Diagnostic residual nonmetric problem")
    print("Question:")
    print()
    print("  When can a residual survive as diagnostic/non-metric without affecting mass or boundary behavior?")
    print()
    print("Reference discipline:")
    print()
    print("  Scalar-tail sector coefficients must vanish unless residuals are inert or theorem-routed.")
    print("  Compact support needs matching/no-shell conditions.")
    print("  Boundary repair routes are rejected.")
    print("  Nonmetric vocabulary is not a proof of no-overlap.")
    print("  This script records no-reentry conditions for diagnostic residuals.")

    with out.governance_assessments():
        out.line(
            "diagnostic residual nonmetric audit opened",
            StatusMark.INFO,
            "checking when residual labels may survive without metric/source/boundary/mass effect",
        )


def case_1_reentry_diagnostics(exprs: ResidualLeakDiagnostic, out: ScriptOutput) -> None:
    header("Case 1: Residual re-entry diagnostics")
    print("If a diagnostic residual re-enters forbidden channels, the load ledger is:")
    print()
    print(f"  total_reentry_load = {sp.sstr(exprs.total_reentry_load)}")
    print()
    print("Representative reduced leakage witnesses:")
    print()
    print(f"  scalar flux from metric tail coefficient = {sp.sstr(exprs.scalar_flux)}")
    print(f"  boundary mass shift from A-tail coefficient = {sp.sstr(exprs.boundary_mass_shift)}")
    print(f"  far-zone current flux = {sp.sstr(exprs.current_flux)}")
    print()
    print("Neutral diagnostic residual status requires all re-entry channels to remain inert.")
    print("Cancellation among these labels is not nonmetric status.")

    with out.derived_results():
        out.line(
            "diagnostic residual re-entry load ledger stated",
            StatusMark.PASS,
            f"total_reentry_load = {sp.sstr(exprs.total_reentry_load)}",
        )
        out.line(
            "metric-tail leakage witness stated",
            StatusMark.PASS,
            f"F = {sp.sstr(exprs.scalar_flux)}",
        )
        out.line(
            "boundary A-tail leakage witness stated",
            StatusMark.PASS,
            f"delta_M_A = {sp.sstr(exprs.boundary_mass_shift)}",
        )
        out.line(
            "far-zone current leakage witness stated",
            StatusMark.PASS,
            f"Phi = {sp.sstr(exprs.current_flux)}",
        )


def case_2_condition_ledger(entries: List[NonmetricConditionEntry], out: ScriptOutput) -> None:
    header("Case 2: Diagnostic/non-metric residual condition ledger")
    for entry in entries:
        print()
        print("-" * 120)
        print(entry.name)
        print("-" * 120)
        print(f"Condition: {entry.condition}")
        print(f"[{status_mark(entry.status).value}] {entry.name}: {entry.status}")
        print(f"Failure if: {entry.failure_if}")
        print(f"Consequence: {entry.consequence}")

    with out.governance_assessments():
        out.line(
            "diagnostic/nonmetric residual condition ledger populated",
            StatusMark.PASS,
            f"{len(entries)} no-reentry conditions stated",
        )


def case_3_reentry_routes(routes: List[ResidualReentryRoute], out: ScriptOutput) -> None:
    header("Case 3: Rejected residual re-entry routes")
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
            "residual re-entry routes rejected",
            StatusMark.FAIL,
            "metric/source/boundary/H/O/recovery re-entry routes are not licensed",
        )


def case_4_failure_controls(out: ScriptOutput) -> None:
    header("Case 4: Failure controls")
    print("The diagnostic residual nonmetric audit fails if a later script allows:")
    print()
    print("1. nonmetric residual to enter metric scalar trace")
    print("2. diagnostic residual to source A, zeta, kappa, curvature, H, exchange, or dark labels")
    print("3. residual accounting to become coefficient reservoir")
    print("4. residual to alter boundary slope/support/smoothing/shell behavior")
    print("5. residual to leave exterior C/r scalar tail")
    print("6. residual to leave far-zone I/(4*pi*r^2) current flux")
    print("7. H or O to reinsert a killed/nonmetric residual")
    print("8. dark label to absorb residual leakage")
    print("9. recovery target to choose nonmetric status")
    print("10. nonmetric vocabulary to be treated as no-overlap theorem")

    with out.governance_assessments():
        out.line(
            "diagnostic residual overclaim controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not convert inert residual labels into active channels",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("A residual may survive as diagnostic/non-metric only if it has:")
    print()
    print("  no metric trace effect")
    print("  no source role")
    print("  no boundary flux")
    print("  no far-zone tail")
    print("  no coefficient reservoir")
    print("  no later re-entry through H, O, dark labels, curvature, exchange, or parent placeholders")
    print("  no recovery-selected status")
    print()
    print("This script does not prove residual-kill or no-overlap.")
    print("It records the no-reentry burden for diagnostic residual survival.")
    print()
    print("Possible next script:")
    print("  candidate_boundary_neutrality_theorem_obligations.py")

    with out.governance_assessments():
        out.line(
            "diagnostic residual nonmetric audit complete",
            StatusMark.PASS,
            "diagnostic residuals are safe only if inert and non-reentering",
        )


def record_derivations(ns, exprs: ResidualLeakDiagnostic) -> None:
    ns.record_derivation(
        derivation_id="diagnostic_residual_reentry_load_ledger_22",
        inputs=[exprs.C_metric, exprs.C_source, exprs.q_boundary, exprs.I_far, exprs.E_account],
        output=exprs.total_reentry_load,
        method="sum representative forbidden residual re-entry labels",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="reentry_load_ledger",
        scope="Group 22 diagnostic residual nonmetric conditions",
    )
    ns.record_derivation(
        derivation_id="diagnostic_residual_nonmetric_conditions_marker_22",
        inputs=[sp.Symbol("metric"), sp.Symbol("source"), sp.Symbol("boundary"), sp.Symbol("far_zone"), sp.Symbol("reentry")],
        output=sp.Symbol("diagnostic_residual_nonmetric_conditions_stated"),
        method="Group 22 diagnostic residual no-reentry requirements ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="requirements_marker",
        scope="Group 22 boundary neutrality and scalar silence",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        (
            "derive_diagnostic_residual_inertness_22",
            "Derive diagnostic residual inertness",
            "Show diagnostic/non-metric residuals have no metric, source, boundary, mass, far-zone, coefficient, or recovery effect.",
        ),
        (
            "derive_residual_non_reentry_theorem_22",
            "Derive residual non-reentry theorem",
            "Show killed/nonmetric residuals cannot re-enter through H, O, dark labels, curvature, exchange, source projectors, or parent placeholders.",
        ),
        (
            "derive_recovery_independent_residual_status_22",
            "Derive recovery-independent residual status",
            "Show residual diagnostic/non-metric status is structural, not selected by Schwarzschild/PPN/gamma_like/AB/B=1/A recovery.",
        ),
    ]

    for obligation_id, title, description in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["ordinary_closed_regime_diagnostic_residual_nonmetric_theorem_22"],
            description=description,
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "derive_diagnostic_residual_inertness_22",
        "derive_residual_non_reentry_theorem_22",
        "derive_recovery_independent_residual_status_22",
    ]

    ns.record_route(RouteRecord(
        route_id="ordinary_closed_regime_diagnostic_residual_nonmetric_theorem_22",
        script_id=SCRIPT_ID,
        name="Ordinary closed-regime diagnostic residual nonmetric theorem target",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "residual has no metric trace effect",
            "residual has no source role",
            "residual has no boundary/far-zone leakage",
            "residual cannot re-enter through H, O, dark, curvature, exchange, or parent placeholders",
            "residual status is not recovery-selected",
        ],
    ))

    for branch_id in [
        "residual_to_metric_trace",
        "residual_to_source_reservoir",
        "residual_to_boundary_repair",
        "residual_to_H_or_O_patch",
        "recovery_selected_nonmetric_status",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_22",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; diagnostic/non-metric residual labels must remain inert and non-reentering.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="diagnostic_residuals_must_be_inert_nonreentering_22",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Diagnostic/non-metric residuals are safe only if they have no metric, source, boundary, far-zone, coefficient, recovery, or later re-entry effect."
        ),
        derivation_ids=[
            "diagnostic_residual_reentry_load_ledger_22",
            "diagnostic_residual_nonmetric_conditions_marker_22",
        ],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Diagnostic Residual Nonmetric Conditions")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    exprs = build_diagnostics()
    conditions = build_conditions()
    routes = build_reentry_routes()

    case_0_problem_statement(out)
    case_1_reentry_diagnostics(exprs, out)
    case_2_condition_ledger(conditions, out)
    case_3_reentry_routes(routes, out)
    case_4_failure_controls(out)
    final_interpretation(out)

    record_derivations(ns, exprs)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
