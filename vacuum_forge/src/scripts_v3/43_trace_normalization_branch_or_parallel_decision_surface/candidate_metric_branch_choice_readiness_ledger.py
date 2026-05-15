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

SCRIPT_LABEL = 'Candidate Metric Branch Choice Readiness Ledger'
MARKER_ID = 'g43_metric_branch'
GROUP_SCOPE = 'Group 43 trace-normalization branch or parallel decision surface'
DEPENDENCIES = [('g42_summary', '42_trace_anchor_equation_choice_exclusion_map__candidate_group_42_status_summary', 'g42_summary'), ('g42_trace_norm_sieve', '42_trace_anchor_equation_choice_exclusion_map__candidate_trace_normalization_equation_family_sieve', 'g42_trace_norm_sieve'), ('g43_problem', '43_trace_normalization_branch_or_parallel_decision_surface__candidate_branch_or_parallel_decision_problem', 'g43_problem')]
QUESTION = 'What would be required before B_s_metric could be chosen explicitly as the trace-normalization branch?'
DISCIPLINE = 'This script audits the metric-coefficient branch as a future explicit-choice candidate only. It does not choose B_s_metric, complete trace normalization, adopt Package B, or license insertion.'
OPENING_DETAIL = 'metric branch readiness ledger only; B_s_metric remains non-active'
CASE1_TITLE = 'Case 1: Metric branch readiness entries'
NEXT_SCRIPT = 'candidate_scale_branch_choice_readiness_ledger.py'
CONCLUSIONS = [('metric branch ledger complete', 'PASS', 'B_s_metric support and obligations inventoried'), ('B_s_metric not chosen', 'DECLARATION_DEFERRED', 'metric branch remains future explicit-choice candidate only')]


def build_entries() -> List[Entry]:
    return [
        Entry('M1: metric candidate form', 'log(B_s_metric)=2*zeta/d may be carried as metric branch candidate form', 'BRANCH_CHOICE_CANDIDATE', 'candidate form remains visible for a later explicit choice record', 'not active declaration'),
        Entry('M2: metric-object clarity', 'metric choice would require a clear metric-coefficient object and scope', 'OPEN', 'B_s_metric must be typed before choice can support declaration', 'object clarity is not choice'),
        Entry('M3: zeta convention and dimension', 'metric choice requires explicit zeta convention, traced dimension d, and normalization scope', 'OPEN', 'factor-of-two burden must be named, not hidden', 'not supplied here'),
        Entry('M4: recovery selector rejected', 'B_s_metric cannot be chosen because it recovers AB=1, gamma, or Schwarzschild more easily', 'RECOVERY_SELECTOR_REJECTED', 'recovery is audit only', 'not an admissible selector'),
        Entry('M5: consequence audit context', 'metric branch consequences may be audited as decision context', 'ADMISSIBLE_CONTEXT', 'consequences can expose obligations and risks', 'not derivation or selection'),
        Entry('M6: downstream insufficiency', 'metric branch choice alone would not open insertion or parent routes', 'NOT_READY', 'residual/source/boundary/divergence gates remain separate', 'branch choice is insufficient'),
    ]


def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: metric by inherited symbol', 'choose B_s_metric because the old overloaded symbol was B_s', 'inherited symbol shape is not a branch selector'),
        Shortcut('X2: metric by recovery', 'choose B_s_metric because it fits AB=1, B=1/A, gamma, or Schwarzschild', 'recovery cannot select branch'),
        Shortcut('X3: metric as declaration', 'treat log(B_s_metric)=2*zeta/d as completed declaration', 'candidate form is not declaration'),
        Shortcut('X4: metric as insertion', 'insert B_s_metric/F_zeta after choosing the metric branch', 'insertion requires separate licensed law'),
    ]


def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: define metric branch object', 'OPEN', 'state B_s_metric domain, scope, and metric-coefficient meaning before any explicit choice', 'avoid overloaded B_s return'),
        ObligationEntry('O2: state zeta and dimension conventions', 'OPEN', 'state zeta convention and traced dimension d before metric declaration', 'avoid hidden normalization'),
        ObligationEntry('O3: keep recovery selector rejected', 'POLICY_RULE', 'do not choose metric branch from recovery targets', 'construction must precede recovery audit'),
        ObligationEntry('O4: keep metric choice non-insertable', 'NOT_READY', 'do not treat metric branch choice as B_s/F_zeta insertion', 'insertion remains downstream'),
    ]


if __name__ == "__main__":
    main()
