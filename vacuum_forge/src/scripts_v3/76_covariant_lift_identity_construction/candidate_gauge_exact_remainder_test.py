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
    ("g76_remainder", "76_covariant_lift_identity_construction__candidate_remainder_obstruction_test", "g76_remainder"),
]
MARKER_ID = "g76_gauge_exact"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    dXi, rho_phys, i_exact, i_phys = sp.symbols("dXi rho_phys i_exact i_phys")
    rho = sp.simplify(dXi*i_exact + rho_phys*i_phys)
    physical_remainder = sp.simplify(rho.subs({i_exact: 0}))
    exact_only = sp.simplify(rho.subs({i_exact: 1, i_phys: 0}))
    unresolved_physical = sp.simplify(rho.subs({i_exact: 1, i_phys: 1}))

    header("Candidate Gauge-Exact Remainder Test")
    print(f"rho = {rho}")
    print(f"exact-only remainder = {exact_only}")
    print(f"physical remainder after removing exact part = {physical_remainder}")
    print(f"unresolved exact+physical remainder = {unresolved_physical}")
    print()
    print("Interpretation:")
    print("  gauge-exact/inert removal is allowed only if the physical remainder vanishes by theorem.")

    with out.derived_results():
        out.line("rho decomposition", StatusMark.PASS, str(rho))
        out.line("physical remainder", StatusMark.PASS, str(physical_remainder))
    with out.governance_assessments():
        out.line("gauge-exact route", StatusMark.INFO, "retained only if exact part is proven nonphysical and physical remainder vanishes")
        out.line("physical remainder", StatusMark.OBLIGATION, "rho_phys=0 must be derived")
    with out.counterexamples():
        out.line("exact label by prose", StatusMark.FAIL, "calling rho gauge-exact is not proof")
        out.line("physical remainder", StatusMark.FAIL, f"unresolved remainder={unresolved_physical}")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=rho,
        method="decompose remainder into exact and physical pieces",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="gauge_exact_remainder_test",
        scope="remainder classification; not gauge theorem",
    )
    record_claim(ns, MARKER_ID, "g76_gauge_exact_c1", GovernanceStatus.POLICY_RULE, "Gauge-exact remainder route requires proof of exactness and zero physical remainder.")
    record_obligation(ns, "g76_gauge_exact_o1", "Derive exact/inert status and rho_phys=0.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_identity_vs_repair_sieve.py")

if __name__ == "__main__":
    main()
