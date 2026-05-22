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
    ("g85_summary", "85_shape_family_payload_suppression_test__candidate_group_85_status_summary", "g85_summary"),
    ("g86_problem", "86_shape_origin_geometry_derivation__candidate_shape_origin_problem", "g86_problem"),
    ("g86_moment_map", "86_shape_origin_geometry_derivation__candidate_moment_map_from_shape_coefficients", "g86_moment_map"),
    ("g86_minimal_degree", "86_shape_origin_geometry_derivation__candidate_minimal_degree_obstruction", "g86_minimal_degree"),
    ("g86_quartic_uniqueness", "86_shape_origin_geometry_derivation__candidate_quartic_uniqueness_theorem", "g86_quartic_uniqueness"),
    ("g86_payload_action", "86_shape_origin_geometry_derivation__candidate_payload_action_minimizer", "g86_payload_action"),
    ("g86_weighted_consistency", "86_shape_origin_geometry_derivation__candidate_weighted_consistency_from_flat_block", "g86_weighted_consistency"),
    ("g86_route_classifier", "86_shape_origin_geometry_derivation__candidate_shape_origin_route_classifier", "g86_route_classifier"),
]
MARKER_ID = "g86_summary"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Group 86 Status Summary")
    print("Question: Was the quartic profile structurally forced inside the reduced payload-suppression problem?")
    print("Group 86 stable result:")
    print("  moment map from even shape coefficients to payload moments derived")
    print("  degree 0 and degree 2 obstruction derived")
    print("  degree 4 is minimal for killing M2 and M4")
    print("  P=1-12y^2+51y^4 uniquely derived in normalized even quartic family")
    print("  same P is unique zero-action minimizer of A=M2^2+M4^2")
    print("  W0..W3 weighted suppression follows from M0..M5 flat moment block")
    print("  shape origin strengthened inside reduced model")
    print("  full physical/covariant origin remains open")
    print("  local rho nonzero remains")
    print("  higher moments M6/W4 remain")
    print("  parent divergence identity remains unproven")
    print("  recombination remains blocked")

    with out.governance_assessments():
        out.line("reduced origin", StatusMark.PASS, "shape has minimal-degree and variational origin inside reduced model")
        out.line("minimal degree", StatusMark.PASS, "degree 4 minimal")
        out.line("quartic uniqueness", StatusMark.PASS, "unique normalized even quartic")
        out.line("payload action", StatusMark.PASS, "zero-action minimizer")
        out.line("weighted consistency", StatusMark.PASS, "W0..W3 follows from M0..M5")
        out.line("full origin", StatusMark.OBLIGATION, "physical/covariant origin remains open")
        out.line("local rho", StatusMark.WARN, "local rho nonzero remains")
        out.line("higher moments", StatusMark.WARN, "M6/W4 remain")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "recombination remains blocked")
    with out.counterexamples():
        out.line("arbitrary profile", StatusMark.FAIL, "not arbitrary inside reduced model")
        out.line("full geometry", StatusMark.FAIL, "reduced origin is not full covariant geometry")
        out.line("full inertness", StatusMark.FAIL, "higher moments/local rho remain")
        out.line("parent equation", StatusMark.FAIL, "parent construction remains forbidden")
    with out.unresolved_obligations():
        out.line("physical origin", StatusMark.OBLIGATION, "derive payload action/shape from geometry or physical principle")
        out.line("moment hierarchy", StatusMark.OBLIGATION, "test higher-degree moment hierarchy")
        out.line("covariant lift", StatusMark.OBLIGATION, "lift reduced shape-origin result")

    print("\nRecommended next routes:")
    print("  87_moment_hierarchy_closure_test")
    print("  87_covariant_payload_suppression_lift")
    print("  87_shape_variational_physical_origin")
    print("  87_payload_projection_operator_necessity")
    print("  87_parent_blocker_refresh")

    record_marker(ns, MARKER_ID, "Group 86 summary; reduced structural origin for quartic profile")
    record_claim(ns, MARKER_ID, "g86_summary_c1", GovernanceStatus.POLICY_RULE, "Group 86 derives a reduced structural origin for P=1-12y^2+51y^4.")
    record_claim(ns, MARKER_ID, "g86_summary_c2", GovernanceStatus.POLICY_RULE, "The result is reduced-class only; physical/covariant origin, higher moments, and local inertness remain open.")
    record_obligation(ns, "g86_summary_o1", "Test moment hierarchy or derive physical/covariant origin next.")
    record_obligation(ns, "g86_summary_o2", "Parent divergence identity remains unproven.")
    ns.write_run_metadata()

if __name__ == "__main__":
    main()
