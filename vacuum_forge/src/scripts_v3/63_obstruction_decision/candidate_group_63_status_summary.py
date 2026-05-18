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
SCRIPT_LABEL = "Candidate Group 63 Status Summary"
MARKER_ID = "g63_summary"

DEPENDENCIES = [
    ("g62_summary", "62_stress_energy_accounting__candidate_group_62_status_summary", "g62_summary"),
    ("g63_problem", "63_obstruction_decision__candidate_obstruction_problem", "g63_problem"),
    ("g63_inputs", "63_obstruction_decision__candidate_obstruction_inputs", "g63_inputs"),
    ("g63_decision", "63_obstruction_decision__candidate_status_decision_surface", "g63_decision"),
    ("g63_down", "63_obstruction_decision__candidate_downgrade_semantics", "g63_down"),
    ("g63_contract", "63_obstruction_decision__candidate_retention_contract", "g63_contract"),
    ("g63_escape", "63_obstruction_decision__candidate_escape_hatch_requirements", "g63_escape"),
    ("g63_class", "63_obstruction_decision__candidate_obstruction_route_classifier", "g63_class"),
    ("g63_reconcile", "63_obstruction_decision__candidate_obstruction_batch_reconcile", "g63_reconcile"),
]


@dataclass(frozen=True)
class StatusEntry:
    name: str
    status: str
    conclusion: str
    boundary: str


@dataclass(frozen=True)
class ResultEntry:
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
class RejectedRoute:
    name: str
    route: str
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
        "OBSTRUCTION_DECISION_OPENED": StatusMark.INFO,
        "OBSTRUCTION_INPUTS_RESTATED": StatusMark.PASS,
        "DECISION_SURFACE_DERIVED": StatusMark.PASS,
        "INSERTION_REJECTED": StatusMark.FAIL,
        "UNQUALIFIED_RETENTION_REJECTED": StatusMark.FAIL,
        "DIAGNOSTIC_DOWNGRADE_ALLOWED": StatusMark.INFO,
        "CONDITIONAL_AUDIT_RETENTION_ALLOWED": StatusMark.INFO,
        "RETENTION_CONTRACT_REQUIRED": StatusMark.OBLIGATION,
        "ESCAPE_REQUIREMENTS_DERIVED": StatusMark.PASS,
        "ESCAPE_HATCH_REJECTED": StatusMark.FAIL,
        "ZERO_RESPONSE_REJECTED_AS_TRIVIAL": StatusMark.FAIL,
        "REPAIR_ROUTE_REJECTED": StatusMark.FAIL,
        "AMPLITUDE_UNDERIVED": StatusMark.OBLIGATION,
        "STRESS_ACCOUNTING_NOT_CLOSED": StatusMark.OBLIGATION,
        "AUDIT_CANDIDATE_RETAINED": StatusMark.INFO,
        "DIAGNOSTIC_ONLY_DOWNGRADE_POSSIBLE": StatusMark.DEFER,
        "DIAGNOSTIC_ONLY_STATUS_DEFINED": StatusMark.PASS,
        "COVARIANT_LIFT_REQUIRED": StatusMark.OBLIGATION,
        "ENERGY_ACCOUNTING_REQUIRED": StatusMark.OBLIGATION,
        "SOURCE_SAFETY_REQUIRED": StatusMark.OBLIGATION,
        "DIVERGENCE_IDENTITY_REQUIRED": StatusMark.OBLIGATION,
        "SAFETY_THEOREMS_REQUIRED": StatusMark.OBLIGATION,
        "PHYSICAL_USE_BLOCKED": StatusMark.DEFER,
        "NOT_INSERTABLE": StatusMark.DEFER,
        "ACTIVE_O_NECESSITY_NOT_ESTABLISHED": StatusMark.DEFER,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REJECTED_ROUTE": StatusMark.FAIL,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {
        "INSERTION_REJECTED",
        "UNQUALIFIED_RETENTION_REJECTED",
        "ESCAPE_HATCH_REJECTED",
        "ZERO_RESPONSE_REJECTED_AS_TRIVIAL",
        "REPAIR_ROUTE_REJECTED",
        "REJECTED_ROUTE",
    }:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {
        "RETENTION_CONTRACT_REQUIRED",
        "AMPLITUDE_UNDERIVED",
        "STRESS_ACCOUNTING_NOT_CLOSED",
        "COVARIANT_LIFT_REQUIRED",
        "ENERGY_ACCOUNTING_REQUIRED",
        "SOURCE_SAFETY_REQUIRED",
        "DIVERGENCE_IDENTITY_REQUIRED",
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
        "DIAGNOSTIC_ONLY_DOWNGRADE_POSSIBLE",
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
        StatusEntry("G63-1: obstruction decision", "OBSTRUCTION_DECISION_OPENED", "Group 63 classified the transition-response candidate after the Group 62 stress-accounting obstruction", "not insertion"),
        StatusEntry("G63-2: promotion rejected", "INSERTION_REJECTED", "the candidate is not insertable or promotable while stress accounting remains unclosed", "rejected"),
        StatusEntry("G63-3: allowed statuses", "DECISION_SURFACE_DERIVED", "only diagnostic-only downgrade or conditional audit retention remain licensed", "status decision"),
        StatusEntry("G63-4: physical use", "PHYSICAL_USE_BLOCKED", "candidate remains blocked for physical use", "not parent-ready"),
    ]


def build_result_entries() -> List[ResultEntry]:
    return [
        ResultEntry("C1: obstruction inputs", "OBSTRUCTION_INPUTS_RESTATED", "Group 62 closure algebra, P obstruction, I_P=2E_pr, and p_free burden control status", "decision is grounded in prior obstruction", "reduced"),
        ResultEntry("C2: insertion status", "INSERTION_REJECTED", "insert_now is rejected", "stress accounting is not closed", "rejected"),
        ResultEntry("C3: unqualified retention", "UNQUALIFIED_RETENTION_REJECTED", "retain_unqualified is rejected", "candidate cannot remain live without a principle contract", "rejected"),
        ResultEntry("C4: diagnostic downgrade", "DIAGNOSTIC_ONLY_STATUS_DEFINED", "diagnostic-only status preserves clues but forbids physical use", "clean downgrade is allowed", "allowed"),
        ResultEntry("C5: conditional audit retention", "RETENTION_CONTRACT_REQUIRED", "conditional retention requires explicit burdens for u, p_free, trace/mass, source, covariance, and boundary behavior", "allowed only under contract", "conditional"),
        ResultEntry("C6: escape matrix", "ESCAPE_REQUIREMENTS_DERIVED", "valid future routes must derive a real stress origin, compensation/inertness, covariant lift, modified closure, or independent tensor sector", "shortcuts are rejected", "open"),
        ResultEntry("C7: shortcut rejection", "ESCAPE_HATCH_REJECTED", "u=±P, P=0 by fiat, p_free=0, and O-disguise are rejected as escapes", "no shortcut solves the obstruction", "rejected"),
        ResultEntry("C8: route status", "STRESS_ACCOUNTING_NOT_CLOSED", "candidate remains audit-only or diagnostic-only", "not promoted", "not insertable"),
    ]


def build_burdens() -> List[BurdenEntry]:
    return [
        BurdenEntry("B1: stress principle or downgrade", "DEFERRED_WITH_TARGET", "next route should either attempt a real stress-origin route or record diagnostic-only downgrade", "avoid looping"),
        BurdenEntry("B2: retention contract", "RETENTION_CONTRACT_REQUIRED", "conditional retention must keep u, p_free, trace/mass, source, covariance, and boundary burdens attached", "avoid candidate hoarding"),
        BurdenEntry("B3: stress-energy principle", "ENERGY_ACCOUNTING_REQUIRED", "derive u/p_r/p_t/p_free if candidate remains live", "avoid arbitrary stress"),
        BurdenEntry("B4: safety theorem package", "SAFETY_THEOREMS_REQUIRED", "prove source/trace/mass/covariant safety if candidate remains live", "avoid hidden load"),
        BurdenEntry("B5: physical-use block", "NOT_INSERTABLE", "keep insertion, active O, recombination, and parent closure closed", "avoid status inflation"),
    ]


def build_rejected() -> List[RejectedRoute]:
    return [
        RejectedRoute("R1: insertion", "insert transition response now", "stress accounting is not closed"),
        RejectedRoute("R2: unqualified retention", "keep candidate live without contract", "hides obstruction"),
        RejectedRoute("R3: zero response", "set p_free=0", "trivial no-response"),
        RejectedRoute("R4: repair amplitude", "choose p_free/u to cancel diagnostics", "repair, not derivation"),
        RejectedRoute("R5: shortcut u=P", "use u=P as full escape", "trace-only closure; active burden remains"),
        RejectedRoute("R6: shortcut u=-P", "use u=-P as full escape", "active-only closure; trace burden remains"),
        RejectedRoute("R7: P=0 by fiat", "declare pressure sum zero", "P witness is nonzero"),
        RejectedRoute("R8: active O disguise", "hide load in active O", "operator is not constructed"),
    ]


def build_handoffs() -> List[HandoffEntry]:
    return [
        HandoffEntry("H1: record downgrade", "DIAGNOSTIC_DOWNGRADE_ALLOWED", "record diagnostic-only downgrade for the transition response", "preserve clues but forbid physical use"),
        HandoffEntry("H2: variational stress origin", "ENERGY_ACCOUNTING_REQUIRED", "attempt a real stress-origin derivation for u, p_free, and closure", "do not use labels as principles"),
        HandoffEntry("H3: covariant layer lift", "COVARIANT_LIFT_REQUIRED", "lift reduced diagnostics to geometric layer objects", "do not treat lift as stress closure by itself"),
    ]


def record_governance(ns, entries, results, burdens, rejected, handoffs) -> None:
    record_marker(ns, MARKER_ID, "G63_obstruction_decision_summary", "Group 63 obstruction decision summary; no physical insertion")
    for idx, item in enumerate(entries, 1):
        record_claim(ns, f"{MARKER_ID}_entry_{idx}", MARKER_ID, item.status, f"{item.name}: {item.conclusion}. Boundary: {item.boundary}.")
    for idx, item in enumerate(results, 1):
        record_claim(ns, f"{MARKER_ID}_result_{idx}", MARKER_ID, item.status, f"{item.name}: {item.result}. Meaning: {item.meaning}. Boundary: {item.boundary}.")
    for idx, item in enumerate(burdens, 1):
        record_obligation(ns, f"{MARKER_ID}_burden_{idx}", f"{item.name}: {item.burden}. Discipline: {item.discipline}.", item.status)
    for idx, item in enumerate(rejected, 1):
        record_claim(ns, f"{MARKER_ID}_rejected_{idx}", MARKER_ID, "REJECTED_ROUTE", f"Rejected route: {item.route}. Reason: {item.reason}.")
    for idx, item in enumerate(handoffs, 1):
        record_obligation(ns, f"{MARKER_ID}_handoff_{idx}", f"{item.name}: {item.route}. Caution: {item.caution}.", item.status)


def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    entries = build_status_entries()
    results = build_result_entries()
    burdens = build_burdens()
    rejected = build_rejected()
    handoffs = build_handoffs()

    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  What status is licensed for the transition response after the Group 62 stress-accounting obstruction?\n")
    print("Discipline:\n")
    print("  Preserve rejected insertion, diagnostic-only downgrade, conditional retention contract, and blocked physical use.")
    emit_line(out, "Group 63 status summary opened", "PASS", "closing obstruction decision without solving closure or inserting the response")

    header("Case 1: Group 63 compact result ledger")
    ledger = [
        ("obstruction decision opened", "OBSTRUCTION_DECISION_OPENED", "candidate status was classified after Group 62 obstruction"),
        ("inputs restated", "OBSTRUCTION_INPUTS_RESTATED", "P/I_P/p_free burdens control status"),
        ("decision surface", "DECISION_SURFACE_DERIVED", "allowed statuses are diagnostic-only downgrade or conditional retention"),
        ("insertion rejected", "INSERTION_REJECTED", "physical use is not licensed"),
        ("unqualified retention rejected", "UNQUALIFIED_RETENTION_REJECTED", "candidate cannot remain live without contract"),
        ("diagnostic downgrade", "DIAGNOSTIC_ONLY_STATUS_DEFINED", "downgrade preserves clues and forbids physical use"),
        ("conditional retention", "RETENTION_CONTRACT_REQUIRED", "retention requires named future derivation burdens"),
        ("escape matrix", "ESCAPE_REQUIREMENTS_DERIVED", "valid future routes must derive something real"),
        ("shortcut escapes", "ESCAPE_HATCH_REJECTED", "u/P/p_free/O shortcuts rejected"),
        ("candidate status", "STRESS_ACCOUNTING_NOT_CLOSED", "candidate is audit-only or diagnostic-only, not promoted"),
        ("physical use", "PHYSICAL_USE_BLOCKED", "no insertion, active O, recombination, or parent closure opened"),
    ]
    for label, status, text in ledger:
        emit_line(out, label, status, text)

    header("Case 2: Group 63 status entries")
    for item in entries:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.conclusion}. Boundary: {item.boundary}.")

    header("Case 3: Obstruction decision results")
    for item in results:
        subheader(item.name)
        print(f"Result: {item.result}")
        print(f"Meaning: {item.meaning}")
        emit_line(out, item.name, item.status, f"{item.meaning}. Boundary: {item.boundary}.")

    header("Case 4: Open burdens after Group 63")
    for item in burdens:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.burden}. Discipline: {item.discipline}.", obligation=True)

    header("Case 5: Rejected obstruction-status routes")
    for item in rejected:
        subheader(item.name)
        print(f"Route: {item.route}")
        emit_line(out, item.name, "REJECTED_ROUTE", item.reason)

    header("Case 6: Safe handoffs")
    for item in handoffs:
        subheader(item.name)
        emit_line(out, item.name, item.status, f"{item.route}. Caution: {item.caution}.")

    header("Case 7: Final interpretation")
    conclusions = [
        ("C1: Group 63 result", "DECISION_SURFACE_DERIVED", "candidate status was classified after the stress-accounting obstruction"),
        ("C2: rejected promotion", "INSERTION_REJECTED", "insertion and unqualified retention are rejected"),
        ("C3: allowed downgrade", "DIAGNOSTIC_ONLY_STATUS_DEFINED", "diagnostic-only downgrade is allowed and preserves useful clues"),
        ("C4: conditional retention", "RETENTION_CONTRACT_REQUIRED", "conditional audit retention is allowed only with explicit future-principle burdens"),
        ("C5: candidate status", "STRESS_ACCOUNTING_NOT_CLOSED", "candidate remains audit-only or diagnostic-only"),
        ("C6: physical-use status", "NOT_INSERTABLE", "B_s/F_zeta insertion, active O, recombination, and parent route remain closed"),
    ]
    for label, status, text in conclusions:
        emit_line(out, label, status, text)

    header("Final summary")
    print("Group 63 status summary result:\n")
    print("  Group 63 classified the obstructed transition-response candidate after Group 62.")
    print("  It did not solve stress-energy accounting and did not insert the candidate.")
    print()
    print("  Main status results:")
    print("    Insertion is rejected.")
    print("    Unqualified live-candidate retention is rejected.")
    print("    Diagnostic-only downgrade is allowed and defined.")
    print("    Conditional audit retention is allowed only with an explicit retention contract.")
    print("    Shortcut escapes are rejected: u=±P, P=0 by fiat, p_free=0, repair amplitude, and active-O disguise.")
    print()
    print("  Diagnostic-only preserves:")
    print("    R1/R2 clues, N_w construction, eta/eta^2 profiles, P obstruction, I_P=2E_pr, trace/mass tension, and boundary-layer lesson.")
    print()
    print("  Diagnostic-only forbids:")
    print("    field-equation term, stress tensor claim, source/mass/trace response, covariant conservation claim, and parent ingredient.")
    print()
    print("  Conditional retention requires:")
    print("    derive u relation, p_free, trace/mass status, source neutrality, covariant conservation/lift, and boundary behavior.")
    print()
    print("Still required:")
    print("  either record diagnostic-only downgrade or attempt a real stress-origin route.")
    print()
    print("Forbidden immediate next step:")
    print("  B_s/F_zeta insertion, transition response insertion, active O construction, recombination, or parent closure.")

    record_governance(ns, entries, results, burdens, rejected, handoffs)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
