
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
    ("g69_summary", "069_boundary_covariant_cancellation_attempt__candidate_group_69_status_summary", "g69_summary"),
    ("g70_bulk_gauge", "070_boundary_lift_matching_theorem_attempt__candidate_bulk_gauge_neutrality", "g70_bulk_gauge"),
]
MARKER_ID = "g70_discriminator"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    routes = [
        ("derived_common_generator", "retained", "sigma and coefficients derived from shared geometry"),
        ("chosen_sigma", "rejected", "orientation sign selected to cancel"),
        ("chosen_coefficients", "rejected", "component coefficients selected to cancel"),
        ("drop_bulk_gauge", "rejected", "L_bulk/L_gauge ignored without theorem"),
        ("diagnostic_layer_insertion", "rejected", "diagnostic transition used as D_layer"),
    ]

    header("Candidate Matching-vs-Repair Discriminator")
    for name, status, reason in routes:
        print(f"{name}: {status}; {reason}")
    with out.governance_assessments():
        out.line("derived common generator", StatusMark.INFO, "retained theorem route if actually derived")
    with out.counterexamples():
        for name, status, reason in routes[1:]:
            out.line(name, StatusMark.FAIL, reason)
    with out.unresolved_obligations():
        out.line("matching theorem", StatusMark.OBLIGATION, "derive common-generator route, do not choose it")

    record_marker(ns, MARKER_ID, "matching-vs-repair discriminator; no theorem proof")
    record_claim(ns, MARKER_ID, "g70_discriminator_c1", GovernanceStatus.POLICY_RULE, "Only derived common-generator matching is retained.")
    record_claim(ns, MARKER_ID, "g70_discriminator_c2", GovernanceStatus.REJECTED_ROUTE, "Chosen signs, coefficients, dropped bulk/gauge, and diagnostic insertion are rejected.")
    record_obligation(ns, "g70_discriminator_o1", "Attempt or reject a real common boundary generator next.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_theorem_burden_classifier.py")

if __name__ == "__main__":
    main()
