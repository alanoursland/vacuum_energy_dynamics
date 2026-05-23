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
    ("g77_gauge_exact", "077_remainder_obstruction_audit__candidate_gauge_exact_classification_test", "g77_gauge_exact"),
]
MARKER_ID = "g77_boundary_exact"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    divB, rho_bulk, i_boundary, i_bulk = sp.symbols("divB rho_bulk i_boundary i_bulk")
    rho = sp.simplify(divB*i_boundary + rho_bulk*i_bulk)
    boundary_only = sp.simplify(rho.subs({i_boundary: 1, i_bulk: 0}))
    bulk_remainder = sp.simplify(rho.subs({i_boundary: 0, i_bulk: 1}))
    unresolved = sp.simplify(rho.subs({i_boundary: 1, i_bulk: 1}))

    header("Candidate Boundary Exactness Test")
    print(f"rho = {rho}")
    print(f"boundary-only route = {boundary_only}")
    print(f"bulk remainder = {bulk_remainder}")
    print(f"unresolved boundary+bulk = {unresolved}")
    print()
    print("Interpretation:")
    print("  boundary-exact status requires proof that boundary term has no physical bulk payload and rho_bulk=0.")

    with out.derived_results():
        out.line("rho boundary decomposition", StatusMark.PASS, str(rho))
        out.line("bulk remainder", StatusMark.PASS, str(bulk_remainder))
    with out.governance_assessments():
        out.line("boundary-exact route", StatusMark.INFO, "retained only if boundary exactness and zero bulk remainder are derived")
        out.line("rho_bulk", StatusMark.OBLIGATION, "rho_bulk=0 must be derived")
    with out.counterexamples():
        out.line("boundary label", StatusMark.FAIL, "calling rho boundary-exact is not proof")
        out.line("unresolved bulk", StatusMark.FAIL, f"unresolved={unresolved}")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=rho,
        method="decompose rho into boundary-exact and bulk physical pieces",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="boundary_exactness_test",
        scope="classification; not boundary theorem",
    )
    record_claim(ns, MARKER_ID, "g77_boundary_c1", GovernanceStatus.POLICY_RULE, "Boundary-exact rho removal requires proof of exactness and zero bulk remainder.")
    record_obligation(ns, "g77_boundary_o1", "Derive boundary-exact status and zero bulk remainder.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_physical_remainder_payload_test.py")

if __name__ == "__main__":
    main()
