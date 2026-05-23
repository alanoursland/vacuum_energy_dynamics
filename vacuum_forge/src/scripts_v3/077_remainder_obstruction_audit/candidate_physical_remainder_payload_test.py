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
    ("g77_boundary_exact", "077_remainder_obstruction_audit__candidate_boundary_exactness_test", "g77_boundary_exact"),
]
MARKER_ID = "g77_payload"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    rho_phys, S_M, T_zeta, M_A, D_parent = sp.symbols("rho_phys S_M T_zeta M_A D_parent")
    i_src, i_trace, i_mass, i_div = sp.symbols("i_src i_trace i_mass i_div")
    source_payload = sp.simplify(rho_phys * S_M * i_src)
    trace_payload = sp.simplify(rho_phys * T_zeta * i_trace)
    mass_payload = sp.simplify(rho_phys * M_A * i_mass)
    divergence_payload = sp.simplify(rho_phys * D_parent * i_div)
    total_payload = sp.simplify(source_payload + trace_payload + mass_payload + divergence_payload)
    safe_payload = sp.simplify(total_payload.subs({i_src:0, i_trace:0, i_mass:0, i_div:0}))

    header("Candidate Physical Remainder Payload Test")
    print(f"source payload = {source_payload}")
    print(f"trace payload = {trace_payload}")
    print(f"mass payload = {mass_payload}")
    print(f"divergence payload = {divergence_payload}")
    print(f"total payload = {total_payload}")
    print(f"safe no-payload route = {safe_payload}")
    print()
    print("Interpretation:")
    print("  any physical rho payload blocks shared lift identity until proven absent or inert.")

    with out.derived_results():
        out.line("total payload", StatusMark.PASS, str(total_payload))
        out.line("safe no-payload route", StatusMark.PASS, str(safe_payload))
    with out.governance_assessments():
        out.line("payload filter", StatusMark.PASS, "source/trace/mass/divergence payloads identified")
        out.line("inertness", StatusMark.OBLIGATION, "no-payload or inertness theorem required")
    with out.counterexamples():
        out.line("source payload", StatusMark.FAIL, str(source_payload.subs(i_src, 1)))
        out.line("trace payload", StatusMark.FAIL, str(trace_payload.subs(i_trace, 1)))
        out.line("mass payload", StatusMark.FAIL, str(mass_payload.subs(i_mass, 1)))
        out.line("divergence payload", StatusMark.FAIL, str(divergence_payload.subs(i_div, 1)))

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=total_payload,
        method="factor physical rho into forbidden payload channels",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="physical_remainder_payload_test",
        scope="payload filter; not inertness theorem",
    )
    record_claim(ns, MARKER_ID, "g77_payload_c1", GovernanceStatus.POLICY_RULE, "Physical rho payload blocks shared identity unless absent or inert by theorem.")
    record_obligation(ns, "g77_payload_o1", "Derive no-payload/inertness theorem or retain physical obstruction.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_remainder_route_classifier.py")

if __name__ == "__main__":
    main()
