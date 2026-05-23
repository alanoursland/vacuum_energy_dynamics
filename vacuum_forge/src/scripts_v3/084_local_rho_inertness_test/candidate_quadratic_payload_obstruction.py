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
    ("g84_tradeoff", "084_local_rho_inertness_test__candidate_skew_inertness_tradeoff_test", "g84_tradeoff"),
]
MARKER_ID = "g84_quadratic_obstruction"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    y, c = sp.symbols("y c")
    f = (1 - y**2)**3
    w = (1 - y**2)**2
    Xi = f * (1 + c*y)
    J = sp.simplify(w * sp.diff(Xi, y))
    rho = sp.factor(sp.diff(J, y))
    M2 = sp.factor(sp.integrate(sp.expand(y**2*rho), (y, -1, 1)))
    dM2dc = sp.simplify(sp.diff(M2, c))
    M2_solutions = sp.solve(sp.Eq(M2, 0), c)

    header("Candidate Quadratic Payload Obstruction")
    print(f"M2 = integral(y^2*rho dy) = {M2}")
    print(f"dM2/dc = {dM2dc}")
    print(f"c solutions for M2=0 = {M2_solutions}")

    with out.derived_results():
        out.line("M2", StatusMark.WARN, str(M2))
        out.line("dM2/dc", StatusMark.PASS, str(dM2dc))
        out.line("M2 zero solutions", StatusMark.WARN, str(M2_solutions))
    with out.governance_assessments():
        out.line("quadratic obstruction", StatusMark.WARN, "quadratic payload moment is nonzero and independent of c")
        out.line("linear-skew insufficiency", StatusMark.WARN, "no linear-skew choice kills M2")
    with out.counterexamples():
        out.line("linear skew inertness", StatusMark.FAIL, "linear skew cannot make local rho inert to quadratic probe")
        out.line("payload-free overclaim", StatusMark.FAIL, "nonzero M2 blocks finite-mode payload inertness")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[y, c],
        output=M2,
        method="compute quadratic payload moment for generic linear skew",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="quadratic_payload_obstruction",
        scope="linear-skew compact-support family",
    )
    record_claim(ns, MARKER_ID, "g84_quad_c1", GovernanceStatus.POLICY_RULE, "Quadratic payload moment is nonzero and cannot be killed by linear skew in this family.")
    record_obligation(ns, "g84_quad_o1", "Classify local inertness route status.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_local_inertness_route_classifier.py")

if __name__ == "__main__":
    main()
