#!/usr/bin/env python3
"""
substance_frame_bounds_sieve.py

VacuumForge-managed first bounds sieve for substance-frame
non-gravitational channels.

This does not use numerical experimental bounds. It records the symbolic
compatibility condition that any detectable frame coupling must satisfy before
the route can become live.

Output:
    theory_v3/development/vacuum_sector/06_non_gravitational_channels/
        substance_frame_bounds_sieve_vacuumforge.md
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
    / "06_non_gravitational_channels"
    / "substance_frame_bounds_sieve_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "substance_frame_coupling_contract_023",
        "023_substance_frame_coupling_contract__substance_frame_coupling_contract",
        "substance_frame_coupling_contract_023",
    )
]


@dataclass(frozen=True)
class BoundsRoute:
    route_id: str
    route: str
    bound_condition: str
    target_condition: str
    missing_input: str
    disposition: str
    next_obligation: str
    has_derived_coupling: int
    has_numeric_bounds: int
    has_source_ledger: int
    metric_quarantined: int
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


def bounds_routes():
    return [
        BoundsRoute(
            route_id="silent_frame",
            route="beta_frame = 0",
            bound_condition="automatically below preferred-frame bounds",
            target_condition="no observable target",
            missing_input="none",
            disposition="silent ontology, not a channel signal",
            next_obligation="no bounds claim needed without coupling",
            has_derived_coupling=1,
            has_numeric_bounds=1,
            has_source_ledger=1,
            metric_quarantined=1,
        ),
        BoundsRoute(
            route_id="derived_bounded_coupling",
            route="0 < beta_frame <= beta_bound with detected target",
            bound_condition="beta_frame <= beta_bound",
            target_condition="beta_frame * A >= delta_target",
            missing_input="derived beta_frame, beta_bound, A, and delta_target",
            disposition="candidate only if all inputs are supplied",
            next_obligation="derive coupling and bind to numeric bounds before use",
            has_derived_coupling=0,
            has_numeric_bounds=0,
            has_source_ledger=0,
            metric_quarantined=1,
        ),
        BoundsRoute(
            route_id="observed_signal_backsolve",
            route="solve beta_frame from desired observed anisotropy",
            bound_condition="checked only after beta is fit",
            target_condition="beta_frame = delta_target / A",
            missing_input="pre-observation derivation of beta_frame",
            disposition="rejected as target-value insertion",
            next_obligation="do not use as derivation",
            has_derived_coupling=0,
            has_numeric_bounds=0,
            has_source_ledger=0,
            metric_quarantined=1,
            rejected=1,
        ),
        BoundsRoute(
            route_id="unbounded_frame_coupling",
            route="nonzero beta_frame with no bounds ledger",
            bound_condition="absent",
            target_condition="asserted signal",
            missing_input="preferred-frame, anisotropy, Lorentz, and calibration bounds",
            disposition="rejected as unbounded preferred-frame claim",
            next_obligation="return only with bounds ledger",
            has_derived_coupling=0,
            has_numeric_bounds=0,
            has_source_ledger=0,
            metric_quarantined=1,
            rejected=1,
        ),
    ]


def run_sympy_checks(routes):
    beta_frame, A, delta_target, beta_bound = sp.symbols(
        "beta_frame A delta_target beta_bound", positive=True
    )
    signal = beta_frame * A
    beta_required = sp.solve(sp.Eq(signal, delta_target), beta_frame)[0]
    compatibility_margin = beta_bound - beta_required

    require_equal("target backsolve for beta", beta_required, delta_target / A)
    require_equal("bound compatibility margin", compatibility_margin, beta_bound - delta_target / A)
    require_equal("silent frame signal", signal.subs(beta_frame, 0), 0)
    require_true("compatibility needs target and bound symbols", compatibility_margin.has(delta_target) and compatibility_margin.has(beta_bound))

    live_routes = [
        route.route_id
        for route in routes
        if (
            route.has_derived_coupling
            and route.has_numeric_bounds
            and route.has_source_ledger
            and route.metric_quarantined
            and not route.rejected
            and route.route_id != "silent_frame"
        )
    ]
    require_equal("no observable frame channel is live", len(live_routes), 0)

    return {
        "signal": signal,
        "beta_required": beta_required,
        "compatibility_margin": compatibility_margin,
        "live_routes": live_routes,
    }


def markdown_routes(routes):
    return "\n".join(
        (
            "| {route_id} | {route} | {bound_condition} | {target_condition} | "
            "{missing_input} | {disposition} | {next_obligation} |"
        ).format(
            route_id=route.route_id,
            route=route.route,
            bound_condition=route.bound_condition,
            target_condition=route.target_condition,
            missing_input=route.missing_input,
            disposition=route.disposition,
            next_obligation=route.next_obligation,
        )
        for route in routes
    )


def readiness_rows(routes):
    return "\n".join(
        "| {route_id} | {has_derived_coupling} | {has_numeric_bounds} | {has_source_ledger} | {metric_quarantined} | {live} |".format(
            route_id=route.route_id,
            has_derived_coupling=bool(route.has_derived_coupling),
            has_numeric_bounds=bool(route.has_numeric_bounds),
            has_source_ledger=bool(route.has_source_ledger),
            metric_quarantined=bool(route.metric_quarantined),
            live=bool(
                route.has_derived_coupling
                and route.has_numeric_bounds
                and route.has_source_ledger
                and route.metric_quarantined
                and not route.rejected
                and route.route_id != "silent_frame"
            ),
        )
        for route in routes
    )


def write_report(routes, data):
    route_md = markdown_routes(routes)
    readiness_md = readiness_rows(routes)
    md = f"""# VacuumForge Substance-Frame Bounds Sieve

## Purpose

This report applies the first symbolic bounds sieve to substance-frame
non-gravitational channels. It does not import numerical experimental bounds.

This report depends on:

```text
substance_frame_coupling_contract_023
```

It satisfies:

```text
substance_frame_bounds_sieve_required_023
```

## Symbolic Checks

Frame-channel signal:

```text
Delta O_frame = {sp.sstr(data["signal"])}
```

Target backsolve:

```text
beta_required = {sp.sstr(data["beta_required"])}
```

Compatibility margin:

```text
beta_bound - beta_required = {sp.sstr(data["compatibility_margin"])}
```

An observable frame channel is possible only if the derived coupling satisfies
both the target condition and the independent bounds condition. Solving
`beta_frame` from the desired target is a backsolve unless `beta_frame` was
derived before observation.

## Bounds Route Ledger

| route | route form | bound condition | target condition | missing input | disposition | next obligation |
| --- | --- | --- | --- | --- | --- | --- |
{route_md}

## Readiness

| route | derived coupling | numeric bounds | source ledger | metric quarantined | live observable channel |
| --- | --- | --- | --- | --- | --- |
{readiness_md}

## Current Conclusion

No observable substance-frame channel is live. The silent frame remains
allowed but predicts no preferred-frame signal. Coupled routes require a
derived coupling, a source/exchange ledger, metric quarantine, and explicit
preferred-frame/calibration bounds before use.

## Classification

```text
result type: substance-frame bounds sieve
scope: non-gravitational preferred-frame/calibration channels
conclusion: no bounded observable frame channel is licensed
non-conclusion: no global no-go theorem against frame-sensitive channels
```

The next technical target is:

```text
interior_cap_admissibility_contract_required_024
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")


def record_archive(ns, routes):
    marker_id = "substance_frame_bounds_sieve_024"
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[sp.Symbol("substance_frame_coupling_contract_result")],
        output=sp.Symbol("substance_frame_bounds_sieve_result"),
        method="SymPy target-threshold and bounds-compatibility sieve",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        is_placeholder=False,
        scope="Substance-frame coupling bounds readiness",
    )

    for route in routes:
        status = (
            GovernanceStatus.REJECTED_ROUTE
            if route.rejected
            else GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
        )
        ns.record_claim(
            ClaimRecord(
                claim_id=f"substance_frame_bounds_route_{route.route_id}_024",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=status,
                statement=f"{route.route_id}: {route.disposition}",
                derivation_ids=[marker_id],
                obligation_ids=["interior_cap_admissibility_contract_required_024"],
            )
        )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="substance_frame_bounds_sieve_required_023",
            script_id=SCRIPT_ID,
            title="Apply first bounds sieve to substance-frame channels",
            status=ObligationStatus.SATISFIED,
            required_by=["023_substance_frame_coupling_contract__substance_frame_coupling_contract"],
            satisfied_by=[SCRIPT_ID],
            description=(
                "Satisfied by separating silent-frame status, bounded derived "
                "coupling candidates, target backsolves, and unbounded "
                "preferred-frame claims."
            ),
        )
    )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="interior_cap_admissibility_contract_required_024",
            script_id=SCRIPT_ID,
            title="Open the strong-field/interior admissibility contract",
            status=ObligationStatus.OPEN,
            required_by=[SCRIPT_ID],
            description=(
                "After the first non-gravitational channel sweep, move to "
                "strong-field/interior admissibility and separate exterior GR "
                "matching from finite-strain interior claims."
            ),
        )
    )


def main() -> None:
    header("Vacuum Sector 024: Substance-Frame Bounds Sieve")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    routes = bounds_routes()
    data = run_sympy_checks(routes)

    out = ScriptOutput()
    for route in routes:
        status = StatusMark.FAIL if route.rejected else StatusMark.DEFER
        with out.governance_assessments():
            out.line(route.route_id, status, route.disposition)
    with out.unresolved_obligations():
        out.line(
            "Interior admissibility contract required",
            StatusMark.OBLIGATION,
            "open the strong-field/interior workstream",
        )

    record_archive(ns, routes)
    ns.write_run_metadata()
    write_report(routes, data)

    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
