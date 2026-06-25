#!/usr/bin/env python3
"""
lambda_selector_sieve.py

VacuumForge-managed first sieve for Lambda baseline selector candidates.

This is not a derivation of a nonzero cosmological constant. It checks whether
the chartered selector rows currently contain enough instantiated evidence to
open a concrete nonzero-Lambda mechanism.

Output:
    theory_v3/development/vacuum_sector/04_lambda_baseline/
        lambda_selector_sieve_vacuumforge.md
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
    / "lambda_selector_sieve_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "lambda_baseline_selector_charter_009",
        "009_lambda_baseline_selector_charter__lambda_baseline_selector_charter",
        "lambda_baseline_selector_charter_009",
    )
]

EVIDENCE_GATES = [
    "selector_object",
    "boundary_instantiation",
    "sign_value_derivation",
    "source_conservation",
    "local_equation_quarantine",
    "operational_falsifier",
]


@dataclass(frozen=True)
class SelectorSieveRow:
    selector_id: str
    selector_name: str
    selector_object: int
    boundary_instantiation: int
    sign_value_derivation: int
    source_conservation: int
    local_equation_quarantine: int
    operational_falsifier: int
    missing_first: str
    disposition: str
    next_obligation: str


SIEVE_ROWS = [
    SelectorSieveRow(
        selector_id="variational_minimum_selector",
        selector_name="variational minimum selector",
        selector_object=0,
        boundary_instantiation=0,
        sign_value_derivation=0,
        source_conservation=0,
        local_equation_quarantine=0,
        operational_falsifier=0,
        missing_first="explicit variational object and varied variable",
        disposition="not ready; chartered but no mechanism may open",
        next_obligation="write a variational minimum probe before claiming a selected Lambda value",
    ),
    SelectorSieveRow(
        selector_id="admissibility_boundary_selector",
        selector_name="admissibility or boundary selector",
        selector_object=0,
        boundary_instantiation=0,
        sign_value_derivation=0,
        source_conservation=0,
        local_equation_quarantine=0,
        operational_falsifier=0,
        missing_first="specific boundary class replacing asymptotic flatness",
        disposition="not ready; chartered but no mechanism may open",
        next_obligation="state the boundary class and derive its constant-curvature family",
    ),
    SelectorSieveRow(
        selector_id="topology_global_constraint_selector",
        selector_name="topology or global constraint selector",
        selector_object=0,
        boundary_instantiation=0,
        sign_value_derivation=0,
        source_conservation=0,
        local_equation_quarantine=0,
        operational_falsifier=0,
        missing_first="global constraint equation with variational or admissibility role",
        disposition="not ready; chartered but no mechanism may open",
        next_obligation="identify the invariant and show how it constrains Lambda rather than decorating it",
    ),
    SelectorSieveRow(
        selector_id="measure_identity_selector",
        selector_name="measure identity selector",
        selector_object=0,
        boundary_instantiation=0,
        sign_value_derivation=0,
        source_conservation=0,
        local_equation_quarantine=0,
        operational_falsifier=0,
        missing_first="covariant measure identity with a conserved source ledger",
        disposition="not ready; chartered but no mechanism may open",
        next_obligation="write the identity before using dimensional scales or observed values",
    ),
    SelectorSieveRow(
        selector_id="relaxation_nonlocal_history_selector",
        selector_name="relaxation or nonlocal history selector",
        selector_object=0,
        boundary_instantiation=0,
        sign_value_derivation=0,
        source_conservation=0,
        local_equation_quarantine=0,
        operational_falsifier=0,
        missing_first="kernel, domain, and fixed-point equation",
        disposition="not ready; chartered but no mechanism may open",
        next_obligation="prove constant-floor reduction plus conservation before use",
    ),
    SelectorSieveRow(
        selector_id="frustration_floor_microphysics_selector",
        selector_name="frustration-floor microphysics selector",
        selector_object=0,
        boundary_instantiation=0,
        sign_value_derivation=0,
        source_conservation=0,
        local_equation_quarantine=0,
        operational_falsifier=0,
        missing_first="microstate variable and coarse-graining map",
        disposition="not ready; chartered but no mechanism may open",
        next_obligation="derive a constant floor before assigning abundance or clustering behavior",
    ),
]


def require_equal(label, lhs, rhs) -> None:
    residual = sp.simplify(lhs - rhs)
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


def run_sympy_sieve():
    matrix_rows = []
    for row in SIEVE_ROWS:
        matrix_rows.append(
            [
                row.selector_object,
                row.boundary_instantiation,
                row.sign_value_derivation,
                row.source_conservation,
                row.local_equation_quarantine,
                row.operational_falsifier,
            ]
        )
    evidence = sp.Matrix(matrix_rows)
    gate_count = len(EVIDENCE_GATES)
    row_totals = [sum(evidence.row(i)) for i in range(evidence.rows)]
    pass_vector = sp.Matrix([1 if total == gate_count else 0 for total in row_totals])
    pass_count = sum(pass_vector)

    require_true("sieve has rows", evidence.rows > 0)
    require_equal("no selector row passes the first evidence sieve", pass_count, 0)
    require_true(
        "every row is still missing an instantiated selector object",
        all(row.selector_object == 0 for row in SIEVE_ROWS),
    )

    return {
        "evidence": evidence,
        "row_totals": row_totals,
        "pass_vector": pass_vector,
        "pass_count": pass_count,
        "gate_count": gate_count,
    }


def markdown_rows():
    return "\n".join(
        "| {selector_id} | {scores} | {missing_first} | {disposition} | {next_obligation} |".format(
            selector_id=row.selector_id,
            scores=(
                f"{row.selector_object}/"
                f"{row.boundary_instantiation}/"
                f"{row.sign_value_derivation}/"
                f"{row.source_conservation}/"
                f"{row.local_equation_quarantine}/"
                f"{row.operational_falsifier}"
            ),
            missing_first=row.missing_first,
            disposition=row.disposition,
            next_obligation=row.next_obligation,
        )
        for row in SIEVE_ROWS
    )


def write_report(data):
    rows = markdown_rows()
    row_totals = ", ".join(str(total) for total in data["row_totals"])
    pass_vector = ", ".join(str(value) for value in list(data["pass_vector"]))
    md = f"""# VacuumForge Lambda Selector Sieve

## Purpose

This report applies the first evidence sieve to the chartered Lambda baseline
selectors. It does not reject the selector classes as physics. It only checks
whether any row currently contains enough instantiated evidence to open a
specific nonzero-`Lambda` mechanism.

This report depends on:

```text
lambda_baseline_selector_charter_009
```

It satisfies:

```text
lambda_selector_sieve_required_009
```

## Evidence Gates

Each selector row must supply:

```text
selector object;
boundary instantiation;
sign/value derivation;
source conservation;
local-equation quarantine;
operational falsifier.
```

The score columns below use this order:

```text
selector_object / boundary_instantiation / sign_value_derivation /
source_conservation / local_equation_quarantine / operational_falsifier
```

## SymPy Sieve Check

SymPy evaluates the binary evidence matrix:

```text
matrix shape: {data["evidence"].rows} x {data["evidence"].cols}
row totals: {row_totals}
required total per passing row: {data["gate_count"]}
pass vector: {pass_vector}
pass count: {data["pass_count"]}
```

The current pass count is zero.

The binary score is adequate while every row lacks an instantiated selector
object. Once a future row has partial evidence, this sieve should be promoted
to an absent/partial/complete ledger so partial progress is not mistaken for a
passing selector.

## Sieve Ledger

| selector | evidence score | first missing object | disposition | next obligation |
| --- | --- | --- | --- | --- |
{rows}

## Current Conclusion

No chartered Lambda selector currently passes the first evidence sieve. The
result is not a no-go theorem against nonzero `Lambda`. It says that a
mechanism cannot be opened until at least one row supplies an instantiated
selector object and then passes boundary, sign/value, source, quarantine, and
falsifier checks.

The first concrete handoff is the variational-minimum probe because it is the
least additional-structure selector and can be tested without importing a
microphysics or nonlocal kernel.

## Classification

```text
result type: Lambda selector sieve / evidence readiness check
scope: chartered baseline selectors before mechanism opening
conclusion: no selector row is mechanism-ready
non-conclusion: no selector class is globally killed; nonzero Lambda is not derived
```

The next technical target is:

```text
lambda_variational_minimum_probe_required_010
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")


def record_archive(ns):
    marker_id = "lambda_selector_sieve_010"
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[sp.Symbol("lambda_baseline_selector_charter")],
        output=sp.Symbol("lambda_selector_sieve_result"),
        method="SymPy binary evidence-sieve check over chartered selector rows",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        is_placeholder=False,
        scope="Readiness of Lambda baseline selectors before mechanism opening",
    )

    for row in SIEVE_ROWS:
        ns.record_claim(
            ClaimRecord(
                claim_id=f"lambda_selector_sieve_{row.selector_id}_010",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
                statement=(
                    f"{row.selector_name} does not currently pass the Lambda "
                    f"selector sieve. First missing object: {row.missing_first}."
                ),
                derivation_ids=[marker_id],
                obligation_ids=["lambda_variational_minimum_probe_required_010"],
            )
        )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="lambda_selector_sieve_required_009",
            script_id=SCRIPT_ID,
            title="Apply first Lambda selector sieve",
            status=ObligationStatus.SATISFIED,
            required_by=["009_lambda_baseline_selector_charter__lambda_baseline_selector_charter"],
            satisfied_by=[SCRIPT_ID],
            description=(
                "Satisfied by screening chartered selector rows against the "
                "first evidence gates. No row is mechanism-ready."
            ),
        )
    )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="lambda_variational_minimum_probe_required_010",
            script_id=SCRIPT_ID,
            title="Test the variational-minimum Lambda selector first",
            status=ObligationStatus.OPEN,
            required_by=[SCRIPT_ID],
            description=(
                "Build the first concrete selector object: a variational "
                "minimum probe that checks whether sign and value can be "
                "selected without observed-value insertion."
            ),
        )
    )


def main() -> None:
    header("Vacuum Sector 010: Lambda Selector Sieve")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    data = run_sympy_sieve()

    out = ScriptOutput()
    for row in SIEVE_ROWS:
        with out.governance_assessments():
            out.line(
                row.selector_id,
                StatusMark.OBLIGATION,
                f"not mechanism-ready; first missing object: {row.missing_first}",
            )
    with out.unresolved_obligations():
        out.line(
            "Lambda variational-minimum probe required",
            StatusMark.OBLIGATION,
            "instantiate the first selector object before claiming a selected value",
        )

    record_archive(ns)
    ns.write_run_metadata()
    write_report(data)

    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
