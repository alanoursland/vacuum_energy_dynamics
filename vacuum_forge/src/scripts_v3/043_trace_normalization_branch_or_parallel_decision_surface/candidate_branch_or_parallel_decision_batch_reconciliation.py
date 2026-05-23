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

SCRIPT_LABEL = 'Candidate Branch or Parallel Decision Batch Reconciliation'
MARKER_ID = 'g43_recon'
GROUP_SCOPE = 'Group 43 trace-normalization branch or parallel decision surface'
DEPENDENCIES = [('g42_summary', '42_trace_anchor_equation_choice_exclusion_map__candidate_group_42_status_summary', 'g42_summary'), ('g43_problem', '43_trace_normalization_branch_or_parallel_decision_surface__candidate_branch_or_parallel_decision_problem', 'g43_problem'), ('g43_metric_branch', '43_trace_normalization_branch_or_parallel_decision_surface__candidate_metric_branch_choice_readiness_ledger', 'g43_metric_branch'), ('g43_scale_branch', '43_trace_normalization_branch_or_parallel_decision_surface__candidate_scale_branch_choice_readiness_ledger', 'g43_scale_branch'), ('g43_parallel_records', '43_trace_normalization_branch_or_parallel_decision_surface__candidate_parallel_declaration_candidate_ledger', 'g43_parallel_records'), ('g43_selector_sieve', '43_trace_normalization_branch_or_parallel_decision_surface__candidate_selector_admissibility_and_rejection_sieve', 'g43_selector_sieve'), ('g43_obligation_matrix', '43_trace_normalization_branch_or_parallel_decision_surface__candidate_branch_decision_obligation_matrix', 'g43_obligation_matrix')]
QUESTION = 'Did the Group 43 batch produce the expected branch-or-parallel decision-surface shape, and what should a later status summary preserve?'
DISCIPLINE = 'This script reconciles the Group 43 batch. It does not close the group as final summary and does not choose a branch, complete declarations, adopt Package B, insert B_s/F_zeta, or open parent closure.'
OPENING_DETAIL = 'batch reconciliation only; no final summary and no branch choice'
CASE1_TITLE = 'Case 1: Batch reconciliation entries'
NEXT_SCRIPT = 'candidate_group_43_status_summary.py'
CONCLUSIONS = [('batch reconciliation prepared', 'PASS', 'write summary only after actual outputs are reviewed'), ('no group close here', 'DECLARATION_DEFERRED', 'candidate_group_43_status_summary.py should be written after review')]


def build_entries() -> List[Entry]:
    return [
        Entry('Q1: opener expectation', 'Group 43 opened as a branch-or-parallel decision-surface audit', 'MATCHED_EXPECTATION', 'expected if routes are classified without branch choice', 'summary may call this decision-surface audit only'),
        Entry('Q2: metric branch expectation', 'metric branch readiness was inventoried without choosing B_s_metric', 'MATCHED_EXPECTATION', 'expected if metric candidate remains future explicit-choice route', 'summary must preserve not chosen'),
        Entry('Q3: scale branch expectation', 'scale branch readiness was inventoried without choosing b_s_scale', 'MATCHED_EXPECTATION', 'expected if scale candidate remains future explicit-choice route', 'summary must preserve not chosen'),
        Entry('Q4: parallel record expectation', 'explicit parallel branch-indexed record route was classified', 'MATCHED_EXPECTATION', 'expected if parallel records remain non-active and not one neutral law', 'summary must preserve parallel/not-declared boundary'),
        Entry('Q5: selector expectation', 'forbidden selectors were rejected and admissible context separated', 'MATCHED_EXPECTATION', 'expected if recovery/downstream/neutral-expression selectors remain forbidden', 'summary must not turn context into choice'),
        Entry('Q6: obligation expectation', 'route-specific obligations were mapped but not closed', 'MATCHED_EXPECTATION', 'expected if visibility remains distinct from closure', 'summary must preserve obligations open'),
        Entry('Q7: downstream gates', 'Package B adoption, insertion, active O, residual control, recombination, and parent closure remain closed', 'NOT_READY', 'expected final boundary', 'summary must not open field-equation routes'),
    ]


def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: reconciliation as final summary', 'treat this script as group close', 'final summary should be written after actual outputs are reviewed'),
        Shortcut('X2: readiness as branch choice', 'treat metric or scale readiness as selected branch', 'readiness is not choice'),
        Shortcut('X3: parallel as declaration', 'treat parallel records as completed trace normalization', 'parallel candidates are not declarations'),
        Shortcut('X4: selector context as derivation', 'treat admissible context as proof of branch', 'context is not derivation'),
        Shortcut('X5: obligations as solved', 'treat listed route obligations as closed', 'obligation visibility is not closure'),
        Shortcut('X6: decision surface as insertion', 'open B_s/F_zeta insertion or parent route', 'downstream gates remain closed'),
    ]


def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: summary must follow actual outputs', 'OPEN', 'final summary must report any mismatch in batch outputs', 'actual outputs control close'),
        ObligationEntry('O2: preserve no branch chosen', 'DECLARATION_DEFERRED', 'final summary must say no metric or scale branch was chosen unless actual output chose it', 'avoid choice by summary prose'),
        ObligationEntry('O3: preserve parallel/declaration boundary', 'NOT_DECLARED', 'parallel records remain candidates and not completed declaration', 'avoid declaration drift'),
        ObligationEntry('O4: preserve selector discipline', 'POLICY_RULE', 'recovery, downstream convenience, and neutral-expression selectors remain forbidden', 'avoid smuggled selector'),
        ObligationEntry('O5: preserve downstream locks', 'NOT_READY', 'adoption, insertion, active O, residual control, recombination, and parent closure remain closed', 'avoid field-equation overreach'),
    ]


if __name__ == "__main__":
    main()
