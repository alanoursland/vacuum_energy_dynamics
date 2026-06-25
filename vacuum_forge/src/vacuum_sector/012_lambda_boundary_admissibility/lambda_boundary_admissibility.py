#!/usr/bin/env python3
"""
lambda_boundary_admissibility.py

VacuumForge-managed probe for the Lambda boundary/admissibility selector.

This is not a derivation of a nonzero cosmological constant. It tests whether
explicit boundary or admissibility data can select Lambda without importing a
length, radius, volume, or asymptotic class.

Output:
    theory_v3/development/vacuum_sector/04_lambda_baseline/
        lambda_boundary_admissibility_probe_vacuumforge.md
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
    / "lambda_boundary_admissibility_probe_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "lambda_variational_minimum_probe_011",
        "011_lambda_variational_minimum_probe__lambda_variational_minimum_probe",
        "lambda_variational_minimum_probe_011",
    )
]


@dataclass(frozen=True)
class BoundaryProbe:
    probe_id: str
    boundary_data: str
    relation: str
    selected_quantity: str
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
    r, M = sp.symbols("r M", positive=True)
    Lambda = sp.symbols("Lambda", real=True)
    L, Rb, V, chi = sp.symbols("L R_b V chi", positive=True)

    phi = -M / r - Lambda * r**2 / 6
    radial_field = simplify_expr(-sp.diff(phi, r))
    flux = simplify_expr(r**2 * radial_field)
    flux_derivative = simplify_expr(sp.diff(flux, r))
    lambda_from_finite_flux = sp.solve(sp.Eq(flux_derivative, 0), Lambda)[0]

    de_sitter_relation = sp.solve(sp.Eq(1 - Lambda * L**2 / 3, 0), Lambda)[0]
    anti_de_sitter_relation = -3 / L**2

    gauss_bonnet_density = sp.Rational(8, 3) * Lambda**2
    gauss_bonnet_integral = gauss_bonnet_density * V
    lambda_squared_from_gb = sp.solve(sp.Eq(gauss_bonnet_integral, 32 * sp.pi**2 * chi), Lambda**2)[0]

    horizon_relation = sp.solve(sp.Eq(1 - Lambda * Rb**2 / 3, 0), Lambda)[0]

    require_equal("radial Lambda flux derivative", flux_derivative, Lambda * r**2)
    require_equal("finite flat flux selects Lambda zero", lambda_from_finite_flux, 0)
    require_equal("de Sitter radius relation", de_sitter_relation, 3 / L**2)
    require_equal("anti-de Sitter radius relation sign", anti_de_sitter_relation, -3 / L**2)
    require_equal("Gauss-Bonnet constant-curvature density", gauss_bonnet_density, sp.Rational(8, 3) * Lambda**2)
    require_equal("Gauss-Bonnet Lambda-square relation", lambda_squared_from_gb, 12 * sp.pi**2 * chi / V)
    require_equal("horizon boundary radius relation", horizon_relation, 3 / Rb**2)
    require_true("de Sitter relation imports L", de_sitter_relation.has(L))
    require_true("Gauss-Bonnet relation imports V", lambda_squared_from_gb.has(V))
    require_true("horizon relation imports boundary radius", horizon_relation.has(Rb))

    probes = [
        BoundaryProbe(
            probe_id="asymptotically_flat_finite_flux",
            boundary_data="finite radius-independent scalar flux at infinity",
            relation=f"d(r^2 F)/dr = {sp.sstr(flux_derivative)}",
            selected_quantity=f"Lambda = {sp.sstr(lambda_from_finite_flux)}",
            source_of_scale="no nonzero background scale supplied",
            disposition="selects Lambda = 0 within the asymptotically flat scalar bridge",
            next_obligation="do not infer observed nonzero Lambda from this sector",
        ),
        BoundaryProbe(
            probe_id="de_sitter_radius_boundary",
            boundary_data="asymptotic de Sitter radius L",
            relation="1 - Lambda L^2 / 3 = 0",
            selected_quantity=f"Lambda = {sp.sstr(de_sitter_relation)}",
            source_of_scale="boundary radius L",
            disposition="converts supplied L into positive Lambda",
            next_obligation="derive L before claiming derived nonzero Lambda",
        ),
        BoundaryProbe(
            probe_id="anti_de_sitter_radius_boundary",
            boundary_data="asymptotic anti-de Sitter radius L",
            relation="curvature scale sign supplied by AdS boundary class",
            selected_quantity=f"Lambda = {sp.sstr(anti_de_sitter_relation)}",
            source_of_scale="boundary radius L and AdS sign class",
            disposition="converts supplied L and sign class into negative Lambda",
            next_obligation="derive L and sign class before claiming derived Lambda",
        ),
        BoundaryProbe(
            probe_id="compact_constant_curvature_gb",
            boundary_data="compact constant-curvature 4D topology and volume",
            relation="(8/3) Lambda^2 V = 32 pi^2 chi",
            selected_quantity=f"Lambda^2 = {sp.sstr(lambda_squared_from_gb)}",
            source_of_scale="volume V; sign still unselected",
            disposition="constrains magnitude when V and chi are supplied",
            next_obligation="derive volume and sign selector before claiming a value",
        ),
        BoundaryProbe(
            probe_id="horizon_domain_radius_boundary",
            boundary_data="domain or horizon radius R_b",
            relation="1 - Lambda R_b^2 / 3 = 0",
            selected_quantity=f"Lambda = {sp.sstr(horizon_relation)}",
            source_of_scale="boundary radius R_b",
            disposition="converts supplied boundary radius into Lambda",
            next_obligation="derive R_b from vacuum admissibility before claiming selection",
        ),
    ]

    return {
        "phi": phi,
        "radial_field": radial_field,
        "flux": flux,
        "flux_derivative": flux_derivative,
        "lambda_from_finite_flux": lambda_from_finite_flux,
        "de_sitter_relation": de_sitter_relation,
        "anti_de_sitter_relation": anti_de_sitter_relation,
        "gauss_bonnet_density": gauss_bonnet_density,
        "lambda_squared_from_gb": lambda_squared_from_gb,
        "horizon_relation": horizon_relation,
        "probes": probes,
    }


def markdown_rows(probes):
    return "\n".join(
        "| {probe_id} | {boundary_data} | {relation} | {selected_quantity} | {source_of_scale} | {disposition} | {next_obligation} |".format(
            probe_id=probe.probe_id,
            boundary_data=probe.boundary_data,
            relation=probe.relation,
            selected_quantity=probe.selected_quantity,
            source_of_scale=probe.source_of_scale,
            disposition=probe.disposition,
            next_obligation=probe.next_obligation,
        )
        for probe in probes
    )


def write_report(data):
    rows = markdown_rows(data["probes"])
    md = f"""# VacuumForge Lambda Boundary/Admissibility Probe

## Purpose

This report tests whether boundary/admissibility data can select a nonzero
`Lambda` baseline without observed-value insertion or local-equation
modification. It does not derive the observed cosmological constant.

This report depends on:

```text
lambda_variational_minimum_probe_011
```

It satisfies:

```text
lambda_boundary_admissibility_probe_required_011
```

## Symbolic Checks

For the asymptotically flat scalar bridge:

```text
Phi = {sp.sstr(data["phi"])}
F_r = {sp.sstr(data["radial_field"])}
r^2 F_r = {sp.sstr(data["flux"])}
d(r^2 F_r)/dr = {sp.sstr(data["flux_derivative"])}
finite-flux Lambda = {sp.sstr(data["lambda_from_finite_flux"])}
```

For supplied constant-curvature boundary scales:

```text
de Sitter radius L:      Lambda = {sp.sstr(data["de_sitter_relation"])}
anti-de Sitter radius L: Lambda = {sp.sstr(data["anti_de_sitter_relation"])}
horizon/domain R_b:      Lambda = {sp.sstr(data["horizon_relation"])}
```

For a compact constant-curvature 4D topology/volume ledger:

```text
Gauss-Bonnet density E = {sp.sstr(data["gauss_bonnet_density"])}
Lambda^2 from E V = 32 pi^2 chi:
  Lambda^2 = {sp.sstr(data["lambda_squared_from_gb"])}
```

## Probe Ledger

| probe | boundary data | relation | selected quantity | source of scale | disposition | next obligation |
| --- | --- | --- | --- | --- | --- | --- |
{rows}

## Current Conclusion

Boundary/admissibility data can select allowed `Lambda` families and can
convert a supplied boundary length, radius, volume, or asymptotic class into a
`Lambda` relation. It does not derive a nonzero value unless the boundary scale
or volume is itself selected by the vacuum ontology.

The clean split is:

```text
asymptotically flat finite-flux data:
  Lambda = 0

de Sitter / anti-de Sitter / horizon data:
  nonzero Lambda inherits a supplied length or radius

compact constant-curvature topology:
  Lambda^2 V is constrained, but V and sign still require selection
```

## Classification

```text
result type: Lambda boundary/admissibility selector probe
scope: boundary data as source of Lambda baseline relations
conclusion: boundary data can convert supplied scales into Lambda, but does not derive the scale
non-conclusion: no nonzero Lambda value is derived; topology/global constraints are not yet fully tested
```

The next technical target is:

```text
lambda_topology_global_constraint_probe_required_012
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")


def record_archive(ns, probes):
    marker_id = "lambda_boundary_admissibility_probe_012"
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[sp.Symbol("lambda_variational_minimum_probe_result")],
        output=sp.Symbol("lambda_boundary_admissibility_probe_result"),
        method="SymPy boundary-scale and Gauss-Bonnet Lambda relation checks",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        is_placeholder=False,
        scope="Boundary/admissibility data as Lambda baseline selector",
    )

    for probe in probes:
        ns.record_claim(
            ClaimRecord(
                claim_id=f"lambda_boundary_probe_{probe.probe_id}_012",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
                statement=(
                    f"{probe.probe_id}: {probe.disposition}. Source of scale: "
                    f"{probe.source_of_scale}."
                ),
                derivation_ids=[marker_id],
                obligation_ids=["lambda_topology_global_constraint_probe_required_012"],
            )
        )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="lambda_boundary_admissibility_probe_required_011",
            script_id=SCRIPT_ID,
            title="Test the boundary/admissibility Lambda selector",
            status=ObligationStatus.SATISFIED,
            required_by=["011_lambda_variational_minimum_probe__lambda_variational_minimum_probe"],
            satisfied_by=[SCRIPT_ID],
            description=(
                "Satisfied by boundary-scale checks showing that nonzero "
                "Lambda requires a supplied boundary scale, volume, or sign "
                "class unless another selector derives it."
            ),
        )
    )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="lambda_topology_global_constraint_probe_required_012",
            script_id=SCRIPT_ID,
            title="Test topology/global constraints as Lambda selectors",
            status=ObligationStatus.OPEN,
            required_by=[SCRIPT_ID],
            description=(
                "Boundary/admissibility can convert supplied scales into "
                "Lambda. Test whether topology/global constraints can supply "
                "a dimensionful value or only constrain it after a volume or "
                "measure is provided."
            ),
        )
    )


def main() -> None:
    header("Vacuum Sector 012: Lambda Boundary/Admissibility Probe")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    data = run_sympy_checks()

    out = ScriptOutput()
    for probe in data["probes"]:
        with out.governance_assessments():
            out.line(probe.probe_id, StatusMark.DEFER, probe.disposition)
    with out.unresolved_obligations():
        out.line(
            "Lambda topology/global constraint probe required",
            StatusMark.OBLIGATION,
            "test whether topology supplies a value or only constrains it after a scale is supplied",
        )

    record_archive(ns, data["probes"])
    ns.write_run_metadata()
    write_report(data)

    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
