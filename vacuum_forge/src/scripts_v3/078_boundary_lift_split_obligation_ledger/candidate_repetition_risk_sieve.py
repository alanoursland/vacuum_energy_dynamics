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
    ("g78_readiness", "078_boundary_lift_split_obligation_ledger__candidate_readiness_gate_matrix", "g78_readiness"),
]
MARKER_ID = "g78_repetition_sieve"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    rejected_repeat = [
        "another_broad_common_generator_search",
        "another_abstract_exactness_classification",
        "another_compatibility_only_sign_or_coefficient_solve",
        "another_route_summary_as_theorem",
        "another_active_O_by_frustration_argument",
    ]
    retained_future = [
        "concrete_D_layer_geometry_test",
        "concrete_covariant_lift_identity_test",
        "concrete_gauge_exact_remainder_theorem",
        "concrete_boundary_exact_remainder_theorem",
        "explicit_axiom_candidate_inventory",
        "route_management_ledger_update",
    ]

    header("Candidate Repetition Risk Sieve")
    print("Rejected repeat patterns:")
    for item in rejected_repeat:
        print(f"  - {item}")
    print("Retained future patterns:")
    for item in retained_future:
        print(f"  - {item}")

    with out.governance_assessments():
        out.line("repeat sieve", StatusMark.PASS, "abstract repetition patterns rejected")
        out.line("concrete future work", StatusMark.INFO, "future theorem attempts require concrete structures")
    with out.counterexamples():
        for item in rejected_repeat:
            out.line(item, StatusMark.FAIL, "would repackage existing obstruction without new input")
    with out.unresolved_obligations():
        out.line("concrete input", StatusMark.OBLIGATION, "supply concrete route object before next theorem attempt")

    record_marker(ns, MARKER_ID, "repetition risk sieve; no theorem proof")
    record_claim(ns, MARKER_ID, "g78_repeat_c1", GovernanceStatus.REJECTED_ROUTE, "Repeated broad abstract searches are rejected without new concrete input.")
    record_claim(ns, MARKER_ID, "g78_repeat_c2", GovernanceStatus.POLICY_RULE, "Future theorem attempts should use concrete route objects or be explicit route-management.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_active_O_threshold_gate.py")

if __name__ == "__main__":
    main()
