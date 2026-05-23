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
    ("g73_measure_origin", "73_layer_generator_construction__candidate_boundary_measure_origin_test", "g73_measure_origin"),
]
MARKER_ID = "g73_component_membership"


def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES); print_archive_status(ns, invalidated)
    out = ScriptOutput()

    D_jump, D_layer, D_tail = sp.symbols("D_jump D_layer D_tail")
    m_jump, m_layer, m_tail = sp.symbols("m_jump m_layer m_tail")
    generated_B = sp.simplify(m_jump*D_jump + m_layer*D_layer + m_tail*D_tail)
    target_B = sp.simplify(D_jump + D_layer + D_tail)
    residual = sp.simplify(generated_B - target_B)
    equations = [sp.Eq(sp.diff(residual, D_jump), 0), sp.Eq(sp.diff(residual, D_layer), 0), sp.Eq(sp.diff(residual, D_tail), 0)]
    solution = sp.solve(equations, [m_jump, m_layer, m_tail], dict=True)
    missing_layer = sp.simplify(residual.subs({m_jump: 1, m_layer: 0, m_tail: 1}))
    jump_tail_only = sp.simplify(generated_B.subs({m_jump: 1, m_layer: 0, m_tail: 1}))
    all_member = sp.simplify(generated_B.subs({m_jump: 1, m_layer: 1, m_tail: 1}))

    header("Candidate Component Membership Origin Test")
    print(f"generated B = {generated_B}")
    print(f"target B = {target_B}")
    print(f"membership residual = {residual}")
    print(f"membership equations = {equations}")
    print(f"solution = {solution}")
    print(f"missing-layer residual = {missing_layer}")
    print(f"jump/tail-only generator = {jump_tail_only}")
    print(f"all-component generator form = {all_member}")

    with out.derived_results():
        out.line("membership residual", StatusMark.PASS, str(residual))
        out.line("membership solution", StatusMark.PASS, str(solution))
    with out.governance_assessments():
        out.line("all-component route", StatusMark.INFO, "retained only if jump/layer/tail membership is geometrically derived")
        out.line("layer membership", StatusMark.OBLIGATION, "m_layer=1 must be derived, not declared")
    with out.counterexamples():
        out.line("missing layer", StatusMark.FAIL, f"residual={missing_layer}")
        out.line("membership by flag", StatusMark.FAIL, "setting m_layer=1 is compatibility, not origin theorem")
        out.line("diagnostic membership", StatusMark.FAIL, "old diagnostic transition cannot satisfy layer membership")
    with out.unresolved_obligations():
        out.line("component membership theorem", StatusMark.OBLIGATION, "derive jump/layer/tail membership from common boundary geometry")
        out.line("layer component origin", StatusMark.OBLIGATION, "derive D_layer as member of the generator rather than add-on")

    ns.record_derivation(derivation_id=MARKER_ID, inputs=[], output=residual, method="solve component-membership requirements for generated boundary object", status=Status.DERIVED, record_kind=RecordKind.COMPATIBILITY_EXAMPLE, result_type="component_membership_origin_test", scope="membership compatibility; not membership theorem")
    record_claim(ns, MARKER_ID, "g73_membership_c1", GovernanceStatus.POLICY_RULE, "Generated boundary object requires jump/layer/tail membership, but membership is not derived by flags.")
    record_claim(ns, MARKER_ID, "g73_membership_c2", GovernanceStatus.REJECTED_ROUTE, "Missing layer and diagnostic layer membership routes are rejected.")
    record_obligation(ns, "g73_membership_o1", "Derive component membership from common boundary geometry.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_payload_purity_and_role_test.py")


if __name__ == "__main__": main()
