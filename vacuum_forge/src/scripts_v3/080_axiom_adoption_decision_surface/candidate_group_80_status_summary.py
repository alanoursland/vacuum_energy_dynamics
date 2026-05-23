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
    ("g79_summary", "079_axiom_candidate_inventory__candidate_group_79_status_summary", "g79_summary"),
    ("g80_problem", "080_axiom_adoption_decision_surface__candidate_adoption_surface_problem", "g80_problem"),
    ("g80_criteria", "080_axiom_adoption_decision_surface__candidate_adoption_decision_criteria", "g80_criteria"),
    ("g80_D_layer_surface", "080_axiom_adoption_decision_surface__candidate_D_layer_axiom_decision_surface", "g80_D_layer_surface"),
    ("g80_lift_surface", "080_axiom_adoption_decision_surface__candidate_lift_axiom_decision_surface", "g80_lift_surface"),
    ("g80_rho_surface", "080_axiom_adoption_decision_surface__candidate_rho_axiom_decision_surface", "g80_rho_surface"),
    ("g80_parent_gate", "080_axiom_adoption_decision_surface__candidate_parent_facing_axiom_gate", "g80_parent_gate"),
    ("g80_route_classifier", "080_axiom_adoption_decision_surface__candidate_adoption_route_classifier", "g80_route_classifier"),
]
MARKER_ID = "g80_summary"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    header("Candidate Group 80 Status Summary")
    print("Question: Which axiom candidates are admissible for future adoption decision?")
    print("Group 80 stable result:")
    for line in ["adoption-decision criteria explicit", "D_layer candidates deferred; diagnostic/repair layer shortcuts rejected", "lift candidates deferred; chosen cancellation and dropped residue shortcuts rejected", "rho candidates deferred; dropped-rho and exact-by-label shortcuts rejected", "no axiom adopted", "no axiom ready for adoption inside this group", "future owner decision required before any axiom use", "parent divergence identity remains unproven", "recombination remains blocked"]:
        print(f"  {line}")
    with out.governance_assessments():
        out.line("decision surface", StatusMark.PASS, "axiom adoption decision surface complete")
        out.line("adoption", StatusMark.DEFER, "no axiom adopted")
        out.line("readiness", StatusMark.DEFER, "no axiom adoption-ready in this group")
        out.line("D_layer candidates", StatusMark.INFO, "deferred with validation obligations")
        out.line("lift candidates", StatusMark.INFO, "deferred with validation obligations")
        out.line("rho candidates", StatusMark.INFO, "deferred with validation obligations")
        out.line("shortcut axioms", StatusMark.PASS, "unsafe shortcut axioms rejected")
        out.line("future owner decision", StatusMark.OBLIGATION, "required before any axiom use")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "parent recombination remains blocked")
    with out.counterexamples():
        out.line("candidate as adopted", StatusMark.FAIL, "candidate status cannot be used as adopted axiom")
        out.line("axiom as theorem", StatusMark.FAIL, "axiom adoption would not be derivation")
        out.line("parent equation", StatusMark.FAIL, "parent construction remains forbidden")
        out.line("repair shortcut", StatusMark.FAIL, "repair-style axiom routes remain rejected")
    with out.unresolved_obligations():
        out.line("adoption decision", StatusMark.OBLIGATION, "explicit future group required for any actual adoption")
        out.line("validation tests", StatusMark.OBLIGATION, "future validation tests required for any adopted axiom")
        out.line("parent identity", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
    print("\nRecommended next routes:")
    print("  if concrete input appears: 81_concrete_geometry_input_handoff")
    print("  if active O must be reconsidered: 81_active_O_necessity_or_rejection")
    print("  if parent status needs refresh: 81_parent_blocker_refresh")
    print("  otherwise: pause boundary-lift theorem attempts until concrete input or explicit adoption instruction exists")
    record_marker(ns, MARKER_ID, "Group 80 summary; no axiom adopted")
    record_claim(ns, MARKER_ID, "g80_summary_c1", GovernanceStatus.POLICY_RULE, "Group 80 builds axiom adoption-decision surface and adopts no axiom.")
    record_claim(ns, MARKER_ID, "g80_summary_c2", GovernanceStatus.REJECTED_ROUTE, "Shortcut axiom forms remain rejected.")
    record_obligation(ns, "g80_summary_o1", "Explicit future owner decision required before any axiom use.")
    record_obligation(ns, "g80_summary_o2", "Parent divergence identity remains unproven.")
    ns.write_run_metadata()
if __name__ == "__main__": main()
