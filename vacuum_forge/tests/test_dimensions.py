"""Tests for dimensional checks (M28)."""

import sympy
from vacuumforge.core.dimensions import Dimension, DimensionChecker


def test_dimensionless_ratio():
    checker = DimensionChecker()
    result = checker.check_ratio("Phi", "c")
    assert result.is_valid


def test_pure_dimensionless_symbols():
    checker = DimensionChecker()
    kappa = sympy.Symbol("kappa")
    sigma = sympy.Symbol("sigma")
    result = checker.check(kappa + sigma)
    assert result.is_valid


def test_exp_phi_over_c2():
    checker = DimensionChecker()
    Phi = sympy.Symbol("Phi")
    c = sympy.Symbol("c")
    expr = sympy.exp(Phi / c**2)
    result = checker.check(expr)
    assert result.is_valid


def test_numeric_expression():
    checker = DimensionChecker()
    result = checker.check(sympy.Integer(1))
    assert result.is_valid
    assert result.dimension == Dimension.DIMENSIONLESS


def test_standard_dimensions():
    checker = DimensionChecker()
    assert checker.get_dimension("A") == Dimension.DIMENSIONLESS
    assert checker.get_dimension("Phi") == Dimension.POTENTIAL
    assert checker.get_dimension("c") == Dimension.VELOCITY


def test_custom_dimension():
    checker = DimensionChecker()
    checker.set_dimension("my_var", Dimension.LENGTH)
    assert checker.get_dimension("my_var") == Dimension.LENGTH
