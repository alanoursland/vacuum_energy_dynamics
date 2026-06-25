#!/usr/bin/env python3
"""
casimir_ufft_operator_instantiation.py

VacuumForge-managed audit of candidate Casimir/UFFT channel-operator
instantiations.

This does not derive a new vacuum-channel effect. It checks whether candidate
operator forms derive their coefficient from the vacuum ontology or import
standard QFT/material physics, observed fits, or free coupling constants.

Output:
    theory_v3/development/vacuum_sector/06_non_gravitational_channels/
        casimir_ufft_operator_instantiation_vacuumforge.md
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
    / "casimir_ufft_operator_instantiation_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "casimir_ufft_channel_contract_021",
        "021_casimir_ufft_channel_contract__casimir_ufft_channel_contract",
        "casimir_ufft_channel_contract_021",
    )
]


@dataclass(frozen=True)
class OperatorRoute:
    route_id: str
    operator_form: str
    coefficient_route: str
    ontology_derivation: str
    source_ledger: str
    disposition: str
    next_obligation: str
    derived_operator: int
    derived_coefficient: int
    source_ready: int
    metric_quarantine: int


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


def operator_routes():
    return [
        OperatorRoute(
            route_id="standard_casimir_qft",
            operator_form="-C_qft / L^4",
            coefficient_route="C_qft imported from ordinary QFT/material boundary physics",
            ontology_derivation="not supplied by the vacuum ontology",
            source_ledger="ordinary apparatus/material ledger, not a new vacuum source",
            disposition="baseline/background, not a new channel operator",
            next_obligation="do not count standard Casimir as new vacuum-sector signal",
            derived_operator=0,
            derived_coefficient=0,
            source_ready=1,
            metric_quarantine=1,
        ),
        OperatorRoute(
            route_id="fit_to_standard_scaling",
            operator_form="eta_ch * chi_m / L^4 matched to -C_qft / L^4",
            coefficient_route="eta_ch = -C_qft / chi_m",
            ontology_derivation="coefficient is inherited from imported C_qft and chi_m",
            source_ledger="not a new source ledger",
            disposition="rejected as coefficient backsolve",
            next_obligation="derive eta_ch before use",
            derived_operator=0,
            derived_coefficient=0,
            source_ready=0,
            metric_quarantine=1,
        ),
        OperatorRoute(
            route_id="free_boundary_channel",
            operator_form="eta_ch * chi_m * G_B / L^4",
            coefficient_route="eta_ch and boundary functional G_B left free",
            ontology_derivation="not derived",
            source_ledger="not supplied",
            disposition="deferred pending operator and ledger",
            next_obligation="derive eta_ch, G_B, and exchange bookkeeping",
            derived_operator=0,
            derived_coefficient=0,
            source_ready=0,
            metric_quarantine=1,
        ),
        OperatorRoute(
            route_id="universal_yukawa_reroute",
            operator_form="alpha_y exp(-r/lambda_y) / r",
            coefficient_route="gravitational residual parameters",
            ontology_derivation="belongs to residual-gate ledger, not this channel",
            source_ledger="wrong ledger",
            disposition="rejected as gravitational reroute",
            next_obligation="return to epsilon residual gates if desired",
            derived_operator=0,
            derived_coefficient=0,
            source_ready=0,
            metric_quarantine=0,
        ),
    ]


def run_sympy_checks(routes):
    L, chi_m, C_qft, G_B, r, alpha_y, lambda_y = sp.symbols(
        "L chi_m C_qft G_B r alpha_y lambda_y", positive=True
    )
    eta_ch = sp.symbols("eta_ch")
    standard_casimir = -C_qft / L**4
    channel_schema = eta_ch * chi_m / L**4
    solved_eta = sp.solve(sp.Eq(channel_schema, standard_casimir), eta_ch)[0]
    free_boundary = eta_ch * chi_m * G_B / L**4
    yukawa = alpha_y * sp.exp(-r / lambda_y) / r

    require_equal("eta backsolve imports standard coefficient", solved_eta, -C_qft / chi_m)
    require_equal("standard and schema have same L scaling", sp.diff(standard_casimir, L) / standard_casimir, -4 / L)
    require_equal("free boundary operator imports G_B", sp.diff(free_boundary, G_B), eta_ch * chi_m / L**4)
    require_equal("Yukawa route has no material dependence", sp.diff(yukawa, chi_m), 0)
    require_true("free boundary operator has free coefficient", free_boundary.has(eta_ch) and free_boundary.has(G_B))

    live_routes = [
        route.route_id
        for route in routes
        if route.derived_operator and route.derived_coefficient and route.source_ready and route.metric_quarantine
    ]
    require_equal("no Casimir/UFFT operator route is live", len(live_routes), 0)

    return {
        "standard_casimir": standard_casimir,
        "channel_schema": channel_schema,
        "solved_eta": solved_eta,
        "free_boundary": free_boundary,
        "yukawa": yukawa,
        "live_routes": live_routes,
    }


def markdown_routes(routes):
    return "\n".join(
        (
            "| {route_id} | {operator_form} | {coefficient_route} | {ontology_derivation} | "
            "{source_ledger} | {disposition} | {next_obligation} |"
        ).format(
            route_id=route.route_id,
            operator_form=route.operator_form,
            coefficient_route=route.coefficient_route,
            ontology_derivation=route.ontology_derivation,
            source_ledger=route.source_ledger,
            disposition=route.disposition,
            next_obligation=route.next_obligation,
        )
        for route in routes
    )


def readiness_rows(routes):
    return "\n".join(
        "| {route_id} | {derived_operator} | {derived_coefficient} | {source_ready} | {metric_quarantine} | {live} |".format(
            route_id=route.route_id,
            derived_operator=bool(route.derived_operator),
            derived_coefficient=bool(route.derived_coefficient),
            source_ready=bool(route.source_ready),
            metric_quarantine=bool(route.metric_quarantine),
            live=bool(route.derived_operator and route.derived_coefficient and route.source_ready and route.metric_quarantine),
        )
        for route in routes
    )


def write_report(routes, data):
    route_md = markdown_routes(routes)
    readiness_md = readiness_rows(routes)
    md = f"""# VacuumForge Casimir/UFFT Operator Instantiation Audit

## Purpose

This report audits whether the Casimir/UFFT channel contract can instantiate a
new channel operator. It does not derive a new signal.

This report depends on:

```text
casimir_ufft_channel_contract_021
```

It satisfies:

```text
casimir_ufft_operator_instantiation_required_021
```

## Symbolic Checks

Standard Casimir-scaling placeholder:

```text
O_C = {sp.sstr(data["standard_casimir"])}
```

Channel schema:

```text
O_ch = {sp.sstr(data["channel_schema"])}
eta_ch required to match O_C = {sp.sstr(data["solved_eta"])}
```

Free boundary-channel schema:

```text
O_B = {sp.sstr(data["free_boundary"])}
```

Yukawa reroute placeholder:

```text
Phi_Y = {sp.sstr(data["yukawa"])}
```

Matching the placeholder channel to standard Casimir scaling backsolves
`eta_ch` from the imported standard coefficient and material response. It does
not derive a new vacuum-channel operator.

## Operator Route Audit

| route | operator form | coefficient route | ontology derivation | source ledger | disposition | next obligation |
| --- | --- | --- | --- | --- | --- | --- |
{route_md}

## Readiness

| route | derived operator | derived coefficient | source ready | metric quarantine | live |
| --- | --- | --- | --- | --- | --- |
{readiness_md}

## Current Conclusion

No Casimir/UFFT operator route is live. Standard Casimir scaling belongs to
ordinary QFT/material boundary physics unless a new ontology coupling is
derived. Fitting the channel coefficient to that scaling is a backsolve, not a
derivation. A free boundary-channel schema remains possible but unlicensed.

## Classification

```text
result type: Casimir/UFFT operator-instantiation audit
scope: boundary/material non-gravitational channel operator
conclusion: no new operator is instantiated or licensed
non-conclusion: no global no-go theorem against Casimir/UFFT channels
```

The next technical target is:

```text
substance_frame_coupling_contract_required_022
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")


def record_archive(ns, routes):
    marker_id = "casimir_ufft_operator_instantiation_audit_022"
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[sp.Symbol("casimir_ufft_channel_contract_result")],
        output=sp.Symbol("casimir_ufft_operator_instantiation_result"),
        method="SymPy coefficient-backsolve and dependency audit for candidate Casimir/UFFT operators",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        is_placeholder=False,
        scope="Casimir/UFFT operator instantiation audit",
    )

    for route in routes:
        if route.route_id in {"fit_to_standard_scaling", "universal_yukawa_reroute"}:
            status = GovernanceStatus.REJECTED_ROUTE
        else:
            status = GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
        ns.record_claim(
            ClaimRecord(
                claim_id=f"casimir_ufft_operator_route_{route.route_id}_022",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=status,
                statement=f"{route.route_id}: {route.disposition}",
                derivation_ids=[marker_id],
                obligation_ids=["substance_frame_coupling_contract_required_022"],
            )
        )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="casimir_ufft_operator_instantiation_required_021",
            script_id=SCRIPT_ID,
            title="Instantiate or reject the Casimir/UFFT channel operator",
            status=ObligationStatus.SATISFIED,
            required_by=["021_casimir_ufft_channel_contract__casimir_ufft_channel_contract"],
            satisfied_by=[SCRIPT_ID],
            description=(
                "Satisfied by auditing standard Casimir scaling, coefficient "
                "backsolves, free boundary-channel schemas, and universal "
                "Yukawa reroutes. No route is live as a new channel operator."
            ),
        )
    )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="substance_frame_coupling_contract_required_022",
            script_id=SCRIPT_ID,
            title="Write the substance-frame coupling contract",
            status=ObligationStatus.OPEN,
            required_by=[SCRIPT_ID],
            description=(
                "Define whether a vacuum substance-frame variable has any "
                "non-gravitational coupling operator, metric quarantine, "
                "source ledger, observable, and falsifier."
            ),
        )
    )


def main() -> None:
    header("Vacuum Sector 022: Casimir/UFFT Operator Instantiation Audit")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    routes = operator_routes()
    data = run_sympy_checks(routes)

    out = ScriptOutput()
    for route in routes:
        status = (
            StatusMark.FAIL
            if route.route_id in {"fit_to_standard_scaling", "universal_yukawa_reroute"}
            else StatusMark.DEFER
        )
        with out.governance_assessments():
            out.line(route.route_id, status, route.disposition)
    with out.unresolved_obligations():
        out.line(
            "Substance-frame coupling contract required",
            StatusMark.OBLIGATION,
            "audit the next non-gravitational channel family",
        )

    record_archive(ns, routes)
    ns.write_run_metadata()
    write_report(routes, data)

    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
