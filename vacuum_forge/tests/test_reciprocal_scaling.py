"""Tests for reciprocal scaling checks."""

import sympy
from vacuumforge.metric.reciprocal import (
    check_exact_reciprocal,
    check_kappa_zero,
    check_perturbative_reciprocal,
)


def test_reciprocal_exponential_passes():
    """A = exp(Phi/c^2), B = exp(-Phi/c^2) => AB = 1."""
    Phi = sympy.Symbol("Phi")
    c = sympy.Symbol("c", positive=True)
    A = sympy.exp(Phi / c**2)
    B = sympy.exp(-Phi / c**2)
    result = check_exact_reciprocal(A, B)
    assert result.status == "pass"
    assert result.holds is True


def test_parallel_scaling_fails():
    """A = B = exp(Phi/c^2) => AB != 1."""
    Phi = sympy.Symbol("Phi")
    c = sympy.Symbol("c", positive=True)
    A = sympy.exp(Phi / c**2)
    B = sympy.exp(Phi / c**2)
    result = check_exact_reciprocal(A, B)
    assert result.status == "fail"
    assert result.holds is False


def test_explicit_reciprocal():
    """B = 1/A."""
    A = sympy.Symbol("A", positive=True)
    B = 1 / A
    result = check_exact_reciprocal(A, B)
    assert result.status == "pass"


def test_free_gamma_fails():
    """B = A^(-gamma_v) with free gamma_v fails for generic gamma_v."""
    Phi = sympy.Symbol("Phi")
    c = sympy.Symbol("c", positive=True)
    gamma_v = sympy.Symbol("gamma_v")
    A = sympy.exp(Phi / c**2)
    B = sympy.exp(-gamma_v * Phi / c**2)
    result = check_exact_reciprocal(A, B)
    # Should fail because gamma_v is free
    assert result.status == "fail"


def test_kappa_zero_passes():
    result = check_kappa_zero(sympy.Integer(0))
    assert result.status == "pass"
    assert result.holds is True


def test_kappa_nonzero_fails():
    kappa = sympy.Symbol("kappa")
    result = check_kappa_zero(kappa)
    assert result.status == "fail"


def test_perturbative_reciprocal():
    Phi = sympy.Symbol("Phi")
    c = sympy.Symbol("c", positive=True)
    A = sympy.exp(Phi / c**2)
    B = sympy.exp(-Phi / c**2)
    result = check_perturbative_reciprocal(A, B, Phi, c, order=2)
    assert result.status == "pass"


def test_perturbative_parallel_fails():
    Phi = sympy.Symbol("Phi")
    c = sympy.Symbol("c", positive=True)
    A = sympy.exp(Phi / c**2)
    B = sympy.exp(Phi / c**2)
    result = check_perturbative_reciprocal(A, B, Phi, c, order=2)
    assert result.status == "fail"


def test_context_reciprocal_check(ctx):
    """Test through the context checks proxy."""
    import sympy as sp
    ms = ctx._mode_symbols
    A = sp.exp(ms.Phi / ms.c**2)
    B = sp.exp(-ms.Phi / ms.c**2)
    result = ctx.checks.reciprocal_scaling(A, B)
    assert result.status == "pass"
