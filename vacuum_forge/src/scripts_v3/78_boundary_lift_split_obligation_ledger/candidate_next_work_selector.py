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
    ("g78_readiness", "78_boundary_lift_split_obligation_ledger__candidate_readiness_gate_matrix", "g78_readiness"),
    ("g78_active_O_gate", "78_boundary_lift_split_obligation_ledger__candidate_active_O_threshold_gate", "g78_active_O_gate"),
]
MARKER_ID = "g78_next_work"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    routes = [
        ("79_gauge_exact_remainder_theorem_attempt", "conditional", "only if concrete exactness operator is supplied"),
        ("79_boundary_exact_remainder_theorem_attempt", "conditional", "only if concrete boundary divergence object is supplied"),
        ("79_layer_geometry_concrete_test", "conditional", "only if concrete boundary/layer geometry is supplied"),
        ("79_axiom_candidate_inventory", "safe_fallback", "if theory wants to inventory explicit axiom candidates"),
        ("79_active_O_necessity_or_rejection", "later", "only after O-free split targets fail cleanly or require projection"),
    ]

    header("Candidate Next Work Selector")
    for name, status, reason in routes:
        print(f"{name}: {status}; {reason}")

    with out.governance_assessments():
        out.line("concrete theorem routes", StatusMark.INFO, "allowed only with concrete route input")
        out.line("axiom inventory", StatusMark.INFO, "safe fallback if no theorem input exists")
        out.line("active O", StatusMark.DEFER, "later only after clean O-free failure/projection requirement")
    with out.counterexamples():
        out.line("repeat broad search", StatusMark.FAIL, "do not run another abstract search without new input")
        out.line("immediate parent", StatusMark.FAIL, "parent route remains blocked")
    with out.unresolved_obligations():
        out.line("next input", StatusMark.OBLIGATION, "choose next group based on available concrete structure")

    record_marker(ns, MARKER_ID, "next work selector; no theorem proof")
    record_claim(ns, MARKER_ID, "g78_next_c1", GovernanceStatus.POLICY_RULE, "Next theorem attempt requires concrete route input; otherwise use axiom inventory or route management.")
    record_obligation(ns, "g78_next_o1", "Select next group based on available concrete input.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_group_78_status_summary.py")

if __name__ == "__main__":
    main()
