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
    ("g79_summary", "079_axiom_candidate_inventory__candidate_group_79_status_summary", "g79_summary"),
    ("g80_problem", "080_axiom_adoption_decision_surface__candidate_adoption_surface_problem", "g80_problem"),
]
MARKER_ID = "g80_criteria"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    criteria = ["scope locked", "role locked", "payload purity accounted", "dependency order respected", "validation tests named", "downstream consequences explicit", "no repair behavior", "no diagnostic promotion", "no parent jump", "owner decision required for actual adoption"]
    header("Candidate Adoption Decision Criteria")
    print("Axiom candidate may be considered for future adoption decision only if:")
    for item in criteria: print(f"  - {item}")
    with out.governance_assessments():
        out.line("criteria", StatusMark.PASS, "adoption-decision criteria stated")
        out.line("owner decision", StatusMark.OBLIGATION, "actual adoption requires future owner decision")
        out.line("validation", StatusMark.OBLIGATION, "validation tests must be named before adoption")
    with out.counterexamples():
        out.line("repair adoption", StatusMark.FAIL, "repair behavior blocks adoption readiness")
        out.line("diagnostic promotion", StatusMark.FAIL, "diagnostic promotion blocks adoption readiness")
        out.line("parent jump", StatusMark.FAIL, "parent jump blocks adoption readiness")
    record_marker(ns, MARKER_ID, "adoption-decision criteria; no adoption")
    record_claim(ns, MARKER_ID, "g80_criteria_c1", GovernanceStatus.POLICY_RULE, "Future axiom adoption requires scope, role, validation, dependency, and no-repair criteria.")
    record_obligation(ns, "g80_criteria_o1", "Apply adoption criteria to D_layer candidates.")
    ns.write_run_metadata()
    print("\nPossible next script:\n  candidate_D_layer_axiom_decision_surface.py")
if __name__ == "__main__": main()
