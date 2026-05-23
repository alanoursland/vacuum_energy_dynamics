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

DEPENDENCIES = [('g78_summary', '078_boundary_lift_split_obligation_ledger__candidate_group_78_status_summary', 'g78_summary'), ('g79_problem', '079_axiom_candidate_inventory__candidate_axiom_inventory_problem', 'g79_problem'), ('g79_criteria', '079_axiom_candidate_inventory__candidate_axiom_admissibility_criteria', 'g79_criteria'), ('g79_D_layer_axioms', '079_axiom_candidate_inventory__candidate_D_layer_axiom_candidates', 'g79_D_layer_axioms'), ('g79_lift_axioms', '079_axiom_candidate_inventory__candidate_lift_identity_axiom_candidates', 'g79_lift_axioms'), ('g79_rho_axioms', '079_axiom_candidate_inventory__candidate_rho_status_axiom_candidates', 'g79_rho_axioms'), ('g79_risk_sieve', '079_axiom_candidate_inventory__candidate_axiom_risk_sieve', 'g79_risk_sieve'), ('g79_route_classifier', '079_axiom_candidate_inventory__candidate_axiom_route_classifier', 'g79_route_classifier')]
MARKER_ID = 'g79_summary'
def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header('Candidate Group 79 Status Summary')
    print('Question:')
    print('  What explicit axiom candidates could be considered later, and what would each cost?')
    print('')
    print('Group 79 stable result:')
    print('  axiom admissibility criteria explicit')
    print('  D_layer axiom candidates inventoried')
    print('  lift identity axiom candidates inventoried')
    print('  rho status axiom candidates inventoried')
    print('  high-risk shortcut axioms rejected/quarantined')
    print('  no axiom adopted')
    print('  future adoption-decision group required before any axiom use')
    print('  parent divergence identity remains unproven')
    print('  recombination remains blocked')
    print('')
    print('Recommended next routes:')
    print('  if considering axioms: 80_axiom_adoption_decision_surface')
    print('  if concrete input appears: 80_concrete_geometry_input_handoff')
    print('  if active O is reconsidered: 80_active_O_necessity_or_rejection')
    print('  otherwise: pause boundary-lift theorem attempts until concrete input exists')

    with out.governance_assessments():
        out.line('criteria', StatusMark.PASS, 'axiom admissibility criteria stated')
        out.line('inventory', StatusMark.PASS, 'D_layer/lift/rho candidates inventoried')
        out.line('adoption', StatusMark.DEFER, 'no axiom adopted')
        out.line('risk quarantine', StatusMark.PASS, 'unsafe shortcuts rejected/quarantined')
        out.line('future decision', StatusMark.OBLIGATION, 'future adoption decision required before use')
        out.line('parent divergence', StatusMark.OBLIGATION, 'parent divergence identity remains unproven')
        out.line('recombination', StatusMark.DEFER, 'parent recombination remains blocked')
    with out.counterexamples():
        out.line('candidate as theorem', StatusMark.FAIL, 'axiom candidate is not derivation')
        out.line('candidate as adopted', StatusMark.FAIL, 'inventory is not adoption')
        out.line('repair axiom', StatusMark.FAIL, 'repair paint cannot be axiom shortcut')
        out.line('parent equation', StatusMark.FAIL, 'parent construction remains forbidden')
    with out.unresolved_obligations():
        out.line('adoption surface', StatusMark.OBLIGATION, 'write adoption-decision group only if theory owner wants explicit axioms')
        out.line('validation', StatusMark.OBLIGATION, 'future validation tests required for any adopted axiom')

    record_marker(ns, MARKER_ID, 'Group 79 marker: Candidate Group 79 Status Summary')
    record_claim(ns, MARKER_ID, 'g79_g79_summary_1', GovernanceStatus.POLICY_RULE, 'Group 79 inventories axiom candidates and adopts none.')
    record_claim(ns, MARKER_ID, 'g79_g79_summary_2', GovernanceStatus.REJECTED_ROUTE, 'Repair, diagnostic-promotion, dropped-rho, dropped-lift, active-O-label, and parent-jump axiom shortcuts are rejected.')
    record_obligation(ns, 'g79_g79_summary_o1', 'write adoption-decision group only if theory owner wants explicit axioms')
    record_obligation(ns, 'g79_g79_summary_o2', 'future validation tests required for any adopted axiom')
    ns.write_run_metadata()

if __name__ == '__main__':
    main()
