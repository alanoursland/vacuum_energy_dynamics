from __future__ import annotations

from pathlib import Path
import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import RecordKind, ScriptOutput, StatusMark

ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / '.vacuumforge_archive'
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"
MARKER_ID = 'g61_tension'


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
    ns.declare_dependency(dependency_id='g61_mass', upstream_script_id='61_source_safety_audit__candidate_mass_moment', upstream_derivation_id='g61_mass')
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
    header('Candidate Trace/Mass Tension')
    y, R, ell, p0, u = sp.symbols('y R ell p0 u', positive=True)
    c = sp.simplify(2*R*ell/(7*R**2 + ell**2))
    eta = sp.simplify((1-y**2)**2 * (y-c))
    r = sp.simplify(R + ell*y)
    p_r = sp.simplify(p0*eta**2)
    dp_dr = sp.simplify(sp.diff(p_r, y)/ell)
    p_t = sp.simplify(p_r + r*dp_dr/2)
    pressure_sum = sp.simplify(p_r + 2*p_t)
    trace_diag = sp.simplify(-u + pressure_sum)
    active_mass_diag = sp.simplify(u + pressure_sum)
    u_trace = sp.solve(sp.Eq(trace_diag,0), u)[0]
    u_mass = sp.solve(sp.Eq(active_mass_diag,0), u)[0]
    tension = sp.simplify(u_trace-u_mass)
    print(f'p_r + 2 p_t = {pressure_sum}')
    print(f'trace-free requires u = {u_trace}')
    print(f'active-mass-neutral requires u = {u_mass}')
    print(f'tension u_trace-u_mass = {tension}')
    audit_output = tension

    header('Status lines')
    with out.governance_assessments():
        out.line('trace free conditional', StatusMark.INFO, 'TRACE_FREE_CLOSURE_CONDITIONAL: trace-free closure requires u=p_r+2p_t')
        out.line('active mass neutral conditional', StatusMark.INFO, 'ACTIVE_MASS_NEUTRAL_CLOSURE_CONDITIONAL: active-mass-neutral closure requires u=-(p_r+2p_t)')
        out.line('trace mass tension found', StatusMark.OBLIGATION, 'TRACE_MASS_TENSION_FOUND: both closures require p_r+2p_t=0, not generic')
        out.line('source safety not closed', StatusMark.OBLIGATION, 'SOURCE_SAFETY_NOT_CLOSED: mass/trace safety remains open')
    header('Final summary')
    print('Trace-free and active-mass-neutral closures require opposite energy-density choices.')
    print('This exposes a real reduced closure tension, not a solved theorem.')
    record_marker(ns, audit_output, 'Candidate Trace/Mass Tension')
    ns.write_run_metadata()
    print('\nPossible next script:')
    print('  candidate_conservation_exchange.py')


if __name__ == '__main__':
    main()
