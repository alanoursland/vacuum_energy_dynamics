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
    ("g84_flat_moments", "84_local_rho_inertness_test__candidate_flat_probe_moment_test", "g84_flat_moments"),
    ("g84_weighted_moments", "84_local_rho_inertness_test__candidate_weighted_probe_moment_test", "g84_weighted_moments"),
    ("g84_tradeoff", "84_local_rho_inertness_test__candidate_skew_inertness_tradeoff_test", "g84_tradeoff"),
    ("g84_quadratic_obstruction", "84_local_rho_inertness_test__candidate_quadratic_payload_obstruction", "g84_quadratic_obstruction"),
]
MARKER_ID = "g84_route_classifier"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    classifications = [
        ("GLOBAL_SOURCE_NEUTRALITY_RETAINED", "stable", "M0=0"),
        ("DIPOLE_PAYLOAD_NONZERO", "stable", "M1 nonzero for Group 83 skew"),
        ("QUADRATIC_PAYLOAD_NONZERO", "stable", "M2=1024/1155"),
        ("WEIGHTED_TOTAL_NEUTRALITY_RETAINED", "stable", "W0=0 by Group 83 skew"),
        ("WEIGHTED_LOCAL_PAYLOAD_NONZERO", "stable", "weighted W1/W2 nonzero"),
        ("WEIGHTED_NEUTRALITY_DIPOLE_INERTNESS_TRADEOFF", "stable", "weighted neutrality requires c=3ell/(2R), dipole inertness requires c=0"),
        ("LINEAR_SKEW_CANNOT_KILL_QUADRATIC_PAYLOAD", "stable", "M2 independent of c"),
        ("LOCAL_INERTNESS_OBSTRUCTED_IN_FINITE_MODE_TEST", "stable", "low-order probes detect local rho"),
        ("RHO_EXACTNESS_STILL_GLOBALLY_USEFUL", "stable", "flat and weighted total neutrality remain meaningful"),
        ("PARENT_DIVERGENCE_UNPROVEN", "stable", "parent identity remains blocked"),
        ("RECOMBINATION_BLOCKED", "stable", "no recombination license"),
    ]

    header("Candidate Local Inertness Route Classifier")
    for name, status, reason in classifications:
        print(f"{name}: {status}; {reason}")

    with out.governance_assessments():
        out.line("global source neutrality", StatusMark.PASS, "retained")
        out.line("weighted total neutrality", StatusMark.PASS, "retained")
        out.line("dipole payload", StatusMark.WARN, "nonzero")
        out.line("quadratic payload", StatusMark.WARN, "nonzero and c-independent")
        out.line("finite-mode inertness", StatusMark.WARN, "obstructed in tested basis")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "recombination remains blocked")
    with out.counterexamples():
        out.line("total neutrality as local inertness", StatusMark.FAIL, "flat/weighted total neutrality cannot be spent as local inertness")
        out.line("linear skew as payload cure", StatusMark.FAIL, "linear skew cannot kill quadratic payload moment")
        out.line("full theorem overclaim", StatusMark.FAIL, "finite-mode obstruction is not full physical theorem")
        out.line("parent jump", StatusMark.FAIL, "parent equation remains forbidden")
    with out.unresolved_obligations():
        out.line("richer shape family", StatusMark.OBLIGATION, "test whether richer profiles can suppress payload moments")
        out.line("payload projection", StatusMark.OBLIGATION, "consider whether a legitimate projection/inertness mechanism is required")
        out.line("covariant lift", StatusMark.OBLIGATION, "finite-mode result needs covariant interpretation")

    record_marker(ns, MARKER_ID, "local inertness route classifier")
    record_claim(ns, MARKER_ID, "g84_class_c1", GovernanceStatus.POLICY_RULE, "Local rho inertness is obstructed in the tested low-order finite-mode basis.")
    record_claim(ns, MARKER_ID, "g84_class_c2", GovernanceStatus.POLICY_RULE, "Rho exactness remains globally useful but locally payload-dangerous.")
    record_obligation(ns, "g84_class_o1", "Test richer shape family or payload projection if exactness route continues.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_group_84_status_summary.py")

if __name__ == "__main__":
    main()
