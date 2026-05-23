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

SCRIPT_LABEL = 'Candidate Paired Scope Record Schema'
MARKER_ID = 'g48_schema'
DEPENDENCIES = [('g47_summary', '047_normalization_declaration_scope_closure_audit__candidate_group_47_status_summary', 'g47_summary'), ('g48_problem', '048_explicit_paired_declaration_scope_status_record__candidate_paired_scope_status_record_problem', 'g48_problem')]
QUESTION = 'What fields must the explicit paired declaration-scope/status record contain?'
DISCIPLINE = 'This script states the schema of the paired scope/status record. The schema makes the artifact explicit but does not install trace normalization.'
OPENING_LINE = 'Paired scope/status record schema opened -- schema only; no declaration or downstream route'
SCOPE = 'Group 48 paired declaration-scope/status record schema'
NEXT_SCRIPT = 'candidate_status_field_and_nonactive_branch_record.py'


def build_entries() -> List[Entry]:
    return [
        Entry('S1: record identity', 'record identifies itself as paired declaration-scope/status record', 'SCOPE_STATUS_RECORD', 'identity distinguishes this artifact from a declaration record', 'not equation status'),
        Entry('S2: paired-record domain', 'domain is the paired non-active metric/scale record surface', 'DOMAIN_FIELD', 'domain references B_s_metric and b_s_scale records together', 'not physical insertion domain'),
        Entry('S3: status field', 'status is scope-record / pre-declaration / not declared', 'STATUS_FIELD', 'status must be visible and non-active', 'not declared by omission'),
        Entry('S4: assumption fields', 'shared zeta, symbolic d, numeric-d condition, and non-active branch status', 'ASSUMPTION_FIELD', 'assumptions are carried explicitly', 'not theorem proof'),
        Entry('S5: caveat fields', 'forbids insertion, active O, residual/source proof, recombination, and parent use', 'CAVEAT_FIELD', 'record carries its own limitations', 'not optional'),
        Entry('S6: handoff field', 'future declaration attempt requires separate explicit declaration record', 'DEFERRED_WITH_TARGET', 'schema names the next possible route without executing it', 'not declaration attempt'),
    ]


def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: schema as declaration', 'treat schema completeness as trace-normalization declaration', 'schema is a container, not installation'),
        Shortcut('X2: domain drift', 'treat paired record domain as physical field-equation domain', 'record domain is review/declaration-scope infrastructure only'),
        Shortcut('X3: omitted caveats', 'leave caveats implicit', 'omission invites insertion and parent overreach'),
        Shortcut('X4: assumption hiding', 'hide numeric d or branch status in prose', 'assumptions must be fields'),
    ]


def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: preserve schema/declaration boundary', 'NOT_DECLARED', 'future summaries must call this a scope/status record, not a declaration', 'avoid record inflation'),
        ObligationEntry('O2: keep all fields explicit', 'POLICY_RULE', 'status, domain, assumptions, numeric-d condition, branch status, and caveats must stay explicit', 'avoid hidden assumptions'),
        ObligationEntry('O3: preserve downstream caveats', 'NOT_READY', 'do not drop non-insertion and no-parent fields', 'avoid downstream drift'),
    ]


LOCAL_CONCLUSIONS = [('schema stated', 'PASS', 'paired scope/status record fields made explicit'), ('schema not declaration', 'NOT_DECLARED', 'field completeness is not trace-normalization declaration')]


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
