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
    ("g77_summary", "77_remainder_obstruction_audit__candidate_group_77_status_summary", "g77_summary"),
    ("g78_problem", "78_boundary_lift_split_obligation_ledger__candidate_obligation_ledger_problem", "g78_problem"),
]
MARKER_ID = "g78_inventory"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    open_targets = [
        "common_boundary_generator_origin",
        "D_layer_geometric_legitimacy",
        "D_layer_component_membership",
        "L_bulk_neutrality",
        "L_gauge_neutrality",
        "shared_lift_identity",
        "rho_zero_exact_inert_status",
        "parent_divergence_identity",
        "recombination_rule",
    ]
    retained_routes = [
        "concrete_D_layer_geometry_route",
        "concrete_covariant_lift_identity_route",
        "concrete_gauge_exact_rho_route",
        "concrete_boundary_exact_rho_route",
    ]
    rejected_routes = [
        "diagnostic_transition_insertion",
        "B_with_hat_generator",
        "free_signs_or_coefficients",
        "repair_currents",
        "dropped_L_bulk_or_L_gauge",
        "dropped_rho",
        "exact_or_inert_by_label",
        "active_O_by_label",
        "parent_equation_jump",
    ]
    deferred_routes = [
        "active_O_necessity_audit",
        "compatibility_only_hard_downgrade",
        "axiom_adoption",
    ]

    header("Candidate Split Target Inventory")
    print("Open theorem targets:")
    for item in open_targets:
        print(f"  - {item}")
    print("Retained concrete theorem routes:")
    for item in retained_routes:
        print(f"  - {item}")
    print("Rejected routes:")
    for item in rejected_routes:
        print(f"  - {item}")
    print("Deferred routes:")
    for item in deferred_routes:
        print(f"  - {item}")

    with out.governance_assessments():
        out.line("open targets", StatusMark.OBLIGATION, f"{len(open_targets)} open targets inventoried")
        out.line("retained routes", StatusMark.INFO, "retained only with concrete input")
        out.line("rejected routes", StatusMark.PASS, "unsafe shortcuts remain rejected")
        out.line("deferred routes", StatusMark.DEFER, "active O, hard downgrade, and axiom adoption deferred")
    with out.counterexamples():
        out.line("promotion", StatusMark.FAIL, "open target cannot be promoted to theorem")
        out.line("hard kill", StatusMark.FAIL, "retained route cannot be treated as no-go theorem")

    record_marker(ns, MARKER_ID, "split target inventory; no theorem proof")
    record_claim(ns, MARKER_ID, "g78_inventory_c1", GovernanceStatus.POLICY_RULE, "Boundary-lift route is split into open targets, retained concrete routes, rejected shortcuts, and deferred decisions.")
    for item in open_targets:
        record_obligation(ns, f"g78_open_{item}", f"Open boundary-lift obligation: {item}.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_route_dependency_graph.py")

if __name__ == "__main__":
    main()
