# Candidate no-overlap operator role inventory
#
# Group:
#   20_no_overlap_and_projection_operators
#
# Script type:
#   INVENTORY
#
# Purpose
# -------
# Group 20 starts from the unresolved no-overlap operator O that appears across
# Groups 16-19. This script inventories the jobs currently hidden inside O
# before any projector is accepted as mathematical structure.
#
# Locked-door question:
#
#   What jobs are being hidden inside O?
#
# This is a role inventory, not a projector definition or field equation.


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
class NoOverlapRoleEntry:
    name: str
    hidden_job: str
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
        dependency_id="parent_correction_tensor_group_status_marker",
        upstream_script_id="19_parent_correction_tensor_audit__candidate_parent_correction_tensor_group_status_summary",
        upstream_derivation_id="parent_correction_tensor_group_status_summary_marker",
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
        "THEOREM_TARGET": StatusMark.DEFER,
        "UNRESOLVED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def build_entries() -> List[NoOverlapRoleEntry]:
    return [
        NoOverlapRoleEntry(
            name="O1: universal no-overlap placeholder",
            hidden_job="one O is being asked to separate metric, source, residual, current, curvature, boundary, and correction-tensor sectors",
            role="global audit target",
            allowed_if="universal O is replaced by explicit role-specific projector requirements",
            forbidden_if="one operator is accepted because it promises to prevent every overlap",
            status="UNRESOLVED",
            missing="domain, kernel, image, measure, sector basis, and boundary behavior",
            consequence="universal O is too broad to count as a defined operator",
        ),
        NoOverlapRoleEntry(
            name="O2: O_metric",
            hidden_job="separate A-sector mass response, B_s insertion, zeta volume insertion, and residual metric trace",
            role="metric-sector no-overlap target",
            allowed_if="metric domain, scalar trace basis, residual status, and insertion rule are specified",
            forbidden_if="O erases residual trace after B_s/F_zeta insertion is chosen",
            status="THEOREM_TARGET",
            missing="metric-sector projector and residual-kill derivation",
            consequence="B_s/F_zeta insertion remains theorem target",
        ),
        NoOverlapRoleEntry(
            name="O3: O_residual",
            hidden_job="kill, isolate, or demote zeta/kappa residual trace",
            role="residual safety target",
            allowed_if="residual is explicitly non-metric, diagnostic-only, or projected by a real kernel/image split",
            forbidden_if="residual trace is hidden by vocabulary while still carrying metric/source effect",
            status="SAFE_IF",
            missing="residual kernel/image or non-metric bookkeeping rule",
            consequence="residual-kill remains provisional unless O_residual is derived",
        ),
        NoOverlapRoleEntry(
            name="O4: O_source",
            hidden_job="separate ordinary matter, A-sector mass, curvature accounting, exchange source, and optional dark source roles",
            role="source-sector separation target",
            allowed_if="source projectors preserve ordinary matter routing and A-sector mass charge",
            forbidden_if="O hides double-counting of T_mu_nu, rho, e_curv, A_curv, Sigma/R, or dark labels",
            status="THEOREM_TARGET",
            missing="source-domain projector and ordinary matter separation theorem",
            consequence="source separation remains required before correction tensors can be inserted",
        ),
        NoOverlapRoleEntry(
            name="O5: O_current",
            hidden_job="make J_sub/J_exch or J_V subroles operator-level",
            role="vacuum-current split target",
            allowed_if="J_V and source sides are defined before the split is promoted",
            forbidden_if="projection turns role-level J_sub/J_exch bookkeeping into a current law by name",
            status="DEFER",
            missing="J_V, J_sub/J_exch split criterion, Sigma/R operators",
            consequence="current split remains role-level only",
        ),
        NoOverlapRoleEntry(
            name="O6: O_curv",
            hidden_job="separate curvature admissibility diagnostics from dynamics, source reservoirs, and anti-singularity claims",
            role="curvature diagnostic separation target",
            allowed_if="A_curv/e_curv/J_curv roles remain diagnostic or receive independent definitions",
            forbidden_if="O_curv promotes diagnostic admissibility into dynamics or singularity avoidance",
            status="SAFE_IF",
            missing="curvature diagnostic projector and J_curv definition",
            consequence="curvature admissibility remains branch-filter / diagnostic only",
        ),
        NoOverlapRoleEntry(
            name="O7: O_H",
            hidden_job="make H_curv/H_exch source-separated and insertable",
            role="correction-tensor no-overlap target",
            allowed_if="tensor source, divergence, boundary, mass, and scalar neutrality are derived independently",
            forbidden_if="O_H is used as an insertability patch for undefined correction tensors",
            status="REQUIRED",
            missing="projection class, source separation theorem, divergence theorem, boundary theorem",
            consequence="no correction tensor becomes insertable from O language alone",
        ),
        NoOverlapRoleEntry(
            name="O8: O_boundary",
            hidden_job="prevent boundary leakage, exterior scalar charge, far-zone flux, shell sources, and M_ext shifts",
            role="boundary/exterior neutrality target",
            allowed_if="boundary behavior follows from structural support, measure, and flux conditions",
            forbidden_if="O_boundary cancels leakage after it appears",
            status="THEOREM_TARGET",
            missing="boundary measure, support law, exterior neutrality theorem",
            consequence="boundary neutrality remains required and not derived",
        ),
        NoOverlapRoleEntry(
            name="O9: O_recovery",
            hidden_job="choose projectors from gamma_like, AB, Schwarzschild, or PPN recovery",
            role="forbidden recovery-smuggling branch",
            allowed_if="never as construction; recovery may test only after the projector is defined",
            forbidden_if="recovery behavior chooses kernel, image, coefficients, support, or residual status",
            status="REJECTED",
            missing="not pursued",
            consequence="recovery remains downstream",
        ),
        NoOverlapRoleEntry(
            name="O10: O_magic",
            hidden_job="erase overlap without domain, codomain, kernel, image, idempotence, measure, or boundary behavior",
            role="forbidden decorative projector",
            allowed_if="never as derivation",
            forbidden_if="accepted because it has the word projector or no-overlap in its name",
            status="REJECTED",
            missing="not pursued",
            consequence="projection language cannot replace mathematical structure",
        ),
        NoOverlapRoleEntry(
            name="O11: diagnostic sector labels",
            hidden_job="label sectors for audits without active field-equation projection",
            role="safe fallback",
            allowed_if="explicitly diagnostic-only and never used to insert a term or erase a source",
            forbidden_if="diagnostic labels are treated as active operators",
            status="SAFE_IF",
            missing="none if kept diagnostic",
            consequence="audits can continue without claiming O is defined",
        ),
        NoOverlapRoleEntry(
            name="O12: role-specific projector requirement",
            hidden_job="replace one universal O with separate metric/source/current/curvature/boundary/correction requirements",
            role="recommended next structure",
            allowed_if="each projector class declares its own domain, kernel, image, measure, and boundary behavior",
            forbidden_if="all role-specific jobs are collapsed back into one undefined O",
            status="RECOMMENDED",
            missing="minimum projector structure ledger",
            consequence="next script should define the minimum burden for any projector",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: No-overlap operator role inventory problem")
    print("Question:")
    print()
    print("  What jobs are being hidden inside O?")
    print()
    print("Goal:")
    print()
    print("  inventory all uses of no-overlap language before defining an operator")
    print()
    print("Discipline:")
    print()
    print("  no O by declaration")
    print("  no residual eraser")
    print("  no recovery projector")
    print("  no boundary repair")
    print("  no source double-counting eraser")
    print("  no Sigma/R or J_sub/J_exch promotion by name")
    print("  no H_curv/H_exch insertability patch")
    print("  no projector without domain/kernel/image")
    with out.unresolved_obligations():
        out.line("no-overlap role inventory problem posed", StatusMark.OBLIGATION, "minimum projector structure still required")


def case_1_inventory(entries: List[NoOverlapRoleEntry]) -> None:
    header("Case 1: No-overlap role inventory")
    for entry in entries:
        print()
        print("-" * 120)
        print(entry.name)
        print("-" * 120)
        print(f"Hidden job: {entry.hidden_job}")
        print(f"Role: {entry.role}")
        print(f"Allowed if: {entry.allowed_if}")
        print(f"Forbidden if: {entry.forbidden_if}")
        print(f"[{entry_status_mark(entry.status).value}] {entry.name}: {entry.status}")
        print(f"Missing: {entry.missing}")
        print(f"Consequence: {entry.consequence}")


def case_2_compact_table(entries: List[NoOverlapRoleEntry], out: ScriptOutput) -> None:
    header("Case 2: Compact no-overlap role ledger")
    print("| Entry | Hidden job | Status | Consequence |")
    print("|---|---|---|---|")
    for entry in entries:
        print(f"| {entry.name} | {entry.hidden_job} | {entry.status} | {entry.consequence} |")
    with out.governance_assessments():
        out.line("compact no-overlap role ledger produced", StatusMark.INFO, "role inventory only")


def case_3_status_counts(entries: List[NoOverlapRoleEntry], out: ScriptOutput) -> None:
    header("Case 3: Status counts")
    counts = {}
    for entry in entries:
        counts[entry.status] = counts.get(entry.status, 0) + 1
    for status in sorted(counts):
        print(f"{status}: {counts[status]}")
    print()
    print("Interpretation:")
    print("  O has too many jobs to be accepted as one universal operator.")
    print("  Metric, source, current, curvature, boundary, and correction tensor roles need")
    print("  role-specific projector requirements.")
    print("  Recovery and decorative O branches are rejected.")
    with out.governance_assessments():
        out.line("no-overlap status count produced", StatusMark.INFO, str(counts))


def case_4_role_split(out: ScriptOutput) -> None:
    header("Case 4: Role split decision")
    print("Required role-specific splits:")
    print()
    print("  O_metric   -> A/B_s/zeta/residual metric separation")
    print("  O_source   -> ordinary matter / curvature / exchange source separation")
    print("  O_current  -> J_V / J_sub / J_exch split only after currents exist")
    print("  O_curv     -> curvature diagnostics versus dynamics")
    print("  O_boundary -> boundary and exterior neutrality")
    print("  O_H        -> correction tensor source/divergence separation")
    print()
    print("Current decision:")
    print()
    print("  one universal O is not currently a defined operator")
    print("  role-specific projector requirements are the next technical burden")
    with out.governance_assessments():
        out.line("universal O rejected as current structure", StatusMark.DEFER, "role-specific requirements needed")


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("No-overlap inventory fails if:")
    print()
    print("1. O is defined as whatever prevents overlap.")
    print("2. O erases residual trace after the fact.")
    print("3. O makes H_curv or H_exch insertable.")
    print("4. O hides ordinary matter double-counting.")
    print("5. O chooses B_s/F_zeta by recovery.")
    print("6. O separates Sigma/R or J_sub/J_exch by name.")
    print("7. O cancels boundary leakage or scalar charge.")
    print("8. O protects M_ext by declaration.")
    print("9. O has no domain/kernel/image/idempotence burden.")
    print("10. Orthogonality is claimed without measure or pairing.")
    with out.counterexamples():
        out.line("decorative O branch rejected", StatusMark.FAIL, "no domain/kernel/image/idempotence")
        out.line("recovery-defined O branch rejected", StatusMark.FAIL, "recovery remains downstream")


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("The current no-overlap symbol O is carrying too many jobs:")
    print()
    print("  metric insertion separation")
    print("  residual trace isolation")
    print("  source routing")
    print("  current split promotion")
    print("  curvature diagnostic separation")
    print("  correction tensor source separation")
    print("  boundary and exterior neutrality")
    print()
    print("Therefore:")
    print()
    print("  O is not yet defined.")
    print("  One universal O should not be accepted.")
    print("  No-overlap should be split into role-specific projector requirements.")
    print("  Diagnostic sector labels remain safe if they are not active projectors.")
    print()
    print("Possible next artifact:")
    print("  candidate_no_overlap_operator_role_inventory.md")
    print()
    print("Possible next script:")
    print("  candidate_projection_operator_minimum_structure.py")
    with out.governance_assessments():
        out.line("no-overlap inventory complete", StatusMark.PASS, "role-specific projector requirements identified")


def record_governance(ns) -> None:
    ns.record_obligation(ProofObligationRecord(
        obligation_id="define_minimum_projector_structure_20",
        script_id=SCRIPT_ID,
        title="Define minimum projector structure",
        status=ObligationStatus.OPEN,
        required_by=["no_overlap_operator_route"],
        description=(
            "Any no-overlap projector must specify domain, codomain, kernel, image, "
            "composition/idempotence law, measure or pairing if orthogonality is used, "
            "and boundary behavior."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_metric_sector_no_overlap_20",
        script_id=SCRIPT_ID,
        title="Derive metric-sector no-overlap projector",
        status=ObligationStatus.OPEN,
        required_by=["metric_sector_no_overlap_route"],
        description=(
            "Show how A-sector mass response, B_s insertion, zeta volume insertion, "
            "and residual zeta/kappa trace are separated without scalar double-counting."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_source_sector_projection_20",
        script_id=SCRIPT_ID,
        title="Derive source-sector projection",
        status=ObligationStatus.OPEN,
        required_by=["source_sector_projection_route"],
        description=(
            "Show how ordinary matter, A-sector mass, curvature accounting, exchange roles, "
            "and optional dark labels are separated without double-counting or repair."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_boundary_neutral_projection_20",
        script_id=SCRIPT_ID,
        title="Derive boundary-neutral projection behavior",
        status=ObligationStatus.OPEN,
        required_by=["boundary_neutral_projection_route"],
        description=(
            "Show that any projection structure preserves M_ext, exterior scalar silence, "
            "no shell source, no boundary repair, and no far-zone hidden flux."
        ),
    ))

    ns.record_route(RouteRecord(
        route_id="diagnostic_sector_label_route_20",
        script_id=SCRIPT_ID,
        name="Diagnostic sector labels only",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[],
        activation_conditions=[
            "labels are explicitly diagnostic-only",
            "labels are not inserted into field equations",
            "labels do not erase sources or residual trace",
        ],
    ))
    ns.record_route(RouteRecord(
        route_id="role_specific_projector_route_20",
        script_id=SCRIPT_ID,
        name="Role-specific projection requirements",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[
            "define_minimum_projector_structure_20",
            "derive_metric_sector_no_overlap_20",
            "derive_source_sector_projection_20",
            "derive_boundary_neutral_projection_20",
        ],
        activation_conditions=[
            "each projector class declares its domain/kernel/image",
            "orthogonality claims include a measure or pairing",
            "boundary behavior is stated before recovery tests",
        ],
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_universal_O_20",
        script_id=SCRIPT_ID,
        branch_id="universal_no_overlap_operator",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "define_minimum_projector_structure_20",
            "derive_metric_sector_no_overlap_20",
            "derive_source_sector_projection_20",
            "derive_boundary_neutral_projection_20",
        ],
        description=(
            "One universal O is deferred because it lacks domain, kernel, image, "
            "sector basis, measure, and boundary behavior."
        ),
    ))
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_recovery_defined_O_20",
        script_id=SCRIPT_ID,
        branch_id="recovery_defined_no_overlap_operator",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        description="O_recovery is rejected: gamma_like, AB, Schwarzschild, or PPN recovery may test a projector but may not define it.",
    ))
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_decorative_O_20",
        script_id=SCRIPT_ID,
        branch_id="decorative_no_overlap_operator",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        description="O_magic is rejected: no-overlap language without domain/kernel/image/idempotence is not a projector.",
    ))
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_current_split_projection_20",
        script_id=SCRIPT_ID,
        branch_id="current_split_projection_operator",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=["define_minimum_projector_structure_20"],
        description="O_current cannot make J_sub/J_exch operator-level until J_V and source sides are defined.",
    ))

    ns.record_claim(ClaimRecord(
        claim_id="no_overlap_operator_role_inventory_summary",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.HEURISTIC,
        statement=(
            "The no-overlap symbol O is currently carrying multiple distinct jobs. "
            "It should be split into role-specific projection requirements; diagnostic "
            "sector labels remain safe only if not treated as active operators."
        ),
        obligation_ids=[
            "define_minimum_projector_structure_20",
            "derive_metric_sector_no_overlap_20",
            "derive_source_sector_projection_20",
            "derive_boundary_neutral_projection_20",
        ],
    ))


def main():
    header("Candidate No-Overlap Operator Role Inventory")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    case_0_problem_statement(out)
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_role_split(out)
    case_5_failure_controls(out)
    final_interpretation(out)

    record_governance(ns)
    ns.record_derivation(
        derivation_id="no_overlap_operator_role_inventory_marker",
        inputs=[],
        output=sp.Symbol("no_overlap_operator_role_inventory_complete"),
        method="no_overlap_operator_role_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
