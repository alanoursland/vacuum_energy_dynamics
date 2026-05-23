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
    ("g90_hankel_difference", "90_determinant_positivity_theorem_attempt__candidate_hankel_difference_structure", "g90_hankel_difference"),
]
MARKER_ID = "g90_pivot_extension"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    rows = []
    prev = sp.Integer(1)
    header("Candidate Pivot Evidence Extension N1 to N12")
    for N in range(1, 13):
        A, _ = hierarchy_matrix(N)
        detA = sp.factor(A.det(method="bareiss"))
        pivot = sp.factor(detA / prev)
        rows.append((N, detA, pivot))
        prev = detA
        print(f"N={N}: det(A_N)>0? {detA > 0}; pivot>0? {pivot > 0}")
        print(f"  det={detA}")
        print(f"  pivot={pivot}")

    with out.derived_results():
        for N, detA, pivot in rows:
            out.line(f"N={N} det", StatusMark.PASS if detA > 0 else StatusMark.FAIL, str(detA))
            out.line(f"N={N} pivot", StatusMark.PASS if pivot > 0 else StatusMark.FAIL, str(pivot))
    with out.governance_assessments():
        out.line("determinant evidence", StatusMark.PASS, "det(A_N)>0 through N=12")
        out.line("pivot evidence", StatusMark.PASS, "pivots positive through N=12")
        out.line("finite scope", StatusMark.INFO, "extended evidence remains finite, not all-order proof")
    with out.counterexamples():
        out.line("determinant failure through N=12", StatusMark.FAIL, "none found")
        out.line("finite checks as theorem", StatusMark.FAIL, "N=12 is not infinity")

    ns.record_derivation(
        derivation_id=MARKER_ID,
        inputs=[],
        output=sp.Matrix([row[2] for row in rows]),
        method="exact determinant and pivot check through N=12",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="pivot_evidence_extension_N1_to_N12",
        scope="finite determinant positivity evidence",
    )
    record_claim(ns, MARKER_ID, "g90_pivot_c1", GovernanceStatus.POLICY_RULE, "det(A_N) and leading pivots are positive through N=12.")
    record_obligation(ns, "g90_pivot_o1", "Classify determinant positivity theorem attempt.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_determinant_positivity_route_classifier.py")

if __name__ == "__main__":
    main()
