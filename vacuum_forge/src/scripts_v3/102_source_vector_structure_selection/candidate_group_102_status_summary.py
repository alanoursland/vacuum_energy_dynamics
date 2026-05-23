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

def source_vector_entry(k, source_expr, x):
    return sp.factor(2 * sp.integrate(test_psi(k, x) * source_expr * weight(x), (x, 0, 1)))

def sign_pattern(entries):
    return [int(sp.sign(e)) for e in entries]

def classify_pattern(signs):
    if all(s > 0 for s in signs):
        return "ALL_POSITIVE"
    if all(s < 0 for s in signs):
        return "ALL_NEGATIVE"
    flips = sum(1 for a, b in zip(signs, signs[1:]) if a != b)
    if flips == 1 and signs[0] > 0 and all(s < 0 for s in signs[1:]):
        return "LEADING_POSITIVE_THEN_NEGATIVE"
    if flips == 1 and signs[0] < 0 and all(s > 0 for s in signs[1:]):
        return "LEADING_NEGATIVE_THEN_POSITIVE"
    return f"MULTI_OR_MIXED_FLIP_{flips}"

DEPENDENCIES = [
    ("g101_summary", "101_residual_source_reconstruction_attempt__candidate_group_101_status_summary", "g101_summary"),
    ("g102_problem", "102_source_vector_structure_selection__candidate_source_structure_problem", "g102_problem"),
    ("g102_monomial_scan", "102_source_vector_structure_selection__candidate_monomial_source_signature_scan", "g102_monomial_scan"),
    ("g102_endpoint_scan", "102_source_vector_structure_selection__candidate_endpoint_weight_source_signature_scan", "g102_endpoint_scan"),
    ("g102_mixed_scan", "102_source_vector_structure_selection__candidate_mixed_source_signature_scan", "g102_mixed_scan"),
    ("g102_classifier", "102_source_vector_structure_selection__candidate_source_structure_classifier", "g102_classifier"),
]
MARKER_ID = "g102_summary"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Group 102 Status Summary")
    print("Group 102 classifies formal source-vector structures.")
    print("Stable result:")
    print("  monomial source signatures scanned")
    print("  endpoint-weight source signatures scanned")
    print("  mixed source signatures scanned")
    print("  clean formal signature families identified")
    print("  physical source not selected")
    print("  boundary/domain origin required for physical selection")
    print("  physical ledger assignment deferred")
    print("  hierarchy remains auxiliary admissibility candidate")
    print("  parent equation not ready")
    print("  recombination blocked")

    with out.governance_assessments():
        out.line("source scan", StatusMark.PASS, "completed")
        out.line("signature classes", StatusMark.PASS, "identified")
        out.line("physical source", StatusMark.DEFER, "not selected")
        out.line("boundary origin", StatusMark.OBLIGATION, "required")
        out.line("hierarchy role", StatusMark.PASS, "auxiliary admissibility candidate retained")
    with out.counterexamples():
        out.line("signature as source selection", StatusMark.FAIL, "not licensed")
        out.line("S as matter source", StatusMark.FAIL, "not licensed")
        out.line("projection as ledger assignment", StatusMark.FAIL, "not licensed")
    with out.unresolved_obligations():
        out.line("boundary/domain origin", StatusMark.OBLIGATION, "derive selection mechanism")
        out.line("physical source", StatusMark.OBLIGATION, "derive S(x) physically")
        out.line("admissibility theorem", StatusMark.OBLIGATION, "continue determinant/numerator route if desired")

    print("\nRecommended next routes:")
    print("  103_boundary_condition_origin_attempt")
    print("  103_source_vector_target_compatibility")
    print("  103_difference_numerator_factorization_attempt")

    record_marker(ns, MARKER_ID, "Group 102 summary; source vector structure selection")
    record_claim(ns, MARKER_ID, "g102_summary_c1", GovernanceStatus.POLICY_RULE, "Group 102 classifies formal source-vector signature families without selecting a physical source.")
    record_claim(ns, MARKER_ID, "g102_summary_c2", GovernanceStatus.POLICY_RULE, "Boundary/domain origin is required before physical source selection.")
    record_obligation(ns, "g102_summary_o1", "Attempt boundary condition origin or source-vector target compatibility next.")
    record_obligation(ns, "g102_summary_o2", "Parent divergence identity remains unproven.")
    ns.write_run_metadata()

if __name__ == "__main__":
    main()
