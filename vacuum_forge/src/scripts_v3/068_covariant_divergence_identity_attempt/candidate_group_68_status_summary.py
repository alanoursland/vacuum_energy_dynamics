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
SCRIPT_LABEL = "Candidate Group 68 Status Summary"
MARKER_ID = "g68_summary"

DEPENDENCIES = [
    ("g67_summary", "067_source_trace_divergence_blocker_audit__candidate_group_67_status_summary", "g67_summary"),
    ("g68_problem", "068_covariant_divergence_identity_attempt__candidate_covariant_identity_problem", "g68_problem"),
    ("g68_target", "068_covariant_divergence_identity_attempt__candidate_no_repair_identity_target", "g68_target"),
    ("g68_lift", "068_covariant_divergence_identity_attempt__candidate_covariant_lift_requirement", "g68_lift"),
    ("g68_boundary", "068_covariant_divergence_identity_attempt__candidate_boundary_divergence_neutrality", "g68_boundary"),
    ("g68_repair", "068_covariant_divergence_identity_attempt__candidate_repair_current_rejection", "g68_repair"),
    ("g68_o", "068_covariant_divergence_identity_attempt__candidate_active_O_divergence_necessity", "g68_o"),
    ("g68_class", "068_covariant_divergence_identity_attempt__candidate_divergence_identity_route_classifier", "g68_class"),
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
        "NO_REPAIR_TARGET_DERIVED": StatusMark.PASS,
        "O_FREE_TARGET_DERIVED": StatusMark.PASS,
        "DIVERGENCE_TARGET_SHARPENED": StatusMark.PASS,
        "COVARIANT_LIFT_REQUIRED": StatusMark.OBLIGATION,
        "COVARIANT_LIFT_NOT_PROVEN": StatusMark.OBLIGATION,
        "BOUNDARY_NEUTRALITY_REQUIRED": StatusMark.OBLIGATION,
        "BOUNDARY_NEUTRALITY_NOT_PROVEN": StatusMark.OBLIGATION,
        "REPAIR_CURRENT_REJECTED": StatusMark.FAIL,
        "ACTIVE_O_NOT_CONSTRUCTED": StatusMark.DEFER,
        "ACTIVE_O_CONDITIONALLY_REQUIRED": StatusMark.DEFER,
        "ACTIVE_O_BY_LABEL_REJECTED": StatusMark.FAIL,
        "TRANSITION_REMAINS_DIAGNOSTIC": StatusMark.PASS,
        "DIVERGENCE_IDENTITY_NOT_PROVEN": StatusMark.OBLIGATION,
        "STRUCTURAL_CANCELLATION_REQUIRED": StatusMark.OBLIGATION,
        "RECOMBINATION_BLOCKED": StatusMark.DEFER,
        "PARENT_EQUATION_BLOCKED": StatusMark.DEFER,
        "NEXT_ROUTE_PRIORITIZED": StatusMark.INFO,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {"REPAIR_CURRENT_REJECTED", "ACTIVE_O_BY_LABEL_REJECTED"}:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {
        "COVARIANT_LIFT_REQUIRED",
        "COVARIANT_LIFT_NOT_PROVEN",
        "BOUNDARY_NEUTRALITY_REQUIRED",
        "BOUNDARY_NEUTRALITY_NOT_PROVEN",
        "DIVERGENCE_IDENTITY_NOT_PROVEN",
        "STRUCTURAL_CANCELLATION_REQUIRED",
    }:
        return GovernanceStatus.POLICY_RULE
    return GovernanceStatus.UNVERIFIED


def obligation_status(status: str) -> ObligationStatus:
    if status in {
        "RECOMBINATION_BLOCKED",
        "PARENT_EQUATION_BLOCKED",
        "DEFERRED_WITH_TARGET",
        "ACTIVE_O_NOT_CONSTRUCTED",
        "ACTIVE_O_CONDITIONALLY_REQUIRED",
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
        SummaryEntry("S1: no-repair target", "NO_REPAIR_TARGET_DERIVED", "D_lift + D_boundary + D_O = 0 is the no-repair target", "target not proof"),
        SummaryEntry("S2: O-free target", "O_FREE_TARGET_DERIVED", "D_lift + D_boundary = 0 is the preferred O-free target", "target not proof"),
        SummaryEntry("S3: covariant lift", "COVARIANT_LIFT_NOT_PROVEN", "covariant lift remains required and unproved", "open"),
        SummaryEntry("S4: boundary neutrality", "BOUNDARY_NEUTRALITY_NOT_PROVEN", "boundary divergence neutrality remains required and unproved", "open"),
        SummaryEntry("S5: repair", "REPAIR_CURRENT_REJECTED", "arbitrary D_repair cancellation is rejected", "rejected"),
        SummaryEntry("S6: active O", "ACTIVE_O_NOT_CONSTRUCTED", "active O remains unconstructed and cannot be used by label", "blocked"),
        SummaryEntry("S7: divergence identity", "DIVERGENCE_IDENTITY_NOT_PROVEN", "parent divergence identity remains unproven", "open"),
        SummaryEntry("S8: recombination", "RECOMBINATION_BLOCKED", "parent recombination remains blocked", "blocked"),
        SummaryEntry("S9: next route", "NEXT_ROUTE_PRIORITIZED", "boundary/covariant cancellation attempt is recommended next", "handoff"),
    ]


def record_governance(ns, entries: List[SummaryEntry]) -> None:
    record_marker(ns, MARKER_ID, "Group 68 covariant divergence identity attempt; no parent equation")
    for idx, item in enumerate(entries, 1):
        record_claim(ns, f"{MARKER_ID}_entry_{idx}", MARKER_ID, item.status, f"{item.name}: {item.result}. Boundary: {item.boundary}.")
    for label, status, text in [
        ("structural_cancellation", "STRUCTURAL_CANCELLATION_REQUIRED", "The O-free target D_lift + D_boundary = 0 requires structural theorem, not repair."),
        ("covariant_lift", "COVARIANT_LIFT_REQUIRED", "A covariant lift theorem is required before reduced divergence can become parent identity."),
        ("boundary_neutrality", "BOUNDARY_NEUTRALITY_REQUIRED", "Boundary divergence neutrality must be derived or structurally cancelled."),
        ("next_group", "DEFERRED_WITH_TARGET", "Move next to boundary/covariant cancellation attempt or covariant lift construction."),
    ]:
        record_obligation(ns, f"{MARKER_ID}_{label}", text, status)


def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    entries = build_entries()

    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  Did Group 68 prove a no-repair covariant parent divergence identity?\n")
    print("Discipline:\n")
    print("  Preserve sharpened identity targets without claiming divergence closure.")
    emit_line(out, "Group 68 status summary opened", "PASS", "closing divergence identity attempt without parent construction")

    header("Case 1: Group 68 compact status ledger")
    for item in entries:
        emit_line(out, item.name, item.status, f"{item.result}. Boundary: {item.boundary}.")

    header("Case 2: Derived targets")
    print("No-repair target:")
    print("  D_lift + D_boundary + D_O = 0")
    print()
    print("Preferred O-free target:")
    print("  D_lift + D_boundary = 0")
    print()
    print("Rejected repair:")
    print("  D_repair = -(D_lift + D_boundary + D_O)")

    header("Case 3: Open theorem burdens")
    emit_line(out, "structural cancellation required", "STRUCTURAL_CANCELLATION_REQUIRED", "D_lift + D_boundary = 0 must be derived structurally", obligation=True)
    emit_line(out, "covariant lift required", "COVARIANT_LIFT_REQUIRED", "reduced divergence balance is not yet covariant", obligation=True)
    emit_line(out, "boundary neutrality required", "BOUNDARY_NEUTRALITY_REQUIRED", "boundary divergence burden remains open", obligation=True)
    emit_line(out, "active O not constructed", "ACTIVE_O_NOT_CONSTRUCTED", "O cannot be used as cancellation label")
    emit_line(out, "recombination blocked", "RECOMBINATION_BLOCKED", "parent recombination remains unlicensed")

    header("Final summary")
    print("Group 68 status summary result:\n")
    print("  The no-repair divergence target is explicit.")
    print("  The preferred O-free target is explicit.")
    print("  Repair-current cancellation is rejected.")
    print("  Active O is not constructed and cannot be used by label.")
    print("  Covariant lift and boundary neutrality remain unproved.")
    print("  Parent divergence identity remains unproven.")
    print("  Parent recombination remains blocked.")
    print()
    print("Recommended next group:")
    print("  69_boundary_covariant_cancellation_attempt")

    record_governance(ns, entries)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
