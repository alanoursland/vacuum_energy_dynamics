#!/usr/bin/env python3
"""
lambda_baseline_inventory.py

VacuumForge-managed inventory for the Lambda baseline workstream.

This is not a derivation of the observed cosmological constant. It opens the
baseline-selection folder after the higher-curvature residual routes fail or
quarantine, and records which Lambda roles are allowed, selected, or still
underdetermined.

Output:
    theory_v3/development/vacuum_sector/04_lambda_baseline/
        lambda_baseline_inventory_vacuumforge.md
"""

from dataclasses import dataclass
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
    / "04_lambda_baseline"
    / "lambda_baseline_inventory_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "higher_curvature_tensor_route_audit_007",
        "007_higher_curvature_tensor_route_audit__higher_curvature_tensor_route_audit",
        "higher_curvature_tensor_route_audit_007",
    )
]


@dataclass(frozen=True)
class LambdaRoute:
    route_id: str
    route_name: str
    baseline_role: str
    boundary_data: str
    source_ledger: str
    status: str
    next_obligation: str


ROUTES = [
    LambdaRoute(
        route_id="lambda_zero_flat_bridge",
        route_name="Lambda = 0 asymptotically flat bridge",
        baseline_role="scalar boundary-flux sector with no supplied background curvature",
        boundary_data="asymptotic flatness",
        source_ledger="ordinary localized matter only",
        status="selected baseline when no background curvature is supplied",
        next_obligation="do not use this sector to infer the observed nonzero Lambda",
    ),
    LambdaRoute(
        route_id="free_lovelock_constant",
        route_name="free Lovelock/background constant",
        baseline_role="allowed EH/Lovelock p=0 term",
        boundary_data="de Sitter or anti-de Sitter background data required",
        source_ledger="vacuum background, not matter and not dark excess",
        status="allowed but unvalued",
        next_obligation="provide a selector before treating the value as derived",
    ),
    LambdaRoute(
        route_id="derived_vacuum_floor",
        route_name="derived vacuum floor",
        baseline_role="nonzero vacuum baseline selected by ontology, measure, topology, or admissibility",
        boundary_data="baseline-selection boundary data not yet supplied",
        source_ledger="must distinguish constant floor from transportable excess",
        status="selector required",
        next_obligation="state the variational/admissibility rule that fixes sign and value",
    ),
    LambdaRoute(
        route_id="relaxation_or_nonlocal_selection",
        route_name="relaxation or nonlocal baseline selection",
        baseline_role="global or history-dependent vacuum floor",
        boundary_data="domain/history/kernel data required",
        source_ledger="must leave closed local metric equations intact or explicitly route deviations",
        status="not yet evaluated",
        next_obligation="prove local-equation quarantine and conservation identity",
    ),
    LambdaRoute(
        route_id="dark_excess_not_lambda",
        route_name="dark-sector excess is not the Lambda baseline",
        baseline_role="transportable or clustered excess over the floor",
        boundary_data="downstream dark-sector workstream",
        source_ledger="must not be inserted as constant Lambda",
        status="separate workstream",
        next_obligation="open only after baseline ledger prevents source double-counting",
    ),
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


def radial_laplacian(expr, r):
    return simplify_expr(sp.diff(r**2 * sp.diff(expr, r), r) / r**2)


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
    r, G, M, Lambda = sp.symbols("r G M Lambda", positive=True)

    phi_mass = -G * M / r
    phi_lambda = -Lambda * r**2 / 6
    phi_total = phi_mass + phi_lambda

    lap_mass = radial_laplacian(phi_mass, r)
    lap_lambda = radial_laplacian(phi_lambda, r)
    lap_total = radial_laplacian(phi_total, r)
    acceleration = simplify_expr(-sp.diff(phi_total, r))
    flat_recovery = radial_laplacian(phi_total.subs(Lambda, 0), r)
    lambda_limit = sp.limit(phi_lambda, r, sp.oo)

    require_equal("mass potential is harmonic for r > 0", lap_mass, 0)
    require_equal("Lambda potential solves modified vacuum Poisson equation", lap_lambda, -Lambda)
    require_equal("combined exterior equation", lap_total, -Lambda)
    require_equal("radial acceleration with Lambda", acceleration, -G * M / r**2 + Lambda * r / 3)
    require_equal("flat bridge recovered at Lambda zero", flat_recovery, 0)
    require_true("positive Lambda potential not asymptotically flat", lambda_limit == -sp.oo)

    rho_vac = sp.symbols("rho_vac", positive=True)
    pressure_vac = -rho_vac
    active_source = simplify_expr(rho_vac + 3 * pressure_vac)
    require_equal("vacuum equation-of-state active source", active_source, -2 * rho_vac)

    return {
        "phi_mass": phi_mass,
        "phi_lambda": phi_lambda,
        "phi_total": phi_total,
        "lap_mass": lap_mass,
        "lap_lambda": lap_lambda,
        "lap_total": lap_total,
        "acceleration": acceleration,
        "flat_recovery": flat_recovery,
        "lambda_limit": lambda_limit,
        "active_source": active_source,
    }


def status_mark(status: str):
    marks = {
        "selected baseline when no background curvature is supplied": StatusMark.PASS,
        "allowed but unvalued": StatusMark.DEFER,
        "selector required": StatusMark.OBLIGATION,
        "not yet evaluated": StatusMark.INFO,
        "separate workstream": StatusMark.DEFER,
    }
    if status not in marks:
        raise ValueError(f"Unknown Lambda route status: {status!r}")
    return marks[status]


def governance_status(status: str):
    if status == "selected baseline when no background curvature is supplied":
        return GovernanceStatus.POLICY_RULE
    if status in {"allowed but unvalued", "not yet evaluated", "separate workstream"}:
        return GovernanceStatus.UNVERIFIED
    if status == "selector required":
        return GovernanceStatus.POLICY_RULE
    raise ValueError(f"Unknown Lambda route status: {status!r}")


def markdown_route_rows():
    return "\n".join(
        "| {route_id} | {baseline_role} | {boundary_data} | {source_ledger} | {status} | {next_obligation} |".format(
            route_id=route.route_id,
            baseline_role=route.baseline_role,
            boundary_data=route.boundary_data,
            source_ledger=route.source_ledger,
            status=route.status,
            next_obligation=route.next_obligation,
        )
        for route in ROUTES
    )


def write_report(data):
    rows = markdown_route_rows()
    md = f"""# VacuumForge Lambda Baseline Inventory

## Purpose

This report opens the Lambda baseline workstream after the higher-curvature
residual detour. It does not derive the observed cosmological constant. It
separates baseline selection from local strain residuals and dark-sector
excess bookkeeping.

This report depends on:

```text
higher_curvature_tensor_route_audit_007
```

It satisfies:

```text
lambda_baseline_folder_required_007
```

## Symbolic Checks

For a localized mass plus cosmological term:

```text
Phi_M      = {sp.sstr(data["phi_mass"])}
Phi_Lambda = {sp.sstr(data["phi_lambda"])}
Phi_total  = {sp.sstr(data["phi_total"])}
```

SymPy verifies:

```text
Delta Phi_M (r > 0) = {sp.sstr(data["lap_mass"])}
Delta Phi_Lambda = {sp.sstr(data["lap_lambda"])}
Delta Phi_total  = {sp.sstr(data["lap_total"])}
a_r              = {sp.sstr(data["acceleration"])}
Lambda -> 0 bridge residual = {sp.sstr(data["flat_recovery"])}
lim Phi_Lambda as r -> infinity = {sp.sstr(data["lambda_limit"])}
```

Therefore positive nonzero `Lambda` is a background-curvature sector, not the
asymptotically flat scalar boundary-flux bridge.

The vacuum equation-of-state bookkeeping gives:

```text
rho_vac + 3 P_vac = {sp.sstr(data["active_source"])}
```

This is only a source-ledger identity. It does not compute the value of
`rho_vac`.

## Route Inventory

| route | baseline role | boundary data | source ledger | status | next obligation |
| --- | --- | --- | --- | --- | --- |
{rows}

## Current Conclusion

The Lambda baseline workstream is open. The `Lambda = 0` branch is the
asymptotically flat scalar boundary-flux sector when no nonzero background
curvature is supplied. Nonzero `Lambda` is allowed by the EH/Lovelock branch
but remains unvalued. A derived nonzero vacuum floor requires a selector:
variational, admissibility, topology, measure, or relaxation.

Dark-sector excess remains downstream and must not be inserted as the constant
baseline.

## Classification

```text
result type: Lambda baseline inventory / selector contract opener
scope: baseline/background curvature after local residual routes
conclusion: Lambda is allowed but not valued; nonzero Lambda requires a baseline selector
non-conclusion: observed Lambda is not derived; no dark-sector excess is licensed
```

The next technical target is a selector test:

```text
state candidate baseline selectors and kill conditions before any nonzero
Lambda mechanism is used.
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")


def record_archive(ns):
    marker_id = "lambda_baseline_inventory_008"
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[sp.Symbol("higher_curvature_route_classification")],
        output=sp.Symbol("lambda_baseline_inventory"),
        method="SymPy Newtonian Lambda bookkeeping plus baseline route inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        is_placeholder=False,
        scope="Lambda baseline/background curvature after local residual audit",
    )

    for route in ROUTES:
        ns.record_claim(
            ClaimRecord(
                claim_id=f"lambda_baseline_route_{route.route_id}_008",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=governance_status(route.status),
                statement=(
                    f"{route.route_name}: {route.status}; source ledger: "
                    f"{route.source_ledger}; next obligation: {route.next_obligation}."
                ),
                derivation_ids=[marker_id],
                obligation_ids=[],
            )
        )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="lambda_baseline_folder_required_007",
            script_id=SCRIPT_ID,
            title="Open Lambda baseline workstream",
            status=ObligationStatus.SATISFIED,
            required_by=["007_higher_curvature_tensor_route_audit__higher_curvature_tensor_route_audit"],
            satisfied_by=[SCRIPT_ID],
            description=(
                "Satisfied by opening 04_lambda_baseline and recording the "
                "Lambda baseline inventory."
            ),
        )
    )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="lambda_baseline_selector_required_008",
            script_id=SCRIPT_ID,
            title="State candidate Lambda baseline selectors",
            status=ObligationStatus.OPEN,
            required_by=[SCRIPT_ID],
            description=(
                "Candidate nonzero Lambda mechanisms must state selector rule, "
                "boundary data, source ledger, kill condition, and relation to "
                "the closed local metric equations."
            ),
        )
    )


def main() -> None:
    header("Vacuum Sector 008: Lambda Baseline Inventory")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    data = run_sympy_checks()

    out = ScriptOutput()
    for route in ROUTES:
        with out.governance_assessments():
            out.line(route.route_id, status_mark(route.status), f"{route.status}: {route.next_obligation}")
    with out.unresolved_obligations():
        out.line(
            "Lambda baseline selector required",
            StatusMark.OBLIGATION,
            "state selector candidates and kill conditions before using nonzero Lambda",
        )

    record_archive(ns)
    ns.write_run_metadata()
    write_report(data)

    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
