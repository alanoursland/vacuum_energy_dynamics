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

def beta_moment(s):
    s = sp.sympify(s)
    denom = sp.prod(2*s + 2*m + 1 for m in range(5))
    return sp.factor(sp.Rational(768, 1) / denom)

def hierarchy_entry(k, j):
    k = sp.sympify(k)
    j = sp.sympify(j)
    return sp.factor(beta_moment(k+j) - ((2*k - 1) / (2*k + 3)) * beta_moment(k+j-1))

def hierarchy_matrix(N: int):
    A = sp.zeros(N, N)
    for k in range(1, N + 1):
        for j in range(1, N + 1):
            A[k-1, j-1] = hierarchy_entry(k, j)
    return A

DEPENDENCIES = [
    ("g98_summary", "098_hierarchy_burden_ledger_role_audit__candidate_group_098_status_summary", "g98_summary"),
    ("g099_problem", "099_hierarchy_source_origin_audit__candidate_source_origin_problem", "g099_problem"),
    ("g099_formula_inventory", "099_hierarchy_source_origin_audit__candidate_hierarchy_formula_structure_inventory", "g099_formula_inventory"),
    ("g099_origin_matrix", "099_hierarchy_source_origin_audit__candidate_origin_route_evidence_matrix", "g099_origin_matrix"),
    ("g099_moment_probe", "099_hierarchy_source_origin_audit__candidate_moment_projection_plausibility_probe", "g099_moment_probe"),
    ("g099_decision_surface", "099_hierarchy_source_origin_audit__candidate_source_origin_decision_surface", "g099_decision_surface"),
]
MARKER_ID = "g099_summary"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Group 099 Status Summary")
    print("Group 099 audits the source/functional origin of the hierarchy A_N.")
    print("Stable result:")
    print("  A_N formula is moment-like")
    print("  beta_moment has beta-type moment-integral structure")
    print("  moment/projection origin is plausible but underderived")
    print("  variational Hessian origin is not licensed")
    print("  interface origin is not licensed")
    print("  exchange origin is not licensed")
    print("  total burden origin is not licensed")
    print("  source origin remains open")
    print("  hierarchy remains auxiliary admissibility candidate")
    print("  parent equation remains not ready")
    print("  recombination remains blocked")

    with out.governance_assessments():
        out.line("source audit", StatusMark.PASS, "completed")
        out.line("moment structure", StatusMark.PASS, "supported")
        out.line("moment/projection origin", StatusMark.INFO, "plausible but underderived")
        out.line("physical origin", StatusMark.DEFER, "not yet derived")
        out.line("hierarchy role", StatusMark.PASS, "auxiliary admissibility candidate retained")
        out.line("parent equation", StatusMark.OBLIGATION, "not ready")
    with out.counterexamples():
        out.line("A_N as J_curv", StatusMark.FAIL, "not licensed")
        out.line("A_N as exchange equation", StatusMark.FAIL, "not licensed")
        out.line("A_N as total burden", StatusMark.FAIL, "not licensed")
        out.line("A_N as field equation", StatusMark.FAIL, "not licensed")
    with out.unresolved_obligations():
        out.line("moment projection derivation", StatusMark.OBLIGATION, "derive residual/basis/source/boundary problem")
        out.line("difference numerator theorem", StatusMark.OBLIGATION, "optional auxiliary admissibility continuation")
        out.line("burden functional", StatusMark.OBLIGATION, "not defined")
        out.line("divergence identity", StatusMark.OBLIGATION, "not proven")

    print("\nRecommended next routes:")
    print("  100_moment_projection_derivation_attempt")
    print("  100_difference_numerator_factorization_attempt")
    print("  100_burden_functional_minimum_requirements")
    print()
    print("Recommendation:")
    print("  If grounding hierarchy origin: 100_moment_projection_derivation_attempt")
    print("  If finishing current math trail: 100_difference_numerator_factorization_attempt")

    record_marker(ns, MARKER_ID, "Group 099 summary; hierarchy source-origin audit")
    record_claim(ns, MARKER_ID, "g099_summary_c1", GovernanceStatus.POLICY_RULE, "Group 099 finds moment-like structure and a plausible but underderived projection origin for A_N.")
    record_claim(ns, MARKER_ID, "g099_summary_c2", GovernanceStatus.POLICY_RULE, "A_N remains auxiliary admissibility infrastructure until residual/source/functional origin is derived.")
    record_obligation(ns, "g099_summary_o1", "Choose moment projection derivation or difference numerator factorization next.")
    record_obligation(ns, "g099_summary_o2", "Parent divergence identity remains unproven.")
    ns.write_run_metadata()

if __name__ == "__main__":
    main()
