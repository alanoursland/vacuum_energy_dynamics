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

SCRIPT_LABEL = "Candidate Group 49 Status Summary"
MARKER_ID = "g49_summary"
DEPENDENCIES = [
    ("g49_recon", "49_parallel_trace_declaration_readiness_review__candidate_declaration_readiness_review_batch_reconciliation", "g49_recon"),
    ("g49_route_classifier", "49_parallel_trace_declaration_readiness_review__candidate_parallel_declaration_attempt_route_classifier", "g49_route_classifier"),
    ("g49_failure_sieve", "49_parallel_trace_declaration_readiness_review__candidate_predeclaration_failure_mode_sieve", "g49_failure_sieve"),
    ("g49_requirement_matrix", "49_parallel_trace_declaration_readiness_review__candidate_declaration_record_requirement_matrix", "g49_requirement_matrix"),
    ("g49_numeric_d_readiness", "49_parallel_trace_declaration_readiness_review__candidate_numeric_d_condition_readiness_audit", "g49_numeric_d_readiness"),
    ("g49_record_acceptance", "49_parallel_trace_declaration_readiness_review__candidate_scope_status_record_acceptance_audit", "g49_record_acceptance"),
    ("g49_problem", "49_parallel_trace_declaration_readiness_review__candidate_declaration_readiness_review_problem", "g49_problem"),
    ("g48_summary", "48_explicit_paired_declaration_scope_status_record__candidate_group_48_status_summary", "g48_summary"),
]


@dataclass(frozen=True)
class StatusEntry:
    name: str
    topic: str
    status: str
    conclusion: str
    boundary: str


@dataclass(frozen=True)
class GapEntry:
    name: str
    status: str
    gap: str
    discipline: str


@dataclass(frozen=True)
class HandoffEntry:
    name: str
    status: str
    route: str
    caution: str


@dataclass(frozen=True)
class RejectedUpgrade:
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
        "DECLARATION_READINESS_REVIEW": StatusMark.INFO,
        "RECORD_ACCEPTED_FOR_REVIEW": StatusMark.INFO,
        "READY_FOR_DECLARATION_ATTEMPT_WITH_CONDITIONS": StatusMark.INFO,
        "DECLARATION_ATTEMPT_CANDIDATE": StatusMark.INFO,
        "DECLARATION_RECORD_REQUIREMENT": StatusMark.INFO,
        "PAIRED_SCOPE_STATUS_RECORD": StatusMark.INFO,
        "SCOPE_STATUS_RECORD": StatusMark.INFO,
        "STATUS_FIELD": StatusMark.INFO,
        "ASSUMPTION_FIELD": StatusMark.INFO,
        "CAVEAT_FIELD": StatusMark.INFO,
        "SYMBOLIC_D_ALLOWED": StatusMark.INFO,
        "NUMERIC_D_CONDITION": StatusMark.OBLIGATION,
        "CONSISTENCY_RULE": StatusMark.OBLIGATION,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "SCOPE_REQUIRED": StatusMark.OBLIGATION,
        "REJECTED_ROUTE": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "NOT_DECLARED": StatusMark.DEFER,
        "NOT_CHOSEN": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "THEOREM_REQUIRED": StatusMark.DEFER,
        "CHOICE_REQUIRED": StatusMark.DEFER,
        "AXIOM_REQUIRED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {"REJECTED_ROUTE", "FORBIDDEN_SHORTCUT"}:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {"POLICY_RULE", "CONSISTENCY_RULE", "NUMERIC_D_CONDITION", "SCOPE_REQUIRED"}:
        return GovernanceStatus.POLICY_RULE
    return GovernanceStatus.UNVERIFIED


def obligation_status(status: str) -> ObligationStatus:
    if status in {
        "DEFERRED_WITH_TARGET",
        "NOT_DECLARED",
        "NOT_CHOSEN",
        "NOT_ADOPTED",
        "NOT_DERIVED",
        "THEOREM_REQUIRED",
        "CHOICE_REQUIRED",
        "AXIOM_REQUIRED",
        "NOT_READY",
    }:
        return ObligationStatus.DEFERRED
    return ObligationStatus.OPEN


def record_marker(ns, marker_id: str, symbol_name: str, scope: str) -> None:
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[],
        output=sp.Symbol(symbol_name),
        method="inventory marker; no physical derivation",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
        scope=scope,
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


def record_obligation(ns, obligation_id: str, statement: str, status: str = "OPEN") -> None:
    ns.record_obligation(
        ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=obligation_id,
            status=obligation_status(status),
            required_by=[SCRIPT_ID],
            description=statement,
        )
    )


def emit_line(out: ScriptOutput, label: str, status: str, text: str, *, obligation: bool = False) -> None:
    if obligation:
        with out.unresolved_obligations():
            out.line(label, mark(status), f"{status}: {text}")
    else:
        with out.governance_assessments():
            out.line(label, mark(status), f"{status}: {text}")


def build_status_entries() -> List[StatusEntry]:
    return [
        StatusEntry(
            "G49-1: declaration-readiness review",
            "Group 49 reviewed whether the Group 48 paired scope/status record can support a later declaration attempt",
            "DECLARATION_READINESS_REVIEW",
            "the review target is accepted as the instantiated paired declaration-scope/status artifact",
            "readiness review is not trace-normalization declaration",
        ),
        StatusEntry(
            "G49-2: record accepted as input",
            "accepted review input",
            "RECORD_ACCEPTED_FOR_REVIEW",
            "identity, domain, status, assumptions, numeric-d condition, caveats, and handoff route are complete enough for review",
            "input acceptance is not equation installation",
        ),
        StatusEntry(
            "G49-3: numeric-d condition",
            "symbolic and scope-conditioned dimension handling",
            "READY_FOR_DECLARATION_ATTEMPT_WITH_CONDITIONS",
            "numeric d does not block a symbolic paired declaration attempt if numeric d remains explicitly conditioned and unfixed",
            "not a numeric d declaration and not parent-facing dimension support",
        ),
        StatusEntry(
            "G49-4: declaration-record requirements",
            "future declaration-attempt record fields",
            "DECLARATION_RECORD_REQUIREMENT",
            "the future attempt must include identity, paired branch domain, separated expressions, zeta/d clauses, status transition, and downstream caveats",
            "requirement clarity is not declaration execution",
        ),
        StatusEntry(
            "G49-5: failure modes",
            "predeclaration failure-mode sieve",
            "REJECTED_ROUTE",
            "branch smuggling, neutral-law collapse, numeric-d leakage, recovery selector use, and downstream drift were rejected",
            "bad broadenings die while the limited symbolic paired route survives",
        ),
        StatusEntry(
            "G49-6: next route",
            "parallel declaration attempt route classification",
            "DEFERRED_WITH_TARGET",
            "the next non-looping target is a separate parallel trace-normalization declaration attempt under stated conditions",
            "attempt-ready is not declaration success and the attempt may fail or remain conditional",
        ),
        StatusEntry(
            "G49-7: downstream locks",
            "insertion, active O, residual/source safety, recombination, and parent closure",
            "NOT_READY",
            "all downstream field-equation gates remain closed after declaration-readiness review",
            "readiness cannot be used as scalar-response law, projector construction, safety theorem, or parent identity",
        ),
    ]


def build_gaps() -> List[GapEntry]:
    return [
        GapEntry("G1: declaration attempt not yet written", "DEFERRED_WITH_TARGET", "the separate parallel declaration-attempt record is now the next target but has not been written", "do not call Group 49 the declaration"),
        GapEntry("G2: trace normalization undeclared", "NOT_DECLARED", "trace normalization remains undeclared until a separate attempt succeeds or is explicitly classified", "avoid readiness-as-declaration drift"),
        GapEntry("G3: numeric d condition", "NUMERIC_D_CONDITION", "numeric d remains conditioned and unfixed", "future attempt must remain symbolic/scope-conditioned"),
        GapEntry("G4: branch neutrality", "NOT_CHOSEN", "B_s_metric and b_s_scale remain paired candidates", "do not smuggle branch choice through declaration language"),
        GapEntry("G5: Package B adoption", "NOT_ADOPTED", "attempt-readiness is not Package B adoption", "adoption remains a separate explicit theory decision"),
        GapEntry("G6: downstream machinery", "NOT_READY", "B_s/F_zeta insertion, active O, residual/source safety, recombination, and parent closure remain closed", "do not turn declaration readiness into field-equation use"),
    ]


def build_handoffs() -> List[HandoffEntry]:
    return [
        HandoffEntry("H1: separate parallel declaration attempt", "DEFERRED_WITH_TARGET", "write a separate symbolic paired trace-normalization declaration-attempt record", "must preserve paired labels, separated expressions, symbolic d, numeric-d condition, and caveats"),
        HandoffEntry("H2: failure-aware declaration review", "POLICY_RULE", "carry Group 49 failure modes into the declaration attempt", "branch smuggling, neutral-law collapse, numeric-d leak, recovery selection, and downstream drift must fail the attempt"),
        HandoffEntry("H3: explicit branch-choice route", "NOT_CHOSEN", "available only as a separate daylight-labeled choice route", "do not let the paired declaration attempt choose metric or scale"),
        HandoffEntry("H4: adoption route", "NOT_ADOPTED", "available only after separate theory decision", "declaration attempt permission is not adoption"),
        HandoffEntry("H5: insertion or parent route", "NOT_READY", "not available from Group 49", "requires scalar-response law, safety gates, active projector if needed, and parent identity support"),
    ]


def build_rejected_upgrades() -> List[RejectedUpgrade]:
    return [
        RejectedUpgrade("R1: readiness as declaration", "Treat Group 49 readiness as trace-normalization declaration", "readiness permits only a separate attempt"),
        RejectedUpgrade("R2: attempt-ready as guaranteed success", "Assume the future declaration attempt must succeed", "the attempt may fail or remain conditional"),
        RejectedUpgrade("R3: numeric d fixed", "Quietly fix numeric d in the future attempt", "numeric d remains conditioned"),
        RejectedUpgrade("R4: neutral law", "Collapse the paired expressions into unqualified B_s or neutral F_zeta", "factor-of-two burden must stay visible"),
        RejectedUpgrade("R5: branch choice by attempt", "Let the declaration attempt choose metric or scale", "branch choice requires a separate explicit record"),
        RejectedUpgrade("R6: recovery support", "Use Schwarzschild, AB=1, gamma, or weak-field recovery as declaration support", "recovery remains audit only"),
        RejectedUpgrade("R7: declaration as adoption", "Treat declaration attempt permission as Package B adoption", "adoption remains separate"),
        RejectedUpgrade("R8: declaration as insertion", "Use attempt-readiness to insert B_s/F_zeta", "insertion remains not ready"),
        RejectedUpgrade("R9: caveats as theorems", "Treat caveats as residual/source safety proof", "negative caveats are not positive theorems"),
        RejectedUpgrade("R10: parent-facing readiness", "Call the symbolic paired route parent-facing", "parent identity and safety support are absent"),
    ]


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  What did Group 49 establish about whether the instantiated paired")
    print("  declaration-scope/status record can support a later parallel")
    print("  trace-normalization declaration attempt?\n")
    print("Discipline:\n")
    print("  This script summarizes Group 49 after reviewing the batch outputs.")
    print("  It preserves attempt-ready-with-conditions status while keeping")
    print("  trace normalization undeclared. It chooses no branch, adopts nothing,")
    print("  inserts nothing, constructs no active O, and opens no parent gate.")
    emit_line(out, "Group 49 status summary opened", "PASS", "closing declaration-readiness review while preserving attempt-ready-with-conditions / no-declaration / no-insertion boundary")


def case_1(out: ScriptOutput) -> None:
    header("Case 1: Group 49 summary boundary ledger")
    ledger = [
        ("declaration-readiness review", "DECLARATION_READINESS_REVIEW", "readiness reviewed without declaration"),
        ("scope/status record", "RECORD_ACCEPTED_FOR_REVIEW", "Group 48 artifact accepted as review input"),
        ("numeric d", "READY_FOR_DECLARATION_ATTEMPT_WITH_CONDITIONS", "symbolic paired attempt may proceed only with numeric d conditioned and unfixed"),
        ("declaration requirements", "DECLARATION_RECORD_REQUIREMENT", "future declaration-attempt fields explicit"),
        ("failure modes", "REJECTED_ROUTE", "branch smuggling, neutral-law collapse, numeric-d leak, recovery support, and downstream drift rejected"),
        ("next target", "DEFERRED_WITH_TARGET", "separate parallel trace-normalization declaration attempt under conditions"),
        ("trace declaration", "NOT_DECLARED", "trace normalization remains undeclared"),
        ("downstream gates", "NOT_READY", "adoption, insertion, active O, residual control, recombination, and parent closure remain closed"),
    ]
    for subject, status, text in ledger:
        emit_line(out, subject, status, text)


def case_2(out: ScriptOutput, entries: List[StatusEntry]) -> None:
    header("Case 2: Group 49 status entries")
    for entry in entries:
        subheader(entry.name)
        print(f"Topic: {entry.topic}")
        emit_line(out, entry.name, entry.status, f"{entry.conclusion}. Boundary: {entry.boundary}.")
    emit_line(out, "Group 49 status entries stated", "PASS", f"{len(entries)} status entries stated")


def case_3(out: ScriptOutput, gaps: List[GapEntry]) -> None:
    header("Case 3: Final open gaps")
    for gap in gaps:
        subheader(gap.name)
        emit_line(out, gap.name, gap.status, f"{gap.gap}. Discipline: {gap.discipline}.", obligation=True)
    emit_line(out, "Group 49 final gaps stated", "PASS", f"{len(gaps)} gaps remain open, conditioned, not chosen, not declared, not adopted, not derived, or not ready", obligation=True)


def case_4(out: ScriptOutput, handoffs: List[HandoffEntry]) -> None:
    header("Case 4: Final handoffs")
    for handoff in handoffs:
        subheader(handoff.name)
        emit_line(out, handoff.name, handoff.status, f"{handoff.route}. Caution: {handoff.caution}.")
    emit_line(out, "Group 49 handoffs stated", "DEFERRED_WITH_TARGET", f"{len(handoffs)} handoffs stated; separate declaration attempt is the next non-looping target")


def case_5(out: ScriptOutput, rejected: List[RejectedUpgrade]) -> None:
    header("Case 5: Rejected summary upgrades")
    for upgrade in rejected:
        subheader(upgrade.name)
        print(f"Upgrade: {upgrade.upgrade}")
        emit_line(out, upgrade.name, "POLICY_RULE", upgrade.reason)
    emit_line(out, "Group 49 summary upgrades rejected", "PASS", f"{len(rejected)} upgrade shortcuts rejected as policy rules")


def case_6(out: ScriptOutput) -> None:
    header("Case 6: Group 49 conclusions")
    conclusions = [
        ("C1: Group 49 result", "DECLARATION_READINESS_REVIEW", "Group 49 completed a declaration-readiness review"),
        ("C2: input status", "RECORD_ACCEPTED_FOR_REVIEW", "the Group 48 paired scope/status record is accepted as review input"),
        ("C3: attempt status", "READY_FOR_DECLARATION_ATTEMPT_WITH_CONDITIONS", "a separate symbolic paired declaration attempt is an honest next target under conditions"),
        ("C4: declaration status", "NOT_DECLARED", "trace normalization is not declared"),
        ("C5: branch/adoption status", "NOT_ADOPTED", "no branch is chosen and Package B is not adopted"),
        ("C6: downstream status", "NOT_READY", "B_s/F_zeta insertion, active O, recombination, and parent equation remain not ready"),
    ]
    for label, status, text in conclusions:
        emit_line(out, label, status, text)
    emit_line(out, "Group 49 status summary conclusion stated", "PASS", "attempt-ready-with-conditions status established; no declaration, adoption, insertion, active O, recombination, or parent route opened")
    header("Final interpretation")
    print("Group 49 status summary result:\n")
    print("  Group 49 completed declaration-readiness review for the paired trace-normalization route.")
    print("  The Group 48 paired scope/status record is accepted as input for a future declaration attempt.")
    print("  Symbolic d may be carried into the attempt, but numeric d remains conditioned and unfixed.")
    print("  Future declaration-attempt requirements are explicit: identity, paired branch domain,")
    print("  separated expressions, zeta/d clauses, status transition, and downstream caveats.")
    print("  Forbidden broadenings were rejected: branch smuggling, neutral-law collapse, numeric-d leak,")
    print("  recovery-selector support, insertion, active O, safety-proof, recombination, and parent use.")
    print("  The next non-looping target is a separate symbolic paired trace-normalization declaration attempt under conditions.")
    print("  No trace-normalization declaration is completed.")
    print("  Package B is not adopted or recommended for adoption.")
    print("  B_s/F_zeta insertion, active O, residual control, source protection, recombination, and parent equation remain not ready.\n")
    print("Possible next step:")
    print("  separate symbolic paired trace-normalization declaration attempt with explicit caveats and failure criteria\n")
    print("Forbidden immediate next step:")
    print("  Package B adoption, B_s/F_zeta insertion, active O, recombination, or parent closure")


def record_governance(ns, entries: List[StatusEntry], gaps: List[GapEntry], handoffs: List[HandoffEntry], rejected: List[RejectedUpgrade]) -> None:
    record_marker(
        ns,
        MARKER_ID,
        "group49_declaration_readiness_review_marker",
        "Group 49 status summary marker: declaration-readiness review completed; attempt-ready-with-conditions; no declaration or downstream route",
    )
    for idx, entry in enumerate(entries, start=1):
        record_claim(ns, f"{MARKER_ID}_entry_{idx}", MARKER_ID, entry.status, f"{entry.name}: {entry.conclusion}. Boundary: {entry.boundary}.")
    for idx, gap in enumerate(gaps, start=1):
        record_obligation(ns, f"{MARKER_ID}_gap_{idx}", f"{gap.name}: {gap.gap}. Discipline: {gap.discipline}.", gap.status)
    for idx, handoff in enumerate(handoffs, start=1):
        record_claim(ns, f"{MARKER_ID}_handoff_{idx}", MARKER_ID, handoff.status, f"{handoff.name}: {handoff.route}. Caution: {handoff.caution}.")
    for idx, upgrade in enumerate(rejected, start=1):
        record_claim(ns, f"{MARKER_ID}_rejected_{idx}", MARKER_ID, "POLICY_RULE", f"Rejected upgrade {upgrade.name}: {upgrade.upgrade}; reason: {upgrade.reason}.")


def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    entries = build_status_entries()
    gaps = build_gaps()
    handoffs = build_handoffs()
    rejected = build_rejected_upgrades()
    case_0(out)
    case_1(out)
    case_2(out, entries)
    case_3(out, gaps)
    case_4(out, handoffs)
    case_5(out, rejected)
    case_6(out)
    record_governance(ns, entries, gaps, handoffs, rejected)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
