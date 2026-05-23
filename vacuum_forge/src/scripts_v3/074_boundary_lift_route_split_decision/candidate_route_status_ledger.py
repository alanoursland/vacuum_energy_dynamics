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
    ("g73_summary", "73_layer_generator_construction__candidate_group_73_status_summary", "g73_summary"),
    ("g74_problem", "74_boundary_lift_route_split_decision__candidate_split_decision_problem", "g74_problem"),
]
MARKER_ID = "g74_route_ledger"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    status_rows = [
        ("orientation anti-match", "compatibility derived", "theorem not derived"),
        ("component anti-match", "compatibility derived", "common geometry not derived"),
        ("D_layer", "unresolved", "geometric theorem target only"),
        ("L_bulk", "open", "covariant lift-cleanliness obligation"),
        ("L_gauge", "open", "covariant lift-cleanliness obligation"),
        ("common generator", "not established", "not no-go"),
        ("active O", "not constructed", "not forced"),
        ("parent divergence", "unproven", "blocked"),
        ("recombination", "blocked", "no license"),
    ]

    header("Candidate Route Status Ledger")
    for topic, status, note in status_rows:
        print(f"{topic}: {status}; {note}")

    with out.governance_assessments():
        out.line("orientation", StatusMark.INFO, "compatibility exists but theorem not derived")
        out.line("D_layer", StatusMark.OBLIGATION, "geometric legitimacy remains unresolved")
        out.line("lift cleanliness", StatusMark.OBLIGATION, "L_bulk/L_gauge remain separate lift obligations")
        out.line("common generator", StatusMark.OBLIGATION, "strong generator not established; no no-go theorem")
        out.line("parent", StatusMark.DEFER, "parent divergence and recombination remain blocked")
    with out.counterexamples():
        out.line("route kill", StatusMark.FAIL, "not allowed from broad symbolic/governance obstruction")
        out.line("route promotion", StatusMark.FAIL, "not allowed while subtargets remain open")

    record_marker(ns, MARKER_ID, "route status ledger after Groups 71-73")
    record_claim(ns, MARKER_ID, "g74_route_c1", GovernanceStatus.POLICY_RULE, "Boundary-lift route must carry split unresolved theorem targets.")
    record_claim(ns, MARKER_ID, "g74_route_c2", GovernanceStatus.REJECTED_ROUTE, "Route kill and route promotion are both rejected from current evidence.")
    record_obligation(ns, "g74_route_o1", "Decide how to carry D_layer and L_bulk/L_gauge routes.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_layer_route_status_decision.py")

if __name__ == "__main__":
    main()
