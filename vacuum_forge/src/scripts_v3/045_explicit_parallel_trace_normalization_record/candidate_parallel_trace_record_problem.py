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

SCRIPT_LABEL = 'Candidate Parallel Trace Record Problem'
MARKER_ID = 'g45_problem'
DEPENDENCIES = [('g44_summary', '044_trace_normalization_selector_context_audit__candidate_group_44_status_summary', 'g44_summary'), ('g43_summary', '043_trace_normalization_branch_or_parallel_decision_surface__candidate_group_43_status_summary', 'g43_summary'), ('g42_summary', '042_trace_anchor_equation_choice_exclusion_map__candidate_group_42_status_summary', 'g42_summary')]

def build_entries() -> List[Entry]:
    return [
        Entry('P1: parallel-record route', 'two explicit branch-indexed trace-normalization records', 'PARALLEL_RECORD_AUDIT', 'Group 45 may define record surfaces for metric and scale candidates in parallel', 'route is visibility infrastructure, not active declaration'),
        Entry('P2: metric record candidate', 'metric-coefficient record candidate', 'METRIC_RECORD_CANDIDATE', 'metric record may carry log(B_s_metric)=2*zeta/d with explicit non-active status', 'not chosen and not inserted'),
        Entry('P3: scale record candidate', 'scale-factor record candidate', 'SCALE_RECORD_CANDIDATE', 'scale record may carry log(b_s_scale)=zeta/d with explicit non-active status', 'not chosen and not inserted'),
        Entry('P4: factor-of-two visibility', 'factor-of-two burden remains visible', 'POLICY_RULE', 'parallel records keep zeta/d and 2*zeta/d separated', 'not one neutral law'),
        Entry('P5: downstream locks', 'adoption, insertion, active O, residual control, recombination, and parent closure', 'NOT_READY', 'parallel record work cannot open downstream field-equation routes', 'record clarity is not field-equation use'),
    ]

def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: parallel as branch choice', 'treat carrying both records as choosing both branches', 'parallel records are non-active candidates'),
        Shortcut('X2: parallel as declaration', 'treat record schemas as completed trace-normalization declaration', 'schema visibility is not declaration closure'),
        Shortcut('X3: parallel as neutral law', 'merge the two expressions under unqualified B_s or neutral F_zeta', 'that hides the factor-of-two burden'),
        Shortcut('X4: parallel as insertion', 'insert either record into B_s/F_zeta', 'insertion remains downstream and not ready'),
    ]

def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: preserve non-active status', 'NOT_DECLARED', 'mark both records as candidate / non-active', 'avoid accidental declaration'),
        ObligationEntry('O2: preserve branch labels', 'POLICY_RULE', 'use B_s_metric and b_s_scale labels wherever branch matters', 'avoid overload reentry'),
        ObligationEntry('O3: preserve expression separation', 'POLICY_RULE', 'keep 2*zeta/d and zeta/d in separate record candidates', 'avoid neutral-expression smuggling'),
        ObligationEntry('O4: preserve downstream locks', 'NOT_READY', 'keep adoption, insertion, active O, residual control, recombination, and parent closure closed', 'avoid field-equation overreach'),
    ]


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print('What exactly can Group 45 record if it follows the explicit parallel trace-normalization route')
    print('instead of choosing B_s_metric or b_s_scale?')
    print("\nDiscipline:\n")
    print('This script opens Group 45 as an explicit parallel trace-normalization record audit. It makes the')
    print('two branch-indexed record surfaces concrete, but does not choose a branch, collapse the records')
    print('into one neutral law, complete trace normalization, adopt Package B, or license insertion.')
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
    conclusions = [('Group 45 opener complete', 'PASS', 'parallel trace-normalization record audit opened'), ('no branch chosen', 'NOT_CHOSEN', 'metric and scale branches remain non-active')]
    with out.governance_assessments():
        for name, status, detail in conclusions:
            out.line(name, mark(status), detail)
    print("\nPossible next script:")
    print("  candidate_metric_trace_record_schema.py")


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

    record_governance(ns, MARKER_ID, entries, obligations, 'Group 45 explicit parallel trace-normalization record audit')
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
