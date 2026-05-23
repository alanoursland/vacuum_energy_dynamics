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
    ("g74_decision_matrix", "74_boundary_lift_route_split_decision__candidate_boundary_match_route_decision_matrix", "g74_decision_matrix"),
    ("g74_parent_gate", "74_boundary_lift_route_split_decision__candidate_parent_recombination_gate", "g74_parent_gate"),
]
MARKER_ID = "g74_next_route"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    routes = [
        ("75_covariant_lift_neutrality_attempt", "preferred", "attacks L_bulk/L_gauge without needing new D_layer geometry"),
        ("75_boundary_lift_split_obligation_ledger", "safe_fallback", "records split targets before more attempts"),
        ("75_layer_geometry_axiom_inventory", "conditional", "only if theory wants explicit layer axiom candidates"),
        ("75_layer_generator_construction_with_concrete_geometry", "conditional", "only if new concrete geometry is supplied"),
        ("75_active_O_necessity_or_rejection", "later", "only after O-free split targets fail cleanly"),
    ]

    header("Candidate Next Route Classifier")
    for name, status, reason in routes:
        print(f"{name}: {status}; {reason}")

    with out.governance_assessments():
        out.line("preferred next", StatusMark.INFO, "75_covariant_lift_neutrality_attempt")
        out.line("route split", StatusMark.PASS, "split route state is explicit enough to move to lift-cleanliness")
        out.line("layer route", StatusMark.DEFER, "continue only with new concrete geometry or axiom inventory")
        out.line("active O", StatusMark.DEFER, "later only if O-free routes fail cleanly")
    with out.counterexamples():
        out.line("repeat broad generator search", StatusMark.FAIL, "do not repackage Groups 71-73 without a new concrete family")
        out.line("immediate parent", StatusMark.FAIL, "parent route still closed")

    record_marker(ns, MARKER_ID, "next route classifier")
    record_claim(ns, MARKER_ID, "g74_next_c1", GovernanceStatus.POLICY_RULE, "Preferred next route is covariant lift neutrality, unless route ledger is desired first.")
    record_claim(ns, MARKER_ID, "g74_next_c2", GovernanceStatus.REJECTED_ROUTE, "Repeating broad generator search without a new concrete family is rejected.")
    record_obligation(ns, "g74_next_o1", "Start next group from split theorem target state.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_group_74_status_summary.py")

if __name__ == "__main__":
    main()
