from __future__ import annotations

from pathlib import Path
import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import RecordKind, ScriptOutput, StatusMark

ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / '.vacuumforge_archive'
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"
MARKER_ID = 'g61_exchange'


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
    ns.declare_dependency(dependency_id='g60_summary', upstream_script_id='060_term_exclusion_sieve__candidate_group_60_status_summary', upstream_derivation_id='g60_summary')
    ns.declare_dependency(dependency_id='g61_tension', upstream_script_id='061_source_safety_audit__candidate_trace_mass_tension', upstream_derivation_id='g61_tension')
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
    header('Candidate Conservation Exchange')
    D_A, D_layer, J_exchange = sp.symbols('D_A D_layer J_exchange')
    D_total = sp.simplify(D_A + D_layer + J_exchange)
    cases = {
        'separate silence': D_total.subs({D_A:0,D_layer:0,J_exchange:0}),
        'layer silence only': D_total.subs({D_layer:0,J_exchange:0}),
        'forced exchange repair': D_total.subs({J_exchange:-(D_A+D_layer)}),
    }
    print(f'D_total = {D_total}')
    for name, value in cases.items():
        print(f'{name}: {sp.simplify(value)}')
    audit_output = D_total

    header('Status lines')
    with out.governance_assessments():
        out.line('exchange filter applied', StatusMark.PASS, 'CONSERVATION_EXCHANGE_FILTER_APPLIED: reduced exchange accounting was audited')
        out.line('separate silence conditional', StatusMark.INFO, 'REDUCED_EXCHANGE_SILENCE_CONDITIONAL: D_A=D_layer=J=0 is safe only in reduced diagnostic')
        out.line('exchange repair rejected', StatusMark.FAIL, 'SOURCE_REPAIR_REJECTED: forced J cancellation is repair, not theorem')
        out.line('divergence identity required', StatusMark.OBLIGATION, 'DIVERGENCE_IDENTITY_REQUIRED: reduced D=0 is not covariant conservation')
    header('Final summary')
    print('Reduced D_layer=0 supports internal balance only.')
    print('It does not by itself prove source safety or covariant conservation.')
    record_marker(ns, audit_output, 'Candidate Conservation Exchange')
    ns.write_run_metadata()
    print('\nPossible next script:')
    print('  candidate_source_route_classifier.py')


if __name__ == '__main__':
    main()
