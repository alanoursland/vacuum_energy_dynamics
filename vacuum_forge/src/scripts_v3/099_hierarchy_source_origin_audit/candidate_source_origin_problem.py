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
    return sp.factor(beta_moment(k+j) - sp.Rational(2*k-1, 2*k+3) * beta_moment(k+j-1))

def hierarchy_matrix(N: int):
    A = sp.zeros(N, N)
    for k in range(1, N + 1):
        for j in range(1, N + 1):
            A[k-1, j-1] = hierarchy_entry(k, j)
    return A

DEPENDENCIES = [
    ("g98_summary", "098_hierarchy_burden_ledger_role_audit__candidate_group_98_status_summary", "g98_summary"),
]
MARKER_ID = "g099_problem"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Source Origin Problem")
    print("Open Group 099: audit the source/functional origin of the hierarchy matrix A_N.")
    print("Imported Group 098 state:")
    print("  hierarchy role: AUXILIARY_ADMISSIBILITY_CANDIDATE")
    print("  physical ledger assignment deferred")
    print("  source/functional origin audit required")
    print("  parent equation not ready")
    print("  recombination blocked")
    print()
    print("Central question:")
    print("  What source, variational, moment, projection, or boundary problem could produce A_N?")

    with out.governance_assessments():
        out.line("group opened", StatusMark.PASS, "hierarchy source-origin audit opened")
        out.line("real target", StatusMark.PASS, "identify plausible origin route or preserve origin-unassigned status")
        out.line("scope", StatusMark.INFO, "origin audit, not physical derivation or field-equation insertion")
    with out.counterexamples():
        out.line("A_N as J_curv", StatusMark.FAIL, "not derived")
        out.line("A_N as H_exch", StatusMark.FAIL, "not derived")
        out.line("A_N as total burden", StatusMark.FAIL, "not derived")
        out.line("parent equation jump", StatusMark.FAIL, "not licensed")
    with out.unresolved_obligations():
        out.line("formula inventory", StatusMark.OBLIGATION, "record actual A_N entry structure")
        out.line("origin route matrix", StatusMark.OBLIGATION, "score candidate origins against evidence")
        out.line("moment plausibility", StatusMark.OBLIGATION, "test moment/projection-like structure")

    record_marker(ns, MARKER_ID, "Group 099 opening; hierarchy source-origin audit")
    record_claim(ns, MARKER_ID, "g099_problem_c1", GovernanceStatus.POLICY_RULE, "Group 099 audits the source/functional origin of A_N before physical upgrade.")
    record_obligation(ns, "g099_problem_o1", "Inventory the formula structure of A_N.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_hierarchy_formula_structure_inventory.py")

if __name__ == "__main__":
    main()
