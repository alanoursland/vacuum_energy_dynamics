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
    ("g81_summary", "081_concrete_geometry_input_handoff__candidate_group_81_status_summary", "g81_summary"),
    ("g82_problem", "082_rho_exactness_concrete_test__candidate_rho_exactness_problem", "g82_problem"),
]
MARKER_ID = "g82_requirements"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    y = sp.symbols("y")
    J = sp.Function("J")
    rho = sp.diff(J(y), y)
    flat_charge = sp.integrate(rho, (y, -1, 1))
    boundary_flux_form = sp.simplify(J(1) - J(-1))

    header("Candidate Exact Operator Requirements")
    print(f"rho exact form = {rho}")
    print(f"flat charge by fundamental theorem = {flat_charge}")
    print(f"boundary flux form = {boundary_flux_form}")
    print("Requirements:")
    print("  J(-1)=J(1)=0 proves flat integrated neutrality")
    print("  local rho must be checked separately")
    print("  weighted/covariant neutrality must be checked separately")
    print("  payload inertness must be checked separately")

    with out.derived_results():
        out.line("flat charge identity", StatusMark.PASS, str(flat_charge))
        out.line("boundary flux form", StatusMark.PASS, str(boundary_flux_form))
    with out.governance_assessments():
        out.line("exactness requirements", StatusMark.PASS, "requirements stated")
        out.line("local caution", StatusMark.OBLIGATION, "flat charge does not imply local rho=0")
        out.line("weighted caution", StatusMark.OBLIGATION, "weighted neutrality requires separate test")
    with out.counterexamples():
        out.line("integral as local zero", StatusMark.FAIL, "integral neutrality cannot be spent as local vanishing")
        out.line("exact label as proof", StatusMark.FAIL, "must show flux and measure behavior")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=flat_charge,
        method="fundamental theorem for rho=dJ/dy over [-1,1]",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="exact_operator_requirement",
        scope="reduced one-dimensional exactness requirement",
    )
    record_claim(ns, MARKER_ID, "g82_req_c1", GovernanceStatus.POLICY_RULE, "Flat neutrality from exactness requires endpoint flux control and does not imply local or weighted neutrality.")
    record_obligation(ns, "g82_req_o1", "Construct compact-support exact remainder and test endpoint flux.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_compact_support_exact_remainder.py")

if __name__ == "__main__":
    main()
