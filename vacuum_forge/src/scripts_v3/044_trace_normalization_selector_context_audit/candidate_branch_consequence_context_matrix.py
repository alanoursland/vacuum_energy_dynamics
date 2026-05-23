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

SCRIPT_LABEL = 'Candidate Branch Consequence Context Matrix'
MARKER_ID = 'g44_consequence_context'
DEPENDENCIES = [
    ('g43_summary', '043_trace_normalization_branch_or_parallel_decision_surface__candidate_group_43_status_summary', 'g43_summary'),
    ('g43_metric_branch', '043_trace_normalization_branch_or_parallel_decision_surface__candidate_metric_branch_choice_readiness_ledger', 'g43_metric_branch'),
    ('g43_scale_branch', '043_trace_normalization_branch_or_parallel_decision_surface__candidate_scale_branch_choice_readiness_ledger', 'g43_scale_branch'),
    ('g43_parallel_records', '043_trace_normalization_branch_or_parallel_decision_surface__candidate_parallel_declaration_candidate_ledger', 'g43_parallel_records'),
    ('g44_source_hierarchy', '044_trace_normalization_selector_context_audit__candidate_source_hierarchy_evidence_ledger', 'g44_source_hierarchy'),
]
SCOPE = 'Group 44 trace-normalization selector-context audit'
QUESTION = 'What consequences of metric choice, scale choice, parallel records, and continued deferral are admissible context?'
DISCIPLINE = 'This script compares consequence profiles as context only. It does not choose the route with easier downstream behavior.'
OPENING_STATUS = 'selector-context audit only; no branch choice, declaration completion, adoption, insertion, active O, recombination, or parent route'
CASE_1_TITLE = 'Case 1: Branch consequence context entries'
NEXT_SCRIPT = 'candidate_route_burden_comparison_audit.py'
CONCLUSIONS = [('branch consequence matrix complete', 'PASS', 'route consequence profiles compared as context'),
        ('no route chosen by consequences', 'DEFER', 'consequence context remains non-active')]

def build_entries() -> List[Entry]:
    return [
        Entry('C1: metric consequence profile', 'metric branch keeps log(B_s_metric)=2*zeta/d visible', 'CONSEQUENCE_CONTEXT', 'factor-of-two burden is explicit under metric-coefficient branch', 'not selected and not declared'),
        Entry('C2: scale consequence profile', 'scale branch keeps log(b_s_scale)=zeta/d visible', 'CONSEQUENCE_CONTEXT', 'scale-factor interpretation may align with volume/root intuition as context', 'intuition is not derivation'),
        Entry('C3: parallel consequence profile', 'parallel records preserve both candidate forms', 'PARALLEL_RECORD_CANDIDATE', 'parallel route reduces hidden-branch risk by carrying both branches', 'not one neutral law and not final theory'),
        Entry('C4: deferral consequence profile', 'continued deferral avoids premature convention choice', 'CONTINUED_DEFERRAL', 'deferral can allow residual/source/boundary theorem work to narrow the later choice', 'not no-go result'),
        Entry('C5: insertion distance', 'all routes remain distant from B_s/F_zeta insertion', 'NOT_READY', 'residual/source/boundary/divergence gates still control insertion readiness', 'downstream distance cannot choose route'),
        Entry('C6: hidden-branch risk', 'risk of hidden branch choice is lowest when labels remain explicit', 'POLICY_RULE', 'context should reward visibility and penalize hidden notation', 'visibility is not declaration'),
    ]

def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: easiest insertion wins', 'choose the route that seems easiest to insert later', 'downstream convenience is forbidden selector'),
        Shortcut('X2: cleanest algebra wins', 'choose branch by prettiest factor or slogan', 'aesthetic simplicity is not derivation'),
        Shortcut('X3: parallel records as solution', 'treat parallel visibility as completing trace normalization', 'parallel records are candidates only'),
        Shortcut('X4: deferral as failure', 'treat continued deferral as proof no branch is viable', 'deferral preserves options'),
    ]

def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: keep consequences contextual', 'record consequence profiles without selecting route', 'POLICY_RULE', 'consequence comparison informs later decision only', 'avoid convenience selection'),
        ObligationEntry('O2: preserve insertion boundary', 'keep insertion, residual control, and parent closure separate', 'NOT_READY', 'no consequence profile opens downstream gates', 'avoid field-equation overreach'),
        ObligationEntry('O3: state hidden-branch risk', 'name hidden-branch and factor-of-two risks in later handoffs', 'OPEN', 'later choice must preserve visibility', 'avoid smuggled convention'),
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
