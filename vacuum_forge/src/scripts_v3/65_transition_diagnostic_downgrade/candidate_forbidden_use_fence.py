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

SCRIPT_LABEL = 'Candidate Forbidden Use Fence'
MARKER_ID = 'g65_fence'
DEPENDENCIES = [('g64_summary', '64_variational_stress_origin__candidate_group_64_status_summary', 'g64_summary'), ('g65_problem', '65_transition_diagnostic_downgrade__candidate_downgrade_problem', 'g65_problem'), ('g65_ledger', '65_transition_diagnostic_downgrade__candidate_diagnostic_preservation_ledger', 'g65_ledger')]
QUESTION = 'What physical uses are forbidden after diagnostic-only downgrade?'
DISCIPLINE = 'This script records the hard fence around diagnostic-only status.'
OPENING_LINE = 'Forbidden-use fence opened'
SCOPE = 'Group 65 forbidden use fence'
NEXT_SCRIPT = 'candidate_status_conversion.py'

ENTRIES = [('F1: no term/stress', 'field-equation term or stress tensor', 'FORBIDDEN_USE_FENCE_RECORDED', 'diagnostic-only object cannot be inserted or treated as stress tensor', 'forbidden'), ('F2: no source/mass/trace', 'ordinary-source, mass, or trace response', 'FORBIDDEN_USE_FENCE_RECORDED', 'diagnostic-only object carries no physical load', 'forbidden'), ('F3: no conservation/parent', 'covariant conservation or parent ingredient', 'FORBIDDEN_USE_FENCE_RECORDED', 'diagnostic-only object is not parent material', 'forbidden'), ('F4: no O patch', 'active-O patch', 'FORBIDDEN_USE_FENCE_RECORDED', 'diagnostic status cannot hide load in O', 'forbidden')]
SHORTCUTS = [('X1: term insertion', 'use diagnostic object in parent equation', 'forbidden'), ('X2: stress tensor by wording', 'call diagnostic stress tensor', 'forbidden'), ('X3: O patch', 'revive via unconstructed active O', 'forbidden')]
OBLIGATIONS = [('O1: status conversion', 'POLICY_RULE', 'convert candidate status to diagnostic-only with revival gate', 'avoid ambiguity')]
LOCAL_CONCLUSIONS = [('forbidden fence recorded', 'FORBIDDEN_USE_FENCE_RECORDED', 'physical-use drift blocked'), ('physical use forbidden', 'PHYSICAL_USE_FORBIDDEN', 'diagnostic-only forbids insertion/stress/source/parent use')]


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



def case_forbidden_fence(out: ScriptOutput):
    header("Case 0: Forbidden physical-use fence")

    forbidden = [
        "field-equation insertion",
        "stress tensor claim",
        "ordinary-source response",
        "mass response",
        "trace response",
        "covariant conservation claim",
        "parent equation ingredient",
        "active-O patch",
        "Package B adoption evidence",
    ]

    for item in forbidden:
        print(f"forbid: {item}")

    with out.derived_results():
        for item in forbidden:
            out.line(item, StatusMark.FAIL, "forbidden under diagnostic-only status")

    return {"count": sp.Integer(len(forbidden))}


def record_fence(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g65_fence",
        inputs=[],
        output=data["count"],
        method="record forbidden physical uses under diagnostic-only status",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="diagnostic_forbidden_use_fence",
        scope="status fence; no physical claim",
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

    data = case_forbidden_fence(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_fence(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
