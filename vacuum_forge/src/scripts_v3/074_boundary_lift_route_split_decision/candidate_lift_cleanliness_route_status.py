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
        method="route/governance marker; no physical derivation",
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
    ("g71_bulk_gauge", "071_common_boundary_generator_search__candidate_bulk_gauge_leakage_test", "g71_bulk_gauge"),
    ("g74_layer_decision", "074_boundary_lift_route_split_decision__candidate_layer_route_status_decision", "g74_layer_decision"),
]
MARKER_ID = "g74_lift_cleanliness"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    L_bulk, L_gauge, C_shared = sp.symbols("L_bulk L_gauge C_shared")
    residual = sp.simplify(L_bulk + L_gauge)
    independent_neutral = residual.subs({L_bulk: 0, L_gauge: 0})
    mutual_cancel = residual.subs({L_bulk: C_shared, L_gauge: -C_shared})

    header("Candidate Lift Cleanliness Route Status")
    print(f"post-boundary residual = {residual}")
    print(f"independent neutrality residual = {independent_neutral}")
    print(f"mutual cancellation residual = {mutual_cancel}")
    print("Interpretation:")
    print("  L_bulk=0 and L_gauge=0 remain separate theorem targets unless a lawful shared lift identity is derived.")

    with out.derived_results():
        out.line("lift residual", StatusMark.PASS, str(residual))
        out.line("independent neutral case", StatusMark.PASS, str(independent_neutral))
        out.line("formal mutual cancel", StatusMark.PASS, str(mutual_cancel))
    with out.governance_assessments():
        out.line("lift route", StatusMark.OBLIGATION, "lift cleanliness not solved")
        out.line("shared identity", StatusMark.OBLIGATION, "mutual cancellation requires lawful shared lift identity")
        out.line("split", StatusMark.INFO, "lift cleanliness should split from D_layer legitimacy")
    with out.counterexamples():
        out.line("drop lift terms", StatusMark.FAIL, "dropping L_bulk/L_gauge by prose forbidden")
        out.line("repair cancellation", StatusMark.FAIL, "choosing L_bulk=-L_gauge is repair-like unless derived")
    with out.unresolved_obligations():
        out.line("bulk neutrality", StatusMark.OBLIGATION, "derive L_bulk=0 or lawful shared identity")
        out.line("gauge neutrality", StatusMark.OBLIGATION, "derive L_gauge=0 or lawful shared identity")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=residual,
        method="classify lift-cleanliness route status",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="lift_cleanliness_route_status",
        scope="route status; not lift theorem",
    )
    record_claim(ns, MARKER_ID, "g74_lift_c1", GovernanceStatus.POLICY_RULE, "L_bulk/L_gauge neutrality remains a separate theorem target.")
    record_claim(ns, MARKER_ID, "g74_lift_c2", GovernanceStatus.REJECTED_ROUTE, "Dropped lift terms and repair-like mutual cancellation are rejected.")
    record_obligation(ns, "g74_lift_o1", "Attempt covariant lift neutrality or lawful shared lift identity.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_boundary_match_route_decision_matrix.py")

if __name__ == "__main__":
    main()
