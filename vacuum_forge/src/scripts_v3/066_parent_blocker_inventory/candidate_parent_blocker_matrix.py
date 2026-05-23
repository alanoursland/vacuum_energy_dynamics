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

SCRIPT_LABEL = 'Candidate Parent Blocker Matrix'
MARKER_ID = 'g66_matrix'
DEPENDENCIES = [('g65_summary', '065_transition_diagnostic_downgrade__candidate_group_65_status_summary', 'g65_summary'), ('g66_problem', '066_parent_blocker_inventory__candidate_parent_inventory_problem', 'g66_problem'), ('g66_ledger', '066_parent_blocker_inventory__candidate_artifact_status_ledger', 'g66_ledger')]
QUESTION = 'What remaining blockers prevent parent field-equation construction?'
DISCIPLINE = 'This script records the parent blocker matrix after transition-response quarantine.'
OPENING_LINE = 'Parent blocker matrix opened'
SCOPE = 'Group 66 parent blocker matrix'
NEXT_SCRIPT = 'candidate_recombination_prerequisite_sieve.py'

ENTRIES = [('B1: source/trace', 'source count, trace count, residual nonentry', 'SOURCE_TRACE_DIVERGENCE_TARGET', 'source and trace safety remain central blockers', 'open'), ('B2: divergence/covariance', 'divergence identity and covariant lift', 'DIVERGENCE_IDENTITY_REQUIRED', 'parent construction requires conservation structure', 'open'), ('B3: boundary/mass', 'boundary neutrality and A-sector mass protection', 'BOUNDARY_NEUTRALITY_REQUIRED', 'boundary diagnostics constrain parent candidates', 'open'), ('B4: O/trace decision', 'active O and trace-normalization decisions', 'DEFERRED_WITH_TARGET', 'status decisions remain unresolved', 'open'), ('B5: recombination', 'sector recombination rule', 'RECOMBINATION_BLOCKED', 'parent equation cannot recombine sectors yet', 'blocked')]
SHORTCUTS = [('X1: list equals proof', 'treat matrix as solving blockers', 'matrix only inventories blockers'), ('X2: recombine now', 'combine sectors before prerequisites', 'recombination blocked'), ('X3: ignore transition quarantine', 'include diagnostic transition as parent term', 'not parent ingredient')]
OBLIGATIONS = [('O1: prerequisite sieve', 'POLICY_RULE', 'test whether recombination prerequisites are met', 'avoid premature parent equation')]
LOCAL_CONCLUSIONS = [('blocker matrix recorded', 'BLOCKER_MATRIX_RECORDED', 'remaining parent blockers are explicit'), ('parent equation remains blocked', 'PARENT_EQUATION_BLOCKED', 'no recombination or parent equation licensed')]


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



def case_blocker_matrix(out: ScriptOutput):
    header("Case 0: Parent blocker matrix")

    blockers = [
        ("source count once", "ordinary source must not duplicate or be repaired"),
        ("trace count once", "trace payload must not duplicate or reenter residual"),
        ("residual nonentry", "rejected residual routes must stay dead"),
        ("divergence identity", "parent equation must satisfy a conservation/divergence identity"),
        ("covariant lift", "reduced diagnostics must not be treated as covariant theorems"),
        ("boundary neutrality", "boundary/exterior scalar silence must be protected"),
        ("A-sector mass protection", "source/mass accounting must not shift A-sector by hidden layer load"),
        ("active O decision", "prove unnecessary or construct it"),
        ("trace-normalization decision", "adopt/defer/reject paired trace candidate"),
        ("recombination rule", "define how admissible sectors combine"),
    ]

    for name, detail in blockers:
        print(f"{name}: {detail}")

    with out.derived_results():
        for name, detail in blockers:
            out.line(name, StatusMark.OBLIGATION, detail)

    return {"blocker_count": sp.Integer(len(blockers))}


def record_matrix(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g66_matrix",
        inputs=[],
        output=data["blocker_count"],
        method="record remaining parent blocker matrix after transition quarantine",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="parent_blocker_matrix",
        scope="parent-readiness blocker inventory; no theorem closure",
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

    data = case_blocker_matrix(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_matrix(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
