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
# Script type: RECONCILIATION / DECLARATION ATTEMPT
SCRIPT_LABEL = "Candidate Joint Trace Anchor Declaration Record"
MARKER_ID = "g38_joint_decl"
DEPENDENCIES = [
    ("g38_problem", "038_trace_anchor_explicit_declaration_record__candidate_trace_anchor_declaration_record_problem", "g38_problem"),
    ("g38_bs_fork", "038_trace_anchor_explicit_declaration_record__candidate_Bs_convention_declaration_fork", "g38_bs_fork"),
    ("g38_norm_decl", "038_trace_anchor_explicit_declaration_record__candidate_trace_normalization_declaration_attempt", "g38_norm_decl"),
    ("g38_mem", "038_trace_anchor_explicit_declaration_record__candidate_safe_membership_declaration_attempt", "g38_mem_decl"),
]
# This switch lets a user install exactly one named package after editing the file.
# allowed: "scale_rolepure", "metric_rolepure", "scale_typed", "metric_typed", or None
CHOSEN_PACKAGE = None

@dataclass
class JointEntry:
    name: str; package: str; status: str; consequence: str

def build_entries():
    names = ["scale_typed", "metric_typed", "scale_rolepure", "metric_rolepure"]
    entries = [JointEntry(f"J{i+1}: {name}", name, "CHOSEN" if CHOSEN_PACKAGE==name else "DECLARATION_READY", "eligible package; not selected unless CHOSEN") for i,name in enumerate(names)]
    entries += [
        JointEntry("J5: no package chosen", "None", "DECLARATION_DEFERRED" if CHOSEN_PACKAGE is None else "NOT_CHOSEN", "valid if declaration decision is not ready"),
        JointEntry("J6: package conflict", "multiple", "CONFLICT", "invalid if more than one package is treated as chosen"),
    ]
    return entries

def case_0(out):
    header(SCRIPT_LABEL); print(f"CHOSEN_PACKAGE={CHOSEN_PACKAGE!r}")
    print("This script combines component declaration attempts into a joint declaration surface only if exactly one package is explicitly chosen.")
    with out.governance_assessments(): out.line("joint declaration record attempt opened", StatusMark.PASS, "choice-tolerant; may close as deferred")

def case_1(out):
    header("Case 1: Symbolic joint declaration ledger")
    norm,mem,node_sep,chosen,deferred,conflict=sp.symbols("norm mem node_sep chosen deferred conflict")
    P_insertion,P_active_O,P_residual_kill,P_parent=sp.symbols("P_insertion P_active_O P_residual_kill P_parent")
    L=sp.simplify(norm+mem+node_sep+chosen+deferred+conflict); D=sp.simplify(P_insertion+P_active_O+P_residual_kill+P_parent)
    print(f"L_joint_declaration = {L}"); print(f"L_downstream_closed = {D}")
    with out.derived_results(): out.line("joint declaration symbolic ledger stated", StatusMark.PASS, f"L_joint_declaration={L}; L_downstream_closed={D}")

def case_2(out, entries):
    header("Case 2: Joint package declaration outcomes")
    for e in entries:
        subheader(e.name); print(f"Package: {e.package}")
        with out.governance_assessments(): out.line(e.name, mark(e.status), f"{e.status}: {e.consequence}")

def case_3(out):
    header("Case 3: Invalid joint declaration upgrades")
    for name, reason in [("X1: declaration-ready as chosen", "eligible package is not selected without explicit CHOSEN_PACKAGE"),("X2: one component licenses the other", "nodes remain separate"),("X3: declared candidate as adopted", "adoption separate"),("X4: declared candidate as insertion", "downstream gates closed")]:
        with out.counterexamples(): out.line(name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {reason}")

def case_4(out, entries):
    header("Case 4: Local conclusions")
    completed = CHOSEN_PACKAGE in ["scale_typed", "metric_typed", "scale_rolepure", "metric_rolepure"]
    with out.governance_assessments():
        out.line("joint declaration attempt result", StatusMark.PASS if completed else StatusMark.DEFER, "DECLARATION_COMPLETED" if completed else "DECLARATION_DEFERRED")
        out.line("no adoption/theorem/insertion", StatusMark.DEFER, "declared candidate surface, if any, remains non-adopted and non-derived")

def record_governance(ns, entries):
    record_marker(ns, MARKER_ID, "g38_joint_trace_anchor_declaration_attempt")
    for i,e in enumerate(entries,1): record_claim(ns, f"g38_joint_c{i}", MARKER_ID, GovernanceStatus.POLICY_RULE, f"{e.name}: package={e.package}. Status: {e.status}. {e.consequence}.")
    record_obligation(ns, "g38_joint_choose_one_or_defer", MARKER_ID, "Joint declaration requires exactly one explicit package choice; otherwise declaration remains deferred.")

def main():
    archive,ns,invalidated=prepare_archive(DEPENDENCIES); print_archive_status(ns, invalidated)
    out=ScriptOutput(); entries=build_entries(); case_0(out); case_1(out); case_2(out, entries); case_3(out); case_4(out, entries); record_governance(ns, entries); ns.write_run_metadata()
if __name__=="__main__": main()
