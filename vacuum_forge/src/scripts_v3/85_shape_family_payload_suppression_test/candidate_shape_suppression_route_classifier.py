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
    ("g85_moment_solver", "85_shape_family_payload_suppression_test__candidate_moment_constraint_solver", "g85_moment_solver"),
    ("g85_profile_validation", "85_shape_family_payload_suppression_test__candidate_suppressed_profile_validation", "g85_profile_validation"),
    ("g85_weighted_extension", "85_shape_family_payload_suppression_test__candidate_weighted_payload_extension", "g85_weighted_extension"),
    ("g85_admissibility", "85_shape_family_payload_suppression_test__candidate_shape_admissibility_and_repair_discriminator", "g85_admissibility"),
]
MARKER_ID = "g85_route_classifier"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    classifications = [
        ("EVEN_QUARTIC_SUPPRESSION_PROFILE_FOUND", "stable", "P=1-12y^2+51y^4"),
        ("LOW_ORDER_FLAT_PAYLOAD_SUPPRESSED_THROUGH_M5", "stable", "M0..M5 vanish"),
        ("LOW_ORDER_WEIGHTED_PAYLOAD_SUPPRESSED_THROUGH_W3", "stable", "W0..W3 vanish under quadratic measure"),
        ("NEXT_MOMENT_OBSTRUCTION_M6_W4", "stable", "M6 and W4 nonzero"),
        ("LOCAL_RHO_NONZERO_REMAINS", "stable", "rho(0) nonzero"),
        ("LINEAR_SKEW_OBSTRUCTION_NOT_UNIVERSAL", "stable", "richer shape overcomes Group 84 low-order obstruction"),
        ("SHAPE_ORIGIN_OPEN", "stable", "profile derived from moments, not geometry"),
        ("FULL_LOCAL_INERTNESS_NOT_PROVEN", "stable", "finite-mode suppression only"),
        ("PARENT_DIVERGENCE_UNPROVEN", "stable", "parent identity remains blocked"),
        ("RECOMBINATION_BLOCKED", "stable", "no recombination license"),
    ]

    header("Candidate Shape Suppression Route Classifier")
    for name, status, reason in classifications:
        print(f"{name}: {status}; {reason}")

    with out.governance_assessments():
        out.line("suppression profile", StatusMark.PASS, "even quartic profile found")
        out.line("flat suppression", StatusMark.PASS, "M0..M5 vanish")
        out.line("weighted suppression", StatusMark.PASS, "W0..W3 vanish")
        out.line("higher obstruction", StatusMark.WARN, "M6/W4 remain")
        out.line("shape origin", StatusMark.OBLIGATION, "geometric origin remains open")
        out.line("full inertness", StatusMark.DEFER, "not proven")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "recombination remains blocked")
    with out.counterexamples():
        out.line("linear obstruction universal", StatusMark.FAIL, "richer shape suppresses low-order payload")
        out.line("finite as all-order", StatusMark.FAIL, "M6/W4 remain nonzero")
        out.line("moment profile as geometry", StatusMark.FAIL, "shape origin not derived")
        out.line("parent equation", StatusMark.FAIL, "parent construction remains forbidden")
    with out.unresolved_obligations():
        out.line("shape origin", StatusMark.OBLIGATION, "derive P=1-12y^2+51y^4 from geometry or variational principle")
        out.line("moment hierarchy", StatusMark.OBLIGATION, "test whether higher-order moments can be hierarchically suppressed")
        out.line("covariant lift", StatusMark.OBLIGATION, "lift finite-mode suppression covariantly")

    record_marker(ns, MARKER_ID, "shape suppression route classifier")
    record_claim(ns, MARKER_ID, "g85_class_c1", GovernanceStatus.POLICY_RULE, "Even quartic compact-support shape suppresses low-order flat and weighted payload moments in the reduced class.")
    record_claim(ns, MARKER_ID, "g85_class_c2", GovernanceStatus.POLICY_RULE, "Suppression is finite-mode only; shape origin, higher moments, and covariant lift remain open.")
    record_obligation(ns, "g85_class_o1", "Derive shape origin or test moment hierarchy next.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_group_85_status_summary.py")

if __name__ == "__main__":
    main()
