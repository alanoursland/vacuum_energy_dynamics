#!/usr/bin/env python3
"""
finite_strain_admissibility_probe.py

VacuumForge-managed finite-strain admissibility probe for interior caps.

This is not a nonsingularity theorem. It tests whether a cap scale follows
from a derived admissibility bound or is merely inserted by hand.

Output:
    theory_v3/development/vacuum_sector/07_interior_cap/
        finite_strain_admissibility_probe_vacuumforge.md
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
    / "finite_strain_admissibility_probe_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "exterior_matching_lemma_026",
        "026_exterior_matching_lemma__exterior_matching_lemma",
        "exterior_matching_lemma_026",
    )
]


@dataclass(frozen=True)
class StrainRoute:
    route_id: str
    route: str
    strain_quantity: str
    bound_route: str
    cap_scale_route: str
    observable_face: str
    disposition: str
    next_obligation: str
    has_strain_quantity: int
    derives_bound: int
    derives_scale: int
    preserves_exterior: int
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


def strain_routes():
    return [
        StrainRoute(
            route_id="unbounded_gr_interior",
            route="retain exterior GR and allow interior strain proxy to diverge",
            strain_quantity="K_int = 1/(1 - C)",
            bound_route="no finite bound",
            cap_scale_route="no cap scale",
            observable_face="ordinary strong-interior incompletion",
            disposition="not a cap route",
            next_obligation="do not claim finite interior from exterior closure alone",
            has_strain_quantity=1,
            derives_bound=0,
            derives_scale=0,
            preserves_exterior=1,
        ),
        StrainRoute(
            route_id="imposed_strain_bound",
            route="set K_int <= kappa_max",
            strain_quantity="K_int = 1/(1 - C)",
            bound_route="kappa_max imposed",
            cap_scale_route="R_cap solved from imposed kappa_max",
            observable_face="compactness/redshift cap",
            disposition="rejected as imported admissibility scale",
            next_obligation="derive kappa_max before use",
            has_strain_quantity=1,
            derives_bound=0,
            derives_scale=0,
            preserves_exterior=1,
            rejected=1,
        ),
        StrainRoute(
            route_id="derived_microphysical_bound",
            route="derive K_int <= K_ved from vacuum ontology",
            strain_quantity="chosen finite-strain invariant",
            bound_route="K_ved must be derived before observation",
            cap_scale_route="R_cap follows only after K_ved is derived",
            observable_face="maximum compactness or redshift with exterior preserved",
            disposition="candidate only; missing derivation of K_ved",
            next_obligation="derive or reject finite-strain bound from ontology",
            has_strain_quantity=0,
            derives_bound=0,
            derives_scale=0,
            preserves_exterior=1,
        ),
        StrainRoute(
            route_id="observed_compactness_backsolve",
            route="infer cap scale from desired observed compactness",
            strain_quantity="chosen after target",
            bound_route="observed compactness supplies bound",
            cap_scale_route="R_cap from target compactness",
            observable_face="fit to compact-object target",
            disposition="rejected as observed-value insertion",
            next_obligation="do not use as derivation",
            has_strain_quantity=0,
            derives_bound=0,
            derives_scale=0,
            preserves_exterior=1,
            rejected=1,
        ),
    ]


def run_sympy_checks(routes):
    G, M, c, R_cap, kappa_max, K_ved, C_target = sp.symbols(
        "G M c R_cap kappa_max K_ved C_target", positive=True
    )
    compactness = 2 * G * M / (c**2 * R_cap)
    strain_proxy = 1 / (1 - compactness)
    r_from_kappa = sp.solve(sp.Eq(strain_proxy, kappa_max), R_cap)[0]
    r_from_kved = sp.solve(sp.Eq(strain_proxy, K_ved), R_cap)[0]
    r_from_observed_c = sp.solve(sp.Eq(compactness, C_target), R_cap)[0]

    require_equal(
        "cap radius from imposed kappa",
        r_from_kappa,
        2 * G * M * kappa_max / (c**2 * (kappa_max - 1)),
    )
    require_equal(
        "cap radius from derived K_ved placeholder",
        r_from_kved,
        2 * G * K_ved * M / (c**2 * (K_ved - 1)),
    )
    require_equal("cap radius from observed compactness", r_from_observed_c, 2 * G * M / (C_target * c**2))
    require_true("imposed cap imports kappa_max", r_from_kappa.has(kappa_max))
    require_true("derived route still needs K_ved", r_from_kved.has(K_ved))

    live_routes = [
        route.route_id
        for route in routes
        if (
            route.has_strain_quantity
            and route.derives_bound
            and route.derives_scale
            and route.preserves_exterior
            and not route.rejected
        )
    ]
    require_equal("no finite-strain cap route is live", len(live_routes), 0)

    return {
        "compactness": compactness,
        "strain_proxy": strain_proxy,
        "r_from_kappa": r_from_kappa,
        "r_from_kved": r_from_kved,
        "r_from_observed_c": r_from_observed_c,
        "live_routes": live_routes,
    }


def markdown_routes(routes):
    return "\n".join(
        (
            "| {route_id} | {route} | {strain_quantity} | {bound_route} | "
            "{cap_scale_route} | {observable_face} | {disposition} | {next_obligation} |"
        ).format(
            route_id=route.route_id,
            route=route.route,
            strain_quantity=route.strain_quantity,
            bound_route=route.bound_route,
            cap_scale_route=route.cap_scale_route,
            observable_face=route.observable_face,
            disposition=route.disposition,
            next_obligation=route.next_obligation,
        )
        for route in routes
    )


def readiness_rows(routes):
    return "\n".join(
        "| {route_id} | {has_strain_quantity} | {derives_bound} | {derives_scale} | {preserves_exterior} | {live} |".format(
            route_id=route.route_id,
            has_strain_quantity=bool(route.has_strain_quantity),
            derives_bound=bool(route.derives_bound),
            derives_scale=bool(route.derives_scale),
            preserves_exterior=bool(route.preserves_exterior),
            live=bool(
                route.has_strain_quantity
                and route.derives_bound
                and route.derives_scale
                and route.preserves_exterior
                and not route.rejected
            ),
        )
        for route in routes
    )


def write_report(routes, data):
    route_md = markdown_routes(routes)
    readiness_md = readiness_rows(routes)
    md = f"""# VacuumForge Finite-Strain Admissibility Probe

## Purpose

This report tests whether an interior cap scale is derived by a finite-strain
admissibility rule or imported as a cutoff. It does not prove a nonsingular
interior.

This report depends on:

```text
exterior_matching_lemma_026
```

It satisfies:

```text
finite_strain_admissibility_probe_required_026
```

## Symbolic Checks

Compactness:

```text
C = {sp.sstr(data["compactness"])}
```

Finite-strain proxy:

```text
K_int = {sp.sstr(data["strain_proxy"])}
```

Cap radius from imposed `kappa_max`:

```text
R_cap = {sp.sstr(data["r_from_kappa"])}
```

Cap radius from a placeholder derived bound `K_ved`:

```text
R_cap = {sp.sstr(data["r_from_kved"])}
```

Cap radius from observed compactness:

```text
R_cap = {sp.sstr(data["r_from_observed_c"])}
```

The algebra shows where the missing object lives: a cap scale follows only
after a finite-strain bound is supplied. If that bound is imposed or inferred
from an observed target, the route is not a derivation.

## Finite-Strain Route Ledger

| route | route | strain quantity | bound route | cap scale route | observable face | disposition | next obligation |
| --- | --- | --- | --- | --- | --- | --- | --- |
{route_md}

## Readiness

| route | strain quantity | derives bound | derives scale | preserves exterior | live cap route |
| --- | --- | --- | --- | --- | --- |
{readiness_md}

## Current Conclusion

No finite-strain interior cap is licensed. The exterior matching lemma protects
the exterior only. It does not derive the interior admissibility bound,
cap scale, or nonsingularity rule.

The only possible live route is a future derived microphysical or ontological
bound, and that bound is not supplied here.

## Classification

```text
result type: finite-strain admissibility probe
scope: interior cap scale after exterior preservation
conclusion: no cap scale is derived; imposed cutoffs and observed-target backsolves fail
non-conclusion: no global no-go theorem against finite interiors
```

The next technical target is:

```text
global_boundary_topology_selector_rules_required_027
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")


def record_archive(ns, routes):
    marker_id = "finite_strain_admissibility_probe_027"
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[sp.Symbol("exterior_matching_lemma_result")],
        output=sp.Symbol("finite_strain_admissibility_result"),
        method="SymPy compactness and finite-strain cap-scale audit",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        is_placeholder=False,
        scope="Finite-strain cap-scale readiness",
    )

    for route in routes:
        status = (
            GovernanceStatus.REJECTED_ROUTE
            if route.rejected
            else GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
        )
        ns.record_claim(
            ClaimRecord(
                claim_id=f"finite_strain_route_{route.route_id}_027",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=status,
                statement=f"{route.route_id}: {route.disposition}",
                derivation_ids=[marker_id],
                obligation_ids=["global_boundary_topology_selector_rules_required_027"],
            )
        )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="finite_strain_admissibility_probe_required_026",
            script_id=SCRIPT_ID,
            title="Probe finite-strain admissibility scale for interior caps",
            status=ObligationStatus.SATISFIED,
            required_by=["026_exterior_matching_lemma__exterior_matching_lemma"],
            satisfied_by=[SCRIPT_ID],
            description=(
                "Satisfied by showing that cap radii require a supplied "
                "finite-strain bound; imposed bounds and observed compactness "
                "backsolves are not derivations."
            ),
        )
    )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="global_boundary_topology_selector_rules_required_027",
            script_id=SCRIPT_ID,
            title="Consolidate global, boundary, and topology selector rules",
            status=ObligationStatus.OPEN,
            required_by=[SCRIPT_ID],
            description=(
                "After Lambda and interior probes both expose missing scales, "
                "record the cross-cutting rule for global, boundary, topology, "
                "and admissibility selectors."
            ),
        )
    )


def main() -> None:
    header("Vacuum Sector 027: Finite-Strain Admissibility Probe")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    routes = strain_routes()
    data = run_sympy_checks(routes)

    out = ScriptOutput()
    for route in routes:
        status = StatusMark.FAIL if route.rejected else StatusMark.DEFER
        with out.governance_assessments():
            out.line(route.route_id, status, route.disposition)
    with out.unresolved_obligations():
        out.line(
            "Global/boundary/topology selector rules required",
            StatusMark.OBLIGATION,
            "consolidate the cross-cutting missing-scale rule",
        )

    record_archive(ns, routes)
    ns.write_run_metadata()
    write_report(routes, data)

    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
