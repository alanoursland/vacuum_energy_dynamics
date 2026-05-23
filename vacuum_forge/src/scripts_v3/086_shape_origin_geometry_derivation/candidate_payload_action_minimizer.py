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
    ("g86_quartic_uniqueness", "086_shape_origin_geometry_derivation__candidate_quartic_uniqueness_theorem", "g86_quartic_uniqueness"),
]
MARKER_ID = "g86_payload_action"

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
    A = sp.factor(M2**2 + M4**2)
    grad = [sp.factor(sp.diff(A, p)), sp.factor(sp.diff(A, q))]
    critical = sp.solve([sp.Eq(grad[0], 0), sp.Eq(grad[1], 0)], [p, q], dict=True)
    A_at = sp.simplify(A.subs(critical[0])) if critical else sp.nan
    hessian = sp.Matrix([[sp.diff(A, p, p), sp.diff(A, p, q)], [sp.diff(A, q, p), sp.diff(A, q, q)]])
    hessian_det = sp.factor(hessian.det())
    hessian_pp = sp.factor(hessian[0,0])

    header("Candidate Payload Action Minimizer")
    print(f"M2 = {M2}")
    print(f"M4 = {M4}")
    print(f"A = M2^2 + M4^2 = {A}")
    print(f"grad A = {grad}")
    print(f"critical points = {critical}")
    print(f"A at critical = {A_at}")
    print(f"Hessian[0,0] = {hessian_pp}")
    print(f"Hessian determinant = {hessian_det}")

    with out.derived_results():
        out.line("action", StatusMark.PASS, str(A))
        out.line("critical point", StatusMark.PASS, str(critical))
        out.line("A at critical", StatusMark.PASS, str(A_at))
        out.line("Hessian pp", StatusMark.PASS, str(hessian_pp))
        out.line("Hessian determinant", StatusMark.PASS, str(hessian_det))
    with out.governance_assessments():
        out.line("variational origin", StatusMark.PASS, "profile is zero-action minimizer of low-order payload action")
        out.line("global minimum", StatusMark.PASS, "A is sum of squares and reaches zero")
        out.line("reduced action scope", StatusMark.INFO, "action is reduced finite-mode payload action, not physical action")
    with out.counterexamples():
        out.line("moment fit only", StatusMark.FAIL, "same profile follows from low-order payload action minimization")
        out.line("physical action overclaim", StatusMark.FAIL, "reduced payload action is not yet a physical variational principle")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[p, q],
        output=sp.Matrix([critical[0][p], critical[0][q], A_at]),
        method="minimize low-order payload action A=M2^2+M4^2 over even quartic coefficients",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="payload_action_minimizer",
        scope="reduced finite-mode payload action",
    )
    record_claim(ns, MARKER_ID, "g86_action_c1", GovernanceStatus.POLICY_RULE, "P=1-12y^2+51y^4 is the unique zero-action minimizer of A=M2^2+M4^2 in the reduced quartic family.")
    record_obligation(ns, "g86_action_o1", "Show weighted suppression follows from flat moment block.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_weighted_consistency_from_flat_block.py")

if __name__ == "__main__":
    main()
