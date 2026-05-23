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


def record_claim(ns, derivation_id: str, claim_id: str, status: GovernanceStatus, statement: str) -> None:
    ns.record_claim(
        ClaimRecord(
            claim_id=claim_id,
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=status,
            statement=statement,
            derivation_ids=[derivation_id],
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
    ("g70_orientation", "070_boundary_lift_matching_theorem_attempt__candidate_orientation_sign_sieve", "g70_orientation"),
    ("g71_requirements", "071_common_boundary_generator_search__candidate_boundary_generator_requirements", "g71_requirements"),
]
DERIVATION_ID = "g71_orientation_forcing"


def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    G, sigma = sp.symbols("G sigma")
    D_boundary = G
    L_boundary = -sigma * G
    residual = sp.simplify(D_boundary + L_boundary)
    sigma_solution = sp.solve(sp.Eq(residual, 0), sigma)

    same_orientation_residual = sp.simplify(G + G)
    zero_generator_residual = sp.simplify(residual.subs(G, 0))

    header("Candidate Orientation Forcing Test")
    print(f"D_boundary = {D_boundary}")
    print(f"L_boundary = {L_boundary}")
    print(f"boundary residual = {residual}")
    print(f"sigma solution = {sigma_solution}")
    print()
    print("Classifications:")
    print("  opposite-orientation generator: retained as theorem route if orientation is derived")
    print("  free sigma: rejected unless sigma is forced by geometry")
    print(f"  same orientation residual: {same_orientation_residual} -> rejected")
    print(f"  zero generator residual: {zero_generator_residual} -> rejected as trivial no-boundary object")

    with out.derived_results():
        out.line("orientation residual", StatusMark.PASS, str(residual))
        out.line("sigma requirement", StatusMark.PASS, str(sigma_solution))
    with out.governance_assessments():
        out.line("orientation-forced route", StatusMark.INFO, "retained only if opposite orientation is derived from boundary geometry")
    with out.counterexamples():
        out.line("free sigma", StatusMark.FAIL, "solving for sigma is compatibility, not orientation theorem")
        out.line("same orientation", StatusMark.FAIL, f"residual={same_orientation_residual}")
        out.line("zero generator", StatusMark.FAIL, "G=0 removes the boundary object rather than matching it")
    with out.unresolved_obligations():
        out.line("orientation theorem", StatusMark.OBLIGATION, "derive opposite orientation from a real boundary/covariant generator")

    ns.record_derivation(
        derivation_id=DERIVATION_ID,
        inputs=[],
        output=sp.Integer(1),
        method="solve D_boundary + L_boundary = 0 for orientation parameter sigma",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="orientation_forcing_requirement",
        scope="orientation compatibility; not orientation theorem",
    )
    record_claim(ns, DERIVATION_ID, "g71_orient_c1", GovernanceStatus.POLICY_RULE, "Orientation anti-match requires sigma=1, but geometry must force it.")
    record_claim(ns, DERIVATION_ID, "g71_orient_c2", GovernanceStatus.REJECTED_ROUTE, "Free sigma, same-orientation, and zero-generator routes are rejected.")
    record_obligation(ns, "g71_orient_o1", "Search for a boundary orientation/normal/lift convention that forces opposite orientation.")
    ns.write_run_metadata()

    print("\nPossible next script:")
    print("  candidate_component_forcing_test.py")


if __name__ == "__main__":
    main()
