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
    ("g100_weighted_moment", "100_moment_projection_derivation_attempt__candidate_weighted_moment_identity", "g100_weighted_moment"),
]
MARKER_ID = "g100_projection_derivation"

def integral_projection_entry(k, j):
    x = sp.symbols("x", nonnegative=True)
    return sp.factor(2 * sp.integrate(test_psi(k, x) * trial_phi(j, x) * weight(x), (x, 0, 1)))

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    failures = []
    for k in range(1, 8):
        for j in range(1, 8):
            proj = integral_projection_entry(k, j)
            target = hierarchy_entry(k, j)
            diff = sp.factor(proj - target)
            if diff != 0:
                failures.append((k, j, diff))

    header("Candidate Test/Trial Projection Derivation")
    print("Derive A[k,j] = 2∫ psi_k(x) phi_j(x) (1-x^2)^4 dx.")
    print("phi_j(x)=x^(2j)")
    print("psi_k(x)=x^(2k)-((2k-1)/(2k+3))x^(2k-2)")
    print(f"projection equality failures for k,j=1..7: {failures}")

    with out.derived_results():
        out.line("projection equality failures", StatusMark.PASS if not failures else StatusMark.FAIL, str(failures))
    with out.governance_assessments():
        out.line("formal weighted projection", StatusMark.PASS if not failures else StatusMark.FAIL, "A[k,j] derived from explicit weight/test/trial functions in exact samples")
        out.line("test functions", StatusMark.PASS, "psi_k identified")
        out.line("trial functions", StatusMark.PASS, "phi_j identified")
        out.line("physical residual", StatusMark.OBLIGATION, "not derived")
    with out.counterexamples():
        out.line("projection as physical derivation", StatusMark.FAIL, "residual/source/boundary still missing")
        out.line("projection as Hessian", StatusMark.FAIL, "test/trial pairing is not symmetric Hessian by itself")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=sp.Symbol("formal_weighted_projection_derived"),
        method="derive and verify A[k,j] from explicit weighted test/trial projection in exact samples",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="formal_weighted_projection_derivation",
        scope="moment projection origin",
    )
    record_claim(ns, MARKER_ID, "g100_proj_c1", GovernanceStatus.POLICY_RULE, "A_N has a formal weighted projection representation using identified test and trial functions.")
    record_obligation(ns, "g100_proj_o1", "Inventory row test function structure.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_row_test_function_structure.py")

if __name__ == "__main__":
    main()
