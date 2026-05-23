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

SCRIPT_LABEL = 'Candidate Source / Trace Filter'
MARKER_ID = 'g59_src'
DEPENDENCIES = [('g58_summary', '058_weighted_neutral_layer__candidate_group_58_status_summary', 'g58_summary'), ('g59_problem', '059_transition_term_audit__candidate_transition_problem', 'g59_problem'), ('g59_neu', '059_transition_term_audit__candidate_weighted_neutralizer', 'g59_neu')]
QUESTION = 'Which transition candidates violate source role-purity or count trace more than once?'
DISCIPLINE = 'This script applies reduced source and trace incidence filters. It does not prove source safety.'
OPENING_LINE = 'Source/trace transition filter opened'
SCOPE = 'Group 59 source trace filter'
NEXT_SCRIPT = 'candidate_divergence_filter.py'

ENTRIES = [('S1: source-clean route', 'i_A=1 and i_layer=0', 'SOURCE_TRACE_FILTER_APPLIED', 'layer must not carry ordinary source load', 'necessary condition'), ('S2: source-carrying rejection', 'i_A=1 and i_layer=1 gives source residual', 'SOURCE_CARRYING_TERM_REJECTED', 'ordinary source duplication is forbidden', 'rejected'), ('S3: trace-clean route', 'i_Bs=1, i_layer=0, i_res=0', 'SOURCE_TRACE_FILTER_APPLIED', 'layer must not be extra trace entry', 'necessary condition'), ('S4: trace double-count rejection', 'i_layer=1 or i_res=1 with B_s gives trace residual', 'TRACE_DOUBLE_COUNT_TERM_REJECTED', 'trace double-counting is forbidden', 'rejected')]
SHORTCUTS = [('X1: neutral means source-clean', 'claim Q_weighted=0 proves i_layer=0 for source', 'incidence must be declared/proven'), ('X2: transition as extra trace', 'let transition term carry trace payload in addition to B_s', 'double count risk'), ('X3: source repair', 'use transition term to repair A-sector source mismatch', 'source repair is forbidden')]
OBLIGATIONS = [('O1: source safety theorem', 'SOURCE_SAFETY_REQUIRED', 'prove any surviving transition response is ordinary-source neutral', 'protect A-sector source routing'), ('O2: trace-count theorem', 'SAFETY_THEOREMS_REQUIRED', 'prove transition response does not add extra trace count', 'avoid residual reentry')]
LOCAL_CONCLUSIONS = [('source trace filter applied', 'PASS', 'source-carrying and trace-double-counting transition terms rejected'), ('physical use blocked', 'NOT_INSERTABLE', 'incidence filter is not insertion')]


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
        "TRANSITION_AUDIT_OPENED": StatusMark.INFO,
        "RESIDUE_INVENTORY_DERIVED": StatusMark.PASS,
        "CANDIDATE_TERM_SURFACE_OPENED": StatusMark.INFO,
        "LOCALITY_FILTER_APPLIED": StatusMark.PASS,
        "LOCALIZED_LAYER_TERM_CONFIRMED": StatusMark.PASS,
        "NONLOCAL_TERM_REJECTED": StatusMark.FAIL,
        "WEIGHTED_NEUTRALIZER_DERIVED": StatusMark.PASS,
        "WEIGHTED_NEUTRALITY_CONFIRMED": StatusMark.PASS,
        "SCALAR_CHARGE_TERM_REJECTED": StatusMark.FAIL,
        "SOURCE_CARRYING_TERM_REJECTED": StatusMark.FAIL,
        "TRACE_DOUBLE_COUNT_TERM_REJECTED": StatusMark.FAIL,
        "SOURCE_TRACE_FILTER_APPLIED": StatusMark.PASS,
        "DIVERGENCE_FILTER_APPLIED": StatusMark.PASS,
        "DIVERGENCE_FAILING_TERM_REJECTED": StatusMark.FAIL,
        "CLOSURE_SUPPORTED_TERM_SURVIVES": StatusMark.INFO,
        "TRANSITION_TERM_SURVIVES_CONDITIONALLY": StatusMark.INFO,
        "WEIGHTED_LAYER_ROUTE_SURVIVES_CONDITIONALLY": StatusMark.INFO,
        "COVARIANT_LIFT_REQUIRED": StatusMark.OBLIGATION,
        "ENERGY_ACCOUNTING_REQUIRED": StatusMark.OBLIGATION,
        "SOURCE_SAFETY_REQUIRED": StatusMark.OBLIGATION,
        "DIVERGENCE_IDENTITY_REQUIRED": StatusMark.OBLIGATION,
        "SAFETY_THEOREMS_REQUIRED": StatusMark.OBLIGATION,
        "PHYSICAL_USE_BLOCKED": StatusMark.DEFER,
        "NOT_INSERTABLE": StatusMark.DEFER,
        "ACTIVE_O_NECESSITY_NOT_ESTABLISHED": StatusMark.DEFER,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REJECTED_ROUTE": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {
        "REJECTED_ROUTE",
        "FORBIDDEN_SHORTCUT",
        "NONLOCAL_TERM_REJECTED",
        "SCALAR_CHARGE_TERM_REJECTED",
        "SOURCE_CARRYING_TERM_REJECTED",
        "TRACE_DOUBLE_COUNT_TERM_REJECTED",
        "DIVERGENCE_FAILING_TERM_REJECTED",
    }:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {
        "COVARIANT_LIFT_REQUIRED",
        "ENERGY_ACCOUNTING_REQUIRED",
        "SOURCE_SAFETY_REQUIRED",
        "DIVERGENCE_IDENTITY_REQUIRED",
        "SAFETY_THEOREMS_REQUIRED",
        "POLICY_RULE",
    }:
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



def case_source_trace_filter(out: ScriptOutput):
    header("Case 0: Source and trace incidence filters for transition candidates")

    S_M, T_zeta = sp.symbols("S_M T_zeta")
    i_A, i_layer, i_Bs, i_res = sp.symbols("i_A i_layer i_Bs i_res")

    source_residual = sp.simplify(S_M * (i_A + i_layer - 1))
    trace_residual = sp.simplify(T_zeta * (i_Bs + i_layer + i_res - 1))

    cases = {
        "source clean layer-neutral": {i_A: 1, i_layer: 0},
        "source carrying layer": {i_A: 1, i_layer: 1},
        "missing A with layer": {i_A: 0, i_layer: 1},
    }
    trace_cases = {
        "trace clean Bs only": {i_Bs: 1, i_layer: 0, i_res: 0},
        "trace double layer": {i_Bs: 1, i_layer: 1, i_res: 0},
        "trace residual reentry": {i_Bs: 1, i_layer: 0, i_res: 1},
        "layer-only trace": {i_Bs: 0, i_layer: 1, i_res: 0},
    }

    print(f"source_residual = {source_residual}")
    for name, subs in cases.items():
        value = sp.simplify(source_residual.subs(subs))
        print(f"{name}: {value}")

    print(f"trace_residual = {trace_residual}")
    for name, subs in trace_cases.items():
        value = sp.simplify(trace_residual.subs(subs))
        print(f"{name}: {value}")

    with out.derived_results():
        out.line("source residual", StatusMark.PASS, f"{source_residual}")
        for name, subs in cases.items():
            value = sp.simplify(source_residual.subs(subs))
            out.line(name, StatusMark.PASS if is_zero(value) else StatusMark.FAIL, f"{value}")
        out.line("trace residual", StatusMark.PASS, f"{trace_residual}")
        for name, subs in trace_cases.items():
            value = sp.simplify(trace_residual.subs(subs))
            # layer-only trace has zero incidence residual but is not B_s/F_zeta insertion route; mark info if zero.
            if name == "layer-only trace" and is_zero(value):
                status = StatusMark.INFO
            else:
                status = StatusMark.PASS if is_zero(value) else StatusMark.FAIL
            out.line(name, status, f"{value}")

    return {"source_residual": source_residual, "trace_residual": trace_residual}


def record_src(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g59_src",
        inputs=[],
        output=data["trace_residual"],
        method="apply source and trace incidence filters to transition candidates",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="transition_source_trace_filter",
        scope="reduced incidence filter; not source theorem",
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

    data = case_source_trace_filter(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_src(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
