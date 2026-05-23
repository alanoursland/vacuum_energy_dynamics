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
    ("g86_payload_action", "086_shape_origin_geometry_derivation__candidate_payload_action_minimizer", "g86_payload_action"),
]
MARKER_ID = "g86_weighted_consistency"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    R, ell = sp.symbols("R ell")
    M = sp.symbols("M0:8")
    W = []
    for n in range(4):
        Wn = sp.expand(R**2*M[n] + 2*R*ell*M[n+1] + ell**2*M[n+2])
        W.append(Wn)
    W_under_block = [sp.simplify(expr.subs({M[i]: 0 for i in range(6)})) for expr in W]

    header("Candidate Weighted Consistency From Flat Block")
    print("For quadratic mu = R^2 + 2Rell y + ell^2 y^2:")
    for n, expr in enumerate(W):
        print(f"W{n} = {expr}")
    print("If M0..M5 vanish:")
    for n, expr in enumerate(W_under_block):
        print(f"W{n} -> {expr}")

    with out.derived_results():
        for n, expr in enumerate(W):
            out.line(f"W{n} formula", StatusMark.PASS, str(expr))
        for n, expr in enumerate(W_under_block):
            out.line(f"W{n} under block", StatusMark.PASS, str(expr))
    with out.governance_assessments():
        out.line("weighted consistency", StatusMark.PASS, "W0..W3 suppression follows from M0..M5 under quadratic measure")
        out.line("no separate tuning", StatusMark.PASS, "weighted low-order suppression is consequence of flat moment block")
    with out.counterexamples():
        out.line("weighted suppression independent miracle", StatusMark.FAIL, "weighted suppression follows from moment block and quadratic measure")
        out.line("all weighted orders", StatusMark.FAIL, "only W0..W3 follow from M0..M5")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=list(M[:6]) + [R, ell],
        output=sp.Matrix(W_under_block),
        method="express weighted moments Wn through flat moments for quadratic measure",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="weighted_consistency_from_flat_block",
        scope="quadratic measure and low-order moment block",
    )
    record_claim(ns, MARKER_ID, "g86_weight_c1", GovernanceStatus.POLICY_RULE, "Quadratic-measure W0..W3 suppression follows from flat M0..M5 suppression.")
    record_obligation(ns, "g86_weight_o1", "Classify reduced shape-origin route.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_shape_origin_route_classifier.py")

if __name__ == "__main__":
    main()
