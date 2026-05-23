from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List
import sympy as sp
from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    ClaimRecord, ClaimTier, GovernanceStatus, ObligationStatus,
    ProofObligationRecord, RecordKind, ScriptOutput, StatusMark,
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
    print(); print("="*120); print(title); print("="*120)

def subheader(title: str) -> None:
    print(); print("-"*120); print(title); print("-"*120)

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
        print("[INFO] Archive dependencies: none declared."); return
    print("[INFO] Archive dependency check:")
    for check in checks:
        print(f"  - {check.dependency.dependency_id}: {check.status} ({check.message})")

def mark(status: str) -> StatusMark:
    return {
        "PASS": StatusMark.PASS, "MATCHED_EXPECTATION": StatusMark.PASS,
        "SYMBOLIC_PAIRED_DECLARATION_ATTEMPT": StatusMark.INFO,
        "CONDITIONAL_DECLARATION_ATTEMPT_STATED": StatusMark.INFO,
        "DECLARATION_ATTEMPT_CONDITIONAL_ONLY": StatusMark.INFO,
        "DECLARATION_ATTEMPT_SURVIVES_WITH_CONDITIONS": StatusMark.INFO,
        "DECLARATION_RECORD_FIELD": StatusMark.INFO,
        "PAIRED_BRANCH_DOMAIN": StatusMark.INFO,
        "EXPRESSION_SEPARATION": StatusMark.INFO,
        "SYMBOLIC_D_ALLOWED": StatusMark.INFO,
        "ZETA_CLAUSE": StatusMark.INFO,
        "CAVEAT_FIELD": StatusMark.INFO,
        "NON_ACTIVE": StatusMark.INFO,
        "BRANCH_INDEXED": StatusMark.INFO,
        "NUMERIC_D_CONDITION": StatusMark.OBLIGATION,
        "CONSISTENCY_RULE": StatusMark.OBLIGATION,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "DECLARATION_ATTEMPT_FAILED": StatusMark.FAIL,
        "REJECTED_ROUTE": StatusMark.FAIL, "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "AXIOM_REQUIRED": StatusMark.DEFER, "CHOICE_REQUIRED": StatusMark.DEFER,
        "THEOREM_REQUIRED": StatusMark.DEFER, "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "NOT_DECLARED": StatusMark.DEFER, "NOT_CHOSEN": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER, "NOT_READY": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER, "OPEN": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)

def obligation_status(status: str) -> ObligationStatus:
    if status in {"NOT_READY","NOT_DECLARED","NOT_CHOSEN","NOT_ADOPTED","NOT_DERIVED","DEFERRED_WITH_TARGET","THEOREM_REQUIRED","AXIOM_REQUIRED","CHOICE_REQUIRED"}:
        return ObligationStatus.DEFERRED
    return ObligationStatus.OPEN

def governance_status(status: str) -> GovernanceStatus:
    if status in {"FORBIDDEN_SHORTCUT","REJECTED_ROUTE","DECLARATION_ATTEMPT_FAILED"}:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {"NOT_READY","NOT_DECLARED","NOT_CHOSEN","NOT_ADOPTED","NOT_DERIVED","DEFERRED_WITH_TARGET","OPEN","THEOREM_REQUIRED","AXIOM_REQUIRED","CHOICE_REQUIRED"}:
        return GovernanceStatus.UNVERIFIED
    return GovernanceStatus.POLICY_RULE

def record_marker(ns, marker_id: str, scope: str) -> None:
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[],
        output=sp.Symbol(marker_id),
        method="inventory marker; no physical derivation",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
        scope=scope,
    )

def record_claim(ns, claim_id: str, marker_id: str, status: str, statement: str) -> None:
    ns.record_claim(ClaimRecord(
        claim_id=claim_id, script_id=SCRIPT_ID, claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED, status=governance_status(status), statement=statement,
        derivation_ids=[marker_id], obligation_ids=[]))

def record_obligation(ns, obligation_id: str, title: str, statement: str, status: str = "OPEN") -> None:
    ns.record_obligation(ProofObligationRecord(
        obligation_id=obligation_id, script_id=SCRIPT_ID, title=title,
        status=obligation_status(status), required_by=[SCRIPT_ID], description=statement))

def print_entries(out: ScriptOutput, entries: List[Entry], title: str) -> None:
    header(title)
    for item in entries:
        subheader(item.name)
        print(f"Subject: {item.subject}")
        print(f"Detail: {item.detail}")
        print(f"Boundary: {item.boundary}")
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.detail}. Boundary: {item.boundary}")

def print_shortcuts(out: ScriptOutput, shortcuts: List[Shortcut]) -> None:
    header("Invalid upgrades and forbidden shortcuts")
    for item in shortcuts:
        subheader(item.name)
        print(f"Shortcut: {item.shortcut}")
        with out.counterexamples():
            out.line(item.name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {item.reason}")

def print_obligations(out: ScriptOutput, obligations: List[ObligationEntry]) -> None:
    header("Open obligations")
    for item in obligations:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        with out.unresolved_obligations():
            out.line(item.name, mark(item.status), f"{item.status}: {item.obligation}; discipline: {item.discipline}")

def record_governance(ns, marker_id: str, entries: List[Entry], obligations: List[ObligationEntry], scope: str) -> None:
    record_marker(ns, marker_id, scope)
    for idx, item in enumerate(entries, 1):
        record_claim(ns, f"{marker_id}_c{idx}", marker_id, item.status, f"{item.name}: {item.subject}. {item.detail}. Boundary: {item.boundary}.")
    for idx, item in enumerate(obligations, 1):
        record_obligation(ns, f"{marker_id}_o{idx}", item.name, f"{item.obligation}. Discipline: {item.discipline}.", item.status)

# Group: 50_symbolic_paired_trace_normalization_declaration_attempt
SCRIPT_LABEL = 'Candidate Paired Declaration Attempt Record'
MARKER_ID = 'g50_attempt_record'
DEPENDENCIES = [('g49_summary', '049_parallel_trace_declaration_readiness_review__candidate_group_49_status_summary', 'g49_summary'), ('g50_problem', '050_symbolic_paired_trace_normalization_declaration_attempt__candidate_symbolic_paired_declaration_attempt_problem', 'g50_problem')]
QUESTION = 'What does the paired symbolic declaration-attempt record actually state?'
DISCIPLINE = 'This script states the declaration-attempt record fields. It does not turn the attempt into adoption or field-equation use.'
OPENING_LINE = 'Paired declaration-attempt record opened -- record only; no adoption or insertion'
SCOPE = 'Group 50 paired declaration attempt record'
NEXT_SCRIPT = 'candidate_declaration_expression_separation_audit.py'
LOCAL_CONCLUSIONS = [('attempt record stated', 'PASS', 'paired symbolic attempt record fields stated'), ('not an adopted declaration', 'NOT_ADOPTED', 'attempt remains pre-adoption')]

def build_entries() -> List[Entry]:
    return [
        Entry('R1: artifact identity', 'symbolic paired trace-normalization declaration attempt', 'DECLARATION_RECORD_FIELD', 'the record identifies itself as an attempt under conditions', 'not adoption'),
        Entry('R2: metric-side candidate', 'log(B_s_metric)=2*zeta/d', 'BRANCH_INDEXED', 'metric expression is listed as branch-indexed candidate', 'not selected branch'),
        Entry('R3: scale-side candidate', 'log(b_s_scale)=zeta/d', 'BRANCH_INDEXED', 'scale expression is listed as branch-indexed candidate', 'not selected branch'),
        Entry('R4: symbolic mode', 'symbolic d and shared zeta are carried from prior records', 'SYMBOLIC_D_ALLOWED', 'the attempt remains symbolic and scope-conditioned', 'not numeric closure'),
        Entry('R5: caveat mode', 'non-insertion / non-parent caveats remain attached', 'CAVEAT_FIELD', 'attempt status carries downstream non-use', 'not field-equation use'),
    ]

def build_shortcuts() -> List[Shortcut]:
    return [
        Shortcut('X1: one-expression record', 'write only one unqualified B_s expression', 'that hides branch dependence'),
        Shortcut('X2: omitted caveats', 'leave caveats implicit', 'omission invites insertion and parent drift'),
        Shortcut('X3: adopted attempt', 'treat the attempt record as adopted Package B', 'adoption remains separate'),
        Shortcut('X4: numeric d hidden', 'bury numeric d in prose', 'numeric d must remain conditioned'),
    ]

def build_obligations() -> List[ObligationEntry]:
    return [
        ObligationEntry('O1: keep record complete', 'POLICY_RULE', 'future summaries must preserve identity, paired expressions, symbolic mode, and caveats', 'avoid hidden assumptions'),
        ObligationEntry('O2: preserve non-adoption', 'NOT_ADOPTED', 'do not convert attempt record into Package B adoption', 'avoid adoption drift'),
        ObligationEntry('O3: preserve numeric condition', 'NUMERIC_D_CONDITION', 'numeric d remains conditioned and unfixed', 'avoid hidden numeric declaration'),
    ]

def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    header(SCRIPT_LABEL)
    print("Question:\n")
    print(QUESTION)
    print("\nDiscipline:\n")
    print(DISCIPLINE)
    with out.governance_assessments():
        out.line(f"{SCRIPT_LABEL} opened", StatusMark.PASS, OPENING_LINE)
    entries = build_entries(); shortcuts = build_shortcuts(); obligations = build_obligations()
    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)
    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)
    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    ns.write_run_metadata()
    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")

if __name__ == "__main__":
    main()
