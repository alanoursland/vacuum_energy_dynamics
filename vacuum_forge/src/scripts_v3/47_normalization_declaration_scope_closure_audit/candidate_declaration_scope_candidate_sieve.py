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

SCRIPT_LABEL = 'Candidate Declaration Scope Candidate Sieve'
MARKER_ID = 'g47_scope_candidate_sieve'
DEPENDENCIES = [('g46_summary', '46_parallel_trace_convention_field_closure_audit__candidate_group_46_status_summary', 'g46_summary'), ('g47_review_decl_boundary', '47_normalization_declaration_scope_closure_audit__candidate_review_vs_declaration_scope_boundary', 'g47_review_decl_boundary')]
QUESTION = 'Which declaration-scope candidates survive the current guardrails, and which scope routes are eliminated?'
DISCIPLINE = 'This script sieves possible declaration-scope routes. It may identify a surviving pre-declaration scope candidate but cannot declare trace normalization.'
OPENING_LINE = 'Declaration-scope candidate sieve opened -- candidate routes classified; no declaration executed'
SCOPE = 'Group 47 declaration-scope candidate sieve'
NEXT_SCRIPT = 'candidate_scope_status_and_assumption_matrix.py'

def build_entries() -> List[Entry]:
    return [
        Entry('S1: paired-record declaration-review scope', 'parallel pair may be reviewed as two non-active branch-indexed records', 'DECLARATION_SCOPE_CANDIDATE', 'scope preserves B_s_metric and b_s_scale as paired candidates', 'not one law'),
        Entry('S2: limited trace-normalization declaration-scope candidate', 'a later declaration could be limited to the paired record surface under explicit assumptions', 'DECLARATION_SCOPE_READY_FOR_RECORD', 'this is the strongest surviving candidate scope for a future declaration-scope record', 'not declaration itself'),
        Entry('S3: single-branch declaration scope', 'single-branch scope requires explicit metric or scale choice first', 'CHOICE_REQUIRED', 'branch choice cannot be smuggled through scope', 'not available in this group'),
        Entry('S4: neutral-law declaration scope', 'unqualified B_s or neutral F_zeta with expression is eliminated', 'REJECTED_ROUTE', 'it collapses the factor-of-two burden', 'forbidden route'),
        Entry('S5: parent-facing declaration scope', 'parent-facing trace-normalization scope remains theorem-required', 'THEOREM_REQUIRED', 'needs residual/source/boundary/divergence support', 'not available'),
        Entry('S6: insertion-facing scope', 'B_s/F_zeta insertion-facing scope is not ready', 'NOT_READY', 'requires scalar-response law and downstream safety', 'not declaration scope'),
    ]

def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: neutral declaration scope', 'declare an unqualified B_s law from the pair', 'that hides branch dependence'),
        Shortcut('X2: declaration scope chooses branch', 'make single-branch scope without explicit choice', 'scope is not selector'),
        Shortcut('X3: parent scope shortcut', 'use declaration scope to skip parent identity work', 'parent identity remains missing'),
        Shortcut('X4: scope as insertion law', 'treat surviving scope candidate as B_s/F_zeta insertion', 'scope is not recombination'),
    ]

def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: preserve paired candidate scope', 'OPEN', 'keep surviving scope limited to paired non-active records', 'avoid neutral-law drift'),
        ObligationEntry('O2: require explicit assumptions', 'OPEN', 'future declaration-scope record must state assumptions and status', 'avoid declaration by implication'),
        ObligationEntry('O3: keep single-branch scope choice-required', 'OPEN', 'do not run single-branch route without explicit choice', 'avoid hidden postulate'),
        ObligationEntry('O4: keep parent and insertion scope unavailable', 'OPEN', 'do not broaden surviving scope downstream', 'avoid field-equation overreach'),
    ]

LOCAL_CONCLUSIONS = [('scope candidates sieved', 'PASS', 'surviving route is limited paired-record declaration-scope candidate'), ('downstream scopes rejected or deferred', 'NOT_READY', 'parent-facing and insertion-facing scopes remain unavailable')]

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
