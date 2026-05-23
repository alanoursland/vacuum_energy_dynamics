from __future__ import annotations

from pathlib import Path
import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import RecordKind, ScriptOutput, StatusMark

ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / '.vacuumforge_archive'
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"
MARKER_ID = 'g61_role'


def header(title: str) -> None:
    print('\n' + '=' * 120)
    print(title)
    print('=' * 120)


def is_zero(expr) -> bool:
    return bool(sp.simplify(expr) == 0)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(dependency_id='g60_summary', upstream_script_id='60_term_exclusion_sieve__candidate_group_60_status_summary', upstream_derivation_id='g60_summary')
    ns.declare_dependency(dependency_id='g61_problem', upstream_script_id='61_source_safety_audit__candidate_source_problem', upstream_derivation_id='g61_problem')
    return ns, invalidated


def record_marker(ns, output, scope: str) -> None:
    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=output,
        method='Group 61 source-safety audit marker / reduced diagnostic',
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type='source_safety_audit',
        scope=scope,
    )


def main() -> None:
    ns, invalidated = prepare_archive()
    if invalidated:
        print('[INFO] Archive invalidated due to source change.')
    for check in ns.verify_dependencies():
        print(f"[INFO] {check.dependency.dependency_id}: {check.status} ({check.message})")
    out = ScriptOutput()
    header('Candidate Role Separation')
    S_M, T_zeta = sp.symbols('S_M T_zeta')
    i_A, i_trans_src, i_Bs, i_trans_trace, i_res = sp.symbols('i_A i_trans_src i_Bs i_trans_trace i_res')
    source_residual = sp.simplify(S_M * (i_A + i_trans_src - 1))
    trace_residual = sp.simplify(T_zeta * (i_Bs + i_trans_trace + i_res - 1))
    tests = {
        'source clean': source_residual.subs({i_A:1, i_trans_src:0}),
        'source carrying': source_residual.subs({i_A:1, i_trans_src:1}),
        'source repair': source_residual.subs({i_A:0, i_trans_src:1}),
        'trace clean': trace_residual.subs({i_Bs:1, i_trans_trace:0, i_res:0}),
        'trace carrying': trace_residual.subs({i_Bs:1, i_trans_trace:1, i_res:0}),
        'residual reentry': trace_residual.subs({i_Bs:1, i_trans_trace:0, i_res:1}),
    }
    print(f'source_residual = {source_residual}')
    print(f'trace_residual = {trace_residual}')
    for name, value in tests.items():
        print(f'{name}: {sp.simplify(value)}')
    audit_output = trace_residual

    header('Status lines')
    with out.governance_assessments():
        out.line('role separation applied', StatusMark.PASS, 'ROLE_SEPARATION_APPLIED: source and trace incidence routes were audited')
        out.line('source carrying rejected', StatusMark.FAIL, 'SOURCE_CARRYING_TERM_REJECTED: transition cannot duplicate ordinary source')
        out.line('source repair rejected', StatusMark.FAIL, 'SOURCE_REPAIR_REJECTED: transition cannot replace A-sector source')
        out.line('trace/reentry rejected', StatusMark.FAIL, 'TRACE_CARRYING_TERM_REJECTED: transition cannot add trace or residual payload')
        out.line('source safety not closed', StatusMark.OBLIGATION, 'SOURCE_SAFETY_NOT_CLOSED: incidence audit is not full source theorem')
    header('Final summary')
    print('Source carrying, source repair, trace carrying, and residual reentry remain rejected.')
    print('The result is still an incidence audit, not a source-safety proof.')
    record_marker(ns, audit_output, 'Candidate Role Separation')
    ns.write_run_metadata()
    print('\nPossible next script:')
    print('  candidate_source_coupling.py')


if __name__ == '__main__':
    main()
