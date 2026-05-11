# Candidate boundary current flux silence
#
# Group:
#   22_boundary_neutrality_and_scalar_silence
#
# Script type:
#   REQUIREMENTS / DIAGNOSTIC
#
# Purpose
# -------
# Audit whether non-A boundary or far-zone currents can remain silent.
#
# Locked-door question:
#
#   Can non-A boundary or far-zone currents remain silent?
#
# This script does not define J_V, J_sub, J_exch, J_curv, or H flux.
# It does not prove current neutrality.
# It does not derive neutral transport.
#
# It audits generic radial current profiles:
#
#   j^r = I/(4*pi*r^2)
#
# whose sphere flux is:
#
#   Phi = I
#
# Silence requires I = 0 unless a future theorem derives a neutral
# transport interpretation with no scalar, boundary, source, or mass effect.

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
            "22_boundary_neutrality_and_scalar_silence__candidate_boundary_scalar_silence_targets",
            "boundary_scalar_silence_target_ledger_marker_22",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "sector_scalar_silence_dependency_22",
            "22_boundary_neutrality_and_scalar_silence__candidate_scalar_tail_silence_sector_conditions",
            "scalar_tail_silence_sector_inventory_marker_22",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "far_zone_current_flux_witness_dependency_22",
            "22_boundary_neutrality_and_scalar_silence__candidate_boundary_scalar_silence_targets",
            "boundary_scalar_silence_far_zone_current_flux_witness_22",
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
class CurrentFluxExpression:
    sector: str
    coefficient_symbol: sp.Symbol
    current_profile: sp.Expr
    sphere_flux: sp.Expr
    flux_residual: sp.Expr
    neutrality_condition: sp.Equality


@dataclass
class CurrentFluxLedgerEntry:
    name: str
    sector: str
    current_profile: str
    required_condition: str
    status: str
    allowed_if: str
    forbidden_if: str
    consequence: str


@dataclass
class CurrentRepairRoute:
    name: str
    route: str
    forbidden_use: str
    status: str
    consequence: str


# =============================================================================
# Builders
# =============================================================================


def build_current_fluxes() -> List[CurrentFluxExpression]:
    r = sp.Symbol("r", positive=True)
    sector_symbols = [
        ("J_V", sp.Symbol("I_V", real=True)),
        ("J_sub", sp.Symbol("I_sub", real=True)),
        ("J_exch", sp.Symbol("I_exch", real=True)),
        ("J_curv", sp.Symbol("I_curv", real=True)),
        ("H_flux", sp.Symbol("I_H", real=True)),
        ("boundary_current", sp.Symbol("I_boundary", real=True)),
        ("dark_current", sp.Symbol("I_dark", real=True)),
    ]

    entries: List[CurrentFluxExpression] = []
    for sector, coeff in sector_symbols:
        profile = coeff / (4 * sp.pi * r**2)
        sphere_flux = sp.simplify(4 * sp.pi * r**2 * profile)
        entries.append(CurrentFluxExpression(
            sector=sector,
            coefficient_symbol=coeff,
            current_profile=profile,
            sphere_flux=sphere_flux,
            flux_residual=sp.simplify(sphere_flux - coeff),
            neutrality_condition=sp.Eq(coeff, 0),
        ))
    return entries


def build_ledger() -> List[CurrentFluxLedgerEntry]:
    return [
        CurrentFluxLedgerEntry(
            name="CF1: J_V far-zone flux",
            sector="J_V",
            current_profile="j_V^r = I_V/(4*pi*r^2)",
            required_condition="I_V = 0",
            status="REQUIRED",
            allowed_if="J_V remains unresolved/diagnostic or future theorem derives neutral transport with no mass/scalar/boundary effect",
            forbidden_if="undefined J_V leaves far-zone current flux",
            consequence="J_V cannot be a second flux coin while undefined",
        ),
        CurrentFluxLedgerEntry(
            name="CF2: J_sub pure-wind flux",
            sector="J_sub",
            current_profile="j_sub^r = I_sub/(4*pi*r^2)",
            required_condition="I_sub = 0 in ordinary exterior unless pure-wind neutrality is derived",
            status="REQUIRED",
            allowed_if="pure wind is proven neutral: no M_ext shift, no scalar trace, no matter push, no boundary repair",
            forbidden_if="pure wind gravitates or creates preferred-frame force by existence",
            consequence="pure wind is not gravity",
        ),
        CurrentFluxLedgerEntry(
            name="CF3: J_exch exchange flux",
            sector="J_exch",
            current_profile="j_exch^r = I_exch/(4*pi*r^2)",
            required_condition="I_exch = 0 in ordinary exterior unless exchange source/support law derives neutral behavior",
            status="REQUIRED",
            allowed_if="exchange remains role-level, zero-net, zero-creation, latent, or theorem-routed with no ordinary mass effect",
            forbidden_if="exchange repairs boundary, scalar-tail, source-routing, or recovery failure",
            consequence="exchange is not repair",
        ),
        CurrentFluxLedgerEntry(
            name="CF4: J_curv curvature-current flux",
            sector="J_curv",
            current_profile="j_curv^r = I_curv/(4*pi*r^2)",
            required_condition="I_curv = 0 unless curvature-current law is derived",
            status="REQUIRED",
            allowed_if="J_curv remains unresolved or future theorem derives orientation/source/boundary/mass neutrality",
            forbidden_if="curvature current is chosen by fiat to cancel boundary or singularity problems",
            consequence="J_curv cannot be curvature repair flux",
        ),
        CurrentFluxLedgerEntry(
            name="CF5: H correction flux",
            sector="H_flux",
            current_profile="j_H^r = I_H/(4*pi*r^2)",
            required_condition="I_H = 0 before any H insertion",
            status="REQUIRED",
            allowed_if="H remains diagnostic-only or future tensor theorem proves divergence/source/boundary/mass neutrality",
            forbidden_if="H flux acts as boundary counterterm, scalar-tail cancellation, or M_ext correction",
            consequence="H_curv/H_exch remain non-insertable",
        ),
        CurrentFluxLedgerEntry(
            name="CF6: boundary repair current",
            sector="boundary_current",
            current_profile="j_boundary^r = I_boundary/(4*pi*r^2)",
            required_condition="I_boundary = 0",
            status="REQUIRED",
            allowed_if="boundary behavior is no-shell, smooth-matched, and source-neutral before recovery",
            forbidden_if="boundary current is introduced after leakage appears",
            consequence="boundary purse remains closed",
        ),
        CurrentFluxLedgerEntry(
            name="CF7: dark current patch",
            sector="dark_current",
            current_profile="j_dark^r = I_dark/(4*pi*r^2)",
            required_condition="I_dark = 0 in ordinary-sector audit",
            status="REQUIRED",
            allowed_if="dark coupling is derived downstream and not used to patch ordinary failure",
            forbidden_if="dark current absorbs ordinary boundary/scalar/source leakage",
            consequence="dark sector is not an ordinary flux patch",
        ),
    ]


def build_rejected_routes() -> List[CurrentRepairRoute]:
    return [
        CurrentRepairRoute(
            name="R1: far-zone current as mass flux",
            route="non_A_far_zone_current_mass_flux",
            forbidden_use="nonzero non-A sphere flux counted as ordinary exterior mass or scalar silence",
            status="REJECTED",
            consequence="non-A far-zone current flux must vanish or be future theorem-routed",
        ),
        CurrentRepairRoute(
            name="R2: boundary repair current",
            route="boundary_repair_current",
            forbidden_use="current introduced to cancel boundary flux after leakage appears",
            status="REJECTED",
            consequence="repair current is not boundary neutrality",
        ),
        CurrentRepairRoute(
            name="R3: exchange repair flux",
            route="exchange_repair_flux",
            forbidden_use="J_exch or Sigma/R roles tuned to cancel scalar, source, or boundary mismatch",
            status="REJECTED",
            consequence="exchange needs operators, not repair knobs",
        ),
        CurrentRepairRoute(
            name="R4: curvature rescue flux",
            route="curvature_rescue_flux",
            forbidden_use="J_curv direction/sign/flux chosen to fix curvature, boundary, or singularity problem",
            status="REJECTED",
            consequence="curvature current remains undefined",
        ),
        CurrentRepairRoute(
            name="R5: H flux insertion",
            route="H_flux_insertion",
            forbidden_use="H flux inserted as divergence safety, boundary counterterm, or M_ext correction",
            status="REJECTED",
            consequence="H remains non-insertable",
        ),
        CurrentRepairRoute(
            name="R6: recovery-selected current flux",
            route="recovery_selected_current_flux",
            forbidden_use="current coefficient set by Schwarzschild/PPN/gamma_like/AB recovery",
            status="REJECTED",
            consequence="recovery may audit current behavior but cannot construct it",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Boundary/current flux silence problem")
    print("Question:")
    print()
    print("  Can non-A boundary or far-zone currents remain silent?")
    print()
    print("Reference discipline:")
    print()
    print("  Group 22 requires far-zone non-A current silence.")
    print("  A generic radial current j^r = I/(4*pi*r^2) carries sphere flux I.")
    print("  Current neutrality is not derived by naming J_V, J_sub, J_exch, J_curv, or H.")
    print("  Non-A currents must not repair boundaries, scalar tails, source routing, or recovery failure.")

    with out.governance_assessments():
        out.line(
            "boundary/current flux silence audit opened",
            StatusMark.INFO,
            "testing non-A far-zone radial current flux coefficients",
        )


def case_1_current_flux_table(fluxes: List[CurrentFluxExpression], out: ScriptOutput) -> None:
    header("Case 1: Non-A current flux table")
    for entry in fluxes:
        print()
        print("-" * 120)
        print(entry.sector)
        print("-" * 120)
        print(f"Current profile: {sp.sstr(entry.current_profile)}")
        print(f"Sphere flux: {sp.sstr(entry.sphere_flux)}")
        print(f"Residual Phi - I: {sp.sstr(entry.flux_residual)}")
        print(f"Neutrality condition: {entry.neutrality_condition}")

    all_residuals_zero = all(is_zero(entry.flux_residual) for entry in fluxes)

    with out.derived_results():
        out.line(
            "non-A current flux table derived",
            StatusMark.PASS if all_residuals_zero else StatusMark.FAIL,
            f"{len(fluxes)} current profiles reduce to sphere flux I",
        )


def case_2_current_condition_ledger(entries: List[CurrentFluxLedgerEntry], out: ScriptOutput) -> None:
    header("Case 2: Current flux silence condition ledger")
    for entry in entries:
        print()
        print("-" * 120)
        print(entry.name)
        print("-" * 120)
        print(f"Sector: {entry.sector}")
        print(f"Current profile: {entry.current_profile}")
        print(f"Required condition: {entry.required_condition}")
        print(f"[{status_mark(entry.status).value}] {entry.name}: {entry.status}")
        print(f"Allowed if: {entry.allowed_if}")
        print(f"Forbidden if: {entry.forbidden_if}")
        print(f"Consequence: {entry.consequence}")

    with out.governance_assessments():
        out.line(
            "current flux silence ledger populated",
            StatusMark.PASS,
            f"{len(entries)} non-A current flux routes audited",
        )


def case_3_total_flux_cancellation_warning(fluxes: List[CurrentFluxExpression], out: ScriptOutput) -> None:
    header("Case 3: Total current-flux cancellation warning")
    total_I = sp.simplify(sum(entry.coefficient_symbol for entry in fluxes))
    total_flux = sp.simplify(sum(entry.sphere_flux for entry in fluxes))
    residual = sp.simplify(total_flux - total_I)

    print("If all non-A current fluxes are summed:")
    print()
    print(f"  I_total = {sp.sstr(total_I)}")
    print(f"  Phi_total = {sp.sstr(total_flux)}")
    print(f"  residual Phi_total - I_total = {sp.sstr(residual)}")
    print()
    print("A total cancellation condition would be:")
    print()
    print(f"  {sp.Eq(total_I, 0)}")
    print()
    print("But this is not sector current silence.")
    print("Each ordinary-sector non-A current route must be zero, diagnostic/role-level, or future theorem-routed.")

    with out.counterexamples():
        out.line(
            "total current-flux cancellation rejected",
            StatusMark.FAIL,
            "sum(I_i)=0 is not the same as I_i=0 sector by sector",
        )


def case_4_rejected_routes(routes: List[CurrentRepairRoute], out: ScriptOutput) -> None:
    header("Case 4: Rejected current-flux repair routes")
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
            "current-flux repair routes rejected",
            StatusMark.FAIL,
            "far-zone mass flux, boundary repair current, exchange repair, curvature rescue, H flux insertion, and recovery-selected current are not licensed",
        )


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("The boundary/current flux silence audit fails if a later script allows:")
    print()
    print("1. nonzero non-A far-zone current flux in ordinary exterior")
    print("2. total current cancellation sum(I_i)=0 to replace sector silence")
    print("3. J_V flux while J_V remains undefined")
    print("4. J_sub pure wind to gravitate by existence")
    print("5. J_exch to repair scalar tails, boundaries, or source routing")
    print("6. J_curv to act as curvature rescue flux")
    print("7. H flux to act as boundary counterterm or M_ext correction")
    print("8. boundary current introduced after leakage appears")
    print("9. dark current to patch ordinary failure")
    print("10. recovery target to choose current coefficients or directions")

    with out.governance_assessments():
        out.line(
            "boundary/current flux overclaim controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not treat current-flux targets as neutral transport theorems",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("The current-flux witness is:")
    print()
    print("  j_i^r = I_i/(4*pi*r^2)")
    print("  Phi_i = I_i")
    print()
    print("Therefore ordinary exterior current silence requires:")
    print()
    print("  I_V = I_sub = I_exch = I_curv = I_H = I_boundary = I_dark = 0")
    print()
    print("unless the current is strictly diagnostic/role-level,")
    print("or a future theorem derives neutral transport with no mass, scalar, boundary, source, or recovery effect.")
    print()
    print("This script does not define current laws.")
    print("It records the far-zone and boundary current flux burden.")
    print()
    print("Possible next script:")
    print("  candidate_boundary_repair_route_exclusion.py")

    with out.governance_assessments():
        out.line(
            "boundary/current flux silence audit complete",
            StatusMark.PASS,
            "non-A current flux coefficients must vanish or remain diagnostic/role-level/theorem-targeted",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, fluxes: List[CurrentFluxExpression]) -> None:
    for entry in fluxes:
        safe_sector = entry.sector.replace("/", "_").replace(" ", "_")
        ns.record_derivation(
            derivation_id=f"{safe_sector}_far_zone_current_flux_22",
            inputs=[entry.current_profile, entry.coefficient_symbol],
            output=entry.sphere_flux,
            method=f"simplify(4*pi*r**2*({sp.sstr(entry.current_profile)}))",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="current_flux_witness",
            scope=f"Group 22 boundary/current flux silence audit: {entry.sector}",
        )

    ns.record_derivation(
        derivation_id="boundary_current_flux_silence_inventory_marker_22",
        inputs=[entry.coefficient_symbol for entry in fluxes],
        output=sp.Symbol("boundary_current_flux_silence_conditions_stated"),
        method="Group 22 boundary/current flux silence requirements ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="requirements_marker",
        scope="Group 22 boundary neutrality and scalar silence",
        is_placeholder=True,
    )


def record_obligations(ns, entries: List[CurrentFluxLedgerEntry]) -> None:
    for entry in entries:
        safe_name = entry.name.split(":", 1)[0].replace("-", "_").replace(" ", "_").lower()
        ns.record_obligation(ProofObligationRecord(
            obligation_id=f"derive_{safe_name}_current_flux_silence_22",
            script_id=SCRIPT_ID,
            title=f"Derive current flux silence for {entry.sector}",
            status=ObligationStatus.OPEN,
            required_by=["ordinary_closed_regime_boundary_current_flux_silence_theorem_22"],
            description=(
                f"Show {entry.required_condition}, or prove neutral transport for {entry.sector} with no ordinary mass, scalar, "
                f"boundary, source-routing, or recovery effect. Forbidden: {entry.forbidden_if}."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "derive_cf1_current_flux_silence_22",
        "derive_cf2_current_flux_silence_22",
        "derive_cf3_current_flux_silence_22",
        "derive_cf4_current_flux_silence_22",
        "derive_cf5_current_flux_silence_22",
        "derive_cf6_current_flux_silence_22",
        "derive_cf7_current_flux_silence_22",
    ]

    ns.record_route(RouteRecord(
        route_id="ordinary_closed_regime_boundary_current_flux_silence_theorem_22",
        script_id=SCRIPT_ID,
        name="Ordinary closed-regime boundary/current flux silence theorem target",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "each ordinary non-A far-zone current coefficient vanishes",
            "or each current remains strictly diagnostic/role-level",
            "or a future transport theorem derives no mass, scalar, boundary, source-routing, or recovery effect",
        ],
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_current_flux_silence_by_total_cancellation_22",
        script_id=SCRIPT_ID,
        branch_id="current_flux_total_cancellation",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=obligation_ids,
        description=(
            "Reject total current-flux cancellation as a substitute for sector current silence. "
            "Each ordinary-sector non-A current coefficient must vanish or be theorem-routed as neutral transport."
        ),
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_boundary_current_repair_22",
        script_id=SCRIPT_ID,
        branch_id="boundary_current_repair",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=obligation_ids,
        description=(
            "Reject boundary repair current. A current introduced after leakage appears is not boundary neutrality."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="boundary_current_flux_coefficients_must_vanish_22",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "For ordinary exterior boundary/current flux silence, non-A far-zone radial currents I_i/(4*pi*r^2) carry sphere flux I_i. "
            "Each coefficient must vanish, or the current must remain diagnostic/role-level or future theorem-routed as neutral transport."
        ),
        derivation_ids=[
            "J_V_far_zone_current_flux_22",
            "J_sub_far_zone_current_flux_22",
            "J_exch_far_zone_current_flux_22",
            "J_curv_far_zone_current_flux_22",
            "H_flux_far_zone_current_flux_22",
            "boundary_current_far_zone_current_flux_22",
            "dark_current_far_zone_current_flux_22",
            "boundary_current_flux_silence_inventory_marker_22",
        ],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Boundary Current Flux Silence")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    fluxes = build_current_fluxes()
    entries = build_ledger()
    routes = build_rejected_routes()

    case_0_problem_statement(out)
    case_1_current_flux_table(fluxes, out)
    case_2_current_condition_ledger(entries, out)
    case_3_total_flux_cancellation_warning(fluxes, out)
    case_4_rejected_routes(routes, out)
    case_5_failure_controls(out)
    final_interpretation(out)

    record_derivations(ns, fluxes)
    record_obligations(ns, entries)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
