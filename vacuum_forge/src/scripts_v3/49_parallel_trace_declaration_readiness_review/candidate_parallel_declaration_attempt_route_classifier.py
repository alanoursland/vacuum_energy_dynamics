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

SCRIPT_LABEL = 'Candidate Parallel Declaration Attempt Route Classifier'
MARKER_ID = 'g49_route_classifier'
DEPENDENCIES = [('g48_summary', '48_explicit_paired_declaration_scope_status_record__candidate_group_48_status_summary', 'g48_summary'), ('g49_failure_sieve', '49_parallel_trace_declaration_readiness_review__candidate_predeclaration_failure_mode_sieve', 'g49_failure_sieve')]
QUESTION = 'After declaration-readiness review, what is the honest next route?'
DISCIPLINE = 'This script classifies whether a separate parallel trace-normalization declaration attempt is now an honest next target. It does not write the declaration.'
OPENING_LINE = 'Parallel declaration-attempt route classifier opened -- route classification only; no declaration executed'
SCOPE = 'Group 49 parallel declaration attempt route classifier'
NEXT_SCRIPT = 'candidate_declaration_readiness_review_batch_reconciliation.py'
LOCAL_CONCLUSIONS = [('route classification complete', 'PASS', 'next non-looping target is a separate parallel trace-normalization declaration attempt'), ('attempt ready with conditions', 'READY_FOR_DECLARATION_ATTEMPT_WITH_CONDITIONS', 'readiness is conditional and not declaration itself')]


def build_entries() -> List[Entry]:
    return [
        Entry('R1: record input accepted', 'Group 48 scope/status record is accepted as input for readiness review', 'RECORD_ACCEPTED_FOR_REVIEW', 'the artifact is complete enough to support next-route evaluation', 'not declaration'),
        Entry('R2: numeric-d condition accepted for symbolic attempt', 'numeric d does not block a symbolic/scope-conditioned paired attempt', 'READY_FOR_DECLARATION_ATTEMPT_WITH_CONDITIONS', 'the future attempt must not fix numeric d', 'not numeric declaration'),
        Entry('R3: future declaration record requirements explicit', 'minimum fields for the declaration attempt are now known', 'DECLARATION_RECORD_REQUIREMENT', 'the next group need not rediscover requirements', 'not declaration'),
        Entry('R4: bad broadenings rejected', 'neutral-law, branch-smuggling, numeric-d leak, recovery-selector, insertion, active-O, safety-proof, and parent routes rejected', 'REJECTED_ROUTE', 'only the limited symbolic paired route survives', 'not broadening'),
        Entry('R5: next non-looping target', 'write a separate parallel trace-normalization declaration attempt under stated conditions', 'DEFERRED_WITH_TARGET', 'next group may attempt declaration but must be allowed to fail or remain conditional', 'not automatic success'),
    ]


def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: classifier as declaration', 'treat route classification as the declaration', 'the next group must write a separate record'),
        Shortcut('X2: conditions as closed', 'treat conditions as already satisfied theorem support', 'conditions are constraints on the attempt'),
        Shortcut('X3: direct adoption', 'adopt Package B because declaration attempt is allowed', 'adoption remains later and separate'),
        Shortcut('X4: direct insertion', 'insert B_s/F_zeta because declaration attempt is allowed', 'insertion remains not ready'),
    ]


def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: write separate declaration attempt next', 'DEFERRED_WITH_TARGET', 'if continuing this route, write a separate parallel declaration-attempt script/group', 'avoid audit loop'),
        ObligationEntry('O2: preserve conditions', 'POLICY_RULE', 'the attempt must preserve symbolic d, numeric-d condition, paired branch labels, and caveats', 'avoid hidden postulate'),
        ObligationEntry('O3: preserve no adoption/insertion', 'NOT_READY', 'do not open adoption, insertion, active O, recombination, or parent closure', 'avoid field-equation overreach'),
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
