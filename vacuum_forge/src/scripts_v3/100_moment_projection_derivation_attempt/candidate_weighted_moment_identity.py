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

DEPENDENCIES = [
    ("g100_problem", "100_moment_projection_derivation_attempt__candidate_projection_derivation_problem", "g100_problem"),
]
MARKER_ID = "g100_weighted_moment"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    s = sp.symbols("s", integer=True, positive=True)
    x = sp.symbols("x", nonnegative=True)
    integral_expr = sp.integrate(x**(2*s) * weight(x), (x, 0, 1))
    failures = []
    for n in range(1, 11):
        integral_n = sp.integrate(x**(2*n) * weight(x), (x, 0, 1))
        diff = sp.factor(beta_moment(n) - 2*integral_n)
        if diff != 0:
            failures.append((n, diff))

    header("Candidate Weighted Moment Identity")
    print("Check beta_moment(s)=2∫_0^1 x^(2s)(1-x^2)^4 dx.")
    print(f"Integral expression: {integral_expr}")
    print(f"beta_moment(s): {beta_moment(s)}")
    print(f"identity failures n=1..10: {failures}")

    with out.derived_results():
        out.line("identity failures", StatusMark.PASS if not failures else StatusMark.FAIL, str(failures))
        out.line("integral expression", StatusMark.INFO, str(integral_expr))
    with out.governance_assessments():
        out.line("weighted moment identity", StatusMark.PASS if not failures else StatusMark.FAIL, "verified in exact samples n=1..10")
        out.line("physical source", StatusMark.OBLIGATION, "identity is not residual/source derivation")
    with out.counterexamples():
        out.line("moment identity as field equation", StatusMark.FAIL, "identity alone has no dynamics/source")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[s],
        output=sp.Symbol("weighted_moment_identity_supported"),
        method="verify beta_moment(s)=2 weighted even moment with weight (1-x^2)^4 in exact samples",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="weighted_moment_identity",
        scope="moment projection origin",
    )
    record_claim(ns, MARKER_ID, "g100_weight_c1", GovernanceStatus.POLICY_RULE, "The beta_moment sequence is represented by weighted even moments with weight (1-x^2)^4.")
    record_obligation(ns, "g100_weight_o1", "Derive test/trial projection representation.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_test_trial_projection_derivation.py")

if __name__ == "__main__":
    main()
