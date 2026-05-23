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
]
MARKER_ID = "g81_problem"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Concrete Input Handoff Problem")
    print("Question: What concrete input is required before theorem attempts resume?")
    print("Imported Group 80 status:")
    print("  no axiom adopted")
    print("  no axiom ready for adoption inside Group 80")
    print("  future owner decision required before axiom use")
    print("  parent divergence identity unproven")
    print("  recombination blocked")
    print("Group 81 boundary: build handoff gates only; do not prove or adopt.")

    with out.governance_assessments():
        out.line("group opened", StatusMark.PASS, "concrete-input handoff gate opened")
        out.line("no theorem", StatusMark.DEFER, "no theorem attempt starts in this group")
        out.line("no axiom", StatusMark.DEFER, "no axiom adoption in this group")
        out.line("parent status", StatusMark.DEFER, "parent equation remains blocked")
    with out.counterexamples():
        out.line("label as input", StatusMark.FAIL, "labels alone are not concrete input")
        out.line("scaffold as theorem", StatusMark.FAIL, "compatibility scaffold is not theorem input by itself")
        out.line("parent jump", StatusMark.FAIL, "handoff gate cannot write parent equation")
    with out.unresolved_obligations():
        out.line("input criteria", StatusMark.OBLIGATION, "define concrete input acceptance criteria")
        out.line("route gates", StatusMark.OBLIGATION, "define D_layer/lift/rho/parent/active-O gates")

    record_marker(ns, MARKER_ID, "Group 81 opening; concrete input handoff only")
    record_claim(ns, MARKER_ID, "g81_problem_c1", GovernanceStatus.UNVERIFIED, "Group 81 opens concrete-input handoff gate; no theorem or axiom adoption.")
    record_obligation(ns, "g81_problem_o1", "Define concrete input acceptance criteria.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_concrete_input_acceptance_criteria.py")

if __name__ == "__main__":
    main()
