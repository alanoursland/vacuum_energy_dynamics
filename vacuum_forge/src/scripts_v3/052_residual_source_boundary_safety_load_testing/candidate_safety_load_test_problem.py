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

# Group:
#   52_residual_source_boundary_safety_load_testing
#
# Script type:
#   GOVERNANCE / DIAGNOSTIC

SCRIPT_LABEL = 'Candidate Safety Load Test Problem'
MARKER_ID = 'g52_problem'
DEPENDENCIES = [('g51_summary', '051_trace_normalization_adopt_defer_reject_decision_surface__candidate_group_51_status_summary', 'g51_summary')]
QUESTION = 'What safety load-test surface follows from the Group 51 retained conditional trace-normalization candidate?'
DISCIPLINE = 'This opener frames Group 52 as residual/source/boundary safety load testing. It may classify burdens and obstruction routes, but it must not insert B_s/F_zeta, construct active O, adopt Package B, or open parent closure.'
OPENING_LINE = 'Group 52 safety load-test surface opened -- audit-only candidate; no insertion or parent route'
SCOPE = 'Group 52 safety load-test problem'
NEXT_SCRIPT = 'candidate_count_once_trace_incidence_audit.py'

ENTRIES = [('P1: load-test scope', 'residual/source/boundary safety burdens for the retained conditional attempt', 'SAFETY_LOAD_TEST_SURFACE_OPENED', 'Group 52 may test safety burdens without upgrading the trace candidate', 'not insertion'), ('P2: candidate role', 'conditional trace-normalization attempt remains audit material only', 'CANDIDATE_SURVIVES_AS_AUDIT_ONLY', 'the candidate can be load-tested without physical use', 'not adoption'), ('P3: physical-use closure', 'B_s/F_zeta insertion, active O, recombination, and parent closure remain outside this group', 'NOT_INSERTABLE', 'safety load testing does not open field-equation machinery', 'not parent-ready'), ('P4: possible obstruction', 'a concrete residual/source/boundary obstruction may demote a route', 'THEOREM_TARGET_REFINED', 'obstructions should be recorded if found', 'not pre-assumed')]
SHORTCUTS = [('X1: load test as insertion', 'treat safety-audit scope as permission to insert B_s/F_zeta', 'load testing is not field-equation use'), ('X2: load test as adoption', 'treat candidate survival under audit as Package B adoption', 'adoption remains separate'), ('X3: load test as active O', 'repair safety burdens by naming O', 'O is not constructed here'), ('X4: load test as parent closure', 'summarize safety burden inventory as parent readiness', 'parent identity and divergence support remain missing')]
OBLIGATIONS = [('O1: preserve audit-only role', 'POLICY_RULE', 'keep the conditional candidate as audit material during safety load testing', 'avoid physical-use drift'), ('O2: name safety burdens', 'SAFETY_THEOREMS_REQUIRED', 'make residual/source/boundary safety burdens explicit', 'avoid vague not-ready status'), ('O3: keep insertion closed', 'NOT_INSERTABLE', 'do not open B_s/F_zeta insertion or active O', 'avoid parent-equation overreach')]
LOCAL_CONCLUSIONS = [('safety load-test surface opened', 'PASS', 'Group 52 may proceed to trace/source/boundary burden audits'), ('physical use remains closed', 'NOT_INSERTABLE', 'no insertion or parent route opened by opener')]


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
        "SAFETY_LOAD_TEST_SURFACE_OPENED": StatusMark.INFO,
        "COUNT_ONCE_TRACE_BURDEN_EXPLICIT": StatusMark.OBLIGATION,
        "TRACE_INCIDENCE_DIAGNOSTIC": StatusMark.INFO,
        "RESIDUAL_NONENTRY_THEOREM_REQUIRED": StatusMark.OBLIGATION,
        "RESIDUAL_ENTRY_REJECTED": StatusMark.FAIL,
        "SOURCE_NO_DOUBLE_COUNTING_REQUIRED": StatusMark.OBLIGATION,
        "SOURCE_DUPLICATION_WITNESS": StatusMark.FAIL,
        "A_SECTOR_MASS_PROTECTION_REQUIRED": StatusMark.OBLIGATION,
        "A_SECTOR_MASS_COIN_PROTECTED": StatusMark.INFO,
        "BOUNDARY_SCALAR_SILENCE_REQUIRED": StatusMark.OBLIGATION,
        "SCALAR_TAIL_WITNESS": StatusMark.FAIL,
        "CANDIDATE_SURVIVES_AS_AUDIT_ONLY": StatusMark.INFO,
        "CANDIDATE_BLOCKED_FOR_PHYSICAL_USE": StatusMark.DEFER,
        "THEOREM_TARGET_REFINED": StatusMark.DEFER,
        "OBSTRUCTION_WITNESS_FOUND": StatusMark.FAIL,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "NOT_INSERTABLE": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "THEORY_DECISION_REQUIRED": StatusMark.DEFER,
        "CHOICE_REQUIRED": StatusMark.DEFER,
        "NUMERIC_D_CONDITION": StatusMark.OBLIGATION,
        "SAFETY_THEOREMS_REQUIRED": StatusMark.OBLIGATION,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REJECTED_ROUTE": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "OPEN": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {
        "REJECTED_ROUTE",
        "FORBIDDEN_SHORTCUT",
        "RESIDUAL_ENTRY_REJECTED",
        "SOURCE_DUPLICATION_WITNESS",
        "SCALAR_TAIL_WITNESS",
        "OBSTRUCTION_WITNESS_FOUND",
    }:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {
        "POLICY_RULE",
        "SAFETY_THEOREMS_REQUIRED",
        "COUNT_ONCE_TRACE_BURDEN_EXPLICIT",
        "RESIDUAL_NONENTRY_THEOREM_REQUIRED",
        "SOURCE_NO_DOUBLE_COUNTING_REQUIRED",
        "A_SECTOR_MASS_PROTECTION_REQUIRED",
        "BOUNDARY_SCALAR_SILENCE_REQUIRED",
        "NUMERIC_D_CONDITION",
    }:
        return GovernanceStatus.POLICY_RULE
    return GovernanceStatus.UNVERIFIED


def obligation_status(status: str) -> ObligationStatus:
    if status in {
        "DEFERRED_WITH_TARGET",
        "NOT_INSERTABLE",
        "NOT_ADOPTED",
        "THEORY_DECISION_REQUIRED",
        "CHOICE_REQUIRED",
        "CANDIDATE_BLOCKED_FOR_PHYSICAL_USE",
        "THEOREM_TARGET_REFINED",
    }:
        return ObligationStatus.DEFERRED
    return ObligationStatus.OPEN


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


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


def record_governance(ns, marker_id: str, entries: List[Entry], obligations: List[ObligationEntry], scope: str) -> None:
    record_marker(ns, marker_id, scope)
    for idx, item in enumerate(entries, 1):
        record_claim(
            ns,
            f"{marker_id}_c{idx}",
            marker_id,
            item.status,
            f"{item.name}: {item.subject}. {item.detail}. Boundary: {item.boundary}.",
        )
    for idx, item in enumerate(obligations, 1):
        record_obligation(
            ns,
            f"{marker_id}_o{idx}",
            item.name,
            f"{item.obligation}. Discipline: {item.discipline}.",
            item.status,
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
    header("Rejected shortcuts and invalid upgrades")
    for item in shortcuts:
        subheader(item.name)
        print(f"Shortcut: {item.shortcut}")
        with out.counterexamples():
            out.line(item.name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {item.reason}")


def print_obligations(out: ScriptOutput, obligations: List[ObligationEntry]) -> None:
    header("Open obligations and deferred burdens")
    for item in obligations:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        with out.unresolved_obligations():
            out.line(item.name, mark(item.status), f"{item.status}: {item.obligation}; discipline: {item.discipline}")


def build_entries() -> List[Entry]:
    return [Entry(*item) for item in ENTRIES]


def build_shortcuts() -> List[Shortcut]:
    return [Shortcut(*item) for item in SHORTCUTS]


def build_obligations() -> List[ObligationEntry]:
    return [ObligationEntry(*item) for item in OBLIGATIONS]





def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    entries = build_entries()
    shortcuts = build_shortcuts()
    obligations = build_obligations()

    header(SCRIPT_LABEL)
    print("Question:\n")
    print(QUESTION)
    print("\nDiscipline:\n")
    print(DISCIPLINE)
    with out.governance_assessments():
        out.line(f"{SCRIPT_LABEL} opened", StatusMark.PASS, OPENING_LINE)


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
