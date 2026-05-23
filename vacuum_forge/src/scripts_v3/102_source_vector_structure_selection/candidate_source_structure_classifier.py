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
    ("g102_monomial_scan", "102_source_vector_structure_selection__candidate_monomial_source_signature_scan", "g102_monomial_scan"),
    ("g102_endpoint_scan", "102_source_vector_structure_selection__candidate_endpoint_weight_source_signature_scan", "g102_endpoint_scan"),
    ("g102_mixed_scan", "102_source_vector_structure_selection__candidate_mixed_source_signature_scan", "g102_mixed_scan"),
]
MARKER_ID = "g102_classifier"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    classifications = [
        ("SOURCE_VECTOR_STRUCTURE_SCANNED", "stable", "monomial, endpoint-weight, and mixed families scanned"),
        ("MONOMIAL_SOURCE_CLASSES_IDENTIFIED", "stable", "S=x^(2q) signatures classified"),
        ("ENDPOINT_WEIGHT_CLASSES_IDENTIFIED", "stable", "S=(1-x^2)^p signatures classified"),
        ("MIXED_SOURCE_CLASSES_IDENTIFIED", "stable", "S=x^(2q)(1-x^2)^p signatures classified"),
        ("CLEAN_SIGNATURE_FAMILIES_IDENTIFIED", "stable", "all-negative and leading-positive classes tracked"),
        ("PHYSICAL_SOURCE_NOT_SELECTED", "stable", "no S(x) chosen by physics"),
        ("BOUNDARY_ORIGIN_REQUIRED", "stable", "boundary/domain data needed to select S"),
        ("PHYSICAL_LEDGER_ASSIGNMENT_DEFERRED", "stable", "not J_curv/H_exch/total burden"),
        ("HIERARCHY_REMAINS_AUXILIARY_ADMISSIBILITY_CANDIDATE", "stable", "formal source scan only"),
        ("PARENT_EQUATION_NOT_READY", "stable", "no H insertion/source law"),
        ("RECOMBINATION_BLOCKED", "stable", "no recombination license"),
    ]

    header("Candidate Source Structure Classifier")
    for name, status, reason in classifications:
        print(f"{name}: {status}; {reason}")

    with out.governance_assessments():
        out.line("source structure scan", StatusMark.PASS, "completed")
        out.line("clean signature families", StatusMark.PASS, "identified formally")
        out.line("physical source", StatusMark.DEFER, "not selected")
        out.line("boundary origin", StatusMark.OBLIGATION, "required for physical selection")
    with out.counterexamples():
        out.line("sign signature as physical selection", StatusMark.FAIL, "not enough")
        out.line("formal source as matter", StatusMark.FAIL, "not licensed")
        out.line("ledger assignment", StatusMark.FAIL, "not licensed")
    with out.unresolved_obligations():
        out.line("boundary selection", StatusMark.OBLIGATION, "derive which source class comes from domain/boundary problem")
        out.line("source physics", StatusMark.OBLIGATION, "derive S(x) physically")
        out.line("functional origin", StatusMark.OBLIGATION, "connect source class to burden functional if possible")

    record_marker(ns, MARKER_ID, "source structure classifier")
    record_claim(ns, MARKER_ID, "g102_class_c1", GovernanceStatus.POLICY_RULE, "Formal source-vector signature classes are identified, but no physical source is selected.")
    record_claim(ns, MARKER_ID, "g102_class_c2", GovernanceStatus.POLICY_RULE, "Boundary/domain origin is required before source selection can become physical.")
    record_obligation(ns, "g102_class_o1", "Attempt boundary condition origin or source selection next.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_group_102_status_summary.py")

if __name__ == "__main__":
    main()
