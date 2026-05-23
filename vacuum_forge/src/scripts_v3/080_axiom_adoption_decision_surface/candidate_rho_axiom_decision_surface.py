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
    ("g79_rho_axioms", "079_axiom_candidate_inventory__candidate_rho_status_axiom_candidates", "g79_rho_axioms"),
    ("g80_criteria", "080_axiom_adoption_decision_surface__candidate_adoption_decision_criteria", "g80_criteria"),
]
MARKER_ID = "g80_rho_surface"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    dXi, divB, rho_phys = sp.symbols("dXi divB rho_phys")
    gauge_form = sp.simplify(dXi + rho_phys)
    boundary_form = sp.simplify(divB + rho_phys)
    rows = [("RHO_ZERO_AXIOM", "DEFERRED_HIGH_BURDEN", "erases rho and needs explicit owner decision"), ("RHO_GAUGE_EXACT_AXIOM", "DEFERRED", "requires exactness operator and rho_phys=0"), ("RHO_BOUNDARY_EXACT_AXIOM", "DEFERRED", "requires boundary divergence object and no bulk remainder"), ("RHO_NO_PAYLOAD_AXIOM", "DEFERRED", "requires source/trace/mass/divergence validation"), ("DROPPED_RHO_AXIOM", "REJECTED", "erases rho without theorem/adoption"), ("EXACT_BY_LABEL_AXIOM", "REJECTED", "calls rho exact without content")]
    header("Candidate Rho Axiom Decision Surface")
    print(f"gauge form = {gauge_form}")
    print(f"boundary form = {boundary_form}")
    for name, status, reason in rows: print(f"{name}: {status}; {reason}")
    with out.derived_results():
        out.line("gauge form", StatusMark.PASS, str(gauge_form))
        out.line("boundary form", StatusMark.PASS, str(boundary_form))
    with out.governance_assessments():
        out.line("rho zero axiom", StatusMark.DEFER, "deferred high-burden candidate")
        out.line("rho gauge-exact axiom", StatusMark.DEFER, "deferred pending exactness/no physical remainder")
        out.line("rho boundary-exact axiom", StatusMark.DEFER, "deferred pending boundary object/no bulk remainder")
        out.line("rho no-payload axiom", StatusMark.DEFER, "deferred pending payload validation")
    with out.counterexamples():
        out.line("dropped rho axiom", StatusMark.FAIL, "rejected shortcut")
        out.line("exact-by-label axiom", StatusMark.FAIL, "rejected shortcut")
    with out.unresolved_obligations():
        out.line("rho validation", StatusMark.OBLIGATION, "future rho adoption decision must validate zero/exact/boundary/no-payload status")
    ns.record_derivation(derivation_id=MARKER_ID, inputs=[dXi, divB, rho_phys], output=gauge_form, method="record rho exactness forms carried into decision surface", status=Status.DERIVED, record_kind=RecordKind.COMPATIBILITY_EXAMPLE, result_type="rho_axiom_decision_surface", scope="decision surface; no axiom adoption")
    record_claim(ns, MARKER_ID, "g80_rho_c1", GovernanceStatus.POLICY_RULE, "Rho axiom candidates are deferred; none are adopted.")
    record_claim(ns, MARKER_ID, "g80_rho_c2", GovernanceStatus.REJECTED_ROUTE, "Dropped-rho and exact-by-label shortcuts remain rejected.")
    record_obligation(ns, "g80_rho_o1", "Future rho adoption decision must address exactness, physical remainder, and payload validation.")
    ns.write_run_metadata()
    print("\nPossible next script:\n  candidate_parent_facing_axiom_gate.py")
if __name__ == "__main__": main()
