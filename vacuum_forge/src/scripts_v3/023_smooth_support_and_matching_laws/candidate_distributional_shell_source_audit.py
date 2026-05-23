# Candidate distributional shell source audit
#
# Group:
#   23_smooth_support_and_matching_laws
#
# Script type:
#   REQUIREMENTS / DIAGNOSTIC
#
# Purpose
# -------
# Audit distributional shell terms that appear when boundary profiles are cut off.
#
# Locked-door question:
#
#   What distributional shell terms appear when boundary profiles are cut off?
#
# This script does not prove no-shell matching.
# It does not derive compact support.
# It does not prove boundary neutrality.
# It does not prove scalar silence.
#
# It audits cutoff profiles of the form:
#
#   phi(r) = f(r) * Theta(R-r)
#
# and records where delta-shell terms arise from value and derivative behavior
# at the support boundary.
#
# Sympy's Heaviside/DiracDelta algebra is used as a reduced diagnostic only.

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
            "matching_ladder_dep_23",
            "023_smooth_support_and_matching_laws__candidate_matching_regularization_ladder",
            "matching_regularization_ladder_marker_23",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g22_targets_dep_23",
            "022_boundary_neutrality_and_scalar_silence__candidate_boundary_scalar_silence_targets",
            "boundary_scalar_silence_target_ledger_marker_22",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g22_repair_dep_23",
            "022_boundary_neutrality_and_scalar_silence__candidate_boundary_repair_route_exclusion",
            "boundary_repair_route_exclusion_inventory_marker_22",
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
class CutoffProfileDiagnostic:
    name: str
    interior_profile: sp.Expr
    boundary_value: sp.Expr
    boundary_slope: sp.Expr
    cutoff_profile: sp.Expr
    first_derivative_delta_coeff: sp.Expr
    radial_flux_boundary: sp.Expr
    shell_like_second_order_coeff: sp.Expr
    safe_if: str
    status: str


@dataclass
class ShellAuditEntry:
    name: str
    shell_source: str
    appears_when: str
    status: str
    consequence: str


@dataclass
class RejectedShellRoute:
    name: str
    route: str
    forbidden_use: str
    status: str
    consequence: str


# =============================================================================
# Builders
# =============================================================================


def build_cutoff_diagnostics() -> List[CutoffProfileDiagnostic]:
    r = sp.Symbol("r", positive=True)
    R = sp.Symbol("R", positive=True)
    phi0 = sp.Symbol("phi0", real=True)
    H = sp.Heaviside(R - r)

    profiles = [
        ("S0_constant_cutoff", phi0),
        ("S1_linear_value_match_cutoff", phi0 * (1 - r / R)),
        ("S2_quadratic_value_slope_cutoff", phi0 * (1 - r / R) ** 2),
        ("S3_cubic_value_slope_curvature_cutoff", phi0 * (1 - r / R) ** 3),
        ("S4_smooth_bump_cutoff", phi0 * (1 - r**2 / R**2) ** 2),
    ]

    out: List[CutoffProfileDiagnostic] = []
    for name, f in profiles:
        value_R = sp.simplify(f.subs(r, R))
        slope_R = sp.simplify(sp.diff(f, r).subs(r, R))
        cutoff_profile = sp.simplify(f * H)

        # Diagnostic coefficients for distributional terms:
        #
        # d[f Theta(R-r)]/dr = f' Theta(R-r) - f(R) delta(R-r)
        #
        # In the reduced radial scalar operator, schematic shell-like terms
        # appear from derivative of r^2 f' Theta and derivative of
        # -r^2 f(R) delta.  A necessary diagnostic no-shell burden is
        # f(R)=0 and f'(R)=0.
        first_delta_coeff = sp.simplify(-value_R)
        radial_flux = sp.simplify(4 * sp.pi * R**2 * slope_R)
        second_order_coeff = sp.simplify(-R**2 * slope_R)

        if not is_zero(value_R):
            status = "REJECTED"
            safe_if = "not safe: value jump coefficient is nonzero"
        elif not is_zero(slope_R):
            status = "RISK"
            safe_if = "not safe yet: value matches but slope/flux shell diagnostic is nonzero"
        else:
            status = "SAFE_IF"
            safe_if = "diagnostically safe only if higher distributional/support/source/recovery burdens are also controlled"

        out.append(CutoffProfileDiagnostic(
            name=name,
            interior_profile=f,
            boundary_value=value_R,
            boundary_slope=slope_R,
            cutoff_profile=cutoff_profile,
            first_derivative_delta_coeff=first_delta_coeff,
            radial_flux_boundary=radial_flux,
            shell_like_second_order_coeff=second_order_coeff,
            safe_if=safe_if,
            status=status,
        ))

    return out


def build_shell_audit_entries() -> List[ShellAuditEntry]:
    return [
        ShellAuditEntry(
            name="D1: value-jump delta shell",
            shell_source="delta(R-r) from d[f(r) Theta(R-r)]/dr",
            appears_when="f(R) != 0",
            status="REJECTED",
            consequence="exterior zero does not erase a nonzero boundary value",
        ),
        ShellAuditEntry(
            name="D2: slope / flux shell diagnostic",
            shell_source="boundary flux or reduced radial shell-like term from f'(R)",
            appears_when="f(R)=0 but f'(R) != 0",
            status="RISK",
            consequence="value matching alone does not prove no-shell/no-flux behavior",
        ),
        ShellAuditEntry(
            name="D3: higher-derivative edge diagnostic",
            shell_source="curvature/second-derivative edge behavior",
            appears_when="higher derivatives are uncontrolled or profile is only toy-smooth",
            status="SAFE_IF",
            consequence="higher derivative behavior must be audited before support theorem claims",
        ),
        ShellAuditEntry(
            name="D4: structural support law",
            shell_source="none allowed",
            appears_when="support origin, value/slope matching, distributional shell absence, recovery independence, and source compatibility are derived",
            status="THEOREM_TARGET",
            consequence="positive no-shell route remains open but not derived here",
        ),
    ]


def build_rejected_routes() -> List[RejectedShellRoute]:
    return [
        RejectedShellRoute(
            name="R1: sharp cutoff as scalar silence",
            route="sharp_cutoff_scalar_silence",
            forbidden_use="multiplying by Theta(R-r) and declaring exterior zero",
            status="REJECTED",
            consequence="cutoff can create delta-shell terms",
        ),
        RejectedShellRoute(
            name="R2: value match as no-shell",
            route="value_match_no_shell",
            forbidden_use="using f(R)=0 alone to prove no shell",
            status="REJECTED",
            consequence="slope/boundary flux can remain nonzero",
        ),
        RejectedShellRoute(
            name="R3: slope match as full theorem",
            route="slope_match_full_theorem",
            forbidden_use="using f(R)=f'(R)=0 as the entire support law",
            status="REJECTED",
            consequence="support origin, higher edge behavior, source compatibility, and recovery independence remain open",
        ),
        RejectedShellRoute(
            name="R4: smoothing hides shell",
            route="smoothing_hides_shell",
            forbidden_use="smooth transition layer replaces distributional shell audit",
            status="REJECTED",
            consequence="smooth layers can still carry net flux or hidden source load",
        ),
        RejectedShellRoute(
            name="R5: repair object cancels shell",
            route="O_H_dark_exchange_curvature_shell_repair",
            forbidden_use="O, H, dark, exchange, curvature, or current role cancels boundary shell by name",
            status="REJECTED",
            consequence="repair routes remain rejected",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Distributional shell source audit problem")
    print("Question:")
    print()
    print("  What distributional shell terms appear when boundary profiles are cut off?")
    print()
    print("Reference discipline:")
    print()
    print("  Group 23 matching ladder showed value matching alone is risky.")
    print("  This script audits cutoff profiles f(r)*Theta(R-r).")
    print("  It records delta-shell and slope/flux shell diagnostics.")
    print("  It does not prove no-shell matching or compact support.")

    with out.governance_assessments():
        out.line(
            "distributional shell source audit opened",
            StatusMark.INFO,
            "auditing cutoff profiles for value-jump and slope/flux shell diagnostics",
        )


def case_1_cutoff_profile_table(profiles: List[CutoffProfileDiagnostic], out: ScriptOutput) -> None:
    header("Case 1: Cutoff profile shell diagnostics")
    for profile in profiles:
        print()
        print("-" * 120)
        print(profile.name)
        print("-" * 120)
        print(f"interior f(r): {sp.sstr(profile.interior_profile)}")
        print(f"boundary value f(R): {sp.sstr(profile.boundary_value)}")
        print(f"boundary slope f'(R): {sp.sstr(profile.boundary_slope)}")
        print(f"first-derivative delta coefficient -f(R): {sp.sstr(profile.first_derivative_delta_coeff)}")
        print(f"boundary flux 4*pi*R^2*f'(R): {sp.sstr(profile.radial_flux_boundary)}")
        print(f"shell-like second-order coefficient -R^2*f'(R): {sp.sstr(profile.shell_like_second_order_coeff)}")
        print(f"[{status_mark(profile.status).value}] {profile.name}: {profile.status}")
        print(f"Safe if: {profile.safe_if}")

    bad = [p for p in profiles if p.status == "REJECTED"]
    risky = [p for p in profiles if p.status == "RISK"]
    safe = [p for p in profiles if p.status == "SAFE_IF"]

    with out.sample_results():
        out.line(
            "cutoff value-jump profiles flagged",
            StatusMark.FAIL if bad else StatusMark.PASS,
            f"{len(bad)} rejected cutoff profile(s)",
        )
        out.line(
            "cutoff value-only profiles flagged",
            StatusMark.WARN if risky else StatusMark.PASS,
            f"{len(risky)} risky value-match profile(s)",
        )
        out.line(
            "value/slope matched cutoff profiles are diagnostic safe-if only",
            StatusMark.INFO,
            f"{len(safe)} profile(s) satisfy f(R)=f'(R)=0 diagnostics",
        )


def case_2_shell_audit_ledger(entries: List[ShellAuditEntry], out: ScriptOutput) -> None:
    header("Case 2: Distributional shell audit ledger")
    for entry in entries:
        print()
        print("-" * 120)
        print(entry.name)
        print("-" * 120)
        print(f"Shell source: {entry.shell_source}")
        print(f"Appears when: {entry.appears_when}")
        print(f"[{status_mark(entry.status).value}] {entry.name}: {entry.status}")
        print(f"Consequence: {entry.consequence}")

    with out.governance_assessments():
        out.line(
            "distributional shell audit ledger populated",
            StatusMark.PASS,
            f"{len(entries)} shell diagnostics classified",
        )


def case_3_rejected_routes(routes: List[RejectedShellRoute], out: ScriptOutput) -> None:
    header("Case 3: Rejected shell-source shortcuts")
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
            "shell-source shortcuts rejected",
            StatusMark.FAIL,
            "sharp cutoff, value-match proof, slope-match theorem, smoothing cover, and repair-object cancellation remain rejected",
        )


def case_4_failure_controls(out: ScriptOutput) -> None:
    header("Case 4: Failure controls")
    print("The distributional shell source audit fails if a later script allows:")
    print()
    print("1. f(r)*Theta(R-r) to count as compact support by declaration")
    print("2. nonzero f(R) value jump to be ignored")
    print("3. f(R)=0 alone to prove no shell")
    print("4. nonzero f'(R) boundary flux to be ignored")
    print("5. f(R)=f'(R)=0 to be treated as full support law")
    print("6. smoothing layer to replace distributional audit")
    print("7. O, H, dark, curvature, exchange, or current repair to cancel shell terms")
    print("8. recovery-selected support to determine where the cutoff lives")
    print("9. parent equation to open from no-shell diagnostics alone")

    with out.governance_assessments():
        out.line(
            "distributional shell overclaim controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not confuse cutoff diagnostics with derived no-shell matching",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Distributional shell audit result:")
    print()
    print("  A sharp cutoff can create delta-shell behavior from nonzero f(R).")
    print("  Value matching f(R)=0 removes the first value-jump diagnostic but not slope/flux danger.")
    print("  Slope matching f'(R)=0 is a necessary diagnostic no-flux condition.")
    print("  Value+slope matching is still not a support theorem.")
    print("  Structural support, distributional shell absence, recovery independence, and source compatibility remain open.")
    print()
    print("Possible next script:")
    print("  candidate_compact_support_admissibility_conditions.py")
    print()
    print("Tiny goblin label:")
    print("  Sharp edge makes shell crumbs. Sweep before claiming silence.")

    with out.governance_assessments():
        out.line(
            "distributional shell source audit complete",
            StatusMark.PASS,
            "cutoff shell diagnostics explicit; no-shell theorem remains open",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, profiles: List[CutoffProfileDiagnostic]) -> None:
    for profile in profiles:
        safe = profile.name.replace("/", "_").replace(" ", "_")
        ns.record_derivation(
            derivation_id=f"{safe}_cutoff_shell_diagnostic_23",
            inputs=[profile.interior_profile],
            output=sp.Tuple(
                profile.boundary_value,
                profile.boundary_slope,
                profile.first_derivative_delta_coeff,
                profile.radial_flux_boundary,
                profile.shell_like_second_order_coeff,
            ),
            method="evaluate f(R), f'(R), -f(R), 4*pi*R**2*f'(R), and -R**2*f'(R)",
            status=Status.DERIVED,
            record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
            result_type="cutoff_shell_diagnostic",
            scope="Group 23 smooth support and matching laws",
        )

    ns.record_derivation(
        derivation_id="distributional_shell_source_audit_marker_23",
        inputs=[
            sp.Symbol("value_jump"),
            sp.Symbol("slope_jump"),
            sp.Symbol("boundary_flux"),
            sp.Symbol("shell_absence"),
        ],
        output=sp.Symbol("distributional_shell_source_audit_stated"),
        method="Group 23 distributional shell source audit ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="requirements_marker",
        scope="Group 23 smooth support and matching laws",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        (
            "g23_derive_no_value_jump",
            "Derive no value jump",
            "Show f(R)=0 follows structurally for supported residual profiles.",
        ),
        (
            "g23_derive_no_slope_jump",
            "Derive no slope / flux jump",
            "Show f'(R)=0 or equivalent zero boundary flux follows structurally.",
        ),
        (
            "g23_derive_no_distributional_shell",
            "Derive no distributional shell source",
            "Show cutoff/support behavior produces no delta-shell, shell-like radial source, or hidden boundary source load.",
        ),
        (
            "g23_derive_cutoff_independent_of_recovery",
            "Derive cutoff/support independence from recovery",
            "Show support edge and smoothing are not chosen from Schwarzschild, PPN, gamma_like, AB, or B=1/A recovery.",
        ),
    ]

    for obligation_id, title, description in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g23_no_shell_route"],
            description=description,
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g23_derive_no_value_jump",
        "g23_derive_no_slope_jump",
        "g23_derive_no_distributional_shell",
        "g23_derive_cutoff_independent_of_recovery",
    ]

    ns.record_route(RouteRecord(
        route_id="g23_no_shell_route",
        script_id=SCRIPT_ID,
        name="Group 23 no-shell support theorem target",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "value jump is absent by structural law",
            "slope/flux jump is absent by structural law",
            "distributional shell terms are controlled",
            "support/cutoff behavior is recovery-independent",
        ],
    ))

    for branch_id in [
        "sharp_cutoff_as_silence",
        "value_match_as_no_shell",
        "slope_match_as_full_theorem",
        "smoothing_hides_shell",
        "repair_object_cancels_shell",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_23",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; cutoff diagnostics do not prove no-shell support.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g23_cutoff_shell_diagnostics_not_theorem",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Cutoff profiles can carry value-jump delta terms and slope/flux shell diagnostics. "
            "Value+slope matching is necessary diagnostically, but no-shell support remains theorem-targeted."
        ),
        derivation_ids=[
            "S0_constant_cutoff_cutoff_shell_diagnostic_23",
            "S1_linear_value_match_cutoff_cutoff_shell_diagnostic_23",
            "S2_quadratic_value_slope_cutoff_cutoff_shell_diagnostic_23",
            "S3_cubic_value_slope_curvature_cutoff_cutoff_shell_diagnostic_23",
            "S4_smooth_bump_cutoff_cutoff_shell_diagnostic_23",
            "distributional_shell_source_audit_marker_23",
        ],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Distributional Shell Source Audit")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    profiles = build_cutoff_diagnostics()
    entries = build_shell_audit_entries()
    routes = build_rejected_routes()

    case_0_problem_statement(out)
    case_1_cutoff_profile_table(profiles, out)
    case_2_shell_audit_ledger(entries, out)
    case_3_rejected_routes(routes, out)
    case_4_failure_controls(out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, profiles)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
