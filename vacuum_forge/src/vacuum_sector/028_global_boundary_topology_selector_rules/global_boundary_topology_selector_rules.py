#!/usr/bin/env python3
"""
global_boundary_topology_selector_rules.py

VacuumForge-managed consolidation of global, boundary, topology, and
admissibility selector rules.

This is not a new Lambda or interior mechanism. It records the cross-cutting
missing-scale rule exposed by the Lambda and interior probes.

Output:
    theory_v3/development/vacuum_sector/04_lambda_baseline/
        global_boundary_topology_selector_rules_vacuumforge.md
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
    / "global_boundary_topology_selector_rules_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "finite_strain_admissibility_probe_027",
        "027_finite_strain_admissibility_probe__finite_strain_admissibility_probe",
        "finite_strain_admissibility_probe_027",
    )
]


@dataclass(frozen=True)
class SelectorRule:
    rule_id: str
    selector: str
    supplies_sector: str
    supplies_scale: str
    dimensionful_value: str
    disposition: str
    next_obligation: str
    constrains_sector: int
    derives_scale: int
    derives_value: int
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


def selector_rules():
    return [
        SelectorRule(
            rule_id="topology_only",
            selector="dimensionless topology or sector label",
            supplies_sector="yes",
            supplies_scale="no",
            dimensionful_value="not derived",
            disposition="constrains sectors only",
            next_obligation="supply area, volume, measure, or admissibility scale before value claims",
            constrains_sector=1,
            derives_scale=0,
            derives_value=0,
        ),
        SelectorRule(
            rule_id="topology_plus_measure",
            selector="topology plus derived measure/volume",
            supplies_sector="yes",
            supplies_scale="only if measure is derived",
            dimensionful_value="candidate if sign and scale are supplied",
            disposition="deferred pending measure derivation",
            next_obligation="derive measure/volume and sign selector",
            constrains_sector=1,
            derives_scale=0,
            derives_value=0,
        ),
        SelectorRule(
            rule_id="boundary_admissibility_scale",
            selector="boundary or admissibility class with derived length/area/volume",
            supplies_sector="yes",
            supplies_scale="only if boundary scale is selected by ontology",
            dimensionful_value="candidate after scale derivation",
            disposition="deferred pending boundary-scale selector",
            next_obligation="derive boundary/admissibility scale before value claims",
            constrains_sector=1,
            derives_scale=0,
            derives_value=0,
        ),
        SelectorRule(
            rule_id="observed_value_backsolve",
            selector="choose scale to match observed Lambda or compactness",
            supplies_sector="fit only",
            supplies_scale="observed value inserted",
            dimensionful_value="backsolved",
            disposition="rejected as observed-value insertion",
            next_obligation="do not use as derivation",
            constrains_sector=0,
            derives_scale=0,
            derives_value=0,
            rejected=1,
        ),
    ]


def run_sympy_checks(rules):
    chi, A, V = sp.symbols("chi A V", positive=True)
    Lambda = sp.symbols("Lambda")
    R_2d = 4 * sp.pi * chi / A
    E_4d = 32 * sp.pi**2 * chi / V
    Lambda_sq_from_gb = sp.solve(sp.Eq(sp.Rational(8, 3) * Lambda**2, E_4d), Lambda**2)[0]

    require_equal("2D curvature needs area", R_2d * A, 4 * sp.pi * chi)
    require_equal("4D GB Lambda square needs volume", Lambda_sq_from_gb, 12 * sp.pi**2 * chi / V)
    require_true("2D curvature value depends on area", R_2d.has(A))
    require_true("4D Lambda value depends on volume", Lambda_sq_from_gb.has(V))

    live_rules = [
        rule.rule_id
        for rule in rules
        if rule.constrains_sector and rule.derives_scale and rule.derives_value and not rule.rejected
    ]
    require_equal("no selector rule derives a value yet", len(live_rules), 0)

    return {
        "R_2d": R_2d,
        "E_4d": E_4d,
        "Lambda_sq_from_gb": Lambda_sq_from_gb,
        "live_rules": live_rules,
    }


def markdown_rules(rules):
    return "\n".join(
        (
            "| {rule_id} | {selector} | {supplies_sector} | {supplies_scale} | "
            "{dimensionful_value} | {disposition} | {next_obligation} |"
        ).format(
            rule_id=rule.rule_id,
            selector=rule.selector,
            supplies_sector=rule.supplies_sector,
            supplies_scale=rule.supplies_scale,
            dimensionful_value=rule.dimensionful_value,
            disposition=rule.disposition,
            next_obligation=rule.next_obligation,
        )
        for rule in rules
    )


def readiness_rows(rules):
    return "\n".join(
        "| {rule_id} | {constrains_sector} | {derives_scale} | {derives_value} | {live} |".format(
            rule_id=rule.rule_id,
            constrains_sector=bool(rule.constrains_sector),
            derives_scale=bool(rule.derives_scale),
            derives_value=bool(rule.derives_value),
            live=bool(rule.constrains_sector and rule.derives_scale and rule.derives_value and not rule.rejected),
        )
        for rule in rules
    )


def write_report(rules, data):
    rules_md = markdown_rules(rules)
    readiness_md = readiness_rows(rules)
    md = f"""# VacuumForge Global/Boundary/Topology Selector Rules

## Purpose

This report consolidates the cross-cutting selector rule exposed by the Lambda
and interior-cap probes. It does not derive a nonzero Lambda value, a topology
selector, or an interior cap.

This report depends on:

```text
finite_strain_admissibility_probe_027
```

It satisfies:

```text
global_boundary_topology_selector_rules_required_027
```

## Symbolic Checks

Two-dimensional topology relation:

```text
R = {sp.sstr(data["R_2d"])}
R * A = 4*pi*chi
```

Four-dimensional constant-curvature Gauss-Bonnet proxy:

```text
E = {sp.sstr(data["E_4d"])}
Lambda^2 = {sp.sstr(data["Lambda_sq_from_gb"])}
```

Topology can supply dimensionless sector information. A dimensionful local
value still needs area, volume, measure, length, or an admissibility scale.

## Selector Rule Ledger

| rule | selector | supplies sector | supplies scale | dimensionful value | disposition | next obligation |
| --- | --- | --- | --- | --- | --- | --- |
{rules_md}

## Readiness

| rule | constrains sector | derives scale | derives value | live value selector |
| --- | --- | --- | --- | --- |
{readiness_md}

## Current Conclusion

Global, boundary, topology, and admissibility selectors can restrict sectors
or admissible classes, but they do not set dimensionful values unless the
missing scale is also derived. Observed-value backsolves are rejected.

## Classification

```text
result type: cross-cutting selector rule
scope: Lambda, topology, boundary, measure, and interior admissibility selectors
conclusion: sector selection is not value selection without a derived scale
non-conclusion: no no-go theorem against global or topological selectors
```

The next technical target is:

```text
vacuum_sector_program_checkpoint_required_028
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")


def record_archive(ns, rules):
    marker_id = "global_boundary_topology_selector_rules_028"
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[sp.Symbol("finite_strain_admissibility_result")],
        output=sp.Symbol("global_boundary_topology_selector_rules_result"),
        method="SymPy topology/measure dimensional selector audit",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        is_placeholder=False,
        scope="Cross-cutting global, boundary, topology, and admissibility selector rules",
    )

    for rule in rules:
        status = (
            GovernanceStatus.REJECTED_ROUTE
            if rule.rejected
            else GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
        )
        ns.record_claim(
            ClaimRecord(
                claim_id=f"global_boundary_topology_rule_{rule.rule_id}_028",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=status,
                statement=f"{rule.rule_id}: {rule.disposition}",
                derivation_ids=[marker_id],
                obligation_ids=["vacuum_sector_program_checkpoint_required_028"],
            )
        )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="global_boundary_topology_selector_rules_required_027",
            script_id=SCRIPT_ID,
            title="Consolidate global, boundary, and topology selector rules",
            status=ObligationStatus.SATISFIED,
            required_by=["027_finite_strain_admissibility_probe__finite_strain_admissibility_probe"],
            satisfied_by=[SCRIPT_ID],
            description=(
                "Satisfied by recording that topology, boundary, measure, and "
                "admissibility data can constrain sectors but require a derived "
                "scale before setting dimensionful values."
            ),
        )
    )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="vacuum_sector_program_checkpoint_required_028",
            script_id=SCRIPT_ID,
            title="Checkpoint the vacuum-sector program before opening new branches",
            status=ObligationStatus.OPEN,
            required_by=[SCRIPT_ID],
            description=(
                "After completing the first sweep through residuals, Lambda, "
                "dark excess, non-gravitational channels, interiors, and "
                "cross-cutting selectors, summarize remaining live openings "
                "before starting new branch mechanisms."
            ),
        )
    )


def main() -> None:
    header("Vacuum Sector 028: Global/Boundary/Topology Selector Rules")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    rules = selector_rules()
    data = run_sympy_checks(rules)

    out = ScriptOutput()
    for rule in rules:
        status = StatusMark.FAIL if rule.rejected else StatusMark.DEFER
        with out.governance_assessments():
            out.line(rule.rule_id, status, rule.disposition)
    with out.unresolved_obligations():
        out.line(
            "Vacuum-sector program checkpoint required",
            StatusMark.OBLIGATION,
            "summarize remaining live openings before new branch mechanisms",
        )

    record_archive(ns, rules)
    ns.write_run_metadata()
    write_report(rules, data)

    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
