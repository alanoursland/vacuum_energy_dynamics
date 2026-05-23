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
    ("g099_problem", "099_hierarchy_source_origin_audit__candidate_source_origin_problem", "g099_problem"),
]
MARKER_ID = "g099_formula_inventory"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    s, k, j = sp.symbols("s k j", integer=True, positive=True)
    beta_expr = beta_moment(s)
    entry_expr = hierarchy_entry(k, j)

    A4 = hierarchy_matrix(4)
    symmetry_failures = []
    for r in range(4):
        for c in range(4):
            if sp.factor(A4[r, c] - A4[c, r]) != 0:
                symmetry_failures.append((r+1, c+1, sp.factor(A4[r, c] - A4[c, r])))

    hankel_shift_notes = []
    for kk in range(1, 5):
        row_entries = [hierarchy_entry(kk, jj) for jj in range(1, 5)]
        hankel_shift_notes.append((kk, row_entries))

    header("Candidate Hierarchy Formula Structure Inventory")
    print(f"beta_moment(s) = {beta_expr}")
    print(f"A[k,j] = {entry_expr}")
    print()
    print("Structural observations:")
    print("  beta_moment depends on s through five consecutive odd linear factors.")
    print("  A[k,j] uses beta_moment(k+j) and beta_moment(k+j-1).")
    print("  row coefficient (2k-1)/(2k+3) depends on k only.")
    print(f"  A_4 symmetry failures: {symmetry_failures}")
    print()
    print("Sample row entries:")
    for kk, entries in hankel_shift_notes:
        print(f"  k={kk}: {entries}")

    with out.derived_results():
        out.line("beta formula", StatusMark.PASS, str(beta_expr))
        out.line("entry formula", StatusMark.PASS, str(entry_expr))
        out.line("A_4 symmetry failures", StatusMark.INFO if symmetry_failures else StatusMark.PASS, str(symmetry_failures))
    with out.governance_assessments():
        out.line("moment-like structure", StatusMark.PASS, "entries depend on shifted k+j moments")
        out.line("Gram/Hessian symmetry", StatusMark.WARN if symmetry_failures else StatusMark.PASS, "A_N is not symmetric in raw form" if symmetry_failures else "A_4 symmetric")
        out.line("physical origin", StatusMark.OBLIGATION, "formula inventory is not a derivation")
    with out.counterexamples():
        out.line("raw symmetric Hessian by inspection", StatusMark.FAIL if symmetry_failures else StatusMark.WARN, "raw A_N has symmetry failures" if symmetry_failures else "finite symmetry is not Hessian derivation")
        out.line("moment formula as physical source", StatusMark.FAIL, "moment-like structure is not physical origin")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[s, k, j],
        output=sp.Matrix([beta_expr, entry_expr]),
        method="symbolic inventory of hierarchy moment and entry formulas",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="hierarchy_formula_structure_inventory",
        scope="hierarchy source-origin audit",
    )
    record_claim(ns, MARKER_ID, "g099_formula_c1", GovernanceStatus.POLICY_RULE, "The hierarchy entry structure is moment-like but not yet physically derived.")
    record_obligation(ns, "g099_formula_o1", "Score candidate origin routes.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_origin_route_evidence_matrix.py")

if __name__ == "__main__":
    main()
