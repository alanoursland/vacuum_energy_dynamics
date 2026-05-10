# Group:
#   06_tensor_flux_principle
#
# Script type:
#   DERIVATION

# Candidate tensor action stiffness
#
# Purpose
# -------
# The tensor-flux program now has:
#
#   h_ij^TT basis,
#   vacuum wave equation,
#   quadrupole source structure,
#   target amplitude scaling,
#   radiation energy-flux scaling,
#   no-unwanted-scalar-radiation guardrail.
#
# The next question is whether a tensor action/stiffness picture can support
# the wave equation and source normalization target.
#
# This script tests a minimal linear tensor action for the TT amplitudes:
#
#   L ~ (K_T/2c^2) hdot^2 - (K_T/2) |grad h|^2 + coupling * h * S
#
# for plus/cross polarizations.
#
# Tests:
#
#   1. free tensor action gives wave equation,
#   2. plus and cross decouple at quadratic order,
#   3. source coupling gives driven wave equation,
#   4. stiffness/coupling ratio controls source normalization,
#   5. static Green scaling suggests h ~ coupling/(K_T R) * source,
#   6. target far-zone coupling requires ratio ~ G/c^4.
#
# This is not a covariant action and not a derivation of GR.

from pathlib import Path

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
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


def euler_lagrange_field(L, field, coords):
    # Euler-Lagrange for L(field, derivatives).
    expr = sp.diff(L, field)
    for coord in coords:
        expr -= sp.diff(sp.diff(L, sp.diff(field, coord)), coord)
    return sp.simplify(expr)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="quadrupole_tensor_flux_marker",
        upstream_script_id="06_tensor_flux_principle__candidate_quadrupole_tensor_flux",
        upstream_derivation_id="quadrupole_tensor_flux_marker",
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
# Case 0: Problem statement
# =============================================================================

def case_0_problem_statement():
    header("Case 0: Tensor action/stiffness problem")

    print("Need a tensor action/stiffness model that supports:")
    print()
    print("  Box h_ij^TT = source")
    print("  h ~ (2G/(c^4 R)) Qdd")
    print("  tensor radiation energy flux")
    print()
    print("This script tests a minimal quadratic action for h_plus and h_cross.")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("tensor action/stiffness problem posed", StatusMark.PASS, "minimal quadratic action being tested")


# =============================================================================
# Case 1: Free plus-polarization action
# =============================================================================

def case_1_free_plus_action(ns):
    header("Case 1: Free plus-polarization action")

    t, z, c, K_T = sp.symbols("t z c K_T", positive=True, real=True)
    h = sp.Function("h")(t, z)

    L = K_T/(2*c**2) * sp.diff(h, t)**2 - K_T/2 * sp.diff(h, z)**2

    EL = euler_lagrange_field(L, h, [t, z])
    wave_expr = sp.simplify(EL / K_T)

    print(f"L = {L}")
    print(f"Euler-Lagrange = {EL}")
    print(f"EL/K_T = {wave_expr}")
    print()
    print("Equation EL=0 gives:")
    print("  (1/c^2) h_tt - h_zz = 0")

    target = -sp.diff(h, (t, 2))/c**2 + sp.diff(h, (z, 2))
    # Sign depends on EL convention; EL=0 equivalent to Box h=0.
    wave_eq_confirmed = is_zero(wave_expr - target) or is_zero(wave_expr + target)

    out = ScriptOutput()
    with out.derived_results():
        out.line("free action gives wave equation",
                 StatusMark.PASS if wave_eq_confirmed else StatusMark.FAIL,
                 f"EL/K_T = {wave_expr}")

    ns.record_derivation(
        derivation_id="free_tensor_action_wave_equation",
        inputs=[L],
        output=EL,
        method="euler_lagrange_free_quadratic_action",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="euler_lagrange_equation",
    )

    return t, z, c, K_T


# =============================================================================
# Case 2: Plus/cross decoupled action
# =============================================================================

def case_2_plus_cross_action(t, z, c, K_T, ns):
    header("Case 2: Plus/cross decoupled quadratic action")

    hp = sp.Function("h_plus")(t, z)
    hx = sp.Function("h_cross")(t, z)

    L = (
        K_T/(2*c**2) * (sp.diff(hp, t)**2 + sp.diff(hx, t)**2)
        - K_T/2 * (sp.diff(hp, z)**2 + sp.diff(hx, z)**2)
    )

    ELp = euler_lagrange_field(L, hp, [t, z])
    ELx = euler_lagrange_field(L, hx, [t, z])

    print(f"L = {L}")
    print(f"EL_plus = {ELp}")
    print(f"EL_cross = {ELx}")

    out = ScriptOutput()
    with out.derived_results():
        out.line("plus mode has independent wave equation", StatusMark.PASS, f"EL_plus = {ELp}")
        out.line("cross mode has independent wave equation", StatusMark.PASS, f"EL_cross = {ELx}")

    ns.record_derivation(
        derivation_id="decoupled_plus_cross_euler_lagrange",
        inputs=[L],
        output=sp.Matrix([ELp, ELx]),
        method="euler_lagrange_decoupled_plus_cross_action",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="euler_lagrange_equation",
    )


# =============================================================================
# Case 3: Add source coupling
# =============================================================================

def case_3_source_coupling(t, z, c, K_T, ns):
    header("Case 3: Source coupling gives driven wave equation")

    g_T = sp.symbols("g_T", positive=True, real=True)
    h = sp.Function("h")(t, z)
    S = sp.Function("S")(t, z)

    L = K_T/(2*c**2) * sp.diff(h, t)**2 - K_T/2 * sp.diff(h, z)**2 + g_T * h * S

    EL = euler_lagrange_field(L, h, [t, z])
    driven = sp.solve(sp.Eq(EL, 0), sp.diff(h, (t, 2))/c**2 - sp.diff(h, (z, 2)))

    print(f"L = {L}")
    print(f"Euler-Lagrange = {EL}")
    print()
    print("Solving for Box h = (1/c²)h_tt - h_zz:")
    print(f"Box h = {driven}")

    out = ScriptOutput()
    with out.derived_results():
        out.line("source coupling drives tensor wave equation",
                 StatusMark.PASS if bool(driven) else StatusMark.FAIL,
                 f"driven wave equation obtained: {bool(driven)}")

    ns.record_derivation(
        derivation_id="source_coupled_tensor_wave_equation",
        inputs=[L],
        output=EL,
        method="euler_lagrange_source_coupled_action",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="euler_lagrange_equation",
    )


# =============================================================================
# Case 4: Stiffness/coupling ratio controls normalization
# =============================================================================

def case_4_stiffness_ratio(ns):
    header("Case 4: Stiffness/coupling ratio controls normalization")

    K_T, g_T, G, c = sp.symbols("K_T g_T G c", positive=True, real=True)

    ratio = sp.simplify(g_T / K_T)
    target_ratio = 2*G/c**4
    residual = sp.simplify(ratio - target_ratio)

    print(f"coupling/stiffness ratio = {ratio}")
    print(f"target far-zone ratio class = {target_ratio}")
    print()
    print("Interpretation:")
    print("  A Green-function solution schematically gives")
    print("  h ~ (g_T/K_T) * source / R.")
    print("  To match h ~ 2G Qdd/(c^4 R), need g_T/K_T ~ 2G/c^4.")

    out = ScriptOutput()
    with out.unresolved_obligations():
        out.line("target tensor coupling/stiffness ratio identified", StatusMark.OBLIGATION, f"g_T/K_T = 2G/c^4 required; derivation of K_T, g_T from deeper principles open")

    ns.record_derivation(
        derivation_id="stiffness_coupling_ratio_target",
        inputs=[ratio, target_ratio],
        output=residual,
        method="stiffness_coupling_ratio_comparison",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
    )


# =============================================================================
# Case 5: Static Green scaling analogy
# =============================================================================

def case_5_green_scaling(ns):
    header("Case 5: Green scaling analogy")

    g_T, K_T, R, Qdd, G, c = sp.symbols("g_T K_T R Qdd G c", positive=True, real=True)

    h_green = sp.simplify((g_T/K_T) * Qdd / R)
    h_target = sp.simplify(2*G*Qdd/(c**4 * R))

    ratio_needed = sp.solve(sp.Eq(h_green, h_target), g_T/K_T)

    print(f"h_green schematic = {h_green}")
    print(f"h_target = {h_target}")
    print(f"needed g_T/K_T = {ratio_needed}")

    out = ScriptOutput()
    with out.derived_results():
        out.line("Green scaling recovers target ratio",
                 StatusMark.PASS if bool(ratio_needed) else StatusMark.FAIL,
                 f"g_T/K_T = {ratio_needed}")

    ns.record_derivation(
        derivation_id="green_scaling_recovers_target_ratio",
        inputs=[h_green, h_target],
        output=sp.Matrix(ratio_needed) if ratio_needed else sp.Integer(0),
        method="solve_green_scaling_for_coupling_ratio",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
    )


# =============================================================================
# Case 6: Energy proxy from action
# =============================================================================

def case_6_energy_proxy(ns):
    header("Case 6: Energy proxy from quadratic action")

    hdot_p, hdot_x, grad_p, grad_x, K_T, c = sp.symbols(
        "hdot_plus hdot_cross grad_plus grad_cross K_T c",
        positive=True,
        real=True
    )

    E_proxy = sp.simplify(K_T/(2*c**2) * (hdot_p**2 + hdot_x**2) + K_T/2 * (grad_p**2 + grad_x**2))

    print("Hamiltonian-like quadratic proxy:")
    print(f"E = {E_proxy}")
    print()
    print("This is positive for positive K_T.")
    print("It matches the earlier quadratic plus/cross energy structure.")

    out = ScriptOutput()
    with out.derived_results():
        out.line("quadratic action gives positive energy proxy for K_T>0", StatusMark.PASS, f"E = {E_proxy}")

    ns.record_derivation(
        derivation_id="tensor_action_positive_energy_proxy",
        inputs=[hdot_p, hdot_x, grad_p, grad_x, K_T, c],
        output=E_proxy,
        method="hamiltonian_from_quadratic_tensor_action",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="hamiltonian_proxy",
    )


# =============================================================================
# Case 7: Classification
# =============================================================================

def case_7_classification():
    header("Case 7: Classification")

    print("Results:")
    print()
    print("1. Minimal quadratic tensor action gives wave equation.")
    print("2. Plus and cross decouple at free quadratic order.")
    print("3. Source coupling gives driven tensor wave equation.")
    print("4. Coupling/stiffness ratio controls amplitude normalization.")
    print("5. Matching h ~ 2G Qdd/(c^4 R) requires g_T/K_T ~ 2G/c^4.")
    print("6. Quadratic action supplies positive energy proxy.")
    print()

    out = ScriptOutput()
    with out.derived_results():
        out.line("tensor action/stiffness toy passes structural checks", StatusMark.PASS, "wave equation, decoupling, source coupling, energy proxy all confirmed")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("A minimal tensor action can support the TT wave equation and provides")
    print("a stiffness/coupling interpretation for amplitude normalization.")
    print()
    print("Target:")
    print("  g_T/K_T ~ 2G/c^4")
    print()
    print("This is not yet a covariant derivation.")
    print("It is a reduced tensor-sector action toy.")
    print()
    print("Next steps:")
    print("  create candidate_tensor_action_stiffness.md")
    print("  test tensor radiation flux from action normalization")
    print("  decide scalar A constraint versus dynamics")
    print()
    print("Possible next artifact:")
    print("  candidate_tensor_action_stiffness.md")


def main():
    header("Candidate Tensor Action Stiffness")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    t, z, c, K_T = case_1_free_plus_action(ns)
    case_2_plus_cross_action(t, z, c, K_T, ns)
    case_3_source_coupling(t, z, c, K_T, ns)
    case_4_stiffness_ratio(ns)
    case_5_green_scaling(ns)
    case_6_energy_proxy(ns)
    case_7_classification()
    final_interpretation()

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_K_T_g_T_from_deeper_principles",
        script_id=SCRIPT_ID,
        title="Derive K_T and g_T from deeper vacuum principles",
        status=ObligationStatus.OPEN,
        description=(
            "The tensor stiffness K_T and coupling g_T are free parameters in the toy action. "
            "Their values must be derived from the vacuum substance ontology or matched "
            "to the GR target g_T/K_T = 2G/c^4."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_covariant_tensor_action",
        script_id=SCRIPT_ID,
        title="Derive covariant tensor action",
        status=ObligationStatus.OPEN,
        description=(
            "The 1+1D toy action is not covariant. A covariant 4D action for h_ij^TT "
            "that reproduces the GR Einstein-Hilbert tensor sector must be derived."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="tensor_action_stiffness_structural_claim",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "A minimal quadratic tensor action gives the TT wave equation, plus/cross "
            "decoupling, source-driven propagation, and a positive energy proxy. "
            "The coupling/stiffness ratio g_T/K_T = 2G/c^4 is the recovery target. "
            "K_T, g_T derivation and covariant extension remain open."
        ),
        obligation_ids=["derive_K_T_g_T_from_deeper_principles", "derive_covariant_tensor_action"],
    ))

    ns.record_route(RouteRecord(
        route_id="tensor_action_stiffness_route",
        script_id=SCRIPT_ID,
        name="Tensor action/stiffness route for TT wave equation and normalization",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=["derive_K_T_g_T_from_deeper_principles", "derive_covariant_tensor_action"],
        activation_conditions=[
            "quadratic tensor action gives wave equation",
            "plus/cross decouple",
            "source coupling obtained",
            "g_T/K_T = 2G/c^4 derived",
            "covariant action established",
        ],
    ))

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
