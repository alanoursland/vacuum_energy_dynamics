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


SCRIPT_LABEL = 'Candidate Branch Burden Symbolic Sanity Check'
MARKER_ID = 'g51_branch_burden_sanity'
SYMBOL_NAME = 'G51_branch_burden_symbolic_sanity_check'
SCOPE = 'Group 51 symbolic sanity check: metric and scale trace-normalization expressions remain distinct unless a convention chooses or collapses them'
DEPENDENCIES = [('g50_summary', '50_symbolic_paired_trace_normalization_declaration_attempt__candidate_group_50_status_summary', 'g50_summary'), ('g51_record_level_adoption', '51_trace_normalization_adopt_defer_reject_decision_surface__candidate_record_level_adoption_meaning_audit', 'g51_record_level_adoption')]
QUESTION = 'Does the paired trace-normalization record still carry a live factor-of-two branch burden?'
DISCIPLINE = 'This script performs only a small algebraic sanity check. It does not decide adoption, choose a branch, or create a neutral law.'
OPENING_LINE = 'Branch-burden symbolic sanity check opened -- algebraic distinction only; no adoption evidence'
NEXT_SCRIPT = 'candidate_adoption_prerequisite_matrix.py'


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header(SCRIPT_LABEL)
    print('Question:\n')
    print(QUESTION)
    print('\nDiscipline:\n')
    print(DISCIPLINE)
    with out.governance_assessments():
        out.line(f'{SCRIPT_LABEL} opened', StatusMark.PASS, OPENING_LINE)

    zeta, d = sp.symbols('zeta d', nonzero=True)
    metric_expr = sp.Rational(2) * zeta / d
    scale_expr = zeta / d
    difference = sp.simplify(metric_expr - scale_expr)
    expected = zeta / d
    residual = sp.simplify(difference - expected)

    header('Case 1: Paired expression difference')
    print('metric-side log expression:')
    print(f'  2*zeta/d = {metric_expr}')
    print('scale-side log expression:')
    print(f'  zeta/d = {scale_expr}')
    print('difference:')
    print(f'  (2*zeta/d) - (zeta/d) = {difference}')
    print('residual against expected zeta/d:')
    print(f'  {residual}')

    ok = is_zero(residual)
    nonzero_difference = not is_zero(difference)
    with out.derived_results():
        out.line('branch burden residual', StatusMark.PASS if ok else StatusMark.FAIL, f'residual = {residual}')
        out.line('branch difference remains nonzero generically', StatusMark.PASS if nonzero_difference else StatusMark.FAIL, f'difference = {difference}')

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[metric_expr, scale_expr, zeta, d],
        output=residual,
        method='simplify((2*zeta/d - zeta/d) - zeta/d)',
        status=Status.DERIVED if ok else Status.FAILED,
        record_kind=RecordKind.DERIVATION,
        result_type='symbolic_residual',
        scope=SCOPE,
    )

    entries = [
        Entry('S1: factor-of-two burden remains live', 'metric and scale expressions differ by zeta/d', 'BRANCH_BURDEN_LIVE', 'the paired record is not algebraically one neutral expression', 'not adoption evidence'),
        Entry('S2: no branch collapse from algebra', 'the sanity check does not choose metric or scale', 'CHOICE_REQUIRED', 'an explicit convention would still be required to choose or collapse branches', 'not branch choice'),
        Entry('S3: no physical-use support', 'symbolic distinction says nothing about residual/source/boundary safety', 'NOT_DERIVED', 'the check supplies no insertion theorem', 'not safety proof'),
    ]
    obligations = [
        ObligationEntry('O1: preserve branch burden in decisions', 'POLICY_RULE', 'decision-surface scripts must not erase the zeta/d difference', 'avoid neutral-law drift'),
        ObligationEntry('O2: require explicit branch convention for collapse', 'CHOICE_REQUIRED', 'any collapse or branch selection needs a separate daylight-labeled convention', 'avoid algebraic smuggling'),
    ]
    shortcuts = [
        Shortcut('X1: sanity check as adoption', 'use the residual check to adopt trace normalization', 'the check only shows distinct expressions'),
        Shortcut('X2: sanity check as branch choice', 'choose the metric or scale side from the difference', 'no selector is supplied'),
        Shortcut('X3: sanity check as neutral law', 'pretend the difference is harmless and collapse both expressions', 'the difference is the live burden'),
    ]
    emit_entries(out, entries, 'Case 2: Governance meaning of the symbolic check')
    emit_shortcuts(out, shortcuts)
    emit_obligations(out, obligations)

    for idx, item in enumerate(entries, start=1):
        record_claim(ns, f'{MARKER_ID}_claim_{idx}', MARKER_ID, item.status, f'{item.name}: {item.detail}. Boundary: {item.boundary}.')
    for idx, item in enumerate(obligations, start=1):
        record_obligation(ns, f'{MARKER_ID}_obligation_{idx}', item.name, f'{item.obligation}. Discipline: {item.discipline}.', item.status)

    header('Local conclusions')
    with out.derived_results():
        out.line('symbolic branch burden check complete', StatusMark.PASS if ok else StatusMark.FAIL, 'difference equals zeta/d')
    with out.governance_assessments():
        out.line('check does not decide adoption', StatusMark.DEFER, 'symbolic distinction is an audit guard, not an adoption decision')

    ns.write_run_metadata()
    print('\nPossible next script:')
    print(f'  {NEXT_SCRIPT}')


if __name__ == '__main__':
    main()
