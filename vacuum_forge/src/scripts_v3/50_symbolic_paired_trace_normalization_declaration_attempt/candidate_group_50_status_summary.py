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
SCRIPT_LABEL = "Candidate Group 50 Status Summary"
MARKER_ID = "g50_summary"
DEPENDENCIES = [
    ("g50_recon", "50_symbolic_paired_trace_normalization_declaration_attempt__candidate_symbolic_paired_declaration_attempt_batch_reconciliation", "g50_recon"),
    ("g50_survival_classifier", "50_symbolic_paired_trace_normalization_declaration_attempt__candidate_declaration_attempt_survival_classifier", "g50_survival_classifier"),
    ("g50_failure_sieve", "50_symbolic_paired_trace_normalization_declaration_attempt__candidate_declaration_attempt_failure_sieve", "g50_failure_sieve"),
    ("g50_numeric_zeta_guard", "50_symbolic_paired_trace_normalization_declaration_attempt__candidate_numeric_d_and_zeta_clause_guard", "g50_numeric_zeta_guard"),
    ("g50_expression_separation", "50_symbolic_paired_trace_normalization_declaration_attempt__candidate_declaration_expression_separation_audit", "g50_expression_separation"),
    ("g50_attempt_record", "50_symbolic_paired_trace_normalization_declaration_attempt__candidate_paired_declaration_attempt_record", "g50_attempt_record"),
    ("g50_problem", "50_symbolic_paired_trace_normalization_declaration_attempt__candidate_symbolic_paired_declaration_attempt_problem", "g50_problem"),
    ("g49_summary", "49_parallel_trace_declaration_readiness_review__candidate_group_49_status_summary", "g49_summary"),
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
        "SYMBOLIC_PAIRED_DECLARATION_ATTEMPT": StatusMark.INFO,
        "CONDITIONAL_DECLARATION_ATTEMPT_STATED": StatusMark.INFO,
        "DECLARATION_ATTEMPT_CONDITIONAL_ONLY": StatusMark.INFO,
        "DECLARATION_ATTEMPT_SURVIVES_WITH_CONDITIONS": StatusMark.INFO,
        "DECLARATION_RECORD_FIELD": StatusMark.INFO,
        "PAIRED_BRANCH_DOMAIN": StatusMark.INFO,
        "BRANCH_INDEXED": StatusMark.INFO,
        "EXPRESSION_SEPARATION": StatusMark.INFO,
        "ZETA_CLAUSE": StatusMark.INFO,
        "SYMBOLIC_D_ALLOWED": StatusMark.INFO,
        "CAVEAT_FIELD": StatusMark.INFO,
        "NUMERIC_D_CONDITION": StatusMark.OBLIGATION,
        "CONSISTENCY_RULE": StatusMark.OBLIGATION,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REJECTED_ROUTE": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "NOT_DECLARED": StatusMark.DEFER,
        "NOT_CHOSEN": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "THEOREM_REQUIRED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {"REJECTED_ROUTE", "FORBIDDEN_SHORTCUT"}:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {"POLICY_RULE", "CONSISTENCY_RULE", "NUMERIC_D_CONDITION"}:
        return GovernanceStatus.POLICY_RULE
    return GovernanceStatus.UNVERIFIED


def obligation_status(status: str) -> ObligationStatus:
    if status in {"DEFERRED_WITH_TARGET", "NOT_DECLARED", "NOT_CHOSEN", "NOT_ADOPTED", "NOT_DERIVED", "THEOREM_REQUIRED", "NOT_READY"}:
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
        StatusEntry("G50-1: declaration attempt opened", "Group 50 stated the symbolic paired trace-normalization declaration attempt authorized by Group 49", "SYMBOLIC_PAIRED_DECLARATION_ATTEMPT", "the attempt record exists under explicit conditions", "not automatic success, adoption, insertion, or parent use"),
        StatusEntry("G50-2: paired declaration record", "attempt record identity, paired domain, symbolic mode, and caveats", "CONDITIONAL_DECLARATION_ATTEMPT_STATED", "the record lists both branch-indexed candidates and carries symbolic d, shared zeta, numeric-d condition, and caveats", "not Package B adoption or field-equation use"),
        StatusEntry("G50-3: expression separation", "metric and scale expressions", "EXPRESSION_SEPARATION", "log(B_s_metric)=2*zeta/d and log(b_s_scale)=zeta/d remain separated", "not one neutral law, compromise expression, or branch choice"),
        StatusEntry("G50-4: zeta and d guard", "shared zeta, symbolic d, numeric-d condition, and parent-facing block", "SYMBOLIC_D_ALLOWED", "zeta remains record-local trace payload and d remains symbolic while numeric d is conditioned", "not F_zeta, numeric closure, or parent-facing dimension"),
        StatusEntry("G50-5: failure sieve", "forbidden declaration broadenings", "REJECTED_ROUTE", "branch smuggling, neutral collapse, numeric leak, recovery support, and downstream drift fail", "bad broadenings die while the narrow paired attempt survives"),
        StatusEntry("G50-6: survival classification", "honest status of the attempt", "DECLARATION_ATTEMPT_CONDITIONAL_ONLY", "the attempt survives only as a conditional pre-adoption trace-normalization candidate", "not insertable, adopted, or available for parent equation use"),
        StatusEntry("G50-7: downstream locks", "adoption, insertion, active O, residual/source safety, recombination, and parent closure", "NOT_READY", "all downstream field-equation gates remain closed after the attempt", "conditional attempt cannot be used as scalar-response law or parent identity"),
    ]


def build_gaps() -> List[GapEntry]:
    return [
        GapEntry("G1: adoption", "NOT_ADOPTED", "Package B is not adopted by the conditional attempt", "adoption requires a separate explicit theory decision"),
        GapEntry("G2: field-equation use", "NOT_READY", "B_s/F_zeta insertion, active O, recombination, and parent closure remain closed", "do not treat conditional declaration attempt as field-equation machinery"),
        GapEntry("G3: numeric d", "NUMERIC_D_CONDITION", "numeric d remains conditioned and unfixed", "do not fix d by recovery, convenience, or hidden postulate"),
        GapEntry("G4: branch choice", "NOT_CHOSEN", "B_s_metric and b_s_scale remain paired branch-indexed candidates", "do not select either branch through declaration prose"),
        GapEntry("G5: residual/source theorems", "NOT_DERIVED", "the attempt proves no residual nonentry or source protection theorem", "negative caveats are not positive safety theorems"),
    ]


def build_handoffs() -> List[HandoffEntry]:
    return [
        HandoffEntry("H1: conditional attempt closeout", "DEFERRED_WITH_TARGET", "carry the conditional symbolic paired declaration attempt forward as a trace-normalization candidate", "must preserve conditions, separated expressions, numeric-d condition, and caveats"),
        HandoffEntry("H2: adoption decision route", "NOT_ADOPTED", "evaluate Package B or trace-normalization adoption only as a separate theory decision", "conditional attempt survival is not adoption"),
        HandoffEntry("H3: residual/source safety theorem route", "NOT_DERIVED", "attempt residual nonentry, source no-double-counting, or A-sector protection theorems", "the conditional attempt supplies no theorem support by itself"),
        HandoffEntry("H4: insertion or parent route", "NOT_READY", "not available from Group 50", "requires scalar-response law, safety gates, and parent identity support"),
    ]


def build_rejected() -> List[RejectedUpgrade]:
    return [
        RejectedUpgrade("R1: conditional as adoption", "Treat the conditional attempt as Package B adoption", "adoption remains separate"),
        RejectedUpgrade("R2: conditional as insertion", "Use the attempt in B_s/F_zeta insertion", "insertion requires separate scalar-response law and safety gates"),
        RejectedUpgrade("R3: neutral law", "Collapse paired expressions into unqualified B_s or neutral F_zeta", "factor-of-two burden must stay visible"),
        RejectedUpgrade("R4: branch choice", "Let the paired attempt select metric or scale", "branch choice requires separate explicit record"),
        RejectedUpgrade("R5: numeric d fixed", "Quietly fix numeric d", "numeric d remains conditioned"),
        RejectedUpgrade("R6: recovery support", "Use recovery as support for the attempt", "recovery remains audit only"),
        RejectedUpgrade("R7: caveats as theorems", "Treat caveats as residual/source safety proof", "negative caveats are not positive theorems"),
        RejectedUpgrade("R8: parent-ready", "Call the attempt parent-facing or parent-ready", "parent identity and safety support are absent"),
    ]


def record_governance(ns, entries, gaps, handoffs, rejected):
    record_marker(ns, MARKER_ID, "G50_conditional_paired_trace_declaration_attempt", "Group 50 conditional symbolic paired trace-normalization declaration attempt; no adoption or insertion")
    for idx, item in enumerate(entries, start=1):
        record_claim(ns, f"{MARKER_ID}_entry_{idx}", MARKER_ID, item.status, f"{item.name}: {item.conclusion}. Boundary: {item.boundary}.")
    for idx, item in enumerate(gaps, start=1):
        record_obligation(ns, f"{MARKER_ID}_gap_{idx}", f"{item.name}: {item.gap}. Discipline: {item.discipline}.", item.status)
    for idx, item in enumerate(handoffs, start=1):
        record_obligation(ns, f"{MARKER_ID}_handoff_{idx}", f"{item.name}: {item.route}. Caution: {item.caution}.", item.status)
    for idx, item in enumerate(rejected, start=1):
        record_claim(ns, f"{MARKER_ID}_rejected_{idx}", MARKER_ID, "POLICY_RULE", f"Rejected upgrade: {item.upgrade}. Reason: {item.reason}.")


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  What did Group 50 establish by stating the symbolic paired")
    print("  trace-normalization declaration attempt authorized by Group 49?\n")
    print("Discipline:\n")
    print("  This script summarizes Group 50 after reviewing the batch outputs.")
    print("  It preserves conditional-attempt status while keeping adoption,")
    print("  insertion, active O, recombination, and parent closure closed.")
    emit_line(out, "Group 50 status summary opened", "PASS", "closing symbolic paired declaration attempt while preserving conditional-only / no-adoption / no-insertion boundary")


def case_1(out: ScriptOutput) -> None:
    header("Case 1: Group 50 summary boundary ledger")
    ledger = [
        ("declaration attempt", "SYMBOLIC_PAIRED_DECLARATION_ATTEMPT", "symbolic paired trace-normalization declaration attempt stated"),
        ("attempt record", "CONDITIONAL_DECLARATION_ATTEMPT_STATED", "paired declaration-attempt record exists under conditions"),
        ("expression separation", "EXPRESSION_SEPARATION", "metric and scale expressions remain separated"),
        ("zeta and d", "SYMBOLIC_D_ALLOWED", "zeta remains payload and d remains symbolic with numeric d conditioned"),
        ("failure modes", "REJECTED_ROUTE", "branch smuggling, neutral collapse, numeric leak, recovery support, and downstream drift rejected"),
        ("survival status", "DECLARATION_ATTEMPT_CONDITIONAL_ONLY", "attempt survives only as conditional pre-adoption candidate"),
        ("downstream gates", "NOT_READY", "adoption, insertion, active O, residual control, recombination, and parent closure remain closed"),
    ]
    for subject, status, text in ledger:
        emit_line(out, subject, status, text)


def case_2(out: ScriptOutput, entries: List[StatusEntry]) -> None:
    header("Case 2: Group 50 status entries")
    for entry in entries:
        subheader(entry.name)
        print(f"Topic: {entry.topic}")
        emit_line(out, entry.name, entry.status, f"{entry.conclusion}. Boundary: {entry.boundary}.")
    emit_line(out, "Group 50 status entries stated", "PASS", f"{len(entries)} status entries stated")


def case_3(out: ScriptOutput, gaps: List[GapEntry]) -> None:
    header("Case 3: Final open gaps")
    for gap in gaps:
        subheader(gap.name)
        emit_line(out, gap.name, gap.status, f"{gap.gap}. Discipline: {gap.discipline}.", obligation=True)
    emit_line(out, "Group 50 final gaps stated", "PASS", f"{len(gaps)} gaps remain open, conditioned, not chosen, not adopted, not derived, or not ready", obligation=True)


def case_4(out: ScriptOutput, handoffs: List[HandoffEntry]) -> None:
    header("Case 4: Final handoffs")
    for handoff in handoffs:
        subheader(handoff.name)
        emit_line(out, handoff.name, handoff.status, f"{handoff.route}. Caution: {handoff.caution}.")
    emit_line(out, "Group 50 handoffs stated", "DEFERRED_WITH_TARGET", f"{len(handoffs)} handoffs stated; conditional attempt and downstream locks remain separate")


def case_5(out: ScriptOutput, rejected: List[RejectedUpgrade]) -> None:
    header("Case 5: Rejected summary upgrades")
    for item in rejected:
        subheader(item.name)
        print(f"Upgrade: {item.upgrade}")
        emit_line(out, item.name, "POLICY_RULE", item.reason)
    emit_line(out, "Group 50 summary upgrades rejected", "PASS", f"{len(rejected)} upgrade shortcuts rejected as policy rules")


def case_6(out: ScriptOutput) -> None:
    header("Case 6: Group 50 conclusions")
    conclusions = [
        ("C1: Group 50 result", "SYMBOLIC_PAIRED_DECLARATION_ATTEMPT", "Group 50 stated the symbolic paired trace-normalization declaration attempt"),
        ("C2: attempt status", "DECLARATION_ATTEMPT_CONDITIONAL_ONLY", "the attempt survives only as conditional caveated pre-adoption candidate"),
        ("C3: expression status", "EXPRESSION_SEPARATION", "paired expressions remain separated and branch-indexed"),
        ("C4: declaration/use status", "NOT_READY", "attempt status is not insertable or parent-facing"),
        ("C5: adoption status", "NOT_ADOPTED", "Package B is not adopted"),
        ("C6: downstream status", "NOT_READY", "B_s/F_zeta insertion, active O, recombination, and parent equation remain not ready"),
    ]
    for label, status, text in conclusions:
        emit_line(out, label, status, text)
    emit_line(out, "Group 50 status summary conclusion stated", "PASS", "conditional paired declaration attempt stated; no adoption, insertion, active O, recombination, or parent route opened")
    header("Final interpretation")
    print("Group 50 status summary result:\n")
    print("  Group 50 stated the symbolic paired trace-normalization declaration attempt authorized by Group 49.")
    print("  The attempt carries both branch-indexed expressions:")
    print("    log(B_s_metric)=2*zeta/d")
    print("    log(b_s_scale)=zeta/d")
    print("  The attempt remains symbolic and scope-conditioned: zeta is a record-local trace payload, symbolic d is allowed, and numeric d remains conditioned and unfixed.")
    print("  The attempt survives only as a conditional, caveated, pre-adoption trace-normalization candidate.")
    print("  Branch smuggling, neutral-law collapse, numeric-d leakage, recovery support, insertion drift, active-O drift, safety-proof drift, recombination, and parent use remain rejected.")
    print("  Package B is not adopted or recommended for adoption.")
    print("  B_s/F_zeta insertion, active O, residual control, source protection, recombination, and parent equation remain not ready.\n")
    print("Possible next step:")
    print("  explicit adoption/defer/reject decision for the conditional attempt, or residual/source safety theorem work before any physical use\n")
    print("Forbidden immediate next step:")
    print("  B_s/F_zeta insertion, active O, recombination, or parent closure")


def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    entries = build_status_entries()
    gaps = build_gaps()
    handoffs = build_handoffs()
    rejected = build_rejected()
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
