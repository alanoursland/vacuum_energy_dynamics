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

def beta_moment(s):
    s = sp.sympify(s)
    return sp.factor(sp.Rational(768, 1) / sp.prod(2*s + 2*m + 1 for m in range(5)))

def row_ratio(k):
    k = sp.sympify(k)
    return sp.factor((2*k - 1) / (2*k + 3))

def hierarchy_entry(k, j):
    return sp.factor(beta_moment(k+j) - row_ratio(k) * beta_moment(k+j-1))

def weight(x):
    return (1 - x**2)**4

def trial_phi(j, x):
    return x**(2*j)

def test_psi(k, x):
    return x**(2*k) - row_ratio(k) * x**(2*k-2)

def source_vector_entry(k, source_expr, x):
    return sp.factor(2 * sp.integrate(test_psi(k, x) * source_expr * weight(x), (x, 0, 1)))

DEPENDENCIES = [
    ("g101_minimal_residual", "101_residual_source_reconstruction_attempt__candidate_minimal_residual_family", "g101_minimal_residual"),
]
MARKER_ID = "g101_source_probe"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    x = sp.symbols("x", nonnegative=True)
    sources = [
        ("one", sp.Integer(1)),
        ("x2", x**2),
        ("one_minus_x2", 1-x**2),
        ("one_minus_x2_squared", (1-x**2)**2),
    ]

    results = []
    header("Candidate Source Vector Probe")
    print("Compute formal b_k(S)=2∫psi_k S w dx for simple source profiles.")
    for name, expr in sources:
        entries = []
        signs = []
        for k in range(1, 9):
            b = source_vector_entry(k, expr, x)
            entries.append(b)
            signs.append(sp.sign(b))
        results.append((name, entries, signs))
        print(f"S={name}:")
        print(f"  b_k k=1..8: {entries}")
        print(f"  signs: {signs}")

    sign_summary = {name: signs for name, _, signs in results}

    with out.derived_results():
        for name, entries, signs in results:
            out.line(f"S={name}", StatusMark.INFO, f"signs={signs}")
    with out.governance_assessments():
        out.line("source vector probes", StatusMark.PASS, "simple formal source vectors computed")
        out.line("source selection", StatusMark.DEFER, "no source profile physically selected")
        out.line("structure clue", StatusMark.INFO, "source profiles produce distinct sign patterns")
    with out.counterexamples():
        out.line("simple source as physical mass", StatusMark.FAIL, "not licensed")
        out.line("formal b_k as matter source", StatusMark.FAIL, "source separation not derived")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=sp.Symbol("simple_source_vectors_computed"),
        method="compute formal source vectors for simple source profiles",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="candidate_source_vector_probe",
        scope="residual source reconstruction",
    )
    record_claim(ns, MARKER_ID, "g101_source_c1", GovernanceStatus.POLICY_RULE, "Simple formal source-vector probes are computed, but no physical source is selected.")
    record_obligation(ns, "g101_source_o1", "Classify residual origin status.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_residual_origin_classifier.py")

if __name__ == "__main__":
    main()
