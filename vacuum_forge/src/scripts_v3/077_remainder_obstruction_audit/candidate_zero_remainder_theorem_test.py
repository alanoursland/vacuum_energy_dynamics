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
    ("g77_requirements", "077_remainder_obstruction_audit__candidate_remainder_status_requirements", "g77_requirements"),
]
MARKER_ID = "g77_zero"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    c_rho, R0 = sp.symbols("c_rho R0")
    rho = sp.simplify(c_rho * R0)
    c_solution = sp.solve(sp.Eq(rho, 0), c_rho)
    R0_solution = sp.solve(sp.Eq(rho, 0), R0)
    assigned_zero = sp.simplify(rho.subs(c_rho, 0))
    active_remainder = sp.simplify(rho.subs(c_rho, 1))

    header("Candidate Zero Remainder Theorem Test")
    print(f"rho = {rho}")
    print(f"closure by c_rho solution = {c_solution}")
    print(f"closure by R0 solution = {R0_solution}")
    print(f"assigned-zero residual = {assigned_zero}")
    print(f"active remainder = {active_remainder}")
    print()
    print("Interpretation:")
    print("  zero remainder requires c_rho=0 or R0=0 by theorem, not assignment.")

    with out.derived_results():
        out.line("rho factorization", StatusMark.PASS, str(rho))
        out.line("c_rho closure", StatusMark.PASS, str(c_solution))
        out.line("R0 closure", StatusMark.PASS, str(R0_solution))
    with out.governance_assessments():
        out.line("zero route", StatusMark.INFO, "retained only if c_rho=0 or R0=0 is derived")
        out.line("zero theorem", StatusMark.OBLIGATION, "derive zero remainder from lift structure")
    with out.counterexamples():
        out.line("assigned zero", StatusMark.FAIL, "setting c_rho=0 by hand is compatibility, not theorem")
        out.line("active remainder", StatusMark.FAIL, f"active remainder={active_remainder}")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=rho,
        method="factor rho into coefficient and structural remainder",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="zero_remainder_test",
        scope="zero compatibility; not zero theorem",
    )
    record_claim(ns, MARKER_ID, "g77_zero_c1", GovernanceStatus.POLICY_RULE, "Zero remainder must be derived from c_rho=0 or R0=0 theorem, not assigned.")
    record_obligation(ns, "g77_zero_o1", "Derive c_rho=0 or R0=0 from lift structure if zero route continues.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_gauge_exact_classification_test.py")

if __name__ == "__main__":
    main()
