"""Tests for exact vs perturbative reasoning."""

import sympy
from vacuumforge.metric.exactness import check_reciprocal_exactness, check_condition_perturbative


def test_exact_reciprocal():
    """exp(Phi/c^2) * exp(-Phi/c^2) = 1 exactly."""
    Phi = sympy.Symbol("Phi")
    c = sympy.Symbol("c", positive=True)
    A = sympy.exp(Phi / c**2)
    B = sympy.exp(-Phi / c**2)
    result = check_reciprocal_exactness(A, B, Phi, c)
    assert result.holds_exactly is True


def test_parallel_fails_at_order_1():
    """exp(Phi/c^2)^2 - 1 fails at first order."""
    Phi = sympy.Symbol("Phi")
    c = sympy.Symbol("c", positive=True)
    A = sympy.exp(Phi / c**2)
    B = sympy.exp(Phi / c**2)
    result = check_reciprocal_exactness(A, B, Phi, c)
    assert result.holds_exactly is False
    assert result.holds_to_order is False
    assert result.first_failure_order == 1


def test_first_order_only():
    """A model that matches AB=1 at first order but not second."""
    Phi = sympy.Symbol("Phi")
    c = sympy.Symbol("c", positive=True)
    eps = Phi / c**2
    # A = 1 + eps, B = 1 - eps => AB = 1 - eps^2 (first order ok, second fails)
    A = 1 + eps
    B = 1 - eps
    result = check_condition_perturbative(A * B - 1, Phi, c, order=2,
                                          target_description="AB=1")
    assert result.holds_to_order is False
    assert result.first_failure_order == 2
