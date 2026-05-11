# Candidate group 27 status summary
#
# Group:
#   27_active_O_construction
#
# Script type:
#   SUMMARY
#
# Purpose
# -------
# Close Group 27 by summarizing the active-O construction attempt.
#
# Locked-door question:
#
#   What did the active-O construction attempt establish?
#
# This script is not an active-O theorem.
# It is not residual control.
# It is not B_s/F_zeta insertion.
# It is not parent equation closure.
#
# Tiny goblin rule:
#
#   The map names the missing forge.

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
        "CANDIDATE": StatusMark.DEFER,
        "CONTROLLED_OBSTRUCTION": StatusMark.DEFER,
        "HANDOFF_READY": StatusMark.PASS,
        "NOT_CONSTRUCTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "PARTIAL": StatusMark.INFO,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "SUMMARY": StatusMark.PASS,
        "UNDERDETERMINED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        ("g27_O_problem", "27_active_O_construction__candidate_O_problem_ledger", "g27_O_problem", RecordKind.INVENTORY_MARKER),
        ("g27_dc", "27_active_O_construction__candidate_O_domain_codomain", "g27_O_domain_codomain", RecordKind.INVENTORY_MARKER),
        ("g27_ki", "27_active_O_construction__candidate_O_kernel_image", "g27_O_kernel_image", RecordKind.INVENTORY_MARKER),
        ("g27_pair", "27_active_O_construction__candidate_O_no_overlap_pairing", "g27_O_pairing", RecordKind.INVENTORY_MARKER),
        ("g27_alg", "27_active_O_construction__candidate_O_projection_law", "g27_O_alg_law", RecordKind.INVENTORY_MARKER),
        ("g27_div", "27_active_O_construction__candidate_O_divergence_commutation", "g27_O_divergence", RecordKind.INVENTORY_MARKER),
        ("g27_bsm", "27_active_O_construction__candidate_O_boundary_source_mass", "g27_O_bsm", RecordKind.INVENTORY_MARKER),
        ("g27_rec", "27_active_O_construction__candidate_O_recovery_independence", "g27_O_recovery", RecordKind.INVENTORY_MARKER),
        ("g27_obs", "27_active_O_construction__candidate_O_construction_obstruction", "g27_O_obstruction", RecordKind.INVENTORY_MARKER),
        ("g27_ob", "27_active_O_construction__candidate_O_obligations", "g27_O_obligations", RecordKind.INVENTORY_MARKER),
        ("g26_summary", "26_residual_control_theorem_attempt__candidate_group_26_status_summary", "g26_status_summary", RecordKind.INVENTORY_MARKER),
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
    for attr in ("routes_path", "branch_decisions_path", "claims_path", "obligations_path", "derivations_path", "governance_path"):
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
class SummaryEntry:
    name: str
    topic: str
    status: str
    result: str


@dataclass
class FinalHandoff:
    name: str
    route: str
    status: str
    reason: str


@dataclass
class FinalGate:
    name: str
    status: str
    reason: str


@dataclass
class RejectedSummaryUpgrade:
    name: str
    upgrade: str
    status: str
    reason: str


def build_summary_entries() -> List[SummaryEntry]:
    return [
        SummaryEntry(
            name="G27-1: construction burden",
            topic="what O would have to be",
            status="PARTIAL",
            result="burden is explicit: domain, codomain, kernel, image, pairing, algebraic law, divergence, guardrails, recovery independence, insertion separation, parent closure",
        ),
        SummaryEntry(
            name="G27-2: domain/codomain",
            topic="candidate input/output sectors",
            status="PARTIAL",
            result="candidate ledgers exist but final domain/codomain are not derived",
        ),
        SummaryEntry(
            name="G27-3: kernel/image",
            topic="kernel and image assignments",
            status="UNDERDETERMINED",
            result="zeta_Bs image candidate exists; zeta/kappa residual membership remains underdetermined",
        ),
        SummaryEntry(
            name="G27-4: no-overlap pairing",
            topic="mathematical criterion for no-overlap",
            status="NOT_DERIVED",
            result="no explicit pairing is derived; sector-projection split remains best candidate",
        ),
        SummaryEntry(
            name="G27-5: algebraic law",
            topic="projection/replacement/constraint law",
            status="NOT_DERIVED",
            result="O^2=O, linearity, residual kill, and full constraint law are not derived",
        ),
        SummaryEntry(
            name="G27-6: divergence behavior",
            topic="conservation safety",
            status="NOT_DERIVED",
            result="Div(OX)=O(Div X) is not derived; correction route remains constrained candidate",
        ),
        SummaryEntry(
            name="G27-7: boundary/source/mass behavior",
            topic="guardrail compatibility",
            status="NOT_DERIVED",
            result="mass, scalar-tail, current, source, shell, and support neutrality are not derived",
        ),
        SummaryEntry(
            name="G27-8: recovery independence",
            topic="anti-smuggling",
            status="PARTIAL",
            result="recovery selection is rejected; recovery may audit constructed O, but O is not constructed",
        ),
        SummaryEntry(
            name="G27-9: active O",
            topic="usable operator status",
            status="NOT_CONSTRUCTED",
            result="active O is not usable in residual control or field equations",
        ),
        SummaryEntry(
            name="G27-10: obstruction type",
            topic="status of failed construction",
            status="CONTROLLED_OBSTRUCTION",
            result="controlled underdetermination, not O impossibility",
        ),
    ]


def build_handoffs() -> List[FinalHandoff]:
    return [
        FinalHandoff(
            name="H1: preferred next group",
            route="28_sector_pairing_and_no_overlap_geometry",
            status="HANDOFF_READY",
            reason="missing pairing blocks kernel/image and projection law; sector-projection remains the best candidate no-overlap structure",
        ),
        FinalHandoff(
            name="H2: alternate next group",
            route="28_Bs_Fzeta_coefficient_origin",
            status="HANDOFF_READY",
            reason="coefficient origin may decide residual interpretation and O classification",
        ),
        FinalHandoff(
            name="H3: later O algebra",
            route="28_operator_algebra_and_constraint_law",
            status="OPEN",
            reason="useful after or alongside a no-overlap criterion, but not enough alone",
        ),
        FinalHandoff(
            name="H4: residual-control retest",
            route="28_O_residual_control_retest",
            status="NOT_READY",
            reason="O is not usable yet",
        ),
        FinalHandoff(
            name="H5: parent field equation",
            route="parent_field_equation",
            status="NOT_READY",
            reason="parent closure remains forbidden as next step",
        ),
    ]


def build_gates() -> List[FinalGate]:
    return [
        FinalGate(
            name="active O",
            status="NOT_CONSTRUCTED",
            reason="critical operator structures remain open",
        ),
        FinalGate(
            name="residual control",
            status="NOT_READY",
            reason="O is not usable and non-O residual control remains obstructed from Group 26",
        ),
        FinalGate(
            name="B_s/F_zeta insertion",
            status="OPEN",
            reason="coefficient origin / insertion law remains separate",
        ),
        FinalGate(
            name="count-once recombination",
            status="NOT_READY",
            reason="requires residual control and insertion law",
        ),
        FinalGate(
            name="parent equation",
            status="NOT_READY",
            reason="requires residual control, insertion, divergence, boundary/source/support, and parent identity",
        ),
    ]


def build_rejected_upgrades() -> List[RejectedSummaryUpgrade]:
    return [
        RejectedSummaryUpgrade(
            name="U1: summary as O theorem",
            upgrade="Group 27 summary treated as active-O construction",
            status="REJECTED",
            reason="O is explicitly not constructed",
        ),
        RejectedSummaryUpgrade(
            name="U2: partial structure as usable operator",
            upgrade="candidate domain/codomain and trace preservation treated as usable O",
            status="REJECTED",
            reason="residual action, pairing, law, divergence, and guardrails remain open",
        ),
        RejectedSummaryUpgrade(
            name="U3: underdetermination as impossibility",
            upgrade="failure to construct O treated as O impossible",
            status="REJECTED",
            reason="missing structure is not a no-go theorem",
        ),
        RejectedSummaryUpgrade(
            name="U4: handoff as theorem",
            upgrade="sector pairing or coefficient-origin handoff treated as theorem closure",
            status="REJECTED",
            reason="handoff is not derivation",
        ),
        RejectedSummaryUpgrade(
            name="U5: parent readiness",
            upgrade="Group 27 opens parent equation",
            status="REJECTED",
            reason="parent gate remains closed",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Group 27 summary problem")
    print("Question:")
    print()
    print("  What did the active-O construction attempt establish?")
    print()
    print("Discipline:")
    print()
    print("  This is a group status summary, not theorem closure.")
    print("  The missing forge is named; the tool is not built.")

    with out.governance_assessments():
        out.line(
            "Group 27 status summary opened",
            StatusMark.INFO,
            "summarizing active-O construction attempt and handoff state",
        )


def case_1_summary_entries(entries: List[SummaryEntry], out: ScriptOutput) -> None:
    header("Case 1: Group 27 status entries")
    for entry in entries:
        print()
        print("-" * 120)
        print(entry.name)
        print("-" * 120)
        print(f"Topic: {entry.topic}")
        print(f"[{status_mark(entry.status).value}] {entry.name}: {entry.status}")
        print(f"Result: {entry.result}")

    with out.governance_assessments():
        out.line(
            "Group 27 status entries summarized",
            StatusMark.PASS,
            f"{len(entries)} status entries summarized",
        )


def case_2_handoffs(handoffs: List[FinalHandoff], out: ScriptOutput) -> None:
    header("Case 2: Final handoffs")
    for handoff in handoffs:
        print()
        print("-" * 120)
        print(handoff.name)
        print("-" * 120)
        print(f"Route: {handoff.route}")
        print(f"[{status_mark(handoff.status).value}] {handoff.name}: {handoff.status}")
        print(f"Reason: {handoff.reason}")

    with out.governance_assessments():
        out.line(
            "Group 27 handoffs summarized",
            StatusMark.PASS,
            "preferred next group is sector pairing and no-overlap geometry",
        )


def case_3_gates(gates: List[FinalGate], out: ScriptOutput) -> None:
    header("Case 3: Final gates")
    for gate in gates:
        print()
        print("-" * 120)
        print(gate.name)
        print("-" * 120)
        print(f"[{status_mark(gate.status).value}] {gate.name}: {gate.status}")
        print(f"Reason: {gate.reason}")

    with out.governance_assessments():
        out.line(
            "Group 27 closure gates summarized",
            StatusMark.DEFER,
            "active O, residual control, count-once, and parent gates remain not ready",
        )


def case_4_rejected_upgrades(upgrades: List[RejectedSummaryUpgrade], out: ScriptOutput) -> None:
    header("Case 4: Rejected summary upgrades")
    for upgrade in upgrades:
        print()
        print("-" * 120)
        print(upgrade.name)
        print("-" * 120)
        print(f"Upgrade: {upgrade.upgrade}")
        print(f"[{status_mark(upgrade.status).value}] {upgrade.name}: {upgrade.status}")
        print(f"Reason: {upgrade.reason}")

    with out.counterexamples():
        out.line(
            "Group 27 summary upgrades rejected",
            StatusMark.FAIL,
            "summary, partial structure, underdetermination, handoff, and parent readiness upgrades are rejected",
        )


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("The Group 27 summary fails if a later script allows:")
    print()
    print("1. Group 27 summary treated as active-O theorem")
    print("2. partial O structure treated as usable operator")
    print("3. controlled underdetermination treated as O impossibility")
    print("4. sector-pairing handoff treated as no-overlap theorem")
    print("5. coefficient-origin handoff treated as insertion theorem")
    print("6. residual-control retest before usable O or alternate structure")
    print("7. parent equation attempted next")
    print("8. recovery-selected O reintroduced")
    print("9. repair-selected O reintroduced")
    print("10. O used in field equations before divergence and guardrail behavior")

    with out.governance_assessments():
        out.line(
            "Group 27 summary failure controls stated",
            StatusMark.OBLIGATION,
            "future work must not upgrade summary or handoff to theorem closure",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Group 27 result:")
    print()
    print("  Active O was not constructed.")
    print("  Candidate domain/codomain and safe trace preservation structure exist.")
    print("  Kernel/image, no-overlap pairing, algebraic law, divergence behavior, and boundary/source/mass behavior remain open.")
    print("  Recovery-selected and repair-selected O are rejected.")
    print("  The obstruction is controlled underdetermination, not O impossibility.")
    print("  O is not usable in residual control or field equations.")
    print()
    print("Preferred next group:")
    print("  28_sector_pairing_and_no_overlap_geometry")
    print()
    print("Alternate next group:")
    print("  28_Bs_Fzeta_coefficient_origin")
    print()
    print("Forbidden next group:")
    print("  parent_field_equation")
    print()
    print("Tiny goblin label:")
    print("  The map names the missing forge.")

    with out.governance_assessments():
        out.line(
            "Group 27 active-O construction summary complete",
            StatusMark.PASS,
            "Group 27 closes as controlled underdetermination with handoff to sector pairing/no-overlap geometry",
        )


def record_derivations(ns) -> None:
    ns.record_derivation(
        derivation_id="g27_status_summary",
        inputs=[
            sp.Symbol("O_not_constructed"),
            sp.Symbol("partial_O_structure"),
            sp.Symbol("pairing_missing"),
            sp.Symbol("alg_law_missing"),
            sp.Symbol("div_missing"),
            sp.Symbol("bsm_missing"),
            sp.Symbol("sector_pairing_handoff_ready"),
        ],
        output=sp.Symbol("g27_summary_complete"),
        method="Group 27 active-O construction status summary",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="summary_marker",
        scope="Group 27 active O construction",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g27_sum_O_open", "Active O remains not constructed"),
        ("g27_sum_pairing_open", "No-overlap pairing remains open"),
        ("g27_sum_alg_open", "O algebraic law remains open"),
        ("g27_sum_div_open", "O divergence behavior remains open"),
        ("g27_sum_bsm_open", "O boundary/source/mass behavior remains open"),
        ("g27_sum_residual_not_ready", "Residual-control retest remains not ready"),
        ("g27_sum_parent_closed", "Parent equation remains closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g27_summary_route"],
            description=(
                "Group 27 closes as controlled underdetermination. This obligation remains open for future constructive work."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g27_sum_O_open",
        "g27_sum_pairing_open",
        "g27_sum_alg_open",
        "g27_sum_div_open",
        "g27_sum_bsm_open",
        "g27_sum_residual_not_ready",
        "g27_sum_parent_closed",
    ]

    ns.record_route(RouteRecord(
        route_id="g27_summary_route",
        script_id=SCRIPT_ID,
        name="Group 27 active-O construction summary",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "Group 27 is treated as controlled underdetermination, not active-O theorem",
            "sector pairing/no-overlap geometry is preferred handoff",
            "B_s/F_zeta coefficient origin remains alternate handoff",
            "residual-control retest and parent equation remain not ready",
        ],
    ))

    for branch_id in [
        "summary_as_O_theorem",
        "partial_structure_as_usable_O",
        "underdetermination_as_impossibility",
        "handoff_as_theorem",
        "coefficient_handoff_as_insertion",
        "residual_retest_before_O",
        "parent_as_next",
        "recovery_selected_O",
        "repair_selected_O",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; Group 27 summary is not active-O construction or downstream closure.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g27_summary_not_O",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Group 27 did not construct active O. Candidate domain/codomain and safe trace preservation structure exist, but kernel/image, "
            "no-overlap pairing, algebraic law, divergence behavior, and boundary/source/mass behavior remain open. "
            "The obstruction is controlled underdetermination, not O impossibility. Preferred handoff is sector pairing/no-overlap geometry; "
            "B_s/F_zeta coefficient origin remains alternate. Residual-control retest and parent equation are not ready."
        ),
        derivation_ids=["g27_status_summary"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Group 27 Status Summary")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    entries = build_summary_entries()
    handoffs = build_handoffs()
    gates = build_gates()
    upgrades = build_rejected_upgrades()

    case_0_problem_statement(out)
    case_1_summary_entries(entries, out)
    case_2_handoffs(handoffs, out)
    case_3_gates(gates, out)
    case_4_rejected_upgrades(upgrades, out)
    case_5_failure_controls(out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
