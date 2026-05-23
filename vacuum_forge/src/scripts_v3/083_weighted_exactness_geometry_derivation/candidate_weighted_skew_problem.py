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
    ("g82_summary", "082_rho_exactness_concrete_test__candidate_group_82_status_summary", "g82_summary"),
]
MARKER_ID = "g83_problem"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Weighted Skew Problem")
    print("Question: Is c = 3 ell/(2R) forced by weighted exactness geometry?")
    print("Imported Group 82 status:")
    print("  flat integrated neutrality derived in reduced compact-support class")
    print("  local rho remains nonzero")
    print("  weighted/geometric neutrality is not automatic")
    print("  skew c = 3ell/(2R) restores weighted neutrality as compatibility")
    print("  skew must be derived geometrically, not chosen")
    print("  payload inertness remains open")
    print("  parent divergence identity unproven")
    print("  recombination blocked")

    with out.governance_assessments():
        out.line("group opened", StatusMark.PASS, "weighted-skew geometry derivation attempt opened")
        out.line("real target", StatusMark.PASS, "derive previously found skew from measure-gradient orthogonality")
        out.line("parent status", StatusMark.DEFER, "parent equation remains blocked")
        out.line("recombination", StatusMark.DEFER, "recombination remains blocked")
    with out.counterexamples():
        out.line("solve again only", StatusMark.FAIL, "must derive origin, not just solve weighted charge again")
        out.line("local closure overclaim", StatusMark.FAIL, "weighted skew cannot imply local rho=0")
        out.line("parent jump", StatusMark.FAIL, "weighted exactness cannot write parent equation")
    with out.unresolved_obligations():
        out.line("measure-gradient identity", StatusMark.OBLIGATION, "derive weighted charge as flux orthogonality")
        out.line("parity derivation", StatusMark.OBLIGATION, "derive c from parity-surviving terms")

    record_marker(ns, MARKER_ID, "Group 83 opening; weighted skew geometry target")
    record_claim(ns, MARKER_ID, "g83_problem_c1", GovernanceStatus.UNVERIFIED, "Group 83 attempts to derive weighted skew from reduced measure geometry.")
    record_obligation(ns, "g83_problem_o1", "Derive measure-gradient identity and parity decomposition.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_measure_gradient_identity.py")

if __name__ == "__main__":
    main()
