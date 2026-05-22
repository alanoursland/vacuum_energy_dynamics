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
    ("g87_weighted_inheritance", "87_moment_hierarchy_closure_test__candidate_weighted_block_inheritance_theorem", "g87_weighted_inheritance"),
    ("g87_profiles", "87_moment_hierarchy_closure_test__candidate_hierarchy_profiles_N1_to_N4", "g87_profiles"),
]
MARKER_ID = "g87_next_obstruction"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    rows = []
    header("Candidate Next Moment Obstruction Test")
    for N in range(1, 5):
        y, coeffs, P, J, rho, constraints, sol = hierarchy_solution(N)
        sol0 = sol[0]
        rho_sol = sp.factor(rho.subs(sol0))
        next_flat = sp.factor(sp.integrate(sp.expand(y**(2*N+2)*rho_sol), (y, -1, 1)))
        next_weighted = sp.factor(sp.symbols("ell")**2 * next_flat)
        rho_zero = sp.simplify(rho_sol.subs(y, 0))
        rows.append((N, next_flat, next_weighted, rho_zero))
        print(f"N={N}: M{2*N+2}={next_flat}, leading W{2*N} obstruction ell^2*M{2*N+2}={next_weighted}, rho(0)={rho_zero}")

    with out.derived_results():
        for N, next_flat, next_weighted, rho_zero in rows:
            out.line(f"N={N} next flat", StatusMark.WARN, str(next_flat))
            out.line(f"N={N} next weighted", StatusMark.WARN, str(next_weighted))
            out.line(f"N={N} rho(0)", StatusMark.WARN, str(rho_zero))
    with out.governance_assessments():
        out.line("next obstruction", StatusMark.WARN, "each tested profile leaves next even moment nonzero")
        out.line("local rho", StatusMark.WARN, "local rho remains nonzero")
        out.line("finite-order only", StatusMark.INFO, "hierarchy suppresses finite blocks but does not close all moments")
    with out.counterexamples():
        out.line("all moments vanish", StatusMark.FAIL, "next even moments remain nonzero for N=1..4")
        out.line("rho pointwise zero", StatusMark.FAIL, "rho(0) remains nonzero")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=sp.Matrix([row[1] for row in rows]),
        method="compute next unsuppressed flat moment for hierarchy profiles N=1..4",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="next_moment_obstruction",
        scope="reduced finite moment hierarchy N=1..4",
    )
    record_claim(ns, MARKER_ID, "g87_next_c1", GovernanceStatus.POLICY_RULE, "Each tested hierarchy profile leaves the next even moment nonzero.")
    record_obligation(ns, "g87_next_o1", "Classify hierarchy route status.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_moment_hierarchy_route_classifier.py")

if __name__ == "__main__":
    main()
