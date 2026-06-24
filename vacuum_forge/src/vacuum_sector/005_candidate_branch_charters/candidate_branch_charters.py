#!/usr/bin/env python3
"""
candidate_branch_charters.py

VacuumForge-managed candidate branch charter ledger.

This is not candidate dynamics. It opens the first branch charters only as
gate-planned, not-yet-live candidates after the residual gate ledger.

Output:
    theory_v3/development/vacuum_sector/02_candidate_branches/
        candidate_branch_charters_vacuumforge.md
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
    / "02_candidate_branches"
    / "candidate_branch_charters_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "residual_gate_ledger_004",
        "004_residual_gate_ledger__residual_gate_ledger",
        "residual_gate_ledger_004",
    )
]

GATE_IDS = [
    "metric_limit_test",
    "nonquadratic_routing_test",
    "diffeomorphism_identity_test",
    "boundary_variation_test",
    "mode_count_test",
    "hyperbolicity_test",
    "source_ledger_test",
    "weak_field_residual_test",
    "epsilon_classification_test",
]

ALLOWED_STATUSES = {
    "admissible at epsilon = 0",
    "controlled epsilon != 0 possible",
    "fails accumulated gate",
    "underdetermined without new axiom",
    "not yet evaluated",
}


@dataclass(frozen=True)
class BranchCharter:
    branch_id: str
    name: str
    purpose: str
    x_variable: str
    metric_reduction_map: str
    neighboring_mismatch_rule: str
    candidate_invariant: str
    boundary_term_or_data: str
    matter_coupling_route: str
    expected_epsilon_status: str
    gate_plan: dict[str, str]
    known_risks: str
    kill_condition: str
    first_concrete_test: str
    status: str


BRANCHES = [
    BranchCharter(
        branch_id="eh_ghy_baseline",
        name="EH/GHY baseline",
        purpose="baseline closed metric branch; defines epsilon = 0",
        x_variable="metric data g_ab",
        metric_reduction_map="identity map to the pseudo-Riemannian metric",
        neighboring_mismatch_rule="Levi-Civita metric transport",
        candidate_invariant="R with GHY boundary completion",
        boundary_term_or_data="fixed induced boundary metric plus GHY term",
        matter_coupling_route="standard metric stress tensor",
        expected_epsilon_status="epsilon = 0",
        gate_plan={
            "metric_limit_test": "verify local interval response is the metric branch",
            "nonquadratic_routing_test": "not applicable inside pseudo-Riemannian branch",
            "diffeomorphism_identity_test": "use contracted Bianchi identity",
            "boundary_variation_test": "use GHY differentiability ledger",
            "mode_count_test": "verify two TT modes in the linearized limit",
            "hyperbolicity_test": "verify Lorentzian principal symbol",
            "source_ledger_test": "use metric stress-tensor source route",
            "weak_field_residual_test": "recover Newtonian/PPN baseline",
            "epsilon_classification_test": "classify as epsilon = 0 equivalent",
        },
        known_risks="treating the baseline as selected by local response alone",
        kill_condition="fails if used as an ontology selector without a strain-branch selector",
        first_concrete_test="record baseline boundary and TT-mode references in the gate ledger",
        status="admissible at epsilon = 0",
    ),
    BranchCharter(
        branch_id="inert_boundary_topological",
        name="inert boundary or topological residual",
        purpose="separate bulk-inert terms from genuine residual dynamics",
        x_variable="metric data g_ab unless routed otherwise",
        metric_reduction_map="same pointwise metric branch as EH/GHY",
        neighboring_mismatch_rule="Levi-Civita transport unless boundary/topology route differs",
        candidate_invariant="total derivatives, Euler/Gauss-Bonnet-like, or boundary-local terms",
        boundary_term_or_data="must state whether term changes admissible boundary data",
        matter_coupling_route="no new matter source unless boundary channel is explicit",
        expected_epsilon_status="epsilon = 0 equivalent or boundary-quarantined",
        gate_plan={
            "metric_limit_test": "show no change to local metric response",
            "nonquadratic_routing_test": "show no hidden nonquadratic response",
            "diffeomorphism_identity_test": "show invariant total derivative or routed boundary symmetry",
            "boundary_variation_test": "compute boundary variation explicitly",
            "mode_count_test": "show no new bulk modes",
            "hyperbolicity_test": "show no change to bulk principal symbol",
            "source_ledger_test": "show no hidden boundary source double-counting",
            "weak_field_residual_test": "show no bulk Yukawa/PPN residual",
            "epsilon_classification_test": "classify as inert, boundary-quarantined, or failed",
        },
        known_risks="mistaking a boundary accounting term for new bulk physics",
        kill_condition="fails as a residual if it is only a field redefinition or inert boundary term",
        first_concrete_test="vary a representative total derivative and classify boundary data",
        status="not yet evaluated",
    ),
    BranchCharter(
        branch_id="higher_curvature_local",
        name="higher-curvature local residual",
        purpose="test local curvature corrections without hiding extra modes",
        x_variable="metric data g_ab",
        metric_reduction_map="same pointwise metric branch as EH/GHY",
        neighboring_mismatch_rule="Levi-Civita transport",
        candidate_invariant="R^2, R_ab R^ab, R_abcd R^abcd, or controlled combinations",
        boundary_term_or_data="higher-derivative boundary completion required",
        matter_coupling_route="metric stress tensor plus explicit higher-derivative residual route",
        expected_epsilon_status="controlled epsilon != 0 only if all gates pass",
        gate_plan={
            "metric_limit_test": "verify same pointwise metric response",
            "nonquadratic_routing_test": "not applicable unless response variable changes",
            "diffeomorphism_identity_test": "derive Noether identity for higher-curvature action",
            "boundary_variation_test": "supply higher-derivative boundary terms",
            "mode_count_test": "linearize and count scalar/tensor ghost content",
            "hyperbolicity_test": "check principal symbol and derivative order",
            "source_ledger_test": "separate curvature residual from matter source",
            "weak_field_residual_test": "compute Yukawa/PPN residual map",
            "epsilon_classification_test": "classify as controlled, failed, or routed extra-mode branch",
        },
        known_risks="scalaron, spin-2 ghost, hidden Yukawa term, fourth-order boundary problem",
        kill_condition="fails if extra modes or weak-field residuals are not explicitly routed",
        first_concrete_test="SymPy linearized scalar prototype for fourth-order mode emergence",
        status="not yet evaluated",
    ),
    BranchCharter(
        branch_id="metric_affine_extra_connection",
        name="metric-affine connection residual",
        purpose="test independent transport as more than metric Levi-Civita bookkeeping",
        x_variable="metric data plus independent connection or transport variable",
        metric_reduction_map="must reduce to g_ab with compatible Levi-Civita transport in GR limit",
        neighboring_mismatch_rule="independent affine comparison rule",
        candidate_invariant="curvature, torsion, nonmetricity, or compatibility-enforcing invariant",
        boundary_term_or_data="connection boundary data and compatibility constraints required",
        matter_coupling_route="spin/torsion/nonmetric matter route must be explicit",
        expected_epsilon_status="underdetermined without new axiom",
        gate_plan={
            "metric_limit_test": "derive metric compatibility or route deviations",
            "nonquadratic_routing_test": "show connection does not hide nonmetric response",
            "diffeomorphism_identity_test": "derive metric-affine Noether identity",
            "boundary_variation_test": "state connection boundary data",
            "mode_count_test": "count torsion/nonmetric modes",
            "hyperbolicity_test": "check connection-sector principal symbol",
            "source_ledger_test": "separate spin, torsion, and metric stress sources",
            "weak_field_residual_test": "bound preferred-frame or torsion residuals",
            "epsilon_classification_test": "classify as reduced baseline, routed extra field, or failed",
        },
        known_risks="untracked torsion, nonmetricity, preferred-frame effects, source duplication",
        kill_condition="fails if independent connection has no physical route or no reduction proof",
        first_concrete_test="Palatini-style compatibility check under the vacuum assumptions",
        status="underdetermined without new axiom",
    ),
    BranchCharter(
        branch_id="holonomy_loop_mismatch",
        name="holonomy or loop-mismatch strain",
        purpose="test whether between-point mismatch is naturally loop/transport based",
        x_variable="transport or frame data with metric reduction",
        metric_reduction_map="small-loop limit must recover metric curvature branch or route residuals",
        neighboring_mismatch_rule="closed-loop holonomy mismatch",
        candidate_invariant="leading scalar built from loop curvature or holonomy norm",
        boundary_term_or_data="loop anchoring and boundary transport data required",
        matter_coupling_route="must state whether matter sees metric, frame, or holonomy data",
        expected_epsilon_status="not yet evaluated",
        gate_plan={
            "metric_limit_test": "expand small loops and compare with metric curvature",
            "nonquadratic_routing_test": "route any nonquadratic holonomy norm",
            "diffeomorphism_identity_test": "prove relabeling-invariant loop construction",
            "boundary_variation_test": "state boundary loop/transport data",
            "mode_count_test": "linearize and identify extra transport modes",
            "hyperbolicity_test": "check local limit principal symbol",
            "source_ledger_test": "avoid adding holonomy as a second matter source",
            "weak_field_residual_test": "compute leading weak-field holonomy residual",
            "epsilon_classification_test": "classify as EH-like, controlled residual, or underdetermined",
        },
        known_risks="assuming curvature-as-loop automatically selects EH",
        kill_condition="fails if the leading scalar is chosen by taste rather than a mismatch rule",
        first_concrete_test="small-loop expansion ledger comparing candidate scalars",
        status="not yet evaluated",
    ),
    BranchCharter(
        branch_id="finsler_nonquadratic_directional",
        name="Finsler or nonquadratic directional response",
        purpose="test nonquadratic interval response without hiding it inside metric proofs",
        x_variable="direction-dependent interval response",
        metric_reduction_map="quadratic Hessian limit plus explicit nonquadratic remainder",
        neighboring_mismatch_rule="direction-dependent comparison or calibration rule",
        candidate_invariant="Finsler curvature or nonquadratic strain scalar",
        boundary_term_or_data="direction-bundle boundary data required",
        matter_coupling_route="matter calibration and null-cone route must be explicit",
        expected_epsilon_status="underdetermined without new axiom",
        gate_plan={
            "metric_limit_test": "show the quadratic limit and residual size",
            "nonquadratic_routing_test": "route null-cone and calibration consequences",
            "diffeomorphism_identity_test": "derive bundle/relabeling identity",
            "boundary_variation_test": "state direction-bundle boundary variation",
            "mode_count_test": "count direction-sector modes or constraints",
            "hyperbolicity_test": "check causal cone and well-posedness",
            "source_ledger_test": "separate calibration drift from stress tensor",
            "weak_field_residual_test": "compute PPN/preferred-direction residuals",
            "epsilon_classification_test": "classify as routed nonmetric branch or failed",
        },
        known_risks="untracked null-cone drift, preferred direction, matter calibration conflict",
        kill_condition="fails if nonquadratic response is used while citing metric-branch closure",
        first_concrete_test="directional perturbation prototype with explicit metric Hessian limit",
        status="underdetermined without new axiom",
    ),
    BranchCharter(
        branch_id="medium_configuration_elastic",
        name="medium or configuration-elastic strain",
        purpose="test a deeper material/configuration variable beneath metric data",
        x_variable="internal medium/configuration field plus metric response map",
        metric_reduction_map="constitutive map from medium state to g_ab required",
        neighboring_mismatch_rule="medium strain tensor or configuration-gradient mismatch",
        candidate_invariant="elastic energy, defect strain, or compatibility violation",
        boundary_term_or_data="medium boundary data and defect admissibility required",
        matter_coupling_route="must state whether matter couples to metric only or medium channel",
        expected_epsilon_status="underdetermined without new axiom",
        gate_plan={
            "metric_limit_test": "derive metric response from the constitutive map",
            "nonquadratic_routing_test": "route anisotropic or nonlinear response",
            "diffeomorphism_identity_test": "separate gauge labels from physical medium labels",
            "boundary_variation_test": "state medium and defect boundary data",
            "mode_count_test": "count medium modes and freeze/routing conditions",
            "hyperbolicity_test": "check medium propagation or relaxation law",
            "source_ledger_test": "avoid double-counting medium stress as matter stress",
            "weak_field_residual_test": "bound anisotropy and preferred-frame residuals",
            "epsilon_classification_test": "classify as new axiom branch, controlled residual, or failed",
        },
        known_risks="preferred structure, extra modes, anisotropy, source double-counting",
        kill_condition="fails if constitutive law or matter route is not specified",
        first_concrete_test="minimal constitutive-map contract before any dynamics",
        status="underdetermined without new axiom",
    ),
    BranchCharter(
        branch_id="nonlocal_relaxation",
        name="nonlocal or relaxation strain",
        purpose="test large-scale/baseline relaxation without changing closed local GR equations",
        x_variable="metric data plus nonlocal kernel or relaxation state",
        metric_reduction_map="local limit must reduce to the closed metric branch",
        neighboring_mismatch_rule="kernel-weighted or history-dependent comparison",
        candidate_invariant="nonlocal action kernel, relaxation functional, or baseline selector",
        boundary_term_or_data="history, domain, and boundary kernel data required",
        matter_coupling_route="must quarantine Lambda/dark-sector channel from ordinary stress tensor",
        expected_epsilon_status="not yet evaluated",
        gate_plan={
            "metric_limit_test": "show local metric equations remain closed or route deviation",
            "nonquadratic_routing_test": "route nonlocal response outside local metric proof",
            "diffeomorphism_identity_test": "derive covariant kernel identity or route breaking",
            "boundary_variation_test": "state domain/history boundary data",
            "mode_count_test": "identify memory/relaxation modes",
            "hyperbolicity_test": "check causality and well-posed history dependence",
            "source_ledger_test": "quarantine Lambda/dark excess from matter T_ab",
            "weak_field_residual_test": "bound local and solar-system leakage",
            "epsilon_classification_test": "classify as quarantined sector, controlled residual, or failed",
        },
        known_risks="acausal kernel, hidden local-field modification, dark-sector source insertion",
        kill_condition="fails if it changes closed local equations while being used as a background channel",
        first_concrete_test="local-limit quarantine test for a toy relaxation kernel",
        status="not yet evaluated",
    ),
]


def validate_charters():
    for branch in BRANCHES:
        if branch.status not in ALLOWED_STATUSES:
            raise ValueError(f"{branch.branch_id}: invalid status {branch.status!r}")
        missing = sorted(set(GATE_IDS) - set(branch.gate_plan))
        extra = sorted(set(branch.gate_plan) - set(GATE_IDS))
        if missing or extra:
            raise ValueError(
                f"{branch.branch_id}: gate mismatch; missing={missing}; extra={extra}"
            )

    matrix = sp.Matrix(
        [
            [1 if gate_id in branch.gate_plan else 0 for gate_id in GATE_IDS]
            for branch in BRANCHES
        ]
    )
    row_sums = [sum(matrix.row(i)) for i in range(matrix.rows)]
    if any(total != len(GATE_IDS) for total in row_sums):
        raise ValueError(f"incomplete gate coverage: {row_sums}")
    return matrix, row_sums


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


def markdown_table_rows():
    rows = []
    for branch in BRANCHES:
        rows.append(
            "| {branch_id} | {x_variable} | {neighboring_mismatch_rule} | {candidate_invariant} | {expected_epsilon_status} | {status} | {kill_condition} | {first_concrete_test} |".format(
                branch_id=branch.branch_id,
                x_variable=branch.x_variable,
                neighboring_mismatch_rule=branch.neighboring_mismatch_rule,
                candidate_invariant=branch.candidate_invariant,
                expected_epsilon_status=branch.expected_epsilon_status,
                status=branch.status,
                kill_condition=branch.kill_condition,
                first_concrete_test=branch.first_concrete_test,
            )
        )
    return "\n".join(rows)


def markdown_branch_details():
    parts = []
    for branch in BRANCHES:
        gate_lines = "\n".join(
            f"- `{gate_id}`: {branch.gate_plan[gate_id]}" for gate_id in GATE_IDS
        )
        parts.append(
            f"""### {branch.name}

```text
branch id: {branch.branch_id}
purpose: {branch.purpose}
X variable: {branch.x_variable}
metric reduction map: {branch.metric_reduction_map}
neighboring mismatch rule: {branch.neighboring_mismatch_rule}
candidate invariant/scalar: {branch.candidate_invariant}
boundary term or boundary data: {branch.boundary_term_or_data}
matter coupling route: {branch.matter_coupling_route}
expected epsilon status: {branch.expected_epsilon_status}
known risks: {branch.known_risks}
kill condition: {branch.kill_condition}
first concrete test: {branch.first_concrete_test}
status: {branch.status}
```

Gate plan:

{gate_lines}
"""
        )
    return "\n".join(parts)


def write_report(matrix, row_sums):
    rows = markdown_table_rows()
    details = markdown_branch_details()
    row_sum_text = ", ".join(str(item) for item in row_sums)
    md = f"""# VacuumForge Candidate Branch Charters

## Purpose

This ledger opens the first vacuum-sector candidate branch charters after the
residual gate ledger. It does not select a strain branch, compute `epsilon`, or
license new physics. It only records branch contracts, gate plans, kill
conditions, and first tests.

This ledger depends on:

```text
residual_gate_ledger_004
```

because branch charters are not meaningful until the residual gates exist.

## SymPy Coverage Check

The script constructs a branch-by-gate coverage matrix with shape:

```text
{matrix.rows} x {matrix.cols}
```

Row sums:

```text
{row_sum_text}
```

Each row covers all `{len(GATE_IDS)}` residual gates. This is a governance
coverage check, not a proof that any candidate branch passes the gates.

## Charter Summary

| branch | X variable | neighboring mismatch rule | candidate invariant/scalar | expected epsilon status | status | kill condition | first concrete test |
| --- | --- | --- | --- | --- | --- | --- | --- |
{rows}

## Branch Charters

{details}

## Current Conclusion

The candidate space is now chartered but not live as physics. Only the EH/GHY
baseline is currently admissible at `epsilon = 0`. Every residual branch remains
not-yet-evaluated or underdetermined until its first concrete test supplies
gate evidence.

## Classification

```text
result type: candidate branch charter ledger
scope: starting vacuum-sector strain branches after residual gates
conclusion: candidate work may proceed branch-by-branch under explicit gates
non-conclusion: no residual branch has passed; no non-GR epsilon has been computed
```

The next technical target is the first concrete branch test:

```text
start with the higher-curvature local residual scalar prototype, because it is
the cleanest way to test mode-count, derivative-order, boundary, and weak-field
failure routes before more exotic X choices.
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")


def record_archive(ns):
    marker_id = "candidate_branch_charters_005"
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[sp.Symbol("residual_gate_ledger")],
        output=sp.Symbol("candidate_branch_charters"),
        method="candidate branch charter ledger with SymPy gate coverage matrix",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
        scope="starting vacuum-sector strain branch charters",
    )

    for branch in BRANCHES:
        ns.record_claim(
            ClaimRecord(
                claim_id=f"candidate_branch_charter_{branch.branch_id}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.POLICY_RULE,
                statement=(
                    f"{branch.name}: status {branch.status}; first test: "
                    f"{branch.first_concrete_test}; kill condition: "
                    f"{branch.kill_condition}."
                ),
                derivation_ids=[marker_id],
                obligation_ids=[],
            )
        )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="higher_curvature_scalar_prototype_required_005",
            script_id=SCRIPT_ID,
            title="Run first concrete residual branch test",
            status=ObligationStatus.OPEN,
            required_by=[SCRIPT_ID],
            description=(
                "Begin with the higher-curvature local residual scalar prototype "
                "to test derivative order, mode emergence, boundary data, and "
                "weak-field residual routing before more exotic branches."
            ),
        )
    )


def main() -> None:
    header("Vacuum Sector 005: Candidate Branch Charters")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    matrix, row_sums = validate_charters()

    out = ScriptOutput()
    for branch in BRANCHES:
        mark = (
            StatusMark.PASS
            if branch.status == "admissible at epsilon = 0"
            else StatusMark.OBLIGATION
        )
        with out.governance_assessments():
            out.line(
                branch.branch_id,
                mark,
                f"{branch.status}; first test: {branch.first_concrete_test}",
            )
    with out.unresolved_obligations():
        out.line(
            "higher-curvature scalar prototype required",
            StatusMark.OBLIGATION,
            "run the first concrete residual branch test",
        )

    record_archive(ns)
    ns.write_run_metadata()
    write_report(matrix, row_sums)

    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
