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
    ("g74_active_O_gate", "74_boundary_lift_route_split_decision__candidate_active_O_gate_audit", "g74_active_O_gate"),
]
MARKER_ID = "g74_parent_gate"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    gates = {
        "D_layer_legitimacy": False,
        "L_bulk_neutrality": False,
        "L_gauge_neutrality": False,
        "parent_divergence_identity": False,
        "recombination_rule": False,
        "active_O_decision_if_needed": False,
    }
    recombination_licensed = all(gates.values())

    header("Candidate Parent Recombination Gate")
    print("Parent/recombination prerequisites:")
    for name, closed in gates.items():
        print(f"  {name}: {'closed' if closed else 'open'}")
    print(f"recombination licensed = {recombination_licensed}")

    with out.governance_assessments():
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "recombination remains blocked")
        out.line("parent equation", StatusMark.DEFER, "parent equation construction remains forbidden")
    with out.counterexamples():
        out.line("recombine diagnostics", StatusMark.FAIL, "diagnostic/scaffold objects cannot be recombined into parent equation")
        out.line("recombine unresolved candidates", StatusMark.FAIL, "open theorem targets cannot be treated as closed")
        out.line("summary as theorem", StatusMark.FAIL, "route split decision is not parent identity")

    record_marker(ns, MARKER_ID, "parent recombination gate remains closed")
    record_claim(ns, MARKER_ID, "g74_parent_c1", GovernanceStatus.POLICY_RULE, "Parent recombination remains blocked by open layer/lift/divergence gates.")
    record_claim(ns, MARKER_ID, "g74_parent_c2", GovernanceStatus.REJECTED_ROUTE, "Recombining diagnostics or unresolved candidates is rejected.")
    record_obligation(ns, "g74_parent_o1", "Keep parent recombination closed until prerequisites are derived.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_next_route_classifier.py")

if __name__ == "__main__":
    main()
