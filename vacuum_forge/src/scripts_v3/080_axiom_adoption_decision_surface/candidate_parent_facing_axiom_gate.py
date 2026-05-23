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
    ("g80_D_layer_surface", "080_axiom_adoption_decision_surface__candidate_D_layer_axiom_decision_surface", "g80_D_layer_surface"),
    ("g80_lift_surface", "080_axiom_adoption_decision_surface__candidate_lift_axiom_decision_surface", "g80_lift_surface"),
    ("g80_rho_surface", "080_axiom_adoption_decision_surface__candidate_rho_axiom_decision_surface", "g80_rho_surface"),
]
MARKER_ID = "g80_parent_gate"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    prerequisites = [("D_layer_status", "deferred_not_adopted"), ("lift_status", "deferred_not_adopted"), ("rho_status", "deferred_not_adopted"), ("parent_divergence_identity", "unproven"), ("recombination_rule", "missing")]
    parent_open = False; recombination_open = False
    header("Candidate Parent-Facing Axiom Gate")
    for name, status in prerequisites: print(f"{name}: {status}")
    print(f"parent equation licensed now = {parent_open}")
    print(f"recombination licensed now = {recombination_open}")
    with out.governance_assessments():
        out.line("parent equation", StatusMark.DEFER, "not licensed by axiom decision surface")
        out.line("recombination", StatusMark.DEFER, "not licensed by axiom decision surface")
        out.line("parent-facing axiom", StatusMark.OBLIGATION, "requires separate future group if desired")
    with out.counterexamples():
        out.line("parent from candidate axiom", StatusMark.FAIL, "candidate axiom cannot open parent equation")
        out.line("recombination from deferred axiom", StatusMark.FAIL, "deferred axiom cannot license recombination")
        out.line("divergence by declaration", StatusMark.FAIL, "parent divergence identity remains unproven")
    with out.unresolved_obligations():
        out.line("parent divergence", StatusMark.OBLIGATION, "derive parent divergence identity before parent use")
        out.line("recombination rule", StatusMark.OBLIGATION, "derive recombination rule before recombination")
    record_marker(ns, MARKER_ID, "parent-facing axiom gate; no parent equation")
    record_claim(ns, MARKER_ID, "g80_parent_c1", GovernanceStatus.POLICY_RULE, "No axiom candidate in Group 80 licenses parent equation or recombination.")
    record_obligation(ns, "g80_parent_o1", "Parent divergence identity remains unproven.")
    record_obligation(ns, "g80_parent_o2", "Recombination rule remains missing.")
    ns.write_run_metadata()
    print("\nPossible next script:\n  candidate_adoption_route_classifier.py")
if __name__ == "__main__": main()
