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

DEPENDENCIES = [("g79_summary", "79_axiom_candidate_inventory__candidate_group_79_status_summary", "g79_summary")]
MARKER_ID = "g80_problem"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    header("Candidate Axiom Adoption Decision Surface Problem")
    print("Question: Which axiom candidates are admissible for a future adoption decision, and which are deferred or rejected?")
    print("Imported Group 79 status:")
    for line in [
        "axiom candidates inventoried", "no axiom adopted", "future adoption-decision group required before any axiom use",
        "high-risk shortcuts rejected/quarantined", "parent divergence identity unproven", "recombination blocked",
    ]:
        print(f"  {line}")
    print("Group 80 builds a decision surface. It does not adopt axioms.")
    with out.governance_assessments():
        out.line("group opened", StatusMark.PASS, "axiom adoption-decision surface opened")
        out.line("no adoption", StatusMark.DEFER, "no axiom can be adopted in this group")
        out.line("parent status", StatusMark.DEFER, "parent equation remains blocked")
        out.line("recombination", StatusMark.DEFER, "parent recombination remains blocked")
    with out.counterexamples():
        out.line("candidate as adopted", StatusMark.FAIL, "candidate status cannot become adopted status")
        out.line("decision surface as theorem", StatusMark.FAIL, "decision surface is not derivation")
        out.line("parent jump", StatusMark.FAIL, "axiom decision surface cannot write parent equation")
    with out.unresolved_obligations():
        out.line("decision criteria", StatusMark.OBLIGATION, "state adoption-decision criteria")
        out.line("candidate classification", StatusMark.OBLIGATION, "classify D_layer, lift, and rho candidates")
    record_marker(ns, MARKER_ID, "Group 80 opening; decision surface only")
    record_claim(ns, MARKER_ID, "g80_problem_c1", GovernanceStatus.UNVERIFIED, "Group 80 opens axiom adoption-decision surface; no adoption.")
    record_obligation(ns, "g80_problem_o1", "State adoption-decision criteria.")
    ns.write_run_metadata()
    print("\nPossible next script:\n  candidate_adoption_decision_criteria.py")
if __name__ == "__main__": main()
