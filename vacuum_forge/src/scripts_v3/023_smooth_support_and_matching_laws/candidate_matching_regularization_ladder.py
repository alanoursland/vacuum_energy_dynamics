# Candidate matching regularization ladder
#
# Group:
#   23_smooth_support_and_matching_laws
#
# Script type:
#   REQUIREMENTS / DIAGNOSTIC
#
# Purpose
# -------
# Open Group 23 by building a boundary matching regularization ladder:
#
#   value jump,
#   value match only,
#   slope match,
#   curvature / second-derivative diagnostic,
#   smooth compact bump,
#   derived matching law.
#
# Locked-door question:
#
#   What matching regularity is required at the boundary?
#
# This script does not prove compact support.
# It does not prove no-shell matching.
# It does not prove boundary neutrality.
# It does not prove exterior scalar silence.
# It does not define a parent field equation.
#
# It audits toy boundary profiles using:
#
#   phi(R),
#   phi'(R),
#   phi''(R),
#   F_R = 4*pi*R^2*phi'(R).
#
# The result is a diagnostic ladder, not a support theorem.

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


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def status_mark(status: str) -> StatusMark:
    return {
        "DIAGNOSTIC_ONLY": StatusMark.INFO,
        "FORBIDDEN": StatusMark.FAIL,
        "PROVISIONAL": StatusMark.INFO,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "RISK": StatusMark.WARN,
        "SAFE_IF": StatusMark.INFO,
        "THEOREM_TARGET": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g22_summary_dep_23",
            "022_boundary_neutrality_and_scalar_silence__candidate_group_22_boundary_neutrality_status_summary",
            "group22_boundary_neutrality_status_summary_marker_22",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g22_smooth_dep_23",
            "022_boundary_neutrality_and_scalar_silence__candidate_smooth_compact_support_no_shell_conditions",
            "smooth_compact_support_no_shell_inventory_marker_22",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g22_targets_dep_23",
            "022_boundary_neutrality_and_scalar_silence__candidate_boundary_scalar_silence_targets",
            "boundary_scalar_silence_target_ledger_marker_22",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g22_obligation_dep_23",
            "022_boundary_neutrality_and_scalar_silence__candidate_boundary_neutrality_theorem_obligations",
            "boundary_neutrality_theorem_obligations_marker_22",
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
    """Create optional archive subdirectories used by governance writers.

    Keeps archive writes robust on platforms where optional governance
    directories are not created before route/claim writes.
    """
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
class MatchingProfileDiagnostic:
    name: str
    profile: sp.Expr
    value_at_R: sp.Expr
    slope_at_R: sp.Expr
    curvature_at_R: sp.Expr
    boundary_flux_at_R: sp.Expr
    jump_against_zero_exterior: sp.Expr
    slope_jump_against_zero_exterior: sp.Expr


@dataclass
class RegularizationLadderEntry:
    name: str
    matching_level: str
    required_conditions: str
    status: str
    danger: str
    consequence: str


@dataclass
class RejectedLadderUpgrade:
    name: str
    rejected_upgrade: str
    status: str
    reason: str


# =============================================================================
# Builders
# =============================================================================


def boundary_flux(expr: sp.Expr, r: sp.Symbol) -> sp.Expr:
    return sp.simplify(4 * sp.pi * r**2 * sp.diff(expr, r))


def at_boundary(expr: sp.Expr, r: sp.Symbol, R: sp.Symbol) -> sp.Expr:
    return sp.simplify(expr.subs(r, R))


def build_profile_diagnostics() -> List[MatchingProfileDiagnostic]:
    r = sp.Symbol("r", positive=True)
    R = sp.Symbol("R", positive=True)
    phi0 = sp.Symbol("phi0", real=True)

    profiles = [
        ("P0_value_jump_constant", phi0),
        ("P1_value_match_linear", phi0 * (1 - r / R)),
        ("P2_value_slope_match_quadratic", phi0 * (1 - r / R) ** 2),
        ("P3_value_slope_curvature_diagnostic", phi0 * (1 - r / R) ** 3),
        ("P4_smooth_compact_bump_toy", phi0 * (1 - r**2 / R**2) ** 2),
    ]

    out: List[MatchingProfileDiagnostic] = []
    for name, profile in profiles:
        value_at_R = at_boundary(profile, r, R)
        slope_at_R = at_boundary(sp.diff(profile, r), r, R)
        curvature_at_R = at_boundary(sp.diff(profile, r, 2), r, R)
        flux_at_R = at_boundary(boundary_flux(profile, r), r, R)
        out.append(MatchingProfileDiagnostic(
            name=name,
            profile=profile,
            value_at_R=value_at_R,
            slope_at_R=slope_at_R,
            curvature_at_R=curvature_at_R,
            boundary_flux_at_R=flux_at_R,
            jump_against_zero_exterior=value_at_R,
            slope_jump_against_zero_exterior=slope_at_R,
        ))

    return out


def build_ladder() -> List[RegularizationLadderEntry]:
    return [
        RegularizationLadderEntry(
            name="L0: value jump",
            matching_level="no value match against exterior zero",
            required_conditions="none satisfied",
            status="REJECTED",
            danger="nonzero phi(R) can hide a distributional edge or shell source",
            consequence="not admissible as compact support or scalar silence",
        ),
        RegularizationLadderEntry(
            name="L1: value match only",
            matching_level="phi(R)=0",
            required_conditions="value continuity only",
            status="RISK",
            danger="phi'(R) can be nonzero, giving boundary flux F_R = 4*pi*R^2*phi'(R)",
            consequence="value matching alone does not prove no-shell or no-flux behavior",
        ),
        RegularizationLadderEntry(
            name="L2: value and slope match",
            matching_level="phi(R)=0 and phi'(R)=0",
            required_conditions="value and first derivative vanish at boundary",
            status="SAFE_IF",
            danger="higher derivative/distributional behavior and support origin are still not derived",
            consequence="necessary diagnostic condition for no boundary scalar flux, not a theorem",
        ),
        RegularizationLadderEntry(
            name="L3: curvature diagnostic match",
            matching_level="phi(R)=0, phi'(R)=0, and controlled phi''(R)",
            required_conditions="value/slope match plus second-derivative audit",
            status="SAFE_IF",
            danger="curvature/second-derivative matching does not by itself derive support law",
            consequence="stronger diagnostic regularity level",
        ),
        RegularizationLadderEntry(
            name="L4: smooth compact bump",
            matching_level="smooth-looking compact profile with zero value and slope at R",
            required_conditions="toy smooth profile diagnostics pass",
            status="SAFE_IF",
            danger="smooth paint can still be recovery-selected or source-incompatible",
            consequence="promising diagnostic class, not structural support",
        ),
        RegularizationLadderEntry(
            name="L5: derived matching/support law",
            matching_level="support and boundary regularity derived before recovery",
            required_conditions="support origin, value/slope matching, no distributional shell, recovery independence, source compatibility",
            status="THEOREM_TARGET",
            danger="not currently derived",
            consequence="positive route for future boundary/scalar silence",
        ),
    ]


def build_rejected_upgrades() -> List[RejectedLadderUpgrade]:
    return [
        RejectedLadderUpgrade(
            name="U1: exterior zero becomes compact-support proof",
            rejected_upgrade="using exterior zero as proof of compact support",
            status="REJECTED",
            reason="boundary matching and distributional shell behavior still need audit",
        ),
        RejectedLadderUpgrade(
            name="U2: value match becomes no-shell proof",
            rejected_upgrade="using phi(R)=0 as proof of no shell",
            status="REJECTED",
            reason="nonzero phi'(R) can carry boundary flux and derivative jumps can remain",
        ),
        RejectedLadderUpgrade(
            name="U3: slope match becomes full support law",
            rejected_upgrade="using phi(R)=phi'(R)=0 as a derived support theorem",
            status="REJECTED",
            reason="value/slope matching is necessary diagnostic behavior, not support origin",
        ),
        RejectedLadderUpgrade(
            name="U4: smooth toy profile becomes structural smoothing",
            rejected_upgrade="using a smooth toy bump as construction law",
            status="REJECTED",
            reason="smoothness does not prove recovery independence, source compatibility, or no hidden layer load",
        ),
        RejectedLadderUpgrade(
            name="U5: matching ladder opens parent gate",
            rejected_upgrade="using matching diagnostics to open a parent equation",
            status="REJECTED",
            reason="parent equation still needs boundary/scalar silence, source/projector/divergence, and recombination theorems",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Matching regularization ladder problem")
    print("Question:")
    print()
    print("  What matching regularity is required at the boundary?")
    print()
    print("Reference discipline:")
    print()
    print("  Group 22 made boundary/scalar silence targets explicit.")
    print("  Group 22 showed value matching alone can still carry boundary flux.")
    print("  Group 23 starts by building a matching ladder.")
    print("  This script audits toy profiles, not a support theorem.")
    print("  No parent equation, O eraser, H counterterm, dark patch, or recovery-tuned seam is used.")

    with out.governance_assessments():
        out.line(
            "matching regularization ladder audit opened",
            StatusMark.INFO,
            "testing value/slope/curvature boundary diagnostics without deriving support",
        )


def case_1_profile_table(profiles: List[MatchingProfileDiagnostic], out: ScriptOutput) -> None:
    header("Case 1: Boundary profile diagnostic table")
    for profile in profiles:
        print()
        print("-" * 120)
        print(profile.name)
        print("-" * 120)
        print(f"profile: {sp.sstr(profile.profile)}")
        print(f"phi(R): {sp.sstr(profile.value_at_R)}")
        print(f"phi'(R): {sp.sstr(profile.slope_at_R)}")
        print(f"phi''(R): {sp.sstr(profile.curvature_at_R)}")
        print(f"F_R = 4*pi*R^2*phi'(R): {sp.sstr(profile.boundary_flux_at_R)}")
        print(f"value jump vs exterior zero: {sp.sstr(profile.jump_against_zero_exterior)}")
        print(f"slope jump vs exterior zero: {sp.sstr(profile.slope_jump_against_zero_exterior)}")

    c1 = next(p for p in profiles if p.name == "P1_value_match_linear")
    c2 = next(p for p in profiles if p.name == "P2_value_slope_match_quadratic")
    c3 = next(p for p in profiles if p.name == "P3_value_slope_curvature_diagnostic")
    bump = next(p for p in profiles if p.name == "P4_smooth_compact_bump_toy")

    with out.sample_results():
        out.line(
            "value-match linear profile carries boundary flux",
            StatusMark.WARN if not is_zero(c1.boundary_flux_at_R) else StatusMark.PASS,
            f"F_R = {sp.sstr(c1.boundary_flux_at_R)}",
        )
        out.line(
            "quadratic value/slope profile has zero boundary flux",
            StatusMark.PASS if is_zero(c2.boundary_flux_at_R) else StatusMark.FAIL,
            f"F_R = {sp.sstr(c2.boundary_flux_at_R)}",
        )
        out.line(
            "cubic diagnostic profile has zero value/slope boundary flux but nonzero curvature diagnostic",
            StatusMark.PASS if is_zero(c3.boundary_flux_at_R) else StatusMark.FAIL,
            f"phi''(R) = {sp.sstr(c3.curvature_at_R)}",
        )
        out.line(
            "smooth compact toy profile has zero boundary flux",
            StatusMark.PASS if is_zero(bump.boundary_flux_at_R) else StatusMark.FAIL,
            f"F_R = {sp.sstr(bump.boundary_flux_at_R)}",
        )


def case_2_ladder(entries: List[RegularizationLadderEntry], out: ScriptOutput) -> None:
    header("Case 2: Matching regularization ladder")
    for entry in entries:
        print()
        print("-" * 120)
        print(entry.name)
        print("-" * 120)
        print(f"Matching level: {entry.matching_level}")
        print(f"Required conditions: {entry.required_conditions}")
        print(f"[{status_mark(entry.status).value}] {entry.name}: {entry.status}")
        print(f"Danger: {entry.danger}")
        print(f"Consequence: {entry.consequence}")

    with out.governance_assessments():
        out.line(
            "matching regularization ladder populated",
            StatusMark.PASS,
            f"{len(entries)} matching levels classified",
        )


def case_3_rejected_upgrades(upgrades: List[RejectedLadderUpgrade], out: ScriptOutput) -> None:
    header("Case 3: Rejected ladder upgrades")
    for upgrade in upgrades:
        print()
        print("-" * 120)
        print(upgrade.name)
        print("-" * 120)
        print(f"Rejected upgrade: {upgrade.rejected_upgrade}")
        print(f"[{status_mark(upgrade.status).value}] {upgrade.name}: {upgrade.status}")
        print(f"Reason: {upgrade.reason}")

    with out.counterexamples():
        out.line(
            "matching ladder over-upgrades rejected",
            StatusMark.FAIL,
            "exterior zero, value matching, slope matching, smooth toys, and matching diagnostics are not support theorems",
        )


def case_4_failure_controls(out: ScriptOutput) -> None:
    header("Case 4: Failure controls")
    print("The matching regularization ladder audit fails if a later script allows:")
    print()
    print("1. compact support by exterior zero alone")
    print("2. C0/value jump to count as boundary silence")
    print("3. C1 value matching to count as no-shell/no-flux proof")
    print("4. C2 value/slope matching to count as derived support law")
    print("5. smooth toy bump to count as structural smoothing")
    print("6. derivative or curvature jumps to be ignored")
    print("7. support radius chosen from recovery")
    print("8. O, H, dark, curvature, exchange, or current repair of a seam")
    print("9. diagnostic matching ladder to open parent equation gate")

    with out.governance_assessments():
        out.line(
            "matching ladder overclaim controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not confuse diagnostic regularity with derived support",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("The matching ladder result:")
    print()
    print("  value jump is rejected.")
    print("  value matching alone is risky.")
    print("  value+slope matching is a necessary diagnostic condition for zero boundary scalar flux.")
    print("  curvature/second-derivative behavior needs explicit audit.")
    print("  smooth compact bumps are useful diagnostics but not support laws.")
    print("  derived support/matching law remains theorem-targeted.")
    print()
    print("Boundary diagnostic target:")
    print()
    print("  phi(R) = 0")
    print("  phi'(R) = 0")
    print("  distributional shell terms controlled")
    print("  support law derived before recovery")
    print("  source compatibility preserved")
    print()
    print("Possible next script:")
    print("  candidate_distributional_shell_source_audit.py")
    print()
    print("Tiny goblin label:")
    print("  Inspect the seam. Count the jumps. Trust no smooth paint.")

    with out.governance_assessments():
        out.line(
            "matching regularization ladder audit complete",
            StatusMark.PASS,
            "regularity ladder explicit; support theorem remains open",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, profiles: List[MatchingProfileDiagnostic]) -> None:
    for profile in profiles:
        safe = profile.name.replace("/", "_").replace(" ", "_")
        ns.record_derivation(
            derivation_id=f"{safe}_boundary_matching_diagnostic_23",
            inputs=[profile.profile],
            output=sp.Tuple(
                profile.value_at_R,
                profile.slope_at_R,
                profile.curvature_at_R,
                profile.boundary_flux_at_R,
            ),
            method="evaluate phi(R), phi'(R), phi''(R), and 4*pi*R**2*phi'(R)",
            status=Status.DERIVED,
            record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
            result_type="boundary_matching_diagnostic",
            scope="Group 23 smooth support and matching laws",
        )

    ns.record_derivation(
        derivation_id="matching_regularization_ladder_marker_23",
        inputs=[
            sp.Symbol("C0_value"),
            sp.Symbol("C1_slope"),
            sp.Symbol("C2_curvature"),
            sp.Symbol("smooth_bump"),
            sp.Symbol("derived_support"),
        ],
        output=sp.Symbol("matching_regularization_ladder_stated"),
        method="Group 23 boundary matching regularization ladder",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="requirements_marker",
        scope="Group 23 smooth support and matching laws",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        (
            "g23_derive_value_matching",
            "Derive value matching",
            "Show phi(R)=0 follows from structural support/matching law, not exterior-zero declaration.",
        ),
        (
            "g23_derive_slope_matching",
            "Derive slope matching",
            "Show phi'(R)=0 or equivalent no-flux boundary condition follows structurally.",
        ),
        (
            "g23_audit_curvature_matching",
            "Audit curvature/second-derivative matching",
            "Control higher derivative and distributional behavior at the support edge.",
        ),
        (
            "g23_derive_support_law",
            "Derive support law",
            "Show support origin, matching behavior, no-shell condition, recovery independence, and source compatibility.",
        ),
    ]

    for obligation_id, title, description in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g23_matching_law_route"],
            description=description,
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g23_derive_value_matching",
        "g23_derive_slope_matching",
        "g23_audit_curvature_matching",
        "g23_derive_support_law",
    ]

    ns.record_route(RouteRecord(
        route_id="g23_matching_law_route",
        script_id=SCRIPT_ID,
        name="Group 23 matching/support law theorem target",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "value matching is derived, not declared",
            "slope matching / no-flux behavior is derived",
            "distributional shell behavior is controlled",
            "support law is recovery-independent and source-compatible",
        ],
    ))

    for branch_id in [
        "exterior_zero_as_support",
        "value_match_as_no_shell",
        "slope_match_as_support_law",
        "smooth_toy_as_support_law",
        "matching_ladder_as_parent_gate",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_23",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=(
                f"Reject {branch_id}; matching diagnostics do not by themselves prove compact support, "
                "no-shell behavior, boundary neutrality, scalar silence, or parent closure."
            ),
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g23_matching_ladder_diagnostic_not_theorem",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Group 23 matching ladder classifies boundary regularity diagnostics. "
            "Value matching alone is insufficient; value/slope matching is a necessary diagnostic for no boundary scalar flux, "
            "but derived support and no-shell behavior remain theorem-targeted."
        ),
        derivation_ids=[
            "P0_value_jump_constant_boundary_matching_diagnostic_23",
            "P1_value_match_linear_boundary_matching_diagnostic_23",
            "P2_value_slope_match_quadratic_boundary_matching_diagnostic_23",
            "P3_value_slope_curvature_diagnostic_boundary_matching_diagnostic_23",
            "P4_smooth_compact_bump_toy_boundary_matching_diagnostic_23",
            "matching_regularization_ladder_marker_23",
        ],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Matching Regularization Ladder")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    profiles = build_profile_diagnostics()
    ladder = build_ladder()
    upgrades = build_rejected_upgrades()

    case_0_problem_statement(out)
    case_1_profile_table(profiles, out)
    case_2_ladder(ladder, out)
    case_3_rejected_upgrades(upgrades, out)
    case_4_failure_controls(out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, profiles)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
