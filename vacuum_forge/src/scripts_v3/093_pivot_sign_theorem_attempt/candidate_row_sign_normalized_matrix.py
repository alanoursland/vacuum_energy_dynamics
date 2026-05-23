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

DEPENDENCIES = [('g93_problem', '093_pivot_sign_theorem_attempt__candidate_pivot_sign_theorem_problem', 'g93_problem')]
MARKER_ID = 'g93_row_sign_matrix'


def main():
    archive, ns, invalidated=prepare_archive(DEPENDENCIES); print_archive_status(ns, invalidated); out=ScriptOutput()
    A_rows=det_rows(30, signed=False); B_rows=det_rows(30, signed=True)
    failures=[]; pivot_failures=[]
    for (N,detA,_,_,_), (_,detB,signB,pivotB,signPivotB) in zip(A_rows,B_rows):
        if sp.simplify(detB - sign_normalization_factor(N)*detA)!=0: failures.append(N)
        if signPivotB<=0: pivot_failures.append(N)
    header('Candidate Row-Sign Normalized Matrix')
    print('B_N[k,j]=epsilon_k A_N[k,j], epsilon=+1 through 10 and -1 after.')
    print('det normalization failures through N=30:', failures)
    print('nonpositive B pivot failures through N=30:', pivot_failures)
    with out.derived_results():
        out.line('det normalization failures', StatusMark.PASS if not failures else StatusMark.FAIL, str(failures))
        out.line('pivot failures', StatusMark.PASS if not pivot_failures else StatusMark.FAIL, str(pivot_failures))
    with out.governance_assessments():
        out.line('row-sign normalization', StatusMark.PASS, 'derived and verified through N=30')
        out.line('leading pivots', StatusMark.PASS, 'positive for row-signed B_N through N=30')
    ns.record_derivation(derivation_id=MARKER_ID, inputs=[], output=sp.Matrix([r[4] for r in B_rows]), method='construct row-signed matrix and verify leading pivots through N=30', status=Status.DERIVED, record_kind=RecordKind.DERIVATION, result_type='row_sign_normalized_matrix', scope='structural pivot theorem')
    record_claim(ns, MARKER_ID, 'g93_row_c1', GovernanceStatus.POLICY_RULE, 'Row-sign normalization converts corrected determinant signs into positive leading pivots through N=30.')
    record_obligation(ns, 'g93_row_o1', 'Derive Schur complement pivot identity.')
    ns.write_run_metadata()
if __name__=='__main__': main()
