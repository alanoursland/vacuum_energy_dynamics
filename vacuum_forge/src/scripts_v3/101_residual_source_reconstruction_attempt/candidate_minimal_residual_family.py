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
    ("g101_projected_profile", "101_residual_source_reconstruction_attempt__candidate_projected_profile_identity", "g101_projected_profile"),
]
MARKER_ID = "g101_minimal_residual"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    x = sp.symbols("x", nonnegative=True)
    k = sp.symbols("k", integer=True, positive=True)
    S = sp.Function("S")
    b_formal = sp.Symbol("b_k(S)")

    header("Candidate Minimal Residual Family")
    print("Define formal residual family:")
    print("  R_S[f](x) = f(x) - S(x)")
    print("Projected equations:")
    print("  2∫psi_k(x)[f_N(x)-S(x)]w(x)dx = 0")
    print("Equivalent finite system:")
    print("  A c = b(S)")
    print("where:")
    print("  b_k(S)=2∫psi_k(x)S(x)w(x)dx")
    print()
    print("This is formal only: S(x) is not yet a physical source, mass density, burden ledger, or exchange term.")

    with out.derived_results():
        out.line("minimal residual family", StatusMark.PASS, "R_S[f]=f-S")
        out.line("source vector formula", StatusMark.PASS, "b_k(S)=2∫psi_k S w dx")
    with out.governance_assessments():
        out.line("formal residual", StatusMark.PASS, "minimal projection-compatible family defined")
        out.line("physical source", StatusMark.DEFER, "S(x) not physically identified")
        out.line("boundary conditions", StatusMark.OBLIGATION, "not derived")
    with out.counterexamples():
        out.line("S as physical source", StatusMark.FAIL, "not licensed")
        out.line("R_S as field equation", StatusMark.FAIL, "formal family only")
        out.line("b(S) as matter source", StatusMark.FAIL, "ordinary matter separation not derived")

    record_marker(ns, MARKER_ID, "formal minimal residual family")
    record_claim(ns, MARKER_ID, "g101_minimal_c1", GovernanceStatus.POLICY_RULE, "A minimal formal residual family R_S[f]=f-S yields the source vector formula b_k(S).")
    record_obligation(ns, "g101_minimal_o1", "Probe simple formal source vectors.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_candidate_source_vector_probe.py")

if __name__ == "__main__":
    main()
