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
    ("g82_compact_support", "082_rho_exactness_concrete_test__candidate_compact_support_exact_remainder", "g82_compact_support"),
]
MARKER_ID = "g82_local_nonzero"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    y = sp.symbols("y")
    w = (1 - y**2)**2
    Xi = (1 - y**2)**3
    J = sp.simplify(w * sp.diff(Xi, y))
    rho = sp.factor(sp.diff(J, y))
    rho_at_zero = sp.simplify(rho.subs(y, 0))
    rho_is_zero = sp.simplify(rho) == 0
    roots = sp.solve(sp.Eq(rho, 0), y)

    header("Candidate Local Remainder Nonzero Test")
    print(f"rho = {rho}")
    print(f"rho(0) = {rho_at_zero}")
    print(f"rho identically zero? {rho_is_zero}")
    print(f"rho roots = {roots}")

    with out.derived_results():
        out.line("rho expression", StatusMark.PASS, str(rho))
        out.line("rho at zero", StatusMark.PASS, str(rho_at_zero))
        out.line("rho identically zero", StatusMark.PASS, str(rho_is_zero))
    with out.governance_assessments():
        out.line("local nonzero", StatusMark.WARN, "rho is locally nonzero even though flat charge vanishes")
        out.line("local inertness", StatusMark.OBLIGATION, "local nonzero rho requires inertness or payload filter")
    with out.counterexamples():
        out.line("flat neutral implies local zero", StatusMark.FAIL, "false in this concrete class")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[y],
        output=rho,
        method="evaluate compact-support exact rho locally",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="local_remainder_nonzero_test",
        scope="reduced compact-support exactness class",
    )
    record_claim(ns, MARKER_ID, "g82_local_c1", GovernanceStatus.POLICY_RULE, "Flat exact neutrality does not imply local rho=0 in the tested class.")
    record_obligation(ns, "g82_local_o1", "Test weighted measure neutrality.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_weighted_measure_neutrality_test.py")

if __name__ == "__main__":
    main()
