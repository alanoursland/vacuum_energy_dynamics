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
    ("g81_acceptance", "81_concrete_geometry_input_handoff__candidate_concrete_input_acceptance_criteria", "g81_acceptance"),
]
MARKER_ID = "g81_lift_gate"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    K, rho = sp.symbols("K rho")
    residual = sp.simplify(K + (-K + rho))

    accepted = [
        "covariant lift identity candidate",
        "common K origin",
        "sign/orientation relation",
        "rho handling target",
        "L_bulk/L_gauge domain and role",
    ]
    rejected = [
        "L_bulk=-L_gauge by choice",
        "dropped L_bulk or L_gauge",
        "exact-pair scaffold alone",
        "free sign or coefficient",
        "repair current",
    ]

    header("Candidate Lift Identity Input Gate")
    print(f"shared lift residual carried forward = {residual}")
    print("Lift route accepted input:")
    for item in accepted:
        print(f"  - {item}")
    print("Lift route rejected input:")
    for item in rejected:
        print(f"  - {item}")

    with out.derived_results():
        out.line("shared residual", StatusMark.PASS, str(residual))
    with out.governance_assessments():
        out.line("lift gate", StatusMark.PASS, "lift concrete-input gate stated")
        out.line("K origin", StatusMark.OBLIGATION, "future lift test requires common K origin")
        out.line("rho handling", StatusMark.OBLIGATION, "future lift test must handle rho")
    with out.counterexamples():
        for item in rejected:
            out.line(item, StatusMark.FAIL, "not acceptable lift concrete input")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[K, rho],
        output=residual,
        method="carry shared lift residual into concrete-input gate",
        status=Status.DERIVED,
        record_kind=RecordKind.COMPATIBILITY_EXAMPLE,
        result_type="lift_input_gate",
        scope="handoff gate; no lift theorem",
    )
    record_claim(ns, MARKER_ID, "g81_lift_c1", GovernanceStatus.POLICY_RULE, "Lift theorem attempt requires concrete identity, K/sign origin, and rho handling.")
    record_claim(ns, MARKER_ID, "g81_lift_c2", GovernanceStatus.REJECTED_ROUTE, "Chosen cancellation, dropped lift terms, exact scaffold alone, and repair inputs are rejected.")
    record_obligation(ns, "g81_lift_o1", "Provide concrete covariant lift identity before lift theorem attempt.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_rho_exactness_input_gate.py")

if __name__ == "__main__":
    main()
