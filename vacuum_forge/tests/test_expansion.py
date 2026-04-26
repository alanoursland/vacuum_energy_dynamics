"""Tests for weak-field expansion engine."""

import sympy
from vacuumforge.metric.expansion import ExpansionEngine


def make_engine():
    Phi = sympy.Symbol("Phi")
    c = sympy.Symbol("c", positive=True)
    return ExpansionEngine(Phi, c), Phi, c


def test_expand_exp():
    """exp(Phi/c^2) to second order."""
    eng, Phi, c = make_engine()
    result = eng.weak_field(sympy.exp(Phi / c**2), order=2)
    expected = 1 + Phi / c**2 + Phi**2 / (2 * c**4)
    assert sympy.simplify(result.expanded - expected) == 0


def test_expand_exp_double():
    """exp(2*Phi/c^2) to second order."""
    eng, Phi, c = make_engine()
    result = eng.weak_field(sympy.exp(2 * Phi / c**2), order=2)
    expected = 1 + 2 * Phi / c**2 + 2 * Phi**2 / c**4
    assert sympy.simplify(result.expanded - expected) == 0


def test_coefficient_extraction():
    eng, Phi, c = make_engine()
    expr = sympy.exp(2 * Phi / c**2)
    coeff1 = eng.coefficient(expr, power=1)
    coeff2 = eng.coefficient(expr, power=2)
    assert coeff1 == 2
    assert coeff2 == 2


def test_expand_and_collect():
    eng, Phi, c = make_engine()
    expr = sympy.exp(Phi / c**2)
    coeffs = eng.expand_and_collect(expr, order=2)
    assert coeffs[0] == 1
    assert coeffs[1] == 1
    assert coeffs[2] == sympy.Rational(1, 2)


def test_expansion_order_recorded():
    eng, Phi, c = make_engine()
    result = eng.weak_field(sympy.exp(Phi / c**2), order=3)
    assert result.order == 3
