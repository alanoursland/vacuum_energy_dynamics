from __future__ import annotations

from pathlib import Path
import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import RecordKind, ScriptOutput, StatusMark

ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / '.vacuumforge_archive'
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"
MARKER_ID = 'g61_coupling'


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
    ns.declare_dependency(dependency_id='g61_role', upstream_script_id='61_source_safety_audit__candidate_role_separation', upstream_derivation_id='g61_role')
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
    header('Candidate Source Coupling')
    rho_M, p_free, lam, eta = sp.symbols('rho_M p_free lambda eta')
    p0 = sp.simplify(p_free + lam*rho_M)
    p_r = sp.simplify(p0 * eta**2)
    source_dependence = sp.diff(p_r, rho_M)
    lam_condition = sp.solve(sp.Eq(source_dependence, 0), lam)
    print(f'p0 = {p0}')
    print(f'p_r = {p_r}')
    print(f'd(p_r)/d(rho_M) = {source_dependence}')
    print(f'source-neutral condition = {lam_condition}')
    audit_output = source_dependence

    header('Status lines')
    with out.governance_assessments():
        out.line('source coupling rejected', StatusMark.FAIL, 'SOURCE_COUPLING_REJECTED: p0 depending on rho_M is hidden source dependence')
        out.line('lambda zero conditional', StatusMark.INFO, 'SOURCE_NEUTRAL_AMPLITUDE_CONDITIONAL: lambda=0 leaves source-independent amplitude only')
        out.line('amplitude origin open', StatusMark.OBLIGATION, 'ENERGY_ACCOUNTING_REQUIRED: p_free remains underived')
    header('Final summary')
    print('Direct matter-density coupling in p0 is rejected unless lambda=0.')
    print('A source-independent amplitude remains possible but underived.')
    record_marker(ns, audit_output, 'Candidate Source Coupling')
    ns.write_run_metadata()
    print('\nPossible next script:')
    print('  candidate_mass_moment.py')


if __name__ == '__main__':
    main()
