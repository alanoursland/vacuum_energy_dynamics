
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

SCRIPT_LABEL = 'Candidate Neutral F_zeta Split-Safe Preconditions'
MARKER_ID = 'g40_fzeta_precond'
DEPENDENCIES = [
    ('g39_summary', '039_trace_anchor_branch_choice_readiness_audit__candidate_group_39_status_summary', 'g39_summary'),
    ('g38_summary', '038_trace_anchor_explicit_declaration_record__candidate_group_38_status_summary', 'g38_summary'),
    ('g40_branch_indexed', '040_split_safe_trace_anchor_precondition_audit__candidate_branch_indexed_precondition_ledger', 'g40_branch_indexed'),
]


def build_entries() -> List[Entry]:
    return [
        Entry('F1: expression-free placeholder', 'F_zeta as neutral response placeholder', 'NEUTRAL_SAFE', 'safe if it carries no concrete zeta/d or 2*zeta/d expression', 'placeholder is not declaration'),
        Entry('F2: branch-indexed variants', 'F_zeta_metric and F_zeta_scale as optional parallel placeholders', 'CONDITIONAL', 'safe if explicitly non-active and paired with branch labels', 'parallel variants are not active choice'),
        Entry('F3: no hidden factor', 'neutral label cannot hide the factor-of-two branch burden', 'POLICY_RULE', 'any concrete expression must be branch-indexed or delayed', 'neutral means expression-free'),
        Entry('F4: no theorem support', 'neutral placeholder cannot prove trace normalization', 'NOT_DERIVED', 'neutrality is not derivation', 'theorem route remains separate'),
        Entry('F5: no insertion support', 'neutral placeholder cannot support B_s/F_zeta insertion', 'NOT_READY', 'insertion remains downstream', 'do not insert placeholder'),
    ]


def case_0(out):
    header(SCRIPT_LABEL)
    print("Question:\n")
    print('What preconditions let neutral F_zeta remain safe while B_s branch choice is deferred?')
    print("\nDiscipline:\n")
    print('This script audits neutral F_zeta preconditions. Neutral F_zeta may remain a placeholder only while expression-free, branch-index-free unless explicitly parallelized, and non-insertable.')
    print("\nTiny goblin rule:\n  " + 'A blank label stays safe only while it stays blank.')
    with out.governance_assessments():
        out.line(f"{SCRIPT_LABEL} opened", StatusMark.PASS, "split-safe audit only; no branch choice, declaration completion, adoption, theorem, insertion, or parent route")


def case_1(out):
    header("Case 1: Symbolic split-safe ledger")
    neutral_placeholder, expression_free, branch_indexed_variants, no_hidden_factor, no_insertion, no_theorem, P_insertion, P_active_O, P_residual_kill, P_parent = sp.symbols('neutral_placeholder, expression_free, branch_indexed_variants, no_hidden_factor, no_insertion, no_theorem, P_insertion, P_active_O, P_residual_kill, P_parent')
    L_local = sp.simplify(neutral_placeholder + expression_free + branch_indexed_variants + no_hidden_factor + no_insertion + no_theorem)
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
        ('X1: neutral with expression', 'write F_zeta = zeta/d while calling it neutral', 'hidden branch choice'),
        ('X2: neutral as proof', 'treat placeholder as derived response map', 'placeholder is not proof'),
        ('X3: neutral as adoption', 'adopt neutral F_zeta as Package B component', 'adoption requires explicit decision'),
        ('X4: neutral as insertion', 'insert neutral response into field equation', 'downstream gates remain closed'),
    ]
    for name, shortcut, reason in shortcuts:
        subheader(name)
        print(f"Shortcut: {shortcut}")
        with out.counterexamples():
            out.line(name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {reason}")


def case_4(out):
    header("Case 4: Open obligations")
    obligations = [
        ('O1: keep F_zeta expression-free', 'do not attach concrete normalization under neutral label', 'blocks factor-of-two smuggling'),
        ('O2: label branch variants', 'if variants are used, mark metric and scale variants explicitly', 'parallel is not chosen'),
        ('O3: preserve non-insertability', 'neutral response placeholder remains non-insertable', 'avoid downstream overreach'),
    ]
    for name, obligation, discipline in obligations:
        subheader(name)
        print(f"Obligation: {obligation}")
        with out.unresolved_obligations():
            out.line(name, StatusMark.DEFER, f"OPEN: {obligation}; discipline: {discipline}")


def case_5(out):
    header("Case 5: Local conclusions")
    conclusions = [
        ('neutral F_zeta preconditions complete', 'PASS', 'expression-free deferral boundary stated'),
        ('branch remains deferred', 'DEFER', 'explicit branch choice still required for completed declaration'),
    ]
    with out.governance_assessments():
        for name, status, detail in conclusions:
            out.line(name, mark(status), detail)
    print("\nPossible next script:")
    print("  " + 'candidate_safe_membership_split_safe_preconditions.py')


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
