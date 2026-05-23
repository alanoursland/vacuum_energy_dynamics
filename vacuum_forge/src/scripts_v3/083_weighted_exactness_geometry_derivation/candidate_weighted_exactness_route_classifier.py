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
    ("g83_measure_gradient", "83_weighted_exactness_geometry_derivation__candidate_measure_gradient_identity", "g83_measure_gradient"),
    ("g83_parity", "83_weighted_exactness_geometry_derivation__candidate_flux_parity_decomposition", "g83_parity"),
    ("g83_skew_derivation", "83_weighted_exactness_geometry_derivation__candidate_geometric_skew_derivation", "g83_skew_derivation"),
    ("g83_uniqueness_scaling", "83_weighted_exactness_geometry_derivation__candidate_uniqueness_and_scaling_test", "g83_uniqueness_scaling"),
    ("g83_repair_discriminator", "83_weighted_exactness_geometry_derivation__candidate_repair_discriminator", "g83_repair_discriminator"),
]
MARKER_ID = "g83_route_classifier"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    classifications = [
        ("MEASURE_GRADIENT_ORTHOGONALITY_DERIVED", "stable", "weighted charge reduced to mu' flux pairing"),
        ("FLUX_PARITY_DECOMPOSITION_DERIVED", "stable", "surviving terms isolate skew moment ratio"),
        ("WEIGHTED_SKEW_DERIVED_IN_REDUCED_CLASS", "stable", "c=3ell/(2R) follows from moment ratio"),
        ("UNIQUE_LINEAR_SKEW", "stable", "unique within linear-skew compact-support family"),
        ("THIN_LIMIT_CONSISTENT", "stable", "c scales as ell/R and vanishes as ell/R->0"),
        ("REPAIR_CONCERN_REDUCED_NOT_ELIMINATED", "stable", "not repair inside model; full-theory assumptions open"),
        ("REDUCED_CLASS_ONLY", "stable", "not full covariant theorem"),
        ("LOCAL_RHO_NONZERO_REMAINS", "stable", "from Group 82"),
        ("PAYLOAD_INERTNESS_OPEN", "stable", "payload theorem still required"),
        ("PARENT_DIVERGENCE_UNPROVEN", "stable", "parent identity remains blocked"),
        ("RECOMBINATION_BLOCKED", "stable", "no recombination license"),
    ]

    header("Candidate Weighted Exactness Route Classifier")
    for name, status, reason in classifications:
        print(f"{name}: {status}; {reason}")

    with out.governance_assessments():
        out.line("measure-gradient identity", StatusMark.PASS, "derived")
        out.line("weighted skew", StatusMark.PASS, "derived in reduced class")
        out.line("uniqueness", StatusMark.PASS, "unique in linear family")
        out.line("repair concern", StatusMark.INFO, "reduced inside model but not fully eliminated")
        out.line("reduced scope", StatusMark.WARN, "full covariant lift remains open")
        out.line("local rho", StatusMark.OBLIGATION, "local rho nonzero remains")
        out.line("payload", StatusMark.OBLIGATION, "payload inertness remains open")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "recombination remains blocked")
    with out.counterexamples():
        out.line("full theorem overclaim", StatusMark.FAIL, "reduced-class skew derivation is not full covariant closure")
        out.line("local overclaim", StatusMark.FAIL, "weighted neutrality is not local rho=0")
        out.line("payload ignored", StatusMark.FAIL, "payload channels remain")
        out.line("parent jump", StatusMark.FAIL, "parent equation remains forbidden")
    with out.unresolved_obligations():
        out.line("covariant lift", StatusMark.OBLIGATION, "derive or justify f,w,mu in covariant setting")
        out.line("local inertness", StatusMark.OBLIGATION, "test local rho inertness/no-payload")

    record_marker(ns, MARKER_ID, "weighted exactness route classifier")
    record_claim(ns, MARKER_ID, "g83_class_c1", GovernanceStatus.POLICY_RULE, "Weighted skew c=3ell/(2R) is derived in the reduced weighted-exactness class.")
    record_claim(ns, MARKER_ID, "g83_class_c2", GovernanceStatus.POLICY_RULE, "The derivation is reduced-class only; covariant, local, and payload burdens remain.")
    record_obligation(ns, "g83_class_o1", "Test local rho inertness or covariant lift next.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_group_83_status_summary.py")

if __name__ == "__main__":
    main()
