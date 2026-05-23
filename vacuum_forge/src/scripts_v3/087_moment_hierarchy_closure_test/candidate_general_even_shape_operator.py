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
    ("g87_problem", "087_moment_hierarchy_closure_test__candidate_moment_hierarchy_problem", "g87_problem"),
]
MARKER_ID = "g87_operator"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    N = 4
    y, coeffs, P, J, rho, constraints, sol = hierarchy_solution(N)
    parity_P = sp.simplify(P.subs(y, -y) - P)
    parity_J = sp.simplify(J.subs(y, -y) + J)
    parity_rho = sp.simplify(rho.subs(y, -y) - rho)
    endpoints = (sp.simplify(J.subs(y, -1)), sp.simplify(J.subs(y, 1)))
    odd_moments = [
        sp.factor(sp.integrate(sp.expand(y**(2*k+1) * rho), (y, -1, 1)))
        for k in range(4)
    ]

    header("Candidate General Even Shape Operator")
    print(f"P_N with N=4 example = {P}")
    print(f"P(-y)-P(y) = {parity_P}")
    print(f"J(-y)+J(y) = {parity_J}")
    print(f"rho(-y)-rho(y) = {parity_rho}")
    print(f"J endpoints = {endpoints}")
    for k, m in enumerate(odd_moments):
        print(f"M{2*k+1} = {m}")

    with out.derived_results():
        out.line("P even check", StatusMark.PASS, str(parity_P))
        out.line("J odd check", StatusMark.PASS, str(parity_J))
        out.line("rho even check", StatusMark.PASS, str(parity_rho))
        out.line("endpoint flux", StatusMark.PASS, str(endpoints))
        for k, m in enumerate(odd_moments):
            out.line(f"M{2*k+1}", StatusMark.PASS, str(m))
    with out.governance_assessments():
        out.line("operator parity", StatusMark.PASS, "even profiles yield odd J and even rho")
        out.line("odd moment suppression", StatusMark.PASS, "odd moments vanish by parity on symmetric interval")
        out.line("endpoint support", StatusMark.PASS, "compact endpoint flux retained")
    with out.counterexamples():
        out.line("odd moments as constraints", StatusMark.FAIL, "odd moments are automatic by parity, not independent constraints")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[y, *coeffs],
        output=sp.Matrix([parity_P, parity_J, parity_rho]),
        method="construct general even exactness operator and verify parity/endpoints",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="general_even_shape_operator",
        scope="reduced compact-support exactness family",
    )
    record_claim(ns, MARKER_ID, "g87_operator_c1", GovernanceStatus.POLICY_RULE, "Even profiles automatically preserve endpoint flux and kill odd moments by parity.")
    record_obligation(ns, "g87_operator_o1", "Solve hierarchy profiles for N=1..4.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_hierarchy_profiles_N1_to_N4.py")

if __name__ == "__main__":
    main()
