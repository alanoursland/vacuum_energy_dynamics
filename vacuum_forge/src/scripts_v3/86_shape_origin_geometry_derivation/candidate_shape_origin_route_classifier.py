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
    ("g86_moment_map", "86_shape_origin_geometry_derivation__candidate_moment_map_from_shape_coefficients", "g86_moment_map"),
    ("g86_minimal_degree", "86_shape_origin_geometry_derivation__candidate_minimal_degree_obstruction", "g86_minimal_degree"),
    ("g86_quartic_uniqueness", "86_shape_origin_geometry_derivation__candidate_quartic_uniqueness_theorem", "g86_quartic_uniqueness"),
    ("g86_payload_action", "86_shape_origin_geometry_derivation__candidate_payload_action_minimizer", "g86_payload_action"),
    ("g86_weighted_consistency", "86_shape_origin_geometry_derivation__candidate_weighted_consistency_from_flat_block", "g86_weighted_consistency"),
]
MARKER_ID = "g86_route_classifier"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    classifications = [
        ("MOMENT_MAP_DERIVED", "stable", "shape coefficients map linearly to payload moments"),
        ("MINIMAL_DEGREE_ORIGIN_DERIVED", "stable", "degree 4 is minimal for M2/M4 suppression"),
        ("QUARTIC_UNIQUENESS_DERIVED", "stable", "P=1-12y^2+51y^4 unique in normalized even quartic family"),
        ("LOW_ORDER_PAYLOAD_ACTION_MINIMIZER_DERIVED", "stable", "same P minimizes A=M2^2+M4^2 with A=0"),
        ("WEIGHTED_SUPPRESSION_FOLLOWS_FROM_FLAT_BLOCK", "stable", "W0..W3 follow from M0..M5 for quadratic measure"),
        ("SHAPE_ORIGIN_STRENGTHENED_IN_REDUCED_MODEL", "stable", "profile is structurally forced inside reduced problem"),
        ("FULL_GEOMETRIC_ORIGIN_OPEN", "stable", "physical/covariant origin of the reduced action remains open"),
        ("LOCAL_RHO_NONZERO_REMAINS", "stable", "Group 85 rho remains pointwise nonzero"),
        ("HIGHER_MOMENTS_REMAIN", "stable", "M6/W4 remain from Group 85"),
        ("PARENT_DIVERGENCE_UNPROVEN", "stable", "parent identity remains blocked"),
        ("RECOMBINATION_BLOCKED", "stable", "no recombination license"),
    ]

    header("Candidate Shape Origin Route Classifier")
    for name, status, reason in classifications:
        print(f"{name}: {status}; {reason}")

    with out.governance_assessments():
        out.line("moment map", StatusMark.PASS, "derived")
        out.line("minimal degree", StatusMark.PASS, "derived")
        out.line("quartic uniqueness", StatusMark.PASS, "derived")
        out.line("payload action", StatusMark.PASS, "zero-action minimizer derived")
        out.line("weighted consistency", StatusMark.PASS, "weighted suppression follows from flat block")
        out.line("reduced origin", StatusMark.PASS, "shape origin strengthened inside reduced model")
        out.line("full origin", StatusMark.OBLIGATION, "physical/covariant origin remains open")
        out.line("local rho", StatusMark.WARN, "local rho nonzero remains")
        out.line("higher moments", StatusMark.WARN, "higher moments remain")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "recombination remains blocked")
    with out.counterexamples():
        out.line("profile arbitrary inside reduced model", StatusMark.FAIL, "minimal degree and action minimizer force profile")
        out.line("reduced origin as full physics", StatusMark.FAIL, "physical/covariant origin remains open")
        out.line("full inertness", StatusMark.FAIL, "local rho and higher moments remain")
        out.line("parent equation", StatusMark.FAIL, "parent construction remains forbidden")
    with out.unresolved_obligations():
        out.line("physical action", StatusMark.OBLIGATION, "derive reduced payload action from geometry/physics")
        out.line("moment hierarchy", StatusMark.OBLIGATION, "test higher-degree hierarchy")
        out.line("covariant lift", StatusMark.OBLIGATION, "lift shape-origin result covariantly")

    record_marker(ns, MARKER_ID, "shape-origin route classifier")
    record_claim(ns, MARKER_ID, "g86_class_c1", GovernanceStatus.POLICY_RULE, "Group 86 derives a reduced structural origin for the Group 85 suppression profile.")
    record_claim(ns, MARKER_ID, "g86_class_c2", GovernanceStatus.POLICY_RULE, "Full physical/covariant origin and full inertness remain open.")
    record_obligation(ns, "g86_class_o1", "Derive physical origin of the reduced payload action or test moment hierarchy.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_group_86_status_summary.py")

if __name__ == "__main__":
    main()
