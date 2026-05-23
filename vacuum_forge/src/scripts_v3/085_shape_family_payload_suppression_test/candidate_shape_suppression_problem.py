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
    ("g84_summary", "84_local_rho_inertness_test__candidate_group_84_status_summary", "g84_summary"),
]
MARKER_ID = "g85_problem"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Shape Suppression Problem")
    print("Question: Can a richer exactness shape suppress the low-order payload moments that defeated linear skew?")
    print("Imported Group 84 status:")
    print("  global and weighted total neutrality retained")
    print("  dipole and quadratic payload moments nonzero in linear-skew family")
    print("  linear skew cannot kill quadratic payload")
    print("  local inertness obstructed in finite-mode test")
    print("  parent divergence identity unproven")
    print("  recombination blocked")
    print("Group 85 concrete route: even quartic shape P(y)=1+p*y^2+q*y^4.")

    with out.governance_assessments():
        out.line("group opened", StatusMark.PASS, "shape-family payload suppression test opened")
        out.line("real target", StatusMark.PASS, "test new degrees of freedom, not same linear-skew obstruction")
        out.line("scope", StatusMark.INFO, "reduced compact-support family, not full inertness theorem")
        out.line("parent status", StatusMark.DEFER, "parent equation remains blocked")
    with out.counterexamples():
        out.line("redo linear skew", StatusMark.FAIL, "Group 84 already obstructed linear skew")
        out.line("full inertness overclaim", StatusMark.FAIL, "finite shape suppression cannot prove full inertness")
        out.line("parent jump", StatusMark.FAIL, "shape test cannot write parent equation")
    with out.unresolved_obligations():
        out.line("shape family", StatusMark.OBLIGATION, "derive even quartic shape moments")
        out.line("shape origin", StatusMark.OBLIGATION, "if shape works, future group must derive its origin")

    record_marker(ns, MARKER_ID, "Group 85 opening; even quartic shape-family test")
    record_claim(ns, MARKER_ID, "g85_problem_c1", GovernanceStatus.UNVERIFIED, "Group 85 tests whether richer exactness shape suppresses finite-mode payload moments.")
    record_obligation(ns, "g85_problem_o1", "Define even quartic shape family.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_even_quartic_shape_family.py")

if __name__ == "__main__":
    main()
