#!/usr/bin/env python3
"""
strain_underdetermination_witness.py

Vacuum-sector witness that local pointwise response does not determine the
strain functional.

This script uses SymPy for the symbolic checks and VacuumForge for archive,
claim, and obligation bookkeeping.

Outputs:
    theory_v3/development/vacuum_sector/01_strain_functional/
        underdetermination_witness_vacuumforge.md
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
    / "01_strain_functional"
    / "underdetermination_witness_vacuumforge.md"
)


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label: str, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label: str, lhs, rhs):
    require_zero(label, lhs - rhs)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
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


def euler_lagrange_1d(lagrangian, field, coordinate):
    dx_field = sp.diff(field, coordinate)
    ddx_field = sp.diff(field, coordinate, 2)
    return simplify_expr(
        sp.diff(lagrangian, field)
        - sp.diff(sp.diff(lagrangian, dx_field), coordinate)
        + sp.diff(sp.diff(lagrangian, ddx_field), coordinate, 2)
    )


def boundary_pair_1d(lagrangian, field, coordinate):
    """Boundary coefficients multiplying eta and eta' for L(X,X',X'')."""
    dx_field = sp.diff(field, coordinate)
    ddx_field = sp.diff(field, coordinate, 2)
    coeff_eta_prime = sp.diff(lagrangian, ddx_field)
    coeff_eta = sp.diff(lagrangian, dx_field) - sp.diff(coeff_eta_prime, coordinate)
    return simplify_expr(coeff_eta), simplify_expr(coeff_eta_prime)


def run_symbolic_witness():
    x = sp.symbols("x")
    m, a, b, epsilon = sp.symbols("m a b epsilon")
    y = sp.symbols("y")
    X = sp.Function("X")(x)

    checks = []

    v_local = m**2 * y**2 / 2
    local_hessian = sp.diff(v_local, y, 2)
    require_equal("local Hessian", local_hessian, m**2)
    checks.append("local Hessian is m^2")

    L0 = m**2 * X**2 / 2 + a * sp.diff(X, x) ** 2 / 2
    L1 = L0 + epsilon * b * sp.diff(X, x, 2) ** 2 / 2

    local_hessian_L0 = sp.diff(L0.subs({sp.diff(X, x): 0, sp.diff(X, x, 2): 0}), X, 2)
    local_hessian_L1 = sp.diff(L1.subs({sp.diff(X, x): 0, sp.diff(X, x, 2): 0}), X, 2)
    require_equal("same local Hessian in L0", local_hessian_L0, m**2)
    require_equal("same local Hessian in L1", local_hessian_L1, m**2)
    require_equal("matching local Hessians", local_hessian_L0, local_hessian_L1)
    checks.append("two functionals share the same local Hessian")

    EL0 = euler_lagrange_1d(L0, X, x)
    EL1 = euler_lagrange_1d(L1, X, x)
    EL_residual = simplify_expr(EL1 - EL0)

    require_equal("EL0", EL0, m**2 * X - a * sp.diff(X, x, 2))
    require_equal("EL residual", EL_residual, epsilon * b * sp.diff(X, x, 4))
    checks.append("gradient residual changes the Euler-Lagrange equation")

    eta0, eta_prime0 = boundary_pair_1d(L0, X, x)
    eta1, eta_prime1 = boundary_pair_1d(L1, X, x)
    require_equal("L0 eta boundary coefficient", eta0, a * sp.diff(X, x))
    require_equal("L0 eta-prime boundary coefficient", eta_prime0, 0)
    require_equal(
        "L1 eta boundary coefficient",
        eta1,
        a * sp.diff(X, x) - epsilon * b * sp.diff(X, x, 3),
    )
    require_equal("L1 eta-prime boundary coefficient", eta_prime1, epsilon * b * sp.diff(X, x, 2))
    checks.append("gradient residual changes boundary data")

    if sp.diff(X, x, 4) not in EL1.atoms(sp.Derivative):
        raise AssertionError("EL1 derivative-order check failed")
    checks.append("residual raises derivative order")

    return {
        "checks": checks,
        "EL0": EL0,
        "EL1": EL1,
        "EL_residual": EL_residual,
        "eta0": eta0,
        "eta_prime0": eta_prime0,
        "eta1": eta1,
        "eta_prime1": eta_prime1,
    }


def write_report(result):
    validation_bullets = "\n".join(f"- {item}: passed" for item in result["checks"])

    md = f"""# VacuumForge Underdetermination Witness

## Purpose

This managed witness validates the narrow vacuum-sector claim:

```text
same local Hessian does not imply same strain dynamics.
```

SymPy supplies the algebraic checks. VacuumForge records the derivation,
claim, and open obligation boundary for later proof-chain use.

## Validated Checks

{validation_bullets}

## Prototype

Use:

```text
V_local(X) = (m^2/2) X^2
L0 = (m^2/2) X^2 + (a/2) (dX/dx)^2
L1 = L0 + epsilon (b/2) (d^2X/dx^2)^2
```

Both `L0` and `L1` share the same local Hessian:

```text
d^2 V_local / dX^2 = m^2.
```

## Euler-Lagrange Check

SymPy verifies:

```text
EL(L0) = m^2 X - a X''
EL(L1) = m^2 X - a X'' + epsilon b X''''
```

The same pointwise local response can therefore produce different
field-equation operators once the strain term changes.

## Boundary Check

For boundary variation:

```text
L0:
  B_eta = a X'
  B_eta_prime = 0

L1:
  B_eta = a X' - epsilon b X'''
  B_eta_prime = epsilon b X''
```

The residual changes admissible boundary data as well as the bulk equation.

## VacuumForge Record

This script records:

```text
derivation: local_response_underdetermines_strain_001
claim: local_response_only_selector_underdetermined_001
obligation: strain_branch_selector_required_001
```

## Conclusion

The local-response-only selector is classified as:

```text
underdetermined without new axiom
```

The next selector must come from accumulated gates plus a strain principle,
not from `V_local` alone.
"""
    REPORT_PATH.write_text(md, encoding="utf-8")


def record_vacuumforge(ns, result):
    output_symbol = sp.Symbol("local_response_underdetermines_K_strain")

    ns.record_derivation(
        derivation_id="local_response_underdetermines_strain_001",
        inputs=[],
        output=output_symbol,
        method=(
            "SymPy scalar prototype: L0 and L1 share local Hessian m^2 but "
            "differ in Euler-Lagrange operator, derivative order, and boundary data"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="underdetermination_witness",
        scope="local pointwise response does not determine K_strain",
    )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="strain_branch_selector_required_001",
            script_id=SCRIPT_ID,
            title="Provide a between-point strain selector",
            status=ObligationStatus.OPEN,
            required_by=[SCRIPT_ID],
            description=(
                "A future strain axiom, accumulated-gate theorem, or explicit "
                "candidate branch must choose the neighboring-mismatch rule and "
                "classify epsilon."
            ),
        )
    )

    ns.record_claim(
        ClaimRecord(
            claim_id="local_response_only_selector_underdetermined_001",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.LICENSED_CLAIM,
            statement=(
                "Local quadratic interval response can reconstruct pointwise metric "
                "data, but it does not determine the between-point strain functional. "
                "The scalar witness shows identical local Hessian with different "
                "Euler-Lagrange operator, derivative order, and boundary data."
            ),
            derivation_ids=["local_response_underdetermines_strain_001"],
            obligation_ids=["strain_branch_selector_required_001"],
        )
    )


def main():
    header("Vacuum Sector 001: Strain Underdetermination Witness")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    result = run_symbolic_witness()

    out = ScriptOutput()
    with out.derived_results():
        out.line(
            "local-response-only selector underdetermined",
            StatusMark.PASS,
            "same local Hessian but different EL equation, derivative order, and boundary data",
        )
    with out.unresolved_obligations():
        out.line(
            "strain branch selector still required",
            StatusMark.OBLIGATION,
            "local response alone does not choose K_strain or classify epsilon",
        )

    record_vacuumforge(ns, result)
    ns.write_run_metadata()
    write_report(result)

    print("All symbolic checks passed.")
    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
