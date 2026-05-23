# Candidate residual kill boundary source compatibility
#
# Group:
#   25_residual_kill_or_no_overlap_theorem
#
# Script type:
#   REQUIREMENTS / DIAGNOSTIC
#
# Purpose
# -------
# Audit whether residual kill / inertness / no-overlap can preserve boundary,
# support, source, and mass guardrails.
#
# Locked-door question:
#
#   Can residual kill / inertness preserve boundary and source guardrails?
#
# This script does not derive residual kill.
# It does not derive non-metric inertness.
# It does not derive active no-overlap O.
# It does not derive boundary neutrality, scalar silence, source compatibility,
# support/matching compatibility, B_s/F_zeta insertion, or parent closure.
#
# It records that residual cleanup cannot be a boundary/source repair route.

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


def status_mark(status: str) -> StatusMark:
    return {
        "BLOCKED": StatusMark.FAIL,
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
            "residual_problem_dep_25",
            "025_residual_kill_or_no_overlap_theorem__candidate_residual_kill_problem_ledger",
            "residual_kill_problem_ledger_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "inertness_dep_25",
            "025_residual_kill_or_no_overlap_theorem__candidate_nonmetric_inertness_conditions",
            "nonmetric_inertness_conditions_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "reentry_dep_25",
            "025_residual_kill_or_no_overlap_theorem__candidate_residual_reentry_exclusion_audit",
            "residual_reentry_exclusion_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "recovery_independence_dep_25",
            "025_residual_kill_or_no_overlap_theorem__candidate_residual_kill_recovery_independence",
            "residual_kill_recovery_independence_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g21_summary_dep_25",
            "021_source_routing_and_mass_neutrality__candidate_group_21_source_routing_status_summary",
            "group21_source_routing_status_summary_marker_21",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g22_summary_dep_25",
            "022_boundary_neutrality_and_scalar_silence__candidate_group_22_boundary_neutrality_status_summary",
            "group22_boundary_neutrality_status_summary_marker_22",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g23_summary_dep_25",
            "023_smooth_support_and_matching_laws__candidate_group_23_matching_laws_status_summary",
            "group23_matching_laws_status_summary_marker_23",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g24_source_dep_25",
            "024_metric_insertion_recovery_retest__candidate_metric_insertion_source_compatibility",
            "metric_insertion_source_compatibility_marker_24",
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


@dataclass
class BoundarySourceCompatibilityLedger:
    A_mass_shift: sp.Symbol
    scalar_tail: sp.Symbol
    nonA_current_flux: sp.Symbol
    boundary_flux: sp.Symbol
    shell_source_load: sp.Symbol
    support_layer_load: sp.Symbol
    ordinary_source_dup: sp.Symbol
    recovery_selected_seam: sp.Symbol
    repair_object: sp.Symbol
    insertion_license: sp.Symbol
    compatibility_failure_load: sp.Expr


@dataclass
class BoundarySourceCondition:
    name: str
    condition: str
    status: str
    failure_if: str
    consequence: str


@dataclass
class BoundarySourceBranch:
    name: str
    branch: str
    status: str
    allowed_if: str
    rejected_if: str


@dataclass
class RejectedBoundarySourceShortcut:
    name: str
    shortcut: str
    forbidden_use: str
    status: str
    consequence: str


def build_ledger() -> BoundarySourceCompatibilityLedger:
    (
        A_mass_shift,
        scalar_tail,
        nonA_current_flux,
        boundary_flux,
        shell_source_load,
        support_layer_load,
        ordinary_source_dup,
        recovery_selected_seam,
        repair_object,
        insertion_license,
    ) = sp.symbols(
        "A_mass_shift scalar_tail nonA_current_flux boundary_flux shell_source_load support_layer_load ordinary_source_dup recovery_selected_seam repair_object insertion_license",
        real=True,
    )

    compatibility_failure_load = sp.simplify(
        A_mass_shift
        + scalar_tail
        + nonA_current_flux
        + boundary_flux
        + shell_source_load
        + support_layer_load
        + ordinary_source_dup
        + recovery_selected_seam
        + repair_object
        + insertion_license
    )

    return BoundarySourceCompatibilityLedger(
        A_mass_shift=A_mass_shift,
        scalar_tail=scalar_tail,
        nonA_current_flux=nonA_current_flux,
        boundary_flux=boundary_flux,
        shell_source_load=shell_source_load,
        support_layer_load=support_layer_load,
        ordinary_source_dup=ordinary_source_dup,
        recovery_selected_seam=recovery_selected_seam,
        repair_object=repair_object,
        insertion_license=insertion_license,
        compatibility_failure_load=compatibility_failure_load,
    )


def build_conditions() -> List[BoundarySourceCondition]:
    return [
        BoundarySourceCondition(
            name="C1: no A-sector mass shift",
            condition="A_mass_shift = 0",
            status="REQUIRED",
            failure_if="residual cleanup changes protected A-sector exterior mass",
            consequence="source routing and mass neutrality fail",
        ),
        BoundarySourceCondition(
            name="C2: no exterior scalar tail",
            condition="scalar_tail = 0",
            status="REQUIRED",
            failure_if="residual cleanup leaves C/r scalar tail",
            consequence="scalar silence fails",
        ),
        BoundarySourceCondition(
            name="C3: no non-A current flux",
            condition="nonA_current_flux = 0",
            status="REQUIRED",
            failure_if="residual cleanup exports non-A current flux",
            consequence="boundary/current silence fails",
        ),
        BoundarySourceCondition(
            name="C4: no boundary flux",
            condition="boundary_flux = 0",
            status="REQUIRED",
            failure_if="residual cleanup leaks through boundary",
            consequence="boundary neutrality fails",
        ),
        BoundarySourceCondition(
            name="C5: no shell/source load",
            condition="shell_source_load = 0",
            status="REQUIRED",
            failure_if="residual cleanup creates shell or finite-width source disguise",
            consequence="no-shell and source compatibility fail",
        ),
        BoundarySourceCondition(
            name="C6: no support/layer load",
            condition="support_layer_load = 0",
            status="REQUIRED",
            failure_if="residual cleanup hides load in support radius, smoothing width, or transition layer",
            consequence="smooth-support/matching guardrails fail",
        ),
        BoundarySourceCondition(
            name="C7: no ordinary source duplication",
            condition="ordinary_source_dup = 0",
            status="REQUIRED",
            failure_if="residual cleanup duplicates rho/M_enc or hides ordinary source load",
            consequence="source no-double-counting fails",
        ),
        BoundarySourceCondition(
            name="C8: no recovery-selected seam",
            condition="recovery_selected_seam = 0",
            status="REQUIRED",
            failure_if="residual cleanup chooses seam/support/boundary data from recovery",
            consequence="recovery constructs residual cleanup",
        ),
        BoundarySourceCondition(
            name="C9: no repair object",
            condition="repair_object = 0",
            status="REQUIRED",
            failure_if="O/H/dark/exchange/curvature/current labels supply residual cleanup",
            consequence="repair route smuggles missing theorem",
        ),
        BoundarySourceCondition(
            name="C10: no insertion license",
            condition="insertion_license = 0",
            status="REQUIRED",
            failure_if="residual cleanup alone licenses B_s/F_zeta insertion",
            consequence="metric insertion theorem is smuggled",
        ),
    ]


def build_branches() -> List[BoundarySourceBranch]:
    return [
        BoundarySourceBranch(
            name="B1: compatible residual cleanup",
            branch="residual kill/inertness/O preserves boundary, support, source, and mass guardrails",
            status="THEOREM_TARGET",
            allowed_if="all compatibility loads vanish sector-by-sector or are theorem-routed",
            rejected_if="cleanup hides any boundary/source/support/mass load",
        ),
        BoundarySourceBranch(
            name="B2: diagnostic-only compatibility audit",
            branch="residual cleanup is audited against guardrails without claiming theorem",
            status="SAFE_IF",
            allowed_if="used only to list obligations and reject shortcuts",
            rejected_if="used to license residual kill or insertion",
        ),
        BoundarySourceBranch(
            name="B3: boundary-repair residual cleanup",
            branch="residual cleanup is chosen to remove tail, flux, A-tail, shell, or layer load",
            status="REJECTED",
            allowed_if="never",
            rejected_if="cleanup repairs boundary/support failure",
        ),
        BoundarySourceBranch(
            name="B4: source-repair residual cleanup",
            branch="residual cleanup is chosen to avoid ordinary source duplication",
            status="REJECTED",
            allowed_if="never",
            rejected_if="cleanup repairs source compatibility failure",
        ),
        BoundarySourceBranch(
            name="B5: insertion-licensing residual cleanup",
            branch="residual cleanup is treated as sufficient for B_s/F_zeta insertion",
            status="REJECTED",
            allowed_if="never",
            rejected_if="cleanup opens metric insertion or parent gate",
        ),
    ]


def build_rejected_shortcuts() -> List[RejectedBoundarySourceShortcut]:
    return [
        RejectedBoundarySourceShortcut(
            name="S1: mass shift cleanup",
            shortcut="residual cleanup shifts A-sector mass",
            forbidden_use="residual kill/inertness/O changes protected A mass charge",
            status="REJECTED",
            consequence="Group 21 mass protection fails",
        ),
        RejectedBoundarySourceShortcut(
            name="S2: tail cleanup by kill",
            shortcut="residual kill hides scalar tail",
            forbidden_use="kill/inertness chosen because C/r tail would otherwise remain",
            status="REJECTED",
            consequence="Group 22 scalar silence is bypassed",
        ),
        RejectedBoundarySourceShortcut(
            name="S3: current cleanup by kill",
            shortcut="residual kill hides non-A current flux",
            forbidden_use="kill/inertness chosen because current flux would otherwise remain",
            status="REJECTED",
            consequence="current silence is bypassed",
        ),
        RejectedBoundarySourceShortcut(
            name="S4: shell/source cleanup by kill",
            shortcut="residual cleanup hides shell/source load",
            forbidden_use="kill/inertness/O hides shell source or finite-width source disguise",
            status="REJECTED",
            consequence="no-shell/source compatibility is bypassed",
        ),
        RejectedBoundarySourceShortcut(
            name="S5: support/layer cleanup",
            shortcut="residual cleanup hides in support or transition layer",
            forbidden_use="support radius, smoothing width, transition layer, or matching condition carries residual cleanup",
            status="REJECTED",
            consequence="Group 23 support/matching guardrails fail",
        ),
        RejectedBoundarySourceShortcut(
            name="S6: source duplication cleanup",
            shortcut="residual status chosen to avoid duplicate ordinary source load",
            forbidden_use="residual control is selected from source no-double-counting failure",
            status="REJECTED",
            consequence="source compatibility constructs residual control",
        ),
        RejectedBoundarySourceShortcut(
            name="S7: repair object cleanup",
            shortcut="O/H/dark/exchange/curvature/current label supplies compatibility",
            forbidden_use="repair object closes residual compatibility gap",
            status="REJECTED",
            consequence="repair theorem is smuggled",
        ),
        RejectedBoundarySourceShortcut(
            name="S8: insertion from compatibility",
            shortcut="boundary/source-compatible cleanup licenses B_s/F_zeta insertion",
            forbidden_use="compatibility audit treated as insertion theorem",
            status="REJECTED",
            consequence="metric insertion is smuggled",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Residual-kill boundary/source compatibility problem")
    print("Question:")
    print()
    print("  Can residual kill / inertness preserve boundary and source guardrails?")
    print()
    print("Reference discipline:")
    print()
    print("  Residual cleanup cannot be a boundary/source repair route.")
    print("  It must preserve A-sector mass, scalar silence, current silence, no-shell, support/matching, and source no-double-counting.")
    print("  It cannot license B_s/F_zeta insertion by itself.")

    with out.governance_assessments():
        out.line(
            "residual-kill boundary/source compatibility audit opened",
            StatusMark.INFO,
            "auditing residual cleanup against Groups 21-24 guardrails",
        )


def case_1_compatibility_ledger(ledger: BoundarySourceCompatibilityLedger, out: ScriptOutput) -> None:
    header("Case 1: Residual cleanup compatibility failure-load ledger")
    print("Representative compatibility failure channels:")
    print()
    for name in [
        "A_mass_shift",
        "scalar_tail",
        "nonA_current_flux",
        "boundary_flux",
        "shell_source_load",
        "support_layer_load",
        "ordinary_source_dup",
        "recovery_selected_seam",
        "repair_object",
        "insertion_license",
    ]:
        print(f"  {name} = {sp.sstr(getattr(ledger, name))}")
    print()
    print("Compatibility failure load:")
    print()
    print(f"  L_cleanup_fail = {sp.sstr(ledger.compatibility_failure_load)}")
    print()
    print("Each channel must vanish or be theorem-routed before residual cleanup can be compatible.")

    with out.derived_results():
        out.line(
            "residual cleanup compatibility failure-load ledger stated",
            StatusMark.OBLIGATION,
            f"L_cleanup_fail = {sp.sstr(ledger.compatibility_failure_load)}",
        )


def case_2_conditions(conditions: List[BoundarySourceCondition], out: ScriptOutput) -> None:
    header("Case 2: Boundary/source compatibility conditions")
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
            "residual boundary/source compatibility conditions populated",
            StatusMark.OBLIGATION,
            f"{len(conditions)} compatibility conditions constrain residual cleanup",
        )


def case_3_branches(branches: List[BoundarySourceBranch], out: ScriptOutput) -> None:
    header("Case 3: Boundary/source compatibility branches")
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
            "residual boundary/source compatibility branches classified",
            StatusMark.PASS,
            f"{len(branches)} compatibility branches classified",
        )


def case_4_rejected_shortcuts(shortcuts: List[RejectedBoundarySourceShortcut], out: ScriptOutput) -> None:
    header("Case 4: Rejected boundary/source cleanup shortcuts")
    for shortcut in shortcuts:
        print()
        print("-" * 120)
        print(shortcut.name)
        print("-" * 120)
        print(f"Shortcut: {shortcut.shortcut}")
        print(f"Forbidden use: {shortcut.forbidden_use}")
        print(f"[{status_mark(shortcut.status).value}] {shortcut.name}: {shortcut.status}")
        print(f"Consequence: {shortcut.consequence}")

    with out.counterexamples():
        out.line(
            "residual boundary/source cleanup shortcuts rejected",
            StatusMark.FAIL,
            "mass shifts, tails, fluxes, shells, support loads, source duplication, repair objects, and insertion licensing remain rejected",
        )


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("The residual-kill boundary/source compatibility audit fails if a later script allows:")
    print()
    print("1. residual cleanup shifts A-sector mass")
    print("2. residual cleanup hides scalar tail")
    print("3. residual cleanup hides non-A current flux or boundary flux")
    print("4. residual cleanup hides shell/source load")
    print("5. residual cleanup hides in support/smoothing/transition/matching language")
    print("6. residual cleanup selected from source-compatibility failure")
    print("7. residual cleanup selected from recovery-selected seam data")
    print("8. O/H/dark/exchange/curvature/current repair object supplies compatibility")
    print("9. residual cleanup licenses B_s/F_zeta insertion")
    print("10. residual cleanup opens parent equation")

    with out.governance_assessments():
        out.line(
            "residual boundary/source compatibility failure controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not use residual cleanup as boundary/source repair or insertion license",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Residual-kill boundary/source compatibility result:")
    print()
    print("  Residual cleanup must preserve A-sector mass, scalar silence, current silence, boundary neutrality, no-shell matching, support/matching, and source no-double-counting.")
    print("  Residual cleanup cannot be selected from boundary/source failure.")
    print("  Residual cleanup cannot use O/H/dark/exchange/curvature/current repair labels.")
    print("  Residual cleanup cannot license B_s/F_zeta insertion or parent closure by itself.")
    print("  Compatibility remains theorem-targeted.")
    print()
    print("Possible next script:")
    print("  candidate_residual_kill_theorem_obligations.py")
    print()
    print("Tiny goblin label:")
    print("  Cleanup is not a repair shop.")

    with out.governance_assessments():
        out.line(
            "residual-kill boundary/source compatibility audit complete",
            StatusMark.PASS,
            "boundary/source repair routes rejected; residual-control theorem remains open",
        )


def record_derivations(ns, ledger: BoundarySourceCompatibilityLedger) -> None:
    ns.record_derivation(
        derivation_id="residual_kill_boundary_source_failure_load_25",
        inputs=[
            ledger.A_mass_shift,
            ledger.scalar_tail,
            ledger.nonA_current_flux,
            ledger.boundary_flux,
            ledger.shell_source_load,
            ledger.support_layer_load,
            ledger.ordinary_source_dup,
            ledger.recovery_selected_seam,
            ledger.repair_object,
            ledger.insertion_license,
        ],
        output=ledger.compatibility_failure_load,
        method="sum residual cleanup boundary/source compatibility failure channels",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="residual_boundary_source_compatibility_ledger",
        scope="Group 25 residual kill or no-overlap theorem",
    )

    ns.record_derivation(
        derivation_id="residual_kill_boundary_source_compatibility_marker_25",
        inputs=[
            sp.Symbol("no_A_mass_shift"),
            sp.Symbol("no_scalar_tail"),
            sp.Symbol("no_nonA_current_flux"),
            sp.Symbol("no_shell_source_load"),
            sp.Symbol("no_support_layer_load"),
            sp.Symbol("no_source_duplication"),
            sp.Symbol("no_repair_object"),
            sp.Symbol("no_insertion_license"),
        ],
        output=sp.Symbol("residual_kill_boundary_source_compatibility_stated"),
        method="Group 25 residual-kill boundary/source compatibility audit",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="requirements_marker",
        scope="Group 25 residual kill or no-overlap theorem",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g25_derive_cleanup_no_A_mass_shift", "Derive residual cleanup does not shift A-sector mass"),
        ("g25_derive_cleanup_no_scalar_tail", "Derive residual cleanup leaves no scalar tail"),
        ("g25_derive_cleanup_no_current_boundary_flux", "Derive residual cleanup leaves no current or boundary flux"),
        ("g25_derive_cleanup_no_shell_source_load", "Derive residual cleanup leaves no shell/source load"),
        ("g25_derive_cleanup_no_support_layer_load", "Derive residual cleanup leaves no support/layer load"),
        ("g25_derive_cleanup_no_source_duplication", "Derive residual cleanup duplicates no ordinary source load"),
        ("g25_derive_cleanup_no_recovery_selected_seam", "Derive residual cleanup is not selected from recovery seam data"),
        ("g25_derive_cleanup_no_repair_object", "Derive residual cleanup uses no repair object"),
        ("g25_keep_cleanup_from_insertion_parent_license", "Keep residual cleanup from licensing insertion or parent closure"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g25_residual_boundary_source_compatibility_route"],
            description=(
                "Residual cleanup remains theorem-targeted until boundary, source, support, mass, recovery, repair, and insertion-license channels are closed."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g25_derive_cleanup_no_A_mass_shift",
        "g25_derive_cleanup_no_scalar_tail",
        "g25_derive_cleanup_no_current_boundary_flux",
        "g25_derive_cleanup_no_shell_source_load",
        "g25_derive_cleanup_no_support_layer_load",
        "g25_derive_cleanup_no_source_duplication",
        "g25_derive_cleanup_no_recovery_selected_seam",
        "g25_derive_cleanup_no_repair_object",
        "g25_keep_cleanup_from_insertion_parent_license",
    ]

    ns.record_route(RouteRecord(
        route_id="g25_residual_boundary_source_compatibility_route",
        script_id=SCRIPT_ID,
        name="Group 25 residual cleanup boundary/source compatibility route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "residual cleanup shifts no A-sector mass",
            "residual cleanup leaves no scalar/current/boundary tail",
            "residual cleanup creates no shell/source/support/layer load",
            "residual cleanup duplicates no ordinary source",
            "residual cleanup is not recovery-selected",
            "residual cleanup uses no repair object",
            "residual cleanup does not license insertion or parent closure",
        ],
    ))

    for branch_id in [
        "cleanup_shifts_A_mass",
        "cleanup_hides_scalar_tail",
        "cleanup_hides_current_flux",
        "cleanup_hides_shell_source",
        "cleanup_hides_support_layer_load",
        "cleanup_selected_from_source_failure",
        "cleanup_repair_object",
        "cleanup_licenses_insertion_parent",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_25",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; residual cleanup cannot become boundary/source repair or insertion license.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g25_residual_cleanup_not_boundary_source_repair",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Residual kill, inertness, or no-overlap cannot be selected from boundary/source failure and cannot repair scalar tails, current fluxes, "
            "A-tail shifts, shell/source loads, support/layer loads, ordinary source duplication, or recovery-selected seams. "
            "Residual cleanup also cannot license B_s/F_zeta insertion or parent closure by itself."
        ),
        derivation_ids=[
            "residual_kill_boundary_source_failure_load_25",
            "residual_kill_boundary_source_compatibility_marker_25",
        ],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Residual Kill Boundary Source Compatibility")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    ledger = build_ledger()
    conditions = build_conditions()
    branches = build_branches()
    shortcuts = build_rejected_shortcuts()

    case_0_problem_statement(out)
    case_1_compatibility_ledger(ledger, out)
    case_2_conditions(conditions, out)
    case_3_branches(branches, out)
    case_4_rejected_shortcuts(shortcuts, out)
    case_5_failure_controls(out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, ledger)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
