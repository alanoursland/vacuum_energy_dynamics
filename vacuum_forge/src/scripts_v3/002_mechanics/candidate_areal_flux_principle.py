# Candidate areal-flux principle
#
# Group:
#   02_mechanics
#
# Script type:
#   SAMPLE
#
# Purpose
# -------
# The exact static spherical recovery found that the successful source law is:
#
#   Delta_areal A = 8*pi*G*rho / c**2
#
# where:
#
#   Delta_areal A = (1/r**2) * d/dr(r**2 A')
#
# This is equivalent to a Gauss-law / areal-flux statement:
#
#   d/dr [4*pi*r**2 A'] = 4*pi*r**2 * (8*pi*G*rho/c**2)
#
# or, after integrating:
#
#   4*pi*r**2 A' = 8*pi*G*M_enclosed(r)/c**2
#
# This script studies the exact source law as an areal-flux principle
# rather than as a standard curved-space scalar Laplacian.
#
# IMPORTANT:
# This is still reduced, static, spherical, and areal-radius based.
# It is not a full covariant derivation.

from pathlib import Path

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.core.context import TheoryContext
from vacuumforge.metric.concrete_check import check_concrete_metric
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


def curved_spatial_laplacian(f, B, r):
    return sp.simplify((1/(r**2 * sp.sqrt(B))) * sp.diff((r**2/sp.sqrt(B)) * sp.diff(f, r), r))


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="exact_source_law_geometry_check",
        upstream_script_id="02_mechanics__candidate_exact_source_law_geometry_check",
        upstream_derivation_id="flat_laplacian_harmonic_check_schwarzschild_A",
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


def case_0_define_areal_flux_law(out: ScriptOutput):
    header("Case 0: Define areal-flux law")

    print("Candidate exact reduced source law:")
    print()
    print("  Delta_areal A = 8*pi*G*rho / c^2")
    print()
    print("where:")
    print()
    print("  Delta_areal A = (1/r^2)(r^2 A')'")
    print()
    print("Equivalently:")
    print()
    print("  d/dr(4*pi*r^2 A') = 4*pi*r^2 * 8*pi*G*rho/c^2")
    print()
    print("Define areal flux:")
    print()
    print("  F_A(r) = 4*pi*r^2 A'")
    print()
    print("Then:")
    print()
    print("  F_A'(r) = 32*pi^2*G*r^2*rho/c^2")
    print()

    with out.governance_assessments():
        out.line("areal source law can be written as Gauss-flux law", StatusMark.PASS,
                 "Delta_areal A=8πG*rho/c² equivalently gives d/dr(F_A)=32π²G*r²*rho/c²")


def case_1_source_free_flux_conservation(out: ScriptOutput, ns):
    header("Case 1: Source-free flux conservation")

    r = sp.symbols("r", positive=True, real=True)
    A = sp.Function("A")(r)

    eq = sp.Eq(sp.diff(r**2 * sp.diff(A, r), r), 0)
    sol = sp.dsolve(eq)

    print("Source-free exterior:")
    print("  rho = 0")
    print("  Delta_areal A = 0")
    print("  d/dr(r^2 A') = 0")
    print()
    print(f"Equation: {eq}")
    print(f"General solution: {sol}")
    print()
    print("So:")
    print("  A(r)=C1+C2/r")
    print()

    with out.derived_results():
        out.line("source-free areal flux gives 1/r exterior", StatusMark.PASS,
                 f"solution={sol}")

    ns.record_derivation(
        derivation_id="source_free_areal_flux_ode_solution",
        inputs=[eq],
        output=sol,
        method="dsolve d/dr(r²A')=0 for A(r)",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="ode_solution",
    )


def case_2_mass_flux_normalization(out: ScriptOutput, ns):
    header("Case 2: Mass flux normalization")

    r, r_s, G, M, c = sp.symbols("r r_s G M c", positive=True, real=True)

    A = 1 - r_s/r
    F = areal_flux(A, r)
    target = 8 * sp.pi * G * M / c**2
    sol = sp.solve(sp.Eq(F, target), r_s)

    print(f"A = {A}")
    print(f"A' = {sp.diff(A, r)}")
    print(f"F_A = 4*pi*r^2*A' = {F}")
    print(f"target flux = {target}")
    print(f"r_s solution = {sol}")

    passes = bool(sol) and is_zero(sol[0] - 2*G*M/c**2)

    with out.sample_results():
        out.line("mass flux fixes r_s=2GM/c^2",
                 StatusMark.PASS if passes else StatusMark.FAIL,
                 f"solution={sol}")

    if passes:
        ns.record_derivation(
            derivation_id="areal_flux_mass_normalization",
            inputs=[F, target],
            output=sp.Eq(r_s, 2 * G * M / c**2),
            method="solve 4πr²A'=8πGM/c² for r_s with A=1-r_s/r",
            status=Status.DERIVED,
            record_kind=RecordKind.SAMPLE_DERIVATION,
            scope="areal-gauge static spherical toy; mass normalization assumption",
        )


def case_3_enclosed_mass_form(out: ScriptOutput):
    header("Case 3: Enclosed mass form")

    r, G, c = sp.symbols("r G c", positive=True, real=True)
    rho = sp.Function("rho")(r)
    Menc = sp.Function("M_enc")(r)

    flux = 8*sp.pi*G*Menc/c**2
    flux_derivative = sp.diff(flux, r).subs(sp.diff(Menc, r), 4*sp.pi*r**2*rho)
    rhs_flux_density = 4*sp.pi*r**2 * (8*sp.pi*G*rho/c**2)

    print("Define enclosed mass:")
    print()
    print("  M_enc'(r) = 4*pi*r^2*rho(r)")
    print()
    print("Candidate flux law:")
    print()
    print("  F_A(r) = 8*pi*G*M_enc(r)/c^2")
    print()
    print(f"F_A'(r) = {flux_derivative}")
    print(f"4*pi*r^2 * 8*pi*G*rho/c^2 = {rhs_flux_density}")

    residual = sp.simplify(flux_derivative - rhs_flux_density)

    with out.derived_results():
        out.line("enclosed-mass flux law differentiates to source equation",
                 StatusMark.PASS if is_zero(residual) else StatusMark.FAIL,
                 f"residual={residual}")


def case_4_thin_shell_jump_condition(out: ScriptOutput):
    header("Case 4: Thin shell jump condition")

    G, M_shell, c = sp.symbols("G M_shell c", positive=True, real=True)
    F_inside, F_outside = sp.symbols("F_inside F_outside", real=True)

    jump = 8*sp.pi*G*M_shell/c**2
    equation = sp.Eq(F_outside - F_inside, jump)

    print("For a thin shell source with mass M_shell:")
    print()
    print("  F_A(outside) - F_A(inside) = 8*pi*G*M_shell/c^2")
    print()
    print(f"Jump equation: {equation}")
    print()
    print("If inside flux is zero:")
    print()
    print(f"  F_A(outside) = {jump}")
    print()

    with out.governance_assessments():
        out.line("thin shell gives flux jump proportional to mass", StatusMark.PASS,
                 f"jump=8πGM_shell/c²; F_outside-F_inside={jump}")


def case_5_metric_recovery_from_flux(out: ScriptOutput, ns):
    header("Case 5: Exterior metric recovery from flux principle")

    r, G, M, c = sp.symbols("r G M c", positive=True, real=True)

    r_s = 2*G*M/c**2
    A = 1 - r_s/r
    kappa = sp.Integer(0)
    B = sp.simplify(1 / A)
    AB = sp.simplify(A*B)

    print(f"r_s = {r_s}")
    print(f"A = {A}")
    print(f"kappa = {kappa}")
    print(f"B = {B}")
    print(f"AB = {AB}")
    print()
    print(f"Delta_areal A = {delta_areal(A, r)}")
    print(f"F_A = {areal_flux(A, r)}")

    delta_A = delta_areal(A, r)
    residual_AB = sp.simplify(AB - 1)

    with out.sample_results():
        out.line("A solves source-free areal equation outside source",
                 StatusMark.PASS if is_zero(delta_A) else StatusMark.FAIL,
                 f"Delta_areal_A={delta_A}")
        out.line("kappa=0 gives AB=1",
                 StatusMark.PASS if is_zero(residual_AB) else StatusMark.FAIL,
                 f"residual={residual_AB}")

    ctx = TheoryContext("candidate_areal_flux_principle")
    ctx.define_equal_response_algebraic_symbols()
    ms = ctx._mode_symbols
    A_value = 1 - 2 * ms.G * ms.M / (ms.r * ms.c**2)
    B_value = sp.simplify(1 / A_value)
    concrete = check_concrete_metric(ctx, A_value=A_value, B_value=B_value, requirement_ids=["reciprocal_scaling"])
    if concrete:
        with out.governance_assessments():
            out.line(
                "VacuumForge classifies flux-recovered metric as by-construction reciprocal",
                StatusMark.PASS if concrete[0].status == "satisfied_by_construction" else StatusMark.DEFER,
                concrete[0].message,
            )
        ns.record_derivation(
            derivation_id="areal_flux_exact_metric_check",
            inputs=[A_value],
            output=sp.Symbol(concrete[0].status),
            method="concrete_metric_check: reciprocal_scaling requirement on flux-recovered A",
            status=Status.DERIVED,
            record_kind=RecordKind.COMPATIBILITY_EXAMPLE,
            result_type="compatibility_check",
            metadata={"message": concrete[0].message},
        )


def case_6_boundary_form(out: ScriptOutput):
    header("Case 6: Boundary / Gauss-law form")

    print("Integrated source law over shell r1 < r < r2:")
    print()
    print("  integral Delta_areal A dV = surface flux difference")
    print()
    print("Reduced spherical form:")
    print()
    print("  F_A(r2) - F_A(r1) = 8*pi*G*M_between / c^2")
    print()
    print("where:")
    print()
    print("  F_A(r) = 4*pi*r^2*A'")
    print()
    print("This is the cleanest current interpretation:")
    print()
    print("  mass controls the jump / value of areal A-flux.")
    print()

    with out.governance_assessments():
        out.line("source law has Gauss-law form over areal spheres", StatusMark.PASS,
                 "F_A(r2)-F_A(r1)=8πG*M_between/c²; mass controls areal flux jump")


def case_7_compare_curved_spatial_laplacian(out: ScriptOutput, ns):
    header("Case 7: Comparison to curved spatial Laplacian")

    r, r_s = sp.symbols("r r_s", positive=True, real=True)

    A = 1 - r_s/r
    B = 1/A

    delta_A = delta_areal(A, r)
    curved_A = curved_spatial_laplacian(A, B, r)

    print(f"A = {A}")
    print(f"B = {B}")
    print()
    print(f"Delta_areal A = {delta_A}")
    print(f"Delta_spatial A = {curved_A}")
    print()

    with out.derived_results():
        out.line("areal operator passes",
                 StatusMark.PASS if is_zero(delta_A) else StatusMark.FAIL,
                 f"residual={delta_A}")
        out.line("curved spatial operator fails",
                 StatusMark.PASS if not is_zero(curved_A) else StatusMark.FAIL,
                 f"curved_A={curved_A}")

    print()
    print("Interpretation:")
    print("  The flux principle must not be described as ordinary scalar")
    print("  harmonicity on the curved spatial slice.")

    ns.record_derivation(
        derivation_id="areal_vs_curved_laplacian_comparison",
        inputs=[A, B, r],
        output=sp.Tuple(delta_A, curved_A),
        method="compare Delta_areal and curved_spatial_laplacian for A=1-r_s/r, B=1/A",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="operator_comparison",
    )


def case_8_relation_to_s_equation(out: ScriptOutput):
    header("Case 8: Relation to nonlinear s equation")

    r, r_s = sp.symbols("r r_s", positive=True, real=True)

    A = 1 - r_s/r
    s = sp.log(A)

    nonlinear = sp.simplify(delta_areal(s, r) + sp.diff(s, r)**2)

    print(f"A = {A}")
    print(f"s = ln(A) = {s}")
    print()
    print("Since A=e^s:")
    print("  Delta_areal A = e^s(Delta_areal s + |grad s|^2)")
    print()
    print(f"Delta_areal s + |grad s|^2 = {nonlinear}")

    with out.derived_results():
        out.line("areal flux law for A gives nonlinear s equation",
                 StatusMark.PASS if is_zero(nonlinear) else StatusMark.FAIL,
                 f"residual={nonlinear}")


def case_9_summary(out: ScriptOutput):
    header("Case 9: Summary classification")

    print("Results:")
    print()
    print("1. The exact source law can be stated as areal flux:")
    print("     F_A = 4*pi*r^2*A'")
    print()
    print("2. Source-free exterior gives:")
    print("     F_A = constant")
    print()
    print("3. This implies:")
    print("     A = C0 + C1/r")
    print()
    print("4. Asymptotic flatness gives:")
    print("     C0 = 1")
    print()
    print("5. Mass flux gives:")
    print("     C1 = -2GM/c^2")
    print()
    print("6. Therefore:")
    print("     A = 1 - 2GM/(r*c^2)")
    print()
    print("7. With kappa=0:")
    print("     B = 1/A")
    print()
    print("8. This recovers exact Schwarzschild exterior metric factors.")
    print()
    print("9. The operator is areal-flux / flat-radial, not curved-spatial.")
    print()
    print("Open problem:")
    print("  derive the areal-flux principle from deeper geometry or ontology.")

    with out.unresolved_obligations():
        out.line("derive areal-flux principle from covariant geometry", StatusMark.OBLIGATION,
                 "open problem: explain why mass sources areal flux of A=e^s; not yet derived")


def final_interpretation():
    header("Final interpretation")

    print("This script reframes the exact source law as a Gauss-law-like")
    print("areal-flux principle:")
    print()
    print("  F_A(r) = 4*pi*r^2 A'")
    print()
    print("with:")
    print()
    print("  F_A = 8*pi*G*M_enc(r)/c^2")
    print()
    print("Outside the source, M_enc is constant, so F_A is constant and:")
    print()
    print("  A = 1 - 2GM/(r*c^2)")
    print()
    print("Combined with kappa=0:")
    print()
    print("  B = 1/A")
    print()
    print("This recovers the exact Schwarzschild exterior metric factors.")
    print()
    print("The result does not yet derive the law from covariant geometry.")
    print("It sharpens the target:")
    print()
    print("  explain why mass sources areal flux of A=e^s.")
    print()
    print("Possible next artifact:")
    print("  candidate_areal_flux_principle.md")


def main():
    header("Candidate Areal-Flux Principle")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_define_areal_flux_law(out)
    case_1_source_free_flux_conservation(out, ns)
    case_2_mass_flux_normalization(out, ns)
    case_3_enclosed_mass_form(out)
    case_4_thin_shell_jump_condition(out)
    case_5_metric_recovery_from_flux(out, ns)
    case_6_boundary_form(out)
    case_7_compare_curved_spatial_laplacian(out, ns)
    case_8_relation_to_s_equation(out)
    case_9_summary(out)
    final_interpretation()

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_areal_flux_principle_from_covariant_geometry",
        script_id=SCRIPT_ID,
        title="Derive areal-flux principle for A=e^s from covariant geometry or ontology",
        status=ObligationStatus.OPEN,
        description=(
            "The areal-flux law F_A=4πr²A'=8πGM_enc/c² is established as a successful "
            "reduced static spherical toy. The covariant geometric or ontological principle "
            "explaining why mass sources areal flux of A=e^s is not yet derived."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="areal_flux_principle_is_reduced_toy",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "The areal-flux principle F_A(r)=8πGM_enc(r)/c² is a reduced, static, spherical, "
            "areal-radius-based toy. It is not a full covariant derivation."
        ),
    ))

    ns.record_route(RouteRecord(
        route_id="areal_flux_principle_candidate_route",
        script_id=SCRIPT_ID,
        name="Areal-flux principle as Gauss-law source law for A=e^s",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        description=(
            "The areal-flux reframing F_A=8πGM_enc/c² successfully recovers exact "
            "Schwarzschild exterior under kappa=0 and is distinct from curved spatial "
            "harmonicity. Requires covariant geometric derivation."
        ),
        required_obligations=[
            "derive_areal_flux_principle_from_covariant_geometry",
        ],
    ))

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
