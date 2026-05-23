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
        "DECLARATION_READY": StatusMark.INFO,
        "DECLARATION_OPTION": StatusMark.INFO,
        "DECLARATION_COMPLETED": StatusMark.PASS,
        "DECLARATION_DEFERRED": StatusMark.DEFER,
        "CHOSEN": StatusMark.PASS,
        "NOT_CHOSEN": StatusMark.DEFER,
        "DEFER": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "CONFLICT": StatusMark.FAIL,
        "REJECTED_OPTION": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "NOT_READY": StatusMark.DEFER,
        "COMPATIBLE_IF_DECLARED": StatusMark.INFO,
        "DECLARED_CANDIDATE": StatusMark.PASS,
        "DIAGNOSTIC_ONLY": StatusMark.INFO,
        "POLICY_RULE": StatusMark.OBLIGATION,
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
        scope="Group 38 trace-anchor explicit declaration batch",
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


def record_obligation(ns, obligation_id: str, marker_id: str, statement: str, status=ObligationStatus.OPEN):
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

# Group: 38_trace_anchor_explicit_declaration_record
# Script type: RECONCILIATION
SCRIPT_LABEL = "Candidate Trace Anchor Declaration Batch Reconciliation"
MARKER_ID = "g38_recon"
DEPENDENCIES = [
    ("g38_problem", "38_trace_anchor_explicit_declaration_record__candidate_trace_anchor_declaration_record_problem", "g38_problem"),
    ("g38_bs_fork", "38_trace_anchor_explicit_declaration_record__candidate_Bs_convention_declaration_fork", "g38_bs_fork"),
    ("g38_norm", "38_trace_anchor_explicit_declaration_record__candidate_trace_normalization_declaration_attempt", "g38_norm_decl"),
    ("g38_mem", "38_trace_anchor_explicit_declaration_record__candidate_safe_membership_declaration_attempt", "g38_mem_decl"),
    ("g38_joint", "38_trace_anchor_explicit_declaration_record__candidate_joint_trace_anchor_declaration_record", "g38_joint_decl"),
]

@dataclass
class ReconEntry:
    name: str; expected: str; status: str; consequence: str

def build_entries():
    return [
        ReconEntry("R1: opener", "declaration route opened without choice", "PASS", "matched unless opener claimed adoption/insertion"),
        ReconEntry("R2: B_s fork", "choice may be completed or deferred", "RECONCILE", "summary must report actual branch"),
        ReconEntry("R3: normalization declaration", "completed only if all fields explicit", "RECONCILE", "summary must not assume completion"),
        ReconEntry("R4: membership declaration", "completed only if all fields explicit", "RECONCILE", "summary must not assume completion"),
        ReconEntry("R5: joint declaration", "completed only if exactly one package chosen", "RECONCILE", "otherwise declaration-deferred"),
        ReconEntry("R6: downstream gates", "remain closed", "NOT_READY", "insertion, active O, residual control, and parent closure remain closed"),
    ]

def case_0(out):
    header(SCRIPT_LABEL)
    print("This reconciliation script prepares the actual-output review surface for Group 38.")
    print("It does not close the group and does not write a final summary.")
    with out.governance_assessments(): out.line("declaration batch reconciliation opened", StatusMark.PASS, "summary script should be written only after reviewing actual batch output")

def case_1(out):
    header("Case 1: Symbolic reconciliation ledger")
    problem,bs,norm,mem,joint,mismatch,summary=sp.symbols("problem bs norm mem joint mismatch summary")
    P_insertion,P_active_O,P_residual_kill,P_parent=sp.symbols("P_insertion P_active_O P_residual_kill P_parent")
    L=sp.simplify(problem+bs+norm+mem+joint+mismatch+summary); D=sp.simplify(P_insertion+P_active_O+P_residual_kill+P_parent)
    print(f"L_reconciliation = {L}"); print(f"L_downstream_closed = {D}")
    with out.derived_results(): out.line("declaration batch reconciliation symbolic ledger stated", StatusMark.PASS, f"L_reconciliation={L}; L_downstream_closed={D}")

def case_2(out, entries):
    header("Case 2: Reconciliation checks")
    for e in entries:
        subheader(e.name)
        with out.governance_assessments(): out.line(e.name, mark(e.status), f"Expected: {e.expected}. Consequence: {e.consequence}")

def case_3(out):
    header("Case 3: Invalid reconciliation upgrades")
    for name, reason in [("X1: expected result over actual", "summary must follow actual batch outputs"),("X2: deferred as failed", "declaration-deferred is valid if no choice supplied"),("X3: completed as adopted", "declaration completion is not adoption"),("X4: completed as insertion", "downstream gates remain closed")]:
        with out.counterexamples(): out.line(name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {reason}")

def case_4(out):
    header("Case 4: Local conclusions")
    with out.governance_assessments():
        out.line("batch reconciliation prepared", StatusMark.PASS, "write summary only after actual outputs are reviewed")
        out.line("more exploration may be needed", StatusMark.DEFER, "if declaration remains deferred or convention conflict appears, write follow-up scripts")

def record_governance(ns, entries):
    record_marker(ns, MARKER_ID, "g38_declaration_batch_reconciliation")
    for i,e in enumerate(entries,1): record_claim(ns, f"g38_recon_c{i}", MARKER_ID, GovernanceStatus.POLICY_RULE, f"{e.name}: expected {e.expected}. Status: {e.status}. {e.consequence}.")
    record_obligation(ns, "g38_summary_follow_actual", MARKER_ID, "Group 38 summary must follow actual batch results and report declaration completed, deferred, partial, or conflicted.")

def main():
    archive,ns,invalidated=prepare_archive(DEPENDENCIES); print_archive_status(ns, invalidated)
    out=ScriptOutput(); entries=build_entries(); case_0(out); case_1(out); case_2(out, entries); case_3(out); case_4(out); record_governance(ns, entries); ns.write_run_metadata()
if __name__=="__main__": main()
