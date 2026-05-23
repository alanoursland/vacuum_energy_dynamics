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

SCRIPT_LABEL = 'Candidate No-Repair Identity Target'
MARKER_ID = 'g68_target'
DEPENDENCIES = [('g67_summary', '067_source_trace_divergence_blocker_audit__candidate_group_67_status_summary', 'g67_summary'), ('g68_problem', '068_covariant_divergence_identity_attempt__candidate_covariant_identity_problem', 'g68_problem')]
QUESTION = 'What no-repair and O-free equations must hold for divergence closure?'
DISCIPLINE = 'This script derives the sharp divergence identity target after strict count-once.'
OPENING_LINE = 'No-repair identity target opened'
SCOPE = 'Group 68 no-repair identity target'
NEXT_SCRIPT = 'candidate_covariant_lift_requirement.py'

ENTRIES = [('T1: no-repair target', 'D_lift + D_boundary + D_O = 0', 'NO_REPAIR_TARGET_DERIVED', 'repair current is removed from identity target', 'theorem target'), ('T2: O-free target', 'D_lift + D_boundary = 0', 'O_FREE_TARGET_DERIVED', 'preferred target if active O remains unavailable', 'theorem target'), ('T3: repair route', 'D_repair=-(D_O+D_boundary+D_lift)', 'REPAIR_CURRENT_REJECTED', 'forced repair is rejected', 'rejected'), ('T4: O route', 'D_O=-(D_lift+D_boundary)', 'ACTIVE_O_CONDITIONALLY_REQUIRED', 'only meaningful if O is constructed, not chosen as repair', 'conditional')]
SHORTCUTS = [('X1: forced repair', 'choose D_repair to cancel divergence', 'repair is not derivation'), ('X2: forced O', 'choose D_O as cancellation patch', 'O must be constructed or rejected'), ('X3: count-only identity', 'claim D_count=0 proves D_parent=0', 'remaining target is nonzero unless proved')]
OBLIGATIONS = [('O1: covariant lift', 'COVARIANT_LIFT_REQUIRED', 'audit D_lift requirement', 'avoid treating reduced balance as covariant identity')]
LOCAL_CONCLUSIONS = [('no-repair target derived', 'NO_REPAIR_TARGET_DERIVED', 'D_lift + D_boundary + D_O = 0 is the no-repair target'), ('O-free target derived', 'O_FREE_TARGET_DERIVED', 'D_lift + D_boundary = 0 is the preferred O-free target')]


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



def case_no_repair_target(out: ScriptOutput):
    header("Case 0: No-repair and O-free identity target")

    D_O, D_boundary, D_lift, D_repair = sp.symbols("D_O D_boundary D_lift D_repair")
    D_parent_strict = sp.simplify(D_O + D_boundary + D_lift + D_repair)
    no_repair = sp.simplify(D_parent_strict.subs(D_repair, 0))
    o_free = sp.simplify(no_repair.subs(D_O, 0))
    repair_solution = sp.solve(sp.Eq(D_parent_strict, 0), D_repair)[0]
    o_solution = sp.solve(sp.Eq(no_repair, 0), D_O)[0]

    print(f"D_parent(strict) = {D_parent_strict}")
    print(f"no-repair target = {no_repair} = 0")
    print(f"O-free target = {o_free} = 0")
    print(f"forced D_repair solution = {repair_solution}")
    print(f"forced D_O solution = {o_solution}")

    with out.derived_results():
        out.line("strict parent divergence", StatusMark.OBLIGATION, str(D_parent_strict))
        out.line("no-repair target", StatusMark.PASS, f"{no_repair}=0")
        out.line("O-free target", StatusMark.PASS, f"{o_free}=0")
        out.line("forced repair solution", StatusMark.FAIL, f"D_repair={repair_solution}")
        out.line("forced O solution", StatusMark.OBLIGATION, f"D_O={o_solution}")

    return {"no_repair": no_repair, "o_free": o_free}


def record_target(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g68_target",
        inputs=[],
        output=data["o_free"],
        method="derive no-repair and O-free divergence identity targets from Group 67 strict divergence balance",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="no_repair_divergence_identity_target",
        scope="reduced divergence target; not covariant identity theorem",
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

    data = case_no_repair_target(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_target(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
