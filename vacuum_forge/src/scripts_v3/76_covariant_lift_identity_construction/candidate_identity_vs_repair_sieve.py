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
    ("g76_exact_pair", "76_covariant_lift_identity_construction__candidate_exact_pair_scaffold", "g76_exact_pair"),
    ("g76_remainder", "76_covariant_lift_identity_construction__candidate_remainder_obstruction_test", "g76_remainder"),
    ("g76_gauge_exact", "76_covariant_lift_identity_construction__candidate_gauge_exact_remainder_test", "g76_gauge_exact"),
]
MARKER_ID = "g76_sieve"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    routes = [
        ("derived_exact_pair", "retained_theorem_route", "common K/sign relation derived with no remainder"),
        ("derived_gauge_exact_remainder", "retained_conditional", "exact part nonphysical and physical remainder zero by theorem"),
        ("free_opposite_sign", "rejected", "opposite signs selected to cancel"),
        ("dropped_rho", "rejected", "remainder discarded by prose"),
        ("repair_current", "rejected", "add current to cancel rho"),
        ("active_O_patch", "rejected_here", "projection-like patch outside Group 76"),
    ]

    header("Candidate Identity-vs-Repair Sieve")
    for name, status, reason in routes:
        print(f"{name}: {status}; {reason}")

    with out.governance_assessments():
        out.line("derived exact pair", StatusMark.INFO, "retained only if derived")
        out.line("gauge-exact remainder", StatusMark.INFO, "retained only if physical remainder vanishes")
    with out.counterexamples():
        for name, _status, reason in routes[2:]:
            out.line(name, StatusMark.FAIL, reason)
    with out.unresolved_obligations():
        out.line("identity theorem", StatusMark.OBLIGATION, "derive exact pair or lawful gauge-exact remainder route")

    record_marker(ns, MARKER_ID, "identity-vs-repair sieve; no theorem proof")
    record_claim(ns, MARKER_ID, "g76_sieve_c1", GovernanceStatus.POLICY_RULE, "Only derived exact-pair or proven gauge-exact remainder routes survive.")
    record_claim(ns, MARKER_ID, "g76_sieve_c2", GovernanceStatus.REJECTED_ROUTE, "Free sign, dropped rho, repair current, and active-O patch are rejected here.")
    record_obligation(ns, "g76_sieve_o1", "Classify final lift identity route.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_lift_identity_route_classifier.py")

if __name__ == "__main__":
    main()
