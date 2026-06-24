#!/usr/bin/env python3
"""
x_contract_inventory.py

VacuumForge-managed inventory for candidate vacuum configuration variables X.

This is not a branch selection theorem. It records which X choices are complete
enough to support candidate strain work, which require explicit routing, and
which remain underdetermined.

Output:
    theory_v3/development/vacuum_sector/01_strain_functional/
        x_contract_inventory_vacuumforge.md
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
    / "01_strain_functional"
    / "x_contract_inventory_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "underdetermination_witness_001",
        "001_strain_underdetermination__strain_underdetermination_witness",
        "local_response_underdetermines_strain_001",
    )
]


@dataclass(frozen=True)
class XOption:
    name: str
    x_variable: str
    metric_reduction: str
    matter_route: str
    boundary_data: str
    gauge_physical_split: str
    status: str
    next_obligation: str


OPTIONS = [
    XOption(
        name="metric-data branch",
        x_variable="g_ab",
        metric_reduction="identity: X = g_ab; Q_p(v) = g_ab v^a v^b",
        matter_route="shared metric interval",
        boundary_data="induced metric plus GR-compatible boundary term",
        gauge_physical_split="diffeomorphism redundancy; two TT modes after constraints",
        status="metric-only placeholder",
        next_obligation="cannot by itself explain why vacuum ontology chooses metric data as X",
    ),
    XOption(
        name="interval-response branch",
        x_variable="Q_p(v)",
        metric_reduction="quadratic gate plus polarization gives g_ab(p)",
        matter_route="through derived metric if quadratic; otherwise explicit nonmetric route",
        boundary_data="interval-response boundary data not yet specified",
        gauge_physical_split="pointwise response constrained; between-point gauge split absent",
        status="partial contract",
        next_obligation="supply neighboring mismatch rule for Q_p across points",
    ),
    XOption(
        name="frame/coframe branch",
        x_variable="e^a_mu or coframe data",
        metric_reduction="g_mu_nu = eta_ab e^a_mu e^b_nu",
        matter_route="metric route plus possible spin/frame route",
        boundary_data="frame/coframe or induced metric; choice affects boundary variation",
        gauge_physical_split="local Lorentz redundancy must be separated from physical frame data",
        status="extra-field route required",
        next_obligation="route torsion/spin/frame observables and prove no hidden preferred frame",
    ),
    XOption(
        name="connection/transport branch",
        x_variable="connection or transport map",
        metric_reduction="requires separate metric/calibration relation",
        matter_route="depends on whether matter sees metric, connection, or both",
        boundary_data="connection boundary data or Palatini-type boundary term required",
        gauge_physical_split="projective/torsion/nonmetric sectors require explicit routing",
        status="extra-field route required",
        next_obligation="derive metric compatibility or route nonmetric/torsion residuals",
    ),
    XOption(
        name="internal-medium branch",
        x_variable="medium/order-parameter data",
        metric_reduction="requires constitutive map from medium response to Q_p or g_ab",
        matter_route="must avoid hidden species-dependent calibration",
        boundary_data="medium boundary data and defect data not yet specified",
        gauge_physical_split="internal symmetries and physical medium modes not separated",
        status="underdetermined without new axiom",
        next_obligation="state constitutive law and route extra modes, anisotropy, and frame effects",
    ),
    XOption(
        name="deeper-premetric branch",
        x_variable="unspecified premetric variable",
        metric_reduction="not yet specified",
        matter_route="not yet specified",
        boundary_data="not yet specified",
        gauge_physical_split="not yet specified",
        status="underdetermined without new axiom",
        next_obligation="define X before any strain branch can be evaluated",
    ),
]


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


def status_mark(status: str) -> StatusMark:
    return {
        "partial contract": StatusMark.DEFER,
        "metric-only placeholder": StatusMark.DEFER,
        "extra-field route required": StatusMark.OBLIGATION,
        "underdetermined without new axiom": StatusMark.OBLIGATION,
        "fails accumulated gate": StatusMark.FAIL,
        "complete contract": StatusMark.PASS,
        "not yet evaluated": StatusMark.INFO,
    }.get(status, StatusMark.INFO)


def governance_status(status: str) -> GovernanceStatus:
    if status == "fails accumulated gate":
        return GovernanceStatus.REJECTED_ROUTE
    if status in {"extra-field route required", "underdetermined without new axiom"}:
        return GovernanceStatus.POLICY_RULE
    if status in {"partial contract", "metric-only placeholder"}:
        return GovernanceStatus.UNVERIFIED
    return GovernanceStatus.LICENSED_CLAIM


def write_report():
    rows = "\n".join(
        "| {name} | {x_variable} | {metric_reduction} | {status} | {next_obligation} |".format(
            name=item.name,
            x_variable=item.x_variable,
            metric_reduction=item.metric_reduction,
            status=item.status,
            next_obligation=item.next_obligation,
        )
        for item in OPTIONS
    )

    md = f"""# VacuumForge X Contract Inventory

## Purpose

This inventory makes the `X` contract operational. It does not choose a final
vacuum variable. It classifies candidate `X` choices by whether they are ready
for strain-branch work or still require routing/axioms.

This inventory depends on:

```text
local_response_underdetermines_strain_001
```

because the pointwise local response result showed that an `X` choice must be
paired with a neighboring-mismatch rule before it can generate dynamics.

## Inventory

| branch | X variable | metric reduction | status | next obligation |
| --- | --- | --- | --- | --- |
{rows}

## Current Conclusion

No non-metric `X` option is complete enough to open candidate strain dynamics
without additional routing. The metric-data branch is usable as the GR baseline
but remains a metric-only placeholder for the vacuum ontology unless a selector
explains why vacuum configuration reduces to `g_ab`.

The next technical target is the neighboring-mismatch contract:

```text
how are X(p) and X(q) compared?
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")


def record_archive(ns):
    marker_id = "x_contract_inventory_002"
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[sp.Symbol("local_response_underdetermines_K_strain")],
        output=sp.Symbol("x_contract_inventory"),
        method="contract inventory; no branch selection theorem",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
        scope="candidate X-variable contract status for vacuum-sector strain work",
    )

    for index, item in enumerate(OPTIONS, 1):
        ns.record_claim(
            ClaimRecord(
                claim_id=f"x_contract_option_{index:02d}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=governance_status(item.status),
                statement=(
                    f"{item.name}: X variable {item.x_variable}; status {item.status}; "
                    f"next obligation: {item.next_obligation}."
                ),
                derivation_ids=[marker_id],
                obligation_ids=[],
            )
        )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="neighboring_mismatch_contract_required_002",
            script_id=SCRIPT_ID,
            title="Complete neighboring-mismatch contract",
            status=ObligationStatus.OPEN,
            required_by=[SCRIPT_ID],
            description=(
                "Every nontrivial X option requires a rule for comparing X(p) and X(q), "
                "including boundary data and conservation identity."
            ),
        )
    )


def main() -> None:
    header("Vacuum Sector 002: X Contract Inventory")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    for item in OPTIONS:
        with out.governance_assessments():
            out.line(item.name, status_mark(item.status), f"{item.status}: {item.next_obligation}")
    with out.unresolved_obligations():
        out.line(
            "neighboring mismatch contract required",
            StatusMark.OBLIGATION,
            "X options do not become strain dynamics without X(p)-to-X(q) comparison",
        )

    record_archive(ns)
    ns.write_run_metadata()
    write_report()

    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
