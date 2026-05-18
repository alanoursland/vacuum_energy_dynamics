
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
    ("g69_summary", "69_boundary_covariant_cancellation_attempt__candidate_group_69_status_summary", "g69_summary"),
    ("g70_problem", "70_boundary_lift_matching_theorem_attempt__candidate_matching_problem", "g70_problem"),
]
MARKER_ID = "g70_common_generator"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    D_jump, D_layer, D_tail, L_bulk, L_gauge, sigma = sp.symbols("D_jump D_layer D_tail L_bulk L_gauge sigma")
    B = sp.simplify(D_jump + D_layer + D_tail)
    L_boundary = sp.simplify(-sigma * B)
    residual = sp.simplify(L_bulk + L_boundary + L_gauge + B)

    header("Candidate Common Generator Ansatz")
    print(f"B = {B}")
    print(f"L_boundary = {L_boundary}")
    print(f"O-free residual = {residual}")
    with out.derived_results():
        out.line("common boundary generator", StatusMark.PASS, f"B={B}")
        out.line("anti-match ansatz", StatusMark.PASS, f"L_boundary={L_boundary}")
        out.line("residual under ansatz", StatusMark.PASS, str(residual))
    with out.unresolved_obligations():
        out.line("derive sigma", StatusMark.OBLIGATION, "sigma must be derived from orientation/common geometry")
        out.line("derive bulk/gauge neutrality", StatusMark.OBLIGATION, "L_bulk=0 and L_gauge=0 still required")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=residual,
        method="substitute common-generator anti-match ansatz into O-free residual",
        status=Status.DERIVED,
        record_kind=RecordKind.COMPATIBILITY_EXAMPLE,
        result_type="common_generator_matching_ansatz",
        scope="compatibility ansatz; not matching theorem",
    )
    record_claim(ns, MARKER_ID, "g70_common_c1", GovernanceStatus.POLICY_RULE, "Common-generator ansatz reduces matching to sigma and bulk/gauge burdens.")
    record_obligation(ns, "g70_common_o1", "Derive sigma=1 from orientation/common geometry.")
    record_obligation(ns, "g70_common_o2", "Derive L_bulk=0 and L_gauge=0.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_orientation_sign_sieve.py")

if __name__ == "__main__":
    main()
