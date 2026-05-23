# Candidate J_V mass neutrality conditions
#
# Group:
#   21_source_routing_and_mass_neutrality
#
# Script type:
#   DERIVATION / DIAGNOSTIC / REQUIREMENTS
#
# Purpose
# -------
# Audit whether J_V, J_sub, and J_exch can be ordinary-sector mass-neutral.
#
# Locked-door question:
#
#   Can J_V, J_sub, or J_exch be ordinary-sector mass-neutral?
#
# This script does not define J_V, u_vac, J_sub, J_exch, Sigma/R operators,
# flux direction, source side, exchange law, boundary law, no-overlap, or a
# parent field equation.
#
# It derives reduced diagnostic witnesses for the dangers that an undefined
# current can hide:
#
#   scalar residue:       phi_JV = C_JV/r -> F_phi = -4*pi*C_JV
#   far-zone flux:        j_r = I/(4*pi*r^2) -> Phi_J = I
#   zero-net exchange:    net = Sigma_0 - R_0
#
# Therefore ordinary-sector current branches are safe only if they remain
# role-level/diagnostic, have no scalar residue, have no far-zone current flux,
# do not alter A-flux, and do not repair boundary or source-routing failures.

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
        dependency_id="zeta_kappa_inventory_dependency_21",
        upstream_script_id="21_source_routing_and_mass_neutrality__candidate_zeta_kappa_mass_neutrality_conditions",
        upstream_derivation_id="zeta_kappa_mass_neutrality_inventory_marker_21",
        expected_record_kind=RecordKind.INVENTORY_MARKER,
    )
    ns.declare_dependency(
        dependency_id="zeta_tail_flux_dependency_21",
        upstream_script_id="21_source_routing_and_mass_neutrality__candidate_zeta_kappa_mass_neutrality_conditions",
        upstream_derivation_id="zeta_residual_tail_flux_21",
        expected_record_kind=RecordKind.DERIVATION,
    )
    ns.declare_dependency(
        dependency_id="kappa_tail_flux_dependency_21",
        upstream_script_id="21_source_routing_and_mass_neutrality__candidate_zeta_kappa_mass_neutrality_conditions",
        upstream_derivation_id="kappa_residual_tail_flux_21",
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
        "CANDIDATE": StatusMark.INFO,
        "DEFER": StatusMark.DEFER,
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


# =============================================================================
# Data models
# =============================================================================


@dataclass
class JVExpressionSet:
    r: sp.Symbol
    G: sp.Symbol
    c: sp.Symbol
    C_JV: sp.Symbol
    I_V: sp.Symbol
    I_sub: sp.Symbol
    I_exch: sp.Symbol
    Sigma_0: sp.Symbol
    R_0: sp.Symbol
    phi_JV: sp.Expr
    F_phi_JV: sp.Expr
    F_phi_JV_residual: sp.Expr
    delta_M_JV_like: sp.Expr
    delta_M_JV_like_residual: sp.Expr
    j_V_radial: sp.Expr
    j_sub_radial: sp.Expr
    j_exch_radial: sp.Expr
    Phi_JV: sp.Expr
    Phi_Jsub: sp.Expr
    Phi_Jexch: sp.Expr
    Phi_JV_residual: sp.Expr
    Phi_Jsub_residual: sp.Expr
    Phi_Jexch_residual: sp.Expr
    net_exchange: sp.Expr
    zero_net_residual: sp.Expr


@dataclass
class CurrentConditionEntry:
    name: str
    sector: str
    allowed_condition: str
    forbidden_condition: str
    status: str
    consequence: str
    obligation_id: str | None = None


@dataclass
class RejectedCurrentRoute:
    name: str
    route: str
    forbidden_use: str
    consequence: str
    obligation_id: str | None = None


# =============================================================================
# Builders
# =============================================================================


def build_expressions() -> JVExpressionSet:
    r = sp.Symbol("r", positive=True)
    G = sp.Symbol("G", positive=True)
    c = sp.Symbol("c", positive=True)
    C_JV = sp.Symbol("C_JV", real=True)
    I_V = sp.Symbol("I_V", real=True)
    I_sub = sp.Symbol("I_sub", real=True)
    I_exch = sp.Symbol("I_exch", real=True)
    Sigma_0 = sp.Symbol("Sigma_0", real=True)
    R_0 = sp.Symbol("R_0", real=True)

    # Generic scalar residue left by an unresolved vacuum current.
    phi_JV = C_JV / r
    F_phi_JV = sp.simplify(4 * sp.pi * r**2 * sp.diff(phi_JV, r))
    F_phi_JV_residual = sp.simplify(F_phi_JV + 4 * sp.pi * C_JV)
    delta_M_JV_like = sp.simplify((c**2 / (8 * sp.pi * G)) * F_phi_JV)
    delta_M_JV_like_residual = sp.simplify(delta_M_JV_like + c**2 * C_JV / (2 * G))

    # Generic radial 1/r^2 current flux diagnostics. These do not define J_V;
    # they show why a nonzero far-zone current coefficient is mass-dangerous.
    j_V_radial = I_V / (4 * sp.pi * r**2)
    j_sub_radial = I_sub / (4 * sp.pi * r**2)
    j_exch_radial = I_exch / (4 * sp.pi * r**2)

    Phi_JV = sp.simplify(4 * sp.pi * r**2 * j_V_radial)
    Phi_Jsub = sp.simplify(4 * sp.pi * r**2 * j_sub_radial)
    Phi_Jexch = sp.simplify(4 * sp.pi * r**2 * j_exch_radial)
    Phi_JV_residual = sp.simplify(Phi_JV - I_V)
    Phi_Jsub_residual = sp.simplify(Phi_Jsub - I_sub)
    Phi_Jexch_residual = sp.simplify(Phi_Jexch - I_exch)

    # Role-level zero-net exchange diagnostic.
    net_exchange = sp.simplify(Sigma_0 - R_0)
    zero_net_residual = sp.simplify(net_exchange - (Sigma_0 - R_0))

    return JVExpressionSet(
        r=r,
        G=G,
        c=c,
        C_JV=C_JV,
        I_V=I_V,
        I_sub=I_sub,
        I_exch=I_exch,
        Sigma_0=Sigma_0,
        R_0=R_0,
        phi_JV=phi_JV,
        F_phi_JV=F_phi_JV,
        F_phi_JV_residual=F_phi_JV_residual,
        delta_M_JV_like=delta_M_JV_like,
        delta_M_JV_like_residual=delta_M_JV_like_residual,
        j_V_radial=j_V_radial,
        j_sub_radial=j_sub_radial,
        j_exch_radial=j_exch_radial,
        Phi_JV=Phi_JV,
        Phi_Jsub=Phi_Jsub,
        Phi_Jexch=Phi_Jexch,
        Phi_JV_residual=Phi_JV_residual,
        Phi_Jsub_residual=Phi_Jsub_residual,
        Phi_Jexch_residual=Phi_Jexch_residual,
        net_exchange=net_exchange,
        zero_net_residual=zero_net_residual,
    )


def build_condition_entries() -> List[CurrentConditionEntry]:
    return [
        CurrentConditionEntry(
            name="JV1: unresolved J_V umbrella",
            sector="J_V",
            allowed_condition="J_V remains unresolved notation until a current definition, source side, domain, and flux direction are supplied",
            forbidden_condition="J_V is treated as a physical mass current by name",
            status="UNRESOLVED",
            consequence="J_V cannot carry ordinary exterior mass while undefined.",
            obligation_id="define_JV_current_law_21",
        ),
        CurrentConditionEntry(
            name="JV2: J_V scalar residue",
            sector="J_V residue",
            allowed_condition="C_JV = 0 outside, or residue is strictly non-metric/diagnostic and has no A-flux effect",
            forbidden_condition="phi_JV = C_JV/r with C_JV != 0 behaves as exterior scalar charge",
            status="THEOREM_TARGET",
            consequence="J_V must not leave a hidden 1/r scalar tail.",
            obligation_id="derive_JV_no_scalar_residue_21",
        ),
        CurrentConditionEntry(
            name="JV3: J_V far-zone current flux",
            sector="J_V",
            allowed_condition="I_V = 0 in ordinary exterior unless a future current law derives a neutral transport meaning",
            forbidden_condition="nonzero 1/r^2 far-zone current flux shifts or mimics exterior mass",
            status="THEOREM_TARGET",
            consequence="A far-zone vacuum current cannot become a second mass flux coin.",
            obligation_id="derive_JV_far_zone_flux_neutrality_21",
        ),
        CurrentConditionEntry(
            name="JV4: u_vac domain guard",
            sector="u_vac / J_V domain",
            allowed_condition="u_vac is defined only after J_V is nonzero, timelike where needed, and physically sourced",
            forbidden_condition="u_vac is chosen first and then used to manufacture J_V or Sigma_V",
            status="UNRESOLVED",
            consequence="no frame field can rescue mass routing while J_V is undefined.",
            obligation_id="derive_u_vac_domain_from_JV_21",
        ),
        CurrentConditionEntry(
            name="JS1: J_sub role-level pure wind",
            sector="J_sub",
            allowed_condition="J_sub remains role-level or proves pure wind neutrality with no A-flux, scalar trace, boundary repair, or matter push",
            forbidden_condition="J_sub gravitates by being a wind or preferred-frame flow",
            status="ROLE_LEVEL",
            consequence="pure wind is not gravity without an independent theorem.",
            obligation_id="derive_Jsub_pure_wind_neutrality_21",
        ),
        CurrentConditionEntry(
            name="JS2: J_sub scalar trace leakage",
            sector="J_sub residue",
            allowed_condition="J_sub leaves no scalar residue and no exterior 1/r tail",
            forbidden_condition="J_sub becomes a hidden scalar trace source",
            status="THEOREM_TARGET",
            consequence="substrate-current labels cannot hide a scalar mass route.",
            obligation_id="derive_Jsub_no_scalar_trace_21",
        ),
        CurrentConditionEntry(
            name="JS3: J_sub boundary repair",
            sector="J_sub boundary behavior",
            allowed_condition="J_sub has no boundary effect unless a source-neutral boundary law is derived",
            forbidden_condition="J_sub cancels boundary mismatch, shell flux, or recovery failure",
            status="REJECTED",
            consequence="J_sub cannot be a boundary purse.",
            obligation_id="reject_Jsub_boundary_repair_21",
        ),
        CurrentConditionEntry(
            name="JE1: J_exch role-level exchange current",
            sector="J_exch",
            allowed_condition="J_exch remains role-level until exchange source/support operators are defined",
            forbidden_condition="J_exch is used as ordinary matter source side by convenience",
            status="ROLE_LEVEL",
            consequence="exchange is not an ordinary mass route by vocabulary.",
            obligation_id="derive_Jexch_source_support_law_21",
        ),
        CurrentConditionEntry(
            name="JE2: J_exch repair current",
            sector="J_exch repair route",
            allowed_condition="none in the current ordinary-sector audit",
            forbidden_condition="J_exch repairs ordinary matter routing, boundary leakage, or exterior scalar tails",
            status="REJECTED",
            consequence="exchange cannot fix ordinary-sector failures after the fact.",
            obligation_id="reject_Jexch_repair_current_21",
        ),
        CurrentConditionEntry(
            name="SR1: Sigma/R zero-net branch",
            sector="Sigma_V / R_V",
            allowed_condition="Sigma_0 - R_0 = 0 only as a role-level neutrality target until operators, strengths, signs, and domains are derived",
            forbidden_condition="zero-net is declared to hold without source and relaxation operators",
            status="THEOREM_TARGET",
            consequence="zero-net exchange is promising but not a theorem here.",
            obligation_id="derive_sigma_R_zero_net_ordinary_branch_21",
        ),
        CurrentConditionEntry(
            name="SR2: zero-creation ordinary branch",
            sector="Sigma_V / R_V",
            allowed_condition="ordinary sector may remain zero-creation if curvature is warping/constraint rather than vacuum creation/destruction",
            forbidden_condition="creation language is used as an ordinary source while claiming neutrality",
            status="CANDIDATE",
            consequence="zero-creation remains a safe candidate, not a derived law.",
            obligation_id="derive_zero_creation_ordinary_branch_21",
        ),
        CurrentConditionEntry(
            name="SR3: latent exchange branch",
            sector="latent exchange / curvature-from-warping",
            allowed_condition="exchange roles remain latent or diagnostic unless a real source law activates them without shifting M_A",
            forbidden_condition="latent exchange becomes a hidden mass current or boundary repair",
            status="SAFE_IF",
            consequence="latent exchange may remain bookkeeping only if it has no source, metric, boundary, or mass effect.",
            obligation_id="derive_latent_exchange_mass_neutrality_21",
        ),
    ]


def build_rejected_routes() -> List[RejectedCurrentRoute]:
    return [
        RejectedCurrentRoute(
            name="RJ1: undefined J_V mass current",
            route="undefined_JV_mass_current",
            forbidden_use="J_V shifts exterior mass without current definition, flux law, or source side",
            consequence="undefined J_V cannot carry M_ext.",
            obligation_id="reject_undefined_JV_mass_current_21",
        ),
        RejectedCurrentRoute(
            name="RJ2: J_V scalar 1/r residue",
            route="JV_scalar_tail_mass_route",
            forbidden_use="C_JV/r residue treated as ordinary exterior scalar mass channel",
            consequence="J_V scalar residue must vanish or stay non-metric/diagnostic.",
            obligation_id="reject_JV_scalar_tail_mass_route_21",
        ),
        RejectedCurrentRoute(
            name="RJ3: pure wind gravitates by existence",
            route="Jsub_wind_gravity",
            forbidden_use="J_sub produces gravity merely because a substrate wind exists",
            consequence="pure wind is not a mass source.",
            obligation_id="reject_Jsub_wind_gravity_21",
        ),
        RejectedCurrentRoute(
            name="RJ4: exchange repair current",
            route="Jexch_repair_current",
            forbidden_use="J_exch cancels boundary, source, scalar-tail, or recovery mismatch",
            consequence="exchange is not repair.",
            obligation_id="reject_Jexch_repair_current_route_21",
        ),
        RejectedCurrentRoute(
            name="RJ5: Sigma/R tuning knob",
            route="Sigma_R_tuning_knob",
            forbidden_use="Sigma/R roles are adjusted to preserve mass or recovery after leakage appears",
            consequence="Sigma/R need operators, not knobs.",
            obligation_id="reject_sigma_R_tuning_knob_21",
        ),
        RejectedCurrentRoute(
            name="RJ6: u_vac chosen by recovery",
            route="recovery_chosen_u_vac",
            forbidden_use="u_vac frame is selected from Schwarzschild/PPN/gamma_like/AB recovery",
            consequence="the vacuum frame cannot be a recovery fit.",
            obligation_id="reject_recovery_chosen_uvac_21",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: J_V / J_sub / J_exch mass-neutrality problem")
    print("Question:")
    print()
    print("  Can J_V, J_sub, or J_exch be ordinary-sector mass-neutral?")
    print()
    print("Reference discipline:")
    print()
    print("  A-sector mass charge remains the reduced ordinary exterior reference.")
    print("  J_V is unresolved; J_sub/J_exch are role-level only.")
    print("  Sigma/R operators, flux direction, and u_vac remain missing.")
    print("  No current branch may shift A-flux, create scalar charge, repair a boundary,")
    print("  or reroute ordinary matter by convenience.")
    print("  This script records reduced diagnostics and theorem burden, not a current law.")

    with out.governance_assessments():
        out.line(
            "vacuum-current mass-neutrality audit opened",
            StatusMark.INFO,
            "J_V/J_sub/J_exch are audited for scalar residue, far-zone flux, repair, and source-rerouting danger",
        )


def case_1_JV_scalar_residue(exprs: JVExpressionSet, out: ScriptOutput) -> None:
    header("Case 1: J_V-induced scalar residue")
    print("Take a generic scalar residue that could be left by an unresolved J_V:")
    print()
    print(f"  phi_JV(r) = {sp.sstr(exprs.phi_JV)}")
    print()
    print("Then:")
    print()
    print(f"  F_phi_JV = 4*pi*r^2*phi_JV' = {sp.sstr(exprs.F_phi_JV)}")
    print(f"  delta_M_JV_like = c^2*F_phi_JV/(8*pi*G) = {sp.sstr(exprs.delta_M_JV_like)}")
    print()
    print("Residual checks:")
    print()
    print(f"  F_phi_JV + 4*pi*C_JV = {sp.sstr(exprs.F_phi_JV_residual)}")
    print(f"  delta_M_JV_like + c^2*C_JV/(2*G) = {sp.sstr(exprs.delta_M_JV_like_residual)}")
    print()
    print("Interpretation:")
    print()
    print("  This is a danger diagnostic, not a licensed J_V mass law.")
    print("  It shows that a J_V-induced 1/r scalar residue would act like a second mass coin.")

    with out.derived_results():
        out.line(
            "J_V scalar residue flux derived",
            StatusMark.PASS if is_zero(exprs.F_phi_JV_residual) else StatusMark.FAIL,
            f"F_phi_JV = {sp.sstr(exprs.F_phi_JV)}",
        )
        out.line(
            "J_V A-like mass-shift diagnostic derived",
            StatusMark.PASS if is_zero(exprs.delta_M_JV_like_residual) else StatusMark.FAIL,
            f"delta_M_JV_like = {sp.sstr(exprs.delta_M_JV_like)}",
        )


def case_2_far_zone_current_flux(exprs: JVExpressionSet, out: ScriptOutput) -> None:
    header("Case 2: Far-zone radial current flux diagnostic")
    print("Use generic 1/r^2 radial current profiles as diagnostics:")
    print()
    print(f"  j_V^r    = {sp.sstr(exprs.j_V_radial)}")
    print(f"  j_sub^r  = {sp.sstr(exprs.j_sub_radial)}")
    print(f"  j_exch^r = {sp.sstr(exprs.j_exch_radial)}")
    print()
    print("Their sphere fluxes are:")
    print()
    print(f"  Phi_JV    = 4*pi*r^2*j_V^r    = {sp.sstr(exprs.Phi_JV)}")
    print(f"  Phi_Jsub  = 4*pi*r^2*j_sub^r  = {sp.sstr(exprs.Phi_Jsub)}")
    print(f"  Phi_Jexch = 4*pi*r^2*j_exch^r = {sp.sstr(exprs.Phi_Jexch)}")
    print()
    print("Neutral ordinary exterior current flux requires the relevant I coefficient to vanish")
    print("unless a future current theorem derives a neutral transport interpretation.")

    with out.derived_results():
        out.line(
            "J_V far-zone current flux diagnostic derived",
            StatusMark.PASS if is_zero(exprs.Phi_JV_residual) else StatusMark.FAIL,
            f"Phi_JV = {sp.sstr(exprs.Phi_JV)}",
        )
        out.line(
            "J_sub far-zone current flux diagnostic derived",
            StatusMark.PASS if is_zero(exprs.Phi_Jsub_residual) else StatusMark.FAIL,
            f"Phi_Jsub = {sp.sstr(exprs.Phi_Jsub)}",
        )
        out.line(
            "J_exch far-zone current flux diagnostic derived",
            StatusMark.PASS if is_zero(exprs.Phi_Jexch_residual) else StatusMark.FAIL,
            f"Phi_Jexch = {sp.sstr(exprs.Phi_Jexch)}",
        )


def case_3_zero_net_exchange(exprs: JVExpressionSet, out: ScriptOutput) -> None:
    header("Case 3: Zero-net exchange diagnostic")
    print("At role level, a zero-net ordinary branch would require:")
    print()
    print("  Sigma_0 - R_0 = 0")
    print()
    print("The symbolic net role-label residual is:")
    print()
    print(f"  net_exchange = {sp.sstr(exprs.net_exchange)}")
    print(f"  net_exchange - (Sigma_0 - R_0) = {sp.sstr(exprs.zero_net_residual)}")
    print()
    print("Interpretation:")
    print()
    print("  Zero-net exchange is a theorem target, not a declaration.")
    print("  Sigma/R need operators, signs, strengths, domains, and boundary behavior.")

    with out.derived_results():
        out.line(
            "zero-net exchange diagnostic stated",
            StatusMark.PASS if is_zero(exprs.zero_net_residual) else StatusMark.FAIL,
            "neutral role target is Sigma_0 - R_0 = 0",
        )
    with out.unresolved_obligations():
        out.line(
            "derive Sigma/R operators before zero-net claim",
            StatusMark.OBLIGATION,
            "zero-net exchange cannot be asserted while Sigma/R remain role-level",
        )


def case_4_current_condition_ledger(entries: List[CurrentConditionEntry], out: ScriptOutput) -> None:
    header("Case 4: J_V / J_sub / J_exch condition ledger")
    for entry in entries:
        print()
        print("-" * 120)
        print(entry.name)
        print("-" * 120)
        print(f"Sector: {entry.sector}")
        print(f"Allowed condition: {entry.allowed_condition}")
        print(f"Forbidden condition: {entry.forbidden_condition}")
        print(f"[{entry_status_mark(entry.status).value}] {entry.name}: {entry.status}")
        print(f"Consequence: {entry.consequence}")

    with out.governance_assessments():
        out.line(
            "vacuum-current condition ledger populated",
            StatusMark.PASS,
            f"{len(entries)} current/source-role conditions classified for mass-neutrality burden",
        )


def case_5_rejected_current_routes(routes: List[RejectedCurrentRoute], out: ScriptOutput) -> None:
    header("Case 5: Rejected vacuum-current mass routes")
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
            "vacuum-current mass routes rejected",
            StatusMark.FAIL,
            "undefined J_V mass current, J_V scalar tail, pure-wind gravity, exchange repair, Sigma/R tuning, and recovery-chosen u_vac are not licensed",
        )


def case_6_failure_controls(out: ScriptOutput) -> None:
    header("Case 6: Failure controls")
    print("The J_V / J_sub / J_exch mass-neutrality audit fails if a later script allows:")
    print()
    print("1. J_V to shift exterior mass without a derived current and flux law")
    print("2. J_V to leave a scalar C_JV/r residue with C_JV != 0")
    print("3. a nonzero far-zone J_V, J_sub, or J_exch flux to count as ordinary mass")
    print("4. J_sub to gravitate by being a pure wind or preferred-frame flow")
    print("5. J_exch to repair ordinary source routing or boundary leakage")
    print("6. Sigma/R zero-net language to replace source and relaxation operators")
    print("7. Sigma/R, R_V, or J_exch to tune M_ext after recovery failure")
    print("8. u_vac to be chosen from Schwarzschild/PPN/gamma_like/AB recovery")
    print("9. O to enforce current neutrality without domain/kernel/image/boundary law")

    with out.unresolved_obligations():
        out.line(
            "derive vacuum-current mass-neutrality theorem",
            StatusMark.OBLIGATION,
            "show J_V/J_sub/J_exch have no independent A-flux shift, scalar charge, far-zone current flux, boundary repair, or ordinary matter rerouting",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("The reduced diagnostics are:")
    print()
    print("  phi_JV = C_JV/r       -> F_phi_JV = -4*pi*C_JV")
    print("  j^r = I/(4*pi*r^2)   -> sphere current flux = I")
    print("  zero-net exchange     -> Sigma_0 - R_0 = 0")
    print()
    print("Therefore ordinary-sector vacuum-current neutrality requires:")
    print()
    print("  C_JV = 0 for scalar residue silence")
    print("  I_V = I_sub = I_exch = 0 for no independent far-zone current flux")
    print("  Sigma/R operators before any zero-net exchange claim")
    print("  no boundary repair, source repair, matter rerouting, preferred-frame force, or recovery-chosen u_vac")
    print()
    print("This script does not define J_V, J_sub, J_exch, Sigma/R, or u_vac.")
    print("It records the current theorem burden and keeps vacuum currents role-level.")
    print()
    print("Possible next script:")
    print("  candidate_curvature_accounting_mass_neutrality.py")

    with out.governance_assessments():
        out.line(
            "vacuum-current mass-neutrality audit complete",
            StatusMark.PASS,
            "J_V remains unresolved; J_sub/J_exch remain role-level; zero-net and zero-creation branches remain theorem-targeted",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, exprs: JVExpressionSet) -> None:
    ns.record_derivation(
        derivation_id="JV_scalar_residue_flux_21",
        inputs=[exprs.phi_JV, exprs.r, exprs.C_JV],
        output=exprs.F_phi_JV,
        method="F_phi_JV = simplify(4*pi*r**2*diff(C_JV/r, r))",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="surface_flux",
        scope="reduced ordinary exterior J_V scalar residue diagnostic",
    )
    ns.record_derivation(
        derivation_id="JV_scalar_residue_A_like_mass_shift_21",
        inputs=[exprs.F_phi_JV, exprs.c, exprs.G],
        output=exprs.delta_M_JV_like,
        method="delta_M_JV_like = simplify(c**2*F_phi_JV/(8*pi*G))",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="mass_shift_diagnostic",
        scope="danger diagnostic only; not a licensed J_V mass law",
    )
    ns.record_derivation(
        derivation_id="JV_far_zone_current_flux_diagnostic_21",
        inputs=[exprs.j_V_radial, exprs.r, exprs.I_V],
        output=exprs.Phi_JV,
        method="Phi_JV = simplify(4*pi*r**2*(I_V/(4*pi*r**2)))",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="current_flux_diagnostic",
        scope="far-zone vacuum-current diagnostic only",
    )
    ns.record_derivation(
        derivation_id="Jsub_far_zone_current_flux_diagnostic_21",
        inputs=[exprs.j_sub_radial, exprs.r, exprs.I_sub],
        output=exprs.Phi_Jsub,
        method="Phi_Jsub = simplify(4*pi*r**2*(I_sub/(4*pi*r**2)))",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="current_flux_diagnostic",
        scope="far-zone substrate-current diagnostic only",
    )
    ns.record_derivation(
        derivation_id="Jexch_far_zone_current_flux_diagnostic_21",
        inputs=[exprs.j_exch_radial, exprs.r, exprs.I_exch],
        output=exprs.Phi_Jexch,
        method="Phi_Jexch = simplify(4*pi*r**2*(I_exch/(4*pi*r**2)))",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="current_flux_diagnostic",
        scope="far-zone exchange-current diagnostic only",
    )
    ns.record_derivation(
        derivation_id="Sigma_R_zero_net_exchange_diagnostic_21",
        inputs=[exprs.Sigma_0, exprs.R_0],
        output=exprs.net_exchange,
        method="net_exchange = simplify(Sigma_0 - R_0)",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="zero_net_condition_diagnostic",
        scope="role-level exchange diagnostic only; not an operator derivation",
    )


def record_inventory_marker(ns, entries: List[CurrentConditionEntry]) -> None:
    names = [sp.Symbol(entry.name.split(":", 1)[0].replace("-", "_").replace(" ", "_")) for entry in entries]
    ns.record_derivation(
        derivation_id="JV_mass_neutrality_inventory_marker_21",
        inputs=names,
        output=sp.Symbol("JV_mass_neutrality_conditions_stated"),
        method="J_V/J_sub/J_exch mass-neutrality condition and rejected-route inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="inventory_marker",
        scope="Group 21 source routing and mass neutrality",
        is_placeholder=True,
    )


def record_obligations(ns, entries: List[CurrentConditionEntry], routes: List[RejectedCurrentRoute]) -> None:
    for entry in entries:
        if entry.obligation_id is None:
            continue
        ns.record_obligation(ProofObligationRecord(
            obligation_id=entry.obligation_id,
            script_id=SCRIPT_ID,
            title=f"Resolve vacuum-current condition: {entry.name}",
            status=ObligationStatus.OPEN,
            required_by=["vacuum_current_mass_neutrality_theorem_21"],
            description=(
                f"Sector: {entry.sector}. Allowed condition: {entry.allowed_condition}. "
                f"Forbidden condition: {entry.forbidden_condition}. Consequence: {entry.consequence}."
            ),
        ))

    for route in routes:
        if route.obligation_id is None:
            continue
        ns.record_obligation(ProofObligationRecord(
            obligation_id=route.obligation_id,
            script_id=SCRIPT_ID,
            title=f"Preserve rejection: {route.name}",
            status=ObligationStatus.OPEN,
            required_by=["vacuum_current_mass_neutrality_theorem_21"],
            description=(
                f"Route: {route.route}. Forbidden use: {route.forbidden_use}. "
                f"Consequence: {route.consequence}."
            ),
        ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="vacuum_current_mass_neutrality_theorem_21",
        script_id=SCRIPT_ID,
        title="Derive vacuum-current mass-neutrality theorem",
        status=ObligationStatus.OPEN,
        required_by=["ordinary_closed_regime_mass_neutrality_theorem_21"],
        description=(
            "Show J_V, J_sub, and J_exch have no independent A-flux shift, no exterior scalar charge, "
            "no far-zone current flux, no boundary repair, no scalar trace source, no ordinary matter push, "
            "and no source rerouting unless a future parent/source law derives otherwise."
        ),
    ))


def record_governance(
    ns,
    entries: List[CurrentConditionEntry],
    routes: List[RejectedCurrentRoute],
) -> None:
    obligation_ids = [entry.obligation_id for entry in entries if entry.obligation_id is not None]
    obligation_ids.extend(route.obligation_id for route in routes if route.obligation_id is not None)
    obligation_ids.append("vacuum_current_mass_neutrality_theorem_21")

    ns.record_route(RouteRecord(
        route_id="vacuum_current_mass_neutrality_audit_route_21",
        script_id=SCRIPT_ID,
        name="J_V / J_sub / J_exch mass-neutrality audit route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "A-sector mass charge remains the reduced ordinary exterior reference",
            "J_V remains unresolved until current definition, source side, domain, and flux direction are derived",
            "J_sub/J_exch remain role-level until pure-wind neutrality and exchange source/support laws are derived",
            "no scalar residue, far-zone current flux, boundary repair, source repair, recovery-chosen u_vac, or active O is assumed",
        ],
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_JV_mass_carrier_route_21",
        script_id=SCRIPT_ID,
        branch_id="JV_exterior_mass_carrier",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "define_JV_current_law_21",
            "derive_JV_no_scalar_residue_21",
            "derive_JV_far_zone_flux_neutrality_21",
            "vacuum_current_mass_neutrality_theorem_21",
        ],
        description=(
            "J_V is deferred as an exterior mass carrier until a current definition, flux law, source side, domain, "
            "boundary behavior, scalar neutrality, and A-sector mass neutrality are derived."
        ),
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="keep_Jsub_role_level_21",
        script_id=SCRIPT_ID,
        branch_id="Jsub_pure_wind_branch",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "derive_Jsub_pure_wind_neutrality_21",
            "derive_Jsub_no_scalar_trace_21",
            "reject_Jsub_boundary_repair_21",
        ],
        description=(
            "J_sub remains role-level pure-wind bookkeeping unless pure-wind neutrality, no scalar trace, "
            "no matter push, and no boundary repair are derived."
        ),
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="keep_Jexch_role_level_21",
        script_id=SCRIPT_ID,
        branch_id="Jexch_exchange_current_branch",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "derive_Jexch_source_support_law_21",
            "reject_Jexch_repair_current_21",
            "derive_sigma_R_zero_net_ordinary_branch_21",
        ],
        description=(
            "J_exch remains role-level exchange bookkeeping unless exchange source/support laws, zero-net or zero-creation "
            "ordinary behavior, and no repair/source-rerouting conditions are derived."
        ),
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_vacuum_current_repair_routes_21",
        script_id=SCRIPT_ID,
        branch_id="vacuum_current_repair_routes",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[route.obligation_id for route in routes if route.obligation_id is not None],
        description=(
            "Reject undefined J_V mass current, J_V scalar tail, pure-wind gravity, exchange repair current, "
            "Sigma/R tuning knob, and recovery-chosen u_vac as ordinary mass-neutrality routes."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="vacuum_current_mass_neutrality_conditions_21",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "J_V, J_sub, and J_exch are not licensed as ordinary exterior mass carriers in Group 21. "
            "They must remain unresolved/role-level/diagnostic or prove no A-flux shift, no scalar residue, "
            "no far-zone current flux, no boundary repair, and no ordinary matter rerouting."
        ),
        derivation_ids=[
            "JV_scalar_residue_flux_21",
            "JV_far_zone_current_flux_diagnostic_21",
            "Jsub_far_zone_current_flux_diagnostic_21",
            "Jexch_far_zone_current_flux_diagnostic_21",
            "Sigma_R_zero_net_exchange_diagnostic_21",
        ],
        obligation_ids=obligation_ids,
    ))

    ns.record_claim(ClaimRecord(
        claim_id="vacuum_current_repair_routes_rejected_21",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Vacuum-current labels may not be used as repair mechanisms: J_V cannot be undefined mass current, "
            "J_sub cannot gravitate by pure wind, J_exch cannot repair ordinary routing, Sigma/R cannot tune mass, "
            "and u_vac cannot be selected from recovery."
        ),
        derivation_ids=[
            "JV_scalar_residue_flux_21",
            "Sigma_R_zero_net_exchange_diagnostic_21",
        ],
        obligation_ids=[route.obligation_id for route in routes if route.obligation_id is not None],
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate J_V Mass Neutrality Conditions")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    exprs = build_expressions()
    entries = build_condition_entries()
    routes = build_rejected_routes()

    case_0_problem_statement(out)
    case_1_JV_scalar_residue(exprs, out)
    case_2_far_zone_current_flux(exprs, out)
    case_3_zero_net_exchange(exprs, out)
    case_4_current_condition_ledger(entries, out)
    case_5_rejected_current_routes(routes, out)
    case_6_failure_controls(out)
    final_interpretation(out)

    record_derivations(ns, exprs)
    record_inventory_marker(ns, entries)
    record_obligations(ns, entries, routes)
    record_governance(ns, entries, routes)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
