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

DEPENDENCIES = [('g79_D_layer_axioms', '79_axiom_candidate_inventory__candidate_D_layer_axiom_candidates', 'g79_D_layer_axioms'), ('g79_lift_axioms', '79_axiom_candidate_inventory__candidate_lift_identity_axiom_candidates', 'g79_lift_axioms'), ('g79_rho_axioms', '79_axiom_candidate_inventory__candidate_rho_status_axiom_candidates', 'g79_rho_axioms'), ('g79_risk_sieve', '79_axiom_candidate_inventory__candidate_axiom_risk_sieve', 'g79_risk_sieve')]
MARKER_ID = 'g79_route_classifier'
def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header('Candidate Axiom Route Classifier')
    print('Final axiom route classification:')
    print('  AXIOM_CANDIDATES_INVENTORIED: stable')
    print('  NO_AXIOM_ADOPTED: stable')
    print('  HIGH_RISK_CANDIDATES_QUARANTINED: stable')
    print('  FUTURE_ADOPTION_DECISION_REQUIRED: stable')
    print('  PARENT_DIVERGENCE_UNPROVEN: stable')
    print('  RECOMBINATION_BLOCKED: stable')

    with out.governance_assessments():
        out.line('inventory', StatusMark.PASS, 'axiom candidates inventoried')
        out.line('adoption', StatusMark.DEFER, 'no axiom adopted')
        out.line('risk quarantine', StatusMark.PASS, 'high-risk shortcut axioms rejected/quarantined')
        out.line('future decision', StatusMark.OBLIGATION, 'future adoption decision required before use')
        out.line('parent divergence', StatusMark.OBLIGATION, 'parent divergence identity remains unproven')
        out.line('recombination', StatusMark.DEFER, 'parent recombination remains blocked')
    with out.counterexamples():
        out.line('candidate as adopted', StatusMark.FAIL, 'inventory cannot be treated as adoption')
        out.line('axiom as theorem', StatusMark.FAIL, 'axiom candidate is not derivation')
        out.line('parent jump', StatusMark.FAIL, 'parent equation remains forbidden')
    with out.unresolved_obligations():
        out.line('adoption surface', StatusMark.OBLIGATION, 'create future adoption-decision group if theory owner wants axioms')

    record_marker(ns, MARKER_ID, 'Group 79 marker: Candidate Axiom Route Classifier')
    record_claim(ns, MARKER_ID, 'g79_g79_route_classifier_1', GovernanceStatus.POLICY_RULE, 'Group 79 inventories axiom candidates but adopts none.')
    record_claim(ns, MARKER_ID, 'g79_g79_route_classifier_2', GovernanceStatus.REJECTED_ROUTE, 'High-risk shortcut axioms remain rejected/quarantined.')
    record_obligation(ns, 'g79_g79_route_classifier_o1', 'create future adoption-decision group if theory owner wants axioms')
    ns.write_run_metadata()
    print('\nPossible next script:')
    print('  candidate_group_79_status_summary.py')

if __name__ == '__main__':
    main()
