from __future__ import annotations

from pathlib import Path
import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import RecordKind, ScriptOutput, StatusMark

ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / '.vacuumforge_archive'
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"
MARKER_ID = 'g61_class'


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
    ns.declare_dependency(dependency_id='g61_coupling', upstream_script_id='61_source_safety_audit__candidate_source_coupling', upstream_derivation_id='g61_coupling')
    ns.declare_dependency(dependency_id='g61_mass', upstream_script_id='61_source_safety_audit__candidate_mass_moment', upstream_derivation_id='g61_mass')
    ns.declare_dependency(dependency_id='g61_tension', upstream_script_id='61_source_safety_audit__candidate_trace_mass_tension', upstream_derivation_id='g61_tension')
    ns.declare_dependency(dependency_id='g61_exchange', upstream_script_id='61_source_safety_audit__candidate_conservation_exchange', upstream_derivation_id='g61_exchange')
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
    header('Candidate Source Route Classifier')
    print('Classifier result: source safety is not closed.')
    print('Rejected: source repair, source carrying, trace/reentry, direct rho_M amplitude, mass-coupled route without theorem.')
    print('Retained only: source-independent stress-only transition response as audit material.')
    audit_output = sp.Symbol('g61_source_safety_not_closed')

    header('Status lines')
    with out.governance_assessments():
        out.line('source route classified', StatusMark.PASS, 'PASS: source safety status classified')
        out.line('unsafe routes rejected', StatusMark.FAIL, 'REJECTED_ROUTE: source-coupled, source-repair, source-carrying, trace/reentry, mass-coupled routes rejected or blocked')
        out.line('audit candidate retained', StatusMark.INFO, 'AUDIT_CANDIDATE_RETAINED: source-independent stress-only route remains audit-only')
        out.line('source safety not closed', StatusMark.OBLIGATION, 'SOURCE_SAFETY_NOT_CLOSED: theorem still required')
        out.line('physical use blocked', StatusMark.DEFER, 'PHYSICAL_USE_BLOCKED: no insertion or parent closure opened')
    header('Final summary')
    print('Group 61 classifies source safety as sharpened but not closed.')
    print('The candidate remains audit-only.')
    record_marker(ns, audit_output, 'Candidate Source Route Classifier')
    ns.write_run_metadata()
    print('\nPossible next script:')
    print('  candidate_source_batch_reconcile.py')


if __name__ == '__main__':
    main()
