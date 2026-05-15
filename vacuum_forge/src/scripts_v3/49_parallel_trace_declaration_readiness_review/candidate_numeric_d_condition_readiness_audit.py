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

SCRIPT_LABEL = 'Candidate Numeric d Condition Readiness Audit'
MARKER_ID = 'g49_numeric_d_readiness'
DEPENDENCIES = [('g48_summary', '48_explicit_paired_declaration_scope_status_record__candidate_group_48_status_summary', 'g48_summary'), ('g49_record_acceptance', '49_parallel_trace_declaration_readiness_review__candidate_scope_status_record_acceptance_audit', 'g49_record_acceptance')]
QUESTION = 'Does the numeric-d condition block a later parallel declaration attempt, or can a symbolic scope-conditioned declaration attempt preserve it?'
DISCIPLINE = 'This script decides whether numeric d must be fixed before any declaration attempt. It may permit only a symbolic and scope-conditioned declaration attempt, not a numeric declaration.'
OPENING_LINE = 'Numeric-d condition readiness audit opened -- symbolic/scope-conditioned review only; no numeric d declaration'
SCOPE = 'Group 49 numeric d condition readiness audit'
NEXT_SCRIPT = 'candidate_declaration_record_requirement_matrix.py'
LOCAL_CONCLUSIONS = [('numeric-d condition classified', 'PASS', 'numeric d does not block a symbolic paired declaration attempt if the condition is explicit'), ('numeric d not fixed', 'SCOPE_REQUIRED', 'numeric dimension remains conditioned and undeclared')]


def build_entries() -> List[Entry]:
    return [
        Entry('D1: symbolic d accepted', 'symbolic d can be carried into a declaration attempt as the traced-dimension field', 'SYMBOLIC_D_ALLOWED', 'symbolic d is adequate for a paired symbolic declaration attempt', 'not numeric value'),
        Entry('D2: numeric d remains conditioned', 'numeric d must remain conditional on explicit scope/declaration support', 'NUMERIC_D_CONDITION', 'future declaration must state numeric d is not fixed here', 'not numeric closure'),
        Entry('D3: factor-of-two protection', 'd handling cannot erase 2*zeta/d versus zeta/d', 'CONSISTENCY_RULE', 'dimension conditions must preserve branch-normalization burden', 'not compromise law'),
        Entry('D4: readiness impact', 'numeric d condition does not block a symbolic paired declaration attempt if explicitly preserved', 'READY_FOR_DECLARATION_ATTEMPT_WITH_CONDITIONS', 'the attempt may proceed only without fixing numeric d', 'not full declaration readiness'),
        Entry('D5: forbidden numeric routes', 'recovery, aesthetics, and factor-of-two erasure cannot set numeric d', 'POLICY_RULE', 'numeric d cannot be selected by forbidden shortcuts', 'not selector'),
    ]


def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: numeric d leak', 'quietly fix numeric d in the declaration attempt', 'numeric d remains conditioned'),
        Shortcut('X2: d by recovery', 'choose d from Schwarzschild, AB=1, or gamma recovery', 'recovery is audit only'),
        Shortcut('X3: d erases factor two', 'change d to make branch expressions match', 'dimension cannot hide branch burden'),
        Shortcut('X4: symbolic d as parent d', 'treat symbolic review d as parent-facing dimension', 'parent-facing use requires theorem support'),
    ]


def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: preserve symbolic declaration mode', 'NUMERIC_D_CONDITION', 'any next declaration attempt must remain symbolic/scope-conditioned with respect to d', 'avoid hidden numeric declaration'),
        ObligationEntry('O2: preserve factor-of-two visibility', 'POLICY_RULE', 'keep 2*zeta/d and zeta/d separated', 'avoid neutral-law smuggling'),
        ObligationEntry('O3: preserve parent-facing block', 'THEOREM_REQUIRED', 'do not promote symbolic d to parent-facing dimension without identity and safety support', 'avoid parent drift'),
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
