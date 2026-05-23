
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

DEPENDENCIES=[("g68_summary","068_covariant_divergence_identity_attempt__candidate_group_68_status_summary","g68_summary"),("g69_struct","069_boundary_covariant_cancellation_attempt__candidate_structural_matching_route","g69_struct")]
MARKER_ID="g69_reject"
def main():
    archive,ns,invalidated=prepare_archive(DEPENDENCIES); print_archive_status(ns,invalidated); out=ScriptOutput()
    D_jump,D_layer,D_tail=sp.symbols("D_jump D_layer D_tail"); L_boundary,L_bulk,L_gauge=sp.symbols("L_boundary L_bulk L_gauge")
    forced_layer=sp.solve(sp.Eq(D_jump+D_layer+D_tail,0),D_layer)[0]; forced_lift=sp.solve(sp.Eq(L_bulk+L_boundary+L_gauge+D_jump+D_layer+D_tail,0),L_boundary)[0]
    header("Candidate Layer/Lift Repair Rejection"); print(f"forced layer cancellation: D_layer = {forced_layer}"); print(f"forced lift-boundary cancellation: L_boundary = {forced_lift}")
    with out.counterexamples(): out.line("forced layer cancellation",StatusMark.FAIL,f"D_layer={forced_layer}; repair-like unless derived"); out.line("forced lift-boundary cancellation",StatusMark.FAIL,f"L_boundary={forced_lift}; repair-like unless derived"); out.line("diagnostic transition layer",StatusMark.FAIL,"diagnostic transition response cannot supply D_layer")
    with out.unresolved_obligations(): out.line("structural exception",StatusMark.OBLIGATION,"derive the matching from shared boundary/lift geometry if this route is to survive")
    ns.record_derivation(derivation_id=MARKER_ID,inputs=[],output=forced_lift,method="derive free layer/lift cancellation choices and classify as repair-like",status=Status.DERIVED,record_kind=RecordKind.DERIVATION,result_type="layer_lift_repair_rejection",scope="repair rejection; no matching theorem")
    record_claim(ns,MARKER_ID,"g69_reject_c1",GovernanceStatus.REJECTED_ROUTE,"Free layer and lift-boundary cancellation choices are repair-like and rejected.")
    record_obligation(ns,"g69_reject_o1","A structural matching theorem is required for any legitimate boundary/lift cancellation."); ns.write_run_metadata(); print("\nPossible next script:\n  candidate_boundary_covariant_route_classifier.py")
if __name__=="__main__": main()
