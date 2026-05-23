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

SCRIPT_LABEL = 'Candidate Trace/Mass Closure Sieve'
MARKER_ID = 'g62_closure'
DEPENDENCIES = [('g61_summary', '061_source_safety_audit__candidate_group_61_status_summary', 'g61_summary'), ('g62_problem', '062_stress_energy_accounting__candidate_stress_problem', 'g62_problem'), ('g62_inv', '062_stress_energy_accounting__candidate_closure_inventory', 'g62_inv')]
QUESTION = 'Can a one-parameter closure u=gamma*P satisfy trace-free and active-mass-neutral diagnostics?'
DISCIPLINE = 'This script derives the trace/mass closure conflict algebraically.'
OPENING_LINE = 'Trace/mass closure sieve opened'
SCOPE = 'Group 62 trace mass closure sieve'
NEXT_SCRIPT = 'candidate_pressure_sum_obstruction.py'

ENTRIES = [('C1: trace-free closure', 'u=P or gamma=1', 'TRACE_CLOSURE_IDENTIFIED', 'trace-free route is available algebraically', 'not mass safe'), ('C2: active-mass-neutral closure', 'u=-P or gamma=-1', 'ACTIVE_MASS_CLOSURE_IDENTIFIED', 'active-mass-neutral route is available algebraically', 'not trace safe'), ('C3: simultaneous closure', 'requires P=0', 'TRACE_MASS_TENSION_CONFIRMED', 'one closure cannot satisfy both unless pressure sum vanishes', 'open obstruction')]
SHORTCUTS = [('X1: trace-free as mass-safe', 'use gamma=1 for both diagnostics', 'active diagnostic remains 2P'), ('X2: active-mass-neutral as trace-free', 'use gamma=-1 for both diagnostics', 'trace diagnostic remains 2P'), ('X3: arbitrary gamma', 'choose gamma by convenience', 'diagnostics fix incompatible gamma values')]
OBLIGATIONS = [('O1: pressure-sum obstruction', 'ENERGY_ACCOUNTING_REQUIRED', 'test whether P is actually zero for the layer', 'determine simultaneous closure status')]
LOCAL_CONCLUSIONS = [('trace mass tension confirmed', 'TRACE_MASS_TENSION_CONFIRMED', 'u=gamma*P cannot close both diagnostics unless P=0'), ('stress accounting not closed', 'STRESS_ACCOUNTING_NOT_CLOSED', 'closure choice remains underived')]


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
        "STRESS_AUDIT_OPENED": StatusMark.INFO,
        "CLOSURE_INVENTORY_DERIVED": StatusMark.PASS,
        "TRACE_CLOSURE_IDENTIFIED": StatusMark.INFO,
        "ACTIVE_MASS_CLOSURE_IDENTIFIED": StatusMark.INFO,
        "TRACE_MASS_TENSION_CONFIRMED": StatusMark.OBLIGATION,
        "PRESSURE_SUM_OBSTRUCTION_FOUND": StatusMark.OBLIGATION,
        "INTEGRAL_ACCOUNTING_DERIVED": StatusMark.PASS,
        "ACTIVE_MASS_BURDEN_FOUND": StatusMark.OBLIGATION,
        "TRACE_BURDEN_FOUND": StatusMark.OBLIGATION,
        "ENERGY_SIGN_BURDEN_FOUND": StatusMark.OBLIGATION,
        "ARBITRARY_CLOSURE_REJECTED": StatusMark.FAIL,
        "ZERO_RESPONSE_REJECTED_AS_TRIVIAL": StatusMark.FAIL,
        "AMPLITUDE_UNDERIVED": StatusMark.OBLIGATION,
        "SOURCE_COUPLING_REJECTED": StatusMark.FAIL,
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
        "ARBITRARY_CLOSURE_REJECTED",
        "ZERO_RESPONSE_REJECTED_AS_TRIVIAL",
        "SOURCE_COUPLING_REJECTED",
        "REJECTED_ROUTE",
        "FORBIDDEN_SHORTCUT",
    }:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {
        "TRACE_MASS_TENSION_CONFIRMED",
        "PRESSURE_SUM_OBSTRUCTION_FOUND",
        "ACTIVE_MASS_BURDEN_FOUND",
        "TRACE_BURDEN_FOUND",
        "ENERGY_SIGN_BURDEN_FOUND",
        "AMPLITUDE_UNDERIVED",
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



def case_trace_mass_closure(out: ScriptOutput):
    header("Case 0: u=gamma*P trace/mass closure sieve")

    gamma, P = sp.symbols("gamma P")
    u = sp.simplify(gamma*P)
    trace_diag = sp.simplify(-u + P)
    active_diag = sp.simplify(u + P)

    gamma_trace = sp.solve(sp.Eq(trace_diag, 0), gamma)
    gamma_active = sp.solve(sp.Eq(active_diag, 0), gamma)
    simultaneous = sp.solve([sp.Eq(trace_diag, 0), sp.Eq(active_diag, 0)], [gamma, P], dict=True)

    print(f"u = {u}")
    print(f"T=-u+P = {trace_diag}")
    print(f"A=u+P = {active_diag}")
    print(f"trace-free gamma = {gamma_trace}")
    print(f"active-mass-neutral gamma = {gamma_active}")
    print(f"simultaneous solve = {simultaneous}")

    with out.derived_results():
        out.line("trace-free closure", StatusMark.INFO, f"gamma={gamma_trace}")
        out.line("active-mass-neutral closure", StatusMark.INFO, f"gamma={gamma_active}")
        out.line("simultaneous condition", StatusMark.OBLIGATION, f"{simultaneous}")

    return {"trace_diag": trace_diag, "active_diag": active_diag, "simultaneous": sp.Symbol("P_required_zero")}


def record_closure(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g62_closure",
        inputs=[],
        output=data["simultaneous"],
        method="derive gamma closure conditions for trace-free and active-mass-neutral diagnostics",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="trace_mass_closure_sieve",
        scope="reduced closure algebra; not stress-energy theorem",
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

    data = case_trace_mass_closure(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_closure(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
