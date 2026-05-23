# Candidate group 31 status summary
#
# Group:
#   31_source_divergence_coefficient_law
#
# Human title:
#   Source / Divergence Coefficient Law
#
# Script type:
#   SUMMARY
#
# Purpose
# -------
# Close Group 31 by summarizing the source/divergence coefficient-law theorem route.
#
# Locked-door question:
#
#   What did the source/divergence coefficient-law route establish?
#
# This script does not adopt a new postulate.
# It does not derive the complete coefficient law.
# It does not derive B_s/F_zeta insertion.
# It does not construct active O.
# It does not derive residual control.
# It does not open the parent equation.
#
# Tiny goblin rule:
#
#   The channels are clean; the river is still unmapped.

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
        "CANDIDATE_REMAINS": StatusMark.DEFER,
        "HANDOFF_READY": StatusMark.PASS,
        "HIGH_RISK": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "PARTIAL_CONSTRAINT": StatusMark.INFO,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "SUMMARY": StatusMark.PASS,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g31_obligations",
            "031_source_divergence_coefficient_law__candidate_source_divergence_obligations",
            "g31_obligations",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_trace_norm",
            "031_source_divergence_coefficient_law__candidate_trace_normalization_from_source_divergence",
            "g31_trace_normalization_fork",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_classifier",
            "031_source_divergence_coefficient_law__candidate_source_divergence_coefficient_law_classifier",
            "g31_source_divergence_classifier",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_explicitness",
            "031_source_divergence_coefficient_law__candidate_nonreservoir_divergence_explicitness",
            "g31_nonreservoir_explicitness",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_div_res",
            "031_source_divergence_coefficient_law__candidate_divergence_reservoir_obstruction",
            "g31_divergence_reservoir",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_coeff",
            "031_source_divergence_coefficient_law__candidate_coefficient_source_no_double_counting_tests",
            "g31_coeff_source_tests",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_dup",
            "031_source_divergence_coefficient_law__candidate_source_duplicate_load_ledger",
            "g31_source_duplicate_ledger",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_problem",
            "031_source_divergence_coefficient_law__candidate_source_divergence_problem_ledger",
            "g31_source_divergence_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_summary",
            "030_minimal_coefficient_sector_postulate_inventory__candidate_group_30_status_summary",
            "g30_status_summary",
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
class FinalGap:
    name: str
    status: str
    reason: str


@dataclass
class FinalHandoff:
    name: str
    route: str
    status: str
    reason: str
    caution: str


@dataclass
class RejectedUpgrade:
    name: str
    upgrade: str
    status: str
    reason: str


def build_summary_entries() -> List[SummaryEntry]:
    return [
        SummaryEntry(
            name="G31-1: source/divergence route",
            topic="source/divergence coefficient-law theorem route",
            status="SUMMARY",
            result="opened and completed as partial-constraint route, not full coefficient law",
        ),
        SummaryEntry(
            name="G31-2: duplicate source channels",
            topic="coefficient/residual/boundary/support/correction/exchange/curvature/parent pockets",
            status="PARTIAL_CONSTRAINT",
            result="hidden ordinary source pockets named and forbidden as shortcuts",
        ),
        SummaryEntry(
            name="G31-3: coefficient source neutrality",
            topic="coefficient-side ordinary rho/M_enc load",
            status="PARTIAL_CONSTRAINT",
            result="coefficient may not carry ordinary source load",
        ),
        SummaryEntry(
            name="G31-4: divergence reservoir",
            topic="correction/divergence hidden reservoir",
            status="PARTIAL_CONSTRAINT",
            result="source/boundary/current/mass/support/residual/parent reservoirs rejected",
        ),
        SummaryEntry(
            name="G31-5: non-reservoir explicitness",
            topic="visible auditable correction accounting",
            status="PARTIAL_CONSTRAINT",
            result="admissible discipline, weaker than divergence-safe coefficient law",
        ),
        SummaryEntry(
            name="G31-6: coefficient law",
            topic="complete B_s/F_zeta coefficient law",
            status="NOT_DERIVED",
            result="not derived; source/divergence gives constraints only",
        ),
        SummaryEntry(
            name="G31-7: trace normalization",
            topic="how B_s reads zeta",
            status="CANDIDATE_REMAINS",
            result="not derived; remains open candidate/theorem target",
        ),
        SummaryEntry(
            name="G31-8: safe trace membership",
            topic="zeta_Bs -> T_zeta",
            status="OPEN",
            result="not derived; remains separate open gap",
        ),
        SummaryEntry(
            name="G31-9: trace/residual incidence",
            topic="I(T_zeta,R_zeta)=0 and I(T_zeta,R_kappa)=0",
            status="HIGH_RISK",
            result="not derived; remains high-risk",
        ),
        SummaryEntry(
            name="G31-10: postulate adoption",
            topic="Group 30 candidate postulates",
            status="NOT_ADOPTED",
            result="none adopted by Group 31",
        ),
        SummaryEntry(
            name="G31-11: downstream gates",
            topic="B_s/F_zeta insertion, active O, residual control, parent equation",
            status="NOT_READY",
            result="all remain closed",
        ),
    ]


def build_gaps() -> List[FinalGap]:
    return [
        FinalGap(
            name="Complete coefficient law",
            status="NOT_DERIVED",
            reason="normalization, membership, incidence, and insertion gaps remain",
        ),
        FinalGap(
            name="Source no-double-counting theorem",
            status="NOT_DERIVED",
            reason="hidden channels are rejected but full sector-by-sector theorem is not complete",
        ),
        FinalGap(
            name="Divergence-safe coefficient law",
            status="NOT_DERIVED",
            reason="non-reservoir explicitness is weaker than full divergence-safe law",
        ),
        FinalGap(
            name="Trace normalization",
            status="CANDIDATE_REMAINS",
            reason="source/divergence constraints do not determine how B_s reads zeta",
        ),
        FinalGap(
            name="Safe trace membership",
            status="OPEN",
            reason="source/divergence constraints do not derive zeta_Bs -> T_zeta",
        ),
        FinalGap(
            name="Trace/residual incidence",
            status="HIGH_RISK",
            reason="not derived and still too close to no-overlap/residual-control smuggling",
        ),
        FinalGap(
            name="B_s/F_zeta insertion",
            status="NOT_READY",
            reason="coefficient law and upstream gates remain open",
        ),
        FinalGap(
            name="Parent equation",
            status="NOT_READY",
            reason="parent gate remains closed",
        ),
    ]


def build_handoffs() -> List[FinalHandoff]:
    return [
        FinalHandoff(
            name="H1: explicit-choice route",
            route="032_explicit_minimal_postulate_selection",
            status="OPEN",
            reason="source/divergence did not derive full coefficient law and trace normalization remains open",
            caution="requires explicit user/theory decision; no automatic adoption",
        ),
        FinalHandoff(
            name="H2: trace-normalization theorem route",
            route="032_trace_normalization_theorem",
            status="OPEN",
            reason="N_trace remains theorem target/candidate",
            caution="must not be recovery-selected or repair-selected",
        ),
        FinalHandoff(
            name="H3: safe-membership theorem route",
            route="032_safe_trace_membership_theorem",
            status="OPEN",
            reason="safe membership remains separate and open",
            caution="must not imply no-overlap or residual control unless derived",
        ),
        FinalHandoff(
            name="H4: source/divergence obstruction summary",
            route="032_source_divergence_obstruction_summary",
            status="OPEN",
            reason="Group 31 closed as partial constraints only",
            caution="must not recast obstruction as law",
        ),
        FinalHandoff(
            name="H5: insertion theorem",
            route="032_Bs_Fzeta_insertion_theorem",
            status="NOT_READY",
            reason="normalization, membership, incidence, and coefficient law gaps remain",
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


def build_rejected() -> List[RejectedUpgrade]:
    return [
        RejectedUpgrade(
            name="U1: partial constraints as coefficient law",
            upgrade="Group 31 partial constraints treated as complete B_s/F_zeta coefficient law",
            status="REJECTED",
            reason="normalization, membership, incidence, and insertion gaps remain",
        ),
        RejectedUpgrade(
            name="U2: source neutrality as full source theorem",
            upgrade="coefficient source neutrality treated as full source no-double-counting",
            status="REJECTED",
            reason="sector-by-sector theorem not complete",
        ),
        RejectedUpgrade(
            name="U3: explicitness as divergence-safe law",
            upgrade="non-reservoir explicitness treated as divergence-safe coefficient law",
            status="REJECTED",
            reason="explicitness is weaker than divergence safety",
        ),
        RejectedUpgrade(
            name="U4: trace normalization open as adoption",
            upgrade="trace normalization remains open, therefore adopt it",
            status="REJECTED",
            reason="open candidate is not adoption",
        ),
        RejectedUpgrade(
            name="U5: source/divergence as insertion",
            upgrade="source/divergence discipline treated as B_s/F_zeta insertion",
            status="REJECTED",
            reason="insertion gap remains",
        ),
        RejectedUpgrade(
            name="U6: source/divergence as parent readiness",
            upgrade="partial coefficient discipline opens parent equation",
            status="REJECTED",
            reason="parent gate remains closed",
        ),
        RejectedUpgrade(
            name="U7: summary as postulate adoption",
            upgrade="Group 31 summary adopts Group 30 candidates",
            status="REJECTED",
            reason="summary is not explicit postulate selection",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Group 31 summary problem")
    print("Question:")
    print()
    print("  What did the source/divergence coefficient-law route establish?")
    print()
    print("Discipline:")
    print()
    print("  This is a group status summary.")
    print("  It derives no coefficient law.")
    print("  It adopts no postulate.")
    print()
    print("Tiny goblin rule:")
    print("  The channels are clean; the river is still unmapped.")

    with out.governance_assessments():
        out.line(
            "Group 31 status summary opened",
            StatusMark.INFO,
            "summarizing source/divergence route as partial constraints",
        )


def case_1_summary(entries: List[SummaryEntry], out: ScriptOutput) -> None:
    header("Case 1: Group 31 status entries")
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
            "Group 31 status entries summarized",
            StatusMark.PASS,
            f"{len(entries)} status entries summarized",
        )


def case_2_gaps(gaps: List[FinalGap], out: ScriptOutput) -> None:
    header("Case 2: Final open gaps")
    for gap in gaps:
        print()
        print("-" * 120)
        print(gap.name)
        print("-" * 120)
        print(f"[{status_mark(gap.status).value}] {gap.name}: {gap.status}")
        print(f"Reason: {gap.reason}")

    with out.unresolved_obligations():
        out.line(
            "Group 31 final gaps summarized",
            StatusMark.OBLIGATION,
            f"{len(gaps)} final gaps remain",
        )


def case_3_handoffs(handoffs: List[FinalHandoff], out: ScriptOutput) -> None:
    header("Case 3: Final handoffs")
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
            "Group 31 handoffs summarized",
            StatusMark.PASS,
            "next route requires deliberate choice among open theorem/choice paths",
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
            "Group 31 rejected upgrades summarized",
            StatusMark.FAIL,
            "law, source theorem, divergence safety, adoption, insertion, and parent upgrades rejected",
        )


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("The Group 31 summary fails if later scripts allow:")
    print()
    print("1. partial constraints as complete coefficient law")
    print("2. coefficient source neutrality as full source no-double-counting theorem")
    print("3. non-reservoir explicitness as divergence-safe coefficient law")
    print("4. trace-normalization open status as adoption")
    print("5. source/divergence discipline as B_s/F_zeta insertion")
    print("6. source/divergence discipline as parent readiness")
    print("7. summary as postulate adoption")
    print("8. immediate insertion theorem")
    print("9. active O rebuild")
    print("10. residual-control retest")
    print("11. parent field equation")

    with out.governance_assessments():
        out.line(
            "Group 31 failure controls stated",
            StatusMark.OBLIGATION,
            "future work must not upgrade partial constraints to law or closure",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Group 31 result:")
    print()
    print("  Source/divergence coefficient-law route produced partial constraints only.")
    print("  It ruled out hidden ordinary source carriers.")
    print("  It ruled out hidden divergence reservoirs.")
    print("  It required visible, auditable, non-reservoir correction discipline.")
    print("  It did not derive complete B_s/F_zeta coefficient law.")
    print("  It did not derive trace normalization.")
    print("  It did not derive safe trace membership.")
    print("  It did not derive trace/residual incidence.")
    print("  It did not derive B_s/F_zeta insertion.")
    print("  No Group 30 candidate postulate is adopted.")
    print("  Active O, residual control, and parent equation remain not ready.")
    print()
    print("Open next routes:")
    print("  32_explicit_minimal_postulate_selection")
    print("  32_trace_normalization_theorem")
    print("  32_safe_trace_membership_theorem")
    print("  32_source_divergence_obstruction_summary")
    print()
    print("Forbidden immediate routes:")
    print("  32_Bs_Fzeta_insertion_theorem")
    print("  active_O_rebuild")
    print("  residual_control_retest")
    print("  parent_field_equation")
    print()
    print("Tiny goblin label:")
    print("  The channels are clean; the river is still unmapped.")

    with out.governance_assessments():
        out.line(
            "Group 31 source/divergence summary complete",
            StatusMark.PASS,
            "Group 31 closes as partial-constraint result",
        )


def record_derivations(ns) -> None:
    ns.record_derivation(
        derivation_id="g31_status_summary",
        inputs=[
            sp.Symbol("partial_source_divergence_constraints"),
            sp.Symbol("hidden_source_carriers_rejected"),
            sp.Symbol("hidden_reservoirs_rejected"),
            sp.Symbol("coefficient_law_not_derived"),
            sp.Symbol("trace_normalization_open"),
            sp.Symbol("insertion_not_ready"),
        ],
        output=sp.Symbol("g31_summary_complete"),
        method="Group 31 source/divergence coefficient-law status summary",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="summary_marker",
        scope="Group 31 source/divergence coefficient law",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g31_sum_partial_only", "Preserve Group 31 as partial constraints only"),
        ("g31_sum_no_coeff_law", "Do not claim complete coefficient law"),
        ("g31_sum_trace_norm_open", "Keep trace normalization open"),
        ("g31_sum_membership_open", "Keep safe trace membership open"),
        ("g31_sum_incidence_high_risk", "Keep trace/residual incidence high-risk"),
        ("g31_sum_no_postulate", "Do not adopt Group 30 candidates"),
        ("g31_sum_no_insertion", "Do not claim B_s/F_zeta insertion"),
        ("g31_sum_next_choice", "Choose next route deliberately"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g31_summary_route"],
            description=(
                "Group 31 closes as partial constraints only. Coefficient law and insertion are not derived."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g31_sum_partial_only",
        "g31_sum_no_coeff_law",
        "g31_sum_trace_norm_open",
        "g31_sum_membership_open",
        "g31_sum_incidence_high_risk",
        "g31_sum_no_postulate",
        "g31_sum_no_insertion",
        "g31_sum_next_choice",
    ]

    ns.record_route(RouteRecord(
        route_id="g31_summary_route",
        script_id=SCRIPT_ID,
        name="Group 31 source/divergence status summary",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "Group 31 partial constraints summarized",
            "coefficient law not derived",
            "trace normalization open",
            "safe membership open",
            "trace/residual incidence high-risk",
            "no postulate adopted",
            "insertion/O/residual/parent gates closed",
        ],
    ))

    for branch_id in [
        "partial_constraints_as_coefficient_law",
        "source_neutrality_as_full_source_theorem",
        "explicitness_as_divergence_safe_law",
        "trace_normalization_open_as_adoption",
        "source_divergence_as_insertion",
        "source_divergence_as_parent_readiness",
        "summary_as_postulate_adoption",
        "summary_as_active_O_readiness",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; Group 31 summary is not theorem closure or adoption.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g31_summary_partial_constraint_result",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Group 31 source/divergence coefficient-law route produced partial constraints only. It ruled out hidden ordinary source carriers and hidden divergence reservoirs, and required visible, auditable, non-reservoir correction discipline. "
            "It did not derive complete B_s/F_zeta coefficient law, trace normalization, safe trace membership, trace/residual incidence, or B_s/F_zeta insertion. "
            "No Group 30 candidate postulate is adopted. Active O, residual control, and parent equation remain not ready."
        ),
        derivation_ids=["g31_status_summary"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Group 31 Status Summary")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    entries = build_summary_entries()
    gaps = build_gaps()
    handoffs = build_handoffs()
    rejected = build_rejected()

    case_0_problem_statement(out)
    case_1_summary(entries, out)
    case_2_gaps(gaps, out)
    case_3_handoffs(handoffs, out)
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
