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
SCRIPT_LABEL = "Candidate Group 67 Status Summary"
MARKER_ID = "g67_summary"

DEPENDENCIES = [
    ("g66_summary", "66_parent_blocker_inventory__candidate_group_66_status_summary", "g66_summary"),
    ("g67_problem", "67_source_trace_divergence_blocker_audit__candidate_blocker_problem", "g67_problem"),
    ("g67_incidence", "67_source_trace_divergence_blocker_audit__candidate_source_trace_incidence_audit", "g67_incidence"),
    ("g67_count", "67_source_trace_divergence_blocker_audit__candidate_count_once_compatibility_sieve", "g67_count"),
    ("g67_residual", "67_source_trace_divergence_blocker_audit__candidate_residual_nonentry_sieve", "g67_residual"),
    ("g67_div", "67_source_trace_divergence_blocker_audit__candidate_divergence_identity_obstruction", "g67_div"),
    ("g67_cons", "67_source_trace_divergence_blocker_audit__candidate_conservation_dependency_sieve", "g67_cons"),
    ("g67_class", "67_source_trace_divergence_blocker_audit__candidate_parent_blocker_route_classifier", "g67_class"),
]


@dataclass(frozen=True)
class SummaryEntry:
    name: str
    status: str
    result: str
    boundary: str


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


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
        "INCIDENCE_AUDIT_DERIVED": StatusMark.PASS,
        "SOURCE_COUNT_ONCE_CLARIFIED": StatusMark.PASS,
        "TRACE_COUNT_ONCE_CLARIFIED": StatusMark.PASS,
        "STRICT_SAFE_STATE_IDENTIFIED": StatusMark.PASS,
        "SOURCE_REPAIR_REJECTED": StatusMark.FAIL,
        "TRACE_REPAIR_REJECTED": StatusMark.FAIL,
        "RESIDUAL_NONENTRY_CLARIFIED": StatusMark.PASS,
        "RESIDUAL_REENTRY_REJECTED": StatusMark.FAIL,
        "TRANSITION_REMAINS_DIAGNOSTIC": StatusMark.PASS,
        "DIVERGENCE_BALANCE_DERIVED": StatusMark.PASS,
        "DIVERGENCE_IDENTITY_NOT_PROVEN": StatusMark.OBLIGATION,
        "COUNT_ONCE_NOT_SUFFICIENT": StatusMark.OBLIGATION,
        "FORCED_REPAIR_REJECTED": StatusMark.FAIL,
        "CONSERVATION_DEPENDENCIES_RECORDED": StatusMark.PASS,
        "COVARIANT_LIFT_REQUIRED": StatusMark.OBLIGATION,
        "BOUNDARY_NEUTRALITY_REQUIRED": StatusMark.OBLIGATION,
        "ACTIVE_O_DECISION_REQUIRED": StatusMark.OBLIGATION,
        "RECOMBINATION_BLOCKED": StatusMark.DEFER,
        "PARENT_EQUATION_BLOCKED": StatusMark.DEFER,
        "NEXT_ROUTE_PRIORITIZED": StatusMark.INFO,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {
        "SOURCE_REPAIR_REJECTED",
        "TRACE_REPAIR_REJECTED",
        "RESIDUAL_REENTRY_REJECTED",
        "FORCED_REPAIR_REJECTED",
    }:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {
        "DIVERGENCE_IDENTITY_NOT_PROVEN",
        "COUNT_ONCE_NOT_SUFFICIENT",
        "COVARIANT_LIFT_REQUIRED",
        "BOUNDARY_NEUTRALITY_REQUIRED",
        "ACTIVE_O_DECISION_REQUIRED",
    }:
        return GovernanceStatus.POLICY_RULE
    return GovernanceStatus.UNVERIFIED


def obligation_status(status: str) -> ObligationStatus:
    if status in {
        "RECOMBINATION_BLOCKED",
        "PARENT_EQUATION_BLOCKED",
        "DEFERRED_WITH_TARGET",
    }:
        return ObligationStatus.DEFERRED
    return ObligationStatus.OPEN


def record_marker(ns, marker_id: str, scope: str) -> None:
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[],
        output=sp.Symbol(marker_id),
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


def build_entries() -> List[SummaryEntry]:
    return [
        SummaryEntry("S1: incidence residuals", "INCIDENCE_AUDIT_DERIVED", "source and trace count-once incidence residuals are explicit", "necessary not sufficient"),
        SummaryEntry("S2: strict state", "STRICT_SAFE_STATE_IDENTIFIED", "strict role-compatible incidence state identified", "necessary not sufficient"),
        SummaryEntry("S3: residual nonentry", "RESIDUAL_NONENTRY_CLARIFIED", "residual parent-carrier routes are rejected", "hard fence"),
        SummaryEntry("S4: transition response", "TRANSITION_REMAINS_DIAGNOSTIC", "transition response remains diagnostic-only and noncontributing", "hard fence"),
        SummaryEntry("S5: divergence balance", "DIVERGENCE_BALANCE_DERIVED", "reduced divergence balance shows count-once removes count residual but not full divergence burden", "not covariant theorem"),
        SummaryEntry("S6: divergence identity", "DIVERGENCE_IDENTITY_NOT_PROVEN", "parent divergence identity remains unproven", "open"),
        SummaryEntry("S7: recombination", "RECOMBINATION_BLOCKED", "parent recombination remains blocked", "blocked"),
        SummaryEntry("S8: next route", "NEXT_ROUTE_PRIORITIZED", "covariant divergence identity attempt is the likely next hard blocker", "handoff"),
    ]


def record_governance(ns, entries: List[SummaryEntry]) -> None:
    record_marker(ns, MARKER_ID, "Group 67 source/trace/divergence blocker audit; no parent equation")
    for idx, item in enumerate(entries, 1):
        record_claim(ns, f"{MARKER_ID}_entry_{idx}", MARKER_ID, item.status, f"{item.name}: {item.result}. Boundary: {item.boundary}.")
    for label, status, text in [
        ("covariant_lift", "COVARIANT_LIFT_REQUIRED", "Covariant lift is required before the reduced divergence balance can become a parent identity."),
        ("boundary_neutrality", "BOUNDARY_NEUTRALITY_REQUIRED", "Boundary neutrality remains required for divergence closure."),
        ("active_O_decision", "ACTIVE_O_DECISION_REQUIRED", "Active O must be proven unnecessary or constructed if separation cannot otherwise be achieved."),
        ("next_group", "DEFERRED_WITH_TARGET", "Move next to a covariant divergence identity attempt or boundary diagnostic ledger."),
    ]:
        record_obligation(ns, f"{MARKER_ID}_{label}", text, status)


def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    entries = build_entries()

    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  What did the source/trace/divergence blocker audit establish?\n")
    print("Discipline:\n")
    print("  Preserve incidence progress while not claiming divergence closure or parent recombination.")
    emit_line(out, "Group 67 status summary opened", "PASS", "closing source/trace/divergence audit without parent construction")

    header("Case 1: Group 67 compact status ledger")
    for item in entries:
        emit_line(out, item.name, item.status, f"{item.result}. Boundary: {item.boundary}.")

    header("Case 2: Core incidence result")
    print("Strict parent-compatible incidence:")
    print("  i_A=1")
    print("  i_src_extra=0")
    print("  i_B=1")
    print("  i_res=0")
    print("  i_trace_extra=0")

    header("Case 3: Divergence status")
    emit_line(out, "count-once necessary", "PASS", "strict incidence can remove count residual contribution")
    emit_line(out, "count-once not sufficient", "COUNT_ONCE_NOT_SUFFICIENT", "boundary, covariant lift, active O decision, and no-repair status remain open", obligation=True)
    emit_line(out, "divergence identity not proven", "DIVERGENCE_IDENTITY_NOT_PROVEN", "no covariant parent identity derived", obligation=True)
    emit_line(out, "recombination blocked", "RECOMBINATION_BLOCKED", "parent recombination remains unlicensed")

    header("Final summary")
    print("Group 67 status summary result:\n")
    print("  Source and trace count-once conditions are explicit.")
    print("  The strict safe incidence state is identified.")
    print("  Residual reentry and repair/carrying routes are rejected.")
    print("  Count-once is necessary but not sufficient for divergence identity.")
    print("  Parent divergence identity remains unproven.")
    print("  Parent recombination remains blocked.")
    print()
    print("Recommended next group:")
    print("  68_covariant_divergence_identity_attempt")

    record_governance(ns, entries)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
