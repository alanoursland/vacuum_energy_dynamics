#!/usr/bin/env python3
"""
exterior_matching_lemma.py

VacuumForge-managed exterior matching lemma for interior modifications.

This is not a full Birkhoff theorem. It records the contract-level result that
an interior modification does not change the exterior proxy when exterior
field equations and exterior charges are preserved.

Output:
    theory_v3/development/vacuum_sector/07_interior_cap/
        exterior_matching_lemma_vacuumforge.md
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
    / "07_interior_cap"
    / "exterior_matching_lemma_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "interior_cap_admissibility_contract_025",
        "025_interior_cap_admissibility_contract__interior_cap_admissibility_contract",
        "interior_cap_admissibility_contract_025",
    )
]


@dataclass(frozen=True)
class MatchingRoute:
    route_id: str
    route: str
    exterior_data: str
    matching_condition: str
    exterior_effect: str
    disposition: str
    next_obligation: str
    fixed_exterior_equations: int
    fixed_exterior_charges: int
    matching_written: int
    rejected: int = 0


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_equal(label, lhs, rhs) -> None:
    residual = simplify_expr(lhs - rhs)
    if residual != 0:
        raise AssertionError(f"{label} failed: {residual}")


def require_true(label, condition) -> None:
    if not bool(condition):
        raise AssertionError(f"{label} failed")


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


def matching_routes():
    return [
        MatchingRoute(
            route_id="fixed_charge_exterior",
            route="change only interior variables while preserving exterior charges",
            exterior_data="M_ext and Lambda fixed",
            matching_condition="junction conditions must conserve exterior charges",
            exterior_effect="exterior proxy unchanged",
            disposition="lemma-level exterior preservation",
            next_obligation="now test finite-strain admissibility scale",
            fixed_exterior_equations=1,
            fixed_exterior_charges=1,
            matching_written=1,
        ),
        MatchingRoute(
            route_id="surface_layer_charge_shift",
            route="surface layer changes exterior mass or pressure ledger",
            exterior_data="M_ext -> M_ext + delta_M",
            matching_condition="source ledger required",
            exterior_effect="exterior changes through charge shift",
            disposition="deferred pending source and junction ledger",
            next_obligation="write surface/source bookkeeping before use",
            fixed_exterior_equations=1,
            fixed_exterior_charges=0,
            matching_written=0,
        ),
        MatchingRoute(
            route_id="lambda_baseline_shift",
            route="interior rule changes exterior Lambda baseline",
            exterior_data="Lambda_ext -> Lambda_ext + delta_Lambda",
            matching_condition="must return to Lambda selector ledger",
            exterior_effect="exterior asymptotics change",
            disposition="rejected as wrong ledger here",
            next_obligation="return to Lambda baseline selector if desired",
            fixed_exterior_equations=1,
            fixed_exterior_charges=0,
            matching_written=0,
            rejected=1,
        ),
        MatchingRoute(
            route_id="exterior_residual_leak",
            route="interior rule leaks into exterior field equation",
            exterior_data="epsilon K_residual outside object",
            matching_condition="residual gates required",
            exterior_effect="tested exterior is not protected",
            disposition="rejected as residual-gate reroute",
            next_obligation="return to epsilon residual gates before use",
            fixed_exterior_equations=0,
            fixed_exterior_charges=0,
            matching_written=0,
            rejected=1,
        ),
    ]


def run_sympy_checks(routes):
    G, M_ext, delta_M, r, Lambda_ext, delta_Lambda, c = sp.symbols(
        "G M_ext delta_M r Lambda_ext delta_Lambda c"
    )
    R_cap = sp.symbols("R_cap", positive=True)
    exterior_proxy = 1 - 2 * G * M_ext / (c**2 * r) - Lambda_ext * r**2 / 3
    charge_shift_proxy = exterior_proxy.subs(M_ext, M_ext + delta_M)
    lambda_shift_proxy = exterior_proxy.subs(Lambda_ext, Lambda_ext + delta_Lambda)

    require_equal("fixed charge exterior independent of cap radius", sp.diff(exterior_proxy, R_cap), 0)
    require_equal("mass shift changes exterior", simplify_expr(charge_shift_proxy - exterior_proxy), -2 * G * delta_M / (c**2 * r))
    require_equal("Lambda shift changes exterior", simplify_expr(lambda_shift_proxy - exterior_proxy), -delta_Lambda * r**2 / 3)
    require_true("exterior proxy depends on exterior charges", exterior_proxy.has(M_ext) and exterior_proxy.has(Lambda_ext))

    preserved_routes = [
        route.route_id
        for route in routes
        if route.fixed_exterior_equations and route.fixed_exterior_charges and route.matching_written and not route.rejected
    ]
    require_equal("one fixed-charge exterior lemma route", len(preserved_routes), 1)

    return {
        "exterior_proxy": exterior_proxy,
        "charge_shift_delta": simplify_expr(charge_shift_proxy - exterior_proxy),
        "lambda_shift_delta": simplify_expr(lambda_shift_proxy - exterior_proxy),
        "preserved_routes": preserved_routes,
    }


def markdown_routes(routes):
    return "\n".join(
        (
            "| {route_id} | {route} | {exterior_data} | {matching_condition} | "
            "{exterior_effect} | {disposition} | {next_obligation} |"
        ).format(
            route_id=route.route_id,
            route=route.route,
            exterior_data=route.exterior_data,
            matching_condition=route.matching_condition,
            exterior_effect=route.exterior_effect,
            disposition=route.disposition,
            next_obligation=route.next_obligation,
        )
        for route in routes
    )


def readiness_rows(routes):
    return "\n".join(
        "| {route_id} | {fixed_exterior_equations} | {fixed_exterior_charges} | {matching_written} | {preserved} |".format(
            route_id=route.route_id,
            fixed_exterior_equations=bool(route.fixed_exterior_equations),
            fixed_exterior_charges=bool(route.fixed_exterior_charges),
            matching_written=bool(route.matching_written),
            preserved=bool(
                route.fixed_exterior_equations
                and route.fixed_exterior_charges
                and route.matching_written
                and not route.rejected
            ),
        )
        for route in routes
    )


def write_report(routes, data):
    route_md = markdown_routes(routes)
    readiness_md = readiness_rows(routes)
    md = f"""# VacuumForge Exterior Matching Lemma

## Purpose

This report records the contract-level exterior matching lemma for
interior-cap work. It does not prove a full uniqueness theorem and does not
derive an interior cap.

This report depends on:

```text
interior_cap_admissibility_contract_025
```

It satisfies:

```text
exterior_matching_lemma_required_025
```

## Symbolic Checks

Exterior proxy:

```text
f_ext(r) = {sp.sstr(data["exterior_proxy"])}
d f_ext / d R_cap = 0
```

Exterior charge shift:

```text
Delta f_ext from delta_M = {sp.sstr(data["charge_shift_delta"])}
```

Exterior Lambda shift:

```text
Delta f_ext from delta_Lambda = {sp.sstr(data["lambda_shift_delta"])}
```

If exterior equations and exterior charges are fixed, this proxy has no
dependence on the interior cap radius. If a surface layer changes exterior
mass, or if the Lambda baseline changes, the exterior changes and the claim
must be routed through the appropriate ledger.

## Matching Route Ledger

| route | route | exterior data | matching condition | exterior effect | disposition | next obligation |
| --- | --- | --- | --- | --- | --- | --- |
{route_md}

## Readiness

| route | fixed exterior equations | fixed exterior charges | matching written | exterior preserved |
| --- | --- | --- | --- | --- |
{readiness_md}

## Current Conclusion

The fixed-charge exterior route preserves the exterior proxy at lemma level.
This licenses only the exterior-preservation contract, not an interior cap.
Surface charge shifts need source and junction bookkeeping. Lambda shifts and
exterior residual leaks are wrong-ledger moves here.

## Classification

```text
result type: exterior matching lemma
scope: exterior preservation for interior modifications
conclusion: fixed exterior equations plus fixed exterior charges preserve the exterior proxy
non-conclusion: no finite-strain cap, no nonsingularity theorem, no full uniqueness theorem
```

The next technical target is:

```text
finite_strain_admissibility_probe_required_026
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")


def record_archive(ns, routes):
    marker_id = "exterior_matching_lemma_026"
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[sp.Symbol("interior_cap_admissibility_contract_result")],
        output=sp.Symbol("exterior_matching_lemma_result"),
        method="SymPy exterior-charge proxy and matching-route audit",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        is_placeholder=False,
        scope="Exterior preservation under fixed exterior charges",
    )

    for route in routes:
        status = (
            GovernanceStatus.REJECTED_ROUTE
            if route.rejected
            else GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
        )
        if route.route_id == "fixed_charge_exterior":
            status = GovernanceStatus.LICENSED_CLAIM
        ns.record_claim(
            ClaimRecord(
                claim_id=f"exterior_matching_route_{route.route_id}_026",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=status,
                statement=f"{route.route_id}: {route.disposition}",
                derivation_ids=[marker_id],
                obligation_ids=["finite_strain_admissibility_probe_required_026"],
            )
        )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="exterior_matching_lemma_required_025",
            script_id=SCRIPT_ID,
            title="Prove the exterior matching lemma for interior modifications",
            status=ObligationStatus.SATISFIED,
            required_by=["025_interior_cap_admissibility_contract__interior_cap_admissibility_contract"],
            satisfied_by=[SCRIPT_ID],
            description=(
                "Satisfied at contract level by showing fixed exterior equations "
                "and fixed exterior charges preserve the exterior proxy, while "
                "charge shifts and residual leaks reroute to other ledgers."
            ),
        )
    )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="finite_strain_admissibility_probe_required_026",
            script_id=SCRIPT_ID,
            title="Probe finite-strain admissibility scale for interior caps",
            status=ObligationStatus.OPEN,
            required_by=[SCRIPT_ID],
            description=(
                "With exterior preservation isolated, test whether a finite "
                "interior strain bound or cap scale is derived or merely imported."
            ),
        )
    )


def main() -> None:
    header("Vacuum Sector 026: Exterior Matching Lemma")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    routes = matching_routes()
    data = run_sympy_checks(routes)

    out = ScriptOutput()
    for route in routes:
        if route.route_id == "fixed_charge_exterior":
            status = StatusMark.PASS
        elif route.rejected:
            status = StatusMark.FAIL
        else:
            status = StatusMark.DEFER
        with out.governance_assessments():
            out.line(route.route_id, status, route.disposition)
    with out.unresolved_obligations():
        out.line(
            "Finite-strain admissibility probe required",
            StatusMark.OBLIGATION,
            "test whether the cap scale is derived or imported",
        )

    record_archive(ns, routes)
    ns.write_run_metadata()
    write_report(routes, data)

    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
