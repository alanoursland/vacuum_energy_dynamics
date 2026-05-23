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
    ("g76_summary", "076_covariant_lift_identity_construction__candidate_group_76_status_summary", "g76_summary"),
    ("g77_problem", "077_remainder_obstruction_audit__candidate_remainder_audit_problem", "g77_problem"),
    ("g77_requirements", "077_remainder_obstruction_audit__candidate_remainder_status_requirements", "g77_requirements"),
    ("g77_zero", "077_remainder_obstruction_audit__candidate_zero_remainder_theorem_test", "g77_zero"),
    ("g77_gauge_exact", "077_remainder_obstruction_audit__candidate_gauge_exact_classification_test", "g77_gauge_exact"),
    ("g77_boundary_exact", "077_remainder_obstruction_audit__candidate_boundary_exactness_test", "g77_boundary_exact"),
    ("g77_payload", "077_remainder_obstruction_audit__candidate_physical_remainder_payload_test", "g77_payload"),
    ("g77_route_classifier", "077_remainder_obstruction_audit__candidate_remainder_route_classifier", "g77_route_classifier"),
]
MARKER_ID = "g77_summary"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Group 77 Status Summary")
    print("Question:")
    print("  Is rho zero, exact, inert, or a real lift obstruction?")
    print()
    print("Group 77 stable result:")
    print("  rho status criteria explicit")
    print("  zero-remainder route retained only as theorem target")
    print("  gauge-exact route retained only as theorem target")
    print("  boundary-exact route retained only as theorem target")
    print("  physical-payload filter explicit")
    print("  rho removal not derived")
    print("  rho status remains unresolved")
    print("  shared lift identity remains not closed")
    print("  D_layer remains separate unresolved theorem target")
    print("  parent divergence identity remains unproven")
    print("  recombination remains blocked")

    with out.governance_assessments():
        out.line("criteria", StatusMark.PASS, "legal rho statuses stated")
        out.line("zero route", StatusMark.OBLIGATION, "rho=0 not derived")
        out.line("gauge-exact route", StatusMark.INFO, "retained only as theorem target")
        out.line("boundary-exact route", StatusMark.INFO, "retained only as theorem target")
        out.line("physical payload", StatusMark.OBLIGATION, "payload absence/inertness not derived")
        out.line("shared identity", StatusMark.OBLIGATION, "shared lift identity remains not closed")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "parent recombination remains blocked")
    with out.counterexamples():
        out.line("drop rho", StatusMark.FAIL, "rho cannot be dropped")
        out.line("exact by label", StatusMark.FAIL, "exact/inert status cannot be assigned by prose")
        out.line("repair current", StatusMark.FAIL, "repair current cannot cancel rho")
        out.line("active O", StatusMark.FAIL, "active O by label remains forbidden")
        out.line("parent equation", StatusMark.FAIL, "parent construction remains forbidden")
    with out.unresolved_obligations():
        out.line("rho theorem", StatusMark.OBLIGATION, "derive zero/exact/inert status or retain obstruction")
        out.line("route management", StatusMark.OBLIGATION, "decide whether to attempt exactness theorem or ledger remaining split targets")

    print()
    print("Recommended next routes:")
    print("  if exact route is promising: 78_gauge_exact_remainder_theorem_attempt")
    print("  if boundary exactness is promising: 78_boundary_exact_remainder_theorem_attempt")
    print("  route-management fallback: 78_boundary_lift_split_obligation_ledger")
    print("  active O only later: 78_active_O_necessity_or_rejection, if O-free routes fail cleanly")

    record_marker(ns, MARKER_ID, "Group 77 summary; no parent equation")
    record_claim(ns, MARKER_ID, "g77_summary_c1", GovernanceStatus.POLICY_RULE, "Rho status remains unresolved; zero/exact/inert routes are not derived.")
    record_claim(ns, MARKER_ID, "g77_summary_c2", GovernanceStatus.REJECTED_ROUTE, "Dropped rho, exact/inert labels by prose, repair currents, active-O patch, and parent jump are rejected.")
    record_obligation(ns, "g77_summary_o1", "Derive rho theorem or route-manage remaining split targets.")
    record_obligation(ns, "g77_summary_o2", "Parent divergence identity remains unproven.")
    ns.write_run_metadata()

if __name__ == "__main__":
    main()
