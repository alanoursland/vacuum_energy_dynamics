from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple

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


@dataclass(frozen=True)
class Entry:
    name: str
    subject: str
    status: str
    detail: str
    boundary: str


@dataclass(frozen=True)
class Shortcut:
    name: str
    shortcut: str
    reason: str


@dataclass(frozen=True)
class ObligationEntry:
    name: str
    status: str
    obligation: str
    discipline: str


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
    for item in dependencies:
        if len(item) == 3:
            dep_id, upstream_script_id, upstream_derivation_id = item
            expected_record_kind = RecordKind.INVENTORY_MARKER
        else:
            dep_id, upstream_script_id, upstream_derivation_id, expected_record_kind = item
        ns.declare_dependency(
            dependency_id=dep_id,
            upstream_script_id=upstream_script_id,
            upstream_derivation_id=upstream_derivation_id,
            expected_record_kind=expected_record_kind,
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
        "ADOPTION_DECISION_SURFACE": StatusMark.INFO,
        "THEORY_DECISION_REQUIRED": StatusMark.DEFER,
        "ADOPTION_DECISION_DEFERRED": StatusMark.DEFER,
        "CANDIDATE_RETAINED_FOR_AUDIT": StatusMark.INFO,
        "SAFETY_THEOREMS_REQUIRED": StatusMark.OBLIGATION,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_INSERTABLE": StatusMark.DEFER,
        "NOT_PARENT_FACING": StatusMark.DEFER,
        "REJECTED_ROUTE": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "RECORD_LEVEL_ONLY": StatusMark.INFO,
        "CONDITIONAL_RECORD_ONLY": StatusMark.INFO,
        "PHYSICAL_USE_REJECTED": StatusMark.FAIL,
        "BRANCH_BURDEN_LIVE": StatusMark.PASS,
        "PREREQUISITE_OPEN": StatusMark.OBLIGATION,
        "CHOICE_REQUIRED": StatusMark.DEFER,
        "NUMERIC_D_CONDITION": StatusMark.OBLIGATION,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "NOT_READY": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {"REJECTED_ROUTE", "FORBIDDEN_SHORTCUT", "PHYSICAL_USE_REJECTED"}:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {"POLICY_RULE", "SAFETY_THEOREMS_REQUIRED", "NUMERIC_D_CONDITION", "BRANCH_BURDEN_LIVE"}:
        return GovernanceStatus.POLICY_RULE
    return GovernanceStatus.UNVERIFIED


def obligation_status(status: str) -> ObligationStatus:
    if status in {
        "THEORY_DECISION_REQUIRED",
        "ADOPTION_DECISION_DEFERRED",
        "SAFETY_THEOREMS_REQUIRED",
        "DEFERRED_WITH_TARGET",
        "PREREQUISITE_OPEN",
        "CHOICE_REQUIRED",
        "NUMERIC_D_CONDITION",
        "NOT_READY",
        "NOT_DERIVED",
        "NOT_ADOPTED",
        "NOT_INSERTABLE",
        "NOT_PARENT_FACING",
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


def record_obligation(ns, obligation_id: str, title: str, statement: str, status: str = "OPEN") -> None:
    ns.record_obligation(
        ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=obligation_status(status),
            required_by=[SCRIPT_ID],
            description=statement,
        )
    )


def emit_entries(out: ScriptOutput, entries: List[Entry], title: str) -> None:
    header(title)
    for item in entries:
        subheader(item.name)
        print(f"Subject: {item.subject}")
        print(f"Detail: {item.detail}")
        print(f"Boundary: {item.boundary}")
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.detail}. Boundary: {item.boundary}")


def emit_shortcuts(out: ScriptOutput, shortcuts: List[Shortcut]) -> None:
    header("Rejected shortcuts and invalid upgrades")
    for item in shortcuts:
        subheader(item.name)
        print(f"Shortcut: {item.shortcut}")
        with out.counterexamples():
            out.line(item.name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {item.reason}")


def emit_obligations(out: ScriptOutput, obligations: List[ObligationEntry]) -> None:
    header("Open obligations and deferred burdens")
    for item in obligations:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        with out.unresolved_obligations():
            out.line(item.name, mark(item.status), f"{item.status}: {item.obligation}; discipline: {item.discipline}")


def record_governance(ns, marker_id: str, symbol_name: str, entries: List[Entry], obligations: List[ObligationEntry], scope: str) -> None:
    record_marker(ns, marker_id, symbol_name, scope)
    for idx, item in enumerate(entries, start=1):
        record_claim(
            ns,
            f"{marker_id}_claim_{idx}",
            marker_id,
            item.status,
            f"{item.name}: {item.subject}. {item.detail}. Boundary: {item.boundary}.",
        )
    for idx, item in enumerate(obligations, start=1):
        record_obligation(
            ns,
            f"{marker_id}_obligation_{idx}",
            item.name,
            f"{item.obligation}. Discipline: {item.discipline}.",
            item.status,
        )


SCRIPT_LABEL = 'Candidate Decision Surface Route Classifier'
MARKER_ID = 'g51_route_classifier'
SYMBOL_NAME = 'G51_decision_surface_route_classifier'
SCOPE = 'Group 51 classifier after audits: classifies next honest route without making adoption decision'
DEPENDENCIES = [('g50_summary', '50_symbolic_paired_trace_normalization_declaration_attempt__candidate_group_50_status_summary', 'g50_summary'), ('g51_record_level_adoption', '51_trace_normalization_adopt_defer_reject_decision_surface__candidate_record_level_adoption_meaning_audit', 'g51_record_level_adoption'), ('g51_prereq_matrix', '51_trace_normalization_adopt_defer_reject_decision_surface__candidate_adoption_prerequisite_matrix', 'g51_prereq_matrix'), ('g51_defer_route', '51_trace_normalization_adopt_defer_reject_decision_surface__candidate_defer_route_and_theorem_dependency_audit', 'g51_defer_route'), ('g51_rejection_sieve', '51_trace_normalization_adopt_defer_reject_decision_surface__candidate_rejection_trigger_sieve', 'g51_rejection_sieve')]
QUESTION = 'After adoption meaning, prerequisites, deferral dependencies, and rejection triggers are visible, what is the next honest route?'
DISCIPLINE = 'This classifier reports the decision surface. It does not execute adoption or physical insertion.'
OPENING_LINE = 'Decision-surface route classifier opened -- classify route, do not decide adoption'
NEXT_SCRIPT = 'candidate_adopt_defer_reject_decision_batch_reconciliation.py'


def build_entries() -> List[Entry]:
    return [Entry(*item) for item in [('C1: narrow record route', 'conditional record-level adoption candidate can survive only as caveated audit preservation', 'CONDITIONAL_RECORD_ONLY', 'record-level route is coherent only if non-insertion and caveats remain attached', 'not Package B adoption'), ('C2: strong adoption route', 'stronger adoption remains deferred pending choices and safety theorems', 'ADOPTION_DECISION_DEFERRED', 'the prerequisite matrix remains open', 'not adopted'), ('C3: physical use route', 'B_s/F_zeta insertion and parent-facing use are rejected for now', 'PHYSICAL_USE_REJECTED', 'no insertion, active O, safety, boundary, or divergence support exists', 'not insertable'), ('C4: rejection route', 'rejection applies to forbidden broadenings rather than the narrow conditional candidate', 'REJECTED_ROUTE', 'neutral collapse, numeric leak, recovery support, hidden branch choice, and insertion drift fail', 'not total no-go'), ('C5: next technical route', 'residual/source/boundary safety load testing is the best non-looping technical target', 'DEFERRED_WITH_TARGET', 'the conditional attempt should be tested against physical blockers', 'not another declaration loop'), ('C6: decision route', 'an explicit theory-owner adopt/defer/reject decision remains a possible separate route', 'THEORY_DECISION_REQUIRED', 'decision authority stays outside this classifier', 'not decided here')]]


def build_shortcuts() -> List[Shortcut]:
    return [Shortcut(*item) for item in [('X1: classifier as adoption', 'treat route classification as adopting the record', 'the classifier reports options only'), ('X2: classifier as summary insertion', 'turn C1 into B_s/F_zeta insertion readiness', 'conditional record route is non-insertable'), ('X3: classifier as total rejection', 'turn rejection of bad upgrades into rejection of the narrow candidate', 'the narrow candidate is retained for audit'), ('X4: classifier as next group command', 'assume Group 52 without reading actual outputs', 'handoff should follow reconciliation and summary')]]


def build_obligations() -> List[ObligationEntry]:
    return [ObligationEntry(*item) for item in [('O1: preserve classifier boundary', 'POLICY_RULE', 'report decision-surface classification without executing adoption', 'avoid script-derived theory decision'), ('O2: move to safety load testing', 'DEFERRED_WITH_TARGET', 'consider residual/source/boundary safety as the next technical target', 'avoid trace-declaration looping'), ('O3: preserve explicit decision option', 'THEORY_DECISION_REQUIRED', 'a theory-owner adopt/defer/reject decision remains separate if desired', 'avoid hidden decision')]]


def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header(SCRIPT_LABEL)
    print("Question:\n")
    print(QUESTION)
    print("\nDiscipline:\n")
    print(DISCIPLINE)
    with out.governance_assessments():
        out.line(f"{SCRIPT_LABEL} opened", StatusMark.PASS, OPENING_LINE)

    entries = build_entries()
    shortcuts = build_shortcuts()
    obligations = build_obligations()

    emit_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    emit_shortcuts(out, shortcuts)
    emit_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in [('route classified', 'PASS', 'decision surface classification is complete enough for reconciliation'), ('strong adoption deferred', 'ADOPTION_DECISION_DEFERRED', 'no adoption decision is made by classifier')]:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, SYMBOL_NAME, entries, obligations, SCOPE)
    ns.write_run_metadata()
    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
