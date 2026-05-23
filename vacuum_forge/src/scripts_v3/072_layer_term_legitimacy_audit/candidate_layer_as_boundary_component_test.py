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
    ("g72_requirements", "72_layer_term_legitimacy_audit__candidate_layer_component_requirements", "g72_requirements"),
    ("g72_diagnostic_exclusion", "72_layer_term_legitimacy_audit__candidate_diagnostic_transition_exclusion", "g72_diagnostic_exclusion"),
]
MARKER_ID = "g72_boundary_component"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    D_layer, a_layer = sp.symbols("D_layer a_layer")
    L_layer = sp.simplify(a_layer * D_layer)
    residual = sp.simplify(L_layer + D_layer)
    solution = sp.solve(sp.Eq(sp.diff(residual, D_layer), 0), a_layer)

    patterns = [
        ("geometric_layer_component", sp.simplify((-1)*D_layer + D_layer), "retained only if D_layer has geometric origin"),
        ("missing_layer", sp.simplify(0*D_layer + D_layer), "blocked; leaves D_layer unmatched"),
        ("same_sign_layer", sp.simplify((1)*D_layer + D_layer), "rejected; doubles layer component"),
        ("diagnostic_layer", sp.Symbol("D_diag"), "rejected; diagnostic transition cannot supply component"),
    ]

    header("Candidate Layer As Boundary Component Test")
    print(f"L_layer = {L_layer}")
    print(f"residual = {residual}")
    print(f"a_layer solution = {solution}")
    print()
    print("Layer component patterns:")
    for name, expr, reason in patterns:
        print(f"  {name}: residual={expr}; {reason}")

    with out.derived_results():
        out.line("layer residual", StatusMark.PASS, str(residual))
        out.line("a_layer compatibility", StatusMark.PASS, str(solution))
    with out.governance_assessments():
        out.line("component route", StatusMark.INFO, "a_layer=-1 retained only as compatibility unless geometric layer origin is derived")
        out.line("layer theorem", StatusMark.OBLIGATION, "D_layer legitimacy remains required before component anti-match can be physical")
    with out.counterexamples():
        out.line("manual coefficient", StatusMark.FAIL, "solving a_layer=-1 is compatibility, not layer theorem")
        out.line("missing layer", StatusMark.FAIL, "leaves D_layer unmatched")
        out.line("diagnostic layer", StatusMark.FAIL, "old diagnostic transition response remains excluded")
    with out.unresolved_obligations():
        out.line("D_layer component theorem", StatusMark.OBLIGATION, "derive D_layer as legitimate component in common boundary object")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=sp.Tuple(*solution),
        method="solve layer component anti-match compatibility",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="layer_component_compatibility",
        scope="compatibility; not D_layer legitimacy theorem",
    )
    record_claim(ns, MARKER_ID, "g72_component_c1", GovernanceStatus.POLICY_RULE, "Layer anti-match requires a_layer=-1 as compatibility only.")
    record_claim(ns, MARKER_ID, "g72_component_c2", GovernanceStatus.REJECTED_ROUTE, "Diagnostic and missing-layer routes are rejected.")
    record_obligation(ns, "g72_component_o1", "Derive D_layer legitimacy from boundary geometry.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_layer_measure_support_test.py")

if __name__ == "__main__":
    main()
