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
    detB = sp.factor(B.det(method="bareiss"))
    if N == 1:
        alpha = B[0, 0]
        correction = sp.Integer(0)
        schur = sp.factor(alpha)
        previous_det = sp.Integer(1)
    else:
        C = B[:N-1, :N-1]
        u = B[:N-1, N-1]
        v_row = B[N-1, :N-1]
        alpha = B[N-1, N-1]
        x = C.LUsolve(u)
        correction = sp.factor((v_row * x)[0])
        schur = sp.factor(alpha - correction)
        previous_det = sp.factor(C.det(method="bareiss"))
    pivot = sp.factor(detB / previous_det)
    ratio = None if alpha == 0 else sp.factor(correction / alpha)
    gap = None if alpha == 0 else sp.factor(schur / alpha)
    return {
        "N": N,
        "alpha": sp.factor(alpha),
        "correction": sp.factor(correction),
        "schur": sp.factor(schur),
        "pivot": sp.factor(pivot),
        "ratio": ratio,
        "gap": gap,
        "alpha_sign": sp.sign(alpha),
        "correction_sign": sp.sign(correction),
        "schur_sign": sp.sign(schur),
        "pivot_sign": sp.sign(pivot),
        "ratio_sign": None if ratio is None else sp.sign(ratio),
        "gap_sign": None if gap is None else sp.sign(gap),
        "difference": sp.factor(schur - pivot),
    }

DEPENDENCIES = [
    ("g95_problem", "95_schur_ratio_bound_theorem_attempt__candidate_ratio_bound_problem", "g95_problem"),
]
MARKER_ID = "g95_ratio_equivalence"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    a, c = sp.symbols("alpha correction", positive=True)
    r = c / a
    gap = 1 - r
    schur = a - c

    header("Candidate Ratio Bound Equivalence")
    print("Assume post-transition alpha_N > 0.")
    print("Then 0 < correction/alpha < 1 is equivalent to:")
    print("  correction > 0")
    print("  alpha - correction > 0")
    print("The second condition is exactly schur_N > 0.")
    print(f"symbolic gap 1-r = {sp.factor(gap)}")
    print(f"schur/alpha = {sp.factor(schur/a)}")
    print(f"difference = {sp.simplify(gap - schur/a)}")

    # Verify equivalence against finite data N=11..25.
    rows = [schur_components(N) for N in range(11, 26)]
    failures = []
    for row in rows:
        ratio = row["ratio"]
        cond_ratio = (ratio > 0 and ratio < 1)
        cond_signs = (row["alpha"] > 0 and row["correction"] > 0 and row["schur"] > 0)
        if cond_ratio != cond_signs:
            failures.append((row["N"], cond_ratio, cond_signs))
    print(f"finite equivalence failures N=11..25: {failures}")

    with out.derived_results():
        out.line("gap-schur/alpha difference", StatusMark.PASS, str(sp.simplify(gap - schur/a)))
        out.line("finite equivalence failures", StatusMark.PASS if not failures else StatusMark.FAIL, str(failures))
    with out.governance_assessments():
        out.line("ratio equivalence", StatusMark.PASS, "post-transition ratio bound reduces to alpha/correction/schur signs under alpha>0")
        out.line("route audit", StatusMark.INFO, "ratio route is a repackaging unless gap positivity is easier to prove")
    with out.counterexamples():
        out.line("ratio theorem independent of Schur positivity", StatusMark.FAIL, "under alpha>0, ratio<1 is equivalent to schur>0 with correction>0")
        out.line("equivalence as all-order proof", StatusMark.FAIL, "logical reduction is not proof of signs")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[a, c],
        output=sp.simplify(gap - schur/a),
        method="symbolically compare 1-correction/alpha with schur/alpha",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="ratio_bound_equivalence",
        scope="Schur ratio-bound theorem branch",
    )
    record_claim(ns, MARKER_ID, "g95_equiv_c1", GovernanceStatus.POLICY_RULE, "For alpha>0, the Schur ratio bound is equivalent to correction>0 and schur>0.")
    record_obligation(ns, "g95_equiv_o1", "Extend post-transition exact evidence.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_post_transition_ratio_evidence_N11_to_N25.py")

if __name__ == "__main__":
    main()
