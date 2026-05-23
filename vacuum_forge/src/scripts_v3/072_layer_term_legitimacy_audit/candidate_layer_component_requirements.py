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
]
MARKER_ID = "g72_requirements"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    D_jump, D_layer, D_tail, L_bulk, L_gauge = sp.symbols("D_jump D_layer D_tail L_bulk L_gauge")
    B = sp.simplify(D_jump + D_layer + D_tail)
    L_boundary_ideal = sp.simplify(-B)
    residual_ideal = sp.simplify(B + L_boundary_ideal + L_bulk + L_gauge)

    header("Candidate Layer Component Requirements")
    print(f"B = {B}")
    print(f"ideal L_boundary = {L_boundary_ideal}")
    print(f"ideal residual after boundary anti-match = {residual_ideal}")
    print()
    print("Legal D_layer criteria:")
    criteria = [
        "boundary-generated before coefficient choice",
        "local to boundary/layer region",
        "not supplied by quarantined diagnostic transition response",
        "not ordinary-source carrying",
        "not trace carrying",
        "not mass response",
        "not repair current",
        "not active O by label",
        "compatible with common boundary object",
    ]
    for item in criteria:
        print(f"  - {item}")

    with out.derived_results():
        out.line("boundary sum", StatusMark.PASS, f"B={B}")
        out.line("ideal anti-match residual", StatusMark.PASS, str(residual_ideal))
    with out.governance_assessments():
        out.line("requirement", StatusMark.INFO, "D_layer must be boundary-generated, not selected or imported")
        out.line("bulk/gauge", StatusMark.OBLIGATION, "ideal boundary anti-match still leaves lift-cleanliness obligations")
    with out.counterexamples():
        out.line("diagnostic import", StatusMark.FAIL, "diagnostic transition material cannot be D_layer")
        out.line("repair current", StatusMark.FAIL, "after-the-fact cancellation is not layer legitimacy")
        out.line("source/trace payload", StatusMark.FAIL, "D_layer cannot carry ordinary source or trace payload")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=residual_ideal,
        method="state ideal layer-inclusive boundary anti-match requirements",
        status=Status.DERIVED,
        record_kind=RecordKind.COMPATIBILITY_EXAMPLE,
        result_type="layer_component_requirements",
        scope="requirements; not D_layer theorem",
    )
    record_claim(ns, MARKER_ID, "g72_req_c1", GovernanceStatus.POLICY_RULE, "A legitimate D_layer must be boundary-generated and role-pure.")
    record_claim(ns, MARKER_ID, "g72_req_c2", GovernanceStatus.REJECTED_ROUTE, "Source/trace/repair/diagnostic payloads are rejected as layer legitimacy.")
    record_obligation(ns, "g72_req_o1", "Derive D_layer from boundary/layer geometry or keep unresolved.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_diagnostic_transition_exclusion.py")

if __name__ == "__main__":
    main()
