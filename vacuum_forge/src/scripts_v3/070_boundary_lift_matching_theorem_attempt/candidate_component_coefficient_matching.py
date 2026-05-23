
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
    ("g70_orientation", "070_boundary_lift_matching_theorem_attempt__candidate_orientation_sign_sieve", "g70_orientation"),
]
MARKER_ID = "g70_coefficients"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    D_jump, D_layer, D_tail = sp.symbols("D_jump D_layer D_tail")
    a_jump, a_layer, a_tail = sp.symbols("a_jump a_layer a_tail")
    L_boundary = sp.simplify(a_jump*D_jump + a_layer*D_layer + a_tail*D_tail)
    residual = sp.simplify(L_boundary + D_jump + D_layer + D_tail)
    equations = [
        sp.Eq(sp.diff(residual, D_jump), 0),
        sp.Eq(sp.diff(residual, D_layer), 0),
        sp.Eq(sp.diff(residual, D_tail), 0),
    ]
    solution = sp.solve(equations, [a_jump, a_layer, a_tail], dict=True)

    header("Candidate Component Coefficient Matching")
    print(f"L_boundary = {L_boundary}")
    print(f"residual = {residual}")
    print(f"coefficient equations = {equations}")
    print(f"solution = {solution}")
    with out.derived_results():
        out.line("coefficient residual", StatusMark.PASS, str(residual))
        out.line("matching solution", StatusMark.PASS, str(solution))
    with out.unresolved_obligations():
        out.line("coefficient theorem", StatusMark.OBLIGATION, "a_jump=a_layer=a_tail=-1 must be derived from geometry")
    with out.counterexamples():
        out.line("coefficient choice", StatusMark.FAIL, "choosing coefficients to cancel residual is repair-like")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=sp.Tuple(-1, -1, -1),
        method="solve component coefficient anti-match requirements",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="component_coefficient_matching",
        scope="coefficient compatibility; not geometry theorem",
    )
    record_claim(ns, MARKER_ID, "g70_coeff_c1", GovernanceStatus.POLICY_RULE, "Component matching requires all lift-boundary coefficients equal -1.")
    record_obligation(ns, "g70_coeff_o1", "Derive component coefficients from common boundary/lift geometry.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_bulk_gauge_neutrality.py")

if __name__ == "__main__":
    main()
