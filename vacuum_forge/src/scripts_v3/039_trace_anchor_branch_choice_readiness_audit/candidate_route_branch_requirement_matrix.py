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

SCRIPT_LABEL = 'Candidate Route Branch Requirement Matrix'
MARKER_ID = 'g39_route_matrix'
DEPENDENCIES = [
    ('g38_summary', '038_trace_anchor_explicit_declaration_record__candidate_group_38_status_summary', 'g38_summary'),
    ('g38_bs_split', '038_trace_anchor_explicit_declaration_record__candidate_Bs_notation_split_declaration', 'g38_bs_split_decl'),
    ('g38_bs_choice', '038_trace_anchor_explicit_declaration_record__candidate_Bs_explicit_branch_choice_sieve', 'g38_bs_branch_choice'),
    ('g37_status_summary', '037_trace_anchor_declaration_option_sieve__candidate_group_37_status_summary', 'g37_status_summary'),
    ('g39_problem', '039_trace_anchor_branch_choice_readiness_audit__candidate_branch_choice_readiness_problem', 'g39_problem'),
]

@dataclass
class Entry:
    name: str
    subject: str
    status: str
    detail: str
    boundary: str


def build_entries() -> List[Entry]:
    raw = [('R1: trace-normalization declaration completion', 'requires active branch to decide log(B_s_metric)=2*zeta/d or log(b_s_scale)=zeta/d', 'BRANCH_REQUIRED', 'cannot complete exact normalization without active branch', 'requirement is not selection'), ('R2: safe-membership declaration completion', 'can partly proceed under split notation if membership object is branch-independent, but joint Package B still needs branch status', 'CONDITIONAL', 'membership fields may be inventoried, but active Package B use requires branch visibility', 'membership is not incidence or insertion'), ('R3: notation-quality source hierarchy', 'can proceed under split notation', 'SPLIT_SAFE', 'rank evidence sources without choosing branch', 'source hierarchy is not declaration'), ('R4: neutral F_zeta bookkeeping', 'can proceed only if no concrete normalization expression is installed', 'NEUTRAL_SAFE', 'use as deferral route', 'neutral placeholder is not hidden branch'), ('R5: explicit adoption decision', 'requires declaration clarity or must explicitly adopt under unresolved branch risk', 'BRANCH_REQUIRED', 'adoption without branch clarity would hide what is adopted', 'adoption remains separate choice'), ('R6: theorem route after declarations', 'requires active branch and explicit assumptions', 'BRANCH_REQUIRED', 'proof target needs fixed objects', 'theorem target is not proof'), ('R7: insertion or parent route', 'not ready even with active branch', 'NOT_READY', 'requires residual, source, divergence, and recombination gates', 'branch choice is insufficient')]
    return [Entry(*item) for item in raw]


def case_0(out):
    header(SCRIPT_LABEL)
    print('Question:\\n')
    for line in 'Which route types require an active B_s branch, which tolerate split notation, and which can only use neutral F_zeta deferral?'.splitlines():
        print("  " + line if line else "")
    print('\\nDiscipline:\\n')
    print('This script classifies route requirements.')
    print('It does not choose any route or branch.')
    print('It does not install a declaration, postulate, theorem, insertion, or parent equation.')
    print('\\nTiny goblin rule:\\n  Sort the doors by key type. Do not open them.')
    with out.governance_assessments():
        out.line(f"{SCRIPT_LABEL} opened", StatusMark.PASS, "branch-readiness audit only; no branch choice, adoption, theorem, insertion, or parent route")


def case_1(out):
    header("Case 1: Symbolic readiness ledger")
    names = ['normalization_route', 'membership_route', 'source_hierarchy', 'neutral_deferral', 'adoption_route', 'theorem_route', 'downstream_route', 'hidden_branch', 'P_insertion', 'P_active_O', 'P_residual_kill', 'P_parent']
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
    header('Case 2: Route branch-requirement matrix')
    for item in entries:
        subheader(item.name)
        print(f"Subject: {item.subject}")
        print(f"Detail: {item.detail}")
        print(f"Boundary: {item.boundary}")
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.detail} Boundary: {item.boundary}")


def case_3(out):
    header("Case 3: Invalid upgrades and shortcuts")
    for name, shortcut, reason in [('X1: branch-independent normalization', 'complete trace normalization while branch remains deferred', 'normalization expression depends on branch'), ('X2: membership licenses branch', 'let membership declaration choose B_s convention', 'nodes remain separate'), ('X3: branch choice licenses downstream', 'treat active branch as insertion-ready', 'residual/source/divergence gates remain unresolved'), ('X4: adoption under hidden branch', 'adopt Package B without stating branch risk', 'adoption must name what is adopted')]:
        subheader(name)
        print(f"Shortcut: {shortcut}")
        with out.counterexamples():
            out.line(name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {reason}")


def case_4(out):
    header("Case 4: Open obligations")
    for name, obligation, blocks, discipline in [('O1: preserve route requirements', 'carry branch-needed versus branch-tolerant classification into handoffs', 'route confusion', 'route requirements do not choose route'), ('O2: keep neutral F_zeta honest', 'do not attach zeta/d or 2*zeta/d to neutral deferral', 'hidden convention', 'neutral means no installed expression'), ('O3: downstream gates', 'keep insertion and parent closure not ready', 'premature field-equation use', 'branch choice is not sufficient')]:
        subheader(name)
        print(f"Obligation: {obligation}")
        with out.unresolved_obligations():
            out.line(name, StatusMark.DEFER, f"OPEN: blocks {blocks}; discipline: {discipline}")


def case_5(out):
    header("Case 5: Local conclusions")
    with out.governance_assessments():
        for name, status, detail in [('route matrix complete', 'PASS', 'split-safe and branch-required routes separated'), ('active branch still deferred', 'DEFER', 'no branch choice made')]:
            out.line(name, mark(status), detail)
    print("\nPossible next script:")
    print(f"  candidate_split_notation_safe_continuation_sieve.py")


def record_governance(ns, entries):
    record_marker(ns, MARKER_ID, f"{MARKER_ID}_marker")
    for idx, item in enumerate(entries, 1):
        record_claim(ns, f"{MARKER_ID}_c{idx}", MARKER_ID, f"{item.name}: {item.subject}. {item.detail} Boundary: {item.boundary}.")
    for idx, item in enumerate([('O1: preserve route requirements', 'carry branch-needed versus branch-tolerant classification into handoffs', 'route confusion', 'route requirements do not choose route'), ('O2: keep neutral F_zeta honest', 'do not attach zeta/d or 2*zeta/d to neutral deferral', 'hidden convention', 'neutral means no installed expression'), ('O3: downstream gates', 'keep insertion and parent closure not ready', 'premature field-equation use', 'branch choice is not sufficient')], 1):
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
