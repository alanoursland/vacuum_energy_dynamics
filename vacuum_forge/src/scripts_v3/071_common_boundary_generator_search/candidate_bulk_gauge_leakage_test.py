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


def record_claim(ns, derivation_id: str, claim_id: str, status: GovernanceStatus, statement: str) -> None:
    ns.record_claim(
        ClaimRecord(
            claim_id=claim_id,
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=status,
            statement=statement,
            derivation_ids=[derivation_id],
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
    ("g70_bulk_gauge", "070_boundary_lift_matching_theorem_attempt__candidate_bulk_gauge_neutrality", "g70_bulk_gauge"),
    ("g71_components", "071_common_boundary_generator_search__candidate_component_forcing_test", "g71_component_forcing"),
]
DERIVATION_ID = "g71_bulk_gauge_leakage"


def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    L_bulk, L_gauge, X = sp.symbols("L_bulk L_gauge X")
    residual = sp.simplify(L_bulk + L_gauge)
    cases = [
        ("bulk_gauge_neutral", {L_bulk: 0, L_gauge: 0}, "retained theorem target"),
        ("bulk_leakage", {L_bulk: X, L_gauge: 0}, "blocked"),
        ("gauge_leakage", {L_bulk: 0, L_gauge: X}, "blocked"),
        ("mixed_cancellation", {L_bulk: X, L_gauge: -X}, "rejected unless shared lift identity derives it"),
        ("independent_unknown", {}, "open lift-cleanliness obligation"),
    ]

    header("Candidate Bulk/Gauge Leakage Test")
    print(f"post-boundary-match residual = {residual}")
    print()
    print("Classifications:")
    for name, subs, status in cases:
        value = sp.simplify(residual.subs(subs)) if subs else residual
        print(f"  {name}: residual={value}; {status}")

    with out.derived_results():
        out.line("post-boundary residual", StatusMark.PASS, str(residual))
    with out.governance_assessments():
        out.line("neutral route", StatusMark.INFO, "L_bulk=0 and L_gauge=0 retained as lift-cleanliness theorem target")
        out.line("mixed cancellation", StatusMark.OBLIGATION, "bulk/gauge mutual cancellation requires shared lift identity, not repair choice")
    with out.counterexamples():
        out.line("bulk leakage", StatusMark.FAIL, "L_bulk != 0 blocks parent divergence identity")
        out.line("gauge leakage", StatusMark.FAIL, "L_gauge != 0 blocks parent divergence identity")
        out.line("forced mutual cancellation", StatusMark.FAIL, "choosing L_bulk=-L_gauge is repair-like unless derived")
    with out.unresolved_obligations():
        out.line("bulk neutrality", StatusMark.OBLIGATION, "derive L_bulk=0 or a lawful shared lift identity")
        out.line("gauge neutrality", StatusMark.OBLIGATION, "derive L_gauge=0 or a lawful shared lift identity")

    ns.record_derivation(
        derivation_id=DERIVATION_ID,
        inputs=[],
        output=residual,
        method="classify bulk/gauge leakage after boundary anti-match",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="bulk_gauge_leakage_sieve",
        scope="leakage classification; not covariant lift theorem",
    )
    record_claim(ns, DERIVATION_ID, "g71_bulk_gauge_c1", GovernanceStatus.POLICY_RULE, "Boundary anti-match does not close L_bulk or L_gauge.")
    record_claim(ns, DERIVATION_ID, "g71_bulk_gauge_c2", GovernanceStatus.REJECTED_ROUTE, "Bulk/gauge leakage and forced mutual cancellation are rejected as theorem substitutes.")
    record_obligation(ns, "g71_bulk_gauge_o1", "Derive bulk/gauge neutrality or split it into a separate covariant-lift theorem target.")
    ns.write_run_metadata()

    print("\nPossible next script:")
    print("  candidate_generator_class_sieve.py")


if __name__ == "__main__":
    main()
