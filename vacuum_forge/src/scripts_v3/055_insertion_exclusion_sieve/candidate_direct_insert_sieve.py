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

SCRIPT_LABEL = 'Candidate Direct Insertion Sieve'
MARKER_ID = 'g55_direct'
DEPENDENCIES = [('g54_summary', '054_boundary_neutrality_exterior_scalar_silence_theorem_route__candidate_group_54_status_summary', 'g54_summary'), ('g55_problem', '055_insertion_exclusion_sieve__candidate_insert_problem', 'g55_problem')]
QUESTION = 'Does direct insertion create trace/source/boundary/mass load before theorem support exists?'
DISCIPLINE = 'This script builds a direct insertion load diagnostic. It rejects direct load routes and preserves only no-direct-load/silent routes as possible theorem targets.'
OPENING_LINE = 'Direct insertion sieve opened -- reject direct load routes'
SCOPE = 'Group 55 direct insertion sieve'
NEXT_SCRIPT = 'candidate_trace_count_filter.py'

ENTRIES = [('D1: direct load diagnostic', 'L=a_T*T_zeta+a_S*S_M+a_C*C1+a_J*J+a_Q*Q_trace', 'DIRECT_INSERTION_REJECTED', 'nonzero direct load indicates unsafe insertion family', 'not field equation'), ('D2: no-direct-load case', 'all direct load coefficients zero', 'SILENT_INSERTION_ROUTE_SURVIVES_CONDITIONALLY', 'silent route survives only as theorem target', 'not insertion'), ('D3: trace/source/boundary/mass witnesses', 'nonzero trace, source, boundary, or mass load creates obstruction', 'DIRECT_INSERTION_REJECTED', 'unsafe direct route rejected', 'not total candidate rejection')]
SHORTCUTS = [('X1: direct load as physical law', 'use nonzero direct load as insertion equation', 'that creates unlicensed physical load'), ('X2: silent route as insertion', 'insert because no-direct-load case exists', 'silent survival is not construction'), ('X3: hide load in coefficient', 'hide trace/source/mass load in coefficients', 'load must remain explicit')]
OBLIGATIONS = [('O1: insertion law required', 'INSERTION_LAW_REQUIRED', 'derive an insertion law that creates no forbidden direct load', 'avoid ad hoc source terms'), ('O2: keep physical use blocked', 'NOT_INSERTABLE', 'do not insert from the diagnostic', 'avoid field-equation drift')]
LOCAL_CONCLUSIONS = [('direct insertion routes rejected', 'DIRECT_INSERTION_REJECTED', 'direct trace/source/boundary/mass load routes are unsafe'), ('silent route remains conditional', 'SILENT_INSERTION_ROUTE_SURVIVES_CONDITIONALLY', 'no-direct-load route is only theorem target')]


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
        "INSERTION_EXCLUSION_SURFACE_OPENED": StatusMark.INFO,
        "DIRECT_INSERTION_REJECTED": StatusMark.FAIL,
        "TRACE_COUNT_FILTER_APPLIED": StatusMark.PASS,
        "TRACE_DOUBLE_ENTRY_REJECTED": StatusMark.FAIL,
        "TRACE_MISSING_ENTRY_REJECTED": StatusMark.FAIL,
        "SOURCE_FILTER_APPLIED": StatusMark.PASS,
        "SOURCE_CARRYING_INSERTION_REJECTED": StatusMark.FAIL,
        "BOUNDARY_FILTER_APPLIED": StatusMark.PASS,
        "BOUNDARY_LEAKING_INSERTION_REJECTED": StatusMark.FAIL,
        "MASS_FILTER_APPLIED": StatusMark.PASS,
        "MASS_SHIFTING_INSERTION_REJECTED": StatusMark.FAIL,
        "SILENT_INSERTION_ROUTE_SURVIVES_CONDITIONALLY": StatusMark.INFO,
        "INSERTION_LAW_REQUIRED": StatusMark.OBLIGATION,
        "PHYSICAL_USE_BLOCKED": StatusMark.DEFER,
        "CANDIDATE_SURVIVES_AS_AUDIT_ONLY": StatusMark.INFO,
        "ACTIVE_O_NECESSITY_NOT_ESTABLISHED": StatusMark.DEFER,
        "SAFETY_THEOREMS_REQUIRED": StatusMark.OBLIGATION,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "NOT_INSERTABLE": StatusMark.DEFER,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "REJECTED_ROUTE": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {
        "DIRECT_INSERTION_REJECTED",
        "TRACE_DOUBLE_ENTRY_REJECTED",
        "TRACE_MISSING_ENTRY_REJECTED",
        "SOURCE_CARRYING_INSERTION_REJECTED",
        "BOUNDARY_LEAKING_INSERTION_REJECTED",
        "MASS_SHIFTING_INSERTION_REJECTED",
        "REJECTED_ROUTE",
        "FORBIDDEN_SHORTCUT",
    }:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {"INSERTION_LAW_REQUIRED", "SAFETY_THEOREMS_REQUIRED", "POLICY_RULE"}:
        return GovernanceStatus.POLICY_RULE
    return GovernanceStatus.UNVERIFIED


def obligation_status(status: str) -> ObligationStatus:
    if status in {
        "PHYSICAL_USE_BLOCKED",
        "NOT_INSERTABLE",
        "DEFERRED_WITH_TARGET",
        "ACTIVE_O_NECESSITY_NOT_ESTABLISHED",
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
        record_claim(ns, f"{marker_id}_c{idx}", marker_id, item.status, f"{item.name}: {item.subject}. {item.detail}. Boundary: {item.boundary}.")
    for idx, item in enumerate(obligations, 1):
        record_obligation(ns, f"{marker_id}_o{idx}", item.name, f"{item.obligation}. Discipline: {item.discipline}.", item.status)


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



def case_direct_load(out: ScriptOutput):
    header("Case 0: Direct insertion load diagnostic")

    a_T, a_S, a_C, a_J, a_Q = sp.symbols("a_T a_S a_C a_J a_Q")
    T_zeta, S_M, C1, J, Q_trace = sp.symbols("T_zeta S_M C1 J Q_trace")

    L = sp.simplify(a_T*T_zeta + a_S*S_M + a_C*C1 + a_J*J + a_Q*Q_trace)
    silent_L = sp.simplify(L.subs({a_T:0, a_S:0, a_C:0, a_J:0, a_Q:0}))
    trace_L = sp.simplify(L.subs({a_T:1, a_S:0, a_C:0, a_J:0, a_Q:0}))
    source_L = sp.simplify(L.subs({a_T:0, a_S:1, a_C:0, a_J:0, a_Q:0}))
    boundary_L = sp.simplify(L.subs({a_T:0, a_S:0, a_C:1, a_J:1, a_Q:0}))
    mass_L = sp.simplify(L.subs({a_T:0, a_S:0, a_C:0, a_J:0, a_Q:1}))

    print(f"L = {L}")
    print(f"silent/no-direct-load case = {silent_L}")
    print(f"trace direct load = {trace_L}")
    print(f"source direct load = {source_L}")
    print(f"boundary direct load = {boundary_L}")
    print(f"mass direct load = {mass_L}")

    with out.derived_results():
        out.line("direct insertion load", StatusMark.PASS, f"L = {L}")
        out.line("silent no-direct-load case", StatusMark.PASS if is_zero(silent_L) else StatusMark.FAIL, f"L = {silent_L}")
        out.line("trace direct load witness", StatusMark.FAIL if not is_zero(trace_L) else StatusMark.PASS, f"L = {trace_L}")
        out.line("source direct load witness", StatusMark.FAIL if not is_zero(source_L) else StatusMark.PASS, f"L = {source_L}")
        out.line("boundary direct load witness", StatusMark.FAIL if not is_zero(boundary_L) else StatusMark.PASS, f"L = {boundary_L}")
        out.line("mass direct load witness", StatusMark.FAIL if not is_zero(mass_L) else StatusMark.PASS, f"L = {mass_L}")

    return {"L": L, "silent_L": silent_L, "trace_L": trace_L, "source_L": source_L, "boundary_L": boundary_L, "mass_L": mass_L}


def record_direct(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g55_direct_L",
        inputs=[],
        output=data["L"],
        method="direct insertion load diagnostic",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="direct_insert_load",
        scope="diagnostic insertion-family exclusion; not field equation",
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

    data = case_direct_load(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_direct(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
