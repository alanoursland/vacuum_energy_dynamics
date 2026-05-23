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
    ("g72_summary", "072_layer_term_legitimacy_audit__candidate_group_72_status_summary", "g72_summary"),
]
MARKER_ID = "g73_problem"


def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Layer Generator Construction Problem")
    print("Question:")
    print("  Can D_layer be derived from a legitimate boundary/layer geometry generator?")
    print()
    print("Imported Group 72 status:")
    print("  D_layer legitimacy not established")
    print("  diagnostic transition insertion rejected")
    print("  source/trace/mass payload routes rejected")
    print("  parent divergence identity unproven")

    with out.governance_assessments():
        out.line("group opened", StatusMark.PASS, "geometric layer-generator construction attempt opened")
        out.line("starting state", StatusMark.INFO, "Group 72 left D_layer as unresolved boundary-side blocker")
        out.line("parent status", StatusMark.DEFER, "parent equation remains blocked")
        out.line("recombination", StatusMark.DEFER, "parent recombination remains blocked")
    with out.counterexamples():
        out.line("diagnostic ghost", StatusMark.FAIL, "old diagnostic transition response cannot supply D_layer")
        out.line("layer by name", StatusMark.FAIL, "naming D_layer does not derive a geometric generator")
        out.line("active O escape", StatusMark.FAIL, "active O remains unconstructed and out of scope")
        out.line("parent construction", StatusMark.FAIL, "do not write parent equation during generator construction audit")
    with out.unresolved_obligations():
        out.line("generator criteria", StatusMark.OBLIGATION, "state legal geometric layer-generator requirements")
        out.line("candidate tests", StatusMark.OBLIGATION, "test support, measure, component membership, payload purity, and lift interface")

    record_marker(ns, MARKER_ID, "Group 73 opening; no parent equation")
    record_claim(ns, MARKER_ID, "g73_problem_c1", GovernanceStatus.UNVERIFIED, "Group 73 opens geometric D_layer generator construction attempt.")
    record_claim(ns, MARKER_ID, "g73_problem_c2", GovernanceStatus.REJECTED_ROUTE, "Diagnostic transition, layer-by-name, active-O, and parent-construction shortcuts remain rejected.")
    record_obligation(ns, "g73_problem_o1", "State legal geometric layer-generator requirements.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_geometric_layer_generator_requirements.py")


if __name__ == "__main__":
    main()
