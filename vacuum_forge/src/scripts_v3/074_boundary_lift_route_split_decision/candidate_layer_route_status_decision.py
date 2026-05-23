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
    ("g73_summary", "073_layer_generator_construction__candidate_group_73_status_summary", "g73_summary"),
    ("g74_route_ledger", "074_boundary_lift_route_split_decision__candidate_route_status_ledger", "g74_route_ledger"),
]
MARKER_ID = "g74_layer_decision"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    D_layer_geo, D_diag, D_repair, x_geo, x_diag, x_repair = sp.symbols("D_layer_geo D_diag D_repair x_geo x_diag x_repair")
    candidate = sp.simplify(D_layer_geo*x_geo + D_diag*x_diag + D_repair*x_repair)
    legal_form = sp.simplify(candidate.subs({x_diag: 0, x_repair: 0}))

    header("Candidate Layer Route Status Decision")
    print(f"D_layer candidate = {candidate}")
    print(f"legal form after diagnostic/repair exclusion = {legal_form}")
    print()
    print("Layer route decision:")
    print("  not legitimate yet")
    print("  not rejected as impossible")
    print("  retained only as geometric theorem target")
    print("  diagnostic transition remains excluded")

    with out.derived_results():
        out.line("candidate decomposition", StatusMark.PASS, str(candidate))
        out.line("legal residual route", StatusMark.PASS, str(legal_form))
    with out.governance_assessments():
        out.line("D_layer status", StatusMark.OBLIGATION, "legitimacy not established")
        out.line("retention", StatusMark.INFO, "geometric D_layer route retained only as theorem target")
        out.line("diagnostic exclusion", StatusMark.PASS, "old transition diagnostics remain excluded")
    with out.counterexamples():
        out.line("diagnostic route", StatusMark.FAIL, "D_diag cannot supply D_layer")
        out.line("repair route", StatusMark.FAIL, "D_repair cannot supply D_layer")
        out.line("hard rejection", StatusMark.FAIL, "no proof that geometric D_layer is impossible")
    with out.unresolved_obligations():
        out.line("geometric layer theorem", StatusMark.OBLIGATION, "derive or reject D_layer_geo from concrete geometry")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=legal_form,
        method="exclude diagnostic and repair payloads from D_layer route",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="layer_route_status_decision",
        scope="route status; not D_layer theorem",
    )
    record_claim(ns, MARKER_ID, "g74_layer_c1", GovernanceStatus.POLICY_RULE, "D_layer remains unresolved and retained only as geometric theorem target.")
    record_claim(ns, MARKER_ID, "g74_layer_c2", GovernanceStatus.REJECTED_ROUTE, "Diagnostic and repair layer routes remain rejected.")
    record_obligation(ns, "g74_layer_o1", "Derive or route-manage geometric D_layer origin.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_lift_cleanliness_route_status.py")

if __name__ == "__main__":
    main()
