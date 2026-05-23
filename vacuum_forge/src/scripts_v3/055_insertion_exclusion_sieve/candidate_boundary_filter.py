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

SCRIPT_LABEL = 'Candidate Boundary Filter'
MARKER_ID = 'g55_boundary'
DEPENDENCIES = [('g54_summary', '054_boundary_neutrality_exterior_scalar_silence_theorem_route__candidate_group_54_status_summary', 'g54_summary'), ('g55_problem', '055_insertion_exclusion_sieve__candidate_insert_problem', 'g55_problem'), ('g55_source', '055_insertion_exclusion_sieve__candidate_source_filter', 'g55_source')]
QUESTION = 'Which insertion families survive reduced exterior scalar silence conditions?'
DISCIPLINE = 'This script applies the boundary filter from Group 54. It rejects scalar-tail, nonzero-flux, and shell-source insertion families.'
OPENING_LINE = 'Boundary filter opened -- reject boundary-leaking insertion'
SCOPE = 'Group 55 boundary filter'
NEXT_SCRIPT = 'candidate_mass_filter.py'

ENTRIES = [('B1: boundary filter', 'C0=0, C1=0, flux=0, and J=0 required', 'BOUNDARY_FILTER_APPLIED', 'reduced exterior silence conditions applied', 'not full theorem'), ('B2: scalar-tail route', 'nonzero C1 creates exterior one-over-r scalar tail', 'BOUNDARY_LEAKING_INSERTION_REJECTED', 'violates exterior silence', 'rejected'), ('B3: shell route', 'nonzero J creates boundary shell source', 'BOUNDARY_LEAKING_INSERTION_REJECTED', 'violates no-shell neutrality', 'rejected'), ('B4: silent boundary route', 'zero tail, zero flux, and no shell survive conditionally', 'SILENT_INSERTION_ROUTE_SURVIVES_CONDITIONALLY', 'requires boundary theorem support', 'not insertion')]
SHORTCUTS = [('X1: boundary repair', 'insert and then cancel scalar tail with counterterm', 'repair is not silence'), ('X2: zero C1 by fiat', 'assume C1=0 without support', 'zero charge must be theorem/condition'), ('X3: shell hidden', 'hide J in boundary term', 'shell source must be explicit')]
OBLIGATIONS = [('O1: boundary theorem required', 'SAFETY_THEOREMS_REQUIRED', 'prove zero tail, zero flux, and no-shell conditions', 'avoid boundary leakage'), ('O2: physical use blocked', 'NOT_INSERTABLE', 'do not insert from conditional boundary survival', 'avoid field-equation drift')]
LOCAL_CONCLUSIONS = [('boundary filter applied', 'PASS', 'scalar-tail and shell-source insertion routes rejected'), ('silent boundary route conditional', 'SILENT_INSERTION_ROUTE_SURVIVES_CONDITIONALLY', 'requires theorem support')]


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



def case_boundary_filter(out: ScriptOutput):
    header("Case 0: Boundary insertion filter")

    r, C0, C1, J = sp.symbols("r C0 C1 J", positive=True)
    phi = C0 + C1/r
    flux = sp.simplify(4*sp.pi*r**2*sp.diff(phi, r))
    silent_phi = sp.simplify(phi.subs({C0:0, C1:0}))
    silent_flux = sp.simplify(flux.subs(C1, 0))
    no_shell = sp.simplify(J.subs(J, 0))

    print(f"phi = {phi}")
    print(f"flux = {flux}")
    print(f"phi|C0=C1=0 = {silent_phi}")
    print(f"flux|C1=0 = {silent_flux}")
    print(f"J|J=0 = {no_shell}")

    with out.derived_results():
        out.line("boundary scalar", StatusMark.PASS, f"phi = {phi}")
        out.line("boundary flux", StatusMark.FAIL if not is_zero(flux) else StatusMark.PASS, f"flux = {flux}")
        out.line("zero-tail condition", StatusMark.PASS if is_zero(silent_phi) else StatusMark.FAIL, f"phi = {silent_phi}")
        out.line("zero-flux condition", StatusMark.PASS if is_zero(silent_flux) else StatusMark.FAIL, f"flux = {silent_flux}")
        out.line("no-shell condition", StatusMark.PASS if is_zero(no_shell) else StatusMark.FAIL, f"J = {no_shell}")

    return {"phi": phi, "flux": flux, "silent_phi": silent_phi, "silent_flux": silent_flux, "no_shell": no_shell}


def record_boundary(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g55_boundary_filter",
        inputs=[],
        output=data["flux"],
        method="boundary insertion filter using phi=C0+C1/r and flux",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="boundary_filter",
        scope="diagnostic boundary filter; not full boundary theorem",
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

    data = case_boundary_filter(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_boundary(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
