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
SCRIPT_LABEL = "Candidate Safe-Membership Declaration Attempt"
MARKER_ID = "g38_mem_decl"
DEPENDENCIES = [
    ("g38_problem", "38_trace_anchor_explicit_declaration_record__candidate_trace_anchor_declaration_record_problem", "g38_problem"),
    ("g37_mem", "37_trace_anchor_declaration_option_sieve__candidate_safe_membership_declaration_option_sieve", "g37_membership_options"),
]
MEMBERSHIP_FORM = None  # allowed: "typed", "role_pure", or None
ZETA_BS_OBJECT = None
T_ZETA_SECTOR = None
DOMAIN = None
CODOMAIN = None
CRITERION = None
ROLE_PURITY = None
SCOPE = None

@dataclass
class MemEntry:
    name: str; field: str; value: str; status: str; consequence: str

def build_entries():
    fields = [MEMBERSHIP_FORM, ZETA_BS_OBJECT, T_ZETA_SECTOR, DOMAIN, CODOMAIN, CRITERION, ROLE_PURITY, SCOPE]
    complete = all(fields)
    return [
        MemEntry("M1: membership form", "form", str(MEMBERSHIP_FORM), "DECLARED_CANDIDATE" if MEMBERSHIP_FORM else "DECLARATION_DEFERRED", "typed or role-pure form must be explicit"),
        MemEntry("M2: zeta_Bs object", "zeta_Bs", str(ZETA_BS_OBJECT), "DECLARED_CANDIDATE" if ZETA_BS_OBJECT else "DECLARATION_DEFERRED", "object must be declared before membership claim"),
        MemEntry("M3: T_zeta sector", "T_zeta", str(T_ZETA_SECTOR), "DECLARED_CANDIDATE" if T_ZETA_SECTOR else "DECLARATION_DEFERRED", "sector must be declared before membership claim"),
        MemEntry("M4: domain/codomain", "domain -> codomain", f"{DOMAIN}->{CODOMAIN}", "DECLARED_CANDIDATE" if DOMAIN and CODOMAIN else "DECLARATION_DEFERRED", "membership must be typed"),
        MemEntry("M5: criterion", "criterion", str(CRITERION), "DECLARED_CANDIDATE" if CRITERION else "DECLARATION_DEFERRED", "criterion is required before theorem/adoption routes"),
        MemEntry("M6: role purity", "role_purity", str(ROLE_PURITY), "DECLARED_CANDIDATE" if ROLE_PURITY else "DECLARATION_DEFERRED", "exclusion zones must remain explicit"),
        MemEntry("M7: scope", "scope", str(SCOPE), "DECLARED_CANDIDATE" if SCOPE else "DECLARATION_DEFERRED", "diagnostic or active candidate scope must be stated"),
        MemEntry("M8: membership declaration result", "result", "complete" if complete else "deferred", "DECLARED_CANDIDATE" if complete else "DECLARATION_DEFERRED", "declared candidate only; not proof"),
    ]

def case_0(out):
    header(SCRIPT_LABEL); print("This script attempts to assemble safe-membership declaration values.")
    print(f"MEMBERSHIP_FORM={MEMBERSHIP_FORM!r}; ZETA_BS_OBJECT={ZETA_BS_OBJECT!r}; T_ZETA_SECTOR={T_ZETA_SECTOR!r}")
    with out.governance_assessments(): out.line("safe-membership declaration attempt opened", StatusMark.PASS, "completed only if all membership fields are explicit")

def case_1(out):
    header("Case 1: Symbolic membership declaration ledger")
    obj,sector,dom,codom,crit,pure,scope = sp.symbols("obj sector dom codom crit pure scope")
    P_insertion,P_active_O,P_residual_kill,P_parent = sp.symbols("P_insertion P_active_O P_residual_kill P_parent")
    L=sp.simplify(obj+sector+dom+codom+crit+pure+scope); D=sp.simplify(P_insertion+P_active_O+P_residual_kill+P_parent)
    print(f"L_membership_declaration = {L}"); print(f"L_downstream_closed = {D}")
    with out.derived_results(): out.line("membership declaration symbolic ledger stated", StatusMark.PASS, f"L_membership_declaration={L}; L_downstream_closed={D}")

def case_2(out, entries):
    header("Case 2: Membership declaration fields")
    for e in entries:
        subheader(e.name); print(f"{e.field}: {e.value}")
        with out.governance_assessments(): out.line(e.name, mark(e.status), f"{e.status}: {e.consequence}")

def case_3(out):
    header("Case 3: Invalid membership declaration upgrades")
    for name, reason in [("X1: partial membership as complete", "all fields must be explicit"),("X2: membership as incidence", "incidence theorem remains separate"),("X3: membership as residual control", "residual kill/active O remain separate"),("X4: membership as insertion", "insertion remains not ready")]:
        with out.counterexamples(): out.line(name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {reason}")

def case_4(out, entries):
    header("Case 4: Local conclusions")
    complete = entries[-1].status == "DECLARED_CANDIDATE"
    with out.governance_assessments():
        out.line("safe-membership declaration attempt result", StatusMark.PASS if complete else StatusMark.DEFER, "DECLARATION_COMPLETED" if complete else "DECLARATION_DEFERRED")
        out.line("no theorem/adoption/insertion", StatusMark.DEFER, "declaration attempt does not prove or adopt membership")

def record_governance(ns, entries):
    record_marker(ns, MARKER_ID, "g38_safe_membership_declaration_attempt")
    for i,e in enumerate(entries,1): record_claim(ns, f"g38_mem_c{i}", MARKER_ID, GovernanceStatus.POLICY_RULE, f"{e.name}: {e.field}={e.value}. Status: {e.status}. {e.consequence}.")
    record_obligation(ns, "g38_mem_complete_fields", MARKER_ID, "Safe-membership declaration requires explicit object, sector, domain, codomain, criterion, role purity, and scope.")

def main():
    archive,ns,invalidated=prepare_archive(DEPENDENCIES); print_archive_status(ns, invalidated)
    out=ScriptOutput(); entries=build_entries(); case_0(out); case_1(out); case_2(out, entries); case_3(out); case_4(out, entries); record_governance(ns, entries); ns.write_run_metadata()
if __name__=="__main__": main()
