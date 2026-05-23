# Candidate boundary flux mass preservation
#
# Group:
#   21_source_routing_and_mass_neutrality
#
# Script type:
#   DERIVATION / DIAGNOSTIC / REQUIREMENTS
#
# Purpose
# -------
# Test whether boundary or smoothing behavior can preserve the A-sector mass
# charge without becoming a repair mechanism.
#
# Locked-door question:
#
#   Can boundary or smoothing behavior preserve A-sector mass without repair?
#
# This script does not derive a boundary theorem, matching law, shell law,
# source law, no-overlap operator, or parent field equation.
#
# It derives the reduced warning identity for an exterior non-A boundary tail:
#
#   delta A_boundary = q/r
#   delta F_A = 4*pi*r^2*(delta A_boundary)' = -4*pi*q
#   delta M_A = c^2*delta F_A/(8*pi*G) = -c^2*q/(2*G)
#
# Therefore a non-A boundary contribution with a 1/r exterior coefficient shifts
# the A-sector mass charge unless q = 0 or a future source theorem explicitly
# redefines the mass law without double counting.

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
        dependency_id="residual_scalar_zero_flux_condition_dependency_21",
        upstream_script_id="21_source_routing_and_mass_neutrality__candidate_residual_scalar_tail_flux_audit",
        upstream_derivation_id="residual_scalar_tail_zero_flux_condition_21",
        expected_record_kind=RecordKind.DERIVATION,
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
    }.get(status, StatusMark.INFO)


# =============================================================================
# Data models
# =============================================================================


@dataclass
class BoundaryFluxExpressionSet:
    r: sp.Symbol
    R: sp.Symbol
    G: sp.Symbol
    c: sp.Symbol
    q: sp.Symbol
    phi0: sp.Symbol
    delta_A_tail: sp.Expr
    delta_F_A_tail: sp.Expr
    delta_M_A_tail: sp.Expr
    flux_residual: sp.Expr
    mass_residual: sp.Expr
    zero_flux_condition: sp.Equality
    c1_profile: sp.Expr
    c1_value_at_R: sp.Expr
    c1_slope_at_R: sp.Expr
    c1_flux_at_R: sp.Expr
    c2_profile: sp.Expr
    c2_value_at_R: sp.Expr
    c2_slope_at_R: sp.Expr
    c2_flux_at_R: sp.Expr
    compact_profile: sp.Expr
    compact_value_at_R: sp.Expr
    compact_slope_at_R: sp.Expr
    compact_flux_at_R: sp.Expr


@dataclass
class BoundaryBranchEntry:
    name: str
    branch: str
    status: str
    condition: str
    consequence: str
    obligation_id: str | None = None


@dataclass
class RejectedRepairEntry:
    name: str
    route: str
    forbidden_use: str
    consequence: str


# =============================================================================
# Symbolic construction
# =============================================================================


def build_boundary_expressions() -> BoundaryFluxExpressionSet:
    r = sp.Symbol("r", positive=True)
    R = sp.Symbol("R", positive=True)
    G = sp.Symbol("G", positive=True)
    c = sp.Symbol("c", positive=True)
    q = sp.Symbol("q", real=True)
    phi0 = sp.Symbol("phi0", real=True)

    delta_A_tail = q / r
    delta_F_A_tail = sp.simplify(4 * sp.pi * r**2 * sp.diff(delta_A_tail, r))
    delta_M_A_tail = sp.simplify((c**2 / (8 * sp.pi * G)) * delta_F_A_tail)
    flux_residual = sp.simplify(delta_F_A_tail + 4 * sp.pi * q)
    mass_residual = sp.simplify(delta_M_A_tail + c**2 * q / (2 * G))
    zero_flux_condition = sp.Eq(q, 0)

    # C0-continuous but slope-discontinuous toy boundary profile.
    c1_profile = phi0 * (1 - r / R)
    c1_value_at_R = sp.simplify(c1_profile.subs(r, R))
    c1_slope_at_R = sp.simplify(sp.diff(c1_profile, r).subs(r, R))
    c1_flux_at_R = sp.simplify((4 * sp.pi * r**2 * sp.diff(c1_profile, r)).subs(r, R))

    # Value and first-derivative-neutral toy profile at the boundary.
    c2_profile = phi0 * (1 - r / R) ** 2
    c2_value_at_R = sp.simplify(c2_profile.subs(r, R))
    c2_slope_at_R = sp.simplify(sp.diff(c2_profile, r).subs(r, R))
    c2_flux_at_R = sp.simplify((4 * sp.pi * r**2 * sp.diff(c2_profile, r)).subs(r, R))

    # Smooth compact diagnostic profile with zero value and zero flux at support edge.
    compact_profile = phi0 * (1 - r**2 / R**2) ** 2
    compact_value_at_R = sp.simplify(compact_profile.subs(r, R))
    compact_slope_at_R = sp.simplify(sp.diff(compact_profile, r).subs(r, R))
    compact_flux_at_R = sp.simplify((4 * sp.pi * r**2 * sp.diff(compact_profile, r)).subs(r, R))

    return BoundaryFluxExpressionSet(
        r=r,
        R=R,
        G=G,
        c=c,
        q=q,
        phi0=phi0,
        delta_A_tail=delta_A_tail,
        delta_F_A_tail=delta_F_A_tail,
        delta_M_A_tail=delta_M_A_tail,
        flux_residual=flux_residual,
        mass_residual=mass_residual,
        zero_flux_condition=zero_flux_condition,
        c1_profile=c1_profile,
        c1_value_at_R=c1_value_at_R,
        c1_slope_at_R=c1_slope_at_R,
        c1_flux_at_R=c1_flux_at_R,
        c2_profile=c2_profile,
        c2_value_at_R=c2_value_at_R,
        c2_slope_at_R=c2_slope_at_R,
        c2_flux_at_R=c2_flux_at_R,
        compact_profile=compact_profile,
        compact_value_at_R=compact_value_at_R,
        compact_slope_at_R=compact_slope_at_R,
        compact_flux_at_R=compact_flux_at_R,
    )


def build_branch_entries() -> List[BoundaryBranchEntry]:
    return [
        BoundaryBranchEntry(
            name="BND1: smooth compact residual",
            branch="smooth_compact_residual",
            status="SAFE_IF",
            condition="boundary value and boundary flux vanish, and support/matching are derived before recovery",
            consequence="safe only as diagnostic/sample until a compact-support law is derived",
            obligation_id="derive_compact_boundary_support_law_21",
        ),
        BoundaryBranchEntry(
            name="BND2: C1 residual profile",
            branch="C1_residual_profile",
            status="RISK",
            condition="value matches at boundary but derivative/flux may be nonzero",
            consequence="can hide shell flux or tune exterior A' unless derivative neutrality is derived",
            obligation_id="derive_no_C1_boundary_flux_leak_21",
        ),
        BoundaryBranchEntry(
            name="BND3: C2 residual profile",
            branch="C2_residual_profile",
            status="SAFE_IF",
            condition="value and first derivative vanish in the toy profile",
            consequence="may be diagnostic if no source, metric, or recovery effect follows from the residual",
            obligation_id="derive_C2_boundary_matching_law_21",
        ),
        BoundaryBranchEntry(
            name="BND4: boundary shell source",
            branch="boundary_shell_source",
            status="REJECTED",
            condition="shell source changes exterior flux or hides discontinuity",
            consequence="ordinary mass preservation cannot be achieved by hidden shell source",
            obligation_id="derive_no_boundary_shell_source_21",
        ),
        BoundaryBranchEntry(
            name="BND5: surface counterterm",
            branch="surface_counterterm",
            status="REJECTED",
            condition="counterterm selected after leakage appears",
            consequence="boundary counterterms cannot preserve M_A by repair",
            obligation_id="reject_surface_counterterm_mass_repair_21",
        ),
        BoundaryBranchEntry(
            name="BND6: diagnostic boundary audit",
            branch="diagnostic_boundary_audit",
            status="SAFE_IF",
            condition="audit labels boundary behavior without modifying equations",
            consequence="safe bookkeeping if it has no source, metric, flux, or recovery effect",
            obligation_id=None,
        ),
        BoundaryBranchEntry(
            name="BND7: residual-kill convention",
            branch="residual_kill_convention",
            status="PROVISIONAL",
            condition="residual is kept non-metric or killed before it can alter A-flux",
            consequence="safer than residual mass but not a derived no-overlap theorem",
            obligation_id="derive_residual_kill_boundary_neutrality_21",
        ),
        BoundaryBranchEntry(
            name="BND8: neutral residual theorem target",
            branch="neutral_residual_theorem_target",
            status="THEOREM_TARGET",
            condition="derive delta F_A|boundary,non-A = 0 with no shell and no recovery tuning",
            consequence="the desired future boundary mass-preservation theorem",
            obligation_id="derive_boundary_flux_mass_preservation_theorem_21",
        ),
    ]


def build_rejected_repairs() -> List[RejectedRepairEntry]:
    return [
        RejectedRepairEntry(
            name="R1: boundary repair current",
            route="boundary_repair_current",
            forbidden_use="current selected to cancel boundary flux after leakage appears",
            consequence="repair current is not a mass-preservation theorem",
        ),
        RejectedRepairEntry(
            name="R2: R_V boundary cancellation",
            route="R_V_boundary_cancellation",
            forbidden_use="relaxation role used to erase non-A boundary mismatch",
            consequence="R_V cannot be a boundary purse while its operator remains role-level",
        ),
        RejectedRepairEntry(
            name="R3: H boundary counterterm",
            route="H_boundary_counterterm",
            forbidden_use="undefined correction tensor absorbs boundary flux mismatch",
            consequence="H_curv/H_exch remain non-insertable",
        ),
        RejectedRepairEntry(
            name="R4: curvature boundary rescue",
            route="curvature_boundary_rescue",
            forbidden_use="curvature diagnostic or balance term smooths mass by repair",
            consequence="curvature admissibility remains diagnostic/branch-filter, not a mass source",
        ),
        RejectedRepairEntry(
            name="R5: recovery-tuned smoothing",
            route="recovery_tuned_smoothing",
            forbidden_use="boundary behavior chosen to recover Schwarzschild, gamma_like, AB, or B=1/A",
            consequence="recovery remains downstream diagnostic, not construction rule",
        ),
        RejectedRepairEntry(
            name="R6: sharp support hiding shell charge",
            route="sharp_support_hides_shell_charge",
            forbidden_use="compact support imposed with derivative jump or hidden shell flux",
            consequence="support and matching must be derived, not imposed after leakage",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Boundary flux mass-preservation problem")
    print("Question:")
    print()
    print("  Can boundary or smoothing behavior preserve A-sector mass without repair?")
    print()
    print("Reference discipline:")
    print()
    print("  A-flux outside must remain fixed by the A-sector mass charge.")
    print("  Non-A boundary behavior must not change exterior A'.")
    print("  No shell source, smoothing repair, counterterm, or recovery-tuned boundary condition is licensed.")
    print("  This script is a reduced diagnostic and requirements audit, not a boundary theorem.")

    with out.governance_assessments():
        out.line(
            "boundary flux mass-preservation audit opened",
            StatusMark.INFO,
            "testing reduced boundary flux conditions without assuming a boundary repair mechanism",
        )


def case_1_boundary_tail_flux(exprs: BoundaryFluxExpressionSet, out: ScriptOutput) -> None:
    header("Case 1: Exterior non-A boundary tail shifts A-flux")
    print("Take a generic exterior non-A boundary contribution:")
    print()
    print(f"  delta_A_boundary(r) = {sp.sstr(exprs.delta_A_tail)}")
    print()
    print("Then:")
    print()
    print(f"  delta_F_A = 4*pi*r^2*d(delta_A_boundary)/dr = {sp.sstr(exprs.delta_F_A_tail)}")
    print(f"  delta_M_A = c^2*delta_F_A/(8*pi*G) = {sp.sstr(exprs.delta_M_A_tail)}")
    print()
    print("Residual checks:")
    print()
    print(f"  delta_F_A + 4*pi*q = {sp.sstr(exprs.flux_residual)}")
    print(f"  delta_M_A + c^2*q/(2*G) = {sp.sstr(exprs.mass_residual)}")
    print()
    print("Neutrality condition:")
    print()
    print(f"  {sp.sstr(exprs.zero_flux_condition)}")

    flux_identity_ok = is_zero(exprs.flux_residual)
    mass_identity_ok = is_zero(exprs.mass_residual)
    generically_nonzero = not is_zero(exprs.delta_F_A_tail)

    with out.derived_results():
        out.line(
            "boundary 1/r A-flux shift derived",
            StatusMark.PASS if flux_identity_ok else StatusMark.FAIL,
            f"delta_F_A = {sp.sstr(exprs.delta_F_A_tail)}",
        )
        out.line(
            "boundary 1/r mass shift derived",
            StatusMark.PASS if mass_identity_ok else StatusMark.FAIL,
            f"delta_M_A = {sp.sstr(exprs.delta_M_A_tail)}",
        )
        out.line(
            "generic nonzero q shifts A-sector mass",
            StatusMark.PASS if generically_nonzero else StatusMark.FAIL,
            "delta_F_A vanishes only when the exterior boundary-tail coefficient q vanishes",
        )


def case_2_boundary_profile_diagnostics(exprs: BoundaryFluxExpressionSet, out: ScriptOutput) -> None:
    header("Case 2: Boundary profile diagnostics")
    print("C1-style toy profile:")
    print()
    print(f"  phi_C1(r) = {sp.sstr(exprs.c1_profile)}")
    print(f"  phi_C1(R) = {sp.sstr(exprs.c1_value_at_R)}")
    print(f"  phi_C1'(R) = {sp.sstr(exprs.c1_slope_at_R)}")
    print(f"  boundary flux at R = {sp.sstr(exprs.c1_flux_at_R)}")
    print()
    print("C2-style toy profile:")
    print()
    print(f"  phi_C2(r) = {sp.sstr(exprs.c2_profile)}")
    print(f"  phi_C2(R) = {sp.sstr(exprs.c2_value_at_R)}")
    print(f"  phi_C2'(R) = {sp.sstr(exprs.c2_slope_at_R)}")
    print(f"  boundary flux at R = {sp.sstr(exprs.c2_flux_at_R)}")
    print()
    print("Smooth compact toy profile:")
    print()
    print(f"  phi_compact(r) = {sp.sstr(exprs.compact_profile)}")
    print(f"  phi_compact(R) = {sp.sstr(exprs.compact_value_at_R)}")
    print(f"  phi_compact'(R) = {sp.sstr(exprs.compact_slope_at_R)}")
    print(f"  boundary flux at R = {sp.sstr(exprs.compact_flux_at_R)}")
    print()
    print("Interpretation:")
    print()
    print("  A value-continuous boundary profile can still carry boundary flux if its slope is not neutral.")
    print("  Zero boundary value and zero boundary slope are safer diagnostic conditions.")
    print("  But compact support and smoothing must be derived, not chosen to repair recovery.")

    with out.sample_results():
        out.line(
            "C1 toy boundary profile can carry shell-like flux",
            StatusMark.PASS if not is_zero(exprs.c1_flux_at_R) else StatusMark.FAIL,
            f"boundary flux = {sp.sstr(exprs.c1_flux_at_R)}",
        )
        out.line(
            "C2 toy boundary profile has zero boundary flux",
            StatusMark.PASS if is_zero(exprs.c2_flux_at_R) else StatusMark.FAIL,
            f"boundary flux = {sp.sstr(exprs.c2_flux_at_R)}",
        )
        out.line(
            "smooth compact toy profile has zero boundary flux",
            StatusMark.PASS if is_zero(exprs.compact_flux_at_R) else StatusMark.FAIL,
            f"boundary flux = {sp.sstr(exprs.compact_flux_at_R)}",
        )


def case_3_branch_ledger(branches: List[BoundaryBranchEntry], out: ScriptOutput) -> None:
    header("Case 3: Boundary branch ledger")
    for branch in branches:
        print()
        print("-" * 120)
        print(branch.name)
        print("-" * 120)
        print(f"Branch: {branch.branch}")
        print(f"Condition: {branch.condition}")
        print(f"[{status_mark(branch.status).value}] {branch.name}: {branch.status}")
        print(f"Consequence: {branch.consequence}")

    with out.governance_assessments():
        out.line(
            "boundary branch ledger populated",
            StatusMark.PASS,
            f"{len(branches)} boundary branches classified for mass-preservation risk",
        )


def case_4_rejected_repair_routes(repairs: List[RejectedRepairEntry], out: ScriptOutput) -> None:
    header("Case 4: Rejected boundary repair routes")
    for repair in repairs:
        print()
        print("-" * 120)
        print(repair.name)
        print("-" * 120)
        print(f"Route: {repair.route}")
        print(f"Forbidden use: {repair.forbidden_use}")
        print(f"[FAIL] {repair.name}: REJECTED")
        print(f"Consequence: {repair.consequence}")

    with out.counterexamples():
        out.line(
            "boundary repair routes rejected",
            StatusMark.FAIL,
            "shell sources, counterterms, recovery tuning, and undefined repair currents are not mass-preservation theorems",
        )


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("The boundary flux mass-preservation audit fails if a later script allows:")
    print()
    print("1. non-A boundary behavior to change exterior A' or A-flux")
    print("2. a smoothing layer to tune M_ext after recovery failure")
    print("3. a shell source or derivative jump to hide mass leakage")
    print("4. R_V, J_exch, curvature balance, or H to act as boundary repair")
    print("5. compact support to be imposed without matching and no-shell conditions")
    print("6. residual-kill to be treated as a derived boundary theorem")
    print("7. boundary conditions to be chosen by Schwarzschild/PPN/AB recovery")
    print("8. O to enforce boundary neutrality without domain/kernel/image/boundary law")

    with out.unresolved_obligations():
        out.line(
            "derive boundary mass-preservation theorem",
            StatusMark.OBLIGATION,
            "show delta F_A|boundary,non-A = 0 with no shell source, no repair current, and no recovery tuning",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("The reduced boundary warning is:")
    print()
    print("  delta_A_boundary = q/r")
    print("  delta_F_A = -4*pi*q")
    print("  delta_M_A = -c^2*q/(2*G)")
    print()
    print("Therefore:")
    print()
    print("  a non-A boundary or smoothing contribution with a nonzero exterior 1/r coefficient")
    print("  shifts the A-sector mass charge unless q = 0 or a future parent/source identity")
    print("  derives a new mass law without double counting.")
    print()
    print("This script does not prove boundary mass preservation.")
    print("It records the reduced flux witness and the branch-level repair exclusions.")
    print()
    print("Possible next script:")
    print("  candidate_zeta_kappa_mass_neutrality_conditions.py")

    with out.governance_assessments():
        out.line(
            "boundary flux mass-preservation audit complete",
            StatusMark.PASS,
            "boundary mass preservation remains theorem-targeted; only neutral diagnostic behavior is safe",
        )


# =============================================================================
# Archive recording
# =============================================================================


def record_derivations(ns, exprs: BoundaryFluxExpressionSet) -> None:
    ns.record_derivation(
        derivation_id="boundary_tail_delta_A_flux_21",
        inputs=[exprs.delta_A_tail, exprs.r, exprs.q],
        output=exprs.delta_F_A_tail,
        method="delta_F_A = simplify(4*pi*r**2*diff(q/r, r))",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="boundary_flux_shift",
        scope="reduced static spherical exterior non-A boundary tail",
    )

    ns.record_derivation(
        derivation_id="boundary_tail_delta_MA_21",
        inputs=[exprs.delta_F_A_tail, exprs.c, exprs.G],
        output=exprs.delta_M_A_tail,
        method="delta_M_A = simplify(c**2*delta_F_A/(8*pi*G))",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="mass_charge_shift",
        scope="reduced static spherical exterior non-A boundary tail",
    )

    ns.record_derivation(
        derivation_id="boundary_tail_flux_residual_21",
        inputs=[exprs.delta_F_A_tail, exprs.q],
        output=exprs.flux_residual,
        method="simplify(delta_F_A + 4*pi*q)",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
        scope="boundary tail A-flux identity",
    )

    ns.record_derivation(
        derivation_id="boundary_tail_mass_residual_21",
        inputs=[exprs.delta_M_A_tail, exprs.q, exprs.c, exprs.G],
        output=exprs.mass_residual,
        method="simplify(delta_M_A + c**2*q/(2*G))",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
        scope="boundary tail mass-shift identity",
    )

    ns.record_derivation(
        derivation_id="boundary_tail_zero_flux_condition_21",
        inputs=[exprs.delta_F_A_tail],
        output=exprs.zero_flux_condition,
        method="solve delta_F_A = 0 for exterior boundary-tail coefficient",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="neutrality_condition",
        scope="ordinary-sector non-A boundary 1/r contribution",
    )

    ns.record_derivation(
        derivation_id="boundary_C1_profile_flux_diagnostic_21",
        inputs=[exprs.c1_profile, exprs.r, exprs.R, exprs.phi0],
        output=exprs.c1_flux_at_R,
        method="boundary flux of phi0*(1-r/R) at r=R",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="boundary_flux_diagnostic",
        scope="toy boundary profile diagnostic",
    )

    ns.record_derivation(
        derivation_id="boundary_C2_profile_flux_diagnostic_21",
        inputs=[exprs.c2_profile, exprs.r, exprs.R, exprs.phi0],
        output=exprs.c2_flux_at_R,
        method="boundary flux of phi0*(1-r/R)**2 at r=R",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="boundary_flux_diagnostic",
        scope="toy boundary profile diagnostic",
    )

    ns.record_derivation(
        derivation_id="boundary_compact_profile_flux_diagnostic_21",
        inputs=[exprs.compact_profile, exprs.r, exprs.R, exprs.phi0],
        output=exprs.compact_flux_at_R,
        method="boundary flux of phi0*(1-r**2/R**2)**2 at r=R",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="boundary_flux_diagnostic",
        scope="toy compact-support boundary profile diagnostic",
    )


def record_inventory_marker(ns, branches: List[BoundaryBranchEntry]) -> None:
    names = [sp.Symbol(branch.name.split(":", 1)[0].replace("-", "_").replace(" ", "_")) for branch in branches]
    ns.record_derivation(
        derivation_id="boundary_flux_mass_preservation_inventory_marker_21",
        inputs=names,
        output=sp.Symbol("boundary_flux_mass_preservation_inventory_stated"),
        method="boundary branch and repair-route inventory for mass preservation",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="inventory_marker",
        scope="Group 21 source routing and mass neutrality",
        is_placeholder=True,
    )


def record_obligations(ns, branches: List[BoundaryBranchEntry]) -> None:
    for branch in branches:
        if branch.obligation_id is None:
            continue
        ns.record_obligation(ProofObligationRecord(
            obligation_id=branch.obligation_id,
            script_id=SCRIPT_ID,
            title=f"Resolve boundary branch: {branch.branch}",
            status=ObligationStatus.OPEN,
            required_by=["ordinary_closed_boundary_mass_preservation_theorem_21"],
            description=(
                f"Branch condition: {branch.condition}. Consequence: {branch.consequence}. "
                "Future work must show whether this branch is genuinely boundary-neutral, diagnostic-only, "
                "or rejected as a repair/source route."
            ),
        ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_boundary_non_A_delta_FA_zero_21",
        script_id=SCRIPT_ID,
        title="Derive non-A boundary delta F_A equals zero",
        status=ObligationStatus.OPEN,
        required_by=["ordinary_closed_boundary_mass_preservation_theorem_21"],
        description=(
            "Show that non-A boundary behavior does not change exterior A-flux or A-sector mass charge. "
            "This requires delta F_A|boundary,non-A = 0 before recovery tests are used."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_no_recovery_tuned_smoothing_21",
        script_id=SCRIPT_ID,
        title="Derive boundary smoothing without recovery tuning",
        status=ObligationStatus.OPEN,
        required_by=["ordinary_closed_boundary_mass_preservation_theorem_21"],
        description=(
            "Show that any smoothing or matching law is derived structurally and is not chosen from Schwarzschild, PPN, AB, or B=1/A recovery."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="ordinary_closed_boundary_mass_preservation_theorem_21",
        script_id=SCRIPT_ID,
        title="Derive ordinary closed-regime boundary mass-preservation theorem",
        status=ObligationStatus.OPEN,
        required_by=["ordinary_closed_regime_mass_neutrality_theorem_21"],
        description=(
            "Show that boundary smoothing, compact residuals, current support, curvature diagnostics, and correction labels "
            "do not alter exterior A-flux, create shell sources, or tune M_ext by repair."
        ),
    ))


def record_governance(
    ns,
    branches: List[BoundaryBranchEntry],
    repairs: List[RejectedRepairEntry],
) -> None:
    obligation_ids = [branch.obligation_id for branch in branches if branch.obligation_id is not None]
    obligation_ids.extend([
        "derive_boundary_non_A_delta_FA_zero_21",
        "derive_no_recovery_tuned_smoothing_21",
        "ordinary_closed_boundary_mass_preservation_theorem_21",
    ])

    ns.record_route(RouteRecord(
        route_id="boundary_flux_mass_preservation_audit_route_21",
        script_id=SCRIPT_ID,
        name="Boundary flux mass-preservation audit route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "A-sector mass charge remains the reduced exterior reference",
            "non-A boundary contributions must satisfy delta F_A = 0",
            "no shell source, counterterm, recovery tuning, active O, or undefined repair current is assumed",
            "compact or smooth profiles remain diagnostic until support and matching are derived",
        ],
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_boundary_shell_source_mass_repair_21",
        script_id=SCRIPT_ID,
        branch_id="boundary_shell_source_mass_repair",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=["derive_no_boundary_shell_source_21"],
        description=(
            "Reject boundary shell sources as ordinary mass-preservation repairs. Boundary shell behavior cannot hide "
            "a jump in flux or tune exterior A' by declaration."
        ),
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_surface_counterterm_mass_preservation_21",
        script_id=SCRIPT_ID,
        branch_id="surface_counterterm_mass_preservation",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=["reject_surface_counterterm_mass_repair_21"],
        description=(
            "Reject surface counterterms chosen after leakage appears. Counterterms do not prove boundary mass preservation."
        ),
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_recovery_tuned_boundary_smoothing_21",
        script_id=SCRIPT_ID,
        branch_id="recovery_tuned_boundary_smoothing",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=["derive_no_recovery_tuned_smoothing_21"],
        description=(
            "Reject boundary smoothing selected from Schwarzschild, PPN, AB, or B=1/A recovery targets. Recovery is downstream only."
        ),
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_neutral_boundary_residual_theorem_21",
        script_id=SCRIPT_ID,
        branch_id="neutral_boundary_residual_theorem",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "derive_boundary_non_A_delta_FA_zero_21",
            "derive_no_boundary_shell_source_21",
            "ordinary_closed_boundary_mass_preservation_theorem_21",
        ],
        description=(
            "Defer neutral residual boundary behavior as a theorem target. It needs support, matching, no-shell, and no-recovery-tuning proofs."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="boundary_tail_A_flux_shift_rule_21",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.LICENSING,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "For a reduced exterior non-A boundary contribution delta_A = q/r, the A-flux shift is "
            "delta_F_A = -4*pi*q and the A-sector mass shift is delta_M_A = -c^2*q/(2*G). "
            "Thus q = 0 is required for this boundary tail to be mass-neutral."
        ),
        derivation_ids=[
            "boundary_tail_delta_A_flux_21",
            "boundary_tail_delta_MA_21",
            "boundary_tail_zero_flux_condition_21",
        ],
    ))

    ns.record_claim(ClaimRecord(
        claim_id="boundary_mass_preservation_requirement_21",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Boundary or smoothing behavior must not alter exterior A-flux, create shell source, tune M_ext, "
            "or use repair mechanisms. Boundary mass preservation remains a theorem target."
        ),
        derivation_ids=["boundary_tail_delta_A_flux_21", "boundary_tail_delta_MA_21"],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Boundary Flux Mass Preservation")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    exprs = build_boundary_expressions()
    branches = build_branch_entries()
    repairs = build_rejected_repairs()

    case_0_problem_statement(out)
    case_1_boundary_tail_flux(exprs, out)
    case_2_boundary_profile_diagnostics(exprs, out)
    case_3_branch_ledger(branches, out)
    case_4_rejected_repair_routes(repairs, out)
    case_5_failure_controls(out)
    final_interpretation(out)

    record_derivations(ns, exprs)
    record_inventory_marker(ns, branches)
    record_obligations(ns, branches)
    record_governance(ns, branches, repairs)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
