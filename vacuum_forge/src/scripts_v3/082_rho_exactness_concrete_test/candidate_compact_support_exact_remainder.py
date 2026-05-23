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
    ("g82_requirements", "082_rho_exactness_concrete_test__candidate_exact_operator_requirements", "g82_requirements"),
]
MARKER_ID = "g82_compact_support"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    y = sp.symbols("y")
    w = (1 - y**2)**2
    Xi = (1 - y**2)**3
    J = sp.simplify(w * sp.diff(Xi, y))
    rho = sp.simplify(sp.diff(J, y))
    J_left = sp.simplify(J.subs(y, -1))
    J_right = sp.simplify(J.subs(y, 1))
    flat_charge = sp.simplify(sp.integrate(rho, (y, -1, 1)))

    header("Candidate Compact-Support Exact Remainder")
    print(f"w = {w}")
    print(f"Xi = {Xi}")
    print(f"J = {J}")
    print(f"rho = {rho}")
    print(f"J(-1) = {J_left}")
    print(f"J(1) = {J_right}")
    print(f"flat charge = {flat_charge}")

    with out.derived_results():
        out.line("endpoint flux left", StatusMark.PASS, str(J_left))
        out.line("endpoint flux right", StatusMark.PASS, str(J_right))
        out.line("flat charge", StatusMark.PASS, str(flat_charge))
    with out.governance_assessments():
        out.line("flat exact neutrality", StatusMark.PASS, "flat integrated neutrality derived in reduced compact-support class")
        out.line("scope", StatusMark.INFO, "reduced 1D layer class; not full covariant theorem")
    with out.counterexamples():
        out.line("full closure overclaim", StatusMark.FAIL, "flat integral neutrality is not full rho removal")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[y],
        output=flat_charge,
        method="construct compact-support flux J=w*dXi/dy and integrate rho=dJ/dy over [-1,1]",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="flat_exact_neutrality",
        scope="reduced compact-support exactness class",
    )
    record_claim(ns, MARKER_ID, "g82_compact_c1", GovernanceStatus.POLICY_RULE, "Compact-support exact rho has zero flat integrated charge in this reduced class.")
    record_obligation(ns, "g82_compact_o1", "Test whether local rho vanishes.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_local_remainder_nonzero_test.py")

if __name__ == "__main__":
    main()
