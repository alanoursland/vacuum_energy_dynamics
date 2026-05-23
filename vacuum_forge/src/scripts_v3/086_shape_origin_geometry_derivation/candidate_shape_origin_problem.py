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
    ("g85_summary", "85_shape_family_payload_suppression_test__candidate_group_85_status_summary", "g85_summary"),
]
MARKER_ID = "g86_problem"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Shape Origin Problem")
    print("Question: Is P=1-12y^2+51y^4 structurally forced inside the reduced payload-suppression problem?")
    print("Imported Group 85 status:")
    print("  even quartic suppression profile found")
    print("  M0..M5 vanish")
    print("  W0..W3 vanish")
    print("  local rho remains nonzero")
    print("  M6/W4 remain nonzero")
    print("  shape origin remains open")
    print("  parent divergence identity unproven")
    print("  recombination blocked")

    with out.governance_assessments():
        out.line("group opened", StatusMark.PASS, "shape-origin structural test opened")
        out.line("real target", StatusMark.PASS, "test minimal-degree and variational origin")
        out.line("scope", StatusMark.INFO, "reduced model origin, not full physical derivation")
        out.line("parent status", StatusMark.DEFER, "parent equation remains blocked")
    with out.counterexamples():
        out.line("moment profile as full geometry", StatusMark.FAIL, "must not promote reduced origin to full geometry")
        out.line("all-order inertness", StatusMark.FAIL, "M6/W4 remain from Group 85")
        out.line("parent jump", StatusMark.FAIL, "shape-origin test cannot write parent equation")
    with out.unresolved_obligations():
        out.line("minimal degree", StatusMark.OBLIGATION, "test lower-degree obstruction and quartic uniqueness")
        out.line("variational origin", StatusMark.OBLIGATION, "test payload-action minimizer")

    record_marker(ns, MARKER_ID, "Group 86 opening; reduced shape origin test")
    record_claim(ns, MARKER_ID, "g86_problem_c1", GovernanceStatus.UNVERIFIED, "Group 86 tests reduced structural origin of the Group 85 suppression profile.")
    record_obligation(ns, "g86_problem_o1", "Derive moment map from shape coefficients.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_moment_map_from_shape_coefficients.py")

if __name__ == "__main__":
    main()
