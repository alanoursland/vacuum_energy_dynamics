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

SCRIPT_LABEL = 'Candidate Scalar Flux / Charge Zero Condition'
MARKER_ID = 'g54_flux_charge'
DEPENDENCIES = [('g53_summary', '053_count_once_trace_residual_source_safety_theorem_route__candidate_group_53_status_summary', 'g53_summary'), ('g54_problem', '054_boundary_neutrality_exterior_scalar_silence_theorem_route__candidate_boundary_scalar_silence_theorem_problem', 'g54_problem'), ('g54_laplace', '054_boundary_neutrality_exterior_scalar_silence_theorem_route__candidate_exterior_radial_laplace_silence_theorem_attempt', 'g54_laplace')]
QUESTION = 'What scalar flux/charge condition kills the exterior one-over-r scalar tail?'
DISCIPLINE = 'This script computes the reduced exterior scalar flux and identifies the zero-charge condition. It does not prove that the condition holds.'
OPENING_LINE = 'Scalar flux / charge zero condition opened -- reduced flux calculation'
SCOPE = 'Group 54 scalar flux / charge zero condition'
NEXT_SCRIPT = 'candidate_boundary_shell_jump_neutrality_audit.py'

ENTRIES = [('F1: scalar flux', 'phi=C1/r gives F_phi=-4*pi*C1', 'BOUNDARY_FLUX_NEUTRALITY_CONDITION_DERIVED', 'nonzero C1 gives nonzero exterior scalar flux', 'not allowed for scalar silence'), ('F2: scalar charge', 'C1 is the scalar charge coefficient up to sign convention', 'ZERO_SCALAR_CHARGE_CONDITION_DERIVED', 'zero scalar charge is C1=0', 'not automatic'), ('F3: zero flux condition', 'C1=0 gives F_phi=0', 'ZERO_SCALAR_CHARGE_CONDITION_DERIVED', 'zero flux condition kills one-over-r charge', 'not full boundary theorem'), ('F4: physical use', 'candidate remains blocked pending boundary theorem', 'PHYSICAL_USE_BLOCKED_PENDING_BOUNDARY_THEOREM', 'flux calculation does not license insertion', 'not insertable')]
SHORTCUTS = [('X1: ignore nonzero flux', 'allow C1/r tail while claiming scalar silence', 'nonzero flux is not silence'), ('X2: zero charge by fiat', 'set C1=0 without theorem or condition', 'zero charge must be justified'), ('X3: flux as insertion', 'use flux calculation to insert B_s/F_zeta', 'calculation is safety condition only')]
OBLIGATIONS = [('O1: zero scalar charge theorem', 'BOUNDARY_SCALAR_SILENCE_REQUIRED', 'prove or condition C1=0', 'avoid exterior scalar tail'), ('O2: boundary origin of zero flux', 'BOUNDARY_SCALAR_SILENCE_REQUIRED', 'connect C1=0 to boundary neutrality or source absence', 'avoid fiat')]
LOCAL_CONCLUSIONS = [('flux condition derived', 'PASS', 'reduced scalar flux is -4*pi*C1'), ('zero charge condition conditional', 'ZERO_SCALAR_CHARGE_CONDITION_DERIVED', 'C1=0 is required for silence')]


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



def case_flux_charge(out: ScriptOutput):
    header("Case 0: Scalar flux / charge zero condition")

    r, C1 = sp.symbols("r C1", positive=True)
    phi = C1 / r
    flux = sp.simplify(4 * sp.pi * r**2 * sp.diff(phi, r))
    zero_flux = sp.simplify(flux.subs(C1, 0))
    charge_from_flux = sp.simplify(-flux / (4 * sp.pi))

    print(f"phi_tail = {phi}")
    print(f"F_phi = 4*pi*r^2*phi' = {flux}")
    print(f"scalar charge convention q_phi = -F_phi/(4*pi) = {charge_from_flux}")
    print(f"zero C1 gives flux = {zero_flux}")

    with out.derived_results():
        out.line("scalar flux", StatusMark.FAIL if not is_zero(flux) else StatusMark.PASS, f"F_phi = {flux}")
        out.line("charge coefficient", StatusMark.PASS, f"q_phi = {charge_from_flux}")
        out.line("zero-charge flux condition", StatusMark.PASS if is_zero(zero_flux) else StatusMark.FAIL, f"F_phi|C1=0 = {zero_flux}")

    return {"r": r, "C1": C1, "phi": phi, "flux": flux, "zero_flux": zero_flux, "charge": charge_from_flux}


def record_flux(ns, data) -> None:
    ns.record_derivation(
        derivation_id="g54_scalar_flux_charge_condition",
        inputs=[data["r"], data["C1"]],
        output=data["flux"],
        method="compute 4*pi*r^2*d(C1/r)/dr",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="scalar_flux_condition",
        scope="reduced exterior scalar flux; not full boundary theorem",
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

    data = case_flux_charge(out)

    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)
    record_flux(ns, data)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
