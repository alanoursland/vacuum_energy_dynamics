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

DEPENDENCIES = [('g93_row_sign_matrix', '93_pivot_sign_theorem_attempt__candidate_row_sign_normalized_matrix', 'g93_row_sign_matrix'), ('g93_schur_pivots', '93_pivot_sign_theorem_attempt__candidate_schur_complement_pivot_identity', 'g93_schur_pivots'), ('g93_total_positivity', '93_pivot_sign_theorem_attempt__candidate_total_positivity_obstruction', 'g93_total_positivity'), ('g93_principal_minor_test', '93_pivot_sign_theorem_attempt__candidate_principal_minor_route_test', 'g93_principal_minor_test'), ('g93_leading_minor_table', '93_pivot_sign_theorem_attempt__candidate_positive_leading_minor_table', 'g93_leading_minor_table')]
MARKER_ID = 'g93_route_classifier'


def main():
    archive, ns, invalidated=prepare_archive(DEPENDENCIES); print_archive_status(ns, invalidated); out=ScriptOutput()
    classes=['ROW_SIGN_NORMALIZATION_DERIVED','SIGN_NORMALIZED_LEADING_MINORS_POSITIVE_N1_TO_N30','SIGN_NORMALIZED_PIVOTS_POSITIVE_N1_TO_N30','SCHUR_COMPLEMENT_PIVOT_IDENTITY_DERIVED','TOTAL_POSITIVITY_ROUTE_BLOCKED','PRINCIPAL_MINOR_ROUTE_TESTED_SMALL_N','ALL_ORDER_PIVOT_SIGN_THEOREM_OPEN','ALL_ORDER_NONZERO_DETERMINANT_THEOREM_OPEN','PARENT_DIVERGENCE_UNPROVEN','RECOMBINATION_BLOCKED']
    header('Candidate Pivot Sign Route Classifier')
    for c in classes: print(c)
    with out.governance_assessments():
        out.line('row-sign normalization', StatusMark.PASS, 'derived')
        out.line('Schur pivot identity', StatusMark.PASS, 'derived')
        out.line('total positivity', StatusMark.WARN, 'simple route blocked')
        out.line('all-order pivot theorem', StatusMark.OBLIGATION, 'not proven')
        out.line('parent divergence', StatusMark.OBLIGATION, 'parent divergence identity remains unproven')
        out.line('recombination', StatusMark.DEFER, 'recombination remains blocked')
    record_marker(ns, MARKER_ID, 'pivot sign route classifier')
    record_claim(ns, MARKER_ID, 'g93_class_c1', GovernanceStatus.POLICY_RULE, 'Group 93 reduces pivot sign theorem to row-signed leading Schur complement positivity.')
    record_claim(ns, MARKER_ID, 'g93_class_c2', GovernanceStatus.POLICY_RULE, 'Simple total positivity route is blocked; all-order Schur positivity remains open.')
    record_obligation(ns, 'g93_class_o1', 'Attempt Schur complement positivity theorem or biorthogonal construction next.')
    ns.write_run_metadata()
if __name__=='__main__': main()
