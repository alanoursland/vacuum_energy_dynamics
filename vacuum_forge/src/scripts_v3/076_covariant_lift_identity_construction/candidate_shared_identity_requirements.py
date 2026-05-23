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
    ("g75_summary", "75_covariant_lift_neutrality_attempt__candidate_group_75_status_summary", "g75_summary"),
    ("g76_problem", "76_covariant_lift_identity_construction__candidate_lift_identity_problem", "g76_problem"),
]
MARKER_ID = "g76_requirements"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    K, rho = sp.symbols("K rho")
    L_bulk = K
    L_gauge = -K + rho
    R_lift = sp.simplify(L_bulk + L_gauge)
    exact_pair_residual = sp.simplify(R_lift.subs(rho, 0))

    header("Candidate Shared Identity Requirements")
    print(f"L_bulk = {L_bulk}")
    print(f"L_gauge = {L_gauge}")
    print(f"R_lift = {R_lift}")
    print(f"exact-pair residual when rho=0 = {exact_pair_residual}")
    print()
    print("Legal shared identity requires:")
    print("  common generator K")
    print("  opposite sign relation")
    print("  rho = 0 or proven inert/gauge-exact")
    print()
    print("Rejected:")
    print("  free sign")
    print("  free coefficients")
    print("  dropped rho")
    print("  repair current")
    print("  active O by label")

    with out.derived_results():
        out.line("shared residual", StatusMark.PASS, str(R_lift))
        out.line("exact pair residual", StatusMark.PASS, str(exact_pair_residual))
    with out.governance_assessments():
        out.line("requirements", StatusMark.PASS, "shared identity requirements stated")
        out.line("rho", StatusMark.OBLIGATION, "rho=0 or inert/gauge-exact status must be derived")
    with out.counterexamples():
        out.line("dropped rho", StatusMark.FAIL, "rho cannot be dropped by prose")
        out.line("free sign", StatusMark.FAIL, "opposite sign must be derived")
        out.line("repair current", StatusMark.FAIL, "repair current is not shared identity")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=R_lift,
        method="state shared lift identity residual with remainder",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="shared_identity_requirements",
        scope="requirements; not lift identity theorem",
    )
    record_claim(ns, MARKER_ID, "g76_req_c1", GovernanceStatus.POLICY_RULE, "Shared lift identity requires common K, opposite sign, and zero/inert remainder.")
    record_obligation(ns, "g76_req_o1", "Test exact-pair scaffold.")
    record_obligation(ns, "g76_req_o2", "Test remainder obstruction.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_exact_pair_scaffold.py")

if __name__ == "__main__":
    main()
