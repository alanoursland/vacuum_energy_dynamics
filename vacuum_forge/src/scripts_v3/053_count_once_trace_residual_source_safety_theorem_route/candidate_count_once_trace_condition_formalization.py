from __future__ import annotations

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

# Group:
#   53_count_once_trace_residual_source_safety_theorem_route
#
# Script type:
#   GOVERNANCE / DIAGNOSTIC / CONDITIONAL THEOREM-SURFACE

SCRIPT_LABEL = 'Candidate Count-Once Trace Condition Formalization'
MARKER_ID = 'g53_count_once_condition'
DEPENDENCIES = [('g52_summary', '052_residual_source_boundary_safety_load_testing__candidate_group_52_status_summary', 'g52_summary'), ('g53_problem', '053_count_once_trace_residual_source_safety_theorem_route__candidate_residual_source_safety_theorem_problem', 'g53_problem')]
QUESTION = 'What incidence conditions are required for trace payload to enter exactly once?'
DISCIPLINE = 'This script formalizes the incidence condition from Group 52. It classifies allowed incidence patterns and rejected patterns, but does not derive dynamics or insertion.'
OPENING_LINE = 'Count-once trace condition formalization opened -- incidence condition only'
SCOPE = 'Group 53 count-once trace condition formalization'
NEXT_SCRIPT = 'candidate_residual_nonentry_non_o_route_audit.py'

ENTRIES = [('C1: count-once equation', 'trace incidence requires i_Bs + i_res = 1', 'COUNT_ONCE_TRACE_CONDITION_FORMALIZED', 'the condition separates single-entry from double-entry and missing-entry patterns', 'not dynamics'), ('C2: B_s route condition', 'i_Bs=1 and i_res=0 is clean at incidence level', 'RESIDUAL_NONENTRY_THEOREM_REQUIRED', 'this route requires residual nonentry theorem support', 'not proven'), ('C3: residual-only route condition', 'i_Bs=0 and i_res=1 is clean at incidence level but does not activate B_s/F_zeta', 'THEOREM_TARGET_REFINED', 'this route cannot serve insertion without a separate law', 'not B_s route'), ('C4: double-entry route', 'i_Bs=1 and i_res=1 produces nonzero residual', 'TRACE_DOUBLE_ENTRY_REJECTED', 'double-entry is rejected for physical use', 'not allowed'), ('C5: missing-entry route', 'i_Bs=0 and i_res=0 produces nonzero residual if trace entry is required', 'TRACE_MISSING_ENTRY_REJECTED', 'missing trace does not satisfy count-once target', 'not allowed if trace needed')]
SHORTCUTS = [('X1: clean incidence as theorem', 'treat zero residual under a substitution as a full safety theorem', 'it is only an incidence condition'), ('X2: choose B_s by condition', 'use the B_s clean pattern to choose branch or insert B_s/F_zeta', 'the condition does not select branch or physical law'), ('X3: erase residual by declaration', 'set i_res=0 without theorem support', 'residual nonentry must be derived or justified')]
OBLIGATIONS = [('O1: residual nonentry theorem', 'RESIDUAL_NONENTRY_THEOREM_REQUIRED', 'prove i_res=0 if the B_s/F_zeta route is pursued', 'avoid count-once violation'), ('O2: insertion remains closed', 'NOT_INSERTABLE', 'do not treat count-once incidence condition as B_s/F_zeta insertion license', 'avoid field-equation drift')]
LOCAL_CONCLUSIONS = [('count-once condition formalized', 'PASS', 'single-entry equation and rejected patterns are explicit'), ('theorem still open', 'RESIDUAL_NONENTRY_THEOREM_REQUIRED', 'clean B_s incidence requires residual nonentry proof')]


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
        "COUNT_ONCE_TRACE_THEOREM_SURFACE_OPENED": StatusMark.INFO,
        "COUNT_ONCE_TRACE_CONDITION_FORMALIZED": StatusMark.INFO,
        "TRACE_DOUBLE_ENTRY_REJECTED": StatusMark.FAIL,
        "TRACE_MISSING_ENTRY_REJECTED": StatusMark.FAIL,
        "RESIDUAL_NONENTRY_ROUTE_DEFINED": StatusMark.INFO,
        "RESIDUAL_NONENTRY_THEOREM_REQUIRED": StatusMark.OBLIGATION,
        "RESIDUAL_ZERO_INCIDENCE_CONDITION": StatusMark.INFO,
        "SOURCE_NO_DOUBLE_COUNTING_ROUTE_DEFINED": StatusMark.INFO,
        "SOURCE_ROLE_PURITY_CONDITION": StatusMark.INFO,
        "SOURCE_NO_DOUBLE_COUNTING_REQUIRED": StatusMark.OBLIGATION,
        "A_SECTOR_MASS_PROTECTION_ROUTE_DEFINED": StatusMark.INFO,
        "TRACE_MASS_NEUTRALITY_CONDITION": StatusMark.INFO,
        "A_SECTOR_MASS_PROTECTION_REQUIRED": StatusMark.OBLIGATION,
        "NON_O_ROUTE_SURVIVES_CONDITIONALLY": StatusMark.INFO,
        "NON_O_ROUTE_OBSTRUCTED": StatusMark.FAIL,
        "ACTIVE_O_NECESSITY_NOT_ESTABLISHED": StatusMark.DEFER,
        "ACTIVE_O_NECESSITY_CONDITIONED": StatusMark.DEFER,
        "THEOREM_TARGET_REFINED": StatusMark.DEFER,
        "CANDIDATE_SURVIVES_AS_AUDIT_ONLY": StatusMark.INFO,
        "CANDIDATE_BLOCKED_FOR_PHYSICAL_USE": StatusMark.DEFER,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "NOT_INSERTABLE": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "CHOICE_REQUIRED": StatusMark.DEFER,
        "SAFETY_THEOREMS_REQUIRED": StatusMark.OBLIGATION,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REJECTED_ROUTE": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "OBSTRUCTION_WITNESS_FOUND": StatusMark.FAIL,
        "OPEN": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {
        "TRACE_DOUBLE_ENTRY_REJECTED",
        "TRACE_MISSING_ENTRY_REJECTED",
        "NON_O_ROUTE_OBSTRUCTED",
        "REJECTED_ROUTE",
        "FORBIDDEN_SHORTCUT",
        "OBSTRUCTION_WITNESS_FOUND",
    }:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {
        "RESIDUAL_NONENTRY_THEOREM_REQUIRED",
        "SOURCE_NO_DOUBLE_COUNTING_REQUIRED",
        "A_SECTOR_MASS_PROTECTION_REQUIRED",
        "SAFETY_THEOREMS_REQUIRED",
        "POLICY_RULE",
    }:
        return GovernanceStatus.POLICY_RULE
    return GovernanceStatus.UNVERIFIED


def obligation_status(status: str) -> ObligationStatus:
    if status in {
        "CANDIDATE_BLOCKED_FOR_PHYSICAL_USE",
        "DEFERRED_WITH_TARGET",
        "NOT_INSERTABLE",
        "NOT_ADOPTED",
        "CHOICE_REQUIRED",
        "ACTIVE_O_NECESSITY_NOT_ESTABLISHED",
        "ACTIVE_O_NECESSITY_CONDITIONED",
        "THEOREM_TARGET_REFINED",
    }:
        return ObligationStatus.DEFERRED
    return ObligationStatus.OPEN


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


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
    ns.record_claim(
        ClaimRecord(
            claim_id=claim_id,
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=governance_status(status),
            statement=statement,
            derivation_ids=[marker_id],
            obligation_ids=[],
        )
    )


def record_obligation(ns, obligation_id: str, title: str, statement: str, status: str = "OPEN") -> None:
    ns.record_obligation(
        ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=obligation_status(status),
            required_by=[SCRIPT_ID],
            description=statement,
        )
    )


def record_governance(ns, marker_id: str, entries: List[Entry], obligations: List[ObligationEntry], scope: str) -> None:
    record_marker(ns, marker_id, scope)
    for idx, item in enumerate(entries, 1):
        record_claim(
            ns,
            f"{marker_id}_c{idx}",
            marker_id,
            item.status,
            f"{item.name}: {item.subject}. {item.detail}. Boundary: {item.boundary}.",
        )
    for idx, item in enumerate(obligations, 1):
        record_obligation(
            ns,
            f"{marker_id}_o{idx}",
            item.name,
            f"{item.obligation}. Discipline: {item.discipline}.",
            item.status,
        )


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
    header("Rejected shortcuts and invalid upgrades")
    for item in shortcuts:
        subheader(item.name)
        print(f"Shortcut: {item.shortcut}")
        with out.counterexamples():
            out.line(item.name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {item.reason}")


def print_obligations(out: ScriptOutput, obligations: List[ObligationEntry]) -> None:
    header("Open obligations and deferred burdens")
    for item in obligations:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        with out.unresolved_obligations():
            out.line(item.name, mark(item.status), f"{item.status}: {item.obligation}; discipline: {item.discipline}")


def build_entries() -> List[Entry]:
    return [Entry(*item) for item in ENTRIES]


def build_shortcuts() -> List[Shortcut]:
    return [Shortcut(*item) for item in SHORTCUTS]


def build_obligations() -> List[ObligationEntry]:
    return [ObligationEntry(*item) for item in OBLIGATIONS]



def case_count_once_conditions(out: ScriptOutput):
    header("Case 0: Count-once trace condition formalization")

    T_zeta = sp.Symbol("T_zeta")
    i_Bs, i_res = sp.symbols("i_Bs i_res")
    residual = sp.simplify(T_zeta * (i_Bs + i_res - 1))

    cases = [
        ("B_s route", {i_Bs: 1, i_res: 0}, "allowed incidence pattern if residual nonentry is proven"),
        ("residual-only route", {i_Bs: 0, i_res: 1}, "allowed incidence pattern only if trace does not enter B_s/F_zeta"),
        ("double-entry route", {i_Bs: 1, i_res: 1}, "rejected double-count pattern"),
        ("missing-trace route", {i_Bs: 0, i_res: 0}, "rejected if trace entry is required"),
    ]

    print(f"trace residual = {residual}")
    print("Count-once equation:")
    print("  i_Bs + i_res = 1")
    print()

    results = {}
    for label, subs, meaning in cases:
        value = sp.simplify(residual.subs(subs))
        results[label] = value
        print(f"{label}: residual = {value}; {meaning}")

    with out.derived_results():
        out.line("count-once residual", StatusMark.PASS, f"residual = {residual}")
        out.line("B_s route residual", StatusMark.PASS if is_zero(results["B_s route"]) else StatusMark.FAIL, f"residual = {results['B_s route']}")
        out.line("residual-only route residual", StatusMark.PASS if is_zero(results["residual-only route"]) else StatusMark.FAIL, f"residual = {results['residual-only route']}")
        out.line("double-entry route residual", StatusMark.FAIL if not is_zero(results["double-entry route"]) else StatusMark.PASS, f"residual = {results['double-entry route']}")
        out.line("missing-trace route residual", StatusMark.FAIL if not is_zero(results["missing-trace route"]) else StatusMark.PASS, f"residual = {results['missing-trace route']}")

    return {
        "T_zeta": T_zeta,
        "i_Bs": i_Bs,
        "i_res": i_res,
        "residual": residual,
        "cases": results,
    }


def record_count_once_conditions(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g53_count_once_condition_residual",
        inputs=[data["T_zeta"], data["i_Bs"], data["i_res"]],
        output=data["residual"],
        method="formalize count-once trace residual T_zeta*(i_Bs+i_res-1)",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="count_once_condition",
        scope="diagnostic theorem-surface condition; not insertion theorem",
    )



def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    entries = build_entries()
    shortcuts = build_shortcuts()
    obligations = build_obligations()

    header(SCRIPT_LABEL)
    print("Question:\n")
    print(QUESTION)
    print("\nDiscipline:\n")
    print(DISCIPLINE)
    with out.governance_assessments():
        out.line(f"{SCRIPT_LABEL} opened", StatusMark.PASS, OPENING_LINE)

    data = case_count_once_conditions(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_count_once_conditions(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
