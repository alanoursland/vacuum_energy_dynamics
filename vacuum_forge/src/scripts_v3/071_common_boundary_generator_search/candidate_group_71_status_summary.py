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
        method="Group 71 summary marker; no physical derivation",
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
    ("g70_summary", "070_boundary_lift_matching_theorem_attempt__candidate_group_70_status_summary", "g70_summary"),
    ("g71_problem", "071_common_boundary_generator_search__candidate_generator_search_problem", "g71_problem"),
    ("g71_requirements", "071_common_boundary_generator_search__candidate_boundary_generator_requirements", "g71_requirements"),
    ("g71_orientation", "071_common_boundary_generator_search__candidate_orientation_forcing_test", "g71_orientation_forcing"),
    ("g71_components", "071_common_boundary_generator_search__candidate_component_forcing_test", "g71_component_forcing"),
    ("g71_bulk_gauge", "071_common_boundary_generator_search__candidate_bulk_gauge_leakage_test", "g71_bulk_gauge_leakage"),
    ("g71_class_sieve", "071_common_boundary_generator_search__candidate_generator_class_sieve", "g71_class_sieve"),
    ("g71_route_classifier", "071_common_boundary_generator_search__candidate_generator_route_classifier", "g71_route_classifier"),
]
MARKER_ID = "g71_summary"


def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Group 71 Status Summary")
    print("Question:")
    print("  Are the Group 70 signs carved by geometry, or only knobs selected to stop the leak?")
    print()
    print("Group 71 stable result:")
    print("  generator criteria explicit")
    print("  orientation anti-match compatibility explicit")
    print("  component anti-match compatibility explicit")
    print("  free-parameter / renamed-B / repair routes rejected")
    print("  D_layer legitimacy remains unresolved")
    print("  L_bulk and L_gauge remain lift-cleanliness obligations")
    print("  no strong common generator established in tested classes (not a no-go theorem)")
    print("  boundary-lift matching route remains partial theorem target / controlled obstruction")
    print("  parent divergence identity remains unproven")
    print("  recombination remains blocked")

    with out.governance_assessments():
        out.line("generator criteria", StatusMark.PASS, "legal common-generator requirements stated")
        out.line("orientation", StatusMark.PASS, "sigma=1 compatibility rederived as orientation anti-match requirement")
        out.line("components", StatusMark.PASS, "a_jump=a_layer=a_tail=-1 compatibility rederived as component anti-match requirement")
        out.line("strong generator", StatusMark.OBLIGATION, "not established in tested classes (not a no-go theorem)")
        out.line("partial route", StatusMark.INFO, "oriented common-boundary route retained as theorem target; no concrete partial generator found")
        out.line("D_layer", StatusMark.OBLIGATION, "layer component legitimacy remains unresolved")
        out.line("bulk/gauge", StatusMark.OBLIGATION, "L_bulk=0 and L_gauge=0 remain lift-cleanliness obligations")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "parent recombination remains blocked")
    with out.counterexamples():
        out.line("renamed B", StatusMark.FAIL, "B with a hat is not a generator")
        out.line("chosen signs", StatusMark.FAIL, "chosen sigma or coefficients are repair paint")
        out.line("diagnostic layer", StatusMark.FAIL, "old diagnostic transition response cannot supply D_layer")
        out.line("active O", StatusMark.FAIL, "active O by label remains forbidden")
        out.line("parent equation", StatusMark.FAIL, "parent equation construction remains forbidden")
    with out.unresolved_obligations():
        out.line("common boundary generator", StatusMark.OBLIGATION, "derive or abandon a real common boundary/covariant object")
        out.line("layer term legitimacy", StatusMark.OBLIGATION, "audit whether D_layer can be a legitimate boundary component")
        out.line("covariant lift neutrality", StatusMark.OBLIGATION, "derive L_bulk=0 and L_gauge=0 or split the route")

    print()
    print("Recommended next routes:")
    print("  primary if layer is the blocker: 72_layer_term_legitimacy_audit")
    print("  primary if lift cleanliness is prioritized: 72_covariant_lift_neutrality_attempt")
    print("  route-management fallback: 72_boundary_lift_route_downgrade or split-theorem-targets group")
    print("  active O only later: 72_active_O_necessity_or_rejection, if O-free routes fail cleanly")

    record_marker(ns, MARKER_ID, "Group 71 summary; no parent equation")
    record_claim(ns, MARKER_ID, "g71_summary_c1", GovernanceStatus.POLICY_RULE, "Group 71 did not establish a strong common generator in tested classes (not a no-go theorem); matching remains a partial theorem target.")
    record_claim(ns, MARKER_ID, "g71_summary_c2", GovernanceStatus.REJECTED_ROUTE, "Renamed-B, free-coefficient, diagnostic-layer, active-O-by-label, and parent-equation routes remain rejected.")
    record_claim(ns, MARKER_ID, "g71_summary_c3", GovernanceStatus.UNVERIFIED, "D_layer legitimacy and L_bulk/L_gauge neutrality remain open theorem burdens.")
    record_obligation(ns, "g71_summary_o1", "Decide next route: layer legitimacy, covariant lift neutrality, or route downgrade/split.")
    record_obligation(ns, "g71_summary_o2", "Parent divergence identity remains unproven and recombination remains blocked.")
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
