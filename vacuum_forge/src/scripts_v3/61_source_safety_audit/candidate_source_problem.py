from __future__ import annotations

from pathlib import Path
import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import RecordKind, ScriptOutput, StatusMark

ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / '.vacuumforge_archive'
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"
MARKER_ID = 'g61_problem'


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
    header('Candidate Source Safety Problem')
    print('Question: can the narrowed stress-only transition response remain source-clean?')
    print('Scope: source-safety audit only; no insertion, active O, recombination, or parent closure.')
    audit_output = sp.Symbol('g61_source_safety_problem_opened')

    header('Status lines')
    with out.governance_assessments():
        out.line('source audit opened', StatusMark.INFO, 'SOURCE_AUDIT_OPENED: audit the Group 60 survivor for source/mass role safety')
        out.line('source safety required', StatusMark.OBLIGATION, 'SOURCE_SAFETY_REQUIRED: weighted neutrality and incidence filtering are not a source theorem')
        out.line('physical use blocked', StatusMark.DEFER, 'PHYSICAL_USE_BLOCKED: no insertion or parent use opened')
    header('Final summary')
    print('Group 61 source-safety audit opened.')
    print('The target remains audit-only and non-insertable.')
    record_marker(ns, audit_output, 'Candidate Source Safety Problem')
    ns.write_run_metadata()
    print('\nPossible next script:')
    print('  candidate_role_separation.py')


if __name__ == '__main__':
    main()
