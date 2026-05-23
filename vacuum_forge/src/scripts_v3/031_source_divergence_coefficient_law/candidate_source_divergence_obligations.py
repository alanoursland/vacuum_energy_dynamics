# Candidate source divergence obligations
#
# Group:
#   31_source_divergence_coefficient_law
#
# Script type:
#   OBLIGATION / HANDOFF SUMMARY
#
# Purpose
# -------
# Summarize Group 31 partial constraints, unresolved gaps, and safe handoffs.
#
# Locked-door question:
#
#   What did the source/divergence coefficient-law route clarify,
#   and what remains open?
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
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "PARTIAL_CONSTRAINT": StatusMark.INFO,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "UNDERDETERMINED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g31_trace_norm",
            "31_source_divergence_coefficient_law__candidate_trace_normalization_from_source_divergence",
            "g31_trace_normalization_fork",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_classifier",
            "31_source_divergence_coefficient_law__candidate_source_divergence_coefficient_law_classifier",
            "g31_source_divergence_classifier",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_explicitness",
            "31_source_divergence_coefficient_law__candidate_nonreservoir_divergence_explicitness",
            "g31_nonreservoir_explicitness",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_div_res",
            "31_source_divergence_coefficient_law__candidate_divergence_reservoir_obstruction",
            "g31_divergence_reservoir",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_coeff",
            "31_source_divergence_coefficient_law__candidate_coefficient_source_no_double_counting_tests",
            "g31_coeff_source_tests",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_dup",
            "31_source_divergence_coefficient_law__candidate_source_duplicate_load_ledger",
            "g31_source_duplicate_ledger",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_problem",
            "31_source_divergence_coefficient_law__candidate_source_divergence_problem_ledger",
            "g31_source_divergence_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_summary",
            "30_minimal_coefficient_sector_postulate_inventory__candidate_group_30_status_summary",
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
class ClarifiedItem:
    name: str
    item: str
    status: str
    meaning: str


@dataclass
class OpenGap:
    name: str
    gap: str
    status: str
    current_result: str
    discipline: str


@dataclass
class Handoff:
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


@dataclass
class ObligationConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_clarified_items() -> List[ClarifiedItem]:
    return [
        ClarifiedItem(
            name="D1: duplicate-source pockets",
            item="coefficient/residual/boundary/support/correction/exchange/curvature/parent source pockets",
            status="PARTIAL_CONSTRAINT",
            meaning="all named; no hidden source pocket may be used as shortcut",
        ),
        ClarifiedItem(
            name="D2: coefficient source neutrality",
            item="coefficient-side ordinary rho/M_enc load",
            status="PARTIAL_CONSTRAINT",
            meaning="coefficient may not carry ordinary source load",
        ),
        ClarifiedItem(
            name="D3: divergence reservoir obstruction",
            item="correction cannot hide source/boundary/current/mass/support/residual/parent load",
            status="PARTIAL_CONSTRAINT",
            meaning="reservoir routes rejected",
        ),
        ClarifiedItem(
            name="D4: non-reservoir explicitness",
            item="visible, auditable correction accounting",
            status="PARTIAL_CONSTRAINT",
            meaning="admissible discipline, weaker than divergence-safe coefficient law",
        ),
        ClarifiedItem(
            name="D5: source/divergence classifier",
            item="complete coefficient law status",
            status="NOT_DERIVED",
            meaning="source/divergence gives partial constraints, not full coefficient law",
        ),
        ClarifiedItem(
            name="D6: trace normalization fork",
            item="how B_s reads zeta",
            status="CANDIDATE_REMAINS",
            meaning="not derived by source/divergence; remains open candidate/theorem target",
        ),
        ClarifiedItem(
            name="D7: postulate status",
            item="Group 30 candidate postulates",
            status="NOT_ADOPTED",
            meaning="no candidate postulate adopted by Group 31",
        ),
        ClarifiedItem(
            name="D8: downstream gates",
            item="B_s/F_zeta insertion, active O, residual control, parent equation",
            status="NOT_READY",
            meaning="all remain closed",
        ),
    ]


def build_open_gaps() -> List[OpenGap]:
    return [
        OpenGap(
            name="G1: complete coefficient law",
            gap="complete B_s/F_zeta coefficient law",
            status="NOT_DERIVED",
            current_result="partial source/divergence constraints only",
            discipline="do not treat constraints as law",
        ),
        OpenGap(
            name="G2: trace normalization",
            gap="N_trace / how B_s reads zeta",
            status="OPEN",
            current_result="not fixed by source/divergence",
            discipline="do not select from recovery or repair",
        ),
        OpenGap(
            name="G3: safe trace membership",
            gap="zeta_Bs -> T_zeta",
            status="OPEN",
            current_result="not derived by source/divergence",
            discipline="do not smuggle no-overlap",
        ),
        OpenGap(
            name="G4: trace/residual incidence",
            gap="I(T_zeta,R_zeta)=0 and I(T_zeta,R_kappa)=0",
            status="OPEN",
            current_result="not derived; remains high-risk",
            discipline="do not use as residual control",
        ),
        OpenGap(
            name="G5: source no-double-counting theorem",
            gap="full sector-by-sector source no-double-counting",
            status="OPEN",
            current_result="coefficient source carrier and hidden pockets rejected, but theorem not complete",
            discipline="no total cancellation shortcut",
        ),
        OpenGap(
            name="G6: divergence-safe coefficient law",
            gap="full divergence-safe coefficient behavior",
            status="OPEN",
            current_result="reservoir and hidden correction routes rejected, but law not complete",
            discipline="explicitness is not full safety",
        ),
        OpenGap(
            name="G7: insertion",
            gap="B_s/F_zeta insertion",
            status="NOT_READY",
            current_result="not derived",
            discipline="partial constraints are not insertion",
        ),
    ]


def build_handoffs() -> List[Handoff]:
    return [
        Handoff(
            name="H1: status summary",
            route="candidate_group_31_status_summary.py",
            status="HANDOFF_READY",
            reason="Group 31 has enough results to close as partial-constraint/obligation summary",
            caution="must not overclaim law or insertion",
        ),
        Handoff(
            name="H2: explicit minimal postulate selection",
            route="32_explicit_minimal_postulate_selection",
            status="OPEN",
            reason="source/divergence did not derive full law and trace normalization remains open",
            caution="requires explicit user/theory decision; no automatic adoption",
        ),
        Handoff(
            name="H3: trace-normalization theorem route",
            route="32_trace_normalization_theorem",
            status="OPEN",
            reason="N_trace remains theorem target/candidate",
            caution="must not be recovery-selected or repair-selected",
        ),
        Handoff(
            name="H4: safe-membership theorem route",
            route="32_safe_trace_membership_theorem",
            status="OPEN",
            reason="safe membership remains separate and open",
            caution="must not imply no-overlap or residual control unless derived",
        ),
        Handoff(
            name="H5: insertion theorem",
            route="32_Bs_Fzeta_insertion_theorem",
            status="NOT_READY",
            reason="normalization, membership, incidence, and coefficient law gaps remain",
            caution="forbidden as immediate next group",
        ),
        Handoff(
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
            name="R1: partial constraints as coefficient law",
            upgrade="Group 31 partial constraints treated as complete B_s/F_zeta coefficient law",
            status="REJECTED",
            reason="normalization, membership, incidence, and insertion gaps remain",
        ),
        RejectedUpgrade(
            name="R2: source neutrality as full source theorem",
            upgrade="coefficient source neutrality treated as complete source no-double-counting",
            status="REJECTED",
            reason="residual/boundary/support/correction/exchange/curvature/parent channels remain obligations",
        ),
        RejectedUpgrade(
            name="R3: explicitness as divergence-safe law",
            upgrade="non-reservoir explicitness treated as divergence-safe coefficient law",
            status="REJECTED",
            reason="explicitness is weaker than divergence safety",
        ),
        RejectedUpgrade(
            name="R4: trace-normalization fork as adoption",
            upgrade="trace normalization remains open, therefore adopt it",
            status="REJECTED",
            reason="open candidate is not adoption",
        ),
        RejectedUpgrade(
            name="R5: source/divergence as insertion",
            upgrade="source/divergence discipline treated as B_s/F_zeta insertion",
            status="REJECTED",
            reason="insertion gap remains",
        ),
        RejectedUpgrade(
            name="R6: source/divergence as parent readiness",
            upgrade="partial coefficient discipline opens parent equation",
            status="REJECTED",
            reason="parent gate remains closed",
        ),
    ]


def build_conclusions() -> List[ObligationConclusion]:
    return [
        ObligationConclusion(
            name="C1: Group 31 result",
            conclusion="source/divergence route produced partial constraints only",
            status="PARTIAL_CONSTRAINT",
            meaning="hidden source and hidden reservoir shortcuts are excluded",
        ),
        ObligationConclusion(
            name="C2: no coefficient law",
            conclusion="complete B_s/F_zeta coefficient law is not derived",
            status="NOT_DERIVED",
            meaning="normalization, membership, incidence, and insertion gaps remain",
        ),
        ObligationConclusion(
            name="C3: trace normalization",
            conclusion="trace normalization remains open candidate/theorem target",
            status="CANDIDATE_REMAINS",
            meaning="source/divergence did not choose the cup shape",
        ),
        ObligationConclusion(
            name="C4: no adoption",
            conclusion="no Group 30 candidate postulate is adopted",
            status="NOT_ADOPTED",
            meaning="theorem-route partiality does not select postulates",
        ),
        ObligationConclusion(
            name="C5: next",
            conclusion="Group 31 status summary should close the group",
            status="HANDOFF_READY",
            meaning="then choose next route deliberately",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Source/divergence obligations problem")
    print("Question:")
    print()
    print("  What did the source/divergence coefficient-law route clarify, and what remains open?")
    print()
    print("Discipline:")
    print()
    print("  This script summarizes obligations and handoffs.")
    print("  It derives no coefficient law.")
    print("  It adopts no postulate.")
    print()
    print("Tiny goblin rule:")
    print("  The channels are clean; the river is still unmapped.")

    with out.governance_assessments():
        out.line(
            "source/divergence obligations summary opened",
            StatusMark.INFO,
            "summarizing partial constraints and remaining gaps",
        )


def case_1_clarified(items: List[ClarifiedItem], out: ScriptOutput) -> None:
    header("Case 1: What Group 31 clarified")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Item: {item.item}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Meaning: {item.meaning}")

    with out.governance_assessments():
        out.line(
            "Group 31 clarified items summarized",
            StatusMark.PASS,
            f"{len(items)} clarified items summarized",
        )


def case_2_open_gaps(items: List[OpenGap], out: ScriptOutput) -> None:
    header("Case 2: Open gaps")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Gap: {item.gap}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Current result: {item.current_result}")
        print(f"Discipline: {item.discipline}")

    with out.unresolved_obligations():
        out.line(
            "Group 31 open gaps summarized",
            StatusMark.OBLIGATION,
            f"{len(items)} open gaps summarized",
        )


def case_3_handoffs(items: List[Handoff], out: ScriptOutput) -> None:
    header("Case 3: Handoffs")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Route: {item.route}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")
        print(f"Caution: {item.caution}")

    with out.governance_assessments():
        out.line(
            "Group 31 handoffs summarized",
            StatusMark.PASS,
            "status summary handoff-ready",
        )


def case_4_rejected(items: List[RejectedUpgrade], out: ScriptOutput) -> None:
    header("Case 4: Rejected upgrades")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Upgrade: {item.upgrade}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")

    with out.counterexamples():
        out.line(
            "Group 31 rejected upgrades summarized",
            StatusMark.FAIL,
            "coefficient law, source theorem, divergence safety, adoption, insertion, and parent upgrades rejected",
        )


def case_5_conclusions(items: List[ObligationConclusion], out: ScriptOutput) -> None:
    header("Case 5: Obligations conclusions")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Conclusion: {item.conclusion}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Meaning: {item.meaning}")

    with out.governance_assessments():
        out.line(
            "Group 31 obligations conclusion stated",
            StatusMark.PASS,
            "Group 31 status summary should run next",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Source/divergence obligations result:")
    print()
    print("  Group 31 produced partial constraints only.")
    print("  It ruled out hidden ordinary source carriers and hidden divergence reservoirs.")
    print("  It did not derive complete B_s/F_zeta coefficient law.")
    print("  It did not derive trace normalization.")
    print("  It did not derive safe trace membership.")
    print("  It did not derive trace/residual incidence.")
    print("  It did not derive B_s/F_zeta insertion.")
    print("  No Group 30 candidate postulate is adopted.")
    print("  Active O, residual control, and parent equation remain not ready.")
    print()
    print("Possible next script:")
    print("  candidate_group_31_status_summary.py")
    print()
    print("Tiny goblin label:")
    print("  The channels are clean; the river is still unmapped.")

    with out.governance_assessments():
        out.line(
            "source/divergence obligations summary complete",
            StatusMark.PASS,
            "Group 31 status summary should run next",
        )


def record_derivations(ns) -> None:
    ns.record_derivation(
        derivation_id="g31_obligations",
        inputs=[
            sp.Symbol("partial_source_divergence_constraints"),
            sp.Symbol("coefficient_law_not_derived"),
            sp.Symbol("trace_normalization_open"),
            sp.Symbol("safe_membership_open"),
            sp.Symbol("incidence_high_risk"),
            sp.Symbol("insertion_not_ready"),
        ],
        output=sp.Symbol("g31_obligations_summary"),
        method="summarize Group 31 partial constraints, unresolved gaps, and handoffs",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="source_divergence_obligations_marker",
        scope="Group 31 source/divergence coefficient law",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g31_ob_partial_only", "Preserve Group 31 as partial constraints only"),
        ("g31_ob_no_coeff_law", "Do not claim complete coefficient law"),
        ("g31_ob_trace_norm_open", "Keep trace normalization open"),
        ("g31_ob_membership_open", "Keep safe trace membership open"),
        ("g31_ob_incidence_high_risk", "Keep trace/residual incidence high-risk"),
        ("g31_ob_no_postulate", "Do not adopt Group 30 candidates"),
        ("g31_ob_no_insertion", "Do not claim B_s/F_zeta insertion"),
        ("g31_ob_summary_next", "Write Group 31 status summary next"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g31_obligations_route"],
            description=(
                "Group 31 produced partial source/divergence constraints only. Coefficient law and insertion are not derived."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g31_ob_partial_only",
        "g31_ob_no_coeff_law",
        "g31_ob_trace_norm_open",
        "g31_ob_membership_open",
        "g31_ob_incidence_high_risk",
        "g31_ob_no_postulate",
        "g31_ob_no_insertion",
        "g31_ob_summary_next",
    ]

    ns.record_route(RouteRecord(
        route_id="g31_obligations_route",
        script_id=SCRIPT_ID,
        name="Group 31 source/divergence obligations summary",
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
        "obligations_as_postulate_adoption",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; obligations summary is not theorem closure or adoption.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g31_obligations_summary_result",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Group 31 produced partial constraints only. It ruled out hidden ordinary source carriers and hidden divergence reservoirs. "
            "It did not derive complete B_s/F_zeta coefficient law, trace normalization, safe trace membership, trace/residual incidence, or B_s/F_zeta insertion. "
            "No Group 30 candidate postulate is adopted. Active O, residual control, and parent equation remain not ready."
        ),
        derivation_ids=["g31_obligations"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Source Divergence Obligations")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    clarified = build_clarified_items()
    open_gaps = build_open_gaps()
    handoffs = build_handoffs()
    rejected = build_rejected()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_clarified(clarified, out)
    case_2_open_gaps(open_gaps, out)
    case_3_handoffs(handoffs, out)
    case_4_rejected(rejected, out)
    case_5_conclusions(conclusions, out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
