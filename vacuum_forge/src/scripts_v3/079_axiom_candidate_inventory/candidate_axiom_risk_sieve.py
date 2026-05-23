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

DEPENDENCIES = [('g79_D_layer_axioms', '079_axiom_candidate_inventory__candidate_D_layer_axiom_candidates', 'g79_D_layer_axioms'), ('g79_lift_axioms', '079_axiom_candidate_inventory__candidate_lift_identity_axiom_candidates', 'g79_lift_axioms'), ('g79_rho_axioms', '079_axiom_candidate_inventory__candidate_rho_status_axiom_candidates', 'g79_rho_axioms')]
MARKER_ID = 'g79_risk_sieve'
def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header('Candidate Axiom Risk Sieve')
    print('Risk categories:')
    print('  - source_double_counting')
    print('  - trace_double_counting')
    print('  - mass_leakage')
    print('  - repair_paint')
    print('  - diagnostic_promotion')
    print('  - active_O_by_label')
    print('  - parent_jump')
    print('  - unvalidated_recombination')
    print('Safe requirements:')
    print('  - scope lock')
    print('  - role lock')
    print('  - payload purity')
    print('  - dependency order')
    print('  - future adoption decision')
    print('  - future validation tests')

    with out.governance_assessments():
        out.line('risk sieve', StatusMark.PASS, 'risk categories stated')
        out.line('safe requirements', StatusMark.PASS, 'safe requirements stated')
    with out.counterexamples():
        out.line('source/trace/mass risk', StatusMark.FAIL, 'must be blocked or explicitly validated before adoption')
        out.line('repair/diagnostic risk', StatusMark.FAIL, 'must remain quarantined')
        out.line('parent/recombination risk', StatusMark.FAIL, 'cannot be opened by axiom candidate')
    with out.unresolved_obligations():
        out.line('adoption surface', StatusMark.OBLIGATION, 'future adoption group must apply risk sieve')

    record_marker(ns, MARKER_ID, 'Group 79 marker: Candidate Axiom Risk Sieve')
    record_claim(ns, MARKER_ID, 'g79_g79_risk_sieve_1', GovernanceStatus.POLICY_RULE, 'Axiom candidates must pass risk sieve before any future adoption.')
    record_obligation(ns, 'g79_g79_risk_sieve_o1', 'future adoption group must apply risk sieve')
    ns.write_run_metadata()
    print('\nPossible next script:')
    print('  candidate_axiom_route_classifier.py')

if __name__ == '__main__':
    main()
