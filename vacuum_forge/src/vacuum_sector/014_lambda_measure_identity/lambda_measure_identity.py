#!/usr/bin/env python3
"""
lambda_measure_identity.py

VacuumForge-managed probe for measure identities as Lambda selectors.

This is not a derivation of a nonzero cosmological constant. It tests whether
a measure identity supplies a conserved constant floor, merely fits dimensions,
or actually belongs to the dark-sector excess ledger.

Output:
    theory_v3/development/vacuum_sector/04_lambda_baseline/
        lambda_measure_identity_probe_vacuumforge.md
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
    / "lambda_measure_identity_probe_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "lambda_topology_global_constraint_probe_013",
        "013_lambda_topology_global_constraint__lambda_topology_global_constraint",
        "lambda_topology_global_constraint_probe_013",
    )
]


@dataclass(frozen=True)
class MeasureProbe:
    probe_id: str
    candidate_identity: str
    conservation_face: str
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
    a, rho0, kappa = sp.symbols("a rho0 kappa", positive=True)
    L, C = sp.symbols("L C", positive=True)

    dim_rho = sp.Integer(-4)
    dim_kappa = sp.Integer(2)
    dim_lambda = sp.Integer(-2)
    dimension_balance = dim_kappa + dim_rho - dim_lambda

    dimensional_fit = C / L**2

    rho_floor = rho0 * a**0
    lambda_floor = kappa * rho_floor
    lambda_floor_derivative = simplify_expr(sp.diff(lambda_floor, a))

    rho_dust = rho0 / a**3
    lambda_dust = kappa * rho_dust
    lambda_dust_derivative = simplify_expr(sp.diff(lambda_dust, a))

    rho_string = rho0 / a**2
    lambda_string_derivative = simplify_expr(sp.diff(kappa * rho_string, a))

    w = sp.symbols("w", real=True)
    rho_w = rho0 * a ** (-3 * (1 + w))
    rho_w_floor = simplify_expr(rho_w.subs(w, -1))
    rho_w_dust = simplify_expr(rho_w.subs(w, 0))
    rho_w_wall = simplify_expr(rho_w.subs(w, sp.Rational(-2, 3)))

    require_equal("kappa rho dimension matches Lambda", dimension_balance, 0)
    require_true("dimensional fit imports L", dimensional_fit.has(L))
    require_equal("w=-1 floor density is constant", rho_w_floor, rho0)
    require_equal("w=0 dust density scales as a^-3", rho_w_dust, rho0 / a**3)
    require_equal("w=-2/3 wall density scales as a^-1", rho_w_wall, rho0 / a)
    require_equal("constant floor Lambda derivative", lambda_floor_derivative, 0)
    require_equal("dust-like Lambda derivative is nonzero expression", lambda_dust_derivative, -3 * kappa * rho0 / a**4)
    require_equal("string-like Lambda derivative is nonzero expression", lambda_string_derivative, -2 * kappa * rho0 / a**3)

    probes = [
        MeasureProbe(
            probe_id="no_measure_identity",
            candidate_identity="no measure identity is written",
            conservation_face="none",
            source_ledger="undetermined",
            disposition="cannot select Lambda",
            next_obligation="write a covariant identity before claiming a measure-derived value",
        ),
        MeasureProbe(
            probe_id="dimensional_fit",
            candidate_identity=f"Lambda = {sp.sstr(dimensional_fit)}",
            conservation_face="constant if L is supplied",
            source_ledger="observed or imported length scale unless L is derived",
            disposition="dimensionally valid but not a derivation",
            next_obligation="derive L or reject as dimensional fitting",
        ),
        MeasureProbe(
            probe_id="conserved_vacuum_density_floor",
            candidate_identity=f"Lambda = {sp.sstr(lambda_floor)}",
            conservation_face="w = -1 gives constant rho and constant Lambda",
            source_ledger="Lambda floor candidate if rho0 is derived before observation",
            disposition="candidate only after the measure derives rho0",
            next_obligation="derive rho0 and prove covariant conservation",
        ),
        MeasureProbe(
            probe_id="dustlike_measure_excess",
            candidate_identity=f"Lambda(a) = {sp.sstr(lambda_dust)}",
            conservation_face="w = 0 gives a^-3 scaling and dLambda/da != 0",
            source_ledger="dark-sector excess, not constant Lambda",
            disposition="route to dark-sector ledger",
            next_obligation="do not count clustered excess as the Lambda floor",
        ),
        MeasureProbe(
            probe_id="defectlike_measure_excess",
            candidate_identity="measure density with string/wall-like scaling",
            conservation_face="w != -1 gives variable density",
            source_ledger="defect/excess sector, not constant Lambda",
            disposition="route to dark-sector or defect ledger",
            next_obligation="classify equation of state and clustering before use",
        ),
    ]

    return {
        "dimension_balance": dimension_balance,
        "dimensional_fit": dimensional_fit,
        "lambda_floor": lambda_floor,
        "lambda_floor_derivative": lambda_floor_derivative,
        "lambda_dust": lambda_dust,
        "lambda_dust_derivative": lambda_dust_derivative,
        "lambda_string_derivative": lambda_string_derivative,
        "rho_w_floor": rho_w_floor,
        "rho_w_dust": rho_w_dust,
        "rho_w_wall": rho_w_wall,
        "probes": probes,
    }


def markdown_rows(probes):
    return "\n".join(
        "| {probe_id} | {candidate_identity} | {conservation_face} | {source_ledger} | {disposition} | {next_obligation} |".format(
            probe_id=probe.probe_id,
            candidate_identity=probe.candidate_identity,
            conservation_face=probe.conservation_face,
            source_ledger=probe.source_ledger,
            disposition=probe.disposition,
            next_obligation=probe.next_obligation,
        )
        for probe in probes
    )


def write_report(data):
    rows = markdown_rows(data["probes"])
    md = f"""# VacuumForge Lambda Measure Identity Probe

## Purpose

This report tests whether a measure identity can supply a conserved density or
curvature scale for `Lambda` without observed-value insertion or dark-excess
double counting. It does not derive the observed cosmological constant.

This report depends on:

```text
lambda_topology_global_constraint_probe_013
```

It satisfies:

```text
lambda_measure_identity_probe_required_013
```

## Symbolic Checks

Dimension check:

```text
dim(kappa) + dim(rho) - dim(Lambda) = {sp.sstr(data["dimension_balance"])}
```

Dimensional fit:

```text
Lambda = {sp.sstr(data["dimensional_fit"])}
```

Conserved floor:

```text
Lambda_floor = {sp.sstr(data["lambda_floor"])}
d Lambda_floor / da = {sp.sstr(data["lambda_floor_derivative"])}
rho(w=-1) = {sp.sstr(data["rho_w_floor"])}
```

Transportable/excess scalings:

```text
rho(w=0) = {sp.sstr(data["rho_w_dust"])}
Lambda_dust(a) = {sp.sstr(data["lambda_dust"])}
d Lambda_dust / da = {sp.sstr(data["lambda_dust_derivative"])}
rho(w=-2/3) = {sp.sstr(data["rho_w_wall"])}
d Lambda_string / da = {sp.sstr(data["lambda_string_derivative"])}
```

## Probe Ledger

| probe | candidate identity | conservation face | source ledger | disposition | next obligation |
| --- | --- | --- | --- | --- | --- |
{rows}

## Current Conclusion

A measure identity can be a Lambda selector only if it supplies a derived,
covariantly conserved, constant floor before observation is used. Dimensional
fits import a scale. Dustlike, stringlike, wall-like, clustered, or
transportable densities belong to dark-sector or defect ledgers, not the
constant Lambda baseline.

The clean split is:

```text
conserved w = -1 floor:
  possible Lambda selector only after rho0 is derived

Lambda = C/L^2:
  dimensional fit unless L is derived

w != -1 measure density:
  variable/excess sector, not constant Lambda
```

## Classification

```text
result type: Lambda measure identity probe
scope: measure identities as Lambda baseline selectors
conclusion: a measure route needs a derived conserved floor; otherwise it is fitting or dark excess
non-conclusion: no nonzero Lambda value is derived; relaxation/fixed-point routes are not yet tested
```

The next technical target is:

```text
lambda_relaxation_fixed_point_probe_required_014
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")


def record_archive(ns, probes):
    marker_id = "lambda_measure_identity_probe_014"
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[sp.Symbol("lambda_topology_global_constraint_probe_result")],
        output=sp.Symbol("lambda_measure_identity_probe_result"),
        method="SymPy dimensional and equation-of-state conservation checks for Lambda measure identities",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        is_placeholder=False,
        scope="Measure identities as Lambda baseline selectors",
    )

    for probe in probes:
        status = GovernanceStatus.CANDIDATE_ROUTE if probe.probe_id == "conserved_vacuum_density_floor" else GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
        ns.record_claim(
            ClaimRecord(
                claim_id=f"lambda_measure_probe_{probe.probe_id}_014",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=status,
                statement=f"{probe.probe_id}: {probe.disposition}",
                derivation_ids=[marker_id],
                obligation_ids=["lambda_relaxation_fixed_point_probe_required_014"],
            )
        )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="lambda_measure_identity_probe_required_013",
            script_id=SCRIPT_ID,
            title="Test measure identity as a Lambda selector",
            status=ObligationStatus.SATISFIED,
            required_by=["013_lambda_topology_global_constraint__lambda_topology_global_constraint"],
            satisfied_by=[SCRIPT_ID],
            description=(
                "Satisfied by dimensional and conservation checks separating "
                "derived constant floors from dimensional fits and dark-sector "
                "excess densities."
            ),
        )
    )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="lambda_relaxation_fixed_point_probe_required_014",
            script_id=SCRIPT_ID,
            title="Test relaxation/fixed-point routes as Lambda selectors",
            status=ObligationStatus.OPEN,
            required_by=[SCRIPT_ID],
            description=(
                "Measure identities need a derived conserved floor. Test "
                "whether relaxation or fixed-point dynamics can select a "
                "nonzero floor without importing a target value."
            ),
        )
    )


def main() -> None:
    header("Vacuum Sector 014: Lambda Measure Identity Probe")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    data = run_sympy_checks()

    out = ScriptOutput()
    for probe in data["probes"]:
        status = StatusMark.DEFER
        if probe.probe_id == "conserved_vacuum_density_floor":
            status = StatusMark.OBLIGATION
        with out.governance_assessments():
            out.line(probe.probe_id, status, probe.disposition)
    with out.unresolved_obligations():
        out.line(
            "Lambda relaxation/fixed-point probe required",
            StatusMark.OBLIGATION,
            "test whether dynamics can supply a nonzero floor without target insertion",
        )

    record_archive(ns, data["probes"])
    ns.write_run_metadata()
    write_report(data)

    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
