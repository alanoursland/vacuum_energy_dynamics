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
    ("g97_summary", "97_parity_gap_theorem_attempt__candidate_group_97_status_summary", "g97_summary"),
]
MARKER_ID = "g98_problem"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Burden Ledger Role Problem")
    print("Open Group 98: determine what physical ledger the hierarchy branch is licensed to represent.")
    print("Imported Group 97 state:")
    print("  difference numerator positivity target identified")
    print("  all-order difference numerator theorem open")
    print("  all-order parity gap / ratio-bound / Schur positivity / determinant nonzero remain open")
    print()
    print("Physical bridge question:")
    print("  Is the hierarchy configuration energy, exchange compensation, interface smoothing, total burden, or auxiliary admissibility?")

    with out.governance_assessments():
        out.line("group opened", StatusMark.PASS, "hierarchy burden-ledger role audit opened")
        out.line("real target", StatusMark.PASS, "assign safe current role or defer assignment with explicit requirements")
        out.line("scope", StatusMark.INFO, "role classification and equation-balance audit, not field-equation insertion")
    with out.counterexamples():
        out.line("hierarchy as J_curv by name", StatusMark.FAIL, "J_curv is not covariantly defined")
        out.line("hierarchy as H_exch by name", StatusMark.FAIL, "H_exch is not insertable or independently defined")
        out.line("hierarchy as total burden by name", StatusMark.FAIL, "total burden functional has not been defined")
        out.line("parent equation jump", StatusMark.FAIL, "role audit cannot write a parent equation")
    with out.unresolved_obligations():
        out.line("role decision matrix", StatusMark.OBLIGATION, "score hierarchy against candidate physical ledgers")
        out.line("balance audit", StatusMark.OBLIGATION, "test whether configuration-only accounting can satisfy balance requirements")

    record_marker(ns, MARKER_ID, "Group 98 opening; burden-ledger role audit")
    record_claim(ns, MARKER_ID, "g98_problem_c1", GovernanceStatus.POLICY_RULE, "Group 98 audits the physical role of the determinant/Schur hierarchy before further numerator work.")
    record_obligation(ns, "g98_problem_o1", "Build hierarchy role decision matrix.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_hierarchy_role_decision_matrix.py")

if __name__ == "__main__":
    main()
