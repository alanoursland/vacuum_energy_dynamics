# Group:
#   04_source_law_interior
#
# Script type:
#   DIAGNOSTIC
#
# Candidate pressure/stress source extension
#
# Purpose
# -------
# The reduced static spherical program currently has:
#
#   A-flux law:
#     F_A(r) = 4*pi*r**2*A'(r)
#     F_A(r) = 8*pi*G*M_enc(r)/c**2
#
# and:
#
#   exterior kappa = 0
#
# This works for the exact Schwarzschild exterior. But interior comparison
# with the GR constant-density Schwarzschild solution shows missing
# second-order structure inside matter.
#
# The likely missing physics is pressure/stress and/or traceful interior
# kappa response.
#
# This script tests simple source-channel hypotheses:
#
#   H1. pressure modifies A-flux source directly,
#   H2. pressure/stress sources kappa inside,
#   H3. pressure corrections vanish at boundary and preserve exterior flux,
#   H4. GR interior residual can be shaped by a pressure-like profile.
#
# IMPORTANT:
# This is a reduced diagnostic script. It does not derive the TOV equation
# or a full relativistic matter coupling.

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


def header(title: str) -> None:
    print()
    print("=" * 112)
    print(title)
    print("=" * 112)


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    return archive, ns, invalidated


def series_u(expr, u, order):
    return sp.simplify(sp.series(expr, u, 0, order).removeO())


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: Problem statement")

    print("Current reduced source law:")
    print()
    print("  F_A(r) = 4*pi*r^2*A'(r)")
    print("  F_A(r) = 8*pi*G*M_enc(r)/c^2")
    print()
    print("This captures exterior Schwarzschild and weak-field interior potential.")
    print()
    print("But GR interior comparison shows missing second-order structure.")
    print("Candidate missing channels:")
    print("  pressure/stress source for A-flux")
    print("  pressure/stress source for interior kappa")
    print("  nonlinear interior self-field correction")
    print()

    with out.governance_assessments():
        out.line("pressure/stress source question isolated",
                 StatusMark.PASS,
                 "density-only A-flux law misses second-order interior structure vs GR")

    with out.unresolved_obligations():
        out.line("derive pressure/stress coupling to A-flux or interior kappa",
                 StatusMark.OBLIGATION,
                 "hypotheses H1-H4 are diagnostic; no first-principles derivation given")


def case_1_gr_pressure_profile_weak_order(out: ScriptOutput, ns=None):
    header("Case 1: GR constant-density pressure profile expansion")

    x, u, rho0, c = sp.symbols("x u rho0 c", positive=True, real=True)

    # Exact GR interior Schwarzschild pressure:
    # p/(rho c^2) = [sqrt(1-u x^2) - sqrt(1-u)] /
    #               [3 sqrt(1-u) - sqrt(1-u x^2)]
    p_over_rhoc2 = (sp.sqrt(1-u*x**2) - sp.sqrt(1-u)) / (
        3*sp.sqrt(1-u) - sp.sqrt(1-u*x**2)
    )

    p_series = series_u(p_over_rhoc2, u, 3)

    print("Dimensionless pressure profile for GR constant-density interior:")
    print("  p/(rho c^2) = [sqrt(1-u x^2)-sqrt(1-u)] /")
    print("                 [3sqrt(1-u)-sqrt(1-u x^2)]")
    print()
    print(f"p/(rho c^2) series through u^2 = {p_series}")

    leading = series_u(p_over_rhoc2, u, 2)
    print(f"leading pressure ratio = {leading}")

    starts_at_order_u = not is_zero(leading)
    vanishes_at_surface = is_zero(sp.simplify(p_over_rhoc2.subs(x, 1)))

    with out.derived_results():
        out.line("pressure begins at order u",
                 StatusMark.PASS if starts_at_order_u else StatusMark.FAIL,
                 f"leading = {leading}")
        out.line("pressure vanishes at surface x=1",
                 StatusMark.PASS if vanishes_at_surface else StatusMark.FAIL)

    if ns is not None:
        ns.record_derivation(
            derivation_id="gr_pressure_profile_weak_field_series",
            inputs=[p_over_rhoc2, x, u],
            output=leading,
            method="series_u(p/rho_c^2, u, 2)",
            status=Status.DERIVED,
            record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
            scope="GR constant-density interior pressure, weak-field series",
        )


def case_2_A_residual_vs_pressure_shape(out: ScriptOutput, ns=None):
    header("Case 2: A residual versus pressure-like shape")

    x, u = sp.symbols("x u", real=True)

    A_red = 1 - sp.Rational(3, 2)*u + sp.Rational(1, 2)*u*x**2
    A_gr = sp.Rational(1, 4) * (3*sp.sqrt(1-u) - sp.sqrt(1-u*x**2))**2

    residual = sp.simplify(A_gr - A_red)
    residual_leading = sp.simplify(series_u(residual, u, 3).coeff(u, 2) * u**2)

    # Leading GR pressure shape p/(rho c^2) ~ u(1-x^2)/4.
    # A residual leading is ~ 3 u^2 (1-x^2)^2 / 16.
    pressure_shape = u*(1-x**2)/4
    pressure_squared_shape = sp.simplify(3 * pressure_shape**2)

    print(f"A_GR - A_red leading = {residual_leading}")
    print(f"leading pressure shape = {pressure_shape}")
    print(f"3 * pressure_shape^2 = {pressure_squared_shape}")
    print(f"difference = {sp.simplify(residual_leading - pressure_squared_shape)}")

    residual_shape_match = is_zero(residual_leading - pressure_squared_shape)

    with out.derived_results():
        out.line("A residual has pressure-squared-like boundary shape",
                 StatusMark.PASS if residual_shape_match else StatusMark.FAIL,
                 f"leading residual = {residual_leading}")

    print()
    print("Interpretation:")
    print("  The A residual begins at order u^2 and has shape (1-x^2)^2.")
    print("  This resembles a second-order pressure/self-field correction.")

    if ns is not None:
        ns.record_derivation(
            derivation_id="A_residual_pressure_shape_comparison",
            inputs=[residual_leading, pressure_squared_shape],
            output=sp.simplify(residual_leading - pressure_squared_shape),
            method="series comparison of A_GR - A_red vs 3*(u*(1-x^2)/4)^2",
            status=Status.DERIVED,
            record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
            scope="leading order A residual vs pressure-squared shape",
        )


def case_3_pressure_direct_A_flux_hypothesis(out: ScriptOutput):
    header("Case 3: Pressure as direct A-flux source hypothesis")

    r, G, c, rho, p, chi = sp.symbols("r G c rho p chi", positive=True, real=True)

    # Hypothesis:
    #   Delta_areal A = 8*pi*G/c^2 * (rho + chi*p/c^2)
    source = 8*sp.pi*G/c**2 * (rho + chi*p/c**2)

    print("Hypothesis H1:")
    print()
    print("  Delta_areal A = 8*pi*G/c^2 * (rho + chi p/c^2)")
    print()
    print(f"source = {source}")
    print()
    print("Consequences:")
    print("  pressure changes A-flux directly.")
    print("  if pressure vanishes at boundary, exterior flux can still be set by")
    print("  integrated effective source.")
    print()

    with out.governance_assessments():
        out.line("direct pressure A-source hypothesis formulated",
                 StatusMark.PASS,
                 "H1 is a candidate; coefficient chi and coupling form not derived")

    with out.unresolved_obligations():
        out.line("derive direct pressure A-flux coupling coefficient chi",
                 StatusMark.OBLIGATION,
                 "H1 requires coefficient chi from matter coupling; not derived")


def case_4_pressure_as_kappa_source_hypothesis(out: ScriptOutput, ns=None):
    header("Case 4: Pressure/stress as kappa-source hypothesis")

    kappa, C_k, rho, p, a, b, c = sp.symbols("kappa C_k rho p a b c", real=True)

    # Toy trace-like source:
    # J_k = a*rho*c^2 + b*p
    # In units-free reduced form, use J_k as a linear source.
    J_k = a*rho*c**2 + b*p
    E = C_k*kappa**2 - J_k*kappa

    eq = sp.Eq(sp.diff(E, kappa), 0)
    sol = sp.solve(eq, kappa)

    print("Hypothesis H2:")
    print()
    print("  pressure/stress sources interior kappa")
    print()
    print(f"J_k = {J_k}")
    print(f"E = {E}")
    print(f"stationary equation = {eq}")
    print(f"kappa_eq = {sol}")
    print()
    print("If J_k vanishes in exterior, kappa relaxes to zero outside.")

    with out.governance_assessments():
        out.line("pressure/stress kappa-source hypothesis formulated",
                 StatusMark.PASS if bool(sol) else StatusMark.FAIL,
                 "H2 is a candidate; coupling coefficients a, b not derived")

    with out.unresolved_obligations():
        out.line("derive pressure/stress kappa source coefficients a and b",
                 StatusMark.OBLIGATION,
                 "H2 requires coupling a, b from matter coupling; not derived")

    if ns is not None:
        ns.record_derivation(
            derivation_id="pressure_kappa_source_toy_response",
            inputs=[J_k, C_k],
            output=sol[0] if sol else sp.nan,
            method="stationary equation of C_k*kappa^2 - J_k*kappa",
            status=Status.DERIVED,
            record_kind=RecordKind.SAMPLE_DERIVATION,
            scope="toy energy penalty model with pressure/stress source",
        )


def case_5_boundary_preservation_conditions(out: ScriptOutput, ns=None):
    header("Case 5: Boundary preservation conditions")

    x, u = sp.symbols("x u", real=True)

    pressure_shape = u*(1-x**2)/4
    kappa_shape = -3*u*(1-x**2)/4
    A_residual_shape = 3*u**2*(1-x**2)**2/16

    print(f"pressure leading shape ~ {pressure_shape}")
    print(f"kappa leading GR diagnostic shape ~ {kappa_shape}")
    print(f"A residual leading shape ~ {A_residual_shape}")
    print()
    print(f"pressure at boundary = {sp.simplify(pressure_shape.subs(x, 1))}")
    print(f"kappa at boundary = {sp.simplify(kappa_shape.subs(x, 1))}")
    print(f"A residual at boundary = {sp.simplify(A_residual_shape.subs(x, 1))}")
    print(f"A residual derivative at boundary = {sp.simplify(sp.diff(A_residual_shape, x).subs(x, 1))}")

    p_vanishes = is_zero(pressure_shape.subs(x, 1))
    k_vanishes = is_zero(kappa_shape.subs(x, 1))
    a_smooth = is_zero(sp.diff(A_residual_shape, x).subs(x, 1))

    with out.derived_results():
        out.line("pressure-like corrections vanish at boundary",
                 StatusMark.PASS if p_vanishes else StatusMark.FAIL,
                 f"p(x=1) = {sp.simplify(pressure_shape.subs(x, 1))}")
        out.line("kappa-like corrections vanish at boundary",
                 StatusMark.PASS if k_vanishes else StatusMark.FAIL,
                 f"kappa(x=1) = {sp.simplify(kappa_shape.subs(x, 1))}")
        out.line("A residual is boundary-smooth",
                 StatusMark.PASS if a_smooth else StatusMark.FAIL,
                 f"dA_residual/dx(x=1) = {sp.simplify(sp.diff(A_residual_shape, x).subs(x, 1))}")

    print()
    print("Interpretation:")
    print("  Interior pressure/stress corrections can be boundary-contained.")
    print("  This lets exterior A-flux and kappa=0 remain intact.")

    if ns is not None:
        ns.record_derivation(
            derivation_id="pressure_correction_boundary_vanishing_check",
            inputs=[pressure_shape, kappa_shape, A_residual_shape, x],
            output=sp.Matrix([
                sp.simplify(pressure_shape.subs(x, 1)),
                sp.simplify(kappa_shape.subs(x, 1)),
                sp.simplify(sp.diff(A_residual_shape, x).subs(x, 1)),
            ]),
            method="evaluate pressure/kappa/A-residual leading shapes at x=1",
            status=Status.DERIVED,
            record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
            scope="boundary behavior of pressure and kappa leading shapes",
        )


def case_6_channel_classification(out: ScriptOutput):
    header("Case 6: Source-channel classification")

    print("Candidate source channels:")
    print()
    print("1. Density -> A-flux")
    print("   F_A = 8*pi*G*M_enc/c^2")
    print("   controls exterior mass field")
    print()
    print("2. Pressure/stress -> interior kappa")
    print("   traceful matter response")
    print("   should vanish or relax at boundary")
    print()
    print("3. Pressure/self-field -> second-order A residual")
    print("   interior-supported correction")
    print("   boundary-smooth so exterior Schwarzschild remains")
    print()
    print("4. Exterior source-free vacuum")
    print("   kappa -> 0")
    print("   A-flux conserved")
    print("   B = 1/A")
    print()

    with out.governance_assessments():
        out.line("source-channel map separated",
                 StatusMark.PASS,
                 "four distinct channels identified; none fully derived")


def final_interpretation():
    header("Final interpretation")

    print("Pressure/stress likely belongs to the interior problem, not the")
    print("ordinary exterior mass-flux law.")
    print()
    print("The cleanest current hypothesis is:")
    print()
    print("  density / total mass fixes exterior A-flux,")
    print("  pressure and stress source interior kappa and/or boundary-smooth")
    print("  second-order A corrections,")
    print("  source-free exterior suppresses kappa and conserves A-flux.")
    print()
    print("Possible next artifact:")
    print("  candidate_pressure_stress_source_extension.md")


def main():
    header("Candidate Pressure/Stress Source Extension")
    archive, ns, invalidated = prepare_archive()
    if invalidated:
        print("[INFO] Archive invalidated due to source change.")

    out = ScriptOutput()

    case_0_problem_statement(out)
    case_1_gr_pressure_profile_weak_order(out, ns)
    case_2_A_residual_vs_pressure_shape(out, ns)
    case_3_pressure_direct_A_flux_hypothesis(out)
    case_4_pressure_as_kappa_source_hypothesis(out, ns)
    case_5_boundary_preservation_conditions(out, ns)
    case_6_channel_classification(out)
    final_interpretation()

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_pressure_A_flux_coupling",
        script_id=SCRIPT_ID,
        title="Derive pressure coupling coefficient for direct A-flux source (H1)",
        status=ObligationStatus.OPEN,
        description=(
            "Hypothesis H1 proposes Delta_areal A = 8piG/c^2 * (rho + chi*p/c^2). "
            "The coefficient chi and the full coupling form are not derived from "
            "first principles. A covariant source action is missing."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_pressure_kappa_source_coefficients",
        script_id=SCRIPT_ID,
        title="Derive pressure/stress kappa source coefficients (H2)",
        status=ObligationStatus.OPEN,
        description=(
            "Hypothesis H2 proposes J_k = a*rho*c^2 + b*p as interior kappa source. "
            "Coefficients a and b are not derived from matter coupling. The full "
            "source law form has not been established."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="pressure_corrections_boundary_contained",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.HEURISTIC,
        statement=(
            "Interior pressure and stress corrections can in principle be boundary-"
            "contained: they vanish at the source boundary and are boundary-smooth, "
            "leaving exterior A-flux and kappa=0 intact. This is a diagnostic "
            "assessment based on leading-order shape comparison, not a derivation."
        ),
        obligation_ids=["derive_pressure_A_flux_coupling",
                        "derive_pressure_kappa_source_coefficients"],
    ))

    ns.record_route(RouteRecord(
        route_id="density_mass_flux_pressure_kappa_split_route",
        script_id=SCRIPT_ID,
        name="Density -> A-flux; pressure/stress -> interior kappa split",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=["derive_pressure_A_flux_coupling",
                              "derive_pressure_kappa_source_coefficients"],
    ))

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
