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
SCRIPT_LABEL = "Candidate Group 52 Status Summary"
MARKER_ID = "g52_summary"

DEPENDENCIES = [
    (
        "g51_summary",
        "051_trace_normalization_adopt_defer_reject_decision_surface__candidate_group_51_status_summary",
        "g51_summary",
    ),
    (
        "g52_problem",
        "052_residual_source_boundary_safety_load_testing__candidate_safety_load_test_problem",
        "g52_problem",
    ),
    (
        "g52_count_once_trace",
        "052_residual_source_boundary_safety_load_testing__candidate_count_once_trace_incidence_audit",
        "g52_count_once_trace",
    ),
    (
        "g52_residual_nonentry",
        "052_residual_source_boundary_safety_load_testing__candidate_residual_nonentry_obstruction_sieve",
        "g52_residual_nonentry",
    ),
    (
        "g52_source_matrix",
        "052_residual_source_boundary_safety_load_testing__candidate_source_no_double_counting_matrix",
        "g52_source_matrix",
    ),
    (
        "g52_a_mass_protection",
        "052_residual_source_boundary_safety_load_testing__candidate_a_sector_mass_protection_audit",
        "g52_a_mass_protection",
    ),
    (
        "g52_boundary_silence",
        "052_residual_source_boundary_safety_load_testing__candidate_boundary_scalar_silence_dependency_audit",
        "g52_boundary_silence",
    ),
    (
        "g52_safety_classifier",
        "052_residual_source_boundary_safety_load_testing__candidate_safety_load_route_classifier",
        "g52_safety_classifier",
    ),
    (
        "g52_safety_reconciliation",
        "052_residual_source_boundary_safety_load_testing__candidate_residual_source_boundary_safety_batch_reconciliation",
        "g52_safety_reconciliation",
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
class WitnessEntry:
    name: str
    status: str
    witness: str
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
        "SAFETY_LOAD_TEST_SURFACE_OPENED": StatusMark.INFO,
        "TRACE_INCIDENCE_DIAGNOSTIC": StatusMark.INFO,
        "COUNT_ONCE_TRACE_BURDEN_EXPLICIT": StatusMark.OBLIGATION,
        "RESIDUAL_NONENTRY_THEOREM_REQUIRED": StatusMark.OBLIGATION,
        "SOURCE_NO_DOUBLE_COUNTING_REQUIRED": StatusMark.OBLIGATION,
        "A_SECTOR_MASS_PROTECTION_REQUIRED": StatusMark.OBLIGATION,
        "BOUNDARY_SCALAR_SILENCE_REQUIRED": StatusMark.OBLIGATION,
        "SAFETY_THEOREMS_REQUIRED": StatusMark.OBLIGATION,
        "A_SECTOR_MASS_COIN_PROTECTED": StatusMark.INFO,
        "CANDIDATE_SURVIVES_AS_AUDIT_ONLY": StatusMark.INFO,
        "CANDIDATE_BLOCKED_FOR_PHYSICAL_USE": StatusMark.DEFER,
        "THEOREM_TARGET_REFINED": StatusMark.DEFER,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "NOT_INSERTABLE": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "OBSTRUCTION_WITNESS_FOUND": StatusMark.FAIL,
        "SOURCE_DUPLICATION_WITNESS": StatusMark.FAIL,
        "SCALAR_TAIL_WITNESS": StatusMark.FAIL,
        "RESIDUAL_ENTRY_REJECTED": StatusMark.FAIL,
        "REJECTED_ROUTE": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "OPEN": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {
        "OBSTRUCTION_WITNESS_FOUND",
        "SOURCE_DUPLICATION_WITNESS",
        "SCALAR_TAIL_WITNESS",
        "RESIDUAL_ENTRY_REJECTED",
        "REJECTED_ROUTE",
        "FORBIDDEN_SHORTCUT",
    }:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {
        "COUNT_ONCE_TRACE_BURDEN_EXPLICIT",
        "RESIDUAL_NONENTRY_THEOREM_REQUIRED",
        "SOURCE_NO_DOUBLE_COUNTING_REQUIRED",
        "A_SECTOR_MASS_PROTECTION_REQUIRED",
        "BOUNDARY_SCALAR_SILENCE_REQUIRED",
        "SAFETY_THEOREMS_REQUIRED",
        "POLICY_RULE",
    }:
        return GovernanceStatus.POLICY_RULE
    return GovernanceStatus.UNVERIFIED


def obligation_status(status: str) -> ObligationStatus:
    if status in {
        "CANDIDATE_BLOCKED_FOR_PHYSICAL_USE",
        "THEOREM_TARGET_REFINED",
        "DEFERRED_WITH_TARGET",
        "NOT_INSERTABLE",
        "NOT_ADOPTED",
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
            name="G52-1: safety load-test scope",
            topic="retained conditional trace-normalization candidate",
            status="SAFETY_LOAD_TEST_SURFACE_OPENED",
            conclusion="Group 52 performed first residual/source/boundary safety load testing",
            boundary="not insertion, adoption, active O, recombination, or parent closure",
        ),
        StatusEntry(
            name="G52-2: candidate status",
            topic="conditional trace candidate after load testing",
            status="CANDIDATE_SURVIVES_AS_AUDIT_ONLY",
            conclusion="the conditional candidate remains useful only as audit material",
            boundary="not physical use",
        ),
        StatusEntry(
            name="G52-3: count-once trace status",
            topic="trace incidence diagnostic",
            status="COUNT_ONCE_TRACE_BURDEN_EXPLICIT",
            conclusion="double entry through B_s/F_zeta and residual trace gives a nonzero incidence residual",
            boundary="not count-once theorem closure",
        ),
        StatusEntry(
            name="G52-4: residual nonentry status",
            topic="residual zeta/kappa and accounting reentry",
            status="RESIDUAL_NONENTRY_THEOREM_REQUIRED",
            conclusion="metric-active residual reentry and accounting-source reentry remain rejected or theorem-burdened",
            boundary="not residual nonentry proof",
        ),
        StatusEntry(
            name="G52-5: source routing status",
            topic="ordinary mass source incidence",
            status="SOURCE_NO_DOUBLE_COUNTING_REQUIRED",
            conclusion="source duplication witnesses block physical use without a source-routing theorem",
            boundary="not ordinary matter separation theorem",
        ),
        StatusEntry(
            name="G52-6: A-sector mass status",
            topic="protected reduced A-sector mass coin",
            status="A_SECTOR_MASS_PROTECTION_REQUIRED",
            conclusion="independent scalar trace charge would shift the protected mass coin",
            boundary="not trace-sector mass neutrality proof",
        ),
        StatusEntry(
            name="G52-7: boundary/scalar silence status",
            topic="exterior scalar tail and boundary neutrality",
            status="BOUNDARY_SCALAR_SILENCE_REQUIRED",
            conclusion="nonzero trace-sector scalar charge creates an exterior scalar-tail flux witness",
            boundary="not boundary neutrality or scalar-silence proof",
        ),
        StatusEntry(
            name="G52-8: physical-use status",
            topic="B_s/F_zeta insertion and parent route",
            status="CANDIDATE_BLOCKED_FOR_PHYSICAL_USE",
            conclusion="B_s/F_zeta insertion remains blocked pending safety theorems",
            boundary="not insertable",
        ),
    ]


def build_witnesses() -> List[WitnessEntry]:
    return [
        WitnessEntry(
            name="W1: count-once double-entry witness",
            status="OBSTRUCTION_WITNESS_FOUND",
            witness="trace residual = T_zeta*(i_Bs + i_res - 1); at i_Bs=1 and i_res=1 residual = T_zeta",
            meaning="trace payload entering both B_s/F_zeta and residual channel double-counts at incidence level",
            boundary="diagnostic witness, not full dynamics",
        ),
        WitnessEntry(
            name="W2: source duplication through B_s",
            status="SOURCE_DUPLICATION_WITNESS",
            witness="source duplicate residual = S_M*(i_A + i_Bs + i_kappa + i_zeta - 1); A+B_s residual = S_M",
            meaning="ordinary mass source duplicated into B_s/F_zeta adds scalar source load",
            boundary="diagnostic witness, not source theorem",
        ),
        WitnessEntry(
            name="W3: source duplication through residual channels",
            status="SOURCE_DUPLICATION_WITNESS",
            witness="A+zeta+kappa residual = 2*S_M",
            meaning="residual channels cannot carry ordinary source load by bookkeeping",
            boundary="diagnostic witness, not total candidate rejection",
        ),
        WitnessEntry(
            name="W4: A-sector mass-shift witness",
            status="OBSTRUCTION_WITNESS_FOUND",
            witness="M_A = M but M_effective = M + Q_trace, so M_effective - M = Q_trace",
            meaning="independent trace-sector mass charge shifts the protected reduced mass coin",
            boundary="diagnostic witness, not covariant mass theorem",
        ),
        WitnessEntry(
            name="W5: exterior scalar-tail witness",
            status="SCALAR_TAIL_WITNESS",
            witness="phi_tail = q_zeta/r gives scalar flux = -4*pi*q_zeta",
            meaning="nonzero trace-sector scalar charge creates exterior scalar flux",
            boundary="zero charge remains condition/theorem target, not derived",
        ),
    ]


def build_burdens() -> List[BurdenEntry]:
    return [
        BurdenEntry(
            name="B1: count-once trace theorem",
            status="SAFETY_THEOREMS_REQUIRED",
            burden="derive or justify single scalar trace incidence before physical use",
            discipline="avoid trace double-counting",
        ),
        BurdenEntry(
            name="B2: residual nonentry theorem",
            status="RESIDUAL_NONENTRY_THEOREM_REQUIRED",
            burden="prove residual zeta/kappa cannot re-enter metric trace or source load",
            discipline="avoid residual metric/source reentry",
        ),
        BurdenEntry(
            name="B3: source no-double-counting theorem",
            status="SOURCE_NO_DOUBLE_COUNTING_REQUIRED",
            burden="derive ordinary source routing so A-sector mass response is not duplicated",
            discipline="protect reduced source channel",
        ),
        BurdenEntry(
            name="B4: A-sector mass protection theorem",
            status="A_SECTOR_MASS_PROTECTION_REQUIRED",
            burden="prove trace-sector variables and boundary terms do not shift M_A or M_ext",
            discipline="protect strongest reduced result",
        ),
        BurdenEntry(
            name="B5: boundary/scalar-silence theorem",
            status="BOUNDARY_SCALAR_SILENCE_REQUIRED",
            burden="derive boundary neutrality and exterior scalar silence or zero scalar charge",
            discipline="avoid shell/counterterm repair and scalar tails",
        ),
        BurdenEntry(
            name="B6: physical-use block",
            status="NOT_INSERTABLE",
            burden="keep B_s/F_zeta insertion, active O, recombination, and parent closure closed",
            discipline="do not turn diagnostic witnesses into field-equation machinery",
        ),
    ]


def build_rejected() -> List[RejectedUpgrade]:
    return [
        RejectedUpgrade(
            name="R1: safety load test as safety proof",
            upgrade="summarize Group 52 as proving residual/source/boundary safety",
            reason="Group 52 found diagnostic witnesses and theorem targets, not theorem closure",
        ),
        RejectedUpgrade(
            name="R2: audit survival as insertion",
            upgrade="use audit-only survival to license B_s/F_zeta insertion",
            reason="physical use remains blocked pending safety theorems",
        ),
        RejectedUpgrade(
            name="R3: witnesses as total rejection",
            upgrade="kill the narrow conditional candidate because diagnostic witnesses exist",
            reason="the candidate can remain useful as audit material",
        ),
        RejectedUpgrade(
            name="R4: active O shortcut",
            upgrade="jump directly to active O construction from Group 52",
            reason="O necessity requires its own audit after non-O routes are assessed",
        ),
        RejectedUpgrade(
            name="R5: zero scalar charge by assumption",
            upgrade="set q_zeta=0 without deriving boundary/scalar silence",
            reason="zero scalar charge is a condition or theorem target, not a result",
        ),
        RejectedUpgrade(
            name="R6: source by label",
            upgrade="route ordinary mass through B_s, zeta, kappa, or bookkeeping labels",
            reason="source load must be explicit, derived, and auditable",
        ),
    ]


def build_handoffs() -> List[HandoffEntry]:
    return [
        HandoffEntry(
            name="H1: residual/source theorem route",
            status="DEFERRED_WITH_TARGET",
            route="attempt a focused count-once trace, residual nonentry, source no-double-counting, and A-sector mass protection theorem group",
            caution="do not open insertion before theorem support",
        ),
        HandoffEntry(
            name="H2: boundary/scalar-silence route",
            status="DEFERRED_WITH_TARGET",
            route="attempt boundary neutrality and exterior scalar silence theorem work",
            caution="do not suppress scalar tails by assumption",
        ),
        HandoffEntry(
            name="H3: non-O obstruction route",
            status="DEFERRED_WITH_TARGET",
            route="classify whether non-O safety routes are obstructed before considering active O",
            caution="active O should not be used as a repair label",
        ),
        HandoffEntry(
            name="H4: forbidden immediate route",
            status="NOT_INSERTABLE",
            route="do not move directly to B_s/F_zeta insertion, active O, recombination, or parent closure",
            caution="Group 52 sharpened safety burdens but opened no physical-use route",
        ),
    ]


def record_governance(
    ns,
    entries: List[StatusEntry],
    witnesses: List[WitnessEntry],
    burdens: List[BurdenEntry],
    rejected: List[RejectedUpgrade],
    handoffs: List[HandoffEntry],
) -> None:
    record_marker(
        ns,
        MARKER_ID,
        "G52_residual_source_boundary_safety_summary",
        "Group 52 residual/source/boundary safety load-testing summary; no physical insertion",
    )

    for idx, item in enumerate(entries, start=1):
        record_claim(
            ns,
            f"{MARKER_ID}_entry_{idx}",
            MARKER_ID,
            item.status,
            f"{item.name}: {item.conclusion}. Boundary: {item.boundary}.",
        )

    for idx, item in enumerate(witnesses, start=1):
        record_claim(
            ns,
            f"{MARKER_ID}_witness_{idx}",
            MARKER_ID,
            item.status,
            f"{item.name}: {item.witness}. Meaning: {item.meaning}. Boundary: {item.boundary}.",
        )

    for idx, item in enumerate(burdens, start=1):
        record_obligation(
            ns,
            f"{MARKER_ID}_burden_{idx}",
            f"{item.name}: {item.burden}. Discipline: {item.discipline}.",
            item.status,
        )

    for idx, item in enumerate(rejected, start=1):
        record_claim(
            ns,
            f"{MARKER_ID}_rejected_{idx}",
            MARKER_ID,
            "REJECTED_ROUTE",
            f"Rejected upgrade: {item.upgrade}. Reason: {item.reason}.",
        )

    for idx, item in enumerate(handoffs, start=1):
        record_obligation(
            ns,
            f"{MARKER_ID}_handoff_{idx}",
            f"{item.name}: {item.route}. Caution: {item.caution}.",
            item.status,
        )


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  What did Group 52 establish by load-testing the retained conditional")
    print("  trace-normalization candidate against residual/source/boundary safety burdens?\n")
    print("Discipline:\n")
    print("  This script summarizes Group 52. It must preserve the difference")
    print("  between diagnostic witnesses, theorem targets, audit-only survival,")
    print("  and physical-use permission.")
    emit_line(
        out,
        "Group 52 status summary opened",
        "PASS",
        "closing safety load-testing batch while preserving audit-only survival and blocked physical use",
    )


def case_1(out: ScriptOutput) -> None:
    header("Case 1: Group 52 compact result ledger")
    ledger = [
        (
            "safety load-test scope",
            "SAFETY_LOAD_TEST_SURFACE_OPENED",
            "Group 52 performed first residual/source/boundary safety load testing",
        ),
        (
            "audit-only candidate survival",
            "CANDIDATE_SURVIVES_AS_AUDIT_ONLY",
            "the retained conditional candidate remains useful only as audit material",
        ),
        (
            "diagnostic witnesses",
            "OBSTRUCTION_WITNESS_FOUND",
            "trace double-count, source duplication, scalar mass-shift, and scalar-tail witnesses were found",
        ),
        (
            "safety theorem status",
            "SAFETY_THEOREMS_REQUIRED",
            "count-once trace, residual nonentry, source no-double-counting, A-sector mass protection, and boundary/scalar silence remain theorem targets",
        ),
        (
            "physical use",
            "NOT_INSERTABLE",
            "B_s/F_zeta insertion, active O, recombination, and parent closure remain closed",
        ),
        (
            "next handoff",
            "DEFERRED_WITH_TARGET",
            "focused residual/source safety or boundary/scalar-silence theorem work is the next non-looping technical target",
        ),
    ]
    for label, status, text in ledger:
        emit_line(out, label, status, text)


def case_2(out: ScriptOutput, entries: List[StatusEntry]) -> None:
    header("Case 2: Group 52 status entries")
    for entry in entries:
        subheader(entry.name)
        print(f"Topic: {entry.topic}")
        emit_line(out, entry.name, entry.status, f"{entry.conclusion}. Boundary: {entry.boundary}.")
    emit_line(out, "Group 52 status entries stated", "PASS", f"{len(entries)} status entries stated")


def case_3(out: ScriptOutput, witnesses: List[WitnessEntry]) -> None:
    header("Case 3: Diagnostic witnesses")
    for item in witnesses:
        subheader(item.name)
        print(f"Witness: {item.witness}")
        print(f"Meaning: {item.meaning}")
        emit_line(out, item.name, item.status, f"{item.meaning}. Boundary: {item.boundary}.")
    emit_line(out, "Group 52 witnesses preserved", "PASS", f"{len(witnesses)} diagnostic witnesses preserved")


def case_4(out: ScriptOutput, burdens: List[BurdenEntry]) -> None:
    header("Case 4: Open safety burdens")
    for burden in burdens:
        subheader(burden.name)
        emit_line(
            out,
            burden.name,
            burden.status,
            f"{burden.burden}. Discipline: {burden.discipline}.",
            obligation=True,
        )
    emit_line(
        out,
        "Group 52 safety burdens preserved",
        "PASS",
        f"{len(burdens)} safety burdens remain explicit",
        obligation=True,
    )


def case_5(out: ScriptOutput, rejected: List[RejectedUpgrade]) -> None:
    header("Case 5: Rejected summary upgrades")
    for item in rejected:
        subheader(item.name)
        print(f"Upgrade: {item.upgrade}")
        emit_line(out, item.name, "REJECTED_ROUTE", item.reason)
    emit_line(out, "Group 52 rejected upgrades preserved", "PASS", f"{len(rejected)} upgrade shortcuts rejected")


def case_6(out: ScriptOutput, handoffs: List[HandoffEntry]) -> None:
    header("Case 6: Safe handoffs")
    for handoff in handoffs:
        subheader(handoff.name)
        emit_line(out, handoff.name, handoff.status, f"{handoff.route}. Caution: {handoff.caution}.")
    emit_line(
        out,
        "Group 52 handoffs stated",
        "DEFERRED_WITH_TARGET",
        f"{len(handoffs)} handoff routes stated without opening physical use",
    )


def case_7(out: ScriptOutput) -> None:
    header("Case 7: Final interpretation")
    conclusions = [
        (
            "C1: Group 52 result",
            "SAFETY_LOAD_TEST_SURFACE_OPENED",
            "Group 52 load-tested the retained conditional trace-normalization candidate against residual/source/boundary safety burdens",
        ),
        (
            "C2: candidate status",
            "CANDIDATE_SURVIVES_AS_AUDIT_ONLY",
            "the conditional candidate survives only as audit material",
        ),
        (
            "C3: witness status",
            "OBSTRUCTION_WITNESS_FOUND",
            "diagnostic witnesses were found, but they are not total no-go theorems",
        ),
        (
            "C4: theorem status",
            "SAFETY_THEOREMS_REQUIRED",
            "safety burdens are sharpened but not closed",
        ),
        (
            "C5: physical-use status",
            "NOT_INSERTABLE",
            "B_s/F_zeta insertion, active O, recombination, and parent route remain closed",
        ),
        (
            "C6: next technical pressure",
            "DEFERRED_WITH_TARGET",
            "focused residual/source safety or boundary/scalar-silence theorem work should follow",
        ),
    ]
    for label, status, text in conclusions:
        emit_line(out, label, status, text)

    header("Final summary")
    print("Group 52 status summary result:\n")
    print("  Group 52 performed the first residual/source/boundary safety load test")
    print("  of the retained conditional symbolic paired trace-normalization candidate.")
    print()
    print("  The candidate remains audit-only. It is not adopted, not branch-selected,")
    print("  not insertable, and not parent-facing.")
    print()
    print("  Diagnostic witnesses found:")
    print("    trace double-count witness:")
    print("      residual = T_zeta when i_Bs=1 and i_res=1")
    print("    source duplication witness:")
    print("      A+B_s residual = S_M")
    print("      A+zeta+kappa residual = 2*S_M")
    print("    A-sector mass-shift witness:")
    print("      M_effective - M = Q_trace")
    print("    exterior scalar-tail witness:")
    print("      phi_tail=q_zeta/r gives scalar flux = -4*pi*q_zeta")
    print()
    print("  These witnesses do not prove total rejection of the narrow candidate.")
    print("  They show that physical use requires real safety theorems.")
    print()
    print("Still required:")
    print("  count-once scalar trace theorem")
    print("  residual nonentry theorem")
    print("  source no-double-counting theorem")
    print("  A-sector mass protection theorem")
    print("  boundary neutrality / exterior scalar silence theorem")
    print()
    print("Forbidden immediate next step:")
    print("  B_s/F_zeta insertion, active O, recombination, or parent closure")
    print()
    print("Best next technical target:")
    print("  focused residual/source safety theorem work or boundary/scalar-silence theorem work")


def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    entries = build_status_entries()
    witnesses = build_witnesses()
    burdens = build_burdens()
    rejected = build_rejected()
    handoffs = build_handoffs()

    case_0(out)
    case_1(out)
    case_2(out, entries)
    case_3(out, witnesses)
    case_4(out, burdens)
    case_5(out, rejected)
    case_6(out, handoffs)
    case_7(out)

    record_governance(ns, entries, witnesses, burdens, rejected, handoffs)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
