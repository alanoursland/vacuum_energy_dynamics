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

SCRIPT_LABEL = 'Candidate Repair Current Rejection'
MARKER_ID = 'g68_repair'
DEPENDENCIES = [('g67_summary', '067_source_trace_divergence_blocker_audit__candidate_group_67_status_summary', 'g67_summary'), ('g68_problem', '068_covariant_divergence_identity_attempt__candidate_covariant_identity_problem', 'g68_problem'), ('g68_boundary', '068_covariant_divergence_identity_attempt__candidate_boundary_divergence_neutrality', 'g68_boundary')]
QUESTION = 'Can a repair current be used to close the remaining divergence balance?'
DISCIPLINE = 'This script rejects arbitrary repair current cancellation and restates the no-repair balance.'
OPENING_LINE = 'Repair-current rejection opened'
SCOPE = 'Group 68 repair current rejection'
NEXT_SCRIPT = 'candidate_active_O_divergence_necessity.py'

ENTRIES = [('R1: repair choice', 'D_repair=-(D_lift+D_boundary+D_O)', 'REPAIR_CURRENT_REJECTED', 'arbitrary repair current is not a conservation theorem', 'rejected'), ('R2: no-repair balance', 'D_lift + D_boundary + D_O = 0', 'NO_REPAIR_TARGET_DERIVED', 'identity must be structural, not patched', 'target'), ('R3: transition status', 'diagnostic transition cannot be repair current', 'TRANSITION_REMAINS_DIAGNOSTIC', 'diagnostic-only material cannot carry D_repair', 'hard fence')]
SHORTCUTS = [('X1: arbitrary repair', 'define D_repair as whatever cancels', 'not derivation'), ('X2: diagnostic repair', 'use transition diagnostic as repair current', 'forbidden'), ('X3: conservation by definition', 'define parent as conserved by adding patch', 'not acceptable')]
OBLIGATIONS = [('O1: active O necessity', 'ACTIVE_O_DECISION_REQUIRED', 'classify active O as unnecessary, necessary, or unconstructed', 'avoid O-as-repair')]
LOCAL_CONCLUSIONS = [('repair current rejected', 'REPAIR_CURRENT_REJECTED', 'forced D_repair cancellation cannot close identity'), ('structural cancellation required', 'STRUCTURAL_CANCELLATION_REQUIRED', 'remaining divergence must cancel structurally')]


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



def case_repair_rejection(out: ScriptOutput):
    header("Case 0: Repair-current rejection")

    D_lift, D_boundary, D_O, D_repair = sp.symbols("D_lift D_boundary D_O D_repair")
    balance = sp.Eq(D_lift + D_boundary + D_O + D_repair, 0)
    repair_choice = sp.solve(balance, D_repair)[0]
    no_repair_balance = sp.Eq(D_lift + D_boundary + D_O, 0)

    print(f"full balance = {balance}")
    print(f"repair choice = {repair_choice}")
    print(f"no-repair balance = {no_repair_balance}")

    with out.derived_results():
        out.line("repair choice", StatusMark.FAIL, f"D_repair={repair_choice}")
        out.line("no-repair balance", StatusMark.PASS, str(no_repair_balance))

    return {"repair_choice": repair_choice}


def record_repair(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g68_repair",
        inputs=[],
        output=data["repair_choice"],
        method="reject arbitrary repair current as divergence identity source",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="repair_current_rejection",
        scope="repair-current governance; no conservation theorem",
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

    data = case_repair_rejection(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_repair(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
