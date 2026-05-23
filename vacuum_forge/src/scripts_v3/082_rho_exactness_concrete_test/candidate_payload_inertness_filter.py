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
    ("g82_local_nonzero", "82_rho_exactness_concrete_test__candidate_local_remainder_nonzero_test", "g82_local_nonzero"),
    ("g82_skew_condition", "82_rho_exactness_concrete_test__candidate_skew_condition_for_weighted_neutrality", "g82_skew_condition"),
]
MARKER_ID = "g82_payload_filter"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    rho, S_M, T_zeta, M_A, D_parent = sp.symbols("rho S_M T_zeta M_A D_parent")
    i_src, i_trace, i_mass, i_div = sp.symbols("i_src i_trace i_mass i_div")
    payload = sp.factor(rho * (S_M*i_src + T_zeta*i_trace + M_A*i_mass + D_parent*i_div))
    safe_payload = sp.simplify(payload.subs({i_src:0, i_trace:0, i_mass:0, i_div:0}))
    source_on = sp.simplify(payload.subs({i_src:1, i_trace:0, i_mass:0, i_div:0}))
    trace_on = sp.simplify(payload.subs({i_src:0, i_trace:1, i_mass:0, i_div:0}))
    mass_on = sp.simplify(payload.subs({i_src:0, i_trace:0, i_mass:1, i_div:0}))
    div_on = sp.simplify(payload.subs({i_src:0, i_trace:0, i_mass:0, i_div:1}))

    header("Candidate Payload Inertness Filter")
    print(f"payload = {payload}")
    print(f"safe no-payload route = {safe_payload}")
    print(f"source payload if on = {source_on}")
    print(f"trace payload if on = {trace_on}")
    print(f"mass payload if on = {mass_on}")
    print(f"divergence payload if on = {div_on}")

    with out.derived_results():
        out.line("payload expression", StatusMark.PASS, str(payload))
        out.line("safe no-payload route", StatusMark.PASS, str(safe_payload))
    with out.governance_assessments():
        out.line("payload filter", StatusMark.PASS, "payload channels explicit")
        out.line("inertness burden", StatusMark.OBLIGATION, "local nonzero rho requires no-payload/inertness theorem")
    with out.counterexamples():
        out.line("source payload", StatusMark.FAIL, str(source_on))
        out.line("trace payload", StatusMark.FAIL, str(trace_on))
        out.line("mass payload", StatusMark.FAIL, str(mass_on))
        out.line("divergence payload", StatusMark.FAIL, str(div_on))

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[rho],
        output=payload,
        method="factor local rho into source/trace/mass/divergence payload channels",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="rho_payload_filter",
        scope="payload inertness filter; not inertness theorem",
    )
    record_claim(ns, MARKER_ID, "g82_payload_c1", GovernanceStatus.POLICY_RULE, "Local nonzero rho requires no-payload/inertness theorem before physical harmlessness is claimed.")
    record_obligation(ns, "g82_payload_o1", "Derive payload inertness if rho exactness route continues.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_rho_exactness_route_classifier.py")

if __name__ == "__main__":
    main()
