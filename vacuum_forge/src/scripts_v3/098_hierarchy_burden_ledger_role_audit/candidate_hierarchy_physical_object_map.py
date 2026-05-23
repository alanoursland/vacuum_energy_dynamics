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

def status_label(ok: bool) -> str:
    return "PASS" if ok else "FAIL"

DEPENDENCIES = [
    ("g98_balance_audit", "98_hierarchy_burden_ledger_role_audit__candidate_ledger_balance_equation_audit", "g98_balance_audit"),
]
MARKER_ID = "g98_object_map"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    mappings = [
        ("det(A_N) nonzero", "finite hierarchy uniqueness / nondegeneracy", "admissibility support", "not a physical energy functional"),
        ("row-signed Schur positivity", "stable leading response chain", "admissibility support", "not J_curv definition"),
        ("Schur gap positivity", "positive post-transition admissibility gap", "proof target", "not exchange current"),
        ("parity branch monotonicity", "structured response convergence clue", "proof target", "not field equation"),
        ("difference numerator positivity", "exact algebraic sign target for admissibility", "next theorem target", "not source law"),
    ]

    rejected = [
        "hierarchy = covariant J_curv",
        "hierarchy = H_curv",
        "hierarchy = H_exch",
        "hierarchy = total burden functional",
        "hierarchy = merger energy prediction",
        "hierarchy = source law",
        "hierarchy = anti-singularity dynamics",
    ]

    header("Candidate Hierarchy Physical Object Map")
    print("Allowed weak mappings:")
    for obj, meaning, role, not_role in mappings:
        print(f"  {obj}: {meaning}; role={role}; guard={not_role}")
    print("\nRejected strong mappings:")
    for item in rejected:
        print(f"  - {item}")

    with out.governance_assessments():
        out.line("determinant role", StatusMark.PASS, "finite response uniqueness / nondegeneracy candidate")
        out.line("Schur role", StatusMark.PASS, "stable admissibility chain candidate")
        out.line("numerator role", StatusMark.PASS, "exact algebraic proof target")
        out.line("physical assignment", StatusMark.DEFER, "not yet assigned to J_curv/exchange/interface/total burden")
    with out.counterexamples():
        for item in rejected:
            out.line(item, StatusMark.FAIL, "not licensed by current hierarchy evidence")
    with out.unresolved_obligations():
        out.line("source origin", StatusMark.OBLIGATION, "derive what physical variational/source problem produces A_N")
        out.line("functional origin", StatusMark.OBLIGATION, "derive whether hierarchy comes from J_curv, interface, exchange, or total burden")
        out.line("merger check route", StatusMark.OBLIGATION, "only after physical functional is assigned")

    record_marker(ns, MARKER_ID, "hierarchy physical object map")
    record_claim(ns, MARKER_ID, "g98_map_c1", GovernanceStatus.POLICY_RULE, "Hierarchy objects currently map safely to auxiliary admissibility roles, not to physical energy/source/correction tensors.")
    record_obligation(ns, "g98_map_o1", "Classify final role decision surface.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_role_decision_surface_classifier.py")

if __name__ == "__main__":
    main()
