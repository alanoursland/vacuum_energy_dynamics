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
SCRIPT_LABEL = "Candidate Group 55 Status Summary"
MARKER_ID = "g55_summary"

DEPENDENCIES = [
    ("g54_summary", "054_boundary_neutrality_exterior_scalar_silence_theorem_route__candidate_group_54_status_summary", "g54_summary"),
    ("g55_problem", "055_insertion_exclusion_sieve__candidate_insert_problem", "g55_problem"),
    ("g55_direct", "055_insertion_exclusion_sieve__candidate_direct_insert_sieve", "g55_direct"),
    ("g55_trace", "055_insertion_exclusion_sieve__candidate_trace_count_filter", "g55_trace"),
    ("g55_source", "055_insertion_exclusion_sieve__candidate_source_filter", "g55_source"),
    ("g55_boundary", "055_insertion_exclusion_sieve__candidate_boundary_filter", "g55_boundary"),
    ("g55_mass", "055_insertion_exclusion_sieve__candidate_mass_filter", "g55_mass"),
    ("g55_class", "055_insertion_exclusion_sieve__candidate_insert_route_classifier", "g55_class"),
    ("g55_reconcile", "055_insertion_exclusion_sieve__candidate_insert_batch_reconcile", "g55_reconcile"),
]


@dataclass(frozen=True)
class StatusEntry:
    name: str
    status: str
    conclusion: str
    boundary: str


@dataclass(frozen=True)
class FilterEntry:
    name: str
    status: str
    filter_condition: str
    rejected: str
    survivor: str


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
            "G55-1: exclusion surface",
            "INSERTION_EXCLUSION_SURFACE_OPENED",
            "Group 55 filtered insertion families by prior safety conditions",
            "not insertion",
        ),
        StatusEntry(
            "G55-2: unsafe families",
            "REJECTED_ROUTE",
            "direct, source-carrying, boundary-leaking, and mass-shifting insertion routes were rejected",
            "not total candidate no-go",
        ),
        StatusEntry(
            "G55-3: survivor",
            "SILENT_INSERTION_ROUTE_SURVIVES_CONDITIONALLY",
            "only a silent/inert insertion route survives as unproved theorem target",
            "not insertable",
        ),
        StatusEntry(
            "G55-4: physical use",
            "PHYSICAL_USE_BLOCKED",
            "candidate remains audit-only and blocked for physical use",
            "not parent-ready",
        ),
        StatusEntry(
            "G55-5: active O",
            "ACTIVE_O_NECESSITY_NOT_ESTABLISHED",
            "insertion-family filtering does not establish active O necessity",
            "not O construction",
        ),
    ]


def build_filters() -> List[FilterEntry]:
    return [
        FilterEntry(
            "F1: direct load",
            "DIRECT_INSERTION_REJECTED",
            "L=a_T*T_zeta+a_S*S_M+a_C*C1+a_J*J+a_Q*Q_trace",
            "nonzero trace/source/boundary/mass direct load",
            "all direct load coefficients zero, as theorem target only",
        ),
        FilterEntry(
            "F2: trace count",
            "TRACE_COUNT_FILTER_APPLIED",
            "T_zeta*(i_Bs+i_res-1)",
            "double-entry and missing-entry trace routes",
            "B_s route only if i_Bs=1 and i_res=0 with residual nonentry theorem",
        ),
        FilterEntry(
            "F3: source routing",
            "SOURCE_FILTER_APPLIED",
            "S_M*(i_A+i_Bs+i_kappa+i_zeta-1)",
            "B_s/zeta/kappa ordinary-source routes and missing A route",
            "A-sector-only source route with theorem support",
        ),
        FilterEntry(
            "F4: boundary silence",
            "BOUNDARY_FILTER_APPLIED",
            "phi=C0+C1/r, flux=-4*pi*C1, J=0",
            "scalar-tail, nonzero-flux, shell-source, and boundary-repair routes",
            "zero tail, zero flux, and no shell with theorem support",
        ),
        FilterEntry(
            "F5: mass neutrality",
            "MASS_FILTER_APPLIED",
            "Delta_M=alpha*Q_trace",
            "nonzero trace-sector mass-shifting route",
            "Q_trace=0 or inert/non-mass-carrying with theorem support",
        ),
    ]


def build_burdens() -> List[BurdenEntry]:
    return [
        BurdenEntry(
            "B1: insertion law",
            "INSERTION_LAW_REQUIRED",
            "derive a silent/inert insertion law before physical use",
            "avoid ad hoc construction",
        ),
        BurdenEntry(
            "B2: residual nonentry",
            "SAFETY_THEOREMS_REQUIRED",
            "prove residual nonentry for any B_s/F_zeta route",
            "avoid count-once trace violation",
        ),
        BurdenEntry(
            "B3: source no-double-counting",
            "SAFETY_THEOREMS_REQUIRED",
            "prove ordinary source routing remains A-sector-only",
            "avoid source duplication",
        ),
        BurdenEntry(
            "B4: boundary silence",
            "SAFETY_THEOREMS_REQUIRED",
            "prove zero tail, zero flux, and no-shell conditions",
            "avoid exterior scalar leakage",
        ),
        BurdenEntry(
            "B5: mass neutrality",
            "SAFETY_THEOREMS_REQUIRED",
            "prove trace-sector mass charge is zero, inert, or non-mass-carrying",
            "protect A-sector mass",
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
        RejectedUpgrade("R1: summary as insertion", "write the silent survivor as inserted", "no insertion occurred"),
        RejectedUpgrade("R2: filters as proof", "treat filters as proving safety theorems", "filters are necessary conditions"),
        RejectedUpgrade("R3: active O necessity", "jump straight to active O construction", "active O necessity is not established"),
        RejectedUpgrade("R4: total candidate no-go", "reject the retained audit candidate entirely", "bad insertion families die, not necessarily the audit candidate"),
        RejectedUpgrade("R5: parent closure", "open recombination or parent equation from route filtering", "parent route remains closed"),
    ]


def build_handoffs() -> List[HandoffEntry]:
    return [
        HandoffEntry(
            "H1: silent insertion law attempt",
            "DEFERRED_WITH_TARGET",
            "try to define a silent/inert insertion law satisfying all filters",
            "do not insert it without theorem support",
        ),
        HandoffEntry(
            "H2: active-O necessity audit",
            "ACTIVE_O_NECESSITY_NOT_ESTABLISHED",
            "audit active O only if silent non-O insertion route fails or becomes obstructed",
            "do not construct O by anxiety",
        ),
        HandoffEntry(
            "H3: parent divergence obstruction audit",
            "DEFERRED_WITH_TARGET",
            "audit divergence/identity obstruction only after insertion route status is clear",
            "do not open parent equation yet",
        ),
    ]


def record_governance(
    ns,
    entries: List[StatusEntry],
    filters: List[FilterEntry],
    burdens: List[BurdenEntry],
    rejected: List[RejectedUpgrade],
    handoffs: List[HandoffEntry],
) -> None:
    record_marker(
        ns,
        MARKER_ID,
        "G55_insertion_exclusion_summary",
        "Group 55 insertion-family exclusion summary; no physical insertion",
    )

    for idx, item in enumerate(entries, 1):
        record_claim(ns, f"{MARKER_ID}_entry_{idx}", MARKER_ID, item.status, f"{item.name}: {item.conclusion}. Boundary: {item.boundary}.")
    for idx, item in enumerate(filters, 1):
        record_claim(ns, f"{MARKER_ID}_filter_{idx}", MARKER_ID, item.status, f"{item.name}: condition {item.filter_condition}. Rejected: {item.rejected}. Survivor: {item.survivor}.")
    for idx, item in enumerate(burdens, 1):
        record_obligation(ns, f"{MARKER_ID}_burden_{idx}", f"{item.name}: {item.burden}. Discipline: {item.discipline}.", item.status)
    for idx, item in enumerate(rejected, 1):
        record_claim(ns, f"{MARKER_ID}_rejected_{idx}", MARKER_ID, "REJECTED_ROUTE", f"Rejected upgrade: {item.upgrade}. Reason: {item.reason}.")
    for idx, item in enumerate(handoffs, 1):
        record_obligation(ns, f"{MARKER_ID}_handoff_{idx}", f"{item.name}: {item.route}. Caution: {item.caution}.", item.status)


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  What did Group 55 establish about B_s/F_zeta insertion-family exclusion?\n")
    print("Discipline:\n")
    print("  This summary must preserve exclusion-only status, conditional silent-route survival,")
    print("  blocked physical use, and no parent closure.")
    emit_line(out, "Group 55 status summary opened", "PASS", "closing insertion-family exclusion group without inserting candidate")


def case_1(out: ScriptOutput) -> None:
    header("Case 1: Group 55 compact result ledger")
    ledger = [
        ("exclusion surface", "INSERTION_EXCLUSION_SURFACE_OPENED", "Group 55 filtered insertion families by prior safety conditions"),
        ("direct insertion", "DIRECT_INSERTION_REJECTED", "direct trace/source/boundary/mass load routes rejected"),
        ("trace filter", "TRACE_COUNT_FILTER_APPLIED", "double-entry and missing-entry trace routes rejected"),
        ("source filter", "SOURCE_CARRYING_INSERTION_REJECTED", "source-carrying B_s/zeta/kappa routes rejected"),
        ("boundary filter", "BOUNDARY_LEAKING_INSERTION_REJECTED", "scalar-tail, nonzero-flux, shell, and repair routes rejected"),
        ("mass filter", "MASS_SHIFTING_INSERTION_REJECTED", "mass-shifting trace charge routes rejected"),
        ("survivor", "SILENT_INSERTION_ROUTE_SURVIVES_CONDITIONALLY", "only silent/inert insertion route survives conditionally"),
        ("physical use", "PHYSICAL_USE_BLOCKED", "no insertion, active O, recombination, or parent closure opened"),
    ]
    for label, status, text in ledger:
        emit_line(out, label, status, text)


def case_2(out: ScriptOutput, entries: List[StatusEntry]) -> None:
    header("Case 2: Group 55 status entries")
    for item in entries:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.conclusion}. Boundary: {item.boundary}.")
    emit_line(out, "Group 55 status entries stated", "PASS", f"{len(entries)} status entries stated")


def case_3(out: ScriptOutput, filters: List[FilterEntry]) -> None:
    header("Case 3: Insertion-family filters")
    for item in filters:
        subheader(item.name)
        print(f"Filter condition: {item.filter_condition}")
        print(f"Rejected: {item.rejected}")
        print(f"Survivor: {item.survivor}")
        emit_line(out, item.name, item.status, f"Rejected: {item.rejected}. Survivor: {item.survivor}.")
    emit_line(out, "Group 55 filters preserved", "PASS", f"{len(filters)} filters preserved")


def case_4(out: ScriptOutput, burdens: List[BurdenEntry]) -> None:
    header("Case 4: Open burdens after Group 55")
    for item in burdens:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.burden}. Discipline: {item.discipline}.", obligation=True)
    emit_line(out, "Group 55 burdens preserved", "PASS", f"{len(burdens)} burdens remain explicit", obligation=True)


def case_5(out: ScriptOutput, rejected: List[RejectedUpgrade]) -> None:
    header("Case 5: Rejected summary upgrades")
    for item in rejected:
        subheader(item.name)
        print(f"Upgrade: {item.upgrade}")
        emit_line(out, item.name, "REJECTED_ROUTE", item.reason)
    emit_line(out, "Group 55 rejected upgrades preserved", "PASS", f"{len(rejected)} upgrade shortcuts rejected")


def case_6(out: ScriptOutput, handoffs: List[HandoffEntry]) -> None:
    header("Case 6: Safe handoffs")
    for item in handoffs:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.route}. Caution: {item.caution}.")
    emit_line(out, "Group 55 handoffs stated", "DEFERRED_WITH_TARGET", f"{len(handoffs)} handoff routes stated without opening physical use")


def case_7(out: ScriptOutput) -> None:
    header("Case 7: Final interpretation")
    conclusions = [
        ("C1: Group 55 result", "INSERTION_EXCLUSION_SURFACE_OPENED", "unsafe insertion families were excluded"),
        ("C2: survivor status", "SILENT_INSERTION_ROUTE_SURVIVES_CONDITIONALLY", "silent/inert route survives only as unproved theorem target"),
        ("C3: theorem status", "INSERTION_LAW_REQUIRED", "an insertion law and safety theorem support remain required"),
        ("C4: active O status", "ACTIVE_O_NECESSITY_NOT_ESTABLISHED", "active O necessity is not established"),
        ("C5: physical-use status", "NOT_INSERTABLE", "B_s/F_zeta insertion, active O, recombination, and parent route remain closed"),
    ]
    for label, status, text in conclusions:
        emit_line(out, label, status, text)

    header("Final summary")
    print("Group 55 status summary result:\n")
    print("  Group 55 filtered B_s/F_zeta insertion families using trace, source, boundary, and mass safety conditions.")
    print("  Direct physical insertion routes are rejected.")
    print("  Source-carrying, boundary-leaking, and mass-shifting insertion routes are rejected.")
    print()
    print("  Only a silent/inert insertion route survives conditionally.")
    print("  That survivor requires an insertion law plus residual/source/boundary/mass theorem support.")
    print()
    print("Still required:")
    print("  silent/inert insertion law")
    print("  residual nonentry theorem")
    print("  source no-double-counting theorem")
    print("  boundary scalar-silence theorem")
    print("  trace-sector mass neutrality theorem")
    print()
    print("Forbidden immediate next step:")
    print("  B_s/F_zeta insertion, active O construction, recombination, or parent closure")


def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    entries = build_status_entries()
    filters = build_filters()
    burdens = build_burdens()
    rejected = build_rejected()
    handoffs = build_handoffs()

    case_0(out)
    case_1(out)
    case_2(out, entries)
    case_3(out, filters)
    case_4(out, burdens)
    case_5(out, rejected)
    case_6(out, handoffs)
    case_7(out)

    record_governance(ns, entries, filters, burdens, rejected, handoffs)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
