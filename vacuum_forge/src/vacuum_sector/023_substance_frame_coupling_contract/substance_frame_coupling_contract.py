#!/usr/bin/env python3
"""
substance_frame_coupling_contract.py

VacuumForge-managed contract for substance-frame non-gravitational couplings.

This is not a derivation of a preferred-frame signal. It checks that an
ontological frame remains observationally silent unless a coupling operator is
added, and that any added coupling must be quarantined from the closed metric
sector and routed through bounds.

Output:
    theory_v3/development/vacuum_sector/06_non_gravitational_channels/
        substance_frame_coupling_contract_vacuumforge.md
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
    / "substance_frame_coupling_contract_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "casimir_ufft_operator_instantiation_audit_022",
        "022_casimir_ufft_operator_instantiation__casimir_ufft_operator_instantiation",
        "casimir_ufft_operator_instantiation_audit_022",
    )
]


@dataclass(frozen=True)
class FrameRoute:
    route_id: str
    frame_variable: str
    coupling_object: str
    metric_quarantine: str
    observable: str
    bounds_route: str
    disposition: str
    next_obligation: str
    coupling_written: int
    source_ready: int
    metric_quarantined: int
    bounds_ready: int
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


def frame_routes():
    return [
        FrameRoute(
            route_id="silent_frame",
            frame_variable="unit timelike substance-frame direction u^a",
            coupling_object="none",
            metric_quarantine="closed metric sector has no u^a force term",
            observable="none",
            bounds_route="not applicable until a coupling is added",
            disposition="ontological frame only; no preferred-frame prediction",
            next_obligation="do not infer signal from frame existence alone",
            coupling_written=0,
            source_ready=1,
            metric_quarantined=1,
            bounds_ready=1,
        ),
        FrameRoute(
            route_id="calibration_anisotropy_channel",
            frame_variable="u^a plus apparatus direction n^a",
            coupling_object="beta_frame * (u dot n)^2 calibration response",
            metric_quarantine="epsilon_g = 0 unless residual gates are reopened",
            observable="orientation or sidereal calibration drift",
            bounds_route="preferred-frame, anisotropy, and calibration bounds required",
            disposition="quarantined candidate only",
            next_obligation="derive beta_frame and bind to bounds",
            coupling_written=1,
            source_ready=0,
            metric_quarantined=1,
            bounds_ready=0,
        ),
        FrameRoute(
            route_id="matter_clock_channel",
            frame_variable="u^a plus matter clock or phase variable",
            coupling_object="frame-sensitive matter-clock operator, not yet derived",
            metric_quarantine="epsilon_g = 0 unless residual gates are reopened",
            observable="clock, phase, or matter-calibration anisotropy",
            bounds_route="Lorentz and preferred-frame bounds required",
            disposition="deferred pending operator and source ledger",
            next_obligation="write operator and exchange bookkeeping",
            coupling_written=0,
            source_ready=0,
            metric_quarantined=1,
            bounds_ready=0,
        ),
        FrameRoute(
            route_id="metric_preferred_frame_reroute",
            frame_variable="u^a inserted into gravitational action",
            coupling_object="preferred-frame metric residual",
            metric_quarantine="fails: changes closed metric response",
            observable="preferred-frame gravity",
            bounds_route="belongs to residual gates and gravitational tests",
            disposition="rejected as wrong ledger",
            next_obligation="return to epsilon residual gates if desired",
            coupling_written=1,
            source_ready=0,
            metric_quarantined=0,
            bounds_ready=0,
            rejected=1,
        ),
    ]


def run_sympy_checks(routes):
    beta_frame, theta, epsilon_g = sp.symbols("beta_frame theta epsilon_g")
    anisotropy = beta_frame * sp.cos(theta) ** 2
    angular_sensitivity = sp.diff(anisotropy, theta)
    metric_leak = epsilon_g * anisotropy

    require_equal("silent frame has zero observable when beta is zero", anisotropy.subs(beta_frame, 0), 0)
    require_equal("metric quarantine kills frame metric leak", metric_leak.subs(epsilon_g, 0), 0)
    require_equal("anisotropy angular sensitivity", angular_sensitivity, -2 * beta_frame * sp.sin(theta) * sp.cos(theta))
    require_true("anisotropy depends on coupling", anisotropy.has(beta_frame))

    live_routes = [
        route.route_id
        for route in routes
        if route.coupling_written and route.source_ready and route.metric_quarantined and route.bounds_ready and not route.rejected
    ]
    require_equal("no substance-frame coupling route is live", len(live_routes), 0)

    return {
        "anisotropy": anisotropy,
        "angular_sensitivity": angular_sensitivity,
        "metric_leak": metric_leak,
        "live_routes": live_routes,
    }


def markdown_routes(routes):
    return "\n".join(
        (
            "| {route_id} | {frame_variable} | {coupling_object} | {metric_quarantine} | "
            "{observable} | {bounds_route} | {disposition} | {next_obligation} |"
        ).format(
            route_id=route.route_id,
            frame_variable=route.frame_variable,
            coupling_object=route.coupling_object,
            metric_quarantine=route.metric_quarantine,
            observable=route.observable,
            bounds_route=route.bounds_route,
            disposition=route.disposition,
            next_obligation=route.next_obligation,
        )
        for route in routes
    )


def readiness_rows(routes):
    return "\n".join(
        "| {route_id} | {coupling_written} | {source_ready} | {metric_quarantined} | {bounds_ready} | {live} |".format(
            route_id=route.route_id,
            coupling_written=bool(route.coupling_written),
            source_ready=bool(route.source_ready),
            metric_quarantined=bool(route.metric_quarantined),
            bounds_ready=bool(route.bounds_ready),
            live=bool(
                route.coupling_written
                and route.source_ready
                and route.metric_quarantined
                and route.bounds_ready
                and not route.rejected
            ),
        )
        for route in routes
    )


def write_report(routes, data):
    route_md = markdown_routes(routes)
    readiness_md = readiness_rows(routes)
    md = f"""# VacuumForge Substance-Frame Coupling Contract

## Purpose

This report writes the first contract for a substance-frame
non-gravitational channel. It does not derive a preferred-frame signal.

This report depends on:

```text
casimir_ufft_operator_instantiation_audit_022
```

It satisfies:

```text
substance_frame_coupling_contract_required_022
```

## Symbolic Checks

Frame-anisotropy placeholder:

```text
Delta O_frame = {sp.sstr(data["anisotropy"])}
d(Delta O_frame)/d theta = {sp.sstr(data["angular_sensitivity"])}
Delta O_frame | beta_frame = 0 -> 0
```

Metric leakage proxy:

```text
Delta_metric = {sp.sstr(data["metric_leak"])}
Delta_metric | epsilon_g = 0 -> 0
```

The check is narrow: a frame variable is observationally silent unless a
coupling is added. A nonzero coupling creates a preferred-frame/calibration
channel that must be bounded and kept out of the closed metric response.

## Route Ledger

| route | frame variable | coupling object | metric quarantine | observable | bounds route | disposition | next obligation |
| --- | --- | --- | --- | --- | --- | --- | --- |
{route_md}

## Readiness

| route | coupling written | source ready | metric quarantined | bounds ready | live |
| --- | --- | --- | --- | --- | --- |
{readiness_md}

## Current Conclusion

No substance-frame coupling route is live. The frame may remain an ontological
object without predicting a preferred-frame signal. Observable routes require a
coupling operator, source/exchange ledger, metric quarantine, and preferred
frame or calibration bounds.

## Classification

```text
result type: substance-frame coupling contract
scope: non-gravitational preferred-frame/calibration channels
conclusion: frame existence alone predicts no signal; coupled routes are unlicensed
non-conclusion: no global no-go theorem against substance-frame channels
```

The next technical target is:

```text
substance_frame_bounds_sieve_required_023
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")


def record_archive(ns, routes):
    marker_id = "substance_frame_coupling_contract_023"
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[sp.Symbol("casimir_ufft_operator_instantiation_result")],
        output=sp.Symbol("substance_frame_coupling_contract_result"),
        method="SymPy silent-frame and anisotropy-coupling quarantine check",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        is_placeholder=False,
        scope="Substance-frame non-gravitational coupling contract",
    )

    for route in routes:
        status = (
            GovernanceStatus.REJECTED_ROUTE
            if route.rejected
            else GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
        )
        ns.record_claim(
            ClaimRecord(
                claim_id=f"substance_frame_route_{route.route_id}_023",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=status,
                statement=f"{route.route_id}: {route.disposition}",
                derivation_ids=[marker_id],
                obligation_ids=["substance_frame_bounds_sieve_required_023"],
            )
        )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="substance_frame_coupling_contract_required_022",
            script_id=SCRIPT_ID,
            title="Write the substance-frame coupling contract",
            status=ObligationStatus.SATISFIED,
            required_by=["022_casimir_ufft_operator_instantiation__casimir_ufft_operator_instantiation"],
            satisfied_by=[SCRIPT_ID],
            description=(
                "Satisfied by separating silent ontological frame status from "
                "coupled preferred-frame/calibration channels and rejecting "
                "metric preferred-frame reroutes as wrong ledger moves."
            ),
        )
    )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="substance_frame_bounds_sieve_required_023",
            script_id=SCRIPT_ID,
            title="Apply first bounds sieve to substance-frame channels",
            status=ObligationStatus.OPEN,
            required_by=[SCRIPT_ID],
            description=(
                "Any frame-sensitive coupling must be checked against "
                "preferred-frame, anisotropy, Lorentz, and calibration bounds "
                "before it can become a live channel."
            ),
        )
    )


def main() -> None:
    header("Vacuum Sector 023: Substance-Frame Coupling Contract")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    routes = frame_routes()
    data = run_sympy_checks(routes)

    out = ScriptOutput()
    for route in routes:
        status = StatusMark.FAIL if route.rejected else StatusMark.DEFER
        with out.governance_assessments():
            out.line(route.route_id, status, route.disposition)
    with out.unresolved_obligations():
        out.line(
            "Substance-frame bounds sieve required",
            StatusMark.OBLIGATION,
            "bind any frame coupling to preferred-frame and calibration bounds",
        )

    record_archive(ns, routes)
    ns.write_run_metadata()
    write_report(routes, data)

    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
