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
    ("g099_summary", "099_hierarchy_source_origin_audit__candidate_group_099_status_summary", "g099_summary"),
    ("g100_problem", "100_moment_projection_derivation_attempt__candidate_projection_derivation_problem", "g100_problem"),
    ("g100_weighted_moment", "100_moment_projection_derivation_attempt__candidate_weighted_moment_identity", "g100_weighted_moment"),
    ("g100_projection_derivation", "100_moment_projection_derivation_attempt__candidate_test_trial_projection_derivation", "g100_projection_derivation"),
    ("g100_row_structure", "100_moment_projection_derivation_attempt__candidate_row_test_function_structure", "g100_row_structure"),
    ("g100_classifier", "100_moment_projection_derivation_attempt__candidate_projection_origin_classifier", "g100_classifier"),
]
MARKER_ID = "g100_summary"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    header("Candidate Group 100 Status Summary")
    print("Group 100 derives A_N as a formal weighted projection matrix.")
    print("Stable result:")
    print("  weight function identified: w(x)=(1-x^2)^4")
    print("  trial functions identified: phi_j=x^(2j)")
    print("  test functions identified: psi_k=x^(2k)-((2k-1)/(2k+3))x^(2k-2)")
    print("  formal projection derived: A[k,j]=2∫psi_k phi_j w dx")
    print("  row test functions are sign-changing with interior roots")
    print("  physical residual/source/boundary not derived")
    print("  physical ledger assignment deferred")
    print("  hierarchy remains auxiliary admissibility candidate")
    print("  parent equation not ready; recombination blocked")

    with out.governance_assessments():
        out.line("formal projection", StatusMark.PASS, "derived")
        out.line("weight/test/trial machinery", StatusMark.PASS, "identified")
        out.line("physical origin", StatusMark.DEFER, "residual/source/boundary not derived")
        out.line("hierarchy role", StatusMark.PASS, "auxiliary admissibility candidate retained")
    with out.counterexamples():
        out.line("projection as field equation", StatusMark.FAIL, "not licensed")
        out.line("projection as J_curv/H_exch/total burden", StatusMark.FAIL, "not licensed")
        out.line("projection as Hessian", StatusMark.FAIL, "not licensed by non-symmetric sign-changing test/trial pairing")
    with out.unresolved_obligations():
        out.line("residual reconstruction", StatusMark.OBLIGATION, "derive R[f], source vector, and boundary conditions")
        out.line("admissibility theorem", StatusMark.OBLIGATION, "continue determinant/numerator proof if desired")
        out.line("ledger assignment", StatusMark.OBLIGATION, "deferred until physical residual/source origin exists")

    print("\nRecommended next routes:")
    print("  101_residual_source_reconstruction_attempt")
    print("  101_difference_numerator_factorization_attempt")
    print("  101_burden_functional_minimum_requirements")

    record_marker(ns, MARKER_ID, "Group 100 summary; formal moment projection derivation")
    record_claim(ns, MARKER_ID, "g100_summary_c1", GovernanceStatus.POLICY_RULE, "Group 100 derives A_N as a formal weighted projection matrix.")
    record_claim(ns, MARKER_ID, "g100_summary_c2", GovernanceStatus.POLICY_RULE, "The hierarchy remains auxiliary admissibility infrastructure until residual/source/boundary physics is derived.")
    record_obligation(ns, "g100_summary_o1", "Attempt residual/source reconstruction or numerator factorization next.")
    record_obligation(ns, "g100_summary_o2", "Parent divergence identity remains unproven.")
    ns.write_run_metadata()

if __name__ == "__main__":
    main()
