#!/usr/bin/env python3
"""
residual_gate_ledger.py

VacuumForge-managed ledger for residual gates.

This is not a candidate residual test. It records the gates that must be passed
or explicitly routed before any candidate can be classified as controlled
epsilon != 0.

Output:
    theory_v3/development/vacuum_sector/03_epsilon_tests/
        residual_gate_ledger_vacuumforge.md
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
    / "03_epsilon_tests"
    / "residual_gate_ledger_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "neighboring_mismatch_inventory_003",
        "003_neighboring_mismatch_inventory__neighboring_mismatch_inventory",
        "neighboring_mismatch_inventory_003",
    )
]


@dataclass(frozen=True)
class ResidualGate:
    gate_id: str
    purpose: str
    required_evidence: str
    fail_route: str
    blocks: str


GATES = [
    ResidualGate(
        gate_id="metric_limit_test",
        purpose="preserve Q_p(v) = g_ab v^a v^b at lowest order or explicitly leave the metric branch",
        required_evidence="local-response expansion and metric-reduction map",
        fail_route="route as nonmetric/nonquadratic branch or reject",
        blocks="hidden change to closed metric response",
    ),
    ResidualGate(
        gate_id="nonquadratic_routing_test",
        purpose="prevent Finsler or nonquadratic response from being hidden inside pseudo-Riemannian proofs",
        required_evidence="explicit nonquadratic variable, coupling route, and observable suppression or channel",
        fail_route="route outside metric branch or reject",
        blocks="untracked null-cone or calibration drift",
    ),
    ResidualGate(
        gate_id="diffeomorphism_identity_test",
        purpose="ensure variational equations imply the correct Noether/conservation identity",
        required_evidence="Noether/Bianchi-style identity or explicit symmetry-breaking route",
        fail_route="route as extra-field/nonconserved sector or reject",
        blocks="unconserved source or coordinate-label dependence",
    ),
    ResidualGate(
        gate_id="boundary_variation_test",
        purpose="make the variational problem well posed",
        required_evidence="total derivative accounting and boundary data/counterterm",
        fail_route="supply boundary completion or reject",
        blocks="uncontrolled boundary equations or hidden boundary source",
    ),
    ResidualGate(
        gate_id="mode_count_test",
        purpose="preserve two TT modes in the GR branch unless extra modes are explicitly routed",
        required_evidence="linearized mode count around Minkowski or GR background",
        fail_route="route extra scalar/vector/tensor modes or reject",
        blocks="hidden scalaron, vector, ghost, or medium mode",
    ),
    ResidualGate(
        gate_id="hyperbolicity_test",
        purpose="preserve Lorentzian causal propagation in the GR limit",
        required_evidence="principal-symbol or propagation-speed check",
        fail_route="route dissipative/nonlocal/elliptic behavior or reject",
        blocks="wrong causal cone or ill-posed evolution",
    ),
    ResidualGate(
        gate_id="source_ledger_test",
        purpose="avoid double-counting matter, scalar flux, Lambda baseline, torsion, nonmetric drift, or dark excess",
        required_evidence="source-role purity ledger",
        fail_route="move to the appropriate source/baseline/extra-field ledger or reject",
        blocks="source duplication and hidden dark-sector insertion",
    ),
    ResidualGate(
        gate_id="weak_field_residual_test",
        purpose="detect hidden Yukawa, PPN, preferred-frame, scalaron, or propagation deviations",
        required_evidence="weak-field expansion or observational residual map",
        fail_route="route as testable residual with bound/kill condition or reject",
        blocks="unnoticed conflict with closed weak-field sector",
    ),
    ResidualGate(
        gate_id="epsilon_classification_test",
        purpose="classify candidate as epsilon = 0 equivalent, controlled epsilon != 0, failed, or underdetermined",
        required_evidence="results from all earlier gates plus kill condition",
        fail_route="retain as not yet evaluated or underdetermined",
        blocks="free-knob epsilon language",
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


def write_report():
    rows = "\n".join(
        "| {gate_id} | {purpose} | {required_evidence} | {fail_route} | {blocks} |".format(
            gate_id=item.gate_id,
            purpose=item.purpose,
            required_evidence=item.required_evidence,
            fail_route=item.fail_route,
            blocks=item.blocks,
        )
        for item in GATES
    )

    md = f"""# VacuumForge Residual Gate Ledger

## Purpose

This ledger makes the residual gate manifest operational. It does not test a
candidate residual. It records the gates that every candidate must pass or
explicitly route before it can be classified as:

```text
controlled epsilon != 0
```

This ledger depends on:

```text
neighboring_mismatch_inventory_003
```

because mismatch rules do not become candidate branches until residual tests
are defined.

## Gate Ledger

| gate | purpose | required evidence | fail route | blocks |
| --- | --- | --- | --- | --- |
{rows}

## Current Conclusion

No candidate residual is currently licensed as controlled `epsilon != 0`.
Candidate branches may be chartered only as not-yet-evaluated or
underdetermined until they provide gate evidence.

This is a gate-ledger result, not a no-go theorem against residuals.

## Classification

```text
result type: residual gate ledger / governance classification
scope: required tests for K_residual candidates
conclusion: controlled epsilon != 0 is unavailable until gates pass or route
non-conclusion: no residual tested; no residual killed; no epsilon computed
```

The next technical target is candidate branch chartering:

```text
open candidate branches only with explicit kill conditions and gate plan.
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")


def record_archive(ns):
    marker_id = "residual_gate_ledger_004"
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[sp.Symbol("neighboring_mismatch_inventory")],
        output=sp.Symbol("residual_gate_ledger"),
        method="residual gate ledger; no candidate residual tested",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
        scope="required tests for vacuum-sector K_residual candidates",
    )

    for index, item in enumerate(GATES, 1):
        ns.record_claim(
            ClaimRecord(
                claim_id=f"residual_gate_{index:02d}_{item.gate_id}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.POLICY_RULE,
                statement=(
                    f"{item.gate_id}: requires {item.required_evidence}; "
                    f"blocks {item.blocks}; fail route: {item.fail_route}."
                ),
                derivation_ids=[marker_id],
                obligation_ids=[],
            )
        )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="candidate_branch_charters_required_004",
            script_id=SCRIPT_ID,
            title="Open candidate branch charters with gate plans",
            status=ObligationStatus.OPEN,
            required_by=[SCRIPT_ID],
            description=(
                "Each candidate branch must include X contract, mismatch contract, "
                "residual gate plan, kill condition, and first concrete test."
            ),
        )
    )


def main() -> None:
    header("Vacuum Sector 004: Residual Gate Ledger")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    for gate in GATES:
        with out.governance_assessments():
            out.line(gate.gate_id, StatusMark.OBLIGATION, f"requires {gate.required_evidence}")
    with out.unresolved_obligations():
        out.line(
            "candidate branch charters required",
            StatusMark.OBLIGATION,
            "branches need kill conditions and gate plans before live candidate work",
        )

    record_archive(ns)
    ns.write_run_metadata()
    write_report()

    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
