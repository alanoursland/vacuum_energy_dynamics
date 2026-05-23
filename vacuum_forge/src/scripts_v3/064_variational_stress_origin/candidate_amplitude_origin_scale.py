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

SCRIPT_LABEL = 'Candidate Amplitude Origin Scale'
MARKER_ID = 'g64_amp'
DEPENDENCIES = [('g63_summary', '063_obstruction_decision__candidate_group_63_status_summary', 'g63_summary'), ('g64_problem', '064_variational_stress_origin__candidate_variational_problem', 'g64_problem'), ('g64_lin', '064_variational_stress_origin__candidate_linear_closure_origin', 'g64_lin')]
QUESTION = 'Can p_free be derived by source coupling, normalization, diagnostic scaling, or zero response?'
DISCIPLINE = 'This script rejects source-coupled and repair amplitude origins and treats normalization as scale-setting, not physics.'
OPENING_LINE = 'Amplitude-origin scale audit opened'
SCOPE = 'Group 64 amplitude origin scale'
NEXT_SCRIPT = 'candidate_boundary_variation_sieve.py'

ENTRIES = [('A1: source-coupled scale', 'p0=p_free+lambda rho_M', 'SOURCE_COUPLING_REJECTED', 'direct source dependence remains forbidden', 'rejected'), ('A2: normalization scale', 'solve p_free from target normalization', 'NORMALIZATION_NOT_ORIGIN', 'normalization sets units but does not derive physics', 'open'), ('A3: diagnostic repair scale', 'choose p_free to cancel diagnostic', 'AMPLITUDE_REPAIR_REJECTED', 'repair, not derivation', 'rejected'), ('A4: zero response', 'p_free=0', 'ZERO_RESPONSE_REJECTED_AS_TRIVIAL', 'kills response', 'rejected'), ('A5: underived scale', 'p_free independent but unexplained', 'AMPLITUDE_UNDERIVED', 'still a burden', 'open')]
SHORTCUTS = [('X1: source amplitude', 'derive p_free from rho_M', 'hidden source coupling'), ('X2: normalization as derivation', 'use integral target as physics', 'scale-setting only'), ('X3: zero response', 'claim survival with p_free=0', 'trivial no-response')]
OBLIGATIONS = [('O1: amplitude principle', 'ENERGY_ACCOUNTING_REQUIRED', 'derive p_free from a real principle if candidate remains live', 'avoid arbitrary coefficient')]
LOCAL_CONCLUSIONS = [('amplitude origin not found', 'AMPLITUDE_UNDERIVED', 'p_free remains underived'), ('retention weakened', 'CONDITIONAL_AUDIT_RETENTION_WEAKENED', 'another origin route failed')]


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
        "VARIATIONAL_ORIGIN_OPENED": StatusMark.INFO,
        "REQUIREMENTS_RESTATED": StatusMark.PASS,
        "QUADRATIC_ORIGIN_REJECTED": StatusMark.FAIL,
        "EL_RATIO_NOT_CONSTANT": StatusMark.OBLIGATION,
        "LINEAR_CLOSURE_TESTED": StatusMark.PASS,
        "TRACE_MASS_TENSION_REPRODUCED": StatusMark.OBLIGATION,
        "AMPLITUDE_UNDERIVED": StatusMark.OBLIGATION,
        "AMPLITUDE_REPAIR_REJECTED": StatusMark.FAIL,
        "SOURCE_COUPLING_REJECTED": StatusMark.FAIL,
        "ZERO_RESPONSE_REJECTED_AS_TRIVIAL": StatusMark.FAIL,
        "NORMALIZATION_NOT_ORIGIN": StatusMark.OBLIGATION,
        "BOUNDARY_VARIATION_TESTED": StatusMark.PASS,
        "BOUNDARY_SILENCE_NOT_ORIGIN": StatusMark.OBLIGATION,
        "SIMPLE_ORIGIN_FAILED": StatusMark.FAIL,
        "DIAGNOSTIC_DOWNGRADE_STRENGTHENED": StatusMark.INFO,
        "CONDITIONAL_AUDIT_RETENTION_WEAKENED": StatusMark.DEFER,
        "RETENTION_CONTRACT_REQUIRED": StatusMark.OBLIGATION,
        "STRESS_ACCOUNTING_NOT_CLOSED": StatusMark.OBLIGATION,
        "AUDIT_CANDIDATE_RETAINED": StatusMark.INFO,
        "DIAGNOSTIC_ONLY_DOWNGRADE_POSSIBLE": StatusMark.DEFER,
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
        "QUADRATIC_ORIGIN_REJECTED",
        "AMPLITUDE_REPAIR_REJECTED",
        "SOURCE_COUPLING_REJECTED",
        "ZERO_RESPONSE_REJECTED_AS_TRIVIAL",
        "SIMPLE_ORIGIN_FAILED",
        "REJECTED_ROUTE",
        "FORBIDDEN_SHORTCUT",
    }:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {
        "EL_RATIO_NOT_CONSTANT",
        "TRACE_MASS_TENSION_REPRODUCED",
        "AMPLITUDE_UNDERIVED",
        "NORMALIZATION_NOT_ORIGIN",
        "BOUNDARY_SILENCE_NOT_ORIGIN",
        "RETENTION_CONTRACT_REQUIRED",
        "STRESS_ACCOUNTING_NOT_CLOSED",
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
        "DIAGNOSTIC_ONLY_DOWNGRADE_POSSIBLE",
        "CONDITIONAL_AUDIT_RETENTION_WEAKENED",
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


def layer_symbols():
    y, R, ell, p0 = sp.symbols("y R ell p0", positive=True)
    c = sp.simplify(2*R*ell/(7*R**2 + ell**2))
    eta = sp.simplify((1 - y**2)**2 * (y - c))
    r = sp.simplify(R + ell*y)
    p_r = sp.simplify(p0 * eta**2)
    dp_dr = sp.simplify(sp.diff(p_r, y) / ell)
    p_t = sp.simplify(p_r + r*dp_dr/2)
    P = sp.simplify(p_r + 2*p_t)
    return y, R, ell, p0, r, eta, p_r, p_t, P



def case_amplitude_scale(out: ScriptOutput):
    header("Case 0: Amplitude-origin / scale audit")

    p_free, rho_M, lam, N_target, E_unit, k_trace, k_mass = sp.symbols("p_free rho_M lambda N_target E_unit k_trace k_mass")
    p0_source = sp.simplify(p_free + lam*rho_M)
    source_dep = sp.diff(p0_source, rho_M)

    normalization_solution = sp.solve(sp.Eq(k_trace*p_free, N_target), p_free)
    energy_unit_solution = sp.solve(sp.Eq(k_mass*p_free, E_unit), p_free)
    zero_solution = sp.solve(sp.Eq(p_free, 0), p_free)

    print(f"p0_source = {p0_source}")
    print(f"d p0/d rho_M = {source_dep}")
    print(f"normalization solve = {normalization_solution}")
    print(f"energy-unit solve = {energy_unit_solution}")
    print(f"zero response = {zero_solution}")

    with out.derived_results():
        out.line("source dependence", StatusMark.FAIL, f"{source_dep}")
        out.line("normalization solve", StatusMark.OBLIGATION, f"{normalization_solution}")
        out.line("energy-unit solve", StatusMark.OBLIGATION, f"{energy_unit_solution}")
        out.line("zero response", StatusMark.FAIL, f"{zero_solution}")

    return {"source_dep": source_dep, "normalization": sp.Symbol("normalization_not_origin")}


def record_amp(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g64_amp",
        inputs=[],
        output=data["source_dep"],
        method="audit whether p_free can be derived from source coupling, normalization, diagnostic repair, or zero response",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="amplitude_scale_origin_sieve",
        scope="amplitude-origin audit; not coefficient derivation",
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

    data = case_amplitude_scale(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_amp(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
