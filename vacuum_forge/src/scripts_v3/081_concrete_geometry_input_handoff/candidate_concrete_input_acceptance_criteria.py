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
    ("g80_summary", "080_axiom_adoption_decision_surface__candidate_group_80_status_summary", "g80_summary"),
    ("g81_problem", "081_concrete_geometry_input_handoff__candidate_concrete_input_handoff_problem", "g81_problem"),
]
MARKER_ID = "g81_acceptance"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    accepted = [
        "named mathematical object",
        "domain/codomain or target sector",
        "role in one deferred route",
        "not selected by desired cancellation",
        "testable equations or conditions",
        "payload and boundary risks visible",
        "validation checklist",
    ]
    rejected = [
        "label only",
        "summary only",
        "compatibility scaffold only",
        "desired cancellation",
        "owner preference without adoption group",
        "recovery-selected object",
    ]

    header("Candidate Concrete Input Acceptance Criteria")
    print("Accepted concrete-input criteria:")
    for item in accepted:
        print(f"  - {item}")
    print("Rejected as insufficient input:")
    for item in rejected:
        print(f"  - {item}")

    with out.governance_assessments():
        out.line("acceptance criteria", StatusMark.PASS, "concrete-input criteria stated")
        out.line("validation", StatusMark.OBLIGATION, "future route must provide validation checklist")
    with out.counterexamples():
        for item in rejected:
            out.line(item, StatusMark.FAIL, "insufficient concrete input")
    with out.unresolved_obligations():
        out.line("route-specific gates", StatusMark.OBLIGATION, "apply criteria to D_layer, lift, and rho routes")

    record_marker(ns, MARKER_ID, "concrete input acceptance criteria; no theorem")
    record_claim(ns, MARKER_ID, "g81_accept_c1", GovernanceStatus.POLICY_RULE, "Future theorem attempts require concrete route-specific input.")
    record_obligation(ns, "g81_accept_o1", "Apply criteria to D_layer geometry input.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_D_layer_geometry_input_gate.py")

if __name__ == "__main__":
    main()
