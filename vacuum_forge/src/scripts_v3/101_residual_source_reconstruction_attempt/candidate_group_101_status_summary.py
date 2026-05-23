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
    ("g100_summary", "100_moment_projection_derivation_attempt__candidate_group_100_status_summary", "g100_summary"),
    ("g101_problem", "101_residual_source_reconstruction_attempt__candidate_residual_reconstruction_problem", "g101_problem"),
    ("g101_projected_profile", "101_residual_source_reconstruction_attempt__candidate_projected_profile_identity", "g101_projected_profile"),
    ("g101_minimal_residual", "101_residual_source_reconstruction_attempt__candidate_minimal_residual_family", "g101_minimal_residual"),
    ("g101_source_probe", "101_residual_source_reconstruction_attempt__candidate_candidate_source_vector_probe", "g101_source_probe"),
    ("g101_classifier", "101_residual_source_reconstruction_attempt__candidate_residual_origin_classifier", "g101_classifier"),
]
MARKER_ID = "g101_summary"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Group 101 Status Summary")
    print("Group 101 reconstructs a formal residual/source layer behind the projection matrix.")
    print("Stable result:")
    print("  projected profile identity derived")
    print("  minimal formal residual family R_S[f]=f-S defined")
    print("  source-vector formula b_k(S)=2∫psi_k S w dx derived")
    print("  simple formal source probes completed")
    print("  physical source not identified")
    print("  boundary conditions not derived")
    print("  physical ledger assignment deferred")
    print("  hierarchy remains auxiliary admissibility candidate")
    print("  parent equation not ready")
    print("  recombination blocked")

    with out.governance_assessments():
        out.line("projected profile identity", StatusMark.PASS, "derived")
        out.line("minimal residual family", StatusMark.PASS, "formal")
        out.line("source-vector formula", StatusMark.PASS, "derived")
        out.line("physical source", StatusMark.DEFER, "not identified")
        out.line("hierarchy role", StatusMark.PASS, "auxiliary admissibility candidate retained")
    with out.counterexamples():
        out.line("R_S as field equation", StatusMark.FAIL, "not licensed")
        out.line("S as physical source", StatusMark.FAIL, "not licensed")
        out.line("projection as ledger assignment", StatusMark.FAIL, "not licensed")
    with out.unresolved_obligations():
        out.line("source selection", StatusMark.OBLIGATION, "derive S(x) physically")
        out.line("boundary/domain origin", StatusMark.OBLIGATION, "derive boundary conditions")
        out.line("admissibility theorem", StatusMark.OBLIGATION, "continue determinant/numerator route if desired")

    print("\nRecommended next routes:")
    print("  102_source_vector_structure_selection")
    print("  102_boundary_condition_origin_attempt")
    print("  102_difference_numerator_factorization_attempt")

    record_marker(ns, MARKER_ID, "Group 101 summary; residual/source reconstruction attempt")
    record_claim(ns, MARKER_ID, "g101_summary_c1", GovernanceStatus.POLICY_RULE, "Group 101 derives the formal projected-profile identity and source-vector family.")
    record_claim(ns, MARKER_ID, "g101_summary_c2", GovernanceStatus.POLICY_RULE, "Physical source, boundary conditions, and ledger assignment remain open.")
    record_obligation(ns, "g101_summary_o1", "Attempt source-vector structure selection or boundary condition origin next.")
    record_obligation(ns, "g101_summary_o2", "Parent divergence identity remains unproven.")
    ns.write_run_metadata()

if __name__ == "__main__":
    main()
