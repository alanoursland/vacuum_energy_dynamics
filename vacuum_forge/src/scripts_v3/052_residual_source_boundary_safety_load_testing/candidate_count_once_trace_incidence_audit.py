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
#   52_residual_source_boundary_safety_load_testing
#
# Script type:
#   GOVERNANCE / DIAGNOSTIC

SCRIPT_LABEL = 'Candidate Count-Once Trace Incidence Audit'
MARKER_ID = 'g52_count_once_trace'
DEPENDENCIES = [('g51_summary', '51_trace_normalization_adopt_defer_reject_decision_surface__candidate_group_51_status_summary', 'g51_summary'), ('g52_problem', '52_residual_source_boundary_safety_load_testing__candidate_safety_load_test_problem', 'g52_problem')]
QUESTION = 'What would it mean for scalar trace to enter exactly once if the paired trace-normalization candidate is retained?'
DISCIPLINE = 'This script builds a small incidence diagnostic. It identifies double-count conditions; it does not prove a complete count-once theorem.'
OPENING_LINE = 'Count-once trace incidence audit opened -- diagnostic incidence only'
SCOPE = 'Group 52 count-once trace incidence audit'
NEXT_SCRIPT = 'candidate_residual_nonentry_obstruction_sieve.py'

ENTRIES = [('T1: incidence burden', 'trace payload must not enter both B_s/F_zeta and residual zeta/kappa metric channels', 'COUNT_ONCE_TRACE_BURDEN_EXPLICIT', 'double-entry produces a nonzero diagnostic residual', 'not theorem closure'), ('T2: residual nonentry', 'residual trace channel must be killed, inert, or non-metric if B_s/F_zeta receives trace payload', 'RESIDUAL_NONENTRY_THEOREM_REQUIRED', 'count-once safety requires residual nonentry support', 'not proven here'), ('T3: audit-only survival', 'the conditional candidate survives this script only as an audit object', 'CANDIDATE_SURVIVES_AS_AUDIT_ONLY', 'the incidence diagnostic states burden, not insertability', 'not physical use')]
SHORTCUTS = [('X1: incidence as theorem', 'treat the incidence ledger as proving count-once trace', 'the ledger identifies conditions; it does not derive dynamics'), ('X2: residual ignored', 'set residual incidence to zero by declaration', 'residual nonentry requires theorem support'), ('X3: double count accepted', 'allow both trace and residual metric channels to carry the same payload', 'that violates count-once discipline')]
OBLIGATIONS = [('O1: count-once theorem target', 'SAFETY_THEOREMS_REQUIRED', 'derive or otherwise justify single scalar trace incidence before physical use', 'avoid trace double-counting'), ('O2: residual nonentry target', 'RESIDUAL_NONENTRY_THEOREM_REQUIRED', 'prove residual zeta/kappa cannot re-enter metric trace if B_s/F_zeta is active', 'avoid residual metric reentry')]
LOCAL_CONCLUSIONS = [('count-once incidence burden stated', 'PASS', 'symbolic incidence ledger identifies double-count witness'), ('count-once theorem not closed', 'SAFETY_THEOREMS_REQUIRED', 'diagnostic result is not a complete safety theorem')]


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
        "SAFETY_LOAD_TEST_SURFACE_OPENED": StatusMark.INFO,
        "COUNT_ONCE_TRACE_BURDEN_EXPLICIT": StatusMark.OBLIGATION,
        "TRACE_INCIDENCE_DIAGNOSTIC": StatusMark.INFO,
        "RESIDUAL_NONENTRY_THEOREM_REQUIRED": StatusMark.OBLIGATION,
        "RESIDUAL_ENTRY_REJECTED": StatusMark.FAIL,
        "SOURCE_NO_DOUBLE_COUNTING_REQUIRED": StatusMark.OBLIGATION,
        "SOURCE_DUPLICATION_WITNESS": StatusMark.FAIL,
        "A_SECTOR_MASS_PROTECTION_REQUIRED": StatusMark.OBLIGATION,
        "A_SECTOR_MASS_COIN_PROTECTED": StatusMark.INFO,
        "BOUNDARY_SCALAR_SILENCE_REQUIRED": StatusMark.OBLIGATION,
        "SCALAR_TAIL_WITNESS": StatusMark.FAIL,
        "CANDIDATE_SURVIVES_AS_AUDIT_ONLY": StatusMark.INFO,
        "CANDIDATE_BLOCKED_FOR_PHYSICAL_USE": StatusMark.DEFER,
        "THEOREM_TARGET_REFINED": StatusMark.DEFER,
        "OBSTRUCTION_WITNESS_FOUND": StatusMark.FAIL,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "NOT_INSERTABLE": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "THEORY_DECISION_REQUIRED": StatusMark.DEFER,
        "CHOICE_REQUIRED": StatusMark.DEFER,
        "NUMERIC_D_CONDITION": StatusMark.OBLIGATION,
        "SAFETY_THEOREMS_REQUIRED": StatusMark.OBLIGATION,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REJECTED_ROUTE": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "OPEN": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {
        "REJECTED_ROUTE",
        "FORBIDDEN_SHORTCUT",
        "RESIDUAL_ENTRY_REJECTED",
        "SOURCE_DUPLICATION_WITNESS",
        "SCALAR_TAIL_WITNESS",
        "OBSTRUCTION_WITNESS_FOUND",
    }:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {
        "POLICY_RULE",
        "SAFETY_THEOREMS_REQUIRED",
        "COUNT_ONCE_TRACE_BURDEN_EXPLICIT",
        "RESIDUAL_NONENTRY_THEOREM_REQUIRED",
        "SOURCE_NO_DOUBLE_COUNTING_REQUIRED",
        "A_SECTOR_MASS_PROTECTION_REQUIRED",
        "BOUNDARY_SCALAR_SILENCE_REQUIRED",
        "NUMERIC_D_CONDITION",
    }:
        return GovernanceStatus.POLICY_RULE
    return GovernanceStatus.UNVERIFIED


def obligation_status(status: str) -> ObligationStatus:
    if status in {
        "DEFERRED_WITH_TARGET",
        "NOT_INSERTABLE",
        "NOT_ADOPTED",
        "THEORY_DECISION_REQUIRED",
        "CHOICE_REQUIRED",
        "CANDIDATE_BLOCKED_FOR_PHYSICAL_USE",
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



def case_symbolic_trace_incidence(out: ScriptOutput):
    header("Case 0: Symbolic count-once trace incidence diagnostic")

    T_zeta = sp.Symbol("T_zeta")
    i_Bs, i_res = sp.symbols("i_Bs i_res")

    trace_load = sp.simplify((i_Bs + i_res) * T_zeta)
    count_once_target = T_zeta
    residual = sp.simplify(trace_load - count_once_target)
    double_count_witness = sp.simplify(residual.subs({i_Bs: 1, i_res: 1}))
    clean_once_residual = sp.simplify(residual.subs({i_Bs: 1, i_res: 0}))

    print("Trace payload:")
    print(f"  T_zeta = {T_zeta}")
    print("Incidence flags:")
    print("  i_Bs  = trace payload enters B_s/F_zeta channel")
    print("  i_res = trace payload re-enters residual zeta/kappa channel")
    print()
    print(f"trace_load = (i_Bs + i_res) * T_zeta = {trace_load}")
    print(f"count_once_target = {count_once_target}")
    print(f"residual = trace_load - target = {residual}")
    print()
    print(f"double-count witness (i_Bs=1, i_res=1): {double_count_witness}")
    print(f"clean once residual (i_Bs=1, i_res=0): {clean_once_residual}")

    with out.derived_results():
        out.line(
            "trace incidence residual",
            StatusMark.PASS,
            f"residual = {residual}",
        )
        out.line(
            "double-count witness",
            StatusMark.FAIL if not is_zero(double_count_witness) else StatusMark.PASS,
            f"residual at i_Bs=i_res=1 is {double_count_witness}",
        )
        out.line(
            "single-entry diagnostic",
            StatusMark.PASS if is_zero(clean_once_residual) else StatusMark.FAIL,
            f"residual at i_Bs=1, i_res=0 is {clean_once_residual}",
        )

    return {
        "T_zeta": T_zeta,
        "i_Bs": i_Bs,
        "i_res": i_res,
        "trace_load": trace_load,
        "residual": residual,
        "double_count_witness": double_count_witness,
        "clean_once_residual": clean_once_residual,
    }


def record_symbolic_trace_incidence(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g52_count_once_trace_residual",
        inputs=[data["i_Bs"], data["i_res"], data["T_zeta"]],
        output=data["residual"],
        method="trace_load - count_once_target with incidence flags",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="incidence_residual",
        scope="diagnostic count-once trace incidence; not a theorem",
    )
    ns.record_derivation(
        derivation_id="g52_count_once_double_count_witness",
        inputs=[data["residual"]],
        output=data["double_count_witness"],
        method="substitute i_Bs=1, i_res=1",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="obstruction_witness",
        scope="diagnostic double-count witness; not branch rejection by itself",
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

    data = case_symbolic_trace_incidence(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_symbolic_trace_incidence(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
