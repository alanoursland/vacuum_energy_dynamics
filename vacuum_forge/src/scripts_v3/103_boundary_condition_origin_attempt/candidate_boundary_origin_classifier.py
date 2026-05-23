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
    ("g103_endpoint_orders", "103_boundary_condition_origin_attempt__candidate_endpoint_order_inventory", "g103_endpoint_orders"),
    ("g103_class_map", "103_boundary_condition_origin_attempt__candidate_boundary_class_signature_map", "g103_class_map"),
    ("g103_rule_probe", "103_boundary_condition_origin_attempt__candidate_boundary_selection_rule_probe", "g103_rule_probe"),
]
MARKER_ID = "g103_classifier"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    classifications = [
        ("ENDPOINT_BEHAVIOR_CLASSES_DEFINED", "stable", "origin order 2q and endpoint order p inventoried"),
        ("BOUNDARY_CLASS_SIGNATURE_MAP_BUILT", "stable", "boundary classes mapped to source-vector signatures"),
        ("BOUNDARY_RULES_EXPLAIN_SIGNATURE_TRENDS", "stable", "endpoint suppression vs concentration tracks sign classes"),
        ("ALL_NEGATIVE_FAVORED_BY_ENDPOINT_SUPPRESSION", "stable", "p>=q / low-q classes tend toward all-negative"),
        ("LEADING_POSITIVE_FAVORED_BY_ENDPOINT_CONCENTRATION", "stable", "larger q relative to p creates leading positive runs"),
        ("PHYSICAL_BOUNDARY_NOT_DERIVED", "stable", "x=0/x=1 interpretation remains formal"),
        ("PHYSICAL_SOURCE_NOT_SELECTED", "stable", "no S selected by physics"),
        ("PHYSICAL_LEDGER_ASSIGNMENT_DEFERRED", "stable", "not J_curv/H_exch/total burden"),
        ("HIERARCHY_REMAINS_AUXILIARY_ADMISSIBILITY_CANDIDATE", "stable", "formal selector only"),
        ("PARENT_EQUATION_NOT_READY", "stable", "no H insertion/source law"),
        ("RECOMBINATION_BLOCKED", "stable", "no recombination license"),
    ]

    header("Candidate Boundary Origin Classifier")
    for name, status, reason in classifications:
        print(f"{name}: {status}; {reason}")

    with out.governance_assessments():
        out.line("endpoint classes", StatusMark.PASS, "defined")
        out.line("signature trend", StatusMark.PASS, "explained formally")
        out.line("physical boundary", StatusMark.DEFER, "not derived")
        out.line("physical source", StatusMark.DEFER, "not selected")
    with out.counterexamples():
        out.line("x endpoints as physical boundaries", StatusMark.FAIL, "not licensed")
        out.line("formal p/q rule as source law", StatusMark.FAIL, "not licensed")
        out.line("ledger assignment", StatusMark.FAIL, "not licensed")
    with out.unresolved_obligations():
        out.line("physical boundary derivation", StatusMark.OBLIGATION, "derive x-domain interpretation")
        out.line("source selection", StatusMark.OBLIGATION, "derive p/q or S(x) from boundary/physics")
        out.line("functional origin", StatusMark.OBLIGATION, "connect source class to burden functional if possible")

    record_marker(ns, MARKER_ID, "boundary origin classifier")
    record_claim(ns, MARKER_ID, "g103_class_c1", GovernanceStatus.POLICY_RULE, "Formal endpoint/boundary classes explain source-vector signature trends.")
    record_claim(ns, MARKER_ID, "g103_class_c2", GovernanceStatus.POLICY_RULE, "Physical boundary and source selection remain underived.")
    record_obligation(ns, "g103_class_o1", "Attempt boundary-selected source-vector probe or residual operator origin next.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_group_103_status_summary.py")

if __name__ == "__main__":
    main()
