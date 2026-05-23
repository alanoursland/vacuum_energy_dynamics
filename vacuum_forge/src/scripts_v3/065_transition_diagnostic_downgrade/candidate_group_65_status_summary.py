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
SCRIPT_LABEL = "Candidate Group 65 Status Summary"
MARKER_ID = "g65_summary"

DEPENDENCIES = [
    ("g64_summary", "064_variational_stress_origin__candidate_group_64_status_summary", "g64_summary"),
    ("g65_problem", "065_transition_diagnostic_downgrade__candidate_downgrade_problem", "g65_problem"),
    ("g65_ledger", "065_transition_diagnostic_downgrade__candidate_diagnostic_preservation_ledger", "g65_ledger"),
    ("g65_fence", "065_transition_diagnostic_downgrade__candidate_forbidden_use_fence", "g65_fence"),
    ("g65_convert", "065_transition_diagnostic_downgrade__candidate_status_conversion", "g65_convert"),
    ("g65_revival", "065_transition_diagnostic_downgrade__candidate_revival_conditions", "g65_revival"),
    ("g65_parent", "065_transition_diagnostic_downgrade__candidate_parent_path_implications", "g65_parent"),
    ("g65_class", "065_transition_diagnostic_downgrade__candidate_downgrade_route_classifier", "g65_class"),
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
        "DOWNGRADE_OPENED": StatusMark.INFO,
        "DIAGNOSTIC_LEDGER_RECORDED": StatusMark.PASS,
        "DIAGNOSTIC_ONLY_STATUS_ASSIGNED": StatusMark.PASS,
        "FORBIDDEN_USE_FENCE_RECORDED": StatusMark.PASS,
        "PHYSICAL_USE_FORBIDDEN": StatusMark.FAIL,
        "REVIVAL_GATE_RECORDED": StatusMark.PASS,
        "REVIVAL_REQUIRES_THEOREM": StatusMark.OBLIGATION,
        "PARENT_PATH_CLEANED": StatusMark.INFO,
        "CANDIDATE_QUARANTINED": StatusMark.INFO,
        "BOUNDARY_DIAGNOSTICS_PRESERVED": StatusMark.PASS,
        "NOT_FULL_NO_GO": StatusMark.DEFER,
        "PHYSICAL_USE_BLOCKED": StatusMark.DEFER,
        "NOT_INSERTABLE": StatusMark.DEFER,
        "DEFERRED_WITH_TARGET": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status in {"PHYSICAL_USE_FORBIDDEN"}:
        return GovernanceStatus.REJECTED_ROUTE
    if status in {"REVIVAL_REQUIRES_THEOREM", "POLICY_RULE"}:
        return GovernanceStatus.POLICY_RULE
    return GovernanceStatus.UNVERIFIED


def obligation_status(status: str) -> ObligationStatus:
    if status in {"PHYSICAL_USE_BLOCKED", "NOT_INSERTABLE", "DEFERRED_WITH_TARGET", "NOT_FULL_NO_GO"}:
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
        SummaryEntry("S1: downgrade", "DIAGNOSTIC_ONLY_STATUS_ASSIGNED", "transition response is formally diagnostic-only", "not deletion and not candidate use"),
        SummaryEntry("S2: preservation", "BOUNDARY_DIAGNOSTICS_PRESERVED", "boundary-layer clues are preserved in a diagnostic ledger", "diagnostic only"),
        SummaryEntry("S3: forbidden use", "FORBIDDEN_USE_FENCE_RECORDED", "field-equation/stress/source/mass/trace/parent uses are forbidden", "hard fence"),
        SummaryEntry("S4: revival", "REVIVAL_GATE_RECORDED", "future revival requires a stronger theorem", "not automatic"),
        SummaryEntry("S5: parent path", "PARENT_PATH_CLEANED", "transition response is no longer a parent ingredient", "parent route still closed"),
        SummaryEntry("S6: caveat", "NOT_FULL_NO_GO", "this is not a proof that all future origins are impossible", "stronger theorem routes remain possible"),
        SummaryEntry("S7: physical use", "PHYSICAL_USE_BLOCKED", "no insertion, active O, recombination, or parent closure opened", "blocked"),
    ]


def record_governance(ns, entries: List[SummaryEntry]) -> None:
    record_marker(ns, MARKER_ID, "Group 65 diagnostic-only transition downgrade; no physical insertion")
    for idx, item in enumerate(entries, 1):
        record_claim(ns, f"{MARKER_ID}_entry_{idx}", MARKER_ID, item.status, f"{item.name}: {item.result}. Boundary: {item.boundary}.")
    record_obligation(
        ns,
        f"{MARKER_ID}_revival_gate",
        "Do not revive the transition response unless a future theorem derives u, p_free, trace/mass/source/covariant status, and boundary behavior.",
        "REVIVAL_REQUIRES_THEOREM",
    )
    record_obligation(
        ns,
        f"{MARKER_ID}_next_route",
        "Move next to parent blocker inventory or boundary diagnostic ledger unless a stronger origin route is deliberately attempted.",
        "DEFERRED_WITH_TARGET",
    )


def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    entries = build_entries()

    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  Did Group 65 formally quarantine the transition response as diagnostic-only?\n")
    print("Discipline:\n")
    print("  Preserve diagnostics, forbid physical use, and avoid full-no-go overclaim.")
    emit_line(out, "Group 65 status summary opened", "PASS", "closing diagnostic downgrade without insertion")

    header("Case 1: Group 65 compact status ledger")
    for item in entries:
        emit_line(out, item.name, item.status, f"{item.result}. Boundary: {item.boundary}.")

    header("Case 2: Diagnostic-only preserves")
    preserved = [
        "R1/R2 residue clues",
        "N_w weighted-neutralizer construction",
        "eta and eta^2 profiles",
        "weighted-neutrality construction",
        "P obstruction",
        "I_P=2*E_pr accounting",
        "trace/mass closure tension",
        "endpoint value/slope silence",
        "simple-origin failure record",
        "boundary-layer lesson",
    ]
    for item in preserved:
        emit_line(out, item, "BOUNDARY_DIAGNOSTICS_PRESERVED", "preserved as diagnostic clue")

    header("Case 3: Diagnostic-only forbids")
    forbidden = [
        "field-equation insertion",
        "stress tensor claim",
        "ordinary-source response",
        "mass response",
        "trace response",
        "covariant conservation claim",
        "parent equation ingredient",
        "active-O patch",
    ]
    for item in forbidden:
        emit_line(out, item, "PHYSICAL_USE_FORBIDDEN", "forbidden under diagnostic-only status")

    header("Case 4: Revival gate")
    revival = [
        "derive u relation",
        "derive p_free",
        "resolve trace/mass status",
        "prove ordinary-source neutrality",
        "provide covariant conservation or lift",
        "preserve boundary behavior",
        "avoid active-O disguise",
        "avoid source/repair/normalization/zero shortcuts",
    ]
    for item in revival:
        emit_line(out, item, "REVIVAL_REQUIRES_THEOREM", "required for future revival", obligation=True)

    header("Final summary")
    print("Group 65 status summary result:\n")
    print("  The transition response is formally diagnostic-only.")
    print("  Boundary-layer clues are preserved.")
    print("  Physical use is forbidden.")
    print("  Future revival requires a stronger theorem.")
    print("  This is not a full no-go theorem for every possible origin.")
    print()
    print("Next honest move:")
    print("  parent blocker inventory or boundary diagnostic ledger.")

    record_governance(ns, entries)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
