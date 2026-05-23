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
    ("g98_problem", "098_hierarchy_burden_ledger_role_audit__candidate_burden_ledger_role_problem", "g98_problem"),
]
MARKER_ID = "g98_role_matrix"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    evidence = {
        "det_nonzero_target": True,
        "schur_positivity_target": True,
        "parity_gap_structure": True,
        "difference_numerator_target": True,
        "covariant_J_curv_definition": False,
        "exchange_current_definition": False,
        "interface_profile_definition": False,
        "total_burden_functional": False,
        "source_origin": False,
        "divergence_identity": False,
        "ordinary_matter_separation": False,
        "merger_energy_prediction": False,
    }

    roles = {
        "CONFIGURATION_ONLY": [
            "covariant_J_curv_definition",
            "source_origin",
            "ordinary_matter_separation",
        ],
        "EXCHANGE_COMPENSATION": [
            "exchange_current_definition",
            "source_origin",
            "divergence_identity",
            "ordinary_matter_separation",
        ],
        "INTERFACE_SMOOTHING": [
            "interface_profile_definition",
            "source_origin",
            "ordinary_matter_separation",
        ],
        "TOTAL_BURDEN": [
            "total_burden_functional",
            "covariant_J_curv_definition",
            "exchange_current_definition",
            "interface_profile_definition",
            "source_origin",
            "divergence_identity",
            "ordinary_matter_separation",
        ],
        "AUXILIARY_ADMISSIBILITY": [
            "det_nonzero_target",
            "schur_positivity_target",
            "parity_gap_structure",
            "difference_numerator_target",
        ],
        "AUXILIARY_RECONSTRUCTION": [
            "det_nonzero_target",
        ],
    }

    results = []
    header("Candidate Hierarchy Role Decision Matrix")
    for role, reqs in roles.items():
        missing = [r for r in reqs if not evidence.get(r, False)]
        passed = not missing
        results.append((role, passed, missing))
        print(f"{role}: {'SUPPORTED' if passed else 'NOT_LICENSED'}")
        if missing:
            print(f"  missing: {missing}")

    supported = [r for r, ok, _ in results if ok]
    strongest = "AUXILIARY_ADMISSIBILITY" if "AUXILIARY_ADMISSIBILITY" in supported else ("AUXILIARY_RECONSTRUCTION" if "AUXILIARY_RECONSTRUCTION" in supported else "NONE")
    print(f"\nStrongest licensed role: {strongest}")

    with out.derived_results():
        for role, ok, missing in results:
            out.line(role, StatusMark.PASS if ok else StatusMark.WARN, "supported" if ok else f"missing={missing}")
    with out.governance_assessments():
        out.line("strongest licensed role", StatusMark.PASS, strongest)
        out.line("physical ledger assignment", StatusMark.DEFER, "configuration/exchange/interface/total-burden assignments are not licensed")
    with out.counterexamples():
        out.line("configuration-only assignment", StatusMark.FAIL, "missing covariant J_curv/source/separation")
        out.line("exchange assignment", StatusMark.FAIL, "missing exchange current and divergence identity")
        out.line("total-burden assignment", StatusMark.FAIL, "missing burden functional and all subledgers")

    record_marker(ns, MARKER_ID, "hierarchy role decision matrix")
    record_claim(ns, MARKER_ID, "g98_matrix_c1", GovernanceStatus.POLICY_RULE, "The hierarchy is currently licensed as an auxiliary admissibility candidate, not as a physical burden ledger.")
    record_obligation(ns, "g98_matrix_o1", "Audit ledger-balance equation requirements.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_ledger_balance_equation_audit.py")

if __name__ == "__main__":
    main()
