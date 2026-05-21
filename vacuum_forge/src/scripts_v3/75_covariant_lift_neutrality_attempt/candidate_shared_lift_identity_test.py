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
    ("g75_bulk", "75_covariant_lift_neutrality_attempt__candidate_bulk_neutrality_test", "g75_bulk"),
    ("g75_gauge", "75_covariant_lift_neutrality_attempt__candidate_gauge_neutrality_test", "g75_gauge"),
]
MARKER_ID = "g75_shared_identity"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    K, rho, sigma = sp.symbols("K rho sigma")
    L_bulk = sp.simplify(K)
    L_gauge = sp.simplify(-sigma * K + rho)
    R_lift = sp.simplify(L_bulk + L_gauge)
    strict_shared = sp.simplify(R_lift.subs({sigma: 1, rho: 0}))
    sigma_solution = sp.solve(sp.Eq(R_lift.subs(rho, 0), 0), sigma)
    header("Candidate Shared Lift Identity Test")
    print(f"L_bulk = {L_bulk}")
    print(f"L_gauge = {L_gauge}")
    print(f"R_lift = {R_lift}")
    print(f"strict shared identity residual (sigma=1, rho=0) = {strict_shared}")
    print(f"sigma solution if rho=0 = {sigma_solution}")
    print("\nInterpretation:")
    print("  shared identity compatibility exists if paired terms are produced with opposite sign and no remainder.")
    print("  Group 75 does not derive the shared generator K or prove rho=0.")
    with out.derived_results():
        out.line("shared residual", StatusMark.PASS, str(R_lift))
        out.line("strict shared residual", StatusMark.PASS, str(strict_shared))
        out.line("shared sign solution", StatusMark.PASS, str(sigma_solution))
    with out.governance_assessments():
        out.line("shared identity route", StatusMark.INFO, "retained only if K, sign, and zero remainder are derived")
        out.line("remainder", StatusMark.OBLIGATION, "rho=0 must be derived, not dropped")
    with out.counterexamples():
        out.line("chosen opposite sign", StatusMark.FAIL, "choosing sigma=1 is compatibility, not lift identity theorem")
        out.line("dropped remainder", StatusMark.FAIL, "dropping rho by prose is repair-like")
    ns.record_derivation(derivation_id=MARKER_ID, inputs=[], output=R_lift, method="test shared bulk/gauge lift identity ansatz", status=Status.DERIVED, record_kind=RecordKind.COMPATIBILITY_EXAMPLE, result_type="shared_lift_identity_test", scope="shared-identity compatibility; not lift theorem")
    record_claim(ns, MARKER_ID, "g75_shared_c1", GovernanceStatus.POLICY_RULE, "Shared lift cancellation is retained only if common lift identity derives paired signs and zero remainder.")
    record_obligation(ns, "g75_shared_o1", "Derive shared lift generator K and remainder rho=0.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_mutual_cancellation_discriminator.py")
if __name__ == "__main__":
    main()
