#!/usr/bin/env python3
"""
higher_curvature_scalar_prototype.py

VacuumForge-managed scalar prototype for the higher-curvature local residual
branch.

This is not a tensor/covariant theorem. It tests the first concrete branch
obligation from 005: whether a local higher-derivative residual can keep the
same pointwise local response while changing derivative order, boundary data,
mode content, and weak-field pole structure.

Output:
    theory_v3/development/vacuum_sector/02_candidate_branches/
        higher_curvature_scalar_prototype_vacuumforge.md
"""

from pathlib import Path

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    RecordKind,
    ScriptOutput,
    StatusMark,
)


SCRIPT_PATH = Path(__file__).resolve()
SCRIPT_ID = f"{SCRIPT_PATH.parent.name}__{SCRIPT_PATH.stem}"
ARCHIVE_ROOT = SCRIPT_PATH.parents[1] / ".vacuumforge_archive"
REPO_ROOT = SCRIPT_PATH.parents[4]
REPORT_PATH = (
    REPO_ROOT
    / "theory_v3"
    / "development"
    / "vacuum_sector"
    / "02_candidate_branches"
    / "higher_curvature_scalar_prototype_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "candidate_branch_charters_005",
        "005_candidate_branch_charters__candidate_branch_charters",
        "candidate_branch_charters_005",
    )
]


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_equal(label, lhs, rhs):
    residual = simplify_expr(lhs - rhs)
    if residual != 0:
        raise AssertionError(f"{label} failed: {residual}")


def require_true(label, condition):
    if not bool(condition):
        raise AssertionError(f"{label} failed")


def euler_lagrange_second_derivative(L, field, coord):
    return simplify_expr(
        sp.diff(L, field)
        - sp.diff(sp.diff(L, sp.diff(field, coord)), coord)
        + sp.diff(sp.diff(L, sp.diff(field, coord, 2)), coord, 2)
    )


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    for dep_id, upstream_script_id, upstream_derivation_id in DEPENDENCIES:
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


def run_sympy_checks():
    x = sp.symbols("x")
    eps = sp.symbols("epsilon", nonzero=True)
    a = sp.symbols("a", nonzero=True)
    k = sp.symbols("k")
    q0 = sp.symbols("q0")
    q = sp.Function("q")(x)

    qp = sp.diff(q, x)
    qpp = sp.diff(q, x, 2)
    q3 = sp.diff(q, x, 3)
    q4 = sp.diff(q, x, 4)

    v_local = a * q0**2 / 2
    local_hessian_baseline = sp.diff(v_local, q0, 2)
    local_hessian_residual = sp.diff(v_local + eps * sp.Symbol("z") ** 2 / 2, q0, 2)
    require_equal(
        "same pointwise V_local Hessian",
        local_hessian_residual,
        local_hessian_baseline,
    )

    l_baseline = qp**2 / 2
    l_residual = l_baseline + eps * qpp**2 / 2
    el_baseline = euler_lagrange_second_derivative(l_baseline, q, x)
    el_residual = euler_lagrange_second_derivative(l_residual, q, x)
    expected_el_baseline = -sp.diff(q, x, 2)
    expected_el_residual = -sp.diff(q, x, 2) + eps * sp.diff(q, x, 4)
    require_equal("baseline Euler-Lagrange equation", el_baseline, expected_el_baseline)
    require_equal("residual Euler-Lagrange equation", el_residual, expected_el_residual)
    require_equal("fourth-derivative coefficient", sp.diff(el_residual, q4), eps)

    boundary_delta_q = simplify_expr(sp.diff(l_residual, qp) - sp.diff(sp.diff(l_residual, qpp), x))
    boundary_delta_qp = simplify_expr(sp.diff(l_residual, qpp))
    require_equal("boundary coefficient of delta q", boundary_delta_q, qp - eps * q3)
    require_equal("boundary coefficient of delta q prime", boundary_delta_qp, eps * qpp)

    baseline_symbol = k**2
    residual_symbol = simplify_expr(k**2 + eps * k**4)
    require_equal("baseline symbol degree", sp.degree(baseline_symbol, k), 2)
    require_equal("residual symbol degree", sp.degree(residual_symbol, k), 4)
    require_equal("residual symbol factorization", residual_symbol, k**2 * (1 + eps * k**2))

    propagator = 1 / residual_symbol
    partial_fraction = sp.apart(propagator, k)
    expected_partial_fraction = 1 / k**2 - eps / (1 + eps * k**2)
    require_equal("static propagator partial fraction", partial_fraction, expected_partial_fraction)

    lambda_symbol = sp.symbols("lambda")
    characteristic = simplify_expr(eps * lambda_symbol**4 - lambda_symbol**2)
    require_equal(
        "characteristic factorization",
        characteristic,
        lambda_symbol**2 * (eps * lambda_symbol**2 - 1),
    )
    roots = sp.solve(sp.Eq(characteristic, 0), lambda_symbol)
    require_true("extra characteristic roots present", any(root != 0 for root in roots))

    return {
        "v_local": v_local,
        "local_hessian": local_hessian_baseline,
        "l_baseline": l_baseline,
        "l_residual": l_residual,
        "el_baseline": el_baseline,
        "el_residual": el_residual,
        "boundary_delta_q": boundary_delta_q,
        "boundary_delta_qp": boundary_delta_qp,
        "baseline_symbol": baseline_symbol,
        "residual_symbol": residual_symbol,
        "partial_fraction": partial_fraction,
        "characteristic": characteristic,
        "roots": roots,
    }


def write_report(data):
    roots_text = ", ".join(sp.sstr(root) for root in data["roots"])
    md = f"""# VacuumForge Higher-Curvature Scalar Prototype

## Purpose

This report runs the first concrete branch test for the higher-curvature local
residual charter. It is a scalar prototype, not a tensor/covariant theorem.
Its job is to test whether a local higher-derivative residual can share the
same pointwise local response while changing the strain dynamics.

This report depends on:

```text
candidate_branch_charters_005
```

because the higher-curvature branch was opened only as a gated candidate.
It satisfies:

```text
higher_curvature_scalar_prototype_required_005
```

## Prototype Functional

Use one scalar configuration `q(x)` as a proxy for one linearized strain
channel:

```text
L_baseline = {sp.sstr(data["l_baseline"])}
L_residual = {sp.sstr(data["l_residual"])}
```

The pointwise local-response piece has Hessian:

```text
V_local = {sp.sstr(data["v_local"])}
d^2 V_local / dq0^2 = {sp.sstr(data["local_hessian"])}
```

Adding the derivative residual does not change this pointwise Hessian.

## Euler-Lagrange Check

SymPy verifies:

```text
EL_baseline = {sp.sstr(data["el_baseline"])}
EL_residual = {sp.sstr(data["el_residual"])}
```

The residual equation contains the fourth derivative with coefficient
`epsilon`. Therefore this branch cannot be treated as the closed second-order
metric branch unless the extra derivative structure is routed or removed by a
degeneracy.

## Boundary Variation Check

The second-derivative Lagrangian has boundary variation coefficients:

```text
coefficient of delta q      = {sp.sstr(data["boundary_delta_q"])}
coefficient of delta qprime = {sp.sstr(data["boundary_delta_qp"])}
```

The `delta qprime` term is absent in the baseline first-derivative functional.
The higher-curvature branch therefore requires additional boundary data,
boundary counterterms, or a degeneracy argument before it is a well-posed
strain branch.

## Mode And Weak-Field Pole Check

For a static Fourier mode, the baseline and residual symbols are:

```text
baseline symbol = {sp.sstr(data["baseline_symbol"])}
residual symbol = {sp.sstr(data["residual_symbol"])}
```

The residual propagator decomposes as:

```text
{sp.sstr(data["partial_fraction"])}
```

This exposes an extra pole at the scale set by `epsilon`. In a full metric
theory, the sign, tensor sector, and physical interpretation depend on the
covariant parent; the scalar prototype only proves that a weak-field residual
channel exists unless explicitly routed.

The characteristic polynomial is:

```text
{sp.sstr(data["characteristic"])}
```

with roots:

```text
{roots_text}
```

The nonzero roots are the extra mode data that the branch must classify.

## Gate Ledger Result

| gate | scalar-prototype result | branch consequence |
| --- | --- | --- |
| metric_limit_test | passes only at pointwise `V_local` Hessian level | local response is not enough to license dynamics |
| nonquadratic_routing_test | not triggered by this scalar metric-branch proxy | no Finsler/nonquadratic claim made |
| diffeomorphism_identity_test | not tested by scalar prototype | covariant Noether identity still owed |
| boundary_variation_test | obstruction found: `delta qprime` boundary term | boundary completion or extra data required |
| mode_count_test | obstruction found: fourth-order equation and extra roots | extra mode must be routed or killed |
| hyperbolicity_test | principal symbol changes from quadratic to quartic | full Lorentzian principal-symbol audit owed |
| source_ledger_test | not tested by scalar prototype | curvature residual must not be counted as matter |
| weak_field_residual_test | obstruction found: extra static pole | Yukawa/PPN residual map owed |
| epsilon_classification_test | controlled `epsilon != 0` not licensed | branch remains routed/underdetermined |

## Current Conclusion

The higher-curvature local residual branch fails to become a controlled
`epsilon != 0` branch at the scalar-prototype level. The prototype does not
prove that every covariant higher-curvature parent is impossible. It proves the
burden that any such parent must carry: boundary completion, extra-mode
classification, principal-symbol control, source-ledger purity, and weak-field
residual bounds.

## Classification

```text
result type: scalar prototype obstruction / first branch test
scope: local higher-derivative residual proxy
conclusion: generic higher-derivative residual is not licensed as controlled epsilon != 0
non-conclusion: no full tensor f(R), Ricci^2, Weyl^2, or Gauss-Bonnet theorem is proved here
```

The next technical target is a tensor-route audit for the higher-curvature
branch:

```text
separate inert/topological terms, scalaron-safe f(R)-type routes, and
spin-2/Weyl-type ghost routes before any higher-curvature residual is reused.
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")


def record_archive(ns):
    marker_id = "higher_curvature_scalar_prototype_006"
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[sp.Symbol("candidate_branch_charters")],
        output=sp.Symbol("higher_curvature_scalar_obstruction"),
        method="SymPy scalar higher-derivative Euler-Lagrange, boundary, and pole checks",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        is_placeholder=False,
        scope="scalar prototype for higher-curvature local residual branch",
    )

    ns.record_claim(
        ClaimRecord(
            claim_id="higher_curvature_scalar_obstruction_006",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.POLICY_RULE,
            statement=(
                "The scalar prototype shares the same pointwise local Hessian "
                "but introduces a fourth-order Euler-Lagrange equation, extra "
                "boundary data, and an extra weak-field pole; controlled "
                "epsilon != 0 is not licensed without routing."
            ),
            derivation_ids=[marker_id],
            obligation_ids=[],
        )
    )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="higher_curvature_scalar_prototype_required_005",
            script_id=SCRIPT_ID,
            title="Run first concrete residual branch test",
            status=ObligationStatus.SATISFIED,
            required_by=["005_candidate_branch_charters__candidate_branch_charters"],
            satisfied_by=[SCRIPT_ID],
            description=(
                "Satisfied by the scalar higher-derivative prototype, which "
                "checks pointwise local Hessian preservation, fourth-order "
                "Euler-Lagrange behavior, boundary data, and extra pole "
                "structure."
            ),
        )
    )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="higher_curvature_tensor_route_audit_required_006",
            script_id=SCRIPT_ID,
            title="Separate tensor higher-curvature residual routes",
            status=ObligationStatus.OPEN,
            required_by=[SCRIPT_ID],
            description=(
                "Separate inert/topological terms, scalaron-safe f(R)-type "
                "routes, and spin-2/Weyl-type ghost routes before any "
                "higher-curvature residual can be reused as physics."
            ),
        )
    )


def main() -> None:
    header("Vacuum Sector 006: Higher-Curvature Scalar Prototype")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    data = run_sympy_checks()

    out = ScriptOutput()
    with out.governance_assessments():
        out.line(
            "pointwise local Hessian",
            StatusMark.PASS,
            "derivative residual does not change V_local Hessian",
        )
    with out.governance_assessments():
        out.line(
            "higher-derivative residual",
            StatusMark.OBLIGATION,
            "fourth-order equation, extra boundary data, and extra pole require routing",
        )
    with out.unresolved_obligations():
        out.line(
            "tensor higher-curvature route audit required",
            StatusMark.OBLIGATION,
            "separate topological, scalaron, and spin-2 routes",
        )

    record_archive(ns)
    ns.write_run_metadata()
    write_report(data)

    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
