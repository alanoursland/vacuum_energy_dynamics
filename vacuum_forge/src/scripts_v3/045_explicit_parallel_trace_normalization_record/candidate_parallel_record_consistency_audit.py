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

SCRIPT_LABEL = 'Candidate Parallel Record Consistency Audit'
MARKER_ID = 'g45_consistency'
DEPENDENCIES = [('g44_summary', '44_trace_normalization_selector_context_audit__candidate_group_44_status_summary', 'g44_summary'), ('g45_metric_record', '45_explicit_parallel_trace_normalization_record__candidate_metric_trace_record_schema', 'g45_metric_record'), ('g45_scale_record', '45_explicit_parallel_trace_normalization_record__candidate_scale_trace_record_schema', 'g45_scale_record')]

def build_entries() -> List[Entry]:
    return [
        Entry('C1: paired record identities', 'metric and scale records are paired as parallel candidates', 'PARALLEL_RECORD_CANDIDATE', 'records are compared as a pair', 'not a joint active declaration'),
        Entry('C2: label consistency', 'B_s_metric and b_s_scale labels remain explicit', 'CONSISTENCY_RULE', 'branch labels prevent overload reentry', 'not optional where branch matters'),
        Entry('C3: expression separation', '2*zeta/d and zeta/d remain separated', 'CONSISTENCY_RULE', 'factor-of-two burden stays visible', 'not neutral F_zeta'),
        Entry('C4: shared convention fields', 'zeta convention, dimension d, and scope fields are parallel', 'OPEN', 'shared fields expose what later declaration would need', 'not closed here'),
        Entry('C5: status alignment', 'both records remain non-active candidates', 'POLICY_RULE', 'neither record becomes active through pairing', 'not chosen'),
        Entry('C6: no downstream asymmetry', 'neither record gets insertion privilege', 'NOT_READY', 'insertion remains locked for both records', 'no branch-specific shortcut'),
    ]

def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: paired as declared', 'treat paired records as completed trace normalization', 'pairing is not declaration'),
        Shortcut('X2: labels dropped', 'use unqualified B_s in handoff where branch matters', 'that reintroduces overload'),
        Shortcut('X3: expression averaged', 'combine zeta/d and 2*zeta/d into a compromise law', 'that creates an unsupported third law'),
        Shortcut('X4: one record quietly active', 'let one side become active because it looks easier', 'hidden branch choice is forbidden'),
    ]

def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: preserve pair labels', 'POLICY_RULE', 'carry B_s_metric and b_s_scale explicitly in handoffs', 'avoid overloaded B_s'),
        ObligationEntry('O2: preserve factor-of-two visibility', 'POLICY_RULE', 'keep branch expressions separated', 'avoid neutral-expression smuggling'),
        ObligationEntry('O3: preserve shared convention gaps', 'OPEN', 'track zeta, d, and scope gaps on both records', 'avoid false declaration support'),
        ObligationEntry('O4: preserve equal non-insertability', 'NOT_READY', 'do not allow either record to insert B_s/F_zeta', 'avoid asymmetric downstream drift'),
    ]


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print('Do the metric and scale trace-normalization record schemas remain explicitly parallel without')
    print('collapsing into a hidden branch choice?')
    print("\nDiscipline:\n")
    print('This script audits consistency between the two non-active record schemas. It keeps the records')
    print('paired, labeled, and expression-separated without treating them as one law.')
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
    conclusions = [('parallel consistency audit complete', 'PASS', 'metric and scale records remain paired and non-active'), ('records not collapsed', 'POLICY_RULE', 'no neutral law or unqualified B_s law is created')]
    with out.governance_assessments():
        for name, status, detail in conclusions:
            out.line(name, mark(status), detail)
    print("\nPossible next script:")
    print("  candidate_parallel_record_declaration_boundary.py")


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

    record_governance(ns, MARKER_ID, entries, obligations, 'Group 45 parallel trace-normalization record consistency audit')
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
