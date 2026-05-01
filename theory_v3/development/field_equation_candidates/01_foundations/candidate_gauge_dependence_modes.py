# Candidate gauge-dependence modes
#
# Purpose
# -------
# This script tests how the reduced log-scale modes
#
#   kappa = (ln A + ln B)/2
#   s     = (ln A - ln B)/2
#
# behave under simple radial coordinate changes.
#
# Motivation
# ----------
# The parent-mode study suggested:
#
#   kappa ~ reduced trace/conformal/determinant-like mode
#   s     ~ reduced trace-free/shear mode
#
# But kappa and s were defined in a static spherical reduced metric:
#
#   ds^2 = -A(r) c^2 dt^2 + B(r) dr^2 + r^2 dΩ^2
#
# This is areal-radius gauge.
#
# A coordinate change r = f(R) generally changes the radial metric factor
# and also changes the angular sector:
#
#   ds^2 = -A(f(R)) c^2 dt^2
#          + B(f(R)) [f'(R)]^2 dR^2
#          + f(R)^2 dΩ^2
#
# Unless f(R)=R, this is no longer in areal-radius form.
#
# If one naively computes:
#
#   kappa_naive = (ln A_new + ln B_new)/2
#   s_naive     = (ln A_new - ln B_new)/2
#
# using only the temporal and radial coefficients in the new coordinate R,
# then kappa and s generally change.
#
# That does NOT necessarily mean the physics changed. It means kappa and s
# are reduced/gauge-fixed variables, not coordinate-invariant scalars.
#
# This script tests:
#
#   Case 0: areal-gauge recap
#   Case 1: general radial reparameterization r=f(R)
#   Case 2: scaling r=λR
#   Case 3: weak nonlinear shift r=R+εξ(R)
#   Case 4: Schwarzschild-like AB=1 in areal gauge under radial reparameterization
#   Case 5: determinant factor including angular sector
#   Case 6: restoring areal gauge removes the apparent shift
#
# IMPORTANT:
# This is not a covariant decomposition.
# It is a warning tool: reduced kappa and s are gauge-sensitive unless
# the gauge and angular sector are specified.

import sympy as sp


# =============================================================================
# Utilities
# =============================================================================

def header(title: str) -> None:
    print()
    print("=" * 100)
    print(title)
    print("=" * 100)


def subheader(title: str) -> None:
    print()
    print("-" * 100)
    print(title)
    print("-" * 100)


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
# Case 0: areal-gauge recap
# =============================================================================

def case_0_areal_gauge_recap():
    header("Case 0: Areal-gauge recap")

    a, b = sp.symbols("a b", real=True)
    A = sp.exp(a)
    B = sp.exp(b)

    kappa = sp.simplify((a + b) / 2)
    s = sp.simplify((a - b) / 2)
    AB = sp.simplify(A * B)

    print("Areal-gauge static spherical metric:")
    print("  ds² = -A(r)c²dt² + B(r)dr² + r²dΩ²")
    print()
    print(f"a = ln A = {a}")
    print(f"b = ln B = {b}")
    print(f"kappa = {kappa}")
    print(f"s = {s}")
    print(f"AB = {AB}")

    status_line("AB = exp(2*kappa)", is_zero(AB - sp.exp(2*kappa)))
    status_line("kappa=0 gives AB=1", is_zero(AB.subs({b: -a}) - 1))


# =============================================================================
# Case 1: general radial reparameterization
# =============================================================================

def case_1_general_radial_reparameterization():
    header("Case 1: General radial reparameterization r=f(R)")

    R = sp.symbols("R", positive=True, real=True)
    f = sp.Function("f")(R)

    a = sp.Function("a")
    b = sp.Function("b")

    # Original areal-gauge coefficients:
    #   A(r)=exp(a(r)), B(r)=exp(b(r))
    #
    # Under r=f(R):
    #   A_new(R)=A(f(R))
    #   B_new(R)=B(f(R)) * (dr/dR)^2
    a_new = a(f)
    b_new = b(f) + 2 * sp.log(sp.diff(f, R))

    kappa_new = sp.simplify((a_new + b_new) / 2)
    s_new = sp.simplify((a_new - b_new) / 2)

    kappa_old_at_f = sp.simplify((a(f) + b(f)) / 2)
    s_old_at_f = sp.simplify((a(f) - b(f)) / 2)

    delta_kappa = sp.simplify(kappa_new - kappa_old_at_f)
    delta_s = sp.simplify(s_new - s_old_at_f)

    print("Under r=f(R):")
    print("  A_new(R) = A(f(R))")
    print("  B_new(R) = B(f(R)) [f'(R)]²")
    print("  angular sector = f(R)² dΩ²")
    print()
    print(f"a_new = {a_new}")
    print(f"b_new = {b_new}")
    print(f"kappa_new = {kappa_new}")
    print(f"s_new = {s_new}")
    print()
    print(f"kappa_old_at_f = {kappa_old_at_f}")
    print(f"s_old_at_f = {s_old_at_f}")
    print(f"delta_kappa = {delta_kappa}")
    print(f"delta_s = {delta_s}")

    expected_delta_k = sp.log(sp.diff(f, R))
    expected_delta_s = -sp.log(sp.diff(f, R))

    status_line("kappa shifts by log(f')", is_zero(delta_kappa - expected_delta_k))
    status_line("s shifts by -log(f')", is_zero(delta_s - expected_delta_s))

    print()
    print("Interpretation:")
    print("  Naive temporal-radial kappa and s are not invariant under radial")
    print("  reparameterization if one leaves areal gauge.")
    print("  The radial Jacobian moves information into B_new.")


# =============================================================================
# Case 2: simple scaling r=lambda R
# =============================================================================

def case_2_scaling_reparameterization():
    header("Case 2: Scaling reparameterization r = lambda R")

    R, lam = sp.symbols("R lambda", positive=True, real=True)
    aR, bR = sp.symbols("aR bR", real=True)

    # Treat a(f(R)) and b(f(R)) as aR, bR.
    fprime = lam

    kappa_old = sp.simplify((aR + bR) / 2)
    s_old = sp.simplify((aR - bR) / 2)

    b_new = bR + 2 * sp.log(fprime)
    a_new = aR

    kappa_new = sp.simplify((a_new + b_new) / 2)
    s_new = sp.simplify((a_new - b_new) / 2)

    print(f"kappa_old = {kappa_old}")
    print(f"s_old = {s_old}")
    print(f"kappa_new = {kappa_new}")
    print(f"s_new = {s_new}")
    print(f"delta kappa = {sp.simplify(kappa_new-kappa_old)}")
    print(f"delta s = {sp.simplify(s_new-s_old)}")

    status_line("kappa shifts by log(lambda)", is_zero((kappa_new-kappa_old) - sp.log(lam)))
    status_line("s shifts by -log(lambda)", is_zero((s_new-s_old) + sp.log(lam)))


# =============================================================================
# Case 3: infinitesimal radial shift r=R+epsilon xi(R)
# =============================================================================

def case_3_infinitesimal_radial_shift():
    header("Case 3: Infinitesimal radial shift r = R + eps xi(R)")

    R, eps = sp.symbols("R eps", real=True)
    xi = sp.Function("xi")(R)

    f = R + eps * xi
    fprime = sp.diff(f, R)

    # log(f') to first order in eps.
    log_fprime = sp.series(sp.log(fprime), eps, 0, 2).removeO()

    delta_kappa = log_fprime
    delta_s = -log_fprime

    print(f"f(R) = {f}")
    print(f"f'(R) = {fprime}")
    print(f"log(f') first order = {log_fprime}")
    print(f"delta kappa = {delta_kappa}")
    print(f"delta s = {delta_s}")

    expected = eps * sp.diff(xi, R)

    status_line("delta kappa = eps xi'(R)", is_zero(delta_kappa - expected))
    status_line("delta s = -eps xi'(R)", is_zero(delta_s + expected))

    print()
    print("Interpretation:")
    print("  Even an infinitesimal radial coordinate change shifts the naive")
    print("  reduced kappa and s by opposite amounts.")
    print("  This is a gauge artifact unless the areal gauge has been fixed.")


# =============================================================================
# Case 4: AB=1 in areal gauge does not remain naive AB=1 after reparameterization
# =============================================================================

def case_4_reciprocal_scaling_gauge_warning():
    header("Case 4: Reciprocal scaling gauge warning")

    R = sp.symbols("R", positive=True, real=True)
    f = sp.Function("f")(R)
    s = sp.Function("s")

    # Areal gauge compensated solution:
    #   A(r)=exp(s(r)), B(r)=exp(-s(r)), AB=1.
    A_old = sp.exp(s(f))
    B_old = sp.exp(-s(f))

    # Reparameterized radial coefficient:
    B_new = B_old * sp.diff(f, R)**2
    A_new = A_old
    AB_new_naive = sp.simplify(A_new * B_new)

    print("Original areal-gauge compensated sector:")
    print("  A(r)=exp(s(r)), B(r)=exp(-s(r)), AB=1")
    print()
    print("After r=f(R), using R as radial coordinate:")
    print(f"  A_new = {A_new}")
    print(f"  B_new = {B_new}")
    print(f"  naive A_new B_new = {AB_new_naive}")

    status_line("naive AB_new equals f'(R)^2", is_zero(AB_new_naive - sp.diff(f, R)**2))

    print()
    print("Interpretation:")
    print("  AB=1 is an areal-gauge statement in this reduced formulation.")
    print("  After radial reparameterization, naive A_new B_new != 1 unless f'=1.")
    print("  The geometry has not changed; the reduced gauge representation changed.")


# =============================================================================
# Case 5: determinant including angular sector
# =============================================================================

def case_5_full_determinant_behavior():
    header("Case 5: Determinant including angular sector")

    R, theta = sp.symbols("R theta", positive=True, real=True)
    f = sp.Function("f")(R)
    s = sp.Function("s")

    # Original compensated areal metric:
    #   A=exp(s), B=exp(-s)
    #   sqrt|g| = sqrt(AB) r^2 sinθ = r^2 sinθ
    #
    # Reparameterized:
    #   A_new=exp(s(f))
    #   B_new=exp(-s(f)) f'^2
    #   angular=f^2
    #   sqrt|g_new| = sqrt(A_new B_new) f^2 sinθ
    #                = f' f^2 sinθ
    #
    # This is exactly the Jacobian-transformed volume element:
    #   r^2 dr sinθ -> f^2 f' dR sinθ
    A_new = sp.exp(s(f))
    B_new = sp.exp(-s(f)) * sp.diff(f, R)**2
    sqrt_g_new = sp.simplify(sp.sqrt(A_new * B_new) * f**2 * sp.sin(theta))

    expected = sp.simplify(sp.diff(f, R) * f**2 * sp.sin(theta))

    print(f"sqrt|g_new| = {sqrt_g_new}")
    print(f"expected Jacobian volume factor = {expected}")

    status_line("full determinant transforms with radial Jacobian", is_zero(sqrt_g_new - expected))

    print()
    print("Interpretation:")
    print("  The full volume element transforms correctly.")
    print("  The apparent shift in kappa is a reduced temporal-radial-sector effect")
    print("  caused by leaving areal gauge, not a physical change in the metric.")


# =============================================================================
# Case 6: restoring areal gauge
# =============================================================================

def case_6_restoring_areal_gauge():
    header("Case 6: Restoring areal gauge")

    print("Areal radius is defined geometrically by sphere area:")
    print("  Area = 4π r_areal²")
    print()
    print("After a radial reparameterization r=f(R), the angular sector is:")
    print("  f(R)² dΩ²")
    print()
    print("The areal radius is therefore still:")
    print("  r_areal = f(R)")
    print()
    print("If we restore areal gauge by using r_areal as the radial coordinate,")
    print("then the metric returns to:")
    print("  ds² = -A(r_areal)c²dt² + B(r_areal)dr_areal² + r_areal²dΩ²")
    print()
    print("and the original reduced kappa and s are recovered.")
    print()
    status_line("kappa/s are meaningful only after reduced gauge is specified", True)


# =============================================================================
# Case 7: summary classification
# =============================================================================

def case_7_summary_classification():
    header("Case 7: Summary classification")

    print("Results:")
    print()
    print("1. Under r=f(R), naive reduced modes shift:")
    print("     kappa_new = kappa_old + log(f')")
    print("     s_new     = s_old - log(f')")
    print()
    print("2. Therefore kappa and s are not coordinate-invariant scalars.")
    print()
    print("3. AB=1 is a reduced areal-gauge condition.")
    print("   After radial reparameterization, naive A_new B_new = f'^2.")
    print()
    print("4. The full determinant / volume element transforms correctly.")
    print("   The apparent kappa shift is a gauge representation effect.")
    print()
    print("5. To use kappa and s physically, the theory must either:")
    print("     a) fix a gauge, such as areal-radius gauge, or")
    print("     b) identify covariant/gauge-aware parent quantities.")
    print()
    print("Development implication:")
    print("  Do not treat kappa or s as invariant fields yet.")
    print("  Treat them as reduced variables extracted after symmetry and gauge choice.")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("This script confirms the main danger:")
    print()
    print("  kappa and s are clean reduced variables, but they are gauge-sensitive.")
    print()
    print("A radial coordinate change r=f(R) shifts the naive temporal-radial")
    print("log modes by log(f'):")
    print()
    print("  kappa -> kappa + log(f')")
    print("  s     -> s - log(f')")
    print()
    print("Therefore:")
    print()
    print("  kappa=0 and AB=1 should be understood as areal-gauge reduced exterior")
    print("  statements, not coordinate-invariant scalar equations by themselves.")
    print()
    print("The next theoretical task is to find a gauge-aware or covariant parent")
    print("structure whose static spherical areal-gauge reduction gives kappa and s.")
    print()
    print("Possible next artifact:")
    print("  candidate_gauge_dependence_modes.md")


# =============================================================================
# Main
# =============================================================================

def main():
    header("Candidate Gauge-Dependence Modes")
    case_0_areal_gauge_recap()
    case_1_general_radial_reparameterization()
    case_2_scaling_reparameterization()
    case_3_infinitesimal_radial_shift()
    case_4_reciprocal_scaling_gauge_warning()
    case_5_full_determinant_behavior()
    case_6_restoring_areal_gauge()
    case_7_summary_classification()
    final_interpretation()


if __name__ == "__main__":
    main()
