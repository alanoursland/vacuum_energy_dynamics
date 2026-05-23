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

DEPENDENCIES = [('g79_lift_axioms', '079_axiom_candidate_inventory__candidate_lift_identity_axiom_candidates', 'g79_lift_axioms')]
MARKER_ID = 'g79_rho_axioms'
def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header('Candidate Rho Status Axiom Candidates')
    print('RHO_ZERO_AXIOM: candidate; rho=0 by explicit postulate')
    print('RHO_GAUGE_EXACT_AXIOM: candidate; rho=dXi and physical remainder vanishes')
    print('RHO_BOUNDARY_EXACT_AXIOM: candidate; rho=divB and bulk physical remainder vanishes')
    print('RHO_NO_PAYLOAD_AXIOM: candidate; rho carries no source/trace/mass/divergence payload')
    print('DROPPED_RHO_AXIOM: rejected; would erase rho without theorem/adoption')
    print('EXACT_BY_LABEL_AXIOM: rejected; would call rho exact without content')

    rho, rho_phys, dXi, divB = sp.symbols('rho rho_phys dXi divB')
    gauge_form = sp.simplify(dXi + rho_phys)
    boundary_form = sp.simplify(divB + rho_phys)
    print(f'gauge form = {gauge_form}')
    print(f'boundary form = {boundary_form}')
    with out.derived_results():
        out.line('gauge form', StatusMark.PASS, str(gauge_form))
        out.line('boundary form', StatusMark.PASS, str(boundary_form))


    with out.governance_assessments():
        out.line('rho zero axiom', StatusMark.INFO, 'candidate only; not adopted')
        out.line('rho exact axioms', StatusMark.INFO, 'candidates only; not adopted')
        out.line('rho no-payload axiom', StatusMark.INFO, 'candidate only; not adopted')
    with out.counterexamples():
        out.line('dropped rho axiom', StatusMark.FAIL, 'rho cannot be erased by informal label')
        out.line('exact by label axiom', StatusMark.FAIL, 'exactness requires content or explicit adoption surface')
    with out.unresolved_obligations():
        out.line('rho adoption decision', StatusMark.OBLIGATION, 'future adoption surface required before rho axiom use')

    record_marker(ns, MARKER_ID, 'Group 79 marker: Candidate Rho Status Axiom Candidates')
    record_claim(ns, MARKER_ID, 'g79_g79_rho_axioms_1', GovernanceStatus.POLICY_RULE, 'Rho status axiom candidates are inventoried but not adopted.')
    record_claim(ns, MARKER_ID, 'g79_g79_rho_axioms_2', GovernanceStatus.REJECTED_ROUTE, 'Dropped-rho and exact-by-label axioms are rejected.')
    record_obligation(ns, 'g79_g79_rho_axioms_o1', 'future adoption surface required before rho axiom use')
    ns.write_run_metadata()
    print('\nPossible next script:')
    print('  candidate_axiom_risk_sieve.py')

if __name__ == '__main__':
    main()
