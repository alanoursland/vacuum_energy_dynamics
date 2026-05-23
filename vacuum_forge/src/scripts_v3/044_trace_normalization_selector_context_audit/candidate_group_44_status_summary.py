from __future__ import annotations

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
    ScriptOutput,
    StatusMark,
)

ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"

# Group:
#   44_trace_normalization_selector_context_audit
# Script type:
#   STATUS SUMMARY

SCRIPT_LABEL = "Candidate Group 44 Status Summary"
MARKER_ID = "g44_summary"

DEPENDENCIES = [
    ("g44_recon", "44_trace_normalization_selector_context_audit__candidate_selector_context_batch_reconciliation", "g44_recon"),
    ("g44_context_sufficiency", "44_trace_normalization_selector_context_audit__candidate_context_sufficiency_and_deferral_sieve", "g44_context_sufficiency"),
    ("g44_owner_boundary", "44_trace_normalization_selector_context_audit__candidate_theory_owner_choice_boundary", "g44_owner_boundary"),
    ("g44_route_burden", "44_trace_normalization_selector_context_audit__candidate_route_burden_comparison_audit", "g44_route_burden"),
    ("g44_consequence_context", "44_trace_normalization_selector_context_audit__candidate_branch_consequence_context_matrix", "g44_consequence_context"),
    ("g44_source_hierarchy", "44_trace_normalization_selector_context_audit__candidate_source_hierarchy_evidence_ledger", "g44_source_hierarchy"),
    ("g44_problem", "44_trace_normalization_selector_context_audit__candidate_selector_context_problem", "g44_problem"),
    ("g43_summary", "43_trace_normalization_branch_or_parallel_decision_surface__candidate_group_43_status_summary", "g43_summary"),
]


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
        "CONTEXT_AUDIT": StatusMark.INFO,
        "CONTEXT_ONLY": StatusMark.INFO,
        "ADMISSIBLE_CONTEXT": StatusMark.INFO,
        "EVIDENCE_CONTEXT": StatusMark.INFO,
        "CONSEQUENCE_CONTEXT": StatusMark.INFO,
        "ROUTE_BURDEN_CONTEXT": StatusMark.INFO,
        "CHOICE_CONTEXT_READY": StatusMark.DEFER,
        "PARALLEL_ROUTE_PREFERRED": StatusMark.INFO,
        "CONTINUED_DEFERRAL": StatusMark.DEFER,
        "CONTEXT_INSUFFICIENT": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "DEFER": StatusMark.DEFER,
        "DECLARATION_DEFERRED": StatusMark.DEFER,
        "NOT_DECLARED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "EXPLICIT_CHOICE_REQUIRED": StatusMark.OBLIGATION,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "SELECTOR_REJECTED": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
    }.get(status, StatusMark.INFO)


def obligation_status(status: str) -> ObligationStatus:
    if status in {
        "NOT_READY",
        "NOT_DECLARED",
        "NOT_ADOPTED",
        "NOT_DERIVED",
        "DECLARATION_DEFERRED",
        "CONTINUED_DEFERRAL",
        "CONTEXT_INSUFFICIENT",
    }:
        return ObligationStatus.DEFERRED
    return ObligationStatus.OPEN


def governance_status(status: str):
    if status in {"POLICY_RULE", "EXPLICIT_CHOICE_REQUIRED"}:
        return GovernanceStatus.POLICY_RULE
    if hasattr(GovernanceStatus, "DEFERRED") and status in {
        "NOT_READY",
        "NOT_DECLARED",
        "DECLARATION_DEFERRED",
        "CONTINUED_DEFERRAL",
        "OPEN",
    }:
        return GovernanceStatus.DEFERRED
    if hasattr(GovernanceStatus, "CANDIDATE_ROUTE") and status in {
        "ADMISSIBLE_CONTEXT",
        "CONTEXT_ONLY",
        "CHOICE_CONTEXT_READY",
        "PARALLEL_ROUTE_PREFERRED",
    }:
        return GovernanceStatus.CANDIDATE_ROUTE
    return GovernanceStatus.POLICY_RULE


def record_marker(ns, marker_id: str, symbol_name: str) -> None:
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[],
        output=sp.Symbol(symbol_name),
        method="inventory marker; no physical derivation",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
        scope="Group 44 trace-normalization selector-context audit summary",
    )


def record_claim(ns, claim_id: str, marker_id: str, status: str, statement: str) -> None:
    ns.record_claim(
        ClaimRecord(
            claim_id=claim_id,
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=governance_status(status),
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


def build_status_entries() -> List[StatusEntry]:
    return [
        StatusEntry(
            "G44-1: selector-context opener",
            "Group 44 opened as a trace-normalization selector-context audit",
            "CONTEXT_AUDIT",
            "source hierarchy, consequence profiles, route burdens, and explicit convention-choice boundaries were sharpened as context for a later decision",
            "context is not branch choice, trace-normalization declaration, adoption, insertion, or parent readiness",
        ),
        StatusEntry(
            "G44-2: source hierarchy evidence",
            "source and notation evidence classes",
            "ADMISSIBLE_CONTEXT",
            "earliest internal definitions, current snapshot/governance records, actual script records, and summaries can inform a later decision if ranked by authority and relevance",
            "majority hit count and old overloaded shorthand cannot select a branch or restore unqualified B_s",
        ),
        StatusEntry(
            "G44-3: consequence context",
            "metric, scale, parallel, and deferral consequence profiles",
            "CONSEQUENCE_CONTEXT",
            "route consequences can expose factor-of-two burden, volume/root intuition, hidden-branch risk, deferral value, and insertion distance",
            "consequence comparison remains context and cannot become downstream-convenience selection",
        ),
        StatusEntry(
            "G44-4: route burden comparison",
            "burdens for metric choice, scale choice, parallel records, and continued deferral",
            "ROUTE_BURDEN_CONTEXT",
            "burdens were made comparable, including object/scope, zeta convention, dimension, selector records, explicit labels, and deferral-target requirements",
            "smaller or cleaner burden is not an admissible selector by itself",
        ),
        StatusEntry(
            "G44-5: theory-owner choice boundary",
            "future explicit convention-choice requirements",
            "EXPLICIT_CHOICE_REQUIRED",
            "a future choice record must name the chosen route, label convention status if not derived, disclaim forbidden selectors, list known obligations, and preserve downstream non-readiness",
            "the boundary does not make the theory-owner choice and does not convert intuition into derivation",
        ),
        StatusEntry(
            "G44-6: context sufficiency and deferral",
            "choice-ready, parallel-preferred, and continued-deferral handoff conditions",
            "CHOICE_CONTEXT_READY",
            "current context is improved enough to support a later explicit choice record or a parallel/deferral handoff, but it remains non-self-selecting",
            "handoff recommendation is not execution, declaration, or insertion",
        ),
        StatusEntry(
            "G44-7: batch reconciliation",
            "actual batch outputs were reconciled before summary",
            "MATCHED_EXPECTATION",
            "outputs matched the expected selector-context audit shape: context was sharpened, forbidden shortcuts stayed blocked, and no route was chosen",
            "reconciliation is not group closure by itself, branch choice, declaration completion, adoption, theorem proof, or insertion",
        ),
        StatusEntry(
            "G44-8: downstream gates",
            "Package B adoption, B_s/F_zeta insertion, active O, residual control, recombination, and parent closure",
            "NOT_READY",
            "all downstream gates remain closed after selector-context sharpening",
            "Group 44 is not Package B adoption, scalar recombination, active O construction, residual control, or parent readiness",
        ),
    ]


def build_gaps() -> List[GapEntry]:
    return [
        GapEntry(
            "G1: no branch or route chosen",
            "DECLARATION_DEFERRED",
            "metric, scale, parallel, and continued-deferral routes remain available but unselected",
            "a later explicit record is required before any route becomes active",
        ),
        GapEntry(
            "G2: source hierarchy not fully ranked",
            "OPEN",
            "source hierarchy is admissible context only if authority, age, relevance, and repaired-notation status are ranked explicitly",
            "do not choose by hit count, old shorthand, or cherry-picked source fragments",
        ),
        GapEntry(
            "G3: consequence context remains non-selective",
            "OPEN",
            "consequence profiles identify risks and burdens but do not choose a route",
            "do not choose by ease of insertion, clean algebra, parent convenience, or hidden-branch avoidance alone",
        ),
        GapEntry(
            "G4: route burdens remain open",
            "OPEN",
            "burdens are visible but not closed for metric, scale, parallel, or deferral routes",
            "visibility is not closure and smaller burden is not selector",
        ),
        GapEntry(
            "G5: explicit convention choice remains future",
            "EXPLICIT_CHOICE_REQUIRED",
            "theory-owner intuition may enter only in a later daylight-labeled convention or choice record",
            "do not report intuition, source context, or consequence context as derivation",
        ),
        GapEntry(
            "G6: trace-normalization declaration",
            "NOT_DECLARED",
            "selector context does not install log(B_s_metric)=2*zeta/d, log(b_s_scale)=zeta/d, or any neutral law",
            "declaration requires separate explicit branch or parallel-record assumptions and conventions",
        ),
        GapEntry(
            "G7: adoption and insertion",
            "NOT_READY",
            "selector-context sharpening does not license Package B adoption or B_s/F_zeta insertion",
            "residual/source/boundary/divergence gates remain separate",
        ),
        GapEntry(
            "G8: recombination and parent closure",
            "NOT_READY",
            "context sufficiency does not solve active O, residual control, recombination, parent identity, or parent equation",
            "parent field-equation routes remain closed",
        ),
    ]


def build_handoffs() -> List[HandoffEntry]:
    return [
        HandoffEntry(
            "H1: explicit branch-choice record",
            "EXPLICIT_CHOICE_REQUIRED",
            "may now be written if the project wants a daylight-labeled convention choice between metric or scale route",
            "must state that the choice is not derived from recovery, downstream convenience, neutral expression, inherited symbol, or majority count",
        ),
        HandoffEntry(
            "H2: explicit parallel-record route",
            "PARALLEL_ROUTE_PREFERRED",
            "may keep both branch-indexed trace-normalization candidates visible if the project wants progress without choosing",
            "parallel records remain visibility infrastructure, not one neutral law and not declaration completion",
        ),
        HandoffEntry(
            "H3: source-hierarchy ranking route",
            "OPEN",
            "may rank earliest/internal/current/authoritative sources before a later choice",
            "source hierarchy is context only and cannot select a branch without a later explicit decision",
        ),
        HandoffEntry(
            "H4: branch consequence comparison continuation",
            "ADMISSIBLE_CONTEXT",
            "may deepen consequence profiles and hidden-branch risk without selecting by convenience",
            "consequence comparison must not become downstream-fit selection",
        ),
        HandoffEntry(
            "H5: continued deferral with named target",
            "CONTINUED_DEFERRAL",
            "may defer branch choice while naming the next narrowing target, such as source hierarchy, residual/source theorem work, or parallel record preparation",
            "deferral must not become a loop or branch rejection",
        ),
        HandoffEntry(
            "H6: trace-normalization declaration attempt",
            "NOT_DECLARED",
            "may be attempted only after explicit branch or parallel-record assumptions and conventions are supplied",
            "not available directly from Group 44 as a completed result",
        ),
        HandoffEntry(
            "H7: insertion or parent route",
            "NOT_READY",
            "not available from Group 44",
            "forbidden as immediate handoff",
        ),
    ]


def build_rejected_upgrades() -> List[RuleEntry]:
    return [
        RuleEntry("R1: context as branch choice", "treat source hierarchy, consequence context, route burden, or convention boundary as selecting metric or scale", "context can inform only a later explicit record"),
        RuleEntry("R2: source count as selector", "choose from majority notation count or old overloaded B_s shorthand", "authority and repaired notation status matter more than hit count"),
        RuleEntry("R3: burden as selector", "choose the route with fewer or cleaner obligations", "burden comparison is practical context only"),
        RuleEntry("R4: consequence as downstream convenience", "choose the route that seems easier to insert or fit into parent closure", "downstream convenience remains forbidden"),
        RuleEntry("R5: convention as derivation", "present theory-owner intuition as theorem or derivation", "choice must be daylight-labeled as choice if not derived"),
        RuleEntry("R6: recommendation as execution", "treat choice-ready, parallel-preferred, or deferral handoff as executing that route", "handoff status is not execution"),
        RuleEntry("R7: context as declaration", "treat sharpened context as trace-normalization declaration", "declaration requires separate record"),
        RuleEntry("R8: context as insertion", "open B_s/F_zeta insertion, active O, recombination, or parent route from context clarity", "downstream gates remain closed"),
    ]


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  What did Group 44 establish about admissible context for a later")
    print("  trace-normalization route decision?")
    print("\nDiscipline:\n")
    print("  This script summarizes Group 44 after reviewing the batch outputs.")
    print("  It does not choose B_s_metric or b_s_scale.")
    print("  It does not complete trace-normalization declaration.")
    print("  It adopts nothing, inserts nothing, constructs no active O, and opens no parent gate.")
    with out.governance_assessments():
        out.line(
            "Group 44 status summary opened",
            StatusMark.PASS,
            "closing selector-context audit while preserving context-only / no-choice / no-declaration / no-insertion boundary",
        )


def case_1(out: ScriptOutput) -> None:
    header("Case 1: Group 44 summary boundary ledger")
    ledger = [
        ("selector context", "CONTEXT_AUDIT", "source hierarchy, consequences, burden comparison, and convention boundaries sharpened"),
        ("source hierarchy", "ADMISSIBLE_CONTEXT", "ranked evidence may inform a later choice but cannot select"),
        ("consequence context", "CONSEQUENCE_CONTEXT", "risk and obligation profiles can be compared but not used as convenience selectors"),
        ("route burden", "ROUTE_BURDEN_CONTEXT", "burdens visible but not closed and not selectors"),
        ("choice boundary", "EXPLICIT_CHOICE_REQUIRED", "future intuition or convention must be explicitly labeled"),
        ("handoff status", "CHOICE_CONTEXT_READY", "choice-ready, parallel-preferred, and deferral conditions stated as handoffs only"),
        ("trace declaration", "NOT_DECLARED", "no trace-normalization declaration completed"),
        ("downstream gates", "NOT_READY", "adoption, insertion, active O, residual control, recombination, and parent closure remain closed"),
    ]
    for name, status, detail in ledger:
        with out.governance_assessments():
            out.line(name, mark(status), f"{status}: {detail}")


def case_2(out: ScriptOutput, entries: List[StatusEntry]) -> None:
    header("Case 2: Group 44 status entries")
    for item in entries:
        subheader(item.name)
        print(f"Topic: {item.topic}")
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.result}. Boundary: {item.boundary}")
    with out.governance_assessments():
        out.line("Group 44 status entries stated", StatusMark.PASS, f"{len(entries)} status entries stated")


def case_3(out: ScriptOutput, gaps: List[GapEntry]) -> None:
    header("Case 3: Final open gaps")
    for item in gaps:
        subheader(item.name)
        with out.unresolved_obligations():
            out.line(item.name, mark(item.status), f"{item.status}: {item.reason}. Discipline: {item.discipline}")
    with out.unresolved_obligations():
        out.line("Group 44 final gaps stated", StatusMark.PASS, f"{len(gaps)} gaps remain open, explicit-choice-required, not declared, or not ready")


def case_4(out: ScriptOutput, handoffs: List[HandoffEntry]) -> None:
    header("Case 4: Final handoffs")
    for item in handoffs:
        subheader(item.name)
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.reason}. Caution: {item.caution}")
    with out.governance_assessments():
        out.line("Group 44 handoffs stated", StatusMark.DEFER, f"{len(handoffs)} handoffs stated; choice, declaration, and downstream gates remain separate")


def case_5(out: ScriptOutput, rules: List[RuleEntry]) -> None:
    header("Case 5: Rejected summary upgrades")
    for item in rules:
        subheader(item.name)
        print(f"Upgrade: {item.upgrade}")
        with out.governance_assessments():
            out.line(item.name, StatusMark.OBLIGATION, f"POLICY_RULE: {item.reason}")
    with out.governance_assessments():
        out.line("Group 44 summary upgrades rejected", StatusMark.PASS, f"{len(rules)} upgrade shortcuts rejected as policy rules")


def case_6(out: ScriptOutput) -> None:
    header("Case 6: Group 44 conclusions")
    conclusions = [
        ("C1: Group 44 result", "CONTEXT_AUDIT", "Group 44 completed a trace-normalization selector-context audit"),
        ("C2: context status", "CONTEXT_ONLY", "source hierarchy, consequence context, route burden, and choice boundary are sharper"),
        ("C3: choice status", "DECLARATION_DEFERRED", "no metric, scale, parallel, or deferral route is executed"),
        ("C4: evidence status", "ADMISSIBLE_CONTEXT", "ranked evidence may inform later choice but cannot select"),
        ("C5: convention status", "EXPLICIT_CHOICE_REQUIRED", "future intuition or theory-owner preference must be labeled as choice"),
        ("C6: declaration status", "NOT_DECLARED", "trace normalization is not completed"),
        ("C7: downstream status", "NOT_READY", "B_s/F_zeta insertion, active O, recombination, and parent equation remain not ready"),
    ]
    for name, status, meaning in conclusions:
        subheader(name)
        with out.governance_assessments():
            out.line(name, mark(status), f"{status}: {meaning}")
    with out.governance_assessments():
        out.line(
            "Group 44 status summary conclusion stated",
            StatusMark.PASS,
            "selector context sharpened; no branch, declaration, adoption, insertion, active O, recombination, or parent route opened",
        )


def final_interpretation() -> None:
    header("Final interpretation")
    print("Group 44 status summary result:\n")
    print("  Group 44 completed a trace-normalization selector-context audit.")
    print("  It made admissible context sharper for a later decision, but context did not choose a branch.")
    print("  Ranked source hierarchy can inform a later explicit record, but majority count and old overloaded B_s shorthand remain rejected.")
    print("  Branch consequences can expose risk, factor-of-two burden, hidden-branch risk, and insertion distance, but downstream convenience cannot select a route.")
    print("  Route burdens are visible and comparable, but smaller burden is not a selector and visibility is not closure.")
    print("  A later theory-owner convention choice must be explicit, labeled as choice if not derived, and must disclaim forbidden selectors.")
    print("  Context is improved enough to support a later explicit choice record, explicit parallel-record handoff, or continued deferral with a named target.")
    print("  No B_s branch is chosen.")
    print("  No trace-normalization declaration is completed.")
    print("  Package B is not adopted or recommended for adoption.")
    print("  B_s/F_zeta insertion, active O, residual control, recombination, and parent equation remain not ready.")
    print("\nPossible next step:")
    print("  explicit branch-choice record, explicit parallel-record route,")
    print("  source-hierarchy ranking route, branch consequence continuation,")
    print("  or continued deferral with a named narrowing target")
    print("\nForbidden immediate next step:")
    print("  Package B adoption, B_s/F_zeta insertion, active O, residual control, recombination, or parent closure")


def record_governance(ns, statuses: List[StatusEntry], gaps: List[GapEntry], handoffs: List[HandoffEntry], rules: List[RuleEntry]) -> None:
    record_marker(ns, MARKER_ID, "g44_selector_context_summary")
    for idx, item in enumerate(statuses, 1):
        record_claim(
            ns,
            f"g44_status_{idx}",
            MARKER_ID,
            item.status,
            f"{item.name}: {item.topic}. Result: {item.result}. Boundary: {item.boundary}.",
        )
    for idx, item in enumerate(gaps, 1):
        record_obligation(
            ns,
            f"g44_gap_{idx}",
            MARKER_ID,
            item.name,
            f"{item.reason}. Discipline: {item.discipline}.",
            item.status,
        )
    for idx, item in enumerate(handoffs, 1):
        record_claim(
            ns,
            f"g44_handoff_{idx}",
            MARKER_ID,
            item.status,
            f"{item.name}: {item.reason}. Caution: {item.caution}.",
        )
    for idx, item in enumerate(rules, 1):
        record_claim(
            ns,
            f"g44_rule_{idx}",
            MARKER_ID,
            "POLICY_RULE",
            f"Rejected upgrade: {item.upgrade}. Reason: {item.reason}.",
        )


def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    statuses = build_status_entries()
    gaps = build_gaps()
    handoffs = build_handoffs()
    rules = build_rejected_upgrades()
    case_0(out)
    case_1(out)
    case_2(out, statuses)
    case_3(out, gaps)
    case_4(out, handoffs)
    case_5(out, rules)
    case_6(out)
    final_interpretation()
    record_governance(ns, statuses, gaps, handoffs, rules)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
