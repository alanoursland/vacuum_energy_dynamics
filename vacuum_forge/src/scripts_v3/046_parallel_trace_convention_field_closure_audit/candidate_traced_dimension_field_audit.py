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

SCRIPT_LABEL = 'Candidate Traced Dimension Field Audit'
MARKER_ID = 'g46_dimension_field'
DEPENDENCIES = [('g45_summary', '045_explicit_parallel_trace_normalization_record__candidate_group_45_status_summary', 'g45_summary'), ('g46_zeta_convention', '046_parallel_trace_convention_field_closure_audit__candidate_zeta_convention_field_audit', 'g46_zeta_convention')]


def build_entries() -> List[Entry]:
    return [
        Entry('D1: symbolic traced-dimension role', 'd may be closed for review as the dimension of the trace block named by the record scope', 'CLOSED_FOR_REVIEW', 'd is the denominator attached to the traced payload, not a free fitting coefficient', 'symbolic role closure is not numerical declaration'),
        Entry('D2: numerical d value', 'a numeric value for d remains scope-dependent', 'SCOPE_REQUIRED', 'spatial d=3 or other values require explicit normalization scope', 'do not fix d before scope'),
        Entry('D3: shared d across record pair', 'metric and scale records should share the same symbolic d field for comparison', 'SHARED_FIELD', 'shared d keeps the factor-of-two distinction honest', 'shared d does not choose branch'),
        Entry('D4: branch-indexed d fallback', 'branch-indexed d fields would signal scope mismatch, not declaration support', 'DEFERRED_WITH_TARGET', 'd_metric and d_scale would be repair targets if shared d fails', 'not introduced unless required'),
        Entry('D5: factor-of-two protection', 'changing d cannot be used to erase the difference between zeta/d and 2*zeta/d', 'CONSISTENCY_RULE', 'dimension convention must not absorb branch normalization difference', 'no compromise law'),
    ]


def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: d by pretty formula', 'choose d because the expression looks cleaner', 'algebraic aesthetics are not convention closure'),
        Shortcut('X2: d by recovery', 'fix d from Schwarzschild, gamma, or AB=1 recovery', 'recovery is not construction'),
        Shortcut('X3: d absorbs factor of two', 'change d separately in each branch to make expressions appear equal', 'that hides the branch burden'),
        Shortcut('X4: d as declaration', 'treat symbolic d role as completed trace-normalization declaration', 'field role closure is not declaration'),
    ]


def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: keep symbolic d shared for review', 'CLOSED_FOR_REVIEW', 'use one traced-dimension field across the paired records unless scope forces labels', 'preserve comparison quality'),
        ObligationEntry('O2: defer numeric d until scope', 'SCOPE_REQUIRED', 'do not assign numeric d without a declared normalization scope', 'avoid hidden scope choice'),
        ObligationEntry('O3: prevent d from hiding factor of two', 'POLICY_RULE', 'do not use dimension fields to collapse zeta/d and 2*zeta/d', 'avoid fake neutral law'),
    ]


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print('What does the traced dimension d mean in the paired expressions 2*zeta/d and zeta/d?')
    print("\nDiscipline:\n")
    print('This script audits the d field in the explicit parallel trace records.')
    print('It distinguishes symbolic traced-dimension role from numerical dimension choice, so d cannot be fixed by algebraic prettiness or recovery.')
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
        ('d role classified', 'CLOSED_FOR_REVIEW', 'd can be treated as the symbolic traced-dimension field for record review'),
        ('numeric d remains scope-blocked', 'SCOPE_REQUIRED', 'numerical dimension choice must wait on explicit normalization scope'),
    ]
    with out.governance_assessments():
        for name, status, detail in conclusions:
            out.line(name, mark(status), detail)
    print("\nPossible next script:")
    print("  candidate_normalization_scope_field_audit.py")


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
