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

SCRIPT_LABEL = 'Candidate Exterior Radial Laplace Silence Theorem Attempt'
MARKER_ID = 'g54_laplace'
DEPENDENCIES = [('g53_summary', '053_count_once_trace_residual_source_safety_theorem_route__candidate_group_53_status_summary', 'g53_summary'), ('g54_problem', '054_boundary_neutrality_exterior_scalar_silence_theorem_route__candidate_boundary_scalar_silence_theorem_problem', 'g54_problem')]
QUESTION = 'Does the reduced homogeneous exterior scalar equation yield a zero-tail condition?'
DISCIPLINE = 'This script derives the reduced static-spherical exterior scalar form and the zero-tail condition. It is not a full covariant boundary theorem.'
OPENING_LINE = 'Exterior radial Laplace silence theorem attempt opened -- reduced symbolic derivation'
SCOPE = 'Group 54 reduced exterior radial Laplace theorem attempt'
NEXT_SCRIPT = 'candidate_scalar_flux_charge_zero_condition.py'

ENTRIES = [('L1: exterior solution', 'homogeneous radial exterior scalar has phi=C0+C1/r', 'EXTERIOR_LAPLACE_SILENCE_CONDITION_DERIVED', 'the reduced ansatz satisfies the radial equation', 'not covariant uniqueness'), ('L2: asymptotic offset', 'C0=0 removes exterior constant scalar offset', 'EXTERIOR_LAPLACE_SILENCE_CONDITION_DERIVED', 'zero offset is a boundary/asymptotic condition', 'not automatic'), ('L3: zero-tail condition', 'C0=0 and C1=0 imply phi=0', 'EXTERIOR_LAPLACE_SILENCE_CONDITION_DERIVED', 'zero scalar charge is still required', 'not full boundary proof'), ('L4: candidate status', 'candidate remains audit-only', 'CANDIDATE_SURVIVES_AS_AUDIT_ONLY', 'reduced silence condition does not license insertion', 'not physical use')]
SHORTCUTS = [('X1: reduced theorem as full theorem', 'treat radial exterior result as full covariant boundary theorem', 'scope is reduced static-spherical'), ('X2: C1 zero by declaration', 'set C1=0 without charge/flux condition', 'zero charge must be derived or carried as condition'), ('X3: constant offset as silence', 'leave C0 nonzero and call it scalar silence', 'offset requires asymptotic/gauge handling')]
OBLIGATIONS = [('O1: scalar charge condition', 'BOUNDARY_SCALAR_SILENCE_REQUIRED', 'derive or impose C1=0 via zero scalar charge/flux', 'avoid scalar tail'), ('O2: asymptotic offset condition', 'BOUNDARY_SCALAR_SILENCE_REQUIRED', 'derive or set C0=0 as asymptotic scalar reference', 'avoid constant exterior trace offset'), ('O3: insertion remains closed', 'NOT_INSERTABLE', 'do not treat reduced silence condition as B_s/F_zeta insertion license', 'avoid field-equation drift')]
LOCAL_CONCLUSIONS = [('reduced exterior solution checked', 'PASS', 'phi=C0+C1/r satisfies the homogeneous radial equation'), ('silence condition conditional', 'EXTERIOR_LAPLACE_SILENCE_CONDITION_DERIVED', 'zero offset plus zero scalar charge gives phi=0')]


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



def case_radial_laplace_solution(out: ScriptOutput):
    header("Case 0: Reduced exterior radial Laplace theorem attempt")

    r = sp.symbols("r", positive=True)
    C0, C1 = sp.symbols("C0 C1")
    phi = C0 + C1 / r
    radial_laplace = sp.simplify(sp.diff(r**2 * sp.diff(phi, r), r) / r**2)
    asym_zero_phi = sp.simplify(phi.subs(C0, 0))
    silent_phi = sp.simplify(phi.subs({C0: 0, C1: 0}))

    print(f"Exterior ansatz phi(r) = {phi}")
    print("Radial homogeneous equation: (r^2 phi')'/r^2 = 0")
    print(f"Equation residual = {radial_laplace}")
    print(f"With zero asymptotic offset C0=0: phi = {asym_zero_phi}")
    print(f"With C0=0 and C1=0: phi = {silent_phi}")

    with out.derived_results():
        out.line("radial Laplace residual", StatusMark.PASS if is_zero(radial_laplace) else StatusMark.FAIL, f"residual = {radial_laplace}")
        out.line("zero-offset one-over-r tail", StatusMark.PASS, f"phi|C0=0 = {asym_zero_phi}")
        out.line("zero-offset zero-charge silence", StatusMark.PASS if is_zero(silent_phi) else StatusMark.FAIL, f"phi|C0=C1=0 = {silent_phi}")

    return {"r": r, "C0": C0, "C1": C1, "phi": phi, "radial_laplace": radial_laplace, "silent_phi": silent_phi}


def record_laplace(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g54_laplace_exterior_solution_residual",
        inputs=[data["r"], data["C0"], data["C1"]],
        output=data["radial_laplace"],
        method="verify phi=C0+C1/r satisfies reduced homogeneous radial Laplace equation",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="reduced_exterior_laplace_residual",
        scope="reduced static-spherical exterior scalar theorem surface; not covariant theorem",
    )
    ns.record_derivation(
        derivation_id="g54_laplace_zero_tail_condition",
        inputs=[data["C0"], data["C1"]],
        output=data["silent_phi"],
        method="substitute C0=0 and C1=0 into exterior solution",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="zero_tail_condition",
        scope="conditional exterior scalar silence; not insertion permission",
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

    data = case_radial_laplace_solution(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_laplace(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
