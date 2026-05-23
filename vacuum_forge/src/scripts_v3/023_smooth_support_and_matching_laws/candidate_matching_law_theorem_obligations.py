# Candidate matching law theorem obligations
#
# Group:
#   23_smooth_support_and_matching_laws
#
# Script type:
#   OBLIGATION SUMMARY / REQUIREMENTS
#
# Purpose
# -------
# Consolidate the theorem obligations required before claiming a real
# matching/support law.
#
# Locked-door question:
#
#   What must be proved before claiming a real matching/support law?
#
# This script does not prove matching/support law.
# It does not prove compact support.
# It does not prove no-shell matching.
# It does not prove boundary neutrality or scalar silence.
# It does not open the parent field equation.
#
# It consolidates Group 23 obligations into a closure-ready ledger.

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
            "transition_layer_dep_23",
            "23_smooth_support_and_matching_laws__candidate_transition_layer_mass_flux_audit",
            "transition_layer_mass_flux_marker_23",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "parameter_dep_23",
            "23_smooth_support_and_matching_laws__candidate_boundary_parameter_independence",
            "boundary_parameter_independence_marker_23",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "source_compat_dep_23",
            "23_smooth_support_and_matching_laws__candidate_matching_law_source_compatibility",
            "matching_law_source_compatibility_marker_23",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g22_obligation_dep_23",
            "22_boundary_neutrality_and_scalar_silence__candidate_boundary_neutrality_theorem_obligations",
            "boundary_neutrality_theorem_obligations_marker_22",
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
class MatchingTheoremObligation:
    name: str
    theorem_target: str
    required_inputs: str
    status: str
    blocks: str
    failure_if: str


@dataclass
class MatchingClosureGate:
    name: str
    gate: str
    status: str
    opens_if: str
    remains_closed_if: str


@dataclass
class RejectedMatchingUpgrade:
    name: str
    rejected_upgrade: str
    status: str
    reason: str


def build_obligations() -> List[MatchingTheoremObligation]:
    return [
        MatchingTheoremObligation(
            name="O1: support origin",
            theorem_target="derive structural support origin",
            required_inputs="field/source/boundary law that fixes support before recovery or leakage repair",
            status="REQUIRED",
            blocks="compact support and transition layer claims",
            failure_if="support is declared, sharply imposed, or selected after failure appears",
        ),
        MatchingTheoremObligation(
            name="O2: value matching",
            theorem_target="derive f(R)=0 or equivalent value matching",
            required_inputs="boundary law or support law that removes value-jump shell diagnostic",
            status="REQUIRED",
            blocks="no-shell and compact support claims",
            failure_if="nonzero boundary value or exterior-zero declaration is ignored",
        ),
        MatchingTheoremObligation(
            name="O3: slope / no-flux matching",
            theorem_target="derive f'(R)=0 or equivalent no-flux condition",
            required_inputs="matching law that removes boundary scalar flux and slope-shell diagnostic",
            status="REQUIRED",
            blocks="boundary flux and scalar silence claims",
            failure_if="C1 value matching is treated as no-flux proof",
        ),
        MatchingTheoremObligation(
            name="O4: distributional shell absence",
            theorem_target="derive absence of delta-shell and shell-like radial source terms",
            required_inputs="distributional audit, support regularity, derivative-jump control",
            status="REQUIRED",
            blocks="no-shell matching and boundary neutrality claims",
            failure_if="cutoff/smoothing hides shell source",
        ),
        MatchingTheoremObligation(
            name="O5: transition layer neutrality",
            theorem_target="derive neutral transition layer behavior",
            required_inputs="zero C_layer, q_layer, I_layer, sigma_layer, alpha_recovery, source_load or derived neutral equivalents",
            status="REQUIRED",
            blocks="smooth transition and compact support claims",
            failure_if="smooth layer hides scalar, mass, current, shell/source, or recovery load",
        ),
        MatchingTheoremObligation(
            name="O6: recovery independence",
            theorem_target="derive recovery-independent support, smoothing, residual status, and boundary data",
            required_inputs="structural parameter origin before Schwarzschild/PPN/gamma_like/AB/B=1/A audits",
            status="REQUIRED",
            blocks="anti-smuggling and recovery audit claims",
            failure_if="recovery selects support radius, smoothing width, tail status, or boundary data",
        ),
        MatchingTheoremObligation(
            name="O7: source compatibility",
            theorem_target="derive matching/support/layer source no-double-counting",
            required_inputs="ordinary rho/M_enc remains A-routed; zero duplicate shell/scalar/current/repair/parameter loads",
            status="REQUIRED",
            blocks="ordinary closed-regime source/boundary closure",
            failure_if="ordinary source is rerouted into seam pockets",
        ),
        MatchingTheoremObligation(
            name="O8: residual non-reentry",
            theorem_target="derive diagnostic residual non-reentry through support/matching language",
            required_inputs="residuals do not re-enter metric, source, boundary, support, layer, recovery, H, O, dark, curvature, exchange, or parent placeholders",
            status="REQUIRED",
            blocks="diagnostic residual survival and scalar silence claims",
            failure_if="nonmetric residual becomes support or layer parameter",
        ),
        MatchingTheoremObligation(
            name="O9: no repair route",
            theorem_target="derive matching/support law without repair mechanisms",
            required_inputs="no O/H/dark/exchange/curvature/current/surface counterterm/recovery smoothing repair",
            status="REQUIRED",
            blocks="boundary neutrality and scalar silence closure claims",
            failure_if="repair object supplies missing support or matching law",
        ),
    ]


def build_gates() -> List[MatchingClosureGate]:
    return [
        MatchingClosureGate(
            name="G1: compact support gate",
            gate="compact support",
            status="NOT_READY",
            opens_if="structural support origin, value/slope matching, no shell, recovery independence, no leakage, and source compatibility are derived",
            remains_closed_if="support is declared, toy-profiled, recovery-selected, or repair supplied",
        ),
        MatchingClosureGate(
            name="G2: no-shell matching gate",
            gate="no-shell matching",
            status="NOT_READY",
            opens_if="value jump, derivative jump, slope flux, and hidden shell/source layer loads are all eliminated structurally",
            remains_closed_if="value matching or smoothness alone is used as proof",
        ),
        MatchingClosureGate(
            name="G3: transition layer neutrality gate",
            gate="transition layer neutrality",
            status="NOT_READY",
            opens_if="layer has no scalar/current flux, no A-tail, no shell/source load, no recovery tuning, and structural origin",
            remains_closed_if="smoothness hides load or recovery chooses layer data",
        ),
        MatchingClosureGate(
            name="G4: boundary/scalar silence gate",
            gate="boundary neutrality and scalar silence",
            status="NOT_READY",
            opens_if="matching/support laws satisfy Group 22 target ledger without repair routes",
            remains_closed_if="matching laws only state diagnostic conditions",
        ),
        MatchingClosureGate(
            name="G5: parent equation gate",
            gate="parent field equation",
            status="NOT_READY",
            opens_if="matching/support plus boundary/scalar/source/projector/divergence obligations are actually derived",
            remains_closed_if="Group 23 only consolidates matching/support obligations",
        ),
    ]


def build_rejected_upgrades() -> List[RejectedMatchingUpgrade]:
    return [
        RejectedMatchingUpgrade(
            name="U1: regularity ladder becomes support theorem",
            rejected_upgrade="treating value/slope/curvature diagnostics as derived support",
            status="REJECTED",
            reason="diagnostic regularity does not derive support origin",
        ),
        RejectedMatchingUpgrade(
            name="U2: shell audit becomes no-shell theorem",
            rejected_upgrade="treating f(R)=f'(R)=0 diagnostics as complete shell absence",
            status="REJECTED",
            reason="higher distributional/support/source/recovery burdens remain open",
        ),
        RejectedMatchingUpgrade(
            name="U3: admissibility ledger becomes compact support",
            rejected_upgrade="treating required admissibility conditions as satisfied",
            status="REJECTED",
            reason="requirements are not derivations",
        ),
        RejectedMatchingUpgrade(
            name="U4: transition-layer audit becomes neutral layer theorem",
            rejected_upgrade="treating zero ledger targets as derived transition neutrality",
            status="REJECTED",
            reason="layer origin and neutrality law remain theorem-targeted",
        ),
        RejectedMatchingUpgrade(
            name="U5: source compatibility ledger becomes proof",
            rejected_upgrade="treating source no-double-counting requirements as derived compatibility",
            status="REJECTED",
            reason="ordinary source preservation still needs theorem support",
        ),
        RejectedMatchingUpgrade(
            name="U6: matching law opens parent gate",
            rejected_upgrade="opening parent equation from Group 23 requirements",
            status="REJECTED",
            reason="parent closure remains downstream of unresolved boundary/scalar/source/projector/divergence theorems",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Matching law theorem obligations problem")
    print("Question:")
    print()
    print("  What must be proved before claiming a real matching/support law?")
    print()
    print("Reference discipline:")
    print()
    print("  Group 23 has built diagnostics and requirements for regularity, shell absence, compact support, transition layers, parameter independence, and source compatibility.")
    print("  This script consolidates the theorem burden.")
    print("  It does not prove any of the obligations.")

    with out.governance_assessments():
        out.line(
            "matching law theorem obligation audit opened",
            StatusMark.INFO,
            "consolidating Group 23 theorem burdens without upgrading them to proofs",
        )


def case_1_obligation_ledger(entries: List[MatchingTheoremObligation], out: ScriptOutput) -> None:
    header("Case 1: Matching/support theorem obligation ledger")
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
            "matching/support theorem obligations consolidated",
            StatusMark.OBLIGATION,
            f"{len(entries)} theorem obligations remain open",
        )


def case_2_closure_gates(gates: List[MatchingClosureGate], out: ScriptOutput) -> None:
    header("Case 2: Matching/support closure gates")
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
            "matching/support closure gates remain not ready",
            StatusMark.DEFER,
            "compact support, no-shell matching, transition neutrality, boundary/scalar silence, and parent gates remain closed",
        )


def case_3_rejected_upgrades(upgrades: List[RejectedMatchingUpgrade], out: ScriptOutput) -> None:
    header("Case 3: Rejected matching/support upgrades")
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
            "matching/support obligation upgrades rejected",
            StatusMark.FAIL,
            "diagnostics, ledgers, and requirements are not derived matching/support theorems",
        )


def case_4_failure_controls(out: ScriptOutput) -> None:
    header("Case 4: Failure controls")
    print("The matching-law theorem obligation audit fails if a later script allows:")
    print()
    print("1. matching regularity diagnostics to count as support theorem")
    print("2. f(R)=0 or f'(R)=0 diagnostics to count as no-shell theorem")
    print("3. compact-support admissibility conditions to count as derived support")
    print("4. transition layer targets to count as neutral layer theorem")
    print("5. recovery independence to be assumed")
    print("6. source compatibility to be assumed")
    print("7. residuals to re-enter through support/matching/layer parameters")
    print("8. O, H, dark, exchange, curvature, current, or surface counterterm to supply missing support law")
    print("9. parent equation to open from Group 23 requirements alone")

    with out.governance_assessments():
        out.line(
            "matching/support theorem overclaim controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not upgrade requirements into solved matching/support theorems",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Before claiming a real matching/support law, Group 23 requires:")
    print()
    print("  structural support origin")
    print("  value matching")
    print("  slope / no-flux matching")
    print("  distributional shell absence")
    print("  transition layer neutrality")
    print("  recovery independence")
    print("  source compatibility")
    print("  residual non-reentry")
    print("  no repair route")
    print()
    print("All remain open theorem obligations.")
    print()
    print("Possible next script:")
    print("  candidate_group_23_matching_laws_status_summary.py")
    print()
    print("Tiny goblin label:")
    print("  The seam has rules. The theorem is still locked.")

    with out.governance_assessments():
        out.line(
            "matching law theorem obligation audit complete",
            StatusMark.PASS,
            "Group 23 obligations are explicit; matching/support theorem remains open",
        )


def record_derivations(ns, entries: List[MatchingTheoremObligation]) -> None:
    ns.record_derivation(
        derivation_id="matching_law_theorem_obligations_marker_23",
        inputs=[sp.Symbol(entry.name.split(":", 1)[0].replace("-", "_")) for entry in entries],
        output=sp.Symbol("matching_law_theorem_obligations_stated"),
        method="Group 23 matching/support theorem obligations ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="obligation_marker",
        scope="Group 23 smooth support and matching laws",
        is_placeholder=True,
    )


def record_obligations(ns, entries: List[MatchingTheoremObligation]) -> None:
    for entry in entries:
        safe = entry.name.split(":", 1)[0].replace("-", "_").replace(" ", "_").lower()
        ns.record_obligation(ProofObligationRecord(
            obligation_id=f"g23_close_{safe}",
            script_id=SCRIPT_ID,
            title=f"Close obligation: {entry.theorem_target}",
            status=ObligationStatus.OPEN,
            required_by=["g23_matching_theorem_route"],
            description=(
                f"Required inputs: {entry.required_inputs}. Blocks: {entry.blocks}. Failure if: {entry.failure_if}."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g23_close_o1",
        "g23_close_o2",
        "g23_close_o3",
        "g23_close_o4",
        "g23_close_o5",
        "g23_close_o6",
        "g23_close_o7",
        "g23_close_o8",
        "g23_close_o9",
    ]

    ns.record_route(RouteRecord(
        route_id="g23_matching_theorem_route",
        script_id=SCRIPT_ID,
        name="Group 23 smooth support and matching law theorem target",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "structural support origin is derived",
            "value and slope/no-flux matching are derived",
            "distributional shell absence is derived",
            "transition layer neutrality is derived",
            "recovery independence is derived",
            "source compatibility is derived",
            "residual non-reentry and no-repair discipline are preserved",
        ],
    ))

    for branch_id in [
        "regularity_ladder_as_support",
        "shell_audit_as_no_shell_theorem",
        "admissibility_ledger_as_compact_support",
        "transition_audit_as_neutral_layer",
        "source_ledger_as_source_compatibility",
        "matching_law_opens_parent_gate",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_23",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; Group 23 requirements remain theorem targets, not solved claims.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g23_matching_obligations_explicit_not_solved",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Group 23 matching/support obligations are explicit but not solved. "
            "Structural support, no-shell matching, transition neutrality, recovery independence, source compatibility, "
            "and boundary/scalar silence remain theorem-targeted."
        ),
        derivation_ids=["matching_law_theorem_obligations_marker_23"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Matching Law Theorem Obligations")
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
