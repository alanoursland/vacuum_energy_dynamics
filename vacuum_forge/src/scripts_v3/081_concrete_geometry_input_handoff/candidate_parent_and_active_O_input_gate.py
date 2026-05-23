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
    ("g81_dlayer_gate", "81_concrete_geometry_input_handoff__candidate_D_layer_geometry_input_gate", "g81_dlayer_gate"),
    ("g81_lift_gate", "81_concrete_geometry_input_handoff__candidate_lift_identity_input_gate", "g81_lift_gate"),
    ("g81_rho_gate", "81_concrete_geometry_input_handoff__candidate_rho_exactness_input_gate", "g81_rho_gate"),
]
MARKER_ID = "g81_parent_active_gate"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    parent_prereqs = [
        "D_layer closed or explicitly adopted later",
        "lift route closed or explicitly adopted later",
        "rho route closed or explicitly adopted later",
        "parent divergence identity derived",
        "recombination rule derived",
    ]
    active_O_prereqs = [
        "O-free split targets fail cleanly",
        "projection requirement is structural",
        "domain/kernel/image/boundary behavior supplied",
        "not repair current",
    ]
    parent_ready = False
    active_O_forced = False

    header("Candidate Parent and Active-O Input Gate")
    print("Parent route prerequisites:")
    for item in parent_prereqs:
        print(f"  - {item}")
    print("Active-O route prerequisites:")
    for item in active_O_prereqs:
        print(f"  - {item}")
    print(f"parent ready now = {parent_ready}")
    print(f"active O forced now = {active_O_forced}")

    with out.governance_assessments():
        out.line("parent gate", StatusMark.DEFER, "parent route remains blocked")
        out.line("active O gate", StatusMark.DEFER, "active O not forced")
        out.line("projection requirements", StatusMark.OBLIGATION, "active O requires real operator structure if pursued")
    with out.counterexamples():
        out.line("parent from handoff", StatusMark.FAIL, "handoff gate cannot license parent equation")
        out.line("active O by frustration", StatusMark.FAIL, "frustration alone does not force active O")
        out.line("projection by label", StatusMark.FAIL, "active O requires domain/kernel/image/boundary behavior")

    record_marker(ns, MARKER_ID, "parent and active-O input gate; no parent/O construction")
    record_claim(ns, MARKER_ID, "g81_parent_active_c1", GovernanceStatus.POLICY_RULE, "Parent and active-O routes remain blocked/deferred without concrete prerequisites.")
    record_obligation(ns, "g81_parent_active_o1", "Parent divergence and recombination remain prerequisites.")
    record_obligation(ns, "g81_parent_active_o2", "Active O requires clean O-free failure or structural projection requirement.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_next_group_selector_from_input.py")

if __name__ == "__main__":
    main()
