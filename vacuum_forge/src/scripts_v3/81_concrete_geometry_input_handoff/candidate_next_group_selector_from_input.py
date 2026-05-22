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
    ("g81_dlayer_gate", "81_concrete_geometry_input_handoff__candidate_D_layer_geometry_input_gate", "g81_dlayer_gate"),
    ("g81_lift_gate", "81_concrete_geometry_input_handoff__candidate_lift_identity_input_gate", "g81_lift_gate"),
    ("g81_rho_gate", "81_concrete_geometry_input_handoff__candidate_rho_exactness_input_gate", "g81_rho_gate"),
    ("g81_parent_active_gate", "81_concrete_geometry_input_handoff__candidate_parent_and_active_O_input_gate", "g81_parent_active_gate"),
]
MARKER_ID = "g81_next_selector"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    routes = [
        ("concrete_D_layer_geometry", "82_layer_geometry_concrete_test"),
        ("concrete_lift_identity", "82_covariant_lift_identity_concrete_test"),
        ("concrete_rho_exactness", "82_rho_exactness_concrete_test"),
        ("explicit_axiom_instruction", "82_axiom_owner_decision"),
        ("active_O_structural_requirement", "82_active_O_necessity_or_rejection"),
        ("no_concrete_input", "pause_theorem_attempts_or_82_parent_blocker_refresh"),
    ]

    header("Candidate Next Group Selector From Input")
    for input_type, next_group in routes:
        print(f"{input_type}: {next_group}")

    with out.governance_assessments():
        out.line("selector", StatusMark.PASS, "input-to-next-group selector stated")
        out.line("no input", StatusMark.DEFER, "pause theorem attempts or refresh parent blockers")
        out.line("axiom instruction", StatusMark.OBLIGATION, "explicit instruction required for owner decision")
    with out.counterexamples():
        out.line("abstract rerun", StatusMark.FAIL, "no concrete input means no new abstract theorem attempt")
        out.line("parent jump", StatusMark.FAIL, "parent route remains blocked")
    with out.unresolved_obligations():
        out.line("input choice", StatusMark.OBLIGATION, "future group must declare which input type it supplies")

    record_marker(ns, MARKER_ID, "next group selector from concrete input; no theorem")
    record_claim(ns, MARKER_ID, "g81_selector_c1", GovernanceStatus.POLICY_RULE, "Future theorem group must be selected by concrete input type.")
    record_claim(ns, MARKER_ID, "g81_selector_c2", GovernanceStatus.REJECTED_ROUTE, "No concrete input means no repeated abstract theorem attempt.")
    record_obligation(ns, "g81_selector_o1", "Declare concrete input type before starting future theorem group.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_group_81_status_summary.py")

if __name__ == "__main__":
    main()
