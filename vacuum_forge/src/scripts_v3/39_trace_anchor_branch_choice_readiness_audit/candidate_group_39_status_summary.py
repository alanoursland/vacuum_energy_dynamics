from dataclasses import dataclass
from pathlib import Path
from typing import List

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
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

# Group:
#   39_trace_anchor_branch_choice_readiness_audit
# Script type:
#   STATUS SUMMARY

SCRIPT_LABEL = "Candidate Group 39 Status Summary"
MARKER_ID = "g39_summary"

DEPENDENCIES = [
    ("g39_recon", "39_trace_anchor_branch_choice_readiness_audit__candidate_branch_readiness_batch_reconciliation", "g39_recon"),
    ("g39_blockers", "39_trace_anchor_branch_choice_readiness_audit__candidate_branch_choice_blocker_inventory", "g39_blockers"),
    ("g39_fzeta_boundary", "39_trace_anchor_branch_choice_readiness_audit__candidate_neutral_Fzeta_deferral_boundary", "g39_fzeta_boundary"),
    ("g39_split_safe", "39_trace_anchor_branch_choice_readiness_audit__candidate_split_notation_safe_continuation_sieve", "g39_split_safe"),
    ("g39_route_matrix", "39_trace_anchor_branch_choice_readiness_audit__candidate_route_branch_requirement_matrix", "g39_route_matrix"),
    ("g39_problem", "39_trace_anchor_branch_choice_readiness_audit__candidate_branch_choice_readiness_problem", "g39_problem"),
    ("g38_summary", "38_trace_anchor_explicit_declaration_record__candidate_group_38_status_summary", "g38_summary"),
]


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def subheader(title: str) -> None:
    print()
    print("-" * 120)
    print(title)
    print("-" * 120)


def prepare_archive(dependencies):
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    for dep_id, upstream_script_id, upstream_derivation_id in dependencies:
        ns.declare_dependency(
            dependency_id=dep_id,
            upstream_script_id=upstream_script_id,
            upstream_derivation_id=upstream_derivation_id,
            expected_record_kind=RecordKind.INVENTORY_MARKER,
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


def mark(status: str) -> StatusMark:
    return {
        "PASS": StatusMark.PASS,
        "MATCHED_EXPECTATION": StatusMark.PASS,
        "OPTION_SIEVE": StatusMark.INFO,
        "BRANCH_READINESS_AUDIT": StatusMark.INFO,
        "BRANCH_REQUIRED": StatusMark.OBLIGATION,
        "SPLIT_SAFE": StatusMark.INFO,
        "NEUTRAL_SAFE": StatusMark.INFO,
        "CONDITIONAL": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "DEFER": StatusMark.DEFER,
        "DECLARATION_DEFERRED": StatusMark.DEFER,
        "NOT_CHOSEN": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
    }.get(status, StatusMark.INFO)


def obligation_status(status: str) -> ObligationStatus:
    if status in {"NOT_READY", "DECLARATION_DEFERRED", "NOT_CHOSEN", "NOT_ADOPTED", "NOT_DERIVED"}:
        return ObligationStatus.DEFERRED
    return ObligationStatus.OPEN


def record_marker(ns, marker_id: str, symbol_name: str) -> None:
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[],
        output=sp.Symbol(symbol_name),
        method="inventory marker; no physical derivation",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
        scope="Group 39 branch-choice readiness audit summary",
    )


def record_claim(ns, claim_id: str, marker_id: str, status, statement: str) -> None:
    ns.record_claim(
        ClaimRecord(
            claim_id=claim_id,
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=status,
            statement=statement,
            derivation_ids=[marker_id],
            obligation_ids=[],
        )
    )


def record_obligation(ns, obligation_id: str, marker_id: str, title: str, description: str, status: str = "OPEN") -> None:
    ns.record_obligation(
        ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=obligation_status(status),
            required_by=[SCRIPT_ID],
            description=description,
        )
    )


@dataclass(frozen=True)
class StatusEntry:
    name: str
    topic: str
    status: str
    result: str
    boundary: str


@dataclass(frozen=True)
class GapEntry:
    name: str
    status: str
    reason: str
    discipline: str


@dataclass(frozen=True)
class HandoffEntry:
    name: str
    status: str
    reason: str
    caution: str


@dataclass(frozen=True)
class RuleEntry:
    name: str
    upgrade: str
    reason: str


def build_status_entries() -> List[StatusEntry]:
    return [
        StatusEntry(
            "G39-1: branch-readiness opener",
            "Group 39 opened as a trace-anchor branch-choice readiness audit",
            "BRANCH_READINESS_AUDIT",
            "future routes are classified by whether they require an active B_s branch, tolerate split notation, or allow neutral F_zeta deferral",
            "the opener chooses no metric_coefficient or scale_factor branch",
        ),
        StatusEntry(
            "G39-2: route branch-requirement matrix",
            "route types were sorted by branch need",
            "PASS",
            "completed trace-normalization declaration, adoption, and theorem routes require branch clarity; notation-quality and some precondition work can proceed under split notation; insertion and parent routes remain not ready",
            "route requirement is not route selection",
        ),
        StatusEntry(
            "G39-3: split-notation safe continuations",
            "safe continuation under B_s_metric and b_s_scale was classified",
            "SPLIT_SAFE",
            "notation-quality audits and route-precondition inventories are split-safe; residual/source safety and membership inventories are conditional; exact normalization is branch-required",
            "split-safe continuation is not active declaration",
        ),
        StatusEntry(
            "G39-4: neutral F_zeta boundary",
            "neutral F_zeta deferral boundary was stated",
            "NEUTRAL_SAFE",
            "F_zeta may remain a neutral response placeholder only while it carries no concrete zeta/d or 2*zeta/d expression",
            "neutral placeholder is not convention choice, theorem support, or insertion",
        ),
        StatusEntry(
            "G39-5: branch-choice blockers",
            "blockers to active branch choice were inventoried",
            "OPEN",
            "choice is blocked by missing explicit theory-owner choice, unresolved evidence-quality hierarchy, and unaudited branch consequences; these are not branch no-go theorems",
            "missing support means open or deferred, not branch rejection",
        ),
        StatusEntry(
            "G39-6: batch reconciliation",
            "speculative batch outputs were reconciled before summary",
            "MATCHED_EXPECTATION",
            "actual outputs matched the expected readiness-audit shape: route classes separated, no branch chosen, downstream gates closed",
            "reconciliation is not branch choice or group closure by itself",
        ),
        StatusEntry(
            "G39-7: active branch status",
            "metric_coefficient versus scale_factor branch",
            "DECLARATION_DEFERRED",
            "no active B_s branch is chosen",
            "B_s_metric and b_s_scale remain live split objects, not selected declarations",
        ),
        StatusEntry(
            "G39-8: downstream gates",
            "B_s/F_zeta insertion, active O, residual control, and parent closure",
            "NOT_READY",
            "all downstream gates remain closed",
            "branch-readiness audit is not insertion, active O, residual control, or parent readiness",
        ),
    ]


def build_gaps() -> List[GapEntry]:
    return [
        GapEntry(
            "G1: active branch choice",
            "OPEN",
            "B_s_metric and b_s_scale are distinct named branches, but neither is active",
            "a later explicit branch-choice record is required for completed trace-normalization declaration",
        ),
        GapEntry(
            "G2: exact trace-normalization declaration",
            "DECLARATION_DEFERRED",
            "single exact normalization cannot be completed while the branch remains deferred",
            "do not install zeta/d or 2*zeta/d under a neutral label",
        ),
        GapEntry(
            "G3: neutral F_zeta boundary",
            "OPEN",
            "F_zeta may remain neutral only if it stays expression-free",
            "neutral notation cannot hide a factor-of-two branch choice",
        ),
        GapEntry(
            "G4: branch-quality evidence hierarchy",
            "OPEN",
            "earliest or authoritative notation sources have not been ranked",
            "evidence-quality work may continue but must not choose from recovery or majority hit count",
        ),
        GapEntry(
            "G5: branch consequence audit",
            "OPEN",
            "metric versus scale branch consequences for later declarations and preconditions have not been fully compared",
            "consequence comparison is not downstream-fit selection",
        ),
        GapEntry(
            "G6: Package B declaration and adoption",
            "NOT_ADOPTED",
            "no branch choice means no completed joint Package B declaration; Group 39 is not adoption",
            "adoption remains a separate explicit decision",
        ),
        GapEntry(
            "G7: insertion and parent closure",
            "NOT_READY",
            "branch readiness does not resolve residual, source, divergence, recombination, or parent gates",
            "B_s/F_zeta insertion and parent equation remain closed",
        ),
    ]


def build_handoffs() -> List[HandoffEntry]:
    return [
        HandoffEntry(
            "H1: notation-quality source hierarchy",
            "SPLIT_SAFE",
            "can proceed under split notation by ranking earliest or authoritative notation sources",
            "must not cherry-pick recovery-facing evidence or choose by hit count",
        ),
        HandoffEntry(
            "H2: explicit branch-choice record",
            "OPEN",
            "may deliberately choose metric_coefficient or scale_factor branch",
            "choice is declaration support only, not adoption, proof, or insertion",
        ),
        HandoffEntry(
            "H3: neutral F_zeta deferral",
            "NEUTRAL_SAFE",
            "may keep F_zeta as expression-free placeholder",
            "must not attach zeta/d or 2*zeta/d while calling it neutral",
        ),
        HandoffEntry(
            "H4: split-safe route-precondition audit",
            "SPLIT_SAFE",
            "may continue classifying route preconditions while both branches remain visible",
            "preconditions are not declarations or theorems",
        ),
        HandoffEntry(
            "H5: residual/source safety audit under split notation",
            "CONDITIONAL",
            "may state general no-hidden-load checks if branch-dependent metric-entry claims are avoided",
            "cannot prove branch-specific residual nonentry without explicit assumptions",
        ),
        HandoffEntry(
            "H6: exact trace-normalization declaration",
            "BRANCH_REQUIRED",
            "requires active branch or two explicitly parallel branch records",
            "cannot be completed as one neutral declaration",
        ),
        HandoffEntry(
            "H7: insertion or parent route",
            "NOT_READY",
            "not available from Group 39",
            "forbidden as immediate handoff",
        ),
    ]


def build_rules() -> List[RuleEntry]:
    return [
        RuleEntry("R1: readiness as choice", "treat branch-required classification as choosing a branch", "readiness inventory is not branch choice"),
        RuleEntry("R2: split-safe as universal safety", "treat every future route as safe under split notation", "some routes require active branch and downstream gates remain closed"),
        RuleEntry("R3: neutral F_zeta as hidden branch", "attach zeta/d or 2*zeta/d to F_zeta while calling it neutral", "neutral deferral must remain expression-free"),
        RuleEntry("R4: blocker as no-go theorem", "treat branch-choice blockers as proof neither branch works", "blockers are governance/evidence gaps, not mathematical no-go results"),
        RuleEntry("R5: rejected selector as rejected branch", "treat recovery-selector rejection as branch rejection", "selector failure is not branch failure"),
        RuleEntry("R6: branch choice as insertion", "treat active branch clarity as B_s/F_zeta insertion readiness", "residual/source/divergence/recombination gates remain unresolved"),
        RuleEntry("R7: readiness as parent readiness", "open parent closure from branch-readiness classification", "parent gate remains closed"),
    ]


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  What did Group 39 establish about whether future trace-anchor routes require")
    print("  an active B_s branch, can proceed under split notation, or can use neutral")
    print("  F_zeta deferral?")
    print("\nDiscipline:\n")
    print("  This script summarizes Group 39.")
    print("  It does not choose metric_coefficient or scale_factor.")
    print("  It does not fill trace-normalization or safe-membership declarations.")
    print("  It adopts nothing, proves nothing, and opens no downstream gate.")
    print("\nTiny goblin rule:\n  The doors are sorted by key type. No key is turned.")
    with out.governance_assessments():
        out.line(
            "Group 39 status summary opened",
            StatusMark.PASS,
            "closing branch-choice readiness audit while preserving branch-deferred/no-adoption/no-insertion boundary",
        )


def case_1(out: ScriptOutput) -> None:
    header("Case 1: Group 39 symbolic summary loads")
    branch_required, split_safe, neutral_safe, conditional, blockers, branch_defer = sp.symbols(
        "branch_required split_safe neutral_safe conditional blockers branch_defer"
    )
    adoption_boundary, theorem_boundary = sp.symbols("adoption_boundary theorem_boundary")
    P_insertion, P_active_O, P_residual_kill, P_parent = sp.symbols(
        "P_insertion P_active_O P_residual_kill P_parent"
    )
    L_route_classes = sp.simplify(branch_required + split_safe + neutral_safe + conditional)
    L_boundaries = sp.simplify(blockers + branch_defer + adoption_boundary + theorem_boundary)
    L_downstream_closed = sp.simplify(P_insertion + P_active_O + P_residual_kill + P_parent)
    L_group39_summary = sp.simplify(L_route_classes + L_boundaries + L_downstream_closed)
    print(f"Route-class load: L_route_classes = {L_route_classes}")
    print(f"Boundary/deferred load: L_boundaries = {L_boundaries}")
    print(f"Downstream closed load: L_downstream_closed = {L_downstream_closed}")
    print(f"Group 39 summary load: L_group39_summary = {L_group39_summary}")
    with out.derived_results():
        out.line(
            "Group 39 symbolic summary loads stated",
            StatusMark.PASS,
            f"L_route_classes={L_route_classes}; L_downstream_closed={L_downstream_closed}",
        )


def case_2(out: ScriptOutput, entries: List[StatusEntry]) -> None:
    header("Case 2: Group 39 status entries")
    for item in entries:
        subheader(item.name)
        print(f"Topic: {item.topic}")
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.result}. Boundary: {item.boundary}")
    with out.governance_assessments():
        out.line("Group 39 status entries stated", StatusMark.PASS, f"{len(entries)} status entries stated")


def case_3(out: ScriptOutput, gaps: List[GapEntry]) -> None:
    header("Case 3: Final open gaps")
    for item in gaps:
        subheader(item.name)
        with out.unresolved_obligations():
            out.line(item.name, mark(item.status), f"{item.status}: {item.reason}. Discipline: {item.discipline}")
    with out.unresolved_obligations():
        out.line("Group 39 final gaps stated", StatusMark.PASS, f"{len(gaps)} gaps remain open, deferred, or not ready")


def case_4(out: ScriptOutput, handoffs: List[HandoffEntry]) -> None:
    header("Case 4: Final handoffs")
    for item in handoffs:
        subheader(item.name)
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.reason}. Caution: {item.caution}")
    with out.governance_assessments():
        out.line("Group 39 handoffs stated", StatusMark.DEFER, f"{len(handoffs)} handoffs stated; choices/downstream gates remain separate")


def case_5(out: ScriptOutput, rules: List[RuleEntry]) -> None:
    header("Case 5: Rejected summary upgrades")
    for item in rules:
        subheader(item.name)
        print(f"Upgrade: {item.upgrade}")
        with out.governance_assessments():
            out.line(item.name, StatusMark.OBLIGATION, f"POLICY_RULE: {item.reason}")
    with out.governance_assessments():
        out.line("Group 39 summary upgrades rejected", StatusMark.PASS, f"{len(rules)} upgrade shortcuts rejected as policy rules")


def case_6(out: ScriptOutput) -> None:
    header("Case 6: Group 39 conclusions")
    conclusions = [
        ("C1: Group 39 result", "BRANCH_READINESS_AUDIT", "Group 39 completed a branch-choice readiness audit"),
        ("C2: active branch", "DECLARATION_DEFERRED", "no metric_coefficient or scale_factor branch is chosen"),
        ("C3: route classes", "PASS", "branch-required, split-safe, neutral-safe, conditional, and not-ready routes are separated"),
        ("C4: neutral F_zeta", "NEUTRAL_SAFE", "F_zeta may remain neutral only while expression-free"),
        ("C5: blockers", "OPEN", "branch blockers are governance/evidence gaps, not no-go theorems"),
        ("C6: no adoption or theorem", "NOT_ADOPTED", "Group 39 adopts nothing and derives nothing"),
        ("C7: downstream gates", "NOT_READY", "B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready"),
    ]
    for name, status, meaning in conclusions:
        subheader(name)
        with out.governance_assessments():
            out.line(name, mark(status), f"{status}: {meaning}")
    with out.governance_assessments():
        out.line(
            "Group 39 status summary conclusion stated",
            StatusMark.PASS,
            "readiness audit closed; no active branch, no declaration completion, no adoption, downstream gates closed",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Group 39 status summary result:\n")
    print("  Group 39 completed a trace-anchor branch-choice readiness audit.")
    print("  No active metric_coefficient or scale_factor branch is chosen.")
    print("  B_s_metric and b_s_scale remain live split notation branches.")
    print("  Some future work is split-safe, including notation-quality and route-precondition audits.")
    print("  Neutral F_zeta deferral is safe only while expression-free.")
    print("  Exact trace-normalization declaration, adoption, and theorem routes require branch clarity.")
    print("  Branch-choice blockers remain open/deferred and are not no-go theorems.")
    print("  No trace-normalization or safe-membership declaration is completed.")
    print("  Package B remains compatible-if-declared only.")
    print("  Package B is not adopted or recommended for adoption.")
    print("  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.")
    print("\nPossible next step:")
    print("  notation-quality source hierarchy, explicit branch-choice record,")
    print("  neutral F_zeta deferral record, or split-safe precondition audit")
    print("\nTiny goblin label:")
    print("  The doors are sorted by key type. No key is turned.")
    with out.governance_assessments():
        out.line(
            "candidate Group 39 status summary complete",
            StatusMark.PASS,
            "branch-choice readiness audit closed; choices and downstream gates remain separate",
        )


def record_governance(
    ns,
    status_entries: List[StatusEntry],
    gaps: List[GapEntry],
    handoffs: List[HandoffEntry],
    rules: List[RuleEntry],
) -> None:
    record_marker(ns, MARKER_ID, "g39_branch_choice_readiness_summary")

    for idx, item in enumerate(status_entries, 1):
        record_claim(
            ns,
            f"g39_status_{idx}",
            MARKER_ID,
            GovernanceStatus.POLICY_RULE,
            f"{item.name}: {item.topic}. Result: {item.result}. Boundary: {item.boundary}.",
        )

    for idx, item in enumerate(gaps, 1):
        record_obligation(
            ns,
            f"g39_gap_{idx}",
            MARKER_ID,
            item.name,
            f"{item.reason}. Discipline: {item.discipline}.",
            item.status,
        )

    for idx, item in enumerate(handoffs, 1):
        route_status = GovernanceStatus.CANDIDATE_ROUTE
        if item.status in {"NOT_READY", "BRANCH_REQUIRED", "CONDITIONAL"}:
            route_status = GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
        ns.record_route(
            RouteRecord(
                route_id=f"g39_handoff_{idx}",
                script_id=SCRIPT_ID,
                name=item.name,
                status=route_status,
                tier=ClaimTier.CONSTRAINED,
                required_obligations=[],
                activation_conditions=[item.reason, item.caution],
            )
        )

    for idx, item in enumerate(rules, 1):
        record_claim(
            ns,
            f"g39_rule_{idx}",
            MARKER_ID,
            GovernanceStatus.POLICY_RULE,
            f"{item.name}: {item.upgrade}. Rejected because {item.reason}.",
        )


def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    status_entries = build_status_entries()
    gaps = build_gaps()
    handoffs = build_handoffs()
    rules = build_rules()

    case_0(out)
    case_1(out)
    case_2(out, status_entries)
    case_3(out, gaps)
    case_4(out, handoffs)
    case_5(out, rules)
    case_6(out)
    final_interpretation(out)

    record_governance(ns, status_entries, gaps, handoffs, rules)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
