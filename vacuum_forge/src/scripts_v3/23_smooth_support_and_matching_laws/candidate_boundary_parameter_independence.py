# Candidate boundary parameter independence
#
# Group:
#   23_smooth_support_and_matching_laws
#
# Script type:
#   REQUIREMENTS / DIAGNOSTIC
#
# Purpose
# -------
# Audit whether support, smoothing, layer, and boundary parameters are
# independent of recovery targets.
#
# Locked-door question:
#
#   Are support and smoothing parameters independent of recovery targets?
#
# This script does not derive recovery independence.
# It does not prove compact support.
# It does not prove no-shell matching.
# It does not prove boundary neutrality or scalar silence.
#
# It records forbidden dependencies:
#
#   support radius chosen to recover Schwarzschild,
#   smoothing width chosen to recover PPN gamma_like,
#   coefficient chosen to enforce AB=1,
#   boundary residual status chosen to pass recovery,
#   transition profile chosen to suppress a visible tail.

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
            "matching_ladder_dep_23",
            "23_smooth_support_and_matching_laws__candidate_matching_regularization_ladder",
            "matching_regularization_ladder_marker_23",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "compact_support_dep_23",
            "23_smooth_support_and_matching_laws__candidate_compact_support_admissibility_conditions",
            "compact_support_admissibility_marker_23",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "transition_layer_dep_23",
            "23_smooth_support_and_matching_laws__candidate_transition_layer_mass_flux_audit",
            "transition_layer_mass_flux_marker_23",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g22_summary_dep_23",
            "22_boundary_neutrality_and_scalar_silence__candidate_group_22_boundary_neutrality_status_summary",
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
class BoundaryParameterLedger:
    R_support: sp.Symbol
    ell_smooth: sp.Symbol
    alpha_AB: sp.Symbol
    beta_gamma: sp.Symbol
    chi_tail: sp.Symbol
    eta_boundary: sp.Symbol
    recovery_dependency_load: sp.Expr


@dataclass
class ParameterIndependenceCondition:
    name: str
    parameter: str
    forbidden_dependency: str
    status: str
    required_status: str
    consequence: str


@dataclass
class RecoveryTuningBranch:
    name: str
    branch: str
    status: str
    allowed_if: str
    rejected_if: str


@dataclass
class RejectedParameterRoute:
    name: str
    route: str
    forbidden_use: str
    status: str
    consequence: str


# =============================================================================
# Builders
# =============================================================================


def build_parameter_ledger() -> BoundaryParameterLedger:
    R_support, ell_smooth, alpha_AB, beta_gamma, chi_tail, eta_boundary = sp.symbols(
        "R_support ell_smooth alpha_AB beta_gamma chi_tail eta_boundary",
        real=True,
    )

    recovery_dependency_load = sp.simplify(
        R_support + ell_smooth + alpha_AB + beta_gamma + chi_tail + eta_boundary
    )

    return BoundaryParameterLedger(
        R_support=R_support,
        ell_smooth=ell_smooth,
        alpha_AB=alpha_AB,
        beta_gamma=beta_gamma,
        chi_tail=chi_tail,
        eta_boundary=eta_boundary,
        recovery_dependency_load=recovery_dependency_load,
    )


def build_conditions() -> List[ParameterIndependenceCondition]:
    return [
        ParameterIndependenceCondition(
            name="P1: support radius independence",
            parameter="R_support",
            forbidden_dependency="chosen to recover Schwarzschild exterior, PPN behavior, gamma_like, AB, or B=1/A",
            status="REQUIRED",
            required_status="structural/source-derived before recovery",
            consequence="support radius cannot be recovery fit parameter",
        ),
        ParameterIndependenceCondition(
            name="P2: smoothing width independence",
            parameter="ell_smooth",
            forbidden_dependency="chosen to smooth away shell/source/boundary failure or pass recovery",
            status="REQUIRED",
            required_status="derived from support/matching law or left theorem-targeted",
            consequence="smoothing width cannot be repair knob",
        ),
        ParameterIndependenceCondition(
            name="P3: AB coefficient independence",
            parameter="alpha_AB",
            forbidden_dependency="chosen to enforce AB=1, B=1/A, or Schwarzschild product recovery",
            status="REQUIRED",
            required_status="structural if present, otherwise diagnostic/theorem-targeted",
            consequence="metric product recovery cannot construct boundary law",
        ),
        ParameterIndependenceCondition(
            name="P4: gamma-like coefficient independence",
            parameter="beta_gamma",
            forbidden_dependency="chosen to make gamma_like or PPN response acceptable",
            status="REQUIRED",
            required_status="audited only after support/matching law is fixed",
            consequence="PPN/recovery may test but not select smoothing",
        ),
        ParameterIndependenceCondition(
            name="P5: residual tail status independence",
            parameter="chi_tail",
            forbidden_dependency="chosen to set C_ext=0 or suppress visible tail only after recovery/scalar failure",
            status="REQUIRED",
            required_status="residual status structural, killed, inert, or theorem-targeted before recovery",
            consequence="tail silence cannot be recovery-selected",
        ),
        ParameterIndependenceCondition(
            name="P6: boundary condition independence",
            parameter="eta_boundary",
            forbidden_dependency="chosen to cancel q_A_tail, I_nonA, shell load, or source mismatch",
            status="REQUIRED",
            required_status="boundary condition derived before leakage audit",
            consequence="boundary data cannot be repair data",
        ),
    ]


def build_branches() -> List[RecoveryTuningBranch]:
    return [
        RecoveryTuningBranch(
            name="B1: recovery-selected support",
            branch="R_support chosen from Schwarzschild/PPN/AB target",
            status="REJECTED",
            allowed_if="never as construction rule",
            rejected_if="used to claim support or boundary neutrality",
        ),
        RecoveryTuningBranch(
            name="B2: recovery-selected smoothing",
            branch="ell_smooth chosen to pass gamma_like/PPN/recovery",
            status="REJECTED",
            allowed_if="never as construction rule",
            rejected_if="used to hide shell/source/tail failure",
        ),
        RecoveryTuningBranch(
            name="B3: structural parameter",
            branch="parameter fixed by source/support/matching law before recovery",
            status="THEOREM_TARGET",
            allowed_if="law is derived and then recovery is audited downstream",
            rejected_if="law is inferred from desired recovery behavior",
        ),
        RecoveryTuningBranch(
            name="B4: diagnostic recovery audit",
            branch="recovery test applied after support/matching choices are fixed",
            status="SAFE_IF",
            allowed_if="test does not select or retune boundary/support/layer data",
            rejected_if="test feeds back into parameter choice",
        ),
    ]


def build_rejected_routes() -> List[RejectedParameterRoute]:
    return [
        RejectedParameterRoute(
            name="R1: Schwarzschild-selected support",
            route="schwarzschild_selected_support",
            forbidden_use="support radius chosen because Schwarzschild mass/recovery works there",
            status="REJECTED",
            consequence="support must precede recovery",
        ),
        RejectedParameterRoute(
            name="R2: PPN-selected smoothing",
            route="ppn_selected_smoothing",
            forbidden_use="smoothing width/profile chosen to make gamma_like or PPN response acceptable",
            status="REJECTED",
            consequence="PPN cannot construct support law",
        ),
        RejectedParameterRoute(
            name="R3: AB-product tuning",
            route="AB_product_tuning",
            forbidden_use="coefficient chosen to enforce AB=1 or B=1/A",
            status="REJECTED",
            consequence="metric product recovery is downstream audit only",
        ),
        RejectedParameterRoute(
            name="R4: tail-suppression tuning",
            route="tail_suppression_tuning",
            forbidden_use="coefficient chosen to set C_ext=0 after scalar failure appears",
            status="REJECTED",
            consequence="scalar silence cannot be tuned from recovery",
        ),
        RejectedParameterRoute(
            name="R5: boundary-load tuning",
            route="boundary_load_tuning",
            forbidden_use="boundary parameter chosen to cancel q_A_tail, I_nonA, shell load, or source mismatch",
            status="REJECTED",
            consequence="boundary data cannot be repair data",
        ),
        RejectedParameterRoute(
            name="R6: parent-fit parameter",
            route="parent_fit_parameter",
            forbidden_use="parameter chosen so a parent-looking equation closes",
            status="REJECTED",
            consequence="parent closure cannot choose support parameters",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Boundary parameter independence problem")
    print("Question:")
    print()
    print("  Are support and smoothing parameters independent of recovery targets?")
    print()
    print("Reference discipline:")
    print()
    print("  Compact support and transition layers must be structural, not recovery-selected.")
    print("  Recovery may audit after boundary/support/layer data are fixed.")
    print("  This script records forbidden parameter dependencies.")
    print("  It does not derive recovery independence.")

    with out.governance_assessments():
        out.line(
            "boundary parameter independence audit opened",
            StatusMark.INFO,
            "auditing whether support/smoothing/layer parameters are selected from recovery targets",
        )


def case_1_parameter_ledger(ledger: BoundaryParameterLedger, out: ScriptOutput) -> None:
    header("Case 1: Boundary/recovery parameter ledger")
    print("Representative boundary/support parameters:")
    print()
    print(f"  R_support = {sp.sstr(ledger.R_support)}")
    print(f"  ell_smooth = {sp.sstr(ledger.ell_smooth)}")
    print(f"  alpha_AB = {sp.sstr(ledger.alpha_AB)}")
    print(f"  beta_gamma = {sp.sstr(ledger.beta_gamma)}")
    print(f"  chi_tail = {sp.sstr(ledger.chi_tail)}")
    print(f"  eta_boundary = {sp.sstr(ledger.eta_boundary)}")
    print()
    print("Recovery-dependency load ledger:")
    print()
    print(f"  load = {sp.sstr(ledger.recovery_dependency_load)}")
    print()
    print("For recovery independence, none of these may be chosen from downstream recovery needs.")

    with out.derived_results():
        out.line(
            "boundary parameter dependency ledger stated",
            StatusMark.PASS,
            f"load = {sp.sstr(ledger.recovery_dependency_load)}",
        )


def case_2_condition_ledger(conditions: List[ParameterIndependenceCondition], out: ScriptOutput) -> None:
    header("Case 2: Parameter independence condition ledger")
    for condition in conditions:
        print()
        print("-" * 120)
        print(condition.name)
        print("-" * 120)
        print(f"Parameter: {condition.parameter}")
        print(f"Forbidden dependency: {condition.forbidden_dependency}")
        print(f"[{status_mark(condition.status).value}] {condition.name}: {condition.status}")
        print(f"Required status: {condition.required_status}")
        print(f"Consequence: {condition.consequence}")

    with out.unresolved_obligations():
        out.line(
            "parameter independence conditions populated",
            StatusMark.OBLIGATION,
            f"{len(conditions)} recovery-independence conditions remain required",
        )


def case_3_branch_ledger(branches: List[RecoveryTuningBranch], out: ScriptOutput) -> None:
    header("Case 3: Recovery-tuning branch ledger")
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
            "recovery-tuning branch ledger populated",
            StatusMark.PASS,
            f"{len(branches)} parameter-selection branches classified",
        )


def case_4_rejected_routes(routes: List[RejectedParameterRoute], out: ScriptOutput) -> None:
    header("Case 4: Rejected parameter-selection routes")
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
            "recovery-selected parameter routes rejected",
            StatusMark.FAIL,
            "Schwarzschild, PPN, AB, tail suppression, boundary-load, and parent-fit tuning remain rejected",
        )


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("The boundary parameter independence audit fails if a later script allows:")
    print()
    print("1. support radius chosen from Schwarzschild recovery")
    print("2. smoothing width chosen from PPN/gamma_like recovery")
    print("3. coefficient chosen to enforce AB=1 or B=1/A")
    print("4. residual status chosen to suppress visible tail after failure")
    print("5. boundary parameter chosen to cancel q_A_tail")
    print("6. boundary parameter chosen to cancel I_nonA")
    print("7. boundary parameter chosen to cancel shell/source load")
    print("8. ordinary source rerouted into support/layer parameter")
    print("9. parent closure used to fit boundary/support data")
    print("10. recovery audit feeds back into construction")

    with out.governance_assessments():
        out.line(
            "boundary parameter overclaim controls stated",
            StatusMark.OBLIGATION,
            "future scripts must keep recovery downstream of support/matching construction",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Boundary/support/layer parameters must be fixed before recovery tests.")
    print()
    print("Rejected construction routes:")
    print()
    print("  support radius from Schwarzschild")
    print("  smoothing width from PPN/gamma_like")
    print("  coefficient from AB=1 or B=1/A")
    print("  residual status from scalar-tail failure")
    print("  boundary parameter from A-tail/current/shell/source cancellation")
    print("  parent-fit parameter tuning")
    print()
    print("Allowed only as downstream audit:")
    print()
    print("  recovery tests after support/matching/layer data are fixed")
    print()
    print("Possible next script:")
    print("  candidate_matching_law_source_compatibility.py")
    print()
    print("Tiny goblin label:")
    print("  Recovery is a mirror, not a chisel.")

    with out.governance_assessments():
        out.line(
            "boundary parameter independence audit complete",
            StatusMark.PASS,
            "recovery-selected support/smoothing/boundary parameters remain rejected",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, ledger: BoundaryParameterLedger) -> None:
    ns.record_derivation(
        derivation_id="boundary_parameter_dependency_ledger_23",
        inputs=[
            ledger.R_support,
            ledger.ell_smooth,
            ledger.alpha_AB,
            ledger.beta_gamma,
            ledger.chi_tail,
            ledger.eta_boundary,
        ],
        output=ledger.recovery_dependency_load,
        method="sum representative forbidden recovery-dependent boundary/support parameters",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="parameter_dependency_ledger",
        scope="Group 23 boundary parameter independence",
    )

    ns.record_derivation(
        derivation_id="boundary_parameter_independence_marker_23",
        inputs=[
            sp.Symbol("support_radius"),
            sp.Symbol("smoothing_width"),
            sp.Symbol("AB_coefficient"),
            sp.Symbol("gamma_coefficient"),
            sp.Symbol("tail_status"),
            sp.Symbol("boundary_data"),
        ],
        output=sp.Symbol("boundary_parameter_independence_conditions_stated"),
        method="Group 23 boundary parameter independence ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="requirements_marker",
        scope="Group 23 smooth support and matching laws",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g23_derive_support_param_origin", "Derive support parameter origin"),
        ("g23_derive_smoothing_param_origin", "Derive smoothing parameter origin"),
        ("g23_derive_recovery_downstream", "Derive recovery as downstream audit"),
        ("g23_derive_no_tail_tuning", "Derive no scalar-tail tuning"),
        ("g23_derive_no_boundary_load_tuning", "Derive no boundary-load tuning"),
        ("g23_derive_no_parent_fit_tuning", "Derive no parent-fit tuning"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g23_param_independence_route"],
            description=(
                "Boundary/support/layer parameters must be structural and fixed before recovery; "
                "recovery may audit but may not construct support, smoothing, residual status, or boundary data."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g23_derive_support_param_origin",
        "g23_derive_smoothing_param_origin",
        "g23_derive_recovery_downstream",
        "g23_derive_no_tail_tuning",
        "g23_derive_no_boundary_load_tuning",
        "g23_derive_no_parent_fit_tuning",
    ]

    ns.record_route(RouteRecord(
        route_id="g23_param_independence_route",
        script_id=SCRIPT_ID,
        name="Group 23 boundary parameter independence theorem target",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "support parameters have structural/source origin",
            "smoothing/layer parameters have structural origin",
            "recovery is downstream audit only",
            "tail/boundary/current/source coefficients are not tuned after failure",
            "parent closure is not used to fit boundary/support data",
        ],
    ))

    for branch_id in [
        "schwarzschild_selected_support",
        "ppn_selected_smoothing",
        "AB_product_tuning",
        "tail_suppression_tuning",
        "boundary_load_tuning",
        "parent_fit_parameter",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_23",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; recovery and parent-fit targets cannot select boundary/support parameters.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g23_recovery_not_boundary_chisel",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Boundary/support/layer parameters must be fixed structurally before recovery tests. "
            "Schwarzschild, PPN, AB, scalar-tail, boundary-load, and parent-fit targets may audit but may not construct them."
        ),
        derivation_ids=[
            "boundary_parameter_dependency_ledger_23",
            "boundary_parameter_independence_marker_23",
        ],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Boundary Parameter Independence")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    ledger = build_parameter_ledger()
    conditions = build_conditions()
    branches = build_branches()
    routes = build_rejected_routes()

    case_0_problem_statement(out)
    case_1_parameter_ledger(ledger, out)
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
