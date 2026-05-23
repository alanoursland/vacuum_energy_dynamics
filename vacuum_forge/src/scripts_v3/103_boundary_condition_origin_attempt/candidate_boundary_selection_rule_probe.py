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
    ("g103_class_map", "103_boundary_condition_origin_attempt__candidate_boundary_class_signature_map", "g103_class_map"),
]
MARKER_ID = "g103_rule_probe"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    rows = []
    for p in range(0, 5):
        for q in range(0, 7):
            classification, signs = signature_for(p, q, 12)
            rows.append((p, q, classification, signs))

    rules = {
        "ENDPOINT_VANISHING_p_ge_1": lambda p, q: p >= 1,
        "SMOOTH_ENDPOINT_p_ge_2": lambda p, q: p >= 2,
        "CENTER_SUPPRESSED_q_ge_1": lambda p, q: q >= 1,
        "BALANCED_p_ge_q": lambda p, q: p >= q,
        "BALANCED_p_ge_q_minus_1": lambda p, q: p >= q - 1,
        "ENDPOINT_CONCENTRATED_q_gt_p_plus_1": lambda p, q: q > p + 1,
        "LOW_Q_q_le_1": lambda p, q: q <= 1,
    }

    header("Candidate Boundary Selection Rule Probe")
    print("Probe formal rules against signature classes.")
    summaries = {}
    for rule_name, pred in rules.items():
        selected = [(p, q, c) for p, q, c, _ in rows if pred(p, q)]
        counts = {}
        for _, _, c in selected:
            counts[c] = counts.get(c, 0) + 1
        summaries[rule_name] = counts
        print(f"{rule_name}: count={len(selected)}, classes={counts}")
        print(f"  selected={selected[:15]}")

    with out.derived_results():
        for rule_name, counts in summaries.items():
            out.line(rule_name, StatusMark.INFO, str(counts))
    with out.governance_assessments():
        out.line("selection rule probe", StatusMark.PASS, "completed")
        out.line("balanced rules", StatusMark.INFO, "p>=q and low-q rules favor all-negative/simple signatures")
        out.line("endpoint concentration", StatusMark.INFO, "q>p+1 favors leading-positive/mixed signatures")
        out.line("physical boundary", StatusMark.DEFER, "no rule selected physically")
    with out.counterexamples():
        out.line("formal rule as physical boundary", StatusMark.FAIL, "not licensed")
        out.line("signature trend as source law", StatusMark.FAIL, "not licensed")

    record_marker(ns, MARKER_ID, "boundary selection rule probe")
    record_claim(ns, MARKER_ID, "g103_rule_c1", GovernanceStatus.POLICY_RULE, "Formal boundary selection rules explain signature trends but do not select a physical source.")
    record_obligation(ns, "g103_rule_o1", "Classify boundary origin status.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_boundary_origin_classifier.py")

if __name__ == "__main__":
    main()
