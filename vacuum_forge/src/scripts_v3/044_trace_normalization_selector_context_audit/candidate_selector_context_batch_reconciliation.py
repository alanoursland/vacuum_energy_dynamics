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
        "CONTEXT_ONLY": StatusMark.INFO,
        "ADMISSIBLE_CONTEXT": StatusMark.INFO,
        "EVIDENCE_CONTEXT": StatusMark.INFO,
        "CONSEQUENCE_CONTEXT": StatusMark.INFO,
        "ROUTE_BURDEN_CONTEXT": StatusMark.INFO,
        "BRANCH_CHOICE_CANDIDATE": StatusMark.INFO,
        "PARALLEL_RECORD_CANDIDATE": StatusMark.INFO,
        "PARALLEL_ROUTE_PREFERRED": StatusMark.INFO,
        "CONTINUED_DEFERRAL": StatusMark.DEFER,
        "CONTEXT_INSUFFICIENT": StatusMark.DEFER,
        "CONTEXT_READY": StatusMark.DEFER,
        "CHOICE_CONTEXT_READY": StatusMark.DEFER,
        "EXPLICIT_CHOICE_REQUIRED": StatusMark.OBLIGATION,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "OPEN": StatusMark.DEFER,
        "DEFER": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "NOT_DECLARED": StatusMark.DEFER,
        "DECLARATION_DEFERRED": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "SELECTOR_REJECTED": StatusMark.FAIL,
        "RECOVERY_SELECTOR_REJECTED": StatusMark.FAIL,
        "FORBIDDEN_BY_GUARDRAIL": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "REJECTED": StatusMark.FAIL,
        "ELIMINATED": StatusMark.FAIL,
    }.get(status, StatusMark.INFO)


def obligation_status(status: str) -> ObligationStatus:
    if status in {"NOT_READY", "NOT_DECLARED", "DECLARATION_DEFERRED", "NOT_ADOPTED", "NOT_DERIVED", "CONTEXT_INSUFFICIENT", "CONTINUED_DEFERRAL"}:
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


def record_claim(ns, claim_id: str, marker_id: str, statement: str, status=GovernanceStatus.POLICY_RULE) -> None:
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


def record_obligation(ns, obligation_id: str, title: str, description: str, status: str = "OPEN") -> None:
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
    title: str
    status: str
    obligation: str
    discipline: str

# Group:
#   44_trace_normalization_selector_context_audit
# Script type:
#   AUDIT / CONTEXT

SCRIPT_LABEL = 'Candidate Selector Context Batch Reconciliation'
MARKER_ID = 'g44_recon'
DEPENDENCIES = [
    ('g43_summary', '043_trace_normalization_branch_or_parallel_decision_surface__candidate_group_43_status_summary', 'g43_summary'),
    ('g44_problem', '044_trace_normalization_selector_context_audit__candidate_selector_context_problem', 'g44_problem'),
    ('g44_source_hierarchy', '044_trace_normalization_selector_context_audit__candidate_source_hierarchy_evidence_ledger', 'g44_source_hierarchy'),
    ('g44_consequence_context', '044_trace_normalization_selector_context_audit__candidate_branch_consequence_context_matrix', 'g44_consequence_context'),
    ('g44_route_burden', '044_trace_normalization_selector_context_audit__candidate_route_burden_comparison_audit', 'g44_route_burden'),
    ('g44_owner_boundary', '044_trace_normalization_selector_context_audit__candidate_theory_owner_choice_boundary', 'g44_owner_boundary'),
    ('g44_context_sufficiency', '044_trace_normalization_selector_context_audit__candidate_context_sufficiency_and_deferral_sieve', 'g44_context_sufficiency'),
]
SCOPE = 'Group 44 trace-normalization selector-context audit'
QUESTION = 'Did the Group 44 batch sharpen admissible selector context without turning context into a branch choice?'
DISCIPLINE = 'This script reconciles the Group 44 batch. It does not close the group as final summary and does not choose, declare, adopt, insert, or open parent closure.'
OPENING_STATUS = 'selector-context audit only; no branch choice, declaration completion, adoption, insertion, active O, recombination, or parent route'
CASE_1_TITLE = 'Case 1: Batch reconciliation entries'
NEXT_SCRIPT = 'candidate_group_44_status_summary.py'
CONCLUSIONS = [('batch reconciliation prepared', 'PASS', 'write summary only after actual outputs are reviewed'),
        ('no group close here', 'DEFER', 'candidate_group_44_status_summary.py should be written after review')]

def build_entries() -> List[Entry]:
    return [
        Entry('Q1: opener expectation', 'Group 44 opened as selector-context audit', 'MATCHED_EXPECTATION', 'expected if context was sharpened without branch choice', 'summary may call this context audit only'),
        Entry('Q2: source hierarchy expectation', 'source hierarchy evidence was ranked as context', 'MATCHED_EXPECTATION', 'expected if majority count and inherited symbol shape remain rejected selectors', 'summary must preserve evidence/context boundary'),
        Entry('Q3: consequence expectation', 'branch consequences were compared as risk/burden context', 'MATCHED_EXPECTATION', 'expected if downstream convenience remains forbidden', 'summary must not choose from convenience'),
        Entry('Q4: route burden expectation', 'route burdens were compared but not used as selector', 'MATCHED_EXPECTATION', 'expected if smaller burden remains context only', 'summary must not choose by burden count'),
        Entry('Q5: convention boundary expectation', 'future theory-owner choice requirements were stated', 'MATCHED_EXPECTATION', 'expected if intuition remains explicit choice, not derivation', 'summary must not make the choice'),
        Entry('Q6: context sufficiency expectation', 'choice-ready, parallel-preferred, and deferral conditions were classified as handoff statuses', 'MATCHED_EXPECTATION', 'expected if no recommendation executes a route', 'summary must preserve handoff-only status'),
        Entry('Q7: downstream gates', 'adoption, insertion, active O, residual control, recombination, and parent closure remain closed', 'NOT_READY', 'expected final boundary', 'summary must not open field-equation routes'),
    ]

def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: reconciliation as final summary', 'treat this script as group close', 'final summary should follow actual outputs after review'),
        Shortcut('X2: context as choice', 'treat source, consequence, burden, or convention context as selecting metric or scale branch', 'context is not choice'),
        Shortcut('X3: recommendation as declaration', 'treat handoff recommendation as trace-normalization declaration', 'recommendation is not execution'),
        Shortcut('X4: convention boundary as adopted convention', 'treat the choice-boundary script as making the theory-owner choice', 'boundary is not choice'),
        Shortcut('X5: context as insertion', 'open B_s/F_zeta insertion or parent route from sharpened context', 'downstream gates remain closed'),
    ]

def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: summary must follow actual outputs', 'final summary must report any mismatch in batch outputs', 'OPEN', 'actual outputs control close', 'avoid self-validation'),
        ObligationEntry('O2: preserve context/choice boundary', 'final summary must say no branch or route was selected', 'POLICY_RULE', 'context may inform later choice only', 'avoid choice by summary prose'),
        ObligationEntry('O3: preserve handoff-only recommendations', 'choice-ready or parallel-preferred statuses remain recommendations only', 'OPEN', 'handoff status is not execution', 'avoid declaration drift'),
        ObligationEntry('O4: preserve downstream locks', 'adoption, insertion, active O, recombination, and parent closure remain closed', 'NOT_READY', 'context audit cannot open field-equation routes', 'avoid overreach'),
    ]


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    for line in QUESTION.splitlines():
        print("  " + line if line else "")
    print("\nDiscipline:\n")
    for line in DISCIPLINE.splitlines():
        print("  " + line if line else "")
    with out.governance_assessments():
        out.line(f"{SCRIPT_LABEL} opened", StatusMark.PASS, OPENING_STATUS)


def case_1(out: ScriptOutput, entries: List[Entry]) -> None:
    header(CASE_1_TITLE)
    for item in entries:
        subheader(item.name)
        print(f"Subject: {item.subject}")
        print(f"Detail: {item.detail}")
        print(f"Boundary: {item.boundary}")
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.detail}. Boundary: {item.boundary}")


def case_2(out: ScriptOutput, shortcuts: List[Shortcut]) -> None:
    header("Case 2: Invalid upgrades and forbidden shortcuts")
    for item in shortcuts:
        subheader(item.name)
        print(f"Shortcut: {item.shortcut}")
        with out.counterexamples():
            out.line(item.name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {item.reason}")


def case_3(out: ScriptOutput, obligations: List[ObligationEntry]) -> None:
    header("Case 3: Open obligations")
    for item in obligations:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        with out.unresolved_obligations():
            out.line(item.name, mark(item.status), f"{item.status}: {item.obligation}; discipline: {item.discipline}")


def case_4(out: ScriptOutput) -> None:
    header("Case 4: Local conclusions")
    with out.governance_assessments():
        for name, status, detail in CONCLUSIONS:
            out.line(name, mark(status), detail)
    print("\nPossible next script:")
    print("  " + NEXT_SCRIPT)


def record_governance(ns, entries: List[Entry], obligations: List[ObligationEntry]) -> None:
    record_marker(ns, MARKER_ID, MARKER_ID, SCOPE)
    for idx, item in enumerate(entries, 1):
        record_claim(
            ns,
            f"{MARKER_ID}_c{idx}",
            MARKER_ID,
            f"{item.name}: {item.subject}. {item.detail}. Boundary: {item.boundary}.",
        )
    for idx, item in enumerate(obligations, 1):
        record_obligation(
            ns,
            f"{MARKER_ID}_o{idx}",
            item.title,
            f"{item.obligation}. Discipline: {item.discipline}.",
            item.status,
        )


def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    entries = build_entries()
    shortcuts = build_shortcuts()
    obligations = build_obligations()
    case_0(out)
    case_1(out, entries)
    case_2(out, shortcuts)
    case_3(out, obligations)
    case_4(out)
    record_governance(ns, entries, obligations)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
