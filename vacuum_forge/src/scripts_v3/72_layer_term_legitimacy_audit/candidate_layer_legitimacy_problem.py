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
    ("g71_summary", "71_common_boundary_generator_search__candidate_group_71_status_summary", "g71_summary"),
]
MARKER_ID = "g72_problem"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Layer Term Legitimacy Problem")
    print("Question:")
    print("  Can D_layer be a legitimate boundary-generator component without reusing diagnostic transition response?")
    print()
    print("Imported Group 71 status:")
    print("  strong common generator not established in tested classes")
    print("  D_layer legitimacy unresolved")
    print("  L_bulk/L_gauge lift cleanliness open")
    print("  parent divergence identity unproven")

    with out.governance_assessments():
        out.line("group opened", StatusMark.PASS, "layer term legitimacy audit opened")
        out.line("starting state", StatusMark.INFO, "Group 71 split D_layer as the sharp boundary-side blocker")
        out.line("parent status", StatusMark.DEFER, "parent equation remains blocked")
        out.line("recombination", StatusMark.DEFER, "parent recombination remains blocked")
    with out.counterexamples():
        out.line("diagnostic transition", StatusMark.FAIL, "old diagnostic transition response cannot supply D_layer")
        out.line("D_layer by name", StatusMark.FAIL, "naming a layer component does not prove legitimacy")
        out.line("active O escape", StatusMark.FAIL, "active O remains unconstructed and out of scope")
        out.line("parent construction", StatusMark.FAIL, "do not write parent equation during legitimacy audit")
    with out.unresolved_obligations():
        out.line("legal D_layer criteria", StatusMark.OBLIGATION, "state what a legitimate layer component must satisfy")
        out.line("diagnostic exclusion", StatusMark.OBLIGATION, "separate boundary component from quarantined diagnostic transition")

    record_marker(ns, MARKER_ID, "Group 72 opening; no parent equation")
    record_claim(ns, MARKER_ID, "g72_problem_c1", GovernanceStatus.POLICY_RULE, "Group 72 opens D_layer legitimacy audit without physical insertion.")
    record_claim(ns, MARKER_ID, "g72_problem_c2", GovernanceStatus.REJECTED_ROUTE, "Diagnostic transition response cannot be promoted to D_layer.")
    record_obligation(ns, "g72_problem_o1", "Define legal D_layer criteria and test diagnostic exclusion.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_layer_component_requirements.py")

if __name__ == "__main__":
    main()
