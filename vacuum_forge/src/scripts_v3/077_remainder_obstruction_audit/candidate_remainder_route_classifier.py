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
    ("g77_zero", "077_remainder_obstruction_audit__candidate_zero_remainder_theorem_test", "g77_zero"),
    ("g77_gauge_exact", "077_remainder_obstruction_audit__candidate_gauge_exact_classification_test", "g77_gauge_exact"),
    ("g77_boundary_exact", "077_remainder_obstruction_audit__candidate_boundary_exactness_test", "g77_boundary_exact"),
    ("g77_payload", "077_remainder_obstruction_audit__candidate_physical_remainder_payload_test", "g77_payload"),
]
MARKER_ID = "g77_route_classifier"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    classifications = [
        ("RHO_ZERO_DERIVED", "not established", "zero route compatibility shown, theorem not derived"),
        ("GAUGE_EXACT_REMAINDER_DERIVED", "not established", "gauge-exact classification route retained but not proven"),
        ("BOUNDARY_EXACT_REMAINDER_DERIVED", "not established", "boundary-exact classification route retained but not proven"),
        ("PHYSICAL_REMAINDER_OBSTRUCTION", "conditional", "if rho_phys has payload, shared lift identity is blocked"),
        ("RHO_STATUS_UNRESOLVED", "stable", "no tested route derives zero/exact/inert status"),
        ("REPAIR_ROUTES_REJECTED", "stable", "dropped rho, labels by prose, repair currents rejected"),
        ("SHARED_LIFT_IDENTITY_NOT_CLOSED", "stable", "rho theorem burden remains"),
        ("PARENT_DIVERGENCE_UNPROVEN", "stable", "parent identity remains blocked"),
        ("RECOMBINATION_BLOCKED", "stable", "no recombination license"),
    ]

    header("Candidate Remainder Route Classifier")
    print("Final rho route classification from Group 77 tests:")
    for name, status, reason in classifications:
        print(f"  {name}: {status}; {reason}")
    print()
    print("Reason:")
    print("  Zero, gauge-exact, boundary-exact, and inert/no-payload statuses can be stated.")
    print("  None are derived in the tested abstract classes.")
    print("  Physical payload would make rho a real lift obstruction.")
    print("  Shared lift identity remains not closed.")

    with out.governance_assessments():
        out.line("zero route", StatusMark.OBLIGATION, "rho=0 not derived")
        out.line("gauge-exact route", StatusMark.INFO, "retained only as theorem target")
        out.line("boundary-exact route", StatusMark.INFO, "retained only as theorem target")
        out.line("physical payload", StatusMark.OBLIGATION, "physical payload must be proven absent/inert")
        out.line("shared identity", StatusMark.OBLIGATION, "shared lift identity remains unclosed")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "parent recombination remains blocked")
    with out.counterexamples():
        out.line("dropped rho", StatusMark.FAIL, "rho cannot be dropped")
        out.line("exact label", StatusMark.FAIL, "exact/inert labels are not theorems")
        out.line("repair current", StatusMark.FAIL, "repair current cannot cancel rho")
        out.line("parent jump", StatusMark.FAIL, "parent equation remains forbidden")
    with out.unresolved_obligations():
        out.line("rho theorem", StatusMark.OBLIGATION, "derive zero/exact/inert status or retain obstruction")
        out.line("route management", StatusMark.OBLIGATION, "decide next route if rho remains unresolved")

    record_marker(ns, MARKER_ID, "rho route classifier; no parent equation")
    record_claim(ns, MARKER_ID, "g77_class_c1", GovernanceStatus.POLICY_RULE, "Rho status remains unresolved; zero/exact/inert routes are not derived.")
    record_claim(ns, MARKER_ID, "g77_class_c2", GovernanceStatus.REJECTED_ROUTE, "Dropped rho, exact labels by prose, repair currents, and parent jump are rejected.")
    record_obligation(ns, "g77_class_o1", "Route-manage rho obstruction or attempt concrete exactness theorem.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_group_77_status_summary.py")

if __name__ == "__main__":
    main()
