from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple

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
    for item in dependencies:
        if len(item) == 3:
            dep_id, upstream_script_id, upstream_derivation_id = item
            expected_record_kind = RecordKind.INVENTORY_MARKER
        else:
            dep_id, upstream_script_id, upstream_derivation_id, expected_record_kind = item
        ns.declare_dependency(
            dependency_id=dep_id,
            upstream_script_id=upstream_script_id,
            upstream_derivation_id=upstream_derivation_id,
            expected_record_kind=expected_record_kind,
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
        "ADOPTION_DECISION_SURFACE": StatusMark.INFO,
        "THEORY_DECISION_REQUIRED": StatusMark.DEFER,
        "ADOPTION_DECISION_DEFERRED": StatusMark.DEFER,
        "CANDIDATE_RETAINED_FOR_AUDIT": StatusMark.INFO,
        "SAFETY_THEOREMS_REQUIRED": StatusMark.OBLIGATION,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_INSERTABLE": StatusMark.DEFER,
        "NOT_PARENT_FACING": StatusMark.DEFER,
        "REJECTED_ROUTE": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "RECORD_LEVEL_ONLY": StatusMark.INFO,
        "CONDITIONAL_RECORD_ONLY": StatusMark.INFO,
        "PHYSICAL_USE_REJECTED": StatusMark.FAIL,
        "BRANCH_BURDEN_LIVE": StatusMark.PASS,
        "PREREQUISITE_OPEN": StatusMark.OBLIGATION,
        "CHOICE_REQUIRED": StatusMark.DEFER,
        "NUMERIC_D_CONDITION": StatusMark.OBLIGATION,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "NOT_READY": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {"REJECTED_ROUTE", "FORBIDDEN_SHORTCUT", "PHYSICAL_USE_REJECTED"}:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {"POLICY_RULE", "SAFETY_THEOREMS_REQUIRED", "NUMERIC_D_CONDITION", "BRANCH_BURDEN_LIVE"}:
        return GovernanceStatus.POLICY_RULE
    return GovernanceStatus.UNVERIFIED


def obligation_status(status: str) -> ObligationStatus:
    if status in {
        "THEORY_DECISION_REQUIRED",
        "ADOPTION_DECISION_DEFERRED",
        "SAFETY_THEOREMS_REQUIRED",
        "DEFERRED_WITH_TARGET",
        "PREREQUISITE_OPEN",
        "CHOICE_REQUIRED",
        "NUMERIC_D_CONDITION",
        "NOT_READY",
        "NOT_DERIVED",
        "NOT_ADOPTED",
        "NOT_INSERTABLE",
        "NOT_PARENT_FACING",
    }:
        return ObligationStatus.DEFERRED
    return ObligationStatus.OPEN


def record_marker(ns, marker_id: str, symbol_name: str, scope: str) -> None:
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[],
        output=sp.Symbol(symbol_name),
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


def emit_entries(out: ScriptOutput, entries: List[Entry], title: str) -> None:
    header(title)
    for item in entries:
        subheader(item.name)
        print(f"Subject: {item.subject}")
        print(f"Detail: {item.detail}")
        print(f"Boundary: {item.boundary}")
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.detail}. Boundary: {item.boundary}")


def emit_shortcuts(out: ScriptOutput, shortcuts: List[Shortcut]) -> None:
    header("Rejected shortcuts and invalid upgrades")
    for item in shortcuts:
        subheader(item.name)
        print(f"Shortcut: {item.shortcut}")
        with out.counterexamples():
            out.line(item.name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {item.reason}")


def emit_obligations(out: ScriptOutput, obligations: List[ObligationEntry]) -> None:
    header("Open obligations and deferred burdens")
    for item in obligations:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        with out.unresolved_obligations():
            out.line(item.name, mark(item.status), f"{item.status}: {item.obligation}; discipline: {item.discipline}")


def record_governance(ns, marker_id: str, symbol_name: str, entries: List[Entry], obligations: List[ObligationEntry], scope: str) -> None:
    record_marker(ns, marker_id, symbol_name, scope)
    for idx, item in enumerate(entries, start=1):
        record_claim(
            ns,
            f"{marker_id}_claim_{idx}",
            marker_id,
            item.status,
            f"{item.name}: {item.subject}. {item.detail}. Boundary: {item.boundary}.",
        )
    for idx, item in enumerate(obligations, start=1):
        record_obligation(
            ns,
            f"{marker_id}_obligation_{idx}",
            item.name,
            f"{item.obligation}. Discipline: {item.discipline}.",
            item.status,
        )


SCRIPT_LABEL = 'Candidate Adopt / Defer / Reject Decision Batch Reconciliation'
MARKER_ID = 'g51_recon'
SYMBOL_NAME = 'G51_adopt_defer_reject_decision_batch_reconciliation'
SCOPE = 'Group 51 reconciliation: preserve decision surface, retained narrow candidate, rejected bad upgrades, and deferred strong adoption without opening physical use'
DEPENDENCIES = [('g50_summary', '050_symbolic_paired_trace_normalization_declaration_attempt__candidate_group_50_status_summary', 'g50_summary'), ('g51_problem', '051_trace_normalization_adopt_defer_reject_decision_surface__candidate_adopt_defer_reject_decision_problem', 'g51_problem'), ('g51_record_level_adoption', '051_trace_normalization_adopt_defer_reject_decision_surface__candidate_record_level_adoption_meaning_audit', 'g51_record_level_adoption'), ('g51_branch_burden_sanity', '051_trace_normalization_adopt_defer_reject_decision_surface__candidate_branch_burden_symbolic_sanity_check', 'g51_branch_burden_sanity', RecordKind.DERIVATION), ('g51_prereq_matrix', '051_trace_normalization_adopt_defer_reject_decision_surface__candidate_adoption_prerequisite_matrix', 'g51_prereq_matrix'), ('g51_defer_route', '051_trace_normalization_adopt_defer_reject_decision_surface__candidate_defer_route_and_theorem_dependency_audit', 'g51_defer_route'), ('g51_rejection_sieve', '051_trace_normalization_adopt_defer_reject_decision_surface__candidate_rejection_trigger_sieve', 'g51_rejection_sieve'), ('g51_route_classifier', '051_trace_normalization_adopt_defer_reject_decision_surface__candidate_decision_surface_route_classifier', 'g51_route_classifier')]
QUESTION = 'Did Group 51 classify the adoption/defer/reject decision surface without upgrading the conditional attempt?'
DISCIPLINE = 'This reconciliation prepares the group summary. It must preserve the decision surface and avoid adoption, insertion, branch choice, active O, recombination, and parent closure.'
OPENING_LINE = 'Decision batch reconciliation opened -- summarize surface without upgrading it'
NEXT_SCRIPT = 'candidate_group_51_status_summary.py or result-note pass'


def build_entries() -> List[Entry]:
    return [Entry(*item) for item in [('B1: group scope', 'Group 51 stayed a decision-surface audit', 'ADOPTION_DECISION_SURFACE', 'the batch classified routes and burdens', 'not adoption group'), ('B2: symbolic anchor', 'branch-burden sanity check showed the two expressions differ by zeta/d', 'BRANCH_BURDEN_LIVE', 'factor-of-two burden remains visible', 'not branch choice'), ('B3: record route', 'narrow record-level route can survive only as caveated audit preservation', 'CONDITIONAL_RECORD_ONLY', 'the candidate can be retained for audit', 'not Package B adoption'), ('B4: strong adoption route', 'strong adoption remains deferred pending explicit decision and prerequisites', 'ADOPTION_DECISION_DEFERRED', 'choice and safety burdens remain open', 'not adopted'), ('B5: bad upgrades', 'neutral collapse, numeric leak, recovery support, hidden branch choice, insertion drift, and caveats-as-theorems are rejected', 'REJECTED_ROUTE', 'rejected upgrades do not kill the narrow candidate', 'not total rejection'), ('B6: physical use', 'B_s/F_zeta insertion, active O, recombination, and parent closure remain closed', 'NOT_INSERTABLE', 'no field-equation route is opened', 'not parent-ready'), ('B7: handoff', 'next non-looping target is residual/source/boundary safety load testing or separate theory-owner decision', 'DEFERRED_WITH_TARGET', 'handoff should follow actual summary review', 'not assumed adoption')]]


def build_shortcuts() -> List[Shortcut]:
    return [Shortcut(*item) for item in [('X1: summary as adoption', 'write the group summary as if the conditional attempt were adopted', 'Group 51 did not decide adoption'), ('X2: summary as insertion', 'let record-level route open B_s/F_zeta insertion', 'physical use remains closed'), ('X3: summary as branch choice', 'summarize with only one trace-normalization expression', 'both branches remain explicit'), ('X4: summary as parent readiness', 'say the decision surface opens recombination or parent closure', 'parent equation remains not ready')]]


def build_obligations() -> List[ObligationEntry]:
    return [ObligationEntry(*item) for item in [('O1: write result notes from actual output', 'POLICY_RULE', 'each script result note should state what changed, what died, and what is next', 'avoid output receipts'), ('O2: write group summary carefully', 'POLICY_RULE', 'summary must preserve retained candidate, deferred adoption, rejected upgrades, and closed physical use', 'avoid status inflation'), ('O3: update field-equation snapshot', 'DEFERRED_WITH_TARGET', 'snapshot should say decision surface sharpened but field equation status remains not ready', 'avoid fake progress')]]


def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header(SCRIPT_LABEL)
    print("Question:\n")
    print(QUESTION)
    print("\nDiscipline:\n")
    print(DISCIPLINE)
    with out.governance_assessments():
        out.line(f"{SCRIPT_LABEL} opened", StatusMark.PASS, OPENING_LINE)

    entries = build_entries()
    shortcuts = build_shortcuts()
    obligations = build_obligations()

    emit_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    emit_shortcuts(out, shortcuts)
    emit_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in [('batch reconciled', 'PASS', 'Group 51 decision surface is ready for result notes and group summary'), ('parent route still closed', 'NOT_READY', 'no insertion, active O, recombination, or parent closure opened')]:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, SYMBOL_NAME, entries, obligations, SCOPE)
    ns.write_run_metadata()
    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
