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
    ("g86_problem", "086_shape_origin_geometry_derivation__candidate_shape_origin_problem", "g86_problem"),
]
MARKER_ID = "g86_moment_map"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    y, a1, a2, a3 = sp.symbols("y a1 a2 a3")
    f = (1 - y**2)**3
    w = (1 - y**2)**2
    P = 1 + a1*y**2 + a2*y**4 + a3*y**6
    J = sp.simplify(w * sp.diff(f*P, y))
    rho = sp.factor(sp.diff(J, y))
    moments = {
        n: sp.factor(sp.integrate(sp.expand(y**n * rho), (y, -1, 1)))
        for n in [0, 2, 4, 6]
    }

    header("Candidate Moment Map From Shape Coefficients")
    print(f"P = {P}")
    for n, m in moments.items():
        print(f"M{n} = {m}")

    with out.derived_results():
        for n, m in moments.items():
            out.line(f"M{n}", StatusMark.PASS if n == 0 else StatusMark.INFO, str(m))
    with out.governance_assessments():
        out.line("moment map", StatusMark.PASS, "payload moments are linear in shape coefficients")
        out.line("operator view", StatusMark.INFO, "shape coefficients map through exactness operator to moment payloads")
    with out.counterexamples():
        out.line("moment constraints nonlinear mystery", StatusMark.FAIL, "moment map is explicit and linear")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[y, a1, a2, a3],
        output=sp.Matrix([moments[0], moments[2], moments[4], moments[6]]),
        method="derive finite moment map from even polynomial shape coefficients",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="shape_coefficient_moment_map",
        scope="reduced compact-support exactness family",
    )
    record_claim(ns, MARKER_ID, "g86_map_c1", GovernanceStatus.POLICY_RULE, "Reduced payload moments form an explicit linear map from even shape coefficients.")
    record_obligation(ns, "g86_map_o1", "Test minimal degree obstruction.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_minimal_degree_obstruction.py")

if __name__ == "__main__":
    main()
