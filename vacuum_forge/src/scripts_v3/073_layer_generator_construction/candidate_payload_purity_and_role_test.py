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
    print(); print("=" * 120); print(title); print("=" * 120)


def prepare_archive(dependencies):
    archive = ProjectArchive(ARCHIVE_ROOT); ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    for dep_id, upstream_script_id, upstream_derivation_id in dependencies:
        ns.declare_dependency(dependency_id=dep_id, upstream_script_id=upstream_script_id, upstream_derivation_id=upstream_derivation_id)
    return archive, ns, invalidated


def print_archive_status(ns, invalidated: bool) -> None:
    if invalidated: print("[INFO] Archive invalidated due to source change.")
    checks = ns.verify_dependencies()
    if not checks:
        print("[INFO] Archive dependencies: none declared."); return
    print("[INFO] Archive dependency check:")
    for check in checks: print(f"  - {check.dependency.dependency_id}: {check.status} ({check.message})")


def record_claim(ns, marker_id: str, claim_id: str, status: GovernanceStatus, statement: str) -> None:
    ns.record_claim(ClaimRecord(claim_id=claim_id, script_id=SCRIPT_ID, claim_kind=RecordKind.GOVERNANCE_CLAIM, tier=ClaimTier.CONSTRAINED, status=status, statement=statement, derivation_ids=[marker_id], obligation_ids=[]))


def record_obligation(ns, obligation_id: str, statement: str, status: ObligationStatus = ObligationStatus.OPEN) -> None:
    ns.record_obligation(ProofObligationRecord(obligation_id=obligation_id, script_id=SCRIPT_ID, title=obligation_id, status=status, required_by=[SCRIPT_ID], description=statement))


DEPENDENCIES = [
    ("g73_component_membership", "073_layer_generator_construction__candidate_component_membership_origin_test", "g73_component_membership"),
]
MARKER_ID = "g73_payload_purity"


def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES); print_archive_status(ns, invalidated)
    out = ScriptOutput()

    S_M, T_zeta, M_A, R_repair, O_active, D_diag = sp.symbols("S_M T_zeta M_A R_repair O_active D_diag")
    i_A, i_layer_src = sp.symbols("i_A i_layer_src")
    i_B, i_res, i_layer_trace = sp.symbols("i_B i_res i_layer_trace")
    i_layer_mass, i_repair, i_O, i_diag = sp.symbols("i_layer_mass i_repair i_O i_diag")

    source_residual = sp.simplify(S_M * (i_A + i_layer_src - 1))
    trace_residual = sp.simplify(T_zeta * (i_B + i_res + i_layer_trace - 1))
    mass_payload = sp.simplify(M_A * i_layer_mass)
    forbidden_payload = sp.simplify(R_repair*i_repair + O_active*i_O + D_diag*i_diag)
    safe_source = sp.simplify(source_residual.subs({i_A: 1, i_layer_src: 0}))
    layer_source = sp.simplify(source_residual.subs({i_A: 1, i_layer_src: 1}))
    safe_trace = sp.simplify(trace_residual.subs({i_B: 1, i_res: 0, i_layer_trace: 0}))
    layer_trace = sp.simplify(trace_residual.subs({i_B: 1, i_res: 0, i_layer_trace: 1}))

    header("Candidate Payload Purity and Role Test")
    print(f"source residual = {source_residual}")
    print(f"safe source route = {safe_source}")
    print(f"layer-source route residual = {layer_source}")
    print(f"trace residual = {trace_residual}")
    print(f"safe trace route = {safe_trace}")
    print(f"layer-trace route residual = {layer_trace}")
    print(f"mass payload = {mass_payload}")
    print(f"forbidden repair/O/diagnostic payload = {forbidden_payload}")

    with out.derived_results():
        out.line("source residual", StatusMark.PASS, str(source_residual))
        out.line("trace residual", StatusMark.PASS, str(trace_residual))
        out.line("mass payload", StatusMark.PASS, str(mass_payload))
        out.line("forbidden payload", StatusMark.PASS, str(forbidden_payload))
    with out.governance_assessments():
        out.line("source purity", StatusMark.PASS, "D_layer must not carry ordinary source load")
        out.line("trace purity", StatusMark.PASS, "D_layer must not carry trace payload")
        out.line("mass purity", StatusMark.PASS, "D_layer must not be A-sector mass response")
        out.line("role purity", StatusMark.PASS, "D_layer must exclude repair, active-O, and diagnostic-transition payload")
    with out.counterexamples():
        out.line("layer source", StatusMark.FAIL, f"residual={layer_source}")
        out.line("layer trace", StatusMark.FAIL, f"residual={layer_trace}")
        out.line("layer mass", StatusMark.FAIL, "mass payload route rejected unless inertness theorem exists")
        out.line("repair/O/diagnostic", StatusMark.FAIL, "repair, active-O, and diagnostic payload routes rejected")
    with out.unresolved_obligations():
        out.line("pure geometric role", StatusMark.OBLIGATION, "derive D_layer as boundary-divergence component without forbidden payloads")

    ns.record_derivation(derivation_id=MARKER_ID, inputs=[], output=sp.Tuple(source_residual, trace_residual, mass_payload, forbidden_payload), method="apply source/trace/mass/repair payload purity filters to D_layer", status=Status.DERIVED, record_kind=RecordKind.DERIVATION, result_type="payload_purity_filters", scope="role-purity filters; not D_layer theorem")
    record_claim(ns, MARKER_ID, "g73_payload_c1", GovernanceStatus.POLICY_RULE, "D_layer cannot carry source, trace, mass, repair, active-O, or diagnostic payloads.")
    record_claim(ns, MARKER_ID, "g73_payload_c2", GovernanceStatus.REJECTED_ROUTE, "Payload-bearing D_layer routes are rejected.")
    record_obligation(ns, "g73_payload_o1", "Derive D_layer as pure geometric boundary-divergence component.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_boundary_lift_interface_test.py")


if __name__ == "__main__": main()
