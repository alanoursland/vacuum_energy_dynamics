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
    ("g75_requirements", "075_covariant_lift_neutrality_attempt__candidate_lift_cleanliness_requirements", "g75_requirements"),
    ("g75_shared_identity", "075_covariant_lift_neutrality_attempt__candidate_shared_lift_identity_test", "g75_shared_identity"),
]
MARKER_ID = "g75_discriminator"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    routes = [
        ("independent_neutrality", "retained_theorem_route", "derive L_bulk=0 and L_gauge=0 separately"),
        ("derived_shared_identity", "retained_theorem_route", "derive L_bulk+L_gauge=0 from common lift structure"),
        ("chosen_mutual_cancellation", "rejected", "choose L_bulk=-L_gauge after leakage appears"),
        ("drop_bulk_or_gauge", "rejected", "omit one residue by prose"),
        ("repair_current", "rejected", "add a current to cancel lift residual"),
        ("active_O_patch", "rejected_here", "projection-like patch outside Group 75"),
    ]
    header("Candidate Mutual Cancellation Discriminator")
    for name, status, reason in routes:
        print(f"{name}: {status}; {reason}")
    with out.governance_assessments():
        out.line("independent neutrality", StatusMark.INFO, "retained if derived")
        out.line("derived shared identity", StatusMark.INFO, "retained if common lift structure derives it")
    with out.counterexamples():
        for name, _status, reason in routes[2:]:
            out.line(name, StatusMark.FAIL, reason)
    with out.unresolved_obligations():
        out.line("lift theorem", StatusMark.OBLIGATION, "derive independent neutrality or shared lift identity")
    record_marker(ns, MARKER_ID, "mutual-cancellation discriminator; no theorem proof")
    record_claim(ns, MARKER_ID, "g75_disc_c1", GovernanceStatus.POLICY_RULE, "Independent neutrality and derived shared identity are retained theorem routes.")
    record_claim(ns, MARKER_ID, "g75_disc_c2", GovernanceStatus.REJECTED_ROUTE, "Chosen mutual cancellation, dropped terms, repair currents, and active-O patches are rejected here.")
    record_obligation(ns, "g75_disc_o1", "Classify final lift route after tested routes.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_lift_route_classifier.py")
if __name__ == "__main__":
    main()
