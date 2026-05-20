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
    ("g72_boundary_component", "72_layer_term_legitimacy_audit__candidate_layer_as_boundary_component_test", "g72_boundary_component"),
]
MARKER_ID = "g72_measure_support"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    y = sp.symbols("y")
    w = (1 - y**2)**2
    constant = sp.Integer(1)
    eta_like = w * y
    checks = []
    for name, expr in [("w", w), ("eta_like", eta_like), ("constant", constant)]:
        left_value = sp.simplify(expr.subs(y, -1))
        right_value = sp.simplify(expr.subs(y, 1))
        left_slope = sp.simplify(sp.diff(expr, y).subs(y, -1))
        right_slope = sp.simplify(sp.diff(expr, y).subs(y, 1))
        checks.append((name, left_value, right_value, left_slope, right_slope))

    header("Candidate Layer Measure / Support Test")
    print("Endpoint locality diagnostics:")
    for name, lv, rv, ls, rs in checks:
        print(f"  {name}: value(-1)={lv}, value(1)={rv}, slope(-1)={ls}, slope(1)={rs}")
    print()
    print("Interpretation:")
    print("  endpoint-local profiles can be necessary diagnostics for a layer component")
    print("  endpoint locality is not D_layer legitimacy or covariant boundary theorem")

    with out.derived_results():
        out.line("w endpoints", StatusMark.PASS, f"values/slopes={checks[0][1:]}")
        out.line("eta_like endpoints", StatusMark.PASS, f"values/slopes={checks[1][1:]}")
    with out.governance_assessments():
        out.line("support criterion", StatusMark.INFO, "endpoint support can constrain candidate layers")
        out.line("scope", StatusMark.OBLIGATION, "support/locality does not prove physical D_layer legitimacy")
    with out.counterexamples():
        out.line("constant layer", StatusMark.FAIL, f"constant endpoint values={checks[2][1:3]}")
        out.line("diagnostic promotion", StatusMark.FAIL, "old w/eta/N_w diagnostics cannot be promoted by passing support checks")
        out.line("support as theorem", StatusMark.FAIL, "endpoint silence is not covariant boundary theorem")
    with out.unresolved_obligations():
        out.line("measure origin", StatusMark.OBLIGATION, "derive boundary/layer measure and component status from geometry")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=sp.Tuple(w.subs(y, -1), w.subs(y, 1), sp.diff(w, y).subs(y, -1), sp.diff(w, y).subs(y, 1)),
        method="diagnostic endpoint locality check for layer-like profiles",
        status=Status.DERIVED,
        record_kind=RecordKind.COMPATIBILITY_EXAMPLE,
        result_type="layer_support_diagnostics",
        scope="support diagnostics; not D_layer theorem",
    )
    record_claim(ns, MARKER_ID, "g72_measure_c1", GovernanceStatus.POLICY_RULE, "Endpoint locality is necessary diagnostic evidence only, not layer legitimacy.")
    record_claim(ns, MARKER_ID, "g72_measure_c2", GovernanceStatus.REJECTED_ROUTE, "Constant/nonlocal layer response fails support diagnostics.")
    record_obligation(ns, "g72_measure_o1", "Derive a geometric layer measure and boundary support law.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_layer_source_trace_divergence_filter.py")

if __name__ == "__main__":
    main()
