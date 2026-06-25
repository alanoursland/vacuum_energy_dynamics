#!/usr/bin/env python3
"""
interior_cap_admissibility_contract.py

VacuumForge-managed contract for strong-field/interior admissibility.

This is not a nonsingularity theorem. It opens the interior-cap workstream by
separating exterior preservation from interior finite-strain admissibility and
by rejecting imported cutoff radii or untracked exterior deviations.

Output:
    theory_v3/development/vacuum_sector/07_interior_cap/
        interior_cap_admissibility_contract_vacuumforge.md
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
    / "07_interior_cap"
    / "interior_cap_admissibility_contract_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "substance_frame_bounds_sieve_024",
        "024_substance_frame_bounds_sieve__substance_frame_bounds_sieve",
        "substance_frame_bounds_sieve_024",
    )
]


@dataclass(frozen=True)
class InteriorRoute:
    route_id: str
    route: str
    exterior_condition: str
    interior_rule: str
    scale_route: str
    observable_face: str
    disposition: str
    next_obligation: str
    preserves_exterior: int
    has_matching_rule: int
    has_finite_strain_rule: int
    derives_scale: int
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


def interior_routes():
    return [
        InteriorRoute(
            route_id="exterior_preserving_interior_rule",
            route="modify only interior admissibility while preserving exterior GR matching",
            exterior_condition="same exterior mass M and Lambda; no exterior residual",
            interior_rule="finite-strain cap rule not yet supplied",
            scale_route="cap scale not yet derived",
            observable_face="compactness/redshift/interior-EOS face with no exterior deviation",
            disposition="contracted candidate only",
            next_obligation="prove exterior matching lemma before finite-strain cap claims",
            preserves_exterior=1,
            has_matching_rule=0,
            has_finite_strain_rule=0,
            derives_scale=0,
        ),
        InteriorRoute(
            route_id="surface_layer_matching_route",
            route="allow a surface layer or transition shell",
            exterior_condition="must satisfy junction bookkeeping and conserve exterior charges",
            interior_rule="surface stress or transition law not yet supplied",
            scale_route="shell/cap radius not derived",
            observable_face="surface redshift, merger, echo, or compactness signature",
            disposition="deferred pending matching and source ledger",
            next_obligation="write junction/source ledger before use",
            preserves_exterior=1,
            has_matching_rule=0,
            has_finite_strain_rule=0,
            derives_scale=0,
        ),
        InteriorRoute(
            route_id="imported_cutoff_radius",
            route="insert cap radius by hand",
            exterior_condition="may preserve exterior by construction",
            interior_rule="cutoff imposed, not derived",
            scale_route="imported length or compactness threshold",
            observable_face="chosen cap phenomenology",
            disposition="rejected as imported scale",
            next_obligation="derive cap scale from admissibility before use",
            preserves_exterior=1,
            has_matching_rule=0,
            has_finite_strain_rule=0,
            derives_scale=0,
            rejected=1,
        ),
        InteriorRoute(
            route_id="untracked_exterior_deviation",
            route="alter interior and let exterior change without residual gates",
            exterior_condition="fails: tested exterior is no longer protected",
            interior_rule="not enough",
            scale_route="not enough",
            observable_face="untracked weak-field or radiative deviation",
            disposition="rejected as wrong ledger",
            next_obligation="return to residual gates before exterior modification",
            preserves_exterior=0,
            has_matching_rule=0,
            has_finite_strain_rule=0,
            derives_scale=0,
            rejected=1,
        ),
    ]


def run_sympy_checks(routes):
    M, r, G, c, R_cap, kappa_max = sp.symbols("M r G c R_cap kappa_max", positive=True)
    compactness = 2 * G * M / (c**2 * R_cap)
    horizon_gap = 1 - compactness
    cap_from_compactness = sp.solve(sp.Eq(compactness, 1), R_cap)[0]
    finite_strain_proxy = 1 / horizon_gap
    cap_from_strain_bound = sp.solve(sp.Eq(finite_strain_proxy, kappa_max), R_cap)[0]
    exterior_potential = -G * M / r

    require_equal("Schwarzschild radius from compactness one", cap_from_compactness, 2 * G * M / c**2)
    require_equal(
        "finite strain cap radius from bound",
        cap_from_strain_bound,
        2 * G * M * kappa_max / (c**2 * (kappa_max - 1)),
    )
    require_equal("exterior potential depends on M and r only", sp.diff(exterior_potential, R_cap), 0)
    require_true("finite strain cap imports kappa_max", cap_from_strain_bound.has(kappa_max))

    live_routes = [
        route.route_id
        for route in routes
        if (
            route.preserves_exterior
            and route.has_matching_rule
            and route.has_finite_strain_rule
            and route.derives_scale
            and not route.rejected
        )
    ]
    require_equal("no interior cap route is live", len(live_routes), 0)

    return {
        "compactness": compactness,
        "horizon_gap": horizon_gap,
        "cap_from_compactness": cap_from_compactness,
        "finite_strain_proxy": finite_strain_proxy,
        "cap_from_strain_bound": cap_from_strain_bound,
        "exterior_potential": exterior_potential,
        "live_routes": live_routes,
    }


def markdown_routes(routes):
    return "\n".join(
        (
            "| {route_id} | {route} | {exterior_condition} | {interior_rule} | "
            "{scale_route} | {observable_face} | {disposition} | {next_obligation} |"
        ).format(
            route_id=route.route_id,
            route=route.route,
            exterior_condition=route.exterior_condition,
            interior_rule=route.interior_rule,
            scale_route=route.scale_route,
            observable_face=route.observable_face,
            disposition=route.disposition,
            next_obligation=route.next_obligation,
        )
        for route in routes
    )


def readiness_rows(routes):
    return "\n".join(
        "| {route_id} | {preserves_exterior} | {has_matching_rule} | {has_finite_strain_rule} | {derives_scale} | {live} |".format(
            route_id=route.route_id,
            preserves_exterior=bool(route.preserves_exterior),
            has_matching_rule=bool(route.has_matching_rule),
            has_finite_strain_rule=bool(route.has_finite_strain_rule),
            derives_scale=bool(route.derives_scale),
            live=bool(
                route.preserves_exterior
                and route.has_matching_rule
                and route.has_finite_strain_rule
                and route.derives_scale
                and not route.rejected
            ),
        )
        for route in routes
    )


def write_report(routes, data):
    route_md = markdown_routes(routes)
    readiness_md = readiness_rows(routes)
    md = f"""# VacuumForge Interior-Cap Admissibility Contract

## Purpose

This report opens the strong-field/interior admissibility workstream. It does
not prove a finite interior, a nonsingular compact object, or a new equation of
state.

This report depends on:

```text
substance_frame_bounds_sieve_024
```

It satisfies:

```text
interior_cap_admissibility_contract_required_024
```

## Symbolic Checks

Compactness proxy:

```text
C = {sp.sstr(data["compactness"])}
1 - C = {sp.sstr(data["horizon_gap"])}
R_cap at C = 1 -> {sp.sstr(data["cap_from_compactness"])}
```

Finite-strain placeholder:

```text
K_int = {sp.sstr(data["finite_strain_proxy"])}
R_cap from K_int = kappa_max -> {sp.sstr(data["cap_from_strain_bound"])}
```

Exterior potential proxy:

```text
Phi_ext = {sp.sstr(data["exterior_potential"])}
d(Phi_ext)/dR_cap = 0
```

The check is intentionally narrow. The exterior proxy depends on exterior mass
and radius, not the cap radius, when exterior charges are preserved. A finite
strain cap still imports a bound or admissibility scale unless that scale is
derived.

## Interior Route Ledger

| route | route | exterior condition | interior rule | scale route | observable face | disposition | next obligation |
| --- | --- | --- | --- | --- | --- | --- | --- |
{route_md}

## Readiness

| route | preserves exterior | matching rule | finite-strain rule | derives scale | live cap route |
| --- | --- | --- | --- | --- | --- |
{readiness_md}

## Current Conclusion

No interior-cap route is live. Exterior-preserving interior modification is a
candidate contract only. A cap or finite-strain rule needs exterior matching,
junction/source bookkeeping, and a derived admissibility scale before it can be
used.

Imported cutoff radii and untracked exterior deviations are rejected.

## Classification

```text
result type: interior-cap admissibility contract
scope: strong-field interiors with tested exterior sector preserved
conclusion: no finite-strain cap is licensed without matching and scale derivation
non-conclusion: no nonsingularity theorem; no global no-go theorem against interiors
```

The next technical target is:

```text
exterior_matching_lemma_required_025
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")


def record_archive(ns, routes):
    marker_id = "interior_cap_admissibility_contract_025"
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[sp.Symbol("substance_frame_bounds_sieve_result")],
        output=sp.Symbol("interior_cap_admissibility_contract_result"),
        method="SymPy compactness, exterior-preservation, and finite-strain scale audit",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        is_placeholder=False,
        scope="Strong-field/interior admissibility contract",
    )

    for route in routes:
        status = (
            GovernanceStatus.REJECTED_ROUTE
            if route.rejected
            else GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
        )
        ns.record_claim(
            ClaimRecord(
                claim_id=f"interior_cap_route_{route.route_id}_025",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=status,
                statement=f"{route.route_id}: {route.disposition}",
                derivation_ids=[marker_id],
                obligation_ids=["exterior_matching_lemma_required_025"],
            )
        )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="interior_cap_admissibility_contract_required_024",
            script_id=SCRIPT_ID,
            title="Open the strong-field/interior admissibility contract",
            status=ObligationStatus.SATISFIED,
            required_by=["024_substance_frame_bounds_sieve__substance_frame_bounds_sieve"],
            satisfied_by=[SCRIPT_ID],
            description=(
                "Satisfied by separating exterior-preserving interior routes "
                "from imported cutoff radii and untracked exterior deviations."
            ),
        )
    )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="exterior_matching_lemma_required_025",
            script_id=SCRIPT_ID,
            title="Prove the exterior matching lemma for interior modifications",
            status=ObligationStatus.OPEN,
            required_by=[SCRIPT_ID],
            description=(
                "Show that if exterior field equations and exterior charges are "
                "unchanged, the tested exterior metric remains the GR exterior "
                "before any finite-strain interior cap is claimed."
            ),
        )
    )


def main() -> None:
    header("Vacuum Sector 025: Interior-Cap Admissibility Contract")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    routes = interior_routes()
    data = run_sympy_checks(routes)

    out = ScriptOutput()
    for route in routes:
        status = StatusMark.FAIL if route.rejected else StatusMark.DEFER
        with out.governance_assessments():
            out.line(route.route_id, status, route.disposition)
    with out.unresolved_obligations():
        out.line(
            "Exterior matching lemma required",
            StatusMark.OBLIGATION,
            "prove exterior preservation before finite-strain cap claims",
        )

    record_archive(ns, routes)
    ns.write_run_metadata()
    write_report(routes, data)

    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
