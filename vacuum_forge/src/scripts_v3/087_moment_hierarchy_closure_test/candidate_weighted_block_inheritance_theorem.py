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
    ("g87_rank_uniqueness", "087_moment_hierarchy_closure_test__candidate_constraint_rank_uniqueness_test", "g87_rank_uniqueness"),
]
MARKER_ID = "g87_weighted_inheritance"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    R, ell = sp.symbols("R ell")
    M = sp.symbols("M0:16")
    formulas = []
    inherited = []
    N = 4
    vanishing = {M[k]: 0 for k in range(0, 2*N+2)}  # M0..M9 vanish for N=4 profile by even block + odd parity through M9
    for n in range(0, 2*N):
        Wn = sp.expand(R**2*M[n] + 2*R*ell*M[n+1] + ell**2*M[n+2])
        formulas.append(Wn)
        inherited.append(sp.simplify(Wn.subs(vanishing)))

    header("Candidate Weighted Block Inheritance Theorem")
    print("For quadratic mu, Wn = R^2 M_n + 2Rell M_(n+1) + ell^2 M_(n+2).")
    print("If profile kills M0..M(2N+1), then W0..W(2N-1)=0.")
    for n, expr in enumerate(formulas):
        print(f"W{n} = {expr}; under N=4 block -> {inherited[n]}")

    with out.derived_results():
        for n, expr in enumerate(formulas):
            out.line(f"W{n} formula", StatusMark.PASS, str(expr))
            out.line(f"W{n} inherited", StatusMark.PASS, str(inherited[n]))
    with out.governance_assessments():
        out.line("weighted inheritance", StatusMark.PASS, "quadratic measure shifts flat moment block by at most two")
        out.line("finite block", StatusMark.INFO, "inheritance proven for any finite block with required adjacent moments")
    with out.counterexamples():
        out.line("separate weighted tuning", StatusMark.FAIL, "weighted low-order suppression follows from flat block")
        out.line("all weighted orders", StatusMark.FAIL, "only inherited block is proven")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=list(M[:10]) + [R, ell],
        output=sp.Matrix(inherited),
        method="derive quadratic-measure weighted moment inheritance from flat moment block",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="weighted_block_inheritance",
        scope="quadratic measure; finite moment blocks",
    )
    record_claim(ns, MARKER_ID, "g87_weight_c1", GovernanceStatus.POLICY_RULE, "Quadratic-measure W0..W(2N-1) suppression follows from flat M0..M(2N+1) suppression.")
    record_obligation(ns, "g87_weight_o1", "Compute next moment obstruction for each tested N.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_next_moment_obstruction_test.py")

if __name__ == "__main__":
    main()
