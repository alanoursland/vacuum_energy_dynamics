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
    ("g79_D_layer_axioms", "79_axiom_candidate_inventory__candidate_D_layer_axiom_candidates", "g79_D_layer_axioms"),
    ("g80_criteria", "80_axiom_adoption_decision_surface__candidate_adoption_decision_criteria", "g80_criteria"),
]
MARKER_ID = "g80_D_layer_surface"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    rows = [("D_LAYER_GEOMETRIC_COMPONENT_AXIOM", "DEFERRED", "requires concrete geometry or explicit owner decision"), ("D_LAYER_COMPONENT_MEMBERSHIP_AXIOM", "DEFERRED", "requires common boundary object and membership burden"), ("D_LAYER_PAYLOAD_PURITY_AXIOM", "DEFERRED", "requires source/trace/mass/repair/O payload validation"), ("DIAGNOSTIC_TRANSITION_LAYER_AXIOM", "REJECTED", "diagnostic transition remains excluded"), ("REPAIR_LAYER_AXIOM", "REJECTED", "repair layer would choose term after leakage appears")]
    header("Candidate D_layer Axiom Decision Surface")
    for name, status, reason in rows: print(f"{name}: {status}; {reason}")
    with out.governance_assessments():
        out.line("geometric component axiom", StatusMark.DEFER, "deferred pending concrete geometry or owner decision")
        out.line("component membership axiom", StatusMark.DEFER, "deferred pending common boundary object")
        out.line("payload purity axiom", StatusMark.DEFER, "deferred pending payload validation")
    with out.counterexamples():
        out.line("diagnostic transition axiom", StatusMark.FAIL, "rejected shortcut")
        out.line("repair layer axiom", StatusMark.FAIL, "rejected shortcut")
    with out.unresolved_obligations():
        out.line("D_layer validation", StatusMark.OBLIGATION, "derive or explicitly decide D_layer geometry, membership, and payload purity before use")
    record_marker(ns, MARKER_ID, "D_layer axiom decision surface; no adoption")
    record_claim(ns, MARKER_ID, "g80_dlayer_c1", GovernanceStatus.POLICY_RULE, "D_layer axiom candidates are deferred; none are adopted.")
    record_claim(ns, MARKER_ID, "g80_dlayer_c2", GovernanceStatus.REJECTED_ROUTE, "Diagnostic-transition and repair-layer axiom shortcuts remain rejected.")
    record_obligation(ns, "g80_dlayer_o1", "Future D_layer adoption decision must validate geometry, membership, and payload purity.")
    ns.write_run_metadata()
    print("\nPossible next script:\n  candidate_lift_axiom_decision_surface.py")
if __name__ == "__main__": main()
