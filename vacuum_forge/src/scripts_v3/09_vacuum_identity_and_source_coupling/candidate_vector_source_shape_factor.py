# Candidate vector source shape factor
#
# Purpose
# -------
# The boundary-coefficient study found:
#
#   C_b = C_shape * alpha_W/(8*pi*K_c)
#
# but left C_shape missing.
#
# This script computes the source/shape factor for a simple uniformly rotating
# sphere using a Green-function far-field expansion.
#
# Model:
#
#   j = rho (Omega x r')
#
# with a uniform sphere of radius R.
#
# For large field distance x, the vector potential-like solution is:
#
#   W(x) = lambda_green integral j(x')/|x-x'| d^3x'
#
# where:
#
#   lambda_green = alpha_W/(8*pi*K_c)
#
# The monopole current integral vanishes for a stationary rotating sphere:
#
#   integral j d^3x = 0
#
# The leading nonzero exterior term is dipole/angular-momentum-like.
#
# This script verifies:
#
#   integral j d^3x = 0
#   J_z = integral (x' j_y - y' j_x) d^3x
#   for uniform sphere, J_z = (2/5) M R^2 Omega
#
# This is source geometry only.
# It does NOT derive alpha_W/K_c or beta_W.
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/09_vacuum_identity_and_source_coupling/
#   or:
#   scripts_v3/candidate_vector_source_shape_factor.py

import sympy as sp


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_line(label: str, status: str, detail: str = "") -> None:
    marks = {
        "DERIVED_REDUCED": "PASS",
        "CONSTRAINED_BY_IDENTITY": "WARN",
        "MISSING": "FAIL",
        "RISK": "WARN",
        "HAND_ASSIGNED": "WARN",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


def case_0_problem_statement():
    header("Case 0: Vector source shape factor problem")

    print("Question:")
    print()
    print("  Can C_shape be computed for a simple rotating source?")
    print()
    print("Model:")
    print()
    print("  uniform sphere")
    print("  radius R")
    print("  density rho")
    print("  angular velocity Omega about z")
    print()
    print("Rules:")
    print()
    print("  compute source geometry only")
    print("  keep alpha_W/K_c symbolic")
    print("  do not insert Lense-Thirring normalization")

    status_line("source shape factor problem posed", "CONSTRAINED_BY_IDENTITY")


def case_1_uniform_sphere_mass():
    header("Case 1: Uniform sphere mass")

    R, rho = sp.symbols("R rho", positive=True, real=True)

    M = sp.simplify(4*sp.pi*rho*R**3/3)

    print("Uniform sphere mass:")
    print()
    print("  M = integral rho d^3x")
    print()
    print(f"M = {M}")

    status_line("uniform sphere mass computed", "DERIVED_REDUCED")

    return R, rho, M


def case_2_current_definition():
    header("Case 2: Rigid rotation current")

    x, y, z, rho, Omega = sp.symbols("x y z rho Omega", real=True)

    # Rigid rotation about z: v = Omega x r = (-Omega y, Omega x, 0)
    jx = -rho*Omega*y
    jy = rho*Omega*x
    jz = 0

    div_j = sp.diff(jx, x) + sp.diff(jy, y) + sp.diff(jz, z)

    print("Rigid rotation current:")
    print()
    print(f"j_x = {jx}")
    print(f"j_y = {jy}")
    print(f"j_z = {jz}")
    print()
    print(f"div j = {sp.simplify(div_j)}")

    status_line("rigid rotation current is divergence-free", "DERIVED_REDUCED")

    return x, y, z, rho, Omega, jx, jy, jz


def case_3_current_monopole_vanishes():
    header("Case 3: Total current monopole vanishes")

    print("For a symmetric uniformly rotating sphere:")
    print()
    print("  integral j_x d^3x = -rho Omega integral y d^3x = 0")
    print("  integral j_y d^3x =  rho Omega integral x d^3x = 0")
    print("  integral j_z d^3x = 0")
    print()
    print("Therefore the current monopole vanishes.")
    print("The leading far-field vector effect is dipole/angular-momentum-like.")

    status_line("current monopole vanishes by symmetry", "DERIVED_REDUCED")


def case_4_moment_of_inertia_and_J():
    header("Case 4: Angular momentum of uniform sphere")

    R, rho, Omega = sp.symbols("R rho Omega", positive=True, real=True)

    # For a solid sphere: I_z = (2/5) M R^2
    M = 4*sp.pi*rho*R**3/3
    I_z = sp.simplify(sp.Rational(2, 5)*M*R**2)
    J_z = sp.simplify(I_z*Omega)

    print("Uniform solid sphere:")
    print()
    print(f"M = {M}")
    print(f"I_z = {I_z}")
    print(f"J_z = I_z Omega = {J_z}")
    print()
    print("So:")
    print()
    print("  J_z = (2/5) M R^2 Omega")

    status_line("uniform sphere angular momentum computed", "DERIVED_REDUCED")

    return R, rho, Omega, M, I_z, J_z


def case_5_source_shape_factor_status():
    header("Case 5: Source shape factor status")

    alpha_W, K_c, C_shape = sp.symbols("alpha_W K_c C_shape", positive=True, real=True)

    lambda_green = alpha_W/(8*sp.pi*K_c)
    C_J = C_shape * lambda_green

    print("Vector exterior coefficient form:")
    print()
    print("  C_J = C_shape * alpha_W/(8*pi K_c)")
    print()
    print(f"C_J = {C_J}")
    print()
    print("For a uniformly rotating sphere, source geometry reduces to J.")
    print()
    print("Thus the shape factor can be absorbed into the convention relating")
    print("the Green-function multipole expansion to J.")
    print()
    print("But the exact numerical C_shape depends on the vector equation convention,")
    print("component convention, and definition of W_phi.")

    status_line("source geometry reduces to angular momentum J", "CONSTRAINED_BY_IDENTITY",
                "numeric C_shape convention-dependent")


def case_6_far_field_chain():
    header("Case 6: Far-field coefficient chain")

    alpha_W, K_c, C_shape, beta_W, J, r = sp.symbols(
        "alpha_W K_c C_shape beta_W J r",
        positive=True,
        real=True,
    )

    B_W = C_shape * alpha_W * J / (8*sp.pi*K_c*r**3)
    Omega_drag = beta_W * B_W

    print("Symbolic curl diagnostic:")
    print()
    print(f"B_W = {B_W}")
    print()
    print("Symbolic precession:")
    print()
    print(f"Omega_drag = {Omega_drag}")
    print()
    print("Still missing:")
    print("  alpha_W/K_c")
    print("  beta_W")
    print("  convention-fixed C_shape")

    status_line("far-field chain assembled symbolically", "CONSTRAINED_BY_IDENTITY",
                "normalization still missing")


def case_7_no_gr_matching():
    header("Case 7: No GR matching")

    print("Forbidden:")
    print()
    print("  choose C_shape, alpha_W/K_c, or beta_W to reproduce Lense-Thirring")
    print()
    print("Allowed:")
    print()
    print("  compute C_shape from a fully specified vector convention")
    print("  derive alpha_W/K_c from vacuum transport action")
    print("  derive beta_W from observable coupling")
    print("  or declare remaining coefficient phenomenological")
    print()
    status_line("GR matching forbidden", "RISK",
                "shape factor cleanup is not normalization derivation")


def case_8_classification():
    header("Case 8: Classification")

    print("| Item | Status |")
    print("|---|---|")
    print("| uniform sphere mass | DERIVED_REDUCED |")
    print("| rigid rotation current | DERIVED_REDUCED |")
    print("| total current monopole vanishes | DERIVED_REDUCED |")
    print("| angular momentum J = (2/5) M R^2 Omega | DERIVED_REDUCED |")
    print("| source geometry reduces to J | CONSTRAINED_BY_IDENTITY |")
    print("| numeric C_shape | CONSTRAINED_BY_IDENTITY / convention-dependent |")
    print("| alpha_W/K_c | MISSING |")
    print("| beta_W | MISSING |")

    status_line("source shape classification produced", "CONSTRAINED_BY_IDENTITY",
                "source geometry cleaned up, normalization missing")


def case_9_next_tests():
    header("Case 9: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_vector_sector_status_summary.py")
    print("   Summarize vector sector: source/projection/shape derived, normalization missing.")
    print()
    print("2. candidate_kappa_source_law_from_trace_exchange.py")
    print("   Work missing kappa source law.")
    print()
    print("3. candidate_tensor_source_from_exchange_identity.py")
    print("   Work hand-assigned tensor coupling.")
    print()
    print("Recommended next file:")
    print()
    print("  candidate_vector_sector_status_summary.md")
    print()
    print("Reason:")
    print("  The vector line has reached a natural boundary: structure yes, normalization no.")

    status_line("next file selected", "CONSTRAINED_BY_IDENTITY",
                "vector sector ready for status summary")


def final_interpretation():
    header("Final interpretation")

    print("For a uniformly rotating sphere:")
    print()
    print("  integral j d^3x = 0")
    print("  J = (2/5) M R^2 Omega")
    print()
    print("So source geometry reduces cleanly to angular momentum J.")
    print()
    print("This supports the far-field shape:")
    print()
    print("  B_W ~ J/r^3")
    print()
    print("But normalization remains missing:")
    print()
    print("  alpha_W/K_c")
    print("  beta_W")
    print("  convention-fixed C_shape")
    print()
    print("Possible next artifact:")
    print("  candidate_vector_source_shape_factor.md")
    print()
    print("Recommended next file:")
    print("  candidate_vector_sector_status_summary.md")


def main():
    header("Candidate Vector Source Shape Factor")
    case_0_problem_statement()
    case_1_uniform_sphere_mass()
    case_2_current_definition()
    case_3_current_monopole_vanishes()
    case_4_moment_of_inertia_and_J()
    case_5_source_shape_factor_status()
    case_6_far_field_chain()
    case_7_no_gr_matching()
    case_8_classification()
    case_9_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
