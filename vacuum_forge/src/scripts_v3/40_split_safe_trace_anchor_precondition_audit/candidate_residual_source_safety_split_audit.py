
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

SCRIPT_LABEL = 'Candidate Residual Source Safety Split Audit'
MARKER_ID = 'g40_safety_split'
DEPENDENCIES = [
    ('g39_summary', '39_trace_anchor_branch_choice_readiness_audit__candidate_group_39_status_summary', 'g39_summary'),
    ('g38_summary', '38_trace_anchor_explicit_declaration_record__candidate_group_38_status_summary', 'g38_summary'),
    ('g40_membership_precond', '40_split_safe_trace_anchor_precondition_audit__candidate_safe_membership_split_safe_preconditions', 'g40_membership_precond'),
]


def build_entries() -> List[Entry]:
    return [
        Entry('S1: residual nonentry precondition', 'residual zeta/kappa metric re-entry remains blocked as theorem target', 'CONDITIONAL', 'general nonentry checks can be listed without branch-specific proof', 'not residual-kill theorem'),
        Entry('S2: source visibility precondition', 'ordinary source load must remain visible and not hidden in branch notation', 'SPLIT_SAFE', 'no-hidden-source rule applies to both branches', 'not full source no-double-counting theorem'),
        Entry('S3: divergence explicitness precondition', 'divergence/correction terms must remain explicit and non-reservoir', 'SPLIT_SAFE', 'explicitness guard applies branch-independently', 'not divergence-safe coefficient law'),
        Entry('S4: boundary/support visibility', 'boundary and support loads must remain visible', 'SPLIT_SAFE', 'branch notation cannot hide shell/source/support terms', 'visibility is not neutrality theorem'),
        Entry('S5: branch-specific metric entry', 'branch-specific metric-entry claims require active branch assumptions', 'BRANCH_REQUIRED', 'cannot prove metric entry safety generically from split notation alone', 'branch readiness is not insertion'),
    ]


def case_0(out):
    header(SCRIPT_LABEL)
    print("Question:\n")
    print('Which residual/source safety checks can be stated under split notation without branch-specific metric-entry claims?')
    print("\nDiscipline:\n")
    print('This script audits general no-hidden-load safety preconditions under split notation. It does not prove residual nonentry, source no-double-counting, divergence safety, or insertion readiness.')
    print("\nTiny goblin rule:\n  " + 'Check the sacks for stolen coins. Do not spend them.')
    with out.governance_assessments():
        out.line(f"{SCRIPT_LABEL} opened", StatusMark.PASS, "split-safe audit only; no branch choice, declaration completion, adoption, theorem, insertion, or parent route")


def case_1(out):
    header("Case 1: Symbolic split-safe ledger")
    residual_nonentry, source_visibility, divergence_explicitness, boundary_visibility, metric_entry_block, downstream_lock, P_insertion, P_active_O, P_residual_kill, P_parent = sp.symbols('residual_nonentry, source_visibility, divergence_explicitness, boundary_visibility, metric_entry_block, downstream_lock, P_insertion, P_active_O, P_residual_kill, P_parent')
    L_local = sp.simplify(residual_nonentry + source_visibility + divergence_explicitness + boundary_visibility + metric_entry_block + downstream_lock)
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
        ('X1: safety precondition as theorem', 'call visibility rules residual/source/divergence theorems', 'preconditions are not solved theorems'),
        ('X2: branch-independent metric entry', 'claim metric-entry safety without branch assumptions', 'branch-specific metric-entry needs explicit setup'),
        ('X3: source hidden in branch', 'hide source or boundary load in B_s_metric/b_s_scale naming', 'branch labels are not reservoirs'),
        ('X4: safety audit as insertion', 'treat general safety checks as B_s/F_zeta insertion', 'downstream gates remain closed'),
    ]
    for name, shortcut, reason in shortcuts:
        subheader(name)
        print(f"Shortcut: {shortcut}")
        with out.counterexamples():
            out.line(name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {reason}")


def case_4(out):
    header("Case 4: Open obligations")
    obligations = [
        ('O1: keep safety gates as gates', 'do not report safety preconditions as solved theorems', 'avoid theorem drift'),
        ('O2: keep source/divergence visible', 'ordinary source and divergence loads must remain auditable under both branches', 'avoid reservoirs'),
        ('O3: keep downstream closed', 'do not open insertion or parent closure from split safety audit', 'field-equation use remains not ready'),
    ]
    for name, obligation, discipline in obligations:
        subheader(name)
        print(f"Obligation: {obligation}")
        with out.unresolved_obligations():
            out.line(name, StatusMark.DEFER, f"OPEN: {obligation}; discipline: {discipline}")


def case_5(out):
    header("Case 5: Local conclusions")
    conclusions = [
        ('residual/source safety split audit complete', 'PASS', 'branch-independent safety gates inventoried'),
        ('branch-specific metric-entry proof not supplied', 'DEFER', 'active branch and later theorem support remain required'),
    ]
    with out.governance_assessments():
        for name, status, detail in conclusions:
            out.line(name, mark(status), detail)
    print("\nPossible next script:")
    print("  " + 'candidate_split_safe_precondition_batch_reconciliation.py')


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
