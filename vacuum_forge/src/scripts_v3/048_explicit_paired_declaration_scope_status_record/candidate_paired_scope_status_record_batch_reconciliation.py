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

SCRIPT_LABEL = 'Candidate Paired Scope Status Record Batch Reconciliation'
MARKER_ID = 'g48_recon'
DEPENDENCIES = [('g47_summary', '047_normalization_declaration_scope_closure_audit__candidate_group_47_status_summary', 'g47_summary'), ('g48_problem', '048_explicit_paired_declaration_scope_status_record__candidate_paired_scope_status_record_problem', 'g48_problem'), ('g48_schema', '048_explicit_paired_declaration_scope_status_record__candidate_paired_scope_record_schema', 'g48_schema'), ('g48_status_field', '048_explicit_paired_declaration_scope_status_record__candidate_status_field_and_nonactive_branch_record', 'g48_status_field'), ('g48_assumption_domain', '048_explicit_paired_declaration_scope_status_record__candidate_assumption_domain_and_numeric_d_condition_record', 'g48_assumption_domain'), ('g48_caveat_record', '048_explicit_paired_declaration_scope_status_record__candidate_downstream_caveat_and_rejected_broadening_record', 'g48_caveat_record'), ('g48_integrity_sieve', '048_explicit_paired_declaration_scope_status_record__candidate_scope_status_record_integrity_sieve', 'g48_integrity_sieve')]
QUESTION = 'Did the Group 48 batch instantiate the explicit paired declaration-scope/status record without declaring trace normalization?'
DISCIPLINE = 'This script reconciles the Group 48 batch. It should preserve record-instantiated status while blocking trace declaration, adoption, insertion, active O, and parent closure.'
OPENING_LINE = 'Paired scope/status record batch reconciliation opened -- reconciliation only; no final summary, declaration, or downstream route'
SCOPE = 'Group 48 paired scope status record batch reconciliation'
NEXT_SCRIPT = 'candidate_group_48_status_summary.py'


def build_entries() -> List[Entry]:
    return [
        Entry('Q1: opener expectation', 'Group 48 opened as explicit paired scope/status record instantiation', 'MATCHED_EXPECTATION', 'expected if the batch wrote the requested artifact rather than another audit loop', 'summary may call this record instantiation'),
        Entry('Q2: schema expectation', 'record schema fields are explicit', 'MATCHED_EXPECTATION', 'expected if identity, domain, status, assumptions, caveats, and handoff fields were named', 'not declaration'),
        Entry('Q3: status expectation', 'non-active and not-declared status was preserved', 'MATCHED_EXPECTATION', 'expected if branch choice and declaration did not occur', 'summary must preserve non-active status'),
        Entry('Q4: assumption expectation', 'domain, zeta, symbolic d, and numeric-d condition were made explicit', 'MATCHED_EXPECTATION', 'expected if numeric d stayed conditioned and not fixed', 'summary must preserve numeric-d condition'),
        Entry('Q5: caveat expectation', 'downstream caveats and rejected broadenings remained attached', 'MATCHED_EXPECTATION', 'expected if insertion and parent routes stayed blocked', 'summary must preserve locks'),
        Entry('Q6: integrity expectation', 'assembled record is coherent as pre-declaration infrastructure', 'MATCHED_EXPECTATION', 'expected if next route is conditional declaration review only', 'summary must avoid declaration-ready overclaim'),
        Entry('Q7: downstream gates', 'adoption, insertion, active O, residual control, recombination, and parent closure remain closed', 'NOT_READY', 'expected final boundary', 'summary must not open field-equation routes'),
    ]


def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: reconciliation as final summary', 'treat this script as group close', 'final summary should follow actual outputs'),
        Shortcut('X2: record-instantiated as declaration', 'say trace normalization is now declared', 'the record is pre-declaration infrastructure'),
        Shortcut('X3: artifact as insertion', 'open B_s/F_zeta insertion or parent route', 'downstream gates remain closed'),
        Shortcut('X4: artifact as adoption', 'treat scope/status record as Package B adoption', 'adoption remains separate'),
    ]


def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: summary must follow outputs', 'OPEN', 'final summary must report mismatches if any actual output differs', 'avoid self-validation'),
        ObligationEntry('O2: preserve record-instantiated result', 'PAIRED_SCOPE_STATUS_RECORD', 'summary should say explicit paired scope/status record surface is instantiated', 'avoid vague not-ready'),
        ObligationEntry('O3: preserve no declaration', 'NOT_DECLARED', 'summary must say trace normalization remains undeclared', 'avoid status inflation'),
        ObligationEntry('O4: preserve downstream locks', 'NOT_READY', 'insertion, active O, residual control, recombination, and parent closure remain closed', 'avoid field-equation overreach'),
    ]


LOCAL_CONCLUSIONS = [('batch reconciliation prepared', 'PASS', 'write summary after actual outputs are reviewed'), ('no group close here', 'DEFERRED_WITH_TARGET', 'candidate_group_48_status_summary.py should preserve record-instantiated but not-declared status')]


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
