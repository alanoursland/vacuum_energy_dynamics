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

SCRIPT_LABEL = 'Candidate Trace Mass-Shift Boundary Neutrality Audit'
MARKER_ID = 'g54_boundary_mass'
DEPENDENCIES = [('g53_summary', '053_count_once_trace_residual_source_safety_theorem_route__candidate_group_53_status_summary', 'g53_summary'), ('g54_problem', '054_boundary_neutrality_exterior_scalar_silence_theorem_route__candidate_boundary_scalar_silence_theorem_problem', 'g54_problem'), ('g54_flux_charge', '054_boundary_neutrality_exterior_scalar_silence_theorem_route__candidate_scalar_flux_charge_zero_condition', 'g54_flux_charge'), ('g54_shell_jump', '054_boundary_neutrality_exterior_scalar_silence_theorem_route__candidate_boundary_shell_jump_neutrality_audit', 'g54_shell_jump')]
QUESTION = 'Does zero scalar charge conditionally block trace-sector exterior mass shift?'
DISCIPLINE = 'This script links scalar charge neutrality to trace-sector mass neutrality. It does not prove covariant mass neutrality.'
OPENING_LINE = 'Trace mass-shift boundary neutrality audit opened -- zero-charge mass condition'
SCOPE = 'Group 54 trace mass-shift boundary neutrality audit'
NEXT_SCRIPT = 'candidate_boundary_counterterm_repair_rejection_sieve.py'

ENTRIES = [('M1: mass shift diagnostic', 'Delta_M=alpha*q_zeta', 'A_SECTOR_MASS_PROTECTION_REQUIRED', 'nonzero scalar charge can shift exterior mass', 'not allowed'), ('M2: zero-charge mass neutrality', 'q_zeta=0 gives Delta_M=0', 'TRACE_MASS_SHIFT_BLOCKED_CONDITIONALLY', 'mass shift is blocked if scalar charge is zero', 'conditional'), ('M3: boundary neutrality tie', 'zero scalar charge also supports exterior silence and no mass shift', 'REDUCED_EXTERIOR_SILENCE_SURVIVES_CONDITIONALLY', 'requires theorem support', 'not physical use')]
SHORTCUTS = [('X1: rename mass shift', 'call alpha*q_zeta a dark contribution', 'mass leakage cannot be hidden by labels'), ('X2: zero charge by assumption', 'set q_zeta=0 without theorem or condition', 'zero charge must be justified'), ('X3: mass neutrality as insertion', 'use conditional mass neutrality to insert B_s/F_zeta', 'physical use remains blocked')]
OBLIGATIONS = [('O1: scalar charge neutrality theorem', 'BOUNDARY_SCALAR_SILENCE_REQUIRED', 'prove q_zeta=0 or equivalent no-charge condition', 'avoid scalar tail and mass shift'), ('O2: A-sector mass protection', 'A_SECTOR_MASS_PROTECTION_REQUIRED', 'prove trace-sector boundary behavior does not shift M_ext', 'protect reduced mass coin')]
LOCAL_CONCLUSIONS = [('mass shift condition checked', 'PASS', 'zero scalar charge blocks diagnostic mass shift'), ('mass theorem not closed', 'A_SECTOR_MASS_PROTECTION_REQUIRED', 'zero charge remains condition/theorem target')]


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
        "BOUNDARY_SCALAR_SILENCE_THEOREM_SURFACE_OPENED": StatusMark.INFO,
        "EXTERIOR_LAPLACE_SILENCE_CONDITION_DERIVED": StatusMark.PASS,
        "ZERO_SCALAR_CHARGE_CONDITION_DERIVED": StatusMark.PASS,
        "BOUNDARY_FLUX_NEUTRALITY_CONDITION_DERIVED": StatusMark.PASS,
        "SHELL_SOURCE_ABSENCE_CONDITION_DERIVED": StatusMark.PASS,
        "TRACE_MASS_SHIFT_BLOCKED_CONDITIONALLY": StatusMark.INFO,
        "REDUCED_EXTERIOR_SILENCE_SURVIVES_CONDITIONALLY": StatusMark.INFO,
        "BOUNDARY_COUNTERTERM_REJECTED": StatusMark.FAIL,
        "PHYSICAL_USE_BLOCKED_PENDING_BOUNDARY_THEOREM": StatusMark.DEFER,
        "CANDIDATE_SURVIVES_AS_AUDIT_ONLY": StatusMark.INFO,
        "BOUNDARY_SCALAR_SILENCE_REQUIRED": StatusMark.OBLIGATION,
        "A_SECTOR_MASS_PROTECTION_REQUIRED": StatusMark.OBLIGATION,
        "SAFETY_THEOREMS_REQUIRED": StatusMark.OBLIGATION,
        "ACTIVE_O_NECESSITY_NOT_ESTABLISHED": StatusMark.DEFER,
        "NOT_INSERTABLE": StatusMark.DEFER,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REJECTED_ROUTE": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "OBSTRUCTION_WITNESS_FOUND": StatusMark.FAIL,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {"REJECTED_ROUTE", "FORBIDDEN_SHORTCUT", "BOUNDARY_COUNTERTERM_REJECTED", "OBSTRUCTION_WITNESS_FOUND"}:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {"POLICY_RULE", "BOUNDARY_SCALAR_SILENCE_REQUIRED", "A_SECTOR_MASS_PROTECTION_REQUIRED", "SAFETY_THEOREMS_REQUIRED"}:
        return GovernanceStatus.POLICY_RULE
    return GovernanceStatus.UNVERIFIED


def obligation_status(status: str) -> ObligationStatus:
    if status in {"PHYSICAL_USE_BLOCKED_PENDING_BOUNDARY_THEOREM", "NOT_INSERTABLE", "DEFERRED_WITH_TARGET", "ACTIVE_O_NECESSITY_NOT_ESTABLISHED"}:
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



def case_mass_shift(out: ScriptOutput):
    header("Case 0: Trace mass-shift boundary neutrality audit")

    alpha, q_zeta = sp.symbols("alpha q_zeta")
    mass_shift = sp.simplify(alpha * q_zeta)
    zero_charge_shift = sp.simplify(mass_shift.subs(q_zeta, 0))

    print(f"Trace-sector mass shift diagnostic: Delta_M = {mass_shift}")
    print(f"Zero scalar charge q_zeta=0 gives Delta_M = {zero_charge_shift}")

    with out.derived_results():
        out.line("trace mass shift", StatusMark.FAIL if not is_zero(mass_shift) else StatusMark.PASS, f"Delta_M = {mass_shift}")
        out.line("zero-charge mass neutrality", StatusMark.PASS if is_zero(zero_charge_shift) else StatusMark.FAIL, f"Delta_M|q=0 = {zero_charge_shift}")

    return {"alpha": alpha, "q_zeta": q_zeta, "mass_shift": mass_shift, "zero_charge_shift": zero_charge_shift}


def record_mass(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g54_boundary_trace_mass_shift_condition",
        inputs=[data["alpha"], data["q_zeta"]],
        output=data["mass_shift"],
        method="diagnostic trace-sector exterior mass shift alpha*q_zeta",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="mass_shift_condition",
        scope="diagnostic scalar charge mass-shift condition; not covariant mass theorem",
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

    data = case_mass_shift(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_mass(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
