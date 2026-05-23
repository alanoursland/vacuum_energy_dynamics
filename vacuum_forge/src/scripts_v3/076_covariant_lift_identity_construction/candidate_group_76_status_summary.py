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
    ("g75_summary", "075_covariant_lift_neutrality_attempt__candidate_group_75_status_summary", "g75_summary"),
    ("g76_problem", "076_covariant_lift_identity_construction__candidate_lift_identity_problem", "g76_problem"),
    ("g76_requirements", "076_covariant_lift_identity_construction__candidate_shared_identity_requirements", "g76_requirements"),
    ("g76_exact_pair", "076_covariant_lift_identity_construction__candidate_exact_pair_scaffold", "g76_exact_pair"),
    ("g76_remainder", "076_covariant_lift_identity_construction__candidate_remainder_obstruction_test", "g76_remainder"),
    ("g76_gauge_exact", "076_covariant_lift_identity_construction__candidate_gauge_exact_remainder_test", "g76_gauge_exact"),
    ("g76_sieve", "076_covariant_lift_identity_construction__candidate_identity_vs_repair_sieve", "g76_sieve"),
    ("g76_route_classifier", "076_covariant_lift_identity_construction__candidate_lift_identity_route_classifier", "g76_route_classifier"),
]
MARKER_ID = "g76_summary"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Group 76 Status Summary")
    print("Question:")
    print("  Can a shared lift identity derive paired bulk/gauge cancellation?")
    print()
    print("Group 76 stable result:")
    print("  exact-pair scaffold constructed as compatibility")
    print("  shared identity requirements explicit")
    print("  remainder rho identified as obstruction")
    print("  gauge-exact remainder route retained only as theorem target")
    print("  shared lift identity not derived")
    print("  repair-style sign choice, dropped rho, and repair current rejected")
    print("  D_layer remains separate unresolved theorem target")
    print("  parent divergence identity remains unproven")
    print("  recombination remains blocked")

    with out.governance_assessments():
        out.line("exact pair", StatusMark.INFO, "compatibility scaffold only")
        out.line("rho obstruction", StatusMark.OBLIGATION, "rho=0 or inert/gauge-exact status not derived")
        out.line("gauge-exact route", StatusMark.INFO, "retained only as theorem target")
        out.line("shared identity", StatusMark.OBLIGATION, "shared lift identity not derived")
        out.line("repair rejection", StatusMark.PASS, "free sign, dropped rho, and repair current rejected")
        out.line("D_layer", StatusMark.INFO, "D_layer remains separate")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "parent recombination remains blocked")
    with out.counterexamples():
        out.line("free sign", StatusMark.FAIL, "opposite sign cannot be selected")
        out.line("dropped rho", StatusMark.FAIL, "rho cannot be discarded")
        out.line("active O", StatusMark.FAIL, "active O by label remains forbidden")
        out.line("parent equation", StatusMark.FAIL, "parent construction remains forbidden")
    with out.unresolved_obligations():
        out.line("rho theorem", StatusMark.OBLIGATION, "derive rho=0 or gauge-exact/inert status")
        out.line("identity theorem", StatusMark.OBLIGATION, "derive common K and sign relation")
        out.line("route management", StatusMark.OBLIGATION, "decide next route: rho audit, gauge-exact theorem, ledger, or active-O audit later")

    print()
    print("Recommended next routes:")
    print("  if rho is the blocker: 77_remainder_obstruction_audit")
    print("  if gauge-exact route is promising: 77_gauge_exact_remainder_theorem_attempt")
    print("  route-management fallback: 77_boundary_lift_split_obligation_ledger")
    print("  active O only later: 77_active_O_necessity_or_rejection, if O-free routes fail cleanly")

    record_marker(ns, MARKER_ID, "Group 76 summary; no parent equation")
    record_claim(ns, MARKER_ID, "g76_summary_c1", GovernanceStatus.POLICY_RULE, "Shared lift identity is not derived; rho obstruction remains.")
    record_claim(ns, MARKER_ID, "g76_summary_c2", GovernanceStatus.REJECTED_ROUTE, "Free sign, dropped rho, repair current, active-O patch, and parent jump are rejected.")
    record_obligation(ns, "g76_summary_o1", "Audit rho obstruction or gauge-exact remainder theorem.")
    record_obligation(ns, "g76_summary_o2", "Parent divergence identity remains unproven.")
    ns.write_run_metadata()

if __name__ == "__main__":
    main()
