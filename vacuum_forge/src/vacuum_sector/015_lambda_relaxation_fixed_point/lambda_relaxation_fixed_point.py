#!/usr/bin/env python3
"""
lambda_relaxation_fixed_point.py

VacuumForge-managed probe for relaxation/fixed-point Lambda selectors.

This is not a derivation of a nonzero cosmological constant. It tests whether
simple relaxation dynamics select zero, import a target value, or inherit a
scale from their kernel/domain coefficients.

Output:
    theory_v3/development/vacuum_sector/04_lambda_baseline/
        lambda_relaxation_fixed_point_probe_vacuumforge.md
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
    / "lambda_relaxation_fixed_point_probe_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "lambda_measure_identity_probe_014",
        "014_lambda_measure_identity__lambda_measure_identity",
        "lambda_measure_identity_probe_014",
    )
]


@dataclass(frozen=True)
class RelaxationProbe:
    probe_id: str
    dynamics: str
    fixed_point: str
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
    t, gamma, Lambda0, Lambda_star = sp.symbols("t gamma Lambda0 Lambda_star", positive=True)
    Lambda = sp.symbols("Lambda", real=True)
    beta, sigma, L = sp.symbols("beta sigma L", positive=True)

    zero_relax_solution = Lambda0 * sp.exp(-gamma * t)
    zero_relax_limit = sp.limit(zero_relax_solution, t, sp.oo)
    zero_relax_residual = simplify_expr(sp.diff(zero_relax_solution, t) + gamma * zero_relax_solution)

    target_solution = Lambda_star + (Lambda0 - Lambda_star) * sp.exp(-gamma * t)
    target_limit = sp.limit(target_solution, t, sp.oo)
    target_residual = simplify_expr(sp.diff(target_solution, t) + gamma * (target_solution - Lambda_star))

    scale_target = sigma / L**2
    scale_solution = scale_target + (Lambda0 - scale_target) * sp.exp(-gamma * t)
    scale_limit = sp.limit(scale_solution, t, sp.oo)

    nonlinear_flow = -gamma * Lambda + beta * Lambda**2
    nonlinear_fixed_points = sp.solve(sp.Eq(nonlinear_flow, 0), Lambda)
    nonzero_nonlinear_fixed = gamma / beta
    nonlinear_stability_zero = simplify_expr(sp.diff(nonlinear_flow, Lambda).subs(Lambda, 0))
    nonlinear_stability_nonzero = simplify_expr(sp.diff(nonlinear_flow, Lambda).subs(Lambda, nonzero_nonlinear_fixed))

    require_equal("zero relaxation solves ODE", zero_relax_residual, 0)
    require_equal("zero relaxation fixed point", zero_relax_limit, 0)
    require_equal("target relaxation solves ODE", target_residual, 0)
    require_equal("target relaxation fixed point", target_limit, Lambda_star)
    require_equal("scale relaxation fixed point", scale_limit, scale_target)
    require_true("scale relaxation imports L", scale_limit.has(L))
    require_true("target relaxation imports Lambda_star", target_limit.has(Lambda_star))
    require_true("nonlinear fixed points include zero", 0 in nonlinear_fixed_points)
    require_true("nonlinear fixed points include gamma/beta", nonzero_nonlinear_fixed in nonlinear_fixed_points)
    require_equal("zero fixed point linear stability", nonlinear_stability_zero, -gamma)
    require_equal("nonzero fixed point stability imports coefficients", nonlinear_stability_nonzero, gamma)

    probes = [
        RelaxationProbe(
            probe_id="zero_relaxation",
            dynamics="dLambda/dt = -gamma Lambda",
            fixed_point=f"Lambda -> {sp.sstr(zero_relax_limit)}",
            source_of_scale="none",
            disposition="selects Lambda = 0",
            next_obligation="do not infer nonzero floor from scale-free damping",
        ),
        RelaxationProbe(
            probe_id="target_relaxation",
            dynamics="dLambda/dt = -gamma (Lambda - Lambda_star)",
            fixed_point=f"Lambda -> {sp.sstr(target_limit)}",
            source_of_scale="imported target Lambda_star",
            disposition="selects the supplied target, not a derived value",
            next_obligation="derive Lambda_star before claiming selection",
        ),
        RelaxationProbe(
            probe_id="domain_scale_relaxation",
            dynamics="dLambda/dt = -gamma (Lambda - sigma/L^2)",
            fixed_point=f"Lambda -> {sp.sstr(scale_limit)}",
            source_of_scale="domain length L and dimensionless sigma",
            disposition="nonzero floor inherits a supplied domain scale",
            next_obligation="derive L from admissibility, measure, or microphysics",
        ),
        RelaxationProbe(
            probe_id="nonlinear_self_fixed_point",
            dynamics="dLambda/dt = -gamma Lambda + beta Lambda^2",
            fixed_point=f"Lambda = 0 or Lambda = {sp.sstr(nonzero_nonlinear_fixed)}",
            source_of_scale="coefficient ratio gamma/beta",
            disposition="nonzero fixed point is coefficient-derived only if gamma/beta is derived",
            next_obligation="derive coefficients and prove stable physical branch before use",
        ),
    ]

    return {
        "zero_relax_solution": zero_relax_solution,
        "zero_relax_limit": zero_relax_limit,
        "target_solution": target_solution,
        "target_limit": target_limit,
        "scale_solution": scale_solution,
        "scale_limit": scale_limit,
        "nonlinear_flow": nonlinear_flow,
        "nonlinear_fixed_points": nonlinear_fixed_points,
        "nonlinear_stability_zero": nonlinear_stability_zero,
        "nonlinear_stability_nonzero": nonlinear_stability_nonzero,
        "probes": probes,
    }


def markdown_rows(probes):
    return "\n".join(
        "| {probe_id} | {dynamics} | {fixed_point} | {source_of_scale} | {disposition} | {next_obligation} |".format(
            probe_id=probe.probe_id,
            dynamics=probe.dynamics,
            fixed_point=probe.fixed_point,
            source_of_scale=probe.source_of_scale,
            disposition=probe.disposition,
            next_obligation=probe.next_obligation,
        )
        for probe in probes
    )


def write_report(data):
    rows = markdown_rows(data["probes"])
    fixed_points = ", ".join(sp.sstr(point) for point in data["nonlinear_fixed_points"])
    md = f"""# VacuumForge Lambda Relaxation/Fixed-Point Probe

## Purpose

This report tests whether relaxation/fixed-point dynamics can select a nonzero
`Lambda` floor without target insertion. It does not derive the observed
cosmological constant.

This report depends on:

```text
lambda_measure_identity_probe_014
```

It satisfies:

```text
lambda_relaxation_fixed_point_probe_required_014
```

## Symbolic Checks

Scale-free damping:

```text
Lambda(t) = {sp.sstr(data["zero_relax_solution"])}
limit = {sp.sstr(data["zero_relax_limit"])}
```

Target relaxation:

```text
Lambda(t) = {sp.sstr(data["target_solution"])}
limit = {sp.sstr(data["target_limit"])}
```

Domain-scale relaxation:

```text
Lambda(t) = {sp.sstr(data["scale_solution"])}
limit = {sp.sstr(data["scale_limit"])}
```

Nonlinear self-fixed-point flow:

```text
flow = {sp.sstr(data["nonlinear_flow"])}
fixed points = {fixed_points}
linearized derivative at zero = {sp.sstr(data["nonlinear_stability_zero"])}
linearized derivative at nonzero point = {sp.sstr(data["nonlinear_stability_nonzero"])}
```

## Probe Ledger

| probe | dynamics | fixed point | source of scale | disposition | next obligation |
| --- | --- | --- | --- | --- | --- |
{rows}

## Current Conclusion

Relaxation dynamics can select zero without an extra scale. Nonzero fixed
points appear only when the dynamics import a target, domain length, kernel
scale, or coefficient ratio. Such a route becomes a Lambda selector only after
that scale and the conservation law are derived by the vacuum ontology.

The clean split is:

```text
dLambda/dt = -gamma Lambda:
  selects Lambda = 0

dLambda/dt = -gamma (Lambda - Lambda_star):
  imports Lambda_star

dLambda/dt = -gamma (Lambda - sigma/L^2):
  imports L

nonlinear fixed point:
  imports coefficient ratio unless coefficients are derived
```

## Classification

```text
result type: Lambda relaxation/fixed-point probe
scope: relaxation dynamics as Lambda baseline selectors
conclusion: nonzero relaxation floors require a derived target, scale, or coefficient ratio
non-conclusion: no nonzero Lambda value is derived; microphysical floor routes are not yet tested
```

The next technical target is:

```text
lambda_frustration_floor_microphysics_probe_required_015
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")


def record_archive(ns, probes):
    marker_id = "lambda_relaxation_fixed_point_probe_015"
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[sp.Symbol("lambda_measure_identity_probe_result")],
        output=sp.Symbol("lambda_relaxation_fixed_point_probe_result"),
        method="SymPy relaxation solution and fixed-point checks for Lambda selectors",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        is_placeholder=False,
        scope="Relaxation/fixed-point dynamics as Lambda baseline selectors",
    )

    for probe in probes:
        status = GovernanceStatus.POLICY_RULE if probe.probe_id == "zero_relaxation" else GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
        ns.record_claim(
            ClaimRecord(
                claim_id=f"lambda_relaxation_probe_{probe.probe_id}_015",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=status,
                statement=f"{probe.probe_id}: {probe.disposition}",
                derivation_ids=[marker_id],
                obligation_ids=["lambda_frustration_floor_microphysics_probe_required_015"],
            )
        )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="lambda_relaxation_fixed_point_probe_required_014",
            script_id=SCRIPT_ID,
            title="Test relaxation/fixed-point routes as Lambda selectors",
            status=ObligationStatus.SATISFIED,
            required_by=["014_lambda_measure_identity__lambda_measure_identity"],
            satisfied_by=[SCRIPT_ID],
            description=(
                "Satisfied by checking that scale-free relaxation selects zero "
                "and nonzero fixed points import a target, domain scale, or "
                "coefficient ratio unless further derived."
            ),
        )
    )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="lambda_frustration_floor_microphysics_probe_required_015",
            script_id=SCRIPT_ID,
            title="Test frustration-floor microphysics as a Lambda selector",
            status=ObligationStatus.OPEN,
            required_by=[SCRIPT_ID],
            description=(
                "Relaxation routes need a derived scale. Test whether a "
                "microphysical frustration floor derives the absolute constant "
                "offset, equation of state, and non-clustering ledger."
            ),
        )
    )


def main() -> None:
    header("Vacuum Sector 015: Lambda Relaxation/Fixed-Point Probe")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    data = run_sympy_checks()

    out = ScriptOutput()
    for probe in data["probes"]:
        status = StatusMark.DEFER
        if probe.probe_id == "zero_relaxation":
            status = StatusMark.PASS
        with out.governance_assessments():
            out.line(probe.probe_id, status, probe.disposition)
    with out.unresolved_obligations():
        out.line(
            "Lambda frustration-floor microphysics probe required",
            StatusMark.OBLIGATION,
            "test whether microphysics derives the absolute floor rather than a potential shape",
        )

    record_archive(ns, data["probes"])
    ns.write_run_metadata()
    write_report(data)

    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
