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

SCRIPT_LABEL = 'Candidate Declaration Scope Route Classifier'
MARKER_ID = 'g47_route_classifier'
DEPENDENCIES = [('g46_summary', '46_parallel_trace_convention_field_closure_audit__candidate_group_46_status_summary', 'g46_summary'), ('g47_parent_scope_reject', '47_normalization_declaration_scope_closure_audit__candidate_parent_facing_scope_rejection_audit', 'g47_parent_scope_reject'), ('g47_scope_status_matrix', '47_normalization_declaration_scope_closure_audit__candidate_scope_status_and_assumption_matrix', 'g47_scope_status_matrix')]
QUESTION = 'After the declaration-scope audits, what is the honest next route classification?'
DISCIPLINE = 'This script classifies whether Group 47 made declaration scope ready for a later explicit record, still blocked it, or pushed the problem to axiom/choice/theorem routes.'
OPENING_LINE = 'Declaration-scope route classifier opened -- route classification only; no declaration executed'
SCOPE = 'Group 47 declaration-scope route classifier'
NEXT_SCRIPT = 'candidate_declaration_scope_closure_batch_reconciliation.py'

def build_entries() -> List[Entry]:
    return [
        Entry('R1: review scope status', 'record-review scope remains closed for review', 'CLOSED_FOR_REVIEW', 'unchanged from Group 46 but preserved', 'not declaration'),
        Entry('R2: paired declaration-scope candidate', 'limited paired-record declaration scope is ready for an explicit future scope record', 'DECLARATION_SCOPE_READY_FOR_RECORD', 'scope requirements and caveats are now explicit enough to write a scope record', 'not trace-normalization declaration'),
        Entry('R3: numeric d status', 'numeric d remains scope-dependent and must be handled in the future scope record', 'SCOPE_REQUIRED', 'scope record must not fix d by recovery or prettiness', 'not closed numerically here'),
        Entry('R4: single-branch scope', 'single-branch declaration scope remains choice-required', 'CHOICE_REQUIRED', 'requires explicit branch choice before use', 'not available here'),
        Entry('R5: parent-facing scope', 'parent-facing scope remains theorem-required', 'THEOREM_REQUIRED', 'requires safety and identity support', 'not available here'),
        Entry('R6: next non-looping target', 'write explicit declaration-scope record or scope-status record before declaration attempt', 'DEFERRED_WITH_TARGET', 'next work should instantiate the scope record, not repeat the audit', 'not declaration itself'),
    ]

def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: scope-record-ready as declaration-ready', 'treat readiness for scope record as trace-normalization declaration readiness', 'scope record is still not equation declaration'),
        Shortcut('X2: limited scope as insertion-ready', 'insert B_s/F_zeta from limited scope', 'insertion remains downstream'),
        Shortcut('X3: choice-required as chosen', 'treat single-branch scope route as selected', 'choice requires separate explicit record'),
        Shortcut('X4: theorem-required as theorem supplied', 'treat parent-facing scope requirement as closed', 'theorem support absent'),
    ]

def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: write explicit scope record next', 'OPEN', 'future work should instantiate paired declaration-scope/status record', 'avoid audit loop'),
        ObligationEntry('O2: preserve no declaration', 'OPEN', 'scope record readiness must not be reported as trace-normalization declaration', 'avoid status inflation'),
        ObligationEntry('O3: preserve downstream locks', 'OPEN', 'insertion, active O, residual control, recombination, and parent closure stay closed', 'avoid field-equation overreach'),
    ]

LOCAL_CONCLUSIONS = [('route classification complete', 'PASS', 'next target is explicit paired declaration-scope/status record'), ('trace normalization still undeclared', 'NOT_DECLARED', 'Group 47 does not install trace-normalization declaration')]

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
