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
    ("g76_exact_pair", "076_covariant_lift_identity_construction__candidate_exact_pair_scaffold", "g76_exact_pair"),
]
MARKER_ID = "g76_remainder"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    K, rho = sp.symbols("K rho")
    L_bulk = K
    L_gauge = -K + rho
    R_lift = sp.simplify(L_bulk + L_gauge)
    rho_solution = sp.solve(sp.Eq(R_lift, 0), rho)

    header("Candidate Remainder Obstruction Test")
    print(f"L_bulk = {L_bulk}")
    print(f"L_gauge = {L_gauge}")
    print(f"R_lift = {R_lift}")
    print(f"rho solution for closure = {rho_solution}")
    print()
    print("Interpretation:")
    print("  rho is the lift-identity obstruction unless a theorem proves rho=0 or inert/gauge-exact.")

    with out.derived_results():
        out.line("remainder residual", StatusMark.PASS, str(R_lift))
        out.line("closure condition", StatusMark.PASS, f"rho={rho_solution}")
    with out.governance_assessments():
        out.line("rho obstruction", StatusMark.OBLIGATION, "rho=0 must be derived")
        out.line("shared identity", StatusMark.INFO, "shared identity route remains open only if rho is controlled")
    with out.counterexamples():
        out.line("dropped rho", StatusMark.FAIL, "dropping rho by prose is repair-like")
        out.line("chosen rho zero", StatusMark.FAIL, "setting rho=0 by hand is compatibility, not theorem")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=R_lift,
        method="test shared lift identity with leftover remainder",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="remainder_obstruction_test",
        scope="remainder obstruction; not identity theorem",
    )
    record_claim(ns, MARKER_ID, "g76_rho_c1", GovernanceStatus.POLICY_RULE, "Remainder rho is a theorem burden, not droppable residue.")
    record_obligation(ns, "g76_rho_o1", "Derive rho=0 or inert/gauge-exact status.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_gauge_exact_remainder_test.py")

if __name__ == "__main__":
    main()
