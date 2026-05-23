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
]
MARKER_ID = "g103_class_map"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    class_map = {}
    rows = []
    header("Candidate Boundary Class Signature Map")
    print("Map boundary classes to source-vector signatures for p=0..4, q=0..6.")
    for p in range(0, 5):
        for q in range(0, 7):
            classification, signs = signature_for(p, q, 12)
            classes = boundary_classes(p, q)
            rows.append((p, q, classification, signs, classes))
            for cls in classes:
                class_map.setdefault(cls, {})
                class_map[cls][classification] = class_map[cls].get(classification, 0) + 1
            if q in (0, 1, 2, 6):
                print(f"p={p}, q={q}: {classification}; classes={classes}; signs={signs}")

    print("\nClass map counts:")
    for cls in sorted(class_map):
        print(f"  {cls}: {class_map[cls]}")

    with out.derived_results():
        for cls in sorted(class_map):
            out.line(cls, StatusMark.INFO, str(class_map[cls]))
    with out.governance_assessments():
        out.line("boundary class map", StatusMark.PASS, "built")
        out.line("signature trend", StatusMark.INFO, "endpoint suppression classes favor cleaner negative signatures")
        out.line("physical boundary", StatusMark.DEFER, "not selected")
    with out.counterexamples():
        out.line("boundary class as physical selector", StatusMark.FAIL, "not enough")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=sp.Symbol("boundary_class_signature_map_built"),
        method="map formal boundary classes to source-vector signature classifications",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="boundary_class_signature_map",
        scope="boundary origin attempt",
    )
    record_claim(ns, MARKER_ID, "g103_map_c1", GovernanceStatus.POLICY_RULE, "Formal boundary classes are mapped to source-vector signature families.")
    record_obligation(ns, "g103_map_o1", "Probe candidate boundary selection rules.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_boundary_selection_rule_probe.py")

if __name__ == "__main__":
    main()
