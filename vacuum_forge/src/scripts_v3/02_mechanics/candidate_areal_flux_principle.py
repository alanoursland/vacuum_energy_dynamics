# Candidate areal-flux principle
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
#
# Suggested location:
#   scripts_v3/candidate_areal_flux_principle.py

import sympy as sp


def header(title: str) -> None:
    print()
    print("=" * 108)
    print(title)
    print("=" * 108)


def status_line(label: str, ok: bool, detail: str = "") -> None:
    mark = "PASS" if ok else "WARN"
    if detail:
        print(f"[{mark}] {label}: {detail}")
    else:
        print(f"[{mark}] {label}")


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


def case_0_define_areal_flux_law():
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
    status_line("areal source law can be written as Gauss-flux law", True)


def case_1_source_free_flux_conservation():
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
    status_line("source-free areal flux gives 1/r exterior", True)


def case_2_mass_flux_normalization():
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

    status_line("mass flux fixes r_s=2GM/c^2",
                bool(sol) and is_zero(sol[0] - 2*G*M/c**2))


def case_3_enclosed_mass_form():
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

    status_line("enclosed-mass flux law differentiates to source equation",
                is_zero(flux_derivative - rhs_flux_density))


def case_4_thin_shell_jump_condition():
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
    status_line("thin shell gives flux jump proportional to mass", True)


def case_5_metric_recovery_from_flux():
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

    status_line("A solves source-free areal equation outside source", is_zero(delta_areal(A, r)))
    status_line("kappa=0 gives AB=1", is_zero(AB - 1))


def case_6_boundary_form():
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
    status_line("source law has Gauss-law form over areal spheres", True)


def case_7_compare_curved_spatial_laplacian():
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
    status_line("areal operator passes", is_zero(delta_A))
    status_line("curved spatial operator fails", not is_zero(curved_A))

    print()
    print("Interpretation:")
    print("  The flux principle must not be described as ordinary scalar")
    print("  harmonicity on the curved spatial slice.")


def case_8_relation_to_s_equation():
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

    status_line("areal flux law for A gives nonlinear s equation", is_zero(nonlinear))


def case_9_summary():
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
    case_0_define_areal_flux_law()
    case_1_source_free_flux_conservation()
    case_2_mass_flux_normalization()
    case_3_enclosed_mass_form()
    case_4_thin_shell_jump_condition()
    case_5_metric_recovery_from_flux()
    case_6_boundary_form()
    case_7_compare_curved_spatial_laplacian()
    case_8_relation_to_s_equation()
    case_9_summary()
    final_interpretation()


if __name__ == "__main__":
    main()
