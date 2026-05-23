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
    ("g77_summary", "077_remainder_obstruction_audit__candidate_group_77_status_summary", "g77_summary"),
    ("g78_problem", "078_boundary_lift_split_obligation_ledger__candidate_obligation_ledger_problem", "g78_problem"),
    ("g78_inventory", "078_boundary_lift_split_obligation_ledger__candidate_split_target_inventory", "g78_inventory"),
    ("g78_dependency_graph", "078_boundary_lift_split_obligation_ledger__candidate_route_dependency_graph", "g78_dependency_graph"),
    ("g78_readiness", "078_boundary_lift_split_obligation_ledger__candidate_readiness_gate_matrix", "g78_readiness"),
    ("g78_repetition_sieve", "078_boundary_lift_split_obligation_ledger__candidate_repetition_risk_sieve", "g78_repetition_sieve"),
    ("g78_active_O_gate", "078_boundary_lift_split_obligation_ledger__candidate_active_O_threshold_gate", "g78_active_O_gate"),
    ("g78_next_work", "078_boundary_lift_split_obligation_ledger__candidate_next_work_selector", "g78_next_work"),
]
MARKER_ID = "g78_summary"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Group 78 Status Summary")
    print("Question:")
    print("  What is still owed before the boundary-lift route can advance?")
    print()
    print("Group 78 stable result:")
    print("  split-obligation ledger complete")
    print("  open targets inventoried")
    print("  dependency graph explicit")
    print("  readiness gates explicit")
    print("  repeated abstract audits rejected without concrete input")
    print("  active O not forced")
    print("  no theorem target closed")
    print("  parent divergence identity remains unproven")
    print("  recombination remains blocked")
    print("  next theorem attempt requires concrete route input")

    with out.governance_assessments():
        out.line("ledger", StatusMark.PASS, "split-obligation ledger recorded")
        out.line("readiness gates", StatusMark.PASS, "future-route readiness criteria stated")
        out.line("repetition sieve", StatusMark.PASS, "abstract reruns rejected without new input")
        out.line("active O", StatusMark.DEFER, "active O not forced")
        out.line("theorem closure", StatusMark.OBLIGATION, "no theorem target closed")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "parent recombination remains blocked")
    with out.counterexamples():
        out.line("ledger as theorem", StatusMark.FAIL, "ledger is not derivation")
        out.line("repeat abstract audit", StatusMark.FAIL, "repeating broad audits without concrete input is rejected")
        out.line("active O by frustration", StatusMark.FAIL, "difficulty does not force O")
        out.line("parent equation", StatusMark.FAIL, "parent construction remains forbidden")
    with out.unresolved_obligations():
        out.line("concrete input", StatusMark.OBLIGATION, "supply concrete route object for next theorem attempt")
        out.line("parent identity", StatusMark.OBLIGATION, "derive parent divergence only after subtargets close")

    print()
    print("Recommended next-route policy:")
    print("  if concrete gauge-exact structure exists: 79_gauge_exact_remainder_theorem_attempt")
    print("  if concrete boundary-exact structure exists: 79_boundary_exact_remainder_theorem_attempt")
    print("  if concrete layer geometry exists: 79_layer_geometry_concrete_test")
    print("  if no concrete input exists: 79_axiom_candidate_inventory or pause theorem attempts")
    print("  active O only later: 79_active_O_necessity_or_rejection, after clean O-free failure/projection requirement")

    record_marker(ns, MARKER_ID, "Group 78 summary; no parent equation")
    record_claim(ns, MARKER_ID, "g78_summary_c1", GovernanceStatus.POLICY_RULE, "Boundary-lift route now requires concrete input for further theorem attempts.")
    record_claim(ns, MARKER_ID, "g78_summary_c2", GovernanceStatus.REJECTED_ROUTE, "Repeated broad abstract audits without new input are rejected.")
    record_claim(ns, MARKER_ID, "g78_summary_c3", GovernanceStatus.POLICY_RULE, "Active O is not forced by current unresolved split targets.")
    record_obligation(ns, "g78_summary_o1", "Choose next group based on concrete route input or axiom inventory.")
    record_obligation(ns, "g78_summary_o2", "Parent divergence identity remains unproven.")
    ns.write_run_metadata()

if __name__ == "__main__":
    main()
