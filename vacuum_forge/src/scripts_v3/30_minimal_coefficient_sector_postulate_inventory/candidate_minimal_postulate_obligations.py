# Candidate minimal postulate obligations
#
# Group:
#   30_minimal_coefficient_sector_postulate_inventory
#
# Script type:
#   OBLIGATION / HANDOFF SUMMARY
#
# Purpose
# -------
# Summarize Group 30 obligations, admissible candidates, rejected bundles,
# and theorem-route handoffs.
#
# Locked-door question:
#
#   What did the minimal postulate inventory clarify, and what remains open?
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
#   The teeth are counted, but none are set.

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
        "HIGH_RISK": StatusMark.DEFER,
        "HANDOFF_READY": StatusMark.PASS,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_IDENTIFIED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "THEOREM_ROUTE_PREFERRED": StatusMark.INFO,
        "UNDERDETERMINED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
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
class ClarifiedItem:
    name: str
    item: str
    status: str
    meaning: str


@dataclass
class OpenObligation:
    name: str
    obligation: str
    status: str
    current_result: str
    blocks: str


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
class ObligationsConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_clarified_items() -> List[ClarifiedItem]:
    return [
        ClarifiedItem(
            name="D1: inventory route",
            item="minimal coefficient/sector postulate inventory opened",
            status="REQUIRED",
            meaning="explicit choices can now be tracked without pretending they are derivations",
        ),
        ClarifiedItem(
            name="D2: no adoption",
            item="no postulate adopted",
            status="NOT_ADOPTED",
            meaning="all surviving structures remain candidates or theorem routes",
        ),
        ClarifiedItem(
            name="D3: admissible core",
            item="trace normalization, safe membership, guardrail visibility, divergence explicitness",
            status="ADMISSIBLE_CANDIDATE",
            meaning="survive minimality and anti-smuggling filters",
        ),
        ClarifiedItem(
            name="D4: source/divergence route",
            item="source no-double-counting and divergence-safe coefficient law",
            status="THEOREM_ROUTE_PREFERRED",
            meaning="should be pursued as theorem route before postulating",
        ),
        ClarifiedItem(
            name="D5: incidence",
            item="trace/residual zero incidence",
            status="HIGH_RISK",
            meaning="too close to no-overlap/residual-control smuggling",
        ),
        ClarifiedItem(
            name="D6: minimal set",
            item="complete minimal admissible postulate set",
            status="NOT_IDENTIFIED",
            meaning="inventory narrowed choices but did not choose a set",
        ),
        ClarifiedItem(
            name="D7: downstream gates",
            item="B_s/F_zeta insertion, active O, residual control, parent equation",
            status="NOT_READY",
            meaning="all remain closed",
        ),
    ]


def build_open_obligations() -> List[OpenObligation]:
    return [
        OpenObligation(
            name="O1: explicit adoption decision",
            obligation="any adoption must be made explicitly by user/theory update",
            status="OPEN",
            current_result="no postulate adopted in Group 30",
            blocks="postulate status",
        ),
        OpenObligation(
            name="O2: source/divergence theorem route",
            obligation="derive or test source no-double-counting and divergence-safe coefficient law",
            status="OPEN",
            current_result="theorem-route preferred",
            blocks="field-equation usability and insertion",
        ),
        OpenObligation(
            name="O3: trace-normalization candidate",
            obligation="if adopted later, state only how B_s reads zeta",
            status="OPEN",
            current_result="admissible candidate only",
            blocks="coefficient normalization",
        ),
        OpenObligation(
            name="O4: safe-membership candidate",
            obligation="if adopted later, state only zeta_Bs -> T_zeta",
            status="OPEN",
            current_result="admissible candidate only",
            blocks="sector membership",
        ),
        OpenObligation(
            name="O5: guardrail visibility candidate",
            obligation="if adopted later, state only non-reservoir visibility",
            status="OPEN",
            current_result="admissible candidate only",
            blocks="hidden repair prevention",
        ),
        OpenObligation(
            name="O6: divergence explicitness candidate",
            obligation="if adopted later, state only explicit/auditable correction rule",
            status="OPEN",
            current_result="admissible candidate only",
            blocks="hidden correction prevention",
        ),
        OpenObligation(
            name="O7: incidence caution",
            obligation="do not adopt trace/residual incidence without further obstruction/theorem analysis",
            status="REQUIRED",
            current_result="high-risk",
            blocks="no-overlap/residual control",
        ),
        OpenObligation(
            name="O8: downstream gates",
            obligation="keep insertion, active O, residual control, and parent equation closed",
            status="NOT_READY",
            current_result="not ready",
            blocks="premature theorem closure",
        ),
    ]


def build_handoffs() -> List[Handoff]:
    return [
        Handoff(
            name="H1: preferred theorem route",
            route="31_source_divergence_coefficient_law",
            status="HANDOFF_READY",
            reason="source no-double-counting and divergence-safe coefficient law remain theorem-route preferred",
            caution="must not hide source load or correction load",
        ),
        Handoff(
            name="H2: explicit-choice route",
            route="31_explicit_minimal_postulate_selection",
            status="OPEN",
            reason="admissible core exists but no set is adopted",
            caution="requires explicit user/theory decision; survival is not adoption",
        ),
        Handoff(
            name="H3: trace-normalization route",
            route="31_trace_normalization_choice_or_theorem",
            status="OPEN",
            reason="trace normalization remains admissible candidate and theorem target",
            caution="must not be recovery-selected",
        ),
        Handoff(
            name="H4: safe-membership route",
            route="31_safe_trace_membership_choice_or_theorem",
            status="OPEN",
            reason="safe membership remains admissible candidate and theorem target",
            caution="must not imply incidence/no-overlap/residual control",
        ),
        Handoff(
            name="H5: insertion theorem",
            route="31_Bs_Fzeta_insertion_theorem",
            status="NOT_READY",
            reason="coefficient/source/divergence/membership/incidence gates remain open",
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


def build_rejected_upgrades() -> List[RejectedUpgrade]:
    return [
        RejectedUpgrade(
            name="U1: candidate survival as adoption",
            upgrade="admissible candidate treated as adopted postulate",
            status="REJECTED",
            reason="survival is not adoption",
        ),
        RejectedUpgrade(
            name="U2: inventory as minimal set",
            upgrade="candidate inventory treated as identified minimal set",
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
            name="U6: bundle closure",
            upgrade="postulate bundle treated as insertion or parent readiness",
            status="REJECTED",
            reason="endpoint-selected closure bundle",
        ),
    ]


def build_conclusions() -> List[ObligationsConclusion]:
    return [
        ObligationsConclusion(
            name="C1: Group 30 result",
            conclusion="minimal postulate inventory clarified choices but did not adopt any",
            status="NOT_ADOPTED",
            meaning="Group 30 is inventory/obstruction, not postulate selection",
        ),
        ObligationsConclusion(
            name="C2: admissible core",
            conclusion="trace normalization, safe membership, guardrail visibility, and divergence explicitness survive as candidates",
            status="ADMISSIBLE_CANDIDATE",
            meaning="possible explicit choices only",
        ),
        ObligationsConclusion(
            name="C3: minimal set",
            conclusion="complete minimal admissible set is not identified",
            status="UNDERDETERMINED",
            meaning="choice remains open",
        ),
        ObligationsConclusion(
            name="C4: theorem route",
            conclusion="source/divergence coefficient law is the preferred next theorem route",
            status="HANDOFF_READY",
            meaning="best next work if avoiding premature postulates",
        ),
        ObligationsConclusion(
            name="C5: downstream",
            conclusion="insertion, active O, residual control, and parent equation remain not ready",
            status="NOT_READY",
            meaning="no downstream gate opens",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Minimal postulate obligations problem")
    print("Question:")
    print()
    print("  What did the minimal postulate inventory clarify, and what remains open?")
    print()
    print("Discipline:")
    print()
    print("  This is an obligation and handoff summary.")
    print("  It adopts no postulate.")
    print("  It derives no insertion.")
    print()
    print("Tiny goblin rule:")
    print("  The teeth are counted, but none are set.")

    with out.governance_assessments():
        out.line(
            "minimal postulate obligations summary opened",
            StatusMark.INFO,
            "summarizing admissible candidates, underdetermination, and theorem-route handoffs",
        )


def case_1_clarified(items: List[ClarifiedItem], out: ScriptOutput) -> None:
    header("Case 1: What Group 30 clarified")
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
            "Group 30 clarified items summarized",
            StatusMark.PASS,
            f"{len(items)} clarified items summarized",
        )


def case_2_obligations(items: List[OpenObligation], out: ScriptOutput) -> None:
    header("Case 2: Open obligations")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Obligation: {item.obligation}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Current result: {item.current_result}")
        print(f"Blocks: {item.blocks}")

    with out.unresolved_obligations():
        out.line(
            "Group 30 open obligations summarized",
            StatusMark.OBLIGATION,
            f"{len(items)} obligations summarized",
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
            "Group 30 handoffs summarized",
            StatusMark.PASS,
            "source/divergence coefficient law is handoff-ready as preferred theorem route",
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
            "Group 30 rejected upgrades summarized",
            StatusMark.FAIL,
            "candidate survival, minimal set, incidence, source/divergence, explicitness, and bundle upgrades rejected",
        )


def case_5_conclusions(items: List[ObligationsConclusion], out: ScriptOutput) -> None:
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
            "Group 30 obligations conclusion stated",
            StatusMark.PASS,
            "Group 30 ready for status summary",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Minimal postulate obligations result:")
    print()
    print("  Group 30 clarified the missing explicit-choice inventory.")
    print("  No postulate is adopted.")
    print("  The admissible core candidates are:")
    print("    trace normalization;")
    print("    safe trace membership;")
    print("    guardrail visibility;")
    print("    divergence explicitness.")
    print("  A complete minimal admissible postulate set is not identified.")
    print("  Source no-double-counting and divergence-safe coefficient law remain theorem-route preferred.")
    print("  Trace/residual incidence remains high-risk.")
    print("  B_s/F_zeta insertion is not derived.")
    print("  Active O, residual control, and parent equation remain not ready.")
    print()
    print("Preferred next group:")
    print("  31_source_divergence_coefficient_law")
    print()
    print("Possible explicit-choice route, only by explicit user/theory decision:")
    print("  31_explicit_minimal_postulate_selection")
    print()
    print("Possible next script:")
    print("  candidate_group_30_status_summary.py")
    print()
    print("Tiny goblin label:")
    print("  The teeth are counted, but none are set.")

    with out.governance_assessments():
        out.line(
            "minimal postulate obligations summary complete",
            StatusMark.PASS,
            "Group 30 status summary should run next",
        )


def record_derivations(ns) -> None:
    ns.record_derivation(
        derivation_id="g30_obligations",
        inputs=[
            sp.Symbol("admissible_core_candidates"),
            sp.Symbol("no_postulate_adopted"),
            sp.Symbol("minimal_set_not_identified"),
            sp.Symbol("source_divergence_theorem_route_preferred"),
            sp.Symbol("incidence_high_risk"),
            sp.Symbol("downstream_gates_closed"),
        ],
        output=sp.Symbol("g30_obligations_summary"),
        method="summarize minimal postulate obligations and handoffs",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="minimal_postulate_obligations_marker",
        scope="Group 30 minimal coefficient/sector postulate inventory",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g30_ob_no_adoption", "No postulate adopted by Group 30"),
        ("g30_ob_admissible_core", "Preserve admissible core as candidates only"),
        ("g30_ob_minimal_set", "Minimal admissible set remains underdetermined"),
        ("g30_ob_source_div", "Handoff to source/divergence coefficient law"),
        ("g30_ob_explicit_choice", "Explicit postulate selection requires explicit user/theory decision"),
        ("g30_ob_incidence", "Keep trace/residual incidence high-risk"),
        ("g30_ob_downstream", "Keep insertion/O/residual/parent gates closed"),
        ("g30_ob_summary", "Write Group 30 status summary next"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g30_ob_route"],
            description=(
                "Group 30 clarified admissible postulate candidates but did not adopt any. Source/divergence theorem route remains preferred."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g30_ob_no_adoption",
        "g30_ob_admissible_core",
        "g30_ob_minimal_set",
        "g30_ob_source_div",
        "g30_ob_explicit_choice",
        "g30_ob_incidence",
        "g30_ob_downstream",
        "g30_ob_summary",
    ]

    ns.record_route(RouteRecord(
        route_id="g30_ob_route",
        script_id=SCRIPT_ID,
        name="Group 30 minimal postulate obligations route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "no postulate adopted",
            "admissible core candidates remain candidates only",
            "minimal set not identified",
            "source/divergence coefficient law handoff-ready",
            "explicit postulate selection requires explicit decision",
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
        "obligations_as_adoption",
        "obligations_as_parent_readiness",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; obligations summary is not adoption or theorem closure.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g30_obligations_inventory_summary",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Group 30 clarified the missing explicit-choice inventory but adopted no postulate. The admissible core candidates are trace normalization, safe trace membership, guardrail visibility, and divergence explicitness. "
            "A complete minimal admissible postulate set is not identified. Source no-double-counting and divergence-safe coefficient law remain theorem-route preferred. Trace/residual incidence remains high-risk. "
            "B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready. Preferred next group is source/divergence coefficient law; explicit postulate selection requires explicit user/theory decision."
        ),
        derivation_ids=["g30_obligations"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Minimal Postulate Obligations")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    clarified = build_clarified_items()
    obligations = build_open_obligations()
    handoffs = build_handoffs()
    rejected = build_rejected_upgrades()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_clarified(clarified, out)
    case_2_obligations(obligations, out)
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
