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

SCRIPT_LABEL = 'Candidate Split Notation Safe Continuation Sieve'
MARKER_ID = 'g39_split_safe'
DEPENDENCIES = [
    ('g38_summary', '038_trace_anchor_explicit_declaration_record__candidate_group_38_status_summary', 'g38_summary'),
    ('g38_bs_split', '038_trace_anchor_explicit_declaration_record__candidate_Bs_notation_split_declaration', 'g38_bs_split'),
    ('g38_bs_choice', '038_trace_anchor_explicit_declaration_record__candidate_Bs_explicit_branch_choice_sieve', 'g38_bs_choice'),
    ('g37_summary', '037_trace_anchor_declaration_option_sieve__candidate_group_37_status_summary', 'g37_summary'),
    ('g39_route_matrix', '039_trace_anchor_branch_choice_readiness_audit__candidate_route_branch_requirement_matrix', 'g39_route_matrix'),
]

@dataclass
class Entry:
    name: str
    subject: str
    status: str
    detail: str
    boundary: str


def build_entries() -> List[Entry]:
    raw = [('S1: notation-quality audit', 'safe under split notation', 'SPLIT_SAFE', 'can rank and inspect evidence sources while both branches remain named', 'cannot choose by majority or recovery'), ('S2: route-precondition inventory', 'safe under split notation', 'SPLIT_SAFE', 'can list which route preconditions depend on branch choice', 'preconditions are not declarations'), ('S3: residual/source safety audit', 'conditionally safe if branch-dependent metric-entry claims are not made', 'CONDITIONAL', 'can state general no-hidden-load checks', 'cannot prove branch-specific residual nonentry'), ('S4: membership object inventory', 'conditionally safe if zeta_Bs object is not tied to metric branch', 'CONDITIONAL', 'can inventory object/sector/criterion choices', 'cannot install active Package B membership'), ('S5: exact trace-normalization record', 'not safe under split notation alone', 'BRANCH_REQUIRED', 'needs one active branch or two explicitly parallel records', 'do not complete as single declaration'), ('S6: insertion-facing work', 'not ready', 'NOT_READY', 'branch split is insufficient for insertion', 'downstream gates stay closed')]
    return [Entry(*item) for item in raw]


def case_0(out):
    header(SCRIPT_LABEL)
    print('Question:\\n')
    for line in 'Which investigations can safely continue using B_s_metric and b_s_scale as split notation without choosing an active branch?'.splitlines():
        print("  " + line if line else "")
    print('\\nDiscipline:\\n')
    print('This script sieves branch-independent continuations.')
    print('It preserves the split notation repair.')
    print('It does not complete declarations or select an active branch.')
    print('\\nTiny goblin rule:\\n  Carry both jars only when the road is wide enough.')
    with out.governance_assessments():
        out.line(f"{SCRIPT_LABEL} opened", StatusMark.PASS, "branch-readiness audit only; no branch choice, adoption, theorem, insertion, or parent route")


def case_1(out):
    header("Case 1: Symbolic readiness ledger")
    names = ['safe_notation_audit', 'safe_precondition_audit', 'conditional_safety_audit', 'conditional_membership_inventory', 'branch_needed_norm', 'downstream_block', 'P_insertion', 'P_active_O', 'P_residual_kill', 'P_parent']
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
    header('Case 2: Split-notation safe continuations')
    for item in entries:
        subheader(item.name)
        print(f"Subject: {item.subject}")
        print(f"Detail: {item.detail}")
        print(f"Boundary: {item.boundary}")
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.detail} Boundary: {item.boundary}")


def case_3(out):
    header("Case 3: Invalid upgrades and shortcuts")
    for name, shortcut, reason in [('X1: split-safe as universally safe', 'treat any future route as safe under split notation', 'some routes require active branch'), ('X2: parallel branches as one declaration', 'collapse B_s_metric and b_s_scale back into one active B_s', 'that reintroduces overload'), ('X3: conditional audit as theorem', 'treat branch-independent safety checks as proof', 'theorem support remains separate')]:
        subheader(name)
        print(f"Shortcut: {shortcut}")
        with out.counterexamples():
            out.line(name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {reason}")


def case_4(out):
    header("Case 4: Open obligations")
    for name, obligation, blocks, discipline in [('O1: preserve split labels', 'use B_s_metric and b_s_scale distinctly where both are carried', 'notation collapse', 'two jars stay two jars'), ('O2: mark conditional audits', 'label any branch-dependent claims as conditional', 'overclaim', 'conditional is not proof'), ('O3: block downstream upgrade', 'do not use split notation as insertion readiness', 'downstream overreach', 'split is not field equation')]:
        subheader(name)
        print(f"Obligation: {obligation}")
        with out.unresolved_obligations():
            out.line(name, StatusMark.DEFER, f"OPEN: blocks {blocks}; discipline: {discipline}")


def case_5(out):
    header("Case 5: Local conclusions")
    with out.governance_assessments():
        for name, status, detail in [('split-safe continuations classified', 'PASS', 'safe, conditional, branch-required, and not-ready classes separated'), ('no branch selected', 'DEFER', 'active branch remains deferred')]:
            out.line(name, mark(status), detail)
    print("\nPossible next script:")
    print(f"  candidate_neutral_Fzeta_deferral_boundary.py")


def record_governance(ns, entries):
    record_marker(ns, MARKER_ID, f"{MARKER_ID}_marker")
    for idx, item in enumerate(entries, 1):
        record_claim(ns, f"{MARKER_ID}_c{idx}", MARKER_ID, f"{item.name}: {item.subject}. {item.detail} Boundary: {item.boundary}.")
    for idx, item in enumerate([('O1: preserve split labels', 'use B_s_metric and b_s_scale distinctly where both are carried', 'notation collapse', 'two jars stay two jars'), ('O2: mark conditional audits', 'label any branch-dependent claims as conditional', 'overclaim', 'conditional is not proof'), ('O3: block downstream upgrade', 'do not use split notation as insertion readiness', 'downstream overreach', 'split is not field equation')], 1):
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
