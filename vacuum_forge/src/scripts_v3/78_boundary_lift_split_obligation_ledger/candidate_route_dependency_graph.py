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
    ("g78_inventory", "78_boundary_lift_split_obligation_ledger__candidate_split_target_inventory", "g78_inventory"),
]
MARKER_ID = "g78_dependency_graph"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    chains = {
        "D_layer_route": [
            "concrete_geometry",
            "component_membership",
            "payload_purity",
            "boundary_match_participation",
        ],
        "lift_route": [
            "concrete_lift_identity",
            "K_and_sign_origin",
            "rho_handling",
            "L_bulk_L_gauge_closure",
        ],
        "rho_route": [
            "exactness_candidate",
            "physical_remainder_test",
            "zero_or_inert_theorem",
        ],
        "parent_route": [
            "D_layer_closed",
            "lift_closed",
            "rho_closed",
            "parent_divergence_identity",
            "recombination_rule",
        ],
    }

    header("Candidate Route Dependency Graph")
    for route, steps in chains.items():
        print(f"{route}:")
        for idx, step in enumerate(steps, 1):
            print(f"  {idx}. {step}")

    with out.governance_assessments():
        out.line("D_layer chain", StatusMark.OBLIGATION, "D_layer route requires concrete geometry before membership/use")
        out.line("lift chain", StatusMark.OBLIGATION, "lift route requires concrete identity before rho closure")
        out.line("rho chain", StatusMark.OBLIGATION, "rho route requires exactness and physical remainder tests")
        out.line("parent chain", StatusMark.DEFER, "parent route waits for subtarget closure")
    with out.counterexamples():
        out.line("skip dependency", StatusMark.FAIL, "cannot use downstream target before upstream proof")
        out.line("parent before subtargets", StatusMark.FAIL, "parent recombination cannot precede subtarget closure")

    record_marker(ns, MARKER_ID, "route dependency graph; no theorem proof")
    record_claim(ns, MARKER_ID, "g78_graph_c1", GovernanceStatus.POLICY_RULE, "Future groups must respect dependency order among D_layer, lift, rho, parent, and recombination routes.")
    record_obligation(ns, "g78_graph_o1", "Use dependency graph to gate future theorem attempts.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_readiness_gate_matrix.py")

if __name__ == "__main__":
    main()
