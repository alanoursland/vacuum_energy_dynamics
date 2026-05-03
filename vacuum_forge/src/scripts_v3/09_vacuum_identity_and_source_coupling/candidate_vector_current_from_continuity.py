# Candidate vector current from continuity
#
# Purpose
# -------
# The source-coupling audit found:
#
#   density rho -> A_constraint source
#   current j_i = rho v_i -> W_i source candidate
#
# This script asks whether a vector-current sector can be motivated from
# continuity rather than assigned only by analogy to frame dragging.
#
# It does NOT derive full gravitomagnetism.
# It does NOT set the final coefficient to match GR.
#
# It tests the minimal ontology-native structure:
#
#   1. mass continuity links density and current,
#   2. a vector potential W_i should be sourced by current j_i,
#   3. stationary incompressible current gives transverse source,
#   4. curl W gives a gauge-safer frame-dragging diagnostic,
#   5. coefficient remains underived,
#   6. matching Lense-Thirring would be a later test, not an input.
#
# Status categories:
#
#   DERIVED_REDUCED
#   CONSTRAINED_BY_IDENTITY
#   HAND_ASSIGNED
#   MISSING
#   RISK
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/09_vacuum_identity_and_source_coupling/
#   or:
#   scripts_v3/candidate_vector_current_from_continuity.py

import sympy as sp


# =============================================================================
# Utilities
# =============================================================================

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


# =============================================================================
# Case 0: Problem statement
# =============================================================================

def case_0_problem_statement():
    header("Case 0: Vector current from continuity problem")

    print("Question:")
    print()
    print("  Does continuity demand a vector/current sector W_i?")
    print()
    print("Starting point:")
    print()
    print("  partial_t rho + div j = 0")
    print("  j_i = rho v_i")
    print()
    print("Hypothesis:")
    print()
    print("  W_i should be sourced by current j_i, not assigned only by analogy.")

    status_line("vector current problem posed", "CONSTRAINED_BY_IDENTITY")


# =============================================================================
# Case 1: Mass continuity identity
# =============================================================================

def case_1_mass_continuity():
    header("Case 1: Mass continuity links density and current")

    t, x = sp.symbols("t x", real=True)
    rho = sp.Function("rho")(t, x)
    j = sp.Function("j")(t, x)

    continuity = sp.diff(rho, t) + sp.diff(j, x)

    print("1D continuity equation:")
    print()
    print("  partial_t rho + partial_x j = 0")
    print()
    print(f"expression = {continuity}")
    print()
    print("Interpretation:")
    print("  If density sources scalar exchange, current should source vector transport.")

    status_line("current follows from density continuity", "CONSTRAINED_BY_IDENTITY",
                "identity form is standard but parent derivation still needed")


# =============================================================================
# Case 2: Candidate W_i source equation
# =============================================================================

def case_2_candidate_W_source_equation():
    header("Case 2: Candidate W_i source equation")

    x, K_W, alpha_W = sp.symbols("x K_W alpha_W", positive=True, real=True)
    W = sp.Function("W")(x)
    j = sp.Function("j")(x)

    equation = sp.Eq(sp.diff(W, x, 2), -alpha_W*j/K_W)

    print("Minimal reduced vector-current source equation:")
    print()
    print("  Delta W_i = - (alpha_W / K_W) j_i")
    print()
    print(f"1D schematic = {equation}")
    print()
    print("Status:")
    print("  source object j_i is identity-constrained")
    print("  coefficient alpha_W/K_W is not derived")

    status_line("W_i source form proposed from current", "CONSTRAINED_BY_IDENTITY",
                "coefficient and gauge behavior missing")


# =============================================================================
# Case 3: Stationary incompressible current
# =============================================================================

def case_3_stationary_incompressible_current():
    header("Case 3: Stationary incompressible current is transverse")

    x, y, z = sp.symbols("x y z", real=True)
    J0 = sp.symbols("J0", real=True)

    # Example divergence-free current: circular flow around z axis.
    jx = -J0*y
    jy = J0*x
    jz = 0

    div_j = sp.diff(jx, x) + sp.diff(jy, y) + sp.diff(jz, z)

    print("Example stationary circular current:")
    print(f"j = ({jx}, {jy}, {jz})")
    print(f"div j = {div_j}")
    print()
    print("Interpretation:")
    print("  Stationary rotational current naturally belongs to a transverse/vector sector.")

    status_line("stationary circular current is divergence-free", "DERIVED_REDUCED" if is_zero(div_j) else "RISK")


# =============================================================================
# Case 4: Curl W as frame-dragging diagnostic
# =============================================================================

def case_4_curl_W_diagnostic():
    header("Case 4: Curl W as gauge-safer frame-dragging diagnostic")

    x, y, z = sp.symbols("x y z", real=True)
    a = sp.symbols("a", real=True)

    # Simple rotational vector potential W = (-a y, a x, 0)
    Wx = -a*y
    Wy = a*x
    Wz = 0

    curl_x = sp.diff(Wz, y) - sp.diff(Wy, z)
    curl_y = sp.diff(Wx, z) - sp.diff(Wz, x)
    curl_z = sp.diff(Wy, x) - sp.diff(Wx, y)

    print("Example vector potential:")
    print(f"W = ({Wx}, {Wy}, {Wz})")
    print()
    print("curl W =")
    print(f"({curl_x}, {curl_y}, {curl_z})")
    print()
    print("Interpretation:")
    print("  raw W_i may be gauge-sensitive.")
    print("  curl-like diagnostics are better candidates for physical frame dragging.")

    nonzero = not (is_zero(curl_x) and is_zero(curl_y) and is_zero(curl_z))
    status_line("curl W gives frame-dragging diagnostic candidate",
                "CONSTRAINED_BY_IDENTITY" if nonzero else "RISK",
                "observable normalization still missing")


# =============================================================================
# Case 5: Coefficient discipline
# =============================================================================

def case_5_coefficient_discipline():
    header("Case 5: Coefficient discipline")

    print("Do NOT set alpha_W/K_W by hand to match Lense-Thirring yet.")
    print()
    print("Allowed current status:")
    print()
    print("  W_i source object: j_i = rho v_i")
    print("  W_i equation form: Delta W_i ~ j_i")
    print("  W_i coefficient: missing")
    print("  W_i observable: curl W / frame-dragging diagnostic candidate")
    print()
    print("Future success condition:")
    print()
    print("  derive coefficient from same vacuum exchange normalization that produced A_flux")
    print("  or show exactly where a new independent stiffness enters")

    status_line("coefficient matching forbidden at this stage", "RISK",
                "prevents fake derivation")


# =============================================================================
# Case 6: Relation to angular momentum
# =============================================================================

def case_6_angular_momentum_relation():
    header("Case 6: Current relation to angular momentum")

    x, y, z, rho, vx, vy, vz = sp.symbols("x y z rho v_x v_y v_z", real=True)

    r = sp.Matrix([x, y, z])
    j = sp.Matrix([rho*vx, rho*vy, rho*vz])
    L_density = r.cross(j)

    print("Angular momentum density proxy:")
    print()
    print("  l = r x j")
    print()
    print(f"l = {L_density}")
    print()
    print("Interpretation:")
    print("  If W_i couples to current j_i, frame dragging should be tied to angular")
    print("  momentum through r x j.")

    status_line("angular momentum source follows from current", "CONSTRAINED_BY_IDENTITY",
                "global integral and coefficient missing")


# =============================================================================
# Case 7: Classification
# =============================================================================

def case_7_classification():
    header("Case 7: Classification")

    print("| Item | Status |")
    print("|---|---|")
    print("| current source j_i = rho v_i | CONSTRAINED_BY_IDENTITY |")
    print("| W_i source equation Delta W_i ~ j_i | CONSTRAINED_BY_IDENTITY |")
    print("| stationary rotational current | DERIVED_REDUCED |")
    print("| curl W diagnostic | CONSTRAINED_BY_IDENTITY |")
    print("| W_i coefficient | MISSING |")
    print("| full gauge behavior | MISSING |")
    print("| Lense-Thirring normalization | HAND_ASSIGNED if inserted now |")
    print()
    status_line("vector current classification produced", "CONSTRAINED_BY_IDENTITY",
                "source type is constrained, coefficient missing")


# =============================================================================
# Case 8: Failure controls
# =============================================================================

def case_8_failure_controls():
    header("Case 8: Failure controls")

    print("This vector-current reconstruction fails if:")
    print()
    print("1. W_i coefficient is chosen only to match GR.")
    print("2. raw W_i is treated as observable without gauge control.")
    print("3. curl W does not connect to frame-dragging measurement.")
    print("4. vector radiation appears unsuppressed without evidence.")
    print("5. current continuity does not connect to the scalar density source.")
    print()
    status_line("vector-current failure controls stated", "RISK",
                "next scripts must avoid coefficient matching")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("Continuity strongly suggests a vector/current sector:")
    print()
    print("  density rho -> scalar A source")
    print("  current j_i = rho v_i -> vector W_i source")
    print()
    print("A minimal source form is:")
    print()
    print("  Delta W_i ~ j_i")
    print()
    print("A safer observable candidate is:")
    print()
    print("  curl W")
    print()
    print("But the coefficient, gauge behavior, and frame-dragging normalization")
    print("are not derived.")
    print()
    print("Possible next artifact:")
    print("  candidate_vector_current_from_continuity.md")
    print()
    print("Possible next script:")
    print("  candidate_vector_frame_dragging_observable.py")


def main():
    header("Candidate Vector Current From Continuity")
    case_0_problem_statement()
    case_1_mass_continuity()
    case_2_candidate_W_source_equation()
    case_3_stationary_incompressible_current()
    case_4_curl_W_diagnostic()
    case_5_coefficient_discipline()
    case_6_angular_momentum_relation()
    case_7_classification()
    case_8_failure_controls()
    final_interpretation()


if __name__ == "__main__":
    main()
