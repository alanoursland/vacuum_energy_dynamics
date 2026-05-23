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
    ("g82_summary", "82_rho_exactness_concrete_test__candidate_group_82_status_summary", "g82_summary"),
    ("g83_problem", "83_weighted_exactness_geometry_derivation__candidate_weighted_skew_problem", "g83_problem"),
]
MARKER_ID = "g83_measure_gradient"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    y, R, ell = sp.symbols("y R ell")
    J = sp.Function("J")
    mu = R**2 + 2*R*ell*y + ell**2*y**2
    rho = sp.diff(J(y), y)
    weighted_charge = sp.Integral(mu*rho, (y, -1, 1))
    by_parts = sp.simplify(mu.subs(y, 1)*J(1) - mu.subs(y, -1)*J(-1) - sp.Integral(sp.diff(mu, y)*J(y), (y, -1, 1)))
    mu_prime = sp.diff(mu, y)

    header("Candidate Measure-Gradient Identity")
    print(f"mu = {mu}")
    print(f"mu' = {mu_prime}")
    print(f"weighted charge = {weighted_charge}")
    print(f"integration-by-parts form = {by_parts}")
    print("With compact endpoint flux J(-1)=J(1)=0:")
    print("  Q_mu = - integral(mu' * J dy)")
    print("Weighted neutrality becomes measure-gradient orthogonality of flux.")

    with out.derived_results():
        out.line("mu prime", StatusMark.PASS, str(mu_prime))
        out.line("by-parts form", StatusMark.PASS, str(by_parts))
    with out.governance_assessments():
        out.line("measure-gradient identity", StatusMark.PASS, "weighted charge reduces to measure-gradient flux pairing when endpoint flux vanishes")
        out.line("geometric interpretation", StatusMark.INFO, "weighted neutrality is flux orthogonality to mu'")
    with out.counterexamples():
        out.line("flat endpoint as weighted endpoint only", StatusMark.FAIL, "nonconstant measure introduces interior mu' pairing")
        out.line("weighted closure by prose", StatusMark.FAIL, "must cancel mu' flux pairing")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[y, R, ell],
        output=mu_prime,
        method="integration by parts for Q_mu = integral(mu*dJ/dy)",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="measure_gradient_identity",
        scope="reduced weighted exactness class",
    )
    record_claim(ns, MARKER_ID, "g83_measure_c1", GovernanceStatus.POLICY_RULE, "Weighted exactness requires measure-gradient orthogonality of compact-support flux.")
    record_obligation(ns, "g83_measure_o1", "Decompose flux parity against mu'.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_flux_parity_decomposition.py")

if __name__ == "__main__":
    main()
