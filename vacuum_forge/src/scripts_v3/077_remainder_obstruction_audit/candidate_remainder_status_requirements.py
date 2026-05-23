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
    ("g76_summary", "76_covariant_lift_identity_construction__candidate_group_76_status_summary", "g76_summary"),
    ("g77_problem", "77_remainder_obstruction_audit__candidate_remainder_audit_problem", "g77_problem"),
]
MARKER_ID = "g77_requirements"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    rho, rho_phys, dXi, divB = sp.symbols("rho rho_phys dXi divB")
    zero_status = sp.simplify(rho.subs(rho, 0))
    gauge_form = sp.simplify(dXi + rho_phys)
    boundary_form = sp.simplify(divB + rho_phys)

    header("Candidate Remainder Status Requirements")
    print("Legal rho statuses:")
    print("  ZERO_DERIVED: rho=0 by theorem")
    print("  GAUGE_EXACT: rho=dXi and physical remainder vanishes")
    print("  BOUNDARY_EXACT: rho=div_boundary(Pi) and physical bulk remainder vanishes")
    print("  INERT: rho carries no source/trace/mass/divergence payload by theorem")
    print("  PHYSICAL_REMAINDER: rho_phys remains")
    print("  UNRESOLVED: no theorem status derived")
    print()
    print(f"zero status residual = {zero_status}")
    print(f"gauge-exact form = {gauge_form}")
    print(f"boundary-exact form = {boundary_form}")

    with out.derived_results():
        out.line("zero residual form", StatusMark.PASS, str(zero_status))
        out.line("gauge form", StatusMark.PASS, str(gauge_form))
        out.line("boundary form", StatusMark.PASS, str(boundary_form))
    with out.governance_assessments():
        out.line("requirements", StatusMark.PASS, "legal rho status requirements stated")
        out.line("physical remainder", StatusMark.OBLIGATION, "rho_phys must vanish or be proven inert for exact routes")
    with out.counterexamples():
        out.line("status by label", StatusMark.FAIL, "naming rho exact/inert is not proof")
        out.line("dropped rho", StatusMark.FAIL, "dropping rho is not a legal status")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=gauge_form,
        method="state legal rho status forms",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="rho_status_requirements",
        scope="requirements; not rho theorem",
    )
    record_claim(ns, MARKER_ID, "g77_req_c1", GovernanceStatus.POLICY_RULE, "Rho must be zero, exact/inert with no physical remainder, physical, or unresolved.")
    record_obligation(ns, "g77_req_o1", "Test zero-remainder theorem route.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_zero_remainder_theorem_test.py")

if __name__ == "__main__":
    main()
