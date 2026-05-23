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

DEPENDENCIES = [('g79_problem', '079_axiom_candidate_inventory__candidate_axiom_inventory_problem', 'g79_problem')]
MARKER_ID = 'g79_criteria'
def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header('Candidate Axiom Admissibility Criteria')
    print('Legal axiom-candidate criteria:')
    print('  - scope explicit')
    print('  - role explicit')
    print('  - no source/trace/mass double-counting')
    print('  - not repair current')
    print('  - not diagnostic promotion')
    print('  - not active O by label')
    print('  - not parent recombination by itself')
    print('  - future validation obligations explicit')

    with out.governance_assessments():
        out.line('criteria', StatusMark.PASS, 'admissibility criteria stated')
        out.line('validation', StatusMark.OBLIGATION, 'candidate axiom requires future adoption/validation decision')
    with out.counterexamples():
        out.line('repair axiom', StatusMark.FAIL, 'axiom cannot be repair paint')
        out.line('diagnostic axiom', StatusMark.FAIL, 'diagnostic evidence cannot be promoted by declaration')
        out.line('parent axiom jump', StatusMark.FAIL, 'parent recombination cannot open by candidate listing')
    with out.unresolved_obligations():
        out.line('apply criteria', StatusMark.OBLIGATION, 'apply criteria to D_layer, lift, and rho candidates')

    record_marker(ns, MARKER_ID, 'Group 79 marker: Candidate Axiom Admissibility Criteria')
    record_claim(ns, MARKER_ID, 'g79_g79_criteria_1', GovernanceStatus.POLICY_RULE, 'Axiom candidates require explicit scope, role, risk, and validation obligations.')
    record_obligation(ns, 'g79_g79_criteria_o1', 'apply criteria to D_layer, lift, and rho candidates')
    ns.write_run_metadata()
    print('\nPossible next script:')
    print('  candidate_D_layer_axiom_candidates.py')

if __name__ == '__main__':
    main()
