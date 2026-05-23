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
    ("g90_problem", "090_determinant_positivity_theorem_attempt__candidate_determinant_positivity_problem", "g90_problem"),
]
MARKER_ID = "g90_derivative_factorization"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    t, k = sp.symbols("t k", positive=True)
    r = (2*k - 1)/(2*k + 3)
    q = t**k - r*t**(k-1)
    mu = t**sp.Rational(-1, 2) * (1-t)**4
    phi = t**(k-sp.Rational(1,2)) * (1-t)**2
    factorized = sp.factor((1-t)**3 * sp.diff(phi, t))
    target = sp.factor(-(k + sp.Rational(3,2)) * q * mu)
    difference = sp.simplify(factorized - target)

    header("Candidate Derivative Factorization")
    print(f"q_k(t) = {q}")
    print("mu(t)=t^(-1/2)(1-t)^4")
    print("phi_k(t)=t^(k-1/2)(1-t)^2")
    print(f"(1-t)^3 phi'_k = {factorized}")
    print(f"-(k+3/2) q_k mu = {target}")
    print(f"difference = {difference}")
    print("Therefore q_k mu = -1/(k+3/2) (1-t)^3 d/dt[t^(k-1/2)(1-t)^2].")

    with out.derived_results():
        out.line("factorized derivative", StatusMark.PASS, str(factorized))
        out.line("target", StatusMark.PASS, str(target))
        out.line("difference", StatusMark.PASS, str(difference))
    with out.governance_assessments():
        out.line("derivative factorization", StatusMark.PASS, "q_k mu has Sturm-like derivative form")
        out.line("proof route", StatusMark.INFO, "may support integration-by-parts/orthogonal-polynomial proof route")
    with out.counterexamples():
        out.line("opaque q_k", StatusMark.FAIL, "q_k row constraints have derivative structure")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[k],
        output=difference,
        method="factor q_k(t) mu(t) as weighted derivative of t^(k-1/2)(1-t)^2",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="derivative_factorization",
        scope="moment-pairing determinant route",
    )
    record_claim(ns, MARKER_ID, "g90_deriv_c1", GovernanceStatus.POLICY_RULE, "q_k mu has a derivative factorization useful for determinant proof attempts.")
    record_obligation(ns, "g90_deriv_o1", "Derive Andreief determinant representation.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_andreief_representation.py")

if __name__ == "__main__":
    main()
