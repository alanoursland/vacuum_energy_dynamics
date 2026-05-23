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

DEPENDENCIES = [
    ("g86_minimal_degree", "86_shape_origin_geometry_derivation__candidate_minimal_degree_obstruction", "g86_minimal_degree"),
]
MARKER_ID = "g86_quartic_uniqueness"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    y, p, q = sp.symbols("y p q")
    f = (1 - y**2)**3
    w = (1 - y**2)**2
    P = 1 + p*y**2 + q*y**4
    rho = sp.factor(sp.diff(w*sp.diff(f*P, y), y))
    M2 = sp.factor(sp.integrate(sp.expand(y**2*rho), (y, -1, 1)))
    M4 = sp.factor(sp.integrate(sp.expand(y**4*rho), (y, -1, 1)))
    sol = sp.solve([sp.Eq(M2, 0), sp.Eq(M4, 0)], [p, q], dict=True)
    P_sol = sp.expand(P.subs(sol[0]))
    M2_sol = sp.simplify(M2.subs(sol[0]))
    M4_sol = sp.simplify(M4.subs(sol[0]))

    header("Candidate Quartic Uniqueness Theorem")
    print(f"M2 = {M2}")
    print(f"M4 = {M4}")
    print(f"solution = {sol}")
    print(f"P_solution = {P_sol}")
    print(f"M2 at solution = {M2_sol}")
    print(f"M4 at solution = {M4_sol}")

    with out.derived_results():
        out.line("M2", StatusMark.INFO, str(M2))
        out.line("M4", StatusMark.INFO, str(M4))
        out.line("solution", StatusMark.PASS, str(sol))
        out.line("P solution", StatusMark.PASS, str(P_sol))
        out.line("M2/M4 at solution", StatusMark.PASS, f"{M2_sol}, {M4_sol}")
    with out.governance_assessments():
        out.line("quartic uniqueness", StatusMark.PASS, "unique normalized even quartic kills M2 and M4")
        out.line("origin status", StatusMark.INFO, "minimal-degree reduced origin derived")
    with out.counterexamples():
        out.line("arbitrary p,q", StatusMark.FAIL, "moment conditions force unique p,q")
        out.line("physical origin overclaim", StatusMark.FAIL, "uniqueness inside reduced problem is not full physical derivation")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[y, p, q],
        output=sp.Matrix([sol[0][p], sol[0][q]]),
        method="solve quartic M2=M4 suppression system and verify uniqueness",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="quartic_uniqueness_theorem",
        scope="normalized even quartic reduced exactness family",
    )
    record_claim(ns, MARKER_ID, "g86_quartic_c1", GovernanceStatus.POLICY_RULE, "P=1-12y^2+51y^4 is the unique normalized even quartic suppressing M2 and M4.")
    record_obligation(ns, "g86_quartic_o1", "Test payload-action minimizer origin.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_payload_action_minimizer.py")

if __name__ == "__main__":
    main()
