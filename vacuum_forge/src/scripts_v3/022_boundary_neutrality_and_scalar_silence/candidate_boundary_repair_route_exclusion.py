# Candidate boundary repair route exclusion
#
# Group:
#   22_boundary_neutrality_and_scalar_silence
#
# Script type:
#   REQUIREMENTS / GOVERNANCE AUDIT
#
# Purpose
# -------
# Inventory and reject boundary/scalar repair mechanisms.
#
# Locked-door question:
#
#   Which boundary repair routes must remain rejected?
#
# This script does not prove boundary neutrality.
# It does not prove scalar silence.
# It does not derive compact support, current neutrality, O, H, or dark coupling.
#
# It records that repair mechanisms cannot replace a no-shell, no-tail,
# no-current, no-double-counting theorem.

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
        "ROLE_LEVEL": StatusMark.INFO,
        "SAFE_IF": StatusMark.INFO,
        "THEOREM_TARGET": StatusMark.DEFER,
        "UNRESOLVED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "boundary_scalar_silence_target_ledger_dependency_22",
            "022_boundary_neutrality_and_scalar_silence__candidate_boundary_scalar_silence_targets",
            "boundary_scalar_silence_target_ledger_marker_22",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "smooth_compact_no_shell_dependency_22",
            "022_boundary_neutrality_and_scalar_silence__candidate_smooth_compact_support_no_shell_conditions",
            "smooth_compact_support_no_shell_inventory_marker_22",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "sector_scalar_silence_dependency_22",
            "022_boundary_neutrality_and_scalar_silence__candidate_scalar_tail_silence_sector_conditions",
            "scalar_tail_silence_sector_inventory_marker_22",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "boundary_current_flux_silence_dependency_22",
            "022_boundary_neutrality_and_scalar_silence__candidate_boundary_current_flux_silence",
            "boundary_current_flux_silence_inventory_marker_22",
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
class RepairDiagnosticExpression:
    q_shell: sp.Symbol
    C_tail: sp.Symbol
    I_repair: sp.Symbol
    q_counter: sp.Symbol
    q_smoothing: sp.Symbol
    q_total_repair: sp.Expr
    C_total_repair: sp.Expr
    I_total_repair: sp.Expr
    mass_shift_from_q: sp.Expr
    scalar_flux_from_C: sp.Expr
    current_flux_from_I: sp.Expr


@dataclass
class RepairRouteEntry:
    name: str
    route: str
    forbidden_use: str
    status: str
    reason: str
    consequence: str


@dataclass
class AllowedNonRepairEntry:
    name: str
    condition: str
    status: str
    caution: str
    consequence: str


# =============================================================================
# Builders
# =============================================================================


def build_diagnostics() -> RepairDiagnosticExpression:
    q_shell, C_tail, I_repair, q_counter, q_smoothing = sp.symbols(
        "q_shell C_tail I_repair q_counter q_smoothing",
        real=True,
    )
    G = sp.Symbol("G", positive=True)
    c = sp.Symbol("c", positive=True)

    q_total_repair = sp.simplify(q_shell + q_counter + q_smoothing)
    C_total_repair = sp.simplify(C_tail)
    I_total_repair = sp.simplify(I_repair)

    return RepairDiagnosticExpression(
        q_shell=q_shell,
        C_tail=C_tail,
        I_repair=I_repair,
        q_counter=q_counter,
        q_smoothing=q_smoothing,
        q_total_repair=q_total_repair,
        C_total_repair=C_total_repair,
        I_total_repair=I_total_repair,
        mass_shift_from_q=sp.simplify(-c**2 * q_total_repair / (2 * G)),
        scalar_flux_from_C=sp.simplify(-4 * sp.pi * C_tail),
        current_flux_from_I=I_repair,
    )


def build_repair_routes() -> List[RepairRouteEntry]:
    return [
        RepairRouteEntry(
            name="R1: surface counterterm",
            route="surface_counterterm",
            forbidden_use="counterterm chosen to cancel boundary A-flux, scalar tail, or shell mismatch after leakage appears",
            status="REJECTED",
            reason="counterterm is not a boundary theorem and can hide mass/scalar leakage",
            consequence="no surface counterterm may supply boundary neutrality by repair",
        ),
        RepairRouteEntry(
            name="R2: boundary repair current",
            route="boundary_repair_current",
            forbidden_use="current selected to cancel boundary flux or exterior scalar/current residue",
            status="REJECTED",
            reason="current neutrality requires a current law, not a repair current",
            consequence="boundary currents must vanish or be future theorem-routed as neutral transport",
        ),
        RepairRouteEntry(
            name="R3: R_V boundary cancellation",
            route="R_V_boundary_cancellation",
            forbidden_use="relaxation role adjusted to erase boundary mismatch, scalar tail, or A-flux shift",
            status="REJECTED",
            reason="R_V remains role-level and has no boundary operator",
            consequence="R_V cannot be a boundary purse",
        ),
        RepairRouteEntry(
            name="R4: J_exch repair",
            route="J_exch_repair",
            forbidden_use="exchange current cancels ordinary boundary, scalar, source-routing, or recovery failure",
            status="REJECTED",
            reason="exchange is not repair and no exchange source/support law is derived",
            consequence="J_exch remains role-level/theorem-targeted",
        ),
        RepairRouteEntry(
            name="R5: curvature boundary rescue",
            route="curvature_boundary_rescue",
            forbidden_use="curvature diagnostic, balance, or current smooths mass by boundary repair",
            status="REJECTED",
            reason="curvature accounting remains diagnostic/branch-filter and J_curv remains undefined",
            consequence="curvature cannot rescue boundary neutrality",
        ),
        RepairRouteEntry(
            name="R6: H boundary counterterm",
            route="H_boundary_counterterm",
            forbidden_use="H_curv/H_exch inserted to absorb shell flux, scalar tail, divergence gap, or M_ext correction",
            status="REJECTED",
            reason="H_curv/H_exch are not defined and not insertable",
            consequence="H remains diagnostic-only audit label",
        ),
        RepairRouteEntry(
            name="R7: O boundary eraser",
            route="O_boundary_eraser",
            forbidden_use="O removes boundary/scalar leakage without domain, kernel, image, divergence, and boundary law",
            status="REJECTED",
            reason="Group 20 did not derive active no-overlap operator",
            consequence="O remains theorem-targeted, diagnostic-only labels are safe only if inert",
        ),
        RepairRouteEntry(
            name="R8: dark boundary patch",
            route="dark_boundary_patch",
            forbidden_use="dark label absorbs ordinary boundary, scalar-tail, current, H, or recovery failure",
            status="REJECTED",
            reason="dark sector is optional downstream and not an ordinary repair patch",
            consequence="dark labels cannot make ordinary boundary/scalar silence true",
        ),
        RepairRouteEntry(
            name="R9: recovery-tuned smoothing",
            route="recovery_tuned_smoothing",
            forbidden_use="smoothing profile, support radius, or boundary data chosen from Schwarzschild/PPN/gamma_like/AB/B=1/A",
            status="REJECTED",
            reason="recovery is downstream diagnostic, not construction",
            consequence="boundary conditions cannot be selected by recovery target",
        ),
        RepairRouteEntry(
            name="R10: sharp support hiding shell charge",
            route="sharp_support_hiding_shell_charge",
            forbidden_use="compact support imposed while value or derivative mismatch hides a shell source",
            status="REJECTED",
            reason="compact support must include matching/no-shell conditions",
            consequence="sharp support is not scalar silence",
        ),
    ]


def build_allowed_nonrepair_entries() -> List[AllowedNonRepairEntry]:
    return [
        AllowedNonRepairEntry(
            name="A1: diagnostic boundary audit",
            condition="labels boundary behavior without modifying equations, sources, metrics, or coefficients",
            status="SAFE_IF",
            caution="diagnostic labels must not re-enter as repair mechanisms",
            consequence="safe bookkeeping only",
        ),
        AllowedNonRepairEntry(
            name="A2: smooth matched profile diagnostic",
            condition="toy profile has phi(R)=0 and phi'(R)=0",
            status="SAFE_IF",
            caution="still needs derived support law and no-shell theorem",
            consequence="safe as diagnostic, not as proof",
        ),
        AllowedNonRepairEntry(
            name="A3: derived no-shell support",
            condition="support/matching/no-shell behavior follows before recovery or leakage appears",
            status="THEOREM_TARGET",
            caution="not derived in this script",
            consequence="future positive route for boundary neutrality",
        ),
        AllowedNonRepairEntry(
            name="A4: neutral transport theorem",
            condition="future current law shows no mass, scalar, boundary, source, or recovery effect",
            status="THEOREM_TARGET",
            caution="not derived while currents remain undefined/role-level",
            consequence="possible future route for non-A current silence",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Boundary repair route exclusion problem")
    print("Question:")
    print()
    print("  Which boundary repair routes must remain rejected?")
    print()
    print("Reference discipline:")
    print()
    print("  Boundary/scalar silence targets are explicit.")
    print("  Compact support needs matching/no-shell conditions.")
    print("  Scalar-tail and current-flux sector coefficients must vanish.")
    print("  Repair mechanisms cannot replace the missing theorem.")
    print("  This script excludes repair routes; it does not prove boundary neutrality.")

    with out.governance_assessments():
        out.line(
            "boundary repair route exclusion audit opened",
            StatusMark.INFO,
            "rejecting mechanisms that would patch boundary/scalar/current leakage after the fact",
        )


def case_1_repair_diagnostics(exprs: RepairDiagnosticExpression, out: ScriptOutput) -> None:
    header("Case 1: Reduced repair diagnostics")
    print("Boundary repair terms would still carry reduced witnesses:")
    print()
    print(f"  q_total_repair = {sp.sstr(exprs.q_total_repair)}")
    print(f"  delta_M_A|repair = {sp.sstr(exprs.mass_shift_from_q)}")
    print()
    print(f"  C_total_repair = {sp.sstr(exprs.C_total_repair)}")
    print(f"  F_scalar|repair = {sp.sstr(exprs.scalar_flux_from_C)}")
    print()
    print(f"  I_total_repair = {sp.sstr(exprs.I_total_repair)}")
    print(f"  Phi_current|repair = {sp.sstr(exprs.current_flux_from_I)}")
    print()
    print("Neutral repair would require these coefficients to vanish or be independently theorem-routed.")
    print("Choosing repair coefficients after leakage appears is not a theorem.")

    with out.derived_results():
        out.line(
            "repair A-tail mass diagnostic stated",
            StatusMark.PASS,
            f"delta_M_A|repair = {sp.sstr(exprs.mass_shift_from_q)}",
        )
        out.line(
            "repair scalar-tail flux diagnostic stated",
            StatusMark.PASS,
            f"F_scalar|repair = {sp.sstr(exprs.scalar_flux_from_C)}",
        )
        out.line(
            "repair current-flux diagnostic stated",
            StatusMark.PASS,
            f"Phi_current|repair = {sp.sstr(exprs.current_flux_from_I)}",
        )


def case_2_rejected_repair_ledger(routes: List[RepairRouteEntry], out: ScriptOutput) -> None:
    header("Case 2: Rejected boundary repair route ledger")
    for route in routes:
        print()
        print("-" * 120)
        print(route.name)
        print("-" * 120)
        print(f"Route: {route.route}")
        print(f"Forbidden use: {route.forbidden_use}")
        print(f"[{status_mark(route.status).value}] {route.name}: {route.status}")
        print(f"Reason: {route.reason}")
        print(f"Consequence: {route.consequence}")

    with out.counterexamples():
        out.line(
            "boundary repair route ledger populated",
            StatusMark.FAIL,
            f"{len(routes)} boundary/scalar/current repair routes remain rejected",
        )


def case_3_allowed_nonrepair_ledger(entries: List[AllowedNonRepairEntry], out: ScriptOutput) -> None:
    header("Case 3: Allowed non-repair diagnostic/theorem-target routes")
    for entry in entries:
        print()
        print("-" * 120)
        print(entry.name)
        print("-" * 120)
        print(f"Condition: {entry.condition}")
        print(f"[{status_mark(entry.status).value}] {entry.name}: {entry.status}")
        print(f"Caution: {entry.caution}")
        print(f"Consequence: {entry.consequence}")

    with out.governance_assessments():
        out.line(
            "non-repair safe/theorem-target routes stated",
            StatusMark.PASS,
            "diagnostics and future theorems remain possible; repairs remain rejected",
        )


def case_4_failure_controls(out: ScriptOutput) -> None:
    header("Case 4: Failure controls")
    print("The boundary repair route exclusion audit fails if a later script allows:")
    print()
    print("1. surface counterterm as boundary neutrality")
    print("2. boundary repair current introduced after leakage")
    print("3. R_V to erase boundary mismatch")
    print("4. J_exch to repair scalar/source/boundary failure")
    print("5. curvature diagnostic/current/balance to rescue boundary behavior")
    print("6. H_curv/H_exch as boundary counterterm or M_ext correction")
    print("7. O to erase boundary/scalar leakage by name")
    print("8. dark label to patch ordinary boundary failure")
    print("9. recovery target to select smoothing/support/boundary data")
    print("10. sharp support to hide shell charge")
    print("11. repair coefficients to be chosen after leakage appears")

    with out.governance_assessments():
        out.line(
            "boundary repair overclaim controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not smuggle repair mechanisms as neutrality theorems",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Boundary/scalar silence cannot be supplied by repair routes.")
    print()
    print("Rejected:")
    print()
    print("  surface counterterms")
    print("  boundary repair currents")
    print("  R_V cancellation")
    print("  J_exch repair")
    print("  curvature boundary rescue")
    print("  H boundary counterterms")
    print("  O boundary eraser")
    print("  dark boundary patch")
    print("  recovery-tuned smoothing")
    print("  sharp support hiding shell charge")
    print()
    print("Allowed only as future positive routes:")
    print()
    print("  derived no-shell matching")
    print("  derived compact support")
    print("  derived neutral transport")
    print("  inert diagnostic boundary audit")
    print()
    print("This script rejects boundary repair.")
    print("It does not prove boundary neutrality.")
    print()
    print("Possible next script:")
    print("  candidate_diagnostic_residual_nonmetric_conditions.py")

    with out.governance_assessments():
        out.line(
            "boundary repair route exclusion complete",
            StatusMark.PASS,
            "repair routes rejected; only diagnostics and future derived no-repair theorems remain",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, exprs: RepairDiagnosticExpression) -> None:
    ns.record_derivation(
        derivation_id="boundary_repair_mass_shift_diagnostic_22",
        inputs=[exprs.q_shell, exprs.q_counter, exprs.q_smoothing],
        output=exprs.mass_shift_from_q,
        method="delta_M_A = -c**2*(q_shell + q_counter + q_smoothing)/(2*G)",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="repair_mass_shift_diagnostic",
        scope="Group 22 boundary repair route exclusion",
    )

    ns.record_derivation(
        derivation_id="boundary_repair_scalar_flux_diagnostic_22",
        inputs=[exprs.C_tail],
        output=exprs.scalar_flux_from_C,
        method="F_scalar = -4*pi*C_tail",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="repair_scalar_flux_diagnostic",
        scope="Group 22 boundary repair route exclusion",
    )

    ns.record_derivation(
        derivation_id="boundary_repair_current_flux_diagnostic_22",
        inputs=[exprs.I_repair],
        output=exprs.current_flux_from_I,
        method="Phi_current = I_repair",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="repair_current_flux_diagnostic",
        scope="Group 22 boundary repair route exclusion",
    )

    ns.record_derivation(
        derivation_id="boundary_repair_route_exclusion_inventory_marker_22",
        inputs=[
            sp.Symbol("surface_counterterm"),
            sp.Symbol("boundary_repair_current"),
            sp.Symbol("R_V_cancellation"),
            sp.Symbol("J_exch_repair"),
            sp.Symbol("curvature_rescue"),
            sp.Symbol("H_counterterm"),
            sp.Symbol("O_boundary_eraser"),
            sp.Symbol("dark_patch"),
        ],
        output=sp.Symbol("boundary_repair_routes_rejected"),
        method="Group 22 boundary repair route exclusion ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="requirements_marker",
        scope="Group 22 boundary neutrality and scalar silence",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        (
            "derive_no_repair_boundary_neutrality_22",
            "Derive boundary neutrality without repair routes",
            "Show boundary neutrality follows without surface counterterms, repair currents, R_V cancellation, H insertion, O erasure, dark patch, or recovery-tuned smoothing.",
        ),
        (
            "derive_repair_independence_before_leakage_22",
            "Derive repair independence before leakage",
            "Any allowed boundary/source/current structure must be derived before, not selected after, a leakage or recovery problem appears.",
        ),
        (
            "derive_no_shell_no_tail_no_current_joint_condition_22",
            "Derive joint no-shell/no-tail/no-current condition",
            "Show no shell source, no residual scalar tail, and no non-A far-zone current flux simultaneously.",
        ),
    ]

    for obligation_id, title, description in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["ordinary_closed_regime_boundary_no_repair_theorem_22"],
            description=description,
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "derive_no_repair_boundary_neutrality_22",
        "derive_repair_independence_before_leakage_22",
        "derive_no_shell_no_tail_no_current_joint_condition_22",
    ]

    ns.record_route(RouteRecord(
        route_id="ordinary_closed_regime_boundary_no_repair_theorem_22",
        script_id=SCRIPT_ID,
        name="Ordinary closed-regime boundary no-repair theorem target",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "boundary neutrality follows without repair routes",
            "no shell source, no scalar tail, and no non-A current flux are shown directly",
            "all boundary structures are derived before recovery checks",
        ],
    ))

    rejected_branch_ids = [
        "surface_counterterm",
        "boundary_repair_current",
        "R_V_boundary_cancellation",
        "J_exch_repair",
        "curvature_boundary_rescue",
        "H_boundary_counterterm",
        "O_boundary_eraser",
        "dark_boundary_patch",
        "recovery_tuned_smoothing",
        "sharp_support_hiding_shell_charge",
    ]

    for branch_id in rejected_branch_ids:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_22",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=(
                f"Reject {branch_id} as a boundary/scalar/current repair route. "
                "Boundary neutrality must be derived without after-the-fact repair mechanisms."
            ),
        ))

    ns.record_claim(ClaimRecord(
        claim_id="boundary_repair_routes_rejected_22",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Boundary/scalar silence cannot be supplied by repair routes: surface counterterms, repair currents, R_V cancellation, "
            "J_exch repair, curvature rescue, H counterterms, O erasure, dark patches, recovery-tuned smoothing, and sharp-support shell hiding remain rejected."
        ),
        derivation_ids=[
            "boundary_repair_mass_shift_diagnostic_22",
            "boundary_repair_scalar_flux_diagnostic_22",
            "boundary_repair_current_flux_diagnostic_22",
            "boundary_repair_route_exclusion_inventory_marker_22",
        ],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Boundary Repair Route Exclusion")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    exprs = build_diagnostics()
    routes = build_repair_routes()
    allowed = build_allowed_nonrepair_entries()

    case_0_problem_statement(out)
    case_1_repair_diagnostics(exprs, out)
    case_2_rejected_repair_ledger(routes, out)
    case_3_allowed_nonrepair_ledger(allowed, out)
    case_4_failure_controls(out)
    final_interpretation(out)

    record_derivations(ns, exprs)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
