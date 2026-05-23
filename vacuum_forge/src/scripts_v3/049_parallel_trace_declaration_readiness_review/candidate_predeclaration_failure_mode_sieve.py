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

SCRIPT_LABEL = 'Candidate Predeclaration Failure Mode Sieve'
MARKER_ID = 'g49_failure_sieve'
DEPENDENCIES = [('g48_summary', '48_explicit_paired_declaration_scope_status_record__candidate_group_48_status_summary', 'g48_summary'), ('g49_requirement_matrix', '49_parallel_trace_declaration_readiness_review__candidate_declaration_record_requirement_matrix', 'g49_requirement_matrix')]
QUESTION = 'Which failure modes would still kill or demote a future parallel declaration attempt?'
DISCIPLINE = 'This script attacks the possible declaration attempt before it is written. Surviving this sieve is not declaration.'
OPENING_LINE = 'Predeclaration failure-mode sieve opened -- adversarial review only; no declaration executed'
SCOPE = 'Group 49 predeclaration failure mode sieve'
NEXT_SCRIPT = 'candidate_parallel_declaration_attempt_route_classifier.py'
LOCAL_CONCLUSIONS = [('failure sieve complete', 'PASS', 'forbidden declaration upgrades killed or demoted'), ('limited declaration attempt survives', 'READY_FOR_DECLARATION_ATTEMPT_WITH_CONDITIONS', 'symbolic paired caveated declaration attempt may be considered next')]


def build_entries() -> List[Entry]:
    return [
        Entry('F1: branch smuggling failure', 'single-branch activation without explicit choice would kill the route', 'REJECTED_ROUTE', 'branch choice cannot be hidden inside paired declaration language', 'not allowed'),
        Entry('F2: neutral-law collapse failure', 'unqualified B_s, neutral F_zeta expression, or compromise expression would kill the route', 'REJECTED_ROUTE', 'the paired route survives only if branch expressions remain separated', 'not allowed'),
        Entry('F3: numeric-d leakage failure', 'fixing numeric d without scope support would block or demote the attempt', 'REJECTED_ROUTE', 'numeric d must remain conditioned unless separately justified', 'not allowed'),
        Entry('F4: recovery-selector failure', 'using recovery success as declaration support would invalidate the attempt', 'REJECTED_ROUTE', 'recovery remains audit only', 'not construction'),
        Entry('F5: downstream drift failure', 'insertion, active O, safety theorem, recombination, or parent use would invalidate the attempt', 'REJECTED_ROUTE', 'declaration attempt cannot become field-equation machinery', 'not downstream use'),
        Entry('F6: surviving attempt shape', 'symbolic paired declaration attempt with explicit caveats survives this sieve', 'READY_FOR_DECLARATION_ATTEMPT_WITH_CONDITIONS', 'the route survives only as a separate future attempt under constraints', 'not declaration here'),
    ]


def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: survival as proof', 'treat surviving the sieve as proof of trace normalization', 'sieve survival is permission to attempt, not proof'),
        Shortcut('X2: failure as total no-go', 'treat any blocked broadening as killing the paired symbolic route', 'bad broadenings can die while limited route survives'),
        Shortcut('X3: downstream drift', 'claim declaration attempt can support insertion', 'insertion remains separate'),
    ]


def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: carry failure criteria into next group', 'POLICY_RULE', 'future declaration attempt must be checked against these failure modes', 'avoid repeating forbidden shortcuts'),
        ObligationEntry('O2: preserve limited surviving shape', 'READY_FOR_DECLARATION_ATTEMPT_WITH_CONDITIONS', 'carry only the symbolic paired caveated attempt forward', 'avoid broadening'),
        ObligationEntry('O3: preserve no-declaration status', 'NOT_DECLARED', 'do not call sieve survival a declaration', 'avoid overclaiming'),
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
