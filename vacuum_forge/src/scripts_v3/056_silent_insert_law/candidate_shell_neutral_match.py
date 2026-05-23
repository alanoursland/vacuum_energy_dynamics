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

SCRIPT_LABEL = 'Candidate Shell-Neutral Match'
MARKER_ID = 'g56_shell'
DEPENDENCIES = [('g55_summary', '055_insertion_exclusion_sieve__candidate_group_55_status_summary', 'g55_summary'), ('g56_problem', '056_silent_insert_law__candidate_silent_problem', 'g56_problem'), ('g56_w', '056_silent_insert_law__candidate_boundary_null_profile', 'g56_w'), ('g56_tail', '056_silent_insert_law__candidate_exterior_tail_zero', 'g56_tail')]
QUESTION = 'Does the boundary-null profile avoid a reduced shell jump when matched to exterior zero?'
DISCIPLINE = 'This script verifies reduced no-shell matching for a boundary-null profile and exterior zero. It does not prove a full junction theorem.'
OPENING_LINE = 'Shell-neutral matching check opened'
SCOPE = 'Group 56 shell-neutral match'
NEXT_SCRIPT = 'candidate_divergence_silent_stress.py'

ENTRIES = [('S1: interior boundary value', 'phi_int(R)=0', 'SHELL_NEUTRAL_CONDITION_DERIVED', 'boundary value matches exterior zero', 'reduced'), ('S2: interior derivative', "phi_int'(R)=0", 'SHELL_NEUTRAL_CONDITION_DERIVED', 'boundary derivative matches exterior zero', 'reduced'), ('S3: shell jump', 'J=0', 'SHELL_NEUTRAL_CONDITION_DERIVED', 'reduced shell jump vanishes', 'not full junction theorem'), ('S4: route status', 'boundary-null profile supports no-shell condition conditionally', 'SILENT_INSERTION_ROUTE_SURVIVES_CONDITIONALLY', 'requires theory support', 'not insertion')]
SHORTCUTS = [('X1: shell-neutral as full boundary theorem', 'treat reduced J=0 as full junction proof', 'scope is reduced'), ('X2: no-shell as source theorem', 'treat J=0 as source no-double-counting proof', 'source routing is separate'), ('X3: match as insertion', 'insert because reduced shell jump vanishes', 'matching check is not field equation')]
OBLIGATIONS = [('O1: full matching theorem', 'SAFETY_THEOREMS_REQUIRED', 'derive matching neutrality in the actual geometric setting', 'avoid reduced overclaim'), ('O2: physical use blocked', 'NOT_INSERTABLE', 'do not insert from reduced J=0 alone', 'avoid field-equation drift')]
LOCAL_CONCLUSIONS = [('shell-neutral match derived', 'PASS', 'boundary-null profile matched to exterior zero gives J=0'), ('physical use blocked', 'NOT_INSERTABLE', 'matching check alone is not insertion')]


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



def case_shell_neutral(out: ScriptOutput):
    header("Case 0: Shell-neutral matching from boundary-null profile")

    r, R, A = sp.symbols("r R A", positive=True)
    W = sp.simplify(r**2 * (R-r)**2)
    phi_int = sp.simplify(A*W)
    d_int_R = sp.simplify(sp.diff(phi_int, r).subs(r, R))
    d_ext_R = sp.Integer(0)
    J = sp.simplify(R**2 * (d_ext_R - d_int_R))
    phi_int_R = sp.simplify(phi_int.subs(r, R))

    print(f"phi_int = {phi_int}")
    print(f"phi_int(R) = {phi_int_R}")
    print(f"phi_int'(R) = {d_int_R}")
    print(f"phi_ext'(R) = {d_ext_R}")
    print(f"J = {J}")

    with out.derived_results():
        out.line("interior boundary value", StatusMark.PASS if is_zero(phi_int_R) else StatusMark.FAIL, f"phi_int(R)={phi_int_R}")
        out.line("interior boundary derivative", StatusMark.PASS if is_zero(d_int_R) else StatusMark.FAIL, f"phi_int'(R)={d_int_R}")
        out.line("shell jump", StatusMark.PASS if is_zero(J) else StatusMark.FAIL, f"J={J}")

    return {"r": r, "R": R, "A": A, "phi_int": phi_int, "J": J}


def record_shell(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g56_shell",
        inputs=[data["r"], data["R"], data["A"]],
        output=data["J"],
        method="use phi_int=A*r^2*(R-r)^2 and phi_ext=0 to compute shell jump",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="shell_neutral_match",
        scope="reduced shell-neutral matching; not full junction theorem",
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

    data = case_shell_neutral(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_shell(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
