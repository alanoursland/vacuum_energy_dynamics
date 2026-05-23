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

DEPENDENCIES = [('g78_summary', '078_boundary_lift_split_obligation_ledger__candidate_group_78_status_summary', 'g78_summary')]
MARKER_ID = 'g79_problem'
def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header('Candidate Axiom Inventory Problem')
    print('Question:')
    print('  Which explicit axiom candidates could be considered later, and what would each one cost?')
    print('')
    print('Imported Group 78 status:')
    print('  concrete input required for future theorem attempts')
    print('  active O not forced')
    print('  parent divergence identity unproven')
    print('  recombination blocked')

    with out.governance_assessments():
        out.line('group opened', StatusMark.PASS, 'axiom-candidate inventory opened')
        out.line('not adoption', StatusMark.INFO, 'this group inventories candidates only')
        out.line('parent status', StatusMark.DEFER, 'parent equation remains blocked')
        out.line('recombination', StatusMark.DEFER, 'parent recombination remains blocked')
    with out.counterexamples():
        out.line('axiom by convenience', StatusMark.FAIL, 'candidate listing is not adoption')
        out.line('parent jump', StatusMark.FAIL, 'axiom inventory cannot write parent equation')
        out.line('active O by label', StatusMark.FAIL, 'active O remains unconstructed')
    with out.unresolved_obligations():
        out.line('criteria', StatusMark.OBLIGATION, 'state admissibility criteria for axiom candidates')
        out.line('candidate inventory', StatusMark.OBLIGATION, 'inventory D_layer, lift, rho, and parent-facing candidates')

    record_marker(ns, MARKER_ID, 'Group 79 marker: Candidate Axiom Inventory Problem')
    record_claim(ns, MARKER_ID, 'g79_g79_problem_1', GovernanceStatus.UNVERIFIED, 'Group 79 opens explicit axiom-candidate inventory; no adoption.')
    record_obligation(ns, 'g79_g79_problem_o1', 'state admissibility criteria for axiom candidates')
    record_obligation(ns, 'g79_g79_problem_o2', 'inventory D_layer, lift, rho, and parent-facing candidates')
    ns.write_run_metadata()
    print('\nPossible next script:')
    print('  candidate_axiom_admissibility_criteria.py')

if __name__ == '__main__':
    main()
