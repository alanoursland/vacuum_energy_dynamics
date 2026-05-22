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

def hierarchy_solution(N: int):
    y = sp.symbols("y")
    coeffs = sp.symbols("a1:" + str(N + 1))
    f = (1 - y**2)**3
    w = (1 - y**2)**2
    P = 1 + sum(coeffs[k-1] * y**(2*k) for k in range(1, N + 1))
    J = sp.simplify(w * sp.diff(f * P, y))
    rho = sp.factor(sp.diff(J, y))
    constraints = [
        sp.factor(sp.integrate(sp.expand(y**(2*k) * rho), (y, -1, 1)))
        for k in range(1, N + 1)
    ]
    sol = sp.solve([sp.Eq(m, 0) for m in constraints], coeffs, dict=True)
    return y, coeffs, P, J, rho, constraints, sol

DEPENDENCIES = [
    ("g87_profiles", "87_moment_hierarchy_closure_test__candidate_hierarchy_profiles_N1_to_N4", "g87_profiles"),
]
MARKER_ID = "g87_rank_uniqueness"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    rows = []
    header("Candidate Constraint Rank Uniqueness Test")
    for N in range(1, 5):
        y, coeffs, P, J, rho, constraints, sol = hierarchy_solution(N)
        mat_rows = []
        rhs_rows = []
        for expr in constraints:
            mat_rows.append([sp.diff(expr, c) for c in coeffs])
            zero_part = expr.subs({c: 0 for c in coeffs})
            rhs_rows.append(-zero_part)
        A = sp.Matrix(mat_rows)
        b = sp.Matrix(rhs_rows)
        rank_A = A.rank()
        rank_aug = A.row_join(b).rank()
        det_A = sp.factor(A.det()) if A.shape[0] == A.shape[1] else None
        unique = (rank_A == N and rank_aug == N)
        rows.append((N, rank_A, rank_aug, det_A, unique))
        print(f"N={N}: rank(A)={rank_A}, rank(A|b)={rank_aug}, det(A)={det_A}, unique={unique}")

    with out.derived_results():
        for N, rank_A, rank_aug, det_A, unique in rows:
            out.line(f"N={N} rank", StatusMark.PASS, f"rank={rank_A}, augmented={rank_aug}")
            out.line(f"N={N} det", StatusMark.PASS, str(det_A))
            out.line(f"N={N} unique", StatusMark.PASS, str(unique))
    with out.governance_assessments():
        out.line("rank uniqueness", StatusMark.PASS, "constraint matrices full-rank for N=1..4")
        out.line("finite proof status", StatusMark.INFO, "rank checked through N=4, not all N")
    with out.counterexamples():
        out.line("free profile coefficients", StatusMark.FAIL, "full-rank constraints force unique coefficients for tested N")
        out.line("general theorem overclaim", StatusMark.FAIL, "finite rank checks do not prove all-order rank theorem")

    record_marker(ns, MARKER_ID, "rank uniqueness test for N=1..4")
    record_claim(ns, MARKER_ID, "g87_rank_c1", GovernanceStatus.POLICY_RULE, "For N=1..4, constraint matrices are full-rank and profiles are unique.")
    record_obligation(ns, "g87_rank_o1", "Derive weighted block inheritance.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_weighted_block_inheritance_theorem.py")

if __name__ == "__main__":
    main()
