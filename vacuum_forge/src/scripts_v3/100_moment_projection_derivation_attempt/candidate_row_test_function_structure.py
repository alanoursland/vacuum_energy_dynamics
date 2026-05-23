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
    ("g100_projection_derivation", "100_moment_projection_derivation_attempt__candidate_test_trial_projection_derivation", "g100_projection_derivation"),
]
MARKER_ID = "g100_row_structure"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    k = sp.symbols("k", integer=True, positive=True)
    r = row_ratio(k)
    root = sp.sqrt(r)
    failures = []
    sample = []
    for kk in range(1, 16):
        rr = row_ratio(kk)
        ok = (rr > 0 and rr < 1)
        sample.append((kk, rr, sp.sqrt(rr), ok))
        if not ok:
            failures.append((kk, rr))

    header("Candidate Row Test Function Structure")
    print("psi_k(x)=x^(2k-2)[x^2-r_k]")
    print("r_k=(2k-1)/(2k+3)")
    print(f"r_k - 1 = {sp.factor(r-1)}")
    print(f"root x_k=sqrt(r_k) = {root}")
    print(f"r_k range failures for k=1..15: {failures}")
    for item in sample[:8]:
        print(f"  k={item[0]}: r_k={item[1]}, root={item[2]}, in_(0,1)={item[3]}")

    with out.derived_results():
        out.line("r_k range failures", StatusMark.PASS if not failures else StatusMark.FAIL, str(failures))
        out.line("r_k - 1", StatusMark.INFO, str(sp.factor(r-1)))
    with out.governance_assessments():
        out.line("row test sign-change", StatusMark.PASS if not failures else StatusMark.FAIL, "each tested psi_k has one interior sign-change root")
        out.line("operator clue", StatusMark.INFO, "row tests are sign-changing projection tests, not positive Gram functions")
    with out.counterexamples():
        out.line("positive test basis", StatusMark.FAIL, "psi_k is sign-changing on [0,1]")
        out.line("boundary condition derived", StatusMark.FAIL, "root is algebraic sign-change, not physical boundary")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[k],
        output=root,
        method="inventory row test function sign-change/root structure",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="row_test_function_structure",
        scope="moment projection origin",
    )
    record_claim(ns, MARKER_ID, "g100_row_c1", GovernanceStatus.POLICY_RULE, "The projection test functions are sign-changing row functions with interior roots in the tested range.")
    record_obligation(ns, "g100_row_o1", "Classify projection-origin status.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_projection_origin_classifier.py")

if __name__ == "__main__":
    main()
