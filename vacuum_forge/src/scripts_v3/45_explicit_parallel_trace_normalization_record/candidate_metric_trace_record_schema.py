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
        "PARALLEL_RECORD_AUDIT": StatusMark.INFO,
        "PARALLEL_RECORD_CANDIDATE": StatusMark.INFO,
        "METRIC_RECORD_CANDIDATE": StatusMark.INFO,
        "SCALE_RECORD_CANDIDATE": StatusMark.INFO,
        "SCHEMA_FIELD": StatusMark.INFO,
        "CONDITIONAL": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "DEFER": StatusMark.DEFER,
        "NOT_DECLARED": StatusMark.DEFER,
        "NOT_CHOSEN": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "CONSISTENCY_RULE": StatusMark.OBLIGATION,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
    }.get(status, StatusMark.INFO)


def obligation_status(status: str) -> ObligationStatus:
    if status in {"NOT_READY", "NOT_DECLARED", "NOT_CHOSEN", "NOT_ADOPTED", "NOT_DERIVED"}:
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


def record_claim(ns, claim_id: str, marker_id: str, statement: str) -> None:
    ns.record_claim(
        ClaimRecord(
            claim_id=claim_id,
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.POLICY_RULE,
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
        record_claim(ns, f"{marker_id}_c{idx}", marker_id, f"{item.name}: {item.subject}. {item.detail}. Boundary: {item.boundary}.")
    for idx, item in enumerate(obligations, 1):
        record_obligation(ns, f"{marker_id}_o{idx}", item.name, f"{item.obligation}. Discipline: {item.discipline}.", item.status)

# Group:
#   45_explicit_parallel_trace_normalization_record
# Script type:
#   AUDIT / RECORD-SCHEMA / PRE-DECLARATION

SCRIPT_LABEL = 'Candidate Metric Trace Record Schema'
MARKER_ID = 'g45_metric_record'
DEPENDENCIES = [('g44_summary', '44_trace_normalization_selector_context_audit__candidate_group_44_status_summary', 'g44_summary'), ('g45_problem', '45_explicit_parallel_trace_normalization_record__candidate_parallel_trace_record_problem', 'g45_problem')]

def build_entries() -> List[Entry]:
    return [
        Entry('M1: record identity', 'metric trace-normalization record id', 'SCHEMA_FIELD', 'record explicitly identifies itself as a metric-coefficient branch candidate', 'not unqualified B_s'),
        Entry('M2: branch object', 'B_s_metric object field', 'SCHEMA_FIELD', 'record names B_s_metric as the branch object', 'object naming is not branch choice'),
        Entry('M3: candidate expression', 'log(B_s_metric)=2*zeta/d', 'METRIC_RECORD_CANDIDATE', 'candidate expression is carried only with non-active candidate status', 'not declaration'),
        Entry('M4: convention fields', 'zeta convention, traced dimension d, and normalization scope', 'OPEN', 'record reserves explicit fields for conventions still needed', 'fields are not closed here'),
        Entry('M5: status field', 'non-active / candidate / not chosen', 'POLICY_RULE', 'metric record reports its own non-active status', 'prevents accidental selection'),
        Entry('M6: downstream caveat field', 'not adoption, insertion, active O, recombination, or parent closure', 'NOT_READY', 'record carries downstream caveats', 'record is not recombination law'),
    ]

def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: metric record as choice', 'treat the metric schema as selecting B_s_metric', 'schema is not branch choice'),
        Shortcut('X2: metric expression as declaration', 'treat log(B_s_metric)=2*zeta/d as completed trace normalization', 'candidate expression is not declaration'),
        Shortcut('X3: missing convention fields', 'omit zeta convention, dimension, or scope while pretending declaration support exists', 'required fields remain open'),
        Shortcut('X4: metric record as insertion', 'use metric record directly in B_s/F_zeta insertion', 'insertion law remains separate'),
    ]

def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: define B_s_metric object scope', 'OPEN', 'state metric-coefficient object domain and scope before any future choice', 'avoid ambiguous metric record'),
        ObligationEntry('O2: state zeta and d conventions', 'OPEN', 'record zeta convention and traced dimension before declaration route', 'avoid hidden normalization'),
        ObligationEntry('O3: keep metric record non-active', 'NOT_CHOSEN', 'preserve candidate / not chosen status', 'avoid branch choice by schema'),
        ObligationEntry('O4: preserve insertion lock', 'NOT_READY', 'do not use metric record as B_s/F_zeta insertion support', 'avoid recombination drift'),
    ]


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print('What fields must the B_s_metric trace-normalization record contain if it is carried as a non-')
    print('active parallel candidate?')
    print("\nDiscipline:\n")
    print('This script defines the metric-side record schema only. It does not choose B_s_metric, complete')
    print('trace normalization, or make the metric record insertable.')
    with out.governance_assessments():
        out.line(
            f"{SCRIPT_LABEL} opened",
            StatusMark.PASS,
            "Group 45 parallel trace-normalization record work only; no branch choice, declaration completion, adoption, insertion, active O, recombination, or parent route",
        )


def case_1(out: ScriptOutput, entries: List[Entry]) -> None:
    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")


def case_2(out: ScriptOutput, shortcuts: List[Shortcut]) -> None:
    print_shortcuts(out, shortcuts)


def case_3(out: ScriptOutput, obligations: List[ObligationEntry]) -> None:
    print_obligations(out, obligations)


def case_4(out: ScriptOutput) -> None:
    header("Local conclusions")
    conclusions = [('metric trace record schema complete', 'PASS', 'metric-side record fields stated'), ('B_s_metric not chosen', 'NOT_CHOSEN', 'metric record remains non-active candidate only')]
    with out.governance_assessments():
        for name, status, detail in conclusions:
            out.line(name, mark(status), detail)
    print("\nPossible next script:")
    print("  candidate_scale_trace_record_schema.py")


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

    record_governance(ns, MARKER_ID, entries, obligations, 'Group 45 metric trace-normalization record schema')
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
