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
    ("g98_role_matrix", "098_hierarchy_burden_ledger_role_audit__candidate_hierarchy_role_decision_matrix", "g98_role_matrix"),
    ("g98_balance_audit", "098_hierarchy_burden_ledger_role_audit__candidate_ledger_balance_equation_audit", "g98_balance_audit"),
    ("g98_object_map", "098_hierarchy_burden_ledger_role_audit__candidate_hierarchy_physical_object_map", "g98_object_map"),
]
MARKER_ID = "g98_classifier"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    classifications = [
        ("HIERARCHY_ROLE_AUXILIARY_ADMISSIBILITY_CANDIDATE", "stable", "det/Schur/parity/numerator branch supports nondegeneracy theorem target"),
        ("PHYSICAL_LEDGER_ASSIGNMENT_DEFERRED", "stable", "no derived source/functional/current origin"),
        ("CONFIGURATION_ONLY_ASSIGNMENT_NOT_LICENSED", "stable", "J_curv not covariantly defined and not tied to hierarchy"),
        ("EXCHANGE_COMPENSATION_ASSIGNMENT_NOT_LICENSED", "stable", "J_exch/H_exch not independently defined or insertable"),
        ("INTERFACE_SMOOTHING_ASSIGNMENT_NOT_LICENSED", "stable", "interface profile/functional not defined"),
        ("TOTAL_BURDEN_ASSIGNMENT_NOT_LICENSED", "stable", "combined burden functional not defined"),
        ("NUMERATOR_ROUTE_STILL_VALUABLE_IF_ADMISSIBILITY_TARGET_RETAINED", "stable", "difference numerator theorem would support hierarchy nondegeneracy"),
        ("SOURCE_ORIGIN_AUDIT_REQUIRED_FOR_PHYSICAL_UPGRADE", "stable", "must derive what variational/source problem produces hierarchy"),
        ("PARENT_EQUATION_NOT_READY", "stable", "no H insertion or parent identity"),
        ("RECOMBINATION_BLOCKED", "stable", "no recombination license"),
    ]

    header("Candidate Role Decision Surface Classifier")
    for name, status, reason in classifications:
        print(f"{name}: {status}; {reason}")

    with out.governance_assessments():
        out.line("current role", StatusMark.PASS, "AUXILIARY_ADMISSIBILITY_CANDIDATE")
        out.line("physical ledger assignment", StatusMark.DEFER, "deferred pending source/functional origin")
        out.line("numerator route", StatusMark.INFO, "still valuable if admissibility theorem remains worth proving")
        out.line("parent equation", StatusMark.OBLIGATION, "not ready")
    with out.counterexamples():
        out.line("J_curv assignment", StatusMark.FAIL, "not licensed")
        out.line("H_exch assignment", StatusMark.FAIL, "not licensed")
        out.line("total burden assignment", StatusMark.FAIL, "not licensed")
        out.line("parent equation", StatusMark.FAIL, "not licensed")
    with out.unresolved_obligations():
        out.line("source origin", StatusMark.OBLIGATION, "derive hierarchy from a physical variational/source problem")
        out.line("ledger upgrade", StatusMark.OBLIGATION, "show hierarchy belongs to J_curv/interface/exchange/total burden before physical claims")
        out.line("numerator theorem", StatusMark.OBLIGATION, "optional continuation as auxiliary admissibility theorem")

    record_marker(ns, MARKER_ID, "role decision surface classifier")
    record_claim(ns, MARKER_ID, "g98_class_c1", GovernanceStatus.POLICY_RULE, "The determinant/Schur hierarchy is currently an auxiliary admissibility candidate; physical ledger assignment is deferred.")
    record_claim(ns, MARKER_ID, "g98_class_c2", GovernanceStatus.POLICY_RULE, "Configuration-only, exchange-compensation, interface, and total-burden assignments are not currently licensed.")
    record_obligation(ns, "g98_class_o1", "Choose between numerator factorization and hierarchy source-origin audit next.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_group_098_status_summary.py")

if __name__ == "__main__":
    main()
