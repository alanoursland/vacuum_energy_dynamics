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
    for k in range(1, N + 1):
        r = sp.Rational(2*k - 1, 2*k + 3)
        for j in range(1, N + 1):
            A[k-1, j-1] = beta_moment(k+j) - r*beta_moment(k+j-1)
    return A

def row_epsilon(k: int):
    return sp.Integer(1 if k <= 10 else -1)

def row_signed_matrix(N: int):
    A = hierarchy_matrix(N)
    B = sp.zeros(N, N)
    for k in range(1, N + 1):
        eps = row_epsilon(k)
        for j in range(1, N + 1):
            B[k-1, j-1] = eps * A[k-1, j-1]
    return B

def schur_components(N: int):
    B = row_signed_matrix(N)
    if N == 1:
        alpha = B[0, 0]
        correction = sp.Integer(0)
        schur = sp.factor(alpha)
    else:
        C = B[:N-1, :N-1]
        u = B[:N-1, N-1]
        v_row = B[N-1, :N-1]
        alpha = B[N-1, N-1]
        x = C.LUsolve(u)
        correction = sp.factor((v_row * x)[0])
        schur = sp.factor(alpha - correction)
    ratio = sp.factor(correction / alpha)
    gap = sp.factor(schur / alpha)
    return {"N": N, "alpha": alpha, "correction": correction, "schur": schur, "ratio": ratio, "gap": gap}

def rows(start=11, stop=36):
    return {N: schur_components(N) for N in range(start, stop + 1)}

def rational_sign_parts(expr):
    expr = sp.factor(expr)
    num, den = sp.fraction(expr)
    return sp.factor(num), sp.factor(den), sp.sign(num), sp.sign(den), sp.sign(expr)

DEPENDENCIES = [
    ("g96_summary", "096_post_transition_schur_gap_structure__candidate_group_96_status_summary", "g96_summary"),
]
MARKER_ID = "g97_problem"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Candidate Parity Gap Theorem Problem")
    print("Open Group 97: reduce parity gap monotonicity/interlacing to exact positive differences.")
    print("Imported Group 96 state:")
    print("  post-transition gap positive and ratio bound supported through N=30")
    print("  parity gap monotonicity supported through N=30")
    print("  parity ratio monotonicity supported through N=30")
    print("  gap interlacing supported through N=30")
    print("  simple one-step monotonicity blocked")
    print("  all-order parity gap theorem open")
    print("  parent divergence unproven; recombination blocked")

    with out.governance_assessments():
        out.line("group opened", StatusMark.PASS, "parity gap theorem attempt opened")
        out.line("real target", StatusMark.PASS, "test exact positive branch/interlacing differences")
        out.line("scope", StatusMark.INFO, "finite exact difference tests, not all-order proof")
    with out.counterexamples():
        out.line("finite parity as theorem", StatusMark.FAIL, "Group 96 evidence is finite")
        out.line("simple one-step monotonicity", StatusMark.FAIL, "already blocked")
        out.line("parent jump", StatusMark.FAIL, "gap difference work cannot write parent equation")
    with out.unresolved_obligations():
        out.line("branch differences", StatusMark.OBLIGATION, "test gap_N-gap_N+2 and ratio_N+2-ratio_N")
        out.line("interlacing differences", StatusMark.OBLIGATION, "test even peak difference positivity")

    record_marker(ns, MARKER_ID, "Group 97 opening; parity gap theorem attempt")
    record_claim(ns, MARKER_ID, "g97_problem_c1", GovernanceStatus.POLICY_RULE, "Group 97 attempts to reduce parity gap structure to exact positive difference conditions.")
    record_obligation(ns, "g97_problem_o1", "Test exact branch difference signs.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_branch_difference_signs.py")

if __name__ == "__main__":
    main()
