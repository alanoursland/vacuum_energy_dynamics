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
        "EQUATION_CHOICE_EXCLUSION_MAP": StatusMark.INFO,
        "EQUATION_SPACE_NARROWED": StatusMark.PASS,
        "CONDITIONAL_CANDIDATE": StatusMark.DEFER,
        "AXIOM_REQUIRED": StatusMark.DEFER,
        "PRECONDITION_ONLY": StatusMark.INFO,
        "COMPATIBLE_IF_DECLARED": StatusMark.INFO,
        "DIAGNOSTIC_ONLY": StatusMark.INFO,
        "BRANCH_INDEXED": StatusMark.INFO,
        "NOT_WELL_POSED": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "DEFER": StatusMark.DEFER,
        "DECLARATION_DEFERRED": StatusMark.DEFER,
        "NOT_DECLARED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NO_EQUATION_CHOSEN": StatusMark.DEFER,
        "NO_ADOPTION": StatusMark.DEFER,
        "NO_INSERTION": StatusMark.DEFER,
        "PARENT_NOT_READY": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "FORBIDDEN_BY_GUARDRAIL": StatusMark.FAIL,
        "ELIMINATED": StatusMark.FAIL,
        "DEMOTED_TO_DIAGNOSTIC": StatusMark.INFO,
        "RECOVERY_SELECTOR_REJECTED": StatusMark.FAIL,
        "REPAIR_TOOL_REJECTED": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
    }.get(status, StatusMark.INFO)


def _governance(name: str, fallback=None):
    if fallback is None:
        fallback = GovernanceStatus.POLICY_RULE
    return getattr(GovernanceStatus, name, fallback)


def governance_status_for(status: str):
    info_status = _governance("HEURISTIC")
    deferred_status = _governance("DEFERRED_PENDING_PREREQUISITES", _governance("DEFERRED"))
    candidate_status = _governance("CANDIDATE_ROUTE", info_status)
    policy_status = GovernanceStatus.POLICY_RULE
    rejected_status = _governance("REJECTED", policy_status)

    return {
        "PASS": info_status,
        "MATCHED_EXPECTATION": info_status,
        "EQUATION_CHOICE_EXCLUSION_MAP": info_status,
        "EQUATION_SPACE_NARROWED": info_status,
        "CONDITIONAL_CANDIDATE": candidate_status,
        "AXIOM_REQUIRED": deferred_status,
        "PRECONDITION_ONLY": info_status,
        "COMPATIBLE_IF_DECLARED": candidate_status,
        "DIAGNOSTIC_ONLY": info_status,
        "BRANCH_INDEXED": info_status,
        "NOT_WELL_POSED": deferred_status,
        "OPEN": deferred_status,
        "DEFER": deferred_status,
        "DECLARATION_DEFERRED": deferred_status,
        "NOT_DECLARED": deferred_status,
        "NOT_DERIVED": deferred_status,
        "NOT_READY": deferred_status,
        "NOT_ADOPTED": deferred_status,
        "NO_EQUATION_CHOSEN": deferred_status,
        "NO_ADOPTION": deferred_status,
        "NO_INSERTION": deferred_status,
        "PARENT_NOT_READY": deferred_status,
        "POLICY_RULE": policy_status,
        "FORBIDDEN_BY_GUARDRAIL": rejected_status,
        "ELIMINATED": rejected_status,
        "DEMOTED_TO_DIAGNOSTIC": info_status,
        "RECOVERY_SELECTOR_REJECTED": rejected_status,
        "REPAIR_TOOL_REJECTED": rejected_status,
        "FORBIDDEN_SHORTCUT": policy_status,
    }.get(status, info_status)


def obligation_status(status: str) -> ObligationStatus:
    if status in {
        "AXIOM_REQUIRED",
        "CONDITIONAL_CANDIDATE",
        "NOT_WELL_POSED",
        "OPEN",
        "DEFER",
        "DECLARATION_DEFERRED",
        "NOT_DECLARED",
        "NOT_DERIVED",
        "NOT_READY",
        "NOT_ADOPTED",
        "NO_EQUATION_CHOSEN",
        "NO_ADOPTION",
        "NO_INSERTION",
        "PARENT_NOT_READY",
    }:
        return getattr(ObligationStatus, "DEFERRED", ObligationStatus.OPEN)
    return ObligationStatus.OPEN

# Group:
#   42_trace_anchor_equation_choice_exclusion_map
# Script type:
#   AUDIT / EXCLUSION MAP

SCRIPT_LABEL = 'Candidate Equation Choice Exclusion Batch Reconciliation'
MARKER_ID = 'g42_recon'
GROUP_SCOPE = 'Group 42 trace-anchor equation choice exclusion map'
DEPENDENCIES = [('g41_summary', '041_safe_membership_precondition_continuation__candidate_group_41_status_summary', 'g41_summary'), ('g42_problem', '042_trace_anchor_equation_choice_exclusion_map__candidate_equation_choice_exclusion_problem', 'g42_problem'), ('g42_trace_norm_sieve', '042_trace_anchor_equation_choice_exclusion_map__candidate_trace_normalization_equation_family_sieve', 'g42_trace_norm_sieve'), ('g42_membership_sieve', '042_trace_anchor_equation_choice_exclusion_map__candidate_safe_membership_relation_family_sieve', 'g42_membership_sieve'), ('g42_spatial_response', '042_trace_anchor_equation_choice_exclusion_map__candidate_spatial_response_equation_family_sieve', 'g42_spatial_response'), ('g42_residual_source', '042_trace_anchor_equation_choice_exclusion_map__candidate_residual_source_equation_elimination_audit', 'g42_residual_source'), ('g42_boundary_div', '042_trace_anchor_equation_choice_exclusion_map__candidate_boundary_divergence_equation_elimination_audit', 'g42_boundary_div')]
QUESTION = 'Did the Group 42 batch produce the expected equation-choice exclusion map shape, and what should a later status summary preserve?'
DISCIPLINE = 'This script reconciles the Group 42 batch. It does not close the group as final summary and does not choose, adopt, derive, declare, insert, or open parent closure.'
OPENING_DETAIL = 'batch reconciliation only; no final summary, no equation selection, and no downstream route'
CASE1_TITLE = 'Case 1: Batch reconciliation entries'
NEXT_SCRIPT = 'candidate_group_42_status_summary.py'
CONCLUSIONS = [('batch reconciliation prepared', 'PASS', 'write summary only after actual outputs are reviewed'), ('no group close here', 'DEFER', 'candidate_group_42_status_summary.py should be written after review')]


def build_entries() -> List[Entry]:
    return [
        Entry('Q1: opener expectation', 'Group 42 opened as an equation-choice exclusion audit', 'MATCHED_EXPECTATION', 'expected if equation elimination was allowed and equation selection was forbidden', 'summary may call this equation-space narrowing only'),
        Entry('Q2: trace-normalization expectation', 'trace-normalization families were separated into branch-indexed candidates and forbidden hidden-choice forms', 'MATCHED_EXPECTATION', 'expected if no branch or normalization was selected', 'summary must preserve no trace declaration'),
        Entry('Q3: safe-membership expectation', 'membership relation families were separated into diagnostic, compatible-if-declared, future-route, and forbidden shortcut classes', 'MATCHED_EXPECTATION', 'expected if active membership was not installed', 'summary must preserve compatible-if-declared boundary'),
        Entry('Q4: spatial-response expectation', 'recovery-selected, hidden-expression, mass-duplicating, scalar-tail, and not-well-posed spatial-response families were eliminated or demoted', 'MATCHED_EXPECTATION', 'expected if B_s/F_zeta insertion remains not ready', 'summary must preserve no insertion'),
        Entry('Q5: residual/source expectation', 'residual/source hiding equation families were eliminated or demoted', 'MATCHED_EXPECTATION', 'expected if residual nonentry and source no-double-counting remain theorem targets', 'summary must not claim those theorems'),
        Entry('Q6: boundary/divergence expectation', 'boundary repair, scalar-tail filter, divergence patch, and early-parent families were eliminated or demoted', 'MATCHED_EXPECTATION', 'expected if boundary neutrality and parent identity remain open', 'summary must preserve parent not ready'),
        Entry('Q7: surviving candidate menu', 'surviving families are conditional candidates or axiom-required future routes', 'AXIOM_REQUIRED', 'expected if future axiom choices are visible but not adopted', 'summary must not treat axiom need as adoption'),
        Entry('Q8: downstream gates', 'Package B adoption, B_s/F_zeta insertion, active O, residual control, recombination, and parent closure remain closed', 'NOT_READY', 'expected final boundary', 'summary must not open field-equation routes'),
    ]


def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: reconciliation as final summary', 'treat this script as group close', 'final summary should be written after actual outputs are reviewed'),
        Shortcut('X2: elimination as selection', 'treat narrowed candidate menu as equation choice', 'elimination only narrows the space'),
        Shortcut('X3: axiom-required as adopted', 'treat axiom-required candidates as adopted axioms', 'axiom adoption requires separate explicit decision'),
        Shortcut('X4: candidates as insertion', 'use surviving spatial-response candidates to insert B_s/F_zeta', 'insertion remains not ready'),
        Shortcut('X5: repair eliminations as solved theorems', 'treat eliminated bad repair routes as proof of residual/source/boundary/divergence safety', 'positive theorem support remains separate'),
        Shortcut('X6: readiness as parent readiness', 'open parent closure from equation-space narrowing', 'parent identity remains missing'),
    ]


def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: summary must follow actual outputs', 'OPEN', 'final summary must report any mismatch in batch outputs', 'actual outputs control close'),
        ObligationEntry('O2: preserve no equation chosen', 'NO_EQUATION_CHOSEN', 'final summary must say no equation was selected, declared, adopted, or derived', 'avoid selection by summary prose'),
        ObligationEntry('O3: preserve axiom-required status', 'AXIOM_REQUIRED', 'future axiom candidates must remain future choices', 'avoid hidden postulates'),
        ObligationEntry('O4: preserve downstream locks', 'NOT_READY', 'adoption, insertion, active O, residual control, recombination, and parent closure remain closed', 'avoid field-equation overreach'),
    ]


def record_marker(ns, marker_id: str, symbol_name: str) -> None:
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[],
        output=sp.Symbol(symbol_name),
        method="inventory marker; no physical derivation",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
        scope=GROUP_SCOPE,
    )


def record_claim(ns, claim_id: str, marker_id: str, status: str, statement: str) -> None:
    ns.record_claim(
        ClaimRecord(
            claim_id=claim_id,
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=governance_status_for(status),
            statement=statement,
            derivation_ids=[marker_id],
            obligation_ids=[],
        )
    )


def record_obligation(ns, obligation_id: str, title: str, description: str, status: str = "OPEN") -> None:
    ns.record_obligation(
        ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=obligation_status(status),
            required_by=[SCRIPT_ID],
            description=description,
        )
    )


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


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    for line in QUESTION.splitlines():
        print("  " + line if line else "")
    print("\nDiscipline:\n")
    for line in DISCIPLINE.splitlines():
        print("  " + line if line else "")
    with out.governance_assessments():
        out.line(
            f"{SCRIPT_LABEL} opened",
            StatusMark.PASS,
            OPENING_DETAIL,
        )


def case_1(out: ScriptOutput, entries: List[Entry]) -> None:
    header(CASE1_TITLE)
    for item in entries:
        subheader(item.name)
        print(f"Subject: {item.subject}")
        print(f"Detail: {item.detail}")
        print(f"Boundary: {item.boundary}")
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.detail}. Boundary: {item.boundary}")


def case_2(out: ScriptOutput, shortcuts: List[Shortcut]) -> None:
    header("Case 2: Invalid upgrades and forbidden shortcuts")
    for item in shortcuts:
        subheader(item.name)
        print(f"Shortcut: {item.shortcut}")
        with out.counterexamples():
            out.line(item.name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {item.reason}")


def case_3(out: ScriptOutput, obligations: List[ObligationEntry]) -> None:
    header("Case 3: Open obligations")
    for item in obligations:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        with out.unresolved_obligations():
            out.line(item.name, mark(item.status), f"{item.status}: {item.obligation}; discipline: {item.discipline}")


def case_4(out: ScriptOutput) -> None:
    header("Case 4: Local conclusions")
    with out.governance_assessments():
        for name, status, detail in CONCLUSIONS:
            out.line(name, mark(status), detail)
    print("\nPossible next script:")
    print("  " + NEXT_SCRIPT)


def record_governance(ns, entries: List[Entry], shortcuts: List[Shortcut], obligations: List[ObligationEntry]) -> None:
    record_marker(ns, MARKER_ID, MARKER_ID)
    for idx, item in enumerate(entries, 1):
        record_claim(
            ns,
            f"{MARKER_ID}_c{idx}",
            MARKER_ID,
            item.status,
            f"{item.name}: {item.subject}. {item.detail}. Boundary: {item.boundary}.",
        )
    for idx, item in enumerate(shortcuts, 1):
        record_claim(
            ns,
            f"{MARKER_ID}_x{idx}",
            MARKER_ID,
            "FORBIDDEN_SHORTCUT",
            f"{item.name}: {item.shortcut}. Rejected because {item.reason}.",
        )
    for idx, item in enumerate(obligations, 1):
        record_obligation(
            ns,
            f"{MARKER_ID}_o{idx}",
            item.name,
            f"{item.obligation}. Discipline: {item.discipline}.",
            item.status,
        )


def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    entries = build_entries()
    shortcuts = build_shortcuts()
    obligations = build_obligations()
    case_0(out)
    case_1(out, entries)
    case_2(out, shortcuts)
    case_3(out, obligations)
    case_4(out)
    record_governance(ns, entries, shortcuts, obligations)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
