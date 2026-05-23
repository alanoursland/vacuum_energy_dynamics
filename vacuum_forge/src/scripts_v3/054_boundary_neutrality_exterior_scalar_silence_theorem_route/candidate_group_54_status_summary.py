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
SCRIPT_LABEL = "Candidate Group 54 Status Summary"
MARKER_ID = "g54_summary"

DEPENDENCIES = [
    ("g53_summary", "054_boundary_neutrality_exterior_scalar_silence_theorem_route__candidate_boundary_scalar_silence_theorem_problem", "g54_problem"),
    ("g54_laplace", "054_boundary_neutrality_exterior_scalar_silence_theorem_route__candidate_exterior_radial_laplace_silence_theorem_attempt", "g54_laplace"),
    ("g54_flux", "054_boundary_neutrality_exterior_scalar_silence_theorem_route__candidate_scalar_flux_charge_zero_condition", "g54_flux_charge"),
    ("g54_shell", "054_boundary_neutrality_exterior_scalar_silence_theorem_route__candidate_boundary_shell_jump_neutrality_audit", "g54_shell_jump"),
    ("g54_mass", "054_boundary_neutrality_exterior_scalar_silence_theorem_route__candidate_trace_mass_shift_boundary_neutrality_audit", "g54_boundary_mass"),
    ("g54_repair", "054_boundary_neutrality_exterior_scalar_silence_theorem_route__candidate_boundary_counterterm_repair_rejection_sieve", "g54_counterterm_sieve"),
    ("g54_classifier", "054_boundary_neutrality_exterior_scalar_silence_theorem_route__candidate_boundary_scalar_silence_route_classifier", "g54_route_classifier"),
    ("g54_reconcile", "054_boundary_neutrality_exterior_scalar_silence_theorem_route__candidate_boundary_scalar_silence_batch_reconciliation", "g54_reconciliation"),
]


@dataclass(frozen=True)
class StatusEntry:
    name: str
    status: str
    conclusion: str
    boundary: str


@dataclass(frozen=True)
class ConditionEntry:
    name: str
    status: str
    condition: str
    meaning: str
    boundary: str


@dataclass(frozen=True)
class BurdenEntry:
    name: str
    status: str
    burden: str
    discipline: str


@dataclass(frozen=True)
class RejectedUpgrade:
    name: str
    upgrade: str
    reason: str


@dataclass(frozen=True)
class HandoffEntry:
    name: str
    status: str
    route: str
    caution: str


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
        "REJECTED_ROUTE": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "POLICY_RULE": StatusMark.OBLIGATION,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {"BOUNDARY_COUNTERTERM_REJECTED", "REJECTED_ROUTE", "FORBIDDEN_SHORTCUT"}:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {"BOUNDARY_SCALAR_SILENCE_REQUIRED", "A_SECTOR_MASS_PROTECTION_REQUIRED", "SAFETY_THEOREMS_REQUIRED", "POLICY_RULE"}:
        return GovernanceStatus.POLICY_RULE
    return GovernanceStatus.UNVERIFIED


def obligation_status(status: str) -> ObligationStatus:
    if status in {"PHYSICAL_USE_BLOCKED_PENDING_BOUNDARY_THEOREM", "NOT_INSERTABLE", "DEFERRED_WITH_TARGET", "ACTIVE_O_NECESSITY_NOT_ESTABLISHED"}:
        return ObligationStatus.DEFERRED
    return ObligationStatus.OPEN


def record_marker(ns, marker_id: str, symbol_name: str, scope: str) -> None:
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[],
        output=sp.Symbol(symbol_name),
        method="inventory marker; group status summary, no physical derivation",
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


def record_obligation(ns, obligation_id: str, statement: str, status: str) -> None:
    ns.record_obligation(
        ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=obligation_id,
            status=obligation_status(status),
            required_by=[SCRIPT_ID],
            description=statement,
        )
    )


def emit_line(out: ScriptOutput, label: str, status: str, text: str, *, obligation: bool = False) -> None:
    if obligation:
        with out.unresolved_obligations():
            out.line(label, mark(status), f"{status}: {text}")
    else:
        with out.governance_assessments():
            out.line(label, mark(status), f"{status}: {text}")


def build_status_entries() -> List[StatusEntry]:
    return [
        StatusEntry(
            "G54-1: reduced theorem surface",
            "BOUNDARY_SCALAR_SILENCE_THEOREM_SURFACE_OPENED",
            "Group 54 derived a reduced static-spherical exterior scalar-silence theorem surface",
            "not full covariant boundary theorem",
        ),
        StatusEntry(
            "G54-2: conditional route status",
            "REDUCED_EXTERIOR_SILENCE_SURVIVES_CONDITIONALLY",
            "the reduced exterior silence route survives under zero-offset, zero-charge/flux, and no-shell conditions",
            "not physical use",
        ),
        StatusEntry(
            "G54-3: active O status",
            "ACTIVE_O_NECESSITY_NOT_ESTABLISHED",
            "boundary/scalar-silence route did not force active O",
            "not O construction",
        ),
        StatusEntry(
            "G54-4: candidate status",
            "PHYSICAL_USE_BLOCKED_PENDING_BOUNDARY_THEOREM",
            "candidate remains audit-only and blocked for physical use",
            "not insertable",
        ),
    ]


def build_conditions() -> List[ConditionEntry]:
    return [
        ConditionEntry(
            "C1: exterior scalar form",
            "EXTERIOR_LAPLACE_SILENCE_CONDITION_DERIVED",
            "phi(r)=C0+C1/r solves (r^2 phi')'/r^2=0",
            "homogeneous reduced exterior scalar solution verified",
            "not covariant uniqueness",
        ),
        ConditionEntry(
            "C2: zero-tail condition",
            "ZERO_SCALAR_CHARGE_CONDITION_DERIVED",
            "C0=0 and C1=0 imply phi=0",
            "zero offset plus zero scalar charge kills exterior scalar tail",
            "conditions not automatically derived",
        ),
        ConditionEntry(
            "C3: flux condition",
            "BOUNDARY_FLUX_NEUTRALITY_CONDITION_DERIVED",
            "F_phi=-4*pi*C1",
            "zero scalar flux requires C1=0",
            "not boundary theorem closure",
        ),
        ConditionEntry(
            "C4: no-shell condition",
            "SHELL_SOURCE_ABSENCE_CONDITION_DERIVED",
            "J=R^2*(phi_ext'(R)-phi_int'(R))=0",
            "no boundary shell source requires derivative-jump neutrality",
            "not full junction theorem",
        ),
        ConditionEntry(
            "C5: mass-shift condition",
            "TRACE_MASS_SHIFT_BLOCKED_CONDITIONALLY",
            "Delta_M=alpha*q_zeta and q_zeta=0 implies Delta_M=0",
            "zero scalar charge conditionally blocks trace mass shift",
            "not covariant mass theorem",
        ),
    ]


def build_burdens() -> List[BurdenEntry]:
    return [
        BurdenEntry(
            "B1: zero scalar charge theorem",
            "BOUNDARY_SCALAR_SILENCE_REQUIRED",
            "derive or condition C1=0 / q_zeta=0",
            "avoid exterior scalar tail and scalar flux",
        ),
        BurdenEntry(
            "B2: zero asymptotic offset condition",
            "BOUNDARY_SCALAR_SILENCE_REQUIRED",
            "derive or condition C0=0",
            "avoid constant exterior scalar offset",
        ),
        BurdenEntry(
            "B3: no-shell theorem",
            "BOUNDARY_SCALAR_SILENCE_REQUIRED",
            "derive derivative-jump neutrality J=0 at matching surface",
            "avoid boundary shell source",
        ),
        BurdenEntry(
            "B4: mass neutrality theorem",
            "A_SECTOR_MASS_PROTECTION_REQUIRED",
            "prove trace-sector scalar charge does not shift exterior mass",
            "protect reduced A-sector mass result",
        ),
        BurdenEntry(
            "B5: reduced-to-general gap",
            "SAFETY_THEOREMS_REQUIRED",
            "do not treat reduced static-spherical result as full covariant theorem",
            "preserve scope",
        ),
        BurdenEntry(
            "B6: physical-use block",
            "NOT_INSERTABLE",
            "keep B_s/F_zeta insertion, active O, recombination, and parent closure closed",
            "avoid status inflation",
        ),
    ]


def build_rejected() -> List[RejectedUpgrade]:
    return [
        RejectedUpgrade("R1: boundary counterterm repair", "cancel scalar tail after nonzero flux appears", "repair is not exterior scalar silence"),
        RejectedUpgrade("R2: hidden shell source", "hide derivative jump in boundary term", "shell source must be explicit"),
        RejectedUpgrade("R3: mass patch", "repair trace mass shift by redefining M_ext", "mass neutrality must be derived"),
        RejectedUpgrade("R4: zero charge by fiat", "assume C1=0 or q_zeta=0 without theorem/condition", "zero charge must be supported"),
        RejectedUpgrade("R5: reduced theorem as parent closure", "use reduced exterior silence as full parent-equation readiness", "scope remains reduced"),
    ]


def build_handoffs() -> List[HandoffEntry]:
    return [
        HandoffEntry(
            "H1: boundary theorem strengthening",
            "DEFERRED_WITH_TARGET",
            "attempt to prove zero scalar charge, zero offset, and no-shell matching from theory conditions",
            "do not use boundary counterterms as repair",
        ),
        HandoffEntry(
            "H2: insertion-family exclusion",
            "DEFERRED_WITH_TARGET",
            "begin excluding B_s/F_zeta insertion families that violate residual/source/boundary conditions",
            "do not insert anything yet",
        ),
        HandoffEntry(
            "H3: active-O necessity audit later",
            "ACTIVE_O_NECESSITY_NOT_ESTABLISHED",
            "audit active O only if non-O residual/source/boundary routes fail",
            "do not construct O by anxiety",
        ),
    ]


def record_governance(
    ns,
    entries: List[StatusEntry],
    conditions: List[ConditionEntry],
    burdens: List[BurdenEntry],
    rejected: List[RejectedUpgrade],
    handoffs: List[HandoffEntry],
) -> None:
    record_marker(
        ns,
        MARKER_ID,
        "G54_boundary_scalar_silence_summary",
        "Group 54 reduced boundary/scalar-silence theorem surface summary; no physical insertion",
    )

    for idx, item in enumerate(entries, 1):
        record_claim(ns, f"{MARKER_ID}_entry_{idx}", MARKER_ID, item.status, f"{item.name}: {item.conclusion}. Boundary: {item.boundary}.")
    for idx, item in enumerate(conditions, 1):
        record_claim(ns, f"{MARKER_ID}_condition_{idx}", MARKER_ID, item.status, f"{item.name}: {item.condition}. Meaning: {item.meaning}. Boundary: {item.boundary}.")
    for idx, item in enumerate(burdens, 1):
        record_obligation(ns, f"{MARKER_ID}_burden_{idx}", f"{item.name}: {item.burden}. Discipline: {item.discipline}.", item.status)
    for idx, item in enumerate(rejected, 1):
        record_claim(ns, f"{MARKER_ID}_rejected_{idx}", MARKER_ID, "REJECTED_ROUTE", f"Rejected upgrade: {item.upgrade}. Reason: {item.reason}.")
    for idx, item in enumerate(handoffs, 1):
        record_obligation(ns, f"{MARKER_ID}_handoff_{idx}", f"{item.name}: {item.route}. Caution: {item.caution}.", item.status)


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  What did Group 54 establish about reduced boundary neutrality and exterior scalar silence?\n")
    print("Discipline:\n")
    print("  This summary must preserve reduced scope, conditional theorem status, repair-route rejection,")
    print("  active-O deferral, and blocked physical use.")
    emit_line(out, "Group 54 status summary opened", "PASS", "closing reduced boundary/scalar-silence theorem route without upgrading candidate")


def case_1(out: ScriptOutput) -> None:
    header("Case 1: Group 54 compact result ledger")
    ledger = [
        ("reduced theorem surface", "BOUNDARY_SCALAR_SILENCE_THEOREM_SURFACE_OPENED", "reduced exterior scalar-silence theorem surface derived"),
        ("exterior solution", "EXTERIOR_LAPLACE_SILENCE_CONDITION_DERIVED", "phi=C0+C1/r solves homogeneous radial exterior equation"),
        ("zero-tail condition", "ZERO_SCALAR_CHARGE_CONDITION_DERIVED", "C0=0 and C1=0 imply phi=0"),
        ("flux condition", "BOUNDARY_FLUX_NEUTRALITY_CONDITION_DERIVED", "F_phi=-4*pi*C1, so zero flux requires C1=0"),
        ("shell condition", "SHELL_SOURCE_ABSENCE_CONDITION_DERIVED", "J=0 required for no shell scalar source"),
        ("mass condition", "TRACE_MASS_SHIFT_BLOCKED_CONDITIONALLY", "zero scalar charge blocks diagnostic trace mass shift"),
        ("repair rejection", "BOUNDARY_COUNTERTERM_REJECTED", "boundary counterterm and hidden shell repairs rejected"),
        ("physical use", "NOT_INSERTABLE", "insertion, active O, recombination, and parent closure remain closed"),
    ]
    for label, status, text in ledger:
        emit_line(out, label, status, text)


def case_2(out: ScriptOutput, entries: List[StatusEntry]) -> None:
    header("Case 2: Group 54 status entries")
    for item in entries:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.conclusion}. Boundary: {item.boundary}.")
    emit_line(out, "Group 54 status entries stated", "PASS", f"{len(entries)} status entries stated")


def case_3(out: ScriptOutput, conditions: List[ConditionEntry]) -> None:
    header("Case 3: Reduced theorem-surface conditions")
    for item in conditions:
        subheader(item.name)
        print(f"Condition: {item.condition}")
        print(f"Meaning: {item.meaning}")
        emit_line(out, item.name, item.status, f"{item.meaning}. Boundary: {item.boundary}.")
    emit_line(out, "Group 54 conditions preserved", "PASS", f"{len(conditions)} conditions preserved")


def case_4(out: ScriptOutput, burdens: List[BurdenEntry]) -> None:
    header("Case 4: Open burdens after Group 54")
    for item in burdens:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.burden}. Discipline: {item.discipline}.", obligation=True)
    emit_line(out, "Group 54 burdens preserved", "PASS", f"{len(burdens)} burdens remain explicit", obligation=True)


def case_5(out: ScriptOutput, rejected: List[RejectedUpgrade]) -> None:
    header("Case 5: Rejected boundary-silence upgrades")
    for item in rejected:
        subheader(item.name)
        print(f"Upgrade: {item.upgrade}")
        emit_line(out, item.name, "REJECTED_ROUTE", item.reason)
    emit_line(out, "Group 54 rejected upgrades preserved", "PASS", f"{len(rejected)} upgrade shortcuts rejected")


def case_6(out: ScriptOutput, handoffs: List[HandoffEntry]) -> None:
    header("Case 6: Safe handoffs")
    for item in handoffs:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.route}. Caution: {item.caution}.")
    emit_line(out, "Group 54 handoffs stated", "DEFERRED_WITH_TARGET", f"{len(handoffs)} handoff routes stated without opening physical use")


def case_7(out: ScriptOutput) -> None:
    header("Case 7: Final interpretation")
    conclusions = [
        ("C1: Group 54 result", "REDUCED_EXTERIOR_SILENCE_SURVIVES_CONDITIONALLY", "reduced exterior scalar silence survives conditionally"),
        ("C2: theorem status", "BOUNDARY_SCALAR_SILENCE_REQUIRED", "zero charge, zero offset, and no-shell conditions still need theorem support"),
        ("C3: repair status", "BOUNDARY_COUNTERTERM_REJECTED", "repair routes are rejected"),
        ("C4: active O status", "ACTIVE_O_NECESSITY_NOT_ESTABLISHED", "active O necessity is not established"),
        ("C5: physical-use status", "NOT_INSERTABLE", "B_s/F_zeta insertion, active O, recombination, and parent route remain closed"),
    ]
    for label, status, text in conclusions:
        emit_line(out, label, status, text)

    header("Final summary")
    print("Group 54 status summary result:\n")
    print("  Group 54 derived a reduced static-spherical exterior scalar-silence theorem surface.")
    print("  It did not prove full covariant boundary neutrality.")
    print()
    print("  Reduced conditions:")
    print("    phi(r)=C0+C1/r solves the homogeneous radial exterior equation.")
    print("    C0=0 and C1=0 imply phi=0.")
    print("    F_phi=-4*pi*C1, so zero flux requires C1=0.")
    print("    J=R^2*(phi_ext'(R)-phi_int'(R))=0 is required for no shell scalar source.")
    print("    Delta_M=alpha*q_zeta is blocked conditionally by q_zeta=0.")
    print()
    print("  The reduced exterior silence route survives conditionally.")
    print("  Boundary counterterm repair routes are rejected.")
    print("  Active O necessity is not established.")
    print("  The candidate remains audit-only and blocked for physical use.")
    print()
    print("Still required:")
    print("  zero scalar charge / zero flux theorem")
    print("  zero asymptotic scalar offset condition")
    print("  no-shell / matching neutrality theorem")
    print("  trace-sector mass neutrality theorem")
    print("  reduced-to-general boundary theorem lift")
    print()
    print("Forbidden immediate next step:")
    print("  B_s/F_zeta insertion, active O construction, recombination, or parent closure")


def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    entries = build_status_entries()
    conditions = build_conditions()
    burdens = build_burdens()
    rejected = build_rejected()
    handoffs = build_handoffs()

    case_0(out)
    case_1(out)
    case_2(out, entries)
    case_3(out, conditions)
    case_4(out, burdens)
    case_5(out, rejected)
    case_6(out, handoffs)
    case_7(out)

    record_governance(ns, entries, conditions, burdens, rejected, handoffs)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
