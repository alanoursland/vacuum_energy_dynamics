# Candidate source routing no double counting
#
# Group:
#   21_source_routing_and_mass_neutrality
#
# Script type:
#   DIAGNOSTIC / REQUIREMENTS
#
# Purpose
# -------
# Consolidate ordinary source-routing rules after the Group 21 mass-neutrality
# audits. The goal is to protect the A-sector ordinary mass charge from being
# duplicated by residual trace variables, curvature accounting, vacuum-current
# roles, correction tensor labels, dark labels, or diagnostic energy terms.
#
# Locked-door question:
#
#   Can ordinary matter be routed without being counted multiple times?
#
# This script does not derive a parent source law, a stress-energy coupling,
# a pressure law, a current law, a tensor equation, or a source projector.
#
# It records reduced diagnostics for source double-counting danger:
#
#   duplicate scalar tail: C_dup/r -> F_dup = -4*pi*C_dup
#   duplicate A-tail:      q_dup/r -> delta_M_A = -c^2*q_dup/(2G)
#   extra source ledger:   total_source - rho_A = sum(non-A source labels)
#
# The conclusion is deliberately narrow: ordinary rho / M_enc remains routed
# through the A-sector reference charge unless a future parent theorem derives
# otherwise.

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


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    ns.declare_dependency(
        dependency_id="correction_tensor_guard_dependency_21",
        upstream_script_id="21_source_routing_and_mass_neutrality__candidate_correction_tensor_mass_neutrality_guard",
        upstream_derivation_id="correction_tensor_mass_neutrality_guard_marker_21",
        expected_record_kind=RecordKind.INVENTORY_MARKER,
    )
    ns.declare_dependency(
        dependency_id="H_scalar_trace_leakage_dependency_21",
        upstream_script_id="21_source_routing_and_mass_neutrality__candidate_correction_tensor_mass_neutrality_guard",
        upstream_derivation_id="H_scalar_trace_leakage_flux_21",
        expected_record_kind=RecordKind.DERIVATION,
    )
    ns.declare_dependency(
        dependency_id="A_sector_mass_definition_dependency_21",
        upstream_script_id="21_source_routing_and_mass_neutrality__candidate_A_sector_mass_charge_definition",
        upstream_derivation_id="A_sector_mass_definition_21",
        expected_record_kind=RecordKind.DERIVATION,
    )

    return archive, ns, invalidated


def entry_status_mark(status: str) -> StatusMark:
    return {
        "ACCOUNTING_ONLY": StatusMark.INFO,
        "CANDIDATE": StatusMark.INFO,
        "DEFER": StatusMark.DEFER,
        "DIAGNOSTIC_ONLY": StatusMark.INFO,
        "PROTECTED": StatusMark.PASS,
        "PROVISIONAL": StatusMark.INFO,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "RISK": StatusMark.WARN,
        "ROLE_LEVEL": StatusMark.INFO,
        "SAFE_IF": StatusMark.INFO,
        "THEOREM_TARGET": StatusMark.DEFER,
        "UNRESOLVED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


# =============================================================================
# Data models
# =============================================================================


@dataclass
class SourceRoutingExpressionSet:
    r: sp.Symbol
    G: sp.Symbol
    c: sp.Symbol
    C_dup: sp.Symbol
    q_dup: sp.Symbol
    rho_A: sp.Symbol
    rho_kappa: sp.Symbol
    rho_zeta: sp.Symbol
    rho_curv: sp.Symbol
    rho_H: sp.Symbol
    rho_exch: sp.Symbol
    rho_dark: sp.Symbol
    E_accounting: sp.Symbol
    phi_dup: sp.Expr
    F_dup: sp.Expr
    F_dup_residual: sp.Expr
    delta_M_dup_like: sp.Expr
    delta_M_dup_like_residual: sp.Expr
    delta_A_dup: sp.Expr
    delta_F_A_dup: sp.Expr
    delta_F_A_dup_residual: sp.Expr
    delta_M_A_dup: sp.Expr
    delta_M_A_dup_residual: sp.Expr
    total_source_load: sp.Expr
    extra_source_load: sp.Expr
    extra_source_load_residual: sp.Expr
    cancellation_condition: sp.Eq


@dataclass
class RoutingLedgerEntry:
    name: str
    route: str
    allowed_condition: str
    forbidden_condition: str
    status: str
    consequence: str
    obligation_id: str | None = None


@dataclass
class RejectedRoutingRoute:
    name: str
    route: str
    forbidden_use: str
    consequence: str
    obligation_id: str | None = None


# =============================================================================
# Builders
# =============================================================================


def build_expressions() -> SourceRoutingExpressionSet:
    r = sp.Symbol("r", positive=True)
    G = sp.Symbol("G", positive=True)
    c = sp.Symbol("c", positive=True)
    C_dup = sp.Symbol("C_dup", real=True)
    q_dup = sp.Symbol("q_dup", real=True)

    rho_A = sp.Symbol("rho_A", real=True)
    rho_kappa = sp.Symbol("rho_kappa", real=True)
    rho_zeta = sp.Symbol("rho_zeta", real=True)
    rho_curv = sp.Symbol("rho_curv", real=True)
    rho_H = sp.Symbol("rho_H", real=True)
    rho_exch = sp.Symbol("rho_exch", real=True)
    rho_dark = sp.Symbol("rho_dark", real=True)
    E_accounting = sp.Symbol("E_accounting", real=True)

    # Danger diagnostic only: a duplicate ordinary scalar channel with a 1/r tail
    # carries a nonzero surface flux unless its coefficient vanishes.
    phi_dup = C_dup / r
    F_dup = sp.simplify(4 * sp.pi * r**2 * sp.diff(phi_dup, r))
    F_dup_residual = sp.simplify(F_dup + 4 * sp.pi * C_dup)
    delta_M_dup_like = sp.simplify((c**2 / (8 * sp.pi * G)) * F_dup)
    delta_M_dup_like_residual = sp.simplify(delta_M_dup_like + c**2 * C_dup / (2 * G))

    # Danger diagnostic only: if a duplicate non-A channel induces an A-like
    # exterior tail, it shifts the A-sector mass. This is not a source law.
    delta_A_dup = q_dup / r
    delta_F_A_dup = sp.simplify(4 * sp.pi * r**2 * sp.diff(delta_A_dup, r))
    delta_F_A_dup_residual = sp.simplify(delta_F_A_dup + 4 * sp.pi * q_dup)
    delta_M_A_dup = sp.simplify((c**2 / (8 * sp.pi * G)) * delta_F_A_dup)
    delta_M_A_dup_residual = sp.simplify(delta_M_A_dup + c**2 * q_dup / (2 * G))

    # Algebraic source ledger. rho_A is the protected A-sector ordinary mass source.
    # The extra symbols are not derived source channels; they name the burden that
    # future theorems must keep zero, diagnostic, non-metric, or separately routed.
    total_source_load = sp.simplify(
        rho_A + rho_kappa + rho_zeta + rho_curv + rho_H + rho_exch + rho_dark + E_accounting
    )
    extra_source_load = sp.simplify(total_source_load - rho_A)
    extra_source_load_residual = sp.simplify(
        extra_source_load - (rho_kappa + rho_zeta + rho_curv + rho_H + rho_exch + rho_dark + E_accounting)
    )
    cancellation_condition = sp.Eq(extra_source_load, 0)

    return SourceRoutingExpressionSet(
        r=r,
        G=G,
        c=c,
        C_dup=C_dup,
        q_dup=q_dup,
        rho_A=rho_A,
        rho_kappa=rho_kappa,
        rho_zeta=rho_zeta,
        rho_curv=rho_curv,
        rho_H=rho_H,
        rho_exch=rho_exch,
        rho_dark=rho_dark,
        E_accounting=E_accounting,
        phi_dup=phi_dup,
        F_dup=F_dup,
        F_dup_residual=F_dup_residual,
        delta_M_dup_like=delta_M_dup_like,
        delta_M_dup_like_residual=delta_M_dup_like_residual,
        delta_A_dup=delta_A_dup,
        delta_F_A_dup=delta_F_A_dup,
        delta_F_A_dup_residual=delta_F_A_dup_residual,
        delta_M_A_dup=delta_M_A_dup,
        delta_M_A_dup_residual=delta_M_A_dup_residual,
        total_source_load=total_source_load,
        extra_source_load=extra_source_load,
        extra_source_load_residual=extra_source_load_residual,
        cancellation_condition=cancellation_condition,
    )


def build_ledger_entries() -> List[RoutingLedgerEntry]:
    return [
        RoutingLedgerEntry(
            name="SRD1: rho / M_enc to A-sector",
            route="rho / M_enc -> A-sector mass charge",
            allowed_condition="ordinary mass density sources the reduced A-flux reference charge",
            forbidden_condition="rho is also routed into kappa, zeta, curvature, H, exchange, or dark mass channels by convenience",
            status="PROTECTED",
            consequence="A-sector remains the only currently licensed ordinary exterior mass coin.",
            obligation_id="protect_rho_A_sector_routing_21",
        ),
        RoutingLedgerEntry(
            name="SRD2: longitudinal current",
            route="longitudinal current -> scalar continuity / density redistribution",
            allowed_condition="current affects density redistribution only through a derived continuity/source law",
            forbidden_condition="longitudinal current becomes a second exterior mass flux without a mass-neutral theorem",
            status="THEOREM_TARGET",
            consequence="longitudinal flow needs continuity discipline before mass-routing use.",
            obligation_id="derive_longitudinal_current_routing_21",
        ),
        RoutingLedgerEntry(
            name="SRD3: transverse current",
            route="transverse current -> W_i vector sector",
            allowed_condition="transverse current is routed to W_i and does not create scalar A-flux, kappa, or zeta mass charge",
            forbidden_condition="transverse current is counted again as scalar mass or exchange repair",
            status="SAFE_IF",
            consequence="vector routing is safe only if it remains non-scalar and mass-neutral.",
            obligation_id="derive_transverse_current_mass_neutrality_21",
        ),
        RoutingLedgerEntry(
            name="SRD4: TT stress / quadrupole",
            route="TT stress / quadrupole -> h_TT",
            allowed_condition="radiative/tensor content is routed to tensor sector without duplicating ordinary scalar mass charge",
            forbidden_condition="TT stress becomes H_curv/H_exch source, dark patch, or scalar correction by convenience",
            status="THEOREM_TARGET",
            consequence="tensor/radiative routing remains separate from ordinary exterior mass charge.",
            obligation_id="derive_TT_stress_no_scalar_mass_double_count_21",
        ),
        RoutingLedgerEntry(
            name="SRD5: pressure / trace",
            route="pressure / trace -> diagnostic or non-metric kappa/zeta relaxation only if neutral",
            allowed_condition="pressure trace produces no exterior kappa/zeta 1/r scalar charge unless a parent theorem routes it without double counting",
            forbidden_condition="pressure trace creates exterior kappa Poisson charge or zeta mass route",
            status="THEOREM_TARGET",
            consequence="pressure/trace cannot become a second scalar mass source by declaration.",
            obligation_id="derive_pressure_trace_scalar_neutrality_21",
        ),
        RoutingLedgerEntry(
            name="SRD6: residual zeta/kappa source exclusion",
            route="zeta/kappa residuals excluded from ordinary source roles",
            allowed_condition="residuals are killed, non-metric, diagnostic, compact-neutral, or have vanishing exterior 1/r coefficients",
            forbidden_condition="zeta/kappa residuals become second scalar metric source",
            status="PROVISIONAL",
            consequence="residual-kill/non-metric residual remains safest but not a theorem.",
            obligation_id="derive_residual_source_exclusion_21",
        ),
        RoutingLedgerEntry(
            name="SRD7: curvature diagnostics",
            route="A_curv / e_curv / J_curv excluded from ordinary matter source roles",
            allowed_condition="curvature objects remain diagnostic/accounting/theorem-targeted unless source-neutral dynamics are derived",
            forbidden_condition="curvature diagnostics become matter sources, source reservoirs, or boundary repair currents",
            status="DIAGNOSTIC_ONLY",
            consequence="curvature accounting remains diagnostic, not source energy.",
            obligation_id="derive_curvature_source_separation_21",
        ),
        RoutingLedgerEntry(
            name="SRD8: correction tensors",
            route="H_curv / H_exch excluded from ordinary matter source roles",
            allowed_condition="H labels remain non-inserted diagnostics until tensor definition, source side, divergence safety, and neutrality are derived",
            forbidden_condition="H tensors absorb ordinary source mismatch or define their own source by divergence",
            status="REJECTED",
            consequence="correction tensors cannot be ordinary matter sinks or mass patches.",
            obligation_id="preserve_H_source_exclusion_21",
        ),
        RoutingLedgerEntry(
            name="SRD9: exchange roles",
            route="J_exch / Sigma_exch / R_exch remain separate from ordinary matter routing",
            allowed_condition="exchange roles remain role-level or derive source/support law with zero ordinary mass double count",
            forbidden_condition="ordinary T_mu_nu becomes Sigma_exch or J_exch by convenience",
            status="ROLE_LEVEL",
            consequence="exchange is not ordinary matter rerouting and not repair.",
            obligation_id="derive_exchange_source_separation_21",
        ),
        RoutingLedgerEntry(
            name="SRD10: dark labels",
            route="dark-sector labels optional downstream only",
            allowed_condition="dark coupling is derived after ordinary-sector neutrality, not used to patch ordinary failure",
            forbidden_condition="dark labels absorb ordinary source, boundary, scalar-tail, H, or recovery failure",
            status="DEFER",
            consequence="dark sector is not an ordinary mass patch.",
            obligation_id="preserve_dark_patch_exclusion_21",
        ),
        RoutingLedgerEntry(
            name="SRD11: energy/accounting terms",
            route="e_kappa / e_curv / epsilon_vac_config remain diagnostic/accounting",
            allowed_condition="accounting terms do not source A or supply coefficients unless a source theorem derives it",
            forbidden_condition="energy/accounting labels become coefficient reservoirs or source energy by vocabulary",
            status="ACCOUNTING_ONLY",
            consequence="energy words do not create source channels.",
            obligation_id="derive_accounting_terms_no_source_reservoir_21",
        ),
        RoutingLedgerEntry(
            name="SRD12: ordinary scalar radiation",
            route="ordinary scalar radiation rejected",
            allowed_condition="no ordinary long-range scalar radiation/source channel is licensed in this audit",
            forbidden_condition="scalar radiation reintroduces exterior residual 1/r tails or independent mass flux",
            status="REJECTED",
            consequence="ordinary scalar radiation remains outside the current source-routing license.",
            obligation_id="preserve_ordinary_scalar_radiation_rejection_21",
        ),
    ]


def build_rejected_routes() -> List[RejectedRoutingRoute]:
    return [
        RejectedRoutingRoute(
            name="RR1: rho also sources kappa mass charge",
            route="rho_to_kappa_mass_charge",
            forbidden_use="ordinary density produces an independent exterior kappa mass tail",
            consequence="rho is counted twice unless kappa route is derived and no double counting is proved.",
            obligation_id="reject_rho_to_kappa_mass_charge_21",
        ),
        RejectedRoutingRoute(
            name="RR2: pressure trace exterior scalar charge",
            route="pressure_trace_scalar_charge",
            forbidden_use="pressure or trace source creates exterior kappa/zeta Poisson charge",
            consequence="pressure trace cannot become a long-range scalar mass channel by convenience.",
            obligation_id="reject_pressure_trace_scalar_charge_21",
        ),
        RejectedRoutingRoute(
            name="RR3: ordinary T_mu_nu becomes Sigma_exch",
            route="ordinary_T_to_Sigma_exch",
            forbidden_use="ordinary matter is rerouted into exchange source labels",
            consequence="exchange source side needs its own theorem and cannot absorb ordinary matter.",
            obligation_id="reject_ordinary_T_to_Sigma_exch_21",
        ),
        RejectedRoutingRoute(
            name="RR4: curvature diagnostics as matter sources",
            route="curvature_diagnostics_as_sources",
            forbidden_use="A_curv, e_curv, or J_curv become ordinary matter source channels",
            consequence="curvature diagnostics remain diagnostic/accounting until real dynamics are derived.",
            obligation_id="reject_curvature_diagnostics_as_sources_21",
        ),
        RejectedRoutingRoute(
            name="RR5: H absorbs ordinary mismatch",
            route="H_absorbs_ordinary_source_mismatch",
            forbidden_use="H_curv or H_exch absorbs missing ordinary source, boundary, or divergence content",
            consequence="correction tensors remain non-insertable and cannot define source routing.",
            obligation_id="reject_H_absorbs_ordinary_mismatch_21",
        ),
        RejectedRoutingRoute(
            name="RR6: dark label patches ordinary failure",
            route="dark_label_patches_ordinary_failure",
            forbidden_use="dark label absorbs source, scalar-tail, boundary, H, or recovery failure",
            consequence="dark sector is not an ordinary source-routing patch.",
            obligation_id="reject_dark_label_patch_ordinary_failure_21",
        ),
        RejectedRoutingRoute(
            name="RR7: cancellation ledger instead of sector neutrality",
            route="source_cancellation_ledger",
            forbidden_use="sum of non-A source labels cancels while individual pockets remain nonzero",
            consequence="cancellation is not no-double-counting unless a future parent identity derives it.",
            obligation_id="reject_source_cancellation_ledger_21",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Source-routing no-double-counting problem")
    print("Question:")
    print()
    print("  Can ordinary matter be routed without being counted multiple times?")
    print()
    print("Reference discipline:")
    print()
    print("  A-sector mass charge remains the reduced ordinary exterior reference.")
    print("  Ordinary rho / M_enc routes to A-flux.")
    print("  Non-A sectors must not also count the same ordinary matter as independent mass.")
    print("  No active O, no source projector, no correction tensor, no exchange source side,")
    print("  and no dark label is assumed.")
    print("  This script records a source-routing ledger and no-double-counting guardrails, not a parent source law.")

    with out.governance_assessments():
        out.line(
            "source-routing no-double-counting audit opened",
            StatusMark.INFO,
            "ordinary matter routing is consolidated without deriving a parent source projector",
        )


def case_1_duplicate_scalar_tail(exprs: SourceRoutingExpressionSet, out: ScriptOutput) -> None:
    header("Case 1: Duplicate scalar source tail diagnostic")
    print("If an ordinary source were duplicated into a non-A scalar exterior tail:")
    print()
    print("  phi_dup(r) = C_dup/r")
    print()
    print("then:")
    print()
    print(f"  F_dup = 4*pi*r^2*phi_dup' = {sp.sstr(exprs.F_dup)}")
    print(f"  delta_M_dup_like = c^2*F_dup/(8*pi*G) = {sp.sstr(exprs.delta_M_dup_like)}")
    print()
    print("Residual checks:")
    print()
    print(f"  F_dup + 4*pi*C_dup = {sp.sstr(exprs.F_dup_residual)}")
    print(f"  delta_M_dup_like + c^2*C_dup/(2*G) = {sp.sstr(exprs.delta_M_dup_like_residual)}")
    print()
    print("Interpretation:")
    print()
    print("  This is a danger diagnostic, not a licensed duplicate source law.")
    print("  Any duplicated ordinary scalar tail with C_dup != 0 becomes a second mass coin.")

    with out.derived_results():
        out.line(
            "duplicate scalar tail flux derived",
            StatusMark.PASS if is_zero(exprs.F_dup_residual) else StatusMark.FAIL,
            f"F_dup = {sp.sstr(exprs.F_dup)}",
        )
        out.line(
            "duplicate scalar A-like mass shift diagnostic derived",
            StatusMark.PASS if is_zero(exprs.delta_M_dup_like_residual) else StatusMark.FAIL,
            f"delta_M_dup_like = {sp.sstr(exprs.delta_M_dup_like)}",
        )


def case_2_duplicate_A_tail(exprs: SourceRoutingExpressionSet, out: ScriptOutput) -> None:
    header("Case 2: Duplicate A-tail source diagnostic")
    print("If a non-A source-routing branch were allowed to induce an extra A-like exterior tail:")
    print()
    print("  delta_A_dup(r) = q_dup/r")
    print()
    print("then:")
    print()
    print(f"  delta_F_A|dup = 4*pi*r^2*delta_A_dup' = {sp.sstr(exprs.delta_F_A_dup)}")
    print(f"  delta_M_A|dup = c^2*delta_F_A|dup/(8*pi*G) = {sp.sstr(exprs.delta_M_A_dup)}")
    print()
    print("Residual checks:")
    print()
    print(f"  delta_F_A|dup + 4*pi*q_dup = {sp.sstr(exprs.delta_F_A_dup_residual)}")
    print(f"  delta_M_A|dup + c^2*q_dup/(2*G) = {sp.sstr(exprs.delta_M_A_dup_residual)}")
    print()
    print("Interpretation:")
    print()
    print("  This is not a source law.")
    print("  It shows why non-A branches may not induce q_dup/r A-tails by routing vocabulary.")

    with out.derived_results():
        out.line(
            "duplicate A-tail flux diagnostic derived",
            StatusMark.PASS if is_zero(exprs.delta_F_A_dup_residual) else StatusMark.FAIL,
            f"delta_F_A|dup = {sp.sstr(exprs.delta_F_A_dup)}",
        )
        out.line(
            "duplicate A-tail mass-shift diagnostic derived",
            StatusMark.PASS if is_zero(exprs.delta_M_A_dup_residual) else StatusMark.FAIL,
            f"delta_M_A|dup = {sp.sstr(exprs.delta_M_A_dup)}",
        )


def case_3_source_ledger(exprs: SourceRoutingExpressionSet, out: ScriptOutput) -> None:
    header("Case 3: Algebraic source-load ledger")
    print("Use a symbolic source-load ledger:")
    print()
    print("  rho_A        = protected A-sector ordinary mass source")
    print("  rho_kappa    = forbidden/targeted kappa duplicate source")
    print("  rho_zeta     = forbidden/targeted zeta duplicate source")
    print("  rho_curv     = curvature diagnostic source-reservoir danger")
    print("  rho_H        = correction tensor source-absorption danger")
    print("  rho_exch     = exchange source-rerouting danger")
    print("  rho_dark     = dark-label patch danger")
    print("  E_accounting = energy/accounting source-reservoir danger")
    print()
    print("Total source-load candidate:")
    print()
    print(f"  total_source_load = {sp.sstr(exprs.total_source_load)}")
    print()
    print("Extra non-A source-load beyond A-sector:")
    print()
    print(f"  extra_source_load = total_source_load - rho_A = {sp.sstr(exprs.extra_source_load)}")
    print()
    print("Residual check:")
    print()
    print(f"  extra_source_load residual = {sp.sstr(exprs.extra_source_load_residual)}")
    print()
    print("A cancellation condition would be:")
    print()
    print(f"  {exprs.cancellation_condition}")
    print()
    print("But Group 21 does not accept cancellation ledgers as sector neutrality.")
    print("Each non-A pocket must be empty, diagnostic, non-metric, role-level, or theorem-routed.")

    with out.derived_results():
        out.line(
            "extra non-A source-load ledger derived",
            StatusMark.PASS if is_zero(exprs.extra_source_load_residual) else StatusMark.FAIL,
            f"extra_source_load = {sp.sstr(exprs.extra_source_load)}",
        )
    with out.counterexamples():
        out.line(
            "source cancellation by hand rejected",
            StatusMark.FAIL,
            "extra_source_load = 0 by cancellation is not sector-by-sector no-double-counting",
        )


def case_4_routing_ledger(entries: List[RoutingLedgerEntry], out: ScriptOutput) -> None:
    header("Case 4: Ordinary source-routing ledger")
    for entry in entries:
        print()
        print("-" * 120)
        print(entry.name)
        print("-" * 120)
        print(f"Route: {entry.route}")
        print(f"Allowed condition: {entry.allowed_condition}")
        print(f"Forbidden condition: {entry.forbidden_condition}")
        print(f"[{entry_status_mark(entry.status).value}] {entry.name}: {entry.status}")
        print(f"Consequence: {entry.consequence}")

    with out.governance_assessments():
        out.line(
            "ordinary source-routing ledger populated",
            StatusMark.PASS,
            f"{len(entries)} routing rules classified for no-double-counting burden",
        )


def case_5_rejected_routes(routes: List[RejectedRoutingRoute], out: ScriptOutput) -> None:
    header("Case 5: Rejected source double-counting routes")
    for route in routes:
        print()
        print("-" * 120)
        print(route.name)
        print("-" * 120)
        print(f"Route: {route.route}")
        print(f"Forbidden use: {route.forbidden_use}")
        print(f"[FAIL] {route.name}: REJECTED")
        print(f"Consequence: {route.consequence}")

    with out.counterexamples():
        out.line(
            "source double-counting routes rejected",
            StatusMark.FAIL,
            "rho-to-kappa, pressure scalar charge, ordinary T to exchange, curvature source, H absorption, dark patch, and cancellation ledger are not licensed",
        )


def case_6_failure_controls(out: ScriptOutput) -> None:
    header("Case 6: Failure controls")
    print("The source-routing no-double-counting audit fails if a later script allows:")
    print()
    print("1. rho / M_enc to source any second ordinary exterior mass channel by declaration")
    print("2. rho to also source kappa, zeta, curvature, H, exchange, or dark labels")
    print("3. pressure trace to create exterior kappa/zeta scalar charge")
    print("4. ordinary T_mu_nu to become Sigma_exch, J_exch, H_curv, or H_exch by convenience")
    print("5. curvature diagnostics or accounting terms to become source reservoirs")
    print("6. H tensors to absorb ordinary source mismatch or define their own source by divergence")
    print("7. dark labels to patch ordinary source, boundary, scalar-tail, H, or recovery failure")
    print("8. zeta/kappa residuals to become second scalar metric source")
    print("9. source cancellation ledgers to stand in for sector-by-sector neutrality")
    print("10. O/source projectors to enforce routing without domain/kernel/image/boundary law")

    with out.unresolved_obligations():
        out.line(
            "derive ordinary source no-double-counting theorem",
            StatusMark.OBLIGATION,
            "show ordinary matter routes through protected channels without duplicate non-A mass/source channels",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Current ordinary source-routing discipline:")
    print()
    print("  rho / M_enc -> A-sector mass charge")
    print("  longitudinal current -> continuity / density redistribution only if derived")
    print("  transverse current -> W_i without scalar mass duplication")
    print("  TT stress / quadrupole -> h_TT without scalar mass duplication")
    print("  pressure / trace -> diagnostic or non-metric kappa/zeta relaxation only if neutral")
    print("  ordinary scalar radiation -> rejected")
    print("  ordinary matter -> not rerouted into J_sub/J_exch/Sigma_exch/H_exch/H_curv")
    print()
    print("The reduced danger witnesses are:")
    print()
    print("  duplicate scalar tail C_dup/r -> F_dup = -4*pi*C_dup")
    print("  duplicate A-tail q_dup/r      -> delta_M_A|dup = -c^2*q_dup/(2*G)")
    print("  extra source-load ledger      -> non-A source labels must not survive by cancellation")
    print()
    print("This script does not derive parent source routing.")
    print("It records the no-double-counting burden for the Group 21 closure.")
    print()
    print("Possible next script:")
    print("  candidate_group_21_source_routing_status_summary.py")

    with out.governance_assessments():
        out.line(
            "source-routing no-double-counting audit complete",
            StatusMark.PASS,
            "ordinary matter remains routed to protected channels; source routing remains constrained but not parent-derived",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, exprs: SourceRoutingExpressionSet) -> None:
    ns.record_derivation(
        derivation_id="duplicate_scalar_tail_flux_21",
        inputs=[exprs.phi_dup, exprs.r, exprs.C_dup],
        output=exprs.F_dup,
        method="F_dup = simplify(4*pi*r**2*diff(C_dup/r, r))",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="surface_flux",
        scope="reduced ordinary exterior duplicate scalar source diagnostic",
    )
    ns.record_derivation(
        derivation_id="duplicate_scalar_tail_mass_shift_diagnostic_21",
        inputs=[exprs.F_dup, exprs.c, exprs.G],
        output=exprs.delta_M_dup_like,
        method="delta_M_dup_like = simplify(c**2*F_dup/(8*pi*G))",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="mass_shift_diagnostic",
        scope="danger diagnostic only; not a licensed duplicate mass law",
    )
    ns.record_derivation(
        derivation_id="duplicate_A_tail_flux_diagnostic_21",
        inputs=[exprs.delta_A_dup, exprs.r, exprs.q_dup],
        output=exprs.delta_F_A_dup,
        method="delta_F_A_dup = simplify(4*pi*r**2*diff(q_dup/r, r))",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="A_flux_shift_diagnostic",
        scope="danger diagnostic only; not a licensed duplicate source law",
    )
    ns.record_derivation(
        derivation_id="duplicate_A_tail_mass_shift_diagnostic_21",
        inputs=[exprs.delta_F_A_dup, exprs.c, exprs.G],
        output=exprs.delta_M_A_dup,
        method="delta_M_A_dup = simplify(c**2*delta_F_A_dup/(8*pi*G))",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="mass_shift_diagnostic",
        scope="danger diagnostic only; not a licensed duplicate mass law",
    )
    ns.record_derivation(
        derivation_id="ordinary_source_extra_load_ledger_21",
        inputs=[
            exprs.rho_A,
            exprs.rho_kappa,
            exprs.rho_zeta,
            exprs.rho_curv,
            exprs.rho_H,
            exprs.rho_exch,
            exprs.rho_dark,
            exprs.E_accounting,
        ],
        output=exprs.extra_source_load,
        method="extra_source_load = simplify(total_source_load - rho_A)",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="source_load_ledger",
        scope="source-routing no-double-counting diagnostic only",
    )


def record_inventory_marker(ns, entries: List[RoutingLedgerEntry]) -> None:
    names = [sp.Symbol(entry.name.split(":", 1)[0].replace("-", "_").replace(" ", "_")) for entry in entries]
    ns.record_derivation(
        derivation_id="source_routing_no_double_counting_marker_21",
        inputs=names,
        output=sp.Symbol("source_routing_no_double_counting_rules_stated"),
        method="ordinary source-routing no-double-counting ledger and rejected-route inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="inventory_marker",
        scope="Group 21 source routing and mass neutrality",
        is_placeholder=True,
    )


def record_obligations(
    ns,
    entries: List[RoutingLedgerEntry],
    routes: List[RejectedRoutingRoute],
) -> None:
    for entry in entries:
        if entry.obligation_id is None:
            continue
        ns.record_obligation(ProofObligationRecord(
            obligation_id=entry.obligation_id,
            script_id=SCRIPT_ID,
            title=f"Resolve source-routing rule: {entry.name}",
            status=ObligationStatus.OPEN,
            required_by=["ordinary_source_no_double_counting_theorem_21"],
            description=(
                f"Route: {entry.route}. Allowed condition: {entry.allowed_condition}. "
                f"Forbidden condition: {entry.forbidden_condition}. Consequence: {entry.consequence}."
            ),
        ))

    for route in routes:
        if route.obligation_id is None:
            continue
        ns.record_obligation(ProofObligationRecord(
            obligation_id=route.obligation_id,
            script_id=SCRIPT_ID,
            title=f"Preserve rejected source route: {route.name}",
            status=ObligationStatus.OPEN,
            required_by=["ordinary_source_no_double_counting_theorem_21"],
            description=(
                f"Route: {route.route}. Forbidden use: {route.forbidden_use}. "
                f"Consequence: {route.consequence}."
            ),
        ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="ordinary_source_no_double_counting_theorem_21",
        script_id=SCRIPT_ID,
        title="Derive ordinary source no-double-counting theorem",
        status=ObligationStatus.OPEN,
        required_by=["ordinary_closed_regime_mass_neutrality_theorem_21"],
        description=(
            "Show ordinary rho/T_mu_nu routes through protected ordinary channels without duplicate kappa/zeta scalar mass charge, "
            "curvature source reservoir, correction tensor source absorption, exchange rerouting, dark patching, accounting-source leakage, "
            "or cancellation-ledger replacement for sector neutrality."
        ),
    ))


def record_governance(
    ns,
    entries: List[RoutingLedgerEntry],
    routes: List[RejectedRoutingRoute],
) -> None:
    obligation_ids = [entry.obligation_id for entry in entries if entry.obligation_id is not None]
    obligation_ids.extend(route.obligation_id for route in routes if route.obligation_id is not None)
    obligation_ids.append("ordinary_source_no_double_counting_theorem_21")

    ns.record_route(RouteRecord(
        route_id="ordinary_source_routing_no_double_counting_route_21",
        script_id=SCRIPT_ID,
        name="Ordinary source-routing no-double-counting route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "A-sector mass charge remains the reduced ordinary exterior reference",
            "ordinary rho/M_enc routes to A-flux unless a future parent theorem derives otherwise",
            "longitudinal, transverse, tensor, pressure, residual, curvature, H, exchange, dark, and accounting routes remain source-separated",
            "no active O/source projector, correction tensor, exchange source side, or dark patch is assumed",
        ],
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="protect_A_sector_ordinary_source_routing_21",
        script_id=SCRIPT_ID,
        branch_id="ordinary_rho_Menc_A_sector_routing",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "protect_rho_A_sector_routing_21",
            "ordinary_source_no_double_counting_theorem_21",
        ],
        description=(
            "Ordinary rho/M_enc remains routed to the A-sector reference charge while non-A duplicate source routes remain forbidden, "
            "diagnostic, role-level, or theorem-targeted."
        ),
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_ordinary_source_double_counting_routes_21",
        script_id=SCRIPT_ID,
        branch_id="ordinary_source_double_counting_routes",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[route.obligation_id for route in routes if route.obligation_id is not None],
        description=(
            "Reject source-routing routes that count ordinary matter through multiple independent mass/source channels: rho-to-kappa, "
            "pressure scalar charge, ordinary T to exchange, curvature sources, H source absorption, dark patches, and cancellation ledgers."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="ordinary_source_routing_no_double_counting_conditions_21",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Ordinary source routing in Group 21 remains constrained but not parent-derived: rho/M_enc routes to A-sector mass charge; "
            "non-A channels must not duplicate ordinary mass or source content without future no-double-counting and mass-neutrality theorems."
        ),
        derivation_ids=[
            "duplicate_scalar_tail_flux_21",
            "duplicate_A_tail_flux_diagnostic_21",
            "ordinary_source_extra_load_ledger_21",
        ],
        obligation_ids=obligation_ids,
    ))

    ns.record_claim(ClaimRecord(
        claim_id="ordinary_source_double_counting_routes_rejected_21",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Ordinary matter must not be rerouted into independent kappa/zeta scalar charge, curvature source reservoirs, H tensors, exchange labels, "
            "dark patches, or accounting energy channels by convenience. Cancellation among non-A source labels is not sector neutrality."
        ),
        derivation_ids=[
            "duplicate_scalar_tail_flux_21",
            "duplicate_A_tail_flux_diagnostic_21",
            "ordinary_source_extra_load_ledger_21",
        ],
        obligation_ids=[route.obligation_id for route in routes if route.obligation_id is not None],
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Source Routing No Double Counting")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    exprs = build_expressions()
    entries = build_ledger_entries()
    routes = build_rejected_routes()

    case_0_problem_statement(out)
    case_1_duplicate_scalar_tail(exprs, out)
    case_2_duplicate_A_tail(exprs, out)
    case_3_source_ledger(exprs, out)
    case_4_routing_ledger(entries, out)
    case_5_rejected_routes(routes, out)
    case_6_failure_controls(out)
    final_interpretation(out)

    record_derivations(ns, exprs)
    record_inventory_marker(ns, entries)
    record_obligations(ns, entries, routes)
    record_governance(ns, entries, routes)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
