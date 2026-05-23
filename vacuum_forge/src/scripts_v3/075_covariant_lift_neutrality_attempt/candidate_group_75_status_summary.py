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
        method="inventory marker; no physical derivation",
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
    ("g74_summary", "74_boundary_lift_route_split_decision__candidate_group_74_status_summary", "g74_summary"),
    ("g75_problem", "75_covariant_lift_neutrality_attempt__candidate_lift_neutrality_problem", "g75_problem"),
    ("g75_requirements", "75_covariant_lift_neutrality_attempt__candidate_lift_cleanliness_requirements", "g75_requirements"),
    ("g75_bulk", "75_covariant_lift_neutrality_attempt__candidate_bulk_neutrality_test", "g75_bulk"),
    ("g75_gauge", "75_covariant_lift_neutrality_attempt__candidate_gauge_neutrality_test", "g75_gauge"),
    ("g75_shared_identity", "75_covariant_lift_neutrality_attempt__candidate_shared_lift_identity_test", "g75_shared_identity"),
    ("g75_discriminator", "75_covariant_lift_neutrality_attempt__candidate_mutual_cancellation_discriminator", "g75_discriminator"),
    ("g75_route_classifier", "75_covariant_lift_neutrality_attempt__candidate_lift_route_classifier", "g75_route_classifier"),
]
MARKER_ID = "g75_summary"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    header("Candidate Group 75 Status Summary")
    print("Question:")
    print("  Can L_bulk and L_gauge be neutralized by covariant lift structure?")
    print()
    print("Group 75 stable result:")
    print("  lift-cleanliness criteria explicit")
    print("  independent L_bulk=0 / L_gauge=0 route retained only as theorem target")
    print("  shared lift identity route retained only as theorem target")
    print("  independent neutrality not derived")
    print("  shared lift identity not derived")
    print("  repair-style mutual cancellation rejected")
    print("  D_layer remains separate unresolved theorem target")
    print("  parent divergence identity remains unproven")
    print("  recombination remains blocked")
    with out.governance_assessments():
        out.line("criteria", StatusMark.PASS, "legal lift-cleanliness routes stated")
        out.line("independent neutrality", StatusMark.OBLIGATION, "L_bulk=0 and L_gauge=0 not derived")
        out.line("shared identity", StatusMark.OBLIGATION, "lawful shared lift identity not derived")
        out.line("repair rejection", StatusMark.PASS, "chosen mutual cancellation rejected")
        out.line("D_layer", StatusMark.INFO, "D_layer remains separate open target")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "parent recombination remains blocked")
    with out.counterexamples():
        out.line("drop lift terms", StatusMark.FAIL, "L_bulk/L_gauge cannot be dropped by prose")
        out.line("mutual repair", StatusMark.FAIL, "choosing L_bulk=-L_gauge is repair-like unless derived")
        out.line("active O", StatusMark.FAIL, "active O by label remains forbidden")
        out.line("parent equation", StatusMark.FAIL, "parent construction remains forbidden")
    with out.unresolved_obligations():
        out.line("bulk neutrality", StatusMark.OBLIGATION, "derive L_bulk=0 or lawful shared identity")
        out.line("gauge neutrality", StatusMark.OBLIGATION, "derive L_gauge=0 or lawful shared identity")
        out.line("route management", StatusMark.OBLIGATION, "decide whether to keep lift route open, split ledger, or audit active O later")
    print("\nRecommended next routes:")
    print("  if keeping lift route alive: 76_covariant_lift_identity_construction")
    print("  route-management fallback: 76_boundary_lift_split_obligation_ledger")
    print("  active O only later: 76_active_O_necessity_or_rejection, if O-free routes fail cleanly")
    record_marker(ns, MARKER_ID, "Group 75 summary; no parent equation")
    record_claim(ns, MARKER_ID, "g75_summary_c1", GovernanceStatus.POLICY_RULE, "Lift cleanliness remains open; independent neutrality and shared identity are not derived.")
    record_claim(ns, MARKER_ID, "g75_summary_c2", GovernanceStatus.REJECTED_ROUTE, "Repair-style mutual cancellation and dropped terms are rejected.")
    record_obligation(ns, "g75_summary_o1", "Derive or route-manage L_bulk/L_gauge neutrality.")
    record_obligation(ns, "g75_summary_o2", "Parent divergence identity remains unproven.")
    ns.write_run_metadata()
if __name__ == "__main__":
    main()
