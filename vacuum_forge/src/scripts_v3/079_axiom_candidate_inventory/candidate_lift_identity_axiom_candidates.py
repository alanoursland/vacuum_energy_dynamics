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

DEPENDENCIES = [('g79_criteria', '079_axiom_candidate_inventory__candidate_axiom_admissibility_criteria', 'g79_criteria'), ('g79_D_layer_axioms', '079_axiom_candidate_inventory__candidate_D_layer_axiom_candidates', 'g79_D_layer_axioms')]
MARKER_ID = 'g79_lift_axioms'
def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header('Candidate Lift Identity Axiom Candidates')
    print('INDEPENDENT_LIFT_NEUTRALITY_AXIOM: candidate; L_bulk=0 and L_gauge=0 as explicit lift postulate')
    print('SHARED_LIFT_IDENTITY_AXIOM: candidate; bulk/gauge residues arise from common K with opposite signs')
    print('K_SIGN_ORIGIN_AXIOM: candidate; common K and orientation sign are postulated')
    print('CHOSEN_MUTUAL_CANCELLATION_AXIOM: rejected; would choose L_bulk=-L_gauge as repair')
    print('DROPPED_LIFT_RESIDUE_AXIOM: rejected; would omit a residue by declaration')

    K, rho = sp.symbols('K rho')
    shared_residual = sp.simplify(K + (-K + rho))
    exact_residual = sp.simplify(shared_residual.subs(rho, 0))
    print(f'shared residual with rho = {shared_residual}')
    print(f'exact residual if rho=0 = {exact_residual}')
    with out.derived_results():
        out.line('shared residual', StatusMark.PASS, str(shared_residual))
        out.line('exact residual', StatusMark.PASS, str(exact_residual))


    with out.governance_assessments():
        out.line('independent neutrality axiom', StatusMark.INFO, 'candidate only; not adopted')
        out.line('shared identity axiom', StatusMark.INFO, 'candidate only; not adopted')
        out.line('K/sign axiom', StatusMark.INFO, 'candidate only; not adopted')
    with out.counterexamples():
        out.line('chosen cancellation axiom', StatusMark.FAIL, 'repair-like mutual cancellation rejected')
        out.line('dropped residue axiom', StatusMark.FAIL, 'cannot drop L_bulk/L_gauge by axiom label')
    with out.unresolved_obligations():
        out.line('lift adoption decision', StatusMark.OBLIGATION, 'future adoption surface required before lift axiom use')

    record_marker(ns, MARKER_ID, 'Group 79 marker: Candidate Lift Identity Axiom Candidates')
    record_claim(ns, MARKER_ID, 'g79_g79_lift_axioms_1', GovernanceStatus.POLICY_RULE, 'Lift identity axiom candidates are inventoried but not adopted.')
    record_claim(ns, MARKER_ID, 'g79_g79_lift_axioms_2', GovernanceStatus.REJECTED_ROUTE, 'Chosen mutual cancellation and dropped lift residue axioms are rejected.')
    record_obligation(ns, 'g79_g79_lift_axioms_o1', 'future adoption surface required before lift axiom use')
    ns.write_run_metadata()
    print('\nPossible next script:')
    print('  candidate_rho_status_axiom_candidates.py')

if __name__ == '__main__':
    main()
