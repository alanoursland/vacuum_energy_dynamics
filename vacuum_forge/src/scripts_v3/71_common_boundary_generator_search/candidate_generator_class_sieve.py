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
        method="generator class sieve marker; no physical derivation",
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
    ("g71_orientation", "71_common_boundary_generator_search__candidate_orientation_forcing_test", "g71_orientation_forcing"),
    ("g71_components", "71_common_boundary_generator_search__candidate_component_forcing_test", "g71_component_forcing"),
    ("g71_bulk_gauge", "71_common_boundary_generator_search__candidate_bulk_gauge_leakage_test", "g71_bulk_gauge_leakage"),
]
MARKER_ID = "g71_class_sieve"


def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    classes = [
        (
            "pure_common_boundary_generator",
            "conditional_retained",
            "would force D_boundary=+B and L_boundary=-B if B is a real boundary object; bulk/gauge remain separate obligations",
        ),
        (
            "boundary_plus_lift_boundary_generator",
            "partial_retained",
            "can express anti-match but must prove orientation and component membership from shared geometry",
        ),
        (
            "renamed_B_only",
            "rejected",
            "B with a hat does not explain why lift side is the opposite orientation",
        ),
        (
            "free_coefficient_generator",
            "rejected",
            "works only by choosing sigma or component coefficients",
        ),
        (
            "bulk_contaminated_generator",
            "blocked_or_deferred",
            "introduces L_bulk unless separate lift theorem neutralizes it",
        ),
        (
            "gauge_contaminated_generator",
            "blocked_or_deferred",
            "introduces L_gauge unless separate gauge theorem neutralizes it",
        ),
        (
            "layer_dependent_generator",
            "dangerous_partial",
            "requires D_layer legitimacy and must not import diagnostic transition response",
        ),
        (
            "repair_current_generator",
            "rejected",
            "cancels residual after the fact rather than generating paired orientations",
        ),
        (
            "active_O_generator",
            "rejected_here",
            "projection-like object is outside Group 71 unless fully constructed elsewhere",
        ),
    ]

    header("Candidate Generator Class Sieve")
    for name, status, reason in classes:
        print(f"{name}: {status}; {reason}")

    with out.governance_assessments():
        out.line("pure common generator", StatusMark.INFO, "retained only as theorem route if real geometric origin is supplied")
        out.line("boundary/lift generator", StatusMark.INFO, "partial route; orientation and component inclusion remain burdens")
        out.line("layer-dependent route", StatusMark.OBLIGATION, "D_layer legitimacy remains the dangerous component burden")
        out.line("bulk/gauge contaminated", StatusMark.OBLIGATION, "separate lift-cleanliness theorem required")
    with out.counterexamples():
        out.line("renamed B", StatusMark.FAIL, "not a generator")
        out.line("free coefficients", StatusMark.FAIL, "repair-like")
        out.line("repair current", StatusMark.FAIL, "cancellation after leakage")
        out.line("active O", StatusMark.FAIL, "out of scope by label")
    with out.unresolved_obligations():
        out.line("common generator", StatusMark.OBLIGATION, "find a real boundary/covariant object that forces paired orientations")
        out.line("component membership", StatusMark.OBLIGATION, "derive jump/layer/tail membership in the same boundary object")
        out.line("lift cleanliness", StatusMark.OBLIGATION, "derive or split L_bulk and L_gauge neutrality")

    record_marker(ns, MARKER_ID, "generator class sieve; no common generator theorem")
    record_claim(ns, MARKER_ID, "g71_class_c1", GovernanceStatus.POLICY_RULE, "Only a real oriented common boundary object can retain the generator route as theorem target.")
    record_claim(ns, MARKER_ID, "g71_class_c2", GovernanceStatus.REJECTED_ROUTE, "Renamed-B, free-coefficient, repair-current, and active-O-by-label generator classes are rejected.")
    record_claim(ns, MARKER_ID, "g71_class_c3", GovernanceStatus.UNVERIFIED, "Layer-dependent and bulk/gauge-contaminated classes remain unresolved partial routes, not successes.")
    record_obligation(ns, "g71_class_o1", "If route continues, audit D_layer legitimacy and/or covariant lift neutrality next.")
    ns.write_run_metadata()

    print("\nPossible next script:")
    print("  candidate_generator_route_classifier.py")


if __name__ == "__main__":
    main()
