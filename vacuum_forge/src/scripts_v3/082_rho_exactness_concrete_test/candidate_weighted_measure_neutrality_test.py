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
    ("g82_local_nonzero", "082_rho_exactness_concrete_test__candidate_local_remainder_nonzero_test", "g82_local_nonzero"),
]
MARKER_ID = "g82_weighted"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    y, R, ell = sp.symbols("y R ell", nonzero=True)
    w = (1 - y**2)**2
    Xi = (1 - y**2)**3
    J = sp.simplify(w * sp.diff(Xi, y))
    rho = sp.factor(sp.diff(J, y))
    mu = R**2 + 2*R*ell*y + ell**2*y**2
    flat_charge = sp.simplify(sp.integrate(rho, (y, -1, 1)))
    weighted_charge = sp.factor(sp.integrate(sp.expand(mu*rho), (y, -1, 1)))

    header("Candidate Weighted Measure Neutrality Test")
    print(f"mu = {mu}")
    print(f"flat charge = {flat_charge}")
    print(f"weighted charge = {weighted_charge}")
    print("Interpretation: exact flat neutrality does not automatically imply weighted/geometric neutrality.")

    with out.derived_results():
        out.line("flat charge", StatusMark.PASS, str(flat_charge))
        out.line("weighted charge", StatusMark.WARN, str(weighted_charge))
    with out.governance_assessments():
        out.line("weighted obstruction", StatusMark.WARN, "nonconstant measure can produce nonzero weighted charge")
        out.line("covariant caution", StatusMark.OBLIGATION, "derive weighted neutrality or measure-compatible skew")
    with out.counterexamples():
        out.line("flat exactness as covariant neutrality", StatusMark.FAIL, "false unless weighted charge also vanishes")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[y, R, ell],
        output=weighted_charge,
        method="integrate mu*rho over [-1,1] for compact-support exact rho",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="weighted_measure_neutrality_test",
        scope="reduced layer with quadratic geometric measure",
    )
    record_claim(ns, MARKER_ID, "g82_weighted_c1", GovernanceStatus.POLICY_RULE, "Flat exactness does not automatically imply weighted neutrality in the tested class.")
    record_obligation(ns, "g82_weighted_o1", "Test whether a skew condition can restore weighted neutrality.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_skew_condition_for_weighted_neutrality.py")

if __name__ == "__main__":
    main()
