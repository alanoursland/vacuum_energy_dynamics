
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
    ("g70_common_generator", "70_boundary_lift_matching_theorem_attempt__candidate_common_generator_ansatz", "g70_common_generator"),
    ("g70_orientation", "70_boundary_lift_matching_theorem_attempt__candidate_orientation_sign_sieve", "g70_orientation"),
    ("g70_coefficients", "70_boundary_lift_matching_theorem_attempt__candidate_component_coefficient_matching", "g70_coefficients"),
    ("g70_bulk_gauge", "70_boundary_lift_matching_theorem_attempt__candidate_bulk_gauge_neutrality", "g70_bulk_gauge"),
    ("g70_discriminator", "70_boundary_lift_matching_theorem_attempt__candidate_matching_vs_repair_discriminator", "g70_discriminator"),
]
MARKER_ID = "g70_class"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Theorem Burden Classifier")
    with out.governance_assessments():
        out.line("compatibility derived", StatusMark.PASS, "sigma=1, all coefficients=-1, and L_bulk=L_gauge=0 are sufficient conditions")
        out.line("theorem status", StatusMark.OBLIGATION, "boundary-lift matching theorem is not proven")
        out.line("parent divergence status", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "parent recombination remains blocked")
        out.line("next route", StatusMark.INFO, "71_common_boundary_generator_search")
    with out.counterexamples():
        out.line("chosen values", StatusMark.FAIL, "choosing sigma or coefficients is repair-like")
        out.line("bulk/gauge omission", StatusMark.FAIL, "omitting L_bulk/L_gauge is not covariant lift proof")
    with out.unresolved_obligations():
        out.line("common generator", StatusMark.OBLIGATION, "find or reject common generator that derives the required anti-match")
        out.line("bulk/gauge lift", StatusMark.OBLIGATION, "prove L_bulk=0 and L_gauge=0")

    record_marker(ns, MARKER_ID, "Group 70 classifier; no parent equation")
    record_claim(ns, MARKER_ID, "g70_class_c1", GovernanceStatus.POLICY_RULE, "Group 70 derives compatibility requirements but not the boundary-lift matching theorem.")
    record_claim(ns, MARKER_ID, "g70_class_c2", GovernanceStatus.REJECTED_ROUTE, "Repair-style choices are rejected.")
    record_obligation(ns, "g70_class_o1", "Search for a common boundary generator next.")
    record_obligation(ns, "g70_class_o2", "Parent divergence identity remains unproven.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_group_70_status_summary.py")

if __name__ == "__main__":
    main()
