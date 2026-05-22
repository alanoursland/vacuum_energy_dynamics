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
    ("g81_summary", "81_concrete_geometry_input_handoff__candidate_group_81_status_summary", "g81_summary"),
    ("g82_problem", "82_rho_exactness_concrete_test__candidate_rho_exactness_problem", "g82_problem"),
    ("g82_requirements", "82_rho_exactness_concrete_test__candidate_exact_operator_requirements", "g82_requirements"),
    ("g82_compact_support", "82_rho_exactness_concrete_test__candidate_compact_support_exact_remainder", "g82_compact_support"),
    ("g82_local_nonzero", "82_rho_exactness_concrete_test__candidate_local_remainder_nonzero_test", "g82_local_nonzero"),
    ("g82_weighted", "82_rho_exactness_concrete_test__candidate_weighted_measure_neutrality_test", "g82_weighted"),
    ("g82_skew_condition", "82_rho_exactness_concrete_test__candidate_skew_condition_for_weighted_neutrality", "g82_skew_condition"),
    ("g82_payload_filter", "82_rho_exactness_concrete_test__candidate_payload_inertness_filter", "g82_payload_filter"),
    ("g82_route_classifier", "82_rho_exactness_concrete_test__candidate_rho_exactness_route_classifier", "g82_route_classifier"),
]
MARKER_ID = "g82_summary"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Group 82 Status Summary")
    print("Question: Does concrete exactness pay any of the rho debt?")
    print("Group 82 stable result:")
    print("  concrete exactness operator tested")
    print("  flat integrated neutrality derived in reduced compact-support class")
    print("  local rho remains nonzero")
    print("  weighted/geometric neutrality is not automatic")
    print("  skew condition for weighted neutrality exists as compatibility")
    print("  skew must be derived geometrically, not chosen")
    print("  payload inertness remains open")
    print("  rho exactness route strengthened but partial")
    print("  parent divergence identity remains unproven")
    print("  recombination remains blocked")

    with out.governance_assessments():
        out.line("concrete test", StatusMark.PASS, "real exactness candidate tested")
        out.line("flat neutrality", StatusMark.PASS, "flat integrated neutrality derived in reduced class")
        out.line("local rho", StatusMark.WARN, "local rho nonzero")
        out.line("weighted neutrality", StatusMark.WARN, "weighted neutrality not automatic")
        out.line("skew condition", StatusMark.INFO, "weighted neutrality condition found but not derived")
        out.line("payload inertness", StatusMark.OBLIGATION, "payload inertness remains open")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "recombination remains blocked")
    with out.counterexamples():
        out.line("flat as full", StatusMark.FAIL, "flat exact neutrality is not full covariant closure")
        out.line("flat as local zero", StatusMark.FAIL, "flat charge zero does not imply rho=0 locally")
        out.line("chosen skew", StatusMark.FAIL, "weighted skew cannot be chosen as repair")
        out.line("payload ignored", StatusMark.FAIL, "payload channels cannot be ignored")
        out.line("parent equation", StatusMark.FAIL, "parent construction remains forbidden")
    with out.unresolved_obligations():
        out.line("weighted geometry", StatusMark.OBLIGATION, "derive weighted skew/geometric neutrality")
        out.line("local inertness", StatusMark.OBLIGATION, "derive local rho inertness or no-payload status")
        out.line("covariant lift", StatusMark.OBLIGATION, "lift exactness remains reduced-class only")

    print("\nRecommended next routes:")
    print("  83_weighted_exactness_geometry_derivation")
    print("  83_local_rho_inertness_test")
    print("  83_covariant_exactness_lift")
    print("  83_parent_blocker_refresh")

    record_marker(ns, MARKER_ID, "Group 82 summary; concrete rho exactness partial result")
    record_claim(ns, MARKER_ID, "g82_summary_c1", GovernanceStatus.POLICY_RULE, "Concrete exactness derives flat integrated neutrality in a reduced compact-support class.")
    record_claim(ns, MARKER_ID, "g82_summary_c2", GovernanceStatus.POLICY_RULE, "Rho exactness remains partial because local, weighted, payload, and covariant burdens remain.")
    record_obligation(ns, "g82_summary_o1", "Derive weighted skew from geometry or test local inertness.")
    record_obligation(ns, "g82_summary_o2", "Parent divergence identity remains unproven.")
    ns.write_run_metadata()

if __name__ == "__main__":
    main()
