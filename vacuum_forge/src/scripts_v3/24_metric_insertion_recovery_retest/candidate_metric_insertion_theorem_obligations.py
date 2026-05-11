# Candidate metric insertion theorem obligations
#
# Group:
#   24_metric_insertion_recovery_retest
#
# Script type:
#   OBLIGATION SUMMARY / REQUIREMENTS
#
# Purpose
# -------
# Consolidate the theorem obligations required before claiming B_s/F_zeta
# metric insertion.
#
# Locked-door question:
#
#   What must be proved before claiming B_s/F_zeta insertion?
#
# This script does not derive B_s/F_zeta insertion.
# It does not derive recovery.
# It does not derive count-once recombination.
# It does not derive boundary/support compatibility.
# It does not derive source compatibility.
# It does not open the parent field equation.
#
# It consolidates the Group 24 theorem burden into a closure-ready ledger.

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
            "recovery_antismuggle_dep_24",
            "24_metric_insertion_recovery_retest__candidate_recovery_target_anti_smuggling_audit",
            "recovery_target_anti_smuggling_marker_24",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "count_once_dep_24",
            "24_metric_insertion_recovery_retest__candidate_count_once_metric_trace_audit",
            "count_once_metric_trace_marker_24",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "gamma_AB_dep_24",
            "24_metric_insertion_recovery_retest__candidate_gamma_AB_recovery_diagnostics",
            "gamma_AB_recovery_diagnostics_marker_24",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "boundary_support_dep_24",
            "24_metric_insertion_recovery_retest__candidate_metric_insertion_boundary_support_compatibility",
            "metric_insertion_boundary_support_marker_24",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "source_compat_dep_24",
            "24_metric_insertion_recovery_retest__candidate_metric_insertion_source_compatibility",
            "metric_insertion_source_compatibility_marker_24",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g20_summary_dep_24",
            "20_no_overlap_and_projection_operators__candidate_no_overlap_projection_group_status_summary",
            "no_overlap_projection_group_status_summary_marker",
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
class InsertionTheoremObligation:
    name: str
    theorem_target: str
    required_inputs: str
    status: str
    blocks: str
    failure_if: str


@dataclass
class InsertionClosureGate:
    name: str
    gate: str
    status: str
    opens_if: str
    remains_closed_if: str


@dataclass
class RejectedInsertionUpgrade:
    name: str
    rejected_upgrade: str
    status: str
    reason: str


# =============================================================================
# Builders
# =============================================================================


def build_obligations() -> List[InsertionTheoremObligation]:
    return [
        InsertionTheoremObligation(
            name="O1: F_zeta insertion law",
            theorem_target="derive B_s = F_zeta[A, zeta, J_V, Sigma_V, R_V] or a replacement law",
            required_inputs="structural map from volume/spatial response objects to scalar spatial metric response",
            status="REQUIRED",
            blocks="metric insertion claim",
            failure_if="B_s is copied from GR, B=1/A, AB=1, or gamma-like recovery",
        ),
        InsertionTheoremObligation(
            name="O2: coefficient origin",
            theorem_target="derive insertion coefficients before recovery",
            required_inputs="coefficient law independent of Schwarzschild, AB, B=1/A, gamma_like, PPN, support, or parent-fit tuning",
            status="REQUIRED",
            blocks="recovery anti-smuggling",
            failure_if="coefficients are chosen from diagnostics",
        ),
        InsertionTheoremObligation(
            name="O3: count-once recombination",
            theorem_target="derive scalar spatial trace counted exactly once",
            required_inputs="zeta enters B_s only once; residual zeta/kappa metric trace killed, inert, or projected by derived operator",
            status="REQUIRED",
            blocks="ordinary metric recombination",
            failure_if="zeta/kappa residual metric trace survives or re-enters",
        ),
        InsertionTheoremObligation(
            name="O4: residual-kill or no-overlap",
            theorem_target="derive residual-kill, non-metric inertness, or active no-overlap O",
            required_inputs="operator/domain/kernel/image/divergence/boundary/source law if O is used",
            status="REQUIRED",
            blocks="overlap control",
            failure_if="O erases overlap by name or residual status chosen from recovery",
        ),
        InsertionTheoremObligation(
            name="O5: gamma / AB recovery independence",
            theorem_target="derive recovery behavior without diagnostic tuning",
            required_inputs="fixed candidate passes or fails gamma/AB/B=1/A/kappa_areal diagnostics without coefficient retuning",
            status="REQUIRED",
            blocks="recovery classification",
            failure_if="gamma, AB, B=1/A, or kappa diagnostics construct the branch",
        ),
        InsertionTheoremObligation(
            name="O6: boundary / scalar silence compatibility",
            theorem_target="derive no scalar tail, no current flux, no A-tail, and no boundary shell under insertion",
            required_inputs="C_ext=0, I_nonA=0, q_A_tail=0, sigma_shell=0 or derived equivalent",
            status="REQUIRED",
            blocks="boundary/scalar compatibility",
            failure_if="insertion leaves exterior tail, current flux, A-tail, or shell source",
        ),
        InsertionTheoremObligation(
            name="O7: smooth support / matching compatibility",
            theorem_target="derive insertion seam support/matching law",
            required_inputs="structural support origin, value/slope matching, transition neutrality, recovery-independent seam data",
            status="REQUIRED",
            blocks="support/matching compatibility",
            failure_if="toy support, smoothness, or recovery-selected seam is used",
        ),
        InsertionTheoremObligation(
            name="O8: source compatibility",
            theorem_target="derive no ordinary source duplication under insertion",
            required_inputs="rho/M_enc remains A-routed; zero duplicate loads in coefficients, residuals, seam parameters, repair labels, and cancellation ledgers",
            status="REQUIRED",
            blocks="source no-double-counting",
            failure_if="ordinary source load hides in metric insertion or seam pockets",
        ),
        InsertionTheoremObligation(
            name="O9: no repair insertion",
            theorem_target="derive insertion without O-by-name, H, dark, exchange, curvature, current, or source repair patches",
            required_inputs="no repair object supplies missing insertion, boundary, support, source, or recovery law",
            status="REQUIRED",
            blocks="honest insertion closure",
            failure_if="repair object supplies missing metric branch",
        ),
    ]


def build_gates() -> List[InsertionClosureGate]:
    return [
        InsertionClosureGate(
            name="G1: B_s/F_zeta insertion gate",
            gate="metric insertion theorem",
            status="NOT_READY",
            opens_if="F_zeta law, coefficient origin, count-once recombination, boundary/support compatibility, source compatibility, and no-repair insertion are derived",
            remains_closed_if="Group 24 only states diagnostics and obligations",
        ),
        InsertionClosureGate(
            name="G2: gamma-like recovery gate",
            gate="gamma-like / PPN-like recovery",
            status="NOT_READY",
            opens_if="fixed insertion candidate produces recovery behavior without diagnostic tuning",
            remains_closed_if="gamma_s or equivalent coefficient is chosen from desired recovery",
        ),
        InsertionClosureGate(
            name="G3: AB / B=1/A gate",
            gate="AB and static exterior spatial recovery",
            status="NOT_READY",
            opens_if="fixed insertion candidate passes AB/B=1/A diagnostics without using them as construction rules",
            remains_closed_if="AB=1 or B=1/A constructs B_s",
        ),
        InsertionClosureGate(
            name="G4: no-overlap / residual gate",
            gate="count-once residual control",
            status="NOT_READY",
            opens_if="residual-kill, non-metric inertness, or active no-overlap operator is derived",
            remains_closed_if="residual status is assumed or recovery-selected",
        ),
        InsertionClosureGate(
            name="G5: boundary/support/source gate",
            gate="compatibility with Groups 21-23",
            status="NOT_READY",
            opens_if="all boundary, support, transition, recovery-independent seam, and source no-double-counting obligations are derived",
            remains_closed_if="metric insertion uses seam/source shortcuts",
        ),
        InsertionClosureGate(
            name="G6: parent equation gate",
            gate="parent field equation",
            status="NOT_READY",
            opens_if="metric insertion plus source, boundary, support, no-overlap, divergence, and recombination theorems are derived",
            remains_closed_if="recovery retest diagnostics are used as parent closure",
        ),
    ]


def build_rejected_upgrades() -> List[RejectedInsertionUpgrade]:
    return [
        RejectedInsertionUpgrade(
            name="U1: retest ledger becomes insertion theorem",
            rejected_upgrade="treating Group 24 retest inventory as B_s/F_zeta construction",
            status="REJECTED",
            reason="inventory and guardrails are not an insertion law",
        ),
        RejectedInsertionUpgrade(
            name="U2: recovery diagnostics become construction",
            rejected_upgrade="using Schwarzschild, gamma, AB, B=1/A, or kappa diagnostics to build B_s",
            status="REJECTED",
            reason="recovery may audit but not forge the branch",
        ),
        RejectedInsertionUpgrade(
            name="U3: count-once convention becomes no-overlap theorem",
            rejected_upgrade="treating residual-kill or nonmetric convention as derived O",
            status="REJECTED",
            reason="active no-overlap operator remains theorem-targeted",
        ),
        RejectedInsertionUpgrade(
            name="U4: boundary/support audit licenses insertion",
            rejected_upgrade="claiming insertion while boundary/support loads remain obligations",
            status="REJECTED",
            reason="compatibility audit does not derive boundary/scalar/support silence",
        ),
        RejectedInsertionUpgrade(
            name="U5: source audit licenses insertion",
            rejected_upgrade="claiming insertion while source duplicate loads remain obligations",
            status="REJECTED",
            reason="source no-double-counting remains theorem-targeted",
        ),
        RejectedInsertionUpgrade(
            name="U6: Group 24 opens parent gate",
            rejected_upgrade="opening parent equation from metric insertion recovery retest",
            status="REJECTED",
            reason="parent closure requires derived insertion, source, boundary, support, no-overlap, divergence, and recombination theorems",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Metric insertion theorem obligations problem")
    print("Question:")
    print()
    print("  What must be proved before claiming B_s/F_zeta insertion?")
    print()
    print("Reference discipline:")
    print()
    print("  Group 24 has audited retest objects, recovery anti-smuggling, count-once trace, gamma/AB diagnostics, boundary/support compatibility, and source compatibility.")
    print("  This script consolidates the theorem burden.")
    print("  It does not prove metric insertion.")

    with out.governance_assessments():
        out.line(
            "metric insertion theorem obligation audit opened",
            StatusMark.INFO,
            "consolidating Group 24 theorem burdens without upgrading them to proof",
        )


def case_1_obligation_ledger(entries: List[InsertionTheoremObligation], out: ScriptOutput) -> None:
    header("Case 1: Metric insertion theorem obligation ledger")
    for entry in entries:
        print()
        print("-" * 120)
        print(entry.name)
        print("-" * 120)
        print(f"Theorem target: {entry.theorem_target}")
        print(f"Required inputs: {entry.required_inputs}")
        print(f"[{status_mark(entry.status).value}] {entry.name}: {entry.status}")
        print(f"Blocks: {entry.blocks}")
        print(f"Failure if: {entry.failure_if}")

    with out.unresolved_obligations():
        out.line(
            "metric insertion theorem obligations consolidated",
            StatusMark.OBLIGATION,
            f"{len(entries)} insertion theorem obligations remain open",
        )


def case_2_closure_gates(gates: List[InsertionClosureGate], out: ScriptOutput) -> None:
    header("Case 2: Metric insertion closure gates")
    for gate in gates:
        print()
        print("-" * 120)
        print(gate.name)
        print("-" * 120)
        print(f"Gate: {gate.gate}")
        print(f"[{status_mark(gate.status).value}] {gate.name}: {gate.status}")
        print(f"Opens if: {gate.opens_if}")
        print(f"Remains closed if: {gate.remains_closed_if}")

    with out.governance_assessments():
        out.line(
            "metric insertion closure gates remain not ready",
            StatusMark.DEFER,
            "insertion, recovery, no-overlap, boundary/support/source, and parent gates remain closed",
        )


def case_3_rejected_upgrades(upgrades: List[RejectedInsertionUpgrade], out: ScriptOutput) -> None:
    header("Case 3: Rejected metric insertion upgrades")
    for upgrade in upgrades:
        print()
        print("-" * 120)
        print(upgrade.name)
        print("-" * 120)
        print(f"Rejected upgrade: {upgrade.rejected_upgrade}")
        print(f"[{status_mark(upgrade.status).value}] {upgrade.name}: {upgrade.status}")
        print(f"Reason: {upgrade.reason}")

    with out.counterexamples():
        out.line(
            "metric insertion obligation upgrades rejected",
            StatusMark.FAIL,
            "diagnostics, conventions, and compatibility audits are not B_s/F_zeta insertion theorem",
        )


def case_4_failure_controls(out: ScriptOutput) -> None:
    header("Case 4: Failure controls")
    print("The metric insertion theorem obligation audit fails if a later script allows:")
    print()
    print("1. F_zeta insertion law assumed instead of derived")
    print("2. coefficient origin selected by recovery")
    print("3. count-once convention treated as no-overlap theorem")
    print("4. O invoked without operator structure")
    print("5. gamma/AB/B=1/A/kappa diagnostics used as construction")
    print("6. boundary/scalar loads ignored")
    print("7. smooth support / no-shell matching assumed")
    print("8. ordinary source load hidden in coefficients/residuals/seam parameters")
    print("9. H/dark/exchange/curvature/current repair object supplies insertion")
    print("10. parent equation opened from Group 24 requirements alone")

    with out.governance_assessments():
        out.line(
            "metric insertion theorem overclaim controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not upgrade Group 24 diagnostics into insertion or parent closure",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Before claiming B_s/F_zeta insertion, Group 24 requires:")
    print()
    print("  F_zeta insertion law")
    print("  coefficient origin independent of recovery")
    print("  count-once recombination")
    print("  residual-kill or no-overlap derivation")
    print("  gamma / AB recovery without diagnostic tuning")
    print("  boundary / scalar silence compatibility")
    print("  smooth support / matching compatibility")
    print("  source compatibility")
    print("  no repair insertion")
    print()
    print("All remain open theorem obligations.")
    print()
    print("Possible next script:")
    print("  candidate_group_24_metric_insertion_status_summary.py")
    print()
    print("Tiny goblin label:")
    print("  The mirror judged. The engine is not built.")

    with out.governance_assessments():
        out.line(
            "metric insertion theorem obligation audit complete",
            StatusMark.PASS,
            "Group 24 insertion obligations explicit; B_s/F_zeta theorem remains open",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, entries: List[InsertionTheoremObligation]) -> None:
    ns.record_derivation(
        derivation_id="metric_insertion_theorem_obligations_marker_24",
        inputs=[sp.Symbol(entry.name.split(":", 1)[0].replace("-", "_").replace(" ", "_")) for entry in entries],
        output=sp.Symbol("metric_insertion_theorem_obligations_stated"),
        method="Group 24 metric insertion theorem obligations ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="obligation_marker",
        scope="Group 24 metric insertion recovery retest",
        is_placeholder=True,
    )


def record_obligations(ns, entries: List[InsertionTheoremObligation]) -> None:
    for entry in entries:
        safe = entry.name.split(":", 1)[0].replace("-", "_").replace(" ", "_").lower()
        ns.record_obligation(ProofObligationRecord(
            obligation_id=f"g24_close_{safe}",
            script_id=SCRIPT_ID,
            title=f"Close obligation: {entry.theorem_target}",
            status=ObligationStatus.OPEN,
            required_by=["g24_insertion_theorem_route"],
            description=(
                f"Required inputs: {entry.required_inputs}. Blocks: {entry.blocks}. Failure if: {entry.failure_if}."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g24_close_o1",
        "g24_close_o2",
        "g24_close_o3",
        "g24_close_o4",
        "g24_close_o5",
        "g24_close_o6",
        "g24_close_o7",
        "g24_close_o8",
        "g24_close_o9",
    ]

    ns.record_route(RouteRecord(
        route_id="g24_insertion_theorem_route",
        script_id=SCRIPT_ID,
        name="Group 24 B_s/F_zeta metric insertion theorem target",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "F_zeta insertion law is derived",
            "coefficients are structurally fixed before recovery",
            "count-once recombination or no-overlap is derived",
            "gamma/AB recovery is downstream only",
            "boundary/support/source compatibility is derived",
            "no repair object supplies insertion",
        ],
    ))

    for branch_id in [
        "retest_ledger_as_insertion_theorem",
        "recovery_diagnostics_as_construction",
        "count_once_as_no_overlap_theorem",
        "boundary_support_audit_licenses_insertion",
        "source_audit_licenses_insertion",
        "group24_opens_parent_gate",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_24",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; Group 24 requirements remain theorem targets, not solved claims.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g24_insertion_obligations_explicit_not_solved",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Group 24 metric insertion obligations are explicit but not solved. "
            "B_s/F_zeta insertion, coefficient origin, count-once/no-overlap, recovery independence, "
            "boundary/support compatibility, source compatibility, and parent closure remain theorem-targeted."
        ),
        derivation_ids=["metric_insertion_theorem_obligations_marker_24"],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Metric Insertion Theorem Obligations")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    obligations = build_obligations()
    gates = build_gates()
    upgrades = build_rejected_upgrades()

    case_0_problem_statement(out)
    case_1_obligation_ledger(obligations, out)
    case_2_closure_gates(gates, out)
    case_3_rejected_upgrades(upgrades, out)
    case_4_failure_controls(out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, obligations)
    record_obligations(ns, obligations)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
