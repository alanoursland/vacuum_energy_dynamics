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
    ("g74_route_ledger", "074_boundary_lift_route_split_decision__candidate_route_status_ledger", "g74_route_ledger"),
    ("g74_layer_decision", "074_boundary_lift_route_split_decision__candidate_layer_route_status_decision", "g74_layer_decision"),
    ("g74_lift_cleanliness", "074_boundary_lift_route_split_decision__candidate_lift_cleanliness_route_status", "g74_lift_cleanliness"),
]
MARKER_ID = "g74_decision_matrix"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    routes = [
        ("monolithic_boundary_lift_theorem", "not_ready", "D_layer and lift cleanliness remain open"),
        ("split_theorem_targets", "retained_preferred", "carries D_layer and lift cleanliness separately"),
        ("compatibility_only_downgrade", "defer", "possible later if subroutes fail cleanly"),
        ("active_O_jump", "rejected_now", "O-free subtargets unresolved, not exhausted"),
        ("parent_equation_jump", "rejected", "parent divergence unproven and recombination blocked"),
        ("new_axiom_adoption", "defer", "would require separate explicit axiom group"),
    ]

    header("Candidate Boundary-Match Route Decision Matrix")
    for name, status, reason in routes:
        print(f"{name}: {status}; {reason}")

    with out.governance_assessments():
        out.line("split route", StatusMark.PASS, "split theorem targets are the safest retained route")
        out.line("monolithic route", StatusMark.OBLIGATION, "not ready as one theorem")
        out.line("downgrade", StatusMark.DEFER, "hard downgrade deferred until subroutes fail cleanly")
        out.line("active O", StatusMark.DEFER, "not yet forced")
        out.line("parent", StatusMark.DEFER, "parent equation blocked")
    with out.counterexamples():
        out.line("monolithic closure", StatusMark.FAIL, "would hide D_layer/lift blockers")
        out.line("active O jump", StatusMark.FAIL, "frustration is not O construction")
        out.line("parent jump", StatusMark.FAIL, "parent equation construction remains forbidden")

    record_marker(ns, MARKER_ID, "boundary-lift route decision matrix")
    record_claim(ns, MARKER_ID, "g74_matrix_c1", GovernanceStatus.POLICY_RULE, "Boundary-lift route should split into theorem targets rather than close monolithically.")
    record_claim(ns, MARKER_ID, "g74_matrix_c2", GovernanceStatus.REJECTED_ROUTE, "Active-O and parent jumps are rejected at this stage.")
    record_obligation(ns, "g74_matrix_o1", "Carry split theorem targets forward explicitly.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_active_O_gate_audit.py")

if __name__ == "__main__":
    main()
