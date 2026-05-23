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

SCRIPT_LABEL = 'Candidate Parent Blocker Route Classifier'
MARKER_ID = 'g67_class'
DEPENDENCIES = [('g66_summary', '066_parent_blocker_inventory__candidate_group_66_status_summary', 'g66_summary'), ('g67_problem', '067_source_trace_divergence_blocker_audit__candidate_blocker_problem', 'g67_problem'), ('g67_incidence', '067_source_trace_divergence_blocker_audit__candidate_source_trace_incidence_audit', 'g67_incidence'), ('g67_count', '067_source_trace_divergence_blocker_audit__candidate_count_once_compatibility_sieve', 'g67_count'), ('g67_residual', '067_source_trace_divergence_blocker_audit__candidate_residual_nonentry_sieve', 'g67_residual'), ('g67_div', '067_source_trace_divergence_blocker_audit__candidate_divergence_identity_obstruction', 'g67_div'), ('g67_cons', '067_source_trace_divergence_blocker_audit__candidate_conservation_dependency_sieve', 'g67_cons')]
QUESTION = 'What is the final status after the source/trace/divergence blocker audit?'
DISCIPLINE = 'This classifier reports Group 67 status without opening parent recombination.'
OPENING_LINE = 'Parent blocker route classifier opened'
SCOPE = 'Group 67 parent blocker route classifier'
NEXT_SCRIPT = 'candidate_group_67_status_summary.py'

ENTRIES = [('C1: incidence', 'source/trace count-once residuals explicit', 'INCIDENCE_AUDIT_DERIVED', 'incidence conditions derived', 'necessary'), ('C2: strict state', 'i_A=1,i_src_extra=0,i_B=1,i_res=0,i_trace_extra=0', 'STRICT_SAFE_STATE_IDENTIFIED', 'strict role-compatible count-once state identified', 'necessary'), ('C3: residual', 'residual nonentry clarified', 'RESIDUAL_NONENTRY_CLARIFIED', 'residual parent carrier routes rejected', 'necessary'), ('C4: divergence', 'count-once not sufficient', 'DIVERGENCE_IDENTITY_NOT_PROVEN', 'divergence identity remains unproven', 'open'), ('C5: dependencies', 'conservation prerequisites recorded', 'CONSERVATION_DEPENDENCIES_RECORDED', 'covariant lift, boundary neutrality, O decision remain', 'open'), ('C6: recombination', 'blocked', 'RECOMBINATION_BLOCKED', 'parent recombination remains unlicensed', 'blocked'), ('C7: next route', 'covariant divergence identity attempt', 'NEXT_ROUTE_PRIORITIZED', 'likely next hard blocker', 'handoff')]
SHORTCUTS = [('X1: parent construction', 'write parent equation now', 'divergence identity not proven'), ('X2: count-only recombination', 'recombine because strict incidence exists', 'count-once is necessary but not sufficient'), ('X3: residual carrier', 'let residual carry trace/source', 'residual nonentry rejects it'), ('X4: transition carrier', 'use diagnostic transition as divergence/source/trace term', 'diagnostic-only forbids it')]
OBLIGATIONS = [('O1: summary', 'POLICY_RULE', 'write summary preserving count-once progress and divergence obstruction', 'avoid overclaim'), ('O2: next group', 'DEFERRED_WITH_TARGET', 'move to covariant divergence identity attempt or boundary diagnostic ledger', 'make parent-readiness progress')]
LOCAL_CONCLUSIONS = [('source/trace blocker clarified', 'PASS', 'count-once incidence and strict state identified'), ('divergence remains open', 'DIVERGENCE_IDENTITY_NOT_PROVEN', 'count-once is necessary but not sufficient'), ('parent remains blocked', 'PARENT_EQUATION_BLOCKED', 'no parent field equation opened')]


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
    for dep_id, upstream_script_id, upstream_derivation_id in dependencies:
        ns.declare_dependency(
            dependency_id=dep_id,
            upstream_script_id=upstream_script_id,
            upstream_derivation_id=upstream_derivation_id,
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
        "BLOCKER_AUDIT_OPENED": StatusMark.INFO,
        "INCIDENCE_AUDIT_DERIVED": StatusMark.PASS,
        "SOURCE_COUNT_ONCE_CLARIFIED": StatusMark.PASS,
        "TRACE_COUNT_ONCE_CLARIFIED": StatusMark.PASS,
        "STRICT_SAFE_STATE_IDENTIFIED": StatusMark.PASS,
        "SOURCE_REPAIR_REJECTED": StatusMark.FAIL,
        "TRACE_REPAIR_REJECTED": StatusMark.FAIL,
        "RESIDUAL_NONENTRY_CLARIFIED": StatusMark.PASS,
        "RESIDUAL_REENTRY_REJECTED": StatusMark.FAIL,
        "TRANSITION_REMAINS_DIAGNOSTIC": StatusMark.PASS,
        "DIVERGENCE_BALANCE_DERIVED": StatusMark.PASS,
        "DIVERGENCE_IDENTITY_NOT_PROVEN": StatusMark.OBLIGATION,
        "COUNT_ONCE_NOT_SUFFICIENT": StatusMark.OBLIGATION,
        "FORCED_REPAIR_REJECTED": StatusMark.FAIL,
        "CONSERVATION_DEPENDENCIES_RECORDED": StatusMark.PASS,
        "COVARIANT_LIFT_REQUIRED": StatusMark.OBLIGATION,
        "BOUNDARY_NEUTRALITY_REQUIRED": StatusMark.OBLIGATION,
        "ACTIVE_O_DECISION_REQUIRED": StatusMark.OBLIGATION,
        "SOURCE_SAFETY_REQUIRED": StatusMark.OBLIGATION,
        "TRACE_SAFETY_REQUIRED": StatusMark.OBLIGATION,
        "DIVERGENCE_IDENTITY_REQUIRED": StatusMark.OBLIGATION,
        "RECOMBINATION_BLOCKED": StatusMark.DEFER,
        "PARENT_EQUATION_BLOCKED": StatusMark.DEFER,
        "NEXT_ROUTE_PRIORITIZED": StatusMark.INFO,
        "PHYSICAL_USE_BLOCKED": StatusMark.DEFER,
        "NOT_INSERTABLE": StatusMark.DEFER,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REJECTED_ROUTE": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {
        "SOURCE_REPAIR_REJECTED",
        "TRACE_REPAIR_REJECTED",
        "RESIDUAL_REENTRY_REJECTED",
        "FORCED_REPAIR_REJECTED",
        "REJECTED_ROUTE",
        "FORBIDDEN_SHORTCUT",
    }:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {
        "DIVERGENCE_IDENTITY_NOT_PROVEN",
        "COUNT_ONCE_NOT_SUFFICIENT",
        "COVARIANT_LIFT_REQUIRED",
        "BOUNDARY_NEUTRALITY_REQUIRED",
        "ACTIVE_O_DECISION_REQUIRED",
        "SOURCE_SAFETY_REQUIRED",
        "TRACE_SAFETY_REQUIRED",
        "DIVERGENCE_IDENTITY_REQUIRED",
        "POLICY_RULE",
    }:
        return GovernanceStatus.POLICY_RULE
    return GovernanceStatus.UNVERIFIED


def obligation_status(status: str) -> ObligationStatus:
    if status in {
        "PHYSICAL_USE_BLOCKED",
        "NOT_INSERTABLE",
        "DEFERRED_WITH_TARGET",
        "RECOMBINATION_BLOCKED",
        "PARENT_EQUATION_BLOCKED",
    }:
        return ObligationStatus.DEFERRED
    return ObligationStatus.OPEN


def record_marker(ns, marker_id: str, scope: str) -> None:
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[],
        output=sp.Symbol(marker_id),
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


def record_governance(ns, marker_id: str, entries: List[Entry], obligations: List[ObligationEntry], scope: str) -> None:
    record_marker(ns, marker_id, scope)
    for idx, item in enumerate(entries, 1):
        record_claim(ns, f"{marker_id}_c{idx}", marker_id, item.status, f"{item.name}: {item.subject}. {item.detail}. Boundary: {item.boundary}.")
    for idx, item in enumerate(obligations, 1):
        record_obligation(ns, f"{marker_id}_o{idx}", item.name, f"{item.obligation}. Discipline: {item.discipline}.", item.status)


def print_entries(out: ScriptOutput, entries: List[Entry], title: str) -> None:
    header(title)
    for item in entries:
        subheader(item.name)
        print(f"Subject: {item.subject}")
        print(f"Detail: {item.detail}")
        print(f"Boundary: {item.boundary}")
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.detail}. Boundary: {item.boundary}")


def print_shortcuts(out: ScriptOutput, shortcuts: List[Shortcut]) -> None:
    header("Rejected shortcuts and invalid upgrades")
    for item in shortcuts:
        subheader(item.name)
        print(f"Shortcut: {item.shortcut}")
        with out.counterexamples():
            out.line(item.name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {item.reason}")


def print_obligations(out: ScriptOutput, obligations: List[ObligationEntry]) -> None:
    header("Open obligations and deferred burdens")
    for item in obligations:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        with out.unresolved_obligations():
            out.line(item.name, mark(item.status), f"{item.status}: {item.obligation}; discipline: {item.discipline}")


def build_entries() -> List[Entry]:
    return [Entry(*item) for item in ENTRIES]


def build_shortcuts() -> List[Shortcut]:
    return [Shortcut(*item) for item in SHORTCUTS]


def build_obligations() -> List[ObligationEntry]:
    return [ObligationEntry(*item) for item in OBLIGATIONS]





def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    entries = build_entries()
    shortcuts = build_shortcuts()
    obligations = build_obligations()

    header(SCRIPT_LABEL)
    print("Question:\n")
    print(QUESTION)
    print("\nDiscipline:\n")
    print(DISCIPLINE)
    with out.governance_assessments():
        out.line(f"{SCRIPT_LABEL} opened", StatusMark.PASS, OPENING_LINE)


    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
