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
    ("g100_projection_derivation", "100_moment_projection_derivation_attempt__candidate_test_trial_projection_derivation", "g100_projection_derivation"),
    ("g100_row_structure", "100_moment_projection_derivation_attempt__candidate_row_test_function_structure", "g100_row_structure"),
]
MARKER_ID = "g100_classifier"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    classifications = [
        ("WEIGHT_FUNCTION_IDENTIFIED", "stable", "w(x)=(1-x^2)^4"),
        ("TRIAL_FUNCTIONS_IDENTIFIED", "stable", "phi_j=x^(2j)"),
        ("TEST_FUNCTIONS_IDENTIFIED", "stable", "psi_k=x^(2k)-r_k x^(2k-2)"),
        ("FORMAL_WEIGHTED_PROJECTION_DERIVED", "stable", "A[k,j]=2∫psi_k phi_j w dx"),
        ("ROW_TESTS_SIGN_CHANGING", "stable", "psi_k has interior root sqrt((2k-1)/(2k+3))"),
        ("PHYSICAL_RESIDUAL_NOT_DERIVED", "stable", "no R[f] equation"),
        ("SOURCE_VECTOR_NOT_DERIVED", "stable", "no source/boundary RHS"),
        ("BOUNDARY_CONDITIONS_NOT_DERIVED", "stable", "no physical boundary problem"),
        ("PHYSICAL_LEDGER_ASSIGNMENT_DEFERRED", "stable", "not J_curv/H_exch/total burden"),
        ("HIERARCHY_REMAINS_AUXILIARY_ADMISSIBILITY_CANDIDATE", "stable", "formal origin but not physical origin"),
    ]

    header("Candidate Projection Origin Classifier")
    for name, status, reason in classifications:
        print(f"{name}: {status}; {reason}")

    with out.governance_assessments():
        out.line("formal projection", StatusMark.PASS, "derived")
        out.line("projection machinery", StatusMark.PASS, "weight/test/trial functions identified")
        out.line("physical origin", StatusMark.DEFER, "residual/source/boundary still missing")
        out.line("ledger assignment", StatusMark.DEFER, "not licensed")
    with out.counterexamples():
        out.line("projection as field equation", StatusMark.FAIL, "residual/source/boundary not derived")
        out.line("projection as physical ledger", StatusMark.FAIL, "not assigned")
        out.line("projection as Hessian", StatusMark.FAIL, "test/trial pairing is non-symmetric and sign-changing")
    with out.unresolved_obligations():
        out.line("residual reconstruction", StatusMark.OBLIGATION, "derive candidate R[f] whose projection gives A_N")
        out.line("source vector", StatusMark.OBLIGATION, "derive RHS/source terms")
        out.line("boundary conditions", StatusMark.OBLIGATION, "derive domain and boundary conditions")

    record_marker(ns, MARKER_ID, "projection origin classifier")
    record_claim(ns, MARKER_ID, "g100_class_c1", GovernanceStatus.POLICY_RULE, "A_N has a formal weighted projection representation with identified weight, test functions, and trial functions.")
    record_claim(ns, MARKER_ID, "g100_class_c2", GovernanceStatus.POLICY_RULE, "The physical residual/source/boundary problem remains underived; hierarchy remains auxiliary admissibility infrastructure.")
    record_obligation(ns, "g100_class_o1", "Attempt residual/source reconstruction next.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_group_100_status_summary.py")

if __name__ == "__main__":
    main()
