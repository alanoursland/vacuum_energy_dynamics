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

SCRIPT_LABEL = 'Candidate Boundary Shell-Jump Neutrality Audit'
MARKER_ID = 'g54_shell_jump'
DEPENDENCIES = [('g53_summary', '53_count_once_trace_residual_source_safety_theorem_route__candidate_group_53_status_summary', 'g53_summary'), ('g54_problem', '54_boundary_neutrality_exterior_scalar_silence_theorem_route__candidate_boundary_scalar_silence_theorem_problem', 'g54_problem'), ('g54_flux_charge', '54_boundary_neutrality_exterior_scalar_silence_theorem_route__candidate_scalar_flux_charge_zero_condition', 'g54_flux_charge')]
QUESTION = 'What boundary derivative-jump condition prevents a shell scalar source?'
DISCIPLINE = 'This script computes a reduced matching-surface scalar derivative jump. It does not prove full junction neutrality.'
OPENING_LINE = 'Boundary shell-jump neutrality audit opened -- reduced jump condition'
SCOPE = 'Group 54 boundary shell-jump neutrality audit'
NEXT_SCRIPT = 'candidate_trace_mass_shift_boundary_neutrality_audit.py'

ENTRIES = [('J1: shell jump condition', "J=R^2*(phi_ext'(R)-phi_int'(R))", 'SHELL_SOURCE_ABSENCE_CONDITION_DERIVED', 'nonzero jump is shell-source diagnostic', 'not full junction theorem'), ('J2: no-shell matching', 'J=0 requires matched derivative / neutral boundary', 'SHELL_SOURCE_ABSENCE_CONDITION_DERIVED', 'matching condition must be proven or imposed', 'not automatic'), ('J3: zero-charge zero-derivative case', 'C1=0 and interior derivative zero gives J=0', 'SHELL_SOURCE_ABSENCE_CONDITION_DERIVED', 'conditional no-shell case', 'not full boundary proof'), ('J4: counterterm risk', 'boundary repair terms cannot replace neutrality theorem', 'BOUNDARY_SCALAR_SILENCE_REQUIRED', 'repair is not silence', 'not allowed')]
SHORTCUTS = [('X1: shell source hidden', 'hide derivative jump in a boundary term', 'shell source must be explicit'), ('X2: counterterm repair', 'cancel shell source after creating it', 'repair is not neutral matching'), ('X3: no-shell by declaration', 'declare J=0 without matching condition', 'zero jump must be derived or conditioned')]
OBLIGATIONS = [('O1: no-shell theorem', 'BOUNDARY_SCALAR_SILENCE_REQUIRED', 'derive derivative-jump neutrality at matching surface', 'avoid shell sources'), ('O2: connect to source absence', 'BOUNDARY_SCALAR_SILENCE_REQUIRED', 'connect no-shell condition to absence of trace-sector boundary source', 'avoid boundary patch')]
LOCAL_CONCLUSIONS = [('shell jump condition derived', 'PASS', 'reduced derivative-jump condition stated'), ('no-shell condition conditional', 'SHELL_SOURCE_ABSENCE_CONDITION_DERIVED', 'J=0 requires matching/zero-charge support')]


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



def case_shell_jump(out: ScriptOutput):
    header("Case 0: Boundary shell-jump neutrality audit")

    R, C1, a_int = sp.symbols("R C1 a_int", positive=True)
    phi_ext_prime_R = -C1 / R**2
    phi_int_prime_R = a_int
    shell_jump = sp.simplify(R**2 * (phi_ext_prime_R - phi_int_prime_R))
    no_shell_int_condition = sp.simplify(shell_jump.subs({C1: 0, a_int: 0}))
    no_shell_match_condition = sp.solve(sp.Eq(shell_jump, 0), a_int)

    print(f"phi_ext'(R) = {phi_ext_prime_R}")
    print(f"phi_int'(R) = {phi_int_prime_R}")
    print(f"J = R^2*(phi_ext'(R)-phi_int'(R)) = {shell_jump}")
    print(f"No-shell matching condition solved for a_int: {no_shell_match_condition}")
    print(f"With C1=0 and a_int=0: J = {no_shell_int_condition}")

    with out.derived_results():
        out.line("shell jump", StatusMark.FAIL if not is_zero(shell_jump) else StatusMark.PASS, f"J = {shell_jump}")
        out.line("no-shell matching condition", StatusMark.PASS, f"a_int = {no_shell_match_condition}")
        out.line("zero exterior charge + zero interior derivative", StatusMark.PASS if is_zero(no_shell_int_condition) else StatusMark.FAIL, f"J = {no_shell_int_condition}")

    return {"R": R, "C1": C1, "a_int": a_int, "shell_jump": shell_jump, "zero_case": no_shell_int_condition}


def record_shell(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g54_boundary_shell_jump_condition",
        inputs=[data["R"], data["C1"], data["a_int"]],
        output=data["shell_jump"],
        method="compute R^2*(phi_ext_prime(R)-phi_int_prime(R))",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="shell_jump_condition",
        scope="reduced matching-surface diagnostic; not full junction theorem",
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

    data = case_shell_jump(out)

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
