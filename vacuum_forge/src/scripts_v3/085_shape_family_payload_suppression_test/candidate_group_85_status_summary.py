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
    ("g84_summary", "084_local_rho_inertness_test__candidate_group_84_status_summary", "g84_summary"),
    ("g85_problem", "085_shape_family_payload_suppression_test__candidate_shape_suppression_problem", "g85_problem"),
    ("g85_even_quartic_family", "085_shape_family_payload_suppression_test__candidate_even_quartic_shape_family", "g85_even_quartic_family"),
    ("g85_moment_solver", "085_shape_family_payload_suppression_test__candidate_moment_constraint_solver", "g85_moment_solver"),
    ("g85_profile_validation", "085_shape_family_payload_suppression_test__candidate_suppressed_profile_validation", "g85_profile_validation"),
    ("g85_weighted_extension", "085_shape_family_payload_suppression_test__candidate_weighted_payload_extension", "g85_weighted_extension"),
    ("g85_admissibility", "085_shape_family_payload_suppression_test__candidate_shape_admissibility_and_repair_discriminator", "g85_admissibility"),
    ("g85_route_classifier", "085_shape_family_payload_suppression_test__candidate_shape_suppression_route_classifier", "g85_route_classifier"),
]
MARKER_ID = "g85_summary"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Group 85 Status Summary")
    print("Question: Can a richer exactness shape suppress low-order local payload moments?")
    print("Group 85 stable result:")
    print("  even quartic shape family tested")
    print("  P=1-12y^2+51y^4 found from M2=M4 constraints")
    print("  profile is regular/positive on [-1,1]")
    print("  endpoint compact flux retained")
    print("  M0..M5 vanish")
    print("  W0..W3 vanish under quadratic measure")
    print("  local rho remains nonzero")
    print("  M6 and W4 remain nonzero")
    print("  Group 84 linear-skew obstruction is not universal")
    print("  shape origin remains open")
    print("  full local inertness not proven")
    print("  parent divergence identity remains unproven")
    print("  recombination remains blocked")

    with out.governance_assessments():
        out.line("shape family", StatusMark.PASS, "richer shape family tested")
        out.line("profile found", StatusMark.PASS, "P=1-12y^2+51y^4")
        out.line("flat moments", StatusMark.PASS, "M0..M5 vanish")
        out.line("weighted moments", StatusMark.PASS, "W0..W3 vanish")
        out.line("higher obstruction", StatusMark.WARN, "M6/W4 remain")
        out.line("local rho", StatusMark.WARN, "rho remains nonzero")
        out.line("shape origin", StatusMark.OBLIGATION, "shape origin remains open")
        out.line("full inertness", StatusMark.DEFER, "full local inertness not proven")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "recombination remains blocked")
    with out.counterexamples():
        out.line("linear obstruction universal", StatusMark.FAIL, "even quartic family suppresses low-order payload")
        out.line("all-order inertness", StatusMark.FAIL, "higher moments remain")
        out.line("shape as physical derivation", StatusMark.FAIL, "moment-derived shape not yet geometrically derived")
        out.line("parent equation", StatusMark.FAIL, "parent construction remains forbidden")
    with out.unresolved_obligations():
        out.line("shape origin", StatusMark.OBLIGATION, "derive the profile from geometry/variational principle")
        out.line("higher moments", StatusMark.OBLIGATION, "test moment hierarchy or richer profiles")
        out.line("covariant lift", StatusMark.OBLIGATION, "lift finite-mode suppression covariantly")

    print("\nRecommended next routes:")
    print("  86_shape_origin_geometry_derivation")
    print("  86_moment_hierarchy_closure_test")
    print("  86_covariant_payload_suppression_lift")
    print("  86_payload_projection_operator_necessity")
    print("  86_parent_blocker_refresh")

    record_marker(ns, MARKER_ID, "Group 85 summary; even quartic payload suppression")
    record_claim(ns, MARKER_ID, "g85_summary_c1", GovernanceStatus.POLICY_RULE, "Group 85 finds an even quartic exactness profile suppressing low-order flat and weighted payload moments.")
    record_claim(ns, MARKER_ID, "g85_summary_c2", GovernanceStatus.POLICY_RULE, "Suppression is finite-mode and reduced-class; shape origin and higher/covariant inertness remain open.")
    record_obligation(ns, "g85_summary_o1", "Derive shape origin from geometry or test moment hierarchy.")
    record_obligation(ns, "g85_summary_o2", "Parent divergence identity remains unproven.")
    ns.write_run_metadata()

if __name__ == "__main__":
    main()
