# Candidate compact support admissibility conditions
#
# Group:
#   23_smooth_support_and_matching_laws
#
# Script type:
#   REQUIREMENTS / DIAGNOSTIC
#
# Purpose
# -------
# Separate admissible compact support from declared compact support.
#
# Locked-door question:
#
#   When is compact support admissible rather than imposed?
#
# This script does not derive compact support.
# It does not prove no-shell matching.
# It does not prove boundary neutrality.
# It does not prove scalar silence.
#
# It records the admissibility conditions required before compact support can be
# treated as safe:
#
#   structural support origin,
#   boundary value vanishes,
#   boundary slope vanishes,
#   distributional shell terms vanish,
#   support radius not recovery-selected,
#   no hidden coefficient tuning,
#   no non-A A-tail,
#   no residual scalar 1/r exterior tail.

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
        "ADMISSIBLE_IF": StatusMark.INFO,
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
            "shell_audit_dep_23",
            "023_smooth_support_and_matching_laws__candidate_distributional_shell_source_audit",
            "distributional_shell_source_audit_marker_23",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g22_scalar_dep_23",
            "022_boundary_neutrality_and_scalar_silence__candidate_scalar_tail_silence_sector_conditions",
            "scalar_tail_silence_sector_inventory_marker_22",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g21_mass_dep_23",
            "021_source_routing_and_mass_neutrality__candidate_A_sector_mass_charge_definition",
            "A_sector_mass_definition_21",
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
class CompactSupportDiagnostic:
    R_support: sp.Symbol
    C_ext: sp.Symbol
    q_A_tail: sp.Symbol
    sigma_shell: sp.Symbol
    alpha_tune: sp.Symbol
    value_residual: sp.Symbol
    slope_residual: sp.Symbol
    scalar_flux_ext: sp.Expr
    A_mass_shift_ext: sp.Expr
    admissibility_residual: sp.Expr


@dataclass
class CompactSupportCondition:
    name: str
    condition: str
    status: str
    failure_if: str
    consequence: str


@dataclass
class CompactSupportBranch:
    name: str
    branch: str
    status: str
    allowed_if: str
    rejected_if: str


@dataclass
class RejectedCompactRoute:
    name: str
    route: str
    forbidden_use: str
    status: str
    consequence: str


# =============================================================================
# Builders
# =============================================================================


def build_diagnostics() -> CompactSupportDiagnostic:
    R_support, C_ext, q_A_tail, sigma_shell, alpha_tune, value_residual, slope_residual = sp.symbols(
        "R_support C_ext q_A_tail sigma_shell alpha_tune value_residual slope_residual",
        real=True,
    )
    G = sp.Symbol("G", positive=True)
    c = sp.Symbol("c", positive=True)

    scalar_flux_ext = sp.simplify(-4 * sp.pi * C_ext)
    A_mass_shift_ext = sp.simplify(-c**2 * q_A_tail / (2 * G))

    admissibility_residual = sp.simplify(
        value_residual
        + slope_residual
        + sigma_shell
        + C_ext
        + q_A_tail
        + alpha_tune
    )

    return CompactSupportDiagnostic(
        R_support=R_support,
        C_ext=C_ext,
        q_A_tail=q_A_tail,
        sigma_shell=sigma_shell,
        alpha_tune=alpha_tune,
        value_residual=value_residual,
        slope_residual=slope_residual,
        scalar_flux_ext=scalar_flux_ext,
        A_mass_shift_ext=A_mass_shift_ext,
        admissibility_residual=admissibility_residual,
    )


def build_conditions() -> List[CompactSupportCondition]:
    return [
        CompactSupportCondition(
            name="A1: structural support origin",
            condition="support follows from field/source/boundary law before recovery checks",
            status="REQUIRED",
            failure_if="support is imposed after scalar, boundary, mass, or recovery failure appears",
            consequence="declared support is not admissible",
        ),
        CompactSupportCondition(
            name="A2: boundary value vanishes",
            condition="f(R)=0",
            status="REQUIRED",
            failure_if="nonzero boundary value creates value-jump shell diagnostic",
            consequence="exterior zero cannot hide a nonzero boundary value",
        ),
        CompactSupportCondition(
            name="A3: boundary slope vanishes",
            condition="f'(R)=0 or equivalent no-flux matching condition",
            status="REQUIRED",
            failure_if="nonzero slope leaves boundary flux or shell-like radial diagnostic",
            consequence="value matching alone is insufficient",
        ),
        CompactSupportCondition(
            name="A4: distributional shell terms vanish",
            condition="no delta-shell, derivative-jump, shell-like radial source, or hidden boundary source load",
            status="REQUIRED",
            failure_if="shell source is hidden by cutoff, smoothing, or support language",
            consequence="no-shell behavior must be audited explicitly",
        ),
        CompactSupportCondition(
            name="A5: support radius not recovery-selected",
            condition="R_support is structural/source-derived, not chosen from Schwarzschild/PPN/gamma_like/AB/B=1/A recovery",
            status="REQUIRED",
            failure_if="support boundary is selected to pass a recovery test",
            consequence="recovery remains downstream diagnostic",
        ),
        CompactSupportCondition(
            name="A6: no hidden coefficient tuning",
            condition="no support/smoothing coefficient is chosen to cancel visible scalar tail, A-tail, or current flux",
            status="REQUIRED",
            failure_if="tuning parameter erases leakage after the fact",
            consequence="support cannot be a repair knob",
        ),
        CompactSupportCondition(
            name="A7: no non-A A-tail",
            condition="q_A_tail = 0",
            status="REQUIRED",
            failure_if="compact support leaves exterior delta A = q/r",
            consequence="compact support must not shift protected A-sector mass",
        ),
        CompactSupportCondition(
            name="A8: no residual scalar exterior tail",
            condition="C_ext = 0",
            status="REQUIRED",
            failure_if="compact support leaves exterior C/r residual tail",
            consequence="scalar silence remains violated",
        ),
        CompactSupportCondition(
            name="A9: source compatibility",
            condition="support law does not create boundary shell source, duplicate ordinary source load, or non-A repair channel",
            status="REQUIRED",
            failure_if="ordinary rho/T is rerouted into boundary/support terms",
            consequence="support must preserve Group 21 source no-double-counting",
        ),
    ]


def build_branches() -> List[CompactSupportBranch]:
    return [
        CompactSupportBranch(
            name="B1: declared compact support",
            branch="set exterior residual to zero by declaration",
            status="REJECTED",
            allowed_if="never as theorem; at most a diagnostic label if all support burdens are separately open",
            rejected_if="used to claim scalar silence, no shell, or boundary neutrality",
        ),
        CompactSupportBranch(
            name="B2: value/slope diagnostic support",
            branch="f(R)=0 and f'(R)=0 in toy profile",
            status="SAFE_IF",
            allowed_if="used only as diagnostic necessary condition",
            rejected_if="treated as structural support law",
        ),
        CompactSupportBranch(
            name="B3: smooth profile support",
            branch="smooth-looking transition or bump",
            status="SAFE_IF",
            allowed_if="structural origin, zero net flux, no A-tail, no scalar tail, no recovery tuning, and source compatibility remain explicit obligations",
            rejected_if="smoothness replaces shell/source/recovery audit",
        ),
        CompactSupportBranch(
            name="B4: structural compact support",
            branch="support follows from field/source/boundary law",
            status="THEOREM_TARGET",
            allowed_if="all admissibility conditions are derived",
            rejected_if="any condition is chosen after leakage appears",
        ),
    ]


def build_rejected_routes() -> List[RejectedCompactRoute]:
    return [
        RejectedCompactRoute(
            name="R1: support by declaration",
            route="compact_support_by_declaration",
            forbidden_use="exterior zero or cutoff used as proof of compact support",
            status="REJECTED",
            consequence="support must be derived, not named",
        ),
        RejectedCompactRoute(
            name="R2: recovery-selected support",
            route="recovery_selected_support",
            forbidden_use="R_support or smoothing width chosen to pass Schwarzschild/PPN/gamma_like/AB/B=1/A",
            status="REJECTED",
            consequence="recovery cannot construct boundary law",
        ),
        RejectedCompactRoute(
            name="R3: coefficient-tuned support",
            route="coefficient_tuned_support",
            forbidden_use="support coefficient chosen to cancel C_ext, q_A_tail, I_nonA, or shell term",
            status="REJECTED",
            consequence="support cannot be repair tuning",
        ),
        RejectedCompactRoute(
            name="R4: support creates boundary source",
            route="support_boundary_source",
            forbidden_use="compact support creates shell source or duplicate ordinary source load",
            status="REJECTED",
            consequence="source no-double-counting must be preserved",
        ),
        RejectedCompactRoute(
            name="R5: repair object supplies support",
            route="O_H_dark_exchange_curvature_support_patch",
            forbidden_use="O, H, dark, exchange, curvature, or current role supplies missing support law",
            status="REJECTED",
            consequence="repair objects cannot derive compact support",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Compact support admissibility problem")
    print("Question:")
    print()
    print("  When is compact support admissible rather than imposed?")
    print()
    print("Reference discipline:")
    print()
    print("  Matching ladder and shell audit show value/slope conditions are diagnostic.")
    print("  Compact support also needs structural origin, no shell, no tails, no recovery tuning, and source compatibility.")
    print("  This script records admissibility conditions; it does not derive compact support.")

    with out.governance_assessments():
        out.line(
            "compact support admissibility audit opened",
            StatusMark.INFO,
            "separating structural compact support from declared support",
        )


def case_1_diagnostics(exprs: CompactSupportDiagnostic, out: ScriptOutput) -> None:
    header("Case 1: Compact support leakage diagnostics")
    print("Representative compact-support failure coefficients:")
    print()
    print(f"  value_residual = {sp.sstr(exprs.value_residual)}")
    print(f"  slope_residual = {sp.sstr(exprs.slope_residual)}")
    print(f"  sigma_shell = {sp.sstr(exprs.sigma_shell)}")
    print(f"  C_ext = {sp.sstr(exprs.C_ext)}")
    print(f"  q_A_tail = {sp.sstr(exprs.q_A_tail)}")
    print(f"  alpha_tune = {sp.sstr(exprs.alpha_tune)}")
    print()
    print("Reduced leakage witnesses:")
    print()
    print(f"  scalar flux from C_ext: {sp.sstr(exprs.scalar_flux_ext)}")
    print(f"  A-sector mass shift from q_A_tail: {sp.sstr(exprs.A_mass_shift_ext)}")
    print()
    print("Admissibility residual ledger:")
    print()
    print(f"  residual = {sp.sstr(exprs.admissibility_residual)}")
    print()
    print("All entries must vanish or be independently theorem-routed before compact support is admissible.")

    with out.derived_results():
        out.line(
            "compact support scalar-tail leakage witness stated",
            StatusMark.PASS,
            f"F = {sp.sstr(exprs.scalar_flux_ext)}",
        )
        out.line(
            "compact support A-tail mass-shift witness stated",
            StatusMark.PASS,
            f"delta_M_A = {sp.sstr(exprs.A_mass_shift_ext)}",
        )
        out.line(
            "compact support admissibility residual ledger stated",
            StatusMark.PASS,
            f"residual = {sp.sstr(exprs.admissibility_residual)}",
        )


def case_2_condition_ledger(conditions: List[CompactSupportCondition], out: ScriptOutput) -> None:
    header("Case 2: Compact support admissibility condition ledger")
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
            "compact support admissibility conditions populated",
            StatusMark.OBLIGATION,
            f"{len(conditions)} admissibility conditions remain required",
        )


def case_3_branch_ledger(branches: List[CompactSupportBranch], out: ScriptOutput) -> None:
    header("Case 3: Compact support branch ledger")
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
            "compact support branch ledger populated",
            StatusMark.PASS,
            f"{len(branches)} support branches classified",
        )


def case_4_rejected_routes(routes: List[RejectedCompactRoute], out: ScriptOutput) -> None:
    header("Case 4: Rejected compact-support routes")
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
            "compact-support false routes rejected",
            StatusMark.FAIL,
            "support by declaration, recovery selection, coefficient tuning, boundary source creation, and repair patches remain rejected",
        )


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("The compact support admissibility audit fails if a later script allows:")
    print()
    print("1. compact support by declaration")
    print("2. exterior zero as support proof")
    print("3. value/slope matching as full support theorem")
    print("4. support radius chosen from recovery")
    print("5. smoothing width or coefficient chosen from recovery")
    print("6. support coefficient tuned to cancel C_ext, q_A_tail, I_nonA, or shell term")
    print("7. compact support to create boundary shell source")
    print("8. compact support to duplicate ordinary source load")
    print("9. O, H, dark, exchange, curvature, or current object to supply missing support law")
    print("10. parent equation opened from compact-support admissibility conditions alone")

    with out.governance_assessments():
        out.line(
            "compact support overclaim controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not confuse admissibility conditions with derived support",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Compact support is admissible only if:")
    print()
    print("  support origin is structural")
    print("  f(R)=0")
    print("  f'(R)=0 or equivalent no-flux condition")
    print("  distributional shell terms vanish")
    print("  support radius is not recovery-selected")
    print("  no hidden coefficient tuning occurs")
    print("  q_A_tail = 0")
    print("  C_ext = 0")
    print("  source no-double-counting is preserved")
    print()
    print("This script does not derive compact support.")
    print("It records the admissibility burden.")
    print()
    print("Possible next script:")
    print("  candidate_transition_layer_mass_flux_audit.py")
    print()
    print("Tiny goblin label:")
    print("  Declared support is a painted door. Structural support needs hinges.")

    with out.governance_assessments():
        out.line(
            "compact support admissibility audit complete",
            StatusMark.PASS,
            "admissibility conditions explicit; compact-support theorem remains open",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, exprs: CompactSupportDiagnostic) -> None:
    ns.record_derivation(
        derivation_id="compact_support_scalar_tail_leakage_23",
        inputs=[exprs.C_ext],
        output=exprs.scalar_flux_ext,
        method="F_ext = -4*pi*C_ext",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="scalar_tail_leakage_witness",
        scope="Group 23 compact support admissibility",
    )

    ns.record_derivation(
        derivation_id="compact_support_A_tail_mass_shift_23",
        inputs=[exprs.q_A_tail],
        output=exprs.A_mass_shift_ext,
        method="delta_M_A = -c**2*q_A_tail/(2*G)",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="A_tail_mass_shift_witness",
        scope="Group 23 compact support admissibility",
    )

    ns.record_derivation(
        derivation_id="compact_support_admissibility_marker_23",
        inputs=[
            exprs.value_residual,
            exprs.slope_residual,
            exprs.sigma_shell,
            exprs.C_ext,
            exprs.q_A_tail,
            exprs.alpha_tune,
        ],
        output=sp.Symbol("compact_support_admissibility_conditions_stated"),
        method="Group 23 compact support admissibility ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="requirements_marker",
        scope="Group 23 smooth support and matching laws",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g23_derive_structural_support", "Derive structural support origin"),
        ("g23_derive_value_slope_matching", "Derive value and slope matching"),
        ("g23_derive_no_shell_support", "Derive no-shell compact support"),
        ("g23_derive_recovery_independent_support", "Derive recovery-independent support"),
        ("g23_derive_no_tail_no_A_shift", "Derive no exterior scalar tail and no A-tail shift"),
        ("g23_derive_source_compatible_support", "Derive source-compatible support"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g23_compact_support_route"],
            description=(
                "Compact support remains theorem-targeted until structural origin, matching, no-shell behavior, "
                "recovery independence, no leakage, and source compatibility are derived."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g23_derive_structural_support",
        "g23_derive_value_slope_matching",
        "g23_derive_no_shell_support",
        "g23_derive_recovery_independent_support",
        "g23_derive_no_tail_no_A_shift",
        "g23_derive_source_compatible_support",
    ]

    ns.record_route(RouteRecord(
        route_id="g23_compact_support_route",
        script_id=SCRIPT_ID,
        name="Group 23 compact support admissibility theorem target",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "support origin is structural",
            "value and slope matching are derived",
            "distributional shell terms vanish",
            "support is recovery-independent",
            "no exterior scalar tail or A-tail shift remains",
            "source no-double-counting is preserved",
        ],
    ))

    for branch_id in [
        "support_by_declaration",
        "recovery_selected_support",
        "coefficient_tuned_support",
        "support_boundary_source",
        "repair_object_support_patch",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_23",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; compact support must be structural, neutral, no-shell, and source-compatible.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g23_compact_support_admissibility_not_theorem",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Compact support is admissible only with structural origin, value/slope matching, no shell, recovery independence, "
            "no hidden tuning, no exterior scalar tail, no A-tail mass shift, and source compatibility. "
            "This script states admissibility conditions, not a compact-support theorem."
        ),
        derivation_ids=[
            "compact_support_scalar_tail_leakage_23",
            "compact_support_A_tail_mass_shift_23",
            "compact_support_admissibility_marker_23",
        ],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Compact Support Admissibility Conditions")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    diagnostics = build_diagnostics()
    conditions = build_conditions()
    branches = build_branches()
    routes = build_rejected_routes()

    case_0_problem_statement(out)
    case_1_diagnostics(diagnostics, out)
    case_2_condition_ledger(conditions, out)
    case_3_branch_ledger(branches, out)
    case_4_rejected_routes(routes, out)
    case_5_failure_controls(out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, diagnostics)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
