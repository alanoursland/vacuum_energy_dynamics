#!/usr/bin/env python3
"""
lambda_frustration_floor_microphysics.py

VacuumForge-managed probe for frustration-floor microphysics as a Lambda
selector.

This is not a derivation of a nonzero cosmological constant. It tests whether
a microphysical potential shape derives the absolute constant floor, or merely
leaves an offset that must be supplied by another selector.

Output:
    theory_v3/development/vacuum_sector/04_lambda_baseline/
        lambda_frustration_floor_microphysics_probe_vacuumforge.md
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
    / "lambda_frustration_floor_microphysics_probe_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "lambda_relaxation_fixed_point_probe_015",
        "015_lambda_relaxation_fixed_point__lambda_relaxation_fixed_point",
        "lambda_relaxation_fixed_point_probe_015",
    )
]


@dataclass(frozen=True)
class MicrophysicsProbe:
    probe_id: str
    candidate_object: str
    symbolic_result: str
    source_ledger: str
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
    phi = sp.symbols("phi", real=True)
    lam, v, V0, rho_obs = sp.symbols("lambda_f v V0 rho_obs", positive=True)

    potential = lam * (phi**2 - v**2) ** 2 / 4 + V0
    first_derivative = simplify_expr(sp.diff(potential, phi))
    second_derivative = simplify_expr(sp.diff(potential, phi, 2))

    minimum_value_plus = simplify_expr(potential.subs(phi, v))
    minimum_value_minus = simplify_expr(potential.subs(phi, -v))
    maximum_value = simplify_expr(potential.subs(phi, 0))
    mass_squared_at_minimum = simplify_expr(second_derivative.subs(phi, v))
    curvature_at_origin = simplify_expr(second_derivative.subs(phi, 0))

    zero_offset_floor = minimum_value_plus.subs(V0, 0)
    target_offset_floor = minimum_value_plus.subs(V0, rho_obs)
    pressure_floor = -minimum_value_plus
    equation_of_state_residual = simplify_expr(pressure_floor + minimum_value_plus)

    fluctuation = sp.symbols("delta_phi", real=True)
    quadratic_excitation_energy = simplify_expr(mass_squared_at_minimum * fluctuation**2 / 2)

    require_equal("Landau first derivative", first_derivative, lam * phi * (phi**2 - v**2))
    require_equal("minimum value at plus v", minimum_value_plus, V0)
    require_equal("minimum value at minus v", minimum_value_minus, V0)
    require_equal("origin value", maximum_value, V0 + lam * v**4 / 4)
    require_equal("mass squared at minimum", mass_squared_at_minimum, 2 * lam * v**2)
    require_equal("curvature at origin", curvature_at_origin, -lam * v**2)
    require_equal("zero offset gives zero floor", zero_offset_floor, 0)
    require_equal("target offset gives target floor", target_offset_floor, rho_obs)
    require_equal("constant floor has w=-1 pressure residual", equation_of_state_residual, 0)
    require_true("excitation energy is not constant floor", quadratic_excitation_energy.has(fluctuation))

    probes = [
        MicrophysicsProbe(
            probe_id="no_microphysical_variable",
            candidate_object="no microstate variable or coarse-graining map",
            symbolic_result="no floor equation",
            source_ledger="undetermined",
            disposition="cannot select Lambda",
            next_obligation="state microstate variable before claiming microphysical floor",
        ),
        MicrophysicsProbe(
            probe_id="landau_shape_with_free_offset",
            candidate_object=f"V(phi) = {sp.sstr(potential)}",
            symbolic_result=f"V(+/-v) = {sp.sstr(minimum_value_plus)}",
            source_ledger="absolute offset V0 is free",
            disposition="potential shape does not derive the absolute floor",
            next_obligation="derive V0 before using it as Lambda",
        ),
        MicrophysicsProbe(
            probe_id="zero_offset_floor",
            candidate_object="same potential with V0 = 0",
            symbolic_result=f"floor = {sp.sstr(zero_offset_floor)}",
            source_ledger="zero floor",
            disposition="selects no nonzero Lambda",
            next_obligation="do not infer nonzero floor from symmetry breaking alone",
        ),
        MicrophysicsProbe(
            probe_id="target_offset_floor",
            candidate_object="same potential with V0 = rho_obs",
            symbolic_result=f"floor = {sp.sstr(target_offset_floor)}",
            source_ledger="observed-value insertion",
            disposition="not a derivation",
            next_obligation="reject unless rho_obs is independently derived",
        ),
        MicrophysicsProbe(
            probe_id="constant_floor_equation_of_state",
            candidate_object="constant floor stress ledger",
            symbolic_result="p + rho = 0",
            source_ledger="Lambda floor candidate only after V0 is derived",
            disposition="w = -1 ledger is necessary but not sufficient",
            next_obligation="derive V0 and prove non-clustering",
        ),
        MicrophysicsProbe(
            probe_id="massive_excitation_excess",
            candidate_object="fluctuations around the minimum",
            symbolic_result=f"quadratic excitation energy = {sp.sstr(quadratic_excitation_energy)}",
            source_ledger="transportable excitation/excess sector",
            disposition="route to dark-sector or particle/defect ledger, not Lambda",
            next_obligation="separate excitations from constant floor",
        ),
    ]

    return {
        "potential": potential,
        "first_derivative": first_derivative,
        "second_derivative": second_derivative,
        "minimum_value_plus": minimum_value_plus,
        "minimum_value_minus": minimum_value_minus,
        "maximum_value": maximum_value,
        "mass_squared_at_minimum": mass_squared_at_minimum,
        "curvature_at_origin": curvature_at_origin,
        "zero_offset_floor": zero_offset_floor,
        "target_offset_floor": target_offset_floor,
        "equation_of_state_residual": equation_of_state_residual,
        "quadratic_excitation_energy": quadratic_excitation_energy,
        "probes": probes,
    }


def markdown_rows(probes):
    return "\n".join(
        "| {probe_id} | {candidate_object} | {symbolic_result} | {source_ledger} | {disposition} | {next_obligation} |".format(
            probe_id=probe.probe_id,
            candidate_object=probe.candidate_object,
            symbolic_result=probe.symbolic_result,
            source_ledger=probe.source_ledger,
            disposition=probe.disposition,
            next_obligation=probe.next_obligation,
        )
        for probe in probes
    )


def write_report(data):
    rows = markdown_rows(data["probes"])
    md = f"""# VacuumForge Lambda Frustration-Floor Microphysics Probe

## Purpose

This report tests whether microphysical frustration or a potential shape
derives an absolute constant `Lambda` floor. It does not derive the observed
cosmological constant.

This report depends on:

```text
lambda_relaxation_fixed_point_probe_015
```

It satisfies:

```text
lambda_frustration_floor_microphysics_probe_required_015
```

## Symbolic Checks

Landau-style shape:

```text
V(phi) = {sp.sstr(data["potential"])}
dV/dphi = {sp.sstr(data["first_derivative"])}
d2V/dphi2 = {sp.sstr(data["second_derivative"])}
V(+v) = {sp.sstr(data["minimum_value_plus"])}
V(-v) = {sp.sstr(data["minimum_value_minus"])}
V(0) = {sp.sstr(data["maximum_value"])}
mass^2 at minimum = {sp.sstr(data["mass_squared_at_minimum"])}
curvature at origin = {sp.sstr(data["curvature_at_origin"])}
```

Offset checks:

```text
V0 = 0 floor = {sp.sstr(data["zero_offset_floor"])}
V0 = rho_obs floor = {sp.sstr(data["target_offset_floor"])}
p + rho for constant floor = {sp.sstr(data["equation_of_state_residual"])}
quadratic excitation energy = {sp.sstr(data["quadratic_excitation_energy"])}
```

## Probe Ledger

| probe | candidate object | symbolic result | source ledger | disposition | next obligation |
| --- | --- | --- | --- | --- | --- |
{rows}

## Current Conclusion

Microphysical potential shape is not enough to derive a nonzero `Lambda`
baseline. A Landau-style potential can provide minima, excitations, and a
constant-floor ledger, but the absolute offset `V0` remains free unless the
microphysics derives it. Setting `V0 = 0` gives no nonzero floor. Setting
`V0 = rho_obs` inserts the target. Excitations around the floor are not the
constant Lambda baseline and must be routed to dark-sector or particle/defect
ledgers.

The clean split is:

```text
potential shape:
  derives minima and excitation scale, not absolute floor

constant offset V0:
  Lambda candidate only if derived before observation

fluctuations/excitations:
  transportable excess, not Lambda
```

## Classification

```text
result type: Lambda frustration-floor microphysics probe
scope: microphysical potentials as Lambda baseline selectors
conclusion: microphysics must derive the absolute constant offset before it selects Lambda
non-conclusion: no nonzero Lambda value is derived; dark-sector excess is not yet developed
```

The next technical target is:

```text
dark_excess_source_ledger_required_016
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")


def record_archive(ns, probes):
    marker_id = "lambda_frustration_floor_microphysics_probe_016"
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[sp.Symbol("lambda_relaxation_fixed_point_probe_result")],
        output=sp.Symbol("lambda_frustration_floor_microphysics_probe_result"),
        method="SymPy potential-minimum, offset, equation-of-state, and excitation checks",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        is_placeholder=False,
        scope="Microphysical frustration floors as Lambda baseline selectors",
    )

    for probe in probes:
        status = GovernanceStatus.CANDIDATE_ROUTE if probe.probe_id == "constant_floor_equation_of_state" else GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
        ns.record_claim(
            ClaimRecord(
                claim_id=f"lambda_microphysics_probe_{probe.probe_id}_016",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=status,
                statement=f"{probe.probe_id}: {probe.disposition}",
                derivation_ids=[marker_id],
                obligation_ids=["dark_excess_source_ledger_required_016"],
            )
        )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="lambda_frustration_floor_microphysics_probe_required_015",
            script_id=SCRIPT_ID,
            title="Test frustration-floor microphysics as a Lambda selector",
            status=ObligationStatus.SATISFIED,
            required_by=["015_lambda_relaxation_fixed_point__lambda_relaxation_fixed_point"],
            satisfied_by=[SCRIPT_ID],
            description=(
                "Satisfied by potential-minimum checks showing that a shape "
                "can supply minima and excitations but not the absolute floor "
                "unless the offset is derived."
            ),
        )
    )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="dark_excess_source_ledger_required_016",
            script_id=SCRIPT_ID,
            title="Open dark-sector excess source ledger",
            status=ObligationStatus.OPEN,
            required_by=[SCRIPT_ID],
            description=(
                "Lambda floor probes separate constant floors from "
                "transportable excitations. Open the dark-sector ledger to "
                "classify excess equations of state, conservation, clustering, "
                "and source bookkeeping."
            ),
        )
    )


def main() -> None:
    header("Vacuum Sector 016: Lambda Frustration-Floor Microphysics Probe")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    data = run_sympy_checks()

    out = ScriptOutput()
    for probe in data["probes"]:
        status = StatusMark.DEFER
        if probe.probe_id == "constant_floor_equation_of_state":
            status = StatusMark.OBLIGATION
        with out.governance_assessments():
            out.line(probe.probe_id, status, probe.disposition)
    with out.unresolved_obligations():
        out.line(
            "Dark excess source ledger required",
            StatusMark.OBLIGATION,
            "separate transportable excitations/excess from the Lambda floor",
        )

    record_archive(ns, data["probes"])
    ns.write_run_metadata()
    write_report(data)

    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
