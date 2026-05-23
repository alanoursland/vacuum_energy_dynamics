
from __future__ import annotations
from pathlib import Path
import sympy as sp
from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import ClaimRecord, ClaimTier, GovernanceStatus, ObligationStatus, ProofObligationRecord, RecordKind, ScriptOutput, StatusMark
ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"
def header(title):
    print(); print("="*120); print(title); print("="*120)
def prepare_archive(dependencies):
    archive=ProjectArchive(ARCHIVE_ROOT); ns=archive.script_namespace(SCRIPT_ID); invalidated=ns.check_source_invalidation(__file__)
    for dep_id, sid, did in dependencies:
        ns.declare_dependency(dependency_id=dep_id, upstream_script_id=sid, upstream_derivation_id=did)
    return archive, ns, invalidated
def print_archive_status(ns, invalidated):
    if invalidated: print("[INFO] Archive invalidated due to source change.")
    checks=ns.verify_dependencies()
    if not checks:
        print("[INFO] Archive dependencies: none declared."); return
    print("[INFO] Archive dependency check:")
    for check in checks: print(f"  - {check.dependency.dependency_id}: {check.status} ({check.message})")
def record_marker(ns, marker_id, scope):
    ns.record_derivation(derivation_id=marker_id, inputs=[], output=sp.Symbol(marker_id), method="inventory marker; no physical derivation", status=Status.DERIVED, record_kind=RecordKind.INVENTORY_MARKER, is_placeholder=True, scope=scope)
def record_claim(ns, marker_id, claim_id, status, statement):
    ns.record_claim(ClaimRecord(claim_id=claim_id, script_id=SCRIPT_ID, claim_kind=RecordKind.GOVERNANCE_CLAIM, tier=ClaimTier.CONSTRAINED, status=status, statement=statement, derivation_ids=[marker_id], obligation_ids=[]))
def record_obligation(ns, obligation_id, statement, status=ObligationStatus.OPEN):
    ns.record_obligation(ProofObligationRecord(obligation_id=obligation_id, script_id=SCRIPT_ID, title=obligation_id, status=status, required_by=[SCRIPT_ID], description=statement))

DEPENDENCIES=[("g68_summary","068_covariant_divergence_identity_attempt__candidate_group_68_status_summary","g68_summary"),("g69_problem","069_boundary_covariant_cancellation_attempt__candidate_boundary_covariant_problem","g69_problem")]
MARKER_ID="g69_condition"
def main():
    archive,ns,invalidated=prepare_archive(DEPENDENCIES); print_archive_status(ns,invalidated); out=ScriptOutput()
    D_jump,D_layer,D_tail=sp.symbols("D_jump D_layer D_tail"); L_bulk,L_boundary,L_gauge=sp.symbols("L_bulk L_boundary L_gauge")
    D_boundary=sp.simplify(D_jump+D_layer+D_tail); D_lift=sp.simplify(L_bulk+L_boundary+L_gauge); residual=sp.simplify(D_lift+D_boundary)
    header("Candidate O-Free Cancellation Condition"); print(f"D_boundary = {D_boundary}"); print(f"D_lift = {D_lift}"); print(f"O-free residual = {residual}")
    with out.derived_results():
        out.line("D_boundary decomposition",StatusMark.PASS,str(D_boundary)); out.line("D_lift decomposition",StatusMark.PASS,str(D_lift)); out.line("expanded O-free residual",StatusMark.PASS,str(residual))
    with out.unresolved_obligations(): out.line("structural matching",StatusMark.OBLIGATION,"derive residual=0 structurally, not by selected cancellation")
    ns.record_derivation(derivation_id=MARKER_ID,inputs=[],output=residual,method="expand D_lift + D_boundary into boundary/lift components",status=Status.DERIVED,record_kind=RecordKind.DERIVATION,result_type="o_free_cancellation_condition",scope="reduced divergence target; not parent identity theorem")
    record_claim(ns,MARKER_ID,"g69_condition_c1",GovernanceStatus.POLICY_RULE,"The O-free identity is now the expanded structural target residual=0.")
    record_obligation(ns,"g69_condition_o1","Prove the expanded residual vanishes by structural boundary-lift relation.")
    ns.write_run_metadata(); print("\nPossible next script:\n  candidate_boundary_lift_decomposition.py")
if __name__=="__main__": main()
