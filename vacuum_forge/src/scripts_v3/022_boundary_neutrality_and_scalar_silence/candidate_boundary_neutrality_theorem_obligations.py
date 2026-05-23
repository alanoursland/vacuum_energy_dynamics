# Candidate boundary neutrality theorem obligations
#
# Group:
#   22_boundary_neutrality_and_scalar_silence
#
# Script type:
#   OBLIGATION SUMMARY / REQUIREMENTS
#
# Purpose
# -------
# Turn boundary/scalar silence requirements into explicit theorem obligations.
#
# Locked-door question:
#
#   What theorem obligations are required before claiming boundary neutrality?
#
# This script does not prove boundary neutrality.
# It does not prove scalar silence.
# It does not derive compact support, no-shell matching, residual-kill,
# no-overlap O, H insertion, current neutrality, or a parent field equation.
#
# It consolidates Group 22 obligations into a closure-ready ledger.

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
            "boundary_scalar_silence_target_ledger_dependency_22",
            "022_boundary_neutrality_and_scalar_silence__candidate_boundary_scalar_silence_targets",
            "boundary_scalar_silence_target_ledger_marker_22",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "smooth_compact_no_shell_dependency_22",
            "022_boundary_neutrality_and_scalar_silence__candidate_smooth_compact_support_no_shell_conditions",
            "smooth_compact_support_no_shell_inventory_marker_22",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "sector_scalar_silence_dependency_22",
            "022_boundary_neutrality_and_scalar_silence__candidate_scalar_tail_silence_sector_conditions",
            "scalar_tail_silence_sector_inventory_marker_22",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "boundary_current_flux_silence_dependency_22",
            "022_boundary_neutrality_and_scalar_silence__candidate_boundary_current_flux_silence",
            "boundary_current_flux_silence_inventory_marker_22",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "boundary_repair_exclusion_dependency_22",
            "022_boundary_neutrality_and_scalar_silence__candidate_boundary_repair_route_exclusion",
            "boundary_repair_route_exclusion_inventory_marker_22",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "diagnostic_residual_nonmetric_dependency_22",
            "022_boundary_neutrality_and_scalar_silence__candidate_diagnostic_residual_nonmetric_conditions",
            "diagnostic_residual_nonmetric_conditions_marker_22",
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
class BoundaryObligationEntry:
    name: str
    theorem_target: str
    required_inputs: str
    status: str
    blocks: str
    failure_if: str


@dataclass
class ClosureGateEntry:
    name: str
    gate: str
    status: str
    opens_if: str
    remains_closed_if: str


@dataclass
class RejectedUpgradeEntry:
    name: str
    rejected_upgrade: str
    status: str
    reason: str


def build_obligations() -> List[BoundaryObligationEntry]:
    return [
        BoundaryObligationEntry(
            name="O1: no-shell condition",
            theorem_target="derive no-shell boundary condition",
            required_inputs="matching law, support law, distributional boundary audit",
            status="REQUIRED",
            blocks="compact support and boundary neutrality claims",
            failure_if="value jump, derivative jump, sharp support, or shell source is treated as harmless",
        ),
        BoundaryObligationEntry(
            name="O2: residual scalar silence",
            theorem_target="derive residual scalar coefficient vanishing or strict nonmetric inertness",
            required_inputs="sector coefficients, residual-kill/nonmetric proof, no-reentry proof",
            status="REQUIRED",
            blocks="scalar silence and parent recombination claims",
            failure_if="any ordinary-sector C_i/r tail survives with C_i != 0",
        ),
        BoundaryObligationEntry(
            name="O3: non-A boundary A-flux neutrality",
            theorem_target="derive delta F_A|boundary,non-A = 0",
            required_inputs="boundary A-tail audit, A-sector mass-charge protection, no repair route",
            status="REQUIRED",
            blocks="boundary mass preservation claims",
            failure_if="non-A q/r A-tail shifts M_A",
        ),
        BoundaryObligationEntry(
            name="O4: current flux silence",
            theorem_target="derive non-A far-zone current flux silence",
            required_inputs="current definitions or role-level inertness, neutral transport theorem if nonzero",
            status="REQUIRED",
            blocks="current neutrality and boundary flux claims",
            failure_if="I_i/(4*pi*r^2) flux survives without neutral-transport theorem",
        ),
        BoundaryObligationEntry(
            name="O5: compact-support matching law",
            theorem_target="derive compact support with value/slope matching and no shell",
            required_inputs="support mechanism, matching order, derivative behavior, recovery independence",
            status="REQUIRED",
            blocks="compact-support scalar silence claims",
            failure_if="support is declared, recovery-selected, or sharply imposed",
        ),
        BoundaryObligationEntry(
            name="O6: diagnostic residual non-reentry",
            theorem_target="derive diagnostic residual inertness and non-reentry",
            required_inputs="metric/source/boundary/far-zone/coefficient/recovery no-effect proof",
            status="REQUIRED",
            blocks="nonmetric residual survival claims",
            failure_if="diagnostic residual re-enters through metric, source, H, O, dark, curvature, exchange, or parent placeholder",
        ),
        BoundaryObligationEntry(
            name="O7: no recovery-tuned boundary data",
            theorem_target="derive boundary/support/residual status independent of recovery targets",
            required_inputs="structural boundary law before Schwarzschild/PPN/gamma_like/AB/B=1/A tests",
            status="REQUIRED",
            blocks="anti-smuggling and recovery audit claims",
            failure_if="recovery selects smoothing, support radius, coefficients, residual status, or current direction",
        ),
        BoundaryObligationEntry(
            name="O8: source-routing compatibility",
            theorem_target="derive compatibility with ordinary source no-double-counting",
            required_inputs="A-sector source routing, non-A source exclusion, no cancellation ledger",
            status="REQUIRED",
            blocks="ordinary closed-regime source/boundary closure",
            failure_if="ordinary rho/T is rerouted into boundary, scalar, current, curvature, H, exchange, or dark repair",
        ),
        BoundaryObligationEntry(
            name="O9: no-repair theorem",
            theorem_target="derive boundary/scalar silence without repair routes",
            required_inputs="no shell, no tail, no current flux, no O/H/dark/curvature/exchange/smoothing repair",
            status="REQUIRED",
            blocks="all boundary neutrality closure claims",
            failure_if="surface counterterm, repair current, H, O, dark patch, curvature rescue, or exchange repair is used",
        ),
    ]


def build_gates() -> List[ClosureGateEntry]:
    return [
        ClosureGateEntry(
            name="G1: scalar silence claim gate",
            gate="scalar silence",
            status="NOT_READY",
            opens_if="all sector C_i coefficients vanish or are proven strictly nonmetric/inert/nonreentering",
            remains_closed_if="any sector uses cancellation, O/H repair, shell absorption, recovery selection, or diagnostic re-entry",
        ),
        ClosureGateEntry(
            name="G2: boundary neutrality claim gate",
            gate="boundary neutrality",
            status="NOT_READY",
            opens_if="delta F_A|boundary,non-A = 0, no shell, no A-tail, no current flux, no repair route",
            remains_closed_if="boundary A-tail, shell source, smoothing repair, or support-by-declaration remains",
        ),
        ClosureGateEntry(
            name="G3: compact support claim gate",
            gate="compact support",
            status="NOT_READY",
            opens_if="support is derived with value/slope matching, no derivative jump, no shell, and recovery independence",
            remains_closed_if="sharp support, value-only matching, recovery-selected support, or residual-kill-as-support remains",
        ),
        ClosureGateEntry(
            name="G4: parent equation gate",
            gate="parent field equation",
            status="NOT_READY",
            opens_if="boundary/scalar silence plus source/projector/divergence obligations are actually derived",
            remains_closed_if="Group 22 only states obligations and does not prove them",
        ),
    ]


def build_rejected_upgrades() -> List[RejectedUpgradeEntry]:
    return [
        RejectedUpgradeEntry(
            name="U1: target becomes theorem",
            rejected_upgrade="treating vanishing targets as solved",
            status="REJECTED",
            reason="Group 22 records obligations; it does not prove the vanishing conditions",
        ),
        RejectedUpgradeEntry(
            name="U2: diagnostic becomes operator",
            rejected_upgrade="diagnostic/nonmetric label treated as no-overlap O",
            status="REJECTED",
            reason="nonmetric vocabulary is not an operator with domain/kernel/image/boundary law",
        ),
        RejectedUpgradeEntry(
            name="U3: safe toy profile becomes support law",
            rejected_upgrade="C2/smooth toy profile treated as derived compact support",
            status="REJECTED",
            reason="toy boundary flux checks are diagnostics, not support dynamics",
        ),
        RejectedUpgradeEntry(
            name="U4: repair exclusion becomes positive proof",
            rejected_upgrade="rejecting repairs treated as proving boundary neutrality",
            status="REJECTED",
            reason="excluding fake routes does not prove the real route",
        ),
        RejectedUpgradeEntry(
            name="U5: future theorem route becomes current law",
            rejected_upgrade="neutral transport theorem target treated as J_V/J_sub/J_exch/J_curv law",
            status="REJECTED",
            reason="the currents remain undefined or role-level",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Boundary neutrality theorem obligations problem")
    print("Question:")
    print()
    print("  What theorem obligations are required before claiming boundary neutrality?")
    print()
    print("Reference discipline:")
    print()
    print("  Group 22 has stated targets and rejected shortcuts.")
    print("  This script consolidates obligations.")
    print("  It does not prove boundary neutrality or scalar silence.")
    print("  It prepares the Group 22 status summary.")

    with out.governance_assessments():
        out.line(
            "boundary neutrality theorem obligation audit opened",
            StatusMark.INFO,
            "consolidating Group 22 theorem burdens without upgrading them to proofs",
        )


def case_1_obligation_ledger(entries: List[BoundaryObligationEntry], out: ScriptOutput) -> None:
    header("Case 1: Boundary/scalar theorem obligation ledger")
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
            "boundary/scalar theorem obligations consolidated",
            StatusMark.OBLIGATION,
            f"{len(entries)} theorem obligations remain open",
        )


def case_2_closure_gates(gates: List[ClosureGateEntry], out: ScriptOutput) -> None:
    header("Case 2: Closure gates")
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
            "closure gates remain not ready",
            StatusMark.DEFER,
            "scalar silence, boundary neutrality, compact support, and parent equation gates remain closed",
        )


def case_3_rejected_upgrades(upgrades: List[RejectedUpgradeEntry], out: ScriptOutput) -> None:
    header("Case 3: Rejected obligation upgrades")
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
            "obligation-to-theorem upgrades rejected",
            StatusMark.FAIL,
            "targets, diagnostics, toy profiles, repair exclusions, and theorem routes are not solved claims",
        )


def case_4_failure_controls(out: ScriptOutput) -> None:
    header("Case 4: Failure controls")
    print("The theorem-obligation audit fails if a later script allows:")
    print()
    print("1. Group 22 target conditions to be treated as proved")
    print("2. scalar silence claim while sector coefficients remain unproved")
    print("3. boundary neutrality claim while no-shell/no-tail/no-current obligations remain open")
    print("4. compact support claim from toy profiles alone")
    print("5. diagnostic residual label to replace residual-kill/no-overlap theorem")
    print("6. repair-route exclusion to count as positive boundary proof")
    print("7. neutral transport target to count as current law")
    print("8. recovery tests to select boundary/scalar/current data")
    print("9. parent equation to be opened from Group 22 requirements alone")

    with out.governance_assessments():
        out.line(
            "boundary theorem-obligation overclaim controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not upgrade requirements into solved theorems",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Before claiming boundary neutrality, Group 22 requires:")
    print()
    print("  no-shell boundary condition")
    print("  residual scalar silence")
    print("  non-A boundary A-flux neutrality")
    print("  current flux silence")
    print("  compact-support matching law")
    print("  diagnostic residual non-reentry")
    print("  no recovery-tuned boundary data")
    print("  source-routing compatibility")
    print("  no-repair boundary theorem")
    print()
    print("All remain open theorem obligations.")
    print()
    print("This script prepares the Group 22 closing summary.")
    print("It does not prove any of these obligations.")
    print()
    print("Possible next script:")
    print("  candidate_group_22_boundary_neutrality_status_summary.py")

    with out.governance_assessments():
        out.line(
            "boundary neutrality theorem obligation audit complete",
            StatusMark.PASS,
            "Group 22 obligations are explicit; closure remains not ready as a theorem",
        )


def record_derivations(ns, entries: List[BoundaryObligationEntry]) -> None:
    ns.record_derivation(
        derivation_id="boundary_neutrality_theorem_obligations_marker_22",
        inputs=[sp.Symbol(entry.name.split(":", 1)[0].replace("-", "_")) for entry in entries],
        output=sp.Symbol("boundary_neutrality_theorem_obligations_stated"),
        method="Group 22 boundary neutrality theorem obligations ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="obligation_marker",
        scope="Group 22 boundary neutrality and scalar silence",
        is_placeholder=True,
    )


def record_obligations(ns, entries: List[BoundaryObligationEntry]) -> None:
    for entry in entries:
        safe = entry.name.split(":", 1)[0].replace("-", "_").replace(" ", "_").lower()
        ns.record_obligation(ProofObligationRecord(
            obligation_id=f"close_{safe}_22",
            script_id=SCRIPT_ID,
            title=f"Close obligation: {entry.theorem_target}",
            status=ObligationStatus.OPEN,
            required_by=["ordinary_closed_regime_boundary_neutrality_and_scalar_silence_theorem_22"],
            description=(
                f"Required inputs: {entry.required_inputs}. Blocks: {entry.blocks}. Failure if: {entry.failure_if}."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "close_o1_22",
        "close_o2_22",
        "close_o3_22",
        "close_o4_22",
        "close_o5_22",
        "close_o6_22",
        "close_o7_22",
        "close_o8_22",
        "close_o9_22",
    ]

    ns.record_route(RouteRecord(
        route_id="g22_boundary_silence_theorem",
        script_id=SCRIPT_ID,
        name="Ordinary closed-regime boundary neutrality and scalar silence theorem target",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "no-shell boundary condition derived",
            "sector residual scalar silence derived",
            "non-A boundary A-flux neutrality derived",
            "far-zone non-A current silence derived",
            "diagnostic residual non-reentry derived",
            "no repair routes used",
            "source-routing compatibility shown",
        ],
    ))

    for branch_id in [
        "target_conditions_as_theorems",
        "toy_profiles_as_support_law",
        "repair_exclusion_as_positive_proof",
        "diagnostic_label_as_no_overlap",
        "neutral_transport_target_as_current_law",
        "parent_equation_from_requirements",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_22",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; Group 22 obligations remain theorem targets, not solved claims.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="boundary_neutrality_obligations_explicit_not_solved_22",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Group 22 boundary neutrality and scalar silence obligations are explicit but not solved. "
            "Scalar silence, boundary neutrality, compact support, neutral transport, no-overlap, and parent closure remain not ready as theorems."
        ),
        derivation_ids=["boundary_neutrality_theorem_obligations_marker_22"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Boundary Neutrality Theorem Obligations")
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

    record_derivations(ns, obligations)
    record_obligations(ns, obligations)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
