# Candidate group 30 status summary
#
# Group:
#   30_minimal_coefficient_sector_postulate_inventory
#
# Human title:
#   Minimal Coefficient / Sector Postulate Inventory
#
# Script type:
#   SUMMARY
#
# Purpose
# -------
# Close Group 30 by summarizing the minimal coefficient/sector postulate inventory.
#
# Locked-door question:
#
#   What did the minimal coefficient/sector postulate inventory establish?
#
# This script does not adopt a new postulate.
# It does not derive B_s/F_zeta insertion.
# It does not derive no-overlap sector geometry.
# It does not construct active O.
# It does not derive residual control.
# It does not open the parent equation.
#
# Tiny goblin rule:
#
#   The teeth are sorted; the key is not cut.

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
        "ADMISSIBLE_CANDIDATE": StatusMark.INFO,
        "HANDOFF_READY": StatusMark.PASS,
        "HIGH_RISK": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_IDENTIFIED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "SUMMARY": StatusMark.PASS,
        "THEOREM_ROUTE_PREFERRED": StatusMark.INFO,
        "UNDERDETERMINED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g30_obligations",
            "30_minimal_coefficient_sector_postulate_inventory__candidate_minimal_postulate_obligations",
            "g30_obligations",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_obstruction",
            "30_minimal_coefficient_sector_postulate_inventory__candidate_minimal_postulate_set_obstruction",
            "g30_postulate_set_obstruction",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_isd",
            "30_minimal_coefficient_sector_postulate_inventory__candidate_incidence_source_divergence_postulate_inventory",
            "g30_incidence_source_divergence",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_safe_membership",
            "30_minimal_coefficient_sector_postulate_inventory__candidate_safe_trace_membership_postulate",
            "g30_safe_membership",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_trace_norm",
            "30_minimal_coefficient_sector_postulate_inventory__candidate_trace_normalization_postulate",
            "g30_trace_normalization",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_filter",
            "30_minimal_coefficient_sector_postulate_inventory__candidate_postulate_smuggling_filter",
            "g30_postulate_smuggling_filter",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_minimality",
            "30_minimal_coefficient_sector_postulate_inventory__candidate_postulate_minimality_tests",
            "g30_postulate_minimality",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_problem",
            "30_minimal_coefficient_sector_postulate_inventory__candidate_minimal_postulate_problem_ledger",
            "g30_postulate_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g29_summary",
            "29_Bs_Fzeta_coefficient_origin__candidate_group_29_status_summary",
            "g29_status_summary",
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
    caution: str


@dataclass
class FinalGate:
    name: str
    status: str
    reason: str


@dataclass
class RejectedUpgrade:
    name: str
    upgrade: str
    status: str
    reason: str


def build_summary_entries() -> List[SummaryEntry]:
    return [
        SummaryEntry(
            name="G30-1: inventory route",
            topic="minimal coefficient/sector postulate inventory",
            status="SUMMARY",
            result="explicit-choice inventory opened without adoption",
        ),
        SummaryEntry(
            name="G30-2: trace normalization",
            topic="how B_s reads zeta",
            status="ADMISSIBLE_CANDIDATE",
            result="survives as narrow candidate and theorem target; not adopted",
        ),
        SummaryEntry(
            name="G30-3: safe trace membership",
            topic="zeta_Bs -> T_zeta",
            status="ADMISSIBLE_CANDIDATE",
            result="survives as narrow candidate and theorem target; not adopted",
        ),
        SummaryEntry(
            name="G30-4: guardrail visibility",
            topic="boundary/current/mass/support non-reservoir visibility",
            status="ADMISSIBLE_CANDIDATE",
            result="survives as narrow candidate; not neutrality theorem",
        ),
        SummaryEntry(
            name="G30-5: divergence explicitness",
            topic="explicit/auditable/non-reservoir correction rule",
            status="ADMISSIBLE_CANDIDATE",
            result="survives as narrow candidate; not divergence-safe coefficient law",
        ),
        SummaryEntry(
            name="G30-6: source no-double-counting",
            topic="ordinary source load enters once",
            status="THEOREM_ROUTE_PREFERRED",
            result="should be pursued via source/divergence coefficient law before postulating",
        ),
        SummaryEntry(
            name="G30-7: trace/residual incidence",
            topic="I(T_zeta,R_zeta)=0 and I(T_zeta,R_kappa)=0",
            status="HIGH_RISK",
            result="not adopted; too close to no-overlap/residual-control smuggling",
        ),
        SummaryEntry(
            name="G30-8: minimal set",
            topic="complete minimal admissible postulate set",
            status="NOT_IDENTIFIED",
            result="candidate inventory narrowed but no set chosen",
        ),
        SummaryEntry(
            name="G30-9: downstream gates",
            topic="B_s/F_zeta insertion, active O, residual control, parent equation",
            status="NOT_READY",
            result="all remain closed",
        ),
    ]


def build_handoffs() -> List[FinalHandoff]:
    return [
        FinalHandoff(
            name="H1: preferred next group",
            route="31_source_divergence_coefficient_law",
            status="HANDOFF_READY",
            reason="source no-double-counting and divergence-safe coefficient law remain theorem-route preferred",
            caution="must not hide source load or correction load",
        ),
        FinalHandoff(
            name="H2: explicit-choice route",
            route="31_explicit_minimal_postulate_selection",
            status="OPEN",
            reason="admissible candidates exist but no set is adopted",
            caution="requires explicit user/theory decision; survival is not adoption",
        ),
        FinalHandoff(
            name="H3: trace-normalization route",
            route="31_trace_normalization_choice_or_theorem",
            status="OPEN",
            reason="trace normalization remains admissible candidate and theorem target",
            caution="must not be recovery-selected",
        ),
        FinalHandoff(
            name="H4: safe-membership route",
            route="31_safe_trace_membership_choice_or_theorem",
            status="OPEN",
            reason="safe membership remains admissible candidate and theorem target",
            caution="must not imply incidence/no-overlap/residual control",
        ),
        FinalHandoff(
            name="H5: insertion theorem",
            route="31_Bs_Fzeta_insertion_theorem",
            status="NOT_READY",
            reason="coefficient/source/divergence/membership/incidence gates remain open",
            caution="forbidden as immediate next group",
        ),
        FinalHandoff(
            name="H6: parent field equation",
            route="parent_field_equation",
            status="NOT_READY",
            reason="upstream gates remain open",
            caution="forbidden as next group",
        ),
    ]


def build_gates() -> List[FinalGate]:
    return [
        FinalGate(
            name="Postulate adoption",
            status="NOT_ADOPTED",
            reason="Group 30 is inventory/obstruction, not selection",
        ),
        FinalGate(
            name="Minimal admissible postulate set",
            status="UNDERDETERMINED",
            reason="complete minimal set not identified",
        ),
        FinalGate(
            name="Trace normalization",
            status="ADMISSIBLE_CANDIDATE",
            reason="narrow candidate only; may remain theorem target",
        ),
        FinalGate(
            name="Safe trace membership",
            status="ADMISSIBLE_CANDIDATE",
            reason="narrow zeta_Bs -> T_zeta candidate only",
        ),
        FinalGate(
            name="Trace/residual incidence",
            status="HIGH_RISK",
            reason="too close to no-overlap/residual control",
        ),
        FinalGate(
            name="Source no-double-counting",
            status="THEOREM_ROUTE_PREFERRED",
            reason="preferred next theorem route",
        ),
        FinalGate(
            name="Divergence-safe coefficient law",
            status="THEOREM_ROUTE_PREFERRED",
            reason="preferred next theorem route",
        ),
        FinalGate(
            name="B_s/F_zeta insertion",
            status="NOT_READY",
            reason="upstream coefficient/source/divergence/membership/incidence gates open",
        ),
        FinalGate(
            name="Active O / residual control",
            status="NOT_READY",
            reason="postulate inventory does not derive operator or residual control",
        ),
        FinalGate(
            name="Parent equation",
            status="NOT_READY",
            reason="parent gate remains closed",
        ),
    ]


def build_rejected() -> List[RejectedUpgrade]:
    return [
        RejectedUpgrade(
            name="U1: candidate survival as adoption",
            upgrade="surviving admissibility filters treated as adopted postulate",
            status="REJECTED",
            reason="survival is not adoption",
        ),
        RejectedUpgrade(
            name="U2: inventory as minimal set",
            upgrade="candidate inventory treated as complete minimal set",
            status="REJECTED",
            reason="minimal set remains underdetermined",
        ),
        RejectedUpgrade(
            name="U3: incidence as no-overlap",
            upgrade="trace/residual incidence treated as no-overlap theorem",
            status="REJECTED",
            reason="incidence remains high-risk",
        ),
        RejectedUpgrade(
            name="U4: source/divergence as insertion",
            upgrade="source/divergence discipline treated as B_s/F_zeta insertion",
            status="REJECTED",
            reason="source/divergence is not insertion",
        ),
        RejectedUpgrade(
            name="U5: divergence explicitness as divergence safety",
            upgrade="explicit correction visibility treated as divergence-safe coefficient law",
            status="REJECTED",
            reason="explicitness is weaker than safety theorem",
        ),
        RejectedUpgrade(
            name="U6: bundle as closure",
            upgrade="postulate bundle treated as insertion, active O, residual control, or parent readiness",
            status="REJECTED",
            reason="endpoint-selected closure bundle",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Group 30 summary problem")
    print("Question:")
    print()
    print("  What did the minimal coefficient/sector postulate inventory establish?")
    print()
    print("Discipline:")
    print()
    print("  This is a group status summary, not postulate adoption.")
    print("  The teeth are sorted; the key is not cut.")

    with out.governance_assessments():
        out.line(
            "Group 30 status summary opened",
            StatusMark.INFO,
            "summarizing minimal postulate inventory and handoff state",
        )


def case_1_summary(entries: List[SummaryEntry], out: ScriptOutput) -> None:
    header("Case 1: Group 30 status entries")
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
            "Group 30 status entries summarized",
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
        print(f"Caution: {handoff.caution}")

    with out.governance_assessments():
        out.line(
            "Group 30 handoffs summarized",
            StatusMark.PASS,
            "source/divergence coefficient law is preferred next group",
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
            "Group 30 final gates summarized",
            StatusMark.DEFER,
            "no postulate adopted; source/divergence theorem route handoff-ready; downstream gates closed",
        )


def case_4_rejected(upgrades: List[RejectedUpgrade], out: ScriptOutput) -> None:
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
            "Group 30 rejected upgrades summarized",
            StatusMark.FAIL,
            "candidate survival, inventory, incidence, source/divergence, explicitness, and bundle upgrades rejected",
        )


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("The Group 30 summary fails if later scripts allow:")
    print()
    print("1. candidate survival as adoption")
    print("2. inventory as minimal set")
    print("3. trace/residual incidence as no-overlap")
    print("4. source/divergence discipline as insertion")
    print("5. divergence explicitness as divergence-safe coefficient law")
    print("6. bundle as closure")
    print("7. immediate B_s/F_zeta insertion theorem")
    print("8. active O rebuild")
    print("9. residual-control retest")
    print("10. parent field equation")

    with out.governance_assessments():
        out.line(
            "Group 30 failure controls stated",
            StatusMark.OBLIGATION,
            "future work must not upgrade inventory to adoption or theorem closure",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Group 30 result:")
    print()
    print("  Minimal coefficient/sector postulate inventory clarified the explicit-choice landscape.")
    print("  No postulate is adopted.")
    print("  A complete minimal admissible postulate set is not identified.")
    print("  The admissible core candidates are:")
    print("    trace normalization;")
    print("    safe trace membership;")
    print("    guardrail visibility;")
    print("    divergence explicitness.")
    print("  Source no-double-counting and divergence-safe coefficient law remain theorem-route preferred.")
    print("  Trace/residual incidence remains high-risk.")
    print("  B_s/F_zeta insertion is not derived.")
    print("  Active O, residual control, and parent equation remain not ready.")
    print()
    print("Preferred next group:")
    print("  31_source_divergence_coefficient_law")
    print()
    print("Explicit-choice route only by explicit user/theory decision:")
    print("  31_explicit_minimal_postulate_selection")
    print()
    print("Forbidden next groups:")
    print("  31_Bs_Fzeta_insertion_theorem")
    print("  active_O_rebuild")
    print("  residual_control_retest")
    print("  parent_field_equation")
    print()
    print("Tiny goblin label:")
    print("  The teeth are sorted; the key is not cut.")

    with out.governance_assessments():
        out.line(
            "Group 30 minimal postulate inventory summary complete",
            StatusMark.PASS,
            "Group 30 closes as inventory/obstruction with handoff to source/divergence coefficient law",
        )


def record_derivations(ns) -> None:
    ns.record_derivation(
        derivation_id="g30_status_summary",
        inputs=[
            sp.Symbol("no_postulate_adopted"),
            sp.Symbol("admissible_core_candidates"),
            sp.Symbol("minimal_set_not_identified"),
            sp.Symbol("source_divergence_theorem_route_preferred"),
            sp.Symbol("incidence_high_risk"),
            sp.Symbol("downstream_gates_closed"),
        ],
        output=sp.Symbol("g30_summary_complete"),
        method="Group 30 minimal coefficient/sector postulate inventory status summary",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="summary_marker",
        scope="Group 30 minimal coefficient/sector postulate inventory",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g30_sum_no_adoption", "No postulate adopted"),
        ("g30_sum_admissible_core", "Admissible core remains candidate only"),
        ("g30_sum_minimal_set", "Minimal admissible postulate set not identified"),
        ("g30_sum_source_div", "Source/divergence coefficient law is preferred next group"),
        ("g30_sum_explicit_choice", "Explicit postulate selection requires explicit user/theory decision"),
        ("g30_sum_incidence", "Trace/residual incidence remains high-risk"),
        ("g30_sum_downstream", "Insertion/O/residual/parent gates remain closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g30_summary_route"],
            description=(
                "Group 30 closes as inventory/obstruction. No postulate is adopted and downstream gates remain closed."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g30_sum_no_adoption",
        "g30_sum_admissible_core",
        "g30_sum_minimal_set",
        "g30_sum_source_div",
        "g30_sum_explicit_choice",
        "g30_sum_incidence",
        "g30_sum_downstream",
    ]

    ns.record_route(RouteRecord(
        route_id="g30_summary_route",
        script_id=SCRIPT_ID,
        name="Group 30 minimal postulate inventory summary",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "no postulate adopted",
            "admissible core remains candidate only",
            "minimal set not identified",
            "source/divergence coefficient law is preferred next group",
            "explicit postulate selection requires explicit user/theory decision",
            "downstream gates remain closed",
        ],
    ))

    for branch_id in [
        "candidate_survival_as_adoption",
        "inventory_as_minimal_set",
        "incidence_as_no_overlap",
        "source_divergence_as_insertion",
        "divergence_explicit_as_divergence_safety",
        "bundle_as_closure",
        "insertion_attempt_next",
        "active_O_rebuild_next",
        "residual_control_retest_next",
        "parent_as_next",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; Group 30 summary is not adoption or theorem closure.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g30_summary_inventory_obstruction",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Group 30 clarified the minimal coefficient/sector postulate inventory but adopted no postulate. A complete minimal admissible postulate set is not identified. "
            "The admissible core candidates are trace normalization, safe trace membership, guardrail visibility, and divergence explicitness. "
            "Source no-double-counting and divergence-safe coefficient law remain theorem-route preferred. Trace/residual incidence remains high-risk. "
            "B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready. Preferred next group is 31_source_divergence_coefficient_law. "
            "Explicit postulate selection requires explicit user/theory decision."
        ),
        derivation_ids=["g30_status_summary"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Group 30 Status Summary")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    entries = build_summary_entries()
    handoffs = build_handoffs()
    gates = build_gates()
    rejected = build_rejected()

    case_0_problem_statement(out)
    case_1_summary(entries, out)
    case_2_handoffs(handoffs, out)
    case_3_gates(gates, out)
    case_4_rejected(rejected, out)
    case_5_failure_controls(out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
