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

SCRIPT_LABEL = 'Candidate Branch Decision Obligation Matrix'
MARKER_ID = 'g43_obligation_matrix'
GROUP_SCOPE = 'Group 43 trace-normalization branch or parallel decision surface'
DEPENDENCIES = [('g42_summary', '42_trace_anchor_equation_choice_exclusion_map__candidate_group_42_status_summary', 'g42_summary'), ('g43_metric_branch', '43_trace_normalization_branch_or_parallel_decision_surface__candidate_metric_branch_choice_readiness_ledger', 'g43_metric_branch'), ('g43_scale_branch', '43_trace_normalization_branch_or_parallel_decision_surface__candidate_scale_branch_choice_readiness_ledger', 'g43_scale_branch'), ('g43_parallel_records', '43_trace_normalization_branch_or_parallel_decision_surface__candidate_parallel_declaration_candidate_ledger', 'g43_parallel_records'), ('g43_selector_sieve', '43_trace_normalization_branch_or_parallel_decision_surface__candidate_selector_admissibility_and_rejection_sieve', 'g43_selector_sieve')]
QUESTION = 'What obligations must be closed before metric choice, scale choice, parallel records, or continued deferral can progress?'
DISCIPLINE = 'This script maps obligations for each trace-normalization decision route. It does not close the obligations or choose the route.'
OPENING_DETAIL = 'obligation matrix only; route burdens visible but unsolved'
CASE1_TITLE = 'Case 1: Branch decision obligation matrix entries'
NEXT_SCRIPT = 'candidate_branch_or_parallel_decision_batch_reconciliation.py'
CONCLUSIONS = [('branch decision obligation matrix complete', 'PASS', 'route-specific burdens mapped'), ('route obligations remain open', 'DECLARATION_DEFERRED', 'no metric, scale, parallel, or deferral route is selected as final')]


def build_entries() -> List[Entry]:
    return [
        Entry('D1: metric choice obligations', 'metric branch choice needs object/scope, zeta convention, dimension, selector record, and downstream caveats', 'BRANCH_CHOICE_CANDIDATE', 'obligations visible for future explicit choice', 'not closed here'),
        Entry('D2: scale choice obligations', 'scale branch choice needs object/scope, zeta convention, dimension, selector record, and downstream caveats', 'BRANCH_CHOICE_CANDIDATE', 'obligations visible for future explicit choice', 'not closed here'),
        Entry('D3: parallel record obligations', 'parallel records need explicit labels, separated expressions, and no neutral-law collapse', 'PARALLEL_RECORD_CANDIDATE', 'parallel route remains available if choice is unsupported', 'not active declaration'),
        Entry('D4: continued deferral obligations', 'deferral remains valid if branch support is insufficient or theorem/axiom work should run first', 'CONTINUED_DEFERRAL', 'deferral can be a disciplined route', 'not no-go theorem'),
        Entry('D5: declaration obligations', 'trace-normalization declaration requires explicit branch or explicit parallel record assumptions plus conventions', 'NOT_DECLARED', 'declaration route remains later', 'not completed here'),
        Entry('D6: adoption and insertion obligations', 'Package B adoption and B_s/F_zeta insertion require separate downstream support', 'NOT_READY', 'branch-decision surface cannot open them', 'still closed'),
    ]


def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: obligations as closed', 'treat listed obligations as satisfied because they are named', 'visibility is not closure'),
        Shortcut('X2: obligation burden chooses branch', 'choose the branch with fewer listed obligations by convenience', 'burden comparison is not selector by itself'),
        Shortcut('X3: deferral as failure', 'treat continued deferral as branch rejection', 'deferral preserves options'),
        Shortcut('X4: declaration from matrix', 'complete trace-normalization declaration from obligation matrix', 'matrix is not declaration'),
        Shortcut('X5: adoption from matrix', 'adopt Package B because route burdens are visible', 'adoption remains separate'),
    ]


def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: close route obligations separately', 'OPEN', 'future route must close its own object, scope, convention, selector, and boundary obligations', 'avoid visibility-as-proof'),
        ObligationEntry('O2: keep burden comparison non-selective', 'POLICY_RULE', 'do not choose by downstream convenience or smaller burden alone', 'avoid convenience selector'),
        ObligationEntry('O3: preserve declaration boundary', 'NOT_DECLARED', 'declaration remains a later explicit record', 'avoid declaration by matrix'),
        ObligationEntry('O4: preserve downstream locks', 'NOT_READY', 'adoption, insertion, active O, residual control, recombination, and parent closure remain closed', 'avoid field-equation overreach'),
    ]


if __name__ == "__main__":
    main()
