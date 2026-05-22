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
    ("g83_parity", "83_weighted_exactness_geometry_derivation__candidate_flux_parity_decomposition", "g83_parity"),
]
MARKER_ID = "g83_skew_derivation"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    y, R, ell, c = sp.symbols("y R ell c", nonzero=True)
    f = (1 - y**2)**3
    w = (1 - y**2)**2
    J0 = sp.factor(w * sp.diff(f, y))
    J1 = sp.factor(w * (f + y*sp.diff(f, y)))
    A = sp.simplify(sp.integrate(J1, (y, -1, 1)))
    B = sp.simplify(sp.integrate(y*J0, (y, -1, 1)))
    c_from_moments = sp.simplify(-ell*B/(R*A))
    pairing = sp.factor(2*R*ell*c*A + 2*ell**2*B)
    solved_c = sp.solve(sp.Eq(pairing, 0), c)
    target = sp.simplify(3*ell/(2*R))
    check = sp.simplify(c_from_moments - target)

    header("Candidate Geometric Skew Derivation")
    print(f"A = int J1 dy = {A}")
    print(f"B = int y*J0 dy = {B}")
    print(f"measure-gradient pairing = {pairing}")
    print(f"c from moment ratio = -ell*B/(R*A) = {c_from_moments}")
    print(f"solve pairing=0 -> {solved_c}")
    print(f"target 3ell/(2R) = {target}")
    print(f"difference = {check}")

    with out.derived_results():
        out.line("A moment", StatusMark.PASS, str(A))
        out.line("B moment", StatusMark.PASS, str(B))
        out.line("c from moments", StatusMark.PASS, str(c_from_moments))
        out.line("target check", StatusMark.PASS, str(check))
    with out.governance_assessments():
        out.line("skew derived", StatusMark.PASS, "c=3ell/(2R) forced by measure-gradient orthogonality in reduced class")
        out.line("scope", StatusMark.INFO, "depends on reduced measure and chosen f,w compact-support family")
    with out.counterexamples():
        out.line("chosen c only", StatusMark.FAIL, "within this model c follows from moment ratio, not arbitrary selection")
        out.line("full covariant overclaim", StatusMark.FAIL, "reduced-class derivation is not full covariant theorem")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[y, R, ell],
        output=c_from_moments,
        method="derive c from measure-gradient flux orthogonality moment ratio",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="weighted_skew_derivation",
        scope="reduced weighted exactness class; linear-skew compact-support family",
    )
    record_claim(ns, MARKER_ID, "g83_skew_c1", GovernanceStatus.POLICY_RULE, "Within the reduced weighted-exactness class, c=3ell/(2R) is forced by measure-gradient orthogonality.")
    record_obligation(ns, "g83_skew_o1", "Test uniqueness and scaling of the derived skew.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_uniqueness_and_scaling_test.py")

if __name__ == "__main__":
    main()
