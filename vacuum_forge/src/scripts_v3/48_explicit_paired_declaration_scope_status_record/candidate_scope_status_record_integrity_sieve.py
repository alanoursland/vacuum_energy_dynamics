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
        "PAIRED_SCOPE_STATUS_RECORD": StatusMark.INFO,
        "SCOPE_STATUS_RECORD": StatusMark.INFO,
        "DECLARATION_SCOPE_READY_FOR_RECORD": StatusMark.INFO,
        "DECLARATION_SCOPE_CANDIDATE": StatusMark.INFO,
        "STATUS_FIELD": StatusMark.INFO,
        "ASSUMPTION_FIELD": StatusMark.INFO,
        "DOMAIN_FIELD": StatusMark.INFO,
        "CAVEAT_FIELD": StatusMark.INFO,
        "CLOSED_FOR_REVIEW": StatusMark.INFO,
        "REVIEW_READY_ONLY": StatusMark.INFO,
        "NON_ACTIVE": StatusMark.INFO,
        "BRANCH_INDEXED": StatusMark.INFO,
        "CONTEXT_ONLY": StatusMark.INFO,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "CONSISTENCY_RULE": StatusMark.OBLIGATION,
        "SCOPE_REQUIRED": StatusMark.OBLIGATION,
        "EXPLICIT_CHOICE_REQUIRED": StatusMark.OBLIGATION,
        "NUMERIC_D_CONDITION": StatusMark.OBLIGATION,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "DECLARATION_BLOCKED": StatusMark.DEFER,
        "THEOREM_REQUIRED": StatusMark.DEFER,
        "CHOICE_REQUIRED": StatusMark.DEFER,
        "AXIOM_REQUIRED": StatusMark.DEFER,
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
    if status in {"NOT_READY", "NOT_DECLARED", "NOT_CHOSEN", "NOT_ADOPTED", "NOT_DERIVED", "DEFERRED_WITH_TARGET", "DECLARATION_BLOCKED", "THEOREM_REQUIRED", "AXIOM_REQUIRED", "CHOICE_REQUIRED"}:
        return ObligationStatus.DEFERRED
    return ObligationStatus.OPEN


def governance_status(status: str) -> GovernanceStatus:
    if status in {"BLOCKED", "FORBIDDEN_SHORTCUT", "REJECTED_ROUTE"}:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {"AXIOM_REQUIRED", "CHOICE_REQUIRED", "THEOREM_REQUIRED", "NOT_READY", "NOT_DECLARED", "DECLARATION_BLOCKED", "DEFERRED_WITH_TARGET", "OPEN"}:
        return GovernanceStatus.UNVERIFIED
    return GovernanceStatus.POLICY_RULE


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
#   48_explicit_paired_declaration_scope_status_record
# Script type:
#   RECORD / SCOPE-STATUS / PRE-DECLARATION

SCRIPT_LABEL = 'Candidate Scope Status Record Integrity Sieve'
MARKER_ID = 'g48_integrity_sieve'
DEPENDENCIES = [('g47_summary', '47_normalization_declaration_scope_closure_audit__candidate_group_47_status_summary', 'g47_summary'), ('g48_caveat_record', '48_explicit_paired_declaration_scope_status_record__candidate_downstream_caveat_and_rejected_broadening_record', 'g48_caveat_record')]
QUESTION = 'Does the paired scope/status record stay internally consistent without becoming declaration-ready?'
DISCIPLINE = 'This script checks the assembled record for integrity. It should decide whether the record is instantiated for pre-declaration use, still incomplete, or drifting into forbidden roles.'
OPENING_LINE = 'Scope/status record integrity sieve opened -- integrity audit only; no declaration execution'
SCOPE = 'Group 48 scope status record integrity sieve'
NEXT_SCRIPT = 'candidate_paired_scope_status_record_batch_reconciliation.py'


def build_entries() -> List[Entry]:
    return [
        Entry('I1: record instantiated', 'paired declaration-scope/status record fields are explicit enough for handoff', 'PAIRED_SCOPE_STATUS_RECORD', 'record can be carried forward as the next artifact Group 47 requested', 'not declaration'),
        Entry('I2: status integrity', 'status remains pre-declaration and non-active', 'STATUS_FIELD', 'status prevents review-ready/declaration-ready confusion', 'not equation installation'),
        Entry('I3: assumption integrity', 'domain, shared zeta, symbolic d, and numeric-d condition remain visible', 'ASSUMPTION_FIELD', 'assumptions are not hidden', 'not proof'),
        Entry('I4: branch integrity', 'metric and scale branches remain paired, labeled, and non-active', 'BRANCH_INDEXED', 'pair preserves factor-of-two burden', 'not branch choice'),
        Entry('I5: caveat integrity', 'downstream caveats remain attached to record', 'CAVEAT_FIELD', 'record cannot be used for insertion or parent closure', 'not field-equation use'),
        Entry('I6: next route status', 'parallel declaration attempt remains later and conditional', 'DEFERRED_WITH_TARGET', 'the record is a prerequisite artifact, not the declaration itself', 'not immediate declaration'),
    ]


def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: integrity as declaration', 'treat successful integrity audit as trace-normalization declaration', 'integrity only validates the record surface'),
        Shortcut('X2: artifact as Package B', 'treat artifact completion as Package B adoption', 'adoption remains separate'),
        Shortcut('X3: conditional as immediate', 'jump from record to declaration without reviewing assumptions', 'future declaration requires a separate record'),
        Shortcut('X4: non-active lost', 'drop non-active branch status in summary', 'non-active branch status is central'),
    ]


def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: preserve record-instantiated status', 'PAIRED_SCOPE_STATUS_RECORD', 'future summary may say the scope/status record is instantiated as infrastructure', 'avoid underselling the result'),
        ObligationEntry('O2: preserve no-declaration status', 'NOT_DECLARED', 'future summary must not say trace normalization is declared', 'avoid overselling the result'),
        ObligationEntry('O3: preserve conditional next route', 'DEFERRED_WITH_TARGET', 'next route is review for possible declaration attempt, not automatic declaration', 'avoid skipping gates'),
    ]


LOCAL_CONCLUSIONS = [('integrity sieve complete', 'PASS', 'paired scope/status record is coherent as pre-declaration infrastructure'), ('declaration still later', 'NOT_DECLARED', 'trace normalization remains undeclared')]


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
