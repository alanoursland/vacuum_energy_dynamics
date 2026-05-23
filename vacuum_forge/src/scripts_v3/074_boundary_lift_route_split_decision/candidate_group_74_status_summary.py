from __future__ import annotations
from pathlib import Path
import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    ClaimRecord, ClaimTier, GovernanceStatus, ObligationStatus,
    ProofObligationRecord, RecordKind, ScriptOutput, StatusMark,
)

ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"

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

def record_marker(ns, marker_id: str, scope: str) -> None:
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[],
        output=sp.Symbol(marker_id),
        method="route/governance marker; no physical derivation",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
        scope=scope,
    )

def record_claim(ns, marker_id: str, claim_id: str, status: GovernanceStatus, statement: str) -> None:
    ns.record_claim(
        ClaimRecord(
            claim_id=claim_id,
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=status,
            statement=statement,
            derivation_ids=[marker_id],
            obligation_ids=[],
        )
    )

def record_obligation(ns, obligation_id: str, statement: str, status: ObligationStatus = ObligationStatus.OPEN) -> None:
    ns.record_obligation(
        ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=obligation_id,
            status=status,
            required_by=[SCRIPT_ID],
            description=statement,
        )
    )

DEPENDENCIES = [
    ("g73_summary", "073_layer_generator_construction__candidate_group_73_status_summary", "g73_summary"),
    ("g74_problem", "074_boundary_lift_route_split_decision__candidate_split_decision_problem", "g74_problem"),
    ("g74_route_ledger", "074_boundary_lift_route_split_decision__candidate_route_status_ledger", "g74_route_ledger"),
    ("g74_layer_decision", "074_boundary_lift_route_split_decision__candidate_layer_route_status_decision", "g74_layer_decision"),
    ("g74_lift_cleanliness", "074_boundary_lift_route_split_decision__candidate_lift_cleanliness_route_status", "g74_lift_cleanliness"),
    ("g74_decision_matrix", "074_boundary_lift_route_split_decision__candidate_boundary_match_route_decision_matrix", "g74_decision_matrix"),
    ("g74_active_O_gate", "074_boundary_lift_route_split_decision__candidate_active_O_gate_audit", "g74_active_O_gate"),
    ("g74_parent_gate", "074_boundary_lift_route_split_decision__candidate_parent_recombination_gate", "g74_parent_gate"),
    ("g74_next_route", "074_boundary_lift_route_split_decision__candidate_next_route_classifier", "g74_next_route"),
]
MARKER_ID = "g74_summary"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Group 74 Status Summary")
    print("Question:")
    print("  Should the boundary-lift route remain monolithic, split, downgrade, or jump to active O?")
    print()
    print("Group 74 stable result:")
    stable = [
        "monolithic boundary-lift closure not ready",
        "boundary-lift route should split into theorem targets",
        "D_layer remains geometric theorem target; not legitimate yet; not rejected",
        "L_bulk/L_gauge remain covariant lift-cleanliness obligations",
        "compatibility-only downgrade deferred; not yet hard downgrade",
        "active O not yet forced",
        "parent divergence identity remains unproven",
        "recombination remains blocked",
        "preferred next route: 75_covariant_lift_neutrality_attempt",
    ]
    for item in stable:
        print(f"  {item}")

    with out.governance_assessments():
        out.line("route split", StatusMark.PASS, "split theorem targets required")
        out.line("monolithic closure", StatusMark.OBLIGATION, "not ready")
        out.line("D_layer", StatusMark.OBLIGATION, "geometric legitimacy remains open")
        out.line("lift cleanliness", StatusMark.OBLIGATION, "L_bulk/L_gauge remain open")
        out.line("active O", StatusMark.DEFER, "not yet forced")
        out.line("parent divergence", StatusMark.OBLIGATION, "unproven")
        out.line("recombination", StatusMark.DEFER, "blocked")
        out.line("next route", StatusMark.INFO, "075_covariant_lift_neutrality_attempt")
    with out.counterexamples():
        out.line("hard route kill", StatusMark.FAIL, "current obstruction is not no-go theorem")
        out.line("route promotion", StatusMark.FAIL, "cannot promote while D_layer/lift remain open")
        out.line("active O by frustration", StatusMark.FAIL, "not proof of necessity")
        out.line("parent equation", StatusMark.FAIL, "parent construction remains forbidden")
    with out.unresolved_obligations():
        out.line("D_layer theorem", StatusMark.OBLIGATION, "derive or route-manage D_layer origin")
        out.line("lift theorem", StatusMark.OBLIGATION, "derive L_bulk/L_gauge neutrality or lawful shared identity")
        out.line("parent identity", StatusMark.OBLIGATION, "derive parent divergence identity only after subtargets close")

    record_marker(ns, MARKER_ID, "Group 74 summary; route split decision only")
    record_claim(ns, MARKER_ID, "g74_summary_c1", GovernanceStatus.POLICY_RULE, "Boundary-lift route should split into theorem targets; monolithic closure is not ready.")
    record_claim(ns, MARKER_ID, "g74_summary_c2", GovernanceStatus.POLICY_RULE, "D_layer and L_bulk/L_gauge remain separate obligations.")
    record_claim(ns, MARKER_ID, "g74_summary_c3", GovernanceStatus.REJECTED_ROUTE, "Hard route kill, route promotion, active-O jump, and parent construction are rejected.")
    record_obligation(ns, "g74_summary_o1", "Attempt covariant lift neutrality next or record split obligations.")
    record_obligation(ns, "g74_summary_o2", "Keep parent recombination blocked.")
    ns.write_run_metadata()
    print("\nRecommended next group:")
    print("  75_covariant_lift_neutrality_attempt")

if __name__ == "__main__":
    main()
