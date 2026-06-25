#!/usr/bin/env python3
"""
lambda_variational_minimum_probe.py

VacuumForge-managed probe for the Lambda variational-minimum selector.

This is not a derivation of a nonzero cosmological constant. It tests selector
functionals F(Lambda), not variation of the full EH action with respect to
Lambda. The question is whether a bare variational minimum over Lambda selects
a nonzero value without an imported bias, target, boundary class, or
microphysical scale.

Output:
    theory_v3/development/vacuum_sector/04_lambda_baseline/
        lambda_variational_minimum_probe_vacuumforge.md
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
    / "lambda_variational_minimum_probe_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "lambda_selector_sieve_010",
        "010_lambda_selector_sieve__lambda_selector_sieve",
        "lambda_selector_sieve_010",
    )
]


@dataclass(frozen=True)
class VariationalProbe:
    probe_id: str
    selector_functional: str
    stationarity_result: str
    source_of_scale: str
    disposition: str
    next_obligation: str


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


def run_sympy_checks():
    Lambda = sp.symbols("Lambda", real=True)
    a = sp.symbols("a", positive=True)
    b, Lambda_star, c = sp.symbols("b Lambda_star c", real=True)

    free_selector = c
    free_derivative = simplify_expr(sp.diff(free_selector, Lambda))

    no_scale_convex = a * Lambda**2 / 2
    no_scale_derivative = simplify_expr(sp.diff(no_scale_convex, Lambda))
    no_scale_stationary = sp.solve(sp.Eq(no_scale_derivative, 0), Lambda)[0]
    no_scale_second = simplify_expr(sp.diff(no_scale_convex, Lambda, 2))

    linear_selector = b * Lambda
    linear_derivative = simplify_expr(sp.diff(linear_selector, Lambda))

    biased_convex = a * Lambda**2 / 2 + b * Lambda
    biased_derivative = simplify_expr(sp.diff(biased_convex, Lambda))
    biased_stationary = sp.solve(sp.Eq(biased_derivative, 0), Lambda)[0]
    biased_second = simplify_expr(sp.diff(biased_convex, Lambda, 2))

    target_selector = a * (Lambda - Lambda_star) ** 2 / 2
    target_derivative = simplify_expr(sp.diff(target_selector, Lambda))
    target_stationary = sp.solve(sp.Eq(target_derivative, 0), Lambda)[0]
    target_second = simplify_expr(sp.diff(target_selector, Lambda, 2))

    require_equal("Lambda-independent selector imposes no equation", free_derivative, 0)
    require_equal("no-scale convex selector stationary point", no_scale_stationary, 0)
    require_equal("no-scale convex second derivative", no_scale_second, a)
    require_equal("linear selector has no stationary point for nonzero b", linear_derivative, b)
    require_equal("biased convex stationary point", biased_stationary, -b / a)
    require_equal("biased convex second derivative", biased_second, a)
    require_equal("biased convex returns zero without bias", biased_stationary.subs(b, 0), 0)
    require_equal("biased stationary value depends on imported bias", sp.diff(biased_stationary, b), -1 / a)
    require_equal("target selector stationary point", target_stationary, Lambda_star)
    require_equal("target selector second derivative", target_second, a)
    require_equal("target stationary value depends on target", sp.diff(target_stationary, Lambda_star), 1)
    require_true("positive curvature of convex probes is explicit", no_scale_second == biased_second == target_second)

    probes = [
        VariationalProbe(
            probe_id="lambda_independent_selector",
            selector_functional=f"F = {sp.sstr(free_selector)}",
            stationarity_result="dF/dLambda = 0 identically; Lambda remains free",
            source_of_scale="none",
            disposition="does not select a value",
            next_obligation="supply an actual selector equation or boundary condition",
        ),
        VariationalProbe(
            probe_id="no_scale_convex_minimum",
            selector_functional=f"F = {sp.sstr(no_scale_convex)}",
            stationarity_result=f"Lambda = {sp.sstr(no_scale_stationary)}",
            source_of_scale="none; only positive stiffness a",
            disposition="selects Lambda = 0, not nonzero Lambda",
            next_obligation="nonzero value requires a bias, target, boundary class, or new scale",
        ),
        VariationalProbe(
            probe_id="linear_bias_no_minimum",
            selector_functional=f"F = {sp.sstr(linear_selector)}",
            stationarity_result=f"dF/dLambda = {sp.sstr(linear_derivative)}",
            source_of_scale="imported linear bias b",
            disposition="no interior stationary point for nonzero b on an unconstrained continuous domain",
            next_obligation="add a boundary/admissibility domain, dynamics, or stabilizing term before claiming a minimum",
        ),
        VariationalProbe(
            probe_id="biased_convex_minimum",
            selector_functional=f"F = {sp.sstr(biased_convex)}",
            stationarity_result=f"Lambda = {sp.sstr(biased_stationary)}",
            source_of_scale="imported bias b and stiffness a",
            disposition="nonzero value is inherited from imported coefficients",
            next_obligation="derive b/a from vacuum ontology before using the value",
        ),
        VariationalProbe(
            probe_id="target_inserted_minimum",
            selector_functional=f"F = {sp.sstr(target_selector)}",
            stationarity_result=f"Lambda = {sp.sstr(target_stationary)}",
            source_of_scale="imported target Lambda_star",
            disposition="selects the supplied target, not a derived value",
            next_obligation="do not treat target insertion as a selector derivation",
        ),
    ]

    return {
        "free_derivative": free_derivative,
        "no_scale_derivative": no_scale_derivative,
        "no_scale_stationary": no_scale_stationary,
        "no_scale_second": no_scale_second,
        "linear_derivative": linear_derivative,
        "biased_derivative": biased_derivative,
        "biased_stationary": biased_stationary,
        "biased_second": biased_second,
        "target_derivative": target_derivative,
        "target_stationary": target_stationary,
        "target_second": target_second,
        "probes": probes,
    }


def markdown_rows(probes):
    return "\n".join(
        "| {probe_id} | {selector_functional} | {stationarity_result} | {source_of_scale} | {disposition} | {next_obligation} |".format(
            probe_id=probe.probe_id,
            selector_functional=probe.selector_functional,
            stationarity_result=probe.stationarity_result,
            source_of_scale=probe.source_of_scale,
            disposition=probe.disposition,
            next_obligation=probe.next_obligation,
        )
        for probe in probes
    )


def write_report(data):
    probes = data["probes"]
    rows = markdown_rows(probes)
    md = f"""# VacuumForge Lambda Variational-Minimum Probe

## Purpose

This report tests the variational-minimum Lambda selector opened by the
selector sieve. It tests selector functionals `F(Lambda)`, not variation of
the full EH action with respect to `Lambda`. It does not derive the observed
cosmological constant. It asks whether a bare stationarity/minimum principle
over `Lambda` selects a nonzero value before a bias, target, boundary class,
or microphysical scale is supplied.

This report depends on:

```text
lambda_selector_sieve_010
```

It satisfies:

```text
lambda_variational_minimum_probe_required_010
```

## Symbolic Checks

SymPy checks five selector prototypes.

No selector object:

```text
dF/dLambda = {sp.sstr(data["free_derivative"])}
```

No-scale convex minimum:

```text
dF/dLambda = {sp.sstr(data["no_scale_derivative"])}
Lambda_*   = {sp.sstr(data["no_scale_stationary"])}
d2F/dLambda2 = {sp.sstr(data["no_scale_second"])}
```

Linear bias without stabilizing dynamics:

```text
dF/dLambda = {sp.sstr(data["linear_derivative"])}
```

This means no interior stationary point on an unconstrained continuous
`Lambda` domain for nonzero `b`. A boundary extremum would belong to the
boundary/admissibility probe, not to this bare variational probe.

Biased convex minimum:

```text
dF/dLambda = {sp.sstr(data["biased_derivative"])}
Lambda_*   = {sp.sstr(data["biased_stationary"])}
d2F/dLambda2 = {sp.sstr(data["biased_second"])}
```

Target-inserted minimum:

```text
dF/dLambda = {sp.sstr(data["target_derivative"])}
Lambda_*   = {sp.sstr(data["target_stationary"])}
d2F/dLambda2 = {sp.sstr(data["target_second"])}
```

## Probe Ledger

| probe | selector functional | stationarity result | source of scale | disposition | next obligation |
| --- | --- | --- | --- | --- | --- |
{rows}

## Current Conclusion

A bare variational-minimum selector does not currently derive a nonzero
`Lambda`. The available outcomes are:

```text
no selector object: Lambda remains free;
no-scale convex minimum: Lambda = 0;
linear bias alone: no interior stationary point on an unconstrained domain;
biased convex minimum: nonzero Lambda inherits imported b/a;
target minimum: nonzero Lambda is inserted as Lambda_star.
```

Therefore the variational-minimum route is not mechanism-ready as a derived
nonzero baseline. It can be reopened only after the project supplies the
missing source of scale: a boundary/admissibility class, a global constraint, a
measure identity, relaxation dynamics, or microphysical floor.

## Provenance

This agrees with the older Lambda branch-selector status:

```text
zero Lambda is selected by asymptotically flat finite-flux boundary data;
constant nonzero Lambda is allowed but not selected by the local metric branch;
cancellation or nonzero targeting is tuning unless a dynamics or selector
equation supplies it.
```

## Classification

```text
result type: variational-minimum selector probe
scope: Lambda baseline selection before boundary, measure, relaxation, or microphysics
conclusion: variational minimum alone does not derive nonzero Lambda
non-conclusion: no global no-go theorem against nonzero Lambda; no other selector class is killed
```

The next technical target is:

```text
lambda_boundary_admissibility_probe_required_011
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")


def record_archive(ns, probes):
    marker_id = "lambda_variational_minimum_probe_011"
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[sp.Symbol("lambda_selector_sieve_result")],
        output=sp.Symbol("lambda_variational_minimum_probe_result"),
        method="SymPy stationarity checks for bare, biased, and target-inserted Lambda selector functionals",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        is_placeholder=False,
        scope="Variational-minimum Lambda baseline selector before additional scale input",
    )

    for probe in probes:
        ns.record_claim(
            ClaimRecord(
                claim_id=f"lambda_variational_probe_{probe.probe_id}_011",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
                statement=(
                    f"{probe.probe_id}: {probe.disposition}. Source of scale: "
                    f"{probe.source_of_scale}."
                ),
                derivation_ids=[marker_id],
                obligation_ids=["lambda_boundary_admissibility_probe_required_011"],
            )
        )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="lambda_variational_minimum_probe_required_010",
            script_id=SCRIPT_ID,
            title="Test the variational-minimum Lambda selector first",
            status=ObligationStatus.SATISFIED,
            required_by=["010_lambda_selector_sieve__lambda_selector_sieve"],
            satisfied_by=[SCRIPT_ID],
            description=(
                "Satisfied by stationarity checks showing that a bare "
                "variational minimum selects zero, leaves Lambda free, or "
                "imports the nonzero scale."
            ),
        )
    )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="lambda_boundary_admissibility_probe_required_011",
            script_id=SCRIPT_ID,
            title="Test the boundary/admissibility Lambda selector",
            status=ObligationStatus.OPEN,
            required_by=[SCRIPT_ID],
            description=(
                "The variational-minimum route needs an external scale or "
                "selector equation. Test whether boundary/admissibility data "
                "can supply a nonzero baseline without observed-value insertion."
            ),
        )
    )


def main() -> None:
    header("Vacuum Sector 011: Lambda Variational-Minimum Probe")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    data = run_sympy_checks()

    out = ScriptOutput()
    for probe in data["probes"]:
        with out.governance_assessments():
            out.line(probe.probe_id, StatusMark.DEFER, probe.disposition)
    with out.unresolved_obligations():
        out.line(
            "Lambda boundary/admissibility probe required",
            StatusMark.OBLIGATION,
            "test whether boundary data can supply the missing nonzero scale",
        )

    record_archive(ns, data["probes"])
    ns.write_run_metadata()
    write_report(data)

    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
