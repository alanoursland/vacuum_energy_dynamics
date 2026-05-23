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

SCRIPT_LABEL = 'Candidate Status Field and Nonactive Branch Record'
MARKER_ID = 'g48_status_field'
DEPENDENCIES = [('g47_summary', '047_normalization_declaration_scope_closure_audit__candidate_group_47_status_summary', 'g47_summary'), ('g48_schema', '048_explicit_paired_declaration_scope_status_record__candidate_paired_scope_record_schema', 'g48_schema')]
QUESTION = 'How should the status field prevent the paired record from becoming a hidden declaration or branch choice?'
DISCIPLINE = 'This script audits the status field and branch non-active clauses. It must prevent scope-record clarity from becoming branch choice, declaration, or adoption.'
OPENING_LINE = 'Status/non-active branch record opened -- status discipline only; no branch choice or declaration'
SCOPE = 'Group 48 status field and non-active branch record'
NEXT_SCRIPT = 'candidate_assumption_domain_and_numeric_d_condition_record.py'


def build_entries() -> List[Entry]:
    return [
        Entry('T1: scope-record status', 'record status is explicit paired declaration-scope/status record', 'STATUS_FIELD', 'the status names the artifact without installing an equation', 'not declared'),
        Entry('T2: pre-declaration status', 'trace normalization remains not declared', 'NOT_DECLARED', 'pre-declaration status must be written on the record', 'not declaration-ready by implication'),
        Entry('T3: metric branch status', 'B_s_metric remains non-active / candidate / not chosen', 'NON_ACTIVE', 'metric side can be referenced only as paired candidate', 'not selected'),
        Entry('T4: scale branch status', 'b_s_scale remains non-active / candidate / not chosen', 'NON_ACTIVE', 'scale side can be referenced only as paired candidate', 'not selected'),
        Entry('T5: Package B status', 'Package B remains not adopted', 'NOT_ADOPTED', 'scope/status record is not theory adoption', 'adoption separate'),
    ]


def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: status omission', 'omit status and let readers infer declaration', 'status omission caused exactly the drift this group prevents'),
        Shortcut('X2: both branches active', 'treat paired status as adopting both branches', 'parallel records are non-active candidates'),
        Shortcut('X3: one branch quietly active', 'let one side become active because it is more convenient', 'hidden branch choice is forbidden'),
        Shortcut('X4: record as adoption', 'treat status record as Package B adoption', 'adoption is separate'),
    ]


def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: require status field', 'POLICY_RULE', 'scope/status record must carry explicit non-declared status', 'avoid declaration drift'),
        ObligationEntry('O2: preserve branch non-active status', 'NOT_CHOSEN', 'both branch records remain candidates until separate choice/declaration', 'avoid branch drift'),
        ObligationEntry('O3: preserve adoption boundary', 'NOT_ADOPTED', 'do not treat record instantiation as Package B adoption', 'avoid adoption drift'),
    ]


LOCAL_CONCLUSIONS = [('status field disciplined', 'PASS', 'status and branch non-active clauses prevent accidental declaration'), ('no branch selected', 'NOT_CHOSEN', 'metric and scale records remain paired candidates')]


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
