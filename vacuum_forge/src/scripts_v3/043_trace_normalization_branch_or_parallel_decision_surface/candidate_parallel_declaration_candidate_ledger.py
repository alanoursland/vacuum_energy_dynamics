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
        "BRANCH_DECISION_SURFACE": StatusMark.INFO,
        "BRANCH_CHOICE_CANDIDATE": StatusMark.INFO,
        "PARALLEL_RECORD_CANDIDATE": StatusMark.INFO,
        "CONTINUED_DEFERRAL": StatusMark.DEFER,
        "DECLARATION_DEFERRED": StatusMark.DEFER,
        "EXPLICIT_CHOICE_REQUIRED": StatusMark.OBLIGATION,
        "ADMISSIBLE_CONTEXT": StatusMark.INFO,
        "SELECTOR_REJECTED": StatusMark.FAIL,
        "RECOVERY_SELECTOR_REJECTED": StatusMark.FAIL,
        "FORBIDDEN_BY_GUARDRAIL": StatusMark.FAIL,
        "CONDITIONAL": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "DEFER": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "NOT_DECLARED": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
    }.get(status, StatusMark.INFO)


def _governance(name: str, fallback=None):
    if fallback is None:
        fallback = GovernanceStatus.POLICY_RULE
    return getattr(GovernanceStatus, name, fallback)


def governance_status_for(status: str):
    info_status = _governance("HEURISTIC")
    deferred_status = _governance("DEFERRED_PENDING_PREREQUISITES", _governance("DEFERRED"))
    candidate_status = _governance("CANDIDATE_ROUTE", info_status)
    policy_status = GovernanceStatus.POLICY_RULE
    rejected_status = _governance("REJECTED", policy_status)
    return {
        "PASS": info_status,
        "MATCHED_EXPECTATION": info_status,
        "BRANCH_DECISION_SURFACE": info_status,
        "BRANCH_CHOICE_CANDIDATE": candidate_status,
        "PARALLEL_RECORD_CANDIDATE": candidate_status,
        "CONTINUED_DEFERRAL": deferred_status,
        "DECLARATION_DEFERRED": deferred_status,
        "EXPLICIT_CHOICE_REQUIRED": deferred_status,
        "ADMISSIBLE_CONTEXT": info_status,
        "SELECTOR_REJECTED": rejected_status,
        "RECOVERY_SELECTOR_REJECTED": rejected_status,
        "FORBIDDEN_BY_GUARDRAIL": rejected_status,
        "CONDITIONAL": candidate_status,
        "OPEN": deferred_status,
        "DEFER": deferred_status,
        "NOT_READY": deferred_status,
        "NOT_DECLARED": deferred_status,
        "NOT_ADOPTED": deferred_status,
        "NOT_DERIVED": deferred_status,
        "POLICY_RULE": policy_status,
        "FORBIDDEN_SHORTCUT": policy_status,
    }.get(status, info_status)


def obligation_status(status: str) -> ObligationStatus:
    if status in {
        "CONTINUED_DEFERRAL",
        "DECLARATION_DEFERRED",
        "EXPLICIT_CHOICE_REQUIRED",
        "CONDITIONAL",
        "OPEN",
        "DEFER",
        "NOT_READY",
        "NOT_DECLARED",
        "NOT_ADOPTED",
        "NOT_DERIVED",
    }:
        return getattr(ObligationStatus, "DEFERRED", ObligationStatus.OPEN)
    return ObligationStatus.OPEN


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


def record_marker(ns, marker_id: str, symbol_name: str) -> None:
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[],
        output=sp.Symbol(symbol_name),
        method="inventory marker; no physical derivation",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
        scope=GROUP_SCOPE,
    )


def record_claim(ns, claim_id: str, marker_id: str, status: str, statement: str) -> None:
    ns.record_claim(
        ClaimRecord(
            claim_id=claim_id,
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=governance_status_for(status),
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


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    for line in QUESTION.splitlines():
        print("  " + line if line else "")
    print("\nDiscipline:\n")
    for line in DISCIPLINE.splitlines():
        print("  " + line if line else "")
    with out.governance_assessments():
        out.line(f"{SCRIPT_LABEL} opened", StatusMark.PASS, OPENING_DETAIL)


def case_1(out: ScriptOutput, entries: List[Entry]) -> None:
    header(CASE1_TITLE)
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


def record_governance(ns, entries: List[Entry], shortcuts: List[Shortcut], obligations: List[ObligationEntry]) -> None:
    record_marker(ns, MARKER_ID, MARKER_ID)
    for idx, item in enumerate(entries, 1):
        record_claim(
            ns,
            f"{MARKER_ID}_entry_{idx}",
            MARKER_ID,
            item.status,
            f"{item.name}: {item.subject}. {item.detail}. Boundary: {item.boundary}.",
        )
    for idx, item in enumerate(shortcuts, 1):
        record_claim(
            ns,
            f"{MARKER_ID}_shortcut_{idx}",
            MARKER_ID,
            "POLICY_RULE",
            f"Rejected shortcut {item.name}: {item.shortcut}. Reason: {item.reason}.",
        )
    for idx, item in enumerate(obligations, 1):
        record_obligation(
            ns,
            f"{MARKER_ID}_obligation_{idx}",
            item.name,
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
    record_governance(ns, entries, shortcuts, obligations)
    ns.write_run_metadata()



# Group:
#   43_trace_normalization_branch_or_parallel_decision_surface
# Script type:
#   AUDIT / DECISION SURFACE

SCRIPT_LABEL = 'Candidate Parallel Declaration Candidate Ledger'
MARKER_ID = 'g43_parallel_records'
GROUP_SCOPE = 'Group 43 trace-normalization branch or parallel decision surface'
DEPENDENCIES = [('g42_summary', '042_trace_anchor_equation_choice_exclusion_map__candidate_group_42_status_summary', 'g42_summary'), ('g43_metric_branch', '043_trace_normalization_branch_or_parallel_decision_surface__candidate_metric_branch_choice_readiness_ledger', 'g43_metric_branch'), ('g43_scale_branch', '043_trace_normalization_branch_or_parallel_decision_surface__candidate_scale_branch_choice_readiness_ledger', 'g43_scale_branch')]
QUESTION = 'Can metric and scale trace-normalization forms be carried as two explicit parallel declaration candidates without choosing either?'
DISCIPLINE = 'This script audits explicitly parallel branch-indexed declaration candidates. It preserves both branch forms as non-active candidates and does not collapse them into a neutral law.'
OPENING_DETAIL = 'parallel record audit only; no active branch or declaration installed'
CASE1_TITLE = 'Case 1: Parallel declaration candidate entries'
NEXT_SCRIPT = 'candidate_selector_admissibility_and_rejection_sieve.py'
CONCLUSIONS = [('parallel record ledger complete', 'PASS', 'two explicit branch-indexed declaration candidates classified'), ('parallel records not active', 'DECLARATION_DEFERRED', 'parallel record option does not complete trace normalization')]


def build_entries() -> List[Entry]:
    return [
        Entry('P1: two explicit records', 'metric and scale candidate forms may be carried in two explicit records', 'PARALLEL_RECORD_CANDIDATE', 'parallel tracking preserves both branches without choosing', 'not one neutral law'),
        Entry('P2: metric record content', 'metric record may carry log(B_s_metric)=2*zeta/d as non-active candidate', 'BRANCH_CHOICE_CANDIDATE', 'candidate form remains branch-indexed', 'not selected'),
        Entry('P3: scale record content', 'scale record may carry log(b_s_scale)=zeta/d as non-active candidate', 'BRANCH_CHOICE_CANDIDATE', 'candidate form remains branch-indexed', 'not selected'),
        Entry('P4: factor-of-two visibility', 'parallel records keep the factor-of-two burden visible', 'POLICY_RULE', 'parallelization prevents neutral-expression smuggling', 'not declaration support by itself'),
        Entry('P5: declaration separation', 'parallel declaration candidates may prepare a later declaration route', 'CONDITIONAL', 'future declaration route remains possible if obligations close', 'not current declaration'),
        Entry('P6: no insertion support', 'parallel records cannot insert B_s/F_zeta', 'NOT_READY', 'candidate records are not recombination laws', 'insertion remains closed'),
    ]


def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: parallel as active declaration', 'treat two records as completing trace normalization', 'parallel candidates are not declarations'),
        Shortcut('X2: parallel as neutral expression', 'merge 2*zeta/d and zeta/d under neutral F_zeta or unqualified B_s', 'that hides branch burden'),
        Shortcut('X3: parallel as branch choice', 'say carrying both branches chooses both or chooses neither as final theory', 'parallel is a deferral/visibility route'),
        Shortcut('X4: parallel as insertion', 'use either parallel candidate in B_s/F_zeta insertion', 'insertion remains not ready'),
    ]


def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: keep records explicitly branch-indexed', 'POLICY_RULE', 'preserve B_s_metric and b_s_scale labels in all parallel records', 'avoid overloaded B_s return'),
        ObligationEntry('O2: keep factor-of-two burden visible', 'POLICY_RULE', 'do not hide zeta/d versus 2*zeta/d under neutral notation', 'avoid normalization smuggling'),
        ObligationEntry('O3: keep declaration deferred', 'DECLARATION_DEFERRED', 'treat parallel records as candidates until a later explicit declaration route', 'avoid premature declaration'),
        ObligationEntry('O4: keep insertion closed', 'NOT_READY', 'do not use parallel records as B_s/F_zeta insertion support', 'candidate records are not equations of recombination'),
    ]


if __name__ == "__main__":
    main()
