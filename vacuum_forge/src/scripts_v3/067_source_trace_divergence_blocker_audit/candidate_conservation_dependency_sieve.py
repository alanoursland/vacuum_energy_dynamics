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

SCRIPT_LABEL = 'Candidate Conservation Dependency Sieve'
MARKER_ID = 'g67_cons'
DEPENDENCIES = [('g66_summary', '66_parent_blocker_inventory__candidate_group_66_status_summary', 'g66_summary'), ('g67_problem', '67_source_trace_divergence_blocker_audit__candidate_blocker_problem', 'g67_problem'), ('g67_div', '67_source_trace_divergence_blocker_audit__candidate_divergence_identity_obstruction', 'g67_div')]
QUESTION = 'What prerequisites remain for a real parent divergence identity?'
DISCIPLINE = 'This script records conservation prerequisites after the reduced divergence obstruction.'
OPENING_LINE = 'Conservation dependency sieve opened'
SCOPE = 'Group 67 conservation dependency sieve'
NEXT_SCRIPT = 'candidate_parent_blocker_route_classifier.py'

ENTRIES = [('K1: count prerequisites', 'source and trace count once', 'CONSERVATION_DEPENDENCIES_RECORDED', 'count-once conditions are necessary', 'required'), ('K2: residual prerequisite', 'residual nonentry', 'CONSERVATION_DEPENDENCIES_RECORDED', 'residual channels must stay out', 'required'), ('K3: lift/boundary prerequisites', 'covariant lift and boundary neutrality', 'COVARIANT_LIFT_REQUIRED', 'reduced balance must be lifted and boundary protected', 'open'), ('K4: O/repair prerequisites', 'active O decision and no repair currents', 'ACTIVE_O_DECISION_REQUIRED', 'operator/repair shortcuts cannot fake identity', 'open'), ('K5: transition status', 'diagnostic-only', 'TRANSITION_REMAINS_DIAGNOSTIC', 'transition response remains noncontributing', 'hard fence')]
SHORTCUTS = [('X1: repair identity', 'derive conservation by adding repair current', 'rejected'), ('X2: O identity by label', 'assume active O supplies conservation', 'O decision/construction missing'), ('X3: reduced identity', 'use reduced algebra as covariant proof', 'covariant lift missing')]
OBLIGATIONS = [('O1: route classifier', 'POLICY_RULE', 'classify next route after source/trace/divergence audit', 'avoid parent overclaim')]
LOCAL_CONCLUSIONS = [('conservation dependencies recorded', 'CONSERVATION_DEPENDENCIES_RECORDED', 'divergence identity prerequisites are explicit'), ('divergence identity still required', 'DIVERGENCE_IDENTITY_REQUIRED', 'no covariant parent identity proven')]


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
        "BLOCKER_AUDIT_OPENED": StatusMark.INFO,
        "INCIDENCE_AUDIT_DERIVED": StatusMark.PASS,
        "SOURCE_COUNT_ONCE_CLARIFIED": StatusMark.PASS,
        "TRACE_COUNT_ONCE_CLARIFIED": StatusMark.PASS,
        "STRICT_SAFE_STATE_IDENTIFIED": StatusMark.PASS,
        "SOURCE_REPAIR_REJECTED": StatusMark.FAIL,
        "TRACE_REPAIR_REJECTED": StatusMark.FAIL,
        "RESIDUAL_NONENTRY_CLARIFIED": StatusMark.PASS,
        "RESIDUAL_REENTRY_REJECTED": StatusMark.FAIL,
        "TRANSITION_REMAINS_DIAGNOSTIC": StatusMark.PASS,
        "DIVERGENCE_BALANCE_DERIVED": StatusMark.PASS,
        "DIVERGENCE_IDENTITY_NOT_PROVEN": StatusMark.OBLIGATION,
        "COUNT_ONCE_NOT_SUFFICIENT": StatusMark.OBLIGATION,
        "FORCED_REPAIR_REJECTED": StatusMark.FAIL,
        "CONSERVATION_DEPENDENCIES_RECORDED": StatusMark.PASS,
        "COVARIANT_LIFT_REQUIRED": StatusMark.OBLIGATION,
        "BOUNDARY_NEUTRALITY_REQUIRED": StatusMark.OBLIGATION,
        "ACTIVE_O_DECISION_REQUIRED": StatusMark.OBLIGATION,
        "SOURCE_SAFETY_REQUIRED": StatusMark.OBLIGATION,
        "TRACE_SAFETY_REQUIRED": StatusMark.OBLIGATION,
        "DIVERGENCE_IDENTITY_REQUIRED": StatusMark.OBLIGATION,
        "RECOMBINATION_BLOCKED": StatusMark.DEFER,
        "PARENT_EQUATION_BLOCKED": StatusMark.DEFER,
        "NEXT_ROUTE_PRIORITIZED": StatusMark.INFO,
        "PHYSICAL_USE_BLOCKED": StatusMark.DEFER,
        "NOT_INSERTABLE": StatusMark.DEFER,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REJECTED_ROUTE": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {
        "SOURCE_REPAIR_REJECTED",
        "TRACE_REPAIR_REJECTED",
        "RESIDUAL_REENTRY_REJECTED",
        "FORCED_REPAIR_REJECTED",
        "REJECTED_ROUTE",
        "FORBIDDEN_SHORTCUT",
    }:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {
        "DIVERGENCE_IDENTITY_NOT_PROVEN",
        "COUNT_ONCE_NOT_SUFFICIENT",
        "COVARIANT_LIFT_REQUIRED",
        "BOUNDARY_NEUTRALITY_REQUIRED",
        "ACTIVE_O_DECISION_REQUIRED",
        "SOURCE_SAFETY_REQUIRED",
        "TRACE_SAFETY_REQUIRED",
        "DIVERGENCE_IDENTITY_REQUIRED",
        "POLICY_RULE",
    }:
        return GovernanceStatus.POLICY_RULE
    return GovernanceStatus.UNVERIFIED


def obligation_status(status: str) -> ObligationStatus:
    if status in {
        "PHYSICAL_USE_BLOCKED",
        "NOT_INSERTABLE",
        "DEFERRED_WITH_TARGET",
        "RECOMBINATION_BLOCKED",
        "PARENT_EQUATION_BLOCKED",
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



def case_conservation_dependencies(out: ScriptOutput):
    header("Case 0: Conservation dependency sieve")

    deps = [
        ("source count once", "required"),
        ("trace count once", "required"),
        ("residual nonentry", "required"),
        ("covariant lift", "required"),
        ("boundary neutrality", "required"),
        ("active O decision or rejection", "required if separation cannot be achieved otherwise"),
        ("no repair currents", "required"),
        ("transition remains diagnostic", "required"),
    ]

    for name, status in deps:
        print(f"{name}: {status}")

    with out.derived_results():
        for name, status in deps:
            out.line(name, StatusMark.OBLIGATION, status)

    return {"dependency_count": sp.Integer(len(deps))}


def record_cons(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g67_cons",
        inputs=[],
        output=data["dependency_count"],
        method="record prerequisites for a real parent divergence/conservation identity",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="conservation_dependency_sieve",
        scope="conservation prerequisite inventory; no divergence theorem",
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

    data = case_conservation_dependencies(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_cons(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
