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
    denom = sp.prod(2*s + 2*m + 1 for m in range(5))
    return sp.Rational(768, 1) / denom

def hierarchy_matrix(N: int):
    A = sp.zeros(N, N)
    b = sp.zeros(N, 1)
    for k in range(1, N + 1):
        r = sp.Rational(2*k - 1, 2*k + 3)
        for j in range(1, N + 1):
            A[k-1, j-1] = beta_moment(k+j) - r*beta_moment(k+j-1)
        b[k-1, 0] = r*beta_moment(k-1) - beta_moment(k)
    return A, b

def det_sequence(max_n: int):
    rows = []
    prev = sp.Integer(1)
    for N in range(1, max_n + 1):
        A, _ = hierarchy_matrix(N)
        detA = sp.factor(A.det(method="bareiss"))
        pivot = sp.factor(detA / prev)
        rows.append((N, detA, sp.sign(detA), pivot, sp.sign(pivot)))
        prev = detA
    return rows

def expected_det_sign(N: int):
    if N <= 10:
        return sp.Integer(1)
    return sp.Integer(-1 if N % 2 else 1)

def expected_pivot_sign(N: int):
    if N <= 10:
        return sp.Integer(1)
    return sp.Integer(-1)

DEPENDENCIES = [
    ("g90_pivot_extension", "090_determinant_positivity_theorem_attempt__candidate_pivot_evidence_extension_N1_to_N12", "g90_pivot_extension"),
]
MARKER_ID = "g91_problem"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Sign Pattern Problem")
    print("Question: after positivity fails at N=11, does nonzero invertibility remain plausible?")
    print("Starting correction:")
    print("  det(A_N)>0 for all N is false as stated.")
    print("  det(A_N)!=0 for all N remains the relevant hierarchy theorem.")
    print("  determinant sign pattern must be audited.")
    print("  profile generation needs invertibility, not positivity.")
    print("  parent divergence identity remains unproven.")
    print("  recombination remains blocked.")

    with out.governance_assessments():
        out.line("group opened", StatusMark.PASS, "sign-pattern and nonzero audit opened")
        out.line("positivity status", StatusMark.FAIL, "positivity theorem already has N=11 counterexample")
        out.line("real target", StatusMark.PASS, "retarget determinant work to nonzero/sign pattern")
        out.line("scope", StatusMark.INFO, "finite sign audit, not all-order theorem")
    with out.counterexamples():
        out.line("revive positivity", StatusMark.FAIL, "positivity must not be carried forward after N=11")
        out.line("negative determinant as failure", StatusMark.FAIL, "negative determinant is still invertible if nonzero")
        out.line("parent jump", StatusMark.FAIL, "determinant audit cannot write parent equation")
    with out.unresolved_obligations():
        out.line("N=11 verification", StatusMark.OBLIGATION, "verify sign flip directly")
        out.line("sign sequence", StatusMark.OBLIGATION, "compute determinant and pivot signs across larger range")

    record_marker(ns, MARKER_ID, "Group 91 opening; determinant sign-pattern and nonzero audit")
    record_claim(ns, MARKER_ID, "g91_problem_c1", GovernanceStatus.POLICY_RULE, "Group 91 retargets determinant work from positivity to nonzero/sign-pattern analysis.")
    record_obligation(ns, "g91_problem_o1", "Verify N=11 positivity counterexample.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_n11_counterexample_verification.py")

if __name__ == "__main__":
    main()
