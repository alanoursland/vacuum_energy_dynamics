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

SCRIPT_LABEL = 'Candidate Residual / Source / Boundary Safety Batch Reconciliation'
MARKER_ID = 'g52_safety_reconciliation'
DEPENDENCIES = [('g51_summary', '051_trace_normalization_adopt_defer_reject_decision_surface__candidate_group_51_status_summary', 'g51_summary'), ('g52_problem', '052_residual_source_boundary_safety_load_testing__candidate_safety_load_test_problem', 'g52_problem'), ('g52_count_once_trace', '052_residual_source_boundary_safety_load_testing__candidate_count_once_trace_incidence_audit', 'g52_count_once_trace'), ('g52_residual_nonentry', '052_residual_source_boundary_safety_load_testing__candidate_residual_nonentry_obstruction_sieve', 'g52_residual_nonentry'), ('g52_source_matrix', '052_residual_source_boundary_safety_load_testing__candidate_source_no_double_counting_matrix', 'g52_source_matrix'), ('g52_a_mass_protection', '052_residual_source_boundary_safety_load_testing__candidate_a_sector_mass_protection_audit', 'g52_a_mass_protection'), ('g52_boundary_silence', '052_residual_source_boundary_safety_load_testing__candidate_boundary_scalar_silence_dependency_audit', 'g52_boundary_silence'), ('g52_safety_classifier', '052_residual_source_boundary_safety_load_testing__candidate_safety_load_route_classifier', 'g52_safety_classifier')]
QUESTION = 'Did Group 52 load-test the retained conditional trace-normalization candidate against residual/source/boundary safety burdens without upgrading it?'
DISCIPLINE = 'This reconciliation prepares the Group 52 summary. It must preserve audit-only survival, physical-use blockage, and the named safety burdens.'
OPENING_LINE = 'Residual/source/boundary safety batch reconciliation opened -- summarize load test without upgrading candidate'
SCOPE = 'Group 52 residual/source/boundary safety batch reconciliation'
NEXT_SCRIPT = 'candidate_group_52_status_summary.py or result-note pass'

ENTRIES = [('Q1: group scope', 'Group 52 performed first safety load testing of the retained conditional trace candidate', 'SAFETY_LOAD_TEST_SURFACE_OPENED', 'the batch sharpened burdens and witnesses', 'not insertion group'), ('Q2: trace incidence', 'count-once trace burden is explicit and double-count witness is visible', 'COUNT_ONCE_TRACE_BURDEN_EXPLICIT', 'diagnostic ledger is not theorem closure', 'not safety proof'), ('Q3: residual/source status', 'residual reentry and source duplication remain theorem-burdened or rejected routes', 'SAFETY_THEOREMS_REQUIRED', 'physical use remains blocked', 'not solved'), ('Q4: mass/boundary status', 'A-sector mass protection and boundary/scalar silence remain required before insertion', 'A_SECTOR_MASS_PROTECTION_REQUIRED', 'scalar charge and scalar tail witnesses define burdens', 'not neutralized'), ('Q5: candidate status', 'conditional trace candidate survives only as audit material', 'CANDIDATE_SURVIVES_AS_AUDIT_ONLY', 'survival is not adoption or use', 'not Package B adoption'), ('Q6: physical-use status', 'B_s/F_zeta insertion, active O, recombination, and parent closure remain closed', 'NOT_INSERTABLE', 'no field-equation route is opened', 'not parent-ready'), ('Q7: handoff', 'next non-looping target is focused residual/source safety or boundary/scalar-silence theorem work', 'DEFERRED_WITH_TARGET', 'do not loop on trace declaration', 'not assumed')]
SHORTCUTS = [('X1: summary as safety theorem', 'write the group summary as if safety were proven', 'Group 52 only load-tested burdens'), ('X2: summary as insertion', 'use audit survival to license B_s/F_zeta insertion', 'physical use remains blocked'), ('X3: witnesses as total rejection', 'kill the conditional candidate because diagnostic obstructions exist', 'candidate can remain audit material'), ('X4: summary as active O necessity', 'jump straight to active O construction', 'O necessity requires its own audit')]
OBLIGATIONS = [('O1: write result notes from actual output', 'POLICY_RULE', 'each result note should state what changed, what failed, and what remains open', 'avoid stdout receipts'), ('O2: write group summary carefully', 'POLICY_RULE', 'summary must preserve audit-only survival, blocked physical use, and named safety burdens', 'avoid status inflation'), ('O3: update field-equation snapshot', 'DEFERRED_WITH_TARGET', 'snapshot should say safety burdens were sharpened but parent equation remains not ready', 'avoid fake field-equation progress')]
LOCAL_CONCLUSIONS = [('safety batch reconciled', 'PASS', 'Group 52 load-testing batch is ready for result notes and summary'), ('parent route still closed', 'NOT_INSERTABLE', 'no insertion, active O, recombination, or parent closure opened')]


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
