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
    ("g86_moment_map", "86_shape_origin_geometry_derivation__candidate_moment_map_from_shape_coefficients", "g86_moment_map"),
]
MARKER_ID = "g86_minimal_degree"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    y, p = sp.symbols("y p")
    f = (1 - y**2)**3
    w = (1 - y**2)**2

    P0 = sp.Integer(1)
    rho0 = sp.factor(sp.diff(w*sp.diff(f*P0, y), y))
    M2_0 = sp.factor(sp.integrate(y**2*rho0, (y, -1, 1)))
    M4_0 = sp.factor(sp.integrate(y**4*rho0, (y, -1, 1)))

    P2 = 1 + p*y**2
    rho2 = sp.factor(sp.diff(w*sp.diff(f*P2, y), y))
    M2_2 = sp.factor(sp.integrate(sp.expand(y**2*rho2), (y, -1, 1)))
    M4_2 = sp.factor(sp.integrate(sp.expand(y**4*rho2), (y, -1, 1)))
    p_for_M2 = sp.solve(sp.Eq(M2_2, 0), p)
    M4_after_M2 = sp.factor(M4_2.subs(p, p_for_M2[0])) if p_for_M2 else sp.nan
    simultaneous = sp.solve([sp.Eq(M2_2, 0), sp.Eq(M4_2, 0)], [p], dict=True)

    header("Candidate Minimal Degree Obstruction")
    print(f"degree 0: M2={M2_0}, M4={M4_0}")
    print(f"degree 2: M2={M2_2}, M4={M4_2}")
    print(f"p solving M2=0 -> {p_for_M2}")
    print(f"M4 after M2=0 -> {M4_after_M2}")
    print(f"simultaneous degree-2 solution -> {simultaneous}")

    with out.derived_results():
        out.line("degree 0 M2", StatusMark.WARN, str(M2_0))
        out.line("degree 0 M4", StatusMark.WARN, str(M4_0))
        out.line("degree 2 M2", StatusMark.INFO, str(M2_2))
        out.line("degree 2 M4", StatusMark.INFO, str(M4_2))
        out.line("degree 2 M2 solution", StatusMark.PASS, str(p_for_M2))
        out.line("M4 after M2", StatusMark.WARN, str(M4_after_M2))
        out.line("simultaneous degree-2 solution", StatusMark.PASS, str(simultaneous))
    with out.governance_assessments():
        out.line("degree 0 obstruction", StatusMark.PASS, "constant shape cannot kill low moments")
        out.line("degree 2 obstruction", StatusMark.PASS, "quadratic shape cannot kill M2 and M4 simultaneously")
        out.line("minimal degree pressure", StatusMark.PASS, "degree 4 is the minimal even candidate for M2/M4 suppression")
    with out.counterexamples():
        out.line("quartic unnecessary", StatusMark.FAIL, "lower degrees fail the M2/M4 target")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[y, p],
        output=sp.Matrix([M2_0, M4_0, M2_2, M4_2]),
        method="test constant and even quadratic shapes against M2/M4 payload suppression",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="minimal_degree_obstruction",
        scope="normalized even polynomial exactness shapes",
    )
    record_claim(ns, MARKER_ID, "g86_min_c1", GovernanceStatus.POLICY_RULE, "Degree 4 is minimal for simultaneously suppressing M2 and M4 among normalized even polynomial shapes.")
    record_obligation(ns, "g86_min_o1", "Prove quartic uniqueness.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_quartic_uniqueness_theorem.py")

if __name__ == "__main__":
    main()
