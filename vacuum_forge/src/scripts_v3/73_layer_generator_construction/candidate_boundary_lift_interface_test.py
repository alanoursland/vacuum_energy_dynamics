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
    print(); print("=" * 120); print(title); print("=" * 120)


def prepare_archive(dependencies):
    archive = ProjectArchive(ARCHIVE_ROOT); ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    for dep_id, upstream_script_id, upstream_derivation_id in dependencies:
        ns.declare_dependency(dependency_id=dep_id, upstream_script_id=upstream_script_id, upstream_derivation_id=upstream_derivation_id)
    return archive, ns, invalidated


def print_archive_status(ns, invalidated: bool) -> None:
    if invalidated: print("[INFO] Archive invalidated due to source change.")
    checks = ns.verify_dependencies()
    if not checks:
        print("[INFO] Archive dependencies: none declared."); return
    print("[INFO] Archive dependency check:")
    for check in checks: print(f"  - {check.dependency.dependency_id}: {check.status} ({check.message})")


def record_claim(ns, marker_id: str, claim_id: str, status: GovernanceStatus, statement: str) -> None:
    ns.record_claim(ClaimRecord(claim_id=claim_id, script_id=SCRIPT_ID, claim_kind=RecordKind.GOVERNANCE_CLAIM, tier=ClaimTier.CONSTRAINED, status=status, statement=statement, derivation_ids=[marker_id], obligation_ids=[]))


def record_obligation(ns, obligation_id: str, statement: str, status: ObligationStatus = ObligationStatus.OPEN) -> None:
    ns.record_obligation(ProofObligationRecord(obligation_id=obligation_id, script_id=SCRIPT_ID, title=obligation_id, status=status, required_by=[SCRIPT_ID], description=statement))


DEPENDENCIES = [
    ("g73_payload_purity", "73_layer_generator_construction__candidate_payload_purity_and_role_test", "g73_payload_purity"),
]
MARKER_ID = "g73_lift_interface"


def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES); print_archive_status(ns, invalidated)
    out = ScriptOutput()

    D_jump, D_layer_geo, D_tail, L_bulk, L_gauge, sigma = sp.symbols("D_jump D_layer_geo D_tail L_bulk L_gauge sigma")
    B_geo = sp.simplify(D_jump + D_layer_geo + D_tail)
    L_boundary = sp.simplify(-sigma * B_geo)
    residual = sp.simplify(B_geo + L_boundary + L_bulk + L_gauge)
    strict_residual = sp.simplify(residual.subs(sigma, 1))
    no_lift_residual = sp.simplify(strict_residual.subs({L_bulk: 0, L_gauge: 0}))
    missing_layer_residual = sp.simplify(residual.subs({D_layer_geo: 0, sigma: 1}))

    header("Candidate Boundary-Lift Interface Test")
    print(f"B_geo = {B_geo}")
    print(f"L_boundary = {L_boundary}")
    print(f"residual = {residual}")
    print(f"strict orientation residual (sigma=1) = {strict_residual}")
    print(f"with lift cleanliness = {no_lift_residual}")
    print(f"missing geometric layer under sigma=1 = {missing_layer_residual}")
    print("Interpretation:")
    print("  a legitimate D_layer_geo can enter the boundary anti-match algebra")
    print("  but this does not derive D_layer_geo or lift neutrality")

    with out.derived_results():
        out.line("geometric boundary sum", StatusMark.PASS, str(B_geo))
        out.line("boundary-lift residual", StatusMark.PASS, str(residual))
        out.line("strict residual", StatusMark.PASS, str(strict_residual))
    with out.governance_assessments():
        out.line("interface", StatusMark.INFO, "geometric D_layer could participate in anti-match if derived")
        out.line("lift cleanliness", StatusMark.OBLIGATION, "L_bulk=0 and L_gauge=0 remain separate obligations")
        out.line("D_layer origin", StatusMark.OBLIGATION, "interface algebra does not derive D_layer_geo")
    with out.counterexamples():
        out.line("missing layer", StatusMark.FAIL, "if D_layer has no geometric origin, boundary generator is incomplete")
        out.line("sigma choice", StatusMark.FAIL, "choosing sigma=1 remains compatibility, not theorem")
        out.line("lift omission", StatusMark.FAIL, "dropping L_bulk/L_gauge by prose remains forbidden")
    with out.unresolved_obligations():
        out.line("D_layer theorem", StatusMark.OBLIGATION, "derive geometric D_layer origin")
        out.line("lift theorem", StatusMark.OBLIGATION, "derive L_bulk=0 and L_gauge=0 or lawful shared lift identity")

    ns.record_derivation(derivation_id=MARKER_ID, inputs=[], output=residual, method="substitute geometric layer component into boundary-lift anti-match interface", status=Status.DERIVED, record_kind=RecordKind.COMPATIBILITY_EXAMPLE, result_type="boundary_lift_interface_with_geometric_layer", scope="interface compatibility; not D_layer/lift theorem")
    record_claim(ns, MARKER_ID, "g73_lift_c1", GovernanceStatus.POLICY_RULE, "A derived geometric D_layer could participate in boundary anti-match, but interface algebra does not derive it.")
    record_claim(ns, MARKER_ID, "g73_lift_c2", GovernanceStatus.POLICY_RULE, "L_bulk and L_gauge remain separate lift-cleanliness obligations.")
    record_obligation(ns, "g73_lift_o1", "Derive D_layer_geo and lift neutrality before parent divergence can close.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_layer_generator_route_classifier.py")


if __name__ == "__main__": main()
