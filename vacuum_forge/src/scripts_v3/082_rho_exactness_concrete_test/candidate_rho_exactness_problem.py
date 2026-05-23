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
    ("g81_summary", "81_concrete_geometry_input_handoff__candidate_group_81_status_summary", "g81_summary"),
]
MARKER_ID = "g82_problem"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Rho Exactness Problem")
    print("Question: Can a concrete exact/divergence form pay down the rho obstruction?")
    print("Imported Group 81 status:")
    print("  future theorem work requires a real object")
    print("  rho route accepts exactness operator / boundary divergence / inertness tests")
    print("  rho=0 by assertion, exact-by-label, and dropped rho are rejected")
    print("  parent divergence identity unproven")
    print("  recombination blocked")
    print("Group 82 concrete candidate: rho = dJ/dy on y in [-1, 1].")

    with out.governance_assessments():
        out.line("group opened", StatusMark.PASS, "concrete rho exactness test opened")
        out.line("real object", StatusMark.PASS, "candidate exact operator rho=dJ/dy supplied")
        out.line("parent status", StatusMark.DEFER, "parent equation remains blocked")
        out.line("recombination", StatusMark.DEFER, "recombination remains blocked")
    with out.counterexamples():
        out.line("rho by assertion", StatusMark.FAIL, "rho=0 by assertion remains forbidden")
        out.line("exact by label", StatusMark.FAIL, "exactness must be calculated")
        out.line("parent jump", StatusMark.FAIL, "rho exactness test cannot write parent equation")
    with out.unresolved_obligations():
        out.line("exactness tests", StatusMark.OBLIGATION, "test endpoint flux, flat charge, local residual, weighted charge, and payloads")

    record_marker(ns, MARKER_ID, "Group 82 opening; concrete rho exactness object supplied")
    record_claim(ns, MARKER_ID, "g82_problem_c1", GovernanceStatus.UNVERIFIED, "Group 82 opens concrete rho exactness test.")
    record_obligation(ns, "g82_problem_o1", "Test compact-support exact remainder.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_exact_operator_requirements.py")

if __name__ == "__main__":
    main()
