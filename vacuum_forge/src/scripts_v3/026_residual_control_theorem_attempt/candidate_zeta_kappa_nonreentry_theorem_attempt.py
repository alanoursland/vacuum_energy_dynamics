# Candidate zeta kappa nonreentry theorem attempt
#
# Group:
#   26_residual_control_theorem_attempt
#
# Script type:
#   THEOREM ATTEMPT
#
# Purpose
# -------
# Test whether the geometric residuals can be blocked from reentry
# sector-by-sector.
#
# Locked-door question:
#
#   Can zeta and kappa residuals be blocked from reentry sector-by-sector?
#
# This script does not derive B_s/F_zeta insertion.
# It does not derive active no-overlap O.
# It does not derive parent equation closure.
#
# It focuses on:
#
#   zeta_residual_metric
#   kappa_metric
#
# because the prior direct-kill and strict-inertness attempts left these as
# the dangerous geometric trace residuals.
#
# Tiny goblin rule:
#
#   No ghost through another crack.

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
        "CONDITIONALLY_REDUCED": StatusMark.INFO,
        "DIAGNOSTIC_ONLY": StatusMark.INFO,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "PARTIAL_REDUCTION": StatusMark.INFO,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "SAFE_IF": StatusMark.INFO,
        "THEOREM_ATTEMPT": StatusMark.DEFER,
        "THEOREM_TARGET": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "problem_ledger_dep_26",
            "026_residual_control_theorem_attempt__candidate_residual_control_theorem_problem_ledger",
            "residual_control_theorem_problem_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "structural_kill_dep_26",
            "026_residual_control_theorem_attempt__candidate_structural_residual_kill_law_attempt",
            "structural_residual_kill_law_attempt_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "inertness_attempt_dep_26",
            "026_residual_control_theorem_attempt__candidate_nonmetric_inertness_theorem_attempt",
            "nonmetric_inertness_theorem_attempt_marker_26",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g25_reentry_dep_26",
            "025_residual_kill_or_no_overlap_theorem__candidate_residual_reentry_exclusion_audit",
            "residual_reentry_exclusion_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g24_count_once_dep_26",
            "024_metric_insertion_recovery_retest__candidate_count_once_metric_trace_audit",
            "count_once_metric_trace_marker_24",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g24_boundary_source_dep_26",
            "024_metric_insertion_recovery_retest__candidate_metric_insertion_boundary_support_compatibility",
            "metric_insertion_boundary_support_marker_24",
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
class GeometricReentryLedger:
    zeta_metric_reentry: sp.Symbol
    zeta_source_reentry: sp.Symbol
    zeta_boundary_reentry: sp.Symbol
    zeta_support_reentry: sp.Symbol
    zeta_recovery_reentry: sp.Symbol
    zeta_repair_reentry: sp.Symbol
    zeta_parent_reentry: sp.Symbol
    kappa_metric_reentry: sp.Symbol
    kappa_source_reentry: sp.Symbol
    kappa_boundary_reentry: sp.Symbol
    kappa_support_reentry: sp.Symbol
    kappa_recovery_reentry: sp.Symbol
    kappa_repair_reentry: sp.Symbol
    kappa_parent_reentry: sp.Symbol
    zeta_reentry_load: sp.Expr
    kappa_reentry_load: sp.Expr
    geometric_reentry_load: sp.Expr


@dataclass
class GeometricResidualAttempt:
    name: str
    residual: str
    target: str
    status: str
    result: str
    missing_theorem: str


@dataclass
class ReentryChannelAttempt:
    name: str
    channel: str
    zeta_status: str
    kappa_status: str
    zeta_result: str
    kappa_result: str


@dataclass
class RejectedGeometricShortcut:
    name: str
    shortcut: str
    forbidden_use: str
    status: str
    consequence: str


@dataclass
class GeometricNonreentryConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


# =============================================================================
# Builders
# =============================================================================


def build_ledger() -> GeometricReentryLedger:
    (
        zeta_metric_reentry,
        zeta_source_reentry,
        zeta_boundary_reentry,
        zeta_support_reentry,
        zeta_recovery_reentry,
        zeta_repair_reentry,
        zeta_parent_reentry,
        kappa_metric_reentry,
        kappa_source_reentry,
        kappa_boundary_reentry,
        kappa_support_reentry,
        kappa_recovery_reentry,
        kappa_repair_reentry,
        kappa_parent_reentry,
    ) = sp.symbols(
        "zeta_metric_reentry zeta_source_reentry zeta_boundary_reentry zeta_support_reentry zeta_recovery_reentry zeta_repair_reentry zeta_parent_reentry "
        "kappa_metric_reentry kappa_source_reentry kappa_boundary_reentry kappa_support_reentry kappa_recovery_reentry kappa_repair_reentry kappa_parent_reentry",
        real=True,
    )

    zeta_reentry_load = sp.simplify(
        zeta_metric_reentry
        + zeta_source_reentry
        + zeta_boundary_reentry
        + zeta_support_reentry
        + zeta_recovery_reentry
        + zeta_repair_reentry
        + zeta_parent_reentry
    )

    kappa_reentry_load = sp.simplify(
        kappa_metric_reentry
        + kappa_source_reentry
        + kappa_boundary_reentry
        + kappa_support_reentry
        + kappa_recovery_reentry
        + kappa_repair_reentry
        + kappa_parent_reentry
    )

    geometric_reentry_load = sp.simplify(zeta_reentry_load + kappa_reentry_load)

    return GeometricReentryLedger(
        zeta_metric_reentry=zeta_metric_reentry,
        zeta_source_reentry=zeta_source_reentry,
        zeta_boundary_reentry=zeta_boundary_reentry,
        zeta_support_reentry=zeta_support_reentry,
        zeta_recovery_reentry=zeta_recovery_reentry,
        zeta_repair_reentry=zeta_repair_reentry,
        zeta_parent_reentry=zeta_parent_reentry,
        kappa_metric_reentry=kappa_metric_reentry,
        kappa_source_reentry=kappa_source_reentry,
        kappa_boundary_reentry=kappa_boundary_reentry,
        kappa_support_reentry=kappa_support_reentry,
        kappa_recovery_reentry=kappa_recovery_reentry,
        kappa_repair_reentry=kappa_repair_reentry,
        kappa_parent_reentry=kappa_parent_reentry,
        zeta_reentry_load=zeta_reentry_load,
        kappa_reentry_load=kappa_reentry_load,
        geometric_reentry_load=geometric_reentry_load,
    )


def build_residual_attempts() -> List[GeometricResidualAttempt]:
    return [
        GeometricResidualAttempt(
            name="G1: zeta residual non-reentry",
            residual="zeta_residual_metric",
            target="zeta residual cannot re-enter after zeta_to_Bs insertion",
            status="NOT_DERIVED",
            result="count-once requires this, but no current theorem proves every zeta residual reentry channel vanishes",
            missing_theorem="B_s/F_zeta insertion law, coefficient origin, zeta residual non-reentry, or active O",
        ),
        GeometricResidualAttempt(
            name="G2: kappa residual non-reentry",
            residual="kappa_metric",
            target="kappa cannot restore killed zeta trace or source role",
            status="NOT_DERIVED",
            result="diagnostic-only / areal-kappa guardrails constrain kappa use, but do not prove every kappa reentry channel vanishes",
            missing_theorem="kappa nonmetric theorem, kappa non-reentry theorem, or active O",
        ),
        GeometricResidualAttempt(
            name="G3: zeta-kappa coupled reentry",
            residual="zeta_residual_metric + kappa_metric",
            target="zeta and kappa residuals cannot trade roles or cancel unsafe channels",
            status="NOT_DERIVED",
            result="no theorem currently prevents zeta/kappa role trade except guardrails; total cancellation is not allowed",
            missing_theorem="sector-by-sector coupled non-reentry or active O",
        ),
    ]


def build_channel_attempts() -> List[ReentryChannelAttempt]:
    return [
        ReentryChannelAttempt(
            name="C1: metric trace channel",
            channel="metric",
            zeta_status="NOT_DERIVED",
            kappa_status="NOT_DERIVED",
            zeta_result="zeta_to_Bs is allowed target, but zeta_residual_metric absence is not derived",
            kappa_result="kappa_metric absence is not derived; diagnostic-only is not enough",
        ),
        ReentryChannelAttempt(
            name="C2: source channel",
            channel="source",
            zeta_status="CONDITIONALLY_REDUCED",
            kappa_status="CONDITIONALLY_REDUCED",
            zeta_result="source duplication is rejected, but zeta no-source theorem is not derived",
            kappa_result="source role is rejected, but kappa no-source theorem is not derived",
        ),
        ReentryChannelAttempt(
            name="C3: boundary / scalar-tail channel",
            channel="boundary_scalar",
            zeta_status="NOT_DERIVED",
            kappa_status="NOT_DERIVED",
            zeta_result="scalar-tail silence is required, but zeta residual boundary neutrality is not derived",
            kappa_result="kappa boundary/scalar neutrality is not derived",
        ),
        ReentryChannelAttempt(
            name="C4: current flux channel",
            channel="current_flux",
            zeta_status="NOT_DERIVED",
            kappa_status="NOT_DERIVED",
            zeta_result="non-A current flux is forbidden, but zeta current silence is not derived",
            kappa_result="kappa current silence is not derived",
        ),
        ReentryChannelAttempt(
            name="C5: A-tail mass channel",
            channel="A_tail_mass",
            zeta_status="CONDITIONALLY_REDUCED",
            kappa_status="CONDITIONALLY_REDUCED",
            zeta_result="A-sector mass protection exists, but zeta no-mass-shift theorem is not derived",
            kappa_result="A-sector mass protection exists, but kappa no-mass-shift theorem is not derived",
        ),
        ReentryChannelAttempt(
            name="C6: shell / support / layer channel",
            channel="support_matching",
            zeta_status="NOT_DERIVED",
            kappa_status="NOT_DERIVED",
            zeta_result="support/matching guardrails exist, but zeta support-neutrality theorem is not derived",
            kappa_result="support/matching guardrails exist, but kappa support-neutrality theorem is not derived",
        ),
        ReentryChannelAttempt(
            name="C7: recovery coefficient channel",
            channel="recovery",
            zeta_status="CONDITIONALLY_REDUCED",
            kappa_status="CONDITIONALLY_REDUCED",
            zeta_result="recovery-selected zeta residual status is rejected, but structural status is not derived",
            kappa_result="recovery-selected kappa status is rejected, but structural status is not derived",
        ),
        ReentryChannelAttempt(
            name="C8: repair-label channel",
            channel="repair",
            zeta_status="CONDITIONALLY_REDUCED",
            kappa_status="CONDITIONALLY_REDUCED",
            zeta_result="O/H/dark/exchange/curvature/current repair routes are rejected, but theorem is not derived",
            kappa_result="O/H/dark/exchange/curvature/current repair routes are rejected, but theorem is not derived",
        ),
        ReentryChannelAttempt(
            name="C9: parent-placeholder channel",
            channel="parent",
            zeta_status="CONDITIONALLY_REDUCED",
            kappa_status="CONDITIONALLY_REDUCED",
            zeta_result="parent closure is blocked, but zeta non-parent role theorem is not derived",
            kappa_result="parent closure is blocked, but kappa non-parent role theorem is not derived",
        ),
    ]


def build_rejected_shortcuts() -> List[RejectedGeometricShortcut]:
    return [
        RejectedGeometricShortcut(
            name="S1: zeta residual reentry hidden in B_s",
            shortcut="zeta enters B_s and also residual metric trace",
            forbidden_use="double-counting zeta scalar spatial response",
            status="REJECTED",
            consequence="count-once recombination fails",
        ),
        RejectedGeometricShortcut(
            name="S2: kappa restores zeta trace",
            shortcut="kappa_metric replaces or restores killed zeta_residual_metric",
            forbidden_use="kappa reintroduces residual trace",
            status="REJECTED",
            consequence="residual kill/inertness is bypassed",
        ),
        RejectedGeometricShortcut(
            name="S3: zeta/kappa total cancellation",
            shortcut="zeta and kappa reentry channels cancel only in total",
            forbidden_use="total cancellation substitutes for sector-by-sector non-reentry",
            status="REJECTED",
            consequence="unsafe geometric residual path remains",
        ),
        RejectedGeometricShortcut(
            name="S4: recovery-selected zeta/kappa silence",
            shortcut="choose zeta/kappa residual status from Schwarzschild/gamma/AB/B=1/A/PPN",
            forbidden_use="recovery selects geometric residual status",
            status="REJECTED",
            consequence="recovery constructs residual control",
        ),
        RejectedGeometricShortcut(
            name="S5: boundary/source-selected zeta/kappa silence",
            shortcut="choose zeta/kappa residual status to repair tail, flux, shell, source, or support failure",
            forbidden_use="repair need selects geometric residual status",
            status="REJECTED",
            consequence="boundary/source cleanup becomes theorem",
        ),
        RejectedGeometricShortcut(
            name="S6: hidden O zeta/kappa separator",
            shortcut="use a projection-like split to separate zeta/kappa without O burden",
            forbidden_use="active no-overlap operator is smuggled",
            status="REJECTED",
            consequence="O eraser by another name",
        ),
        RejectedGeometricShortcut(
            name="S7: non-reentry licenses insertion",
            shortcut="zeta/kappa non-reentry attempt licenses B_s/F_zeta insertion",
            forbidden_use="non-reentry replaces insertion law or coefficient origin",
            status="REJECTED",
            consequence="metric insertion is smuggled",
        ),
        RejectedGeometricShortcut(
            name="S8: non-reentry opens parent",
            shortcut="zeta/kappa non-reentry attempt opens parent equation",
            forbidden_use="non-reentry replaces parent identity and divergence closure",
            status="REJECTED",
            consequence="parent equation is smuggled",
        ),
    ]


def build_conclusions() -> List[GeometricNonreentryConclusion]:
    return [
        GeometricNonreentryConclusion(
            name="C1: zeta residual non-reentry",
            conclusion="not derived sector-by-sector",
            status="NOT_DERIVED",
            meaning="zeta residual remains blocked by missing insertion law, coefficient origin, non-reentry theorem, or active O",
        ),
        GeometricNonreentryConclusion(
            name="C2: kappa residual non-reentry",
            conclusion="not derived sector-by-sector",
            status="NOT_DERIVED",
            meaning="kappa remains diagnostic-constrained but not proven unable to restore trace or source role",
        ),
        GeometricNonreentryConclusion(
            name="C3: accounting residual separation",
            conclusion="zeta/kappa geometric residuals are sharper obstruction than epsilon/e_kappa accounting residuals",
            status="CONDITIONALLY_REDUCED",
            meaning="the next obstruction is geometric non-reentry, not accounting bookkeeping",
        ),
        GeometricNonreentryConclusion(
            name="C4: next route",
            conclusion="test epsilon/e_kappa accounting inertness separately, then check whether non-O residual control closes",
            status="SAFE_IF",
            meaning="geometric non-reentry remains open; accounting entries may be easier to isolate",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Zeta/kappa non-reentry theorem attempt problem")
    print("Question:")
    print()
    print("  Can zeta and kappa residuals be blocked from reentry sector-by-sector?")
    print()
    print("Reference discipline:")
    print()
    print("  zeta may enter B_s only once.")
    print("  kappa cannot restore killed zeta trace.")
    print("  Non-reentry must be sector-by-sector, not total cancellation.")
    print("  Recovery, repair routes, insertion licensing, and parent closure do not count.")

    with out.governance_assessments():
        out.line(
            "zeta/kappa non-reentry theorem attempt opened",
            StatusMark.INFO,
            "testing dangerous geometric residuals after direct kill and full inertness were not derived",
        )


def case_1_reentry_ledger(ledger: GeometricReentryLedger, out: ScriptOutput) -> None:
    header("Case 1: Geometric residual reentry ledger")
    print("Zeta reentry load:")
    print()
    print(f"  L_zeta_reentry = {sp.sstr(ledger.zeta_reentry_load)}")
    print()
    print("Kappa reentry load:")
    print()
    print(f"  L_kappa_reentry = {sp.sstr(ledger.kappa_reentry_load)}")
    print()
    print("Total geometric reentry load:")
    print()
    print(f"  L_geometric_reentry = {sp.sstr(ledger.geometric_reentry_load)}")
    print()
    print("Interpretation:")
    print()
    print("  Geometric non-reentry requires zeta and kappa loads to vanish sector-by-sector.")
    print("  A total zeta/kappa cancellation is not a theorem.")

    with out.derived_results():
        out.line(
            "zeta residual reentry load stated",
            StatusMark.OBLIGATION,
            f"L_zeta_reentry = {sp.sstr(ledger.zeta_reentry_load)}",
        )
        out.line(
            "kappa residual reentry load stated",
            StatusMark.OBLIGATION,
            f"L_kappa_reentry = {sp.sstr(ledger.kappa_reentry_load)}",
        )
        out.line(
            "geometric residual reentry load stated",
            StatusMark.OBLIGATION,
            f"L_geometric_reentry = {sp.sstr(ledger.geometric_reentry_load)}",
        )


def case_2_residual_attempts(attempts: List[GeometricResidualAttempt], out: ScriptOutput) -> None:
    header("Case 2: Geometric residual non-reentry attempts")
    for attempt in attempts:
        print()
        print("-" * 120)
        print(attempt.name)
        print("-" * 120)
        print(f"Residual: {attempt.residual}")
        print(f"Target: {attempt.target}")
        print(f"[{status_mark(attempt.status).value}] {attempt.name}: {attempt.status}")
        print(f"Result: {attempt.result}")
        print(f"Missing theorem: {attempt.missing_theorem}")

    with out.unresolved_obligations():
        out.line(
            "geometric residual non-reentry attempts classified",
            StatusMark.OBLIGATION,
            f"{len(attempts)} geometric residual attempts tested; non-reentry not derived",
        )


def case_3_channel_attempts(attempts: List[ReentryChannelAttempt], out: ScriptOutput) -> None:
    header("Case 3: Zeta/kappa reentry channel tests")
    for attempt in attempts:
        print()
        print("-" * 120)
        print(attempt.name)
        print("-" * 120)
        print(f"Channel: {attempt.channel}")
        print(f"[{status_mark(attempt.zeta_status).value}] zeta: {attempt.zeta_status}")
        print(f"  zeta result: {attempt.zeta_result}")
        print(f"[{status_mark(attempt.kappa_status).value}] kappa: {attempt.kappa_status}")
        print(f"  kappa result: {attempt.kappa_result}")

    with out.governance_assessments():
        out.line(
            "zeta/kappa reentry channels tested",
            StatusMark.PASS,
            f"{len(attempts)} channels evaluated; geometric non-reentry remains open",
        )


def case_4_rejected_shortcuts(shortcuts: List[RejectedGeometricShortcut], out: ScriptOutput) -> None:
    header("Case 4: Rejected zeta/kappa non-reentry shortcuts")
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
            "zeta/kappa non-reentry shortcuts rejected",
            StatusMark.FAIL,
            "double zeta entry, kappa trace restoration, total cancellation, recovery/repair selection, hidden O, insertion, and parent shortcuts are rejected",
        )


def case_5_conclusions(conclusions: List[GeometricNonreentryConclusion], out: ScriptOutput) -> None:
    header("Case 5: Zeta/kappa non-reentry conclusions")
    for conclusion in conclusions:
        print()
        print("-" * 120)
        print(conclusion.name)
        print("-" * 120)
        print(f"Conclusion: {conclusion.conclusion}")
        print(f"[{status_mark(conclusion.status).value}] {conclusion.name}: {conclusion.status}")
        print(f"Meaning: {conclusion.meaning}")

    with out.governance_assessments():
        out.line(
            "zeta/kappa non-reentry theorem-attempt conclusion stated",
            StatusMark.DEFER,
            "geometric non-reentry not derived; accounting inertness and non-O obstruction remain next checks",
        )


def case_6_failure_controls(out: ScriptOutput) -> None:
    header("Case 6: Failure controls")
    print("The zeta/kappa non-reentry theorem attempt fails if a later script allows:")
    print()
    print("1. zeta enters B_s and residual metric trace")
    print("2. kappa restores killed zeta trace")
    print("3. zeta/kappa source reentry")
    print("4. zeta/kappa boundary/scalar/current reentry")
    print("5. zeta/kappa A-tail mass shift")
    print("6. zeta/kappa support/layer reentry")
    print("7. zeta/kappa recovery-selected status")
    print("8. zeta/kappa repair-label separation")
    print("9. total zeta/kappa cancellation treated as non-reentry")
    print("10. zeta/kappa non-reentry licenses insertion or parent closure")

    with out.governance_assessments():
        out.line(
            "zeta/kappa non-reentry failure controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not convert guardrails into geometric non-reentry theorem",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Zeta/kappa non-reentry theorem attempt result:")
    print()
    print("  Zeta residual non-reentry is not derived sector-by-sector.")
    print("  Kappa residual non-reentry is not derived sector-by-sector.")
    print("  Zeta/kappa total cancellation is rejected.")
    print("  The dangerous geometric residuals remain blocked by missing insertion law, coefficient origin, sector-by-sector non-reentry, or active O.")
    print("  epsilon/e_kappa accounting residuals should be tested separately.")
    print("  B_s/F_zeta insertion and parent closure remain not ready.")
    print()
    print("Possible next script:")
    print("  candidate_epsilon_ekappa_inertness_theorem_attempt.py")
    print()
    print("Tiny goblin label:")
    print("  No ghost through another crack.")

    with out.governance_assessments():
        out.line(
            "zeta/kappa non-reentry theorem attempt complete",
            StatusMark.PASS,
            "geometric non-reentry not derived; accounting inertness route remains next",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, ledger: GeometricReentryLedger) -> None:
    ns.record_derivation(
        derivation_id="zeta_kappa_geometric_reentry_load_26",
        inputs=[
            ledger.zeta_reentry_load,
            ledger.kappa_reentry_load,
        ],
        output=ledger.geometric_reentry_load,
        method="sum zeta and kappa residual reentry channels for sector-by-sector theorem attempt",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="zeta_kappa_nonreentry_attempt_ledger",
        scope="Group 26 residual control theorem attempt",
    )

    ns.record_derivation(
        derivation_id="zeta_kappa_nonreentry_theorem_attempt_marker_26",
        inputs=[
            sp.Symbol("zeta_residual_metric"),
            sp.Symbol("kappa_metric"),
            sp.Symbol("metric_source_boundary_support_recovery_repair_parent_channels"),
        ],
        output=sp.Symbol("zeta_kappa_nonreentry_theorem_not_derived"),
        method="Group 26 zeta/kappa non-reentry theorem attempt",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="theorem_attempt_marker",
        scope="Group 26 residual control theorem attempt",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g26_zeta_no_metric_reentry", "Derive zeta no metric reentry after B_s insertion"),
        ("g26_kappa_no_metric_reentry", "Derive kappa no metric trace restoration"),
        ("g26_zeta_kappa_no_source_reentry", "Derive zeta/kappa no source reentry"),
        ("g26_zeta_kappa_no_boundary_current_reentry", "Derive zeta/kappa no boundary/scalar/current reentry"),
        ("g26_zeta_kappa_no_mass_support_reentry", "Derive zeta/kappa no mass/support reentry"),
        ("g26_zeta_kappa_no_recovery_repair_parent_reentry", "Derive zeta/kappa no recovery/repair/parent reentry"),
        ("g26_reject_zeta_kappa_total_cancellation", "Reject zeta/kappa total cancellation as non-reentry"),
        ("g26_keep_insertion_parent_closed_after_zeta_kappa_attempt", "Keep insertion and parent gates closed after zeta/kappa attempt"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g26_zeta_kappa_nonreentry_theorem_attempt_route"],
            description=(
                "Zeta/kappa geometric residual non-reentry is not derived here. Future work must close each reentry channel sector-by-sector."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g26_zeta_no_metric_reentry",
        "g26_kappa_no_metric_reentry",
        "g26_zeta_kappa_no_source_reentry",
        "g26_zeta_kappa_no_boundary_current_reentry",
        "g26_zeta_kappa_no_mass_support_reentry",
        "g26_zeta_kappa_no_recovery_repair_parent_reentry",
        "g26_reject_zeta_kappa_total_cancellation",
        "g26_keep_insertion_parent_closed_after_zeta_kappa_attempt",
    ]

    ns.record_route(RouteRecord(
        route_id="g26_zeta_kappa_nonreentry_theorem_attempt_route",
        script_id=SCRIPT_ID,
        name="Group 26 zeta/kappa geometric residual non-reentry theorem attempt",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "zeta residual cannot re-enter after zeta_to_Bs insertion",
            "kappa cannot restore killed trace",
            "zeta/kappa source, boundary, support, recovery, repair, and parent reentry channels are closed",
            "total cancellation is not used",
            "insertion and parent gates remain closed",
        ],
    ))

    for branch_id in [
        "zeta_double_entry_Bs_and_residual_trace",
        "kappa_restores_zeta_trace",
        "zeta_kappa_source_reentry",
        "zeta_kappa_boundary_current_reentry",
        "zeta_kappa_mass_support_reentry",
        "zeta_kappa_recovery_selected_status",
        "zeta_kappa_repair_label_separation",
        "zeta_kappa_total_cancellation",
        "zeta_kappa_nonreentry_licenses_insertion",
        "zeta_kappa_nonreentry_opens_parent",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_26",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; zeta/kappa non-reentry requires sector-by-sector theorem.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g26_zeta_kappa_nonreentry_not_derived",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Zeta residual non-reentry and kappa residual non-reentry are not derived sector-by-sector. "
            "The dangerous geometric residuals remain blocked by missing insertion law, coefficient origin, sector-by-sector non-reentry, or active O. "
            "Zeta/kappa total cancellation is rejected, and B_s/F_zeta insertion and parent closure remain not ready."
        ),
        derivation_ids=[
            "zeta_kappa_geometric_reentry_load_26",
            "zeta_kappa_nonreentry_theorem_attempt_marker_26",
        ],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Zeta Kappa Nonreentry Theorem Attempt")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    ledger = build_ledger()
    attempts = build_residual_attempts()
    channels = build_channel_attempts()
    shortcuts = build_rejected_shortcuts()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_reentry_ledger(ledger, out)
    case_2_residual_attempts(attempts, out)
    case_3_channel_attempts(channels, out)
    case_4_rejected_shortcuts(shortcuts, out)
    case_5_conclusions(conclusions, out)
    case_6_failure_controls(out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, ledger)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
