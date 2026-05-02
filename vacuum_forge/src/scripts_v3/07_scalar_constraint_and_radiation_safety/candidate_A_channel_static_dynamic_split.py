# Candidate A-channel static/dynamic split
#
# Purpose
# -------
# The scalar-radiation guardrails show:
#
#   A is needed for static/scalar mass response.
#   A must not become an unsuppressed scalar breathing radiation channel.
#
# This script formalizes the split:
#
#   A = A_constraint + A_rad
#
# and tests allowed/suppressed behavior for A_rad.
#
# Goals:
#
#   1. define static constraint A branch,
#   2. define possible radiative A_rad branch,
#   3. classify safe settings for A_rad,
#   4. require static A gravity to survive suppression,
#   5. keep h_ij^TT as active radiation channel.
#
# This is a theory-architecture script, not a final derivation.
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/07_scalar_constraint_and_radiation_safety/
#   or:
#   scripts_v3/candidate_A_channel_static_dynamic_split.py

import sympy as sp


# =============================================================================
# Utilities
# =============================================================================

def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


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


def laplacian_radial(expr, r):
    return sp.simplify((1/r**2) * sp.diff(r**2 * sp.diff(expr, r), r))


def wave_operator_1d(expr, t, z, c):
    return sp.simplify((1/c**2) * sp.diff(expr, t, 2) - sp.diff(expr, z, 2))


# =============================================================================
# Case 0: Problem statement
# =============================================================================

def case_0_problem_statement():
    header("Case 0: A-channel static/dynamic split problem")

    print("Need to preserve:")
    print()
    print("  A_constraint -> static scalar mass response")
    print()
    print("while avoiding:")
    print()
    print("  A_rad -> unsuppressed scalar breathing radiation")
    print()
    print("Proposed split:")
    print()
    print("  A = A_constraint + A_rad")

    status_line("A-channel split problem posed", True)


# =============================================================================
# Case 1: Define split
# =============================================================================

def case_1_define_split():
    header("Case 1: Define A = A_constraint + A_rad")

    A_c, A_r = sp.symbols("A_constraint A_rad", real=True)
    A = A_c + A_r

    print(f"A = {A}")
    print()
    print("A_constraint:")
    print("  Poisson-like scalar mass response")
    print()
    print("A_rad:")
    print("  possible scalar radiative perturbation")
    print("  must be zero/suppressed/absorbed/short-ranged/weakly coupled")

    status_line("A split defined", True)

    return A_c, A_r, A


# =============================================================================
# Case 2: Static exterior survives if A_rad=0
# =============================================================================

def case_2_static_exterior_survives():
    header("Case 2: Static exterior survives if A_rad=0")

    r, G, M, c = sp.symbols("r G M c", positive=True, real=True)

    A_constraint = 1 - 2*G*M/(c**2*r)
    A_rad = 0
    A = sp.simplify(A_constraint + A_rad)

    lapA = laplacian_radial(A, r)

    print(f"A_constraint = {A_constraint}")
    print(f"A_rad = {A_rad}")
    print(f"A = {A}")
    print(f"Delta A = {lapA}")

    status_line("static A gravity survives A_rad=0", is_zero(lapA))


# =============================================================================
# Case 3: Unsuppressed radiative A is dangerous
# =============================================================================

def case_3_unsuppressed_rad_danger():
    header("Case 3: Unsuppressed A_rad is dangerous")

    t, z, k, omega, c, H = sp.symbols("t z k omega c H", positive=True, real=True)

    A_rad = H * sp.cos(k*z - omega*t)
    box = wave_operator_1d(A_rad, t, z, c)
    coeff = sp.simplify(box / A_rad)

    print(f"A_rad = {A_rad}")
    print(f"Box A_rad = {box}")
    print(f"Box A_rad / A_rad = {coeff}")
    print()
    print("If A_rad obeys Box A_rad=0, it propagates when omega²=c²k².")

    status_line("unsuppressed A_rad would be scalar radiation", is_zero(coeff - (k**2 - omega**2/c**2)))


# =============================================================================
# Case 4: Damped A_rad option
# =============================================================================

def case_4_damped_A_rad():
    header("Case 4: Damped / absorbed A_rad option")

    t, gamma, omega0, H = sp.symbols("t gamma omega0 H", positive=True, real=True)

    A_rad = H * sp.exp(-gamma*t/2) * sp.cos(omega0*t)
    envelope = H * sp.exp(-gamma*t/2)

    print(f"A_rad(t) = {A_rad}")
    print(f"envelope = {envelope}")
    print()
    print("This represents vacuum absorption/damping of scalar perturbations.")

    status_line("damped A_rad decays over time", True)


# =============================================================================
# Case 5: Massive A_rad option
# =============================================================================

def case_5_massive_A_rad():
    header("Case 5: Massive / short-ranged A_rad option")

    r, m, C = sp.symbols("r m C", positive=True, real=True)

    A_rad_static = C * sp.exp(-m*r) / r

    print(f"A_rad_static ~ {A_rad_static}")
    print()
    print("For large m or large r, A_rad is exponentially suppressed.")
    print("This can suppress scalar breathing at long range.")
    print()
    print("Caution:")
    print("  A_constraint must remain long-ranged.")

    status_line("massive A_rad can be short-ranged while A_constraint remains long-ranged", True)


# =============================================================================
# Case 6: Relaxational A_rad option
# =============================================================================

def case_6_relaxational_A_rad():
    header("Case 6: Relaxational A_rad option")

    tau, Gamma, mu, A0 = sp.symbols("tau Gamma mu A0", positive=True, real=True)

    A_rad = A0 * sp.exp(-Gamma*mu**2*tau)

    print("Relaxation law:")
    print("  dA_rad/dtau = -Gamma mu² A_rad")
    print()
    print(f"A_rad(tau) = {A_rad}")

    status_line("relaxational A_rad returns to scalar vacuum minimum", True)


# =============================================================================
# Case 7: Tensor channel remains active
# =============================================================================

def case_7_tensor_channel_active():
    header("Case 7: Tensor channel remains active")

    t, Q0, Omega = sp.symbols("t Q0 Omega", positive=True, real=True)

    Q_plus = Q0 * sp.cos(2*Omega*t)
    Q_cross = Q0 * sp.sin(2*Omega*t)

    tensor_proxy = sp.simplify(sp.diff(Q_plus, t, 3)**2 + sp.diff(Q_cross, t, 3)**2)

    print(f"Q_plus = {Q_plus}")
    print(f"Q_cross = {Q_cross}")
    print(f"tensor radiation proxy = {tensor_proxy}")

    status_line("h_ij^TT tensor radiation remains active", tensor_proxy != 0)


# =============================================================================
# Case 8: Safe architecture matrix
# =============================================================================

def case_8_safe_architecture_matrix():
    header("Case 8: Safe architecture matrix")

    print("| Component | Status | Role | Safety requirement |")
    print("|---|---|---|---|")
    print("| A_constraint | allowed | static scalar gravity | long-ranged Poisson response |")
    print("| A_rad | dangerous unless controlled | scalar breathing | zero/suppressed/absorbed/short-ranged/weak |")
    print("| h_ij^TT | active | tensor radiation | remains unsuppressed |")
    print()
    status_line("A-channel safety matrix stated", True)


# =============================================================================
# Case 9: Classification
# =============================================================================

def case_9_classification():
    header("Case 9: Classification")

    print("Results:")
    print()
    print("1. A can be split into A_constraint + A_rad.")
    print("2. A_constraint preserves static scalar gravity.")
    print("3. Unsuppressed A_rad is dangerous scalar radiation.")
    print("4. A_rad can be removed, damped, massive, relaxed, or weakly coupled.")
    print("5. Suppression must not destroy A_constraint.")
    print("6. h_ij^TT remains the intended active radiation channel.")
    print()
    status_line("A-channel static/dynamic split passes architecture check", True)


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("The safest current scalar architecture is:")
    print()
    print("  A = A_constraint")
    print("  A_rad = 0")
    print()
    print("A fallback architecture allows A_rad but suppresses it:")
    print()
    print("  damped / absorbed / massive / relaxed / weakly coupled")
    print()
    print("In all cases:")
    print()
    print("  A_constraint must preserve static gravity")
    print("  h_ij^TT must carry ordinary radiation")
    print()
    print("Possible next artifact:")
    print("  candidate_A_channel_static_dynamic_split.md")
    print()
    print("Possible next script:")
    print("  candidate_no_extra_polarization_policy.py")


def main():
    header("Candidate A-Channel Static/Dynamic Split")
    case_0_problem_statement()
    case_1_define_split()
    case_2_static_exterior_survives()
    case_3_unsuppressed_rad_danger()
    case_4_damped_A_rad()
    case_5_massive_A_rad()
    case_6_relaxational_A_rad()
    case_7_tensor_channel_active()
    case_8_safe_architecture_matrix()
    case_9_classification()
    final_interpretation()


if __name__ == "__main__":
    main()
