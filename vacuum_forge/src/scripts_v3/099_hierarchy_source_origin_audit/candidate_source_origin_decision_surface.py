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
    return sp.factor(sp.Rational(768, 1) / denom)

def hierarchy_entry(k, j):
    k = sp.sympify(k)
    j = sp.sympify(j)
    return sp.factor(beta_moment(k+j) - ((2*k - 1) / (2*k + 3)) * beta_moment(k+j-1))

def hierarchy_matrix(N: int):
    A = sp.zeros(N, N)
    for k in range(1, N + 1):
        for j in range(1, N + 1):
            A[k-1, j-1] = hierarchy_entry(k, j)
    return A

DEPENDENCIES = [
    ("g099_formula_inventory", "099_hierarchy_source_origin_audit__candidate_hierarchy_formula_structure_inventory", "g099_formula_inventory"),
    ("g099_origin_matrix", "099_hierarchy_source_origin_audit__candidate_origin_route_evidence_matrix", "g099_origin_matrix"),
    ("g099_moment_probe", "099_hierarchy_source_origin_audit__candidate_moment_projection_plausibility_probe", "g099_moment_probe"),
]
MARKER_ID = "g099_decision_surface"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    classifications = [
        ("FORMULA_IS_MOMENT_LIKE", "stable", "A_N entries depend on shifted k+j moments"),
        ("BETA_MOMENT_INTEGRAL_STRUCTURE_SUPPORTED", "stable", "beta_moment admits beta-type moment representation"),
        ("MOMENT_PROJECTION_ORIGIN_PLAUSIBLE_BUT_UNDERDERIVED", "stable", "residual/basis/source/boundary missing"),
        ("VARIATIONAL_HESSIAN_ORIGIN_NOT_LICENSED", "stable", "functional and Hessian/symmetry derivation missing"),
        ("INTERFACE_ORIGIN_NOT_LICENSED", "stable", "interface domain/profile/matching derivation missing"),
        ("EXCHANGE_ORIGIN_NOT_LICENSED", "stable", "exchange current/divergence/source separation missing"),
        ("TOTAL_BURDEN_ORIGIN_NOT_LICENSED", "stable", "combined burden functional and subledgers missing"),
        ("SOURCE_ORIGIN_REMAINS_OPEN", "stable", "no physical derivation of A_N yet"),
        ("HIERARCHY_REMAINS_AUXILIARY_ADMISSIBILITY_CANDIDATE", "stable", "physical upgrade deferred"),
        ("PARENT_EQUATION_NOT_READY", "stable", "no H insertion or source law"),
        ("RECOMBINATION_BLOCKED", "stable", "no recombination license"),
    ]

    header("Candidate Source Origin Decision Surface")
    for name, status, reason in classifications:
        print(f"{name}: {status}; {reason}")

    with out.governance_assessments():
        out.line("moment structure", StatusMark.PASS, "supported")
        out.line("moment origin", StatusMark.INFO, "plausible but underderived")
        out.line("physical origin", StatusMark.DEFER, "not derived")
        out.line("hierarchy role", StatusMark.PASS, "auxiliary admissibility candidate retained")
        out.line("parent equation", StatusMark.OBLIGATION, "not ready")
    with out.counterexamples():
        out.line("A_N as physical functional", StatusMark.FAIL, "not licensed")
        out.line("A_N as exchange equation", StatusMark.FAIL, "not licensed")
        out.line("A_N as total burden", StatusMark.FAIL, "not licensed")
        out.line("parent equation", StatusMark.FAIL, "not licensed")
    with out.unresolved_obligations():
        out.line("projection derivation", StatusMark.OBLIGATION, "derive continuum residual, basis/test functions, source vector, and boundary conditions")
        out.line("functional derivation", StatusMark.OBLIGATION, "derive whether A_N is a Hessian/Gram matrix of a burden functional")
        out.line("ledger assignment", StatusMark.OBLIGATION, "assign physical ledger only after source origin")

    record_marker(ns, MARKER_ID, "source origin decision surface")
    record_claim(ns, MARKER_ID, "g099_decision_c1", GovernanceStatus.POLICY_RULE, "A_N has moment-like structure and a plausible projection origin, but physical source origin remains underderived.")
    record_claim(ns, MARKER_ID, "g099_decision_c2", GovernanceStatus.POLICY_RULE, "The hierarchy remains an auxiliary admissibility candidate pending source/functional derivation.")
    record_obligation(ns, "g099_decision_o1", "Attempt moment projection derivation or return to numerator factorization.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_group_099_status_summary.py")

if __name__ == "__main__":
    main()
