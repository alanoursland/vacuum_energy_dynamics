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

SCRIPT_LABEL = 'Candidate Neutral F_zeta Deferral Boundary'
MARKER_ID = 'g39_fzeta_boundary'
DEPENDENCIES = [
    ('g38_summary', '038_trace_anchor_explicit_declaration_record__candidate_group_38_status_summary', 'g38_summary'),
    ('g38_bs_split', '038_trace_anchor_explicit_declaration_record__candidate_Bs_notation_split_declaration', 'g38_bs_split'),
    ('g38_bs_choice', '038_trace_anchor_explicit_declaration_record__candidate_Bs_explicit_branch_choice_sieve', 'g38_bs_choice'),
    ('g37_summary', '037_trace_anchor_declaration_option_sieve__candidate_group_37_status_summary', 'g37_summary'),
    ('g39_split_safe', '039_trace_anchor_branch_choice_readiness_audit__candidate_split_notation_safe_continuation_sieve', 'g39_split_safe'),
]

@dataclass
class Entry:
    name: str
    subject: str
    status: str
    detail: str
    boundary: str


def build_entries() -> List[Entry]:
    raw = [('F1: neutral placeholder', 'F_zeta may name an unresolved response functional', 'NEUTRAL_SAFE', 'safe if it carries no zeta/d or 2*zeta/d expression', 'placeholder is not declaration'), ('F2: branch-indexed placeholders', 'F_zeta_metric and F_zeta_scale may be named if kept parallel', 'CONDITIONAL', 'safe if explicitly branch-indexed and non-active', 'parallel names are not active choice'), ('F3: concrete normalization', 'any concrete expression requires active branch or parallel explicit branches', 'BRANCH_REQUIRED', 'cannot install one expression under neutral label', 'no hidden factor of two'), ('F4: theorem/adoption route', 'neutral F_zeta cannot support theorem proof or adoption by itself', 'BLOCKED', 'requires declaration/status assumptions', 'neutrality is not support'), ('F5: insertion route', 'not ready', 'NOT_READY', 'neutral F_zeta cannot insert B_s/F_zeta', 'downstream gates closed')]
    return [Entry(*item) for item in raw]


def case_0(out):
    header(SCRIPT_LABEL)
    print('Question:\\n')
    for line in 'What are the exact boundaries on using neutral F_zeta while the active B_s branch remains unchosen?'.splitlines():
        print("  " + line if line else "")
    print('\\nDiscipline:\\n')
    print('This script audits neutral F_zeta deferral.')
    print('It allows neutral bookkeeping only if no branch-specific normalization is installed.')
    print('It adopts nothing, proves nothing, and opens no downstream gate.')
    print('\\nTiny goblin rule:\\n  A blank label is safe only while it stays blank.')
    with out.governance_assessments():
        out.line(f"{SCRIPT_LABEL} opened", StatusMark.PASS, "branch-readiness audit only; no branch choice, adoption, theorem, insertion, or parent route")


def case_1(out):
    header("Case 1: Symbolic readiness ledger")
    names = ['neutral_placeholder', 'branch_indexed_placeholder', 'concrete_norm', 'theorem_adoption_block', 'downstream_block', 'hidden_factor', 'P_insertion', 'P_active_O', 'P_residual_kill', 'P_parent']
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
    header('Case 2: Neutral F_zeta deferral boundary')
    for item in entries:
        subheader(item.name)
        print(f"Subject: {item.subject}")
        print(f"Detail: {item.detail}")
        print(f"Boundary: {item.boundary}")
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.detail} Boundary: {item.boundary}")


def case_3(out):
    header("Case 3: Invalid upgrades and shortcuts")
    for name, shortcut, reason in [('X1: neutral with expression', 'write F_zeta = zeta/d or 2*zeta/d while calling it neutral', 'that hides active branch'), ('X2: neutral as theorem target proof', 'treat neutral placeholder as derived map', 'placeholder is not proof'), ('X3: neutral as insertion', 'insert neutral F_zeta into field equation', 'downstream route not ready')]:
        subheader(name)
        print(f"Shortcut: {shortcut}")
        with out.counterexamples():
            out.line(name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {reason}")


def case_4(out):
    header("Case 4: Open obligations")
    for name, obligation, blocks, discipline in [('O1: preserve empty expression', 'keep neutral F_zeta expression-free until branch choice', 'factor-of-two smuggling', 'neutral means expression-free'), ('O2: mark branch-indexed variants', 'if parallel variants are used, label them explicitly', 'notation drift', 'parallel is not chosen'), ('O3: preserve downstream locks', 'do not treat neutral deferral as insertion', 'downstream overreach', 'neutrality is not theorem')]:
        subheader(name)
        print(f"Obligation: {obligation}")
        with out.unresolved_obligations():
            out.line(name, StatusMark.DEFER, f"OPEN: blocks {blocks}; discipline: {discipline}")


def case_5(out):
    header("Case 5: Local conclusions")
    with out.governance_assessments():
        for name, status, detail in [('neutral F_zeta boundary stated', 'PASS', 'neutral deferral can continue only without installed expression'), ('branch remains deferred', 'DEFER', 'explicit branch choice still needed for completed declaration')]:
            out.line(name, mark(status), detail)
    print("\nPossible next script:")
    print(f"  candidate_branch_choice_blocker_inventory.py")


def record_governance(ns, entries):
    record_marker(ns, MARKER_ID, f"{MARKER_ID}_marker")
    for idx, item in enumerate(entries, 1):
        record_claim(ns, f"{MARKER_ID}_c{idx}", MARKER_ID, f"{item.name}: {item.subject}. {item.detail} Boundary: {item.boundary}.")
    for idx, item in enumerate([('O1: preserve empty expression', 'keep neutral F_zeta expression-free until branch choice', 'factor-of-two smuggling', 'neutral means expression-free'), ('O2: mark branch-indexed variants', 'if parallel variants are used, label them explicitly', 'notation drift', 'parallel is not chosen'), ('O3: preserve downstream locks', 'do not treat neutral deferral as insertion', 'downstream overreach', 'neutrality is not theorem')], 1):
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
