# Candidate zeta/kappa mass neutrality conditions
#
# Group:
#   21_source_routing_and_mass_neutrality
#
# Script type:
#   DERIVATION / DIAGNOSTIC / REQUIREMENTS
#
# Purpose
# -------
# Apply the Group 21 mass-neutrality rules to the residual trace variables
# zeta and kappa.
#
# Locked-door question:
#
#   Under what conditions can zeta/kappa exist without shifting exterior mass?
#
# This script does not derive the zeta insertion law, a kappa field equation,
# residual-kill, no-overlap, Box zeta, Box kappa, boundary neutrality, or a
# parent mass theorem.
#
# It derives the reduced warning identities for exterior residual tails:
#
#   zeta_tail  = C_zeta/r
#   kappa_tail = C_kappa/r
#
# with surface fluxes:
#
#   F_zeta  = -4*pi*C_zeta
#   F_kappa = -4*pi*C_kappa
#
# If either tail is allowed to behave as an A-like exterior mass contribution,
# the equivalent mass shift would be:
#
#   delta M ~ -c^2*C/(2*G)
#
# Therefore ordinary-sector residual zeta/kappa can be safe only if they are
# non-metric, killed/suppressed, compact-neutral, or exterior-neutral with
# vanishing 1/r coefficients. Cancellation between residual tails is not a
# theorem and is treated as a rejected repair route unless derived by a future
# parent identity with no double counting.

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
        dependency_id="residual_scalar_tail_flux_dependency_21",
        upstream_script_id="21_source_routing_and_mass_neutrality__candidate_residual_scalar_tail_flux_audit",
        upstream_derivation_id="residual_scalar_tail_flux_1_over_r_21",
        expected_record_kind=RecordKind.DERIVATION,
    )
    ns.declare_dependency(
        dependency_id="boundary_tail_delta_A_flux_dependency_21",
        upstream_script_id="21_source_routing_and_mass_neutrality__candidate_boundary_flux_mass_preservation",
        upstream_derivation_id="boundary_tail_delta_A_flux_21",
        expected_record_kind=RecordKind.DERIVATION,
    )
    ns.declare_dependency(
        dependency_id="boundary_mass_preservation_inventory_dependency_21",
        upstream_script_id="21_source_routing_and_mass_neutrality__candidate_boundary_flux_mass_preservation",
        upstream_derivation_id="boundary_flux_mass_preservation_inventory_marker_21",
        expected_record_kind=RecordKind.INVENTORY_MARKER,
    )
    ns.declare_dependency(
        dependency_id="A_sector_mass_definition_dependency_21",
        upstream_script_id="21_source_routing_and_mass_neutrality__candidate_A_sector_mass_charge_definition",
        upstream_derivation_id="A_sector_mass_definition_21",
        expected_record_kind=RecordKind.DERIVATION,
    )

    return archive, ns, invalidated


def status_mark(status: str) -> StatusMark:
    return {
        "DERIVED_REDUCED": StatusMark.PASS,
        "DIAGNOSTIC": StatusMark.INFO,
        "REQUIRED": StatusMark.OBLIGATION,
        "THEOREM_TARGET": StatusMark.DEFER,
        "REJECTED": StatusMark.FAIL,
        "SAFE_IF": StatusMark.INFO,
        "UNRESOLVED": StatusMark.DEFER,
        "RISK": StatusMark.WARN,
        "PROVISIONAL": StatusMark.INFO,
        "NOT_INSERTABLE": StatusMark.FAIL,
    }.get(status, StatusMark.INFO)


# =============================================================================
# Data models
# =============================================================================


@dataclass
class ZetaKappaExpressionSet:
    r: sp.Symbol
    G: sp.Symbol
    c: sp.Symbol
    C_zeta: sp.Symbol
    C_kappa: sp.Symbol
    zeta_tail: sp.Expr
    kappa_tail: sp.Expr
    F_zeta: sp.Expr
    F_kappa: sp.Expr
    zeta_flux_residual: sp.Expr
    kappa_flux_residual: sp.Expr
    delta_M_zeta_like: sp.Expr
    delta_M_kappa_like: sp.Expr
    zeta_mass_residual: sp.Expr
    kappa_mass_residual: sp.Expr
    combined_tail: sp.Expr
    combined_flux: sp.Expr
    combined_flux_residual: sp.Expr
    cancellation_condition: sp.Equality
    independent_zero_residuals: sp.Matrix


@dataclass
class ZetaKappaConditionEntry:
    name: str
    sector: str
    status: str
    allowed_condition: str
    forbidden_condition: str
    consequence: str
    obligation_id: str | None = None


@dataclass
class RejectedResidualRoute:
    name: str
    route: str
    forbidden_use: str
    consequence: str


# =============================================================================
# Symbolic construction
# =============================================================================


def build_zeta_kappa_expressions() -> ZetaKappaExpressionSet:
    r = sp.Symbol("r", positive=True)
    G = sp.Symbol("G", positive=True)
    c = sp.Symbol("c", positive=True)
    C_zeta = sp.Symbol("C_zeta", real=True)
    C_kappa = sp.Symbol("C_kappa", real=True)

    zeta_tail = C_zeta / r
    kappa_tail = C_kappa / r

    F_zeta = sp.simplify(4 * sp.pi * r**2 * sp.diff(zeta_tail, r))
    F_kappa = sp.simplify(4 * sp.pi * r**2 * sp.diff(kappa_tail, r))
    zeta_flux_residual = sp.simplify(F_zeta + 4 * sp.pi * C_zeta)
    kappa_flux_residual = sp.simplify(F_kappa + 4 * sp.pi * C_kappa)

    delta_M_zeta_like = sp.simplify((c**2 / (8 * sp.pi * G)) * F_zeta)
    delta_M_kappa_like = sp.simplify((c**2 / (8 * sp.pi * G)) * F_kappa)
    zeta_mass_residual = sp.simplify(delta_M_zeta_like + c**2 * C_zeta / (2 * G))
    kappa_mass_residual = sp.simplify(delta_M_kappa_like + c**2 * C_kappa / (2 * G))

    combined_tail = sp.simplify(zeta_tail + kappa_tail)
    combined_flux = sp.simplify(4 * sp.pi * r**2 * sp.diff(combined_tail, r))
    combined_flux_residual = sp.simplify(combined_flux + 4 * sp.pi * (C_zeta + C_kappa))
    cancellation_condition = sp.Eq(C_zeta + C_kappa, 0)
    independent_zero_residuals = sp.Matrix([C_zeta, C_kappa])

    return ZetaKappaExpressionSet(
        r=r,
        G=G,
        c=c,
        C_zeta=C_zeta,
        C_kappa=C_kappa,
        zeta_tail=zeta_tail,
        kappa_tail=kappa_tail,
        F_zeta=F_zeta,
        F_kappa=F_kappa,
        zeta_flux_residual=zeta_flux_residual,
        kappa_flux_residual=kappa_flux_residual,
        delta_M_zeta_like=delta_M_zeta_like,
        delta_M_kappa_like=delta_M_kappa_like,
        zeta_mass_residual=zeta_mass_residual,
        kappa_mass_residual=kappa_mass_residual,
        combined_tail=combined_tail,
        combined_flux=combined_flux,
        combined_flux_residual=combined_flux_residual,
        cancellation_condition=cancellation_condition,
        independent_zero_residuals=independent_zero_residuals,
    )


def build_condition_entries() -> List[ZetaKappaConditionEntry]:
    return [
        ZetaKappaConditionEntry(
            name="ZK1: zeta residual non-metric branch",
            sector="zeta_residual",
            status="SAFE_IF",
            allowed_condition="zeta residual is strictly non-metric / diagnostic and has no source, flux, or A-effect",
            forbidden_condition="zeta residual becomes a metric scalar source or second mass channel",
            consequence="safest current zeta residual route; still requires bookkeeping discipline",
            obligation_id="derive_zeta_nonmetric_bookkeeping_rule_21",
        ),
        ZetaKappaConditionEntry(
            name="ZK2: zeta residual exterior-neutral branch",
            sector="zeta_residual",
            status="THEOREM_TARGET",
            allowed_condition="C_zeta = 0 outside, with no boundary shell and no recovery-tuned support",
            forbidden_condition="zeta_tail = C_zeta/r with C_zeta != 0",
            consequence="neutral zeta metric trace is theorem-heavy but not logically forbidden",
            obligation_id="derive_zeta_residual_C_zero_21",
        ),
        ZetaKappaConditionEntry(
            name="ZK3: zeta residual metric 1/r tail",
            sector="zeta_residual",
            status="REJECTED",
            allowed_condition="never in ordinary exterior unless routed by a future A-sector theorem without double counting",
            forbidden_condition="nonzero zeta 1/r tail treated as ordinary exterior scalar charge",
            consequence="zeta cannot carry the ordinary exterior mass coin by declaration",
            obligation_id="reject_zeta_scalar_tail_mass_route_21",
        ),
        ZetaKappaConditionEntry(
            name="ZK4: kappa suppressed exterior branch",
            sector="kappa_residual",
            status="SAFE_IF",
            allowed_condition="kappa is suppressed or killed before ordinary exterior, with no exterior 1/r tail",
            forbidden_condition="kappa leak repairs boundary mismatch or changes AB/recovery",
            consequence="matches the current reduced exterior discipline: kappa remains suppressed/diagnostic",
            obligation_id="derive_kappa_exterior_suppression_21",
        ),
        ZetaKappaConditionEntry(
            name="ZK5: kappa residual exterior-neutral branch",
            sector="kappa_residual",
            status="THEOREM_TARGET",
            allowed_condition="C_kappa = 0 outside, with no boundary shell and no recovery-tuned support",
            forbidden_condition="kappa_tail = C_kappa/r with C_kappa != 0",
            consequence="neutral kappa residual metric trace is theorem-heavy but possible as a target",
            obligation_id="derive_kappa_residual_C_zero_21",
        ),
        ZetaKappaConditionEntry(
            name="ZK6: kappa residual metric 1/r tail",
            sector="kappa_residual",
            status="REJECTED",
            allowed_condition="never in ordinary exterior unless routed by a future A-sector theorem without double counting",
            forbidden_condition="nonzero kappa 1/r tail treated as exterior scalar mass response",
            consequence="kappa leak is scalar-silence and equal-response danger",
            obligation_id="reject_kappa_scalar_tail_mass_route_21",
        ),
        ZetaKappaConditionEntry(
            name="ZK7: e_kappa diagnostic stiffness",
            sector="e_kappa",
            status="SAFE_IF",
            allowed_condition="e_kappa remains stiffness/diagnostic bookkeeping and does not source A or exterior kappa",
            forbidden_condition="e_kappa becomes a source reservoir or boundary mass purse",
            consequence="kappa energy may suppress imbalance but cannot add mass charge",
            obligation_id="derive_e_kappa_source_neutrality_21",
        ),
        ZetaKappaConditionEntry(
            name="ZK8: epsilon_vac_config accounting",
            sector="epsilon_vac_config",
            status="SAFE_IF",
            allowed_condition="configuration energy remains diagnostic/accounting or receives independent source-neutral law",
            forbidden_condition="configuration label becomes mass energy or boundary repair by vocabulary",
            consequence="configuration bookkeeping cannot shift M_A without a source theorem",
            obligation_id="derive_epsilon_vac_config_mass_neutrality_21",
        ),
        ZetaKappaConditionEntry(
            name="ZK9: zeta/kappa cancellation branch",
            sector="zeta_residual + kappa_residual",
            status="REJECTED",
            allowed_condition="not licensed; future parent theorem would need sector source routing and no double counting",
            forbidden_condition="C_zeta + C_kappa = 0 used to hide nonzero residual scalar pockets",
            consequence="cancellation is not sector neutrality; each pocket must be empty or non-metric",
            obligation_id="reject_zeta_kappa_scalar_tail_cancellation_21",
        ),
        ZetaKappaConditionEntry(
            name="ZK10: residual-kill / non-metric convention",
            sector="zeta_residual + kappa_residual",
            status="PROVISIONAL",
            allowed_condition="residual metric trace is killed or demoted before source/metric effect",
            forbidden_condition="residual-kill is treated as a derived no-overlap theorem",
            consequence="safest current convention, but still provisional",
            obligation_id="derive_residual_kill_no_metric_trace_21",
        ),
        ZetaKappaConditionEntry(
            name="ZK11: Box zeta / Box kappa route",
            sector="zeta_residual + kappa_residual",
            status="REJECTED",
            allowed_condition="not in ordinary exterior as a scalar Poisson route",
            forbidden_condition="Box zeta or Box kappa produces a long-range ordinary scalar charge",
            consequence="ordinary scalar radiation/source channel remains rejected unless separately derived",
            obligation_id="reject_box_zeta_box_kappa_ordinary_scalar_route_21",
        ),
        ZetaKappaConditionEntry(
            name="ZK12: B_s / zeta insertion dependency",
            sector="B_s / zeta insertion",
            status="THEOREM_TARGET",
            allowed_condition="derive insertion with residual-kill or neutral residual trace and delta M_A = 0",
            forbidden_condition="B_s or zeta insertion chosen from gamma_like, AB, B=1/A, or recovery target",
            consequence="B_s/F_zeta insertion remains outside this script's license",
            obligation_id="derive_Bs_zeta_insertion_mass_neutrality_21",
        ),
    ]


def build_rejected_routes() -> List[RejectedResidualRoute]:
    return [
        RejectedResidualRoute(
            name="RZK1: nonzero zeta exterior tail",
            route="zeta_tail_mass_route",
            forbidden_use="C_zeta/r treated as an ordinary exterior scalar mass channel",
            consequence="zeta residual must be non-metric, killed, compact-neutral, or C_zeta = 0",
        ),
        RejectedResidualRoute(
            name="RZK2: nonzero kappa exterior tail",
            route="kappa_tail_mass_route",
            forbidden_use="C_kappa/r treated as an ordinary exterior scalar mass channel",
            consequence="kappa residual must be suppressed, non-metric, compact-neutral, or C_kappa = 0",
        ),
        RejectedResidualRoute(
            name="RZK3: residual cancellation by hand",
            route="zeta_kappa_tail_cancellation",
            forbidden_use="C_zeta + C_kappa = 0 used to hide nonzero sector tails",
            consequence="cancellation is not mass neutrality unless a future parent identity derives it",
        ),
        RejectedResidualRoute(
            name="RZK4: Box zeta / Box kappa scalar source",
            route="box_zeta_box_kappa_scalar_source",
            forbidden_use="ordinary exterior scalar Poisson channel introduced for zeta/kappa",
            consequence="no ordinary long-range residual scalar charge is licensed",
        ),
        RejectedResidualRoute(
            name="RZK5: residual relaxation repairs A-flux",
            route="residual_relaxation_A_flux_repair",
            forbidden_use="residual relaxation changes exterior A-flux or boundary slope to save recovery",
            consequence="residual relaxation is not a boundary purse",
        ),
        RejectedResidualRoute(
            name="RZK6: recovery-chosen residual status",
            route="recovery_chosen_residual_status",
            forbidden_use="zeta/kappa residual role chosen from Schwarzschild, PPN, gamma_like, AB, or B=1/A",
            consequence="recovery remains downstream, not a residual-routing rule",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: zeta/kappa mass-neutrality problem")
    print("Question:")
    print()
    print("  Under what conditions can zeta/kappa exist without shifting exterior mass?")
    print()
    print("Reference discipline:")
    print()
    print("  A-sector mass charge remains the reduced ordinary exterior reference.")
    print("  zeta may be a volume-form candidate but is not a mass route by declaration.")
    print("  kappa remains diagnostic / suppressed / non-metric unless a source law derives otherwise.")
    print("  No Box zeta, no Box kappa, no exterior zeta/kappa 1/r tail, no residual cancellation by hand.")
    print("  This script records reduced flux witnesses and conditions, not a residual-neutrality theorem.")

    with out.governance_assessments():
        out.line(
            "zeta/kappa mass-neutrality audit opened",
            StatusMark.INFO,
            "testing residual trace variables against A-sector mass neutrality and scalar silence",
        )


def case_1_individual_tail_flux(exprs: ZetaKappaExpressionSet, out: ScriptOutput) -> None:
    header("Case 1: Individual zeta/kappa exterior-tail flux")
    print("Take residual exterior tails:")
    print()
    print(f"  zeta_tail(r)  = {sp.sstr(exprs.zeta_tail)}")
    print(f"  kappa_tail(r) = {sp.sstr(exprs.kappa_tail)}")
    print()
    print("Then their reduced surface fluxes are:")
    print()
    print(f"  F_zeta  = 4*pi*r^2*zeta_tail'  = {sp.sstr(exprs.F_zeta)}")
    print(f"  F_kappa = 4*pi*r^2*kappa_tail' = {sp.sstr(exprs.F_kappa)}")
    print()
    print("Flux residual checks:")
    print()
    print(f"  F_zeta + 4*pi*C_zeta = {sp.sstr(exprs.zeta_flux_residual)}")
    print(f"  F_kappa + 4*pi*C_kappa = {sp.sstr(exprs.kappa_flux_residual)}")
    print()
    print("Exterior scalar silence requires independent vanishing coefficients:")
    print()
    print("  C_zeta = 0")
    print("  C_kappa = 0")

    with out.derived_results():
        out.line(
            "zeta 1/r tail flux derived",
            StatusMark.PASS if is_zero(exprs.zeta_flux_residual) else StatusMark.FAIL,
            f"F_zeta = {sp.sstr(exprs.F_zeta)}",
        )
        out.line(
            "kappa 1/r tail flux derived",
            StatusMark.PASS if is_zero(exprs.kappa_flux_residual) else StatusMark.FAIL,
            f"F_kappa = {sp.sstr(exprs.F_kappa)}",
        )
        out.line(
            "independent zeta/kappa scalar silence condition stated",
            StatusMark.PASS,
            "ordinary exterior requires C_zeta = 0 and C_kappa = 0 unless residuals are non-metric/diagnostic",
        )


def case_2_A_like_mass_shift_diagnostic(exprs: ZetaKappaExpressionSet, out: ScriptOutput) -> None:
    header("Case 2: A-like mass-shift diagnostic")
    print("If a residual scalar tail is incorrectly allowed to behave as an A-like exterior mass contribution:")
    print()
    print(f"  delta_M_zeta_like  = c^2*F_zeta/(8*pi*G)  = {sp.sstr(exprs.delta_M_zeta_like)}")
    print(f"  delta_M_kappa_like = c^2*F_kappa/(8*pi*G) = {sp.sstr(exprs.delta_M_kappa_like)}")
    print()
    print("Mass residual checks:")
    print()
    print(f"  delta_M_zeta_like + c^2*C_zeta/(2*G) = {sp.sstr(exprs.zeta_mass_residual)}")
    print(f"  delta_M_kappa_like + c^2*C_kappa/(2*G) = {sp.sstr(exprs.kappa_mass_residual)}")
    print()
    print("Interpretation:")
    print()
    print("  This is a danger diagnostic, not a licensed mass law.")
    print("  It shows the mass-equivalent size of the leak if zeta/kappa were allowed to enter A-like flux.")

    with out.derived_results():
        out.line(
            "zeta A-like mass-shift diagnostic derived",
            StatusMark.PASS if is_zero(exprs.zeta_mass_residual) else StatusMark.FAIL,
            f"delta_M_zeta_like = {sp.sstr(exprs.delta_M_zeta_like)}",
        )
        out.line(
            "kappa A-like mass-shift diagnostic derived",
            StatusMark.PASS if is_zero(exprs.kappa_mass_residual) else StatusMark.FAIL,
            f"delta_M_kappa_like = {sp.sstr(exprs.delta_M_kappa_like)}",
        )


def case_3_combined_tail_cancellation_diagnostic(exprs: ZetaKappaExpressionSet, out: ScriptOutput) -> None:
    header("Case 3: Combined-tail cancellation diagnostic")
    print("Combined residual tail:")
    print()
    print(f"  phi_zk(r) = zeta_tail + kappa_tail = {sp.sstr(exprs.combined_tail)}")
    print()
    print("Combined surface flux:")
    print()
    print(f"  F_zk = {sp.sstr(exprs.combined_flux)}")
    print()
    print("Residual check:")
    print()
    print(f"  F_zk + 4*pi*(C_zeta + C_kappa) = {sp.sstr(exprs.combined_flux_residual)}")
    print()
    print("A total-flux cancellation condition would be:")
    print()
    print(f"  {sp.sstr(exprs.cancellation_condition)}")
    print()
    print("But this is not sector neutrality:")
    print()
    print("  C_zeta = -C_kappa can hide nonzero residual scalar pockets.")
    print("  Group 21 requires empty pockets, non-metric residuals, or a future parent theorem.")

    with out.derived_results():
        out.line(
            "combined zeta/kappa residual flux derived",
            StatusMark.PASS if is_zero(exprs.combined_flux_residual) else StatusMark.FAIL,
            f"F_zk = {sp.sstr(exprs.combined_flux)}",
        )
    with out.counterexamples():
        out.line(
            "zeta/kappa cancellation by hand rejected",
            StatusMark.FAIL,
            "C_zeta + C_kappa = 0 is not the same as C_zeta = C_kappa = 0",
        )


def case_4_condition_ledger(entries: List[ZetaKappaConditionEntry], out: ScriptOutput) -> None:
    header("Case 4: zeta/kappa condition ledger")
    for entry in entries:
        print()
        print("-" * 120)
        print(entry.name)
        print("-" * 120)
        print(f"Sector: {entry.sector}")
        print(f"Allowed condition: {entry.allowed_condition}")
        print(f"Forbidden condition: {entry.forbidden_condition}")
        print(f"[{status_mark(entry.status).value}] {entry.name}: {entry.status}")
        print(f"Consequence: {entry.consequence}")

    with out.governance_assessments():
        out.line(
            "zeta/kappa condition ledger populated",
            StatusMark.PASS,
            f"{len(entries)} residual trace conditions classified for mass-neutrality burden",
        )


def case_5_rejected_routes(routes: List[RejectedResidualRoute], out: ScriptOutput) -> None:
    header("Case 5: Rejected zeta/kappa residual routes")
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
            "zeta/kappa residual mass routes rejected",
            StatusMark.FAIL,
            "nonzero residual tails, cancellation, Box routes, repair relaxation, and recovery-chosen residual status are not licensed",
        )


def case_6_failure_controls(out: ScriptOutput) -> None:
    header("Case 6: Failure controls")
    print("The zeta/kappa mass-neutrality audit fails if a later script allows:")
    print()
    print("1. zeta residual metric trace with C_zeta/r outside and C_zeta != 0")
    print("2. kappa residual metric trace with C_kappa/r outside and C_kappa != 0")
    print("3. C_zeta + C_kappa = 0 cancellation to stand in for sector neutrality")
    print("4. Box zeta or Box kappa as ordinary exterior scalar source laws")
    print("5. e_kappa or epsilon_vac_config to become a source reservoir")
    print("6. residual relaxation to alter A-flux or repair boundary mismatch")
    print("7. residual-kill to be treated as a derived no-overlap theorem")
    print("8. B_s/zeta insertion to be chosen from gamma_like, AB, B=1/A, PPN, or Schwarzschild recovery")
    print("9. O to enforce zeta/kappa neutrality without domain/kernel/image/boundary law")

    with out.unresolved_obligations():
        out.line(
            "derive zeta/kappa residual mass-neutrality theorem",
            StatusMark.OBLIGATION,
            "show residual trace variables are non-metric, killed/suppressed, compact-neutral, or have vanishing exterior 1/r coefficients",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("The reduced flux witness is:")
    print()
    print("  zeta_tail = C_zeta/r  ->  F_zeta = -4*pi*C_zeta")
    print("  kappa_tail = C_kappa/r -> F_kappa = -4*pi*C_kappa")
    print()
    print("Therefore ordinary exterior mass neutrality requires:")
    print()
    print("  C_zeta = 0 and C_kappa = 0")
    print()
    print("unless the residuals are strictly non-metric/diagnostic, killed/suppressed, compact-neutral,")
    print("or routed through a future parent identity that avoids double counting.")
    print()
    print("The safest current convention remains:")
    print()
    print("  residual-kill / non-metric residual for zeta/kappa trace leftovers.")
    print()
    print("Neutral residual metric trace remains theorem-heavy.")
    print()
    print("Possible next script:")
    print("  candidate_JV_mass_neutrality_conditions.py")

    with out.governance_assessments():
        out.line(
            "zeta/kappa mass-neutrality audit complete",
            StatusMark.PASS,
            "residual-kill/non-metric residual remains safest; neutral metric trace remains theorem-targeted",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, exprs: ZetaKappaExpressionSet) -> None:
    ns.record_derivation(
        derivation_id="zeta_residual_tail_flux_21",
        inputs=[exprs.zeta_tail, exprs.r, exprs.C_zeta],
        output=exprs.F_zeta,
        method="F_zeta = simplify(4*pi*r**2*diff(C_zeta/r, r))",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="surface_flux",
        scope="reduced ordinary exterior residual-tail diagnostic",
    )

    ns.record_derivation(
        derivation_id="kappa_residual_tail_flux_21",
        inputs=[exprs.kappa_tail, exprs.r, exprs.C_kappa],
        output=exprs.F_kappa,
        method="F_kappa = simplify(4*pi*r**2*diff(C_kappa/r, r))",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="surface_flux",
        scope="reduced ordinary exterior residual-tail diagnostic",
    )

    ns.record_derivation(
        derivation_id="zeta_residual_A_like_mass_shift_21",
        inputs=[exprs.F_zeta, exprs.c, exprs.G],
        output=exprs.delta_M_zeta_like,
        method="delta_M_zeta_like = simplify(c**2*F_zeta/(8*pi*G))",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="mass_shift_diagnostic",
        scope="danger diagnostic only; not a licensed zeta mass law",
    )

    ns.record_derivation(
        derivation_id="kappa_residual_A_like_mass_shift_21",
        inputs=[exprs.F_kappa, exprs.c, exprs.G],
        output=exprs.delta_M_kappa_like,
        method="delta_M_kappa_like = simplify(c**2*F_kappa/(8*pi*G))",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="mass_shift_diagnostic",
        scope="danger diagnostic only; not a licensed kappa mass law",
    )

    ns.record_derivation(
        derivation_id="zeta_kappa_combined_tail_flux_21",
        inputs=[exprs.combined_tail, exprs.r, exprs.C_zeta, exprs.C_kappa],
        output=exprs.combined_flux,
        method="F_zk = simplify(4*pi*r**2*diff((C_zeta+C_kappa)/r, r))",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="surface_flux",
        scope="combined residual-tail cancellation diagnostic",
    )

    ns.record_derivation(
        derivation_id="zeta_kappa_combined_tail_flux_residual_21",
        inputs=[exprs.combined_flux, exprs.C_zeta, exprs.C_kappa],
        output=exprs.combined_flux_residual,
        method="simplify(F_zk + 4*pi*(C_zeta + C_kappa))",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
        scope="combined residual-tail cancellation diagnostic",
    )

    ns.record_derivation(
        derivation_id="zeta_kappa_independent_zero_conditions_21",
        inputs=[exprs.C_zeta, exprs.C_kappa],
        output=exprs.independent_zero_residuals,
        method="independent scalar silence conditions: Matrix([C_zeta, C_kappa]) == 0",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="neutrality_condition",
        scope="ordinary exterior residual scalar silence requirement",
    )

    ns.record_derivation(
        derivation_id="zeta_kappa_tail_cancellation_condition_diagnostic_21",
        inputs=[exprs.C_zeta, exprs.C_kappa],
        output=sp.simplify(exprs.C_zeta + exprs.C_kappa),
        method="diagnostic cancellation condition C_zeta + C_kappa = 0",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="cancellation_condition",
        scope="diagnostic only; not sector neutrality",
    )


def record_inventory_marker(ns, entries: List[ZetaKappaConditionEntry]) -> None:
    names = [sp.Symbol(entry.name.split(":", 1)[0].replace("-", "_").replace(" ", "_")) for entry in entries]
    ns.record_derivation(
        derivation_id="zeta_kappa_mass_neutrality_inventory_marker_21",
        inputs=names,
        output=sp.Symbol("zeta_kappa_mass_neutrality_conditions_stated"),
        method="zeta/kappa residual condition and rejected-route inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="inventory_marker",
        scope="Group 21 source routing and mass neutrality",
        is_placeholder=True,
    )


def record_obligations(ns, entries: List[ZetaKappaConditionEntry]) -> None:
    for entry in entries:
        if entry.obligation_id is None:
            continue
        ns.record_obligation(ProofObligationRecord(
            obligation_id=entry.obligation_id,
            script_id=SCRIPT_ID,
            title=f"Resolve zeta/kappa condition: {entry.name}",
            status=ObligationStatus.OPEN,
            required_by=["zeta_kappa_mass_neutrality_theorem_21"],
            description=(
                f"Sector: {entry.sector}. Allowed condition: {entry.allowed_condition}. "
                f"Forbidden condition: {entry.forbidden_condition}. Consequence: {entry.consequence}."
            ),
        ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_zeta_kappa_no_exterior_tail_21",
        script_id=SCRIPT_ID,
        title="Derive no exterior zeta/kappa residual tail",
        status=ObligationStatus.OPEN,
        required_by=["zeta_kappa_mass_neutrality_theorem_21"],
        description=(
            "Show C_zeta = 0 and C_kappa = 0 outside ordinary sources, or show residuals are strictly non-metric, "
            "diagnostic, killed/suppressed, or compact-neutral with no boundary shell."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_zeta_kappa_no_A_flux_shift_21",
        script_id=SCRIPT_ID,
        title="Derive zeta/kappa no A-flux shift",
        status=ObligationStatus.OPEN,
        required_by=["ordinary_closed_regime_mass_neutrality_theorem_21"],
        description=(
            "Show residual zeta/kappa variables do not alter exterior A-flux, A-sector mass charge, boundary slope, or measured M_ext."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="zeta_kappa_mass_neutrality_theorem_21",
        script_id=SCRIPT_ID,
        title="Derive zeta/kappa mass-neutrality theorem",
        status=ObligationStatus.OPEN,
        required_by=["ordinary_closed_regime_mass_neutrality_theorem_21"],
        description=(
            "Show zeta/kappa residuals are non-metric, killed/suppressed, compact-neutral, or exterior-neutral, "
            "and that e_kappa / epsilon_vac_config do not become source reservoirs."
        ),
    ))


def record_governance(
    ns,
    entries: List[ZetaKappaConditionEntry],
    routes: List[RejectedResidualRoute],
) -> None:
    obligation_ids = [entry.obligation_id for entry in entries if entry.obligation_id is not None]
    obligation_ids.extend([
        "derive_zeta_kappa_no_exterior_tail_21",
        "derive_zeta_kappa_no_A_flux_shift_21",
        "zeta_kappa_mass_neutrality_theorem_21",
    ])

    ns.record_route(RouteRecord(
        route_id="zeta_kappa_mass_neutrality_audit_route_21",
        script_id=SCRIPT_ID,
        name="zeta/kappa mass-neutrality audit route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "A-sector mass charge remains the reduced ordinary exterior reference",
            "zeta/kappa residuals must be non-metric, killed/suppressed, compact-neutral, or C=0 outside",
            "no Box zeta, Box kappa, scalar-tail cancellation, residual repair, recovery tuning, or active O is assumed",
            "B_s/zeta insertion remains theorem-targeted",
        ],
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_zeta_kappa_nonzero_exterior_tail_21",
        script_id=SCRIPT_ID,
        branch_id="zeta_kappa_nonzero_exterior_scalar_tail",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=["derive_zeta_kappa_no_exterior_tail_21"],
        description=(
            "Reject nonzero ordinary exterior zeta/kappa 1/r residual tails. They carry surface flux and can behave as second scalar mass routes."
        ),
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_zeta_kappa_tail_cancellation_by_hand_21",
        script_id=SCRIPT_ID,
        branch_id="zeta_kappa_tail_cancellation_by_hand",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=["reject_zeta_kappa_scalar_tail_cancellation_21"],
        description=(
            "Reject C_zeta + C_kappa = 0 as a substitute for sector neutrality. Cancellation does not prove empty pockets."
        ),
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_box_zeta_box_kappa_ordinary_scalar_route_21",
        script_id=SCRIPT_ID,
        branch_id="box_zeta_box_kappa_ordinary_scalar_route",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=["reject_box_zeta_box_kappa_ordinary_scalar_route_21"],
        description=(
            "Reject Box zeta / Box kappa as ordinary exterior scalar source routes in the current branch."
        ),
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_neutral_zeta_kappa_metric_trace_21",
        script_id=SCRIPT_ID,
        branch_id="neutral_zeta_kappa_metric_trace",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "derive_zeta_residual_C_zero_21",
            "derive_kappa_residual_C_zero_21",
            "derive_zeta_kappa_no_A_flux_shift_21",
            "zeta_kappa_mass_neutrality_theorem_21",
        ],
        description=(
            "Defer neutral zeta/kappa metric trace as a theorem target. It requires exterior scalar silence, boundary neutrality, and no A-flux shift."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="zeta_kappa_tail_flux_rule_21",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.LICENSING,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "For reduced exterior residual tails zeta=C_zeta/r and kappa=C_kappa/r, the surface fluxes are "
            "F_zeta=-4*pi*C_zeta and F_kappa=-4*pi*C_kappa. Ordinary exterior scalar silence requires "
            "C_zeta=0 and C_kappa=0 unless residuals are non-metric/diagnostic or routed by a future theorem."
        ),
        derivation_ids=[
            "zeta_residual_tail_flux_21",
            "kappa_residual_tail_flux_21",
            "zeta_kappa_independent_zero_conditions_21",
        ],
    ))

    ns.record_claim(ClaimRecord(
        claim_id="zeta_kappa_mass_neutrality_requirement_21",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "zeta/kappa residuals may exist only as non-metric, killed/suppressed, compact-neutral, or theorem-targeted objects. "
            "They may not shift M_A, create exterior scalar tails, act as source reservoirs, or repair boundary/recovery failures by declaration."
        ),
        derivation_ids=[
            "zeta_residual_tail_flux_21",
            "kappa_residual_tail_flux_21",
            "zeta_residual_A_like_mass_shift_21",
            "kappa_residual_A_like_mass_shift_21",
        ],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Zeta/Kappa Mass Neutrality Conditions")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    exprs = build_zeta_kappa_expressions()
    entries = build_condition_entries()
    routes = build_rejected_routes()

    case_0_problem_statement(out)
    case_1_individual_tail_flux(exprs, out)
    case_2_A_like_mass_shift_diagnostic(exprs, out)
    case_3_combined_tail_cancellation_diagnostic(exprs, out)
    case_4_condition_ledger(entries, out)
    case_5_rejected_routes(routes, out)
    case_6_failure_controls(out)
    final_interpretation(out)

    record_derivations(ns, exprs)
    record_inventory_marker(ns, entries)
    record_obligations(ns, entries)
    record_governance(ns, entries, routes)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
