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
    ns.record_derivation(derivation_id=marker_id, inputs=[], output=sp.Symbol(marker_id), method="route classifier marker; no physical derivation", status=Status.DERIVED, record_kind=RecordKind.INVENTORY_MARKER, is_placeholder=True, scope=scope)


def record_claim(ns, marker_id: str, claim_id: str, status: GovernanceStatus, statement: str) -> None:
    ns.record_claim(ClaimRecord(claim_id=claim_id, script_id=SCRIPT_ID, claim_kind=RecordKind.GOVERNANCE_CLAIM, tier=ClaimTier.CONSTRAINED, status=status, statement=statement, derivation_ids=[marker_id], obligation_ids=[]))


def record_obligation(ns, obligation_id: str, statement: str, status: ObligationStatus = ObligationStatus.OPEN) -> None:
    ns.record_obligation(ProofObligationRecord(obligation_id=obligation_id, script_id=SCRIPT_ID, title=obligation_id, status=status, required_by=[SCRIPT_ID], description=statement))


DEPENDENCIES = [
    ("g73_signed_distance", "073_layer_generator_construction__candidate_signed_distance_layer_scaffold", "g73_signed_distance"),
    ("g73_measure_origin", "073_layer_generator_construction__candidate_boundary_measure_origin_test", "g73_measure_origin"),
    ("g73_component_membership", "073_layer_generator_construction__candidate_component_membership_origin_test", "g73_component_membership"),
    ("g73_payload_purity", "073_layer_generator_construction__candidate_payload_purity_and_role_test", "g73_payload_purity"),
    ("g73_lift_interface", "073_layer_generator_construction__candidate_boundary_lift_interface_test", "g73_lift_interface"),
]
MARKER_ID = "g73_route_classifier"


def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES); print_archive_status(ns, invalidated)
    out = ScriptOutput()

    statuses = [
        ("GEOMETRIC_LAYER_GENERATOR_DERIVED", "not established"),
        ("GEOMETRIC_LAYER_SCAFFOLD_RETAINED", "conditional; signed-distance and measure scaffolds can constrain future theorem"),
        ("D_LAYER_LEGITIMACY_NOT_ESTABLISHED", "stable; no script derives physical/covariant D_layer origin"),
        ("DIAGNOSTIC_TRANSITION_REMAINS_EXCLUDED", "stable; old diagnostics cannot supply D_layer"),
        ("PAYLOAD_ROUTES_REJECTED", "stable; source/trace/mass/repair/active-O payloads rejected"),
        ("BOUNDARY_LIFT_INTERFACE_PARTIAL", "conditional; interface algebra works only if D_layer_geo and lift neutrality are derived"),
        ("PARENT_DIVERGENCE_UNPROVEN", "stable"),
        ("RECOMBINATION_BLOCKED", "stable"),
    ]

    header("Candidate Layer Generator Route Classifier")
    print("Final route classification from Group 73 tests:")
    for name, status in statuses:
        print(f"  {name}: {status}")
    print()
    print("Reason:")
    print("  Signed-distance and boundary-measure scaffolds can organize layer locality and measure constraints.")
    print("  But Group 73 does not derive a physical/covariant generator that supplies D_layer.")
    print("  Component membership, payload purity, and lift cleanliness remain theorem burdens.")

    with out.governance_assessments():
        out.line("strong generator", StatusMark.OBLIGATION, "geometric D_layer generator not derived")
        out.line("scaffold", StatusMark.INFO, "layer-coordinate and measure scaffolds retained only as theorem inputs")
        out.line("controlled obstruction", StatusMark.PASS, "failure mode localized to D_layer origin, membership, payload purity, and lift interface")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "parent recombination remains blocked")
    with out.counterexamples():
        out.line("diagnostic transition", StatusMark.FAIL, "old diagnostic transition response cannot supply D_layer")
        out.line("payload D_layer", StatusMark.FAIL, "source/trace/mass/repair/active-O payload routes rejected")
        out.line("support as theorem", StatusMark.FAIL, "locality/measure checks alone are not legitimacy")
    with out.unresolved_obligations():
        out.line("geometric D_layer origin", StatusMark.OBLIGATION, "derive or reject physical/covariant layer generator")
        out.line("component membership", StatusMark.OBLIGATION, "derive D_layer membership in common boundary object")
        out.line("lift cleanliness", StatusMark.OBLIGATION, "derive L_bulk/L_gauge neutrality separately")

    record_marker(ns, MARKER_ID, "Group 73 route classifier; no parent equation")
    record_claim(ns, MARKER_ID, "g73_classifier_c1", GovernanceStatus.POLICY_RULE, "Group 73 retains layer scaffolds only as theorem inputs; it does not derive a geometric D_layer generator.")
    record_claim(ns, MARKER_ID, "g73_classifier_c2", GovernanceStatus.REJECTED_ROUTE, "Diagnostic transition, forbidden payloads, and support-as-theorem routes are rejected.")
    record_obligation(ns, "g73_classifier_o1", "Derive or route-manage geometric D_layer origin.")
    record_obligation(ns, "g73_classifier_o2", "Parent divergence identity remains unproven.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_group_73_status_summary.py")


if __name__ == "__main__": main()
