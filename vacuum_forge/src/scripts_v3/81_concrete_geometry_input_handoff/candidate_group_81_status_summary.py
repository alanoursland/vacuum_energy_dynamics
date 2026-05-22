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
    ("g80_summary", "80_axiom_adoption_decision_surface__candidate_group_80_status_summary", "g80_summary"),
    ("g81_problem", "81_concrete_geometry_input_handoff__candidate_concrete_input_handoff_problem", "g81_problem"),
    ("g81_acceptance", "81_concrete_geometry_input_handoff__candidate_concrete_input_acceptance_criteria", "g81_acceptance"),
    ("g81_dlayer_gate", "81_concrete_geometry_input_handoff__candidate_D_layer_geometry_input_gate", "g81_dlayer_gate"),
    ("g81_lift_gate", "81_concrete_geometry_input_handoff__candidate_lift_identity_input_gate", "g81_lift_gate"),
    ("g81_rho_gate", "81_concrete_geometry_input_handoff__candidate_rho_exactness_input_gate", "g81_rho_gate"),
    ("g81_parent_active_gate", "81_concrete_geometry_input_handoff__candidate_parent_and_active_O_input_gate", "g81_parent_active_gate"),
    ("g81_next_selector", "81_concrete_geometry_input_handoff__candidate_next_group_selector_from_input", "g81_next_selector"),
]
MARKER_ID = "g81_summary"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Group 81 Status Summary")
    print("Question: What concrete input is required before boundary-lift theorem attempts resume?")
    print("Group 81 stable result:")
    print("  concrete input acceptance criteria explicit")
    print("  D_layer geometry input gate explicit")
    print("  lift identity input gate explicit")
    print("  rho exactness input gate explicit")
    print("  parent and active-O gates explicit")
    print("  next group selector by input type explicit")
    print("  no theorem attempt started")
    print("  no axiom adopted")
    print("  parent divergence identity remains unproven")
    print("  recombination remains blocked")
    print("  future work requires a real object")

    with out.governance_assessments():
        out.line("handoff gate", StatusMark.PASS, "concrete-input handoff gate built")
        out.line("route gates", StatusMark.PASS, "D_layer/lift/rho/parent/O gates stated")
        out.line("selector", StatusMark.PASS, "next group selector stated")
        out.line("theorem attempt", StatusMark.DEFER, "no theorem attempt started")
        out.line("axiom adoption", StatusMark.DEFER, "no axiom adopted")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "recombination remains blocked")
    with out.counterexamples():
        out.line("label input", StatusMark.FAIL, "labels are insufficient")
        out.line("scaffold input", StatusMark.FAIL, "compatibility scaffold alone is insufficient")
        out.line("abstract rerun", StatusMark.FAIL, "no concrete input means no repeated abstract search")
        out.line("parent equation", StatusMark.FAIL, "parent construction remains forbidden")
    with out.unresolved_obligations():
        out.line("concrete input", StatusMark.OBLIGATION, "supply concrete route object before future theorem attempt")
        out.line("owner decision", StatusMark.OBLIGATION, "explicit owner decision required before any axiom use")

    print("\nRecommended next policy:")
    print("  concrete D_layer geometry -> 82_layer_geometry_concrete_test")
    print("  concrete lift identity -> 82_covariant_lift_identity_concrete_test")
    print("  concrete rho exactness -> 82_rho_exactness_concrete_test")
    print("  explicit axiom instruction -> 82_axiom_owner_decision")
    print("  no concrete input -> pause theorem attempts or 82_parent_blocker_refresh")

    record_marker(ns, MARKER_ID, "Group 81 summary; concrete input handoff only")
    record_claim(ns, MARKER_ID, "g81_summary_c1", GovernanceStatus.POLICY_RULE, "Group 81 builds concrete-input handoff gates and starts no theorem attempt.")
    record_claim(ns, MARKER_ID, "g81_summary_c2", GovernanceStatus.REJECTED_ROUTE, "Labels, scaffolds, desired cancellations, and abstract reruns are rejected as insufficient input.")
    record_obligation(ns, "g81_summary_o1", "Future theorem attempt requires concrete route object.")
    record_obligation(ns, "g81_summary_o2", "Parent divergence identity remains unproven.")
    ns.write_run_metadata()

if __name__ == "__main__":
    main()
