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
#   43_trace_normalization_branch_or_parallel_decision_surface
# Script type:
#   STATUS SUMMARY

SCRIPT_LABEL = "Candidate Group 43 Status Summary"
MARKER_ID = "g43_summary"

DEPENDENCIES = [
    ("g43_recon", "43_trace_normalization_branch_or_parallel_decision_surface__candidate_branch_or_parallel_decision_batch_reconciliation", "g43_recon"),
    ("g43_obligation_matrix", "43_trace_normalization_branch_or_parallel_decision_surface__candidate_branch_decision_obligation_matrix", "g43_obligation_matrix"),
    ("g43_selector_sieve", "43_trace_normalization_branch_or_parallel_decision_surface__candidate_selector_admissibility_and_rejection_sieve", "g43_selector_sieve"),
    ("g43_parallel_records", "43_trace_normalization_branch_or_parallel_decision_surface__candidate_parallel_declaration_candidate_ledger", "g43_parallel_records"),
    ("g43_scale_branch", "43_trace_normalization_branch_or_parallel_decision_surface__candidate_scale_branch_choice_readiness_ledger", "g43_scale_branch"),
    ("g43_metric_branch", "43_trace_normalization_branch_or_parallel_decision_surface__candidate_metric_branch_choice_readiness_ledger", "g43_metric_branch"),
    ("g43_problem", "43_trace_normalization_branch_or_parallel_decision_surface__candidate_branch_or_parallel_decision_problem", "g43_problem"),
    ("g42_summary", "42_trace_anchor_equation_choice_exclusion_map__candidate_group_42_status_summary", "g42_summary"),
    ("g42_trace_norm_sieve", "42_trace_anchor_equation_choice_exclusion_map__candidate_trace_normalization_equation_family_sieve", "g42_trace_norm_sieve"),
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
        "BRANCH_DECISION_SURFACE": StatusMark.INFO,
        "BRANCH_CHOICE_CANDIDATE": StatusMark.INFO,
        "PARALLEL_RECORD_CANDIDATE": StatusMark.INFO,
        "ADMISSIBLE_CONTEXT": StatusMark.INFO,
        "EXPLICIT_CHOICE_REQUIRED": StatusMark.OBLIGATION,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "RECOVERY_SELECTOR_REJECTED": StatusMark.FAIL,
        "SELECTOR_REJECTED": StatusMark.FAIL,
        "FORBIDDEN_BY_GUARDRAIL": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "CONTINUED_DEFERRAL": StatusMark.DEFER,
        "DECLARATION_DEFERRED": StatusMark.DEFER,
        "NOT_DECLARED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "DEFER": StatusMark.DEFER,
        "CONDITIONAL": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def governance_status(status: str):
    # Keep archive writes robust across VacuumForge enum revisions.
    candidates = {
        "PASS": "POLICY_RULE",
        "MATCHED_EXPECTATION": "POLICY_RULE",
        "BRANCH_DECISION_SURFACE": "CANDIDATE_ROUTE",
        "BRANCH_CHOICE_CANDIDATE": "CANDIDATE_ROUTE",
        "PARALLEL_RECORD_CANDIDATE": "CANDIDATE_ROUTE",
        "ADMISSIBLE_CONTEXT": "CANDIDATE_ROUTE",
        "CONTINUED_DEFERRAL": "DEFERRED_PENDING_PREREQUISITES",
        "DECLARATION_DEFERRED": "DEFERRED_PENDING_PREREQUISITES",
        "NOT_DECLARED": "DEFERRED_PENDING_PREREQUISITES",
        "NOT_READY": "DEFERRED_PENDING_PREREQUISITES",
        "NOT_ADOPTED": "DEFERRED_PENDING_PREREQUISITES",
        "OPEN": "DEFERRED_PENDING_PREREQUISITES",
        "CONDITIONAL": "DEFERRED_PENDING_PREREQUISITES",
        "EXPLICIT_CHOICE_REQUIRED": "POLICY_RULE",
        "POLICY_RULE": "POLICY_RULE",
        "RECOVERY_SELECTOR_REJECTED": "REJECTED",
        "SELECTOR_REJECTED": "REJECTED",
        "FORBIDDEN_BY_GUARDRAIL": "POLICY_RULE",
        "FORBIDDEN_SHORTCUT": "POLICY_RULE",
    }
    enum_name = candidates.get(status, "POLICY_RULE")
    return getattr(GovernanceStatus, enum_name, GovernanceStatus.POLICY_RULE)


def obligation_status(status: str):
    if status in {"NOT_READY", "NOT_DECLARED", "DECLARATION_DEFERRED", "NOT_ADOPTED", "CONTINUED_DEFERRAL", "OPEN", "CONDITIONAL"}:
        return getattr(ObligationStatus, "DEFERRED", ObligationStatus.OPEN)
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
        scope="Group 43 trace-normalization branch-or-parallel decision surface summary",
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
            "G43-1: branch-or-parallel decision surface",
            "Group 43 opened as a trace-normalization branch-or-parallel decision-surface audit",
            "BRANCH_DECISION_SURFACE",
            "metric branch choice, scale branch choice, explicit parallel records, and continued deferral were separated as legitimate route classes",
            "route classification is not branch choice, trace-normalization declaration, adoption, insertion, or parent readiness",
        ),
        StatusEntry(
            "G43-2: metric branch route",
            "B_s_metric as future explicit branch-choice candidate",
            "BRANCH_CHOICE_CANDIDATE",
            "log(B_s_metric)=2*zeta/d remains visible as a metric-coefficient candidate form, with object/scope, zeta convention, traced dimension, selector, and downstream caveat obligations",
            "B_s_metric is not chosen, declared, inserted, or used as recovery-selected construction",
        ),
        StatusEntry(
            "G43-3: scale branch route",
            "b_s_scale as future explicit branch-choice candidate",
            "BRANCH_CHOICE_CANDIDATE",
            "log(b_s_scale)=zeta/d remains visible as a scale-factor candidate form, with object/scope, zeta convention, traced dimension, selector, and downstream caveat obligations",
            "b_s_scale is not chosen, declared, inserted, or used as recovery-selected construction",
        ),
        StatusEntry(
            "G43-4: explicit parallel records",
            "two branch-indexed trace-normalization candidate records",
            "PARALLEL_RECORD_CANDIDATE",
            "metric and scale candidate forms may be carried in parallel while preserving the factor-of-two burden",
            "parallel records are not one neutral law, not completed trace normalization, not adoption, and not insertion support",
        ),
        StatusEntry(
            "G43-5: selector discipline",
            "admissible and forbidden branch-decision selectors",
            "POLICY_RULE",
            "recovery, downstream convenience, neutral-expression, symbol-shape, and majority-count selectors were rejected; source hierarchy, consequence context, and explicit theory-owner convention may be context only",
            "context is not derivation; theory-owner convention must be daylight-labeled as choice if used later",
        ),
        StatusEntry(
            "G43-6: route obligation matrix",
            "obligations for metric choice, scale choice, parallel records, declaration, adoption, and insertion",
            "OPEN",
            "route-specific burdens were mapped so later work knows what must close before progress",
            "obligation visibility is not obligation closure and burden comparison is not a selector",
        ),
        StatusEntry(
            "G43-7: batch reconciliation",
            "actual batch outputs were reconciled before summary",
            "MATCHED_EXPECTATION",
            "outputs matched the expected decision-surface shape: routes classified, forbidden selectors rejected, obligations visible, no choice made",
            "reconciliation is not group closure by itself, branch choice, declaration completion, adoption, theorem proof, or insertion",
        ),
        StatusEntry(
            "G43-8: downstream gates",
            "Package B adoption, B_s/F_zeta insertion, active O, residual control, recombination, and parent closure",
            "NOT_READY",
            "all downstream gates remain closed after decision-surface work",
            "Group 43 is not Package B adoption, scalar recombination, active O construction, residual control, or parent readiness",
        ),
    ]


def build_gaps() -> List[GapEntry]:
    return [
        GapEntry(
            "G1: no branch chosen",
            "DECLARATION_DEFERRED",
            "metric and scale routes are visible but neither B_s_metric nor b_s_scale is selected",
            "a later explicit branch-choice record is required for a single active branch",
        ),
        GapEntry(
            "G2: metric branch obligations",
            "OPEN",
            "metric branch choice still needs object/scope, zeta convention, traced dimension, admissible selector record, and downstream caveats",
            "candidate form is not declaration support by itself",
        ),
        GapEntry(
            "G3: scale branch obligations",
            "OPEN",
            "scale branch choice still needs object/scope, zeta convention, traced dimension, admissible selector record, and downstream caveats",
            "determinant/root intuition may be context only and cannot become derivation",
        ),
        GapEntry(
            "G4: parallel record obligations",
            "NOT_DECLARED",
            "parallel records preserve visibility but do not complete trace normalization",
            "do not collapse metric and scale candidate forms into an unqualified B_s law or neutral F_zeta expression",
        ),
        GapEntry(
            "G5: selector evidence quality",
            "OPEN",
            "source hierarchy can be admissible context only if source authority is ranked rather than counted by hits",
            "do not use recovery, downstream convenience, or symbol-shape shortcuts as selectors",
        ),
        GapEntry(
            "G6: trace-normalization declaration",
            "NOT_DECLARED",
            "declaration requires an explicit branch or explicit parallel-record assumptions plus conventions",
            "decision-surface clarity is not declaration completion",
        ),
        GapEntry(
            "G7: adoption and insertion",
            "NOT_READY",
            "branch route clarity does not license Package B adoption or B_s/F_zeta insertion",
            "residual/source/boundary/divergence gates remain separate",
        ),
        GapEntry(
            "G8: recombination and parent closure",
            "NOT_READY",
            "route classification does not solve active O, residual control, recombination, or parent identity",
            "parent field-equation routes remain closed",
        ),
    ]


def build_handoffs() -> List[HandoffEntry]:
    return [
        HandoffEntry(
            "H1: explicit branch-choice record",
            "EXPLICIT_CHOICE_REQUIRED",
            "may deliberately choose B_s_metric or b_s_scale as a labeled theory-owner convention or supported decision",
            "must not claim derivation from recovery, downstream convenience, majority notation, or neutral expression",
        ),
        HandoffEntry(
            "H2: source-hierarchy evidence route",
            "OPEN",
            "may rank earliest or authoritative notation sources to inform a later decision",
            "source hierarchy is context, not branch choice by itself",
        ),
        HandoffEntry(
            "H3: branch consequence comparison",
            "ADMISSIBLE_CONTEXT",
            "may compare obligation profiles and later consequences for metric, scale, and parallel routes",
            "consequence comparison must not become downstream-convenience selection",
        ),
        HandoffEntry(
            "H4: explicit parallel declaration candidate route",
            "PARALLEL_RECORD_CANDIDATE",
            "may carry two branch-indexed candidate records to avoid premature branch choice",
            "parallel records are not one neutral law and not completed declaration",
        ),
        HandoffEntry(
            "H5: continued deferral",
            "CONTINUED_DEFERRAL",
            "may keep branch choice deferred while residual/source/boundary/insertion theorem work continues",
            "deferral is not branch rejection or theorem failure",
        ),
        HandoffEntry(
            "H6: trace-normalization declaration attempt",
            "NOT_DECLARED",
            "may later attempt declaration only after branch or parallel-record assumptions and conventions are explicit",
            "not available directly from Group 43 as a completed result",
        ),
        HandoffEntry(
            "H7: insertion or parent route",
            "NOT_READY",
            "not available from Group 43",
            "forbidden as immediate handoff",
        ),
    ]


def build_rejected_upgrades() -> List[RuleEntry]:
    return [
        RuleEntry("R1: decision surface as branch choice", "treat metric/scale route readiness as choosing a branch", "route classification is not choice"),
        RuleEntry("R2: candidate form as declaration", "treat log(B_s_metric)=2*zeta/d or log(b_s_scale)=zeta/d as completed trace normalization", "candidate forms are non-active"),
        RuleEntry("R3: parallel records as neutral law", "collapse two branch-indexed records into one unqualified B_s or neutral F_zeta law", "that hides the factor-of-two burden"),
        RuleEntry("R4: recovery as selector", "choose branch from AB=1, B=1/A, Schwarzschild, gamma, weak-field success, kappa=0, or parent fit", "recovery is audit only"),
        RuleEntry("R5: downstream convenience as selector", "choose the branch that makes insertion, residual handling, or parent fit easier", "downstream convenience smuggles the construction target"),
        RuleEntry("R6: neutral expression as selector", "place zeta/d or 2*zeta/d under neutral F_zeta to force a decision", "neutral F_zeta must remain expression-free"),
        RuleEntry("R7: context as derivation", "treat source hierarchy, consequence context, or intuition as theorem proof", "context and convention are not derivation"),
        RuleEntry("R8: obligations as closed", "treat listed obligations as satisfied because they are visible", "visibility is not closure"),
        RuleEntry("R9: deferral as branch rejection", "treat continued deferral as proof neither branch works", "deferral is governance status, not no-go theorem"),
        RuleEntry("R10: decision surface as downstream readiness", "open adoption, insertion, active O, residual control, recombination, or parent route", "downstream gates remain closed"),
    ]


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  What did Group 43 establish about whether trace normalization should proceed")
    print("  by metric branch choice, scale branch choice, explicit parallel records,")
    print("  or continued deferral?")
    print("\nDiscipline:\n")
    print("  This script summarizes Group 43 after reviewing the batch outputs.")
    print("  It does not choose B_s_metric or b_s_scale.")
    print("  It does not complete trace-normalization declaration.")
    print("  It adopts nothing, inserts nothing, constructs no active O, and opens no parent gate.")
    with out.governance_assessments():
        out.line(
            "Group 43 status summary opened",
            StatusMark.PASS,
            "closing branch-or-parallel decision-surface audit while preserving branch-deferred/no-declaration/no-insertion boundary",
        )


def case_1(out: ScriptOutput) -> None:
    header("Case 1: Group 43 summary boundary ledger")
    ledger = [
        ("decision surface", "BRANCH_DECISION_SURFACE", "metric, scale, parallel, and deferral routes separated"),
        ("metric branch", "BRANCH_CHOICE_CANDIDATE", "B_s_metric candidate visible but not chosen"),
        ("scale branch", "BRANCH_CHOICE_CANDIDATE", "b_s_scale candidate visible but not chosen"),
        ("parallel records", "PARALLEL_RECORD_CANDIDATE", "two explicit non-active records may preserve the factor-of-two burden"),
        ("selector discipline", "POLICY_RULE", "recovery, downstream convenience, neutral expression, and weak notation selectors rejected"),
        ("route obligations", "OPEN", "obligations visible but not closed"),
        ("trace declaration", "NOT_DECLARED", "no trace-normalization declaration completed"),
        ("downstream gates", "NOT_READY", "adoption, insertion, active O, residual control, recombination, and parent closure remain closed"),
    ]
    for name, status, detail in ledger:
        with out.governance_assessments():
            out.line(name, mark(status), f"{status}: {detail}")


def case_2(out: ScriptOutput, entries: List[StatusEntry]) -> None:
    header("Case 2: Group 43 status entries")
    for item in entries:
        subheader(item.name)
        print(f"Topic: {item.topic}")
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.result}. Boundary: {item.boundary}")
    with out.governance_assessments():
        out.line("Group 43 status entries stated", StatusMark.PASS, f"{len(entries)} status entries stated")


def case_3(out: ScriptOutput, gaps: List[GapEntry]) -> None:
    header("Case 3: Final open gaps")
    for item in gaps:
        subheader(item.name)
        with out.unresolved_obligations():
            out.line(item.name, mark(item.status), f"{item.status}: {item.reason}. Discipline: {item.discipline}")
    with out.unresolved_obligations():
        out.line("Group 43 final gaps stated", StatusMark.PASS, f"{len(gaps)} gaps remain open, deferred, not declared, or not ready")


def case_4(out: ScriptOutput, handoffs: List[HandoffEntry]) -> None:
    header("Case 4: Final handoffs")
    for item in handoffs:
        subheader(item.name)
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.reason}. Caution: {item.caution}")
    with out.governance_assessments():
        out.line("Group 43 handoffs stated", StatusMark.DEFER, f"{len(handoffs)} handoffs stated; choices, declarations, and downstream gates remain separate")


def case_5(out: ScriptOutput, rules: List[RuleEntry]) -> None:
    header("Case 5: Rejected summary upgrades")
    for item in rules:
        subheader(item.name)
        print(f"Upgrade: {item.upgrade}")
        with out.governance_assessments():
            out.line(item.name, StatusMark.OBLIGATION, f"POLICY_RULE: {item.reason}")
    with out.governance_assessments():
        out.line("Group 43 summary upgrades rejected", StatusMark.PASS, f"{len(rules)} upgrade shortcuts rejected as policy rules")


def case_6(out: ScriptOutput) -> None:
    header("Case 6: Group 43 conclusions")
    conclusions = [
        ("C1: Group 43 result", "BRANCH_DECISION_SURFACE", "Group 43 completed a branch-or-parallel decision-surface audit"),
        ("C2: branch choice status", "DECLARATION_DEFERRED", "no metric or scale branch is chosen"),
        ("C3: route classes", "PASS", "metric choice, scale choice, parallel records, and continued deferral are separated"),
        ("C4: selector status", "POLICY_RULE", "forbidden selectors are rejected and admissible context remains non-active"),
        ("C5: declaration status", "NOT_DECLARED", "trace normalization is not completed"),
        ("C6: no adoption or insertion", "NOT_READY", "Package B adoption and B_s/F_zeta insertion remain closed"),
        ("C7: parent status", "NOT_READY", "active O, residual control, recombination, and parent equation remain not ready"),
    ]
    for name, status, meaning in conclusions:
        subheader(name)
        with out.governance_assessments():
            out.line(name, mark(status), f"{status}: {meaning}")
    with out.governance_assessments():
        out.line(
            "Group 43 status summary conclusion stated",
            StatusMark.PASS,
            "decision surface clarified; no branch, declaration, adoption, insertion, active O, recombination, or parent route opened",
        )


def final_interpretation() -> None:
    header("Final interpretation")
    print("Group 43 status summary result:\n")
    print("  Group 43 completed a trace-normalization branch-or-parallel decision-surface audit.")
    print("  The legitimate route classes are now separated: metric branch choice, scale branch choice, explicit parallel records, and continued deferral.")
    print("  B_s_metric remains a future explicit-choice candidate, carrying log(B_s_metric)=2*zeta/d only as a non-active candidate form.")
    print("  b_s_scale remains a future explicit-choice candidate, carrying log(b_s_scale)=zeta/d only as a non-active candidate form.")
    print("  Explicit parallel records remain available as a visibility route that preserves the factor-of-two burden without choosing a branch.")
    print("  Continued deferral remains legitimate and is not branch rejection.")
    print("  Recovery, downstream convenience, neutral-expression, inherited-symbol, and majority-count selectors are rejected.")
    print("  Source hierarchy, consequence context, and theory-owner convention may inform a later explicit decision, but are not derivations.")
    print("  Route obligations are visible but not closed.")
    print("  No B_s branch is chosen.")
    print("  No trace-normalization declaration is completed.")
    print("  Package B is not adopted or recommended for adoption.")
    print("  B_s/F_zeta insertion, active O, residual control, recombination, and parent equation remain not ready.")
    print("\nPossible next step:")
    print("  explicit branch-choice record, source-hierarchy evidence route,")
    print("  branch consequence comparison, explicit parallel declaration candidate route,")
    print("  continued deferral with residual/source theorem work, or later trace-normalization declaration attempt")
    print("\nForbidden immediate next step:")
    print("  Package B adoption, B_s/F_zeta insertion, active O, residual control, recombination, or parent closure")


def record_governance(ns, statuses: List[StatusEntry], gaps: List[GapEntry], handoffs: List[HandoffEntry], rules: List[RuleEntry]) -> None:
    record_marker(ns, MARKER_ID, MARKER_ID)
    for idx, item in enumerate(statuses, 1):
        record_claim(
            ns,
            f"g43_status_c{idx}",
            MARKER_ID,
            item.status,
            f"{item.name}: {item.topic}. Result: {item.result}. Boundary: {item.boundary}.",
        )
    for idx, item in enumerate(gaps, 1):
        record_obligation(
            ns,
            f"g43_gap_{idx}",
            MARKER_ID,
            item.name,
            f"{item.reason}. Discipline: {item.discipline}.",
            item.status,
        )
    for idx, item in enumerate(handoffs, 1):
        record_claim(
            ns,
            f"g43_handoff_{idx}",
            MARKER_ID,
            item.status,
            f"{item.name}: {item.reason}. Caution: {item.caution}.",
        )
    for idx, item in enumerate(rules, 1):
        record_claim(
            ns,
            f"g43_rule_{idx}",
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
