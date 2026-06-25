#!/usr/bin/env python3
"""
minimal_strain_axiom_contract.py

VacuumForge-managed contract for any proposed nonbaseline strain axiom.

This does not adopt an axiom. It states the minimum interface a new axiom must
provide before it can license a nonbaseline strain branch.

Output:
    theory_v3/development/vacuum_sector/01_strain_functional/
        minimal_strain_axiom_contract_vacuumforge.md
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
    / "01_strain_functional"
    / "minimal_strain_axiom_contract_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "strain_branch_selector_decision_table_030",
        "030_strain_branch_selector_decision_table__strain_branch_selector_decision_table",
        "strain_branch_selector_decision_table_030",
    )
]


@dataclass(frozen=True)
class AxiomRequirement:
    requirement_id: str
    requirement: str
    purpose: str
    failure_if_absent: str


@dataclass(frozen=True)
class AxiomRoute:
    route_id: str
    route: str
    contract_status: str
    missing_items: str
    decision: str
    next_obligation: str
    satisfies_contract: int
    licenses_nonbaseline: int
    rejected: int = 0
    governance_status: GovernanceStatus = GovernanceStatus.DEFERRED_PENDING_PREREQUISITES


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


def axiom_requirements():
    return [
        AxiomRequirement(
            requirement_id="x_variable",
            requirement="Name the vacuum configuration variable X",
            purpose="prevents unnamed ontology from generating dynamics",
            failure_if_absent="underdetermined X contract",
        ),
        AxiomRequirement(
            requirement_id="metric_response_map",
            requirement="Map X to local interval response and metric/Hessian response",
            purpose="preserves the closed metric-response branch or routes deviations",
            failure_if_absent="hidden change to measured local response",
        ),
        AxiomRequirement(
            requirement_id="neighboring_mismatch",
            requirement="Define how X(p) and X(q) are compared",
            purpose="turns pointwise response into strain dynamics",
            failure_if_absent="no K_strain can be formed",
        ),
        AxiomRequirement(
            requirement_id="strain_invariant",
            requirement="State the scalar/invariant K_strain and admitted derivative order",
            purpose="defines the variational object",
            failure_if_absent="notation without action",
        ),
        AxiomRequirement(
            requirement_id="boundary_variation",
            requirement="State boundary data and counterterms",
            purpose="keeps the variational problem well posed",
            failure_if_absent="uncontrolled boundary equations",
        ),
        AxiomRequirement(
            requirement_id="conservation_identity",
            requirement="State the Noether/Bianchi/source-ledger identity",
            purpose="prevents unconserved or double-counted sources",
            failure_if_absent="source-ledger failure",
        ),
        AxiomRequirement(
            requirement_id="mode_hyperbolicity",
            requirement="Route mode count and hyperbolicity",
            purpose="protects the closed radiative and weak-field gates",
            failure_if_absent="hidden scalar, ghost, vector, or ill-posed mode",
        ),
        AxiomRequirement(
            requirement_id="epsilon_classification",
            requirement="Classify epsilon as zero, controlled nonzero, failed, or underdetermined",
            purpose="blocks free-knob residual language",
            failure_if_absent="unclassified residual",
        ),
        AxiomRequirement(
            requirement_id="falsifier",
            requirement="State a kill condition or operational falsifier",
            purpose="prevents unfalsifiable mechanism drift",
            failure_if_absent="orphan mechanism",
        ),
    ]


def axiom_routes():
    return [
        AxiomRoute(
            route_id="no_new_axiom_baseline",
            route="decline a new axiom and retain accumulated-gate EH/GHY closure",
            contract_status="complete only for epsilon = 0 baseline",
            missing_items="none for baseline; all nonbaseline content absent",
            decision="allowed null choice",
            next_obligation="do not claim nonbaseline vacuum physics",
            satisfies_contract=1,
            licenses_nonbaseline=0,
            governance_status=GovernanceStatus.LICENSED_CLAIM,
        ),
        AxiomRoute(
            route_id="primitive_nonmetric_x_axiom",
            route="postulate a deeper nonmetric X",
            contract_status="open",
            missing_items="metric response map, mismatch rule, invariant, boundary, modes, falsifier",
            decision="candidate contract only",
            next_obligation="instantiate all axiom fields before branch charter",
            satisfies_contract=0,
            licenses_nonbaseline=0,
            governance_status=GovernanceStatus.UNRESOLVED_PROOF_OBLIGATION,
        ),
        AxiomRoute(
            route_id="primitive_mismatch_axiom",
            route="postulate a comparison/mismatch rule beneath Levi-Civita transport",
            contract_status="open",
            missing_items="X variable, invariant, boundary rule, conservation identity, mode route",
            decision="candidate contract only",
            next_obligation="show why mismatch produces EH baseline plus routed residual",
            satisfies_contract=0,
            licenses_nonbaseline=0,
            governance_status=GovernanceStatus.UNRESOLVED_PROOF_OBLIGATION,
        ),
        AxiomRoute(
            route_id="nonlocal_relaxation_axiom",
            route="postulate a nonlocal relaxation or history selector",
            contract_status="deferred",
            missing_items="local GR limit, kernel conservation, source quarantine, hyperbolicity route",
            decision="not local strain physics until gates are routed",
            next_obligation="separate local closure from large-scale/nonlocal ledger",
            satisfies_contract=0,
            licenses_nonbaseline=0,
            governance_status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        ),
        AxiomRoute(
            route_id="boundary_global_axiom",
            route="postulate boundary/topology/admissibility selection of strain class",
            contract_status="deferred",
            missing_items="local invariant, derived scale, and variational object",
            decision="can constrain classes, not supply K_strain alone",
            next_obligation="derive local strain object before value/action claims",
            satisfies_contract=0,
            licenses_nonbaseline=0,
            governance_status=GovernanceStatus.POLICY_RULE,
        ),
        AxiomRoute(
            route_id="mechanism_fit_axiom",
            route="choose axiom to rescue a desired Lambda, dark, channel, or interior mechanism",
            contract_status="rejected",
            missing_items="independence from target mechanism",
            decision="rejected as post-hoc selector",
            next_obligation="do not use as derivation",
            satisfies_contract=0,
            licenses_nonbaseline=0,
            rejected=1,
            governance_status=GovernanceStatus.REJECTED_ROUTE,
        ),
    ]


def run_sympy_checks(requirements, routes):
    required_fields = len(requirements)
    licensed_nonbaseline = sum(route.licenses_nonbaseline for route in routes if not route.rejected)
    adopted_nonbaseline_axioms = [
        route.route_id
        for route in routes
        if route.satisfies_contract and route.licenses_nonbaseline and not route.rejected
    ]
    rejected_routes = sum(route.rejected for route in routes)
    open_axiom_routes = sum(
        1
        for route in routes
        if route.governance_status == GovernanceStatus.UNRESOLVED_PROOF_OBLIGATION
    )

    require_true("minimal contract has enough fields", required_fields >= 8)
    require_equal("no nonbaseline axiom is licensed", licensed_nonbaseline, 0)
    require_equal("no adopted nonbaseline axiom exists", len(adopted_nonbaseline_axioms), 0)
    require_true("there are open axiom routes", open_axiom_routes >= 1)
    require_true("post-hoc mechanism axiom is rejected", rejected_routes >= 1)

    return {
        "required_fields": required_fields,
        "licensed_nonbaseline": licensed_nonbaseline,
        "adopted_nonbaseline_axioms": adopted_nonbaseline_axioms,
        "open_axiom_routes": open_axiom_routes,
        "rejected_routes": rejected_routes,
    }


def markdown_requirements(requirements):
    return "\n".join(
        "| {rid} | {req} | {purpose} | {failure} |".format(
            rid=req.requirement_id,
            req=req.requirement,
            purpose=req.purpose,
            failure=req.failure_if_absent,
        )
        for req in requirements
    )


def markdown_routes(routes):
    return "\n".join(
        "| {rid} | {route} | {status} | {missing} | {decision} | {next_obligation} |".format(
            rid=route.route_id,
            route=route.route,
            status=route.contract_status,
            missing=route.missing_items,
            decision=route.decision,
            next_obligation=route.next_obligation,
        )
        for route in routes
    )


def readiness_rows(routes):
    return "\n".join(
        "| {rid} | {satisfies} | {licenses} | {rejected} |".format(
            rid=route.route_id,
            satisfies=bool(route.satisfies_contract),
            licenses=bool(route.licenses_nonbaseline),
            rejected=bool(route.rejected),
        )
        for route in routes
    )


def write_report(requirements, routes, data):
    requirements_md = markdown_requirements(requirements)
    routes_md = markdown_routes(routes)
    readiness_md = readiness_rows(routes)
    adopted = ", ".join(data["adopted_nonbaseline_axioms"]) or "none"
    md = f"""# VacuumForge Minimal Strain Axiom Contract

## Purpose

This report defines the minimum contract for any new strain axiom. It does not
adopt an axiom and does not license a nonbaseline residual.

It depends on:

```text
strain_branch_selector_decision_table_030
```

It satisfies:

```text
minimal_strain_axiom_contract_required_030
```

## Readiness Check

```text
required axiom fields = {data["required_fields"]}
licensed nonbaseline axioms = {data["licensed_nonbaseline"]}
adopted nonbaseline axioms = {adopted}
open axiom routes = {data["open_axiom_routes"]}
rejected routes = {data["rejected_routes"]}
```

## Required Axiom Fields

| requirement id | requirement | purpose | failure if absent |
| --- | --- | --- | --- |
{requirements_md}

## Axiom Route Ledger

| route id | route | contract status | missing items | decision | next obligation |
| --- | --- | --- | --- | --- | --- |
{routes_md}

## Readiness

| route id | satisfies contract | licenses nonbaseline | rejected |
| --- | --- | --- | --- |
{readiness_md}

## Current Conclusion

A new strain axiom is the only disciplined path to nonbaseline vacuum-sector
strain physics after the current gates, but no such axiom is adopted here.
Post-hoc axioms chosen to rescue Lambda, dark-sector, channel, or interior
targets are rejected.

## Classification

```text
result type: minimal strain axiom contract
scope: required interface for any future nonbaseline strain axiom
conclusion: no axiom adopted; nonbaseline strain remains unlicensed
non-conclusion: no no-go theorem against a future explicit axiom
```

The next technical target is:

```text
strain_axiom_candidate_sieve_required_031
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")


def record_archive(ns, routes):
    marker_id = "minimal_strain_axiom_contract_031"
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[sp.Symbol("strain_branch_selector_decision_table_result")],
        output=sp.Symbol("minimal_strain_axiom_contract_result"),
        method="VacuumForge axiom interface ledger with readiness count checks",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        is_placeholder=False,
        scope="Minimal contract for any future strain axiom",
    )

    for route in routes:
        ns.record_claim(
            ClaimRecord(
                claim_id=f"minimal_strain_axiom_route_{route.route_id}_031",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=route.governance_status,
                statement=f"{route.route_id}: {route.decision}",
                derivation_ids=[marker_id],
                obligation_ids=["strain_axiom_candidate_sieve_required_031"],
            )
        )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="minimal_strain_axiom_contract_required_030",
            script_id=SCRIPT_ID,
            title="Write a minimal strain axiom contract",
            status=ObligationStatus.SATISFIED,
            required_by=["030_strain_branch_selector_decision_table__strain_branch_selector_decision_table"],
            satisfied_by=[SCRIPT_ID],
            description=(
                "Satisfied by defining the minimum interface for any new "
                "strain axiom and rejecting post-hoc mechanism-fit axioms."
            ),
        )
    )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="strain_axiom_candidate_sieve_required_031",
            script_id=SCRIPT_ID,
            title="Apply a candidate sieve to possible strain axiom routes",
            status=ObligationStatus.OPEN,
            required_by=[SCRIPT_ID],
            description=(
                "Evaluate whether any candidate axiom route supplies the "
                "required fields without relabeling GR, importing side-ledger "
                "targets, or violating residual gates."
            ),
        )
    )


def main() -> None:
    header("Vacuum Sector 031: Minimal Strain Axiom Contract")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    requirements = axiom_requirements()
    routes = axiom_routes()
    data = run_sympy_checks(requirements, routes)

    out = ScriptOutput()
    for route in routes:
        if route.rejected:
            status = StatusMark.FAIL
        elif route.governance_status == GovernanceStatus.LICENSED_CLAIM:
            status = StatusMark.PASS
        elif route.governance_status == GovernanceStatus.UNRESOLVED_PROOF_OBLIGATION:
            status = StatusMark.OBLIGATION
        else:
            status = StatusMark.DEFER
        with out.governance_assessments():
            out.line(route.route_id, status, route.decision)
    with out.unresolved_obligations():
        out.line(
            "Strain axiom candidate sieve required",
            StatusMark.OBLIGATION,
            "test whether any candidate axiom route can satisfy the contract",
        )

    record_archive(ns, routes)
    ns.write_run_metadata()
    write_report(requirements, routes, data)

    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
