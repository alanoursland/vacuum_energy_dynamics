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
    ("g85_even_quartic_family", "085_shape_family_payload_suppression_test__candidate_even_quartic_shape_family", "g85_even_quartic_family"),
]
MARKER_ID = "g85_moment_solver"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    y, p, q = sp.symbols("y p q")
    f = (1 - y**2)**3
    w = (1 - y**2)**2
    P = 1 + p*y**2 + q*y**4
    Xi = f*P
    J = sp.simplify(w*sp.diff(Xi, y))
    rho = sp.factor(sp.diff(J, y))
    moments = [sp.factor(sp.integrate(sp.expand(y**n*rho), (y, -1, 1))) for n in range(6)]
    sol = sp.solve([sp.Eq(moments[2], 0), sp.Eq(moments[4], 0)], [p, q], dict=True)
    p_sol = sol[0][p]
    q_sol = sol[0][q]

    header("Candidate Moment Constraint Solver")
    for n, m in enumerate(moments):
        print(f"M{n} = {m}")
    print(f"solve M2=0, M4=0 -> {sol}")

    with out.derived_results():
        out.line("M0", StatusMark.PASS, str(moments[0]))
        out.line("M1", StatusMark.PASS, str(moments[1]))
        out.line("M2", StatusMark.WARN, str(moments[2]))
        out.line("M3", StatusMark.PASS, str(moments[3]))
        out.line("M4", StatusMark.WARN, str(moments[4]))
        out.line("solution", StatusMark.PASS, str(sol))
    with out.governance_assessments():
        out.line("moment constraints", StatusMark.PASS, "M2 and M4 constraints solved")
        out.line("unique profile", StatusMark.PASS, "unique p,q for P(0)=1 even quartic family")
    with out.counterexamples():
        out.line("linear skew obstruction universal", StatusMark.FAIL, "even quartic family has moment-suppression solution")
        out.line("shape origin overclaim", StatusMark.FAIL, "solution is moment-derived, not yet physically derived")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[y, p, q],
        output=sp.Matrix([p_sol, q_sol]),
        method="solve M2=0 and M4=0 for even quartic compact-support profile",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="moment_suppression_profile",
        scope="reduced finite-mode moment constraints",
    )
    record_claim(ns, MARKER_ID, "g85_solver_c1", GovernanceStatus.POLICY_RULE, "Even quartic profile P=1-12y^2+51y^4 uniquely kills M2 and M4 in the reduced family.")
    record_obligation(ns, "g85_solver_o1", "Validate suppressed profile moments and local rho.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_suppressed_profile_validation.py")

if __name__ == "__main__":
    main()
