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
    ("g82_weighted", "082_rho_exactness_concrete_test__candidate_weighted_measure_neutrality_test", "g82_weighted"),
]
MARKER_ID = "g82_skew_condition"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    y, R, ell, c = sp.symbols("y R ell c", nonzero=True)
    w = (1 - y**2)**2
    Xi = (1 - y**2)**3 * (1 + c*y)
    J = sp.simplify(w * sp.diff(Xi, y))
    rho = sp.factor(sp.diff(J, y))
    mu = R**2 + 2*R*ell*y + ell**2*y**2
    flat_charge = sp.simplify(sp.integrate(rho, (y, -1, 1)))
    weighted_charge = sp.factor(sp.integrate(sp.expand(mu*rho), (y, -1, 1)))
    c_solution = sp.solve(sp.Eq(weighted_charge, 0), c)
    weighted_at_solution = sp.simplify(weighted_charge.subs(c, c_solution[0])) if c_solution else weighted_charge

    header("Candidate Skew Condition for Weighted Neutrality")
    print(f"Xi_skew = {Xi}")
    print(f"flat charge = {flat_charge}")
    print(f"weighted charge = {weighted_charge}")
    print(f"c solution for weighted neutrality = {c_solution}")
    print(f"weighted charge at solution = {weighted_at_solution}")

    with out.derived_results():
        out.line("flat charge", StatusMark.PASS, str(flat_charge))
        out.line("weighted charge", StatusMark.WARN, str(weighted_charge))
        out.line("c solution", StatusMark.PASS, str(c_solution))
        out.line("weighted at solution", StatusMark.PASS, str(weighted_at_solution))
    with out.governance_assessments():
        out.line("skew compatibility", StatusMark.INFO, "weighted neutrality can be restored by a skew condition in this class")
        out.line("skew derivation", StatusMark.OBLIGATION, "c must be derived geometrically, not selected")
    with out.counterexamples():
        out.line("chosen skew", StatusMark.FAIL, "choosing c to cancel weighted charge is compatibility, not theorem")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[y, R, ell, c],
        output=weighted_charge,
        method="solve for skew coefficient c that makes weighted charge vanish",
        status=Status.DERIVED,
        record_kind=RecordKind.COMPATIBILITY_EXAMPLE,
        result_type="weighted_skew_condition",
        scope="reduced layer weighted-neutrality compatibility",
    )
    record_claim(ns, MARKER_ID, "g82_skew_c1", GovernanceStatus.POLICY_RULE, "Weighted neutrality requires a derived skew condition; chosen skew is compatibility only.")
    record_obligation(ns, "g82_skew_o1", "Derive skew coefficient from geometry if weighted exactness route continues.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_payload_inertness_filter.py")

if __name__ == "__main__":
    main()
