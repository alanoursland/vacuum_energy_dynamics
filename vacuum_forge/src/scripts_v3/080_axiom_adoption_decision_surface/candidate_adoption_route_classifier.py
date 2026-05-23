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
    ("g80_D_layer_surface", "080_axiom_adoption_decision_surface__candidate_D_layer_axiom_decision_surface", "g80_D_layer_surface"),
    ("g80_lift_surface", "080_axiom_adoption_decision_surface__candidate_lift_axiom_decision_surface", "g80_lift_surface"),
    ("g80_rho_surface", "080_axiom_adoption_decision_surface__candidate_rho_axiom_decision_surface", "g80_rho_surface"),
    ("g80_parent_gate", "080_axiom_adoption_decision_surface__candidate_parent_facing_axiom_gate", "g80_parent_gate"),
]
MARKER_ID = "g80_route_classifier"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    classifications = [("AXIOM_DECISION_SURFACE_BUILT", "stable", "D_layer, lift, rho, and parent gates classified"), ("NO_AXIOM_ADOPTED", "stable", "Group 80 does not adopt axioms"), ("NO_AXIOM_READY_FOR_ADOPTION", "stable", "all admissible candidates still require owner decision and validation"), ("DEFERRED_CANDIDATES_RETAINED", "stable", "D_layer/lift/rho candidates retained for possible future decision"), ("SHORTCUT_AXIOMS_REJECTED", "stable", "diagnostic/repair/drop/exact-label shortcuts rejected"), ("FUTURE_OWNER_DECISION_REQUIRED", "stable", "adoption requires explicit future owner decision"), ("PARENT_DIVERGENCE_UNPROVEN", "stable", "parent identity remains blocked"), ("RECOMBINATION_BLOCKED", "stable", "no recombination license")]
    header("Candidate Axiom Adoption Route Classifier")
    print("Final adoption decision-surface classification:")
    for name, status, reason in classifications: print(f"  {name}: {status}; {reason}")
    with out.governance_assessments():
        out.line("decision surface", StatusMark.PASS, "axiom decision surface built")
        out.line("adoption", StatusMark.DEFER, "no axiom adopted")
        out.line("readiness", StatusMark.DEFER, "no axiom ready for adoption in this group")
        out.line("deferred candidates", StatusMark.INFO, "candidate families retained for future decision")
        out.line("shortcut rejection", StatusMark.PASS, "unsafe shortcuts rejected")
        out.line("future owner decision", StatusMark.OBLIGATION, "explicit future owner decision required")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "recombination remains blocked")
    with out.counterexamples():
        out.line("candidate as adopted", StatusMark.FAIL, "candidate cannot be used as adopted axiom")
        out.line("owner decision as theorem", StatusMark.FAIL, "owner decision would not be derivation")
        out.line("parent jump", StatusMark.FAIL, "parent equation remains forbidden")
    with out.unresolved_obligations():
        out.line("adoption decision", StatusMark.OBLIGATION, "future group required for any actual adoption")
        out.line("validation", StatusMark.OBLIGATION, "future validation tests required for any adopted axiom")
    record_marker(ns, MARKER_ID, "axiom adoption route classifier; no adoption")
    record_claim(ns, MARKER_ID, "g80_class_c1", GovernanceStatus.POLICY_RULE, "Group 80 builds decision surface but adopts no axiom.")
    record_claim(ns, MARKER_ID, "g80_class_c2", GovernanceStatus.REJECTED_ROUTE, "Shortcut axiom routes remain rejected.")
    record_obligation(ns, "g80_class_o1", "Explicit future owner decision required before any axiom use.")
    ns.write_run_metadata()
    print("\nPossible next script:\n  candidate_group_80_status_summary.py")
if __name__ == "__main__": main()
