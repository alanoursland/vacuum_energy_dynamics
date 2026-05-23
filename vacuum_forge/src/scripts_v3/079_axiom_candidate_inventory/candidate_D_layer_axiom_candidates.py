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

DEPENDENCIES = [('g79_criteria', '79_axiom_candidate_inventory__candidate_axiom_admissibility_criteria', 'g79_criteria')]
MARKER_ID = 'g79_D_layer_axioms'
def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header('Candidate D_layer Axiom Candidates')
    print('D_LAYER_GEOMETRIC_COMPONENT_AXIOM: candidate; D_layer is a genuine boundary/layer geometric component')
    print('D_LAYER_COMPONENT_MEMBERSHIP_AXIOM: candidate; D_layer belongs to the same boundary object as jump/tail')
    print('D_LAYER_PAYLOAD_PURITY_AXIOM: candidate; D_layer carries no source/trace/mass/repair/O payload')
    print('DIAGNOSTIC_TRANSITION_LAYER_AXIOM: rejected; would promote old diagnostics into D_layer')
    print('REPAIR_LAYER_AXIOM: rejected; would choose layer term after leakage appears')

    with out.governance_assessments():
        out.line('geometric component', StatusMark.INFO, 'candidate only; not adopted')
        out.line('component membership', StatusMark.INFO, 'candidate only; not adopted')
        out.line('payload purity', StatusMark.INFO, 'candidate only; not adopted')
    with out.counterexamples():
        out.line('diagnostic transition axiom', StatusMark.FAIL, 'diagnostic transition remains excluded')
        out.line('repair layer axiom', StatusMark.FAIL, 'repair layer cannot be axiom candidate')
    with out.unresolved_obligations():
        out.line('D_layer adoption decision', StatusMark.OBLIGATION, 'future adoption surface required before any D_layer axiom use')

    record_marker(ns, MARKER_ID, 'Group 79 marker: Candidate D_layer Axiom Candidates')
    record_claim(ns, MARKER_ID, 'g79_g79_D_layer_axioms_1', GovernanceStatus.POLICY_RULE, 'D_layer axiom candidates are inventoried but not adopted.')
    record_claim(ns, MARKER_ID, 'g79_g79_D_layer_axioms_2', GovernanceStatus.REJECTED_ROUTE, 'Diagnostic transition and repair layer axioms are rejected.')
    record_obligation(ns, 'g79_g79_D_layer_axioms_o1', 'future adoption surface required before any D_layer axiom use')
    ns.write_run_metadata()
    print('\nPossible next script:')
    print('  candidate_lift_identity_axiom_candidates.py')

if __name__ == '__main__':
    main()
