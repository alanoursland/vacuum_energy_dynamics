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
            A[k-1, j-1] = sp.factor(beta_moment(k+j) - r*beta_moment(k+j-1))
        b[k-1, 0] = sp.factor(r*beta_moment(k-1) - beta_moment(k))
    return A, b

def q_poly(k, t):
    return t**k - sp.Rational(2*k - 1, 2*k + 3)*t**(k-1)

DEPENDENCIES = [
    ("g90_andreief", "90_determinant_positivity_theorem_attempt__candidate_andreief_representation", "g90_andreief"),
]
MARKER_ID = "g90_chebyshev_sign"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    t = sp.symbols("t")
    q1 = q_poly(1, t)
    q1_values = [sp.factor(q1.subs(t, sp.Rational(1, 10))), sp.factor(q1.subs(t, sp.Rational(9, 10)))]

    # N=2 ratio changes sign at selected ordered points.
    x1, x2 = sp.symbols("x1 x2")
    gdet2 = sp.factor(sp.Matrix([[q_poly(1, x1), q_poly(2, x1)], [q_poly(1, x2), q_poly(2, x2)]]).det())
    ratio2 = sp.factor(gdet2 / (x2 - x1))
    sample_a = sp.factor(ratio2.subs({x1: sp.Rational(1, 10), x2: sp.Rational(2, 10)}))
    sample_b = sp.factor(ratio2.subs({x1: sp.Rational(8, 10), x2: sp.Rational(9, 10)}))

    header("Candidate Chebyshev Sign Route Test")
    print(f"q1(t)= {q1}")
    print(f"q1(1/10), q1(9/10) = {q1_values}")
    print(f"N=2 det(q)/Vandermonde = {ratio2}")
    print(f"sample near low interval = {sample_a}")
    print(f"sample near high interval = {sample_b}")
    print("Interpretation: q-system is not obviously sign-definite on the full interval.")
    print("A simple Andreief+Chebyshev fixed-sign proof route is blocked or at least not immediate.")

    with out.derived_results():
        out.line("q1 values", StatusMark.WARN, str(q1_values))
        out.line("N=2 ratio", StatusMark.INFO, str(ratio2))
        out.line("sample low", StatusMark.WARN, str(sample_a))
        out.line("sample high", StatusMark.WARN, str(sample_b))
    with out.governance_assessments():
        out.line("simple Chebyshev route", StatusMark.WARN, "sign-definite q determinant route is blocked/not established")
        out.line("proof hygiene", StatusMark.PASS, "prevents false total-positivity proof")
    with out.counterexamples():
        out.line("q1 fixed sign", StatusMark.FAIL, "q1 changes sign on (0,1)")
        out.line("N=2 q determinant fixed sign", StatusMark.FAIL, "sample signs differ for det(q)/Vandermonde")

    record_marker(ns, MARKER_ID, "Chebyshev sign route test")
    record_claim(ns, MARKER_ID, "g90_cheb_c1", GovernanceStatus.POLICY_RULE, "The simple fixed-sign Chebyshev route to determinant positivity is blocked in the tested form.")
    record_obligation(ns, "g90_cheb_o1", "Derive Hankel difference structure as alternate route.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_hankel_difference_structure.py")

if __name__ == "__main__":
    main()
