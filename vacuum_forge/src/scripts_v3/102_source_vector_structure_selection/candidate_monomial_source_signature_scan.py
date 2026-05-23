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
    ("g102_problem", "102_source_vector_structure_selection__candidate_source_structure_problem", "g102_problem"),
]
MARKER_ID = "g102_monomial_scan"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    x = sp.symbols("x", nonnegative=True)
    rows = []
    header("Candidate Monomial Source Signature Scan")
    print("Scan S_q=x^(2q), q=0..8, k=1..12.")
    for q in range(0, 9):
        S = x**(2*q)
        entries = [source_vector_entry(k, S, x) for k in range(1, 13)]
        signs = sign_pattern(entries)
        classification = classify_pattern(signs)
        rows.append((q, classification, signs, entries))
        print(f"q={q}: {classification}; signs={signs}")
        print(f"  first entries={entries[:4]}")

    counts = {}
    for _, classification, _, _ in rows:
        counts[classification] = counts.get(classification, 0) + 1

    with out.derived_results():
        out.line("monomial class counts", StatusMark.PASS, str(counts))
        for q, classification, signs, _ in rows:
            out.line(f"q={q}", StatusMark.INFO, f"{classification}; signs={signs}")
    with out.governance_assessments():
        out.line("monomial scan", StatusMark.PASS, "completed")
        out.line("structure", StatusMark.INFO, "monomial powers produce classified sign signatures")
        out.line("physical source", StatusMark.DEFER, "no q selected physically")
    with out.counterexamples():
        out.line("monomial source as physical source", StatusMark.FAIL, "not licensed")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=sp.Symbol("monomial_source_signatures_scanned"),
        method="scan b_k signatures for S=x^(2q), q=0..8, k=1..12",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="monomial_source_signature_scan",
        scope="source vector structure selection",
    )
    record_claim(ns, MARKER_ID, "g102_monomial_c1", GovernanceStatus.POLICY_RULE, "Monomial formal source signatures are classified in the tested range.")
    record_obligation(ns, "g102_monomial_o1", "Scan endpoint-weight source signatures.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_endpoint_weight_source_signature_scan.py")

if __name__ == "__main__":
    main()
