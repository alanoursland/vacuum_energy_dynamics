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
    ("g78_dependency_graph", "078_boundary_lift_split_obligation_ledger__candidate_route_dependency_graph", "g78_dependency_graph"),
]
MARKER_ID = "g78_readiness"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    gates = [
        ("D_layer_construction", "concrete boundary/layer geometry supplied", "not ready without concrete geometry"),
        ("gauge_exact_rho_theorem", "concrete exactness operator supplied", "not ready from exact label alone"),
        ("boundary_exact_rho_theorem", "concrete boundary divergence object supplied", "not ready from boundary label alone"),
        ("lift_identity_construction", "concrete covariant lift identity candidate supplied", "not ready from exact-pair scaffold alone"),
        ("active_O_audit", "O-free split targets fail cleanly or require projection", "not ready from frustration alone"),
        ("parent_equation", "parent divergence identity and recombination rule proven", "blocked"),
    ]

    header("Candidate Readiness Gate Matrix")
    for name, requirement, status in gates:
        print(f"{name}:")
        print(f"  required_input: {requirement}")
        print(f"  status: {status}")

    with out.governance_assessments():
        out.line("readiness gates", StatusMark.PASS, "future-route readiness criteria stated")
        out.line("parent gate", StatusMark.DEFER, "parent equation blocked")
        out.line("active O gate", StatusMark.DEFER, "active O not ready from frustration alone")
    with out.counterexamples():
        out.line("label as input", StatusMark.FAIL, "labels are not concrete theorem input")
        out.line("scaffold as theorem", StatusMark.FAIL, "compatibility scaffold is not readiness proof")
        out.line("parent jump", StatusMark.FAIL, "parent equation remains forbidden")

    record_marker(ns, MARKER_ID, "readiness gate matrix; no theorem proof")
    record_claim(ns, MARKER_ID, "g78_ready_c1", GovernanceStatus.POLICY_RULE, "Future theorem attempts require concrete route-specific input.")
    record_obligation(ns, "g78_ready_o1", "Select next work only when readiness gate is satisfied or route-management is intended.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_repetition_risk_sieve.py")

if __name__ == "__main__":
    main()
