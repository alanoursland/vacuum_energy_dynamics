# Candidate covariant parent modes
#
# Purpose
# -------
# This script starts the transition from reduced exterior variables
# to possible full metric/geometric parent structures.
#
# Reduced variables from the exterior program:
#
#   a = ln A
#   b = ln B
#
#   kappa = (a + b)/2
#   s     = (a - b)/2
#
#   A = exp(kappa + s)
#   B = exp(kappa - s)
#   AB = exp(2*kappa)
#
# In static spherical symmetry with kappa=0:
#
#   A = exp(s)
#   B = exp(-s)
#   AB = 1
#
# Question:
#   What are kappa and s shadows of in the full metric?
#
# This script explores reduced candidates:
#
#   1. kappa as a trace/conformal/volume-like mode.
#   2. s as a trace-free or compensated temporal-radial shear mode.
#   3. the relation between reduced 2-sector modes and 3+1 trace splitting.
#   4. the danger that kappa/s are coordinate-gauge artifacts unless their
#      parent quantities are defined carefully.
#
# IMPORTANT:
# This is exploratory. It does not identify the final covariant parent.
# It only tests candidate reductions and normalization conventions.
#
# Suggested location:
#   scripts_v3/candidate_covariant_parent_modes.py

import sympy as sp


# =============================================================================
# Utilities
# =============================================================================

def header(title: str) -> None:
    print()
    print("=" * 96)
    print(title)
    print("=" * 96)


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


def mat_trace(M):
    return sp.simplify(sum(M[i, i] for i in range(M.shape[0])))


# =============================================================================
# Case 0: Reduced log-scale algebra recap
# =============================================================================

def case_0_reduced_log_scale_recap():
    header("Case 0: Reduced log-scale algebra recap")

    kappa, s = sp.symbols("kappa s", real=True)

    a = kappa + s
    b = kappa - s

    A = sp.exp(a)
    B = sp.exp(b)
    AB = sp.simplify(A * B)

    print(f"a = ln A = {a}")
    print(f"b = ln B = {b}")
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"AB = {AB}")

    status_line("AB = exp(2*kappa)", is_zero(AB - sp.exp(2*kappa)))
    status_line("kappa=0 gives reciprocal scaling", is_zero(AB.subs(kappa, 0) - 1))


# =============================================================================
# Case 1: 2-sector trace and shear decomposition
# =============================================================================

def case_1_two_sector_trace_shear():
    header("Case 1: 2-sector trace/shear decomposition")

    a, b = sp.symbols("a b", real=True)

    # Reduced 2-vector of log metric coefficients.
    v = sp.Matrix([a, b])

    # Trace-like direction and shear-like direction in the temporal-radial
    # two-sector.
    trace_basis = sp.Matrix([1, 1])
    shear_basis = sp.Matrix([1, -1])

    kappa = sp.simplify((a + b) / 2)
    s = sp.simplify((a - b) / 2)

    v_reconstructed = sp.simplify(kappa * trace_basis + s * shear_basis)

    print(f"v = [a,b] = {v.T}")
    print(f"kappa = (a+b)/2 = {kappa}")
    print(f"s = (a-b)/2 = {s}")
    print(f"kappa*[1,1] + s*[1,-1] = {v_reconstructed.T}")

    status_line("2-sector decomposition reconstructs [a,b]", v_reconstructed == v)

    # Dot products in Euclidean mode space, only as an algebraic toy.
    dot_trace_shear = sp.simplify(trace_basis.dot(shear_basis))
    print(f"[1,1]·[1,-1] = {dot_trace_shear}")
    status_line("trace and shear basis are orthogonal in toy mode space", is_zero(dot_trace_shear))


# =============================================================================
# Case 2: 3+1 isotropic spatial reduction
# =============================================================================

def case_2_physical_3plus1_trace_split():
    header("Case 2: 3+1 isotropic spatial trace split")

    q_t, q_x, q_y, q_z = sp.symbols("q_t q_x q_y q_z", real=True)

    # Candidate pre-mode log scales:
    #   q_t = temporal log scale
    #   q_i = spatial directional log scales
    #
    # Isotropic spatial reduction:
    #   b = average spatial log scale
    a = q_t
    b = sp.simplify((q_x + q_y + q_z) / 3)

    kappa = sp.simplify((a + b) / 2)
    s = sp.simplify((a - b) / 2)

    print(f"a = q_t = {a}")
    print(f"b = spatial average = {b}")
    print(f"kappa = {kappa}")
    print(f"s = {s}")

    # Trace-kernel condition from earlier:
    #   delta q_t + (delta q_x+delta q_y+delta q_z)/3 = 0
    S = sp.symbols("S", real=True)
    dq = {
        q_t: -S,
        q_x: S,
        q_y: S,
        q_z: S,
    }

    delta_a = sp.simplify(a.subs(dq) - a.subs({q_t: 0, q_x: 0, q_y: 0, q_z: 0}))
    delta_b = sp.simplify(b.subs(dq) - b.subs({q_t: 0, q_x: 0, q_y: 0, q_z: 0}))
    delta_kappa = sp.simplify((delta_a + delta_b) / 2)
    delta_s = sp.simplify((delta_a - delta_b) / 2)

    print()
    print("Isotropic time-vs-space exchange:")
    print("  delta(q_t,q_x,q_y,q_z) = (-S,S,S,S)")
    print(f"  delta a = {delta_a}")
    print(f"  delta b = {delta_b}")
    print(f"  delta kappa = {delta_kappa}")
    print(f"  delta s = {delta_s}")

    status_line("exchange lies in kappa-kernel", is_zero(delta_kappa))
    status_line("exchange excites shear s", not is_zero(delta_s))


# =============================================================================
# Case 3: Linearized metric perturbation trace comparison
# =============================================================================

def case_3_linearized_trace_comparison():
    header("Case 3: Linearized metric perturbation trace comparison")

    # This case compares the reduced log modes with a simple linearized metric
    # perturbation around Minkowski.
    #
    # Use signature (-,+,+,+).
    #
    # Toy diagonal metric:
    #   g_tt = -exp(a)
    #   g_rr =  exp(b)
    #
    # In weak field:
    #   h_tt ~ -(A-1)
    #   h_rr ~  B-1
    #
    # Reduced log modes are cleaner than raw h components, but the linear trace
    # hints at parent trace/shear structure.

    a, b = sp.symbols("a b", real=True)
    eps = sp.symbols("eps", real=True)

    # Substitute a=eps*a1, b=eps*b1 for first-order expansion.
    a1, b1 = sp.symbols("a1 b1", real=True)
    A = sp.exp(eps * a1)
    B = sp.exp(eps * b1)

    # Linear perturbations in diagonal tt and rr components.
    # g_tt = -A = -1 + h_tt => h_tt = -(A-1)
    # g_rr = B = 1 + h_rr => h_rr = B-1
    h_tt = sp.series(-(A - 1), eps, 0, 2).removeO()
    h_rr = sp.series(B - 1, eps, 0, 2).removeO()

    # Minkowski inverse trace contribution for tt and rr:
    # h = eta^{tt} h_tt + eta^{rr} h_rr = -h_tt + h_rr
    trace_2 = sp.simplify(-h_tt + h_rr)

    kappa_linear = sp.simplify((eps*a1 + eps*b1) / 2)
    s_linear = sp.simplify((eps*a1 - eps*b1) / 2)

    print(f"A = exp(eps*a1), B = exp(eps*b1)")
    print(f"h_tt first order = {h_tt}")
    print(f"h_rr first order = {h_rr}")
    print(f"2-sector Minkowski trace contribution -h_tt+h_rr = {trace_2}")
    print(f"kappa linear = {kappa_linear}")
    print(f"s linear = {s_linear}")

    # trace_2 = eps*(a1+b1) = 2*kappa_linear
    status_line("linearized 2-sector trace is 2*kappa", is_zero(trace_2 - 2*kappa_linear))

    print()
    print("Interpretation:")
    print("  In this reduced diagonal sector, kappa matches half of the")
    print("  linearized temporal-radial trace contribution.")
    print("  This supports kappa as a trace/conformal-like parent candidate,")
    print("  but it is not yet a covariant definition.")


# =============================================================================
# Case 4: Trace-free shear in the reduced 2-sector
# =============================================================================

def case_4_trace_free_shear_linearized():
    header("Case 4: Trace-free shear in reduced linearized sector")

    eps, s = sp.symbols("eps s", real=True)

    # Pure shear/compensated mode:
    #   kappa = 0
    #   a = s
    #   b = -s
    a = eps * s
    b = -eps * s

    A = sp.exp(a)
    B = sp.exp(b)

    h_tt = sp.series(-(A - 1), eps, 0, 2).removeO()
    h_rr = sp.series(B - 1, eps, 0, 2).removeO()
    trace_2 = sp.simplify(-h_tt + h_rr)

    print("Pure reduced shear:")
    print(f"  a = {a}")
    print(f"  b = {b}")
    print(f"  A = {A}")
    print(f"  B = {B}")
    print(f"  h_tt first order = {h_tt}")
    print(f"  h_rr first order = {h_rr}")
    print(f"  reduced trace contribution = {trace_2}")

    status_line("pure reduced shear is trace-free to first order", is_zero(trace_2))


# =============================================================================
# Case 5: Determinant / volume caution
# =============================================================================

def case_5_determinant_volume_caution():
    header("Case 5: Determinant / volume caution")

    a, b, r, theta = sp.symbols("a b r theta", real=True, positive=True)

    # Static spherical metric in areal radius:
    #   ds² = -A dt² + B dr² + r² dΩ²
    # determinant magnitude:
    #   |g| = A B r^4 sin²θ
    # sqrt(|g|) = sqrt(A B) r² sinθ = exp(kappa) r² sinθ
    A = sp.exp(a)
    B = sp.exp(b)
    sqrt_abs_g = sp.sqrt(A * B) * r**2 * sp.sin(theta)

    kappa = sp.simplify((a + b) / 2)
    sqrt_abs_g_k = sp.simplify(sp.exp(kappa) * r**2 * sp.sin(theta))

    print("Areal-radius static spherical determinant:")
    print(f"  sqrt(|g|) = {sqrt_abs_g}")
    print(f"  exp(kappa) r² sin(theta) = {sqrt_abs_g_k}")

    status_line("sqrt(|g|) temporal-radial factor is exp(kappa)", is_zero(sqrt_abs_g - sqrt_abs_g_k))

    print()
    print("Caution:")
    print("  In areal-radius coordinates, the angular sector is fixed as r²dΩ².")
    print("  Therefore kappa controls the temporal-radial determinant factor,")
    print("  not a fully coordinate-independent volume mode by itself.")
    print("  A covariant parent must handle gauge/coordinate dependence carefully.")


# =============================================================================
# Case 6: Candidate parent classification
# =============================================================================

def case_6_candidate_parent_classification():
    header("Case 6: Candidate parent classification")

    print("Candidate parent interpretation:")
    print()
    print("  kappa:")
    print("    reduced trace / conformal / determinant-like mode")
    print("    controls AB = exp(2*kappa)")
    print("    equals half the temporal-radial linearized trace contribution")
    print("    controls sqrt(|g|)'s temporal-radial factor in areal gauge")
    print()
    print("  s:")
    print("    reduced trace-free temporal-radial shear mode")
    print("    preserves AB when kappa=0")
    print("    carries compensated exterior distortion")
    print()
    print("Main caution:")
    print("  These are reduced static spherical sector variables.")
    print("  They are not yet covariant fields.")
    print("  A full theory must identify gauge-aware or covariant parent structures.")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("This exploratory script supports the following working hypothesis:")
    print()
    print("  kappa is the reduced trace/conformal/determinant-like mode")
    print("  of the temporal-radial exterior sector.")
    print()
    print("  s is the reduced trace-free/shear mode that remains when")
    print("  the source-free exterior suppresses kappa.")
    print()
    print("In the reduced sector:")
    print("  kappa = 0 -> AB = 1")
    print("  s != 0 carries compensated exterior distortion")
    print()
    print("But this script also emphasizes the caveat:")
    print("  kappa and s are not yet covariant objects.")
    print("  They are reduced variables extracted in a static spherical setting.")
    print()
    print("Next theoretical target:")
    print("  Find a gauge-aware or covariant decomposition of metric variations")
    print("  whose static spherical reduction gives kappa and s.")
    print()
    print("Possible next artifact:")
    print("  candidate_covariant_parent_modes.md")


# =============================================================================
# Main
# =============================================================================

def main():
    header("Candidate Covariant Parent Modes")
    case_0_reduced_log_scale_recap()
    case_1_two_sector_trace_shear()
    case_2_physical_3plus1_trace_split()
    case_3_linearized_trace_comparison()
    case_4_trace_free_shear_linearized()
    case_5_determinant_volume_caution()
    case_6_candidate_parent_classification()
    final_interpretation()


if __name__ == "__main__":
    main()
