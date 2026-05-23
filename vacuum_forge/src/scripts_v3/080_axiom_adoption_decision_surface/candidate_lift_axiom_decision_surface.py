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

DEPENDENCIES = [
    ("g79_lift_axioms", "079_axiom_candidate_inventory__candidate_lift_identity_axiom_candidates", "g79_lift_axioms"),
    ("g80_criteria", "080_axiom_adoption_decision_surface__candidate_adoption_decision_criteria", "g80_criteria"),
]
MARKER_ID = "g80_lift_surface"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    rho = sp.symbols("rho")
    shared_residual = sp.simplify(rho)
    exact_if_zero = sp.simplify(shared_residual.subs(rho, 0))
    rows = [("INDEPENDENT_LIFT_NEUTRALITY_AXIOM", "DEFERRED", "requires explicit postulate decision and validation"), ("SHARED_LIFT_IDENTITY_AXIOM", "DEFERRED", "requires K/sign origin and rho burden"), ("K_SIGN_ORIGIN_AXIOM", "DEFERRED", "requires orientation/sign risk decision"), ("CHOSEN_MUTUAL_CANCELLATION_AXIOM", "REJECTED", "repair-like mutual cancellation"), ("DROPPED_LIFT_RESIDUE_AXIOM", "REJECTED", "omits lift residue by declaration")]
    header("Candidate Lift Axiom Decision Surface")
    print(f"shared residual = {shared_residual}")
    print(f"exact if rho=0 = {exact_if_zero}")
    for name, status, reason in rows: print(f"{name}: {status}; {reason}")
    with out.derived_results():
        out.line("shared residual", StatusMark.PASS, str(shared_residual))
        out.line("exact residual if rho=0", StatusMark.PASS, str(exact_if_zero))
    with out.governance_assessments():
        out.line("independent neutrality axiom", StatusMark.DEFER, "deferred pending explicit postulate decision")
        out.line("shared identity axiom", StatusMark.DEFER, "deferred pending K/sign/rho handling")
        out.line("K/sign axiom", StatusMark.DEFER, "deferred pending orientation risk decision")
    with out.counterexamples():
        out.line("chosen mutual cancellation axiom", StatusMark.FAIL, "rejected shortcut")
        out.line("dropped lift residue axiom", StatusMark.FAIL, "rejected shortcut")
    with out.unresolved_obligations():
        out.line("lift validation", StatusMark.OBLIGATION, "future lift adoption decision must validate neutrality, K/sign origin, and rho handling")
    ns.record_derivation(derivation_id=MARKER_ID, inputs=[rho], output=shared_residual, method="record shared lift residual carried into decision surface", status=Status.DERIVED, record_kind=RecordKind.COMPATIBILITY_EXAMPLE, result_type="lift_axiom_decision_surface", scope="decision surface; no axiom adoption")
    record_claim(ns, MARKER_ID, "g80_lift_c1", GovernanceStatus.POLICY_RULE, "Lift axiom candidates are deferred; none are adopted.")
    record_claim(ns, MARKER_ID, "g80_lift_c2", GovernanceStatus.REJECTED_ROUTE, "Chosen cancellation and dropped residue axiom shortcuts remain rejected.")
    record_obligation(ns, "g80_lift_o1", "Future lift adoption decision must address K/sign/rho and validation.")
    ns.write_run_metadata()
    print("\nPossible next script:\n  candidate_rho_axiom_decision_surface.py")
if __name__ == "__main__": main()
