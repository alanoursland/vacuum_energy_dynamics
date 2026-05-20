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
    ("g72_measure_support", "72_layer_term_legitimacy_audit__candidate_layer_measure_support_test", "g72_measure_support"),
]
MARKER_ID = "g72_source_trace_filter"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    S_M, T_zeta = sp.symbols("S_M T_zeta")
    i_A, i_layer_src = sp.symbols("i_A i_layer_src")
    i_B, i_res, i_layer_trace = sp.symbols("i_B i_res i_layer_trace")
    source_residual = sp.simplify(S_M * (i_A + i_layer_src - 1))
    trace_residual = sp.simplify(T_zeta * (i_B + i_res + i_layer_trace - 1))
    safe_source = sp.simplify(source_residual.subs({i_A: 1, i_layer_src: 0}))
    layer_source = sp.simplify(source_residual.subs({i_A: 1, i_layer_src: 1}))
    safe_trace = sp.simplify(trace_residual.subs({i_B: 1, i_res: 0, i_layer_trace: 0}))
    layer_trace = sp.simplify(trace_residual.subs({i_B: 1, i_res: 0, i_layer_trace: 1}))
    residual_reentry = sp.simplify(trace_residual.subs({i_B: 1, i_res: 1, i_layer_trace: 0}))

    header("Candidate Layer Source / Trace / Divergence Filter")
    print(f"source residual = {source_residual}")
    print(f"safe source route = {safe_source}")
    print(f"layer-source route residual = {layer_source}")
    print(f"trace residual = {trace_residual}")
    print(f"safe trace route = {safe_trace}")
    print(f"layer-trace route residual = {layer_trace}")
    print(f"residual reentry route residual = {residual_reentry}")

    with out.derived_results():
        out.line("source residual", StatusMark.PASS, str(source_residual))
        out.line("trace residual", StatusMark.PASS, str(trace_residual))
    with out.governance_assessments():
        out.line("safe source", StatusMark.PASS, "D_layer must not carry ordinary source load")
        out.line("safe trace", StatusMark.PASS, "D_layer must not carry trace payload")
        out.line("divergence role", StatusMark.INFO, "D_layer may only be boundary-divergence component if geometrically derived")
    with out.counterexamples():
        out.line("layer source", StatusMark.FAIL, f"residual={layer_source}")
        out.line("layer trace", StatusMark.FAIL, f"residual={layer_trace}")
        out.line("residual reentry", StatusMark.FAIL, f"residual={residual_reentry}")
        out.line("repair divergence", StatusMark.FAIL, "D_layer cannot be chosen to cancel parent divergence after the fact")
    with out.unresolved_obligations():
        out.line("boundary-divergence role", StatusMark.OBLIGATION, "derive D_layer as boundary-divergence component without source/trace payload")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=sp.Tuple(source_residual, trace_residual),
        method="source/trace incidence filter for candidate D_layer",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="layer_source_trace_filter",
        scope="incidence filter; not source/trace theorem",
    )
    record_claim(ns, MARKER_ID, "g72_filter_c1", GovernanceStatus.REJECTED_ROUTE, "D_layer carrying ordinary source, trace, or residual reentry is rejected.")
    record_claim(ns, MARKER_ID, "g72_filter_c2", GovernanceStatus.POLICY_RULE, "Only a role-pure boundary-divergence component remains as theorem target.")
    record_obligation(ns, "g72_filter_o1", "Derive role-pure boundary-divergence D_layer if retained.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_layer_legitimacy_route_classifier.py")

if __name__ == "__main__":
    main()
