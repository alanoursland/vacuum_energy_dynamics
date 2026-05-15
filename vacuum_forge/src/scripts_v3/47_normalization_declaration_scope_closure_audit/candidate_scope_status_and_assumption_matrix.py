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
        "DECLARATION_SCOPE_AUDIT": StatusMark.INFO,
        "SCOPE_BOUNDARY": StatusMark.INFO,
        "SCOPE_CANDIDATE": StatusMark.INFO,
        "CLOSED_FOR_REVIEW": StatusMark.INFO,
        "REVIEW_READY_ONLY": StatusMark.INFO,
        "ASSUMPTION_FIELD": StatusMark.INFO,
        "STATUS_FIELD": StatusMark.INFO,
        "BRANCH_INDEXED": StatusMark.INFO,
        "CONTEXT_ONLY": StatusMark.INFO,
        "NON_ACTIVE": StatusMark.INFO,
        "DECLARATION_SCOPE_CANDIDATE": StatusMark.INFO,
        "DECLARATION_SCOPE_READY_FOR_RECORD": StatusMark.INFO,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "CONSISTENCY_RULE": StatusMark.OBLIGATION,
        "EXPLICIT_CHOICE_REQUIRED": StatusMark.OBLIGATION,
        "SCOPE_REQUIRED": StatusMark.OBLIGATION,
        "CONVENTION_BLOCKED": StatusMark.DEFER,
        "DECLARATION_BLOCKED": StatusMark.DEFER,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "THEOREM_REQUIRED": StatusMark.DEFER,
        "AXIOM_REQUIRED": StatusMark.DEFER,
        "CHOICE_REQUIRED": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "NOT_DECLARED": StatusMark.DEFER,
        "NOT_CHOSEN": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "REJECTED_ROUTE": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "BLOCKED": StatusMark.FAIL,
    }.get(status, StatusMark.INFO)


def obligation_status(status: str) -> ObligationStatus:
    if status in {"NOT_READY", "NOT_DECLARED", "NOT_CHOSEN", "NOT_ADOPTED", "NOT_DERIVED", "DEFERRED_WITH_TARGET", "CONVENTION_BLOCKED", "DECLARATION_BLOCKED", "THEOREM_REQUIRED", "AXIOM_REQUIRED", "CHOICE_REQUIRED"}:
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


def governance_status(status: str) -> GovernanceStatus:
    if status in {"BLOCKED", "FORBIDDEN_SHORTCUT", "REJECTED_ROUTE"}:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {"AXIOM_REQUIRED", "CHOICE_REQUIRED", "THEOREM_REQUIRED", "NOT_READY", "NOT_DECLARED", "CONVENTION_BLOCKED", "DECLARATION_BLOCKED", "DEFERRED_WITH_TARGET", "OPEN"}:
        return GovernanceStatus.UNVERIFIED
    return GovernanceStatus.POLICY_RULE


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
    header("Invalid upgrades and forbidden shortcuts")
    for item in shortcuts:
        subheader(item.name)
        print(f"Shortcut: {item.shortcut}")
        with out.counterexamples():
            out.line(item.name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {item.reason}")


def print_obligations(out: ScriptOutput, obligations: List[ObligationEntry]) -> None:
    header("Open obligations")
    for item in obligations:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        with out.unresolved_obligations():
            out.line(item.name, mark(item.status), f"{item.status}: {item.obligation}; discipline: {item.discipline}")


def record_governance(ns, marker_id: str, entries: List[Entry], obligations: List[ObligationEntry], scope: str) -> None:
    record_marker(ns, marker_id, scope)
    for idx, item in enumerate(entries, 1):
        record_claim(ns, f"{marker_id}_c{idx}", marker_id, item.status, f"{item.name}: {item.subject}. {item.detail}. Boundary: {item.boundary}.")
    for idx, item in enumerate(obligations, 1):
        record_obligation(ns, f"{marker_id}_o{idx}", item.name, f"{item.obligation}. Discipline: {item.discipline}.", item.status)

# Group:
#   47_normalization_declaration_scope_closure_audit
# Script type:
#   AUDIT / DECLARATION-SCOPE / PRE-DECLARATION

SCRIPT_LABEL = 'Candidate Scope Status and Assumption Matrix'
MARKER_ID = 'g47_scope_status_matrix'
DEPENDENCIES = [('g46_summary', '46_parallel_trace_convention_field_closure_audit__candidate_group_46_status_summary', 'g46_summary'), ('g47_scope_candidate_sieve', '47_normalization_declaration_scope_closure_audit__candidate_declaration_scope_candidate_sieve', 'g47_scope_candidate_sieve')]
QUESTION = 'What explicit status and assumptions would a surviving paired declaration-scope record need before any declaration attempt?'
DISCIPLINE = 'This script maps the status and assumption fields needed by the surviving paired declaration-scope candidate. It does not close those assumptions as a declaration.'
OPENING_LINE = 'Scope status/assumption matrix opened -- requirements visible; no trace declaration'
SCOPE = 'Group 47 scope status and assumption matrix'
NEXT_SCRIPT = 'candidate_parent_facing_scope_rejection_audit.py'

def build_entries() -> List[Entry]:
    return [
        Entry('M1: scope status field', 'future record must state pre-declaration, declaration-scope candidate, or declared status', 'STATUS_FIELD', 'status must be explicit to prevent review-ready inflation', 'not declared here'),
        Entry('M2: paired-record domain', 'scope domain is the paired metric/scale record surface', 'ASSUMPTION_FIELD', 'domain is adequate for declaration-scope review', 'not physical insertion domain'),
        Entry('M3: zeta assumption', 'shared record-local zeta is inherited as review-closed', 'CLOSED_FOR_REVIEW', 'zeta can be referenced as trace-payload symbol', 'not active field'),
        Entry('M4: d assumption', 'symbolic d is inherited as review-closed; numeric d remains scope-dependent', 'SCOPE_REQUIRED', 'numeric d needs explicit declaration-scope decision', 'not fixed here'),
        Entry('M5: non-active branch status', 'both branch records remain non-active unless a later declaration changes status explicitly', 'NON_ACTIVE', 'status alignment prevents accidental branch choice', 'not active'),
        Entry('M6: downstream caveat field', 'record must state no insertion, no active O, no residual/source theorem, no parent closure', 'NOT_READY', 'declaration-scope clarity cannot erase downstream gates', 'not field-equation use'),
    ]

def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: unstated status', 'omit status and let readers infer declaration', 'status omission causes declaration drift'),
        Shortcut('X2: physical domain shortcut', 'treat paired record domain as field-equation domain', 'record domain is not insertion domain'),
        Shortcut('X3: numeric d by assumption leak', 'quietly set numeric d without scope decision', 'numeric d remains scope-dependent'),
        Shortcut('X4: downstream caveat omitted', 'leave out non-insertion and no-parent caveats', 'omission invites overreach'),
    ]

def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: require explicit status', 'OPEN', 'future declaration-scope record must carry status field', 'avoid review-ready/declaration-ready confusion'),
        ObligationEntry('O2: require assumption list', 'OPEN', 'future record must list zeta, symbolic d, numeric d condition, domain, and caveats', 'avoid hidden assumptions'),
        ObligationEntry('O3: preserve non-active status until declaration', 'OPEN', 'do not activate branch records by matrix', 'avoid branch/declaration drift'),
    ]

LOCAL_CONCLUSIONS = [('matrix complete', 'PASS', 'status and assumption requirements made explicit'), ('assumptions not closed as declaration', 'NOT_DECLARED', 'matrix prepares future record but does not install trace normalization')]

def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header(SCRIPT_LABEL)
    print("Question:\n")
    print(QUESTION)
    print("\nDiscipline:\n")
    print(DISCIPLINE)
    with out.governance_assessments():
        out.line(f"{SCRIPT_LABEL} opened", StatusMark.PASS, OPENING_LINE)

    entries = build_entries()
    shortcuts = build_shortcuts()
    obligations = build_obligations()
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
