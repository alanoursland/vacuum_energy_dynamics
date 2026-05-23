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
SCRIPT_LABEL = "Candidate Group 56 Status Summary"
MARKER_ID = "g56_summary"

DEPENDENCIES = [
    ("g55_summary", "055_insertion_exclusion_sieve__candidate_group_55_status_summary", "g55_summary"),
    ("g56_problem", "056_silent_insert_law__candidate_silent_problem", "g56_problem"),
    ("g56_w", "056_silent_insert_law__candidate_boundary_null_profile", "g56_w"),
    ("g56_q", "056_silent_insert_law__candidate_charge_neutral_source", "g56_q"),
    ("g56_tail", "056_silent_insert_law__candidate_exterior_tail_zero", "g56_tail"),
    ("g56_shell", "056_silent_insert_law__candidate_shell_neutral_match", "g56_shell"),
    ("g56_div", "056_silent_insert_law__candidate_divergence_silent_stress", "g56_div"),
    ("g56_class", "056_silent_insert_law__candidate_silent_route_classifier", "g56_class"),
    ("g56_reconcile", "056_silent_insert_law__candidate_silent_batch_reconcile", "g56_reconcile"),
]


@dataclass(frozen=True)
class StatusEntry:
    name: str
    status: str
    conclusion: str
    boundary: str


@dataclass(frozen=True)
class ConstructiveEntry:
    name: str
    status: str
    result: str
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
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {"REJECTED_ROUTE", "FORBIDDEN_SHORTCUT"}:
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
            "G56-1: constructive surface",
            "SILENT_LAW_SURFACE_OPENED",
            "Group 56 constructed a reduced silent/inert insertion-law theorem surface",
            "not physical insertion",
        ),
        StatusEntry(
            "G56-2: route status",
            "SILENT_INSERTION_ROUTE_SURVIVES_CONDITIONALLY",
            "the silent/inert route survives conditionally with explicit reduced profiles and closures",
            "not insertable",
        ),
        StatusEntry(
            "G56-3: physical use",
            "PHYSICAL_USE_BLOCKED",
            "candidate remains audit-only and blocked for physical use",
            "not parent-ready",
        ),
        StatusEntry(
            "G56-4: active O",
            "ACTIVE_O_NECESSITY_NOT_ESTABLISHED",
            "Group 56 does not establish active O necessity",
            "not O construction",
        ),
    ]


def build_constructive_entries() -> List[ConstructiveEntry]:
    return [
        ConstructiveEntry(
            "C1: boundary-null profile",
            "BOUNDARY_NULL_PROFILE_DERIVED",
            "W(r)=r^2*(R-r)^2 with W(R)=0 and W'(R)=0",
            "nontrivial reduced profile can be boundary-null",
            "not insertion law",
        ),
        ConstructiveEntry(
            "C2: charge-neutral profile",
            "CHARGE_NEUTRAL_PROFILE_DERIVED",
            "rho(r)=rho0*(1-5*r^2/(3R^2)) with integral_0^R r^2*rho dr=0",
            "nontrivial internal profile can carry zero net scalar charge",
            "not source theorem",
        ),
        ConstructiveEntry(
            "C3: exterior tail silence",
            "EXTERIOR_TAIL_ZERO_CONDITION_DERIVED",
            "phi_ext=C0+kQ/r and C0=0,Q=0 imply phi_ext=0",
            "charge neutrality plus zero offset kills reduced exterior tail",
            "not full boundary theorem",
        ),
        ConstructiveEntry(
            "C4: shell-neutral match",
            "SHELL_NEUTRAL_CONDITION_DERIVED",
            "phi_int=A*r^2*(R-r)^2 matched to exterior zero gives J=0",
            "boundary-null profile avoids reduced shell jump",
            "not full junction theorem",
        ),
        ConstructiveEntry(
            "C5: divergence-silent closure",
            "DIVERGENCE_SILENT_CLOSURE_DERIVED",
            "p_t=p_r+r*p_r'/2 gives D=p_r'+2(p_r-p_t)/r=0",
            "reduced anisotropic closure can be divergence-silent",
            "not covariant Bianchi proof",
        ),
    ]


def build_burdens() -> List[BurdenEntry]:
    return [
        BurdenEntry(
            "B1: covariant lift",
            "COVARIANT_LIFT_REQUIRED",
            "lift boundary-null, charge-neutral, shell-neutral, and divergence-silent conditions beyond reduced radial model",
            "avoid reduced overclaim",
        ),
        BurdenEntry(
            "B2: insertion law",
            "INSERTION_LAW_REQUIRED",
            "derive an actual silent/inert insertion law if continuing",
            "avoid ad hoc profile use",
        ),
        BurdenEntry(
            "B3: source safety",
            "SAFETY_THEOREMS_REQUIRED",
            "prove internal silent profile does not duplicate ordinary source load",
            "protect A-sector source routing",
        ),
        BurdenEntry(
            "B4: boundary and mass safety",
            "SAFETY_THEOREMS_REQUIRED",
            "prove zero charge, zero offset, no-shell matching, and mass neutrality in the actual theory",
            "avoid exterior leakage and mass shift",
        ),
        BurdenEntry(
            "B5: divergence identity",
            "COVARIANT_LIFT_REQUIRED",
            "lift reduced D=0 closure to covariant divergence compatibility",
            "avoid parent-identity overclaim",
        ),
        BurdenEntry(
            "B6: physical-use block",
            "NOT_INSERTABLE",
            "keep insertion, active O, recombination, and parent closure closed",
            "avoid status inflation",
        ),
    ]


def build_rejected() -> List[RejectedUpgrade]:
    return [
        RejectedUpgrade("R1: reduced surface as insertion", "treat reduced silent route as field-equation insertion", "no insertion occurred"),
        RejectedUpgrade("R2: reduced surface as covariant theorem", "treat reduced construction as full covariant theorem", "covariant lift remains required"),
        RejectedUpgrade("R3: divergence as parent closure", "use reduced D=0 as Bianchi or parent-equation proof", "not a parent identity"),
        RejectedUpgrade("R4: profile as ordinary matter source", "treat internal silent profile as matter source", "source no-double-counting remains required"),
        RejectedUpgrade("R5: active O finality", "declare active O unnecessary forever", "only current necessity is unestablished"),
    ]


def build_handoffs() -> List[HandoffEntry]:
    return [
        HandoffEntry(
            "H1: covariant lift audit",
            "DEFERRED_WITH_TARGET",
            "test whether the reduced silent/inert construction can be lifted to a covariant/geometric form",
            "do not treat reduced model as already lifted",
        ),
        HandoffEntry(
            "H2: insertion law attempt",
            "DEFERRED_WITH_TARGET",
            "derive a real silent/inert insertion law using the reduced route as a guide",
            "do not insert without safety proof",
        ),
        HandoffEntry(
            "H3: divergence/parent obstruction audit",
            "DEFERRED_WITH_TARGET",
            "audit whether the reduced divergence-silent closure can satisfy the needed parent identity conditions",
            "do not open parent equation yet",
        ),
    ]


def record_governance(
    ns,
    entries: List[StatusEntry],
    constructive: List[ConstructiveEntry],
    burdens: List[BurdenEntry],
    rejected: List[RejectedUpgrade],
    handoffs: List[HandoffEntry],
) -> None:
    record_marker(
        ns,
        MARKER_ID,
        "G56_silent_insert_summary",
        "Group 56 reduced silent/inert insertion-law theorem surface summary; no physical insertion",
    )

    for idx, item in enumerate(entries, 1):
        record_claim(ns, f"{MARKER_ID}_entry_{idx}", MARKER_ID, item.status, f"{item.name}: {item.conclusion}. Boundary: {item.boundary}.")
    for idx, item in enumerate(constructive, 1):
        record_claim(ns, f"{MARKER_ID}_construct_{idx}", MARKER_ID, item.status, f"{item.name}: {item.result}. Meaning: {item.meaning}. Boundary: {item.boundary}.")
    for idx, item in enumerate(burdens, 1):
        record_obligation(ns, f"{MARKER_ID}_burden_{idx}", f"{item.name}: {item.burden}. Discipline: {item.discipline}.", item.status)
    for idx, item in enumerate(rejected, 1):
        record_claim(ns, f"{MARKER_ID}_rejected_{idx}", MARKER_ID, "REJECTED_ROUTE", f"Rejected upgrade: {item.upgrade}. Reason: {item.reason}.")
    for idx, item in enumerate(handoffs, 1):
        record_obligation(ns, f"{MARKER_ID}_handoff_{idx}", f"{item.name}: {item.route}. Caution: {item.caution}.", item.status)


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  What did Group 56 establish about a reduced silent/inert insertion-law surface?\n")
    print("Discipline:\n")
    print("  This summary must preserve constructive reduced progress, covariant-lift burden,")
    print("  blocked physical use, and no parent closure.")
    emit_line(out, "Group 56 status summary opened", "PASS", "closing reduced silent/inert insertion-law theorem-surface group without insertion")


def case_1(out: ScriptOutput) -> None:
    header("Case 1: Group 56 compact result ledger")
    ledger = [
        ("constructive surface", "SILENT_LAW_SURFACE_OPENED", "reduced silent/inert theorem surface constructed"),
        ("boundary-null profile", "BOUNDARY_NULL_PROFILE_DERIVED", "W=r^2*(R-r)^2 gives W(R)=W'(R)=0"),
        ("charge-neutral profile", "CHARGE_NEUTRAL_PROFILE_DERIVED", "nontrivial rho profile has zero net scalar charge"),
        ("exterior tail", "EXTERIOR_TAIL_ZERO_CONDITION_DERIVED", "C0=0 and Q=0 imply phi_ext=0"),
        ("shell matching", "SHELL_NEUTRAL_CONDITION_DERIVED", "boundary-null match to exterior zero gives J=0"),
        ("divergence closure", "DIVERGENCE_SILENT_CLOSURE_DERIVED", "reduced anisotropic closure gives D=0"),
        ("route status", "SILENT_INSERTION_ROUTE_SURVIVES_CONDITIONALLY", "silent route survives as reduced theorem target"),
        ("physical use", "PHYSICAL_USE_BLOCKED", "no insertion, active O, recombination, or parent closure opened"),
    ]
    for label, status, text in ledger:
        emit_line(out, label, status, text)


def case_2(out: ScriptOutput, entries: List[StatusEntry]) -> None:
    header("Case 2: Group 56 status entries")
    for item in entries:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.conclusion}. Boundary: {item.boundary}.")
    emit_line(out, "Group 56 status entries stated", "PASS", f"{len(entries)} status entries stated")


def case_3(out: ScriptOutput, constructive: List[ConstructiveEntry]) -> None:
    header("Case 3: Constructive reduced results")
    for item in constructive:
        subheader(item.name)
        print(f"Result: {item.result}")
        print(f"Meaning: {item.meaning}")
        emit_line(out, item.name, item.status, f"{item.meaning}. Boundary: {item.boundary}.")
    emit_line(out, "Group 56 constructive results preserved", "PASS", f"{len(constructive)} constructive results preserved")


def case_4(out: ScriptOutput, burdens: List[BurdenEntry]) -> None:
    header("Case 4: Open burdens after Group 56")
    for item in burdens:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.burden}. Discipline: {item.discipline}.", obligation=True)
    emit_line(out, "Group 56 burdens preserved", "PASS", f"{len(burdens)} burdens remain explicit", obligation=True)


def case_5(out: ScriptOutput, rejected: List[RejectedUpgrade]) -> None:
    header("Case 5: Rejected summary upgrades")
    for item in rejected:
        subheader(item.name)
        print(f"Upgrade: {item.upgrade}")
        emit_line(out, item.name, "REJECTED_ROUTE", item.reason)
    emit_line(out, "Group 56 rejected upgrades preserved", "PASS", f"{len(rejected)} upgrade shortcuts rejected")


def case_6(out: ScriptOutput, handoffs: List[HandoffEntry]) -> None:
    header("Case 6: Safe handoffs")
    for item in handoffs:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.route}. Caution: {item.caution}.")
    emit_line(out, "Group 56 handoffs stated", "DEFERRED_WITH_TARGET", f"{len(handoffs)} handoff routes stated without opening physical use")


def case_7(out: ScriptOutput) -> None:
    header("Case 7: Final interpretation")
    conclusions = [
        ("C1: Group 56 result", "SILENT_INSERTION_ROUTE_SURVIVES_CONDITIONALLY", "reduced silent/inert route survives conditionally with concrete profiles and closure"),
        ("C2: constructive progress", "SILENT_LAW_SURFACE_OPENED", "route is now a reduced theorem surface, not just a surviving label"),
        ("C3: theorem gap", "COVARIANT_LIFT_REQUIRED", "covariant lift and actual insertion law remain required"),
        ("C4: physical-use status", "NOT_INSERTABLE", "B_s/F_zeta insertion, active O, recombination, and parent route remain closed"),
    ]
    for label, status, text in conclusions:
        emit_line(out, label, status, text)

    header("Final summary")
    print("Group 56 status summary result:\n")
    print("  Group 56 constructed a reduced silent/inert insertion-law theorem surface.")
    print("  It did not insert B_s/F_zeta.")
    print()
    print("  Constructive reduced results:")
    print("    W(r)=r^2*(R-r)^2 with W(R)=0 and W'(R)=0.")
    print("    rho(r)=rho0*(1-5*r^2/(3R^2)) with integral r^2*rho dr = 0.")
    print("    phi_ext=C0+kQ/r, so C0=0 and Q=0 imply phi_ext=0.")
    print("    phi_int=A*r^2*(R-r)^2 matched to exterior zero gives J=0.")
    print("    p_t=p_r+r*p_r'/2 gives reduced D=p_r'+2(p_r-p_t)/r=0.")
    print()
    print("  The silent/inert route survives conditionally as a reduced theorem target.")
    print("  It still requires covariant lift, actual insertion law, source safety, boundary/mass safety, and divergence identity support.")
    print()
    print("Forbidden immediate next step:")
    print("  B_s/F_zeta insertion, active O construction, recombination, or parent closure")


def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    entries = build_status_entries()
    constructive = build_constructive_entries()
    burdens = build_burdens()
    rejected = build_rejected()
    handoffs = build_handoffs()

    case_0(out)
    case_1(out)
    case_2(out, entries)
    case_3(out, constructive)
    case_4(out, burdens)
    case_5(out, rejected)
    case_6(out, handoffs)
    case_7(out)

    record_governance(ns, entries, constructive, burdens, rejected, handoffs)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
