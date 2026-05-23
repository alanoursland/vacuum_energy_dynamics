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
    ("g74_summary", "74_boundary_lift_route_split_decision__candidate_group_74_status_summary", "g74_summary"),
    ("g75_problem", "75_covariant_lift_neutrality_attempt__candidate_lift_neutrality_problem", "g75_problem"),
]
MARKER_ID = "g75_requirements"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    L_bulk, L_gauge, K = sp.symbols("L_bulk L_gauge K")
    R_lift = sp.simplify(L_bulk + L_gauge)
    independent_neutral = sp.simplify(R_lift.subs({L_bulk: 0, L_gauge: 0}))
    shared_identity = sp.simplify(R_lift.subs({L_bulk: K, L_gauge: -K}))
    header("Candidate Lift Cleanliness Requirements")
    print(f"post-boundary residual R_lift = {R_lift}")
    print(f"independent neutrality residual = {independent_neutral}")
    print(f"shared identity compatibility residual = {shared_identity}")
    print()
    print("Legal lift-cleanliness closures:")
    print("  independent neutrality: L_bulk=0 and L_gauge=0")
    print("  lawful shared identity: L_bulk+L_gauge=0 derived from lift/gauge structure")
    print()
    print("Rejected closures:")
    print("  drop L_bulk/L_gauge by prose")
    print("  choose L_bulk=-L_gauge as repair")
    print("  hide repair current")
    print("  active O by label")
    with out.derived_results():
        out.line("lift residual", StatusMark.PASS, str(R_lift))
        out.line("independent neutral residual", StatusMark.PASS, str(independent_neutral))
        out.line("shared identity compatibility", StatusMark.PASS, str(shared_identity))
    with out.governance_assessments():
        out.line("requirements", StatusMark.PASS, "legal lift-cleanliness closure routes stated")
        out.line("shared identity", StatusMark.OBLIGATION, "shared cancellation requires derivation, not selection")
    with out.counterexamples():
        out.line("drop terms", StatusMark.FAIL, "dropping lift terms is not a theorem")
        out.line("repair mutual cancel", StatusMark.FAIL, "choosing L_bulk=-L_gauge is repair-like unless derived")
        out.line("active O", StatusMark.FAIL, "active O by label remains forbidden")
    ns.record_derivation(derivation_id=MARKER_ID, inputs=[], output=R_lift, method="state post-boundary lift residual and legal closure forms", status=Status.DERIVED, record_kind=RecordKind.DERIVATION, result_type="lift_cleanliness_requirements", scope="requirements; not neutrality theorem")
    record_claim(ns, MARKER_ID, "g75_req_c1", GovernanceStatus.POLICY_RULE, "Lift cleanliness requires independent neutrality or derived shared identity.")
    record_obligation(ns, "g75_req_o1", "Test independent bulk neutrality.")
    record_obligation(ns, "g75_req_o2", "Test independent gauge neutrality.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_bulk_neutrality_test.py")
if __name__ == "__main__":
    main()
