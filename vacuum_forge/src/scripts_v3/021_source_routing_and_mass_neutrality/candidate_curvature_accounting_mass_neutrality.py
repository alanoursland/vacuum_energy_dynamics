# Candidate curvature accounting mass neutrality
#
# Group:
#   21_source_routing_and_mass_neutrality
#
# Script type:
#   DERIVATION / DIAGNOSTIC / REQUIREMENTS
#
# Purpose
# -------
# Audit whether curvature admissibility, curvature energy/accounting, or an
# unresolved curvature current can affect the ordinary exterior A-sector mass.
#
# Locked-door question:
#
#   Can curvature admissibility or e_curv affect exterior mass?
#
# This script does not define A_curv, e_curv, J_curv, curvature dynamics,
# curvature balance, anti-singularity dynamics, correction tensors, or a parent
# field equation.
#
# It derives reduced diagnostic witnesses for curvature-accounting leak routes:
#
#   scalar curvature residue: phi_curv = C_curv/r -> F_curv = -4*pi*C_curv
#   e_curv A-tail diagnostic: delta_A_e = q_e/r -> delta_M_e = -c^2*q_e/(2G)
#   far-zone J_curv flux:     j_curv^r = I_curv/(4*pi*r^2) -> Phi_curv = I_curv
#
# The conclusion is deliberately narrow: curvature objects remain diagnostic,
# branch-filter, accounting-only, unresolved, or theorem-targeted unless future
# structure derives source neutrality and mass neutrality.

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
        dependency_id="JV_mass_neutrality_inventory_dependency_21",
        upstream_script_id="021_source_routing_and_mass_neutrality__candidate_JV_mass_neutrality_conditions",
        upstream_derivation_id="JV_mass_neutrality_inventory_marker_21",
        expected_record_kind=RecordKind.INVENTORY_MARKER,
    )
    ns.declare_dependency(
        dependency_id="JV_scalar_residue_flux_dependency_21",
        upstream_script_id="021_source_routing_and_mass_neutrality__candidate_JV_mass_neutrality_conditions",
        upstream_derivation_id="JV_scalar_residue_flux_21",
        expected_record_kind=RecordKind.DERIVATION,
    )
    ns.declare_dependency(
        dependency_id="A_sector_mass_definition_dependency_21",
        upstream_script_id="021_source_routing_and_mass_neutrality__candidate_a_sector_mass_charge_definition",
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
        "NOT_INSERTABLE": StatusMark.FAIL,
        "PROVISIONAL": StatusMark.INFO,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "RISK": StatusMark.WARN,
        "SAFE_IF": StatusMark.INFO,
        "THEOREM_TARGET": StatusMark.DEFER,
        "UNRESOLVED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


# =============================================================================
# Data models
# =============================================================================


@dataclass
class CurvatureExpressionSet:
    r: sp.Symbol
    G: sp.Symbol
    c: sp.Symbol
    C_curv: sp.Symbol
    q_e: sp.Symbol
    I_curv: sp.Symbol
    S_curv: sp.Symbol
    R_curv: sp.Symbol
    phi_curv: sp.Expr
    F_phi_curv: sp.Expr
    F_phi_curv_residual: sp.Expr
    delta_M_curv_like: sp.Expr
    delta_M_curv_like_residual: sp.Expr
    delta_A_e: sp.Expr
    delta_F_A_e: sp.Expr
    delta_F_A_e_residual: sp.Expr
    delta_M_e_like: sp.Expr
    delta_M_e_like_residual: sp.Expr
    j_curv_radial: sp.Expr
    Phi_Jcurv: sp.Expr
    Phi_Jcurv_residual: sp.Expr
    curvature_balance: sp.Expr
    curvature_balance_residual: sp.Expr


@dataclass
class CurvatureConditionEntry:
    name: str
    sector: str
    allowed_condition: str
    forbidden_condition: str
    status: str
    consequence: str
    obligation_id: str | None = None


@dataclass
class RejectedCurvatureRoute:
    name: str
    route: str
    forbidden_use: str
    consequence: str
    obligation_id: str | None = None


# =============================================================================
# Builders
# =============================================================================


def build_expressions() -> CurvatureExpressionSet:
    r = sp.Symbol("r", positive=True)
    G = sp.Symbol("G", positive=True)
    c = sp.Symbol("c", positive=True)
    C_curv = sp.Symbol("C_curv", real=True)
    q_e = sp.Symbol("q_e", real=True)
    I_curv = sp.Symbol("I_curv", real=True)
    S_curv = sp.Symbol("S_curv", real=True)
    R_curv = sp.Symbol("R_curv", real=True)

    # Generic scalar residue that curvature diagnostics/accounting must not leave
    # in the ordinary exterior unless a future source law derives neutral routing.
    phi_curv = C_curv / r
    F_phi_curv = sp.simplify(4 * sp.pi * r**2 * sp.diff(phi_curv, r))
    F_phi_curv_residual = sp.simplify(F_phi_curv + 4 * sp.pi * C_curv)
    delta_M_curv_like = sp.simplify((c**2 / (8 * sp.pi * G)) * F_phi_curv)
    delta_M_curv_like_residual = sp.simplify(delta_M_curv_like + c**2 * C_curv / (2 * G))

    # Danger diagnostic only: if e_curv/accounting were allowed to induce an
    # A-like exterior tail q_e/r, it would shift the A-sector mass. This does not
    # license e_curv as a source.
    delta_A_e = q_e / r
    delta_F_A_e = sp.simplify(4 * sp.pi * r**2 * sp.diff(delta_A_e, r))
    delta_F_A_e_residual = sp.simplify(delta_F_A_e + 4 * sp.pi * q_e)
    delta_M_e_like = sp.simplify((c**2 / (8 * sp.pi * G)) * delta_F_A_e)
    delta_M_e_like_residual = sp.simplify(delta_M_e_like + c**2 * q_e / (2 * G))

    # Unresolved curvature-current far-zone flux diagnostic.
    j_curv_radial = I_curv / (4 * sp.pi * r**2)
    Phi_Jcurv = sp.simplify(4 * sp.pi * r**2 * j_curv_radial)
    Phi_Jcurv_residual = sp.simplify(Phi_Jcurv - I_curv)

    # Role-level curvature balance diagnostic. This is bookkeeping, not a law.
    curvature_balance = sp.simplify(S_curv - R_curv)
    curvature_balance_residual = sp.simplify(curvature_balance - (S_curv - R_curv))

    return CurvatureExpressionSet(
        r=r,
        G=G,
        c=c,
        C_curv=C_curv,
        q_e=q_e,
        I_curv=I_curv,
        S_curv=S_curv,
        R_curv=R_curv,
        phi_curv=phi_curv,
        F_phi_curv=F_phi_curv,
        F_phi_curv_residual=F_phi_curv_residual,
        delta_M_curv_like=delta_M_curv_like,
        delta_M_curv_like_residual=delta_M_curv_like_residual,
        delta_A_e=delta_A_e,
        delta_F_A_e=delta_F_A_e,
        delta_F_A_e_residual=delta_F_A_e_residual,
        delta_M_e_like=delta_M_e_like,
        delta_M_e_like_residual=delta_M_e_like_residual,
        j_curv_radial=j_curv_radial,
        Phi_Jcurv=Phi_Jcurv,
        Phi_Jcurv_residual=Phi_Jcurv_residual,
        curvature_balance=curvature_balance,
        curvature_balance_residual=curvature_balance_residual,
    )


def build_condition_entries() -> List[CurvatureConditionEntry]:
    return [
        CurvatureConditionEntry(
            name="C1: A_curv diagnostic branch-filter",
            sector="A_curv",
            allowed_condition="A_curv remains diagnostic / branch-filter or receives independent source-neutral dynamics",
            forbidden_condition="A_curv changes A-flux, selects boundary behavior after recovery failure, or becomes scalar curvature charge",
            status="DIAGNOSTIC_ONLY",
            consequence="curvature admissibility can filter branches only if it does not become dynamics by vocabulary.",
            obligation_id="preserve_A_curv_diagnostic_only_21",
        ),
        CurvatureConditionEntry(
            name="C2: A_curv scalar residue neutrality",
            sector="A_curv residue",
            allowed_condition="C_curv = 0 outside, or curvature residue is strictly diagnostic/non-metric",
            forbidden_condition="phi_curv = C_curv/r with C_curv != 0 treated as ordinary exterior scalar charge",
            status="THEOREM_TARGET",
            consequence="curvature diagnostics must not leave a hidden scalar mass tail.",
            obligation_id="derive_A_curv_no_scalar_residue_21",
        ),
        CurvatureConditionEntry(
            name="C3: e_curv accounting-only status",
            sector="e_curv",
            allowed_condition="e_curv remains diagnostic/accounting and never sources A without derivation",
            forbidden_condition="e_curv is counted as exterior source energy or coefficient reservoir",
            status="ACCOUNTING_ONLY",
            consequence="curvature accounting cannot become mass source by naming it energy.",
            obligation_id="preserve_e_curv_accounting_only_21",
        ),
        CurvatureConditionEntry(
            name="C4: e_curv A-tail danger",
            sector="e_curv source-reservoir route",
            allowed_condition="q_e = 0 unless a future source law derives e_curv routing and no double counting",
            forbidden_condition="e_curv induces delta_A = q_e/r and shifts M_A by source-reservoir logic",
            status="REJECTED",
            consequence="e_curv cannot become a second exterior A-tail source.",
            obligation_id="reject_e_curv_A_tail_source_reservoir_21",
        ),
        CurvatureConditionEntry(
            name="C5: J_curv unresolved current",
            sector="J_curv",
            allowed_condition="J_curv remains unresolved until orientation, source side, boundary law, and mass neutrality are defined",
            forbidden_condition="J_curv is used as a curvature repair current or gradient-by-fiat",
            status="UNRESOLVED",
            consequence="J_curv cannot carry ordinary exterior mass while undefined.",
            obligation_id="define_J_curv_current_law_21",
        ),
        CurvatureConditionEntry(
            name="C6: J_curv far-zone flux neutrality",
            sector="J_curv far-zone flux",
            allowed_condition="I_curv = 0 in ordinary exterior unless a future curvature-current law derives neutral transport",
            forbidden_condition="nonzero curvature-current sphere flux shifts or mimics exterior mass",
            status="THEOREM_TARGET",
            consequence="curvature flux is not an ordinary mass flux coin.",
            obligation_id="derive_J_curv_far_zone_flux_neutrality_21",
        ),
        CurvatureConditionEntry(
            name="C7: curvature balance role target",
            sector="curvature balance",
            allowed_condition="S_curv - R_curv = 0 only as a future theorem target with defined operators",
            forbidden_condition="curvature balance is used as mass repair or singularity bounce by declaration",
            status="THEOREM_TARGET",
            consequence="curvature balance remains theorem-heavy and cannot tune M_ext.",
            obligation_id="derive_curvature_balance_without_mass_repair_21",
        ),
        CurvatureConditionEntry(
            name="C8: anti-singularity branch-filter guard",
            sector="finite admissibility / anti-singularity language",
            allowed_condition="admissibility filters candidate branches without becoming a source reservoir or bounce energy",
            forbidden_condition="branch-kill or finite-admissibility language is called dynamics that changes exterior mass",
            status="SAFE_IF",
            consequence="anti-singularity language remains diagnostic until a real current/source law exists.",
            obligation_id="preserve_finite_admissibility_as_diagnostic_21",
        ),
        CurvatureConditionEntry(
            name="C9: curvature boundary neutrality",
            sector="curvature boundary behavior",
            allowed_condition="curvature boundary terms are neutral, no-shell, and recovery-independent if introduced",
            forbidden_condition="curvature smoothing preserves mass by repair or hides boundary flux",
            status="THEOREM_TARGET",
            consequence="curvature boundary behavior cannot be a boundary purse.",
            obligation_id="derive_curvature_boundary_mass_neutrality_21",
        ),
        CurvatureConditionEntry(
            name="C10: H_curv rescue dependency",
            sector="H_curv / correction tensor dependency",
            allowed_condition="H_curv remains non-insertable until tensor definition, source side, divergence safety, and mass neutrality are derived",
            forbidden_condition="H_curv is introduced as curvature rescue, M_ext correction, boundary counterterm, or Bianchi paint",
            status="NOT_INSERTABLE",
            consequence="correction tensors cannot be inserted from curvature accounting language.",
            obligation_id="preserve_H_curv_non_insertable_21",
        ),
    ]


def build_rejected_routes() -> List[RejectedCurvatureRoute]:
    return [
        RejectedCurvatureRoute(
            name="RC1: e_curv source reservoir",
            route="e_curv_source_reservoir",
            forbidden_use="e_curv counted as ordinary exterior source energy or coefficient reservoir",
            consequence="curvature energy accounting cannot become mass source by naming it energy.",
            obligation_id="reject_e_curv_source_reservoir_21",
        ),
        RejectedCurvatureRoute(
            name="RC2: curvature balance as mass repair",
            route="curvature_balance_mass_repair",
            forbidden_use="curvature balance adjusted to preserve M_ext or recovery after leakage appears",
            consequence="balance requires operators and cannot tune exterior mass.",
            obligation_id="reject_curvature_balance_mass_repair_21",
        ),
        RejectedCurvatureRoute(
            name="RC3: J_curv gradient by fiat",
            route="J_curv_gradient_by_fiat",
            forbidden_use="J_curv direction, sign, or flux chosen to cancel a boundary or singularity problem",
            consequence="curvature current needs orientation, source side, and boundary law first.",
            obligation_id="reject_J_curv_gradient_by_fiat_21",
        ),
        RejectedCurvatureRoute(
            name="RC4: branch-kill called bounce",
            route="branch_kill_called_bounce",
            forbidden_use="finite-admissibility rejection is rebranded as a dynamical anti-singularity mechanism",
            consequence="diagnostic branch filtering is not dynamics.",
            obligation_id="reject_branch_kill_called_bounce_21",
        ),
        RejectedCurvatureRoute(
            name="RC5: H_curv curvature rescue",
            route="H_curv_curvature_rescue",
            forbidden_use="undefined H_curv inserted to absorb curvature, boundary, divergence, or mass mismatch",
            consequence="H_curv remains non-insertable.",
            obligation_id="reject_H_curv_curvature_rescue_21",
        ),
        RejectedCurvatureRoute(
            name="RC6: recovery-chosen curvature route",
            route="recovery_chosen_curvature_route",
            forbidden_use="curvature scalar, coefficient, boundary behavior, or admissibility threshold chosen from Schwarzschild/PPN/gamma_like/AB recovery",
            consequence="recovery remains downstream diagnostic, not a curvature-routing rule.",
            obligation_id="reject_recovery_chosen_curvature_route_21",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Curvature accounting mass-neutrality problem")
    print("Question:")
    print()
    print("  Can curvature admissibility or e_curv affect exterior mass?")
    print()
    print("Reference discipline:")
    print()
    print("  A-sector mass charge remains the reduced ordinary exterior reference.")
    print("  A_curv is diagnostic / branch-filter until a source-neutral dynamics is derived.")
    print("  e_curv is diagnostic / accounting only and not source energy.")
    print("  J_curv remains unresolved; curvature balance remains theorem-targeted.")
    print("  No curvature object may smooth mass, repair a boundary, or shift M_ext by declaration.")
    print("  This script records reduced diagnostics and theorem burden, not curvature dynamics.")

    with out.governance_assessments():
        out.line(
            "curvature accounting mass-neutrality audit opened",
            StatusMark.INFO,
            "A_curv/e_curv/J_curv are audited for scalar residue, A-tail, far-zone flux, boundary repair, and source-reservoir danger",
        )


def case_1_curvature_scalar_residue(exprs: CurvatureExpressionSet, out: ScriptOutput) -> None:
    header("Case 1: Curvature scalar residue")
    print("Take a generic curvature diagnostic residue:")
    print()
    print(f"  phi_curv(r) = {sp.sstr(exprs.phi_curv)}")
    print()
    print("Then:")
    print()
    print(f"  F_phi_curv = 4*pi*r^2*phi_curv' = {sp.sstr(exprs.F_phi_curv)}")
    print(f"  delta_M_curv_like = c^2*F_phi_curv/(8*pi*G) = {sp.sstr(exprs.delta_M_curv_like)}")
    print()
    print("Residual checks:")
    print()
    print(f"  F_phi_curv + 4*pi*C_curv = {sp.sstr(exprs.F_phi_curv_residual)}")
    print(f"  delta_M_curv_like + c^2*C_curv/(2*G) = {sp.sstr(exprs.delta_M_curv_like_residual)}")
    print()
    print("Interpretation:")
    print()
    print("  This is a danger diagnostic, not a licensed curvature mass law.")
    print("  A nonzero curvature 1/r scalar residue would behave like hidden scalar charge.")

    with out.derived_results():
        out.line(
            "curvature scalar residue flux derived",
            StatusMark.PASS if is_zero(exprs.F_phi_curv_residual) else StatusMark.FAIL,
            f"F_phi_curv = {sp.sstr(exprs.F_phi_curv)}",
        )
        out.line(
            "curvature A-like mass-shift diagnostic derived",
            StatusMark.PASS if is_zero(exprs.delta_M_curv_like_residual) else StatusMark.FAIL,
            f"delta_M_curv_like = {sp.sstr(exprs.delta_M_curv_like)}",
        )


def case_2_e_curv_source_reservoir_diagnostic(exprs: CurvatureExpressionSet, out: ScriptOutput) -> None:
    header("Case 2: e_curv source-reservoir diagnostic")
    print("If curvature accounting were incorrectly allowed to induce an A-like exterior tail:")
    print()
    print(f"  delta_A_e(r) = {sp.sstr(exprs.delta_A_e)}")
    print()
    print("then:")
    print()
    print(f"  delta_F_A|e_curv = 4*pi*r^2*delta_A_e' = {sp.sstr(exprs.delta_F_A_e)}")
    print(f"  delta_M_A|e_curv = c^2*delta_F_A/(8*pi*G) = {sp.sstr(exprs.delta_M_e_like)}")
    print()
    print("Residual checks:")
    print()
    print(f"  delta_F_A|e_curv + 4*pi*q_e = {sp.sstr(exprs.delta_F_A_e_residual)}")
    print(f"  delta_M_A|e_curv + c^2*q_e/(2*G) = {sp.sstr(exprs.delta_M_e_like_residual)}")
    print()
    print("Interpretation:")
    print()
    print("  This is not a source law.")
    print("  It shows why e_curv cannot become an exterior source reservoir by vocabulary.")

    with out.derived_results():
        out.line(
            "e_curv A-tail flux diagnostic derived",
            StatusMark.PASS if is_zero(exprs.delta_F_A_e_residual) else StatusMark.FAIL,
            f"delta_F_A|e_curv = {sp.sstr(exprs.delta_F_A_e)}",
        )
        out.line(
            "e_curv A-like mass-shift diagnostic derived",
            StatusMark.PASS if is_zero(exprs.delta_M_e_like_residual) else StatusMark.FAIL,
            f"delta_M_A|e_curv = {sp.sstr(exprs.delta_M_e_like)}",
        )


def case_3_J_curv_flux_and_balance(exprs: CurvatureExpressionSet, out: ScriptOutput) -> None:
    header("Case 3: J_curv far-zone flux and curvature-balance diagnostic")
    print("Use a generic far-zone radial curvature-current profile:")
    print()
    print(f"  j_curv^r = {sp.sstr(exprs.j_curv_radial)}")
    print()
    print("Its sphere flux is:")
    print()
    print(f"  Phi_Jcurv = 4*pi*r^2*j_curv^r = {sp.sstr(exprs.Phi_Jcurv)}")
    print()
    print("Role-level curvature balance target:")
    print()
    print(f"  curvature_balance = S_curv - R_curv = {sp.sstr(exprs.curvature_balance)}")
    print()
    print("Residual checks:")
    print()
    print(f"  Phi_Jcurv - I_curv = {sp.sstr(exprs.Phi_Jcurv_residual)}")
    print(f"  curvature_balance - (S_curv - R_curv) = {sp.sstr(exprs.curvature_balance_residual)}")
    print()
    print("Interpretation:")
    print()
    print("  J_curv is unresolved; a nonzero far-zone curvature-current coefficient is a mass-leak danger.")
    print("  Curvature balance is a theorem target, not a repair knob.")

    with out.derived_results():
        out.line(
            "J_curv far-zone current flux diagnostic derived",
            StatusMark.PASS if is_zero(exprs.Phi_Jcurv_residual) else StatusMark.FAIL,
            f"Phi_Jcurv = {sp.sstr(exprs.Phi_Jcurv)}",
        )
        out.line(
            "curvature balance diagnostic stated",
            StatusMark.PASS if is_zero(exprs.curvature_balance_residual) else StatusMark.FAIL,
            "role-level target is S_curv - R_curv = 0 only after operators exist",
        )
    with out.unresolved_obligations():
        out.line(
            "derive J_curv and curvature-balance operators before neutrality claim",
            StatusMark.OBLIGATION,
            "curvature current and balance cannot be asserted while source side, orientation, and boundary law are missing",
        )


def case_4_curvature_condition_ledger(entries: List[CurvatureConditionEntry], out: ScriptOutput) -> None:
    header("Case 4: Curvature accounting condition ledger")
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
            "curvature accounting ledger populated",
            StatusMark.PASS,
            f"{len(entries)} curvature/accounting conditions classified for mass-neutrality burden",
        )


def case_5_rejected_curvature_routes(routes: List[RejectedCurvatureRoute], out: ScriptOutput) -> None:
    header("Case 5: Rejected curvature mass routes")
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
            "curvature mass routes rejected",
            StatusMark.FAIL,
            "e_curv source reservoir, curvature balance repair, J_curv by fiat, branch-kill bounce, H_curv rescue, and recovery-chosen curvature routes are not licensed",
        )


def case_6_failure_controls(out: ScriptOutput) -> None:
    header("Case 6: Failure controls")
    print("The curvature accounting mass-neutrality audit fails if a later script allows:")
    print()
    print("1. A_curv to alter A-flux or M_ext as a branch-filter side effect")
    print("2. e_curv to become exterior source energy or a coefficient reservoir")
    print("3. J_curv to act as a repair current without definition, orientation, source side, or boundary law")
    print("4. curvature balance to tune mass or recovery after leakage appears")
    print("5. finite admissibility or branch-kill language to become bounce dynamics by name")
    print("6. curvature boundary behavior to smooth mass by repair or hide shell flux")
    print("7. H_curv to be inserted as curvature rescue before tensor definition and neutrality")
    print("8. Schwarzschild/PPN/gamma_like/AB recovery to choose curvature scalar, coefficient, threshold, or boundary behavior")
    print("9. O to enforce curvature/source neutrality without domain/kernel/image/boundary law")

    with out.unresolved_obligations():
        out.line(
            "derive curvature-accounting mass-neutrality theorem",
            StatusMark.OBLIGATION,
            "show A_curv/e_curv/J_curv have no independent A-flux shift, scalar charge, source reservoir, boundary repair, or recovery tuning",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("The reduced diagnostics are:")
    print()
    print("  phi_curv = C_curv/r      -> F_phi_curv = -4*pi*C_curv")
    print("  delta_A_e = q_e/r        -> delta_M_A|e_curv = -c^2*q_e/(2*G)")
    print("  j_curv^r = I_curv/(4*pi*r^2) -> sphere current flux = I_curv")
    print("  curvature balance target -> S_curv - R_curv = 0 only after operators exist")
    print()
    print("Therefore ordinary-sector curvature accounting neutrality requires:")
    print()
    print("  C_curv = 0 for scalar residue silence")
    print("  q_e = 0 for no e_curv A-tail source-reservoir effect")
    print("  I_curv = 0 for no independent far-zone curvature-current flux")
    print("  A_curv and e_curv remain diagnostic/accounting unless source-neutral dynamics are derived")
    print("  J_curv, curvature balance, and boundary behavior remain theorem-targeted")
    print("  no mass repair, source reservoir, bounce-by-name, H_curv rescue, or recovery-chosen curvature route")
    print()
    print("This script does not define curvature dynamics or J_curv.")
    print("It records the current theorem burden and keeps curvature accounting diagnostic.")
    print()
    print("Possible next script:")
    print("  candidate_correction_tensor_mass_neutrality_guard.py")

    with out.governance_assessments():
        out.line(
            "curvature accounting mass-neutrality audit complete",
            StatusMark.PASS,
            "curvature remains diagnostic/accounting/branch-filter; mass neutrality remains required and not derived",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, exprs: CurvatureExpressionSet) -> None:
    ns.record_derivation(
        derivation_id="curvature_scalar_residue_flux_21",
        inputs=[exprs.phi_curv, exprs.r, exprs.C_curv],
        output=exprs.F_phi_curv,
        method="F_phi_curv = simplify(4*pi*r**2*diff(C_curv/r, r))",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="surface_flux",
        scope="reduced ordinary exterior curvature scalar residue diagnostic",
    )
    ns.record_derivation(
        derivation_id="curvature_scalar_residue_A_like_mass_shift_21",
        inputs=[exprs.F_phi_curv, exprs.c, exprs.G],
        output=exprs.delta_M_curv_like,
        method="delta_M_curv_like = simplify(c**2*F_phi_curv/(8*pi*G))",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="mass_shift_diagnostic",
        scope="danger diagnostic only; not a licensed curvature mass law",
    )
    ns.record_derivation(
        derivation_id="e_curv_A_tail_flux_diagnostic_21",
        inputs=[exprs.delta_A_e, exprs.r, exprs.q_e],
        output=exprs.delta_F_A_e,
        method="delta_F_A_e = simplify(4*pi*r**2*diff(q_e/r, r))",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="A_flux_shift_diagnostic",
        scope="danger diagnostic only; not a licensed e_curv source law",
    )
    ns.record_derivation(
        derivation_id="e_curv_A_like_mass_shift_diagnostic_21",
        inputs=[exprs.delta_F_A_e, exprs.c, exprs.G],
        output=exprs.delta_M_e_like,
        method="delta_M_e_like = simplify(c**2*delta_F_A_e/(8*pi*G))",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="mass_shift_diagnostic",
        scope="danger diagnostic only; not a licensed e_curv mass law",
    )
    ns.record_derivation(
        derivation_id="J_curv_far_zone_current_flux_diagnostic_21",
        inputs=[exprs.j_curv_radial, exprs.r, exprs.I_curv],
        output=exprs.Phi_Jcurv,
        method="Phi_Jcurv = simplify(4*pi*r**2*(I_curv/(4*pi*r**2)))",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="current_flux_diagnostic",
        scope="far-zone curvature-current diagnostic only",
    )
    ns.record_derivation(
        derivation_id="curvature_balance_role_diagnostic_21",
        inputs=[exprs.S_curv, exprs.R_curv],
        output=exprs.curvature_balance,
        method="curvature_balance = simplify(S_curv - R_curv)",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="balance_condition_diagnostic",
        scope="role-level curvature balance diagnostic only; not an operator derivation",
    )


def record_inventory_marker(ns, entries: List[CurvatureConditionEntry]) -> None:
    names = [sp.Symbol(entry.name.split(":", 1)[0].replace("-", "_").replace(" ", "_")) for entry in entries]
    ns.record_derivation(
        derivation_id="curvature_accounting_mass_neutrality_inventory_marker_21",
        inputs=names,
        output=sp.Symbol("curvature_accounting_mass_neutrality_conditions_stated"),
        method="A_curv/e_curv/J_curv mass-neutrality condition and rejected-route inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="inventory_marker",
        scope="Group 21 source routing and mass neutrality",
        is_placeholder=True,
    )


def record_obligations(
    ns,
    entries: List[CurvatureConditionEntry],
    routes: List[RejectedCurvatureRoute],
) -> None:
    for entry in entries:
        if entry.obligation_id is None:
            continue
        ns.record_obligation(ProofObligationRecord(
            obligation_id=entry.obligation_id,
            script_id=SCRIPT_ID,
            title=f"Resolve curvature-accounting condition: {entry.name}",
            status=ObligationStatus.OPEN,
            required_by=["curvature_accounting_mass_neutrality_theorem_21"],
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
            required_by=["curvature_accounting_mass_neutrality_theorem_21"],
            description=(
                f"Route: {route.route}. Forbidden use: {route.forbidden_use}. "
                f"Consequence: {route.consequence}."
            ),
        ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="curvature_accounting_mass_neutrality_theorem_21",
        script_id=SCRIPT_ID,
        title="Derive curvature-accounting mass-neutrality theorem",
        status=ObligationStatus.OPEN,
        required_by=["ordinary_closed_regime_mass_neutrality_theorem_21"],
        description=(
            "Show A_curv/e_curv/J_curv have no independent A-flux shift, no exterior scalar charge, "
            "no source-reservoir role, no far-zone curvature-current flux, no boundary repair, no curvature balance repair, "
            "and no recovery-chosen curvature routing unless a future parent/source law derives otherwise."
        ),
    ))


def record_governance(
    ns,
    entries: List[CurvatureConditionEntry],
    routes: List[RejectedCurvatureRoute],
) -> None:
    obligation_ids = [entry.obligation_id for entry in entries if entry.obligation_id is not None]
    obligation_ids.extend(route.obligation_id for route in routes if route.obligation_id is not None)
    obligation_ids.append("curvature_accounting_mass_neutrality_theorem_21")

    ns.record_route(RouteRecord(
        route_id="curvature_accounting_mass_neutrality_audit_route_21",
        script_id=SCRIPT_ID,
        name="A_curv / e_curv / J_curv mass-neutrality audit route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "A-sector mass charge remains the reduced ordinary exterior reference",
            "A_curv remains diagnostic/branch-filter unless source-neutral dynamics are derived",
            "e_curv remains diagnostic/accounting only and not source energy",
            "J_curv remains unresolved until orientation, source side, boundary law, and mass neutrality are derived",
            "no curvature balance, boundary smoothing, H_curv rescue, active O, or recovery tuning is assumed",
        ],
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="keep_curvature_accounting_diagnostic_21",
        script_id=SCRIPT_ID,
        branch_id="curvature_accounting_diagnostic_branch",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "preserve_A_curv_diagnostic_only_21",
            "preserve_e_curv_accounting_only_21",
            "preserve_finite_admissibility_as_diagnostic_21",
            "curvature_accounting_mass_neutrality_theorem_21",
        ],
        description=(
            "A_curv/e_curv remain diagnostic/accounting/branch-filter objects unless a future source-neutral dynamics "
            "derives their mass and boundary neutrality."
        ),
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_J_curv_mass_carrier_route_21",
        script_id=SCRIPT_ID,
        branch_id="J_curv_exterior_mass_carrier",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "define_J_curv_current_law_21",
            "derive_J_curv_far_zone_flux_neutrality_21",
            "derive_curvature_boundary_mass_neutrality_21",
            "curvature_accounting_mass_neutrality_theorem_21",
        ],
        description=(
            "J_curv is deferred as any exterior mass carrier until a current definition, orientation, source side, boundary law, "
            "far-zone flux neutrality, and A-sector mass neutrality are derived."
        ),
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_curvature_mass_repair_routes_21",
        script_id=SCRIPT_ID,
        branch_id="curvature_mass_repair_routes",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[route.obligation_id for route in routes if route.obligation_id is not None],
        description=(
            "Reject e_curv source reservoir, curvature balance mass repair, J_curv gradient by fiat, branch-kill bounce, "
            "H_curv curvature rescue, and recovery-chosen curvature routing as ordinary mass-neutrality routes."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="curvature_accounting_mass_neutrality_conditions_21",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "A_curv, e_curv, and J_curv are not licensed as ordinary exterior mass carriers in Group 21. "
            "They must remain diagnostic/accounting/unresolved or prove no A-flux shift, no scalar residue, "
            "no source reservoir, no far-zone curvature-current flux, no boundary repair, and no recovery tuning."
        ),
        derivation_ids=[
            "curvature_scalar_residue_flux_21",
            "e_curv_A_tail_flux_diagnostic_21",
            "J_curv_far_zone_current_flux_diagnostic_21",
            "curvature_balance_role_diagnostic_21",
        ],
        obligation_ids=obligation_ids,
    ))

    ns.record_claim(ClaimRecord(
        claim_id="curvature_mass_repair_routes_rejected_21",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Curvature-accounting labels may not be used as repair mechanisms: e_curv cannot become a source reservoir, "
            "curvature balance cannot tune M_ext, J_curv cannot be defined by fiat, branch-kill is not bounce dynamics, "
            "H_curv cannot be curvature rescue, and recovery cannot choose curvature routing."
        ),
        derivation_ids=[
            "curvature_scalar_residue_flux_21",
            "e_curv_A_tail_flux_diagnostic_21",
            "curvature_balance_role_diagnostic_21",
        ],
        obligation_ids=[route.obligation_id for route in routes if route.obligation_id is not None],
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Curvature Accounting Mass Neutrality")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    exprs = build_expressions()
    entries = build_condition_entries()
    routes = build_rejected_routes()

    case_0_problem_statement(out)
    case_1_curvature_scalar_residue(exprs, out)
    case_2_e_curv_source_reservoir_diagnostic(exprs, out)
    case_3_J_curv_flux_and_balance(exprs, out)
    case_4_curvature_condition_ledger(entries, out)
    case_5_rejected_curvature_routes(routes, out)
    case_6_failure_controls(out)
    final_interpretation(out)

    record_derivations(ns, exprs)
    record_inventory_marker(ns, entries)
    record_obligations(ns, entries, routes)
    record_governance(ns, entries, routes)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
