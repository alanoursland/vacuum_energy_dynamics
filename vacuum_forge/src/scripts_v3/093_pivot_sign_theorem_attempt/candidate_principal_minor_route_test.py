from __future__ import annotations
from pathlib import Path
import itertools
import sympy as sp
from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import ClaimRecord, ClaimTier, GovernanceStatus, ObligationStatus, ProofObligationRecord, RecordKind, ScriptOutput, StatusMark
ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"
def header(title: str):
    print("\n" + "="*120); print(title); print("="*120)
def prepare_archive(dependencies):
    archive=ProjectArchive(ARCHIVE_ROOT); ns=archive.script_namespace(SCRIPT_ID); invalidated=ns.check_source_invalidation(__file__)
    for dep_id, upstream_script_id, upstream_derivation_id in dependencies:
        ns.declare_dependency(dependency_id=dep_id, upstream_script_id=upstream_script_id, upstream_derivation_id=upstream_derivation_id)
    return archive, ns, invalidated
def print_archive_status(ns, invalidated):
    if invalidated: print('[INFO] Archive invalidated due to source change.')
    checks=ns.verify_dependencies()
    if not checks: print('[INFO] Archive dependencies: none declared.'); return
    print('[INFO] Archive dependency check:')
    for check in checks: print(f"  - {check.dependency.dependency_id}: {check.status} ({check.message})")
def record_marker(ns, marker_id, scope):
    ns.record_derivation(derivation_id=marker_id, inputs=[], output=sp.Symbol(marker_id), method='inventory marker; no physical derivation', status=Status.DERIVED, record_kind=RecordKind.INVENTORY_MARKER, is_placeholder=True, scope=scope)
def record_claim(ns, marker_id, claim_id, status, statement):
    ns.record_claim(ClaimRecord(claim_id=claim_id, script_id=SCRIPT_ID, claim_kind=RecordKind.GOVERNANCE_CLAIM, tier=ClaimTier.CONSTRAINED, status=status, statement=statement, derivation_ids=[marker_id], obligation_ids=[]))
def record_obligation(ns, obligation_id, statement, status=ObligationStatus.OPEN):
    ns.record_obligation(ProofObligationRecord(obligation_id=obligation_id, script_id=SCRIPT_ID, title=obligation_id, status=status, required_by=[SCRIPT_ID], description=statement))
def beta_moment(s):
    s=sp.sympify(s); return sp.Rational(768,1)/sp.prod(2*s+2*m+1 for m in range(5))
def hierarchy_matrix(N:int):
    A=sp.zeros(N,N)
    for k in range(1,N+1):
        r=sp.Rational(2*k-1,2*k+3)
        for j in range(1,N+1): A[k-1,j-1]=beta_moment(k+j)-r*beta_moment(k+j-1)
    return A
def row_epsilon(k:int): return sp.Integer(1 if k<=10 else -1)
def row_signed_matrix(N:int):
    A=hierarchy_matrix(N); B=sp.zeros(N,N)
    for k in range(1,N+1):
        for j in range(1,N+1): B[k-1,j-1]=row_epsilon(k)*A[k-1,j-1]
    return B
def det_rows(max_n:int, signed=False):
    rows=[]; prev=sp.Integer(1)
    for N in range(1,max_n+1):
        M=row_signed_matrix(N) if signed else hierarchy_matrix(N)
        d=sp.factor(M.det(method='bareiss')); p=sp.factor(d/prev); rows.append((N,d,sp.sign(d),p,sp.sign(p))); prev=d
    return rows
def sign_normalization_factor(N:int): return sp.Integer(1 if N<=10 else (-1 if N%2 else 1))

DEPENDENCIES = [('g93_total_positivity', '093_pivot_sign_theorem_attempt__candidate_total_positivity_obstruction', 'g93_total_positivity')]
MARKER_ID = 'g93_principal_minor_test'


def main():
    archive, ns, invalidated=prepare_archive(DEPENDENCIES); print_archive_status(ns, invalidated); out=ScriptOutput()
    bad=[]; tested=0; max_n=7
    for N in range(1,max_n+1):
        B=row_signed_matrix(N)
        for r in range(1,N+1):
            for idx in itertools.combinations(range(N), r):
                tested+=1; det_sub=sp.factor(B.extract(idx,idx).det(method='bareiss'))
                if det_sub<=0:
                    bad.append((N,tuple(i+1 for i in idx),det_sub)); break
            if bad: break
        if bad: break
    header('Candidate Principal Minor Route Test')
    print('tested count:', tested); print('first bad principal minor:', bad[:1])
    with out.derived_results():
        out.line('tested count', StatusMark.INFO, str(tested))
        out.line('first bad principal minor', StatusMark.WARN if bad else StatusMark.PASS, str(bad[:1]))
    with out.governance_assessments():
        out.line('P-matrix route', StatusMark.WARN if bad else StatusMark.INFO, 'blocked by small principal minor' if bad else 'not blocked in small range; unproven')
    record_marker(ns, MARKER_ID, 'principal minor route test')
    record_claim(ns, MARKER_ID, 'g93_pm_c1', GovernanceStatus.POLICY_RULE if bad else GovernanceStatus.UNVERIFIED, 'P-matrix route tested in small range.')
    record_obligation(ns, 'g93_pm_o1', 'Record leading minor table.')
    ns.write_run_metadata()
if __name__=='__main__': main()
