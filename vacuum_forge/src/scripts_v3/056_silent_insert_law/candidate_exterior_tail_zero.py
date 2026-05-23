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

SCRIPT_LABEL = 'Candidate Exterior Tail Zero'
MARKER_ID = 'g56_tail'
DEPENDENCIES = [('g55_summary', '055_insertion_exclusion_sieve__candidate_group_55_status_summary', 'g55_summary'), ('g56_problem', '056_silent_insert_law__candidate_silent_problem', 'g56_problem'), ('g56_q', '056_silent_insert_law__candidate_charge_neutral_source', 'g56_q')]
QUESTION = 'Does zero scalar charge plus zero offset kill the reduced exterior scalar tail?'
DISCIPLINE = 'This script links charge neutrality to exterior scalar silence in the reduced exterior. It does not prove the full boundary theorem.'
OPENING_LINE = 'Exterior tail zero condition opened'
SCOPE = 'Group 56 exterior tail zero'
NEXT_SCRIPT = 'candidate_shell_neutral_match.py'

ENTRIES = [('E1: tail relation', 'phi_ext=C0+kQ/r', 'EXTERIOR_TAIL_ZERO_CONDITION_DERIVED', 'exterior one-over-r tail tied to net charge', 'reduced relation'), ('E2: silence condition', 'C0=0 and Q=0 imply phi_ext=0', 'EXTERIOR_TAIL_ZERO_CONDITION_DERIVED', 'zero charge plus zero offset kills tail', 'conditional'), ('E3: route status', 'charge-neutral route supports reduced exterior silence conditionally', 'SILENT_INSERTION_ROUTE_SURVIVES_CONDITIONALLY', 'requires theorem support', 'not insertion')]
SHORTCUTS = [('X1: Q=0 by fiat', 'assume scalar charge zero without profile/theorem', 'Group 56 has profile surface, not final theorem'), ('X2: C0 ignored', 'leave constant exterior offset unconstrained', 'zero offset remains condition'), ('X3: reduced tail as full theorem', 'treat reduced exterior silence as covariant boundary closure', 'scope is reduced')]
OBLIGATIONS = [('O1: boundary theorem', 'SAFETY_THEOREMS_REQUIRED', 'derive zero charge and zero offset from theory conditions', 'avoid assumption'), ('O2: covariant lift', 'COVARIANT_LIFT_REQUIRED', 'lift reduced exterior silence to applicable boundary setting', 'avoid overclaim')]
LOCAL_CONCLUSIONS = [('exterior tail zero condition derived', 'PASS', 'C0=0 and Q=0 imply phi_ext=0'), ('physical use blocked', 'NOT_INSERTABLE', 'tail silence condition alone is not insertion')]


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



def case_tail_zero(out: ScriptOutput):
    header("Case 0: Exterior tail from scalar charge")

    r, C0, Q, k = sp.symbols("r C0 Q k", positive=True)
    C1 = sp.simplify(k*Q)
    phi = sp.simplify(C0 + C1/r)
    silent_phi = sp.simplify(phi.subs({C0: 0, Q: 0}))

    print(f"C1 = k*Q = {C1}")
    print(f"phi_ext = {phi}")
    print(f"phi_ext with C0=0 and Q=0 = {silent_phi}")

    with out.derived_results():
        out.line("exterior tail relation", StatusMark.PASS, f"phi={phi}")
        out.line("zero charge zero offset", StatusMark.PASS if is_zero(silent_phi) else StatusMark.FAIL, f"phi={silent_phi}")

    return {"r": r, "C0": C0, "Q": Q, "k": k, "phi": phi, "silent_phi": silent_phi}


def record_tail(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g56_tail",
        inputs=[data["C0"], data["Q"], data["k"], data["r"]],
        output=data["silent_phi"],
        method="set C1=kQ and substitute C0=0,Q=0",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="exterior_tail_zero",
        scope="reduced exterior scalar tail condition; not full boundary theorem",
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

    data = case_tail_zero(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_tail(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
