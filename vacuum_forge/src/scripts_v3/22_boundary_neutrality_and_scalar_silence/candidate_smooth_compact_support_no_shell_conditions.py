# Candidate smooth compact support no-shell conditions
#
# Group:
#   22_boundary_neutrality_and_scalar_silence
#
# Script type:
#   REQUIREMENTS / DIAGNOSTIC
#
# Purpose
# -------
# Test when compact support or boundary matching avoids hiding a shell source.
#
# Locked-door question:
#
#   When does compact support avoid hiding a shell source?
#
# This script does not derive compact support.
# It does not prove boundary neutrality.
# It does not prove scalar silence.
# It does not license recovery-tuned smoothing.
#
# It only audits toy boundary profiles for value matching, derivative matching,
# boundary flux, and derivative-jump / shell danger.

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
        "DIAGNOSTIC": StatusMark.INFO,
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
            "boundary_scalar_silence_target_ledger_dependency_22",
            "22_boundary_neutrality_and_scalar_silence__candidate_boundary_scalar_silence_targets",
            "boundary_scalar_silence_target_ledger_marker_22",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "scalar_tail_flux_witness_dependency_22",
            "22_boundary_neutrality_and_scalar_silence__candidate_boundary_scalar_silence_targets",
            "boundary_scalar_silence_scalar_tail_flux_witness_22",
            RecordKind.DERIVATION,
        ),
        (
            "boundary_A_tail_mass_witness_dependency_22",
            "22_boundary_neutrality_and_scalar_silence__candidate_boundary_scalar_silence_targets",
            "boundary_scalar_silence_boundary_A_tail_mass_witness_22",
            RecordKind.DERIVATION,
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
class BoundaryProfileSet:
    r: sp.Symbol
    R: sp.Symbol
    phi0: sp.Symbol
    c0_profile: sp.Expr
    c1_profile: sp.Expr
    c2_profile: sp.Expr
    compact_profile: sp.Expr
    sharp_inside: sp.Expr
    c0_value_at_R: sp.Expr
    c0_slope_at_R: sp.Expr
    c0_flux_at_R: sp.Expr
    c1_value_at_R: sp.Expr
    c1_slope_at_R: sp.Expr
    c1_flux_at_R: sp.Expr
    c2_value_at_R: sp.Expr
    c2_slope_at_R: sp.Expr
    c2_flux_at_R: sp.Expr
    compact_value_at_R: sp.Expr
    compact_slope_at_R: sp.Expr
    compact_flux_at_R: sp.Expr
    sharp_jump_value: sp.Expr
    sharp_slope_inside_at_R: sp.Expr
    sharp_flux_inside_at_R: sp.Expr


@dataclass
class BoundaryBranchEntry:
    name: str
    branch: str
    condition: str
    status: str
    danger: str
    consequence: str


@dataclass
class RejectedSupportRoute:
    name: str
    route: str
    forbidden_use: str
    status: str
    consequence: str


# =============================================================================
# Builders
# =============================================================================


def boundary_flux(expr: sp.Expr, r: sp.Symbol) -> sp.Expr:
    return sp.simplify(4 * sp.pi * r**2 * sp.diff(expr, r))


def at_boundary(expr: sp.Expr, r: sp.Symbol, R: sp.Symbol) -> sp.Expr:
    return sp.simplify(expr.subs(r, R))


def build_profiles() -> BoundaryProfileSet:
    r = sp.Symbol("r", positive=True)
    R = sp.Symbol("R", positive=True)
    phi0 = sp.Symbol("phi0", real=True)

    # C0-style: value jumps if exterior is zero.
    c0_profile = phi0

    # C1-style: value matches zero at R, slope generally nonzero.
    c1_profile = phi0 * (1 - r / R)

    # C2-style: value and slope vanish at R.
    c2_profile = phi0 * (1 - r / R) ** 2

    # Smooth compact toy: value and slope vanish at R.
    compact_profile = phi0 * (1 - r**2 / R**2) ** 2

    # Sharp support toy: nonzero value inside with exterior zero.
    sharp_inside = phi0

    return BoundaryProfileSet(
        r=r,
        R=R,
        phi0=phi0,
        c0_profile=c0_profile,
        c1_profile=c1_profile,
        c2_profile=c2_profile,
        compact_profile=compact_profile,
        sharp_inside=sharp_inside,
        c0_value_at_R=at_boundary(c0_profile, r, R),
        c0_slope_at_R=at_boundary(sp.diff(c0_profile, r), r, R),
        c0_flux_at_R=at_boundary(boundary_flux(c0_profile, r), r, R),
        c1_value_at_R=at_boundary(c1_profile, r, R),
        c1_slope_at_R=at_boundary(sp.diff(c1_profile, r), r, R),
        c1_flux_at_R=at_boundary(boundary_flux(c1_profile, r), r, R),
        c2_value_at_R=at_boundary(c2_profile, r, R),
        c2_slope_at_R=at_boundary(sp.diff(c2_profile, r), r, R),
        c2_flux_at_R=at_boundary(boundary_flux(c2_profile, r), r, R),
        compact_value_at_R=at_boundary(compact_profile, r, R),
        compact_slope_at_R=at_boundary(sp.diff(compact_profile, r), r, R),
        compact_flux_at_R=at_boundary(boundary_flux(compact_profile, r), r, R),
        sharp_jump_value=phi0,
        sharp_slope_inside_at_R=at_boundary(sp.diff(sharp_inside, r), r, R),
        sharp_flux_inside_at_R=at_boundary(boundary_flux(sharp_inside, r), r, R),
    )


def build_branches() -> List[BoundaryBranchEntry]:
    return [
        BoundaryBranchEntry(
            name="B1: C0 match only",
            branch="C0_or_value_jump_profile",
            condition="value may fail to match exterior zero, or only interior value is specified",
            status="REJECTED",
            danger="nonzero boundary value can hide a distributional edge when exterior is zero",
            consequence="not a safe compact-support condition",
        ),
        BoundaryBranchEntry(
            name="B2: C1 value match",
            branch="C1_value_match",
            condition="phi(R) = 0 but phi'(R) may be nonzero",
            status="RISK",
            danger="boundary flux can survive even when the value vanishes",
            consequence="value continuity alone does not prove no-shell/no-flux behavior",
        ),
        BoundaryBranchEntry(
            name="B3: C2 value and slope match",
            branch="C2_value_and_slope_match",
            condition="phi(R) = 0 and phi'(R) = 0 in the toy profile",
            status="SAFE_IF",
            danger="still requires derived support law and no recovery tuning",
            consequence="safe diagnostic condition, not a compact-support theorem",
        ),
        BoundaryBranchEntry(
            name="B4: smooth compact bump",
            branch="smooth_compact_profile",
            condition="value and slope vanish at boundary in the toy profile",
            status="SAFE_IF",
            danger="support/matching must be structural, not chosen after leakage appears",
            consequence="promising diagnostic class for no-shell behavior",
        ),
        BoundaryBranchEntry(
            name="B5: sharp cutoff",
            branch="sharp_cutoff",
            condition="interior residual is set to zero abruptly outside",
            status="REJECTED",
            danger="derivative/distributional shell can be hidden at the cutoff",
            consequence="sharp support is not neutral by declaration",
        ),
        BoundaryBranchEntry(
            name="B6: derivative jump",
            branch="derivative_jump",
            condition="phi is continuous but derivative jumps at boundary",
            status="REJECTED",
            danger="jump can encode shell-like flux or boundary source",
            consequence="no-shell condition must control derivative matching",
        ),
        BoundaryBranchEntry(
            name="B7: derived compact support",
            branch="derived_compact_support",
            condition="support, value matching, slope matching, and no-shell law follow before recovery",
            status="THEOREM_TARGET",
            danger="currently not derived",
            consequence="target for future boundary neutrality theorem",
        ),
    ]


def build_rejected_routes() -> List[RejectedSupportRoute]:
    return [
        RejectedSupportRoute(
            name="R1: compact support by declaration",
            route="compact_support_by_declaration",
            forbidden_use="support imposed to hide scalar tail or boundary leakage",
            status="REJECTED",
            consequence="support law must be derived before it can protect scalar silence",
        ),
        RejectedSupportRoute(
            name="R2: recovery-selected support radius",
            route="recovery_selected_support_radius",
            forbidden_use="support chosen from Schwarzschild/PPN/gamma_like/AB recovery",
            status="REJECTED",
            consequence="recovery may audit support behavior but may not choose it",
        ),
        RejectedSupportRoute(
            name="R3: derivative jump shell",
            route="derivative_jump_shell",
            forbidden_use="slope mismatch hidden as shell source or harmless seam",
            status="REJECTED",
            consequence="no-shell theorem must control derivative behavior",
        ),
        RejectedSupportRoute(
            name="R4: residual-kill called support theorem",
            route="residual_kill_called_support",
            forbidden_use="residual-kill convention treated as a derived compact-support law",
            status="REJECTED",
            consequence="residual-kill remains provisional unless derived",
        ),
        RejectedSupportRoute(
            name="R5: smoothing as repair",
            route="smoothing_as_repair",
            forbidden_use="smooth profile chosen after boundary/mass/scalar failure appears",
            status="REJECTED",
            consequence="smoothness is not neutrality unless source and boundary behavior are structural",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Smooth compact support no-shell problem")
    print("Question:")
    print()
    print("  When does compact support avoid hiding a shell source?")
    print()
    print("Reference discipline:")
    print()
    print("  Boundary/scalar silence targets are explicit but not proved.")
    print("  Compact support is not safe by name.")
    print("  Value matching alone may still leave boundary flux.")
    print("  Smooth matching must be derived, not chosen by recovery.")
    print("  This script tests toy profiles and records requirements.")

    with out.governance_assessments():
        out.line(
            "smooth compact support no-shell audit opened",
            StatusMark.INFO,
            "testing boundary value/slope/flux diagnostics without deriving support",
        )


def case_1_profile_diagnostics(profiles: BoundaryProfileSet, out: ScriptOutput) -> None:
    header("Case 1: Boundary profile diagnostics")
    print("C0-style interior constant profile:")
    print()
    print(f"  phi_C0(r) = {sp.sstr(profiles.c0_profile)}")
    print(f"  phi_C0(R) = {sp.sstr(profiles.c0_value_at_R)}")
    print(f"  phi_C0'(R) = {sp.sstr(profiles.c0_slope_at_R)}")
    print(f"  boundary flux = {sp.sstr(profiles.c0_flux_at_R)}")
    print("  if exterior value is zero, nonzero phi_C0(R) means value jump danger")
    print()

    print("C1-style toy profile:")
    print()
    print(f"  phi_C1(r) = {sp.sstr(profiles.c1_profile)}")
    print(f"  phi_C1(R) = {sp.sstr(profiles.c1_value_at_R)}")
    print(f"  phi_C1'(R) = {sp.sstr(profiles.c1_slope_at_R)}")
    print(f"  boundary flux = {sp.sstr(profiles.c1_flux_at_R)}")
    print()

    print("C2-style toy profile:")
    print()
    print(f"  phi_C2(r) = {sp.sstr(profiles.c2_profile)}")
    print(f"  phi_C2(R) = {sp.sstr(profiles.c2_value_at_R)}")
    print(f"  phi_C2'(R) = {sp.sstr(profiles.c2_slope_at_R)}")
    print(f"  boundary flux = {sp.sstr(profiles.c2_flux_at_R)}")
    print()

    print("Smooth compact toy profile:")
    print()
    print(f"  phi_compact(r) = {sp.sstr(profiles.compact_profile)}")
    print(f"  phi_compact(R) = {sp.sstr(profiles.compact_value_at_R)}")
    print(f"  phi_compact'(R) = {sp.sstr(profiles.compact_slope_at_R)}")
    print(f"  boundary flux = {sp.sstr(profiles.compact_flux_at_R)}")
    print()

    with out.sample_results():
        out.line(
            "C1 value-match profile can carry boundary flux",
            StatusMark.WARN if not is_zero(profiles.c1_flux_at_R) else StatusMark.PASS,
            f"boundary flux = {sp.sstr(profiles.c1_flux_at_R)}",
        )
        out.line(
            "C2 value/slope profile has zero toy boundary flux",
            StatusMark.PASS if is_zero(profiles.c2_flux_at_R) else StatusMark.FAIL,
            f"boundary flux = {sp.sstr(profiles.c2_flux_at_R)}",
        )
        out.line(
            "smooth compact toy profile has zero toy boundary flux",
            StatusMark.PASS if is_zero(profiles.compact_flux_at_R) else StatusMark.FAIL,
            f"boundary flux = {sp.sstr(profiles.compact_flux_at_R)}",
        )


def case_2_shell_danger(profiles: BoundaryProfileSet, out: ScriptOutput) -> None:
    header("Case 2: Sharp support / shell danger")
    print("Sharp-support toy:")
    print()
    print(f"  phi_inside(r) = {sp.sstr(profiles.sharp_inside)}")
    print("  phi_outside(r) = 0")
    print()
    print("At the boundary:")
    print()
    print(f"  value jump if phi0 != 0: jump = {sp.sstr(profiles.sharp_jump_value)}")
    print(f"  inside slope at R = {sp.sstr(profiles.sharp_slope_inside_at_R)}")
    print(f"  inside flux at R = {sp.sstr(profiles.sharp_flux_inside_at_R)}")
    print()
    print("Interpretation:")
    print()
    print("  zero interior slope does not save a sharp cutoff if the value jumps.")
    print("  a value jump can encode distributional boundary behavior.")
    print("  compact support must include matching/no-shell conditions, not only exterior zero.")

    with out.counterexamples():
        out.line(
            "sharp support can hide shell behavior",
            StatusMark.FAIL,
            "exterior zero is not enough if boundary matching is not controlled",
        )


def case_3_branch_ledger(branches: List[BoundaryBranchEntry], out: ScriptOutput) -> None:
    header("Case 3: Smooth compact support branch ledger")
    for entry in branches:
        print()
        print("-" * 120)
        print(entry.name)
        print("-" * 120)
        print(f"Branch: {entry.branch}")
        print(f"Condition: {entry.condition}")
        print(f"[{status_mark(entry.status).value}] {entry.name}: {entry.status}")
        print(f"Danger: {entry.danger}")
        print(f"Consequence: {entry.consequence}")

    with out.governance_assessments():
        out.line(
            "smooth compact support branch ledger populated",
            StatusMark.PASS,
            f"{len(branches)} support/matching branches classified",
        )


def case_4_rejected_routes(routes: List[RejectedSupportRoute], out: ScriptOutput) -> None:
    header("Case 4: Rejected compact-support shortcuts")
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
            "compact-support shortcuts rejected",
            StatusMark.FAIL,
            "support by declaration, recovery-selected support, shell jumps, residual-kill-as-support, and smoothing repair are not licensed",
        )


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("The smooth compact support no-shell audit fails if a later script allows:")
    print()
    print("1. compact support by declaration")
    print("2. exterior zero to replace boundary matching")
    print("3. value continuity alone to prove no shell")
    print("4. derivative jump to hide shell flux")
    print("5. smoothing selected after recovery failure")
    print("6. support radius chosen from Schwarzschild/PPN/gamma_like/AB/B=1/A")
    print("7. residual-kill treated as a compact-support theorem")
    print("8. sharp cutoff called scalar silence")
    print("9. O, H, dark label, curvature, or exchange used to repair a boundary seam")

    with out.governance_assessments():
        out.line(
            "smooth compact support overclaim controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not mistake toy smooth profiles for derived support laws",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("The diagnostic result is:")
    print()
    print("  value matching alone is not enough.")
    print("  a C1-style profile can have phi(R)=0 while carrying nonzero boundary flux.")
    print("  value and slope matching are safer diagnostic conditions.")
    print("  sharp support can hide a shell if the value or derivative matching is uncontrolled.")
    print()
    print("Safe diagnostic target:")
    print()
    print("  phi(R) = 0")
    print("  phi'(R) = 0")
    print("  no derivative jump")
    print("  no shell source")
    print("  support/matching law derived before recovery")
    print()
    print("This script does not derive compact support.")
    print("It states the matching/no-shell burden for future boundary neutrality.")
    print()
    print("Possible next script:")
    print("  candidate_scalar_tail_silence_sector_conditions.py")

    with out.governance_assessments():
        out.line(
            "smooth compact support no-shell audit complete",
            StatusMark.PASS,
            "compact support is safe only with matching/no-shell conditions; theorem burden remains open",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, profiles: BoundaryProfileSet) -> None:
    ns.record_derivation(
        derivation_id="C1_profile_boundary_flux_22",
        inputs=[profiles.c1_profile, profiles.R, profiles.phi0],
        output=profiles.c1_flux_at_R,
        method="boundary_flux(phi0*(1-r/R), r).subs(r, R)",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="boundary_flux",
        scope="toy boundary matching diagnostic",
    )

    ns.record_derivation(
        derivation_id="C2_profile_boundary_flux_22",
        inputs=[profiles.c2_profile, profiles.R, profiles.phi0],
        output=profiles.c2_flux_at_R,
        method="boundary_flux(phi0*(1-r/R)**2, r).subs(r, R)",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="boundary_flux",
        scope="toy boundary matching diagnostic",
    )

    ns.record_derivation(
        derivation_id="smooth_compact_profile_boundary_flux_22",
        inputs=[profiles.compact_profile, profiles.R, profiles.phi0],
        output=profiles.compact_flux_at_R,
        method="boundary_flux(phi0*(1-r**2/R**2)**2, r).subs(r, R)",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="boundary_flux",
        scope="toy smooth compact support diagnostic",
    )

    ns.record_derivation(
        derivation_id="smooth_compact_support_no_shell_inventory_marker_22",
        inputs=[sp.Symbol("phi_R"), sp.Symbol("dphi_R"), sp.Symbol("shell_source")],
        output=sp.Symbol("smooth_compact_support_no_shell_conditions_stated"),
        method="Group 22 smooth compact support no-shell requirements ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="requirements_marker",
        scope="Group 22 boundary neutrality and scalar silence",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        (
            "derive_compact_support_from_field_law_22",
            "Derive compact support from field law",
            "Show compact support or residual cutoff follows structurally, not from recovery tuning or after-the-fact repair.",
        ),
        (
            "derive_value_and_slope_matching_22",
            "Derive value and slope matching",
            "Show boundary profiles satisfy value and derivative matching sufficient to prevent scalar/boundary flux leakage.",
        ),
        (
            "derive_no_distributional_shell_source_22",
            "Derive no distributional shell source",
            "Show compact support does not hide value jumps, derivative jumps, or shell sources at the matching surface.",
        ),
        (
            "derive_support_independent_of_recovery_22",
            "Derive support independent of recovery",
            "Show support radius, smoothing profile, and matching behavior are not chosen from Schwarzschild, PPN, gamma_like, AB, or B=1/A recovery.",
        ),
    ]

    for obligation_id, title, description in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["ordinary_closed_regime_smooth_compact_no_shell_theorem_22"],
            description=description,
        ))


def record_governance(ns) -> None:
    core_obligations = [
        "derive_compact_support_from_field_law_22",
        "derive_value_and_slope_matching_22",
        "derive_no_distributional_shell_source_22",
        "derive_support_independent_of_recovery_22",
    ]

    ns.record_route(RouteRecord(
        route_id="ordinary_closed_regime_smooth_compact_no_shell_theorem_22",
        script_id=SCRIPT_ID,
        name="Ordinary closed-regime smooth compact support no-shell theorem target",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=core_obligations,
        activation_conditions=[
            "support follows from a structural field/boundary law",
            "value and derivative matching prevent scalar/boundary flux leakage",
            "no distributional shell source is hidden",
            "support and smoothing are recovery-independent",
        ],
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_compact_support_by_declaration_22",
        script_id=SCRIPT_ID,
        branch_id="compact_support_by_declaration",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=core_obligations,
        description=(
            "Reject compact support by declaration. Exterior zero, sharp cutoff, or smoothing profile does not prove no-shell behavior."
        ),
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_compact_support_theorem_22",
        script_id=SCRIPT_ID,
        branch_id="derived_compact_support",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=core_obligations,
        description=(
            "Derived compact support remains theorem-targeted until support law, matching law, no-shell condition, and recovery independence are shown."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="smooth_compact_support_no_shell_requirements_22",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Compact support can be treated as safe only if matching/no-shell conditions are derived. "
            "Value continuity alone is insufficient; derivative behavior and shell sources must be controlled."
        ),
        derivation_ids=[
            "C1_profile_boundary_flux_22",
            "C2_profile_boundary_flux_22",
            "smooth_compact_profile_boundary_flux_22",
            "smooth_compact_support_no_shell_inventory_marker_22",
        ],
        obligation_ids=core_obligations,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Smooth Compact Support No-Shell Conditions")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    profiles = build_profiles()
    branches = build_branches()
    routes = build_rejected_routes()

    case_0_problem_statement(out)
    case_1_profile_diagnostics(profiles, out)
    case_2_shell_danger(profiles, out)
    case_3_branch_ledger(branches, out)
    case_4_rejected_routes(routes, out)
    case_5_failure_controls(out)
    final_interpretation(out)

    record_derivations(ns, profiles)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
