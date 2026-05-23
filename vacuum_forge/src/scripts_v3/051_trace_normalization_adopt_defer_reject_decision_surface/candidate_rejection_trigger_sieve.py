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


SCRIPT_LABEL = 'Candidate Rejection Trigger Sieve'
MARKER_ID = 'g51_rejection_sieve'
SYMBOL_NAME = 'G51_rejection_trigger_sieve'
SCOPE = 'Group 51 adversarial sieve: reject forbidden adoption upgrades while preserving the narrow conditional candidate if it does not require them'
DEPENDENCIES = [('g50_summary', '50_symbolic_paired_trace_normalization_declaration_attempt__candidate_group_50_status_summary', 'g50_summary'), ('g51_defer_route', '51_trace_normalization_adopt_defer_reject_decision_surface__candidate_defer_route_and_theorem_dependency_audit', 'g51_defer_route')]
QUESTION = 'What would force the conditional attempt to be rejected rather than deferred or retained for audit?'
DISCIPLINE = 'This script distinguishes rejection of forbidden broadenings from rejection of the narrow conditional trace-normalization candidate.'
OPENING_LINE = 'Rejection trigger sieve opened -- bad upgrades can die without killing narrow candidate'
NEXT_SCRIPT = 'candidate_decision_surface_route_classifier.py'


def build_entries() -> List[Entry]:
    return [Entry(*item) for item in [('J1: neutral expression requirement', 'reject adoption if it requires neutral F_zeta with an expression or unqualified B_s', 'REJECTED_ROUTE', 'neutral collapse revives the old overload', 'not allowed'), ('J2: numeric-d leak requirement', 'reject adoption if it requires fixing numeric d without scope support', 'REJECTED_ROUTE', 'numeric d remains conditioned', 'not allowed'), ('J3: recovery-support requirement', 'reject adoption if it relies on Schwarzschild, AB=1, gamma, or recovery fit as support', 'REJECTED_ROUTE', 'recovery is audit, not construction', 'not allowed'), ('J4: hidden branch-choice requirement', 'reject adoption if it chooses metric or scale without explicit branch record', 'REJECTED_ROUTE', 'branch choice must be daylight-labeled', 'not allowed'), ('J5: insertion-required requirement', 'reject physical-use claims if adoption only becomes meaningful by insertion', 'PHYSICAL_USE_REJECTED', 'trace record existence cannot supply insertion law', 'not allowed'), ('J6: caveats-as-theorems requirement', 'reject any route that treats caveats as residual/source/boundary proofs', 'REJECTED_ROUTE', 'negative caveats are not positive safety theorems', 'not allowed'), ('J7: narrow candidate survival', 'the narrow conditional candidate is not rejected merely because bad upgrades are rejected', 'CANDIDATE_RETAINED_FOR_AUDIT', 'the candidate survives only while it refuses forbidden upgrades', 'not adoption')]]


def build_shortcuts() -> List[Shortcut]:
    return [Shortcut(*item) for item in [('X1: reject all because upgrades fail', 'kill the narrow candidate because forbidden broadenings fail', 'the sieve separates broadenings from the narrow route'), ('X2: keep upgrades because candidate survives', 'let survival revive forbidden upgrades', 'narrow survival depends on rejecting those upgrades'), ('X3: rejection as theory proof', 'treat rejected upgrades as proving an alternative branch', 'a sieve removes routes; it does not select a branch')]]


def build_obligations() -> List[ObligationEntry]:
    return [ObligationEntry(*item) for item in [('O1: carry rejection triggers forward', 'POLICY_RULE', 'future adoption language must preserve these rejection triggers', 'avoid forbidden shortcut revival'), ('O2: preserve narrow-candidate distinction', 'POLICY_RULE', 'do not collapse rejected upgrades into rejection of the narrow conditional candidate', 'avoid overkilling'), ('O3: keep physical use rejected', 'NOT_INSERTABLE', 'do not use the conditional candidate in B_s/F_zeta insertion', 'avoid field-equation drift')]]


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
    for label, status, text in [('rejection triggers stated', 'PASS', 'bad adoption upgrades are rejected'), ('narrow candidate not killed by sieve', 'CANDIDATE_RETAINED_FOR_AUDIT', 'conditional attempt survives only as audit candidate')]:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, SYMBOL_NAME, entries, obligations, SCOPE)
    ns.write_run_metadata()
    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
