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

SCRIPT_LABEL = 'Candidate Blocker Dependency Graph'
MARKER_ID = 'g66_graph'
DEPENDENCIES = [('g65_summary', '065_transition_diagnostic_downgrade__candidate_group_65_status_summary', 'g65_summary'), ('g66_problem', '066_parent_blocker_inventory__candidate_parent_inventory_problem', 'g66_problem'), ('g66_recomb', '066_parent_blocker_inventory__candidate_recombination_prerequisite_sieve', 'g66_recomb')]
QUESTION = 'How do the remaining parent blockers depend on one another?'
DISCIPLINE = 'This script records the dependency shape that should guide the next groups.'
OPENING_LINE = 'Parent blocker dependency graph opened'
SCOPE = 'Group 66 blocker dependency graph'
NEXT_SCRIPT = 'candidate_next_route_priority.py'

ENTRIES = [('G1: parent dependency', 'parent equation depends on recombination rule', 'DEPENDENCY_GRAPH_RECORDED', 'parent construction is downstream', 'blocked'), ('G2: recombination dependencies', 'source/trace/divergence/covariance/boundary/O/trace decision', 'DEPENDENCY_GRAPH_RECORDED', 'recombination has multiple unsatisfied prerequisites', 'open'), ('G3: source/trace core', 'source count once and trace count once', 'SOURCE_TRACE_DIVERGENCE_TARGET', 'count-once theorems are central', 'open'), ('G4: diagnostics', 'boundary diagnostics feed boundary neutrality', 'DIAGNOSTIC_CONSTRAINT_RETAINED', 'diagnostics constrain but do not insert', 'diagnostic')]
SHORTCUTS = [('X1: parent before dependencies', 'write parent equation before dependencies', 'graph places parent downstream'), ('X2: use diagnostics as dependencies solved', 'treat diagnostic ledger as boundary theorem', 'diagnostics are constraints only')]
OBLIGATIONS = [('O1: route priority', 'POLICY_RULE', 'choose next group based on dependency graph', 'avoid looping')]
LOCAL_CONCLUSIONS = [('dependency graph recorded', 'DEPENDENCY_GRAPH_RECORDED', 'parent blockers organized by dependency'), ('parent still downstream', 'PARENT_EQUATION_BLOCKED', 'parent equation remains blocked')]


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
        "PARENT_INVENTORY_OPENED": StatusMark.INFO,
        "ARTIFACT_LEDGER_RECORDED": StatusMark.PASS,
        "BLOCKER_MATRIX_RECORDED": StatusMark.PASS,
        "RECOMBINATION_BLOCKED": StatusMark.DEFER,
        "PREREQUISITES_RECORDED": StatusMark.PASS,
        "DEPENDENCY_GRAPH_RECORDED": StatusMark.PASS,
        "NEXT_ROUTE_PRIORITIZED": StatusMark.INFO,
        "PARENT_EQUATION_BLOCKED": StatusMark.DEFER,
        "TRANSITION_NOT_PARENT_INGREDIENT": StatusMark.PASS,
        "DIAGNOSTIC_CONSTRAINT_RETAINED": StatusMark.PASS,
        "TRACE_NORMALIZATION_NOT_ADOPTED": StatusMark.DEFER,
        "ACTIVE_O_NOT_CONSTRUCTED": StatusMark.DEFER,
        "SOURCE_TRACE_DIVERGENCE_TARGET": StatusMark.OBLIGATION,
        "COVARIANT_LIFT_REQUIRED": StatusMark.OBLIGATION,
        "BOUNDARY_NEUTRALITY_REQUIRED": StatusMark.OBLIGATION,
        "SOURCE_SAFETY_REQUIRED": StatusMark.OBLIGATION,
        "TRACE_SAFETY_REQUIRED": StatusMark.OBLIGATION,
        "DIVERGENCE_IDENTITY_REQUIRED": StatusMark.OBLIGATION,
        "SAFETY_THEOREMS_REQUIRED": StatusMark.OBLIGATION,
        "PHYSICAL_USE_BLOCKED": StatusMark.DEFER,
        "NOT_INSERTABLE": StatusMark.DEFER,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REJECTED_ROUTE": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {
        "REJECTED_ROUTE",
        "FORBIDDEN_SHORTCUT",
    }:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {
        "SOURCE_TRACE_DIVERGENCE_TARGET",
        "COVARIANT_LIFT_REQUIRED",
        "BOUNDARY_NEUTRALITY_REQUIRED",
        "SOURCE_SAFETY_REQUIRED",
        "TRACE_SAFETY_REQUIRED",
        "DIVERGENCE_IDENTITY_REQUIRED",
        "SAFETY_THEOREMS_REQUIRED",
        "POLICY_RULE",
    }:
        return GovernanceStatus.POLICY_RULE
    return GovernanceStatus.UNVERIFIED


def obligation_status(status: str) -> ObligationStatus:
    if status in {
        "PHYSICAL_USE_BLOCKED",
        "NOT_INSERTABLE",
        "DEFERRED_WITH_TARGET",
        "PARENT_EQUATION_BLOCKED",
        "RECOMBINATION_BLOCKED",
        "TRACE_NORMALIZATION_NOT_ADOPTED",
        "ACTIVE_O_NOT_CONSTRUCTED",
    }:
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
        record_claim(ns, f"{marker_id}_c{idx}", marker_id, item.status, f"{item.name}: {item.subject}. {item.detail}. Boundary: {item.boundary}.")
    for idx, item in enumerate(obligations, 1):
        record_obligation(ns, f"{marker_id}_o{idx}", item.name, f"{item.obligation}. Discipline: {item.discipline}.", item.status)


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



def case_dependency_graph(out: ScriptOutput):
    header("Case 0: Parent blocker dependency graph")

    edges = [
        ("parent equation", "recombination rule"),
        ("recombination rule", "source safety"),
        ("recombination rule", "trace safety"),
        ("recombination rule", "divergence identity"),
        ("recombination rule", "covariant lift"),
        ("recombination rule", "boundary neutrality"),
        ("recombination rule", "active O decision"),
        ("recombination rule", "trace-normalization decision"),
        ("source safety", "source count once"),
        ("trace safety", "trace count once"),
        ("divergence identity", "covariant lift"),
        ("boundary neutrality", "boundary diagnostic ledger"),
    ]

    for parent, dep in edges:
        print(f"{parent} depends_on {dep}")

    with out.derived_results():
        for parent, dep in edges:
            out.line(parent, StatusMark.INFO, f"depends_on={dep}")

    return {"edge_count": sp.Integer(len(edges))}


def record_graph(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g66_graph",
        inputs=[],
        output=data["edge_count"],
        method="record dependency graph among parent blockers",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="parent_blocker_dependency_graph",
        scope="dependency inventory; no blocker solved",
    )



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

    data = case_dependency_graph(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_graph(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
