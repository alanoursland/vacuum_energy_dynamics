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
    ("g82_summary", "82_rho_exactness_concrete_test__candidate_group_82_status_summary", "g82_summary"),
    ("g83_problem", "83_weighted_exactness_geometry_derivation__candidate_weighted_skew_problem", "g83_problem"),
    ("g83_measure_gradient", "83_weighted_exactness_geometry_derivation__candidate_measure_gradient_identity", "g83_measure_gradient"),
    ("g83_parity", "83_weighted_exactness_geometry_derivation__candidate_flux_parity_decomposition", "g83_parity"),
    ("g83_skew_derivation", "83_weighted_exactness_geometry_derivation__candidate_geometric_skew_derivation", "g83_skew_derivation"),
    ("g83_uniqueness_scaling", "83_weighted_exactness_geometry_derivation__candidate_uniqueness_and_scaling_test", "g83_uniqueness_scaling"),
    ("g83_repair_discriminator", "83_weighted_exactness_geometry_derivation__candidate_repair_discriminator", "g83_repair_discriminator"),
    ("g83_route_classifier", "83_weighted_exactness_geometry_derivation__candidate_weighted_exactness_route_classifier", "g83_route_classifier"),
]
MARKER_ID = "g83_summary"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Group 83 Status Summary")
    print("Question: Did geometry pay for the Group 82 weighted skew?")
    print("Group 83 stable result:")
    print("  measure-gradient orthogonality derived")
    print("  flux parity decomposition derived")
    print("  c = 3ell/(2R) derived from moment ratio in reduced weighted-exactness class")
    print("  skew unique within linear-skew compact-support family")
    print("  skew scales as ell/R and vanishes in thin-layer limit")
    print("  repair concern reduced inside the reduced model")
    print("  full covariant theorem remains open")
    print("  local rho nonzero remains")
    print("  payload inertness remains open")
    print("  parent divergence identity remains unproven")
    print("  recombination remains blocked")

    with out.governance_assessments():
        out.line("measure-gradient identity", StatusMark.PASS, "weighted exactness interpreted geometrically")
        out.line("skew derivation", StatusMark.PASS, "c=3ell/(2R) derived in reduced class")
        out.line("uniqueness/scaling", StatusMark.PASS, "unique linear skew with geometric scaling")
        out.line("repair status", StatusMark.INFO, "not repair inside model; full assumptions remain")
        out.line("covariant status", StatusMark.OBLIGATION, "full covariant lift remains open")
        out.line("local rho", StatusMark.OBLIGATION, "local rho nonzero remains")
        out.line("payload", StatusMark.OBLIGATION, "payload inertness remains open")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "recombination remains blocked")
    with out.counterexamples():
        out.line("chosen skew", StatusMark.FAIL, "skew is repair if not tied to measure-gradient derivation")
        out.line("full closure", StatusMark.FAIL, "reduced derivation is not full covariant theorem")
        out.line("local closure", StatusMark.FAIL, "weighted neutrality is not local rho=0")
        out.line("parent equation", StatusMark.FAIL, "parent construction remains forbidden")
    with out.unresolved_obligations():
        out.line("covariant lift", StatusMark.OBLIGATION, "derive reduced f,w,mu structure covariantly")
        out.line("local inertness", StatusMark.OBLIGATION, "prove or reject local rho inertness/no-payload")
        out.line("shape robustness", StatusMark.OBLIGATION, "test whether skew derivation survives other compact-support shapes")

    print("\nRecommended next routes:")
    print("  84_local_rho_inertness_test")
    print("  84_covariant_exactness_lift")
    print("  84_shape_family_robustness_test")
    print("  84_parent_blocker_refresh")

    record_marker(ns, MARKER_ID, "Group 83 summary; weighted skew derived in reduced class")
    record_claim(ns, MARKER_ID, "g83_summary_c1", GovernanceStatus.POLICY_RULE, "Group 83 derives the Group 82 weighted skew from measure-gradient orthogonality in the reduced class.")
    record_claim(ns, MARKER_ID, "g83_summary_c2", GovernanceStatus.POLICY_RULE, "Weighted exactness route is strengthened but remains reduced-class; local/payload/covariant burdens remain.")
    record_obligation(ns, "g83_summary_o1", "Test local rho inertness/no-payload or covariant lift next.")
    record_obligation(ns, "g83_summary_o2", "Parent divergence identity remains unproven.")
    ns.write_run_metadata()

if __name__ == "__main__":
    main()
