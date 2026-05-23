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
    ("g81_acceptance", "081_concrete_geometry_input_handoff__candidate_concrete_input_acceptance_criteria", "g81_acceptance"),
]
MARKER_ID = "g81_dlayer_gate"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    accepted = [
        "boundary/layer geometry object",
        "support/measure/orientation data",
        "component membership claim",
        "payload-purity test",
        "boundary match participation target",
    ]
    rejected = [
        "diagnostic transition response",
        "repair layer",
        "D_layer by name",
        "old window profile without physical role",
        "membership by flag only",
    ]

    header("Candidate D_layer Geometry Input Gate")
    print("D_layer route accepted input:")
    for item in accepted:
        print(f"  - {item}")
    print("D_layer route rejected input:")
    for item in rejected:
        print(f"  - {item}")

    with out.governance_assessments():
        out.line("D_layer gate", StatusMark.PASS, "D_layer concrete-input gate stated")
        out.line("geometry object", StatusMark.OBLIGATION, "future D_layer test requires concrete geometry")
        out.line("payload purity", StatusMark.OBLIGATION, "future D_layer test requires payload-purity test")
    with out.counterexamples():
        for item in rejected:
            out.line(item, StatusMark.FAIL, "not acceptable D_layer concrete input")

    record_marker(ns, MARKER_ID, "D_layer input gate; no D_layer theorem")
    record_claim(ns, MARKER_ID, "g81_dlayer_c1", GovernanceStatus.POLICY_RULE, "D_layer theorem attempt requires concrete geometry, membership, and payload tests.")
    record_claim(ns, MARKER_ID, "g81_dlayer_c2", GovernanceStatus.REJECTED_ROUTE, "Diagnostic, repair, name-only, and flag-only layer inputs are rejected.")
    record_obligation(ns, "g81_dlayer_o1", "Provide concrete D_layer geometry before D_layer theorem attempt.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_lift_identity_input_gate.py")

if __name__ == "__main__":
    main()
