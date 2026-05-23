# Candidate metric insertion boundary support compatibility
#
# Group:
#   24_metric_insertion_recovery_retest
#
# Script type:
#   REQUIREMENTS / DIAGNOSTIC
#
# Purpose
# -------
# Audit whether B_s/F_zeta metric insertion can coexist with Group 22
# boundary/scalar guardrails and Group 23 smooth-support/matching guardrails.
#
# Locked-door question:
#
#   Can metric insertion coexist with Group 22/23 boundary and support guardrails?
#
# This script does not derive B_s/F_zeta insertion.
# It does not prove boundary neutrality.
# It does not prove scalar silence.
# It does not prove compact support.
# It does not prove no-shell matching.
# It does not prove transition-layer neutrality.
# It does not open the parent field equation.
#
# It records that metric insertion cannot be licensed unless boundary/support
# obligations are satisfied or explicitly left theorem-targeted.

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


# =============================================================================
# Utilities
# =============================================================================


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_mark(status: str) -> StatusMark:
    return {
        "BLOCKED": StatusMark.FAIL,
        "CLOSED_DIAGNOSTIC": StatusMark.PASS,
        "DIAGNOSTIC_ONLY": StatusMark.INFO,
        "NOT_READY": StatusMark.DEFER,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "SAFE_IF": StatusMark.INFO,
        "THEOREM_TARGET": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "metric_retest_dep_24",
            "024_metric_insertion_recovery_retest__candidate_metric_insertion_retest_ledger",
            "metric_insertion_retest_ledger_marker_24",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "gamma_AB_dep_24",
            "024_metric_insertion_recovery_retest__candidate_gamma_AB_recovery_diagnostics",
            "gamma_AB_recovery_diagnostics_marker_24",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g22_summary_dep_24",
            "022_boundary_neutrality_and_scalar_silence__candidate_group_22_boundary_neutrality_status_summary",
            "group22_boundary_neutrality_status_summary_marker_22",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g23_summary_dep_24",
            "023_smooth_support_and_matching_laws__candidate_group_23_matching_laws_status_summary",
            "group23_matching_laws_status_summary_marker_23",
            RecordKind.INVENTORY_MARKER,
        ),
    ]

    for dependency_id, upstream_script_id, upstream_derivation_id, expected_record_kind in dependencies:
        ns.declare_dependency(
            dependency_id=dependency_id,
            upstream_script_id=upstream_script_id,
            upstream_derivation_id=upstream_derivation_id,
            expected_record_kind=expected_record_kind,
        )

    return archive, ns, invalidated


def ensure_archive_write_dirs(ns) -> None:
    for attr in (
        "routes_path",
        "branch_decisions_path",
        "claims_path",
        "obligations_path",
        "derivations_path",
        "governance_path",
    ):
        path_obj = getattr(ns, attr, None)
        if path_obj is not None:
            path_obj.mkdir(parents=True, exist_ok=True)


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


# =============================================================================
# Data models
# =============================================================================


@dataclass
class BoundarySupportLedger:
    C_ext: sp.Symbol
    I_nonA: sp.Symbol
    q_A_tail: sp.Symbol
    sigma_shell: sp.Symbol
    value_jump: sp.Symbol
    slope_flux: sp.Symbol
    layer_load: sp.Symbol
    recovery_seam: sp.Symbol
    repair_route: sp.Symbol
    compatibility_load: sp.Expr


@dataclass
class CompatibilityCondition:
    name: str
    condition: str
    status: str
    failure_if: str
    consequence: str


@dataclass
class CompatibilityBranch:
    name: str
    branch: str
    status: str
    allowed_if: str
    rejected_if: str


@dataclass
class RejectedCompatibilityRoute:
    name: str
    route: str
    forbidden_use: str
    status: str
    consequence: str


# =============================================================================
# Builders
# =============================================================================


def build_ledger() -> BoundarySupportLedger:
    C_ext, I_nonA, q_A_tail, sigma_shell, value_jump, slope_flux, layer_load, recovery_seam, repair_route = sp.symbols(
        "C_ext I_nonA q_A_tail sigma_shell value_jump slope_flux layer_load recovery_seam repair_route",
        real=True,
    )
    compatibility_load = sp.simplify(
        C_ext
        + I_nonA
        + q_A_tail
        + sigma_shell
        + value_jump
        + slope_flux
        + layer_load
        + recovery_seam
        + repair_route
    )

    return BoundarySupportLedger(
        C_ext=C_ext,
        I_nonA=I_nonA,
        q_A_tail=q_A_tail,
        sigma_shell=sigma_shell,
        value_jump=value_jump,
        slope_flux=slope_flux,
        layer_load=layer_load,
        recovery_seam=recovery_seam,
        repair_route=repair_route,
        compatibility_load=compatibility_load,
    )


def build_conditions() -> List[CompatibilityCondition]:
    return [
        CompatibilityCondition(
            name="B1: no exterior scalar tail",
            condition="C_ext = 0 for all ordinary-relevant residual scalar channels",
            status="REQUIRED",
            failure_if="metric insertion leaves C/r exterior scalar tail",
            consequence="scalar silence is violated",
        ),
        CompatibilityCondition(
            name="B2: no non-A far-zone current flux",
            condition="I_nonA = 0 unless neutral transport is derived",
            status="REQUIRED",
            failure_if="metric insertion exports I/(4*pi*r^2) current flux",
            consequence="boundary/current silence is violated",
        ),
        CompatibilityCondition(
            name="B3: no induced A-tail",
            condition="q_A_tail = 0",
            status="REQUIRED",
            failure_if="metric insertion seam leaves delta A = q/r",
            consequence="protected A-sector mass is shifted",
        ),
        CompatibilityCondition(
            name="B4: no shell source",
            condition="sigma_shell = 0 and no hidden shell/source load",
            status="REQUIRED",
            failure_if="metric insertion creates shell source or finite-width disguise",
            consequence="no-shell matching is violated",
        ),
        CompatibilityCondition(
            name="B5: value/slope matching",
            condition="value_jump = 0 and slope_flux = 0 or derived equivalents",
            status="REQUIRED",
            failure_if="value matching alone or nonzero slope flux is used",
            consequence="boundary regularity ladder is bypassed",
        ),
        CompatibilityCondition(
            name="B6: neutral transition layer",
            condition="layer_load = 0 or derived neutral transition law",
            status="REQUIRED",
            failure_if="smooth layer hides scalar, A-tail, current, shell/source, recovery, or source load",
            consequence="smoothness is mistaken for neutrality",
        ),
        CompatibilityCondition(
            name="B7: recovery-independent seam",
            condition="recovery_seam = 0; support/smoothing/boundary/layer data are not selected from recovery",
            status="REQUIRED",
            failure_if="gamma/AB/Schwarzschild/PPN targets choose seam data",
            consequence="recovery smuggling returns",
        ),
        CompatibilityCondition(
            name="B8: no repair route",
            condition="repair_route = 0; no O/H/dark/exchange/curvature/current repair patch",
            status="REQUIRED",
            failure_if="repair object supplies missing support or boundary law",
            consequence="Group 22/23 repair exclusions are bypassed",
        ),
    ]


def build_branches() -> List[CompatibilityBranch]:
    return [
        CompatibilityBranch(
            name="C1: compatible insertion candidate",
            branch="B_s/F_zeta candidate with all boundary/support loads zero or theorem-routed",
            status="THEOREM_TARGET",
            allowed_if="all boundary/scalar/support/source/recovery guardrails are derived or explicitly open",
            rejected_if="candidate claims insertion while loads remain unhandled",
        ),
        CompatibilityBranch(
            name="C2: diagnostic-only insertion audit",
            branch="candidate audited against boundary/support ledgers without claiming theorem",
            status="SAFE_IF",
            allowed_if="used to classify risks and obligations only",
            rejected_if="used to license metric insertion",
        ),
        CompatibilityBranch(
            name="C3: recovery-fitted seam",
            branch="support/smoothing/boundary/layer data chosen to pass gamma/AB/Schwarzschild recovery",
            status="REJECTED",
            allowed_if="never as construction",
            rejected_if="used to hide boundary/support failure",
        ),
        CompatibilityBranch(
            name="C4: repair-supported insertion",
            branch="O/H/dark/exchange/curvature/current object supplies missing seam law",
            status="REJECTED",
            allowed_if="never unless the relevant operator/tensor/source theorem is actually derived",
            rejected_if="used as patch by name",
        ),
    ]


def build_rejected_routes() -> List[RejectedCompatibilityRoute]:
    return [
        RejectedCompatibilityRoute(
            name="R1: scalar tail after insertion",
            route="metric_insertion_with_C_ext",
            forbidden_use="B_s/F_zeta licensed while residual C/r tail remains",
            status="REJECTED",
            consequence="scalar silence is bypassed",
        ),
        RejectedCompatibilityRoute(
            name="R2: current flux after insertion",
            route="metric_insertion_with_I_nonA",
            forbidden_use="B_s/F_zeta licensed while non-A far-zone current flux remains",
            status="REJECTED",
            consequence="current/boundary silence is bypassed",
        ),
        RejectedCompatibilityRoute(
            name="R3: A-tail seam shift",
            route="metric_insertion_with_q_A_tail",
            forbidden_use="B_s/F_zeta seam shifts A-sector mass",
            status="REJECTED",
            consequence="Group 21 A-sector mass protection fails",
        ),
        RejectedCompatibilityRoute(
            name="R4: shell source seam",
            route="metric_insertion_with_shell_source",
            forbidden_use="B_s/F_zeta creates or hides boundary shell source",
            status="REJECTED",
            consequence="Group 22/23 no-shell burden is bypassed",
        ),
        RejectedCompatibilityRoute(
            name="R5: toy support theorem",
            route="toy_profile_support_theorem",
            forbidden_use="toy compact profile or smoothness treated as support theorem",
            status="REJECTED",
            consequence="Group 23 matching/support obligations are upgraded falsely",
        ),
        RejectedCompatibilityRoute(
            name="R6: recovery-selected seam",
            route="recovery_selected_boundary_support_layer",
            forbidden_use="gamma/AB/Schwarzschild recovery chooses seam data",
            status="REJECTED",
            consequence="recovery constructs insertion",
        ),
        RejectedCompatibilityRoute(
            name="R7: repair patch seam",
            route="O_H_dark_exchange_curvature_current_seam_patch",
            forbidden_use="repair object supplies missing boundary/support compatibility",
            status="REJECTED",
            consequence="repair exclusions fail",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Metric insertion boundary/support compatibility problem")
    print("Question:")
    print()
    print("  Can metric insertion coexist with Group 22/23 boundary and support guardrails?")
    print()
    print("Reference discipline:")
    print()
    print("  Metric insertion must not leave scalar tails, current fluxes, A-tail shifts, shell sources, toy support, recovery-selected seams, or repair patches.")
    print("  This script audits compatibility burdens; it does not derive them.")

    with out.governance_assessments():
        out.line(
            "metric insertion boundary/support compatibility audit opened",
            StatusMark.INFO,
            "auditing B_s/F_zeta against Group 22 boundary/scalar and Group 23 support/matching guardrails",
        )


def case_1_compatibility_ledger(ledger: BoundarySupportLedger, out: ScriptOutput) -> None:
    header("Case 1: Boundary/support compatibility load ledger")
    print("Representative compatibility loads:")
    print()
    print(f"  C_ext = {sp.sstr(ledger.C_ext)}")
    print(f"  I_nonA = {sp.sstr(ledger.I_nonA)}")
    print(f"  q_A_tail = {sp.sstr(ledger.q_A_tail)}")
    print(f"  sigma_shell = {sp.sstr(ledger.sigma_shell)}")
    print(f"  value_jump = {sp.sstr(ledger.value_jump)}")
    print(f"  slope_flux = {sp.sstr(ledger.slope_flux)}")
    print(f"  layer_load = {sp.sstr(ledger.layer_load)}")
    print(f"  recovery_seam = {sp.sstr(ledger.recovery_seam)}")
    print(f"  repair_route = {sp.sstr(ledger.repair_route)}")
    print()
    print("Compatibility load:")
    print()
    print(f"  L_boundary_support = {sp.sstr(ledger.compatibility_load)}")
    print()
    print("Metric insertion is not licensed while any load remains unproved, unneutralized, or not theorem-routed.")

    with out.derived_results():
        out.line(
            "boundary/support compatibility load ledger stated",
            StatusMark.OBLIGATION,
            f"L_boundary_support = {sp.sstr(ledger.compatibility_load)}",
        )


def case_2_conditions(conditions: List[CompatibilityCondition], out: ScriptOutput) -> None:
    header("Case 2: Boundary/support compatibility conditions")
    for condition in conditions:
        print()
        print("-" * 120)
        print(condition.name)
        print("-" * 120)
        print(f"Condition: {condition.condition}")
        print(f"[{status_mark(condition.status).value}] {condition.name}: {condition.status}")
        print(f"Failure if: {condition.failure_if}")
        print(f"Consequence: {condition.consequence}")

    with out.unresolved_obligations():
        out.line(
            "boundary/support compatibility conditions populated",
            StatusMark.OBLIGATION,
            f"{len(conditions)} compatibility conditions remain required",
        )


def case_3_branches(branches: List[CompatibilityBranch], out: ScriptOutput) -> None:
    header("Case 3: Boundary/support compatibility branches")
    for branch in branches:
        print()
        print("-" * 120)
        print(branch.name)
        print("-" * 120)
        print(f"Branch: {branch.branch}")
        print(f"[{status_mark(branch.status).value}] {branch.name}: {branch.status}")
        print(f"Allowed if: {branch.allowed_if}")
        print(f"Rejected if: {branch.rejected_if}")

    with out.governance_assessments():
        out.line(
            "boundary/support compatibility branches classified",
            StatusMark.PASS,
            f"{len(branches)} branches classified",
        )


def case_4_rejected_routes(routes: List[RejectedCompatibilityRoute], out: ScriptOutput) -> None:
    header("Case 4: Rejected boundary/support compatibility shortcuts")
    for route in routes:
        print()
        print("-" * 120)
        print(route.name)
        print("-" * 120)
        print(f"Route: {route.route}")
        print(f"Forbidden use: {route.forbidden_use}")
        print(f"[{status_mark(route.status).value}] {route.name}: {route.status}")
        print(f"Consequence: {route.consequence}")

    with out.counterexamples():
        out.line(
            "boundary/support metric-insertion shortcuts rejected",
            StatusMark.FAIL,
            "scalar tails, current fluxes, A-tail shifts, shell seams, toy support, recovery-selected seams, and repair patches remain rejected",
        )


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("The metric insertion boundary/support audit fails if a later script allows:")
    print()
    print("1. B_s/F_zeta licensed while C_ext remains")
    print("2. B_s/F_zeta licensed while I_nonA remains")
    print("3. B_s/F_zeta seam shifts A-sector mass")
    print("4. B_s/F_zeta creates or hides shell source")
    print("5. value matching alone treated as no-shell support")
    print("6. smoothness or toy compact profile treated as support theorem")
    print("7. transition layer hides scalar/A/current/shell/source/recovery load")
    print("8. recovery diagnostics choose support/smoothing/boundary/layer data")
    print("9. O/H/dark/exchange/curvature/current patch supplies missing seam law")
    print("10. parent equation opened from boundary/support compatibility audit alone")

    with out.governance_assessments():
        out.line(
            "boundary/support compatibility failure controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not use metric insertion to bypass Group 22/23 guardrails",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Metric insertion boundary/support compatibility result:")
    print()
    print("  B_s/F_zeta cannot be licensed if it leaves scalar tails, current flux, A-tail shifts, shell sources, value/slope mismatch, transition-layer loads, recovery-selected seam data, or repair routes.")
    print("  Boundary/scalar silence and smooth support remain theorem-targeted unless actually derived.")
    print("  Diagnostic compatibility may classify a candidate but cannot prove insertion.")
    print()
    print("Possible next script:")
    print("  candidate_metric_insertion_source_compatibility.py")
    print()
    print("Tiny goblin label:")
    print("  No seam toll. No hidden tail. No smooth disguise.")

    with out.governance_assessments():
        out.line(
            "metric insertion boundary/support compatibility audit complete",
            StatusMark.PASS,
            "boundary/support guardrails imported; insertion theorem remains open",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, ledger: BoundarySupportLedger) -> None:
    ns.record_derivation(
        derivation_id="metric_insertion_boundary_support_load_24",
        inputs=[
            ledger.C_ext,
            ledger.I_nonA,
            ledger.q_A_tail,
            ledger.sigma_shell,
            ledger.value_jump,
            ledger.slope_flux,
            ledger.layer_load,
            ledger.recovery_seam,
            ledger.repair_route,
        ],
        output=ledger.compatibility_load,
        method="sum representative boundary/support compatibility loads",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="boundary_support_compatibility_ledger",
        scope="Group 24 metric insertion recovery retest",
    )

    ns.record_derivation(
        derivation_id="metric_insertion_boundary_support_marker_24",
        inputs=[
            sp.Symbol("C_ext"),
            sp.Symbol("I_nonA"),
            sp.Symbol("q_A_tail"),
            sp.Symbol("shell_absence"),
            sp.Symbol("value_slope_matching"),
            sp.Symbol("transition_layer_neutrality"),
            sp.Symbol("recovery_independent_seam"),
            sp.Symbol("no_repair_route"),
        ],
        output=sp.Symbol("metric_insertion_boundary_support_conditions_stated"),
        method="Group 24 metric insertion boundary/support compatibility ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="requirements_marker",
        scope="Group 24 metric insertion recovery retest",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g24_derive_no_C_ext_after_insertion", "Derive no exterior scalar tail after insertion"),
        ("g24_derive_no_I_nonA_after_insertion", "Derive no non-A current flux after insertion"),
        ("g24_derive_no_A_tail_after_insertion", "Derive no A-tail mass shift after insertion"),
        ("g24_derive_no_shell_after_insertion", "Derive no shell source after insertion"),
        ("g24_derive_value_slope_match_for_insertion", "Derive value/slope matching for insertion seam"),
        ("g24_derive_transition_neutral_for_insertion", "Derive neutral transition layer for insertion"),
        ("g24_derive_recovery_independent_insertion_seam", "Derive recovery-independent insertion seam"),
        ("g24_derive_no_repair_insertion_seam", "Derive no-repair insertion seam"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g24_boundary_support_route"],
            description=(
                "Metric insertion boundary/support compatibility remains theorem-targeted until tails, current flux, A-tail, shell source, "
                "matching, transition, recovery independence, and no-repair constraints are derived."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g24_derive_no_C_ext_after_insertion",
        "g24_derive_no_I_nonA_after_insertion",
        "g24_derive_no_A_tail_after_insertion",
        "g24_derive_no_shell_after_insertion",
        "g24_derive_value_slope_match_for_insertion",
        "g24_derive_transition_neutral_for_insertion",
        "g24_derive_recovery_independent_insertion_seam",
        "g24_derive_no_repair_insertion_seam",
    ]

    ns.record_route(RouteRecord(
        route_id="g24_boundary_support_route",
        script_id=SCRIPT_ID,
        name="Group 24 metric insertion boundary/support compatibility route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "no scalar tail remains",
            "no non-A current flux remains",
            "no A-tail mass shift remains",
            "no shell source or hidden layer load remains",
            "value/slope matching is derived",
            "transition layer neutrality is derived",
            "seam data are recovery-independent",
            "no repair route is used",
        ],
    ))

    for branch_id in [
        "insertion_with_C_ext",
        "insertion_with_I_nonA",
        "insertion_with_A_tail",
        "insertion_with_shell_source",
        "toy_support_theorem",
        "recovery_selected_seam",
        "repair_patch_seam",
        "parent_from_boundary_support_audit",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_24",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; metric insertion cannot bypass boundary/support guardrails.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g24_insertion_requires_boundary_support_compat",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "B_s/F_zeta metric insertion cannot be licensed unless Group 22 boundary/scalar and Group 23 smooth-support/matching guardrails "
            "are satisfied or explicitly left theorem-targeted. Scalar tails, current fluxes, A-tail shifts, shell sources, toy support, "
            "recovery-selected seams, and repair patches remain rejected."
        ),
        derivation_ids=[
            "metric_insertion_boundary_support_load_24",
            "metric_insertion_boundary_support_marker_24",
        ],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Metric Insertion Boundary Support Compatibility")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    ledger = build_ledger()
    conditions = build_conditions()
    branches = build_branches()
    routes = build_rejected_routes()

    case_0_problem_statement(out)
    case_1_compatibility_ledger(ledger, out)
    case_2_conditions(conditions, out)
    case_3_branches(branches, out)
    case_4_rejected_routes(routes, out)
    case_5_failure_controls(out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, ledger)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
