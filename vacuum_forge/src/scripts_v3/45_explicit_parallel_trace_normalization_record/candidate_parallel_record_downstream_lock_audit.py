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

SCRIPT_LABEL = 'Candidate Parallel Record Downstream Lock Audit'
MARKER_ID = 'g45_downstream_lock'
DEPENDENCIES = [('g44_summary', '44_trace_normalization_selector_context_audit__candidate_group_44_status_summary', 'g44_summary'), ('g45_decl_boundary', '45_explicit_parallel_trace_normalization_record__candidate_parallel_record_declaration_boundary', 'g45_decl_boundary')]

def build_entries() -> List[Entry]:
    return [
        Entry('L1: insertion lock', 'B_s/F_zeta insertion remains not ready', 'NOT_READY', 'record candidates are not insertion laws', 'no recombination use'),
        Entry('L2: active O lock', 'active O remains not constructed', 'NOT_READY', 'parallel records do not define projector domain/codomain/kernel/image', 'no no-overlap operator'),
        Entry('L3: residual-control lock', 'residual nonentry or kill remains not derived', 'NOT_DERIVED', 'record clarity does not control zeta/kappa residuals', 'no residual theorem'),
        Entry('L4: source-routing lock', 'source no-double-counting remains not derived', 'NOT_DERIVED', 'records cannot protect A-sector mass by themselves', 'no source theorem'),
        Entry('L5: boundary/divergence lock', 'boundary neutrality and parent identity remain missing', 'NOT_DERIVED', 'records do not solve support, scalar silence, or divergence', 'no parent identity'),
        Entry('L6: adoption lock', 'Package B adoption remains separate', 'NOT_ADOPTED', 'parallel trace records do not adopt the trace-anchor package', 'explicit adoption decision required'),
    ]

def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: records as insertion law', 'use explicit records to insert B_s/F_zeta', 'candidate records are not recombination equations'),
        Shortcut('X2: records as active O', 'treat parallel labels as no-overlap operator', 'labels are not projectors'),
        Shortcut('X3: records as residual control', 'claim record clarity kills residuals', 'residual theorem remains separate'),
        Shortcut('X4: records as source protection', 'claim parallel records prove no source double-counting', 'source theorem remains separate'),
        Shortcut('X5: records as parent readiness', 'open recombination or parent closure from record clarity', 'parent gates remain closed'),
    ]

def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: keep insertion closed', 'NOT_READY', 'do not insert B_s/F_zeta from record candidates', 'avoid premature recombination'),
        ObligationEntry('O2: keep active O closed', 'NOT_READY', 'do not treat labels as active projectors', 'avoid O-by-name'),
        ObligationEntry('O3: keep residual/source theorems separate', 'NOT_DERIVED', 'records do not prove residual or source safety', 'avoid theorem drift'),
        ObligationEntry('O4: keep parent closure closed', 'NOT_READY', 'do not open parent equation from record clarity', 'avoid field-equation overreach'),
    ]


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print('Which downstream routes remain locked even after explicit parallel trace-normalization records are')
    print('available?')
    print("\nDiscipline:\n")
    print('This script audits downstream locks after the parallel records are made explicit. It prevents')
    print('record clarity from being misread as insertion, active O, residual control, recombination, or')
    print('parent readiness.')
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
    conclusions = [('downstream lock audit complete', 'PASS', 'parallel records do not open downstream gates'), ('insertion remains not ready', 'NOT_READY', 'B_s/F_zeta insertion and parent closure remain closed')]
    with out.governance_assessments():
        for name, status, detail in conclusions:
            out.line(name, mark(status), detail)
    print("\nPossible next script:")
    print("  candidate_parallel_trace_record_batch_reconciliation.py")


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

    record_governance(ns, MARKER_ID, entries, obligations, 'Group 45 downstream lock audit')
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
