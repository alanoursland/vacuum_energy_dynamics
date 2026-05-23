
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
    ("g70_problem", "070_boundary_lift_matching_theorem_attempt__candidate_matching_problem", "g70_problem"),
    ("g70_common_generator", "070_boundary_lift_matching_theorem_attempt__candidate_common_generator_ansatz", "g70_common_generator"),
    ("g70_orientation", "070_boundary_lift_matching_theorem_attempt__candidate_orientation_sign_sieve", "g70_orientation"),
    ("g70_coefficients", "070_boundary_lift_matching_theorem_attempt__candidate_component_coefficient_matching", "g70_coefficients"),
    ("g70_bulk_gauge", "070_boundary_lift_matching_theorem_attempt__candidate_bulk_gauge_neutrality", "g70_bulk_gauge"),
    ("g70_discriminator", "070_boundary_lift_matching_theorem_attempt__candidate_matching_vs_repair_discriminator", "g70_discriminator"),
    ("g70_class", "070_boundary_lift_matching_theorem_attempt__candidate_theorem_burden_classifier", "g70_class"),
]
MARKER_ID = "g70_summary"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Group 70 Status Summary")
    print("Question:")
    print("  Did Group 70 prove the boundary-lift matching theorem?")
    with out.governance_assessments():
        out.line("compatibility conditions", StatusMark.PASS, "required matching conditions derived")
        out.line("sigma requirement", StatusMark.PASS, "sigma=1 required")
        out.line("coefficient requirement", StatusMark.PASS, "a_jump=a_layer=a_tail=-1 required")
        out.line("bulk/gauge requirement", StatusMark.OBLIGATION, "L_bulk=0 and L_gauge=0 still require theorem")
        out.line("matching theorem", StatusMark.OBLIGATION, "boundary-lift matching theorem not proven")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "parent recombination remains blocked")
        out.line("next group", StatusMark.INFO, "071_common_boundary_generator_search")
    with out.counterexamples():
        out.line("chosen sign", StatusMark.FAIL, "sigma=1 cannot be selected by convenience")
        out.line("chosen coefficients", StatusMark.FAIL, "coefficients cannot be selected by repair")
        out.line("diagnostic layer", StatusMark.FAIL, "diagnostic transition cannot be inserted as D_layer")

    print()
    print("Compatibility requirements:")
    print("  sigma = 1")
    print("  a_jump = -1")
    print("  a_layer = -1")
    print("  a_tail = -1")
    print("  L_bulk = 0")
    print("  L_gauge = 0")
    print()
    print("Status:")
    print("  compatibility shown; theorem not proven")
    print("  parent divergence identity remains unproven")
    print("  parent recombination remains blocked")
    print()
    print("Recommended next group:")
    print("  71_common_boundary_generator_search")

    record_marker(ns, MARKER_ID, "Group 70 summary; no parent equation")
    record_claim(ns, MARKER_ID, "g70_summary_c1", GovernanceStatus.POLICY_RULE, "Boundary-lift matching compatibility requirements are explicit but not derived as theorem.")
    record_claim(ns, MARKER_ID, "g70_summary_c2", GovernanceStatus.REJECTED_ROUTE, "Choosing signs/coefficients or inserting diagnostic layer is rejected.")
    record_obligation(ns, "g70_summary_o1", "Search for common boundary generator next.")
    record_obligation(ns, "g70_summary_o2", "Parent divergence identity remains unproven.")
    ns.write_run_metadata()

if __name__ == "__main__":
    main()
