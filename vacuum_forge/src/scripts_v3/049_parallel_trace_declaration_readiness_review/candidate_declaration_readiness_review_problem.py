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
        "DECLARATION_READINESS_REVIEW": StatusMark.INFO,
        "RECORD_ACCEPTED_FOR_REVIEW": StatusMark.INFO,
        "READY_FOR_DECLARATION_ATTEMPT_WITH_CONDITIONS": StatusMark.INFO,
        "DECLARATION_ATTEMPT_CANDIDATE": StatusMark.INFO,
        "DECLARATION_RECORD_REQUIREMENT": StatusMark.INFO,
        "SCOPE_STATUS_RECORD": StatusMark.INFO,
        "PAIRED_SCOPE_STATUS_RECORD": StatusMark.INFO,
        "STATUS_FIELD": StatusMark.INFO,
        "ASSUMPTION_FIELD": StatusMark.INFO,
        "CAVEAT_FIELD": StatusMark.INFO,
        "CLOSED_FOR_REVIEW": StatusMark.INFO,
        "REVIEW_READY_ONLY": StatusMark.INFO,
        "NON_ACTIVE": StatusMark.INFO,
        "BRANCH_INDEXED": StatusMark.INFO,
        "SYMBOLIC_D_ALLOWED": StatusMark.INFO,
        "NUMERIC_D_CONDITION": StatusMark.OBLIGATION,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "CONSISTENCY_RULE": StatusMark.OBLIGATION,
        "SCOPE_REQUIRED": StatusMark.OBLIGATION,
        "EXPLICIT_CHOICE_REQUIRED": StatusMark.OBLIGATION,
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
#   49_parallel_trace_declaration_readiness_review
# Script type:
#   DECLARATION READINESS REVIEW / PRE-DECLARATION

SCRIPT_LABEL = 'Candidate Declaration Readiness Review Problem'
MARKER_ID = 'g49_problem'
DEPENDENCIES = [('g48_summary', '48_explicit_paired_declaration_scope_status_record__candidate_group_48_status_summary', 'g48_summary'), ('g48_integrity_sieve', '48_explicit_paired_declaration_scope_status_record__candidate_scope_status_record_integrity_sieve', 'g48_integrity_sieve')]
QUESTION = 'Can the instantiated paired declaration-scope/status record support a later separate parallel trace-normalization declaration attempt?'
DISCIPLINE = 'This script opens Group 49 as declaration-readiness review. It may review whether an attempt is honest, but it does not declare trace normalization, choose a branch, adopt Package B, or license insertion.'
OPENING_LINE = 'Group 49 declaration-readiness review opened -- review only; no trace declaration, branch choice, adoption, insertion, active O, recombination, or parent route'
SCOPE = 'Group 49 declaration readiness review problem'
NEXT_SCRIPT = 'candidate_scope_status_record_acceptance_audit.py'
LOCAL_CONCLUSIONS = [('Group 49 opener complete', 'PASS', 'declaration-readiness review opened'), ('no declaration made', 'NOT_DECLARED', 'readiness review cannot install trace normalization')]


def build_entries() -> List[Entry]:
    return [
        Entry('P1: review target', 'instantiated paired declaration-scope/status record from Group 48', 'DECLARATION_READINESS_REVIEW', 'Group 49 may review whether the artifact can support a later declaration attempt', 'not the declaration itself'),
        Entry('P2: accepted input class', 'paired scope/status record can be treated as the input under review', 'PAIRED_SCOPE_STATUS_RECORD', 'the record has identity, domain, status, assumptions, numeric-d condition, caveats, and handoff route', 'not equation installation'),
        Entry('P3: possible positive outcome', 'a future declaration attempt may be permitted under strict conditions', 'READY_FOR_DECLARATION_ATTEMPT_WITH_CONDITIONS', 'readiness can mean permission to write a separate declaration-attempt record', 'not automatic declaration'),
        Entry('P4: possible negative outcomes', 'readiness may still be blocked, theorem-required, choice-required, or axiom-required', 'DEFERRED_WITH_TARGET', 'the review must classify blockers sharply if they remain', 'not vague not-ready'),
        Entry('P5: downstream locks', 'insertion, active O, residual/source safety, recombination, and parent closure remain outside this review', 'NOT_READY', 'declaration readiness cannot become field-equation use', 'not downstream opening'),
    ]


def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: review as declaration', 'treat readiness review as the declaration itself', 'readiness review is not equation installation'),
        Shortcut('X2: review as adoption', 'treat readiness review as Package B adoption', 'adoption remains a separate theory decision'),
        Shortcut('X3: review as insertion', 'use readiness to insert B_s/F_zeta', 'insertion needs separate scalar-response law and safety gates'),
        Shortcut('X4: review as branch choice', 'let readiness choose metric or scale', 'paired route remains branch-neutral unless a later choice record says otherwise'),
    ]


def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: classify readiness sharply', 'DEFERRED_WITH_TARGET', 'state whether declaration attempt is permitted, blocked, axiom-required, choice-required, or theorem-required', 'avoid another audit loop'),
        ObligationEntry('O2: preserve no declaration', 'NOT_DECLARED', 'do not call readiness review a trace-normalization declaration', 'avoid status inflation'),
        ObligationEntry('O3: preserve downstream locks', 'NOT_READY', 'keep insertion, active O, recombination, and parent closure closed', 'avoid field-equation overreach'),
    ]


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
