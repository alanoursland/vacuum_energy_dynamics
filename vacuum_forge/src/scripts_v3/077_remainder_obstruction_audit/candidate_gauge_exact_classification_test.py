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
    ("g77_zero", "077_remainder_obstruction_audit__candidate_zero_remainder_theorem_test", "g77_zero"),
]
MARKER_ID = "g77_gauge_exact"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    dXi, rho_phys, i_exact, i_phys = sp.symbols("dXi rho_phys i_exact i_phys")
    rho = sp.simplify(dXi*i_exact + rho_phys*i_phys)
    exact_only = sp.simplify(rho.subs({i_exact: 1, i_phys: 0}))
    physical_only = sp.simplify(rho.subs({i_exact: 0, i_phys: 1}))
    physical_removed = sp.simplify(rho.subs({i_exact: 1, i_phys: 0}))
    unresolved = sp.simplify(rho.subs({i_exact: 1, i_phys: 1}))

    header("Candidate Gauge-Exact Classification Test")
    print(f"rho = {rho}")
    print(f"exact-only route = {exact_only}")
    print(f"physical-only remainder = {physical_only}")
    print(f"physical removed route = {physical_removed}")
    print(f"unresolved exact+physical = {unresolved}")
    print()
    print("Interpretation:")
    print("  gauge-exact status requires proof that dXi is nonphysical and rho_phys=0.")

    with out.derived_results():
        out.line("rho decomposition", StatusMark.PASS, str(rho))
        out.line("physical remainder", StatusMark.PASS, str(physical_only))
    with out.governance_assessments():
        out.line("gauge-exact route", StatusMark.INFO, "retained only if exactness and zero physical remainder are derived")
        out.line("rho_phys", StatusMark.OBLIGATION, "rho_phys=0 must be derived")
    with out.counterexamples():
        out.line("exact by label", StatusMark.FAIL, "calling dXi exact/nonphysical is not proof")
        out.line("unresolved physical", StatusMark.FAIL, f"unresolved={unresolved}")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=rho,
        method="decompose rho into gauge-exact and physical pieces",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="gauge_exact_classification_test",
        scope="classification; not gauge theorem",
    )
    record_claim(ns, MARKER_ID, "g77_gauge_c1", GovernanceStatus.POLICY_RULE, "Gauge-exact rho removal requires proof of exactness and rho_phys=0.")
    record_obligation(ns, "g77_gauge_o1", "Derive gauge-exact status and zero physical remainder.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_boundary_exactness_test.py")

if __name__ == "__main__":
    main()
