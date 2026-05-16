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
SCRIPT_LABEL = "Candidate Group 53 Status Summary"
MARKER_ID = "g53_summary"

DEPENDENCIES = [
    (
        "g52_summary",
        "52_residual_source_boundary_safety_load_testing__candidate_group_52_status_summary",
        "g52_summary",
    ),
    (
        "g53_problem",
        "53_count_once_trace_residual_source_safety_theorem_route__candidate_residual_source_safety_theorem_problem",
        "g53_problem",
    ),
    (
        "g53_count_once_condition",
        "53_count_once_trace_residual_source_safety_theorem_route__candidate_count_once_trace_condition_formalization",
        "g53_count_once_condition",
    ),
    (
        "g53_residual_non_o",
        "53_count_once_trace_residual_source_safety_theorem_route__candidate_residual_nonentry_non_o_route_audit",
        "g53_residual_non_o",
    ),
    (
        "g53_source_role_purity",
        "53_count_once_trace_residual_source_safety_theorem_route__candidate_source_routing_role_purity_matrix",
        "g53_source_role_purity",
    ),
    (
        "g53_mass_neutrality",
        "53_count_once_trace_residual_source_safety_theorem_route__candidate_a_sector_mass_neutrality_condition_audit",
        "g53_mass_neutrality",
    ),
    (
        "g53_non_o_obstruction",
        "53_count_once_trace_residual_source_safety_theorem_route__candidate_non_o_safety_route_obstruction_classifier",
        "g53_non_o_obstruction",
    ),
    (
        "g53_route_classifier",
        "53_count_once_trace_residual_source_safety_theorem_route__candidate_residual_source_safety_route_classifier",
        "g53_route_classifier",
    ),
    (
        "g53_reconciliation",
        "53_count_once_trace_residual_source_safety_theorem_route__candidate_residual_source_safety_batch_reconciliation",
        "g53_reconciliation",
    ),
]


@dataclass(frozen=True)
class StatusEntry:
    name: str
    topic: str
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
        "COUNT_ONCE_TRACE_THEOREM_SURFACE_OPENED": StatusMark.INFO,
        "COUNT_ONCE_TRACE_CONDITION_FORMALIZED": StatusMark.INFO,
        "RESIDUAL_NONENTRY_ROUTE_DEFINED": StatusMark.INFO,
        "RESIDUAL_ZERO_INCIDENCE_CONDITION": StatusMark.INFO,
        "SOURCE_NO_DOUBLE_COUNTING_ROUTE_DEFINED": StatusMark.INFO,
        "SOURCE_ROLE_PURITY_CONDITION": StatusMark.INFO,
        "A_SECTOR_MASS_PROTECTION_ROUTE_DEFINED": StatusMark.INFO,
        "TRACE_MASS_NEUTRALITY_CONDITION": StatusMark.INFO,
        "NON_O_ROUTE_SURVIVES_CONDITIONALLY": StatusMark.INFO,
        "ACTIVE_O_NECESSITY_NOT_ESTABLISHED": StatusMark.DEFER,
        "THEOREM_TARGET_REFINED": StatusMark.DEFER,
        "CANDIDATE_SURVIVES_AS_AUDIT_ONLY": StatusMark.INFO,
        "CANDIDATE_BLOCKED_FOR_PHYSICAL_USE": StatusMark.DEFER,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "NOT_INSERTABLE": StatusMark.DEFER,
        "RESIDUAL_NONENTRY_THEOREM_REQUIRED": StatusMark.OBLIGATION,
        "SOURCE_NO_DOUBLE_COUNTING_REQUIRED": StatusMark.OBLIGATION,
        "A_SECTOR_MASS_PROTECTION_REQUIRED": StatusMark.OBLIGATION,
        "SAFETY_THEOREMS_REQUIRED": StatusMark.OBLIGATION,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "TRACE_DOUBLE_ENTRY_REJECTED": StatusMark.FAIL,
        "TRACE_MISSING_ENTRY_REJECTED": StatusMark.FAIL,
        "OBSTRUCTION_WITNESS_FOUND": StatusMark.FAIL,
        "REJECTED_ROUTE": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {
        "TRACE_DOUBLE_ENTRY_REJECTED",
        "TRACE_MISSING_ENTRY_REJECTED",
        "OBSTRUCTION_WITNESS_FOUND",
        "REJECTED_ROUTE",
        "FORBIDDEN_SHORTCUT",
    }:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {
        "RESIDUAL_NONENTRY_THEOREM_REQUIRED",
        "SOURCE_NO_DOUBLE_COUNTING_REQUIRED",
        "A_SECTOR_MASS_PROTECTION_REQUIRED",
        "SAFETY_THEOREMS_REQUIRED",
        "POLICY_RULE",
    }:
        return GovernanceStatus.POLICY_RULE
    return GovernanceStatus.UNVERIFIED


def obligation_status(status: str) -> ObligationStatus:
    if status in {
        "CANDIDATE_BLOCKED_FOR_PHYSICAL_USE",
        "DEFERRED_WITH_TARGET",
        "NOT_INSERTABLE",
        "ACTIVE_O_NECESSITY_NOT_ESTABLISHED",
        "THEOREM_TARGET_REFINED",
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
            name="G53-1: theorem-route scope",
            topic="non-O residual/source safety route",
            status="COUNT_ONCE_TRACE_THEOREM_SURFACE_OPENED",
            conclusion="Group 53 sharpened the non-O residual/source theorem route",
            boundary="not safety proof",
        ),
        StatusEntry(
            name="G53-2: non-O route status",
            topic="active O necessity",
            status="NON_O_ROUTE_SURVIVES_CONDITIONALLY",
            conclusion="the non-O route can be stated as a conditional theorem target",
            boundary="not physical use",
        ),
        StatusEntry(
            name="G53-3: active O status",
            topic="projector necessity",
            status="ACTIVE_O_NECESSITY_NOT_ESTABLISHED",
            conclusion="no actual obstruction currently forces active O",
            boundary="not O construction",
        ),
        StatusEntry(
            name="G53-4: candidate status",
            topic="retained trace-normalization candidate",
            status="CANDIDATE_BLOCKED_FOR_PHYSICAL_USE",
            conclusion="candidate remains audit-only and blocked for physical use",
            boundary="not insertable",
        ),
    ]


def build_conditions() -> List[ConditionEntry]:
    return [
        ConditionEntry(
            name="C1: count-once trace",
            status="COUNT_ONCE_TRACE_CONDITION_FORMALIZED",
            condition="i_Bs + i_res = 1",
            meaning="trace must enter exactly one incidence channel",
            boundary="not dynamics or insertion",
        ),
        ConditionEntry(
            name="C2: B_s clean incidence route",
            status="RESIDUAL_NONENTRY_THEOREM_REQUIRED",
            condition="i_Bs=1 and i_res=0",
            meaning="B_s/F_zeta trace route is clean only if residual nonentry is proven",
            boundary="not proven",
        ),
        ConditionEntry(
            name="C3: residual nonentry",
            status="RESIDUAL_ZERO_INCIDENCE_CONDITION",
            condition="i_res_metric=0 and i_res_source=0",
            meaning="residual metric/source incidence must vanish",
            boundary="not by declaration",
        ),
        ConditionEntry(
            name="C4: A-sector-only source routing",
            status="SOURCE_ROLE_PURITY_CONDITION",
            condition="i_A=1, i_Bs=0, i_zeta=0, i_kappa=0",
            meaning="ordinary source load must remain A-sector-only",
            boundary="not source theorem closure",
        ),
        ConditionEntry(
            name="C5: trace mass neutrality",
            status="TRACE_MASS_NEUTRALITY_CONDITION",
            condition="Q_trace=0 or Q_trace proven inert/non-mass-carrying",
            meaning="trace-sector charge must not shift protected mass",
            boundary="not mass theorem closure",
        ),
    ]


def build_burdens() -> List[BurdenEntry]:
    return [
        BurdenEntry(
            name="B1: residual nonentry theorem",
            status="RESIDUAL_NONENTRY_THEOREM_REQUIRED",
            burden="prove residual zeta/kappa has zero metric/source incidence under the retained candidate",
            discipline="avoid residual reentry and count-once violation",
        ),
        BurdenEntry(
            name="B2: source role-purity theorem",
            status="SOURCE_NO_DOUBLE_COUNTING_REQUIRED",
            burden="prove ordinary source routing is A-sector-only",
            discipline="avoid hidden source duplication",
        ),
        BurdenEntry(
            name="B3: trace-sector mass neutrality theorem",
            status="A_SECTOR_MASS_PROTECTION_REQUIRED",
            burden="prove Q_trace is zero, inert, compactly supported, or non-mass-carrying",
            discipline="protect the reduced A-sector mass coin",
        ),
        BurdenEntry(
            name="B4: boundary/scalar silence remains separate",
            status="DEFERRED_WITH_TARGET",
            burden="boundary neutrality and exterior scalar silence remain unresolved outside this group",
            discipline="do not pretend residual/source safety solves boundary tails",
        ),
        BurdenEntry(
            name="B5: physical-use block",
            status="NOT_INSERTABLE",
            burden="keep B_s/F_zeta insertion, active O, recombination, and parent closure closed",
            discipline="avoid status inflation",
        ),
    ]


def build_rejected() -> List[RejectedUpgrade]:
    return [
        RejectedUpgrade(
            name="R1: summary as safety proof",
            upgrade="write Group 53 as if residual/source safety were proven",
            reason="Group 53 only sharpened theorem targets",
        ),
        RejectedUpgrade(
            name="R2: conditional route as insertion",
            upgrade="insert B_s/F_zeta because the non-O route survives conditionally",
            reason="physical use remains blocked",
        ),
        RejectedUpgrade(
            name="R3: active O necessity",
            upgrade="declare active O necessary immediately",
            reason="non-O route has not failed by obstruction",
        ),
        RejectedUpgrade(
            name="R4: zero incidence by fiat",
            upgrade="assume residual/source zero-incidence and Q_trace neutrality",
            reason="conditions require proof or explicit postulate status",
        ),
        RejectedUpgrade(
            name="R5: branch choice",
            upgrade="choose metric or scale trace-normalization branch",
            reason="branch choice remains separate",
        ),
    ]


def build_handoffs() -> List[HandoffEntry]:
    return [
        HandoffEntry(
            name="H1: focused residual/source theorem attempt",
            status="DEFERRED_WITH_TARGET",
            route="attempt to prove the non-O residual/source conditions",
            caution="do not turn theorem targets into insertion permission",
        ),
        HandoffEntry(
            name="H2: boundary/scalar-silence route",
            status="DEFERRED_WITH_TARGET",
            route="move to boundary neutrality and exterior scalar silence theorem work",
            caution="residual/source route does not solve scalar tails",
        ),
        HandoffEntry(
            name="H3: active-O necessity audit later",
            status="ACTIVE_O_NECESSITY_NOT_ESTABLISHED",
            route="audit O necessity only if non-O theorem routes fail or become obstructed",
            caution="do not construct O by anxiety",
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
        "G53_residual_source_safety_route_summary",
        "Group 53 residual/source safety theorem-route summary; no physical insertion",
    )

    for idx, item in enumerate(entries, start=1):
        record_claim(ns, f"{MARKER_ID}_entry_{idx}", MARKER_ID, item.status, f"{item.name}: {item.conclusion}. Boundary: {item.boundary}.")

    for idx, item in enumerate(conditions, start=1):
        record_claim(ns, f"{MARKER_ID}_condition_{idx}", MARKER_ID, item.status, f"{item.name}: {item.condition}. Meaning: {item.meaning}. Boundary: {item.boundary}.")

    for idx, item in enumerate(burdens, start=1):
        record_obligation(ns, f"{MARKER_ID}_burden_{idx}", f"{item.name}: {item.burden}. Discipline: {item.discipline}.", item.status)

    for idx, item in enumerate(rejected, start=1):
        record_claim(ns, f"{MARKER_ID}_rejected_{idx}", MARKER_ID, "REJECTED_ROUTE", f"Rejected upgrade: {item.upgrade}. Reason: {item.reason}.")

    for idx, item in enumerate(handoffs, start=1):
        record_obligation(ns, f"{MARKER_ID}_handoff_{idx}", f"{item.name}: {item.route}. Caution: {item.caution}.", item.status)


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  What did Group 53 establish about the non-O residual/source safety theorem route?\n")
    print("Discipline:\n")
    print("  This script summarizes Group 53. It must preserve the difference between")
    print("  conditional theorem targets, actual safety proof, active-O necessity, and physical-use permission.")
    emit_line(out, "Group 53 status summary opened", "PASS", "closing residual/source theorem-route batch without upgrading candidate")


def case_1(out: ScriptOutput) -> None:
    header("Case 1: Group 53 compact result ledger")
    ledger = [
        ("non-O route", "NON_O_ROUTE_SURVIVES_CONDITIONALLY", "non-O residual/source route survives only as unproved theorem target"),
        ("count-once condition", "COUNT_ONCE_TRACE_CONDITION_FORMALIZED", "i_Bs+i_res=1 formalized; double-entry and missing-entry rejected"),
        ("residual condition", "RESIDUAL_NONENTRY_THEOREM_REQUIRED", "residual metric/source zero-incidence remains required"),
        ("source condition", "SOURCE_NO_DOUBLE_COUNTING_REQUIRED", "ordinary source routing must remain A-sector-only"),
        ("mass condition", "A_SECTOR_MASS_PROTECTION_REQUIRED", "Q_trace must be zero, inert, or non-mass-carrying"),
        ("active O", "ACTIVE_O_NECESSITY_NOT_ESTABLISHED", "active O necessity is not established"),
        ("physical use", "NOT_INSERTABLE", "B_s/F_zeta insertion, recombination, and parent closure remain closed"),
    ]
    for label, status, text in ledger:
        emit_line(out, label, status, text)


def case_2(out: ScriptOutput, entries: List[StatusEntry]) -> None:
    header("Case 2: Group 53 status entries")
    for entry in entries:
        subheader(entry.name)
        print(f"Topic: {entry.topic}")
        emit_line(out, entry.name, entry.status, f"{entry.conclusion}. Boundary: {entry.boundary}.")
    emit_line(out, "Group 53 status entries stated", "PASS", f"{len(entries)} status entries stated")


def case_3(out: ScriptOutput, conditions: List[ConditionEntry]) -> None:
    header("Case 3: Conditional theorem-target conditions")
    for item in conditions:
        subheader(item.name)
        print(f"Condition: {item.condition}")
        print(f"Meaning: {item.meaning}")
        emit_line(out, item.name, item.status, f"{item.meaning}. Boundary: {item.boundary}.")
    emit_line(out, "Group 53 conditions preserved", "PASS", f"{len(conditions)} conditions preserved")


def case_4(out: ScriptOutput, burdens: List[BurdenEntry]) -> None:
    header("Case 4: Open burdens after Group 53")
    for item in burdens:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.burden}. Discipline: {item.discipline}.", obligation=True)
    emit_line(out, "Group 53 burdens preserved", "PASS", f"{len(burdens)} burdens remain explicit", obligation=True)


def case_5(out: ScriptOutput, rejected: List[RejectedUpgrade]) -> None:
    header("Case 5: Rejected summary upgrades")
    for item in rejected:
        subheader(item.name)
        print(f"Upgrade: {item.upgrade}")
        emit_line(out, item.name, "REJECTED_ROUTE", item.reason)
    emit_line(out, "Group 53 rejected upgrades preserved", "PASS", f"{len(rejected)} upgrade shortcuts rejected")


def case_6(out: ScriptOutput, handoffs: List[HandoffEntry]) -> None:
    header("Case 6: Safe handoffs")
    for item in handoffs:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.route}. Caution: {item.caution}.")
    emit_line(out, "Group 53 handoffs stated", "DEFERRED_WITH_TARGET", f"{len(handoffs)} handoff routes stated without opening physical use")


def case_7(out: ScriptOutput) -> None:
    header("Case 7: Final interpretation")
    conclusions = [
        ("C1: Group 53 result", "NON_O_ROUTE_SURVIVES_CONDITIONALLY", "non-O residual/source route survives only as an unproved theorem target"),
        ("C2: candidate status", "CANDIDATE_BLOCKED_FOR_PHYSICAL_USE", "candidate remains audit-only and blocked for physical use"),
        ("C3: active O status", "ACTIVE_O_NECESSITY_NOT_ESTABLISHED", "active O necessity is not established"),
        ("C4: theorem status", "SAFETY_THEOREMS_REQUIRED", "residual/source safety burdens are sharpened but not closed"),
        ("C5: physical-use status", "NOT_INSERTABLE", "B_s/F_zeta insertion, active O, recombination, and parent route remain closed"),
    ]
    for label, status, text in conclusions:
        emit_line(out, label, status, text)

    header("Final summary")
    print("Group 53 status summary result:\n")
    print("  Group 53 sharpened the non-O residual/source safety theorem route.")
    print("  It did not prove residual/source safety.")
    print()
    print("  Conditional theorem-target conditions:")
    print("    count-once trace: i_Bs + i_res = 1")
    print("    B_s clean route: i_Bs=1 and i_res=0, requiring residual nonentry proof")
    print("    residual nonentry: i_res_metric=0 and i_res_source=0")
    print("    source role-purity: i_A=1, i_Bs=0, i_zeta=0, i_kappa=0")
    print("    mass neutrality: Q_trace=0 or Q_trace proven inert/non-mass-carrying")
    print()
    print("  The non-O route conditionally survives as a theorem target.")
    print("  Active O necessity is not established.")
    print("  The candidate remains audit-only and blocked for physical use.")
    print()
    print("Still required:")
    print("  residual nonentry theorem")
    print("  source no-double-counting theorem")
    print("  A-sector mass protection / trace mass neutrality theorem")
    print("  boundary neutrality and exterior scalar silence remain separate")
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
