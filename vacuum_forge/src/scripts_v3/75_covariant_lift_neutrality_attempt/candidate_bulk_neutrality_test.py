from __future__ import annotations
from pathlib import Path
import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    ClaimRecord, ClaimTier, GovernanceStatus, ObligationStatus,
    ProofObligationRecord, RecordKind, ScriptOutput, StatusMark,
)

ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"

def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)

def prepare_archive(dependencies):
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    for dep_id, upstream_script_id, upstream_derivation_id in dependencies:
        ns.declare_dependency(
            dependency_id=dep_id,
            upstream_script_id=upstream_script_id,
            upstream_derivation_id=upstream_derivation_id,
        )
    return archive, ns, invalidated

def print_archive_status(ns, invalidated: bool) -> None:
    if invalidated:
        print("[INFO] Archive invalidated due to source change.")
    checks = ns.verify_dependencies()
    if not checks:
        print("[INFO] Archive dependencies: none declared.")
        return
    print("[INFO] Archive dependency check:")
    for check in checks:
        print(f"  - {check.dependency.dependency_id}: {check.status} ({check.message})")

def record_marker(ns, marker_id: str, scope: str) -> None:
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[],
        output=sp.Symbol(marker_id),
        method="inventory marker; no physical derivation",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
        scope=scope,
    )

def record_claim(ns, marker_id: str, claim_id: str, status: GovernanceStatus, statement: str) -> None:
    ns.record_claim(
        ClaimRecord(
            claim_id=claim_id,
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=status,
            statement=statement,
            derivation_ids=[marker_id],
            obligation_ids=[],
        )
    )

def record_obligation(ns, obligation_id: str, statement: str, status: ObligationStatus = ObligationStatus.OPEN) -> None:
    ns.record_obligation(
        ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=obligation_id,
            status=status,
            required_by=[SCRIPT_ID],
            description=statement,
        )
    )

DEPENDENCIES = [("g75_requirements", "75_covariant_lift_neutrality_attempt__candidate_lift_cleanliness_requirements", "g75_requirements")]
MARKER_ID = "g75_bulk"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    B_bulk, i_bulk = sp.symbols("B_bulk i_bulk")
    L_bulk = sp.simplify(B_bulk * i_bulk)
    neutral_solution = sp.solve(sp.Eq(L_bulk, 0), i_bulk)
    assigned_neutral = sp.simplify(L_bulk.subs(i_bulk, 0))
    active_bulk = sp.simplify(L_bulk.subs(i_bulk, 1))
    header("Candidate Bulk Neutrality Test")
    print(f"L_bulk = {L_bulk}")
    print(f"solutions for i_bulk from L_bulk=0 = {neutral_solution}")
    print(f"assigned-neutral residual = {assigned_neutral}")
    print(f"active bulk residual = {active_bulk}")
    print("\nInterpretation:")
    print("  i_bulk=0 is compatibility unless covariant lift construction derives no bulk residue.")
    with out.derived_results():
        out.line("bulk residual", StatusMark.PASS, str(L_bulk))
        out.line("bulk neutrality solution", StatusMark.PASS, str(neutral_solution))
    with out.governance_assessments():
        out.line("bulk-neutral route", StatusMark.INFO, "retained only if no-bulk residue follows from covariant lift")
        out.line("bulk theorem", StatusMark.OBLIGATION, "derive i_bulk=0 or equivalent structural neutrality")
    with out.counterexamples():
        out.line("assigned no-bulk", StatusMark.FAIL, "setting i_bulk=0 by hand is compatibility, not theorem")
        out.line("active bulk", StatusMark.FAIL, f"active bulk residue={active_bulk}")
    ns.record_derivation(derivation_id=MARKER_ID, inputs=[], output=L_bulk, method="factor bulk residue into bulk incidence diagnostic", status=Status.DERIVED, record_kind=RecordKind.DERIVATION, result_type="bulk_neutrality_test", scope="bulk-neutrality compatibility; not lift theorem")
    record_claim(ns, MARKER_ID, "g75_bulk_c1", GovernanceStatus.POLICY_RULE, "Bulk neutrality requires derived no-bulk residue, not assigned i_bulk=0.")
    record_obligation(ns, "g75_bulk_o1", "Derive L_bulk=0 from covariant lift construction.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_gauge_neutrality_test.py")
if __name__ == "__main__":
    main()
