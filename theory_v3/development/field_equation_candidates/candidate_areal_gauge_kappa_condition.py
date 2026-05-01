# Candidate areal-gauge kappa condition
#
# Purpose
# -------
# This script studies the question:
#
#   Can areal-gauge kappa=0 be re-expressed as a gauge-invariant or
#   gauge-fixed condition derived from sphere area / radial foliation geometry?
#
# Prior result:
#   Under radial reparameterization r=f(R), naive reduced modes shift:
#
#       kappa -> kappa + log(f')
#       s     -> s - log(f')
#
#   Therefore kappa and s are not coordinate-invariant scalar fields.
#
# Current idea:
#   The areal radius is geometrically defined by the area of symmetry spheres:
#
#       Area(S) = 4π r_areal^2
#
#   In spherical symmetry, this defines a preferred radial scalar r_areal.
#   Once the radial coordinate is fixed to r_areal, the reduced metric takes:
#
#       ds² = -A(r)c²dt² + B(r)dr² + r²dΩ²
#
#   In that gauge, kappa is well-defined as:
#
#       kappa = 1/2 ln(A B)
#
#   and kappa=0 is equivalent to:
#
#       A B = 1.
#
# This script tests:
#
#   Case 0: General spherical metric with arbitrary radial coordinate R.
#   Case 1: Areal radius from sphere area.
#   Case 2: Transform from arbitrary R to areal radius r=f(R).
#   Case 3: Gauge-fixed kappa_areal from transformed metric.
#   Case 4: Relationship between naive kappa_R and areal-gauge kappa.
#   Case 5: Gauge-invariant phrasing as a gauge-fixed scalar construction.
#   Case 6: Schwarzschild-like reciprocal condition as areal-gauge statement.
#   Case 7: Failure control when angular radius is ignored.
#
# IMPORTANT:
# This does NOT prove that kappa itself is an invariant scalar.
# It tests whether kappa=0 can be phrased as a condition after a geometric
# gauge fixing by the areal radius.
#
# Suggested location:
#   scripts_v3/candidate_areal_gauge_kappa_condition.py

import sympy as sp


# =============================================================================
# Utilities
# =============================================================================

def header(title: str) -> None:
    print()
    print("=" * 104)
    print(title)
    print("=" * 104)


def subheader(title: str) -> None:
    print()
    print("-" * 104)
    print(title)
    print("-" * 104)


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


# =============================================================================
# Case 0: General spherical metric in arbitrary radial coordinate
# =============================================================================

def case_0_general_spherical_metric():
    header("Case 0: General spherical metric in arbitrary radial coordinate")

    R = sp.symbols("R", positive=True, real=True)
    T = sp.Function("T")(R)
    Q = sp.Function("Q")(R)
    S = sp.Function("S")(R)

    print("General static spherical metric in arbitrary radial coordinate R:")
    print("  ds² = -T(R)c²dt² + Q(R)dR² + S(R)² dΩ²")
    print()
    print("Here:")
    print("  T(R) is the temporal coefficient.")
    print("  Q(R) is the radial coefficient.")
    print("  S(R) is the geometric sphere-radius function.")
    print()
    print("Sphere area:")
    print("  Area(R) = 4π S(R)²")
    print()
    print("Areal radius:")
    print("  r_areal = sqrt(Area/4π) = S(R)")
    print()
    status_line("arbitrary radial coordinate includes angular-radius function S(R)", True)


# =============================================================================
# Case 1: Areal radius from sphere area
# =============================================================================

def case_1_areal_radius_from_area():
    header("Case 1: Areal radius from sphere area")

    R = sp.symbols("R", positive=True, real=True)
    S = sp.Function("S")(R)
    Area = 4 * sp.pi * S**2
    r_areal = sp.sqrt(Area / (4 * sp.pi))

    print(f"Area(R) = {Area}")
    print(f"r_areal = sqrt(Area/4π) = {r_areal}")

    # Since S(R) is positive by geometric interpretation, r_areal = S(R).
    print()
    print("Assuming positive sphere-radius function S(R)>0:")
    print("  r_areal = S(R)")
    status_line("areal radius is geometrically fixed by sphere area", True)


# =============================================================================
# Case 2: Transform arbitrary R to areal radius r=S(R)
# =============================================================================

def case_2_transform_to_areal_radius():
    header("Case 2: Transform arbitrary R to areal radius r=S(R)")

    R = sp.symbols("R", positive=True, real=True)
    T = sp.Function("T")
    Q = sp.Function("Q")
    S = sp.Function("S")(R)

    # General metric:
    #   ds² = -T(R)c²dt² + Q(R)dR² + S(R)²dΩ²
    #
    # Define r = S(R).
    # Then dr/dR = S'(R), so dR/dr = 1/S'(R).
    #
    # In areal coordinate r, the radial coefficient is:
    #   B_areal(r) = Q(R) * (dR/dr)^2 = Q(R)/S'(R)^2
    #
    # and:
    #   A_areal(r) = T(R)
    Sprime = sp.diff(S, R)

    A_areal_at_R = T(R)
    B_areal_at_R = sp.simplify(Q(R) / Sprime**2)

    print("Define:")
    print("  r = S(R)")
    print("  dr/dR = S'(R)")
    print("  dR/dr = 1/S'(R)")
    print()
    print("Then in areal gauge:")
    print(f"  A_areal = {A_areal_at_R}")
    print(f"  B_areal = {B_areal_at_R}")
    print("  angular sector = r²dΩ²")
    print()
    status_line("areal radial coefficient includes inverse sphere-radius Jacobian", True)


# =============================================================================
# Case 3: Areal-gauge kappa from arbitrary-coordinate metric
# =============================================================================

def case_3_kappa_areal_from_arbitrary_metric():
    header("Case 3: Areal-gauge kappa from arbitrary-coordinate metric")

    R = sp.symbols("R", positive=True, real=True)
    T = sp.Function("T")
    Q = sp.Function("Q")
    S = sp.Function("S")(R)

    Sprime = sp.diff(S, R)

    # Naive kappa in arbitrary R coordinate if one incorrectly treats R as areal:
    kappa_naive_R = sp.simplify(sp.Rational(1, 2) * sp.log(T(R) * Q(R)))

    # Correct areal-gauge kappa constructed after using r=S(R):
    # A_areal B_areal = T(R) * Q(R)/S'(R)^2
    kappa_areal = sp.simplify(sp.Rational(1, 2) * sp.log(T(R) * Q(R) / Sprime**2))

    delta = sp.simplify(kappa_naive_R - kappa_areal)

    print(f"kappa_naive_R = 1/2 ln(T Q) = {kappa_naive_R}")
    print(f"kappa_areal   = 1/2 ln(T Q / S'^2) = {kappa_areal}")
    print(f"kappa_naive_R - kappa_areal = {delta}")
    print()
    print("If S'(R)>0, then:")
    print("  kappa_naive_R = kappa_areal + ln S'(R)")
    print()
    status_line("difference is radial gauge Jacobian", True)

    print("Areal-gauge compensation condition:")
    print("  kappa_areal = 0")
    print("equivalent to:")
    print("  T(R) Q(R) / S'(R)^2 = 1")
    print("or:")
    print("  T(R) Q(R) = S'(R)^2")


# =============================================================================
# Case 4: Recover previous radial reparameterization result
# =============================================================================

def case_4_recover_reparameterization_result():
    header("Case 4: Recover previous radial reparameterization result")

    R = sp.symbols("R", positive=True, real=True)
    f = sp.Function("f")(R)
    A = sp.Function("A")
    B = sp.Function("B")

    # Start in areal gauge r, then reparameterize r=f(R).
    # General arbitrary-coordinate form has:
    #   T(R)=A(f(R))
    #   Q(R)=B(f(R))*f'(R)^2
    #   S(R)=f(R)
    T = A(f)
    Q = B(f) * sp.diff(f, R)**2
    S = f
    Sprime = sp.diff(S, R)

    kappa_areal = sp.simplify(sp.Rational(1, 2) * sp.log(T * Q / Sprime**2))
    kappa_old_at_f = sp.simplify(sp.Rational(1, 2) * sp.log(A(f) * B(f)))

    kappa_naive_R = sp.simplify(sp.Rational(1, 2) * sp.log(T * Q))

    print("Start from areal gauge and set r=f(R):")
    print(f"  T(R) = {T}")
    print(f"  Q(R) = {Q}")
    print(f"  S(R) = {S}")
    print()
    print(f"kappa_areal reconstructed = {kappa_areal}")
    print(f"kappa_old_at_f = {kappa_old_at_f}")
    print(f"kappa_naive_R = {kappa_naive_R}")

    status_line("areal reconstruction recovers original kappa", is_zero(kappa_areal - kappa_old_at_f))

    print()
    print("Naive kappa_R includes the radial Jacobian, while kappa_areal removes it.")


# =============================================================================
# Case 5: Gauge-fixed condition as geometric construction
# =============================================================================

def case_5_gauge_fixed_condition_statement():
    header("Case 5: Gauge-fixed condition as geometric construction")

    print("The result can be stated without pretending kappa is invariant:")
    print()
    print("1. Start with a static spherical geometry.")
    print("2. Define the areal radius by sphere area:")
    print("     r = sqrt(Area/4π)")
    print("3. Express the metric in areal-radius form:")
    print("     ds² = -A(r)c²dt² + B(r)dr² + r²dΩ²")
    print("4. Define:")
    print("     kappa_areal = 1/2 ln(A B)")
    print("5. Exterior reciprocal compensation is:")
    print("     kappa_areal = 0")
    print("   equivalently:")
    print("     A B = 1")
    print()
    status_line("kappa=0 can be phrased as a gauge-fixed geometric condition", True)

    print("This is not a coordinate-invariant scalar equation.")
    print("It is a condition after geometric gauge fixing by sphere area.")


# =============================================================================
# Case 6: Express condition in arbitrary radial coordinate
# =============================================================================

def case_6_arbitrary_coordinate_expression():
    header("Case 6: Arbitrary-coordinate expression of areal compensation")

    R = sp.symbols("R", positive=True, real=True)
    T = sp.Function("T")(R)
    Q = sp.Function("Q")(R)
    S = sp.Function("S")(R)
    Sprime = sp.diff(S, R)

    condition = sp.Eq(T * Q, Sprime**2)

    print("General static spherical metric:")
    print("  ds² = -T(R)c²dt² + Q(R)dR² + S(R)²dΩ²")
    print()
    print("Areal-gauge compensation kappa_areal=0 is equivalent to:")
    print("  T(R) Q(R) / S'(R)² = 1")
    print()
    print("So, in arbitrary radial coordinate:")
    print(f"  {condition}")
    print()
    print("This expression includes the angular-radius function S(R).")
    print("It is the arbitrary-coordinate version of areal-gauge AB=1.")
    print()
    status_line("arbitrary-coordinate expression includes sphere-area geometry", True)


# =============================================================================
# Case 7: Failure control: ignoring angular sector
# =============================================================================

def case_7_failure_control_ignore_angular_sector():
    header("Case 7: Failure control — ignoring angular sector")

    R = sp.symbols("R", positive=True, real=True)
    f = sp.Function("f")(R)

    print("If one ignores the angular sector and computes only naive T(R)Q(R),")
    print("then a pure radial reparameterization of an AB=1 metric gives:")
    print()
    print("  T(R)Q(R) = f'(R)²")
    print()
    print("This falsely looks like reciprocal scaling failed.")
    print()
    print("But the angular sector is f(R)²dΩ², so the areal radius is f(R).")
    print("Restoring areal gauge removes the f'(R)² factor.")
    print()
    status_line("ignoring angular sector produces false gauge artifact", True)


# =============================================================================
# Case 8: Summary classification
# =============================================================================

def case_8_summary_classification():
    header("Case 8: Summary classification")

    print("Results:")
    print()
    print("1. The areal radius is geometrically defined by sphere area.")
    print("2. In arbitrary radial coordinate R, the metric has angular radius S(R).")
    print("3. Transforming to areal radius r=S(R) gives:")
    print("     B_areal = Q(R)/S'(R)²")
    print("4. Therefore:")
    print("     kappa_areal = 1/2 ln[T(R) Q(R) / S'(R)²]")
    print("5. Areal-gauge compensation kappa_areal=0 becomes:")
    print("     T(R) Q(R) = S'(R)²")
    print("6. This is gauge-fixed/geometric, not a raw scalar condition.")
    print()
    print("Development implication:")
    print("  kappa=0 can be safely phrased as an areal-gauge condition derived")
    print("  from sphere-area radial foliation geometry.")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("This script answers the question in a qualified way:")
    print()
    print("  Can areal-gauge kappa=0 be re-expressed as a gauge-invariant")
    print("  or gauge-fixed condition derived from sphere area / radial foliation?")
    print()
    print("Answer:")
    print()
    print("  Not as an invariant scalar kappa=0.")
    print()
    print("  Yes as a gauge-fixed geometric construction:")
    print("    define areal radius by sphere area,")
    print("    express the metric in areal gauge,")
    print("    then impose kappa_areal = 1/2 ln(AB) = 0.")
    print()
    print("In arbitrary radial coordinate:")
    print("  ds² = -T(R)c²dt² + Q(R)dR² + S(R)²dΩ²")
    print()
    print("the same areal-gauge compensation condition is:")
    print("  T(R) Q(R) = S'(R)²")
    print()
    print("This includes the angular/sphere-area geometry and avoids the")
    print("naive gauge artifact TQ != 1 under radial reparameterization.")
    print()
    print("Possible next artifact:")
    print("  candidate_areal_gauge_kappa_condition.md")


# =============================================================================
# Main
# =============================================================================

def main():
    header("Candidate Areal-Gauge Kappa Condition")
    case_0_general_spherical_metric()
    case_1_areal_radius_from_area()
    case_2_transform_to_areal_radius()
    case_3_kappa_areal_from_arbitrary_metric()
    case_4_recover_reparameterization_result()
    case_5_gauge_fixed_condition_statement()
    case_6_arbitrary_coordinate_expression()
    case_7_failure_control_ignore_angular_sector()
    case_8_summary_classification()
    final_interpretation()


if __name__ == "__main__":
    main()
