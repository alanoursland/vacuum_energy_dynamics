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

SCRIPT_LABEL = 'Candidate Theory-Owner Choice Boundary'
MARKER_ID = 'g44_owner_boundary'
DEPENDENCIES = [
    ('g43_summary', '043_trace_normalization_branch_or_parallel_decision_surface__candidate_group_43_status_summary', 'g43_summary'),
    ('g43_selector_sieve', '043_trace_normalization_branch_or_parallel_decision_surface__candidate_selector_admissibility_and_rejection_sieve', 'g43_selector_sieve'),
    ('g44_route_burden', '044_trace_normalization_selector_context_audit__candidate_route_burden_comparison_audit', 'g44_route_burden'),
]
SCOPE = 'Group 44 trace-normalization selector-context audit'
QUESTION = 'What must a later explicit theory-owner convention choice say if intuition is used to choose a trace-normalization route?'
DISCIPLINE = 'This script defines the boundary for future explicit convention choice. It does not make the choice.'
OPENING_STATUS = 'selector-context audit only; no branch choice, declaration completion, adoption, insertion, active O, recombination, or parent route'
CASE_1_TITLE = 'Case 1: Theory-owner choice boundary entries'
NEXT_SCRIPT = 'candidate_context_sufficiency_and_deferral_sieve.py'
CONCLUSIONS = [('theory-owner choice boundary complete', 'PASS', 'future convention-choice requirements stated'),
        ('no convention choice made', 'DEFER', 'theory-owner choice remains future explicit route')]

def build_entries() -> List[Entry]:
    return [
        Entry('T1: chosen route field', 'future choice record must name metric, scale, parallel, or deferral route', 'EXPLICIT_CHOICE_REQUIRED', 'choice cannot be implicit', 'not supplied here'),
        Entry('T2: not-derived label', 'future convention must say it is a choice or convention if not derived', 'EXPLICIT_CHOICE_REQUIRED', 'intuition enters in daylight', 'not theorem proof'),
        Entry('T3: forbidden-selector disclaimer', 'future choice must disclaim recovery, downstream convenience, neutral-expression, and majority-count selection', 'POLICY_RULE', 'choice must not pretend forbidden selectors are valid', 'not optional'),
        Entry('T4: known obligations', 'future choice must list remaining object/scope, zeta, dimension, source, residual, boundary, and insertion obligations', 'OPEN', 'choice cannot erase burdens', 'not declaration completion'),
        Entry('T5: downstream non-readiness', 'future choice must state that insertion, active O, recombination, and parent closure remain closed', 'NOT_READY', 'branch choice is insufficient for field-equation use', 'not insertable'),
        Entry('T6: reversal or deferral condition', 'future choice record should state what later theorem failure would force reconsideration or deferral', 'CONTEXT_ONLY', 'choice should remain accountable to later constraints', 'not instability by itself'),
    ]

def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: intuition as theorem', 'state an intuitive branch preference as derived result', 'choice must be labeled as choice'),
        Shortcut('X2: choice erases obligations', 'let an explicit choice close residual/source/boundary/insertion obligations', 'choice does not prove theorems'),
        Shortcut('X3: choice as adoption', 'treat branch convention as Package B adoption', 'adoption requires separate decision'),
        Shortcut('X4: choice as insertion', 'insert B_s/F_zeta after naming branch', 'insertion law remains separate'),
    ]

def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: require explicit choice record', 'future convention must be recorded as explicit choice', 'EXPLICIT_CHOICE_REQUIRED', 'do not let prose choose silently', 'avoid hidden postulate'),
        ObligationEntry('O2: require forbidden-selector disclaimer', 'future choice must reject recovery and convenience selectors', 'POLICY_RULE', 'choice cannot rely on forbidden selectors', 'avoid smuggled derivation'),
        ObligationEntry('O3: preserve downstream caveats', 'future choice must preserve non-readiness of insertion and parent routes', 'NOT_READY', 'choice is not recombination', 'avoid field-equation overreach'),
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
