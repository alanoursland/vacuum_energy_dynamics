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
]
MARKER_ID = "g74_active_O_gate"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    subtargets = {
        "D_layer_legitimacy": False,
        "L_bulk_neutrality": False,
        "L_gauge_neutrality": False,
        "common_generator_origin": False,
    }
    clean_exhaustion = all(subtargets.values())
    active_O_forced = False

    header("Candidate Active-O Gate Audit")
    print("O-free unresolved subtargets:")
    for name, closed in subtargets.items():
        print(f"  {name}: {'closed' if closed else 'open'}")
    print(f"clean O-free exhaustion = {clean_exhaustion}")
    print(f"active O forced now = {active_O_forced}")

    with out.governance_assessments():
        out.line("O-free route", StatusMark.INFO, "unresolved subtargets remain; route not cleanly exhausted")
        out.line("active O", StatusMark.DEFER, "active O not forced yet")
        out.line("future O audit", StatusMark.OBLIGATION, "only after O-free subtargets fail cleanly or require projection")
    with out.counterexamples():
        out.line("O by frustration", StatusMark.FAIL, "hard route is not proof that O is necessary")
        out.line("O by label", StatusMark.FAIL, "active O remains unconstructed")
        out.line("O as repair", StatusMark.FAIL, "projection cannot be repair paint")

    record_marker(ns, MARKER_ID, "active-O gate audit; O not forced")
    record_claim(ns, MARKER_ID, "g74_O_c1", GovernanceStatus.POLICY_RULE, "Active O is not forced while O-free subtargets remain unresolved rather than exhausted.")
    record_claim(ns, MARKER_ID, "g74_O_c2", GovernanceStatus.REJECTED_ROUTE, "Active O by frustration, label, or repair is rejected.")
    record_obligation(ns, "g74_O_o1", "Revisit active O only after clean O-free obstruction or separate construction burden.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_parent_recombination_gate.py")

if __name__ == "__main__":
    main()
