# Candidate metric-sector no-overlap operator
#
# Group:
#   20_no_overlap_and_projection_operators
#
# Script type:
#   REQUIREMENTS / DIAGNOSTIC
#
# Purpose
# -------
# Test whether a no-overlap operator can separate A, B_s, zeta insertion, and
# residual trace without scalar double-counting or recovery construction.
#
# Locked-door question:
#
#   Can O separate A, B_s, zeta insertion, and residual trace?


from dataclasses import dataclass
from pathlib import Path
from typing import List

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    BranchDecisionRecord,
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    RecordKind,
    RouteRecord,
    ScriptOutput,
    StatusMark,
)


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


@dataclass
class MetricNoOverlapEntry:
    name: str
    candidate: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="projection_operator_minimum_structure_marker",
        upstream_script_id="20_no_overlap_and_projection_operators__candidate_projection_operator_minimum_structure",
        upstream_derivation_id="projection_operator_minimum_structure_marker",
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


def entry_status_mark(status: str) -> StatusMark:
    return {
        "CANDIDATE": StatusMark.INFO,
        "CONSTRAINED": StatusMark.INFO,
        "DEFER": StatusMark.DEFER,
        "RECOMMENDED": StatusMark.PASS,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "RISK": StatusMark.WARN,
        "SAFE_IF": StatusMark.INFO,
        "STRUCTURAL": StatusMark.INFO,
        "THEOREM_TARGET": StatusMark.DEFER,
        "UNRESOLVED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def build_entries() -> List[MetricNoOverlapEntry]:
    return [
        MetricNoOverlapEntry(
            name="M1: metric-sector no-overlap target",
            candidate="O_metric separates A, B_s, zeta insertion, kappa, and residual trace",
            role="core Group 20 metric target",
            allowed_if="domain/kernel/image/idempotence/boundary behavior are supplied",
            forbidden_if="O_metric is named only to prevent scalar double-counting",
            status="THEOREM_TARGET",
            missing="explicit O_metric operator",
            consequence="metric-sector no-overlap remains theorem target",
        ),
        MetricNoOverlapEntry(
            name="M2: trace/traceless spatial split",
            candidate="decompose spatial perturbation into trace and traceless pieces",
            role="candidate algebraic projector class",
            allowed_if="inner product or contraction metric is specified and trace source routing is defined",
            forbidden_if="trace projection is used to hide zeta/kappa residual overlap",
            status="CANDIDATE",
            missing="metric/pairing and source routing",
            consequence="useful local algebraic structure, not enough for B_s insertion",
        ),
        MetricNoOverlapEntry(
            name="M3: determinant/unimodular split",
            candidate="gamma_ij = exp(2 zeta / 3) * bar_gamma_ij with det(bar_gamma)=1",
            role="structural volume/shear split",
            allowed_if="used as decomposition only, not dynamics",
            forbidden_if="declared to be the B_s/F_zeta field law",
            status="STRUCTURAL",
            missing="source law, insertion law, boundary theorem",
            consequence="supports zeta as volume scalar but does not define O_metric",
        ),
        MetricNoOverlapEntry(
            name="M4: conformal volume projector",
            candidate="project scalar volume response into zeta/B_s companion channel",
            role="candidate B_s insertion projector",
            allowed_if="kernel/image separate B_s companion from residual trace and preserve M_ext",
            forbidden_if="projection is chosen to fit gamma_like or AB",
            status="THEOREM_TARGET",
            missing="kernel/image, coefficient origin, boundary neutrality",
            consequence="B_s/F_zeta insertion remains unresolved",
        ),
        MetricNoOverlapEntry(
            name="M5: A-sector scalar source separation",
            candidate="rho and exterior mass response stay in A-sector only",
            role="scalar mass protection rule",
            allowed_if="A carries long-range mass and B_s/zeta/kappa do not duplicate rho",
            forbidden_if="B_s/zeta/kappa become second mass-scalar channels",
            status="REQUIRED",
            missing="source routing theorem",
            consequence="A-sector mass result remains protected",
        ),
        MetricNoOverlapEntry(
            name="M6: residual zeta killed",
            candidate="if zeta enters B_s, residual zeta metric trace is killed",
            role="current safest metric convention",
            allowed_if="explicitly provisional or derived by real O_metric",
            forbidden_if="treated as a derived no-overlap theorem now",
            status="SAFE_IF",
            missing="residual-kill derivation",
            consequence="safest convention remains provisional",
        ),
        MetricNoOverlapEntry(
            name="M7: residual zeta non-metric",
            candidate="residual zeta survives only as diagnostic/accounting/non-metric variable",
            role="safe fallback branch",
            allowed_if="residual has no metric trace, scalar charge, M_ext shift, or source role",
            forbidden_if="non-metric residual later re-enters metric through accounting",
            status="SAFE_IF",
            missing="non-metric bookkeeping rule",
            consequence="residual variables may survive without double-counting",
        ),
        MetricNoOverlapEntry(
            name="M8: residual restored by O",
            candidate="O permits neutral residual metric trace alongside B_s insertion",
            role="high-burden no-overlap branch",
            allowed_if="real O_metric proves orthogonal/no-overlap residual sector with boundary neutrality",
            forbidden_if="used as escape from residual-kill without kernel/image",
            status="RISK",
            missing="O_metric, measure, boundary theorem, scalar neutrality",
            consequence="not current working route",
        ),
        MetricNoOverlapEntry(
            name="M9: recovery-chosen split",
            candidate="choose metric split from gamma_like, AB, Schwarzschild, or PPN recovery",
            role="forbidden recovery construction",
            allowed_if="recovery is only downstream test",
            forbidden_if="recovery chooses kernel/image/coefficient/residual status",
            status="REJECTED",
            missing="not pursued",
            consequence="recovery cannot define O_metric",
        ),
        MetricNoOverlapEntry(
            name="M10: GR-copy spatial metric",
            candidate="copy GR spatial metric form and name it no-overlap",
            role="forbidden construction shortcut",
            allowed_if="never as derivation",
            forbidden_if="accepted as B_s/F_zeta or O_metric derivation",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents metric insertion from becoming GR notation import",
        ),
        MetricNoOverlapEntry(
            name="M11: B=1/A construction",
            candidate="use exterior B=1/A as general metric-sector projector",
            role="forbidden exterior overextension",
            allowed_if="used only as reduced exterior recovery check",
            forbidden_if="used as parent metric no-overlap rule",
            status="REJECTED",
            missing="not pursued",
            consequence="AB recovery remains downstream diagnostic",
        ),
        MetricNoOverlapEntry(
            name="M12: metric-sector current decision",
            candidate="O_metric cannot yet be defined; residual-kill/non-metric residual remains safest",
            role="current branch decision",
            allowed_if="next scripts keep metric-sector O as theorem target",
            forbidden_if="later scripts treat the convention as solved no-overlap",
            status="RECOMMENDED",
            missing="role-specific metric projector derivation",
            consequence="next script should test source-sector projection",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Metric-sector no-overlap problem")
    print("Question:")
    print()
    print("  Can O separate A, B_s, zeta insertion, and residual trace?")
    print()
    print("Goal:")
    print()
    print("  return to the Group 16 metric-insertion bottleneck using the minimum projector burden")
    print()
    print("Discipline:")
    print()
    print("  no scalar double-counting")
    print("  no exterior scalar charge")
    print("  no M_ext shift")
    print("  no residual trace restoration by name")
    print("  no GR-copy spatial metric")
    print("  no B=1/A construction as parent law")
    print("  recovery downstream only")
    with out.unresolved_obligations():
        out.line("metric-sector no-overlap problem posed", StatusMark.OBLIGATION, "O_metric not yet defined")


def case_1_inventory(entries: List[MetricNoOverlapEntry]) -> None:
    header("Case 1: Metric-sector no-overlap inventory")
    for entry in entries:
        print()
        print("-" * 120)
        print(entry.name)
        print("-" * 120)
        print(f"Candidate: {entry.candidate}")
        print(f"Role: {entry.role}")
        print(f"Allowed if: {entry.allowed_if}")
        print(f"Forbidden if: {entry.forbidden_if}")
        print(f"[{entry_status_mark(entry.status).value}] {entry.name}: {entry.status}")
        print(f"Missing: {entry.missing}")
        print(f"Consequence: {entry.consequence}")


def case_2_compact_table(entries: List[MetricNoOverlapEntry], out: ScriptOutput) -> None:
    header("Case 2: Compact metric-sector ledger")
    print("| Entry | Candidate | Status | Consequence |")
    print("|---|---|---|---|")
    for entry in entries:
        print(f"| {entry.name} | {entry.candidate} | {entry.status} | {entry.consequence} |")
    with out.governance_assessments():
        out.line("compact metric-sector no-overlap ledger produced", StatusMark.INFO, "metric O still theorem target")


def case_3_status_counts(entries: List[MetricNoOverlapEntry], out: ScriptOutput) -> None:
    header("Case 3: Status counts")
    counts = {}
    for entry in entries:
        counts[entry.status] = counts.get(entry.status, 0) + 1
    for status in sorted(counts):
        print(f"{status}: {counts[status]}")
    print()
    print("Interpretation:")
    print("  Trace/traceless and determinant/unimodular splits are useful structure.")
    print("  They do not yet define the metric-sector no-overlap operator.")
    print("  Residual-kill or non-metric residual remains the safest current convention.")
    with out.governance_assessments():
        out.line("metric-sector status count produced", StatusMark.INFO, str(counts))


def case_4_trace_projector_check(out: ScriptOutput) -> None:
    header("Case 4: Trace/traceless algebraic projector check")
    h11, h22, h33 = sp.symbols("h11 h22 h33")
    trace = h11 + h22 + h33
    trace_piece = sp.Matrix([
        [trace / 3, 0, 0],
        [0, trace / 3, 0],
        [0, 0, trace / 3],
    ])
    traceless_piece = sp.Matrix([
        [h11 - trace / 3, 0, 0],
        [0, h22 - trace / 3, 0],
        [0, 0, h33 - trace / 3],
    ])
    traceless_trace = sp.simplify(sum(traceless_piece[i, i] for i in range(3)))
    print("For diagonal spatial perturbation h = diag(h11,h22,h33):")
    print()
    print(f"trace(h) = {trace}")
    print()
    print("Trace piece:")
    print(trace_piece)
    print()
    print("Traceless piece:")
    print(traceless_piece)
    print()
    print(f"trace(traceless_piece) = {traceless_trace}")
    print()
    print("Interpretation:")
    print("  The trace/traceless split is an algebraic projector candidate.")
    print("  It does not by itself decide whether trace belongs to B_s, zeta, kappa,")
    print("  residual bookkeeping, or A-sector spatial response.")
    with out.derived_results():
        out.line("trace/traceless split verified algebraically", StatusMark.PASS, "trace of traceless part is zero")
    with out.governance_assessments():
        out.line("trace split insufficient for metric no-overlap", StatusMark.DEFER, "source routing and boundary behavior missing")


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("Metric-sector no-overlap fails if:")
    print()
    print("1. A and zeta/kappa both carry rho scalar mass response.")
    print("2. zeta enters B_s and remains independent residual metric trace.")
    print("3. kappa restores killed residual zeta trace.")
    print("4. recovery chooses the trace split or coefficient.")
    print("5. B=1/A is promoted from exterior diagnostic to parent law.")
    print("6. GR spatial metric is copied as O_metric.")
    print("7. boundary leakage or exterior scalar charge is hidden by projection.")
    print("8. M_ext shifts outside the A-sector source law.")
    with out.counterexamples():
        out.line("zeta-both metric branch rejected", StatusMark.FAIL, "B_s companion plus residual metric trace double-counts")
        out.line("recovery-chosen metric split rejected", StatusMark.FAIL, "recovery remains downstream")
        out.line("B=1/A construction rejected", StatusMark.FAIL, "exterior diagnostic is not parent projector")


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Metric-sector no-overlap is not solved.")
    print()
    print("Useful structures exist:")
    print()
    print("  trace/traceless algebraic split")
    print("  determinant/unimodular volume split")
    print("  conformal-volume zeta handle")
    print()
    print("But they do not yet provide:")
    print()
    print("  O_metric domain/kernel/image")
    print("  B_s/F_zeta insertion law")
    print("  residual-kill derivation")
    print("  boundary neutrality theorem")
    print("  A-sector mass protection theorem")
    print()
    print("Current safest convention:")
    print()
    print("  if zeta enters B_s, residual zeta/kappa metric trace is killed or non-metric")
    print("  unless a real O_metric is later derived")
    print()
    print("Possible next artifact:")
    print("  candidate_metric_sector_no_overlap_operator.md")
    print()
    print("Possible next script:")
    print("  candidate_source_sector_projection_operator.py")
    with out.governance_assessments():
        out.line("metric-sector O remains theorem target", StatusMark.DEFER, "residual-kill/non-metric residual remains safest convention")


def record_governance(ns) -> None:
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_O_metric_20",
        script_id=SCRIPT_ID,
        title="Derive metric-sector no-overlap operator",
        status=ObligationStatus.OPEN,
        required_by=["metric_sector_no_overlap_route_20"],
        description=(
            "Define O_metric with domain, codomain, kernel, image, composition law, "
            "measure/pairing, metric routing, and boundary behavior."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_B_s_F_zeta_insertion_law_20",
        script_id=SCRIPT_ID,
        title="Derive B_s/F_zeta insertion law",
        status=ObligationStatus.OPEN,
        required_by=["metric_sector_no_overlap_route_20"],
        description="Show how zeta or volume structure enters B_s without GR-copying or recovery tuning.",
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_residual_kill_or_nonmetric_rule_20",
        script_id=SCRIPT_ID,
        title="Derive residual-kill or non-metric residual rule",
        status=ObligationStatus.OPEN,
        required_by=["metric_sector_no_overlap_route_20"],
        description="Show why residual zeta/kappa metric trace is killed, non-metric, or genuinely no-overlap.",
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_metric_boundary_neutrality_20",
        script_id=SCRIPT_ID,
        title="Derive metric-sector boundary neutrality",
        status=ObligationStatus.OPEN,
        required_by=["metric_sector_no_overlap_route_20"],
        description="Show no exterior scalar charge, no far-zone scalar flux, no shell source, and no M_ext shift.",
    ))

    ns.record_route(RouteRecord(
        route_id="metric_sector_no_overlap_route_20",
        script_id=SCRIPT_ID,
        name="Metric-sector no-overlap theorem route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[
            "derive_O_metric_20",
            "derive_B_s_F_zeta_insertion_law_20",
            "derive_residual_kill_or_nonmetric_rule_20",
            "derive_metric_boundary_neutrality_20",
        ],
        activation_conditions=[
            "O_metric has domain/kernel/image",
            "B_s/F_zeta insertion law is not recovery-defined",
            "residual trace does not double-count",
            "boundary neutrality is derived",
        ],
    ))
    ns.record_route(RouteRecord(
        route_id="metric_residual_kill_safe_convention_20",
        script_id=SCRIPT_ID,
        name="Residual-kill / non-metric residual safety convention",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[],
        activation_conditions=[
            "explicitly provisional",
            "not claimed as derived O_metric",
            "residual has no metric trace, scalar charge, or M_ext effect",
        ],
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_O_metric_20",
        script_id=SCRIPT_ID,
        branch_id="metric_sector_no_overlap_operator",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "derive_O_metric_20",
            "derive_B_s_F_zeta_insertion_law_20",
            "derive_residual_kill_or_nonmetric_rule_20",
            "derive_metric_boundary_neutrality_20",
        ],
        description="O_metric remains deferred: trace/traceless and conformal-volume splits are structural but not a full metric-sector projector.",
    ))
    for decision_id, branch_id, description in [
        (
            "reject_zeta_both_metric_branch_20",
            "zeta_B_s_companion_and_residual_metric_trace",
            "Reject zeta as both B_s companion and independent residual metric trace without real O_metric.",
        ),
        (
            "reject_recovery_chosen_metric_split_20",
            "recovery_chosen_metric_sector_split",
            "Reject metric split chosen from gamma_like, AB, Schwarzschild, or PPN recovery.",
        ),
        (
            "reject_GR_copy_metric_O_20",
            "GR_copy_metric_no_overlap",
            "Reject copied GR spatial metric as O_metric or B_s/F_zeta derivation.",
        ),
        (
            "reject_B_inverse_A_parent_projector_20",
            "B_inverse_A_parent_metric_projector",
            "Reject B=1/A as a general parent metric projector; it remains exterior recovery diagnostic.",
        ),
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=decision_id,
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            description=description,
        ))

    ns.record_claim(ClaimRecord(
        claim_id="metric_sector_no_overlap_summary",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.HEURISTIC,
        statement=(
            "Trace/traceless and determinant/unimodular splits are useful metric-sector structures, "
            "but they do not yet define O_metric. Residual-kill or non-metric residual remains the "
            "safest convention until B_s/F_zeta insertion, residual status, and boundary neutrality are derived."
        ),
        obligation_ids=[
            "derive_O_metric_20",
            "derive_B_s_F_zeta_insertion_law_20",
            "derive_residual_kill_or_nonmetric_rule_20",
            "derive_metric_boundary_neutrality_20",
        ],
    ))


def main():
    header("Candidate Metric-Sector No-Overlap Operator")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    case_0_problem_statement(out)
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_trace_projector_check(out)
    case_5_failure_controls(out)
    final_interpretation(out)

    record_governance(ns)
    ns.record_derivation(
        derivation_id="metric_sector_no_overlap_operator_marker",
        inputs=[],
        output=sp.Symbol("metric_sector_no_overlap_operator_complete"),
        method="metric_sector_no_overlap_operator",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
