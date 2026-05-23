# Candidate residual kill recovery independence
#
# Group:
#   25_residual_kill_or_no_overlap_theorem
#
# Script type:
#   REQUIREMENTS / DIAGNOSTIC
#
# Purpose
# -------
# Ensure residual-kill / inertness / no-overlap status is not selected from
# recovery outcomes.
#
# Locked-door question:
#
#   Is residual-kill / inertness independent of recovery targets?
#
# This script does not derive residual kill.
# It does not derive non-metric inertness.
# It does not derive active no-overlap O.
# It does not derive B_s/F_zeta insertion.
# It does not prove recovery.
# It does not open parent equation closure.
#
# It records that recovery may audit residual status only after it is derived.
# Recovery may not select residual status.

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
            "O_burden_dep_25",
            "025_residual_kill_or_no_overlap_theorem__candidate_no_overlap_operator_minimum_burden",
            "no_overlap_operator_minimum_burden_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g24_recovery_dep_25",
            "024_metric_insertion_recovery_retest__candidate_recovery_target_anti_smuggling_audit",
            "recovery_target_anti_smuggling_marker_24",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g24_gamma_AB_dep_25",
            "024_metric_insertion_recovery_retest__candidate_gamma_AB_recovery_diagnostics",
            "gamma_AB_recovery_diagnostics_marker_24",
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
class RecoveryDependenceLedger:
    schwarzschild: sp.Symbol
    AB_one: sp.Symbol
    B_inverse_A: sp.Symbol
    gamma_like: sp.Symbol
    PPN_like: sp.Symbol
    areal_kappa_zero: sp.Symbol
    scalar_tail_failure: sp.Symbol
    boundary_load_cancellation: sp.Symbol
    source_compat_failure: sp.Symbol
    parent_fit_closure: sp.Symbol
    recovery_selection_load: sp.Expr


@dataclass
class RejectedRecoveryDependency:
    name: str
    dependency: str
    status: str
    forbidden_use: str
    consequence: str


@dataclass
class RecoveryIndependenceRule:
    name: str
    rule: str
    status: str
    failure_if: str


@dataclass
class RecoveryIndependenceBranch:
    name: str
    branch: str
    status: str
    allowed_if: str
    rejected_if: str


def build_ledger() -> RecoveryDependenceLedger:
    (
        schwarzschild,
        AB_one,
        B_inverse_A,
        gamma_like,
        PPN_like,
        areal_kappa_zero,
        scalar_tail_failure,
        boundary_load_cancellation,
        source_compat_failure,
        parent_fit_closure,
    ) = sp.symbols(
        "schwarzschild AB_one B_inverse_A gamma_like PPN_like areal_kappa_zero scalar_tail_failure boundary_load_cancellation source_compat_failure parent_fit_closure",
        real=True,
    )

    recovery_selection_load = sp.simplify(
        schwarzschild
        + AB_one
        + B_inverse_A
        + gamma_like
        + PPN_like
        + areal_kappa_zero
        + scalar_tail_failure
        + boundary_load_cancellation
        + source_compat_failure
        + parent_fit_closure
    )

    return RecoveryDependenceLedger(
        schwarzschild=schwarzschild,
        AB_one=AB_one,
        B_inverse_A=B_inverse_A,
        gamma_like=gamma_like,
        PPN_like=PPN_like,
        areal_kappa_zero=areal_kappa_zero,
        scalar_tail_failure=scalar_tail_failure,
        boundary_load_cancellation=boundary_load_cancellation,
        source_compat_failure=source_compat_failure,
        parent_fit_closure=parent_fit_closure,
        recovery_selection_load=recovery_selection_load,
    )


def build_rejected_dependencies() -> List[RejectedRecoveryDependency]:
    return [
        RejectedRecoveryDependency(
            name="D1: Schwarzschild-selected residual status",
            dependency="Schwarzschild exterior",
            status="REJECTED",
            forbidden_use="residual kill, inertness, or O chosen to make Schwarzschild recovery pass",
            consequence="recovery constructs residual control",
        ),
        RejectedRecoveryDependency(
            name="D2: AB=1-selected residual status",
            dependency="AB = 1",
            status="REJECTED",
            forbidden_use="residual status chosen to enforce AB=1",
            consequence="AB diagnostic becomes construction",
        ),
        RejectedRecoveryDependency(
            name="D3: B=1/A-selected residual status",
            dependency="B = 1/A",
            status="REJECTED",
            forbidden_use="residual status chosen to preserve B=1/A",
            consequence="static exterior diagnostic becomes construction rule",
        ),
        RejectedRecoveryDependency(
            name="D4: gamma-like-selected residual status",
            dependency="gamma_like / PPN-like response",
            status="REJECTED",
            forbidden_use="residual status chosen to fit gamma_like or PPN behavior",
            consequence="weak-field recovery tunes residual control",
        ),
        RejectedRecoveryDependency(
            name="D5: areal-kappa-selected residual status",
            dependency="kappa_areal = 0",
            status="REJECTED",
            forbidden_use="residual status chosen from areal kappa diagnostic",
            consequence="diagnostic kappa becomes control law",
        ),
        RejectedRecoveryDependency(
            name="D6: scalar-tail-failure-selected residual status",
            dependency="scalar-tail failure",
            status="REJECTED",
            forbidden_use="residual killed or made inert because exterior scalar tail appears",
            consequence="boundary/scalar failure constructs residual status",
        ),
        RejectedRecoveryDependency(
            name="D7: boundary-load-cancellation-selected residual status",
            dependency="boundary-load cancellation",
            status="REJECTED",
            forbidden_use="residual status chosen to cancel boundary/current/A-tail/shell load",
            consequence="residual control becomes boundary repair",
        ),
        RejectedRecoveryDependency(
            name="D8: source-compat-failure-selected residual status",
            dependency="source compatibility failure",
            status="REJECTED",
            forbidden_use="residual status chosen to avoid duplicate source load",
            consequence="residual control becomes source repair",
        ),
        RejectedRecoveryDependency(
            name="D9: parent-fit-selected residual status",
            dependency="parent-fit closure",
            status="REJECTED",
            forbidden_use="residual status chosen to make parent-looking equation close",
            consequence="parent closure constructs residual control",
        ),
    ]


def build_rules() -> List[RecoveryIndependenceRule]:
    return [
        RecoveryIndependenceRule(
            name="R1: residual status before recovery",
            rule="residual kill, inertness, or O status must be fixed by structural law before recovery diagnostics",
            status="REQUIRED",
            failure_if="status is chosen after recovery target is known",
        ),
        RecoveryIndependenceRule(
            name="R2: recovery may audit only",
            rule="Schwarzschild, AB, B=1/A, gamma_like, PPN, and areal kappa may audit derived residual status",
            status="REQUIRED",
            failure_if="recovery target chooses residual status",
        ),
        RecoveryIndependenceRule(
            name="R3: failure may reject, not tune",
            rule="failed recovery may reject or flag a branch but cannot tune residual status",
            status="REQUIRED",
            failure_if="residual kill/inertness/O is changed to pass recovery",
        ),
        RecoveryIndependenceRule(
            name="R4: boundary/source failure may not select status",
            rule="boundary or source failure cannot choose residual kill or inertness",
            status="REQUIRED",
            failure_if="residual status repairs tail, flux, shell, or source duplication",
        ),
        RecoveryIndependenceRule(
            name="R5: parent fit may not select status",
            rule="parent-looking closure cannot select residual status",
            status="REQUIRED",
            failure_if="residual status is picked to make parent equation close",
        ),
    ]


def build_branches() -> List[RecoveryIndependenceBranch]:
    return [
        RecoveryIndependenceBranch(
            name="B1: recovery-independent residual control",
            branch="residual kill/inertness/O status is derived before recovery and then audited",
            status="THEOREM_TARGET",
            allowed_if="status has structural origin and recovery is downstream",
            rejected_if="status depends on any recovery target",
        ),
        RecoveryIndependenceBranch(
            name="B2: diagnostic-only recovery audit",
            branch="recovery diagnostics test an already fixed residual status",
            status="SAFE_IF",
            allowed_if="used only to classify or reject a fixed branch",
            rejected_if="used to tune residual status",
        ),
        RecoveryIndependenceBranch(
            name="B3: recovery-selected residual control",
            branch="residual kill/inertness/O chosen to pass recovery",
            status="REJECTED",
            allowed_if="never",
            rejected_if="Schwarzschild/gamma/AB/B=1/A/PPN/parent-fit selects status",
        ),
        RecoveryIndependenceBranch(
            name="B4: boundary/source-selected residual control",
            branch="residual status chosen to repair boundary/source failure",
            status="REJECTED",
            allowed_if="never",
            rejected_if="tail, flux, shell, A-tail, or source duplication selects status",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Residual-kill recovery-independence problem")
    print("Question:")
    print()
    print("  Is residual-kill / inertness independent of recovery targets?")
    print()
    print("Reference discipline:")
    print()
    print("  Recovery may audit residual status only after it is derived.")
    print("  Recovery may not select residual kill, inertness, or active O.")
    print("  Boundary/source failure and parent-fit closure also may not select residual status.")

    with out.governance_assessments():
        out.line(
            "residual-kill recovery-independence audit opened",
            StatusMark.INFO,
            "testing whether residual status is independent of recovery and repair targets",
        )


def case_1_recovery_dependence_ledger(ledger: RecoveryDependenceLedger, out: ScriptOutput) -> None:
    header("Case 1: Recovery-selection load ledger")
    print("Rejected residual-status dependencies:")
    print()
    for name in [
        "schwarzschild",
        "AB_one",
        "B_inverse_A",
        "gamma_like",
        "PPN_like",
        "areal_kappa_zero",
        "scalar_tail_failure",
        "boundary_load_cancellation",
        "source_compat_failure",
        "parent_fit_closure",
    ]:
        print(f"  {name} = {sp.sstr(getattr(ledger, name))}")
    print()
    print("Recovery-selection load:")
    print()
    print(f"  L_recovery_select = {sp.sstr(ledger.recovery_selection_load)}")
    print()
    print("Interpretation:")
    print()
    print("  All entries must vanish as construction dependencies.")
    print("  Recovery may audit only after residual status is structurally fixed.")

    with out.derived_results():
        out.line(
            "residual recovery-selection load stated",
            StatusMark.OBLIGATION,
            f"L_recovery_select = {sp.sstr(ledger.recovery_selection_load)}",
        )


def case_2_rejected_dependencies(deps: List[RejectedRecoveryDependency], out: ScriptOutput) -> None:
    header("Case 2: Rejected recovery dependencies")
    for dep in deps:
        print()
        print("-" * 120)
        print(dep.name)
        print("-" * 120)
        print(f"Dependency: {dep.dependency}")
        print(f"Forbidden use: {dep.forbidden_use}")
        print(f"[{status_mark(dep.status).value}] {dep.name}: {dep.status}")
        print(f"Consequence: {dep.consequence}")

    with out.counterexamples():
        out.line(
            "recovery-selected residual dependencies rejected",
            StatusMark.FAIL,
            f"{len(deps)} recovery/repair dependencies rejected as residual-status origins",
        )


def case_3_rules(rules: List[RecoveryIndependenceRule], out: ScriptOutput) -> None:
    header("Case 3: Recovery-independence rules")
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
            "recovery-independence rules populated",
            StatusMark.OBLIGATION,
            f"{len(rules)} rules constrain residual status selection",
        )


def case_4_branches(branches: List[RecoveryIndependenceBranch], out: ScriptOutput) -> None:
    header("Case 4: Residual status recovery-independence branches")
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
            "residual recovery-independence branches classified",
            StatusMark.PASS,
            f"{len(branches)} branches classified",
        )


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("The residual-kill recovery-independence audit fails if a later script allows:")
    print()
    print("1. residual status chosen from Schwarzschild recovery")
    print("2. residual status chosen from AB=1")
    print("3. residual status chosen from B=1/A")
    print("4. residual status chosen from gamma_like or PPN response")
    print("5. residual status chosen from areal kappa = 0")
    print("6. residual status chosen from scalar-tail failure")
    print("7. residual status chosen from boundary/current/A-tail/shell cancellation")
    print("8. residual status chosen from source-compatibility failure")
    print("9. residual status chosen from parent-fit closure")
    print("10. recovery success opens insertion or parent gate")

    with out.governance_assessments():
        out.line(
            "residual recovery-independence failure controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not select residual status from recovery or repair targets",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Residual-kill recovery-independence result:")
    print()
    print("  Recovery may audit residual status after it is derived.")
    print("  Recovery may not select residual kill, inertness, or active O.")
    print("  Boundary/source failure may not select residual status.")
    print("  Parent-fit closure may not select residual status.")
    print("  Recovery-independent residual control remains theorem-targeted.")
    print()
    print("Possible next script:")
    print("  candidate_residual_kill_boundary_source_compatibility.py")
    print()
    print("Tiny goblin label:")
    print("  Recovery judges. It does not choose the corpse.")

    with out.governance_assessments():
        out.line(
            "residual-kill recovery-independence audit complete",
            StatusMark.PASS,
            "recovery selection routes rejected; residual control theorem remains open",
        )


def record_derivations(ns, ledger: RecoveryDependenceLedger) -> None:
    ns.record_derivation(
        derivation_id="residual_kill_recovery_selection_load_25",
        inputs=[
            ledger.schwarzschild,
            ledger.AB_one,
            ledger.B_inverse_A,
            ledger.gamma_like,
            ledger.PPN_like,
            ledger.areal_kappa_zero,
            ledger.scalar_tail_failure,
            ledger.boundary_load_cancellation,
            ledger.source_compat_failure,
            ledger.parent_fit_closure,
        ],
        output=ledger.recovery_selection_load,
        method="sum rejected recovery/repair dependencies for residual status selection",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="residual_recovery_independence_ledger",
        scope="Group 25 residual kill or no-overlap theorem",
    )

    ns.record_derivation(
        derivation_id="residual_kill_recovery_independence_marker_25",
        inputs=[
            sp.Symbol("Schwarzschild"),
            sp.Symbol("AB_one"),
            sp.Symbol("B_inverse_A"),
            sp.Symbol("gamma_like"),
            sp.Symbol("PPN_like"),
            sp.Symbol("boundary_failure"),
            sp.Symbol("source_failure"),
            sp.Symbol("parent_fit"),
        ],
        output=sp.Symbol("residual_kill_recovery_independence_stated"),
        method="Group 25 residual-kill recovery-independence audit",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="requirements_marker",
        scope="Group 25 residual kill or no-overlap theorem",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g25_derive_residual_status_structural_origin", "Derive structural origin for residual status"),
        ("g25_derive_no_Schwarzschild_selection", "Derive no Schwarzschild-selected residual status"),
        ("g25_derive_no_AB_BinverseA_selection", "Derive no AB/B=1/A-selected residual status"),
        ("g25_derive_no_gamma_PPN_selection", "Derive no gamma/PPN-selected residual status"),
        ("g25_derive_no_boundary_source_selection", "Derive no boundary/source-selected residual status"),
        ("g25_derive_no_parent_fit_selection", "Derive no parent-fit-selected residual status"),
        ("g25_keep_recovery_audit_only", "Keep recovery audit-only"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g25_residual_recovery_independence_route"],
            description=(
                "Residual status remains theorem-targeted until kill/inertness/O status is derived independently of recovery, boundary/source repair, and parent-fit closure."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g25_derive_residual_status_structural_origin",
        "g25_derive_no_Schwarzschild_selection",
        "g25_derive_no_AB_BinverseA_selection",
        "g25_derive_no_gamma_PPN_selection",
        "g25_derive_no_boundary_source_selection",
        "g25_derive_no_parent_fit_selection",
        "g25_keep_recovery_audit_only",
    ]

    ns.record_route(RouteRecord(
        route_id="g25_residual_recovery_independence_route",
        script_id=SCRIPT_ID,
        name="Group 25 residual-kill recovery-independence route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "residual status has structural origin",
            "Schwarzschild/AB/B=1/A/gamma/PPN/areal-kappa diagnostics do not select residual status",
            "boundary/source failure does not select residual status",
            "parent-fit closure does not select residual status",
            "recovery remains audit-only",
        ],
    ))

    for branch_id in [
        "Schwarzschild_selected_residual_status",
        "AB_selected_residual_status",
        "B_inverse_A_selected_residual_status",
        "gamma_PPN_selected_residual_status",
        "areal_kappa_selected_residual_status",
        "boundary_source_selected_residual_status",
        "parent_fit_selected_residual_status",
        "recovery_success_opens_parent",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_25",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; residual status must be independent of recovery and repair targets.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g25_residual_status_recovery_independent",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Recovery may audit residual kill, inertness, or active-O status only after it is structurally derived. "
            "Schwarzschild, AB=1, B=1/A, gamma_like, PPN, areal kappa, scalar-tail failure, boundary/source repair, "
            "and parent-fit closure may not select residual status."
        ),
        derivation_ids=[
            "residual_kill_recovery_selection_load_25",
            "residual_kill_recovery_independence_marker_25",
        ],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Residual Kill Recovery Independence")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    ledger = build_ledger()
    deps = build_rejected_dependencies()
    rules = build_rules()
    branches = build_branches()

    case_0_problem_statement(out)
    case_1_recovery_dependence_ledger(ledger, out)
    case_2_rejected_dependencies(deps, out)
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
