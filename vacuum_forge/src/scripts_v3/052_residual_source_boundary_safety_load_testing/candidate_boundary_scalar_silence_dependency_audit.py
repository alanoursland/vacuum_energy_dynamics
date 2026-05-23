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

SCRIPT_LABEL = 'Candidate Boundary Scalar Silence Dependency Audit'
MARKER_ID = 'g52_boundary_silence'
DEPENDENCIES = [('g51_summary', '051_trace_normalization_adopt_defer_reject_decision_surface__candidate_group_51_status_summary', 'g51_summary'), ('g52_problem', '052_residual_source_boundary_safety_load_testing__candidate_safety_load_test_problem', 'g52_problem'), ('g52_a_mass_protection', '052_residual_source_boundary_safety_load_testing__candidate_a_sector_mass_protection_audit', 'g52_a_mass_protection')]
QUESTION = 'What boundary neutrality and exterior scalar-silence conditions are required before the conditional candidate can touch physical use?'
DISCIPLINE = 'This script audits exterior scalar-tail and boundary neutrality burdens. It does not prove boundary neutrality.'
OPENING_LINE = 'Boundary scalar-silence dependency audit opened -- boundary burdens only'
SCOPE = 'Group 52 boundary scalar silence dependency audit'
NEXT_SCRIPT = 'candidate_safety_load_route_classifier.py'

ENTRIES = [('B1: exterior scalar tail risk', 'a nonzero trace-sector scalar charge would create an exterior scalar tail', 'SCALAR_TAIL_WITNESS', 'q_zeta/r carries nonzero exterior flux', 'not allowed for ordinary exterior'), ('B2: zero-charge condition', 'exterior scalar silence requires zero or neutralized scalar trace charge', 'BOUNDARY_SCALAR_SILENCE_REQUIRED', 'q_zeta=0 is a condition, not a derived theorem', 'not solved'), ('B3: boundary neutrality burden', 'trace normalization must not create shell source, boundary counterterm, or M_ext shift', 'BOUNDARY_SCALAR_SILENCE_REQUIRED', 'boundary behavior must be derived before insertion', 'not insertion'), ('B4: audit-only survival', 'candidate survives only while boundary/scalar silence remains an explicit burden', 'CANDIDATE_SURVIVES_AS_AUDIT_ONLY', 'survival is not exterior neutrality proof', 'not physical use')]
SHORTCUTS = [('X1: scalar silence by assumption', 'set exterior scalar charge to zero without a theorem', 'zero charge must be derived or carried as a condition'), ('X2: boundary counterterm', 'cancel scalar tail with a boundary patch after leakage appears', 'boundary behavior cannot be repair machinery'), ('X3: shell source from trace record', 'let trace normalization create a shell source', 'source law must be independent and explicit')]
OBLIGATIONS = [('O1: boundary neutrality theorem', 'BOUNDARY_SCALAR_SILENCE_REQUIRED', 'derive boundary neutrality before insertion', 'avoid shell/counterterm repair'), ('O2: exterior scalar silence theorem', 'BOUNDARY_SCALAR_SILENCE_REQUIRED', 'derive exterior scalar silence or zero scalar charge', 'avoid scalar tail leakage'), ('O3: M_ext neutrality', 'A_SECTOR_MASS_PROTECTION_REQUIRED', 'prove trace-sector boundary behavior does not shift exterior mass', 'protect A-sector mass coin')]
LOCAL_CONCLUSIONS = [('boundary/scalar silence burdens stated', 'PASS', 'scalar-tail diagnostic names exterior silence burden'), ('boundary theorem not closed', 'BOUNDARY_SCALAR_SILENCE_REQUIRED', 'zero-charge condition remains theorem target')]


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



def case_scalar_tail_diagnostic(out: ScriptOutput):
    header("Case 0: Exterior scalar-tail and boundary charge diagnostic")

    r, q_zeta = sp.symbols("r q_zeta", nonzero=True)
    phi_tail = q_zeta / r
    radial_flux = sp.simplify(4 * sp.pi * r**2 * sp.diff(phi_tail, r))
    silence_residual = sp.simplify(phi_tail.subs(q_zeta, 0))
    flux_silence_residual = sp.simplify(radial_flux.subs(q_zeta, 0))

    print(f"phi_tail = q_zeta/r = {phi_tail}")
    print(f"scalar flux = 4*pi*r^2*d(phi_tail)/dr = {radial_flux}")
    print(f"tail at q_zeta=0 = {silence_residual}")
    print(f"flux at q_zeta=0 = {flux_silence_residual}")

    with out.derived_results():
        out.line(
            "scalar tail flux witness",
            StatusMark.FAIL if not is_zero(radial_flux) else StatusMark.PASS,
            f"flux = {radial_flux}",
        )
        out.line(
            "zero-charge silence diagnostic",
            StatusMark.PASS if is_zero(silence_residual) and is_zero(flux_silence_residual) else StatusMark.FAIL,
            f"tail={silence_residual}, flux={flux_silence_residual} when q_zeta=0",
        )

    return {
        "r": r,
        "q_zeta": q_zeta,
        "phi_tail": phi_tail,
        "radial_flux": radial_flux,
        "silence_residual": silence_residual,
        "flux_silence_residual": flux_silence_residual,
    }


def record_scalar_tail(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g52_scalar_tail_flux_witness",
        inputs=[data["phi_tail"], data["r"], data["q_zeta"]],
        output=data["radial_flux"],
        method="compute 4*pi*r^2*d(q_zeta/r)/dr",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="scalar_tail_flux_witness",
        scope="diagnostic exterior scalar-tail witness; not boundary theorem",
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

    data = case_scalar_tail_diagnostic(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_scalar_tail(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
