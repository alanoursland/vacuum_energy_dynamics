# Candidate vector global rotation mode
#
# Purpose
# -------
# The vector projection-operator study showed that the local Fourier projector
#
#   P_T = I - k k^T/k^2
#
# works for k^2 != 0, but the k=0/global mode requires boundary treatment.
#
# This script studies the global rotation / angular momentum issue.
#
# It asks:
#
#   1. how angular momentum arises from current,
#   2. why a purely local projector misses global/boundary modes,
#   3. how a rotating compact source can set exterior vector boundary data,
#   4. why the far field should be angular-momentum-like,
#   5. why the coefficient is still missing.
#
# This does NOT derive the Lense-Thirring coefficient.
# It keeps the coefficient symbolic.

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


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def case_0_problem_statement():
    header("Case 0: Global rotation mode problem")

    print("The transverse projector uses 1/k^2 and works for local k != 0 modes.")
    print()
    print("But global rotation / total angular momentum is a boundary/global issue.")
    print()
    print("Question:")
    print()
    print("  How should a compact rotating source set exterior vector boundary data?")
    print()
    print("Rules:")
    print()
    print("  keep coefficients symbolic")
    print("  do not insert Lense-Thirring normalization")
    print("  treat global angular momentum as boundary/source data")

    status_line("global rotation mode problem posed", "CONSTRAINED_BY_IDENTITY")


def case_1_angular_momentum_from_current():
    header("Case 1: Angular momentum from current")

    x, y, z, rho, vx, vy, vz = sp.symbols("x y z rho v_x v_y v_z", real=True)

    r = sp.Matrix([x, y, z])
    j = sp.Matrix([rho*vx, rho*vy, rho*vz])
    ell = sp.simplify(r.cross(j))

    print("Current:")
    print(f"j = {j}")
    print()
    print("Angular momentum density:")
    print("ell = r x j =")
    print(ell)
    print()
    print("Global angular momentum:")
    print()
    print("  J = integral r x j d^3x")
    print()
    print("Interpretation:")
    print("  A rotating source supplies global vector boundary data through J.")

    status_line("angular momentum follows from current", "CONSTRAINED_BY_IDENTITY",
                "global integral requires source model")


def case_2_uniform_rotation_current():
    header("Case 2: Uniform rotation current")

    x, y, z, rho, Omega = sp.symbols("x y z rho Omega", real=True)

    v = sp.Matrix([-Omega*y, Omega*x, 0])
    j = rho * v
    div_j = sp.simplify(sp.diff(j[0], x) + sp.diff(j[1], y) + sp.diff(j[2], z))

    print("Rigid rotation about z:")
    print("v = Omega x r =")
    print(v)
    print()
    print("j = rho v =")
    print(j)
    print()
    print(f"div j = {div_j}")
    print()
    print("For constant rho and Omega, the current is divergence-free.")

    status_line("uniform rotational current is transverse in bulk",
                "DERIVED_REDUCED" if is_zero(div_j) else "RISK")


def case_3_boundary_source_view():
    header("Case 3: Boundary source view")

    J, R, Cb = sp.symbols("J R C_b", positive=True, real=True)

    boundary_flux = Cb * J

    print("For a compact rotating source of radius R:")
    print()
    print("  interior current determines total angular momentum J")
    print("  exterior vector solution should be fixed by boundary data at R")
    print()
    print("Symbolic boundary condition:")
    print()
    print("  vector boundary circulation/flux ~ C_b J")
    print()
    print(f"boundary data = {boundary_flux}")
    print()
    print("C_b is not derived.")

    status_line("global rotation treated as boundary data", "CONSTRAINED_BY_IDENTITY",
                "boundary coefficient missing")


def case_4_far_field_shape():
    header("Case 4: Far-field angular-momentum shape")

    r, J, Cw = sp.symbols("r J C_W", positive=True, real=True)

    BW = Cw * J / r**3

    print("Symbolic far-field curl diagnostic:")
    print()
    print("  B_W ~ C_W J/r^3")
    print()
    print(f"B_W = {BW}")
    print()
    print("Interpretation:")
    print("  J is the only available axial vector for a stationary rotating source.")
    print("  1/r^3 is the expected dipole-like curl falloff.")
    print()
    print("But C_W is missing.")

    status_line("far-field angular-momentum shape stated", "CONSTRAINED_BY_IDENTITY",
                "coefficient missing")


def case_5_zero_mode_boundary_warning():
    header("Case 5: k=0 / boundary warning")

    print("The local projector cannot decide global rotation by itself because:")
    print()
    print("  P_T(k) uses 1/k^2")
    print("  k=0 mode is singular")
    print("  total angular momentum depends on boundary/source integrals")
    print()
    print("Therefore:")
    print()
    print("  local transverse projection handles local current modes")
    print("  global angular momentum must be supplied by boundary/source data")
    print()
    print("This is not failure; it is a boundary problem.")

    status_line("zero-mode requires boundary treatment", "RISK",
                "not solved by local projector")


def case_6_no_gr_matching():
    header("Case 6: No GR matching")

    print("Forbidden at this stage:")
    print()
    print("  set C_W or beta_W to reproduce Lense-Thirring")
    print()
    print("Allowed:")
    print()
    print("  keep C_W symbolic")
    print("  derive C_W from vector action + boundary conditions")
    print("  or declare C_W phenomenological")
    print()
    print("Current status:")
    print()
    print("  source object J: constrained by current")
    print("  far-field shape: constrained")
    print("  coefficient: missing")

    status_line("GR matching forbidden", "RISK",
                "coefficient must not be inserted")


def case_7_classification():
    header("Case 7: Classification")

    print("| Item | Status |")
    print("|---|---|")
    print("| angular momentum J = integral r x j d^3x | CONSTRAINED_BY_IDENTITY |")
    print("| uniform rotation current div j = 0 | DERIVED_REDUCED |")
    print("| global rotation as boundary data | CONSTRAINED_BY_IDENTITY |")
    print("| far-field B_W ~ J/r^3 shape | CONSTRAINED_BY_IDENTITY |")
    print("| boundary coefficient C_b | MISSING |")
    print("| far-field coefficient C_W | MISSING |")
    print("| Lense-Thirring normalization | HAND_ASSIGNED if inserted now |")

    status_line("global rotation classification produced", "CONSTRAINED_BY_IDENTITY",
                "shape/source constrained, coefficient missing")


def case_8_next_tests():
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_vector_boundary_value_problem.py")
    print("   Solve symbolic exterior vector equation with boundary data.")
    print()
    print("2. candidate_kappa_source_law_from_trace_exchange.py")
    print("   Work missing kappa source law.")
    print()
    print("3. candidate_tensor_source_from_exchange_identity.py")
    print("   Work hand-assigned tensor coupling.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_vector_boundary_value_problem.py")

    status_line("next test selected", "CONSTRAINED_BY_IDENTITY",
                "boundary value problem is next vector step")


def final_interpretation():
    header("Final interpretation")

    print("The local projection operator handles k != 0 current splitting.")
    print()
    print("Global rotation is different:")
    print()
    print("  J = integral r x j d^3x")
    print()
    print("A compact rotating source should set exterior vector boundary data.")
    print()
    print("The expected symbolic far-field shape is:")
    print()
    print("  B_W ~ C_W J/r^3")
    print()
    print("But C_W is missing.")
    print()
    print("Possible next artifact:")
    print("  candidate_vector_global_rotation_mode.md")
    print()
    print("Possible next script:")
    print("  candidate_vector_boundary_value_problem.py")


def main():
    header("Candidate Vector Global Rotation Mode")
    case_0_problem_statement()
    case_1_angular_momentum_from_current()
    case_2_uniform_rotation_current()
    case_3_boundary_source_view()
    case_4_far_field_shape()
    case_5_zero_mode_boundary_warning()
    case_6_no_gr_matching()
    case_7_classification()
    case_8_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
