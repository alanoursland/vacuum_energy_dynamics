#!/usr/bin/env python3
"""
vacuum_sector_program_checkpoint.py

VacuumForge-managed checkpoint after the first vacuum-sector sweep.

This is not a new mechanism branch. It summarizes the branch state after the
residual, Lambda, dark-sector, non-gravitational channel, interior, and
cross-cutting selector ledgers.

Output:
    theory_v3/development/vacuum_sector/00_orientation/
        vacuum_sector_program_checkpoint_vacuumforge.md
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
    / "00_orientation"
    / "vacuum_sector_program_checkpoint_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "global_boundary_topology_selector_rules_028",
        "028_global_boundary_topology_selector_rules__global_boundary_topology_selector_rules",
        "global_boundary_topology_selector_rules_028",
    )
]


@dataclass(frozen=True)
class ProgramLane:
    lane_id: str
    lane: str
    current_status: str
    licensed_physics: int
    blocked_by: str
    next_action: str
    checkpoint_disposition: str
    governance_status: GovernanceStatus


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


def program_lanes():
    return [
        ProgramLane(
            lane_id="eh_ghy_baseline",
            lane="closed metric branch",
            current_status="conditionally reconstructed at epsilon = 0",
            licensed_physics=1,
            blocked_by="none inside adopted GR closure",
            next_action="keep as baseline, not as vacuum-ontology derivation",
            checkpoint_disposition="baseline retained",
            governance_status=GovernanceStatus.LICENSED_CLAIM,
        ),
        ProgramLane(
            lane_id="strain_selector",
            lane="vacuum strain branch selector",
            current_status="central missing object",
            licensed_physics=0,
            blocked_by="X contract and neighboring-mismatch contracts do not choose K_strain",
            next_action="state selector options or adopt a new strain axiom",
            checkpoint_disposition="highest-priority open obligation",
            governance_status=GovernanceStatus.UNRESOLVED_PROOF_OBLIGATION,
        ),
        ProgramLane(
            lane_id="higher_curvature_residual",
            lane="local higher-curvature residual",
            current_status="not licensed as controlled epsilon != 0",
            licensed_physics=0,
            blocked_by="extra derivatives, boundary data, weak-field poles, and mode-routing burden",
            next_action="do not reuse without explicit scalaron/P7prime or inert/topological routing",
            checkpoint_disposition="blocked pending route appeal",
            governance_status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        ),
        ProgramLane(
            lane_id="lambda_baseline",
            lane="nonzero Lambda baseline",
            current_status="allowed but not valued",
            licensed_physics=0,
            blocked_by="no derived selector scale, measure, sign branch, or absolute floor",
            next_action="derive scale/floor before value claims",
            checkpoint_disposition="deferred missing-scale route",
            governance_status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        ),
        ProgramLane(
            lane_id="dark_excess",
            lane="transportable dark-sector excess",
            current_status="dustlike excess candidate only",
            licensed_physics=0,
            blocked_by="production, abundance, conservation/exchange, and source ledger remain incomplete",
            next_action="derive production microphysics or formation fraction before use",
            checkpoint_disposition="candidate but unlicensed",
            governance_status=GovernanceStatus.CANDIDATE_ROUTE,
        ),
        ProgramLane(
            lane_id="non_grav_channels",
            lane="Casimir/UFFT/material channels",
            current_status="quarantined only",
            licensed_physics=0,
            blocked_by="no derived channel operator, coefficient, source ledger, or metric quarantine closure",
            next_action="instantiate operator or keep channel silent",
            checkpoint_disposition="quarantined",
            governance_status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        ),
        ProgramLane(
            lane_id="substance_frame",
            lane="substance-frame observables",
            current_status="silent frame allowed; observable coupling unlicensed",
            licensed_physics=0,
            blocked_by="no bounded coupling operator or source/exchange ledger",
            next_action="derive coupling or retain beta_frame = 0",
            checkpoint_disposition="silent ontology allowed",
            governance_status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        ),
        ProgramLane(
            lane_id="interior_cap",
            lane="strong-interior finite cap",
            current_status="exterior-preserving contract only",
            licensed_physics=0,
            blocked_by="no derived finite-strain invariant, bound, or cap scale",
            next_action="derive K_ved or reject cap route",
            checkpoint_disposition="candidate contract only",
            governance_status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        ),
        ProgramLane(
            lane_id="global_boundary_topology",
            lane="global/boundary/topology selectors",
            current_status="sector selectors only without derived scale",
            licensed_physics=0,
            blocked_by="dimensionful value needs area, volume, measure, length, or admissibility scale",
            next_action="do not treat sector selection as value selection",
            checkpoint_disposition="cross-cutting rule retained",
            governance_status=GovernanceStatus.POLICY_RULE,
        ),
    ]


def run_sympy_checks(lanes):
    licensed_nonbaseline = sum(
        lane.licensed_physics
        for lane in lanes
        if lane.lane_id != "eh_ghy_baseline"
    )
    open_obligations = sum(
        1
        for lane in lanes
        if lane.governance_status
        in {
            GovernanceStatus.UNRESOLVED_PROOF_OBLIGATION,
            GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
            GovernanceStatus.CANDIDATE_ROUTE,
        }
    )
    policy_rules = sum(1 for lane in lanes if lane.governance_status == GovernanceStatus.POLICY_RULE)

    require_equal("no nonbaseline lane is licensed", licensed_nonbaseline, 0)
    require_true("checkpoint has open obligations", open_obligations > 0)
    require_true("checkpoint retains at least one policy rule", policy_rules > 0)

    return {
        "licensed_nonbaseline": licensed_nonbaseline,
        "open_obligations": open_obligations,
        "policy_rules": policy_rules,
        "current_licensed_epsilon": sp.Integer(0),
    }


def markdown_lanes(lanes):
    return "\n".join(
        (
            "| {lane_id} | {lane} | {current_status} | {licensed_physics} | "
            "{blocked_by} | {next_action} | {checkpoint_disposition} |"
        ).format(
            lane_id=lane.lane_id,
            lane=lane.lane,
            current_status=lane.current_status,
            licensed_physics=bool(lane.licensed_physics),
            blocked_by=lane.blocked_by,
            next_action=lane.next_action,
            checkpoint_disposition=lane.checkpoint_disposition,
        )
        for lane in lanes
    )


def write_report(lanes, data):
    lane_md = markdown_lanes(lanes)
    md = f"""# VacuumForge Vacuum-Sector Program Checkpoint

## Purpose

This report checkpoints the vacuum-sector program after the first sweep through
strain contracts, residual gates, Lambda baseline selectors, dark-sector
excess, non-gravitational channels, interior caps, and cross-cutting
global/boundary/topology selector rules.

It depends on:

```text
global_boundary_topology_selector_rules_028
```

It satisfies:

```text
vacuum_sector_program_checkpoint_required_028
```

## Symbolic Readiness Check

The checkpoint condition is:

```text
licensed nonbaseline physics lanes = {data["licensed_nonbaseline"]}
open or deferred obligations = {data["open_obligations"]}
policy rules retained = {data["policy_rules"]}
current licensed epsilon = {sp.sstr(data["current_licensed_epsilon"])}
```

This means the currently licensed gravitational branch remains the
conditionally reconstructed EH/GHY baseline at `epsilon = 0`. No nonbaseline
vacuum-sector mechanism is licensed as new physics by this checkpoint.

## Program Lane Ledger

| lane id | lane | current status | licensed physics | blocked by | next action | checkpoint disposition |
| --- | --- | --- | --- | --- | --- | --- |
{lane_md}

## Current Conclusion

The first vacuum-sector sweep has converted many apparent mechanism openings
into routed obligations. The central unresolved object remains the strain
branch selector: what chooses `X`, neighboring mismatch, and `K_strain` before
side ledgers can be treated as physics.

## Classification

```text
result type: program checkpoint / routing ledger
scope: vacuum-sector branches 001-028
conclusion: no nonbaseline mechanism is licensed; return to strain selector
non-conclusion: no global no-go theorem against Lambda, dark excess, channels, or interiors
```

The next technical target is:

```text
strain_branch_selector_decision_table_required_029
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")


def record_archive(ns, lanes):
    marker_id = "vacuum_sector_program_checkpoint_029"
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[sp.Symbol("global_boundary_topology_selector_rules_result")],
        output=sp.Symbol("vacuum_sector_program_checkpoint_result"),
        method="VacuumForge branch readiness ledger with SymPy count checks",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        is_placeholder=False,
        scope="Vacuum-sector program checkpoint after branches 001-028",
    )

    for lane in lanes:
        ns.record_claim(
            ClaimRecord(
                claim_id=f"vacuum_sector_checkpoint_lane_{lane.lane_id}_029",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=lane.governance_status,
                statement=f"{lane.lane_id}: {lane.checkpoint_disposition}",
                derivation_ids=[marker_id],
                obligation_ids=["strain_branch_selector_decision_table_required_029"],
            )
        )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="vacuum_sector_program_checkpoint_required_028",
            script_id=SCRIPT_ID,
            title="Checkpoint the vacuum-sector program before opening new branches",
            status=ObligationStatus.SATISFIED,
            required_by=["028_global_boundary_topology_selector_rules__global_boundary_topology_selector_rules"],
            satisfied_by=[SCRIPT_ID],
            description=(
                "Satisfied by summarizing branch readiness after the first "
                "vacuum-sector sweep and identifying the strain branch selector "
                "as the next central obligation."
            ),
        )
    )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="strain_branch_selector_decision_table_required_029",
            script_id=SCRIPT_ID,
            title="Build a strain-branch selector decision table",
            status=ObligationStatus.OPEN,
            required_by=[SCRIPT_ID],
            description=(
                "Return to the central missing object by comparing possible "
                "selector routes for X, neighboring mismatch, and K_strain: "
                "accumulated gates force EH/GHY, new strain axiom, nonlocal "
                "relaxation, boundary/global selector, or silent ontology."
            ),
        )
    )


def main() -> None:
    header("Vacuum Sector 029: Program Checkpoint")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    lanes = program_lanes()
    data = run_sympy_checks(lanes)

    out = ScriptOutput()
    for lane in lanes:
        status = StatusMark.PASS if lane.licensed_physics else StatusMark.DEFER
        if lane.governance_status == GovernanceStatus.POLICY_RULE:
            status = StatusMark.DEFER
        with out.governance_assessments():
            out.line(lane.lane_id, status, lane.checkpoint_disposition)
    with out.unresolved_obligations():
        out.line(
            "Strain branch selector decision table required",
            StatusMark.OBLIGATION,
            "return to the central missing selector before opening new mechanisms",
        )

    record_archive(ns, lanes)
    ns.write_run_metadata()
    write_report(lanes, data)

    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
