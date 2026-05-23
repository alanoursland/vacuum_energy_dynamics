
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

SCRIPT_LABEL = 'Candidate Safe-Membership Split-Safe Preconditions'
MARKER_ID = 'g40_membership_precond'
DEPENDENCIES = [
    ('g39_summary', '039_trace_anchor_branch_choice_readiness_audit__candidate_group_39_status_summary', 'g39_summary'),
    ('g38_summary', '038_trace_anchor_explicit_declaration_record__candidate_group_38_status_summary', 'g38_summary'),
    ('g40_fzeta_precond', '040_split_safe_trace_anchor_precondition_audit__candidate_neutral_Fzeta_split_safe_preconditions', 'g40_fzeta_precond'),
]


def build_entries() -> List[Entry]:
    return [
        Entry('M1: object slot', 'zeta_Bs object or branch-indexed equivalents', 'CONDITIONAL', 'object may be inventoried if not tied to active branch without declaration', 'object inventory is not membership declaration'),
        Entry('M2: sector slot', 'T_zeta sector definition', 'SPLIT_SAFE', 'sector criteria may be audited branch-independently', 'sector label is not active projector'),
        Entry('M3: domain/codomain and criterion', 'typed membership criteria', 'CONDITIONAL', 'domain/codomain and criterion may be listed as preconditions', 'criterion visibility is not proof'),
        Entry('M4: role-purity exclusions', 'residual/source/correction/boundary/downstream payload exclusions', 'SPLIT_SAFE', 'exclusion zones can be carried as no-hidden-load preconditions', 'role purity is not full source theorem'),
        Entry('M5: active membership', 'active Package B membership claim', 'BRANCH_REQUIRED', 'requires explicit branch/status assumptions before active use', 'not installed here'),
    ]


def case_0(out):
    header(SCRIPT_LABEL)
    print("Question:\n")
    print('Which safe-membership preconditions can be audited while the active B_s branch remains unchosen?')
    print("\nDiscipline:\n")
    print('This script inventories safe-membership preconditions under split notation. It may audit object, sector, criterion, role purity, diagnostic scope, and exclusion zones, but it does not install active membership.')
    print("\nTiny goblin rule:\n  " + 'Name the badge rules. Do not pin the badge.')
    with out.governance_assessments():
        out.line(f"{SCRIPT_LABEL} opened", StatusMark.PASS, "split-safe audit only; no branch choice, declaration completion, adoption, theorem, insertion, or parent route")


def case_1(out):
    header("Case 1: Symbolic split-safe ledger")
    object_slot, sector_slot, criterion_slot, role_purity, diagnostic_scope, branch_tie, P_insertion, P_active_O, P_residual_kill, P_parent = sp.symbols('object_slot, sector_slot, criterion_slot, role_purity, diagnostic_scope, branch_tie, P_insertion, P_active_O, P_residual_kill, P_parent')
    L_local = sp.simplify(object_slot + sector_slot + criterion_slot + role_purity + diagnostic_scope + branch_tie)
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
        ('X1: membership chooses branch', 'let membership object select metric or scale branch', 'nodes remain separate'),
        ('X2: criterion as theorem', 'treat listed criterion as proof of membership', 'precondition is not theorem'),
        ('X3: role purity as source theorem', 'treat exclusion zones as full no-double-counting theorem', 'source theorem remains separate'),
        ('X4: diagnostic as active', 'use diagnostic membership label as active projector', 'diagnostic labels remain inert'),
    ]
    for name, shortcut, reason in shortcuts:
        subheader(name)
        print(f"Shortcut: {shortcut}")
        with out.counterexamples():
            out.line(name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {reason}")


def case_4(out):
    header("Case 4: Open obligations")
    obligations = [
        ('O1: keep membership preconditions explicit', 'carry object/sector/domain/codomain/criterion/role-purity slots visibly', 'avoid hidden membership'),
        ('O2: keep membership branch-neutral only if valid', 'mark any branch-tied membership claim as conditional', 'avoid branch smuggling'),
        ('O3: preserve incidence boundary', 'membership is not trace/residual zero-incidence', 'residual gate remains separate'),
    ]
    for name, obligation, discipline in obligations:
        subheader(name)
        print(f"Obligation: {obligation}")
        with out.unresolved_obligations():
            out.line(name, StatusMark.DEFER, f"OPEN: {obligation}; discipline: {discipline}")


def case_5(out):
    header("Case 5: Local conclusions")
    conclusions = [
        ('membership preconditions inventoried', 'PASS', 'split-safe and conditional membership slots separated'),
        ('active membership not installed', 'DEFER', 'safe membership remains compatible-if-declared'),
    ]
    with out.governance_assessments():
        for name, status, detail in conclusions:
            out.line(name, mark(status), detail)
    print("\nPossible next script:")
    print("  " + 'candidate_residual_source_safety_split_audit.py')


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
