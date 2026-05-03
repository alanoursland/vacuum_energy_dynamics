# Candidate vector frame-dragging observable
#
# Purpose
# -------
# The vector-current continuity study found:
#
#   density rho -> scalar A source
#   current j_i = rho v_i -> vector W_i source
#   Delta W_i ~ j_i
#   curl W is a safer diagnostic candidate than raw W_i
#
# This script asks whether curl W can be organized as a frame-dragging /
# precession diagnostic while keeping all coefficients symbolic.
#
# It does NOT insert the GR Lense-Thirring coefficient.
# It does NOT claim the observable is derived.
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/09_vacuum_identity_and_source_coupling/
#   or:
#   scripts_v3/candidate_vector_frame_dragging_observable.py

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
        "HAND_ASSIGNED": "WARN",
        "MISSING": "FAIL",
        "RISK": "WARN",
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


def curl_vec(V, coords):
    x, y, z = coords
    return sp.Matrix([
        sp.diff(V[2], y) - sp.diff(V[1], z),
        sp.diff(V[0], z) - sp.diff(V[2], x),
        sp.diff(V[1], x) - sp.diff(V[0], y),
    ])


def div_vec(V, coords):
    return sp.simplify(sum(sp.diff(V[i], coords[i]) for i in range(3)))


def case_0_problem_statement():
    header("Case 0: Vector frame-dragging observable problem")

    print("Question:")
    print()
    print("  Can curl W be used as a safer frame-dragging diagnostic candidate?")
    print()
    print("Rules:")
    print()
    print("  raw W_i is not automatically observable")
    print("  coefficients remain symbolic")
    print("  do not insert Lense-Thirring normalization by hand")
    print()
    print("Candidate diagnostic:")
    print()
    print("  B_W = curl W")

    status_line("frame-dragging observable problem posed", "CONSTRAINED_BY_IDENTITY")


def case_1_curl_kills_gradient():
    header("Case 1: Curl kills pure-gradient gauge-like piece")

    x, y, z = sp.symbols("x y z", real=True)
    phi = sp.Function("phi")(x, y, z)

    grad_phi = sp.Matrix([sp.diff(phi, x), sp.diff(phi, y), sp.diff(phi, z)])
    curl_grad = sp.simplify(curl_vec(grad_phi, (x, y, z)))

    print("Pure-gradient vector:")
    print("  W = grad phi")
    print()
    print("curl(grad phi) =")
    print(curl_grad)
    print()
    print("Interpretation:")
    print("  If gauge shifts add gradient-like pieces, curl W removes them.")

    ok = all(is_zero(e) for e in curl_grad)
    status_line("curl removes pure-gradient pieces", "DERIVED_REDUCED" if ok else "RISK")


def case_2_rotational_W():
    header("Case 2: Rotational W gives nonzero curl")

    x, y, z, a = sp.symbols("x y z a", real=True)

    W = sp.Matrix([-a*y, a*x, 0])
    BW = sp.simplify(curl_vec(W, (x, y, z)))
    divW = div_vec(W, (x, y, z))

    print("Rotational W:")
    print(W)
    print()
    print("curl W =")
    print(BW)
    print(f"div W = {divW}")
    print()
    print("Interpretation:")
    print("  Rotational vector structure gives a nonzero curl diagnostic.")

    ok = not all(is_zero(e) for e in BW)
    status_line("rotational W produces nonzero B_W", "CONSTRAINED_BY_IDENTITY" if ok else "RISK",
                "normalization remains symbolic")


def case_3_current_loop_angular_momentum():
    header("Case 3: Current loop / angular momentum structure")

    x, y, z, rho, vx, vy, vz = sp.symbols("x y z rho v_x v_y v_z", real=True)

    r = sp.Matrix([x, y, z])
    j = sp.Matrix([rho*vx, rho*vy, rho*vz])
    ell = r.cross(j)

    print("Current:")
    print(f"j = {j}")
    print()
    print("Angular momentum density:")
    print("ell = r x j =")
    print(ell)
    print()
    print("Interpretation:")
    print("  A frame-dragging diagnostic sourced by current should reduce globally")
    print("  to an angular-momentum-like source for rotating bodies.")

    status_line("angular momentum structure follows from current", "CONSTRAINED_BY_IDENTITY",
                "global integral and coefficient missing")


def case_4_symbolic_precession_relation():
    header("Case 4: Symbolic precession relation")

    beta_W = sp.symbols("beta_W", real=True)
    BWx, BWy, BWz = sp.symbols("B_Wx B_Wy B_Wz", real=True)
    BW = sp.Matrix([BWx, BWy, BWz])

    Omega = beta_W * BW

    print("Candidate precession/frame-dragging relation:")
    print()
    print("  Omega_drag = beta_W * B_W")
    print()
    print(f"Omega_drag = {Omega}")
    print()
    print("Status:")
    print("  B_W = curl W is diagnostic candidate")
    print("  beta_W is not derived")
    print("  do not set beta_W from GR yet")

    status_line("precession relation stated symbolically", "CONSTRAINED_BY_IDENTITY",
                "beta_W missing")


def case_5_dipole_shape():
    header("Case 5: Dipole-like far-field shape")

    r, J, Cw = sp.symbols("r J C_W", positive=True, real=True)

    BW_far = Cw * J / r**3

    print("Expected rotational far-field diagnostic shape:")
    print()
    print("  B_W ~ C_W J / r^3")
    print()
    print(f"B_W_far = {BW_far}")
    print()
    print("Interpretation:")
    print("  Continuity/current gives angular momentum J as source.")
    print("  A dipole-like vector field suggests 1/r^3 curl falloff.")
    print("  Coefficient C_W remains symbolic.")

    status_line("dipole-like far-field shape stated", "CONSTRAINED_BY_IDENTITY",
                "coefficient and derivation missing")


def case_6_observable_safety():
    header("Case 6: Observable safety classification")

    print("| Quantity | Status |")
    print("|---|---|")
    print("| raw W_i | RISK / gauge-sensitive |")
    print("| grad piece of W_i | nonphysical candidate |")
    print("| curl W | CONSTRAINED_BY_IDENTITY diagnostic candidate |")
    print("| Omega_drag = beta_W curl W | CONSTRAINED_BY_IDENTITY, beta_W missing |")
    print("| Lense-Thirring coefficient | HAND_ASSIGNED if inserted now |")
    print()
    status_line("observable safety classification produced", "CONSTRAINED_BY_IDENTITY",
                "raw W_i remains unsafe")


def case_7_failure_controls():
    header("Case 7: Failure controls")

    print("This observable reconstruction fails if:")
    print()
    print("1. raw W_i is treated as measured directly.")
    print("2. beta_W is chosen only to match GR.")
    print("3. curl W does not connect to a physical precession observable.")
    print("4. the current source j_i is disconnected from continuity.")
    print("5. vector radiation is accidentally introduced without suppression or evidence.")
    print()
    status_line("frame-dragging failure controls stated", "RISK",
                "next stage must derive beta_W or mark it independent")


def final_interpretation():
    header("Final interpretation")

    print("The safer vector observable candidate is:")
    print()
    print("  B_W = curl W")
    print()
    print("because curl removes pure-gradient gauge-like pieces.")
    print()
    print("A symbolic frame-dragging relation is:")
    print()
    print("  Omega_drag = beta_W B_W")
    print()
    print("But beta_W and the far-field coefficient are missing.")
    print()
    print("Possible next artifact:")
    print("  candidate_vector_frame_dragging_observable.md")
    print()
    print("Possible next script:")
    print("  candidate_vector_coefficient_normalization.py")


def main():
    header("Candidate Vector Frame-Dragging Observable")
    case_0_problem_statement()
    case_1_curl_kills_gradient()
    case_2_rotational_W()
    case_3_current_loop_angular_momentum()
    case_4_symbolic_precession_relation()
    case_5_dipole_shape()
    case_6_observable_safety()
    case_7_failure_controls()
    final_interpretation()


if __name__ == "__main__":
    main()
