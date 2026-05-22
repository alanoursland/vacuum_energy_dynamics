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
    ("g82_compact_support", "82_rho_exactness_concrete_test__candidate_compact_support_exact_remainder", "g82_compact_support"),
    ("g82_local_nonzero", "82_rho_exactness_concrete_test__candidate_local_remainder_nonzero_test", "g82_local_nonzero"),
    ("g82_weighted", "82_rho_exactness_concrete_test__candidate_weighted_measure_neutrality_test", "g82_weighted"),
    ("g82_skew_condition", "82_rho_exactness_concrete_test__candidate_skew_condition_for_weighted_neutrality", "g82_skew_condition"),
    ("g82_payload_filter", "82_rho_exactness_concrete_test__candidate_payload_inertness_filter", "g82_payload_filter"),
]
MARKER_ID = "g82_route_classifier"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    classifications = [
        ("FLAT_EXACT_NEUTRALITY_DERIVED_IN_REDUCED_CLASS", "stable", "compact-support exact flux gives zero flat charge"),
        ("LOCAL_RHO_NOT_ZERO", "stable", "flat charge does not imply local vanishing"),
        ("WEIGHTED_NEUTRALITY_NOT_AUTOMATIC", "stable", "geometric measure can expose nonzero weighted charge"),
        ("WEIGHTED_SKEW_CONDITION_FOUND", "compatibility", "skew can restore weighted neutrality but must be derived"),
        ("PAYLOAD_INERTNESS_OPEN", "stable", "local rho payload channels must be proven absent/inert"),
        ("RHO_EXACTNESS_PARTIAL", "stable", "exactness route strengthened but not closed"),
        ("PARENT_DIVERGENCE_UNPROVEN", "stable", "parent identity remains blocked"),
        ("RECOMBINATION_BLOCKED", "stable", "no recombination license"),
    ]

    header("Candidate Rho Exactness Route Classifier")
    for name, status, reason in classifications:
        print(f"{name}: {status}; {reason}")

    with out.governance_assessments():
        out.line("flat exact neutrality", StatusMark.PASS, "derived in reduced class")
        out.line("local rho", StatusMark.WARN, "local nonzero obstruction remains")
        out.line("weighted neutrality", StatusMark.WARN, "not automatic")
        out.line("skew condition", StatusMark.INFO, "compatibility condition found")
        out.line("payload inertness", StatusMark.OBLIGATION, "payload inertness remains open")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "recombination remains blocked")
    with out.counterexamples():
        out.line("flat as local", StatusMark.FAIL, "flat exact neutrality cannot be used as local rho=0")
        out.line("chosen skew", StatusMark.FAIL, "skew must be derived, not chosen")
        out.line("payload ignored", StatusMark.FAIL, "local rho payload cannot be ignored")
        out.line("parent jump", StatusMark.FAIL, "parent equation remains forbidden")
    with out.unresolved_obligations():
        out.line("weighted geometry", StatusMark.OBLIGATION, "derive skew/weighted neutrality from geometry")
        out.line("local inertness", StatusMark.OBLIGATION, "derive local rho inertness/no-payload status")

    record_marker(ns, MARKER_ID, "rho exactness route classifier; no parent equation")
    record_claim(ns, MARKER_ID, "g82_class_c1", GovernanceStatus.POLICY_RULE, "Rho exactness is partially validated: flat reduced neutrality derived, but local/weighted/payload burdens remain.")
    record_obligation(ns, "g82_class_o1", "Derive weighted skew geometrically or test local inertness next.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_group_82_status_summary.py")

if __name__ == "__main__":
    main()
