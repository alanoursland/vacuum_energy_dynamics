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

def hierarchy_solution(N: int):
    y = sp.symbols("y")
    coeffs = sp.symbols("a1:" + str(N + 1))
    f = (1 - y**2)**3
    w = (1 - y**2)**2
    P = 1 + sum(coeffs[k-1] * y**(2*k) for k in range(1, N + 1))
    J = sp.simplify(w * sp.diff(f * P, y))
    rho = sp.factor(sp.diff(J, y))
    constraints = [
        sp.factor(sp.integrate(sp.expand(y**(2*k) * rho), (y, -1, 1)))
        for k in range(1, N + 1)
    ]
    sol = sp.solve([sp.Eq(m, 0) for m in constraints], coeffs, dict=True)
    return y, coeffs, P, J, rho, constraints, sol

DEPENDENCIES = [
    ("g87_operator", "087_moment_hierarchy_closure_test__candidate_general_even_shape_operator", "g87_operator"),
    ("g87_profiles", "087_moment_hierarchy_closure_test__candidate_hierarchy_profiles_N1_to_N4", "g87_profiles"),
    ("g87_rank_uniqueness", "087_moment_hierarchy_closure_test__candidate_constraint_rank_uniqueness_test", "g87_rank_uniqueness"),
    ("g87_weighted_inheritance", "087_moment_hierarchy_closure_test__candidate_weighted_block_inheritance_theorem", "g87_weighted_inheritance"),
    ("g87_next_obstruction", "087_moment_hierarchy_closure_test__candidate_next_moment_obstruction_test", "g87_next_obstruction"),
]
MARKER_ID = "g87_route_classifier"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    classifications = [
        ("FINITE_MOMENT_HIERARCHY_SUPPORTED_N1_TO_N4", "stable", "profiles found for N=1..4"),
        ("UNIQUE_PROFILE_PER_ORDER_N1_TO_N4", "stable", "constraint matrices full-rank through N=4"),
        ("WEIGHTED_BLOCK_INHERITANCE_DERIVED", "stable", "quadratic measure inherits suppression block"),
        ("NEXT_MOMENT_OBSTRUCTION_PERSISTS", "stable", "M(2N+2) nonzero in tested cases"),
        ("ALL_ORDER_CLOSURE_NOT_PROVEN", "stable", "finite pattern only"),
        ("LOCAL_RHO_NONZERO_REMAINS", "stable", "rho(0) nonzero in tested profiles"),
        ("PHYSICAL_COVARIANT_ORIGIN_OPEN", "stable", "reduced hierarchy not physically/covariantly derived"),
        ("PARENT_DIVERGENCE_UNPROVEN", "stable", "parent identity remains blocked"),
        ("RECOMBINATION_BLOCKED", "stable", "no recombination license"),
    ]

    header("Candidate Moment Hierarchy Route Classifier")
    for name, status, reason in classifications:
        print(f"{name}: {status}; {reason}")

    with out.governance_assessments():
        out.line("finite hierarchy", StatusMark.PASS, "supported N=1..4")
        out.line("uniqueness", StatusMark.PASS, "unique profile per tested order")
        out.line("weighted inheritance", StatusMark.PASS, "derived")
        out.line("next obstruction", StatusMark.WARN, "next even moment remains")
        out.line("all-order closure", StatusMark.OBLIGATION, "not proven")
        out.line("local rho", StatusMark.WARN, "local rho nonzero remains")
        out.line("physical origin", StatusMark.OBLIGATION, "physical/covariant origin remains open")
        out.line("parent divergence", StatusMark.OBLIGATION, "parent divergence identity remains unproven")
        out.line("recombination", StatusMark.DEFER, "recombination remains blocked")
    with out.counterexamples():
        out.line("quartic one-off", StatusMark.FAIL, "finite hierarchy found through N=4")
        out.line("finite as all-order", StatusMark.FAIL, "finite hierarchy is not infinity")
        out.line("payload full inertness", StatusMark.FAIL, "next moments and local rho remain")
        out.line("parent equation", StatusMark.FAIL, "parent construction remains forbidden")
    with out.unresolved_obligations():
        out.line("general formula", StatusMark.OBLIGATION, "derive recurrence or closed form for general N")
        out.line("all-order limit", StatusMark.OBLIGATION, "test whether hierarchy converges or obstructs")
        out.line("covariant lift", StatusMark.OBLIGATION, "lift reduced hierarchy covariantly")

    record_marker(ns, MARKER_ID, "moment hierarchy route classifier")
    record_claim(ns, MARKER_ID, "g87_class_c1", GovernanceStatus.POLICY_RULE, "Finite moment hierarchy is supported through N=4 with unique profile per order.")
    record_claim(ns, MARKER_ID, "g87_class_c2", GovernanceStatus.POLICY_RULE, "The hierarchy is finite evidence only; next moments, local rho, and covariant origin remain open.")
    record_obligation(ns, "g87_class_o1", "Derive general recurrence/formula or test all-order limit.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_group_87_status_summary.py")

if __name__ == "__main__":
    main()
