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
    ("g83_summary", "83_weighted_exactness_geometry_derivation__candidate_group_83_status_summary", "g83_summary"),
    ("g84_problem", "84_local_rho_inertness_test__candidate_local_inertness_problem", "g84_problem"),
    ("g84_probe_basis", "84_local_rho_inertness_test__candidate_payload_probe_basis", "g84_probe_basis"),
    ("g84_flat_moments", "84_local_rho_inertness_test__candidate_flat_probe_moment_test", "g84_flat_moments"),
    ("g84_weighted_moments", "84_local_rho_inertness_test__candidate_weighted_probe_moment_test", "g84_weighted_moments"),
    ("g84_tradeoff", "84_local_rho_inertness_test__candidate_skew_inertness_tradeoff_test", "g84_tradeoff"),
    ("g84_quadratic_obstruction", "84_local_rho_inertness_test__candidate_quadratic_payload_obstruction", "g84_quadratic_obstruction"),
    ("g84_route_classifier", "84_local_rho_inertness_test__candidate_local_inertness_route_classifier", "g84_route_classifier"),
]
MARKER_ID = "g84_summary"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Group 84 Status Summary")
    print("Question: Does the Group 83 skewed local rho remain inert to low-order payload probes?")
    print("Group 84 stable result:")
    print("  low-order payload probe basis defined")
    print("  global flat source moment M0=0 retained")
    print("  dipole moment M1 nonzero after Group 83 skew")
    print("  quadratic moment M2 nonzero and independent of c")
    print("  weighted total moment W0=0 retained")
    print("  weighted local moments W1/W2 nonzero")
    print("  weighted neutrality and dipole inertness require incompatible c unless ell=0")
    print("  linear skew cannot kill quadratic payload moment")
    print("  local inertness obstructed in finite-mode test")
    print("  rho exactness remains globally useful but locally payload-dangerous")
    print("  parent divergence identity remains unproven")
    print("  recombination remains blocked")

    with out.governance_assessments():
        out.line("finite-mode test", StatusMark.PASS, "low-order local inertness test completed")
        out.line("global neutrality", StatusMark.PASS, "M0 and W0 neutrality retained")
        out.line("dipole obstruction", StatusMark.WARN, "M1 nonzero")
        out.line("quadratic obstruction", StatusMark.WARN, "M2 nonzero and c-independent")
        out.line("local inertness", StatusMark.WARN, "obstructed in finite-mode test")
        out.line("rho exactness", StatusMark.INFO, "globally useful but not locally inert")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "recombination remains blocked")
    with out.counterexamples():
        out.line("global neutrality as payload inertness", StatusMark.FAIL, "total charge neutrality cannot be spent as local inertness")
        out.line("weighted neutrality as payload inertness", StatusMark.FAIL, "weighted total neutrality cannot be spent as local inertness")
        out.line("linear skew solves all", StatusMark.FAIL, "linear skew cannot kill quadratic payload")
        out.line("finite test as full theorem", StatusMark.FAIL, "finite-mode result is not full physical payload theorem")
        out.line("parent equation", StatusMark.FAIL, "parent construction remains forbidden")
    with out.unresolved_obligations():
        out.line("shape family", StatusMark.OBLIGATION, "test richer shape family for simultaneous weighted neutrality and payload suppression")
        out.line("projection/inertness", StatusMark.OBLIGATION, "consider legitimate payload projection or inertness mechanism")
        out.line("covariant lift", StatusMark.OBLIGATION, "interpret finite-mode payload obstruction covariantly")

    print("\nRecommended next routes:")
    print("  85_shape_family_payload_suppression_test")
    print("  85_payload_projection_operator_necessity")
    print("  85_covariant_exactness_lift")
    print("  85_parent_blocker_refresh")

    record_marker(ns, MARKER_ID, "Group 84 summary; local inertness finite-mode obstruction")
    record_claim(ns, MARKER_ID, "g84_summary_c1", GovernanceStatus.POLICY_RULE, "Group 84 finds local rho inertness obstructed in the low-order finite-mode test.")
    record_claim(ns, MARKER_ID, "g84_summary_c2", GovernanceStatus.POLICY_RULE, "Rho exactness remains globally useful but locally payload-dangerous in the tested class.")
    record_obligation(ns, "g84_summary_o1", "Test richer shape family or legitimate projection/inertness route.")
    record_obligation(ns, "g84_summary_o2", "Parent divergence identity remains unproven.")
    ns.write_run_metadata()

if __name__ == "__main__":
    main()
