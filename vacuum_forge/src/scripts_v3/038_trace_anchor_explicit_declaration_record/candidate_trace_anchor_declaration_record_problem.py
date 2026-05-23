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

# Group:
#   38_trace_anchor_explicit_declaration_record
# Script type:
#   AUDIT / PROBLEM

SCRIPT_LABEL = "Candidate Trace Anchor Declaration Record Problem"
MARKER_ID = "g38_problem"

DEPENDENCIES = [
    ("g37_summary", "037_trace_anchor_declaration_option_sieve__candidate_group_37_status_summary", "g37_summary"),
    ("g37_recon", "037_trace_anchor_declaration_option_sieve__candidate_trace_anchor_option_batch_reconciliation", "g37_recon"),
    ("g36_summary", "036_conditional_trace_anchor_precondition_inventory__candidate_group_36_status_summary", "g36_summary"),
]

@dataclass
class ProblemEntry:
    name: str
    subject: str
    status: str
    detail: str
    boundary: str


def build_entries() -> List[ProblemEntry]:
    return [
        ProblemEntry("P1: declaration route", "open explicit declaration-record route", "DECLARATION_OPTION", "the group may install one declaration surface only if a package is explicitly chosen", "opening the route is not choosing a package"),
        ProblemEntry("P2: B_s convention choice", "scale-factor versus metric-coefficient convention must be explicit", "OPEN", "this is the central choice that determines zeta/d versus 2*zeta/d", "must not be selected from recovery, insertion, or parent fit"),
        ProblemEntry("P3: membership criterion choice", "typed or role-pure membership must be declared if used", "OPEN", "membership object, sector, domain, codomain, criterion, role-purity, and scope must be explicit", "membership is not incidence, residual control, active O, or insertion"),
        ProblemEntry("P4: no automatic choice", "the batch is allowed to end deferred", "DECLARATION_DEFERRED", "if no single package is marked chosen, Group 38 remains an exploration/declaration-attempt", "deferred is not failure and not adoption"),
        ProblemEntry("P5: downstream gates", "insertion, active O, residual control, and parent closure remain closed", "NOT_READY", "declarations do not license field-equation use", "do not open downstream gates"),
    ]


def case_0(out):
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  Which trace-anchor declaration package, if any, should be explicitly installed")
    print("  as a declared candidate surface for later theorem, adoption, or precondition routes?")
    print("\nDiscipline:\n")
    print("  This script opens Group 38 as a choice-tolerant explicit declaration route.")
    print("  It does not automatically choose a package.")
    print("  It fills no declaration slot unless a later script marks exactly one package chosen.")
    print("  It adopts nothing and opens no downstream gate.")
    print("\nTiny goblin rule:\n  Put the forms on the table. Do not forge the signature.")
    with out.governance_assessments():
        out.line("Group 38 declaration-record route opened", StatusMark.PASS, "choice-tolerant batch; completed or deferred outcome both allowed")


def case_1(out):
    header("Case 1: Symbolic route ledger")
    B_scale, B_metric, typed, rolepure, no_choice, conflict = sp.symbols("B_scale B_metric typed rolepure no_choice conflict")
    P_insertion, P_active_O, P_residual_kill, P_parent = sp.symbols("P_insertion P_active_O P_residual_kill P_parent")
    L_options = sp.simplify(B_scale + B_metric + typed + rolepure + no_choice + conflict)
    L_downstream = sp.simplify(P_insertion + P_active_O + P_residual_kill + P_parent)
    print(f"Declaration option load: L_options = {L_options}")
    print(f"Downstream closed load: L_downstream_closed = {L_downstream}")
    with out.derived_results():
        out.line("declaration-record symbolic route ledger stated", StatusMark.PASS, f"L_options={L_options}; L_downstream_closed={L_downstream}")


def case_2(out, entries):
    header("Case 2: Declaration-record problem entries")
    for item in entries:
        subheader(item.name)
        print(f"Subject: {item.subject}")
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.detail}; boundary: {item.boundary}")


def case_3(out):
    header("Case 3: Invalid upgrades")
    shortcuts = [
        ("X1: opener as declaration", "opening the route fills declaration values", "route opening is not declaration"),
        ("X2: declaration as adoption", "declared candidate is treated as adopted postulate", "adoption requires separate explicit decision"),
        ("X3: declaration as theorem", "declared convention is treated as derived law", "declaration is not proof"),
        ("X4: declaration as insertion", "declaration clarity opens B_s/F_zeta insertion", "insertion remains downstream and not ready"),
    ]
    for name, shortcut, reason in shortcuts:
        subheader(name)
        print(f"Shortcut: {shortcut}")
        with out.counterexamples():
            out.line(name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {reason}")


def case_4(out):
    header("Case 4: Local conclusions")
    with out.governance_assessments():
        out.line("Group 38 opener complete", StatusMark.PASS, "B_s convention exploration should run next")
        out.line("no choices made", StatusMark.DEFER, "current Package B status remains compatible-if-declared")


def record_governance(ns, entries):
    record_marker(ns, MARKER_ID, "g38_declaration_record_problem_opened")
    for idx, item in enumerate(entries, 1):
        record_claim(ns, f"g38_problem_c{idx}", MARKER_ID, GovernanceStatus.POLICY_RULE, f"{item.name}: {item.subject}. {item.detail}. Boundary: {item.boundary}.")
    record_obligation(ns, "g38_problem_choose_or_defer", MARKER_ID, "Group 38 must either choose exactly one declaration package in a later script or close as declaration-deferred.")


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
    record_governance(ns, entries)
    ns.write_run_metadata()

if __name__ == "__main__":
    main()
