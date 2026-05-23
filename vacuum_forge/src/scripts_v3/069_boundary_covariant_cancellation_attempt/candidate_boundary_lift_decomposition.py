
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

DEPENDENCIES=[("g68_summary","68_covariant_divergence_identity_attempt__candidate_group_68_status_summary","g68_summary"),("g69_condition","69_boundary_covariant_cancellation_attempt__candidate_o_free_cancellation_condition","g69_condition")]
MARKER_ID="g69_decomp"
def main():
    archive,ns,invalidated=prepare_archive(DEPENDENCIES); print_archive_status(ns,invalidated); out=ScriptOutput(); header("Candidate Boundary/Lift Decomposition")
    roles=[("D_jump","matching discontinuity / boundary flux burden","must vanish or match structurally"),("D_layer","transition-layer burden","diagnostic-only unless derived as physical boundary term"),("D_tail","exterior tail / far-zone scalar leakage burden","must vanish or match structurally"),("L_bulk","bulk covariant lift mismatch","must vanish for pure boundary matching route"),("L_boundary","lift-induced boundary term","only legitimate matching carrier if derived"),("L_gauge","gauge/reduction mismatch","must vanish or be controlled by covariant reduction")]
    with out.governance_assessments():
        for name,role,req in roles:
            print(f"{name}: {role}; {req}"); out.line(name,StatusMark.INFO,f"{role}; {req}")
    with out.unresolved_obligations(): out.line("component theorems",StatusMark.OBLIGATION,"component roles are identified but not proven neutral")
    record_marker(ns,MARKER_ID,"component-role decomposition; no cancellation theorem")
    for i,(name,role,req) in enumerate(roles,1): record_claim(ns,MARKER_ID,f"g69_decomp_c{i}",GovernanceStatus.UNVERIFIED,f"{name}: {role}; requirement: {req}.")
    record_obligation(ns,"g69_decomp_o1","Test whether components can cancel generically under independence."); ns.write_run_metadata(); print("\nPossible next script:\n  candidate_generic_independence_no_go.py")
if __name__=="__main__": main()
