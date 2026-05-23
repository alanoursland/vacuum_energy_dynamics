
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
    ("g69_summary", "069_boundary_covariant_cancellation_attempt__candidate_group_69_status_summary", "g69_summary"),
    ("g70_common_generator", "070_boundary_lift_matching_theorem_attempt__candidate_common_generator_ansatz", "g70_common_generator"),
]
MARKER_ID = "g70_orientation"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    B, L_bulk, L_gauge, sigma = sp.symbols("B L_bulk L_gauge sigma")
    residual = sp.simplify(L_bulk + L_gauge + (1 - sigma) * B)
    strict_residual = sp.simplify(residual.subs({L_bulk: 0, L_gauge: 0}))
    sigma_solution = sp.solve(sp.Eq(strict_residual, 0), sigma)

    header("Candidate Orientation Sign Sieve")
    print(f"residual = {residual}")
    print(f"strict residual with L_bulk=L_gauge=0 = {strict_residual}")
    print(f"sigma solution = {sigma_solution}")
    with out.derived_results():
        out.line("strict sign equation", StatusMark.PASS, str(sp.Eq(strict_residual, 0)))
        out.line("sigma solution", StatusMark.PASS, str(sigma_solution))
    with out.unresolved_obligations():
        out.line("orientation theorem", StatusMark.OBLIGATION, "sigma=1 must be derived, not assigned")
    with out.counterexamples():
        out.line("chosen sign", StatusMark.FAIL, "choosing sigma=1 by convenience is repair-like")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=sp.Integer(1),
        method="solve orientation sign requirement under bulk/gauge-neutral ansatz",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="orientation_sign_sieve",
        scope="sign requirement; not orientation theorem",
    )
    record_claim(ns, MARKER_ID, "g70_orientation_c1", GovernanceStatus.POLICY_RULE, "Boundary-lift anti-match requires sigma=1, but orientation theorem is not proved.")
    record_obligation(ns, "g70_orientation_o1", "Derive sigma=1 from boundary orientation/covariant lift convention.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_component_coefficient_matching.py")

if __name__ == "__main__":
    main()
