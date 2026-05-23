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
SCRIPT_LABEL = "Candidate Group 66 Status Summary"
MARKER_ID = "g66_summary"

DEPENDENCIES = [
    ("g65_summary", "65_transition_diagnostic_downgrade__candidate_group_65_status_summary", "g65_summary"),
    ("g66_problem", "66_parent_blocker_inventory__candidate_parent_inventory_problem", "g66_problem"),
    ("g66_ledger", "66_parent_blocker_inventory__candidate_artifact_status_ledger", "g66_ledger"),
    ("g66_matrix", "66_parent_blocker_inventory__candidate_parent_blocker_matrix", "g66_matrix"),
    ("g66_recomb", "66_parent_blocker_inventory__candidate_recombination_prerequisite_sieve", "g66_recomb"),
    ("g66_graph", "66_parent_blocker_inventory__candidate_blocker_dependency_graph", "g66_graph"),
    ("g66_priority", "66_parent_blocker_inventory__candidate_next_route_priority", "g66_priority"),
    ("g66_class", "66_parent_blocker_inventory__candidate_parent_inventory_classifier", "g66_class"),
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
        "ARTIFACT_LEDGER_RECORDED": StatusMark.PASS,
        "BLOCKER_MATRIX_RECORDED": StatusMark.PASS,
        "RECOMBINATION_BLOCKED": StatusMark.DEFER,
        "DEPENDENCY_GRAPH_RECORDED": StatusMark.PASS,
        "NEXT_ROUTE_PRIORITIZED": StatusMark.INFO,
        "PARENT_EQUATION_BLOCKED": StatusMark.DEFER,
        "TRANSITION_NOT_PARENT_INGREDIENT": StatusMark.PASS,
        "DIAGNOSTIC_CONSTRAINT_RETAINED": StatusMark.PASS,
        "SOURCE_TRACE_DIVERGENCE_TARGET": StatusMark.OBLIGATION,
        "DIVERGENCE_IDENTITY_REQUIRED": StatusMark.OBLIGATION,
        "COVARIANT_LIFT_REQUIRED": StatusMark.OBLIGATION,
        "BOUNDARY_NEUTRALITY_REQUIRED": StatusMark.OBLIGATION,
        "ACTIVE_O_NOT_CONSTRUCTED": StatusMark.DEFER,
        "TRACE_NORMALIZATION_NOT_ADOPTED": StatusMark.DEFER,
        "PHYSICAL_USE_BLOCKED": StatusMark.DEFER,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {
        "SOURCE_TRACE_DIVERGENCE_TARGET",
        "DIVERGENCE_IDENTITY_REQUIRED",
        "COVARIANT_LIFT_REQUIRED",
        "BOUNDARY_NEUTRALITY_REQUIRED",
    }:
        return GovernanceStatus.POLICY_RULE
    return GovernanceStatus.UNVERIFIED


def obligation_status(status: str) -> ObligationStatus:
    if status in {
        "PARENT_EQUATION_BLOCKED",
        "RECOMBINATION_BLOCKED",
        "ACTIVE_O_NOT_CONSTRUCTED",
        "TRACE_NORMALIZATION_NOT_ADOPTED",
        "PHYSICAL_USE_BLOCKED",
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
        SummaryEntry("S1: artifact ledger", "ARTIFACT_LEDGER_RECORDED", "current artifacts classified by parent usability", "no parent equation"),
        SummaryEntry("S2: transition response", "TRANSITION_NOT_PARENT_INGREDIENT", "transition response remains diagnostic-only and not a parent ingredient", "hard fence"),
        SummaryEntry("S3: blocker matrix", "BLOCKER_MATRIX_RECORDED", "remaining parent blockers are explicit", "inventory only"),
        SummaryEntry("S4: recombination", "RECOMBINATION_BLOCKED", "recombination prerequisites are unmet", "blocked"),
        SummaryEntry("S5: dependency graph", "DEPENDENCY_GRAPH_RECORDED", "parent equation is downstream of unresolved blockers", "no construction"),
        SummaryEntry("S6: next route", "NEXT_ROUTE_PRIORITIZED", "source/trace/divergence blocker audit is the recommended next group", "handoff"),
        SummaryEntry("S7: parent status", "PARENT_EQUATION_BLOCKED", "no parent field equation is ready", "blocked"),
    ]


def record_governance(ns, entries: List[SummaryEntry]) -> None:
    record_marker(ns, MARKER_ID, "Group 66 parent blocker inventory; no parent equation")
    for idx, item in enumerate(entries, 1):
        record_claim(ns, f"{MARKER_ID}_entry_{idx}", MARKER_ID, item.status, f"{item.name}: {item.result}. Boundary: {item.boundary}.")
    for label, status, text in [
        ("source_trace_divergence", "SOURCE_TRACE_DIVERGENCE_TARGET", "Source count, trace count, and divergence identity remain the highest-priority blocker cluster."),
        ("covariant_lift", "COVARIANT_LIFT_REQUIRED", "Reduced diagnostics require covariant lift before parent use."),
        ("boundary_neutrality", "BOUNDARY_NEUTRALITY_REQUIRED", "Boundary neutrality and exterior scalar silence remain parent constraints."),
        ("next_group", "DEFERRED_WITH_TARGET", "Move next to source/trace/divergence blocker audit unless deliberately choosing a boundary ledger."),
    ]:
        record_obligation(ns, f"{MARKER_ID}_{label}", text, status)


def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    entries = build_entries()

    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  What blocks parent field-equation construction after transition-response quarantine?\n")
    print("Discipline:\n")
    print("  Inventory blockers without writing or implying a parent equation.")
    emit_line(out, "Group 66 status summary opened", "PASS", "closing parent blocker inventory without parent construction")

    header("Case 1: Group 66 compact status ledger")
    for item in entries:
        emit_line(out, item.name, item.status, f"{item.result}. Boundary: {item.boundary}.")

    header("Case 2: Current parent blockers")
    blockers = [
        ("source count once", "SOURCE_TRACE_DIVERGENCE_TARGET", "ordinary source must not duplicate or be repaired"),
        ("trace count once", "SOURCE_TRACE_DIVERGENCE_TARGET", "trace payload must not duplicate or reenter residual"),
        ("divergence identity", "DIVERGENCE_IDENTITY_REQUIRED", "parent equation requires conservation/divergence structure"),
        ("covariant lift", "COVARIANT_LIFT_REQUIRED", "reduced diagnostics cannot be treated as covariant theorems"),
        ("boundary neutrality", "BOUNDARY_NEUTRALITY_REQUIRED", "boundary/exterior scalar silence must be protected"),
        ("active O decision", "ACTIVE_O_NOT_CONSTRUCTED", "active O must be proven unnecessary or constructed"),
        ("trace normalization decision", "TRACE_NORMALIZATION_NOT_ADOPTED", "paired trace normalization remains not adopted"),
        ("recombination rule", "RECOMBINATION_BLOCKED", "admissible sectors cannot yet be recombined"),
    ]
    for label, status, text in blockers:
        emit_line(out, label, status, text, obligation=status.endswith("REQUIRED") or status == "SOURCE_TRACE_DIVERGENCE_TARGET")

    header("Final summary")
    print("Group 66 status summary result:\n")
    print("  Parent blockers are inventoried.")
    print("  The transition response is not a parent ingredient.")
    print("  Boundary diagnostics remain constraints.")
    print("  Recombination is blocked.")
    print("  No parent field equation is ready.")
    print()
    print("Recommended next group:")
    print("  67_source_trace_divergence_blocker_audit")

    record_governance(ns, entries)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
