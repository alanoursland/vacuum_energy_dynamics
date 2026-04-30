# Candidate kappa-suppression functionals v2
#
# Purpose
# -------
# This script extends candidate_kappa_suppression_functionals.py.
#
# v1 showed, in finite-dimensional toy functionals, that:
#
#   - kappa controls reciprocal scaling: AB = exp(2*kappa)
#   - exterior kappa suppression gives AB=1
#   - shear/compensated mode s can remain active while kappa=0
#   - directly sourcing kappa breaks reciprocal scaling generically
#
# v2 adds a continuum-limit toy using symbolic Euler-Lagrange equations.
#
# The target reduced-sector picture is:
#
#   source/interface physics may seed shear s at the boundary,
#   while the static source-free exterior has no kappa source and relaxes
#   kappa -> 0.
#
# This is a toy laboratory for the P7-style exterior compensation idea.
#
# This script is NOT a theorem and NOT a field equation.
# It is a reduced-sector symbolic development experiment.
#
# Suggested location:
#   scripts_v3/candidate_kappa_suppression_functionals_v2.py

import sympy as sp


# =============================================================================
# Utilities
# =============================================================================

def header(title: str) -> None:
    print()
    print("=" * 92)
    print(title)
    print("=" * 92)


def subheader(title: str) -> None:
    print()
    print("-" * 92)
    print(title)
    print("-" * 92)


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


def solve_stationary(energy, variables):
    equations = [sp.Eq(sp.diff(energy, v), 0) for v in variables]
    solutions = sp.solve(equations, variables, dict=True, simplify=True)
    return equations, solutions


def print_stationary_result(name, energy, variables):
    print(f"{name} energy:")
    print(f"  E = {sp.simplify(energy)}")
    equations, solutions = solve_stationary(energy, variables)
    print("Stationary equations:")
    for eq in equations:
        print(f"  {eq}")
    print("Solutions:")
    if solutions:
        for sol in solutions:
            print(f"  {sol}")
    else:
        print("  (none)")
    return equations, solutions


def reciprocal_status(kappa_expr):
    AB = sp.simplify(sp.exp(2 * kappa_expr))
    return AB, is_zero(AB - 1)


def euler_lagrange_density(L, field, coord):
    """Return Euler-Lagrange expression for L(field, field', coord)."""
    f = field
    fp = sp.diff(f, coord)
    return sp.simplify(sp.diff(L, f) - sp.diff(sp.diff(L, fp), coord))


# =============================================================================
# Case 0: Algebraic spine
# =============================================================================

def case_0_algebraic_spine():
    header("Case 0: Algebraic spine")

    kappa, s = sp.symbols("kappa s", real=True)
    A = sp.exp(kappa + s)
    B = sp.exp(kappa - s)
    AB = sp.simplify(A * B)

    print(f"A  = {A}")
    print(f"B  = {B}")
    print(f"AB = {AB}")

    status_line("AB = exp(2*kappa)", is_zero(AB - sp.exp(2 * kappa)))
    status_line("kappa=0 implies AB=1", is_zero(AB.subs(kappa, 0) - 1))


# =============================================================================
# Case 1: finite shell recap — interface shear, exterior kappa absent
# =============================================================================

def case_1_finite_shell_recap():
    header("Case 1: Finite shell recap — interface shear, exterior kappa absent")

    k1, k2, s1, s2 = sp.symbols("kappa_1 kappa_2 s_1 s_2", real=True)
    M_k, K_k, K_s, S_b = sp.symbols("M_k K_k K_s S_b", positive=True, real=True)

    # Same P7-style finite toy as v1 Case 5:
    #   kappa has suppression + smoothing but no source.
    #   shear is boundary-seeded and propagates through stiffness terms.
    E_k = M_k**2 * (k1**2 + k2**2) + K_k * (k2 - k1)**2
    E_s = K_s * ((s1 - S_b)**2 + (s2 - s1)**2 + s2**2)
    E = E_k + E_s

    _, sols = print_stationary_result("Case 1", E, [k1, k2, s1, s2])
    if not sols:
        return

    sol = sols[0]
    k1_eq = sp.simplify(sol[k1])
    k2_eq = sp.simplify(sol[k2])
    s1_eq = sp.simplify(sol[s1])
    s2_eq = sp.simplify(sol[s2])

    AB1, recip1 = reciprocal_status(k1_eq)
    AB2, recip2 = reciprocal_status(k2_eq)

    print()
    print(f"kappa_1_eq = {k1_eq}")
    print(f"kappa_2_eq = {k2_eq}")
    print(f"s_1_eq     = {s1_eq}")
    print(f"s_2_eq     = {s2_eq}")
    print(f"AB_1       = {AB1}")
    print(f"AB_2       = {AB2}")

    status_line("both exterior kappa shells suppressed", k1_eq == 0 and k2_eq == 0)
    status_line("reciprocal scaling holds in both shells", recip1 and recip2)
    status_line("shear remains active", (not is_zero(s1_eq)) and (not is_zero(s2_eq)))


# =============================================================================
# Case 2: finite shell control — interface kappa source
# =============================================================================

def case_2_finite_shell_kappa_source_control():
    header("Case 2: Finite shell control — interface kappa source")

    k1, k2, s1, s2 = sp.symbols("kappa_1 kappa_2 s_1 s_2", real=True)
    M_k, K_k, K_s, S_b, K_b = sp.symbols(
        "M_k K_k K_s S_b K_b", positive=True, real=True
    )

    # Same as Case 1, but now the interface/source directly seeds kappa_1.
    # Expected: kappa propagates outward through stiffness and AB != 1.
    E_k = M_k**2 * ((k1 - K_b)**2 + k2**2) + K_k * (k2 - k1)**2
    E_s = K_s * ((s1 - S_b)**2 + (s2 - s1)**2 + s2**2)
    E = E_k + E_s

    _, sols = print_stationary_result("Case 2", E, [k1, k2, s1, s2])
    if not sols:
        return

    sol = sols[0]
    k1_eq = sp.simplify(sol[k1])
    k2_eq = sp.simplify(sol[k2])
    s1_eq = sp.simplify(sol[s1])
    s2_eq = sp.simplify(sol[s2])

    AB1, recip1 = reciprocal_status(k1_eq)
    AB2, recip2 = reciprocal_status(k2_eq)

    print()
    print(f"kappa_1_eq = {k1_eq}")
    print(f"kappa_2_eq = {k2_eq}")
    print(f"s_1_eq     = {s1_eq}")
    print(f"s_2_eq     = {s2_eq}")
    print(f"AB_1       = {AB1}")
    print(f"AB_2       = {AB2}")

    status_line("kappa becomes nonzero generically", k1_eq != 0 and k2_eq != 0)
    status_line("reciprocal scaling fails generically", (not recip1) and (not recip2))
    status_line("shear remains active", (not is_zero(s1_eq)) and (not is_zero(s2_eq)))


# =============================================================================
# Case 3: continuum Euler-Lagrange toy — source-free exterior
# =============================================================================

def case_3_continuum_source_free_exterior():
    header("Case 3: Continuum Euler-Lagrange toy — source-free exterior")

    r = sp.symbols("r", real=True)
    Kk, Mk, Ks, Ms = sp.symbols("K_k M_k K_s M_s", positive=True, real=True)

    kappa = sp.Function("kappa")(r)
    s = sp.Function("s")(r)

    # Continuum reduced exterior density.
    #
    # Kappa has stiffness + mass/suppression:
    #   L_k = Kk (kappa')^2 + Mk^2 kappa^2
    #
    # Shear has stiffness + optional weak mass/regularizer:
    #   L_s = Ks (s')^2 + Ms^2 s^2
    #
    # Source-free exterior means no linear source term in kappa.
    L = Kk * sp.diff(kappa, r)**2 + Mk**2 * kappa**2 + Ks * sp.diff(s, r)**2 + Ms**2 * s**2

    EL_k = euler_lagrange_density(L, kappa, r)
    EL_s = euler_lagrange_density(L, s, r)

    print("Density:")
    print(f"  L = {L}")
    print()
    print("Euler-Lagrange equations:")
    print(f"  EL_kappa = {EL_k} = 0")
    print(f"  EL_s     = {EL_s} = 0")

    # Check kappa=0 is a solution of the source-free kappa equation.
    EL_k_at_zero = sp.simplify(EL_k.subs({
        kappa: 0,
        sp.diff(kappa, r): 0,
        sp.diff(kappa, (r, 2)): 0,
    }))

    print()
    print(f"EL_kappa | kappa=0 = {EL_k_at_zero}")
    status_line("kappa=0 solves source-free exterior kappa equation", is_zero(EL_k_at_zero))

    print()
    print("Interpretation:")
    print("  With positive Mk^2 and no kappa source, the exterior kappa equation")
    print("  has kappa=0 as its minimum/relaxed solution under zero boundary data.")
    print("  Shear s can be nonzero if seeded by boundary conditions, even though")
    print("  its local source-free equation is homogeneous.")


# =============================================================================
# Case 4: continuum control — kappa source breaks reciprocal scaling
# =============================================================================

def case_4_continuum_kappa_source_control():
    header("Case 4: Continuum control — kappa source")

    r = sp.symbols("r", real=True)
    Kk, Mk, Jk = sp.symbols("K_k M_k J_k", positive=True, real=True)

    kappa = sp.Function("kappa")(r)

    # Add a linear kappa source term.
    L = Kk * sp.diff(kappa, r)**2 + Mk**2 * kappa**2 - Jk * kappa

    EL_k = euler_lagrange_density(L, kappa, r)

    print("Density:")
    print(f"  L = {L}")
    print()
    print("Euler-Lagrange equation:")
    print(f"  EL_kappa = {EL_k} = 0")

    # Constant equilibrium: kappa' = kappa'' = 0.
    k0 = sp.symbols("k0", real=True)
    algebraic_eq = sp.simplify(EL_k.subs({
        kappa: k0,
        sp.diff(kappa, r): 0,
        sp.diff(kappa, (r, 2)): 0,
    }))

    sol_k0 = sp.solve(sp.Eq(algebraic_eq, 0), k0)
    print()
    print(f"Constant-equilibrium equation: {algebraic_eq} = 0")
    print(f"Constant kappa solutions: {sol_k0}")

    if sol_k0:
        k_eq = sp.simplify(sol_k0[0])
        AB, recip = reciprocal_status(k_eq)
        print(f"kappa_eq = {k_eq}")
        print(f"AB       = {AB}")
        status_line("kappa source makes kappa nonzero generically", k_eq != 0)
        status_line("reciprocal scaling fails generically", not recip)


# =============================================================================
# Case 5: continuum boundary-seeded shear, kappa boundary zero
# =============================================================================

def case_5_continuum_boundary_seeded_shear():
    header("Case 5: Continuum boundary-seeded shear, kappa boundary zero")

    r, R = sp.symbols("r R", positive=True, real=True)
    Kk, Mk, Ks = sp.symbols("K_k M_k K_s", positive=True, real=True)
    S0 = sp.symbols("S_0", real=True)

    kappa = sp.Function("kappa")(r)
    s = sp.Function("s")(r)

    # Exterior source-free bulk:
    L_bulk = Kk * sp.diff(kappa, r)**2 + Mk**2 * kappa**2 + Ks * sp.diff(s, r)**2

    EL_k = euler_lagrange_density(L_bulk, kappa, r)
    EL_s = euler_lagrange_density(L_bulk, s, r)

    print("Bulk density:")
    print(f"  L_bulk = {L_bulk}")
    print()
    print("Bulk Euler-Lagrange equations:")
    print(f"  EL_kappa = {EL_k} = 0")
    print(f"  EL_s     = {EL_s} = 0")

    print()
    print("Boundary conditions for toy interpretation:")
    print("  kappa(0) = 0, kappa(infinity or R) = 0")
    print("  s(0) = S_0, s(R) = 0")
    print()
    print("Then:")
    print("  kappa(r)=0 is the relaxed exterior solution.")
    print("  s(r) can interpolate from S_0 at the interface to 0 at the outer boundary.")

    # Explicit simple solution for shear if s'' = 0 on finite interval:
    # s(r) = S0 * (1 - r/R)
    s_trial = S0 * (1 - r / R)
    k_trial = sp.Integer(0)

    EL_k_trial = sp.simplify(EL_k.subs({
        kappa: k_trial,
        sp.diff(kappa, r): 0,
        sp.diff(kappa, (r, 2)): 0,
    }))

    # For s with L=Ks*s'^2, EL_s = -2Ks*s''.
    EL_s_trial = sp.simplify(EL_s.subs({
        s: s_trial,
        sp.diff(s, r): sp.diff(s_trial, r),
        sp.diff(s, (r, 2)): sp.diff(s_trial, (r, 2)),
    }))

    print()
    print(f"Trial kappa(r) = {k_trial}")
    print(f"Trial s(r)     = {s_trial}")
    print(f"EL_kappa trial = {EL_k_trial}")
    print(f"EL_s trial     = {EL_s_trial}")

    status_line("kappa=0 solves exterior bulk equation", is_zero(EL_k_trial))
    status_line("linear boundary-seeded shear solves massless shear bulk equation", is_zero(EL_s_trial))

    AB, recip = reciprocal_status(k_trial)
    print(f"AB for kappa=0 = {AB}")
    status_line("reciprocal scaling holds throughout exterior", recip)


# =============================================================================
# Case 6: continuum boundary kappa source control
# =============================================================================

def case_6_continuum_boundary_kappa_source_control():
    header("Case 6: Continuum boundary kappa source control")

    r, R = sp.symbols("r R", positive=True, real=True)
    K0 = sp.symbols("K_0", real=True)

    # This is a simple boundary-control demonstration rather than a full
    # variational boundary-value solve.
    #
    # If kappa is seeded at the interface and relaxes linearly to zero on
    # a finite interval, then kappa is nonzero in the exterior and AB != 1.
    k_trial = K0 * (1 - r / R)
    AB = sp.simplify(sp.exp(2 * k_trial))

    print("Boundary-seeded kappa trial:")
    print(f"  kappa(r) = {k_trial}")
    print(f"  AB(r)    = {AB}")
    print()
    status_line("kappa is nonzero away from outer boundary", not is_zero(k_trial))
    status_line("reciprocal scaling fails generically", not is_zero(AB - 1))
    print()
    print("Interpretation:")
    print("  If the interface directly seeds kappa into the exterior, the exterior")
    print("  generally has AB != 1 unless an additional condition suppresses kappa.")
    print("  This remains the key failure control.")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("The v2 toy suite supports a sharper P7-style development target:")
    print()
    print("  The exterior functional should contain a kappa-suppression structure")
    print("  or exterior no-source condition such that kappa relaxes to zero.")
    print()
    print("  The source/interface should be allowed to seed the compensated/shear")
    print("  mode s, so the exterior can carry a gravitational distortion.")
    print()
    print("  Directly seeding exterior kappa is the failure mode: it produces")
    print("  AB = exp(2*kappa) != 1 and loses reciprocal scaling.")
    print()
    print("Continuum toy lesson:")
    print()
    print("  A bulk density like")
    print("      K_k (kappa')^2 + M_k^2 kappa^2")
    print("  with no kappa source has kappa=0 as a relaxed exterior solution.")
    print()
    print("  A bulk or boundary source for kappa moves the solution away from")
    print("  kappa=0 and therefore breaks reciprocal scaling unless another")
    print("  constraint removes it.")
    print()
    print("This remains a reduced-sector toy. The future theory still needs:")
    print()
    print("  - a covariant parent of kappa and s,")
    print("  - a source/interface rule,")
    print("  - a source law for the exterior profile,")
    print("  - and a full field equation or variational principle.")


# =============================================================================
# Main
# =============================================================================

def main():
    header("Candidate Kappa-Suppression Functionals v2")
    case_0_algebraic_spine()
    case_1_finite_shell_recap()
    case_2_finite_shell_kappa_source_control()
    case_3_continuum_source_free_exterior()
    case_4_continuum_kappa_source_control()
    case_5_continuum_boundary_seeded_shear()
    case_6_continuum_boundary_kappa_source_control()
    final_interpretation()


if __name__ == "__main__":
    main()
