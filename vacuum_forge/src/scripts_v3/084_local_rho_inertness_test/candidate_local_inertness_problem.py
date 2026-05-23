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
    ("g83_summary", "083_weighted_exactness_geometry_derivation__candidate_group_83_status_summary", "g83_summary"),
]
MARKER_ID = "g84_problem"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Local Rho Inertness Problem")
    print("Question: Is the Group 83 skewed local rho inert to low-order payload probes?")
    print("Imported Group 83 status:")
    print("  weighted skew c=3ell/(2R) derived in reduced class")
    print("  weighted exactness route strengthened")
    print("  local rho nonzero remains")
    print("  payload inertness remains open")
    print("  full covariant theorem remains open")
    print("  parent divergence identity unproven")
    print("  recombination blocked")
    print("Group 84 boundary: finite-mode inertness test only, not full payload theorem.")

    with out.governance_assessments():
        out.line("group opened", StatusMark.PASS, "local rho inertness finite-mode test opened")
        out.line("real target", StatusMark.PASS, "test local rho against concrete low-order probes")
        out.line("scope", StatusMark.INFO, "finite reduced probe basis, not full covariant payload basis")
        out.line("parent status", StatusMark.DEFER, "parent equation remains blocked")
    with out.counterexamples():
        out.line("weighted as local inertness", StatusMark.FAIL, "weighted total neutrality cannot imply local inertness")
        out.line("finite test as full theorem", StatusMark.FAIL, "finite-mode test cannot prove full physical inertness")
        out.line("parent jump", StatusMark.FAIL, "local inertness test cannot write parent equation")
    with out.unresolved_obligations():
        out.line("probe basis", StatusMark.OBLIGATION, "define low-order payload probes")
        out.line("moment tests", StatusMark.OBLIGATION, "compute flat and weighted moments")

    record_marker(ns, MARKER_ID, "Group 84 opening; local rho inertness finite-mode test")
    record_claim(ns, MARKER_ID, "g84_problem_c1", GovernanceStatus.UNVERIFIED, "Group 84 opens finite-mode local rho inertness test.")
    record_obligation(ns, "g84_problem_o1", "Define low-order payload probe basis.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_payload_probe_basis.py")

if __name__ == "__main__":
    main()
