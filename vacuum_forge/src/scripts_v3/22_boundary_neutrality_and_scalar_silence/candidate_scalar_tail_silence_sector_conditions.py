# Candidate scalar tail silence sector conditions
#
# Group:
#   22_boundary_neutrality_and_scalar_silence
#
# Script type:
#   REQUIREMENTS / DIAGNOSTIC
#
# Purpose
# -------
# Apply exterior scalar-tail silence conditions to each residual sector.
#
# Locked-door question:
#
#   Which sectors must have vanishing exterior 1/r scalar coefficients?
#
# This script does not prove scalar silence.
# It does not prove compact support.
# It does not derive residual-kill or no-overlap.
# It audits sector coefficients against the reduced flux witness:
#
#   phi_i = C_i/r  ->  F_i = -4*pi*C_i
#
# and records that ordinary-sector residual scalar tails must vanish,
# remain strictly non-metric/diagnostic, or stay theorem-targeted.

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
            "scalar_tail_flux_witness_dependency_22",
            "22_boundary_neutrality_and_scalar_silence__candidate_boundary_scalar_silence_targets",
            "boundary_scalar_silence_scalar_tail_flux_witness_22",
            RecordKind.DERIVATION,
        ),
        (
            "smooth_compact_no_shell_dependency_22",
            "22_boundary_neutrality_and_scalar_silence__candidate_smooth_compact_support_no_shell_conditions",
            "smooth_compact_support_no_shell_inventory_marker_22",
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
class SectorTailExpression:
    sector: str
    coefficient_symbol: sp.Symbol
    tail: sp.Expr
    flux: sp.Expr
    flux_residual: sp.Expr
    neutrality_condition: sp.Equality


@dataclass
class SectorSilenceEntry:
    name: str
    sector: str
    dangerous_tail: str
    required_condition: str
    status: str
    allowed_if: str
    forbidden_if: str
    consequence: str


@dataclass
class RejectedScalarRoute:
    name: str
    route: str
    forbidden_use: str
    status: str
    consequence: str


# =============================================================================
# Builders
# =============================================================================


def build_tail_expressions() -> List[SectorTailExpression]:
    r = sp.Symbol("r", positive=True)
    sector_symbols = [
        ("zeta", sp.Symbol("C_zeta", real=True)),
        ("kappa", sp.Symbol("C_kappa", real=True)),
        ("J_V", sp.Symbol("C_JV", real=True)),
        ("J_sub", sp.Symbol("C_Jsub", real=True)),
        ("J_exch", sp.Symbol("C_Jexch", real=True)),
        ("curvature", sp.Symbol("C_curv", real=True)),
        ("J_curv", sp.Symbol("C_Jcurv", real=True)),
        ("H_trace", sp.Symbol("C_H", real=True)),
        ("boundary_shell", sp.Symbol("C_boundary", real=True)),
        ("dark_label", sp.Symbol("C_dark", real=True)),
    ]

    entries: List[SectorTailExpression] = []
    for sector, coeff in sector_symbols:
        tail = coeff / r
        flux = sp.simplify(4 * sp.pi * r**2 * sp.diff(tail, r))
        entries.append(SectorTailExpression(
            sector=sector,
            coefficient_symbol=coeff,
            tail=tail,
            flux=flux,
            flux_residual=sp.simplify(flux + 4 * sp.pi * coeff),
            neutrality_condition=sp.Eq(coeff, 0),
        ))
    return entries


def build_sector_entries() -> List[SectorSilenceEntry]:
    return [
        SectorSilenceEntry(
            name="T1: zeta residual",
            sector="zeta",
            dangerous_tail="zeta_tail = C_zeta/r",
            required_condition="C_zeta = 0",
            status="REQUIRED",
            allowed_if="zeta is killed, non-metric, compact-neutral, diagnostic, or future theorem-routed without double counting",
            forbidden_if="zeta residual becomes ordinary exterior scalar charge",
            consequence="zeta cannot carry a second mass coin",
        ),
        SectorSilenceEntry(
            name="T2: kappa residual",
            sector="kappa",
            dangerous_tail="kappa_tail = C_kappa/r",
            required_condition="C_kappa = 0",
            status="REQUIRED",
            allowed_if="kappa is suppressed, killed, non-metric, compact-neutral, diagnostic, or future theorem-routed",
            forbidden_if="kappa leak repairs boundary mismatch or acts as scalar mass response",
            consequence="kappa remains diagnostic/suppressed unless derived otherwise",
        ),
        SectorSilenceEntry(
            name="T3: J_V residue",
            sector="J_V",
            dangerous_tail="phi_JV = C_JV/r",
            required_condition="C_JV = 0",
            status="REQUIRED",
            allowed_if="J_V residue vanishes or remains strictly diagnostic/non-metric while J_V is unresolved",
            forbidden_if="undefined J_V leaves hidden scalar charge",
            consequence="J_V cannot carry scalar tail while undefined",
        ),
        SectorSilenceEntry(
            name="T4: J_sub residue",
            sector="J_sub",
            dangerous_tail="phi_Jsub = C_Jsub/r",
            required_condition="C_Jsub = 0",
            status="REQUIRED",
            allowed_if="J_sub remains pure-wind role-level bookkeeping with no scalar trace",
            forbidden_if="pure wind produces scalar mass tail",
            consequence="pure wind is not gravity",
        ),
        SectorSilenceEntry(
            name="T5: J_exch residue",
            sector="J_exch",
            dangerous_tail="phi_Jexch = C_Jexch/r",
            required_condition="C_Jexch = 0",
            status="REQUIRED",
            allowed_if="exchange remains role-level or future theorem derives neutral source/support behavior",
            forbidden_if="exchange residue repairs ordinary scalar leakage",
            consequence="exchange is not scalar-tail repair",
        ),
        SectorSilenceEntry(
            name="T6: A_curv/e_curv residue",
            sector="curvature",
            dangerous_tail="phi_curv = C_curv/r",
            required_condition="C_curv = 0",
            status="REQUIRED",
            allowed_if="curvature remains diagnostic/accounting/branch-filter or future source-neutral dynamics derives silence",
            forbidden_if="curvature diagnostic becomes exterior scalar charge",
            consequence="curvature accounting is not mass energy",
        ),
        SectorSilenceEntry(
            name="T7: J_curv residue",
            sector="J_curv",
            dangerous_tail="phi_Jcurv = C_Jcurv/r",
            required_condition="C_Jcurv = 0",
            status="REQUIRED",
            allowed_if="J_curv remains undefined/theorem-targeted or future curvature-current theorem proves scalar silence",
            forbidden_if="curvature current leaves scalar residue by repair",
            consequence="J_curv cannot rescue boundary or scalar leakage",
        ),
        SectorSilenceEntry(
            name="T8: H trace leakage",
            sector="H_trace",
            dangerous_tail="phi_H = C_H/r",
            required_condition="C_H = 0",
            status="REQUIRED",
            allowed_if="H remains non-inserted diagnostic label or future tensor theorem proves trace neutrality",
            forbidden_if="H trace cancels or modifies exterior scalar mass",
            consequence="H_curv/H_exch remain non-insertable",
        ),
        SectorSilenceEntry(
            name="T9: boundary shell residue",
            sector="boundary_shell",
            dangerous_tail="phi_boundary = C_boundary/r",
            required_condition="C_boundary = 0",
            status="REQUIRED",
            allowed_if="no-shell matching and compact support are derived structurally",
            forbidden_if="boundary shell or smoothing layer leaves scalar tail",
            consequence="boundary purse remains closed",
        ),
        SectorSilenceEntry(
            name="T10: dark label residue",
            sector="dark_label",
            dangerous_tail="phi_dark = C_dark/r",
            required_condition="C_dark = 0 in ordinary-sector audit",
            status="REQUIRED",
            allowed_if="dark labels remain optional downstream and do not patch ordinary boundary/scalar failure",
            forbidden_if="dark label absorbs ordinary scalar leakage",
            consequence="dark sector is not an ordinary scalar-silence patch",
        ),
    ]


def build_rejected_routes() -> List[RejectedScalarRoute]:
    return [
        RejectedScalarRoute(
            name="R1: scalar silence by cancellation",
            route="sum_C_i_equals_zero",
            forbidden_use="sector tails cancel in the total while individual pockets remain nonzero",
            status="REJECTED",
            consequence="cancellation is not sector silence",
        ),
        RejectedScalarRoute(
            name="R2: O erases sector tails",
            route="O_tail_erasure",
            forbidden_use="projection label kills scalar coefficients without domain/kernel/image/boundary law",
            status="REJECTED",
            consequence="O remains theorem-targeted and cannot erase tails by name",
        ),
        RejectedScalarRoute(
            name="R3: H cancels sector tails",
            route="H_trace_tail_cancellation",
            forbidden_use="correction tensor trace cancels zeta/kappa/J/current/curvature tails",
            status="REJECTED",
            consequence="H remains non-insertable",
        ),
        RejectedScalarRoute(
            name="R4: boundary shell absorbs tail",
            route="boundary_shell_absorbs_tail",
            forbidden_use="shell source or smoothing layer removes exterior scalar leakage by repair",
            status="REJECTED",
            consequence="no-shell condition must be derived before boundary neutrality can be claimed",
        ),
        RejectedScalarRoute(
            name="R5: recovery-selected scalar silence",
            route="recovery_selected_zero_coefficients",
            forbidden_use="coefficients set to zero because Schwarzschild/PPN/gamma_like/AB recovery needs them zero",
            status="REJECTED",
            consequence="recovery may test scalar silence but cannot construct it",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Scalar tail silence sector problem")
    print("Question:")
    print()
    print("  Which sectors must have vanishing exterior 1/r scalar coefficients?")
    print()
    print("Reference discipline:")
    print()
    print("  Group 22 target ledger requires residual scalar silence.")
    print("  Smooth compact support remains theorem-targeted.")
    print("  A scalar tail C_i/r carries F_i = -4*pi*C_i.")
    print("  Sector-by-sector silence is required; cancellation ledgers do not count.")
    print("  This script audits sector coefficients but does not prove they vanish.")

    with out.governance_assessments():
        out.line(
            "scalar tail sector audit opened",
            StatusMark.INFO,
            "applying the 1/r flux witness sector by sector",
        )


def case_1_sector_flux_table(tails: List[SectorTailExpression], out: ScriptOutput) -> None:
    header("Case 1: Sector 1/r tail flux table")
    for entry in tails:
        print()
        print("-" * 120)
        print(entry.sector)
        print("-" * 120)
        print(f"Tail: {sp.sstr(entry.tail)}")
        print(f"Flux: {sp.sstr(entry.flux)}")
        print(f"Residual flux + 4*pi*C: {sp.sstr(entry.flux_residual)}")
        print(f"Neutrality condition: {entry.neutrality_condition}")

    all_residuals_zero = all(is_zero(entry.flux_residual) for entry in tails)

    with out.derived_results():
        out.line(
            "sector scalar-tail flux table derived",
            StatusMark.PASS if all_residuals_zero else StatusMark.FAIL,
            f"{len(tails)} sector tails reduce to F_i = -4*pi*C_i",
        )


def case_2_sector_condition_ledger(entries: List[SectorSilenceEntry], out: ScriptOutput) -> None:
    header("Case 2: Sector scalar-silence condition ledger")
    for entry in entries:
        print()
        print("-" * 120)
        print(entry.name)
        print("-" * 120)
        print(f"Sector: {entry.sector}")
        print(f"Dangerous tail: {entry.dangerous_tail}")
        print(f"Required condition: {entry.required_condition}")
        print(f"[{status_mark(entry.status).value}] {entry.name}: {entry.status}")
        print(f"Allowed if: {entry.allowed_if}")
        print(f"Forbidden if: {entry.forbidden_if}")
        print(f"Consequence: {entry.consequence}")

    with out.governance_assessments():
        out.line(
            "sector scalar-silence ledger populated",
            StatusMark.PASS,
            f"{len(entries)} sector coefficients audited for exterior scalar silence",
        )


def case_3_total_cancellation_warning(tails: List[SectorTailExpression], out: ScriptOutput) -> None:
    header("Case 3: Total-tail cancellation warning")
    total_coeff = sp.simplify(sum(entry.coefficient_symbol for entry in tails))
    total_flux = sp.simplify(sum(entry.flux for entry in tails))
    residual = sp.simplify(total_flux + 4 * sp.pi * total_coeff)

    print("If all sector tails are summed:")
    print()
    print(f"  C_total = {sp.sstr(total_coeff)}")
    print(f"  F_total = {sp.sstr(total_flux)}")
    print(f"  residual F_total + 4*pi*C_total = {sp.sstr(residual)}")
    print()
    print("A total cancellation condition would be:")
    print()
    print(f"  {sp.Eq(total_coeff, 0)}")
    print()
    print("But this is not sector silence.")
    print("Group 22 requires each ordinary-sector pocket to be empty, non-metric/diagnostic, compact-neutral, or theorem-routed.")

    with out.counterexamples():
        out.line(
            "total scalar-tail cancellation rejected",
            StatusMark.FAIL,
            "sum(C_i)=0 is not the same as C_i=0 sector by sector",
        )


def case_4_rejected_routes(routes: List[RejectedScalarRoute], out: ScriptOutput) -> None:
    header("Case 4: Rejected scalar-tail silence shortcuts")
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
            "scalar-tail silence shortcuts rejected",
            StatusMark.FAIL,
            "cancellation, O erasure, H cancellation, boundary shell absorption, and recovery-selected silence are not licensed",
        )


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("The scalar-tail sector audit fails if a later script allows:")
    print()
    print("1. any ordinary-sector residual C_i/r tail with C_i != 0")
    print("2. total cancellation sum(C_i)=0 to replace sector silence")
    print("3. O to erase sector tails without a real operator")
    print("4. H trace to cancel scalar tails")
    print("5. boundary shell or smoothing layer to absorb scalar leakage")
    print("6. dark label to patch ordinary scalar failure")
    print("7. recovery target to set tail coefficients")
    print("8. compact support without matching/no-shell law")
    print("9. diagnostic residuals to re-enter metric/source/boundary routing later")

    with out.governance_assessments():
        out.line(
            "scalar-tail sector overclaim controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not treat coefficient targets as solved silence",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("The sector rule is simple:")
    print()
    print("  phi_i = C_i/r")
    print("  F_i = -4*pi*C_i")
    print()
    print("Therefore ordinary exterior scalar silence requires each sector coefficient to vanish:")
    print()
    print("  C_zeta = C_kappa = C_JV = C_Jsub = C_Jexch = 0")
    print("  C_curv = C_Jcurv = C_H = C_boundary = C_dark = 0")
    print()
    print("unless the sector is strictly non-metric/diagnostic, killed/suppressed,")
    print("compact-neutral with derived matching/no-shell conditions,")
    print("or future theorem-routed without double counting.")
    print()
    print("This script does not prove silence.")
    print("It records the sector-by-sector coefficient burden.")
    print()
    print("Possible next script:")
    print("  candidate_boundary_current_flux_silence.py")

    with out.governance_assessments():
        out.line(
            "scalar-tail sector audit complete",
            StatusMark.PASS,
            "sector coefficients must vanish or remain non-metric/diagnostic/theorem-targeted",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, tails: List[SectorTailExpression]) -> None:
    for entry in tails:
        safe_sector = entry.sector.replace("/", "_").replace(" ", "_")
        ns.record_derivation(
            derivation_id=f"{safe_sector}_scalar_tail_flux_22",
            inputs=[entry.tail, entry.coefficient_symbol],
            output=entry.flux,
            method=f"simplify(4*pi*r**2*diff({sp.sstr(entry.tail)}, r))",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="surface_flux_witness",
            scope=f"Group 22 scalar-tail silence audit: {entry.sector}",
        )

    ns.record_derivation(
        derivation_id="scalar_tail_silence_sector_inventory_marker_22",
        inputs=[entry.coefficient_symbol for entry in tails],
        output=sp.Symbol("scalar_tail_sector_silence_conditions_stated"),
        method="Group 22 sector scalar-tail silence requirements ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="requirements_marker",
        scope="Group 22 boundary neutrality and scalar silence",
        is_placeholder=True,
    )


def record_obligations(ns, entries: List[SectorSilenceEntry]) -> None:
    for entry in entries:
        safe_name = entry.name.split(":", 1)[0].replace("-", "_").replace(" ", "_").lower()
        ns.record_obligation(ProofObligationRecord(
            obligation_id=f"derive_{safe_name}_scalar_silence_22",
            script_id=SCRIPT_ID,
            title=f"Derive scalar silence for {entry.sector}",
            status=ObligationStatus.OPEN,
            required_by=["ordinary_closed_regime_sector_scalar_silence_theorem_22"],
            description=(
                f"Show {entry.required_condition} or prove that {entry.sector} remains strictly non-metric/diagnostic, "
                f"compact-neutral with matching/no-shell conditions, or future theorem-routed without double counting. "
                f"Forbidden: {entry.forbidden_if}."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "derive_t1_scalar_silence_22",
        "derive_t2_scalar_silence_22",
        "derive_t3_scalar_silence_22",
        "derive_t4_scalar_silence_22",
        "derive_t5_scalar_silence_22",
        "derive_t6_scalar_silence_22",
        "derive_t7_scalar_silence_22",
        "derive_t8_scalar_silence_22",
        "derive_t9_scalar_silence_22",
        "derive_t10_scalar_silence_22",
    ]

    ns.record_route(RouteRecord(
        route_id="ordinary_closed_regime_sector_scalar_silence_theorem_22",
        script_id=SCRIPT_ID,
        name="Ordinary closed-regime sector scalar silence theorem target",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "each ordinary residual exterior 1/r coefficient vanishes",
            "or each residual is strictly non-metric/diagnostic",
            "or compact-neutral matching/no-shell conditions are derived",
            "or a future parent theorem routes the sector without double counting",
        ],
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_scalar_tail_silence_by_total_cancellation_22",
        script_id=SCRIPT_ID,
        branch_id="scalar_tail_total_cancellation",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=obligation_ids,
        description=(
            "Reject total scalar-tail cancellation as a substitute for sector scalar silence. "
            "Each ordinary-sector residual pocket must vanish or be made non-metric/diagnostic/theorem-routed."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="sector_scalar_tail_coefficients_must_vanish_22",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "For ordinary exterior scalar silence, sector residual tails C_i/r carry F_i = -4*pi*C_i. "
            "Thus each ordinary-sector coefficient must vanish, or the sector must remain strictly non-metric/diagnostic, "
            "compact-neutral, or future theorem-routed without double counting."
        ),
        derivation_ids=[
            "zeta_scalar_tail_flux_22",
            "kappa_scalar_tail_flux_22",
            "J_V_scalar_tail_flux_22",
            "J_sub_scalar_tail_flux_22",
            "J_exch_scalar_tail_flux_22",
            "curvature_scalar_tail_flux_22",
            "J_curv_scalar_tail_flux_22",
            "H_trace_scalar_tail_flux_22",
            "boundary_shell_scalar_tail_flux_22",
            "dark_label_scalar_tail_flux_22",
            "scalar_tail_silence_sector_inventory_marker_22",
        ],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Scalar Tail Silence Sector Conditions")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    tails = build_tail_expressions()
    entries = build_sector_entries()
    routes = build_rejected_routes()

    case_0_problem_statement(out)
    case_1_sector_flux_table(tails, out)
    case_2_sector_condition_ledger(entries, out)
    case_3_total_cancellation_warning(tails, out)
    case_4_rejected_routes(routes, out)
    case_5_failure_controls(out)
    final_interpretation(out)

    record_derivations(ns, tails)
    record_obligations(ns, entries)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
