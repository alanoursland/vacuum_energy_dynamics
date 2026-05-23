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

DEPENDENCIES = [("g75_bulk", "075_covariant_lift_neutrality_attempt__candidate_bulk_neutrality_test", "g75_bulk")]
MARKER_ID = "g75_gauge"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    G_gauge, i_gauge, chi = sp.symbols("G_gauge i_gauge chi")
    L_gauge = sp.simplify(G_gauge * i_gauge)
    gauge_variation = sp.simplify(sp.diff(chi * L_gauge, chi))
    neutral_solution = sp.solve(sp.Eq(L_gauge, 0), i_gauge)
    assigned_neutral = sp.simplify(L_gauge.subs(i_gauge, 0))
    active_gauge = sp.simplify(L_gauge.subs(i_gauge, 1))
    header("Candidate Gauge Neutrality Test")
    print(f"L_gauge = {L_gauge}")
    print(f"gauge-parameter variation diagnostic = {gauge_variation}")
    print(f"solutions for i_gauge from L_gauge=0 = {neutral_solution}")
    print(f"assigned-neutral residual = {assigned_neutral}")
    print(f"active gauge residual = {active_gauge}")
    print("\nInterpretation:")
    print("  gauge residue may vanish only if gauge dependence is proven pure/inert or absent.")
    with out.derived_results():
        out.line("gauge residual", StatusMark.PASS, str(L_gauge))
        out.line("gauge variation diagnostic", StatusMark.PASS, str(gauge_variation))
        out.line("gauge neutrality solution", StatusMark.PASS, str(neutral_solution))
    with out.governance_assessments():
        out.line("gauge-neutral route", StatusMark.INFO, "retained only if gauge residue is derived pure/inert/absent")
        out.line("gauge theorem", StatusMark.OBLIGATION, "derive i_gauge=0 or a lawful gauge identity")
    with out.counterexamples():
        out.line("assigned gauge removal", StatusMark.FAIL, "setting i_gauge=0 by hand is compatibility, not theorem")
        out.line("active gauge residue", StatusMark.FAIL, f"active gauge residual={active_gauge}")
    ns.record_derivation(derivation_id=MARKER_ID, inputs=[], output=L_gauge, method="factor gauge residue into gauge incidence diagnostic", status=Status.DERIVED, record_kind=RecordKind.DERIVATION, result_type="gauge_neutrality_test", scope="gauge-neutrality compatibility; not gauge theorem")
    record_claim(ns, MARKER_ID, "g75_gauge_c1", GovernanceStatus.POLICY_RULE, "Gauge neutrality requires derived pure/inert/absent gauge residue, not assigned removal.")
    record_obligation(ns, "g75_gauge_o1", "Derive L_gauge=0 or lawful gauge identity.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_shared_lift_identity_test.py")
if __name__ == "__main__":
    main()
