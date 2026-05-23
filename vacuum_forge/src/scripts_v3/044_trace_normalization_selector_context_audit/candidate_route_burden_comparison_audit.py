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

SCRIPT_LABEL = 'Candidate Route Burden Comparison Audit'
MARKER_ID = 'g44_route_burden'
DEPENDENCIES = [
    ('g43_summary', '043_trace_normalization_branch_or_parallel_decision_surface__candidate_group_43_status_summary', 'g43_summary'),
    ('g43_obligation_matrix', '043_trace_normalization_branch_or_parallel_decision_surface__candidate_branch_decision_obligation_matrix', 'g43_obligation_matrix'),
    ('g44_consequence_context', '044_trace_normalization_selector_context_audit__candidate_branch_consequence_context_matrix', 'g44_consequence_context'),
]
SCOPE = 'Group 44 trace-normalization selector-context audit'
QUESTION = 'How do the burdens of metric choice, scale choice, parallel records, and continued deferral compare without becoming selectors?'
DISCIPLINE = 'This script compares route burdens. A smaller or cleaner burden is not a branch selector unless a later explicit convention says so.'
OPENING_STATUS = 'selector-context audit only; no branch choice, declaration completion, adoption, insertion, active O, recombination, or parent route'
CASE_1_TITLE = 'Case 1: Route burden comparison entries'
NEXT_SCRIPT = 'candidate_theory_owner_choice_boundary.py'
CONCLUSIONS = [('route burden comparison complete', 'PASS', 'metric, scale, parallel, and deferral burdens compared'),
        ('burdens do not select route', 'DEFER', 'route burden remains context only')]

def build_entries() -> List[Entry]:
    return [
        Entry('B1: metric burden', 'metric choice needs object/scope, zeta convention, dimension, selector record, and downstream caveats', 'ROUTE_BURDEN_CONTEXT', 'burden is explicit and comparable', 'not closed here'),
        Entry('B2: scale burden', 'scale choice needs object/scope, zeta convention, dimension, selector record, and downstream caveats', 'ROUTE_BURDEN_CONTEXT', 'burden is explicit and comparable', 'not closed here'),
        Entry('B3: parallel burden', 'parallel route needs explicit labels, separated expressions, and no neutral-law collapse', 'ROUTE_BURDEN_CONTEXT', 'parallel burdens preserve both forms while avoiding branch choice', 'not active declaration'),
        Entry('B4: deferral burden', 'continued deferral needs a reason and a next narrowing route', 'CONTINUED_DEFERRAL', 'deferral should name what information is still missing', 'not loop permission'),
        Entry('B5: smaller burden warning', 'smaller burden is context only', 'POLICY_RULE', 'route burden comparison may show practical cost', 'not an admissible selector by itself'),
        Entry('B6: burden-to-handoff use', 'burden map may recommend a later route class', 'CONTEXT_ONLY', 'handoff recommendation can guide next group', 'recommendation is not execution'),
    ]

def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: fewer obligations chooses branch', 'choose the route with the shortest obligation list', 'burden count is not selector'),
        Shortcut('X2: burden visibility as closure', 'treat listed obligations as satisfied', 'visibility is not proof or closure'),
        Shortcut('X3: deferral without target', 'continue deferral without naming the next narrowing work', 'that risks looping'),
        Shortcut('X4: burden comparison as declaration', 'use burden matrix to complete trace normalization', 'matrix is not declaration'),
    ]

def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: keep burden non-selective', 'do not choose by smaller burden alone', 'POLICY_RULE', 'burden context must remain context', 'avoid convenience selector'),
        ObligationEntry('O2: name missing information', 'state what missing information blocks each route', 'OPEN', 'burden map should guide non-looping handoff', 'avoid endless audit loop'),
        ObligationEntry('O3: preserve declaration boundary', 'trace-normalization declaration remains later explicit record', 'NOT_DECLARED', 'burden comparison cannot install equations', 'avoid declaration drift'),
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
