from __future__ import annotations

from pathlib import Path
import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import RecordKind, ScriptOutput, StatusMark

ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / '.vacuumforge_archive'
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"
MARKER_ID = 'g61_mass'


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
    ns.declare_dependency(dependency_id='g61_coupling', upstream_script_id='61_source_safety_audit__candidate_source_coupling', upstream_derivation_id='g61_coupling')
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
    header('Candidate Mass Moment')
    y, R, ell, p0, beta = sp.symbols('y R ell p0 beta', positive=True)
    c = sp.simplify(2*R*ell/(7*R**2 + ell**2))
    eta = sp.simplify((1-y**2)**2 * (y-c))
    p_r = sp.simplify(p0*eta**2)
    E_layer = sp.simplify(sp.integrate(p_r*ell, (y,-1,1)))
    delta_M = sp.simplify(beta*E_layer)
    print(f'E_layer = {sp.factor(E_layer)}')
    print(f'Delta_M = {sp.factor(delta_M)}')
    audit_output = delta_M

    header('Status lines')
    with out.governance_assessments():
        out.line('mass moment burden found', StatusMark.OBLIGATION, 'MASS_MOMENT_BURDEN_FOUND: stress-only response has nonzero reduced layer moment')
        out.line('mass coupled unsafe', StatusMark.FAIL, 'MASS_COUPLED_ROUTE_UNSAFE: beta != 0 would shift mass diagnostic')
        out.line('energy accounting required', StatusMark.OBLIGATION, 'ENERGY_ACCOUNTING_REQUIRED: layer stress cannot be treated as free or massless by naming')
    header('Final summary')
    print('The stress-only response has a nonzero reduced energy/mass-moment diagnostic.')
    print('If mass-coupled, it can shift mass; mass safety remains unproven.')
    record_marker(ns, audit_output, 'Candidate Mass Moment')
    ns.write_run_metadata()
    print('\nPossible next script:')
    print('  candidate_trace_mass_tension.py')


if __name__ == '__main__':
    main()
