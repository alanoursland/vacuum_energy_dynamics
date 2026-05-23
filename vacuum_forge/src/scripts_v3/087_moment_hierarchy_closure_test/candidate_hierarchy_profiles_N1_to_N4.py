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
    ("g87_operator", "087_moment_hierarchy_closure_test__candidate_general_even_shape_operator", "g87_operator"),
]
MARKER_ID = "g87_profiles"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    rows = []
    header("Candidate Hierarchy Profiles N1 to N4")
    for N in range(1, 5):
        y, coeffs, P, J, rho, constraints, sol = hierarchy_solution(N)
        sol0 = sol[0]
        P_sol = sp.expand(P.subs(sol0))
        killed = [sp.simplify(c.subs(sol0)) for c in constraints]
        next_moment = sp.factor(sp.integrate(sp.expand(y**(2*N+2)*rho.subs(sol0)), (y, -1, 1)))
        rows.append((N, sol0, P_sol, killed, next_moment))
        print(f"N={N}")
        print(f"  solution = {sol0}")
        print(f"  P_N = {P_sol}")
        print(f"  killed moments M2..M{2*N} = {killed}")
        print(f"  next M{2*N+2} = {next_moment}")

    with out.derived_results():
        for N, sol0, P_sol, killed, next_moment in rows:
            out.line(f"N={N} solution", StatusMark.PASS, str(sol0))
            out.line(f"N={N} P", StatusMark.PASS, str(P_sol))
            out.line(f"N={N} killed", StatusMark.PASS, str(killed))
            out.line(f"N={N} next", StatusMark.WARN, str(next_moment))
    with out.governance_assessments():
        out.line("finite hierarchy", StatusMark.PASS, "profiles found for N=1..4")
        out.line("next obstruction", StatusMark.WARN, "each tested profile leaves next even moment nonzero")
    with out.counterexamples():
        out.line("quartic one-off", StatusMark.FAIL, "N=1..4 profiles show systematic finite hierarchy")
        out.line("all-order closure", StatusMark.FAIL, "next moments remain nonzero")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=sp.Matrix([row[4] for row in rows]),
        method="solve normalized even degree-2N profiles killing M2..M2N for N=1..4",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="finite_hierarchy_profiles",
        scope="reduced finite moment hierarchy N=1..4",
    )
    record_claim(ns, MARKER_ID, "g87_profiles_c1", GovernanceStatus.POLICY_RULE, "Finite moment-suppression profiles exist for N=1..4.")
    record_obligation(ns, "g87_profiles_o1", "Test constraint rank and uniqueness.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_constraint_rank_uniqueness_test.py")

if __name__ == "__main__":
    main()
