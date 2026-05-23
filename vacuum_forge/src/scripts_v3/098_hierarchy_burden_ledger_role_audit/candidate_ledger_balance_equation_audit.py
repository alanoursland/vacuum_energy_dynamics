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
]
MARKER_ID = "g98_balance_audit"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    J_curv, E_int, E_exch, E_other = sp.symbols("J_curv E_interface E_exchange E_other")
    E_burden = J_curv + E_int + E_exch + E_other

    D_curv, D_exch, D_total = sp.symbols("D_curv D_exch D_total")
    balance = sp.Eq(D_total, D_curv + D_exch)
    exch_required_solution = sp.solve(sp.Eq(D_curv + D_exch, 0), D_exch)[0]

    header("Candidate Ledger Balance Equation Audit")
    print(f"E_burden = {E_burden}")
    print("Parent correction balance target:")
    print("  divergence(H_curv + H_exch) = 0")
    print(f"Symbolic balance: {balance}")
    print(f"If D_curv is nonzero, required exchange/source partner: D_exch = {exch_required_solution}")
    print()
    print("Classification:")
    print("  H_curv alone is safe only if D_curv = 0 independently.")
    print("  If D_curv != 0, an exchange/source-balance partner is required.")
    print("  H_exch cannot be inserted by naming the missing partner; it needs independent definition/source/divergence proof.")

    with out.derived_results():
        out.line("burden ledger", StatusMark.PASS, str(E_burden))
        out.line("required exchange partner", StatusMark.PASS, f"D_exch={exch_required_solution}")
    with out.governance_assessments():
        out.line("configuration-only balance", StatusMark.DEFER, "allowed only if curvature sector is independently divergence-safe")
        out.line("exchange necessity", StatusMark.INFO, "if curvature divergence is nonzero, exchange/source partner is required")
        out.line("H_exch insertability", StatusMark.OBLIGATION, "exchange partner must be independently defined before insertion")
    with out.counterexamples():
        out.line("H_exch as balance paint", StatusMark.FAIL, "naming D_exch=-D_curv is not an independent source law")
        out.line("Bianchi smoke", StatusMark.FAIL, "divergence safety must be derived, not declared")
        out.line("configuration-only by preference", StatusMark.FAIL, "preference does not prove D_curv=0")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[J_curv, E_int, E_exch, E_other, D_curv, D_exch],
        output=exch_required_solution,
        method="symbolic burden ledger and divergence-balance requirement audit",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="ledger_balance_equation_audit",
        scope="hierarchy physical-role audit",
    )
    record_claim(ns, MARKER_ID, "g98_balance_c1", GovernanceStatus.POLICY_RULE, "A configuration-only assignment requires independent divergence safety; otherwise an independently defined exchange/source partner is required.")
    record_obligation(ns, "g98_balance_o1", "Map hierarchy objects to possible physical objects.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_hierarchy_physical_object_map.py")

if __name__ == "__main__":
    main()
