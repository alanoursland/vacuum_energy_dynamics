
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

SCRIPT_LABEL = 'Candidate Split-Safe Precondition Problem'
MARKER_ID = 'g40_problem'
DEPENDENCIES = [
    ('g39_summary', '39_trace_anchor_branch_choice_readiness_audit__candidate_group_39_status_summary', 'g39_summary'),
    ('g38_summary', '38_trace_anchor_explicit_declaration_record__candidate_group_38_status_summary', 'g38_summary'),
]


def build_entries() -> List[Entry]:
    return [
        Entry('P1: split-safe audit route', 'precondition work can continue under split notation', 'SPLIT_SAFE', 'route-precondition, notation-quality, and branch-independent safety inventories may continue', 'split-safe is not active branch choice'),
        Entry('P2: branch-indexed requirement', 'branch-dependent claims must use B_s_metric and b_s_scale explicitly', 'BRANCH_INDEXED', 'parallel claims may be carried only when both branches remain labeled', 'parallel branch indexing is not one completed declaration'),
        Entry('P3: neutral F_zeta boundary', 'F_zeta may remain neutral only while expression-free', 'NEUTRAL_SAFE', 'neutral placeholder can defer branch choice if no zeta/d or 2*zeta/d is installed', 'neutrality is not normalization'),
        Entry('P4: membership preconditions', 'safe-membership slots may be audited if not tied to active branch', 'CONDITIONAL', 'object, sector, criterion, role-purity, and exclusion-zone checks may continue', 'membership audit is not membership declaration'),
        Entry('P5: downstream gates', 'insertion, active O, residual control, and parent closure remain closed', 'NOT_READY', 'Group 40 is precondition audit only', 'do not open field-equation routes'),
    ]


def case_0(out):
    header(SCRIPT_LABEL)
    print("Question:\n")
    print('Which trace-anchor precondition audits can proceed under split B_s notation without choosing an active branch?')
    print("\nDiscipline:\n")
    print('This script opens Group 40 as a split-safe trace-anchor precondition audit. It keeps B_s_metric and b_s_scale visible, leaves neutral F_zeta expression-free, fills no declarations, adopts nothing, proves nothing, and opens no downstream gate.')
    print("\nTiny goblin rule:\n  " + 'Carry both jars only where the shelf is labeled for both.')
    with out.governance_assessments():
        out.line(f"{SCRIPT_LABEL} opened", StatusMark.PASS, "split-safe audit only; no branch choice, declaration completion, adoption, theorem, insertion, or parent route")


def case_1(out):
    header("Case 1: Symbolic split-safe ledger")
    split_safe, branch_indexed, neutral_fzeta, membership_preconditions, safety_preconditions, blocked_downstream, P_insertion, P_active_O, P_residual_kill, P_parent = sp.symbols('split_safe, branch_indexed, neutral_fzeta, membership_preconditions, safety_preconditions, blocked_downstream, P_insertion, P_active_O, P_residual_kill, P_parent')
    L_local = sp.simplify(split_safe + branch_indexed + neutral_fzeta + membership_preconditions + safety_preconditions + blocked_downstream)
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
        ('X1: split as choice', 'treat B_s_metric/b_s_scale split as choosing one branch', 'split repairs notation only'),
        ('X2: neutral as expression', 'attach zeta/d or 2*zeta/d to F_zeta while calling it neutral', 'neutral deferral must remain expression-free'),
        ('X3: precondition as theorem', 'treat audited preconditions as solved theorems', 'precondition visibility is not proof'),
        ('X4: precondition as insertion', 'use split-safe audit to open B_s/F_zeta insertion', 'downstream gates remain closed'),
    ]
    for name, shortcut, reason in shortcuts:
        subheader(name)
        print(f"Shortcut: {shortcut}")
        with out.counterexamples():
            out.line(name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {reason}")


def case_4(out):
    header("Case 4: Open obligations")
    obligations = [
        ('O1: preserve branch-deferred status', 'carry no active branch unless a later explicit choice record changes it', 'deferred is valid status'),
        ('O2: preserve branch labels', 'use B_s_metric and b_s_scale distinctly in branch-indexed work', 'do not collapse two jars back into one'),
        ('O3: preserve downstream locks', 'keep insertion and parent closure closed', 'preconditions are not theorem support'),
    ]
    for name, obligation, discipline in obligations:
        subheader(name)
        print(f"Obligation: {obligation}")
        with out.unresolved_obligations():
            out.line(name, StatusMark.DEFER, f"OPEN: {obligation}; discipline: {discipline}")


def case_5(out):
    header("Case 5: Local conclusions")
    conclusions = [
        ('Group 40 opener complete', 'PASS', 'branch-indexed precondition ledger should run next'),
        ('no branch chosen', 'DEFER', 'active branch remains declaration-deferred'),
    ]
    with out.governance_assessments():
        for name, status, detail in conclusions:
            out.line(name, mark(status), detail)
    print("\nPossible next script:")
    print("  " + 'candidate_branch_indexed_precondition_ledger.py')


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
