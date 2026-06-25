#!/usr/bin/env python3
"""
strain_branch_selector_decision_table.py

VacuumForge-managed decision table for strain-branch selector routes.

This is not a new strain axiom and not a candidate residual. It records what
would count as a selector for X, neighboring mismatch, and K_strain after the
first vacuum-sector program checkpoint.

Output:
    theory_v3/development/vacuum_sector/01_strain_functional/
        strain_branch_selector_decision_table_vacuumforge.md
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
    / "strain_branch_selector_decision_table_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "vacuum_sector_program_checkpoint_029",
        "029_vacuum_sector_program_checkpoint__vacuum_sector_program_checkpoint",
        "vacuum_sector_program_checkpoint_029",
    )
]


@dataclass(frozen=True)
class SelectorRoute:
    route_id: str
    selector_route: str
    selects_x: str
    selects_mismatch: str
    selects_action: str
    evidence_required: str
    current_status: str
    decision: str
    next_obligation: str
    specifies_x: int
    specifies_mismatch: int
    specifies_action: int
    passes_gates: int
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


def selector_routes():
    return [
        SelectorRoute(
            route_id="accumulated_gate_closure",
            selector_route="accumulated gates force the EH/GHY branch",
            selects_x="metric data g_ab",
            selects_mismatch="Levi-Civita metric comparison",
            selects_action="EH bulk plus GHY boundary",
            evidence_required="already conditional on metric compatibility, diffeomorphism invariance, locality, no extra fields, and boundary differentiability",
            current_status="operational baseline closure",
            decision="admissible only as epsilon = 0 baseline",
            next_obligation="do not treat this as a nonbaseline vacuum ontology",
            specifies_x=1,
            specifies_mismatch=1,
            specifies_action=1,
            passes_gates=1,
            licenses_nonbaseline=0,
            governance_status=GovernanceStatus.LICENSED_CLAIM,
        ),
        SelectorRoute(
            route_id="explicit_new_strain_axiom",
            selector_route="adopt a new primitive strain-selection axiom",
            selects_x="must name X and its metric reduction",
            selects_mismatch="must name neighboring comparison",
            selects_action="must state invariant, boundary term, and variational rule",
            evidence_required="postulate text, independence from killed routes, residual gates, falsifier",
            current_status="not adopted",
            decision="only possible route to disciplined nonbaseline selector",
            next_obligation="write minimal strain axiom contract before any mechanism use",
            specifies_x=0,
            specifies_mismatch=0,
            specifies_action=0,
            passes_gates=0,
            licenses_nonbaseline=0,
            governance_status=GovernanceStatus.UNRESOLVED_PROOF_OBLIGATION,
        ),
        SelectorRoute(
            route_id="nonlocal_relaxation_selector",
            selector_route="nonlocal relaxation chooses comparison or strain class",
            selects_x="not specified",
            selects_mismatch="kernel/global history candidate only",
            selects_action="not locally closed",
            evidence_required="kernel, conservation law, local GR limit, hyperbolicity route, source quarantine",
            current_status="deferred",
            decision="not a local strain selector until local limit and gates are supplied",
            next_obligation="route through explicit axiom or large-scale/nonlocal ledger",
            specifies_x=0,
            specifies_mismatch=1,
            specifies_action=0,
            passes_gates=0,
            licenses_nonbaseline=0,
            governance_status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        ),
        SelectorRoute(
            route_id="boundary_global_selector",
            selector_route="boundary, topology, or admissibility data select strain class",
            selects_x="not specified",
            selects_mismatch="can restrict classes only",
            selects_action="not determined without local invariant and scale",
            evidence_required="derived scale plus local variational object",
            current_status="sector selector only",
            decision="cannot select K_strain by itself",
            next_obligation="supply local strain object before value/action claims",
            specifies_x=0,
            specifies_mismatch=0,
            specifies_action=0,
            passes_gates=0,
            licenses_nonbaseline=0,
            governance_status=GovernanceStatus.POLICY_RULE,
        ),
        SelectorRoute(
            route_id="silent_ontology",
            selector_route="ontology carries no operative strain selector",
            selects_x="may remain philosophical or latent",
            selects_mismatch="none",
            selects_action="none beyond baseline",
            evidence_required="explicit silence rule and no residual predictions",
            current_status="allowed null route",
            decision="predicts no nonbaseline residual",
            next_obligation="retain beta/residual silence unless axiom is added",
            specifies_x=0,
            specifies_mismatch=0,
            specifies_action=0,
            passes_gates=1,
            licenses_nonbaseline=0,
            governance_status=GovernanceStatus.POLICY_RULE,
        ),
        SelectorRoute(
            route_id="metric_only_relabeling",
            selector_route="declare X = g_ab and infer EH/GHY by notation",
            selects_x="metric by assertion",
            selects_mismatch="Levi-Civita by assertion",
            selects_action="EH/GHY by assertion",
            evidence_required="would need independent selector rather than relabeling",
            current_status="rejected as derivation",
            decision="baseline can be used, but relabeling is not ontology selection",
            next_obligation="do not count as vacuum-sector derivation",
            specifies_x=1,
            specifies_mismatch=1,
            specifies_action=1,
            passes_gates=0,
            licenses_nonbaseline=0,
            rejected=1,
            governance_status=GovernanceStatus.REJECTED_ROUTE,
        ),
        SelectorRoute(
            route_id="side_ledger_backdoor",
            selector_route="use Lambda, dark excess, channels, or interiors to choose K_strain after the fact",
            selects_x="chosen to fit target",
            selects_mismatch="chosen to fit target",
            selects_action="chosen to fit target",
            evidence_required="would need prior strain selector and source ledger",
            current_status="rejected as wrong-ledger move",
            decision="side ledgers cannot select strain dynamics retroactively",
            next_obligation="route side mechanisms only after strain selector exists",
            specifies_x=0,
            specifies_mismatch=0,
            specifies_action=0,
            passes_gates=0,
            licenses_nonbaseline=0,
            rejected=1,
            governance_status=GovernanceStatus.REJECTED_ROUTE,
        ),
    ]


def run_sympy_checks(routes):
    licensed_nonbaseline = sum(route.licenses_nonbaseline for route in routes if not route.rejected)
    complete_and_passed = [
        route.route_id
        for route in routes
        if (
            route.specifies_x
            and route.specifies_mismatch
            and route.specifies_action
            and route.passes_gates
            and not route.rejected
        )
    ]
    rejected_routes = sum(route.rejected for route in routes)
    open_axiom_routes = sum(
        1
        for route in routes
        if route.governance_status == GovernanceStatus.UNRESOLVED_PROOF_OBLIGATION
    )

    require_equal("no nonbaseline selector is licensed", licensed_nonbaseline, 0)
    require_true("EH/GHY baseline is the only complete passed selector", complete_and_passed == ["accumulated_gate_closure"])
    require_true("at least one bad selector route is rejected", rejected_routes >= 1)
    require_true("explicit axiom route remains open", open_axiom_routes == 1)

    return {
        "licensed_nonbaseline": licensed_nonbaseline,
        "complete_and_passed": complete_and_passed,
        "rejected_routes": rejected_routes,
        "open_axiom_routes": open_axiom_routes,
        "current_licensed_epsilon": sp.Integer(0),
    }


def markdown_routes(routes):
    return "\n".join(
        (
            "| {route_id} | {selector_route} | {selects_x} | {selects_mismatch} | "
            "{selects_action} | {current_status} | {decision} | {next_obligation} |"
        ).format(
            route_id=route.route_id,
            selector_route=route.selector_route,
            selects_x=route.selects_x,
            selects_mismatch=route.selects_mismatch,
            selects_action=route.selects_action,
            current_status=route.current_status,
            decision=route.decision,
            next_obligation=route.next_obligation,
        )
        for route in routes
    )


def readiness_rows(routes):
    return "\n".join(
        (
            "| {route_id} | {specifies_x} | {specifies_mismatch} | {specifies_action} | "
            "{passes_gates} | {licenses_nonbaseline} | {rejected} |"
        ).format(
            route_id=route.route_id,
            specifies_x=bool(route.specifies_x),
            specifies_mismatch=bool(route.specifies_mismatch),
            specifies_action=bool(route.specifies_action),
            passes_gates=bool(route.passes_gates),
            licenses_nonbaseline=bool(route.licenses_nonbaseline),
            rejected=bool(route.rejected),
        )
        for route in routes
    )


def write_report(routes, data):
    route_md = markdown_routes(routes)
    readiness_md = readiness_rows(routes)
    md = f"""# VacuumForge Strain-Branch Selector Decision Table

## Purpose

This report returns the vacuum-sector program to the central selector problem:
what chooses `X`, neighboring mismatch, and `K_strain`?

It depends on:

```text
vacuum_sector_program_checkpoint_029
```

It satisfies:

```text
strain_branch_selector_decision_table_required_029
```

## Symbolic Readiness Check

```text
licensed nonbaseline selectors = {data["licensed_nonbaseline"]}
complete passed selector routes = {", ".join(data["complete_and_passed"])}
rejected selector routes = {data["rejected_routes"]}
open explicit-axiom routes = {data["open_axiom_routes"]}
current licensed epsilon = {sp.sstr(data["current_licensed_epsilon"])}
```

The only complete passed route in the table is the accumulated-gate closure to
the EH/GHY baseline. It licenses the baseline at `epsilon = 0`; it does not
license a nonbaseline vacuum-sector residual.

## Decision Table

| route id | selector route | selects X | selects mismatch | selects action | current status | decision | next obligation |
| --- | --- | --- | --- | --- | --- | --- | --- |
{route_md}

## Readiness

| route id | specifies X | specifies mismatch | specifies action | passes gates | licenses nonbaseline | rejected |
| --- | --- | --- | --- | --- | --- | --- |
{readiness_md}

## Current Conclusion

The program has two disciplined choices:

```text
1. Treat accumulated gates as the operational selector and stay at epsilon = 0.
2. Adopt an explicit new strain axiom before any nonbaseline mechanism is used.
```

Boundary, topology, Lambda, dark-sector, channel, and interior ledgers cannot
select `K_strain` retroactively. They may constrain or motivate later work only
after a strain selector exists.

## Classification

```text
result type: strain selector decision table
scope: X, neighboring mismatch, and K_strain selection routes
conclusion: no nonbaseline selector is adopted; explicit axiom route is the open path
non-conclusion: no global no-go theorem against future strain axioms
```

The next technical target is:

```text
minimal_strain_axiom_contract_required_030
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")


def record_archive(ns, routes):
    marker_id = "strain_branch_selector_decision_table_030"
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[sp.Symbol("vacuum_sector_program_checkpoint_result")],
        output=sp.Symbol("strain_branch_selector_decision_table_result"),
        method="VacuumForge selector-route readiness ledger with SymPy count checks",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        is_placeholder=False,
        scope="Strain-branch selector decision table after program checkpoint",
    )

    for route in routes:
        ns.record_claim(
            ClaimRecord(
                claim_id=f"strain_selector_route_{route.route_id}_030",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=route.governance_status,
                statement=f"{route.route_id}: {route.decision}",
                derivation_ids=[marker_id],
                obligation_ids=["minimal_strain_axiom_contract_required_030"],
            )
        )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="strain_branch_selector_decision_table_required_029",
            script_id=SCRIPT_ID,
            title="Build a strain-branch selector decision table",
            status=ObligationStatus.SATISFIED,
            required_by=["029_vacuum_sector_program_checkpoint__vacuum_sector_program_checkpoint"],
            satisfied_by=[SCRIPT_ID],
            description=(
                "Satisfied by comparing accumulated-gate closure, explicit "
                "new axiom, nonlocal, boundary/global, silent, relabeling, "
                "and side-ledger selector routes."
            ),
        )
    )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="minimal_strain_axiom_contract_required_030",
            script_id=SCRIPT_ID,
            title="Write a minimal strain axiom contract",
            status=ObligationStatus.OPEN,
            required_by=[SCRIPT_ID],
            description=(
                "If the program wants anything beyond the accumulated-gate "
                "EH/GHY closure, the next step is a minimal axiom contract "
                "that names X, neighboring mismatch, K_strain, boundary data, "
                "gate routing, and kill conditions before mechanism use."
            ),
        )
    )


def main() -> None:
    header("Vacuum Sector 030: Strain-Branch Selector Decision Table")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    routes = selector_routes()
    data = run_sympy_checks(routes)

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
            "Minimal strain axiom contract required",
            StatusMark.OBLIGATION,
            "needed before any nonbaseline mechanism can be treated as physics",
        )

    record_archive(ns, routes)
    ns.write_run_metadata()
    write_report(routes, data)

    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
