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
            expected_record_kind=RecordKind.INVENTORY_MARKER,
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
        "MATCHED_EXPECTATION": StatusMark.PASS,
        "CONVENTION_FIELD_AUDIT": StatusMark.INFO,
        "CONVENTION_FIELDS_CLOSED_FOR_REVIEW": StatusMark.INFO,
        "CLOSED_FOR_REVIEW": StatusMark.INFO,
        "FIELD_CLASSIFIED": StatusMark.INFO,
        "ZETA_CONVENTION": StatusMark.INFO,
        "DIMENSION_FIELD": StatusMark.INFO,
        "NORMALIZATION_SCOPE": StatusMark.INFO,
        "SHARED_FIELD": StatusMark.INFO,
        "BRANCH_INDEXED": StatusMark.INFO,
        "REVIEW_READY": StatusMark.INFO,
        "REVIEW_READY_ONLY": StatusMark.INFO,
        "CONTEXT_ONLY": StatusMark.INFO,
        "CONDITIONAL": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "DEFER": StatusMark.DEFER,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "CONVENTION_BLOCKED": StatusMark.DEFER,
        "AXIOM_REQUIRED": StatusMark.DEFER,
        "CHOICE_REQUIRED": StatusMark.DEFER,
        "THEOREM_REQUIRED": StatusMark.DEFER,
        "NOT_DECLARED": StatusMark.DEFER,
        "NOT_CHOSEN": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "CONSISTENCY_RULE": StatusMark.OBLIGATION,
        "SCOPE_REQUIRED": StatusMark.OBLIGATION,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "BLOCKED": StatusMark.FAIL,
    }.get(status, StatusMark.INFO)


def obligation_status(status: str) -> ObligationStatus:
    if status in {"NOT_READY", "NOT_DECLARED", "NOT_CHOSEN", "NOT_ADOPTED", "NOT_DERIVED", "DEFERRED_WITH_TARGET", "CONVENTION_BLOCKED"}:
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


def governance_status(status: str) -> GovernanceStatus:
    if status in {"BLOCKED", "FORBIDDEN_SHORTCUT"}:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {"AXIOM_REQUIRED", "CHOICE_REQUIRED", "THEOREM_REQUIRED", "NOT_READY", "NOT_DECLARED", "CONVENTION_BLOCKED", "DEFERRED_WITH_TARGET"}:
        return GovernanceStatus.UNVERIFIED
    return GovernanceStatus.POLICY_RULE


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
    header("Invalid upgrades and forbidden shortcuts")
    for item in shortcuts:
        subheader(item.name)
        print(f"Shortcut: {item.shortcut}")
        with out.counterexamples():
            out.line(item.name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {item.reason}")


def print_obligations(out: ScriptOutput, obligations: List[ObligationEntry]) -> None:
    header("Open obligations")
    for item in obligations:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        with out.unresolved_obligations():
            out.line(item.name, mark(item.status), f"{item.status}: {item.obligation}; discipline: {item.discipline}")


def record_governance(ns, marker_id: str, entries: List[Entry], obligations: List[ObligationEntry], scope: str) -> None:
    record_marker(ns, marker_id, scope)
    for idx, item in enumerate(entries, 1):
        record_claim(ns, f"{marker_id}_c{idx}", marker_id, item.status, f"{item.name}: {item.subject}. {item.detail}. Boundary: {item.boundary}.")
    for idx, item in enumerate(obligations, 1):
        record_obligation(ns, f"{marker_id}_o{idx}", item.name, f"{item.obligation}. Discipline: {item.discipline}.", item.status)

# Group:
#   46_parallel_trace_convention_field_closure_audit
# Script type:
#   AUDIT / CONVENTION-FIELD / PRE-DECLARATION

SCRIPT_LABEL = 'Candidate Convention Closure Route Classifier'
MARKER_ID = 'g46_route_classifier'
DEPENDENCIES = [('g45_summary', '045_explicit_parallel_trace_normalization_record__candidate_group_45_status_summary', 'g45_summary'), ('g46_zeta_convention', '046_parallel_trace_convention_field_closure_audit__candidate_zeta_convention_field_audit', 'g46_zeta_convention'), ('g46_dimension_field', '046_parallel_trace_convention_field_closure_audit__candidate_traced_dimension_field_audit', 'g46_dimension_field'), ('g46_scope_field', '046_parallel_trace_convention_field_closure_audit__candidate_normalization_scope_field_audit', 'g46_scope_field'), ('g46_pair_consistency', '046_parallel_trace_convention_field_closure_audit__candidate_branch_pair_convention_consistency_sieve', 'g46_pair_consistency')]


def build_entries() -> List[Entry]:
    return [
        Entry('R1: zeta convention route', 'zeta convention is closed for record review as a shared trace payload symbol', 'CLOSED_FOR_REVIEW', 'this improves record clarity without activating zeta', 'not declaration or insertion'),
        Entry('R2: traced dimension route', 'symbolic d is closed for record review, but numeric d remains tied to scope', 'CLOSED_FOR_REVIEW', 'symbolic role is clear enough for review', 'not numerical declaration'),
        Entry('R3: normalization scope route', 'record-review scope is usable, but declaration and parent-facing scope remain blocked', 'CONVENTION_BLOCKED', 'scope is the principal blocker before declaration attempt', 'requires target work'),
        Entry('R4: pair consistency route', 'parallel records are consistent for review and preserve the factor-of-two burden', 'REVIEW_READY_ONLY', 'the pair can be carried forward as sharper infrastructure', 'not active trace normalization'),
        Entry('R5: declaration attempt status', 'parallel trace-normalization declaration attempt is not yet honest unless declaration scope closes', 'NOT_DECLARED', 'future declaration requires explicit scope, status, and assumptions', 'not available directly'),
        Entry('R6: next non-looping route', 'targeted normalization-scope closure or declaration-scope axiom/choice audit should come before declaration attempt', 'DEFERRED_WITH_TARGET', 'the next group should attack the scope blocker or explicitly choose a scope convention', 'do not loop over all fields again'),
    ]


def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: review-ready as declaration-ready', 'treat record-review closure as enough for trace-normalization declaration', 'scope and status blockers remain'),
        Shortcut('X2: scope blocker as failure', 'treat scope blockage as proof the parallel route fails', 'blocker means targeted next work, not no-go theorem'),
        Shortcut('X3: axiom need as adoption', 'treat possible scope convention as adopted axiom', 'axiom or choice requires separate explicit record'),
        Shortcut('X4: review-ready as insertion-ready', 'insert B_s/F_zeta because records are consistent for review', 'insertion remains downstream and unsafe'),
    ]


def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: carry review-ready status accurately', 'REVIEW_READY_ONLY', 'say records are review-ready only, not declaration-ready', 'avoid status inflation'),
        ObligationEntry('O2: target the scope blocker', 'DEFERRED_WITH_TARGET', 'next narrowing work should focus on declaration scope or scope axiom/choice', 'avoid looping over already classified fields'),
        ObligationEntry('O3: preserve declaration separation', 'NOT_DECLARED', 'keep declaration as a later explicit record', 'avoid declaration by classifier'),
        ObligationEntry('O4: preserve downstream locks', 'NOT_READY', 'keep adoption, insertion, active O, residual control, recombination, and parent closure closed', 'avoid field-equation overreach'),
    ]


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print('After convention-field audits, what is the honest route classification?')
    print("\nDiscipline:\n")
    print('This script classifies Group 46 outcomes into review-ready, declaration-blocked, axiom-required, choice-required, theorem-required, or deferred-with-target routes.')
    print('It should force a non-looping handoff rather than merely restating that trace normalization is not ready.')
    with out.governance_assessments():
        out.line(
            f"{SCRIPT_LABEL} opened",
            StatusMark.PASS,
            "Group 46 convention-field audit only; no branch choice, trace declaration, adoption, insertion, active O, recombination, or parent route",
        )


def case_1(out: ScriptOutput, entries: List[Entry]) -> None:
    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")


def case_2(out: ScriptOutput, shortcuts: List[Shortcut]) -> None:
    print_shortcuts(out, shortcuts)


def case_3(out: ScriptOutput, obligations: List[ObligationEntry]) -> None:
    print_obligations(out, obligations)


def case_4(out: ScriptOutput) -> None:
    header("Local conclusions")
    conclusions = [
        ('route classification complete', 'DEFERRED_WITH_TARGET', 'parallel records are review-ready but declaration remains scope-blocked'),
        ('next target named', 'PASS', 'normalization declaration-scope closure is the next non-looping target'),
    ]
    with out.governance_assessments():
        for name, status, detail in conclusions:
            out.line(name, mark(status), detail)
    print("\nPossible next script:")
    print("  candidate_convention_field_closure_batch_reconciliation.py")


def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    entries = build_entries()
    shortcuts = build_shortcuts()
    obligations = build_obligations()

    case_0(out)
    case_1(out, entries)
    case_2(out, shortcuts)
    case_3(out, obligations)
    case_4(out)

    record_governance(ns, MARKER_ID, entries, obligations, 'Group 46 parallel trace convention-field closure audit')
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
