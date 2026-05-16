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

SCRIPT_LABEL = 'Candidate Charge-Neutral Source'
MARKER_ID = 'g56_q'
DEPENDENCIES = [('g55_summary', '55_insertion_exclusion_sieve__candidate_group_55_status_summary', 'g55_summary'), ('g56_problem', '56_silent_insert_law__candidate_silent_problem', 'g56_problem'), ('g56_w', '56_silent_insert_law__candidate_boundary_null_profile', 'g56_w')]
QUESTION = 'Can a nontrivial internal profile carry zero net exterior scalar charge?'
DISCIPLINE = 'This script constructs a nontrivial reduced internal profile whose scalar charge integral vanishes. It does not prove physical source admissibility.'
OPENING_LINE = 'Charge-neutral source construction opened'
SCOPE = 'Group 56 charge-neutral internal source'
NEXT_SCRIPT = 'candidate_exterior_tail_zero.py'

ENTRIES = [('Q1: profile construction', 'rho=rho0*(1-5*r^2/(3R^2))', 'CHARGE_NEUTRAL_PROFILE_DERIVED', 'nontrivial internal profile exists', 'reduced source profile'), ('Q2: charge neutrality', 'integral r^2*rho dr from 0 to R is zero', 'CHARGE_NEUTRAL_PROFILE_DERIVED', 'net exterior scalar charge vanishes', 'not source theorem'), ('Q3: nontriviality', 'rho(R/2) is nonzero', 'CHARGE_NEUTRAL_PROFILE_DERIVED', 'silent need not mean identically zero internally', 'not physical source law'), ('Q4: route status', 'charge-neutral internal route survives conditionally', 'SILENT_INSERTION_ROUTE_SURVIVES_CONDITIONALLY', 'requires exterior/tail and source admissibility checks', 'not insertion')]
SHORTCUTS = [('X1: charge-neutral as source-safe', 'treat zero net charge as source no-double-counting proof', 'source routing is separate'), ('X2: internal profile as physical source', 'treat rho profile as inserted matter/source', 'profile is diagnostic'), ('X3: zero charge as full boundary theorem', 'treat Q=0 as full boundary neutrality', 'shell/divergence checks remain')]
OBLIGATIONS = [('O1: exterior tail check', 'SAFETY_THEOREMS_REQUIRED', 'connect Q=0 to exterior scalar tail silence', 'avoid hidden scalar charge'), ('O2: source admissibility', 'SAFETY_THEOREMS_REQUIRED', 'prove internal profile does not duplicate ordinary source load', 'avoid source leakage')]
LOCAL_CONCLUSIONS = [('charge-neutral profile derived', 'PASS', 'nontrivial internal profile has Q=0'), ('physical use blocked', 'NOT_INSERTABLE', 'charge-neutral profile alone is not insertion')]


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
        "SILENT_LAW_SURFACE_OPENED": StatusMark.INFO,
        "BOUNDARY_NULL_PROFILE_DERIVED": StatusMark.PASS,
        "CHARGE_NEUTRAL_PROFILE_DERIVED": StatusMark.PASS,
        "EXTERIOR_TAIL_ZERO_CONDITION_DERIVED": StatusMark.PASS,
        "SHELL_NEUTRAL_CONDITION_DERIVED": StatusMark.PASS,
        "DIVERGENCE_SILENT_CLOSURE_DERIVED": StatusMark.PASS,
        "SILENT_INSERTION_ROUTE_SURVIVES_CONDITIONALLY": StatusMark.INFO,
        "COVARIANT_LIFT_REQUIRED": StatusMark.OBLIGATION,
        "INSERTION_LAW_REQUIRED": StatusMark.OBLIGATION,
        "SAFETY_THEOREMS_REQUIRED": StatusMark.OBLIGATION,
        "PHYSICAL_USE_BLOCKED": StatusMark.DEFER,
        "NOT_INSERTABLE": StatusMark.DEFER,
        "ACTIVE_O_NECESSITY_NOT_ESTABLISHED": StatusMark.DEFER,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "CANDIDATE_SURVIVES_AS_AUDIT_ONLY": StatusMark.INFO,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REJECTED_ROUTE": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "OBSTRUCTION_WITNESS_FOUND": StatusMark.FAIL,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {"REJECTED_ROUTE", "FORBIDDEN_SHORTCUT", "OBSTRUCTION_WITNESS_FOUND"}:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {
        "COVARIANT_LIFT_REQUIRED",
        "INSERTION_LAW_REQUIRED",
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



def case_charge_neutral_source(out: ScriptOutput):
    header("Case 0: Charge-neutral internal source profile")

    r, R, rho0 = sp.symbols("r R rho0", positive=True)
    rho = sp.simplify(rho0 * (1 - 5*r**2/(3*R**2)))
    Q = sp.simplify(sp.integrate(r**2 * rho, (r, 0, R)))
    nonzero_sample = sp.simplify(rho.subs(r, R/2))

    print(f"rho(r) = {rho}")
    print(f"Q = integral_0^R r^2*rho dr = {Q}")
    print(f"rho(R/2) = {nonzero_sample}")

    with out.derived_results():
        out.line("charge-neutral source profile", StatusMark.PASS, f"rho={rho}")
        out.line("net scalar charge", StatusMark.PASS if is_zero(Q) else StatusMark.FAIL, f"Q={Q}")
        out.line("nontrivial interior sample", StatusMark.PASS if not is_zero(nonzero_sample) else StatusMark.FAIL, f"rho(R/2)={nonzero_sample}")

    return {"r": r, "R": R, "rho0": rho0, "rho": rho, "Q": Q, "sample": nonzero_sample}


def record_q(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g56_q",
        inputs=[data["r"], data["R"], data["rho0"]],
        output=data["Q"],
        method="integrate r^2*rho0*(1-5*r^2/(3R^2)) over [0,R]",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="charge_neutral_profile",
        scope="reduced radial scalar charge neutrality; not source theorem",
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

    data = case_charge_neutral_source(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_q(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
