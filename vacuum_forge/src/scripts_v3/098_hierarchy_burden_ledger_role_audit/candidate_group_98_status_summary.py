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

def status_label(ok: bool) -> str:
    return "PASS" if ok else "FAIL"

DEPENDENCIES = [
    ("g97_summary", "97_parity_gap_theorem_attempt__candidate_group_97_status_summary", "g97_summary"),
    ("g98_problem", "98_hierarchy_burden_ledger_role_audit__candidate_burden_ledger_role_problem", "g98_problem"),
    ("g98_role_matrix", "98_hierarchy_burden_ledger_role_audit__candidate_hierarchy_role_decision_matrix", "g98_role_matrix"),
    ("g98_balance_audit", "98_hierarchy_burden_ledger_role_audit__candidate_ledger_balance_equation_audit", "g98_balance_audit"),
    ("g98_object_map", "98_hierarchy_burden_ledger_role_audit__candidate_hierarchy_physical_object_map", "g98_object_map"),
    ("g98_classifier", "98_hierarchy_burden_ledger_role_audit__candidate_role_decision_surface_classifier", "g98_classifier"),
]
MARKER_ID = "g98_summary"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Group 98 Status Summary")
    print("Group 98 audits the physical burden-ledger role of the determinant/Schur hierarchy.")
    print("Stable result:")
    print("  hierarchy role: AUXILIARY_ADMISSIBILITY_CANDIDATE")
    print("  physical ledger assignment deferred")
    print("  configuration-only assignment not licensed")
    print("  exchange-compensation assignment not licensed")
    print("  interface-smoothing assignment not licensed")
    print("  total-burden assignment not licensed")
    print("  numerator route remains valuable if the admissibility theorem target is retained")
    print("  source/functional origin audit required before physical upgrade")
    print("  parent equation remains not ready")
    print("  recombination remains blocked")

    with out.governance_assessments():
        out.line("role audit", StatusMark.PASS, "completed")
        out.line("current hierarchy role", StatusMark.PASS, "AUXILIARY_ADMISSIBILITY_CANDIDATE")
        out.line("physical ledger assignment", StatusMark.DEFER, "not yet licensed")
        out.line("next theorem route", StatusMark.INFO, "numerator factorization remains useful as auxiliary admissibility")
        out.line("source-origin route", StatusMark.INFO, "needed for physical upgrade")
        out.line("parent equation", StatusMark.OBLIGATION, "not ready")
    with out.counterexamples():
        out.line("hierarchy as J_curv", StatusMark.FAIL, "not licensed")
        out.line("hierarchy as H_curv/H_exch", StatusMark.FAIL, "not licensed")
        out.line("hierarchy as total burden", StatusMark.FAIL, "not licensed")
        out.line("field equation insertion", StatusMark.FAIL, "not licensed")
    with out.unresolved_obligations():
        out.line("difference numerator theorem", StatusMark.OBLIGATION, "prove if continuing auxiliary admissibility route")
        out.line("source origin audit", StatusMark.OBLIGATION, "derive physical problem that produces hierarchy")
        out.line("burden functional", StatusMark.OBLIGATION, "define J_curv/interface/exchange/total burden before physical claims")
        out.line("divergence identity", StatusMark.OBLIGATION, "derive before any correction tensor insertion")

    print("\nRecommended next routes:")
    print("  99_difference_numerator_factorization_attempt")
    print("  99_hierarchy_source_origin_audit")
    print("  99_burden_functional_minimum_requirements")
    print("  99_configuration_exchange_balance_surface")
    print()
    print("Recommendation:")
    print("  If continuing math: 99_difference_numerator_factorization_attempt")
    print("  If grounding physics first: 99_hierarchy_source_origin_audit")

    record_marker(ns, MARKER_ID, "Group 98 summary; hierarchy burden-ledger role audit")
    record_claim(ns, MARKER_ID, "g98_summary_c1", GovernanceStatus.POLICY_RULE, "Group 98 assigns the hierarchy the safe current role of auxiliary admissibility candidate.")
    record_claim(ns, MARKER_ID, "g98_summary_c2", GovernanceStatus.POLICY_RULE, "Physical ledger assignment remains deferred until a source/functional origin is derived.")
    record_obligation(ns, "g98_summary_o1", "Choose numerator factorization or hierarchy source-origin audit next.")
    record_obligation(ns, "g98_summary_o2", "Parent divergence identity remains unproven.")
    ns.write_run_metadata()

if __name__ == "__main__":
    main()
