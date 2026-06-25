#!/usr/bin/env python3
"""
lambda_topology_global_constraint.py

VacuumForge-managed probe for topology/global constraints as Lambda selectors.

This is not a derivation of a nonzero cosmological constant. It tests whether
dimensionless topology can set a dimensionful Lambda value without an imported
area, volume, length, measure, or quantization scale.

Output:
    theory_v3/development/vacuum_sector/04_lambda_baseline/
        lambda_topology_global_constraint_probe_vacuumforge.md
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
    / "lambda_topology_global_constraint_probe_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "lambda_boundary_admissibility_probe_012",
        "012_lambda_boundary_admissibility__lambda_boundary_admissibility",
        "lambda_boundary_admissibility_probe_012",
    )
]


@dataclass(frozen=True)
class TopologyProbe:
    probe_id: str
    global_data: str
    relation: str
    dimension_result: str
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
    chi, A, V, Lambda, q, L = sp.symbols("chi A V Lambda q L", positive=True)

    # Dimension exponents in powers of length L.
    dim_chi = sp.Integer(0)
    dim_lambda = sp.Integer(-2)
    dim_area = sp.Integer(2)
    dim_volume = sp.Integer(4)
    topology_only_dimension_residual = dim_lambda - dim_chi

    curvature_2d = sp.solve(sp.Eq(sp.Symbol("R") * A, 4 * sp.pi * chi), sp.Symbol("R"))[0]
    dim_curvature_from_area = dim_chi - dim_area

    gb_density_4d = sp.Rational(8, 3) * Lambda**2
    lambda_squared_from_volume = sp.solve(sp.Eq(gb_density_4d * V, 32 * sp.pi**2 * chi), Lambda**2)[0]
    dim_lambda_squared_from_volume = dim_chi - dim_volume

    quantized_length_relation = q / L**2
    dim_quantized_length_relation = -2

    require_equal("topology alone has no Lambda dimension", topology_only_dimension_residual, -2)
    require_equal("2D Gauss-Bonnet curvature relation", curvature_2d, 4 * sp.pi * chi / A)
    require_equal("2D curvature dimension supplied by area", dim_curvature_from_area, -2)
    require_equal("4D Lambda-square relation", lambda_squared_from_volume, 12 * sp.pi**2 * chi / V)
    require_equal("4D Lambda-square dimension supplied by volume", dim_lambda_squared_from_volume, -4)
    require_equal("quantized relation dimension", dim_quantized_length_relation, dim_lambda)
    require_true("2D relation imports area", curvature_2d.has(A))
    require_true("4D relation imports volume", lambda_squared_from_volume.has(V))
    require_true("quantized relation imports length", quantized_length_relation.has(L))

    probes = [
        TopologyProbe(
            probe_id="topology_only_dimension_check",
            global_data="Euler/topology invariant chi only",
            relation="Lambda = f(chi)",
            dimension_result="dimension mismatch: chi has L^0 while Lambda has L^-2",
            disposition="topology alone cannot set a dimensionful Lambda value",
            next_obligation="supply area, volume, length, measure, or microphysical scale",
        ),
        TopologyProbe(
            probe_id="two_dimensional_gauss_bonnet",
            global_data="2D Euler characteristic plus area A",
            relation=f"R = {sp.sstr(curvature_2d)}",
            dimension_result="area A supplies the L^-2 curvature scale",
            disposition="topology constrains curvature only after area is supplied",
            next_obligation="derive A before claiming a curvature value",
        ),
        TopologyProbe(
            probe_id="four_dimensional_constant_curvature_gb",
            global_data="4D Euler characteristic plus volume V",
            relation=f"Lambda^2 = {sp.sstr(lambda_squared_from_volume)}",
            dimension_result="volume V supplies L^-4 for Lambda^2; sign remains open",
            disposition="topology constrains magnitude only after volume is supplied",
            next_obligation="derive V and sign selector before claiming Lambda",
        ),
        TopologyProbe(
            probe_id="quantized_length_rule",
            global_data="dimensionless quantum number q plus length L",
            relation=f"Lambda = {sp.sstr(quantized_length_relation)}",
            dimension_result="length L supplies L^-2",
            disposition="global quantization can label sectors but still imports a length scale",
            next_obligation="derive L or route to measure/admissibility selector",
        ),
    ]

    return {
        "topology_only_dimension_residual": topology_only_dimension_residual,
        "curvature_2d": curvature_2d,
        "dim_curvature_from_area": dim_curvature_from_area,
        "gb_density_4d": gb_density_4d,
        "lambda_squared_from_volume": lambda_squared_from_volume,
        "dim_lambda_squared_from_volume": dim_lambda_squared_from_volume,
        "quantized_length_relation": quantized_length_relation,
        "probes": probes,
    }


def markdown_rows(probes):
    return "\n".join(
        "| {probe_id} | {global_data} | {relation} | {dimension_result} | {disposition} | {next_obligation} |".format(
            probe_id=probe.probe_id,
            global_data=probe.global_data,
            relation=probe.relation,
            dimension_result=probe.dimension_result,
            disposition=probe.disposition,
            next_obligation=probe.next_obligation,
        )
        for probe in probes
    )


def write_report(data):
    rows = markdown_rows(data["probes"])
    md = f"""# VacuumForge Lambda Topology/Global Constraint Probe

## Purpose

This report tests whether topology/global constraints can set a dimensionful
`Lambda` value. It does not derive the observed cosmological constant.

This report depends on:

```text
lambda_boundary_admissibility_probe_012
```

It satisfies:

```text
lambda_topology_global_constraint_probe_required_012
```

## Symbolic Checks

Topology alone:

```text
dim(chi) = L^0
dim(Lambda) = L^-2
dimension residual = {sp.sstr(data["topology_only_dimension_residual"])}
```

2D Gauss-Bonnet with supplied area:

```text
integral R dA = 4*pi*chi
R = {sp.sstr(data["curvature_2d"])}
dim(R) from area = L^{sp.sstr(data["dim_curvature_from_area"])}
```

4D constant-curvature Gauss-Bonnet with supplied volume:

```text
E = {sp.sstr(data["gb_density_4d"])}
E V = 32*pi^2 chi
Lambda^2 = {sp.sstr(data["lambda_squared_from_volume"])}
dim(Lambda^2) from volume = L^{sp.sstr(data["dim_lambda_squared_from_volume"])}
```

Global quantization with supplied length:

```text
Lambda = {sp.sstr(data["quantized_length_relation"])}
```

## Probe Ledger

| probe | global data | relation | dimension result | disposition | next obligation |
| --- | --- | --- | --- | --- | --- |
{rows}

## Current Conclusion

Topology and global constraints can restrict allowed sectors, and they can
relate `Lambda` to area, volume, length, or measure data. They do not by
themselves derive a dimensionful `Lambda` value.

The clean split is:

```text
topology alone:
  dimensionless; cannot set Lambda

topology plus area/volume/length:
  constrains curvature or Lambda magnitude after a scale is supplied

constant-curvature 4D topology:
  relates Lambda^2 V to chi; volume and sign still need selectors
```

## Classification

```text
result type: Lambda topology/global constraint probe
scope: topology/global data as Lambda baseline selector
conclusion: topology constrains sectors but needs a dimensionful scale to set Lambda
non-conclusion: no nonzero Lambda value is derived; measure identity has not yet been tested
```

The next technical target is:

```text
lambda_measure_identity_probe_required_013
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")


def record_archive(ns, probes):
    marker_id = "lambda_topology_global_constraint_probe_013"
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[sp.Symbol("lambda_boundary_admissibility_probe_result")],
        output=sp.Symbol("lambda_topology_global_constraint_probe_result"),
        method="SymPy dimensional and Gauss-Bonnet checks for topology/global Lambda constraints",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        is_placeholder=False,
        scope="Topology/global constraints as Lambda baseline selectors",
    )

    for probe in probes:
        ns.record_claim(
            ClaimRecord(
                claim_id=f"lambda_topology_probe_{probe.probe_id}_013",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
                statement=f"{probe.probe_id}: {probe.disposition}",
                derivation_ids=[marker_id],
                obligation_ids=["lambda_measure_identity_probe_required_013"],
            )
        )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="lambda_topology_global_constraint_probe_required_012",
            script_id=SCRIPT_ID,
            title="Test topology/global constraints as Lambda selectors",
            status=ObligationStatus.SATISFIED,
            required_by=["012_lambda_boundary_admissibility__lambda_boundary_admissibility"],
            satisfied_by=[SCRIPT_ID],
            description=(
                "Satisfied by dimensional and Gauss-Bonnet checks showing "
                "that topology constrains Lambda only after a dimensionful "
                "scale such as area, volume, or length is supplied."
            ),
        )
    )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="lambda_measure_identity_probe_required_013",
            script_id=SCRIPT_ID,
            title="Test measure identity as a Lambda selector",
            status=ObligationStatus.OPEN,
            required_by=[SCRIPT_ID],
            description=(
                "Topology/global constraints need a dimensionful scale. Test "
                "whether a measure identity can supply a conserved density or "
                "curvature scale without observed-value insertion."
            ),
        )
    )


def main() -> None:
    header("Vacuum Sector 013: Lambda Topology/Global Constraint Probe")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    data = run_sympy_checks()

    out = ScriptOutput()
    for probe in data["probes"]:
        with out.governance_assessments():
            out.line(probe.probe_id, StatusMark.DEFER, probe.disposition)
    with out.unresolved_obligations():
        out.line(
            "Lambda measure identity probe required",
            StatusMark.OBLIGATION,
            "test whether measure data can supply the missing dimensionful scale",
        )

    record_archive(ns, data["probes"])
    ns.write_run_metadata()
    write_report(data)

    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
