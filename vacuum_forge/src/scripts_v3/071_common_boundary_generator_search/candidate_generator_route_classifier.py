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
        method="route classification marker; no physical derivation",
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
    ("g71_class_sieve", "071_common_boundary_generator_search__candidate_generator_class_sieve", "g71_class_sieve"),
    ("g71_bulk_gauge", "071_common_boundary_generator_search__candidate_bulk_gauge_leakage_test", "g71_bulk_gauge_leakage"),
    ("g71_components", "071_common_boundary_generator_search__candidate_component_forcing_test", "g71_component_forcing"),
]
MARKER_ID = "g71_route_classifier"


def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Generator Route Classifier")
    print("Final route classification from tested classes:")
    print("  STRONG_GENERATOR_NOT_ESTABLISHED: not established in tested classes")
    print("  PARTIAL_ROUTE_RETAINED_AS_THEOREM_TARGET: orientation/component anti-match representable; geometric origin open")
    print("  GENERATOR_FREE_PARAMETER_ONLY: rejected as repair-like")
    print("  NO_STRONG_GENERATOR_ESTABLISHED_IN_TESTED_CLASSES: true (not a no-go theorem)")
    print("  CONTROLLED_OBSTRUCTION: yes")
    print("  SPLIT_THEOREM_TARGETS_REQUIRED: yes")
    print()
    print("Reason:")
    print("  Opposite-orientation and component anti-match can be represented symbolically.")
    print("  But Group 71 does not derive a geometric generator that forces them.")
    print("  D_layer legitimacy and L_bulk/L_gauge neutrality remain separate blockers.")

    with out.governance_assessments():
        out.line("strong generator", StatusMark.OBLIGATION, "not established in tested classes (not a no-go theorem)")
        out.line("partial route", StatusMark.INFO, "oriented common-boundary route retained as theorem target; no concrete partial generator found")
        out.line("controlled obstruction", StatusMark.PASS, "failure mode localized to generator origin, D_layer legitimacy, and lift neutrality")
        out.line("split theorem targets", StatusMark.PASS, "boundary orientation/components, layer legitimacy, and bulk/gauge neutrality should be separated")
        out.line("parent equation", StatusMark.DEFER, "parent equation remains blocked")
    with out.counterexamples():
        out.line("free-parameter only", StatusMark.FAIL, "manual signs/coefficients are repair-like")
        out.line("renamed-B route", StatusMark.FAIL, "boundary sum without origin is not a generator")
        out.line("diagnostic layer", StatusMark.FAIL, "D_layer cannot be supplied by old diagnostic transition response")
    with out.unresolved_obligations():
        out.line("common generator origin", StatusMark.OBLIGATION, "derive real shared boundary/covariant object")
        out.line("D_layer legitimacy", StatusMark.OBLIGATION, "audit whether layer component can be part of boundary generator")
        out.line("bulk/gauge neutrality", StatusMark.OBLIGATION, "derive L_bulk=0 and L_gauge=0 or split to lift route")

    record_marker(ns, MARKER_ID, "route classifier; no strong generator established in tested classes")
    record_claim(ns, MARKER_ID, "g71_route_c1", GovernanceStatus.UNVERIFIED, "No strong common generator established in tested classes; this is not a no-go theorem.")
    record_claim(ns, MARKER_ID, "g71_route_c2", GovernanceStatus.POLICY_RULE, "Boundary-lift matching remains a partial theorem target, not a proven theorem.")
    record_claim(ns, MARKER_ID, "g71_route_c3", GovernanceStatus.REJECTED_ROUTE, "Free-parameter, renamed-B, and diagnostic-layer routes are rejected.")
    record_obligation(ns, "g71_route_o1", "Route management should split boundary generator, D_layer legitimacy, and bulk/gauge neutrality burdens.")
    record_obligation(ns, "g71_route_o2", "Parent divergence identity remains unproven.")
    ns.write_run_metadata()

    print("\nPossible next script:")
    print("  candidate_group_71_status_summary.py")


if __name__ == "__main__":
    main()
