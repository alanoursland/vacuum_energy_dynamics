# Group:
#   04_source_law_interior
#
# Script type:
#   DERIVATION
#
# Candidate interior A source model
#
# Purpose
# -------
# The exact static spherical exterior branch now uses an areal-flux law:
#
#   F_A(r) = 4*pi*r**2*A'(r)
#   F_A(r) = 8*pi*G*M_enc(r)/c**2
#
# Outside the source:
#
#   M_enc(r) = M
#
# so:
#
#   A(r) = 1 - 2GM/(c**2*r)
#
# and with kappa=0:
#
#   B = 1/A
#
# This recovers exact Schwarzschild exterior metric factors.
#
# This script tests whether the same areal-flux source law behaves sensibly
# inside a finite spherical source.
#
# Main test:
#
#   constant-density sphere:
#     rho(r) = rho0 for 0 <= r <= R
#     M_enc(r) = (4*pi/3) rho0 r**3
#
# Then:
#
#   A'(r) = 2G M_enc(r)/(c**2 r**2)
#         = (8*pi*G*rho0/(3*c**2)) r
#
# and:
#
#   A_in(r) = C + (4*pi*G*rho0/(3*c**2)) r**2
#
# Match A and A' at r=R to exterior:
#
#   A_out(r) = 1 - 2GM/(c**2*r)
#   M = (4*pi/3) rho0 R**3
#
# This is NOT the full GR interior Schwarzschild solution.
# It is the interior solution of the reduced areal-flux law.

from pathlib import Path

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.core.context import TheoryContext
from vacuumforge.governance import (
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    RecordKind,
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
    print("=" * 108)
    print(title)
    print("=" * 108)


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def delta_areal(f, r):
    return sp.simplify((1/r**2) * sp.diff(r**2 * sp.diff(f, r), r))


def areal_flux(f, r):
    return sp.simplify(4 * sp.pi * r**2 * sp.diff(f, r))


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="mechanics_areal_flux_metric",
        upstream_script_id="02_mechanics__candidate_areal_flux_principle",
        upstream_derivation_id="areal_flux_exact_metric_check",
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
# Case 0: Areal-flux source law recap
# =============================================================================

def case_0_recap(out: ScriptOutput):
    header("Case 0: Areal-flux source law recap")

    print("Exact reduced source law:")
    print()
    print("  Delta_areal A = 8*pi*G*rho/c^2")
    print()
    print("where:")
    print()
    print("  Delta_areal A = (1/r^2)(r^2 A')'")
    print()
    print("Equivalent flux law:")
    print()
    print("  F_A(r) = 4*pi*r^2 A'")
    print("  F_A(r) = 8*pi*G*M_enc(r)/c^2")
    print()
    print("Interior test:")
    print()
    print("  M_enc(r) varies with r inside the source.")
    print("  Check whether A, A', and flux match smoothly to exterior.")

    with out.derived_results():
        out.line("areal-flux law has interior enclosed-mass form",
                 StatusMark.PASS, "F_A = 8*pi*G*M_enc/c^2 holds for varying M_enc(r)")


# =============================================================================
# Case 1: Constant-density enclosed mass
# =============================================================================

def case_1_constant_density_enclosed_mass(out: ScriptOutput, ns=None):
    header("Case 1: Constant-density enclosed mass")

    r, rho0 = sp.symbols("r rho0", positive=True, real=True)

    M_enc = sp.Rational(4, 3) * sp.pi * rho0 * r**3
    M_enc_prime = sp.diff(M_enc, r)
    expected = 4 * sp.pi * r**2 * rho0

    print(f"rho(r) = {rho0}")
    print(f"M_enc(r) = {M_enc}")
    print(f"M_enc'(r) = {M_enc_prime}")
    print(f"4*pi*r^2*rho0 = {expected}")

    residual = sp.simplify(M_enc_prime - expected)
    ok = is_zero(residual)

    with out.derived_results():
        out.line("M_enc derivative matches density volume element",
                 StatusMark.PASS if ok else StatusMark.FAIL,
                 f"residual = {residual}")

    if ns is not None:
        ns.record_derivation(
            derivation_id="constant_density_enclosed_mass_derivative",
            inputs=[M_enc, r],
            output=residual,
            method="diff(M_enc, r) - 4*pi*r^2*rho0",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="identity_residual",
        )


# =============================================================================
# Case 2: Interior A solution from flux law
# =============================================================================

def case_2_interior_A_solution(out: ScriptOutput, ns=None):
    header("Case 2: Interior A solution from flux law")

    r, G, c, rho0, C = sp.symbols("r G c rho0 C", positive=True, real=True)

    M_enc = sp.Rational(4, 3) * sp.pi * rho0 * r**3
    A_prime = sp.simplify(2 * G * M_enc / (c**2 * r**2))
    A_in = sp.simplify(C + sp.integrate(A_prime, r))

    print(f"M_enc(r) = {M_enc}")
    print(f"A'(r) = 2G M_enc/(c^2 r^2) = {A_prime}")
    print(f"A_in(r) = {A_in}")

    lhs = delta_areal(A_in, r)
    rhs = 8 * sp.pi * G * rho0 / c**2

    print()
    print(f"Delta_areal A_in = {lhs}")
    print(f"8*pi*G*rho0/c^2 = {rhs}")

    residual = sp.simplify(lhs - rhs)
    ok = is_zero(residual)

    with out.derived_results():
        out.line("interior A solves areal source equation",
                 StatusMark.PASS if ok else StatusMark.FAIL,
                 f"Delta_areal A_in - 8piGrho/c^2 = {residual}")

    if ns is not None:
        ns.record_derivation(
            derivation_id="interior_A_areal_source_residual",
            inputs=[A_in, r, rho0],
            output=residual,
            method="delta_areal(A_in) - 8*pi*G*rho0/c^2",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="identity_residual",
        )

    return A_in


# =============================================================================
# Case 3: Match to exterior at r=R
# =============================================================================

def case_3_match_to_exterior(out: ScriptOutput, ns=None):
    header("Case 3: Match interior to exterior at r=R")

    r, R, G, c, rho0, C = sp.symbols("r R G c rho0 C", positive=True, real=True)

    M = sp.Rational(4, 3) * sp.pi * rho0 * R**3
    r_s = 2 * G * M / c**2

    A_in = C + 4 * sp.pi * G * rho0 * r**2 / (3 * c**2)
    A_out = 1 - r_s / r

    A_in_R = sp.simplify(A_in.subs(r, R))
    A_out_R = sp.simplify(A_out.subs(r, R))

    C_solution = sp.solve(sp.Eq(A_in_R, A_out_R), C)
    C_match = sp.simplify(C_solution[0]) if C_solution else None
    A_in_matched = sp.simplify(A_in.subs(C, C_match))

    print(f"M = {M}")
    print(f"r_s = {sp.simplify(r_s)}")
    print(f"A_in = {A_in}")
    print(f"A_out = {A_out}")
    print()
    print(f"A_in(R) = {A_in_R}")
    print(f"A_out(R) = {A_out_R}")
    print(f"C solution = {C_solution}")
    print(f"A_in matched = {A_in_matched}")

    with out.derived_results():
        out.line("A continuity fixes interior constant",
                 StatusMark.PASS if bool(C_solution) else StatusMark.FAIL,
                 f"C = {C_match}")

    dA_in_R = sp.simplify(sp.diff(A_in_matched, r).subs(r, R))
    dA_out_R = sp.simplify(sp.diff(A_out, r).subs(r, R))

    print()
    print(f"A_in'(R) = {dA_in_R}")
    print(f"A_out'(R) = {dA_out_R}")

    derivative_residual = sp.simplify(dA_in_R - dA_out_R)
    deriv_ok = is_zero(derivative_residual)

    with out.derived_results():
        out.line("A' matches at boundary",
                 StatusMark.PASS if deriv_ok else StatusMark.FAIL,
                 f"A_in'(R) - A_out'(R) = {derivative_residual}")

    ctx = TheoryContext("candidate_interior_A_source_model")
    ctx.define_equal_response_algebraic_symbols()
    ms = ctx._mode_symbols
    flux_expr = sp.simplify(4 * sp.pi * ms.r**2 * sp.diff(1 - 2 * ms.G * ms.M / (ms.c**2 * ms.r), ms.r))
    flux_ok = is_zero(flux_expr - 8 * sp.pi * ms.G * ms.M / ms.c**2)

    with out.derived_results():
        out.line("VacuumForge context reproduces exterior flux normalization",
                 StatusMark.PASS if flux_ok else StatusMark.FAIL)

    if ns is not None:
        ns.record_derivation(
            derivation_id="interior_A_boundary_matching",
            inputs=[R, rho0],
            output=sp.Eq(dA_in_R, dA_out_R),
            method="interior_A_match_to_exterior",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="boundary_matching",
        )

    return A_in_matched, A_out, M


# =============================================================================
# Case 4: Flux continuity at boundary
# =============================================================================

def case_4_flux_continuity(out: ScriptOutput, ns=None):
    header("Case 4: Flux continuity at source boundary")

    r, R, G, c, rho0 = sp.symbols("r R G c rho0", positive=True, real=True)

    M = sp.Rational(4, 3) * sp.pi * rho0 * R**3
    A_in = 1 - 4*sp.pi*G*rho0*R**2/c**2 + 4*sp.pi*G*rho0*r**2/(3*c**2)
    A_out = 1 - 2*G*M/(c**2*r)

    F_in_R = sp.simplify(areal_flux(A_in, r).subs(r, R))
    F_out_R = sp.simplify(areal_flux(A_out, r).subs(r, R))
    target = sp.simplify(8*sp.pi*G*M/c**2)

    print(f"F_in(R) = {F_in_R}")
    print(f"F_out(R) = {F_out_R}")
    print(f"target  = {target}")

    flux_match = is_zero(F_in_R - F_out_R)
    mass_norm = is_zero(F_out_R - target)

    with out.derived_results():
        out.line("interior flux at boundary equals exterior flux",
                 StatusMark.PASS if flux_match else StatusMark.FAIL,
                 f"F_in(R) - F_out(R) = {sp.simplify(F_in_R - F_out_R)}")
        out.line("boundary flux equals mass normalization",
                 StatusMark.PASS if mass_norm else StatusMark.FAIL,
                 f"F_out(R) - target = {sp.simplify(F_out_R - target)}")

    if ns is not None:
        ns.record_derivation(
            derivation_id="interior_flux_continuity_at_boundary",
            inputs=[F_in_R, F_out_R],
            output=sp.simplify(F_in_R - F_out_R),
            method="areal_flux_continuity_check",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="identity_residual",
        )


# =============================================================================
# Case 5: Regularity at origin
# =============================================================================

def case_5_origin_regularity(out: ScriptOutput):
    header("Case 5: Regularity at origin")

    r, R, G, c, rho0 = sp.symbols("r R G c rho0", positive=True, real=True)

    A_in = 1 - 4*sp.pi*G*rho0*R**2/c**2 + 4*sp.pi*G*rho0*r**2/(3*c**2)

    A0 = sp.simplify(A_in.subs(r, 0))
    dA0 = sp.simplify(sp.diff(A_in, r).subs(r, 0))
    F0 = sp.simplify(areal_flux(A_in, r).subs(r, 0))

    print(f"A_in(r) = {A_in}")
    print(f"A_in(0) = {A0}")
    print(f"A_in'(0) = {dA0}")
    print(f"F_A(0) = {F0}")

    with out.derived_results():
        out.line("A is finite at origin", StatusMark.PASS, f"A(0) = {A0}")
        out.line("A' vanishes at origin",
                 StatusMark.PASS if is_zero(dA0) else StatusMark.FAIL, f"A'(0) = {dA0}")
        out.line("flux vanishes at origin",
                 StatusMark.PASS if is_zero(F0) else StatusMark.FAIL, f"F(0) = {F0}")


# =============================================================================
# Case 6: Interior B from kappa=0
# =============================================================================

def case_6_interior_B_from_kappa_zero(out: ScriptOutput):
    header("Case 6: Interior B from kappa=0")

    r, R, G, c, rho0 = sp.symbols("r R G c rho0", positive=True, real=True)

    A_in = 1 - 4*sp.pi*G*rho0*R**2/c**2 + 4*sp.pi*G*rho0*r**2/(3*c**2)
    kappa = sp.Integer(0)
    B_in = sp.simplify(1 / A_in)
    AB = sp.simplify(A_in * B_in)

    print(f"A_in = {A_in}")
    print(f"kappa = {kappa}")
    print(f"B_in = 1/A_in = {B_in}")
    print(f"A_in B_in = {AB}")

    with out.sample_results():
        out.line("kappa=0 gives reciprocal interior B",
                 StatusMark.PASS if is_zero(AB - 1) else StatusMark.FAIL,
                 "by-construction: B=1/A when kappa=0")

    print()
    print("Caution:")
    print("  This is the reciprocal interior metric implied by the reduced model.")
    print("  It is not the GR interior Schwarzschild solution.")


# =============================================================================
# Case 7: Compare with weak-field Newtonian potential form
# =============================================================================

def case_7_compare_newtonian_interior_potential(out: ScriptOutput, ns=None):
    header("Case 7: Weak-field comparison to constant-density Newtonian potential")

    r, R, G, c, rho0 = sp.symbols("r R G c rho0", positive=True, real=True)

    A_in = 1 - 4*sp.pi*G*rho0*R**2/c**2 + 4*sp.pi*G*rho0*r**2/(3*c**2)

    # In weak field, A ≈ 1 + 2 Phi/c^2.
    Phi_from_A = sp.simplify((c**2/2) * (A_in - 1))

    print(f"A_in = {A_in}")
    print("Using A ≈ 1 + 2 Phi/c²:")
    print(f"Phi_from_A = {Phi_from_A}")

    # Newtonian potential inside uniform sphere with Phi(infty)=0:
    # Phi(r) = -GM(3R^2-r^2)/(2R^3)
    # with M=(4π/3)ρR^3 -> Phi = -2πGρR^2 + (2πGρ/3)r^2
    Phi_expected = -2*sp.pi*G*rho0*R**2 + 2*sp.pi*G*rho0*r**2/3

    print(f"Phi_expected = {Phi_expected}")

    residual = sp.simplify(Phi_from_A - Phi_expected)
    ok = is_zero(residual)

    with out.derived_results():
        out.line("A interior matches weak-field Newtonian potential normalization",
                 StatusMark.PASS if ok else StatusMark.FAIL,
                 f"Phi_from_A - Phi_expected = {residual}")

    if ns is not None:
        ns.record_derivation(
            derivation_id="interior_A_newtonian_weak_field_match",
            inputs=[A_in, r, R, rho0],
            output=residual,
            method="Phi = c^2/2*(A-1) vs Newtonian_uniform_sphere",
            status=Status.DERIVED,
            record_kind=RecordKind.COMPATIBILITY_EXAMPLE,
            scope="weak-field limit, constant density",
        )


# =============================================================================
# Case 8: Difference from GR interior Schwarzschild
# =============================================================================

def case_8_not_gr_interior_schwarzschild(out: ScriptOutput):
    header("Case 8: Not the full GR interior Schwarzschild solution")

    print("Important caution:")
    print()
    print("  The constant-density interior A(r) found here is the solution of")
    print("  the reduced areal-flux source law.")
    print()
    print("  It matches the weak-field Newtonian interior potential and matches")
    print("  smoothly to the exterior A=1-2GM/(rc²).")
    print()
    print("  But it is not the full GR interior Schwarzschild metric.")
    print()
    print("Reasons:")
    print("  - pressure is not included,")
    print("  - stress-energy is not fully represented,")
    print("  - the GR interior solution has a different exact lapse structure,")
    print("  - the current model enforces kappa=0 / B=1/A even inside.")
    print()

    with out.governance_assessments():
        out.line("interior model is reduced-source toy, not full GR interior",
                 StatusMark.PASS,
                 "pressure and stress not yet included; kappa=0 enforced by construction")

    with out.unresolved_obligations():
        out.line("derive pressure and stress contribution to interior A-source",
                 StatusMark.OBLIGATION,
                 "GR interior Schwarzschild differs at second order; pressure missing")
        out.line("determine whether kappa=0 holds inside matter or only exterior",
                 StatusMark.OBLIGATION,
                 "GR interior has AB!=1 inside matter; kappa=0 may be exterior-only")


# =============================================================================
# Case 9: Summary
# =============================================================================

def case_9_summary():
    header("Case 9: Summary classification")

    print("Results:")
    print()
    print("1. Constant density gives:")
    print("     M_enc(r) = (4π/3) rho0 r³")
    print()
    print("2. Areal flux law gives:")
    print("     A'(r) = 2G M_enc(r)/(c² r²)")
    print()
    print("3. Interior solution:")
    print("     A_in(r) = 1 - 4πG rho0 R²/c² + 4πG rho0 r²/(3c²)")
    print()
    print("4. Exterior solution:")
    print("     A_out(r) = 1 - 2GM/(c²r)")
    print()
    print("5. A and A' match at r=R.")
    print()
    print("6. Areal flux is continuous at r=R.")
    print()
    print("7. The origin is regular.")
    print()
    print("8. The weak-field Newtonian interior potential is recovered.")
    print()
    print("9. This is not the full GR interior Schwarzschild solution.")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("The areal-flux law behaves sensibly for a finite constant-density")
    print("source in the reduced model.")
    print()
    print("It gives a regular interior A(r), smooth matching of A and A' at")
    print("the source boundary, continuous areal flux, and the correct exterior")
    print("Schwarzschild coefficient.")
    print()
    print("In weak field, the interior A(r) corresponds to the standard")
    print("Newtonian potential inside a uniform sphere.")
    print()
    print("However, this is not a full relativistic interior solution.")
    print("The next theoretical gap is pressure/stress and the question of whether")
    print("kappa=0 should hold inside matter or only in source-free exterior.")
    print()
    print("Possible next artifact:")
    print("  candidate_interior_A_source_model.md")


# =============================================================================
# Main
# =============================================================================

def main():
    header("Candidate Interior A Source Model")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_recap(out)
    case_1_constant_density_enclosed_mass(out, ns)
    case_2_interior_A_solution(out, ns)
    case_3_match_to_exterior(out, ns)
    case_4_flux_continuity(out, ns)
    case_5_origin_regularity(out)
    case_6_interior_B_from_kappa_zero(out)
    case_7_compare_newtonian_interior_potential(out, ns)
    case_8_not_gr_interior_schwarzschild(out)
    case_9_summary()
    final_interpretation()

    out.print_summary()

    with ProjectArchive(root=ARCHIVE_ROOT) as archive2:
        ns2 = archive2.script_namespace(SCRIPT_ID)
        ns2.prepare_archive()

        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_interior_pressure_stress_A_source",
            script_id=SCRIPT_ID,
            title="Derive pressure and stress contribution to interior A-source",
            status=ObligationStatus.OPEN,
            description=(
                "The current reduced interior A model does not include pressure or "
                "stress-energy. GR interior Schwarzschild comparison shows missing "
                "second-order structure. Pressure/stress coupling to the A-flux source "
                "or to interior kappa remains underived."
            ),
        ))

        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_interior_kappa_condition",
            script_id=SCRIPT_ID,
            title="Determine whether kappa=0 holds inside matter or only in exterior",
            status=ObligationStatus.OPEN,
            description=(
                "kappa=0 is enforced by construction in the reduced model interior. "
                "GR interior Schwarzschild has AB!=1 inside matter, so kappa=0 may be "
                "an exterior/source-free condition rather than a universal interior law."
            ),
        ))

        ns2.record_claim(ClaimRecord(
            claim_id="interior_A_areal_flux_reduced_toy",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.HEURISTIC,
            statement=(
                "The constant-density interior A(r) derived from the areal-flux law "
                "is a reduced toy model. It matches the weak-field Newtonian potential "
                "and has smooth matching at the source boundary, but is not the full "
                "GR interior Schwarzschild solution."
            ),
            obligation_ids=["derive_interior_pressure_stress_A_source",
                            "derive_interior_kappa_condition"],
        ))

        ns2.write_run_metadata()

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
