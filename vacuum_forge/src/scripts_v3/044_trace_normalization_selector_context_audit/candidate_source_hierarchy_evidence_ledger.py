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

SCRIPT_LABEL = 'Candidate Source Hierarchy Evidence Ledger'
MARKER_ID = 'g44_source_hierarchy'
DEPENDENCIES = [
    ('g43_summary', '43_trace_normalization_branch_or_parallel_decision_surface__candidate_group_43_status_summary', 'g43_summary'),
    ('g43_selector_sieve', '43_trace_normalization_branch_or_parallel_decision_surface__candidate_selector_admissibility_and_rejection_sieve', 'g43_selector_sieve'),
    ('g44_problem', '44_trace_normalization_selector_context_audit__candidate_selector_context_problem', 'g44_problem'),
]
SCOPE = 'Group 44 trace-normalization selector-context audit'
QUESTION = 'What source or notation evidence can legitimately inform a later trace-normalization route choice?'
DISCIPLINE = 'This script ranks evidence-context classes. It separates source hierarchy from majority notation count and does not let evidence choose a branch.'
OPENING_STATUS = 'selector-context audit only; no branch choice, declaration completion, adoption, insertion, active O, recombination, or parent route'
CASE_1_TITLE = 'Case 1: Source hierarchy evidence entries'
NEXT_SCRIPT = 'candidate_branch_consequence_context_matrix.py'
CONCLUSIONS = [('source hierarchy ledger complete', 'PASS', 'source evidence classes ranked as context'),
        ('no evidence selector activated', 'DEFER', 'source hierarchy remains context only')]

def build_entries() -> List[Entry]:
    return [
        Entry('E1: earliest internal definition', 'earliest explicit internal definition may be high-value context', 'EVIDENCE_CONTEXT', 'earliest definitions help identify intended object meaning', 'not a branch selector by itself'),
        Entry('E2: authoritative current snapshot', 'current snapshot and governance records may outrank older shorthand', 'EVIDENCE_CONTEXT', 'current records represent repaired notation state', 'snapshot status is not adoption or choice'),
        Entry('E3: actual script/governance records', 'script outputs with archive markers may clarify what is currently allowed', 'ADMISSIBLE_CONTEXT', 'records expose route status and obligations', 'record presence is not theorem proof'),
        Entry('E4: result summaries', 'group summaries may summarize accepted state if aligned with actual outputs', 'ADMISSIBLE_CONTEXT', 'summaries are useful navigation context', 'not proof archive and not selector alone'),
        Entry('E5: older overloaded shorthand', 'older unqualified B_s usage is weak context only', 'CONTEXT_INSUFFICIENT', 'old shorthand predates notation repair and may hide overload', 'cannot restore overloaded B_s'),
        Entry('E6: majority hit count', 'majority notation count is rejected as selector', 'SELECTOR_REJECTED', 'hit count ignores authority, age, and overload', 'not admissible without source hierarchy'),
        Entry('E7: source hierarchy outcome', 'evidence can improve later explicit choice only when ranked', 'OPEN', 'ranked hierarchy may reduce ambiguity', 'still context, not derivation'),
    ]

def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: hit-count branch choice', 'choose the branch with the most textual appearances', 'majority count is not authority'),
        Shortcut('X2: old shorthand revival', 'use old B_s shorthand to collapse metric and scale branches', 'notation split repaired a real overload'),
        Shortcut('X3: summary as proof', 'treat a result summary as theorem support', 'summaries are navigation artifacts'),
        Shortcut('X4: source hierarchy as declaration', 'treat evidence ranking as trace-normalization declaration', 'evidence context cannot install equation'),
    ]

def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: rank source authority', 'rank sources by authority, recency of repaired notation, and relevance', 'OPEN', 'source hierarchy must be explicit before use', 'avoid cherry-picking'),
        ObligationEntry('O2: preserve repaired notation', 'keep B_s_metric and b_s_scale distinct where branch matters', 'POLICY_RULE', 'do not return to unqualified B_s', 'avoid overload reentry'),
        ObligationEntry('O3: keep evidence contextual', 'evidence may inform only a later explicit decision', 'OPEN', 'evidence cannot choose a branch by itself', 'avoid context-as-choice'),
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
