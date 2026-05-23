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

SCRIPT_LABEL = 'Candidate Boundary Divergence Neutrality'
MARKER_ID = 'g68_boundary'
DEPENDENCIES = [('g67_summary', '067_source_trace_divergence_blocker_audit__candidate_group_67_status_summary', 'g67_summary'), ('g68_problem', '068_covariant_divergence_identity_attempt__candidate_covariant_identity_problem', 'g68_problem'), ('g68_lift', '068_covariant_divergence_identity_attempt__candidate_covariant_lift_requirement', 'g68_lift')]
QUESTION = 'What boundary condition is required for the no-repair divergence identity?'
DISCIPLINE = 'This script records the boundary divergence neutrality target and rejects boundary cancellation by fiat.'
OPENING_LINE = 'Boundary divergence neutrality opened'
SCOPE = 'Group 68 boundary divergence neutrality'
NEXT_SCRIPT = 'candidate_repair_current_rejection.py'

ENTRIES = [('B1: boundary divergence', 'D_boundary=D_jump+D_tail+D_layer', 'BOUNDARY_NEUTRALITY_REQUIRED', 'boundary burden must be represented explicitly', 'required'), ('B2: neutrality target', 'D_boundary=0 or structural cancellation with D_lift', 'BOUNDARY_NEUTRALITY_NOT_PROVEN', 'boundary neutrality is not proved here', 'open'), ('B3: forced layer', 'D_layer=-(D_jump+D_tail)', 'REPAIR_CURRENT_REJECTED', 'forced boundary cancellation is repair-like unless derived', 'rejected'), ('B4: diagnostic boundary', 'boundary diagnostics constrain but do not insert', 'TRANSITION_REMAINS_DIAGNOSTIC', 'diagnostic transition cannot supply D_layer as term', 'hard fence')]
SHORTCUTS = [('X1: boundary silence as divergence theorem', 'treat endpoint silence as D_boundary=0', 'divergence neutrality must be derived'), ('X2: diagnostic layer as cancellation', 'use transition diagnostic to cancel boundary divergence', 'diagnostic-only forbids term use'), ('X3: forced layer cancellation', 'choose layer term to cancel D_jump+D_tail', 'repair-like')]
OBLIGATIONS = [('O1: repair rejection', 'POLICY_RULE', 'reject arbitrary D_repair and boundary repair currents', 'avoid fake conservation')]
LOCAL_CONCLUSIONS = [('boundary neutrality required', 'BOUNDARY_NEUTRALITY_REQUIRED', 'D_boundary remains a real burden'), ('boundary neutrality not proven', 'BOUNDARY_NEUTRALITY_NOT_PROVEN', 'no boundary divergence theorem obtained')]


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
        "DIVERGENCE_ATTEMPT_OPENED": StatusMark.INFO,
        "NO_REPAIR_TARGET_DERIVED": StatusMark.PASS,
        "O_FREE_TARGET_DERIVED": StatusMark.PASS,
        "COVARIANT_LIFT_REQUIRED": StatusMark.OBLIGATION,
        "COVARIANT_LIFT_NOT_PROVEN": StatusMark.OBLIGATION,
        "BOUNDARY_NEUTRALITY_REQUIRED": StatusMark.OBLIGATION,
        "BOUNDARY_NEUTRALITY_NOT_PROVEN": StatusMark.OBLIGATION,
        "REPAIR_CURRENT_REJECTED": StatusMark.FAIL,
        "ACTIVE_O_NOT_CONSTRUCTED": StatusMark.DEFER,
        "ACTIVE_O_CONDITIONALLY_REQUIRED": StatusMark.DEFER,
        "ACTIVE_O_BY_LABEL_REJECTED": StatusMark.FAIL,
        "TRANSITION_REMAINS_DIAGNOSTIC": StatusMark.PASS,
        "DIVERGENCE_IDENTITY_NOT_PROVEN": StatusMark.OBLIGATION,
        "DIVERGENCE_TARGET_SHARPENED": StatusMark.PASS,
        "STRUCTURAL_CANCELLATION_REQUIRED": StatusMark.OBLIGATION,
        "COUNT_ONCE_PRESERVED": StatusMark.PASS,
        "RESIDUAL_NONENTRY_PRESERVED": StatusMark.PASS,
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
        "REPAIR_CURRENT_REJECTED",
        "ACTIVE_O_BY_LABEL_REJECTED",
        "REJECTED_ROUTE",
        "FORBIDDEN_SHORTCUT",
    }:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {
        "COVARIANT_LIFT_REQUIRED",
        "COVARIANT_LIFT_NOT_PROVEN",
        "BOUNDARY_NEUTRALITY_REQUIRED",
        "BOUNDARY_NEUTRALITY_NOT_PROVEN",
        "DIVERGENCE_IDENTITY_NOT_PROVEN",
        "STRUCTURAL_CANCELLATION_REQUIRED",
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
        "ACTIVE_O_NOT_CONSTRUCTED",
        "ACTIVE_O_CONDITIONALLY_REQUIRED",
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



def case_boundary_neutrality(out: ScriptOutput):
    header("Case 0: Boundary divergence neutrality requirement")

    D_jump, D_tail, D_layer = sp.symbols("D_jump D_tail D_layer")
    D_boundary = sp.simplify(D_jump + D_tail + D_layer)
    neutrality_condition = sp.Eq(D_boundary, 0)
    layer_solution = sp.solve(neutrality_condition, D_layer)[0]

    print(f"D_boundary = {D_boundary}")
    print(f"boundary neutrality target: {neutrality_condition}")
    print(f"forced layer cancellation would require D_layer = {layer_solution}")

    with out.derived_results():
        out.line("D_boundary", StatusMark.OBLIGATION, str(D_boundary))
        out.line("neutrality target", StatusMark.OBLIGATION, str(neutrality_condition))
        out.line("forced layer cancellation", StatusMark.FAIL, f"D_layer={layer_solution}")

    return {"D_boundary": D_boundary}


def record_boundary(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g68_boundary",
        inputs=[],
        output=data["D_boundary"],
        method="record boundary divergence neutrality target and reject forced layer cancellation",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="boundary_divergence_neutrality_requirement",
        scope="boundary neutrality requirement; no neutrality theorem",
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

    data = case_boundary_neutrality(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_boundary(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
