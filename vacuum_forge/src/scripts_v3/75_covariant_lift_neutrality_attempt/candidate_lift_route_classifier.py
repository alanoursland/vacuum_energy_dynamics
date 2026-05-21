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
    ("g75_bulk", "75_covariant_lift_neutrality_attempt__candidate_bulk_neutrality_test", "g75_bulk"),
    ("g75_gauge", "75_covariant_lift_neutrality_attempt__candidate_gauge_neutrality_test", "g75_gauge"),
    ("g75_shared_identity", "75_covariant_lift_neutrality_attempt__candidate_shared_lift_identity_test", "g75_shared_identity"),
    ("g75_discriminator", "75_covariant_lift_neutrality_attempt__candidate_mutual_cancellation_discriminator", "g75_discriminator"),
]
MARKER_ID = "g75_route_classifier"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    classifications = [
        ("LIFT_NEUTRALITY_DERIVED", "not established", "no script derives independent L_bulk=L_gauge=0"),
        ("SHARED_LIFT_IDENTITY_DERIVED", "not established", "shared identity compatibility shown, origin not derived"),
        ("SHARED_LIFT_IDENTITY_RETAINED", "conditional theorem target", "K/sign/remainder origin could be pursued later"),
        ("LIFT_NEUTRALITY_NOT_ESTABLISHED", "stable", "lift cleanliness remains open"),
        ("REPAIR_CANCELLATION_REJECTED", "stable", "chosen mutual cancellation rejected"),
        ("D_LAYER_REMAINS_SEPARATE", "stable", "Group 75 does not solve D_layer"),
        ("PARENT_DIVERGENCE_UNPROVEN", "stable", "parent identity remains blocked"),
        ("RECOMBINATION_BLOCKED", "stable", "no recombination license"),
    ]
    header("Candidate Lift Route Classifier")
    print("Final lift route classification from Group 75 tests:")
    for name, status, reason in classifications:
        print(f"  {name}: {status}; {reason}")
    print("\nReason:")
    print("  Independent bulk/gauge neutrality can be represented but not derived.")
    print("  Shared lift cancellation can be represented but not derived.")
    print("  Repair-style cancellation is rejected.")
    print("  D_layer and parent divergence remain separate open blockers.")
    with out.governance_assessments():
        out.line("lift theorem", StatusMark.OBLIGATION, "independent lift neutrality not derived")
        out.line("shared identity", StatusMark.INFO, "retained only as theorem target")
        out.line("repair rejection", StatusMark.PASS, "chosen mutual cancellation rejected")
        out.line("D_layer separation", StatusMark.INFO, "D_layer remains separate")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "parent recombination remains blocked")
    with out.counterexamples():
        out.line("chosen cancellation", StatusMark.FAIL, "L_bulk=-L_gauge by choice is repair paint")
        out.line("drop terms", StatusMark.FAIL, "dropping lift residues is not theorem")
        out.line("parent jump", StatusMark.FAIL, "parent equation remains forbidden")
    with out.unresolved_obligations():
        out.line("bulk neutrality", StatusMark.OBLIGATION, "derive L_bulk=0 or lawful shared identity")
        out.line("gauge neutrality", StatusMark.OBLIGATION, "derive L_gauge=0 or lawful shared identity")
        out.line("shared identity origin", StatusMark.OBLIGATION, "derive K/sign/remainder if shared route continues")
    record_marker(ns, MARKER_ID, "lift route classifier; no parent equation")
    record_claim(ns, MARKER_ID, "g75_class_c1", GovernanceStatus.POLICY_RULE, "Lift neutrality is not established in Group 75.")
    record_claim(ns, MARKER_ID, "g75_class_c2", GovernanceStatus.REJECTED_ROUTE, "Repair-style mutual cancellation and dropped lift terms are rejected.")
    record_obligation(ns, "g75_class_o1", "Route-manage remaining lift obligations or attempt a concrete covariant lift identity.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_group_75_status_summary.py")
if __name__ == "__main__":
    main()
