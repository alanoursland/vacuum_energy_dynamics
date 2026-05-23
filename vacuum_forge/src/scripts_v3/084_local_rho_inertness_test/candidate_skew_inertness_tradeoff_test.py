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
    ("g84_weighted_moments", "084_local_rho_inertness_test__candidate_weighted_probe_moment_test", "g84_weighted_moments"),
]
MARKER_ID = "g84_tradeoff"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    y, R, ell, c = sp.symbols("y R ell c", nonzero=True)
    f = (1 - y**2)**3
    w = (1 - y**2)**2
    Xi = f * (1 + c*y)
    J = sp.simplify(w * sp.diff(Xi, y))
    rho = sp.factor(sp.diff(J, y))
    mu = R**2 + 2*R*ell*y + ell**2*y**2
    M1 = sp.factor(sp.integrate(sp.expand(y*rho), (y, -1, 1)))
    weighted_total = sp.factor(sp.integrate(sp.expand(mu*rho), (y, -1, 1)))
    dipole_solutions = sp.solve(sp.Eq(M1, 0), c)
    weighted_solutions = sp.solve(sp.Eq(weighted_total, 0), c)
    compatibility_residual = sp.simplify((weighted_solutions[0] - dipole_solutions[0]) if dipole_solutions and weighted_solutions else sp.nan)

    header("Candidate Skew-Inertness Tradeoff Test")
    print(f"M1 = {M1}")
    print(f"weighted total = {weighted_total}")
    print(f"dipole inertness c solutions = {dipole_solutions}")
    print(f"weighted neutrality c solutions = {weighted_solutions}")
    print(f"difference weighted - dipole solution = {compatibility_residual}")

    with out.derived_results():
        out.line("M1", StatusMark.PASS, str(M1))
        out.line("weighted total", StatusMark.PASS, str(weighted_total))
        out.line("dipole solution", StatusMark.PASS, str(dipole_solutions))
        out.line("weighted solution", StatusMark.PASS, str(weighted_solutions))
        out.line("solution difference", StatusMark.WARN, str(compatibility_residual))
    with out.governance_assessments():
        out.line("tradeoff", StatusMark.WARN, "weighted neutrality and dipole inertness require different c unless ell=0")
        out.line("finite thickness", StatusMark.INFO, "tradeoff vanishes only in thin/flat ell=0 limit")
    with out.counterexamples():
        out.line("one skew solves all", StatusMark.FAIL, "linear skew cannot generally satisfy weighted total neutrality and dipole inertness")
        out.line("weighted as dipole inertness", StatusMark.FAIL, "Group 83 skew leaves M1 nonzero")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[y, R, ell, c],
        output=sp.Matrix([M1, weighted_total]),
        method="compare c required by dipole inertness and weighted neutrality",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="skew_inertness_tradeoff",
        scope="linear-skew compact-support family",
    )
    record_claim(ns, MARKER_ID, "g84_trade_c1", GovernanceStatus.POLICY_RULE, "In the linear-skew family, weighted neutrality and dipole inertness are incompatible unless ell=0.")
    record_obligation(ns, "g84_trade_o1", "Test whether quadratic payload obstruction is independent of c.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_quadratic_payload_obstruction.py")

if __name__ == "__main__":
    main()
