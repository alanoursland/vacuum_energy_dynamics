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

SCRIPT_LABEL = 'Candidate Parent Path Implications'
MARKER_ID = 'g65_parent'
DEPENDENCIES = [('g64_summary', '64_variational_stress_origin__candidate_group_64_status_summary', 'g64_summary'), ('g65_problem', '65_transition_diagnostic_downgrade__candidate_downgrade_problem', 'g65_problem'), ('g65_revival', '65_transition_diagnostic_downgrade__candidate_revival_conditions', 'g65_revival')]
QUESTION = 'What does diagnostic-only transition status imply for the parent field-equation path?'
DISCIPLINE = 'This script records that the transition response is not a parent ingredient while its diagnostics remain constraints.'
OPENING_LINE = 'Parent path implications opened'
SCOPE = 'Group 65 parent path implications'
NEXT_SCRIPT = 'candidate_downgrade_route_classifier.py'

ENTRIES = [('I1: no parent ingredient', 'transition response excluded from parent insertion', 'PARENT_PATH_CLEANED', 'candidate quarantine cleans parent path', 'not insertable'), ('I2: diagnostics remain', 'boundary diagnostics constrain future work', 'BOUNDARY_DIAGNOSTICS_PRESERVED', 'clues remain useful', 'diagnostic'), ('I3: no Groups 57-64 insertion', 'transition insertion remains blocked', 'NOT_INSERTABLE', 'no field-equation term emerges from this block', 'blocked'), ('I4: next inventory', 'parent blocker inventory can proceed', 'DEFERRED_WITH_TARGET', 'next group can cleanly inventory remaining blockers', 'handoff')]
SHORTCUTS = [('X1: parent insertion', 'carry transition response into parent equation', 'diagnostic-only forbids it'), ('X2: ignore diagnostics', 'lose boundary lessons', 'preserve constraints')]
OBLIGATIONS = [('O1: parent blocker inventory', 'DEFERRED_WITH_TARGET', 'inventory remaining parent blockers after quarantine', 'avoid candidate drift')]
LOCAL_CONCLUSIONS = [('parent path cleaned', 'PARENT_PATH_CLEANED', 'unlicensed transition response removed from parent candidate path'), ('diagnostics preserved', 'BOUNDARY_DIAGNOSTICS_PRESERVED', 'boundary clues remain constraints')]


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
        "DOWNGRADE_OPENED": StatusMark.INFO,
        "DIAGNOSTIC_LEDGER_RECORDED": StatusMark.PASS,
        "DIAGNOSTIC_ONLY_STATUS_ASSIGNED": StatusMark.PASS,
        "FORBIDDEN_USE_FENCE_RECORDED": StatusMark.PASS,
        "PHYSICAL_USE_FORBIDDEN": StatusMark.FAIL,
        "REVIVAL_GATE_RECORDED": StatusMark.PASS,
        "REVIVAL_REQUIRES_THEOREM": StatusMark.OBLIGATION,
        "PARENT_PATH_CLEANED": StatusMark.INFO,
        "CANDIDATE_QUARANTINED": StatusMark.INFO,
        "BOUNDARY_DIAGNOSTICS_PRESERVED": StatusMark.PASS,
        "NOT_FULL_NO_GO": StatusMark.DEFER,
        "STRESS_ACCOUNTING_NOT_CLOSED": StatusMark.OBLIGATION,
        "SOURCE_SAFETY_REQUIRED": StatusMark.OBLIGATION,
        "ENERGY_ACCOUNTING_REQUIRED": StatusMark.OBLIGATION,
        "COVARIANT_LIFT_REQUIRED": StatusMark.OBLIGATION,
        "DIVERGENCE_IDENTITY_REQUIRED": StatusMark.OBLIGATION,
        "SAFETY_THEOREMS_REQUIRED": StatusMark.OBLIGATION,
        "PHYSICAL_USE_BLOCKED": StatusMark.DEFER,
        "NOT_INSERTABLE": StatusMark.DEFER,
        "ACTIVE_O_NECESSITY_NOT_ESTABLISHED": StatusMark.DEFER,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REJECTED_ROUTE": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {
        "PHYSICAL_USE_FORBIDDEN",
        "REJECTED_ROUTE",
        "FORBIDDEN_SHORTCUT",
    }:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {
        "REVIVAL_REQUIRES_THEOREM",
        "STRESS_ACCOUNTING_NOT_CLOSED",
        "SOURCE_SAFETY_REQUIRED",
        "ENERGY_ACCOUNTING_REQUIRED",
        "COVARIANT_LIFT_REQUIRED",
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
        "ACTIVE_O_NECESSITY_NOT_ESTABLISHED",
        "NOT_FULL_NO_GO",
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



def case_parent_implications(out: ScriptOutput):
    header("Case 0: Parent path implications")

    implications = [
        ("not_parent_ingredient", "transition response cannot enter parent equation"),
        ("diagnostics_as_constraints", "boundary diagnostics may constrain future candidates"),
        ("no_group57_64_insertion", "no transition insertion from Groups 57-64"),
        ("parent_blocker_inventory_cleaner", "parent blocker inventory can proceed without this candidate"),
        ("boundary_ledger_needed", "diagnostic facts should be preserved in a boundary ledger"),
    ]

    for label, text in implications:
        print(f"{label}: {text}")

    with out.derived_results():
        for label, text in implications:
            out.line(label, StatusMark.INFO, text)

    return {"count": sp.Integer(len(implications))}


def record_parent(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g65_parent",
        inputs=[],
        output=data["count"],
        method="record parent-field-equation implications of diagnostic-only transition status",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="parent_path_implications",
        scope="parent-route governance; no parent equation",
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

    data = case_parent_implications(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_parent(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
