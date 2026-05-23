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
    print(); print("=" * 120); print(title); print("=" * 120)


def prepare_archive(dependencies):
    archive = ProjectArchive(ARCHIVE_ROOT); ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    for dep_id, upstream_script_id, upstream_derivation_id in dependencies:
        ns.declare_dependency(dependency_id=dep_id, upstream_script_id=upstream_script_id, upstream_derivation_id=upstream_derivation_id)
    return archive, ns, invalidated


def print_archive_status(ns, invalidated: bool) -> None:
    if invalidated: print("[INFO] Archive invalidated due to source change.")
    checks = ns.verify_dependencies()
    if not checks:
        print("[INFO] Archive dependencies: none declared."); return
    print("[INFO] Archive dependency check:")
    for check in checks: print(f"  - {check.dependency.dependency_id}: {check.status} ({check.message})")


def record_marker(ns, marker_id: str, scope: str) -> None:
    ns.record_derivation(derivation_id=marker_id, inputs=[], output=sp.Symbol(marker_id), method="Group 73 summary marker; no physical derivation", status=Status.DERIVED, record_kind=RecordKind.INVENTORY_MARKER, is_placeholder=True, scope=scope)


def record_claim(ns, marker_id: str, claim_id: str, status: GovernanceStatus, statement: str) -> None:
    ns.record_claim(ClaimRecord(claim_id=claim_id, script_id=SCRIPT_ID, claim_kind=RecordKind.GOVERNANCE_CLAIM, tier=ClaimTier.CONSTRAINED, status=status, statement=statement, derivation_ids=[marker_id], obligation_ids=[]))


def record_obligation(ns, obligation_id: str, statement: str, status: ObligationStatus = ObligationStatus.OPEN) -> None:
    ns.record_obligation(ProofObligationRecord(obligation_id=obligation_id, script_id=SCRIPT_ID, title=obligation_id, status=status, required_by=[SCRIPT_ID], description=statement))


DEPENDENCIES = [
    ("g72_summary", "072_layer_term_legitimacy_audit__candidate_group_72_status_summary", "g72_summary"),
    ("g73_problem", "073_layer_generator_construction__candidate_layer_generator_problem", "g73_problem"),
    ("g73_requirements", "073_layer_generator_construction__candidate_geometric_layer_generator_requirements", "g73_requirements"),
    ("g73_signed_distance", "073_layer_generator_construction__candidate_signed_distance_layer_scaffold", "g73_signed_distance"),
    ("g73_measure_origin", "073_layer_generator_construction__candidate_boundary_measure_origin_test", "g73_measure_origin"),
    ("g73_component_membership", "073_layer_generator_construction__candidate_component_membership_origin_test", "g73_component_membership"),
    ("g73_payload_purity", "073_layer_generator_construction__candidate_payload_purity_and_role_test", "g73_payload_purity"),
    ("g73_lift_interface", "073_layer_generator_construction__candidate_boundary_lift_interface_test", "g73_lift_interface"),
    ("g73_route_classifier", "073_layer_generator_construction__candidate_layer_generator_route_classifier", "g73_route_classifier"),
]
MARKER_ID = "g73_summary"


def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES); print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Group 73 Status Summary")
    print("Question:")
    print("  Can D_layer be derived from a legitimate geometric layer generator?")
    print()
    print("Group 73 stable result:")
    print("  legal geometric D_layer criteria explicit")
    print("  signed-distance / layer support scaffold constructed")
    print("  boundary/layer measure scaffold constructed")
    print("  component membership requirements explicit")
    print("  source/trace/mass/repair/active-O payload routes rejected")
    print("  boundary-lift interface remains conditional")
    print("  geometric D_layer generator not derived")
    print("  D_layer legitimacy remains unresolved")
    print("  L_bulk and L_gauge remain lift-cleanliness obligations")
    print("  parent divergence identity remains unproven")
    print("  recombination remains blocked")

    with out.governance_assessments():
        out.line("criteria", StatusMark.PASS, "legal geometric D_layer criteria stated")
        out.line("scaffolds", StatusMark.INFO, "signed-distance and measure scaffolds constructed as theorem inputs")
        out.line("payload rejection", StatusMark.PASS, "source/trace/mass/repair/active-O payload routes rejected")
        out.line("D_layer generator", StatusMark.OBLIGATION, "geometric D_layer generator not derived")
        out.line("boundary-lift interface", StatusMark.INFO, "anti-match interface remains conditional on D_layer and lift neutrality")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "parent recombination remains blocked")
    with out.counterexamples():
        out.line("diagnostic layer", StatusMark.FAIL, "eta/eta^2/N_w/R1/R2 cannot be promoted to D_layer")
        out.line("support as theorem", StatusMark.FAIL, "endpoint/locality/measure checks do not prove physical D_layer")
        out.line("payload layer", StatusMark.FAIL, "D_layer cannot carry source, trace, mass, repair, or active-O payload")
        out.line("parent equation", StatusMark.FAIL, "parent construction remains forbidden")
    with out.unresolved_obligations():
        out.line("geometric D_layer origin", StatusMark.OBLIGATION, "derive D_layer from boundary/layer geometry or route-manage obstruction")
        out.line("component membership", StatusMark.OBLIGATION, "derive D_layer membership in common boundary object")
        out.line("lift cleanliness", StatusMark.OBLIGATION, "L_bulk/L_gauge remain separate obligations")

    print("\nRecommended next routes:")
    print("  route-management fallback: 74_boundary_lift_route_split_decision")
    print("  if continuing constructive layer route: 74_layer_geometry_axiom_inventory or generator construction with a concrete geometry")
    print("  if lift terms become priority: 74_covariant_lift_neutrality_attempt")
    print("  active O only later: 74_active_O_necessity_or_rejection, if O-free routes fail cleanly")

    record_marker(ns, MARKER_ID, "Group 73 summary; no parent equation")
    record_claim(ns, MARKER_ID, "g73_summary_c1", GovernanceStatus.POLICY_RULE, "Group 73 constructs scaffolds but does not derive a geometric D_layer generator.")
    record_claim(ns, MARKER_ID, "g73_summary_c2", GovernanceStatus.REJECTED_ROUTE, "Diagnostic transition, support-as-theorem, payload, active-O, and parent-construction routes are rejected.")
    record_obligation(ns, "g73_summary_o1", "Route-manage D_layer obstruction or provide concrete geometry for next construction attempt.")
    record_obligation(ns, "g73_summary_o2", "Parent divergence identity remains unproven.")
    ns.write_run_metadata()


if __name__ == "__main__": main()
