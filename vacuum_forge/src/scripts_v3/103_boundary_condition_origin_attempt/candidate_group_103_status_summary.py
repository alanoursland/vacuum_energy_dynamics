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

def row_ratio(k):
    k = sp.sympify(k)
    return sp.factor((2*k - 1) / (2*k + 3))

def weight(x):
    return (1 - x**2)**4

def test_psi(k, x):
    return x**(2*k) - row_ratio(k) * x**(2*k-2)

def source_profile(p, q, x):
    return x**(2*q) * (1 - x**2)**p

def source_vector_entry(k, source_expr, x):
    return sp.factor(2 * sp.integrate(test_psi(k, x) * source_expr * weight(x), (x, 0, 1)))

def sign_pattern(entries):
    return [int(sp.sign(e)) for e in entries]

def classify_pattern(signs):
    if all(s > 0 for s in signs):
        return "ALL_POSITIVE"
    if all(s < 0 for s in signs):
        return "ALL_NEGATIVE"
    # Ignore zeros for flip counting but preserve zero-bearing status.
    nonzero = [s for s in signs if s != 0]
    flips = sum(1 for a, b in zip(nonzero, nonzero[1:]) if a != b)
    if signs[0] > 0 and all(s < 0 for s in signs[1:] if s != 0):
        return "LEADING_POSITIVE_THEN_NEGATIVE"
    if len(nonzero) >= 2 and nonzero[0] > 0 and all(s < 0 for s in nonzero[1:]):
        return "ZERO_THEN_OR_LEADING_POSITIVE_THEN_NEGATIVE"
    return f"MULTI_OR_MIXED_FLIP_{flips}"

def signature_for(p, q, kmax=12):
    x = sp.symbols("x", nonnegative=True)
    S = source_profile(p, q, x)
    entries = [source_vector_entry(k, S, x) for k in range(1, kmax+1)]
    signs = sign_pattern(entries)
    return classify_pattern(signs), signs

def boundary_classes(p, q):
    classes = []
    if q >= 0:
        classes.append("B0_FINITE_ORIGIN")
    if q >= 1:
        classes.append("B1_CENTER_SUPPRESSED")
    if p == 0:
        classes.append("B2_ENDPOINT_NONZERO")
    if p >= 1:
        classes.append("B3_ENDPOINT_VANISHING")
    if p >= 2:
        classes.append("B4_ENDPOINT_SMOOTH_VANISHING")
    if q >= 1 and p >= 1:
        classes.append("B5_BALANCED_SUPPRESSED")
    if p >= q:
        classes.append("B6_P_GE_Q")
    if p >= q - 1:
        classes.append("B7_P_GE_Q_MINUS_1")
    return classes

DEPENDENCIES = [
    ("g102_summary", "102_source_vector_structure_selection__candidate_group_102_status_summary", "g102_summary"),
    ("g103_problem", "103_boundary_condition_origin_attempt__candidate_boundary_origin_problem", "g103_problem"),
    ("g103_endpoint_orders", "103_boundary_condition_origin_attempt__candidate_endpoint_order_inventory", "g103_endpoint_orders"),
    ("g103_class_map", "103_boundary_condition_origin_attempt__candidate_boundary_class_signature_map", "g103_class_map"),
    ("g103_rule_probe", "103_boundary_condition_origin_attempt__candidate_boundary_selection_rule_probe", "g103_rule_probe"),
    ("g103_classifier", "103_boundary_condition_origin_attempt__candidate_boundary_origin_classifier", "g103_classifier"),
]
MARKER_ID = "g103_summary"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Group 103 Status Summary")
    print("Group 103 tests formal boundary/domain origin for source-vector signatures.")
    print("Stable result:")
    print("  endpoint behavior classes defined")
    print("  boundary class/signature map built")
    print("  boundary rules explain signature trends formally")
    print("  endpoint suppression favors all-negative/simple signatures")
    print("  endpoint concentration favors leading-positive/mixed signatures")
    print("  physical boundary not derived")
    print("  physical source not selected")
    print("  physical ledger assignment deferred")
    print("  hierarchy remains auxiliary admissibility candidate")
    print("  parent equation not ready")
    print("  recombination blocked")

    with out.governance_assessments():
        out.line("boundary scan", StatusMark.PASS, "completed")
        out.line("signature trend explanation", StatusMark.PASS, "formal")
        out.line("physical boundary", StatusMark.DEFER, "not derived")
        out.line("physical source", StatusMark.DEFER, "not selected")
        out.line("hierarchy role", StatusMark.PASS, "auxiliary admissibility candidate retained")
    with out.counterexamples():
        out.line("boundary rule as physical law", StatusMark.FAIL, "not licensed")
        out.line("source selection", StatusMark.FAIL, "not licensed")
        out.line("ledger assignment", StatusMark.FAIL, "not licensed")
    with out.unresolved_obligations():
        out.line("physical boundary derivation", StatusMark.OBLIGATION, "derive x-domain interpretation")
        out.line("source selection", StatusMark.OBLIGATION, "derive S(x) physically")
        out.line("residual operator origin", StatusMark.OBLIGATION, "derive operator/source equation if possible")

    print("\nRecommended next routes:")
    print("  104_boundary_selected_source_vector_probe")
    print("  104_residual_operator_origin_attempt")
    print("  104_difference_numerator_factorization_attempt")

    record_marker(ns, MARKER_ID, "Group 103 summary; boundary condition origin attempt")
    record_claim(ns, MARKER_ID, "g103_summary_c1", GovernanceStatus.POLICY_RULE, "Group 103 shows formal boundary/endpoint behavior explains source-vector signature trends.")
    record_claim(ns, MARKER_ID, "g103_summary_c2", GovernanceStatus.POLICY_RULE, "Physical boundary, physical source, and ledger assignment remain underived.")
    record_obligation(ns, "g103_summary_o1", "Attempt boundary-selected source-vector probe or residual operator origin next.")
    record_obligation(ns, "g103_summary_o2", "Parent divergence identity remains unproven.")
    ns.write_run_metadata()

if __name__ == "__main__":
    main()
