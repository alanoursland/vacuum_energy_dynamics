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

SCRIPT_LABEL = 'Candidate Parent-Facing Scope Rejection Audit'
MARKER_ID = 'g47_parent_scope_reject'
DEPENDENCIES = [('g46_summary', '046_parallel_trace_convention_field_closure_audit__candidate_group_46_status_summary', 'g46_summary'), ('g47_scope_status_matrix', '047_normalization_declaration_scope_closure_audit__candidate_scope_status_and_assumption_matrix', 'g47_scope_status_matrix')]
QUESTION = 'Which attempts to broaden declaration scope toward insertion or parent-facing use must be rejected now?'
DISCIPLINE = 'This script adversarially rejects scope broadening that would turn a declaration-scope audit into field-equation machinery.'
OPENING_LINE = 'Parent-facing scope rejection audit opened -- downstream broadening rejected unless theorem support exists'
SCOPE = 'Group 47 parent-facing scope rejection audit'
NEXT_SCRIPT = 'candidate_declaration_scope_route_classifier.py'

def build_entries() -> List[Entry]:
    return [
        Entry('P1: parent-facing scope by name', 'calling scope parent-facing without identity support is rejected', 'REJECTED_ROUTE', 'parent-facing trace scope needs residual/source/boundary/divergence and identity support', 'not available'),
        Entry('P2: insertion-facing scope', 'using scope to license B_s/F_zeta insertion is rejected', 'REJECTED_ROUTE', 'insertion needs scalar-response law and safety gates', 'not recombination'),
        Entry('P3: active O scope', 'using scope language to construct or imply active O is rejected', 'REJECTED_ROUTE', 'scope fields do not define projector domain/codomain/kernel/image', 'not no-overlap'),
        Entry('P4: residual/source safety scope', 'using scope to prove residual nonentry or source protection is rejected', 'REJECTED_ROUTE', 'safety theorems remain separate', 'not theorem support'),
        Entry('P5: admissible limited scope', 'limited paired-record declaration-scope candidate survives as pre-declaration infrastructure', 'DECLARATION_SCOPE_CANDIDATE', 'scope may remain useful if explicitly caveated', 'not downstream-ready'),
    ]

def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: scope opens insertion', 'open insertion from declaration-scope clarity', 'insertion remains locked'),
        Shortcut('X2: scope constructs O', 'treat scope as no-overlap operator', 'labels and scopes are not projectors'),
        Shortcut('X3: scope proves safety', 'claim residual/source safety from scope limit', 'theorems remain separate'),
        Shortcut('X4: scope opens parent', 'open parent equation from scope status', 'parent identity remains missing'),
    ]

def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: keep parent-facing scope theorem-required', 'OPEN', 'do not use parent-facing scope without identity and safety support', 'avoid early parent closure'),
        ObligationEntry('O2: keep insertion scope not ready', 'OPEN', 'do not use declaration-scope record as insertion law', 'avoid recombination drift'),
        ObligationEntry('O3: preserve limited surviving scope', 'OPEN', 'carry only paired-record declaration-scope candidate forward', 'avoid broadening'),
    ]

LOCAL_CONCLUSIONS = [('downstream scope routes rejected', 'PASS', 'insertion and parent-facing scope shortcuts rejected'), ('limited scope survives', 'DECLARATION_SCOPE_CANDIDATE', 'surviving scope remains pre-declaration and caveated')]

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
