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
    ("g72_problem", "072_layer_term_legitimacy_audit__candidate_layer_legitimacy_problem", "g72_problem"),
    ("g72_requirements", "072_layer_term_legitimacy_audit__candidate_layer_component_requirements", "g72_requirements"),
]
MARKER_ID = "g72_diagnostic_exclusion"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    D_geo, D_diag, D_repair = sp.symbols("D_geo D_diag D_repair")
    x_geo, x_diag, x_repair = sp.symbols("x_geo x_diag x_repair")
    D_layer_candidate = sp.simplify(x_geo*D_geo + x_diag*D_diag + x_repair*D_repair)
    legal_candidate = sp.simplify(D_layer_candidate.subs({x_diag: 0, x_repair: 0}))
    diagnostic_leak = sp.diff(D_layer_candidate, D_diag)
    repair_leak = sp.diff(D_layer_candidate, D_repair)

    header("Candidate Diagnostic Transition Exclusion")
    print(f"D_layer_candidate = {D_layer_candidate}")
    print(f"diagnostic payload coefficient = {diagnostic_leak}")
    print(f"repair payload coefficient = {repair_leak}")
    print(f"legal candidate after diagnostic/repair exclusion = {legal_candidate}")

    with out.derived_results():
        out.line("candidate decomposition", StatusMark.PASS, str(D_layer_candidate))
        out.line("legal exclusion form", StatusMark.PASS, str(legal_candidate))
    with out.governance_assessments():
        out.line("diagnostic exclusion", StatusMark.PASS, "D_diag coefficient must vanish")
        out.line("repair exclusion", StatusMark.PASS, "D_repair coefficient must vanish")
        out.line("geometric route", StatusMark.INFO, "only D_geo-like origin can remain as theorem target")
    with out.counterexamples():
        out.line("old transition response", StatusMark.FAIL, "eta/eta^2/N_w/R1/R2 remain diagnostic evidence, not D_layer")
        out.line("arbitrary counterterm", StatusMark.FAIL, "repair coefficient cannot supply legitimacy")
        out.line("zero by deletion", StatusMark.FAIL, "setting x_geo=0 is no layer route, not a legitimate layer")
    with out.unresolved_obligations():
        out.line("geometric layer origin", StatusMark.OBLIGATION, "derive D_geo from boundary/layer geometry")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=legal_candidate,
        method="decompose D_layer candidate and exclude diagnostic/repair payloads",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="diagnostic_transition_exclusion",
        scope="exclusion filter; not D_layer origin",
    )
    record_claim(ns, MARKER_ID, "g72_diag_c1", GovernanceStatus.REJECTED_ROUTE, "Diagnostic transition response and repair current are rejected as D_layer sources.")
    record_claim(ns, MARKER_ID, "g72_diag_c2", GovernanceStatus.POLICY_RULE, "Only a geometric layer-origin route remains as theorem target.")
    record_obligation(ns, "g72_diag_o1", "Derive the geometric D_layer origin if route is retained.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_layer_as_boundary_component_test.py")

if __name__ == "__main__":
    main()
