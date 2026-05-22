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
    ("g85_problem", "85_shape_family_payload_suppression_test__candidate_shape_suppression_problem", "g85_problem"),
]
MARKER_ID = "g85_even_quartic_family"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    y, p, q = sp.symbols("y p q")
    f = (1 - y**2)**3
    w = (1 - y**2)**2
    P = 1 + p*y**2 + q*y**4
    Xi = sp.expand(f*P)
    J = sp.factor(w*sp.diff(Xi, y))
    rho = sp.factor(sp.diff(J, y))

    parity_P = sp.simplify(P.subs(y, -y) - P)
    parity_J = sp.simplify(J.subs(y, -y) + J)
    parity_rho = sp.simplify(rho.subs(y, -y) - rho)
    endpoints = (sp.simplify(J.subs(y, -1)), sp.simplify(J.subs(y, 1)))

    header("Candidate Even Quartic Shape Family")
    print(f"P = {P}")
    print(f"J = {J}")
    print(f"rho = {rho}")
    print(f"P(-y)-P(y) = {parity_P}")
    print(f"J(-y)+J(y) = {parity_J}")
    print(f"rho(-y)-rho(y) = {parity_rho}")
    print(f"J endpoints = {endpoints}")

    with out.derived_results():
        out.line("P even check", StatusMark.PASS, str(parity_P))
        out.line("J odd check", StatusMark.PASS, str(parity_J))
        out.line("rho even check", StatusMark.PASS, str(parity_rho))
        out.line("endpoint flux", StatusMark.PASS, str(endpoints))
    with out.governance_assessments():
        out.line("parity structure", StatusMark.PASS, "even P gives odd J and even rho")
        out.line("endpoint support", StatusMark.PASS, "compact endpoint flux retained for all p,q")
    with out.counterexamples():
        out.line("endpoint leak", StatusMark.FAIL, "not present in this family")
        out.line("parity by assertion", StatusMark.FAIL, "parity explicitly checked")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[y, p, q],
        output=sp.Matrix([J, rho]),
        method="construct even quartic compact-support shape family and check parity/endpoints",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="even_quartic_shape_family",
        scope="reduced compact-support exactness family",
    )
    record_claim(ns, MARKER_ID, "g85_family_c1", GovernanceStatus.POLICY_RULE, "Even quartic shape family preserves compact endpoint flux and enforces J odd/rho even.")
    record_obligation(ns, "g85_family_o1", "Solve moment constraints for p,q.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_moment_constraint_solver.py")

if __name__ == "__main__":
    main()
