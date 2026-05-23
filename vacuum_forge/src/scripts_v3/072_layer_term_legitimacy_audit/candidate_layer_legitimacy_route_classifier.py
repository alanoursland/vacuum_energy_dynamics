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
    ("g72_diagnostic_exclusion", "72_layer_term_legitimacy_audit__candidate_diagnostic_transition_exclusion", "g72_diagnostic_exclusion"),
    ("g72_boundary_component", "72_layer_term_legitimacy_audit__candidate_layer_as_boundary_component_test", "g72_boundary_component"),
    ("g72_measure_support", "72_layer_term_legitimacy_audit__candidate_layer_measure_support_test", "g72_measure_support"),
    ("g72_source_trace_filter", "72_layer_term_legitimacy_audit__candidate_layer_source_trace_divergence_filter", "g72_source_trace_filter"),
]
MARKER_ID = "g72_route_classifier"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    classifications = [
        ("DIAGNOSTIC_TRANSITION_INSERTION_REJECTED", "stable", "old transition diagnostics cannot supply D_layer"),
        ("BOUNDARY_LAYER_COMPONENT_RETAINED_AS_THEOREM_TARGET", "conditional", "geometric D_layer remains possible if derived"),
        ("D_LAYER_LEGITIMACY_NOT_ESTABLISHED", "stable", "no script derives boundary-layer component origin"),
        ("SOURCE_TRACE_PAYLOAD_REJECTED", "stable", "D_layer cannot carry ordinary source or trace payload"),
        ("SUPPORT_CRITERIA_DIAGNOSTIC_ONLY", "stable", "endpoint/locality checks constrain but do not prove legitimacy"),
        ("PARENT_DIVERGENCE_UNPROVEN", "stable", "layer audit does not close parent divergence"),
        ("RECOMBINATION_BLOCKED", "stable", "no recombination license"),
    ]

    header("Candidate Layer Legitimacy Route Classifier")
    print("Final route classification from Group 72 tests:")
    for name, status, reason in classifications:
        print(f"  {name}: {status}; {reason}")

    with out.governance_assessments():
        out.line("diagnostic exclusion", StatusMark.PASS, "diagnostic transition insertion rejected")
        out.line("boundary component route", StatusMark.INFO, "geometric layer component retained only as theorem target")
        out.line("D_layer legitimacy", StatusMark.OBLIGATION, "not established in this audit")
        out.line("support criteria", StatusMark.INFO, "diagnostic support checks are not physical legitimacy")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "parent recombination remains blocked")
    with out.counterexamples():
        out.line("diagnostic D_layer", StatusMark.FAIL, "old transition response cannot re-enter")
        out.line("source/trace D_layer", StatusMark.FAIL, "payload routes rejected")
        out.line("repair D_layer", StatusMark.FAIL, "after-the-fact cancellation is not legitimacy")
    with out.unresolved_obligations():
        out.line("geometric D_layer origin", StatusMark.OBLIGATION, "derive or reject a legitimate boundary-layer component")
        out.line("boundary-lift route split", StatusMark.OBLIGATION, "if D_layer remains unresolved, split theorem targets before parent work")

    record_marker(ns, MARKER_ID, "Group 72 classifier; no parent equation")
    record_claim(ns, MARKER_ID, "g72_class_c1", GovernanceStatus.REJECTED_ROUTE, "Diagnostic transition insertion as D_layer is rejected.")
    record_claim(ns, MARKER_ID, "g72_class_c2", GovernanceStatus.POLICY_RULE, "D_layer legitimacy is not established; geometric layer route remains theorem target only.")
    record_obligation(ns, "g72_class_o1", "Derive or reject a legitimate boundary-layer component in future work.")
    record_obligation(ns, "g72_class_o2", "Parent divergence identity remains unproven.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_group_72_status_summary.py")

if __name__ == "__main__":
    main()
