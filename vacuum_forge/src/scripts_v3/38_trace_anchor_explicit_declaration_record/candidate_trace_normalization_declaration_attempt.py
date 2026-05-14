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
# Script type: SIEVE / DECLARATION ATTEMPT
SCRIPT_LABEL = "Candidate Trace-Normalization Declaration Attempt"
MARKER_ID = "g38_norm_decl"
DEPENDENCIES = [
    ("g38_problem", "38_trace_anchor_explicit_declaration_record__candidate_trace_anchor_declaration_record_problem", "g38_problem"),
    ("g38_bs_fork", "38_trace_anchor_explicit_declaration_record__candidate_Bs_convention_declaration_fork", "g38_bs_fork"),
    ("g37_norm", "37_trace_anchor_declaration_option_sieve__candidate_trace_norm_declaration_option_sieve", "g37_norm_options"),
]
CHOSEN_CONVENTION = None  # keep synchronized with B_s fork if making a real declaration
TRACED_DIMENSION = None   # e.g. 3; None keeps declaration deferred
ZETA_CONVENTION = None    # e.g. "total_volume_log_trace"
SCOPE = None              # e.g. "exact_determinant_volume" or "linearized_only"

@dataclass
class NormEntry:
    name: str; field: str; value: str; status: str; consequence: str

def norm_expr():
    if CHOSEN_CONVENTION == "scale_factor" and TRACED_DIMENSION:
        return f"log(B_s)=zeta/{TRACED_DIMENSION}"
    if CHOSEN_CONVENTION == "metric_coefficient" and TRACED_DIMENSION:
        return f"log(B_s)=2*zeta/{TRACED_DIMENSION}"
    return "UNDECLARED"

def build_entries():
    ready = all([CHOSEN_CONVENTION, TRACED_DIMENSION, ZETA_CONVENTION, SCOPE])
    return [
        NormEntry("N1: B_s convention", "B_s", str(CHOSEN_CONVENTION), "DECLARED_CANDIDATE" if CHOSEN_CONVENTION else "DECLARATION_DEFERRED", "controls zeta/d versus 2*zeta/d"),
        NormEntry("N2: zeta convention", "zeta", str(ZETA_CONVENTION), "DECLARED_CANDIDATE" if ZETA_CONVENTION else "DECLARATION_DEFERRED", "prevents hidden dimension factors"),
        NormEntry("N3: traced dimension", "d", str(TRACED_DIMENSION), "DECLARED_CANDIDATE" if TRACED_DIMENSION else "DECLARATION_DEFERRED", "makes trace normalization well-posed"),
        NormEntry("N4: scope", "scope", str(SCOPE), "DECLARED_CANDIDATE" if SCOPE else "DECLARATION_DEFERRED", "prevents linearized/exact drift"),
        NormEntry("N5: normalization expression", "N_trace", norm_expr(), "DECLARED_CANDIDATE" if ready else "DECLARATION_DEFERRED", "declared candidate only; not proof"),
    ]

def case_0(out):
    header(SCRIPT_LABEL); print("This script attempts to assemble trace-normalization declaration values.")
    print(f"CHOSEN_CONVENTION={CHOSEN_CONVENTION!r}; TRACED_DIMENSION={TRACED_DIMENSION!r}; ZETA_CONVENTION={ZETA_CONVENTION!r}; SCOPE={SCOPE!r}")
    with out.governance_assessments(): out.line("trace-normalization declaration attempt opened", StatusMark.PASS, "completed only if all fields are explicitly configured")

def case_1(out):
    header("Case 1: Symbolic normalization declaration ledger")
    B_s_decl,zeta_decl,d_decl,scope_decl,N_expr = sp.symbols("B_s_decl zeta_decl d_decl scope_decl N_expr")
    P_insertion,P_active_O,P_residual_kill,P_parent = sp.symbols("P_insertion P_active_O P_residual_kill P_parent")
    L=sp.simplify(B_s_decl+zeta_decl+d_decl+scope_decl+N_expr); D=sp.simplify(P_insertion+P_active_O+P_residual_kill+P_parent)
    print(f"L_norm_declaration = {L}"); print(f"L_downstream_closed = {D}")
    with out.derived_results(): out.line("normalization declaration symbolic ledger stated", StatusMark.PASS, f"L_norm_declaration={L}; L_downstream_closed={D}")

def case_2(out, entries):
    header("Case 2: Normalization declaration fields")
    for e in entries:
        subheader(e.name); print(f"{e.field}: {e.value}")
        with out.governance_assessments(): out.line(e.name, mark(e.status), f"{e.status}: {e.consequence}")

def case_3(out):
    header("Case 3: Invalid normalization declaration upgrades")
    for name, reason in [("X1: partial declaration as complete", "all fields must be explicit"),("X2: declaration as proof", "declared normalization is not derived normalization law"),("X3: declaration as adoption", "adoption is separate"),("X4: normalization as residual control", "residual gate remains separate")]:
        with out.counterexamples(): out.line(name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {reason}")

def case_4(out, entries):
    header("Case 4: Local conclusions")
    complete = all(e.status == "DECLARED_CANDIDATE" for e in entries)
    with out.governance_assessments():
        out.line("trace-normalization declaration attempt result", StatusMark.PASS if complete else StatusMark.DEFER, "DECLARATION_COMPLETED" if complete else "DECLARATION_DEFERRED")
        out.line("no theorem/adoption/insertion", StatusMark.DEFER, "declaration attempt does not prove or adopt normalization")

def record_governance(ns, entries):
    record_marker(ns, MARKER_ID, "g38_trace_normalization_declaration_attempt")
    for i,e in enumerate(entries,1): record_claim(ns, f"g38_norm_c{i}", MARKER_ID, GovernanceStatus.POLICY_RULE, f"{e.name}: {e.field}={e.value}. Status: {e.status}. {e.consequence}.")
    record_obligation(ns, "g38_norm_complete_fields", MARKER_ID, "Trace-normalization declaration requires explicit B_s convention, zeta convention, traced dimension, scope, and expression.")

def main():
    archive,ns,invalidated=prepare_archive(DEPENDENCIES); print_archive_status(ns, invalidated)
    out=ScriptOutput(); entries=build_entries(); case_0(out); case_1(out); case_2(out, entries); case_3(out); case_4(out, entries); record_governance(ns, entries); ns.write_run_metadata()
if __name__=="__main__": main()
