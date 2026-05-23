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
]
MARKER_ID = "g101_problem"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Residual Reconstruction Problem")
    print("Open Group 101: reconstruct a formal residual/source layer behind the projection matrix.")
    print("Imported Group 100 state:")
    print("  formal weighted projection derived")
    print("  weight/test/trial machinery identified")
    print("  physical residual/source/boundary not derived")
    print("  physical ledger assignment deferred")
    print()
    print("Question:")
    print("  Given A[k,j]=2∫psi_k phi_j w dx, what residual/source equation could produce A c=b?")

    with out.governance_assessments():
        out.line("group opened", StatusMark.PASS, "formal residual/source reconstruction attempt opened")
        out.line("real target", StatusMark.PASS, "derive projected profile identity and source-vector formula")
        out.line("scope", StatusMark.INFO, "formal reconstruction, not physical field equation")
    with out.counterexamples():
        out.line("R[f]=f-S as field equation", StatusMark.FAIL, "not physically derived")
        out.line("S as mass/source/burden", StatusMark.FAIL, "not licensed")
        out.line("boundary conditions", StatusMark.FAIL, "not derived")
    with out.unresolved_obligations():
        out.line("projected profile identity", StatusMark.OBLIGATION, "derive ΣA[k,j]c_j as projection of f_N")
        out.line("source vector formula", StatusMark.OBLIGATION, "derive b_k(S) formally")

    record_marker(ns, MARKER_ID, "Group 101 opening; residual/source reconstruction")
    record_claim(ns, MARKER_ID, "g101_problem_c1", GovernanceStatus.POLICY_RULE, "Group 101 attempts formal residual/source reconstruction behind the weighted projection matrix.")
    record_obligation(ns, "g101_problem_o1", "Derive projected profile identity.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_projected_profile_identity.py")

if __name__ == "__main__":
    main()
