#!/usr/bin/env python3
"""
lambda_baseline_selector_charter.py

VacuumForge-managed charter for candidate Lambda baseline selectors.

This is not a derivation of a nonzero cosmological constant. It records the
minimum fields that each proposed selector must carry before any mechanism can
be treated as a live baseline branch.

Output:
    theory_v3/development/vacuum_sector/04_lambda_baseline/
        lambda_baseline_selector_charter_vacuumforge.md
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
    / "lambda_baseline_selector_charter_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "lambda_baseline_inventory_008",
        "008_lambda_baseline_inventory__lambda_baseline_inventory",
        "lambda_baseline_inventory_008",
    )
]

REQUIRED_FIELDS = [
    "boundary_data",
    "sign_value_mechanism",
    "source_ledger",
    "local_equation_quarantine",
    "falsifier",
    "first_test",
]


@dataclass(frozen=True)
class SelectorCandidate:
    selector_id: str
    selector_name: str
    baseline_role: str
    boundary_data: str
    sign_value_mechanism: str
    source_ledger: str
    local_equation_quarantine: str
    falsifier: str
    first_test: str
    status: str


CANDIDATES = [
    SelectorCandidate(
        selector_id="variational_minimum_selector",
        selector_name="variational minimum selector",
        baseline_role="selects the vacuum reference by a global or constrained minimum",
        boundary_data="admissible vacuum variations and endpoint data for the reference state",
        sign_value_mechanism="stationary minimum or constrained extremum fixes sign and value",
        source_ledger="constant floor only; localized matter and dark excess remain separate",
        local_equation_quarantine="must reduce locally to the closed EH/Lovelock equation with constant Lambda",
        falsifier="fails if it inserts the observed value by hand or destabilizes the flat/de Sitter branch",
        first_test="write the variational object and show which variable is extremized",
        status="chartered only",
    ),
    SelectorCandidate(
        selector_id="admissibility_boundary_selector",
        selector_name="admissibility or boundary selector",
        baseline_role="selects a nonzero baseline by replacing asymptotic flatness with admissible background data",
        boundary_data="explicit asymptotic, horizon, compactness, or domain boundary class",
        sign_value_mechanism="admissibility condition fixes the allowed curvature floor",
        source_ledger="boundary-selected background, not a local matter source",
        local_equation_quarantine="boundary rule must not generate untracked local residual terms",
        falsifier="fails if the value depends on localized source scale or double-counts a boundary term",
        first_test="state the boundary class and derive the permitted constant-curvature family",
        status="chartered only",
    ),
    SelectorCandidate(
        selector_id="topology_global_constraint_selector",
        selector_name="topology or global constraint selector",
        baseline_role="uses global topology or integrated constraints to restrict the baseline",
        boundary_data="global manifold class, compactness condition, or topological sector",
        sign_value_mechanism="integrated constraint fixes or discretizes the curvature floor",
        source_ledger="global constraint ledger; no local stress tensor insertion",
        local_equation_quarantine="local field equations remain EH/Lovelock except for the allowed constant",
        falsifier="fails if a topological invariant is claimed to set local Lambda without a constraint equation",
        first_test="identify the global invariant and its Euler-Lagrange or admissibility role",
        status="chartered only",
    ),
    SelectorCandidate(
        selector_id="measure_identity_selector",
        selector_name="measure identity selector",
        baseline_role="maps the vacuum measure or state-counting identity to a curvature floor",
        boundary_data="measure normalization, state space, and covariance requirements",
        sign_value_mechanism="identity fixes a constant density scale and sign before observation is used",
        source_ledger="measure floor only; transportable excess remains downstream",
        local_equation_quarantine="identity must preserve diffeomorphism covariance and stress conservation",
        falsifier="fails if it is only dimensional fitting or lacks a covariant conserved ledger",
        first_test="write the measure identity and check dimensions, covariance, and conservation",
        status="chartered only",
    ),
    SelectorCandidate(
        selector_id="relaxation_nonlocal_history_selector",
        selector_name="relaxation or nonlocal history selector",
        baseline_role="selects the floor through global relaxation, history, or kernel data",
        boundary_data="history domain, kernel support, initial data, and late-time admissibility class",
        sign_value_mechanism="relaxation fixed point or memory integral determines the constant floor",
        source_ledger="relaxed floor distinct from local matter and clustered excess",
        local_equation_quarantine="must prove local conservation and avoid acausal closed-equation changes",
        falsifier="fails if it violates causality, conservation, or closed local weak-field tests",
        first_test="state the kernel or relaxation variable and prove constant-floor reduction",
        status="chartered only",
    ),
    SelectorCandidate(
        selector_id="frustration_floor_microphysics_selector",
        selector_name="frustration-floor microphysics selector",
        baseline_role="derives a vacuum floor from substance or frustration microphysics",
        boundary_data="microstate class, coarse-graining rule, and vacuum reference ensemble",
        sign_value_mechanism="microphysical frustration or ground-state accounting fixes sign and value",
        source_ledger="floor only; clustered or transportable excess belongs to dark-sector bookkeeping",
        local_equation_quarantine="must not alter the closed local metric response unless routed through residual gates",
        falsifier="fails if it becomes dark matter by assertion or lacks abundance and conservation bookkeeping",
        first_test="state the microphysical variable and derive a constant floor before fitting value",
        status="chartered only",
    ),
]


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


def run_sympy_coverage_check():
    coverage_rows = []
    for candidate in CANDIDATES:
        coverage_rows.append(
            [
                1 if getattr(candidate, field).strip() else 0
                for field in REQUIRED_FIELDS
            ]
        )
    coverage = sp.Matrix(coverage_rows)
    required_total = len(REQUIRED_FIELDS)
    row_totals = [sum(coverage.row(i)) for i in range(coverage.rows)]
    for candidate, row_total in zip(CANDIDATES, row_totals):
        require_true(
            f"{candidate.selector_id} has all required charter fields",
            row_total == required_total,
        )
    require_true("selector charter has candidates", coverage.rows > 0)
    return coverage, row_totals


def markdown_summary_rows():
    return "\n".join(
        "| {selector_id} | {baseline_role} | {status} | {first_test} |".format(
            selector_id=candidate.selector_id,
            baseline_role=candidate.baseline_role,
            status=candidate.status,
            first_test=candidate.first_test,
        )
        for candidate in CANDIDATES
    )


def markdown_detail_sections():
    sections = []
    for candidate in CANDIDATES:
        sections.append(
            f"""### {candidate.selector_name}

```text
id: {candidate.selector_id}
baseline role: {candidate.baseline_role}
boundary data: {candidate.boundary_data}
sign/value mechanism: {candidate.sign_value_mechanism}
source ledger: {candidate.source_ledger}
local-equation quarantine: {candidate.local_equation_quarantine}
falsifier: {candidate.falsifier}
first test: {candidate.first_test}
status: {candidate.status}
```"""
        )
    return "\n\n".join(sections)


def write_report(coverage, row_totals):
    rows = markdown_summary_rows()
    details = markdown_detail_sections()
    candidate_count = len(CANDIDATES)
    required_count = len(REQUIRED_FIELDS)
    totals = ", ".join(str(total) for total in row_totals)
    md = f"""# VacuumForge Lambda Baseline Selector Charter

## Purpose

This report charters candidate selectors for the Lambda baseline. It does not
derive a nonzero `Lambda`, insert an observed value, license a dark-sector
excess, or modify the closed local metric equations.

This report depends on:

```text
lambda_baseline_inventory_008
```

It satisfies:

```text
lambda_baseline_selector_required_008
```

## Required Selector Fields

Every candidate selector must state:

```text
boundary data;
sign/value mechanism;
source ledger;
local-equation quarantine;
falsifier;
first concrete test.
```

## SymPy Coverage Check

This is a governance coverage check, not a physics proof. SymPy verifies that
the charter table has `{candidate_count}` candidates and that each candidate
has all `{required_count}` required fields populated.

```text
coverage matrix shape: {coverage.rows} x {coverage.cols}
row totals: {totals}
required total per candidate: {required_count}
```

## Candidate Selector Summary

| selector | baseline role | status | first test |
| --- | --- | --- | --- |
{rows}

## Candidate Details

{details}

## Current Conclusion

The Lambda selector space is chartered, but no selector is adopted. Future
nonzero `Lambda` mechanisms must pass the selector sieve before they can be
treated as live baseline physics.

The three-way distinction remains:

```text
Lambda = 0:
  asymptotically flat scalar boundary-flux sector when no nonzero background
  curvature is supplied.

Lambda free:
  allowed but unvalued Lovelock/background constant.

Lambda nonzero derived:
  requires a selector that survives boundary, sign/value, source-ledger,
  quarantine, and falsifier checks.
```

## Classification

```text
result type: Lambda selector charter / governance coverage
scope: candidate baseline selectors after Lambda inventory
conclusion: selector candidates are chartered but none is adopted
non-conclusion: nonzero Lambda is not derived; observed value is not inserted
```

The next technical target is a selector sieve:

```text
apply boundary-data, sign/value, source-ledger, local-equation quarantine, and
falsifier checks before opening any specific Lambda mechanism.
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")


def record_archive(ns):
    marker_id = "lambda_baseline_selector_charter_009"
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[sp.Symbol("lambda_baseline_inventory")],
        output=sp.Symbol("lambda_baseline_selector_charter"),
        method="SymPy governance coverage check over candidate selector charter fields",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        is_placeholder=False,
        scope="Candidate selectors for Lambda baseline workstream",
    )

    for candidate in CANDIDATES:
        ns.record_claim(
            ClaimRecord(
                claim_id=f"lambda_selector_candidate_{candidate.selector_id}_009",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.UNVERIFIED,
                statement=(
                    f"{candidate.selector_name} is chartered only. It must pass "
                    f"boundary, sign/value, source-ledger, local-equation "
                    f"quarantine, and falsifier checks before use."
                ),
                derivation_ids=[marker_id],
                obligation_ids=["lambda_selector_sieve_required_009"],
            )
        )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="lambda_baseline_selector_required_008",
            script_id=SCRIPT_ID,
            title="State candidate Lambda baseline selectors",
            status=ObligationStatus.SATISFIED,
            required_by=["008_lambda_baseline_inventory__lambda_baseline_inventory"],
            satisfied_by=[SCRIPT_ID],
            description=(
                "Satisfied by the Lambda selector charter: each candidate now "
                "states boundary data, sign/value mechanism, source ledger, "
                "local-equation quarantine, falsifier, and first test."
            ),
        )
    )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="lambda_selector_sieve_required_009",
            script_id=SCRIPT_ID,
            title="Apply first Lambda selector sieve",
            status=ObligationStatus.OPEN,
            required_by=[SCRIPT_ID],
            description=(
                "Before opening a Lambda mechanism, apply the selector sieve to "
                "candidate rows: boundary data, sign/value mechanism, source "
                "ledger, local-equation quarantine, and falsifier."
            ),
        )
    )


def main() -> None:
    header("Vacuum Sector 009: Lambda Baseline Selector Charter")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    coverage, row_totals = run_sympy_coverage_check()

    out = ScriptOutput()
    for candidate in CANDIDATES:
        with out.governance_assessments():
            out.line(
                candidate.selector_id,
                StatusMark.INFO,
                f"chartered only; first test: {candidate.first_test}",
            )
    with out.unresolved_obligations():
        out.line(
            "Lambda selector sieve required",
            StatusMark.OBLIGATION,
            "screen chartered selectors before opening a specific mechanism",
        )

    record_archive(ns)
    ns.write_run_metadata()
    write_report(coverage, row_totals)

    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
