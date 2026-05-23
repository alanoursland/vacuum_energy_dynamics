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
    ("g101_minimal_residual", "101_residual_source_reconstruction_attempt__candidate_minimal_residual_family", "g101_minimal_residual"),
    ("g101_source_probe", "101_residual_source_reconstruction_attempt__candidate_candidate_source_vector_probe", "g101_source_probe"),
]
MARKER_ID = "g101_classifier"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    classifications = [
        ("PROJECTED_PROFILE_IDENTITY_DERIVED", "stable", "A maps coefficients to weighted projections of f_N"),
        ("MINIMAL_RESIDUAL_FAMILY_FORMAL", "stable", "R_S[f]=f-S gives A c=b(S)"),
        ("SOURCE_VECTOR_FORMULA_DERIVED", "stable", "b_k(S)=2∫psi_k S w dx"),
        ("SIMPLE_SOURCE_PROBES_COMPLETED", "stable", "formal b_k computed for simple S"),
        ("PHYSICAL_SOURCE_NOT_IDENTIFIED", "stable", "no S(x) selected by physics"),
        ("BOUNDARY_CONDITIONS_NOT_DERIVED", "stable", "no domain/boundary physical problem"),
        ("PHYSICAL_LEDGER_ASSIGNMENT_DEFERRED", "stable", "not J_curv/H_exch/total burden"),
        ("HIERARCHY_REMAINS_AUXILIARY_ADMISSIBILITY_CANDIDATE", "stable", "formal residual family only"),
        ("PARENT_EQUATION_NOT_READY", "stable", "no H insertion/source law"),
        ("RECOMBINATION_BLOCKED", "stable", "no recombination license"),
    ]

    header("Candidate Residual Origin Classifier")
    for name, status, reason in classifications:
        print(f"{name}: {status}; {reason}")

    with out.governance_assessments():
        out.line("projected profile identity", StatusMark.PASS, "derived")
        out.line("minimal residual family", StatusMark.PASS, "formal")
        out.line("source vector formula", StatusMark.PASS, "derived")
        out.line("physical source", StatusMark.DEFER, "not identified")
        out.line("boundary conditions", StatusMark.OBLIGATION, "not derived")
    with out.counterexamples():
        out.line("minimal residual as physics", StatusMark.FAIL, "formal only")
        out.line("simple source as matter", StatusMark.FAIL, "not licensed")
        out.line("ledger assignment", StatusMark.FAIL, "not licensed")
    with out.unresolved_obligations():
        out.line("source selection", StatusMark.OBLIGATION, "derive S(x) from physics or boundary data")
        out.line("boundary origin", StatusMark.OBLIGATION, "derive boundary/domain problem")
        out.line("functional origin", StatusMark.OBLIGATION, "connect residual to burden functional if possible")

    record_marker(ns, MARKER_ID, "residual origin classifier")
    record_claim(ns, MARKER_ID, "g101_class_c1", GovernanceStatus.POLICY_RULE, "The projected profile identity and formal source-vector family are derived, but physical source selection remains open.")
    record_claim(ns, MARKER_ID, "g101_class_c2", GovernanceStatus.POLICY_RULE, "The hierarchy remains auxiliary admissibility infrastructure pending source/boundary/functional origin.")
    record_obligation(ns, "g101_class_o1", "Attempt source-vector structure selection or boundary origin next.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_group_101_status_summary.py")

if __name__ == "__main__":
    main()
