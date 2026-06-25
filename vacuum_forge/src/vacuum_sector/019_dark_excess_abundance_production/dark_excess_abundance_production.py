#!/usr/bin/env python3
"""
dark_excess_abundance_production.py

VacuumForge-managed abundance/production probe for dark-sector excess.

This is not a derivation of dark matter. It tests whether common abundance
routes compute a present density or merely import an observed density,
initial yield, interaction scale, or formation fraction.

Output:
    theory_v3/development/vacuum_sector/05_dark_sector/
        dark_excess_abundance_production_probe_vacuumforge.md
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
    / "05_dark_sector"
    / "dark_excess_abundance_production_probe_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "dark_excess_clustering_conservation_probe_018",
        "018_dark_excess_clustering_conservation__dark_excess_clustering_conservation",
        "dark_excess_clustering_conservation_probe_018",
    )
]


@dataclass(frozen=True)
class AbundanceRow:
    row_id: str
    route: str
    symbolic_result: str
    imported_input: str
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
    a_form, a0, rho_form, rho_today, rho_obs = sp.symbols("a_form a0 rho_form rho_today rho_obs", positive=True)
    m, Y, s0, sigma_v, C, f_form, rho_tot_form = sp.symbols("m Y s0 sigma_v C f_form rho_tot_form", positive=True)

    dilution_today = rho_form * (a_form / a0) ** 3
    required_initial = sp.solve(sp.Eq(dilution_today, rho_obs), rho_form)[0]

    yield_density = m * Y * s0
    solved_yield = sp.solve(sp.Eq(yield_density, rho_obs), Y)[0]

    freezeout_proxy = C / sigma_v
    solved_cross_section = sp.solve(sp.Eq(freezeout_proxy, rho_obs), sigma_v)[0]

    formation_density = f_form * rho_tot_form * (a_form / a0) ** 3
    solved_fraction = sp.solve(sp.Eq(formation_density, rho_obs), f_form)[0]

    require_equal("dilution required initial density", required_initial, rho_obs * a0**3 / a_form**3)
    require_equal("yield required value", solved_yield, rho_obs / (m * s0))
    require_equal("freezeout required cross section", solved_cross_section, C / rho_obs)
    require_equal("formation required fraction", solved_fraction, rho_obs * a0**3 / (a_form**3 * rho_tot_form))
    require_true("yield density imports yield", yield_density.has(Y))
    require_true("freezeout proxy imports cross section", freezeout_proxy.has(sigma_v))
    require_true("formation density imports formation fraction", formation_density.has(f_form))

    rows = [
        AbundanceRow(
            row_id="observed_density_backsolve",
            route="solve for initial density from observed density",
            symbolic_result=f"rho_form = {sp.sstr(required_initial)}",
            imported_input="rho_obs",
            disposition="rejected as observed-value insertion",
            next_obligation="do not use as production mechanism",
        ),
        AbundanceRow(
            row_id="yield_route",
            route="conserved yield abundance",
            symbolic_result=f"rho_today = {sp.sstr(yield_density)}",
            imported_input="mass m, yield Y, entropy density s0",
            disposition="candidate only if Y is derived",
            next_obligation="derive yield from production microphysics",
        ),
        AbundanceRow(
            row_id="freezeout_proxy_route",
            route="inverse interaction-strength relic proxy",
            symbolic_result=f"rho_today = {sp.sstr(freezeout_proxy)}",
            imported_input="interaction scale or cross section sigma_v",
            disposition="candidate only if interaction route exists",
            next_obligation="derive coupling/cross section and freezeout regime",
        ),
        AbundanceRow(
            row_id="formation_fraction_route",
            route="defect/excitation formation fraction",
            symbolic_result=f"rho_today = {sp.sstr(formation_density)}",
            imported_input="formation fraction f_form and formation epoch",
            disposition="candidate only if formation dynamics derive f_form",
            next_obligation="derive formation fraction and epoch from vacuum dynamics",
        ),
    ]

    return {
        "dilution_today": dilution_today,
        "required_initial": required_initial,
        "yield_density": yield_density,
        "solved_yield": solved_yield,
        "freezeout_proxy": freezeout_proxy,
        "solved_cross_section": solved_cross_section,
        "formation_density": formation_density,
        "solved_fraction": solved_fraction,
        "rows": rows,
    }


def markdown_rows(rows):
    return "\n".join(
        "| {row_id} | {route} | {symbolic_result} | {imported_input} | {disposition} | {next_obligation} |".format(
            row_id=row.row_id,
            route=row.route,
            symbolic_result=row.symbolic_result,
            imported_input=row.imported_input,
            disposition=row.disposition,
            next_obligation=row.next_obligation,
        )
        for row in rows
    )


def write_report(data):
    rows = markdown_rows(data["rows"])
    md = f"""# VacuumForge Dark Excess Abundance/Production Probe

## Purpose

This report tests abundance and production bookkeeping for pressureless
dark-sector excess. It does not derive dark matter abundance.

This report depends on:

```text
dark_excess_clustering_conservation_probe_018
```

It satisfies:

```text
dark_excess_abundance_production_required_018
```

## Symbolic Checks

Dilution from formation:

```text
rho_today = {sp.sstr(data["dilution_today"])}
required rho_form from rho_obs = {sp.sstr(data["required_initial"])}
```

Conserved yield:

```text
rho_today = {sp.sstr(data["yield_density"])}
required Y from rho_obs = {sp.sstr(data["solved_yield"])}
```

Freezeout proxy:

```text
rho_today = {sp.sstr(data["freezeout_proxy"])}
required sigma_v from rho_obs = {sp.sstr(data["solved_cross_section"])}
```

Formation fraction:

```text
rho_today = {sp.sstr(data["formation_density"])}
required f_form from rho_obs = {sp.sstr(data["solved_fraction"])}
```

## Abundance Ledger

| row | route | symbolic result | imported input | disposition | next obligation |
| --- | --- | --- | --- | --- | --- |
{rows}

## Current Conclusion

No dark-sector abundance route is currently licensed. Back-solving from the
observed density is rejected. Yield, freezeout-like, and formation-fraction
routes remain possible only after their production microphysics, interaction
scale, or formation fraction is derived before observation is used.

## Classification

```text
result type: dark-excess abundance/production probe
scope: abundance bookkeeping after clustering/conservation readiness
conclusion: no abundance route is licensed without production microphysics
non-conclusion: dustlike excess is not globally killed; no halo model is tested
```

The next technical target is:

```text
non_grav_channel_quarantine_required_019
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")


def record_archive(ns, rows):
    marker_id = "dark_excess_abundance_production_probe_019"
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[sp.Symbol("dark_excess_clustering_conservation_result")],
        output=sp.Symbol("dark_excess_abundance_production_result"),
        method="SymPy abundance backsolve, yield, freezeout-proxy, and formation-fraction checks",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        is_placeholder=False,
        scope="Abundance and production readiness for dark-sector excess",
    )

    for row in rows:
        status = GovernanceStatus.REJECTED_ROUTE if row.row_id == "observed_density_backsolve" else GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
        ns.record_claim(
            ClaimRecord(
                claim_id=f"dark_excess_abundance_row_{row.row_id}_019",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=status,
                statement=f"{row.row_id}: {row.disposition}",
                derivation_ids=[marker_id],
                obligation_ids=["non_grav_channel_quarantine_required_019"],
            )
        )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="dark_excess_abundance_production_required_018",
            script_id=SCRIPT_ID,
            title="Test abundance and production gates for dark excess",
            status=ObligationStatus.SATISFIED,
            required_by=["018_dark_excess_clustering_conservation__dark_excess_clustering_conservation"],
            satisfied_by=[SCRIPT_ID],
            description=(
                "Satisfied by separating observed-density backsolves from "
                "yield, freezeout-like, and formation-fraction routes that "
                "need production microphysics before use."
            ),
        )
    )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="non_grav_channel_quarantine_required_019",
            script_id=SCRIPT_ID,
            title="Open non-gravitational vacuum channel quarantine",
            status=ObligationStatus.OPEN,
            required_by=[SCRIPT_ID],
            description=(
                "Dark excess remains unlicensed without production. Move to "
                "non-gravitational channels and require each channel to state "
                "coupling, source ledger, metric quarantine, observable, and "
                "falsifier."
            ),
        )
    )


def main() -> None:
    header("Vacuum Sector 019: Dark Excess Abundance/Production Probe")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    data = run_sympy_checks()

    out = ScriptOutput()
    for row in data["rows"]:
        status = StatusMark.DEFER
        if row.row_id == "observed_density_backsolve":
            status = StatusMark.FAIL
        with out.governance_assessments():
            out.line(row.row_id, status, row.disposition)
    with out.unresolved_obligations():
        out.line(
            "Non-grav channel quarantine required",
            StatusMark.OBLIGATION,
            "open channel contracts only after metric quarantine and falsifiers are stated",
        )

    record_archive(ns, data["rows"])
    ns.write_run_metadata()
    write_report(data)

    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
