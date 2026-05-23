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
        "READY": StatusMark.PASS,
        "HANDOFF_READY": StatusMark.PASS,
        "BRANCH_REQUIRED": StatusMark.OBLIGATION,
        "BRANCH_NOT_REQUIRED": StatusMark.INFO,
        "SPLIT_SAFE": StatusMark.INFO,
        "NEUTRAL_SAFE": StatusMark.INFO,
        "CONDITIONAL": StatusMark.DEFER,
        "DEFER": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "BLOCKED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "REJECTED": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "INFO": StatusMark.INFO,
    }.get(status, StatusMark.INFO)


def record_marker(ns, marker_id: str, symbol_name: str):
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[],
        output=sp.Symbol(symbol_name),
        method="inventory marker; no physical derivation",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
        scope="Group 39 trace-anchor branch-choice readiness audit",
    )


def record_claim(ns, claim_id: str, marker_id: str, statement: str, status=GovernanceStatus.POLICY_RULE):
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


def record_obligation(ns, obligation_id: str, marker_id: str, description: str, status=ObligationStatus.OPEN):
    ns.record_obligation(
        ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=obligation_id,
            status=status,
            required_by=[SCRIPT_ID],
            description=description,
        )
    )

# Group:
#   39_trace_anchor_branch_choice_readiness_audit
# Script type:
#   AUDIT / SIEVE

SCRIPT_LABEL = 'Candidate Branch Choice Readiness Problem'
MARKER_ID = 'g39_problem'
DEPENDENCIES = [
    ('g38_summary', '038_trace_anchor_explicit_declaration_record__candidate_group_38_status_summary', 'g38_summary'),
    ('g38_bs_split', '038_trace_anchor_explicit_declaration_record__candidate_Bs_notation_split_declaration', 'g38_bs_split'),
    ('g38_bs_choice', '038_trace_anchor_explicit_declaration_record__candidate_Bs_explicit_branch_choice_sieve', 'g38_bs_choice'),
    ('g37_summary', '037_trace_anchor_declaration_option_sieve__candidate_group_37_status_summary', 'g37_summary'),
]

@dataclass
class Entry:
    name: str
    subject: str
    status: str
    detail: str
    boundary: str


def build_entries() -> List[Entry]:
    raw = [('P1: active-branch need', 'some future routes require metric_coefficient or scale_factor to be chosen', 'BRANCH_REQUIRED', 'completed trace-normalization declaration and joint Package B declaration require an active branch', 'requirement is not selection'), ('P2: split-notation continuation', 'some audits can proceed with B_s_metric and b_s_scale both visible', 'SPLIT_SAFE', 'notation-quality, route-safety, and branch-independent audits can continue under split notation', 'split is not active declaration'), ('P3: neutral F_zeta deferral', 'F_zeta may remain a neutral placeholder only if it installs no concrete normalization', 'NEUTRAL_SAFE', 'neutrality can preserve deferral without hiding zeta/d or 2*zeta/d', 'neutrality is not convention choice'), ('P4: downstream gates', 'insertion, active O, residual control, and parent closure remain closed', 'NOT_READY', 'branch readiness does not make field-equation routes ready', 'do not open downstream gates')]
    return [Entry(*item) for item in raw]


def case_0(out):
    header(SCRIPT_LABEL)
    print('Question:\\n')
    for line in 'Which future trace-anchor routes require an active B_s branch choice, and which can proceed under split notation or neutral F_zeta deferral?'.splitlines():
        print("  " + line if line else "")
    print('\\nDiscipline:\\n')
    print('This script opens Group 39 as a branch-choice readiness audit.')
    print('It does not choose metric_coefficient or scale_factor.')
    print('It does not fill trace-normalization or safe-membership declarations.')
    print('It adopts nothing, proves nothing, and opens no downstream gate.')
    print('\\nTiny goblin rule:\\n  Check which doors need a key. Do not pick the key.')
    with out.governance_assessments():
        out.line(f"{SCRIPT_LABEL} opened", StatusMark.PASS, "branch-readiness audit only; no branch choice, adoption, theorem, insertion, or parent route")


def case_1(out):
    header("Case 1: Symbolic readiness ledger")
    names = ['branch_required', 'branch_optional', 'split_safe', 'neutral_Fzeta', 'blocked_route', 'hidden_choice', 'P_insertion', 'P_active_O', 'P_residual_kill', 'P_parent']
    syms = sp.symbols(" ".join(names))
    mapping = dict(zip(names, syms))
    for name in names:
        print(f"  {name} = {mapping[name]}")
    local_names = [n for n in names if not n.startswith("P_")]
    downstream_names = ["P_insertion", "P_active_O", "P_residual_kill", "P_parent"]
    L_local = sp.simplify(sum(mapping[n] for n in local_names))
    L_downstream = sp.simplify(sum(mapping[n] for n in downstream_names if n in mapping))
    L_gap = sp.simplify(L_local + L_downstream)
    print(f"Readiness local load: L_local = {L_local}")
    print(f"Downstream closed load: L_downstream_closed = {L_downstream}")
    print(f"Total readiness gap: L_gap = {L_gap}")
    with out.derived_results():
        out.line("symbolic readiness ledger stated", StatusMark.PASS, f"L_local={L_local}; L_downstream_closed={L_downstream}")


def case_2(out, entries):
    header('Case 2: Branch-choice readiness problem classes')
    for item in entries:
        subheader(item.name)
        print(f"Subject: {item.subject}")
        print(f"Detail: {item.detail}")
        print(f"Boundary: {item.boundary}")
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.detail} Boundary: {item.boundary}")


def case_3(out):
    header("Case 3: Invalid upgrades and shortcuts")
    for name, shortcut, reason in [('X1: readiness as choice', 'treat branch-required classification as choosing a branch', 'readiness inventory is not branch choice'), ('X2: split as declaration', 'use B_s_metric/b_s_scale split as if one branch is active', 'split repairs notation only'), ('X3: neutral F_zeta as hidden branch', 'use F_zeta to proceed with zeta/d or 2*zeta/d without choosing', 'neutral notation cannot hide factor-of-two burden'), ('X4: readiness as insertion', 'treat branch-readiness clarity as B_s/F_zeta insertion', 'downstream gates remain closed')]:
        subheader(name)
        print(f"Shortcut: {shortcut}")
        with out.counterexamples():
            out.line(name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {reason}")


def case_4(out):
    header("Case 4: Open obligations")
    for name, obligation, blocks, discipline in [('O1: preserve branch deferred status', 'carry no-active-branch status unless a later explicit choice record changes it', 'hidden branch selection', 'deferred is valid status'), ('O2: classify routes by branch need', 'state whether each future route requires branch choice, split notation, or neutral deferral', 'route drift', 'classification does not select route'), ('O3: preserve downstream locks', 'keep insertion, active O, residual control, and parent closure closed', 'downstream overreach', 'readiness is not theorem support')]:
        subheader(name)
        print(f"Obligation: {obligation}")
        with out.unresolved_obligations():
            out.line(name, StatusMark.DEFER, f"OPEN: blocks {blocks}; discipline: {discipline}")


def case_5(out):
    header("Case 5: Local conclusions")
    with out.governance_assessments():
        for name, status, detail in [('Group 39 opener complete', 'PASS', 'route-requirement matrix should run next'), ('no branch chosen', 'DEFER', 'active branch remains declaration-deferred')]:
            out.line(name, mark(status), detail)
    print("\nPossible next script:")
    print(f"  candidate_route_branch_requirement_matrix.py")


def record_governance(ns, entries):
    record_marker(ns, MARKER_ID, f"{MARKER_ID}_marker")
    for idx, item in enumerate(entries, 1):
        record_claim(ns, f"{MARKER_ID}_c{idx}", MARKER_ID, f"{item.name}: {item.subject}. {item.detail} Boundary: {item.boundary}.")
    for idx, item in enumerate([('O1: preserve branch deferred status', 'carry no-active-branch status unless a later explicit choice record changes it', 'hidden branch selection', 'deferred is valid status'), ('O2: classify routes by branch need', 'state whether each future route requires branch choice, split notation, or neutral deferral', 'route drift', 'classification does not select route'), ('O3: preserve downstream locks', 'keep insertion, active O, residual control, and parent closure closed', 'downstream overreach', 'readiness is not theorem support')], 1):
        record_obligation(ns, f"{MARKER_ID}_o{idx}", MARKER_ID, f"{item[1]} Blocks: {item[2]} Discipline: {item[3]}")


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
