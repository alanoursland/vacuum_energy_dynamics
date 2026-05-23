
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
        "INFO": StatusMark.INFO,
        "SPLIT_SAFE": StatusMark.INFO,
        "BRANCH_INDEXED": StatusMark.INFO,
        "NEUTRAL_SAFE": StatusMark.INFO,
        "CONDITIONAL": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "DEFER": StatusMark.DEFER,
        "BLOCKED": StatusMark.DEFER,
        "BRANCH_REQUIRED": StatusMark.OBLIGATION,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "NOT_READY": StatusMark.DEFER,
        "NOT_DECLARED": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "REJECTED": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "MATCHED_EXPECTATION": StatusMark.PASS,
    }.get(status, StatusMark.INFO)


def record_marker(ns, marker_id: str, symbol_name: str, scope: str):
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


def record_claim(ns, claim_id: str, marker_id: str, status, statement: str):
    ns.record_claim(
        ClaimRecord(
            claim_id=claim_id,
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=status,
            statement=statement,
            derivation_ids=[marker_id],
            obligation_ids=[],
        )
    )


def record_obligation(ns, obligation_id: str, statement: str, status=ObligationStatus.OPEN):
    ns.record_obligation(
        ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=obligation_id,
            status=status,
            required_by=[SCRIPT_ID],
            description=statement,
        )
    )

@dataclass
class Entry:
    name: str
    subject: str
    status: str
    detail: str
    boundary: str

# Group:
#   40_split_safe_trace_anchor_precondition_audit
# Script type:
#   AUDIT / PRECONDITION

SCRIPT_LABEL = 'Candidate Split-Safe Precondition Batch Reconciliation'
MARKER_ID = 'g40_recon'
DEPENDENCIES = [
    ('g39_summary', '039_trace_anchor_branch_choice_readiness_audit__candidate_group_39_status_summary', 'g39_summary'),
    ('g38_summary', '038_trace_anchor_explicit_declaration_record__candidate_group_38_status_summary', 'g38_summary'),
    ('g40_problem', '040_split_safe_trace_anchor_precondition_audit__candidate_split_safe_precondition_problem', 'g40_problem'),
    ('g40_branch_indexed', '040_split_safe_trace_anchor_precondition_audit__candidate_branch_indexed_precondition_ledger', 'g40_branch_indexed'),
    ('g40_fzeta_precond', '040_split_safe_trace_anchor_precondition_audit__candidate_neutral_Fzeta_split_safe_preconditions', 'g40_fzeta_precond'),
    ('g40_membership_precond', '040_split_safe_trace_anchor_precondition_audit__candidate_safe_membership_split_safe_preconditions', 'g40_membership_precond'),
    ('g40_safety_split', '040_split_safe_trace_anchor_precondition_audit__candidate_residual_source_safety_split_audit', 'g40_safety_split'),
]


def build_entries() -> List[Entry]:
    return [
        Entry('Q1: opener expectation', 'Group 40 opened as split-safe precondition audit', 'PASS', 'expected if no branch or declaration was chosen', 'summary may call this precondition audit only'),
        Entry('Q2: branch-indexed expectation', 'parallel metric/scale branch slots were carried visibly', 'PASS', 'expected if B_s_metric and b_s_scale remain separate', 'summary must preserve split labels'),
        Entry('Q3: neutral F_zeta expectation', 'neutral placeholder stayed expression-free', 'PASS', 'expected if no zeta/d or 2*zeta/d was installed', 'summary must preserve neutral boundary'),
        Entry('Q4: membership expectation', 'membership slots audited as split-safe or conditional', 'PASS', 'expected if no active membership was installed', 'summary must preserve compatible-if-declared status'),
        Entry('Q5: safety expectation', 'residual/source/divergence gates stated as preconditions', 'PASS', 'expected if not reported as solved theorems', 'summary must preserve theorem boundary'),
        Entry('Q6: downstream gates', 'insertion, active O, residual control, and parent closure remain closed', 'NOT_READY', 'expected final boundary', 'summary must not open field-equation routes'),
    ]


def case_0(out):
    header(SCRIPT_LABEL)
    print("Question:\n")
    print('Did the Group 40 batch produce the expected split-safe precondition audit shape, and what should a later summary preserve?')
    print("\nDiscipline:\n")
    print('This script reconciles the speculative Group 40 batch. It does not close the group as final summary and does not choose a branch, complete declarations, adopt, prove, insert, or open parent closure.')
    print("\nTiny goblin rule:\n  " + 'Count the jars after the cart ride. Do not pour from them.')
    with out.governance_assessments():
        out.line(f"{SCRIPT_LABEL} opened", StatusMark.PASS, "split-safe audit only; no branch choice, declaration completion, adoption, theorem, insertion, or parent route")


def case_1(out):
    header("Case 1: Symbolic split-safe ledger")
    expected_problem, expected_branch_indexed, expected_neutral, expected_membership, expected_safety, summary_ready, P_insertion, P_active_O, P_residual_kill, P_parent = sp.symbols('expected_problem, expected_branch_indexed, expected_neutral, expected_membership, expected_safety, summary_ready, P_insertion, P_active_O, P_residual_kill, P_parent')
    L_local = sp.simplify(expected_problem + expected_branch_indexed + expected_neutral + expected_membership + expected_safety + summary_ready)
    L_downstream_closed = sp.simplify(P_insertion + P_active_O + P_residual_kill + P_parent)
    L_gap = sp.simplify(L_local + L_downstream_closed)
    print(f"Split-safe local load: L_local = {L_local}")
    print(f"Downstream closed load: L_downstream_closed = {L_downstream_closed}")
    print(f"Total split-safe gap: L_gap = {L_gap}")
    with out.derived_results():
        out.line("symbolic split-safe ledger stated", StatusMark.PASS, f"L_local={L_local}; L_downstream_closed={L_downstream_closed}")


def case_2(out, entries):
    header("Case 2: Split-safe precondition entries")
    for item in entries:
        subheader(item.name)
        print(f"Subject: {item.subject}")
        print(f"Detail: {item.detail}")
        print(f"Boundary: {item.boundary}")
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.detail} Boundary: {item.boundary}")


def case_3(out):
    header("Case 3: Invalid upgrades and shortcuts")
    shortcuts = [
        ('X1: reconciliation as final summary', 'treat this script as group close', 'final summary should be written after actual outputs are reviewed'),
        ('X2: split preconditions as declaration', 'say branch-indexed preconditions completed declarations', 'preconditions are not declarations'),
        ('X3: safety gates as theorems', 'say safety preconditions proved residual/source/divergence safety', 'theorem support remains separate'),
        ('X4: readiness as downstream readiness', 'use precondition audit to open insertion or parent route', 'downstream gates remain closed'),
    ]
    for name, shortcut, reason in shortcuts:
        subheader(name)
        print(f"Shortcut: {shortcut}")
        with out.counterexamples():
            out.line(name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {reason}")


def case_4(out):
    header("Case 4: Open obligations")
    obligations = [
        ('O1: summary must follow actual outputs', 'final summary must report any mismatch in batch outputs', 'actual outputs control close'),
        ('O2: preserve branch-deferred status', 'final summary must keep active branch unchosen unless actual script chose it', 'no choice by summary prose'),
        ('O3: preserve precondition/theorem boundary', 'precondition visibility must not become proof', 'avoid theorem drift'),
    ]
    for name, obligation, discipline in obligations:
        subheader(name)
        print(f"Obligation: {obligation}")
        with out.unresolved_obligations():
            out.line(name, StatusMark.DEFER, f"OPEN: {obligation}; discipline: {discipline}")


def case_5(out):
    header("Case 5: Local conclusions")
    conclusions = [
        ('batch reconciliation prepared', 'PASS', 'write summary only after actual outputs are reviewed'),
        ('no group close here', 'DEFER', 'candidate_group_40_status_summary.py should be written after review'),
    ]
    with out.governance_assessments():
        for name, status, detail in conclusions:
            out.line(name, mark(status), detail)
    print("\nPossible next script:")
    print("  " + 'candidate_group_40_status_summary.py')


def record_governance(ns, entries):
    record_marker(ns, MARKER_ID, MARKER_ID, "Group 40 split-safe trace-anchor precondition audit")
    for idx, item in enumerate(entries, 1):
        record_claim(ns, f"{MARKER_ID}_c{idx}", MARKER_ID, GovernanceStatus.POLICY_RULE, f"{item.name}: {item.subject}. {item.detail} Boundary: {item.boundary}")
    for idx, item in enumerate(entries, 1):
        if item.status in ("OPEN", "DEFER", "CONDITIONAL", "BRANCH_REQUIRED", "NOT_READY"):
            record_obligation(ns, f"{MARKER_ID}_o{idx}", f"Carry forward {item.name} without treating it as branch choice, adoption, theorem proof, insertion, or parent readiness.")


def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    entries = build_entries()
    case_0(out)
    case_1(out)
    case_2(out, entries)
    case_3(out)
    case_4(out)
    case_5(out)
    record_governance(ns, entries)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
