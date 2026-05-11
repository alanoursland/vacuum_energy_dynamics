# Candidate residual kill theorem obligations
#
# Group:
#   25_residual_kill_or_no_overlap_theorem
#
# Script type:
#   OBLIGATION SUMMARY / REQUIREMENTS
#
# Purpose
# -------
# Consolidate the theorem obligations required before claiming residual kill,
# strict non-metric inertness, or active no-overlap O.
#
# Locked-door question:
#
#   What must be proved before claiming residual kill or no-overlap?
#
# This script does not derive residual kill.
# It does not derive non-metric inertness.
# It does not derive active no-overlap O.
# It does not derive B_s/F_zeta insertion.
# It does not open parent equation closure.
#
# It consolidates the Group 25 theorem burden into a closure-ready ledger.

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
            "25_residual_kill_or_no_overlap_theorem__candidate_residual_kill_problem_ledger",
            "residual_kill_problem_ledger_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "classification_dep_25",
            "25_residual_kill_or_no_overlap_theorem__candidate_metric_trace_residual_classification",
            "metric_trace_residual_classification_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "inertness_dep_25",
            "25_residual_kill_or_no_overlap_theorem__candidate_nonmetric_inertness_conditions",
            "nonmetric_inertness_conditions_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "reentry_dep_25",
            "25_residual_kill_or_no_overlap_theorem__candidate_residual_reentry_exclusion_audit",
            "residual_reentry_exclusion_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "O_burden_dep_25",
            "25_residual_kill_or_no_overlap_theorem__candidate_no_overlap_operator_minimum_burden",
            "no_overlap_operator_minimum_burden_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "recovery_independence_dep_25",
            "25_residual_kill_or_no_overlap_theorem__candidate_residual_kill_recovery_independence",
            "residual_kill_recovery_independence_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "boundary_source_dep_25",
            "25_residual_kill_or_no_overlap_theorem__candidate_residual_kill_boundary_source_compatibility",
            "residual_kill_boundary_source_compatibility_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g24_summary_dep_25",
            "24_metric_insertion_recovery_retest__candidate_group_24_metric_insertion_status_summary",
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


@dataclass
class ResidualTheoremObligation:
    name: str
    theorem_target: str
    required_inputs: str
    status: str
    blocks: str
    failure_if: str


@dataclass
class ResidualClosureGate:
    name: str
    gate: str
    status: str
    opens_if: str
    remains_closed_if: str


@dataclass
class RejectedResidualUpgrade:
    name: str
    rejected_upgrade: str
    status: str
    reason: str


def build_obligations() -> List[ResidualTheoremObligation]:
    return [
        ResidualTheoremObligation(
            name="O1: residual-kill law",
            theorem_target="derive a structural law forcing L_double = 0",
            required_inputs="zeta_residual_metric, kappa_metric, epsilon_vac_metric, and e_kappa_metric are killed by law, not declaration",
            status="REQUIRED",
            blocks="count-once recombination",
            failure_if="residuals are set to zero by naming",
        ),
        ResidualTheoremObligation(
            name="O2: non-metric inertness law",
            theorem_target="derive strict non-metric / inert residual status",
            required_inputs="no metric, source, boundary, support, recovery, repair, or parent reentry",
            status="REQUIRED",
            blocks="honest inert residual status",
            failure_if="non-metric or inert labels are used without no-reentry proof",
        ),
        ResidualTheoremObligation(
            name="O3: zeta residual non-reentry",
            theorem_target="derive zeta residual cannot re-enter ordinary metric/source/boundary/support language",
            required_inputs="sector-by-sector absence of zeta_residual_metric reentry",
            status="REQUIRED",
            blocks="zeta count-once insertion",
            failure_if="zeta enters B_s and residual trace/source/seam data",
        ),
        ResidualTheoremObligation(
            name="O4: kappa residual non-reentry",
            theorem_target="derive kappa residual cannot restore killed trace or source role",
            required_inputs="kappa_metric diagnostic-only / inert / zero status with no e_kappa backdoor",
            status="REQUIRED",
            blocks="kappa trace control",
            failure_if="kappa restores residual metric trace or source load",
        ),
        ResidualTheoremObligation(
            name="O5: epsilon_vac_config / e_kappa inertness",
            theorem_target="derive epsilon_vac_config and e_kappa are not metric/source channels",
            required_inputs="no metric, source, support, boundary, recovery, or repair role",
            status="REQUIRED",
            blocks="configuration residual cleanup",
            failure_if="epsilon_vac_config or e_kappa becomes extra metric/source channel",
        ),
        ResidualTheoremObligation(
            name="O6: active O structure if used",
            theorem_target="derive active no-overlap operator structure",
            required_inputs="domain, codomain, kernel, image, idempotence/composition, pairing, divergence, boundary, source, mass, scalar/current/support behavior, and recovery independence",
            status="REQUIRED",
            blocks="active no-overlap projection",
            failure_if="O erases overlap by name",
        ),
        ResidualTheoremObligation(
            name="O7: recovery independence",
            theorem_target="derive residual status independent of recovery outcomes",
            required_inputs="Schwarzschild, AB, B=1/A, gamma_like, PPN, areal kappa, boundary/source failure, and parent fit do not choose status",
            status="REQUIRED",
            blocks="anti-smuggling residual control",
            failure_if="residual status is selected from recovery or repair targets",
        ),
        ResidualTheoremObligation(
            name="O8: boundary/source compatibility",
            theorem_target="derive residual cleanup preserves boundary, support, source, and mass guardrails",
            required_inputs="no A-mass shift, scalar tail, current flux, boundary flux, shell/source load, support/layer load, source duplication, recovery seam, repair object, or insertion license",
            status="REQUIRED",
            blocks="guardrail-compatible residual cleanup",
            failure_if="residual cleanup becomes boundary/source repair",
        ),
        ResidualTheoremObligation(
            name="O9: no insertion / parent shortcut",
            theorem_target="keep residual control from licensing B_s/F_zeta insertion or parent equation",
            required_inputs="separate insertion law and parent closure remain required",
            status="REQUIRED",
            blocks="overclaim prevention",
            failure_if="residual cleanup opens metric insertion or parent gate",
        ),
    ]


def build_gates() -> List[ResidualClosureGate]:
    return [
        ResidualClosureGate(
            name="G1: residual-kill gate",
            gate="structural residual kill",
            status="NOT_READY",
            opens_if="L_double = 0 is derived by law and not selected from recovery or repair targets",
            remains_closed_if="residuals are declared zero or ignored",
        ),
        ResidualClosureGate(
            name="G2: non-metric inertness gate",
            gate="strict inert residual status",
            status="NOT_READY",
            opens_if="all metric/source/boundary/support/recovery/repair/parent reentry channels are closed sector-by-sector",
            remains_closed_if="non-metric or inert labels lack no-reentry proof",
        ),
        ResidualClosureGate(
            name="G3: active O gate",
            gate="active no-overlap operator",
            status="NOT_READY",
            opens_if="full operator structure and compatibility behavior are derived",
            remains_closed_if="O is a placeholder or eraser by name",
        ),
        ResidualClosureGate(
            name="G4: count-once recombination gate",
            gate="zeta_to_Bs as sole ordinary metric scalar trace",
            status="NOT_READY",
            opens_if="residual zeta/kappa/epsilon/e_kappa channels are killed, inert, or projected by derived law",
            remains_closed_if="residual trace can re-enter",
        ),
        ResidualClosureGate(
            name="G5: boundary/source compatibility gate",
            gate="residual cleanup compatible with Groups 21-24 guardrails",
            status="NOT_READY",
            opens_if="cleanup creates no mass shift, tail, flux, shell, support load, source duplication, recovery seam, repair object, or insertion license",
            remains_closed_if="cleanup repairs boundary/source failure",
        ),
        ResidualClosureGate(
            name="G6: B_s/F_zeta insertion gate",
            gate="metric insertion",
            status="NOT_READY",
            opens_if="residual control plus independent insertion law and coefficient origin are derived",
            remains_closed_if="residual cleanup alone is treated as insertion theorem",
        ),
        ResidualClosureGate(
            name="G7: parent equation gate",
            gate="parent field equation",
            status="NOT_READY",
            opens_if="residual control, insertion, boundary/source/support, divergence, and parent identity are derived",
            remains_closed_if="Group 25 obligations are used as parent closure",
        ),
    ]


def build_rejected_upgrades() -> List[RejectedResidualUpgrade]:
    return [
        RejectedResidualUpgrade(
            name="U1: problem ledger becomes residual-kill theorem",
            rejected_upgrade="treating the residual problem ledger as solved residual control",
            status="REJECTED",
            reason="inventory is not a theorem",
        ),
        RejectedResidualUpgrade(
            name="U2: residual label becomes no-reentry law",
            rejected_upgrade="using killed, nonmetric, diagnostic-only, inert, or projected labels as proof",
            status="REJECTED",
            reason="labels need theorem support",
        ),
        RejectedResidualUpgrade(
            name="U3: active O placeholder becomes operator",
            rejected_upgrade="using O as eraser without domain/kernel/image/divergence/boundary/source structure",
            status="REJECTED",
            reason="active O remains theorem-targeted",
        ),
        RejectedResidualUpgrade(
            name="U4: recovery independence audit becomes recovery theorem",
            rejected_upgrade="treating rejected recovery-selection routes as derived recovery behavior",
            status="REJECTED",
            reason="anti-smuggling is not recovery proof",
        ),
        RejectedResidualUpgrade(
            name="U5: boundary/source compatibility audit becomes compatibility theorem",
            rejected_upgrade="treating guardrail audit as derived boundary/source compatibility",
            status="REJECTED",
            reason="compatibility remains theorem-targeted",
        ),
        RejectedResidualUpgrade(
            name="U6: residual cleanup becomes B_s/F_zeta insertion",
            rejected_upgrade="using residual control to license metric insertion",
            status="REJECTED",
            reason="insertion law and coefficient origin remain separate obligations",
        ),
        RejectedResidualUpgrade(
            name="U7: residual cleanup opens parent gate",
            rejected_upgrade="using Group 25 residual-control obligations as parent equation closure",
            status="REJECTED",
            reason="parent closure remains downstream",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Residual-kill theorem obligations problem")
    print("Question:")
    print()
    print("  What must be proved before claiming residual kill or no-overlap?")
    print()
    print("Reference discipline:")
    print()
    print("  Group 25 has audited residual objects, status labels, inertness, reentry, active O burden, recovery independence, and boundary/source compatibility.")
    print("  This script consolidates the theorem burden.")
    print("  It does not prove residual control.")

    with out.governance_assessments():
        out.line(
            "residual-kill theorem obligation audit opened",
            StatusMark.INFO,
            "consolidating Group 25 theorem burdens without upgrading them to proof",
        )


def case_1_obligation_ledger(entries: List[ResidualTheoremObligation], out: ScriptOutput) -> None:
    header("Case 1: Residual-control theorem obligation ledger")
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
            "residual-control theorem obligations consolidated",
            StatusMark.OBLIGATION,
            f"{len(entries)} residual-control theorem obligations remain open",
        )


def case_2_closure_gates(gates: List[ResidualClosureGate], out: ScriptOutput) -> None:
    header("Case 2: Residual-control closure gates")
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
            "residual-control closure gates remain not ready",
            StatusMark.DEFER,
            "residual-kill, inertness, active O, count-once, insertion, and parent gates remain closed",
        )


def case_3_rejected_upgrades(upgrades: List[RejectedResidualUpgrade], out: ScriptOutput) -> None:
    header("Case 3: Rejected residual-control upgrades")
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
            "residual-control obligation upgrades rejected",
            StatusMark.FAIL,
            "diagnostics, labels, placeholder O, and compatibility audits are not residual-control theorem",
        )


def case_4_failure_controls(out: ScriptOutput) -> None:
    header("Case 4: Failure controls")
    print("The residual-kill theorem obligation audit fails if a later script allows:")
    print()
    print("1. L_double killed by declaration")
    print("2. nonmetric/inert labels used without no-reentry proof")
    print("3. zeta residual re-enters through metric/source/boundary/support/recovery/repair/parent language")
    print("4. kappa restores killed trace or source load")
    print("5. epsilon_vac_config or e_kappa becomes metric/source channel")
    print("6. active O erases overlap without full operator structure")
    print("7. residual status selected from recovery")
    print("8. residual cleanup repairs boundary/source failure")
    print("9. residual cleanup licenses B_s/F_zeta insertion")
    print("10. residual cleanup opens parent equation")

    with out.governance_assessments():
        out.line(
            "residual-control overclaim controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not upgrade Group 25 diagnostics into solved residual control",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Before claiming residual kill / inertness / no-overlap, Group 25 requires:")
    print()
    print("  residual-kill law")
    print("  non-metric inertness law")
    print("  zeta residual non-reentry")
    print("  kappa residual non-reentry")
    print("  epsilon_vac_config / e_kappa inertness")
    print("  active O structure if O is used")
    print("  recovery independence")
    print("  boundary/source compatibility")
    print("  no insertion / parent shortcut")
    print()
    print("All remain open theorem obligations.")
    print()
    print("Possible next script:")
    print("  candidate_group_25_residual_kill_status_summary.py")
    print()
    print("Tiny goblin label:")
    print("  The locks are listed. None are picked.")

    with out.governance_assessments():
        out.line(
            "residual-control theorem obligation audit complete",
            StatusMark.PASS,
            "Group 25 residual-control obligations explicit; theorem remains open",
        )


def record_derivations(ns, entries: List[ResidualTheoremObligation]) -> None:
    ns.record_derivation(
        derivation_id="residual_kill_theorem_obligations_marker_25",
        inputs=[sp.Symbol(entry.name.split(":", 1)[0].replace("-", "_").replace(" ", "_")) for entry in entries],
        output=sp.Symbol("residual_kill_theorem_obligations_stated"),
        method="Group 25 residual kill / no-overlap theorem obligations ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="obligation_marker",
        scope="Group 25 residual kill or no-overlap theorem",
        is_placeholder=True,
    )


def record_obligations(ns, entries: List[ResidualTheoremObligation]) -> None:
    for entry in entries:
        safe = entry.name.split(":", 1)[0].replace("-", "_").replace(" ", "_").lower()
        ns.record_obligation(ProofObligationRecord(
            obligation_id=f"g25_close_{safe}",
            script_id=SCRIPT_ID,
            title=f"Close obligation: {entry.theorem_target}",
            status=ObligationStatus.OPEN,
            required_by=["g25_residual_control_theorem_route"],
            description=(
                f"Required inputs: {entry.required_inputs}. Blocks: {entry.blocks}. Failure if: {entry.failure_if}."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g25_close_o1",
        "g25_close_o2",
        "g25_close_o3",
        "g25_close_o4",
        "g25_close_o5",
        "g25_close_o6",
        "g25_close_o7",
        "g25_close_o8",
        "g25_close_o9",
    ]

    ns.record_route(RouteRecord(
        route_id="g25_residual_control_theorem_route",
        script_id=SCRIPT_ID,
        name="Group 25 residual kill / no-overlap theorem target",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "residual-kill law or inertness law is derived",
            "zeta/kappa/epsilon/e_kappa non-reentry is derived",
            "active O structure is derived if O is used",
            "residual status is recovery-independent",
            "boundary/source compatibility is preserved",
            "residual cleanup does not license insertion or parent closure",
        ],
    ))

    for branch_id in [
        "residual_problem_ledger_as_theorem",
        "residual_label_as_no_reentry_law",
        "active_O_placeholder_as_operator",
        "recovery_independence_audit_as_theorem",
        "boundary_source_audit_as_theorem",
        "residual_cleanup_as_Bs_insertion",
        "residual_cleanup_opens_parent",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_25",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; Group 25 requirements remain theorem targets, not solved residual control.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g25_residual_control_obligations_explicit_not_solved",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Group 25 residual-control obligations are explicit but not solved. Residual kill, strict non-metric inertness, "
            "active no-overlap O, count-once recombination, B_s/F_zeta insertion, and parent closure remain theorem-targeted."
        ),
        derivation_ids=["residual_kill_theorem_obligations_marker_25"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Residual Kill Theorem Obligations")
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
