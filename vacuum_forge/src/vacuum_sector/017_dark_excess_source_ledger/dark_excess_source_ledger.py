#!/usr/bin/env python3
"""
dark_excess_source_ledger.py

VacuumForge-managed source ledger for dark-sector excess over the Lambda floor.

This is not a derivation of dark matter. It separates a constant Lambda floor
from transportable or clustered excess candidates and records which equation
of state faces require downstream gates.

Output:
    theory_v3/development/vacuum_sector/05_dark_sector/
        dark_excess_source_ledger_vacuumforge.md
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
    / "dark_excess_source_ledger_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "lambda_frustration_floor_microphysics_probe_016",
        "016_lambda_frustration_floor_microphysics__lambda_frustration_floor_microphysics",
        "lambda_frustration_floor_microphysics_probe_016",
    )
]


@dataclass(frozen=True)
class SourceLedgerRow:
    row_id: str
    source_type: str
    equation_of_state: str
    scaling: str
    ledger_route: str
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
    a, rho0, rho_lambda, rho_excess = sp.symbols("a rho0 rho_Lambda rho_excess", positive=True)
    w = sp.symbols("w", real=True)

    rho_w = rho0 * a ** (-3 * (1 + w))
    scalings = {
        "floor": simplify_expr(rho_w.subs(w, -1)),
        "dust": simplify_expr(rho_w.subs(w, 0)),
        "radiation": simplify_expr(rho_w.subs(w, sp.Rational(1, 3))),
        "string": simplify_expr(rho_w.subs(w, sp.Rational(-1, 3))),
        "wall": simplify_expr(rho_w.subs(w, sp.Rational(-2, 3))),
    }

    total_split = rho_lambda + rho_excess
    split_residual = simplify_expr(total_split - rho_lambda - rho_excess)

    require_equal("source split identity", split_residual, 0)
    require_equal("w=-1 floor scaling", scalings["floor"], rho0)
    require_equal("w=0 dust scaling", scalings["dust"], rho0 / a**3)
    require_equal("w=1/3 radiation scaling", scalings["radiation"], rho0 / a**4)
    require_equal("w=-1/3 string scaling", scalings["string"], rho0 / a**2)
    require_equal("w=-2/3 wall scaling", scalings["wall"], rho0 / a)

    rows = [
        SourceLedgerRow(
            row_id="lambda_floor",
            source_type="constant vacuum floor",
            equation_of_state="w = -1",
            scaling=f"rho(a) = {sp.sstr(scalings['floor'])}",
            ledger_route="Lambda baseline",
            disposition="not dark-sector excess",
            next_obligation="keep floor in Lambda ledger unless an excess is separately defined",
        ),
        SourceLedgerRow(
            row_id="dustlike_excess",
            source_type="gapped/particlelike or nonrelativistic excess",
            equation_of_state="w = 0",
            scaling=f"rho(a) = {sp.sstr(scalings['dust'])}",
            ledger_route="dark-sector excess candidate",
            disposition="candidate only after clustering, conservation, and abundance gates",
            next_obligation="prove clustering and source conservation before use",
        ),
        SourceLedgerRow(
            row_id="radiationlike_excess",
            source_type="relativistic excitation",
            equation_of_state="w = 1/3",
            scaling=f"rho(a) = {sp.sstr(scalings['radiation'])}",
            ledger_route="radiation/excitation ledger",
            disposition="not CDM-like",
            next_obligation="do not count as cold dark excess without a cooling/nonrelativistic route",
        ),
        SourceLedgerRow(
            row_id="stringlike_defect",
            source_type="stringlike defect network",
            equation_of_state="w = -1/3",
            scaling=f"rho(a) = {sp.sstr(scalings['string'])}",
            ledger_route="defect/excess candidate",
            disposition="not CDM-like without additional dynamics",
            next_obligation="route defect dynamics and observational face before use",
        ),
        SourceLedgerRow(
            row_id="walllike_defect",
            source_type="wall-like defect network",
            equation_of_state="w = -2/3",
            scaling=f"rho(a) = {sp.sstr(scalings['wall'])}",
            ledger_route="defect/excess candidate",
            disposition="not CDM-like without additional dynamics",
            next_obligation="route defect dynamics and pressure/anisotropy before use",
        ),
    ]

    return {
        "rho_w": rho_w,
        "scalings": scalings,
        "split_residual": split_residual,
        "rows": rows,
    }


def markdown_rows(rows):
    return "\n".join(
        "| {row_id} | {source_type} | {equation_of_state} | {scaling} | {ledger_route} | {disposition} | {next_obligation} |".format(
            row_id=row.row_id,
            source_type=row.source_type,
            equation_of_state=row.equation_of_state,
            scaling=row.scaling,
            ledger_route=row.ledger_route,
            disposition=row.disposition,
            next_obligation=row.next_obligation,
        )
        for row in rows
    )


def write_report(data):
    rows = markdown_rows(data["rows"])
    md = f"""# VacuumForge Dark Excess Source Ledger

## Purpose

This report opens the dark-sector excess ledger after the Lambda selector
sweep. It separates constant floor, transportable excess, radiationlike
excitations, and defectlike sectors before any dark-matter-like claim is used.

This report depends on:

```text
lambda_frustration_floor_microphysics_probe_016
```

It satisfies:

```text
dark_excess_source_ledger_required_016
```

## Symbolic Checks

Source split:

```text
T_vac = T_floor + T_excess
rho_total - rho_floor - rho_excess = {sp.sstr(data["split_residual"])}
```

Equation-of-state scaling:

```text
rho(a,w) = {sp.sstr(data["rho_w"])}
w = -1:  {sp.sstr(data["scalings"]["floor"])}
w = 0:   {sp.sstr(data["scalings"]["dust"])}
w = 1/3: {sp.sstr(data["scalings"]["radiation"])}
w = -1/3:{sp.sstr(data["scalings"]["string"])}
w = -2/3:{sp.sstr(data["scalings"]["wall"])}
```

## Source Ledger

| row | source type | equation of state | scaling | ledger route | disposition | next obligation |
| --- | --- | --- | --- | --- | --- | --- |
{rows}

## Current Conclusion

The dark-sector excess ledger is open, but no dark-sector model is licensed.
The constant `w = -1` floor remains in the Lambda baseline ledger. A dustlike
`w = 0` excess is the only first-pass CDM-like candidate, and it still needs
conservation, clustering, production, abundance, and source-bookkeeping gates.
Radiationlike and defectlike rows are not CDM-like without further dynamics.

## Classification

```text
result type: dark-sector source ledger
scope: source split and equation-of-state routing after Lambda floor probes
conclusion: floor, dustlike excess, radiation, and defect sectors are separated
non-conclusion: no dark-sector abundance, clustering, or production mechanism is derived
```

The next technical target is:

```text
dark_excess_clustering_conservation_required_017
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")


def record_archive(ns, rows):
    marker_id = "dark_excess_source_ledger_017"
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[sp.Symbol("lambda_frustration_floor_microphysics_probe_result")],
        output=sp.Symbol("dark_excess_source_ledger_result"),
        method="SymPy equation-of-state scaling and source-split ledger checks",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        is_placeholder=False,
        scope="Dark-sector excess source separation after Lambda baseline probes",
    )

    for row in rows:
        status = GovernanceStatus.CANDIDATE_ROUTE if row.row_id == "dustlike_excess" else GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
        if row.row_id == "lambda_floor":
            status = GovernanceStatus.POLICY_RULE
        ns.record_claim(
            ClaimRecord(
                claim_id=f"dark_excess_source_row_{row.row_id}_017",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=status,
                statement=f"{row.row_id}: {row.disposition}",
                derivation_ids=[marker_id],
                obligation_ids=["dark_excess_clustering_conservation_required_017"],
            )
        )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="dark_excess_source_ledger_required_016",
            script_id=SCRIPT_ID,
            title="Open dark-sector excess source ledger",
            status=ObligationStatus.SATISFIED,
            required_by=["016_lambda_frustration_floor_microphysics__lambda_frustration_floor_microphysics"],
            satisfied_by=[SCRIPT_ID],
            description=(
                "Satisfied by separating the Lambda floor from dustlike, "
                "radiationlike, and defectlike excess source rows."
            ),
        )
    )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="dark_excess_clustering_conservation_required_017",
            script_id=SCRIPT_ID,
            title="Test clustering and conservation gates for dark excess",
            status=ObligationStatus.OPEN,
            required_by=[SCRIPT_ID],
            description=(
                "The dustlike row is only a candidate. It must pass clustering, "
                "sound-speed, conservation/exchange, and source-bookkeeping "
                "checks before being treated as dark-sector physics."
            ),
        )
    )


def main() -> None:
    header("Vacuum Sector 017: Dark Excess Source Ledger")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    data = run_sympy_checks()

    out = ScriptOutput()
    for row in data["rows"]:
        status = StatusMark.DEFER
        if row.row_id == "lambda_floor":
            status = StatusMark.PASS
        elif row.row_id == "dustlike_excess":
            status = StatusMark.OBLIGATION
        with out.governance_assessments():
            out.line(row.row_id, status, row.disposition)
    with out.unresolved_obligations():
        out.line(
            "Dark excess clustering/conservation required",
            StatusMark.OBLIGATION,
            "test whether dustlike excess can cluster and conserve without source double-counting",
        )

    record_archive(ns, data["rows"])
    ns.write_run_metadata()
    write_report(data)

    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
