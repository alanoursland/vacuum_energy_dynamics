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

SCRIPT_LABEL = 'Candidate Boundary Scalar Silence Route Classifier'
MARKER_ID = 'g54_route_classifier'
DEPENDENCIES = [('g53_summary', '53_count_once_trace_residual_source_safety_theorem_route__candidate_group_53_status_summary', 'g53_summary'), ('g54_problem', '54_boundary_neutrality_exterior_scalar_silence_theorem_route__candidate_boundary_scalar_silence_theorem_problem', 'g54_problem'), ('g54_laplace', '54_boundary_neutrality_exterior_scalar_silence_theorem_route__candidate_exterior_radial_laplace_silence_theorem_attempt', 'g54_laplace'), ('g54_flux_charge', '54_boundary_neutrality_exterior_scalar_silence_theorem_route__candidate_scalar_flux_charge_zero_condition', 'g54_flux_charge'), ('g54_shell_jump', '54_boundary_neutrality_exterior_scalar_silence_theorem_route__candidate_boundary_shell_jump_neutrality_audit', 'g54_shell_jump'), ('g54_boundary_mass', '54_boundary_neutrality_exterior_scalar_silence_theorem_route__candidate_trace_mass_shift_boundary_neutrality_audit', 'g54_boundary_mass'), ('g54_counterterm_sieve', '54_boundary_neutrality_exterior_scalar_silence_theorem_route__candidate_boundary_counterterm_repair_rejection_sieve', 'g54_counterterm_sieve')]
QUESTION = 'After reduced exterior Laplace, flux, shell-jump, and mass-shift checks, what is the honest boundary/scalar-silence route status?'
DISCIPLINE = 'This classifier reports the reduced boundary/scalar-silence status. It must not turn conditional silence into insertion permission.'
OPENING_LINE = 'Boundary scalar silence route classifier opened -- route classification only'
SCOPE = 'Group 54 boundary scalar silence route classifier'
NEXT_SCRIPT = 'candidate_boundary_scalar_silence_batch_reconciliation.py'

ENTRIES = [('C1: reduced theorem surface', 'homogeneous exterior scalar route gives phi=C0+C1/r', 'EXTERIOR_LAPLACE_SILENCE_CONDITION_DERIVED', 'reduced exterior calculation exists', 'not covariant theorem'), ('C2: zero-tail condition', 'C0=0 and C1=0 imply phi=0', 'ZERO_SCALAR_CHARGE_CONDITION_DERIVED', 'zero offset and zero charge required', 'not automatic'), ('C3: flux condition', 'F_phi=-4*pi*C1, so zero flux requires C1=0', 'BOUNDARY_FLUX_NEUTRALITY_CONDITION_DERIVED', 'scalar charge must vanish', 'not proved'), ('C4: shell condition', 'J=0 required for no boundary shell source', 'SHELL_SOURCE_ABSENCE_CONDITION_DERIVED', 'matching neutrality required', 'not full junction theorem'), ('C5: mass condition', 'zero scalar charge blocks diagnostic trace mass shift', 'TRACE_MASS_SHIFT_BLOCKED_CONDITIONALLY', 'mass neutrality conditional', 'not full mass theorem'), ('C6: route status', 'reduced exterior silence route survives conditionally', 'REDUCED_EXTERIOR_SILENCE_SURVIVES_CONDITIONALLY', 'physical use remains blocked pending theorem support', 'not insertable'), ('C7: active O status', 'active O necessity still not established', 'ACTIVE_O_NECESSITY_NOT_ESTABLISHED', 'boundary route has not forced O', 'not O construction')]
SHORTCUTS = [('X1: classifier as boundary proof', 'treat route classification as proving boundary neutrality', 'classification is not full theorem'), ('X2: conditional silence as insertion', 'insert B_s/F_zeta from reduced silence route', 'physical use remains blocked'), ('X3: O jump', 'declare active O necessary because boundary conditions are hard', 'difficulty is not obstruction'), ('X4: ignore reduced scope', 'use reduced static-spherical theorem as covariant parent result', 'scope remains reduced')]
OBLIGATIONS = [('O1: boundary theorem support', 'BOUNDARY_SCALAR_SILENCE_REQUIRED', 'prove zero offset, zero scalar charge, and no shell under theory conditions', 'turn route into theorem'), ('O2: physical use blocked', 'PHYSICAL_USE_BLOCKED_PENDING_BOUNDARY_THEOREM', 'keep insertion closed pending boundary theorem', 'avoid status inflation'), ('O3: reduced-to-general gap', 'SAFETY_THEOREMS_REQUIRED', 'do not treat reduced exterior result as full covariant theorem', 'preserve scope')]
LOCAL_CONCLUSIONS = [('boundary route classified', 'PASS', 'reduced exterior silence route survives conditionally'), ('physical use still blocked', 'PHYSICAL_USE_BLOCKED_PENDING_BOUNDARY_THEOREM', 'no insertion route opened')]


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


    print_entries(out, entries, f"Case 1: {SCRIPT_LABEL} entries")
    print_shortcuts(out, shortcuts)
    print_obligations(out, obligations)

    header("Local conclusions")
    for label, status, text in LOCAL_CONCLUSIONS:
        with out.governance_assessments():
            out.line(label, mark(status), text)

    record_governance(ns, MARKER_ID, entries, obligations, SCOPE)

    ns.write_run_metadata()

    print("\nPossible next script:")
    print(f"  {NEXT_SCRIPT}")


if __name__ == "__main__":
    main()
