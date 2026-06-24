#!/usr/bin/env python3
"""
neighboring_mismatch_inventory.py

VacuumForge-managed inventory for candidate neighboring-mismatch rules.

This is not a strain action or branch-selection theorem. It records which
between-point comparison rules are baseline placeholders, which require explicit
routing, and which remain underdetermined before candidate strain dynamics can
open.

Output:
    theory_v3/development/vacuum_sector/01_strain_functional/
        neighboring_mismatch_inventory_vacuumforge.md
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
    / "neighboring_mismatch_inventory_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "x_contract_inventory_002",
        "002_x_contract_inventory__x_contract_inventory",
        "x_contract_inventory_002",
    )
]


@dataclass(frozen=True)
class MismatchOption:
    name: str
    comparison_rule: str
    candidate_invariant: str
    boundary_requirement: str
    conservation_route: str
    mode_risk: str
    epsilon_status: str
    status: str
    next_obligation: str


OPTIONS = [
    MismatchOption(
        name="Levi-Civita metric transport",
        comparison_rule="compare g_ab by the torsion-free metric-compatible connection",
        candidate_invariant="EH/GHY curvature scalar baseline",
        boundary_requirement="induced metric plus GHY-style boundary term",
        conservation_route="Bianchi identity and stress conservation in GR branch",
        mode_risk="baseline two-TT-mode branch after constraints",
        epsilon_status="epsilon = 0 only when paired with EH/GHY baseline",
        status="metric-transport placeholder",
        next_obligation="explain why vacuum ontology selects Levi-Civita metric transport",
    ),
    MismatchOption(
        name="independent affine connection",
        comparison_rule="compare X using a connection independent of metric reduction",
        candidate_invariant="Palatini/metric-affine curvature or connection strain",
        boundary_requirement="connection boundary data or compatible boundary counterterm",
        conservation_route="requires metric compatibility, projective gauge, or routed nonmetric current",
        mode_risk="torsion, nonmetricity, or projective modes if not constrained",
        epsilon_status="extra-field route required",
        status="extra-connection route required",
        next_obligation="derive compatibility or route torsion/nonmetric residuals explicitly",
    ),
    MismatchOption(
        name="calibration map",
        comparison_rule="compare local interval responses through a calibration/coherence map",
        candidate_invariant="calibration mismatch scalar not yet specified",
        boundary_requirement="calibration boundary data not yet specified",
        conservation_route="Noether identity absent until calibration field/action is defined",
        mode_risk="nonmetric drift or species-dependent clock/ruler effects",
        epsilon_status="underdetermined without new axiom",
        status="partial mismatch contract",
        next_obligation="define calibration variable, invariant, and matter-coupling route",
    ),
    MismatchOption(
        name="holonomy or loop mismatch",
        comparison_rule="compare transport around infinitesimal loops",
        candidate_invariant="curvature/holonomy scalar; EH-like versus curvature-squared choice unresolved",
        boundary_requirement="curvature-action boundary term depends on derivative order",
        conservation_route="Bianchi-like identity possible but invariant-dependent",
        mode_risk="curvature-squared or higher-derivative modes unless routed",
        epsilon_status="not yet classified",
        status="partial mismatch contract",
        next_obligation="explain why the leading scalar is EH-like or classify residual modes",
    ),
    MismatchOption(
        name="medium strain tensor",
        comparison_rule="compare internal medium/order-parameter gradients",
        candidate_invariant="constitutive elastic scalar not yet specified",
        boundary_requirement="medium boundary/defect data not yet specified",
        conservation_route="requires medium stress and exchange ledger",
        mode_risk="preferred-frame, anisotropy, longitudinal or extra medium modes",
        epsilon_status="underdetermined without new axiom",
        status="underdetermined without new axiom",
        next_obligation="state constitutive law and route extra modes and frame effects",
    ),
    MismatchOption(
        name="Finsler direction map",
        comparison_rule="compare direction-dependent interval responses",
        candidate_invariant="Finsler/nonquadratic strain scalar not yet specified",
        boundary_requirement="direction-bundle boundary data not yet specified",
        conservation_route="requires routed nonmetric matter calibration identity",
        mode_risk="null-cone, PPN, propagation, and species-calibration deviations",
        epsilon_status="requires explicit residual route",
        status="partial mismatch contract",
        next_obligation="route nonquadratic response through epsilon tests before physical use",
    ),
    MismatchOption(
        name="nonlocal kernel",
        comparison_rule="compare X(p) and X(q) through a kernel or global constraint",
        candidate_invariant="nonlocal relaxation functional not yet specified",
        boundary_requirement="global/bulk-boundary split not yet specified",
        conservation_route="requires nonlocal conservation or relaxation identity",
        mode_risk="large-scale response, acausality, or hidden local equation modification",
        epsilon_status="nonlocal route required",
        status="nonlocal route required",
        next_obligation="quarantine to Lambda/dark/large-scale sector unless local equations stay closed",
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
    marks = {
        "complete mismatch contract": StatusMark.PASS,
        "partial mismatch contract": StatusMark.DEFER,
        "metric-transport placeholder": StatusMark.DEFER,
        "extra-connection route required": StatusMark.OBLIGATION,
        "nonlocal route required": StatusMark.OBLIGATION,
        "underdetermined without new axiom": StatusMark.OBLIGATION,
        "fails accumulated gate": StatusMark.FAIL,
        "not yet evaluated": StatusMark.INFO,
    }
    if status not in marks:
        raise ValueError(f"Unknown neighboring-mismatch status: {status!r}")
    return marks[status]


def governance_status(status: str) -> GovernanceStatus:
    if status == "fails accumulated gate":
        return GovernanceStatus.REJECTED_ROUTE
    if status in {
        "extra-connection route required",
        "nonlocal route required",
        "underdetermined without new axiom",
    }:
        return GovernanceStatus.POLICY_RULE
    if status in {"partial mismatch contract", "metric-transport placeholder"}:
        return GovernanceStatus.UNVERIFIED
    if status == "complete mismatch contract":
        return GovernanceStatus.LICENSED_CLAIM
    if status == "not yet evaluated":
        return GovernanceStatus.UNVERIFIED
    raise ValueError(f"Unknown neighboring-mismatch status: {status!r}")


def write_report():
    rows = "\n".join(
        "| {name} | {comparison_rule} | {candidate_invariant} | {boundary_requirement} | {conservation_route} | {mode_risk} | {epsilon_status} | {status} | {next_obligation} |".format(
            name=item.name,
            comparison_rule=item.comparison_rule,
            candidate_invariant=item.candidate_invariant,
            boundary_requirement=item.boundary_requirement,
            conservation_route=item.conservation_route,
            mode_risk=item.mode_risk,
            epsilon_status=item.epsilon_status,
            status=item.status,
            next_obligation=item.next_obligation,
        )
        for item in OPTIONS
    )

    md = f"""# VacuumForge Neighboring-Mismatch Inventory

## Purpose

This inventory makes the neighboring-mismatch contract operational. It does not
choose a strain action. It classifies currently inventoried ways to compare
`X(p)` and `X(q)` before candidate branch dynamics are opened.

This inventory depends on:

```text
x_contract_inventory_002
```

because an `X` option does not generate dynamics until a between-point
comparison rule is supplied.

## Inventory

| branch | comparison rule | candidate invariant | boundary requirement | conservation route | mode risk | epsilon status | status | next obligation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
{rows}

## Current Conclusion

No currently inventoried non-baseline neighboring-mismatch rule is complete
enough to open candidate strain dynamics without additional routing. The
Levi-Civita metric transport rule is usable as the GR baseline, but remains a
metric-transport placeholder for the vacuum ontology unless a selector explains
why vacuum strain uses that comparison rule.

This is an inventory result, not a global no-go theorem against nonmetric,
nonlocal, holonomy, Finsler, or medium mismatch rules.

## Classification

```text
result type: neighboring-mismatch inventory / governance classification
scope: candidate between-point comparison rules for X(p), X(q)
conclusion: no currently inventoried non-baseline mismatch rule is strain-ready without routing
non-conclusion: no K_strain selected; no epsilon computed; no residual branch licensed
```

The next technical target is the residual gate ledger:

```text
which tests must a routed residual pass before candidate branch work opens?
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")


def record_archive(ns):
    marker_id = "neighboring_mismatch_inventory_003"
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[sp.Symbol("x_contract_inventory")],
        output=sp.Symbol("neighboring_mismatch_inventory"),
        method="neighboring-mismatch contract inventory; no strain action selected",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
        scope="candidate X(p)-to-X(q) comparison status for vacuum-sector strain work",
    )

    for index, item in enumerate(OPTIONS, 1):
        ns.record_claim(
            ClaimRecord(
                claim_id=f"neighboring_mismatch_option_{index:02d}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=governance_status(item.status),
                statement=(
                    f"{item.name}: status {item.status}; epsilon status {item.epsilon_status}; "
                    f"next obligation: {item.next_obligation}."
                ),
                derivation_ids=[marker_id],
                obligation_ids=[],
            )
        )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="residual_gate_ledger_required_003",
            script_id=SCRIPT_ID,
            title="Complete residual gate ledger before branch charters",
            status=ObligationStatus.OPEN,
            required_by=[SCRIPT_ID],
            description=(
                "Every routed mismatch residual requires metric-limit, conservation, "
                "boundary, mode-count, hyperbolicity, source-ledger, and weak-field tests."
            ),
        )
    )


def main() -> None:
    header("Vacuum Sector 003: Neighboring-Mismatch Inventory")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    for item in OPTIONS:
        with out.governance_assessments():
            out.line(item.name, status_mark(item.status), f"{item.status}: {item.next_obligation}")
    with out.unresolved_obligations():
        out.line(
            "residual gate ledger required",
            StatusMark.OBLIGATION,
            "mismatch rules do not become candidate branches without residual tests",
        )

    record_archive(ns)
    ns.write_run_metadata()
    write_report()

    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
