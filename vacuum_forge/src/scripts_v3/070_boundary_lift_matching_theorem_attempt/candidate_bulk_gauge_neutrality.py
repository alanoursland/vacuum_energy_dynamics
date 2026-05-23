
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
    ("g69_summary", "069_boundary_covariant_cancellation_attempt__candidate_group_69_status_summary", "g69_summary"),
    ("g70_coefficients", "070_boundary_lift_matching_theorem_attempt__candidate_component_coefficient_matching", "g70_coefficients"),
]
MARKER_ID = "g70_bulk_gauge"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    L_bulk, L_gauge = sp.symbols("L_bulk L_gauge")
    residual_after_boundary_match = sp.simplify(L_bulk + L_gauge)
    independent_solution = sp.solve([sp.Eq(sp.diff(residual_after_boundary_match, L_bulk), 0),
                                     sp.Eq(sp.diff(residual_after_boundary_match, L_gauge), 0)], [L_bulk, L_gauge], dict=True)

    header("Candidate Bulk/Gauge Neutrality")
    print(f"residual after boundary matching = {residual_after_boundary_match}")
    print("For independent L_bulk and L_gauge, identity requires separate neutrality theorems:")
    print("  L_bulk = 0")
    print("  L_gauge = 0")
    with out.derived_results():
        out.line("post-match residual", StatusMark.PASS, str(residual_after_boundary_match))
    with out.unresolved_obligations():
        out.line("bulk lift neutrality", StatusMark.OBLIGATION, "derive L_bulk=0")
        out.line("gauge neutrality", StatusMark.OBLIGATION, "derive L_gauge=0")
    with out.counterexamples():
        out.line("drop bulk/gauge", StatusMark.FAIL, "dropping L_bulk or L_gauge by prose is not a theorem")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=residual_after_boundary_match,
        method="record residual remaining after boundary anti-match",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="bulk_gauge_neutrality_conditions",
        scope="neutrality requirements; not lift theorem",
    )
    record_claim(ns, MARKER_ID, "g70_bulk_gauge_c1", GovernanceStatus.POLICY_RULE, "Boundary matching still requires L_bulk=0 and L_gauge=0.")
    record_obligation(ns, "g70_bulk_gauge_o1", "Derive bulk and gauge neutrality as covariant lift theorems.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_matching_vs_repair_discriminator.py")

if __name__ == "__main__":
    main()
