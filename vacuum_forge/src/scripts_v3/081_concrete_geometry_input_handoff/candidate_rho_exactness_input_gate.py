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
    ("g81_acceptance", "081_concrete_geometry_input_handoff__candidate_concrete_input_acceptance_criteria", "g81_acceptance"),
]
MARKER_ID = "g81_rho_gate"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    dXi, divB, rho_phys = sp.symbols("dXi divB rho_phys")
    gauge_form = sp.simplify(dXi + rho_phys)
    boundary_form = sp.simplify(divB + rho_phys)

    accepted = [
        "exactness operator",
        "boundary divergence object",
        "inertness/no-payload theorem candidate",
        "physical remainder test",
        "source/trace/mass/divergence payload filter",
    ]
    rejected = [
        "rho=0 by assertion",
        "exact by label",
        "dropped rho",
        "no-payload by wish",
        "boundary-exact by name only",
    ]

    header("Candidate Rho Exactness Input Gate")
    print(f"gauge form = {gauge_form}")
    print(f"boundary form = {boundary_form}")
    print("Rho route accepted input:")
    for item in accepted:
        print(f"  - {item}")
    print("Rho route rejected input:")
    for item in rejected:
        print(f"  - {item}")

    with out.derived_results():
        out.line("gauge form", StatusMark.PASS, str(gauge_form))
        out.line("boundary form", StatusMark.PASS, str(boundary_form))
    with out.governance_assessments():
        out.line("rho gate", StatusMark.PASS, "rho concrete-input gate stated")
        out.line("physical remainder", StatusMark.OBLIGATION, "future rho test must address rho_phys")
        out.line("payload filter", StatusMark.OBLIGATION, "future rho test must include payload filter")
    with out.counterexamples():
        for item in rejected:
            out.line(item, StatusMark.FAIL, "not acceptable rho concrete input")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[dXi, divB, rho_phys],
        output=gauge_form,
        method="carry rho exactness forms into concrete-input gate",
        status=Status.DERIVED,
        record_kind=RecordKind.COMPATIBILITY_EXAMPLE,
        result_type="rho_input_gate",
        scope="handoff gate; no rho theorem",
    )
    record_claim(ns, MARKER_ID, "g81_rho_c1", GovernanceStatus.POLICY_RULE, "Rho theorem attempt requires exactness/boundary/inertness object and physical remainder test.")
    record_claim(ns, MARKER_ID, "g81_rho_c2", GovernanceStatus.REJECTED_ROUTE, "Rho assertion, exact-by-label, dropped-rho, and name-only exactness are rejected.")
    record_obligation(ns, "g81_rho_o1", "Provide concrete rho exactness/inertness object before rho theorem attempt.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_parent_and_active_O_input_gate.py")

if __name__ == "__main__":
    main()
