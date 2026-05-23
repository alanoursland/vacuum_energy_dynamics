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
]
MARKER_ID = "g099_origin_matrix"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    evidence = {
        "moment_like_formula": True,
        "shifted_k_plus_j_structure": True,
        "continuum_residual_identified": False,
        "test_basis_identified": False,
        "source_vector_identified": False,
        "boundary_conditions_identified": False,
        "functional_defined": False,
        "hessian_symmetry_or_weighting": False,
        "interface_domain_defined": False,
        "exchange_current_defined": False,
        "total_burden_defined": False,
        "physical_units_tracked": False,
        "ordinary_matter_separation": False,
        "divergence_identity": False,
    }

    routes = {
        "MOMENT_PROJECTION": [
            "moment_like_formula",
            "shifted_k_plus_j_structure",
            "continuum_residual_identified",
            "test_basis_identified",
            "source_vector_identified",
            "boundary_conditions_identified",
        ],
        "VARIATIONAL_HESSIAN": [
            "functional_defined",
            "hessian_symmetry_or_weighting",
            "physical_units_tracked",
            "ordinary_matter_separation",
        ],
        "INTERFACE_SMOOTHING": [
            "interface_domain_defined",
            "boundary_conditions_identified",
            "physical_units_tracked",
        ],
        "EXCHANGE_COMPENSATION": [
            "exchange_current_defined",
            "divergence_identity",
            "ordinary_matter_separation",
        ],
        "TOTAL_BURDEN": [
            "total_burden_defined",
            "functional_defined",
            "exchange_current_defined",
            "interface_domain_defined",
            "ordinary_matter_separation",
            "divergence_identity",
        ],
        "AUXILIARY_ADMISSIBILITY": [
            "moment_like_formula",
            "shifted_k_plus_j_structure",
        ],
    }

    header("Candidate Origin Route Evidence Matrix")
    results = []
    for route, reqs in routes.items():
        missing = [r for r in reqs if not evidence.get(r, False)]
        partial = any(evidence.get(r, False) for r in reqs)
        if not missing:
            status = "SUPPORTED"
        elif partial:
            status = "PLAUSIBLE_BUT_UNDERDERIVED"
        else:
            status = "NOT_LICENSED"
        results.append((route, status, missing))
        print(f"{route}: {status}")
        if missing:
            print(f"  missing: {missing}")

    with out.derived_results():
        for route, status, missing in results:
            mark = StatusMark.PASS if status == "SUPPORTED" else (StatusMark.INFO if status == "PLAUSIBLE_BUT_UNDERDERIVED" else StatusMark.WARN)
            out.line(route, mark, f"{status}; missing={missing}")
    with out.governance_assessments():
        out.line("moment/projection origin", StatusMark.INFO, "plausible but underderived")
        out.line("auxiliary admissibility", StatusMark.PASS, "supported by formula structure")
        out.line("physical origins", StatusMark.DEFER, "not licensed without residual/functional/source definitions")
    with out.counterexamples():
        out.line("variational Hessian origin", StatusMark.FAIL, "missing functional and Hessian/symmetry derivation")
        out.line("exchange origin", StatusMark.FAIL, "missing exchange current/divergence identity")
        out.line("total burden origin", StatusMark.FAIL, "missing total burden functional and subledgers")

    record_marker(ns, MARKER_ID, "origin route evidence matrix")
    record_claim(ns, MARKER_ID, "g099_matrix_c1", GovernanceStatus.POLICY_RULE, "Moment/projection origin is plausible but underderived; physical ledger origins are not currently licensed.")
    record_obligation(ns, "g099_matrix_o1", "Probe moment/projection plausibility.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_moment_projection_plausibility_probe.py")

if __name__ == "__main__":
    main()
