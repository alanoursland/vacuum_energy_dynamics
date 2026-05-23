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
    ("g84_problem", "084_local_rho_inertness_test__candidate_local_inertness_problem", "g84_problem"),
]
MARKER_ID = "g84_probe_basis"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    y = sp.symbols("y")
    probes = [1, y, y**2]
    names = ["P0_uniform_global_source", "P1_dipole_gradient", "P2_quadratic_width_curvature"]

    header("Candidate Payload Probe Basis")
    print("Low-order payload probes:")
    for name, probe in zip(names, probes):
        print(f"  {name}: {probe}")
    print("Moment test:")
    print("  M_n = integral(y^n * rho dy), n=0,1,2")
    print("Interpretation:")
    print("  M0 tests global/source neutrality")
    print("  M1 tests dipole/gradient sensitivity")
    print("  M2 tests quadratic/width/curvature sensitivity")

    with out.governance_assessments():
        out.line("probe basis", StatusMark.PASS, "low-order finite probe basis stated")
        out.line("scope", StatusMark.INFO, "basis is finite and reduced, not complete physical basis")
        out.line("inertness criterion", StatusMark.OBLIGATION, "vanishing of tested moments required for finite-mode inertness")
    with out.counterexamples():
        out.line("complete basis overclaim", StatusMark.FAIL, "1,y,y^2 basis cannot prove full inertness")
        out.line("no-payload by wish", StatusMark.FAIL, "payload inertness must be tested")

    record_marker(ns, MARKER_ID, "payload probe basis; finite reduced test")
    record_claim(ns, MARKER_ID, "g84_basis_c1", GovernanceStatus.POLICY_RULE, "Low-order payload moments provide a finite reduced inertness test, not full physical theorem.")
    record_obligation(ns, "g84_basis_o1", "Compute flat payload moments for derived skew.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_flat_probe_moment_test.py")

if __name__ == "__main__":
    main()
