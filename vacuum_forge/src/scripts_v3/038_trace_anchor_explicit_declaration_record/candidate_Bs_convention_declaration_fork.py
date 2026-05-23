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
# Script type: SIEVE / AUDIT
SCRIPT_LABEL = "Candidate B_s Convention Declaration Fork"
MARKER_ID = "g38_bs_fork"
DEPENDENCIES = [
    ("g38_problem", "038_trace_anchor_explicit_declaration_record__candidate_trace_anchor_declaration_record_problem", "g38_problem"),
    ("g37_status_summary", "037_trace_anchor_declaration_option_sieve__candidate_group_37_status_summary", "g37_status_summary"),
]
CHOSEN_CONVENTION = None  # allowed: "scale_factor", "metric_coefficient", or None

@dataclass
class ConventionEntry:
    name: str; convention: str; status: str; meaning: str; blocked_if: str; consequence: str

def build_entries() -> List[ConventionEntry]:
    chosen = CHOSEN_CONVENTION
    return [
        ConventionEntry("B1: scale-factor convention", "B_s is a scale factor; log(B_s)=zeta/d", "CHOSEN" if chosen=="scale_factor" else "DECLARATION_READY", "coherent if B_s denotes scale factor response", "B_s is actually metric coefficient or factor chosen from recovery", "eligible declaration branch"),
        ConventionEntry("B2: metric-coefficient convention", "B_s is metric coefficient language; log(B_s)=2*zeta/d", "CHOSEN" if chosen=="metric_coefficient" else "DECLARATION_READY", "coherent if B_s denotes the metric coefficient rather than its square-root scale", "factor of two is hidden or chosen from recovery", "eligible declaration branch"),
        ConventionEntry("B3: no convention chosen", "leave B_s convention uninstalled", "DECLARATION_DEFERRED" if chosen is None else "NOT_CHOSEN", "valid conservative outcome if notation is not ready", "later scripts pretend convention is filled", "batch may close as deferred"),
        ConventionEntry("B4: both conventions chosen", "both scale and metric conventions installed", "CONFLICT", "invalid unless explicitly separated into different named notations", "same B_s symbol receives two meanings", "requires repair script if it occurs"),
    ]

def case_0(out):
    header(SCRIPT_LABEL)
    print(f"Configured CHOSEN_CONVENTION = {CHOSEN_CONVENTION!r}")
    print("Allowed values are 'scale_factor', 'metric_coefficient', or None.")
    print("This script explores the fork and may leave the choice deferred.")
    with out.governance_assessments():
        out.line("B_s convention fork opened", StatusMark.PASS, "no automatic convention selection")

def case_1(out):
    header("Case 1: Symbolic B_s convention ledger")
    B_scale, B_metric, B_defer, B_conflict = sp.symbols("B_scale B_metric B_defer B_conflict")
    P_insertion, P_active_O, P_residual_kill, P_parent = sp.symbols("P_insertion P_active_O P_residual_kill P_parent")
    L = sp.simplify(B_scale + B_metric + B_defer + B_conflict)
    D = sp.simplify(P_insertion + P_active_O + P_residual_kill + P_parent)
    print(f"L_Bs_convention = {L}")
    print(f"L_downstream_closed = {D}")
    with out.derived_results(): out.line("B_s convention symbolic ledger stated", StatusMark.PASS, f"L_Bs_convention={L}; L_downstream_closed={D}")

def case_2(out, entries):
    header("Case 2: Convention branches")
    for e in entries:
        subheader(e.name); print(f"Convention: {e.convention}")
        with out.governance_assessments(): out.line(e.name, mark(e.status), f"{e.status}: {e.meaning}. Blocked if: {e.blocked_if}. Consequence: {e.consequence}")

def case_3(out):
    header("Case 3: Invalid convention shortcuts")
    for name, reason in [("X1: hidden factor", "must not hide scale-vs-metric factor of two"),("X2: recovery-selected convention", "recovery is audit, not declaration source"),("X3: convention as adoption", "convention declaration is not postulate adoption"),("X4: convention as insertion", "B_s/F_zeta insertion remains not ready")]:
        subheader(name)
        with out.counterexamples(): out.line(name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {reason}")

def case_4(out):
    header("Case 4: Local conclusions")
    status = "DECLARATION_DEFERRED" if CHOSEN_CONVENTION is None else "DECLARATION_OPTION"
    with out.governance_assessments():
        out.line("B_s convention fork classified", mark(status), f"chosen convention: {CHOSEN_CONVENTION!r}")
        out.line("downstream gates closed", StatusMark.DEFER, "convention classification is not insertion or parent readiness")

def record_governance(ns, entries):
    record_marker(ns, MARKER_ID, "g38_bs_convention_fork")
    for i,e in enumerate(entries,1): record_claim(ns, f"g38_bs_c{i}", MARKER_ID, GovernanceStatus.POLICY_RULE, f"{e.name}: {e.convention}. Status: {e.status}. {e.meaning}.")
    record_obligation(ns, "g38_bs_choice", MARKER_ID, "Choose exactly one B_s convention in a later explicit declaration record, or preserve declaration-deferred status.")

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES); print_archive_status(ns, invalidated)
    out=ScriptOutput(); entries=build_entries(); case_0(out); case_1(out); case_2(out, entries); case_3(out); case_4(out); record_governance(ns, entries); ns.write_run_metadata()
if __name__=="__main__": main()
