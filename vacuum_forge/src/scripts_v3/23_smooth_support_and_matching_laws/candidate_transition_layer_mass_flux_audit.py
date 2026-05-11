# Candidate transition layer mass flux audit
#
# Group:
#   23_smooth_support_and_matching_laws
#
# Script type:
#   REQUIREMENTS / DIAGNOSTIC
#
# Purpose
# -------
# Audit whether a smooth transition layer can hide mass, scalar flux, boundary
# source load, A-tail shift, or recovery-tuned parameters.
#
# Locked-door question:
#
#   Can a smooth transition layer hide mass or scalar flux?
#
# This script does not derive a transition-layer theorem.
# It does not prove compact support.
# It does not prove no-shell matching.
# It does not prove boundary neutrality or scalar silence.
#
# It records that smoothness is not enough:
#
#   transition layers must have zero net scalar flux,
#   no induced A-tail,
#   no exterior scalar 1/r tail,
#   no shell/source load,
#   no recovery-tuned parameters,
#   no source-routing duplication,
#   and no repair role.

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


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


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
            "matching_ladder_dep_23",
            "23_smooth_support_and_matching_laws__candidate_matching_regularization_ladder",
            "matching_regularization_ladder_marker_23",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "shell_audit_dep_23",
            "23_smooth_support_and_matching_laws__candidate_distributional_shell_source_audit",
            "distributional_shell_source_audit_marker_23",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "compact_support_dep_23",
            "23_smooth_support_and_matching_laws__candidate_compact_support_admissibility_conditions",
            "compact_support_admissibility_marker_23",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g22_current_dep_23",
            "22_boundary_neutrality_and_scalar_silence__candidate_boundary_current_flux_silence",
            "boundary_current_flux_silence_inventory_marker_22",
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
class TransitionLayerDiagnostic:
    R: sp.Symbol
    ell: sp.Symbol
    C_layer: sp.Symbol
    q_layer: sp.Symbol
    I_layer: sp.Symbol
    sigma_layer: sp.Symbol
    alpha_recovery: sp.Symbol
    source_load: sp.Symbol
    scalar_flux_layer: sp.Expr
    A_mass_shift_layer: sp.Expr
    current_flux_layer: sp.Expr
    layer_load_residual: sp.Expr
    width_limit_warning: sp.Expr


@dataclass
class TransitionLayerCondition:
    name: str
    condition: str
    status: str
    failure_if: str
    consequence: str


@dataclass
class TransitionLayerBranch:
    name: str
    branch: str
    status: str
    allowed_if: str
    rejected_if: str


@dataclass
class RejectedTransitionRoute:
    name: str
    route: str
    forbidden_use: str
    status: str
    consequence: str


# =============================================================================
# Builders
# =============================================================================


def build_diagnostics() -> TransitionLayerDiagnostic:
    R = sp.Symbol("R", positive=True)
    ell = sp.Symbol("ell", positive=True)
    C_layer, q_layer, I_layer, sigma_layer, alpha_recovery, source_load = sp.symbols(
        "C_layer q_layer I_layer sigma_layer alpha_recovery source_load",
        real=True,
    )
    G = sp.Symbol("G", positive=True)
    c = sp.Symbol("c", positive=True)

    scalar_flux_layer = sp.simplify(-4 * sp.pi * C_layer)
    A_mass_shift_layer = sp.simplify(-c**2 * q_layer / (2 * G))
    current_flux_layer = I_layer

    # Representative ledger: all layer-carried burdens must vanish or be
    # independently theorem-routed.  The width limit warning records that
    # sending ell -> 0 while keeping a finite sigma_layer is shell-like.
    layer_load_residual = sp.simplify(
        C_layer
        + q_layer
        + I_layer
        + sigma_layer
        + alpha_recovery
        + source_load
    )
    width_limit_warning = sp.simplify(sigma_layer / ell)

    return TransitionLayerDiagnostic(
        R=R,
        ell=ell,
        C_layer=C_layer,
        q_layer=q_layer,
        I_layer=I_layer,
        sigma_layer=sigma_layer,
        alpha_recovery=alpha_recovery,
        source_load=source_load,
        scalar_flux_layer=scalar_flux_layer,
        A_mass_shift_layer=A_mass_shift_layer,
        current_flux_layer=current_flux_layer,
        layer_load_residual=layer_load_residual,
        width_limit_warning=width_limit_warning,
    )


def build_conditions() -> List[TransitionLayerCondition]:
    return [
        TransitionLayerCondition(
            name="T1: zero net scalar flux",
            condition="C_layer = 0 or an independently derived neutral layer route",
            status="REQUIRED",
            failure_if="smooth layer leaves an exterior C/r tail or net scalar flux",
            consequence="smoothness does not imply scalar silence",
        ),
        TransitionLayerCondition(
            name="T2: no induced A-tail",
            condition="q_layer = 0",
            status="REQUIRED",
            failure_if="transition layer induces delta A = q/r",
            consequence="layer must not shift protected A-sector mass",
        ),
        TransitionLayerCondition(
            name="T3: no far-zone current flux",
            condition="I_layer = 0 unless neutral transport is derived",
            status="REQUIRED",
            failure_if="transition layer exports I/(4*pi*r^2) non-A current flux",
            consequence="smooth layer cannot become current repair",
        ),
        TransitionLayerCondition(
            name="T4: no hidden shell/source load",
            condition="sigma_layer = 0 and no finite shell load in ell -> 0 limit",
            status="REQUIRED",
            failure_if="transition layer smooths a shell source into finite-width disguise",
            consequence="smooth paint does not remove shell accounting",
        ),
        TransitionLayerCondition(
            name="T5: recovery independence",
            condition="alpha_recovery = 0 and layer width/profile is not chosen from Schwarzschild/PPN/gamma_like/AB/B=1/A recovery",
            status="REQUIRED",
            failure_if="layer parameters are selected to pass recovery",
            consequence="recovery remains downstream diagnostic, not construction",
        ),
        TransitionLayerCondition(
            name="T6: source no-double-counting",
            condition="source_load = 0 for duplicate ordinary source load",
            status="REQUIRED",
            failure_if="ordinary rho/T is rerouted into transition layer stress/source",
            consequence="layer must preserve source-routing compatibility",
        ),
        TransitionLayerCondition(
            name="T7: structural layer origin",
            condition="layer profile follows from support/matching law before leakage appears",
            status="REQUIRED",
            failure_if="layer is introduced after scalar, boundary, mass, or recovery failure",
            consequence="transition layer cannot be a repair mechanism",
        ),
    ]


def build_branches() -> List[TransitionLayerBranch]:
    return [
        TransitionLayerBranch(
            name="B1: smoothing by declaration",
            branch="replace sharp cutoff with smooth layer and declare safe",
            status="REJECTED",
            allowed_if="never as theorem; only as diagnostic object with open burdens",
            rejected_if="used to claim no-shell, scalar silence, or boundary neutrality",
        ),
        TransitionLayerBranch(
            name="B2: zero-flux diagnostic layer",
            branch="layer has zero scalar/current/A-tail coefficients in diagnostic ledger",
            status="SAFE_IF",
            allowed_if="used only as necessary diagnostic condition",
            rejected_if="treated as structural layer origin",
        ),
        TransitionLayerBranch(
            name="B3: finite-width hidden shell layer",
            branch="finite transition layer carries sigma_layer or source_load",
            status="REJECTED",
            allowed_if="never as ordinary silent support",
            rejected_if="used to disguise shell/source load",
        ),
        TransitionLayerBranch(
            name="B4: structural transition layer",
            branch="layer follows from derived support/matching law",
            status="THEOREM_TARGET",
            allowed_if="all neutrality, source, recovery, and no-repair conditions are derived",
            rejected_if="any parameter is selected after leakage appears",
        ),
    ]


def build_rejected_routes() -> List[RejectedTransitionRoute]:
    return [
        RejectedTransitionRoute(
            name="R1: smoothness as neutrality",
            route="smoothness_as_neutrality",
            forbidden_use="smooth profile alone claims no-shell/no-tail behavior",
            status="REJECTED",
            consequence="smoothness is not enough",
        ),
        RejectedTransitionRoute(
            name="R2: finite-width shell disguise",
            route="finite_width_shell_disguise",
            forbidden_use="layer carries finite source/shell load but avoids delta notation",
            status="REJECTED",
            consequence="hidden layer load is still source accounting",
        ),
        RejectedTransitionRoute(
            name="R3: recovery-tuned transition",
            route="recovery_tuned_transition",
            forbidden_use="layer width or shape chosen to recover Schwarzschild/PPN/gamma_like/AB/B=1/A",
            status="REJECTED",
            consequence="recovery cannot choose the layer",
        ),
        RejectedTransitionRoute(
            name="R4: transition layer scalar/A-tail repair",
            route="transition_scalar_A_tail_repair",
            forbidden_use="layer coefficient cancels scalar tail or A-tail after leakage appears",
            status="REJECTED",
            consequence="layer cannot be repair tuning",
        ),
        RejectedTransitionRoute(
            name="R5: transition layer source reroute",
            route="transition_source_reroute",
            forbidden_use="ordinary rho/T is rerouted into layer stress or non-A source load",
            status="REJECTED",
            consequence="source no-double-counting remains protected",
        ),
        RejectedTransitionRoute(
            name="R6: repair object supplies layer",
            route="O_H_dark_exchange_curvature_layer_patch",
            forbidden_use="O, H, dark, exchange, curvature, or current role supplies missing transition law",
            status="REJECTED",
            consequence="repair objects cannot derive transition support",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Transition layer mass/flux audit problem")
    print("Question:")
    print()
    print("  Can a smooth transition layer hide mass or scalar flux?")
    print()
    print("Reference discipline:")
    print()
    print("  Matching and shell audits show regularity diagnostics are not support theorems.")
    print("  Compact support admissibility requires no tails, no A-tail, no hidden tuning, and source compatibility.")
    print("  This script checks whether smoothing layers can hide those failures.")
    print("  It does not derive a transition-layer theorem.")

    with out.governance_assessments():
        out.line(
            "transition layer mass/flux audit opened",
            StatusMark.INFO,
            "testing whether smooth layers can hide scalar, A-tail, current, shell, recovery, or source loads",
        )


def case_1_diagnostics(exprs: TransitionLayerDiagnostic, out: ScriptOutput) -> None:
    header("Case 1: Transition layer leakage diagnostics")
    print("Representative transition layer coefficients:")
    print()
    print(f"  C_layer = {sp.sstr(exprs.C_layer)}")
    print(f"  q_layer = {sp.sstr(exprs.q_layer)}")
    print(f"  I_layer = {sp.sstr(exprs.I_layer)}")
    print(f"  sigma_layer = {sp.sstr(exprs.sigma_layer)}")
    print(f"  alpha_recovery = {sp.sstr(exprs.alpha_recovery)}")
    print(f"  source_load = {sp.sstr(exprs.source_load)}")
    print()
    print("Reduced leakage witnesses:")
    print()
    print(f"  scalar flux from C_layer: {sp.sstr(exprs.scalar_flux_layer)}")
    print(f"  A-sector mass shift from q_layer: {sp.sstr(exprs.A_mass_shift_layer)}")
    print(f"  far-zone current flux from I_layer: {sp.sstr(exprs.current_flux_layer)}")
    print()
    print("Layer residual ledger:")
    print()
    print(f"  layer_load_residual = {sp.sstr(exprs.layer_load_residual)}")
    print()
    print("Thin-layer warning:")
    print()
    print(f"  sigma_layer/ell = {sp.sstr(exprs.width_limit_warning)}")
    print()
    print("If ell -> 0 while sigma_layer remains finite, the smooth layer behaves like a shell ledger.")

    with out.derived_results():
        out.line(
            "transition layer scalar flux witness stated",
            StatusMark.PASS,
            f"F = {sp.sstr(exprs.scalar_flux_layer)}",
        )
        out.line(
            "transition layer A-tail mass-shift witness stated",
            StatusMark.PASS,
            f"delta_M_A = {sp.sstr(exprs.A_mass_shift_layer)}",
        )
        out.line(
            "transition layer current-flux witness stated",
            StatusMark.PASS,
            f"Phi = {sp.sstr(exprs.current_flux_layer)}",
        )
        out.line(
            "transition layer residual ledger stated",
            StatusMark.PASS,
            f"residual = {sp.sstr(exprs.layer_load_residual)}",
        )


def case_2_condition_ledger(conditions: List[TransitionLayerCondition], out: ScriptOutput) -> None:
    header("Case 2: Transition layer neutrality condition ledger")
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
            "transition layer neutrality conditions populated",
            StatusMark.OBLIGATION,
            f"{len(conditions)} transition layer conditions remain required",
        )


def case_3_branch_ledger(branches: List[TransitionLayerBranch], out: ScriptOutput) -> None:
    header("Case 3: Transition layer branch ledger")
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
            "transition layer branch ledger populated",
            StatusMark.PASS,
            f"{len(branches)} transition layer branches classified",
        )


def case_4_rejected_routes(routes: List[RejectedTransitionRoute], out: ScriptOutput) -> None:
    header("Case 4: Rejected transition-layer routes")
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
            "transition-layer false routes rejected",
            StatusMark.FAIL,
            "smoothness, hidden shell load, recovery tuning, coefficient repair, source reroute, and repair patches remain rejected",
        )


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("The transition layer audit fails if a later script allows:")
    print()
    print("1. smoothness to replace no-shell proof")
    print("2. finite-width layer to hide shell/source load")
    print("3. transition width chosen from recovery")
    print("4. transition coefficient chosen to cancel C_ext, q_A_tail, or I_nonA")
    print("5. transition layer to reroute ordinary rho/T")
    print("6. layer to induce q/r A-tail")
    print("7. layer to leave C/r scalar tail")
    print("8. layer to export I/(4*pi*r^2) current flux")
    print("9. O, H, dark, exchange, curvature, or current role to supply missing layer law")
    print("10. parent equation opened from transition-layer diagnostics alone")

    with out.governance_assessments():
        out.line(
            "transition layer overclaim controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not confuse smooth layers with derived neutral support",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("A smooth transition layer is safe only if:")
    print()
    print("  C_layer = 0")
    print("  q_layer = 0")
    print("  I_layer = 0")
    print("  sigma_layer = 0")
    print("  alpha_recovery = 0")
    print("  source_load = 0")
    print("  layer origin is structural")
    print()
    print("This script does not derive a transition-layer theorem.")
    print("It records the mass/flux/source/recovery burden for transition layers.")
    print()
    print("Possible next script:")
    print("  candidate_boundary_parameter_independence.py")
    print()
    print("Tiny goblin label:")
    print("  Smooth paint can hide a purse. Count the layer coins.")

    with out.governance_assessments():
        out.line(
            "transition layer mass/flux audit complete",
            StatusMark.PASS,
            "smoothness is not enough; transition layer neutrality remains theorem-targeted",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, exprs: TransitionLayerDiagnostic) -> None:
    ns.record_derivation(
        derivation_id="transition_layer_scalar_flux_23",
        inputs=[exprs.C_layer],
        output=exprs.scalar_flux_layer,
        method="F_layer = -4*pi*C_layer",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="transition_scalar_flux_witness",
        scope="Group 23 transition layer mass/flux audit",
    )

    ns.record_derivation(
        derivation_id="transition_layer_A_tail_shift_23",
        inputs=[exprs.q_layer],
        output=exprs.A_mass_shift_layer,
        method="delta_M_A = -c**2*q_layer/(2*G)",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="transition_A_tail_mass_shift_witness",
        scope="Group 23 transition layer mass/flux audit",
    )

    ns.record_derivation(
        derivation_id="transition_layer_current_flux_23",
        inputs=[exprs.I_layer],
        output=exprs.current_flux_layer,
        method="Phi_layer = I_layer",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="transition_current_flux_witness",
        scope="Group 23 transition layer mass/flux audit",
    )

    ns.record_derivation(
        derivation_id="transition_layer_mass_flux_marker_23",
        inputs=[
            exprs.C_layer,
            exprs.q_layer,
            exprs.I_layer,
            exprs.sigma_layer,
            exprs.alpha_recovery,
            exprs.source_load,
        ],
        output=sp.Symbol("transition_layer_mass_flux_conditions_stated"),
        method="Group 23 transition layer mass/flux requirements ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="requirements_marker",
        scope="Group 23 smooth support and matching laws",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g23_derive_zero_layer_flux", "Derive zero layer scalar/current flux"),
        ("g23_derive_no_layer_A_tail", "Derive no layer A-tail"),
        ("g23_derive_no_layer_shell_load", "Derive no layer shell/source load"),
        ("g23_derive_recovery_independent_layer", "Derive recovery-independent transition layer"),
        ("g23_derive_source_compatible_layer", "Derive source-compatible transition layer"),
        ("g23_derive_structural_layer_origin", "Derive structural transition layer origin"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g23_transition_layer_route"],
            description=(
                "Transition layer neutrality remains theorem-targeted until zero flux, no A-tail, no hidden shell/source load, "
                "recovery independence, source compatibility, and structural origin are derived."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g23_derive_zero_layer_flux",
        "g23_derive_no_layer_A_tail",
        "g23_derive_no_layer_shell_load",
        "g23_derive_recovery_independent_layer",
        "g23_derive_source_compatible_layer",
        "g23_derive_structural_layer_origin",
    ]

    ns.record_route(RouteRecord(
        route_id="g23_transition_layer_route",
        script_id=SCRIPT_ID,
        name="Group 23 transition layer neutrality theorem target",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "transition layer has zero scalar and current flux",
            "transition layer induces no A-tail mass shift",
            "transition layer carries no hidden shell/source load",
            "transition layer is recovery-independent",
            "transition layer is source-compatible",
            "transition layer origin is structural",
        ],
    ))

    for branch_id in [
        "smoothness_as_neutrality",
        "finite_width_shell_disguise",
        "recovery_tuned_transition",
        "transition_scalar_A_tail_repair",
        "transition_source_reroute",
        "repair_object_layer_patch",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_23",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; smooth transition layers cannot replace derived neutral support.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g23_transition_layer_smooth_not_neutral",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Smooth transition layers are not neutral by smoothness. They must have zero scalar/current flux, no A-tail shift, "
            "no hidden shell/source load, recovery independence, source compatibility, and structural origin."
        ),
        derivation_ids=[
            "transition_layer_scalar_flux_23",
            "transition_layer_A_tail_shift_23",
            "transition_layer_current_flux_23",
            "transition_layer_mass_flux_marker_23",
        ],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Transition Layer Mass Flux Audit")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    diagnostics = build_diagnostics()
    conditions = build_conditions()
    branches = build_branches()
    routes = build_rejected_routes()

    case_0_problem_statement(out)
    case_1_diagnostics(diagnostics, out)
    case_2_condition_ledger(conditions, out)
    case_3_branch_ledger(branches, out)
    case_4_rejected_routes(routes, out)
    case_5_failure_controls(out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, diagnostics)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
