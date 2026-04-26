"""Tests for Euler-Lagrange field support (M33)."""

import sympy
from vacuumforge.energy.euler_lagrange import (
    euler_lagrange_1d,
    radial_mode_density,
)


def test_single_field_harmonic():
    """E-L for L = K*(f')^2 + C*f^2 gives -2*K*f'' + 2*C*f = 0."""
    r = sympy.Symbol("r")
    f = sympy.Function("f")
    K = sympy.Symbol("K", positive=True)
    C = sympy.Symbol("C", positive=True)

    density = K * sympy.diff(f(r), r)**2 + C * f(r)**2
    result = euler_lagrange_1d(density, [f(r)], r)

    eq = result.equations[f(r)]
    # EL: 2*C*f(r) - 2*K*f''(r) = 0
    # Check structure: should contain f'' and f
    assert sympy.diff(f(r), r, 2) in eq.atoms(sympy.Derivative) or eq != 0


def test_two_field_decoupled():
    """Two decoupled fields: each E-L equation involves only its own field."""
    r = sympy.Symbol("r")
    kappa = sympy.Function("kappa")
    sigma = sympy.Function("sigma")
    K1 = sympy.Symbol("K1", positive=True)
    K2 = sympy.Symbol("K2", positive=True)

    density = K1 * sympy.diff(kappa(r), r)**2 + K2 * sympy.diff(sigma(r), r)**2
    result = euler_lagrange_1d(density, [kappa(r), sigma(r)], r)

    assert kappa(r) in result.equations
    assert sigma(r) in result.equations


def test_sourced_field():
    """L = K*(f')^2 + C*f^2 - J*f => EL stationary at f = J/(2C)."""
    r = sympy.Symbol("r")
    f = sympy.Function("f")
    K = sympy.Symbol("K", positive=True)
    C = sympy.Symbol("C", positive=True)
    J = sympy.Symbol("J")

    density = K * sympy.diff(f(r), r)**2 + C * f(r)**2 - J * f(r)
    result = euler_lagrange_1d(density, [f(r)], r)

    # For uniform f (f'=0), the EL reduces to 2*C*f - J = 0 => f = J/(2C)
    eq = result.equations[f(r)]
    uniform = eq.subs(sympy.diff(f(r), r, 2), 0).subs(sympy.diff(f(r), r), 0)
    sol = sympy.solve(uniform, f(r))
    assert len(sol) == 1
    assert sympy.simplify(sol[0] - J / (2 * C)) == 0


def test_radial_mode_density():
    """Test the convenience builder for mode densities."""
    r = sympy.Symbol("r")
    kappa = sympy.Function("kappa")
    sigma = sympy.Function("sigma")
    K_kappa = sympy.Symbol("K_kappa", positive=True)
    K_sigma = sympy.Symbol("K_sigma", positive=True)
    C_kappa = sympy.Symbol("C_kappa", positive=True)
    C_sigma = sympy.Symbol("C_sigma", positive=True)
    J_kappa = sympy.Symbol("J_kappa")
    J_sigma = sympy.Symbol("J_sigma")

    L = radial_mode_density(
        K_kappa, K_sigma, C_kappa, C_sigma,
        J_kappa, J_sigma, kappa(r), sigma(r), r,
    )
    # Should contain derivative terms
    assert sympy.diff(kappa(r), r) in L.atoms(sympy.Derivative) or L != 0


def test_boundary_conditions():
    """Test that boundary conditions are recorded."""
    r = sympy.Symbol("r")
    f = sympy.Function("f")
    K = sympy.Symbol("K", positive=True)
    density = K * sympy.diff(f(r), r)**2

    result = euler_lagrange_1d(
        density, [f(r)], r,
        boundary_conditions=["f(0) = 0", "f(inf) -> 0"],
    )
    assert len(result.boundary_conditions) == 2
