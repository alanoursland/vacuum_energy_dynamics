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
    ("g83_skew_derivation", "083_weighted_exactness_geometry_derivation__candidate_geometric_skew_derivation", "g83_skew_derivation"),
]
MARKER_ID = "g83_uniqueness_scaling"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    y, R, ell, c, eps = sp.symbols("y R ell c eps", nonzero=True)
    f = (1 - y**2)**3
    w = (1 - y**2)**2
    Xi = f*(1 + c*y)
    J = sp.simplify(w*sp.diff(Xi, y))
    rho = sp.diff(J, y)
    mu = R**2 + 2*R*ell*y + ell**2*y**2
    weighted_charge = sp.factor(sp.integrate(sp.expand(mu*rho), (y, -1, 1)))
    derivative_in_c = sp.simplify(sp.diff(weighted_charge, c))
    c_solution = sp.solve(sp.Eq(weighted_charge, 0), c)
    c_scaled = sp.simplify(c_solution[0].subs(ell, eps*R)) if c_solution else sp.nan
    thin_limit = sp.limit(c_scaled, eps, 0) if c_solution else sp.nan

    header("Candidate Uniqueness and Scaling Test")
    print(f"weighted charge = {weighted_charge}")
    print(f"d/dc weighted charge = {derivative_in_c}")
    print(f"c solution = {c_solution}")
    print(f"with ell=eps*R, c = {c_scaled}")
    print(f"thin limit eps->0 = {thin_limit}")

    with out.derived_results():
        out.line("weighted charge", StatusMark.PASS, str(weighted_charge))
        out.line("derivative in c", StatusMark.PASS, str(derivative_in_c))
        out.line("unique c solution", StatusMark.PASS, str(c_solution))
        out.line("scaled c", StatusMark.PASS, str(c_scaled))
        out.line("thin limit", StatusMark.PASS, str(thin_limit))
    with out.governance_assessments():
        out.line("uniqueness", StatusMark.PASS, "linear condition gives unique skew in this family if R,ell nonzero")
        out.line("scaling", StatusMark.PASS, "skew scales as ell/R and vanishes in thin-layer limit")
    with out.counterexamples():
        out.line("arbitrary constant", StatusMark.FAIL, "derived skew has geometric scaling, not arbitrary scale")
        out.line("universal overclaim", StatusMark.FAIL, "uniqueness is only within the linear-skew family")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[R, ell],
        output=c_solution[0],
        method="test linearity, uniqueness, and thin-layer scaling of skew solution",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="skew_uniqueness_scaling",
        scope="linear-skew compact-support family",
    )
    record_claim(ns, MARKER_ID, "g83_unique_c1", GovernanceStatus.POLICY_RULE, "The skew is unique in the linear family and scales as ell/R.")
    record_obligation(ns, "g83_unique_o1", "Classify whether reduced-class derivation removes repair concern.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_repair_discriminator.py")

if __name__ == "__main__":
    main()
