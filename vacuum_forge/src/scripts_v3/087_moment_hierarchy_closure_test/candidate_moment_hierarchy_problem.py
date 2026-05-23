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
    ("g86_summary", "086_shape_origin_geometry_derivation__candidate_group_86_status_summary", "g86_summary"),
]
MARKER_ID = "g87_problem"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Moment Hierarchy Problem")
    print("Question: Is the Group 86 quartic profile part of a systematic hierarchy?")
    print("Imported Group 86 status:")
    print("  moment map derived")
    print("  degree 4 minimal for M2/M4 suppression")
    print("  quartic profile unique and zero-action minimizing")
    print("  weighted suppression W0..W3 follows from M0..M5")
    print("  local rho and higher moments remain")
    print("  physical/covariant origin open")
    print("  parent divergence identity unproven")
    print("  recombination blocked")
    print("Group 87 route: solve degree 2N normalized even profiles for N=1..4.")

    with out.governance_assessments():
        out.line("group opened", StatusMark.PASS, "moment hierarchy test opened")
        out.line("real target", StatusMark.PASS, "test finite hierarchy N=1..4")
        out.line("scope", StatusMark.INFO, "finite hierarchy evidence, not all-order proof")
        out.line("parent status", StatusMark.DEFER, "parent equation remains blocked")
    with out.counterexamples():
        out.line("quartic one-off assumed", StatusMark.FAIL, "must test hierarchy")
        out.line("finite pattern as infinity", StatusMark.FAIL, "N=1..4 cannot prove all-order closure")
        out.line("parent jump", StatusMark.FAIL, "hierarchy test cannot write parent equation")
    with out.unresolved_obligations():
        out.line("operator", StatusMark.OBLIGATION, "construct general even shape operator")
        out.line("profiles", StatusMark.OBLIGATION, "solve hierarchy profiles N=1..4")

    record_marker(ns, MARKER_ID, "Group 87 opening; finite moment hierarchy test")
    record_claim(ns, MARKER_ID, "g87_problem_c1", GovernanceStatus.UNVERIFIED, "Group 87 tests finite moment hierarchy for reduced payload-suppression profiles.")
    record_obligation(ns, "g87_problem_o1", "Construct general even shape operator.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_general_even_shape_operator.py")

if __name__ == "__main__":
    main()
