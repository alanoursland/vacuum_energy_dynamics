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
    ("g78_repetition_sieve", "078_boundary_lift_split_obligation_ledger__candidate_repetition_risk_sieve", "g78_repetition_sieve"),
]
MARKER_ID = "g78_active_O_gate"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    unresolved_o_free = {
        "D_layer_legitimacy": "open_not_impossible",
        "L_bulk_neutrality": "open_not_impossible",
        "L_gauge_neutrality": "open_not_impossible",
        "rho_status": "open_not_impossible",
        "common_generator_origin": "open_not_impossible",
    }
    clean_exhaustion = False
    projection_required = False
    active_O_forced = clean_exhaustion and projection_required

    header("Candidate Active-O Threshold Gate")
    print("O-free split targets:")
    for k, v in unresolved_o_free.items():
        print(f"  {k}: {v}")
    print(f"clean O-free exhaustion = {clean_exhaustion}")
    print(f"projection structurally required = {projection_required}")
    print(f"active O forced now = {active_O_forced}")

    with out.governance_assessments():
        out.line("O-free state", StatusMark.INFO, "targets unresolved but not cleanly impossible")
        out.line("active O", StatusMark.DEFER, "active O not forced now")
        out.line("future O audit", StatusMark.OBLIGATION, "only after clean exhaustion or projection requirement")
    with out.counterexamples():
        out.line("O by frustration", StatusMark.FAIL, "difficulty is not projection theorem")
        out.line("O by label", StatusMark.FAIL, "active O remains unconstructed")
        out.line("O as repair", StatusMark.FAIL, "projection cannot be repair paint")

    record_marker(ns, MARKER_ID, "active-O threshold gate; no active O construction")
    record_claim(ns, MARKER_ID, "g78_activeO_c1", GovernanceStatus.POLICY_RULE, "Active O is not forced by current split-obligation state.")
    record_obligation(ns, "g78_activeO_o1", "Revisit active O only after clean O-free exhaustion or projection requirement.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_next_work_selector.py")

if __name__ == "__main__":
    main()
