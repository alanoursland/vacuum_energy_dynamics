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
    return {
        "N": N,
        "alpha": sp.factor(alpha),
        "correction": sp.factor(correction),
        "schur": sp.factor(schur),
        "pivot": sp.factor(pivot),
        "difference": sp.factor(schur - pivot),
        "alpha_sign": sp.sign(alpha),
        "correction_sign": sp.sign(correction),
        "schur_sign": sp.sign(schur),
        "pivot_sign": sp.sign(pivot),
    }

DEPENDENCIES = [
    ("g94_schur_identity", "94_schur_complement_positivity_attempt__candidate_schur_identity_repair", "g94_schur_identity"),
]
MARKER_ID = "g94_schur_balance"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    rows = [schur_components(N) for N in range(1, 16)]
    failures = []
    header("Candidate Schur Term Balance Regimes")
    print("Analyze schur_N = alpha_N - correction_N.")
    for r in rows:
        N = r["N"]
        alpha = r["alpha"]
        corr = r["correction"]
        if N == 1:
            expected = (r["correction"] == 0 and r["schur_sign"] > 0)
            regime = "base"
        elif N <= 10:
            expected = (r["alpha_sign"] < 0 and r["correction_sign"] < 0 and abs(corr) > abs(alpha) and r["schur_sign"] > 0)
            regime = "negative-alpha negative-correction, correction dominates"
        else:
            expected = (r["alpha_sign"] > 0 and r["correction_sign"] > 0 and alpha > corr and r["schur_sign"] > 0)
            regime = "positive-alpha positive-correction, alpha dominates"
        if not expected:
            failures.append((N, r["alpha_sign"], r["correction_sign"], r["schur_sign"]))
        print(f"N={N}: regime={regime}; alpha_sign={r['alpha_sign']}; correction_sign={r['correction_sign']}; schur_sign={r['schur_sign']}")

    with out.derived_results():
        out.line("regime failures", StatusMark.PASS if not failures else StatusMark.WARN, str(failures))
    with out.governance_assessments():
        out.line("two-regime balance", StatusMark.PASS if not failures else StatusMark.WARN, "supported through N=15")
        out.line("theorem target", StatusMark.INFO, "prove finite observed dominance rules all-order")
    with out.counterexamples():
        out.line("Schur positivity unexplained", StatusMark.FAIL, "finite term-balance pattern identified")
        out.line("finite balance as theorem", StatusMark.FAIL, "N=15 is finite")

    record_marker(ns, MARKER_ID, "Schur alpha/correction two-regime balance")
    record_claim(ns, MARKER_ID, "g94_balance_c1", GovernanceStatus.POLICY_RULE, "Schur positivity has a two-regime alpha/correction dominance pattern through N=15.")
    record_obligation(ns, "g94_balance_o1", "Probe ratio bounds for Schur balance.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_schur_ratio_bound_probe.py")

if __name__ == "__main__":
    main()
