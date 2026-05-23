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
        "CONVENTION_FIELD_AUDIT": StatusMark.INFO,
        "CONVENTION_FIELDS_CLOSED_FOR_REVIEW": StatusMark.INFO,
        "CLOSED_FOR_REVIEW": StatusMark.INFO,
        "FIELD_CLASSIFIED": StatusMark.INFO,
        "ZETA_CONVENTION": StatusMark.INFO,
        "DIMENSION_FIELD": StatusMark.INFO,
        "NORMALIZATION_SCOPE": StatusMark.INFO,
        "SHARED_FIELD": StatusMark.INFO,
        "BRANCH_INDEXED": StatusMark.INFO,
        "REVIEW_READY": StatusMark.INFO,
        "REVIEW_READY_ONLY": StatusMark.INFO,
        "CONTEXT_ONLY": StatusMark.INFO,
        "CONDITIONAL": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "DEFER": StatusMark.DEFER,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "CONVENTION_BLOCKED": StatusMark.DEFER,
        "AXIOM_REQUIRED": StatusMark.DEFER,
        "CHOICE_REQUIRED": StatusMark.DEFER,
        "THEOREM_REQUIRED": StatusMark.DEFER,
        "NOT_DECLARED": StatusMark.DEFER,
        "NOT_CHOSEN": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "CONSISTENCY_RULE": StatusMark.OBLIGATION,
        "SCOPE_REQUIRED": StatusMark.OBLIGATION,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "BLOCKED": StatusMark.FAIL,
    }.get(status, StatusMark.INFO)


def obligation_status(status: str) -> ObligationStatus:
    if status in {"NOT_READY", "NOT_DECLARED", "NOT_CHOSEN", "NOT_ADOPTED", "NOT_DERIVED", "DEFERRED_WITH_TARGET", "CONVENTION_BLOCKED"}:
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
    if status in {"BLOCKED", "FORBIDDEN_SHORTCUT"}:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {"AXIOM_REQUIRED", "CHOICE_REQUIRED", "THEOREM_REQUIRED", "NOT_READY", "NOT_DECLARED", "CONVENTION_BLOCKED", "DEFERRED_WITH_TARGET"}:
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
#   46_parallel_trace_convention_field_closure_audit
# Script type:
#   AUDIT / CONVENTION-FIELD / PRE-DECLARATION

SCRIPT_LABEL = 'Candidate Convention Field Closure Batch Reconciliation'
MARKER_ID = 'g46_recon'
DEPENDENCIES = [('g45_summary', '45_explicit_parallel_trace_normalization_record__candidate_group_45_status_summary', 'g45_summary'), ('g46_problem', '46_parallel_trace_convention_field_closure_audit__candidate_convention_field_closure_problem', 'g46_problem'), ('g46_zeta_convention', '46_parallel_trace_convention_field_closure_audit__candidate_zeta_convention_field_audit', 'g46_zeta_convention'), ('g46_dimension_field', '46_parallel_trace_convention_field_closure_audit__candidate_traced_dimension_field_audit', 'g46_dimension_field'), ('g46_scope_field', '46_parallel_trace_convention_field_closure_audit__candidate_normalization_scope_field_audit', 'g46_scope_field'), ('g46_pair_consistency', '46_parallel_trace_convention_field_closure_audit__candidate_branch_pair_convention_consistency_sieve', 'g46_pair_consistency'), ('g46_route_classifier', '46_parallel_trace_convention_field_closure_audit__candidate_convention_closure_route_classifier', 'g46_route_classifier')]


def build_entries() -> List[Entry]:
    return [
        Entry('Q1: opener expectation', 'Group 46 opened as convention-field closure audit', 'MATCHED_EXPECTATION', 'expected if field closure/classification was allowed but branch choice and declaration were forbidden', 'summary may call this convention-field audit only'),
        Entry('Q2: zeta convention expectation', 'zeta convention was closed for record review only', 'MATCHED_EXPECTATION', 'expected if zeta remained shared, trace-payload, and non-insertable', 'summary must preserve zeta not active'),
        Entry('Q3: dimension expectation', 'symbolic d was closed for review while numeric d stayed scope-dependent', 'MATCHED_EXPECTATION', 'expected if d did not erase factor-of-two burden', 'summary must preserve no numeric declaration'),
        Entry('Q4: scope expectation', 'record-review scope was allowed but declaration/parent-facing scope remained blocked', 'MATCHED_EXPECTATION', 'expected if scope is the main remaining convention blocker', 'summary must preserve declaration blocked'),
        Entry('Q5: pair consistency expectation', 'parallel records remained consistent for review and noncollapsed', 'MATCHED_EXPECTATION', 'expected if labels and expressions stayed separated', 'summary must preserve not one neutral law'),
        Entry('Q6: route classifier expectation', 'batch ended with review-ready-only and deferred-with-target status', 'MATCHED_EXPECTATION', 'expected if next target is scope closure, not declaration', 'summary must not claim declaration readiness'),
        Entry('Q7: downstream gates', 'adoption, insertion, active O, residual control, recombination, and parent closure remain closed', 'NOT_READY', 'expected final boundary', 'summary must not open field-equation routes'),
    ]


def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: reconciliation as final summary', 'treat this script as group close', 'final summary should be written after actual outputs are reviewed'),
        Shortcut('X2: review-ready as declaration-ready', 'say convention fields are closed enough for trace declaration', 'scope blocker remains'),
        Shortcut('X3: zeta/d closure as branch choice', 'let shared zeta or d choose metric or scale branch', 'shared fields are for comparison only'),
        Shortcut('X4: scope blocker ignored', 'proceed to declaration without explicit scope closure', 'declaration scope remains targeted blocker'),
        Shortcut('X5: field audit as insertion', 'open B_s/F_zeta insertion or parent route from field clarity', 'downstream gates remain closed'),
    ]


def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: summary must follow actual outputs', 'OPEN', 'final summary must report mismatches if any script did not match expected boundary', 'actual outputs control close'),
        ObligationEntry('O2: preserve review-ready-only status', 'REVIEW_READY_ONLY', 'final summary must distinguish review-ready from declaration-ready', 'avoid status inflation'),
        ObligationEntry('O3: preserve scope blocker', 'CONVENTION_BLOCKED', 'final summary must name declaration scope as the remaining convention target', 'avoid vague not-ready'),
        ObligationEntry('O4: preserve downstream locks', 'NOT_READY', 'insertion, active O, residual control, recombination, and parent closure remain closed', 'avoid field-equation overreach'),
    ]


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print('Did the Group 46 batch close or sharply classify the convention fields without choosing a branch or declaring trace normalization?')
    print("\nDiscipline:\n")
    print('This script reconciles the Group 46 batch. It does not close the group as final summary.')
    print('It must preserve review-ready-only status and the declared scope blocker if the actual outputs match expectation.')
    with out.governance_assessments():
        out.line(
            f"{SCRIPT_LABEL} opened",
            StatusMark.PASS,
            "Group 46 convention-field audit only; no branch choice, trace declaration, adoption, insertion, active O, recombination, or parent route",
        )


def case_1(out: ScriptOutput, entries: List[Entry]) -> None:
    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")


def case_2(out: ScriptOutput, shortcuts: List[Shortcut]) -> None:
    print_shortcuts(out, shortcuts)


def case_3(out: ScriptOutput, obligations: List[ObligationEntry]) -> None:
    print_obligations(out, obligations)


def case_4(out: ScriptOutput) -> None:
    header("Local conclusions")
    conclusions = [
        ('batch reconciliation prepared', 'PASS', 'write summary only after actual outputs are reviewed'),
        ('no group close here', 'DEFERRED_WITH_TARGET', 'candidate_group_46_status_summary.py should name scope closure as next target if outputs match'),
    ]
    with out.governance_assessments():
        for name, status, detail in conclusions:
            out.line(name, mark(status), detail)
    print("\nPossible next script:")
    print("  candidate_group_46_status_summary.py")


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

    record_governance(ns, MARKER_ID, entries, obligations, 'Group 46 parallel trace convention-field closure audit')
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
