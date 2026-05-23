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

SCRIPT_LABEL = 'Candidate Zeta Convention Field Audit'
MARKER_ID = 'g46_zeta_convention'
DEPENDENCIES = [('g45_summary', '045_explicit_parallel_trace_normalization_record__candidate_group_45_status_summary', 'g45_summary'), ('g45_metric_record', '045_explicit_parallel_trace_normalization_record__candidate_metric_trace_record_schema', 'g45_metric_record'), ('g45_scale_record', '045_explicit_parallel_trace_normalization_record__candidate_scale_trace_record_schema', 'g45_scale_record'), ('g46_problem', '046_parallel_trace_convention_field_closure_audit__candidate_convention_field_closure_problem', 'g46_problem')]


def build_entries() -> List[Entry]:
    return [
        Entry('Z1: record-local zeta symbol', 'zeta may be treated as the shared trace-payload symbol inside both record schemas', 'CLOSED_FOR_REVIEW', 'for record review, zeta can name the same trace payload in both candidate expressions', 'not a parent field or declaration by itself'),
        Entry('Z2: volume/log-density interpretation', 'volume or log-density intuition may be retained as interpretation context', 'CONTEXT_ONLY', 'the interpretation helps explain why zeta is the trace handle under review', 'intuition is not theorem proof'),
        Entry('Z3: branch-shared convention', 'the same zeta convention should be shared unless later evidence forces branch-indexed zeta variants', 'SHARED_FIELD', 'shared zeta prevents metric and scale records from silently describing different payloads', 'shared does not collapse the factor-of-two expressions'),
        Entry('Z4: branch-indexed zeta fallback', 'zeta_metric and zeta_scale variants would be required if payload meaning diverges by branch', 'DEFERRED_WITH_TARGET', 'branch-indexed variants are a fallback blocker classification, not a current choice', 'variants would still be non-active'),
        Entry('Z5: forbidden zeta roles', 'zeta is not F_zeta, not B_s/F_zeta insertion, not residual kill, and not active O', 'POLICY_RULE', 'zeta convention must not absorb downstream or projector roles', 'role purity remains mandatory'),
    ]


def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: zeta as F_zeta', 'treat zeta convention as defining neutral F_zeta response', 'zeta payload and response placeholder remain separate'),
        Shortcut('X2: zeta by recovery', 'choose zeta meaning because it best recovers AB=1 or Schwarzschild', 'recovery cannot set convention fields'),
        Shortcut('X3: mismatched zeta meanings', 'let metric and scale records use different zeta meanings without labels', 'that creates hidden branch asymmetry'),
        Shortcut('X4: zeta as residual control', 'claim zeta convention kills residual zeta/kappa load', 'residual theorem remains separate'),
    ]


def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: preserve shared zeta for review', 'CLOSED_FOR_REVIEW', 'carry one record-local zeta payload convention across both candidate records for review', 'avoid hidden branch mismatch'),
        ObligationEntry('O2: label any future zeta divergence', 'DEFERRED_WITH_TARGET', 'if later work needs branch-specific zeta meanings, introduce explicit zeta_metric and zeta_scale fields', 'avoid silent convention split'),
        ObligationEntry('O3: keep zeta non-insertable', 'NOT_READY', 'do not use zeta convention to license B_s/F_zeta insertion', 'avoid recombination drift'),
    ]


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print('What must zeta mean inside both explicit parallel trace-normalization records?')
    print("\nDiscipline:\n")
    print('This script audits the zeta convention field shared by the metric and scale trace records.')
    print('It may close zeta for record review as a shared trace payload symbol, but cannot make zeta an active field, response map, or insertion law.')
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
        ('zeta convention classified', 'CLOSED_FOR_REVIEW', 'zeta can be shared for record review as a trace payload symbol'),
        ('zeta not active', 'NOT_READY', 'zeta convention does not supply response, residual control, insertion, or parent support'),
    ]
    with out.governance_assessments():
        for name, status, detail in conclusions:
            out.line(name, mark(status), detail)
    print("\nPossible next script:")
    print("  candidate_traced_dimension_field_audit.py")


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
