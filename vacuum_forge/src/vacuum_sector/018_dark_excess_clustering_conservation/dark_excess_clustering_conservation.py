#!/usr/bin/env python3
"""
dark_excess_clustering_conservation.py

VacuumForge-managed clustering/conservation probe for dark-sector excess.

This is not a derivation of dark matter. It tests whether a dustlike excess
has the minimum conservation, pressure, and growth faces required before an
abundance or halo claim can be opened.

Output:
    theory_v3/development/vacuum_sector/05_dark_sector/
        dark_excess_clustering_conservation_probe_vacuumforge.md
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
    / "dark_excess_clustering_conservation_probe_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "dark_excess_source_ledger_017",
        "017_dark_excess_source_ledger__dark_excess_source_ledger",
        "dark_excess_source_ledger_017",
    )
]


@dataclass(frozen=True)
class ClusteringRow:
    row_id: str
    candidate: str
    symbolic_result: str
    gate_status: str
    disposition: str
    next_obligation: str


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_equal(label, lhs, rhs) -> None:
    residual = simplify_expr(lhs - rhs)
    if residual != 0:
        raise AssertionError(f"{label} failed: {residual}")


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
    a, rho0, w, Q, cs2, k, x = sp.symbols("a rho0 w Q c_s2 k x", positive=True)
    delta = sp.exp(x)

    rho_dust = rho0 / a**3
    continuity_dust = simplify_expr(a * sp.diff(rho_dust, a) + 3 * rho_dust)

    rho_w = rho0 * a ** (-3 * (1 + w))
    continuity_w = simplify_expr(a * sp.diff(rho_w, a) + 3 * (1 + w) * rho_w)
    exchange_residual = Q

    pressure_term = cs2 * k**2 / a**2
    dust_pressure_term = pressure_term.subs(cs2, 0)

    growth_residual = simplify_expr(sp.diff(delta, x, 2) + sp.Rational(1, 2) * sp.diff(delta, x) - sp.Rational(3, 2) * delta)

    require_equal("dust continuity residual", continuity_dust, 0)
    require_equal("general constant-w continuity residual", continuity_w, 0)
    require_equal("zero sound-speed pressure term", dust_pressure_term, 0)
    require_equal("matter-era delta=a growth proxy", growth_residual, 0)

    rows = [
        ClusteringRow(
            row_id="conserved_pressureless_dust",
            candidate="w = 0, c_s^2 = 0, separately conserved excess",
            symbolic_result="rho = rho0/a^3, continuity residual = 0, pressure term = 0",
            gate_status="passes clustering readiness proxy",
            disposition="dark-sector excess candidate, not yet abundance-licensed",
            next_obligation="derive production and abundance before claiming dark matter",
        ),
        ClusteringRow(
            row_id="pressure_supported_excess",
            candidate="w = 0 but c_s^2 != 0",
            symbolic_result=f"pressure term = {sp.sstr(pressure_term)}",
            gate_status="blocked pending small-sound-speed route",
            disposition="not CDM-like until pressure support is routed or bounded",
            next_obligation="supply sound-speed bound or microphysical cold limit",
        ),
        ClusteringRow(
            row_id="exchanging_excess",
            candidate="excess exchanges with floor or another sector",
            symbolic_result=f"continuity residual = {sp.sstr(exchange_residual)}",
            gate_status="blocked pending exchange ledger",
            disposition="requires paired conservation with the floor or source sector",
            next_obligation="write exchange law and prove total conservation",
        ),
        ClusteringRow(
            row_id="ordinary_matter_insertion",
            candidate="declare excess as ordinary matter source",
            symbolic_result="no independent vacuum-sector source ledger",
            gate_status="rejected route",
            disposition="source double-counting unless independently derived",
            next_obligation="do not insert into T_ab without production/source route",
        ),
    ]

    return {
        "rho_dust": rho_dust,
        "continuity_dust": continuity_dust,
        "rho_w": rho_w,
        "continuity_w": continuity_w,
        "pressure_term": pressure_term,
        "dust_pressure_term": dust_pressure_term,
        "growth_residual": growth_residual,
        "rows": rows,
    }


def markdown_rows(rows):
    return "\n".join(
        "| {row_id} | {candidate} | {symbolic_result} | {gate_status} | {disposition} | {next_obligation} |".format(
            row_id=row.row_id,
            candidate=row.candidate,
            symbolic_result=row.symbolic_result,
            gate_status=row.gate_status,
            disposition=row.disposition,
            next_obligation=row.next_obligation,
        )
        for row in rows
    )


def write_report(data):
    rows = markdown_rows(data["rows"])
    md = f"""# VacuumForge Dark Excess Clustering/Conservation Probe

## Purpose

This report tests the first clustering and conservation gates for dustlike
vacuum-sector excess. It does not derive dark matter abundance or halo
phenomenology.

This report depends on:

```text
dark_excess_source_ledger_017
```

It satisfies:

```text
dark_excess_clustering_conservation_required_017
```

## Symbolic Checks

Dust conservation:

```text
rho_dust = {sp.sstr(data["rho_dust"])}
a d rho_dust/da + 3 rho_dust = {sp.sstr(data["continuity_dust"])}
```

Constant-w conservation form:

```text
rho(a,w) = {sp.sstr(data["rho_w"])}
a d rho/da + 3(1+w)rho = {sp.sstr(data["continuity_w"])}
```

Pressure and growth proxies:

```text
pressure term = {sp.sstr(data["pressure_term"])}
pressure term at c_s^2 = 0 = {sp.sstr(data["dust_pressure_term"])}
matter-era delta=a growth residual = {sp.sstr(data["growth_residual"])}
```

## Gate Ledger

| row | candidate | symbolic result | gate status | disposition | next obligation |
| --- | --- | --- | --- | --- | --- |
{rows}

## Current Conclusion

A separately conserved, pressureless `w = 0` excess has the minimum
clustering-readiness face, but it is still not a dark-sector model. It needs a
production mechanism, abundance calculation, and source ledger before it can be
used as dark matter. Pressure-supported or exchanging excess rows require
their own routing. Ordinary matter insertion is rejected as source
double-counting.

## Classification

```text
result type: dark-excess clustering/conservation probe
scope: dustlike excess readiness after source/equation-of-state ledger
conclusion: conserved pressureless dust is a candidate only; abundance and production remain open
non-conclusion: no dark matter abundance, halo model, or particle identity is derived
```

The next technical target is:

```text
dark_excess_abundance_production_required_018
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")


def record_archive(ns, rows):
    marker_id = "dark_excess_clustering_conservation_probe_018"
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[sp.Symbol("dark_excess_source_ledger_result")],
        output=sp.Symbol("dark_excess_clustering_conservation_result"),
        method="SymPy continuity, sound-speed, and growth-proxy checks",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        is_placeholder=False,
        scope="Clustering and conservation readiness for dark-sector excess",
    )

    for row in rows:
        status = GovernanceStatus.CANDIDATE_ROUTE if row.row_id == "conserved_pressureless_dust" else GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
        if row.row_id == "ordinary_matter_insertion":
            status = GovernanceStatus.REJECTED_ROUTE
        ns.record_claim(
            ClaimRecord(
                claim_id=f"dark_excess_clustering_row_{row.row_id}_018",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=status,
                statement=f"{row.row_id}: {row.disposition}",
                derivation_ids=[marker_id],
                obligation_ids=["dark_excess_abundance_production_required_018"],
            )
        )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="dark_excess_clustering_conservation_required_017",
            script_id=SCRIPT_ID,
            title="Test clustering and conservation gates for dark excess",
            status=ObligationStatus.SATISFIED,
            required_by=["017_dark_excess_source_ledger__dark_excess_source_ledger"],
            satisfied_by=[SCRIPT_ID],
            description=(
                "Satisfied by checking dust conservation, pressure support, "
                "growth readiness, exchange-ledger needs, and source insertion."
            ),
        )
    )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="dark_excess_abundance_production_required_018",
            script_id=SCRIPT_ID,
            title="Test abundance and production gates for dark excess",
            status=ObligationStatus.OPEN,
            required_by=[SCRIPT_ID],
            description=(
                "A conserved pressureless excess is only a candidate. It needs "
                "a production or formation mechanism and abundance route before "
                "being treated as dark-sector physics."
            ),
        )
    )


def main() -> None:
    header("Vacuum Sector 018: Dark Excess Clustering/Conservation Probe")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    data = run_sympy_checks()

    out = ScriptOutput()
    for row in data["rows"]:
        status = StatusMark.DEFER
        if row.row_id == "conserved_pressureless_dust":
            status = StatusMark.OBLIGATION
        elif row.row_id == "ordinary_matter_insertion":
            status = StatusMark.FAIL
        with out.governance_assessments():
            out.line(row.row_id, status, row.disposition)
    with out.unresolved_obligations():
        out.line(
            "Dark excess abundance/production required",
            StatusMark.OBLIGATION,
            "derive production and abundance before treating dustlike excess as dark matter",
        )

    record_archive(ns, data["rows"])
    ns.write_run_metadata()
    write_report(data)

    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
