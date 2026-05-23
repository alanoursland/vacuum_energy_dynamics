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
    ("g76_exact_pair", "76_covariant_lift_identity_construction__candidate_exact_pair_scaffold", "g76_exact_pair"),
    ("g76_remainder", "76_covariant_lift_identity_construction__candidate_remainder_obstruction_test", "g76_remainder"),
    ("g76_gauge_exact", "76_covariant_lift_identity_construction__candidate_gauge_exact_remainder_test", "g76_gauge_exact"),
    ("g76_sieve", "76_covariant_lift_identity_construction__candidate_identity_vs_repair_sieve", "g76_sieve"),
]
MARKER_ID = "g76_route_classifier"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    classifications = [
        ("EXACT_PAIR_IDENTITY_DERIVED", "not established", "exact-pair scaffold shown but K/sign origin not derived"),
        ("REMAINDER_OBSTRUCTION_FOUND", "stable", "honest shared route exposes rho"),
        ("GAUGE_EXACT_ROUTE_RETAINED", "conditional theorem target", "requires exactness and rho_phys=0 theorem"),
        ("SHARED_IDENTITY_NOT_ESTABLISHED", "stable", "no script derives full shared lift identity"),
        ("REPAIR_ROUTES_REJECTED", "stable", "free sign, dropped rho, repair current rejected"),
        ("D_LAYER_REMAINS_SEPARATE", "stable", "Group 76 does not solve D_layer"),
        ("PARENT_DIVERGENCE_UNPROVEN", "stable", "parent identity remains blocked"),
        ("RECOMBINATION_BLOCKED", "stable", "no recombination license"),
    ]

    header("Candidate Lift Identity Route Classifier")
    print("Final lift-identity route classification from Group 76 tests:")
    for name, status, reason in classifications:
        print(f"  {name}: {status}; {reason}")
    print()
    print("Reason:")
    print("  Exact-pair cancellation can be represented as scaffold.")
    print("  Honest shared identity leaves rho unless a theorem removes it.")
    print("  Gauge-exact route is retained only if physical remainder vanishes.")
    print("  Repair-style removal is rejected.")

    with out.governance_assessments():
        out.line("exact pair", StatusMark.INFO, "compatibility scaffold only")
        out.line("rho obstruction", StatusMark.OBLIGATION, "rho remains theorem burden")
        out.line("gauge-exact route", StatusMark.INFO, "conditional theorem target")
        out.line("shared identity", StatusMark.OBLIGATION, "shared lift identity not established")
        out.line("repair rejection", StatusMark.PASS, "repair routes rejected")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "parent recombination remains blocked")
    with out.counterexamples():
        out.line("free sign", StatusMark.FAIL, "opposite sign by choice is repair paint")
        out.line("dropped rho", StatusMark.FAIL, "rho cannot be dropped")
        out.line("parent jump", StatusMark.FAIL, "parent equation remains forbidden")
    with out.unresolved_obligations():
        out.line("rho theorem", StatusMark.OBLIGATION, "derive rho=0 or gauge-exact/inert status")
        out.line("identity origin", StatusMark.OBLIGATION, "derive common K and sign relation")

    record_marker(ns, MARKER_ID, "lift identity route classifier; no parent equation")
    record_claim(ns, MARKER_ID, "g76_class_c1", GovernanceStatus.POLICY_RULE, "Group 76 does not establish shared lift identity; rho obstruction remains.")
    record_claim(ns, MARKER_ID, "g76_class_c2", GovernanceStatus.REJECTED_ROUTE, "Free sign, dropped rho, repair current, and parent jump are rejected.")
    record_obligation(ns, "g76_class_o1", "Audit rho obstruction or derive gauge-exact remainder theorem.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_group_76_status_summary.py")

if __name__ == "__main__":
    main()
