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
    ("g71_summary", "071_common_boundary_generator_search__candidate_group_71_status_summary", "g71_summary"),
    ("g72_problem", "072_layer_term_legitimacy_audit__candidate_layer_legitimacy_problem", "g72_problem"),
    ("g72_requirements", "072_layer_term_legitimacy_audit__candidate_layer_component_requirements", "g72_requirements"),
    ("g72_diagnostic_exclusion", "072_layer_term_legitimacy_audit__candidate_diagnostic_transition_exclusion", "g72_diagnostic_exclusion"),
    ("g72_boundary_component", "072_layer_term_legitimacy_audit__candidate_layer_as_boundary_component_test", "g72_boundary_component"),
    ("g72_measure_support", "072_layer_term_legitimacy_audit__candidate_layer_measure_support_test", "g72_measure_support"),
    ("g72_source_trace_filter", "072_layer_term_legitimacy_audit__candidate_layer_source_trace_divergence_filter", "g72_source_trace_filter"),
    ("g72_route_classifier", "072_layer_term_legitimacy_audit__candidate_layer_legitimacy_route_classifier", "g72_route_classifier"),
]
MARKER_ID = "g72_summary"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Group 72 Status Summary")
    print("Question:")
    print("  Can D_layer be a legitimate boundary-generator component?")
    print()
    print("Group 72 stable result:")
    print("  legal D_layer criteria explicit")
    print("  diagnostic transition insertion rejected")
    print("  a_layer=-1 compatibility remains compatibility, not theorem")
    print("  endpoint/locality support checks remain diagnostic only")
    print("  source/trace/mass payload routes rejected")
    print("  D_layer legitimacy not established")
    print("  boundary-layer component route retained only as theorem target")
    print("  parent divergence identity remains unproven")
    print("  recombination remains blocked")

    with out.governance_assessments():
        out.line("criteria", StatusMark.PASS, "legal D_layer criteria stated")
        out.line("diagnostic exclusion", StatusMark.PASS, "old diagnostic transition response cannot supply D_layer")
        out.line("component compatibility", StatusMark.PASS, "a_layer=-1 compatibility derived")
        out.line("D_layer legitimacy", StatusMark.OBLIGATION, "not established")
        out.line("boundary component route", StatusMark.INFO, "retained only as theorem target")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "parent recombination remains blocked")
    with out.counterexamples():
        out.line("diagnostic layer", StatusMark.FAIL, "eta/eta^2/N_w/R1/R2 cannot be promoted to D_layer")
        out.line("source/trace layer", StatusMark.FAIL, "D_layer cannot carry ordinary source or trace payload")
        out.line("repair layer", StatusMark.FAIL, "after-the-fact cancellation cannot supply legitimacy")
        out.line("active O", StatusMark.FAIL, "active O by label remains forbidden")
        out.line("parent equation", StatusMark.FAIL, "parent construction remains forbidden")
    with out.unresolved_obligations():
        out.line("geometric layer component", StatusMark.OBLIGATION, "derive D_layer from boundary/layer geometry or split route")
        out.line("lift cleanliness", StatusMark.OBLIGATION, "L_bulk/L_gauge remain separate obligations from Group 71")

    print()
    print("Recommended next routes:")
    print("  if continuing layer route: 73_layer_generator_construction")
    print("  if route management is preferred: 73_boundary_lift_route_split_decision")
    print("  if lift terms become priority: 73_covariant_lift_neutrality_attempt")
    print("  active O only later: 73_active_O_necessity_or_rejection, if O-free routes fail cleanly")

    record_marker(ns, MARKER_ID, "Group 72 summary; no parent equation")
    record_claim(ns, MARKER_ID, "g72_summary_c1", GovernanceStatus.POLICY_RULE, "D_layer legality criteria are explicit, but legitimacy is not established.")
    record_claim(ns, MARKER_ID, "g72_summary_c2", GovernanceStatus.REJECTED_ROUTE, "Diagnostic transition reentry as D_layer is rejected.")
    record_obligation(ns, "g72_summary_o1", "Derive or split the geometric D_layer component route.")
    record_obligation(ns, "g72_summary_o2", "Parent divergence identity remains unproven.")
    ns.write_run_metadata()

if __name__ == "__main__":
    main()
