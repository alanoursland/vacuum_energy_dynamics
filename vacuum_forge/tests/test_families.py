"""Tests for candidate family templates."""

import sympy
from vacuumforge.metric.expansion import ExpansionEngine
from vacuumforge.metric.ppn import extract_gamma, extract_beta
from vacuumforge.metric.reciprocal import check_exact_reciprocal
from vacuumforge.metric.weak_field import WeakFieldMetric
from vacuumforge.search.families import (
    reciprocal_power_family,
    exponential_scale_family,
    scan_power_family,
)


def test_power_family_p1():
    """p=1 gives reciprocal scaling."""
    Phi = sympy.Symbol("Phi")
    c = sympy.Symbol("c", positive=True)
    A, B, p = reciprocal_power_family(Phi, c, p=1)
    result = check_exact_reciprocal(A, B)
    assert result.holds is True


def test_power_family_p_half():
    """p=1/2 fails reciprocal scaling."""
    Phi = sympy.Symbol("Phi")
    c = sympy.Symbol("c", positive=True)
    A, B, p = reciprocal_power_family(Phi, c, p=sympy.Rational(1, 2))
    result = check_exact_reciprocal(A, B)
    assert result.holds is False


def test_power_family_gamma():
    """gamma_v = p for the reciprocal power family."""
    Phi = sympy.Symbol("Phi")
    c = sympy.Symbol("c", positive=True)
    eng = ExpansionEngine(Phi, c)
    p = sympy.Symbol("p")
    A, B, _ = reciprocal_power_family(Phi, c, p=p)
    metric = WeakFieldMetric(A, B)
    result = extract_gamma(metric, eng)
    assert result.value == p


def test_exponential_scale_family():
    """General exponential family."""
    Phi = sympy.Symbol("Phi")
    c = sympy.Symbol("c", positive=True)
    A, B, alpha, lam = exponential_scale_family(Phi, c)
    eng = ExpansionEngine(Phi, c)
    metric = WeakFieldMetric(A, B)
    gamma = extract_gamma(metric, eng)
    beta = extract_beta(metric, eng)
    assert gamma.value == lam
    assert sympy.simplify(beta.value - alpha**2) == 0


def test_scan_power_family():
    """Scan p = 0, 1/2, 1, 2."""
    Phi = sympy.Symbol("Phi")
    c = sympy.Symbol("c", positive=True)
    eng = ExpansionEngine(Phi, c)
    results = scan_power_family(
        Phi, c,
        [0, sympy.Rational(1, 2), 1, 2],
        expansion_engine=eng,
    )
    assert len(results) == 4
    # p=0: gamma=0, no reciprocal
    assert results[0].gamma_v == 0
    assert results[0].reciprocal is False
    # p=1: gamma=1, reciprocal
    assert results[2].gamma_v == 1
    assert results[2].reciprocal is True
    # p=2: gamma=2, no reciprocal
    assert results[3].gamma_v == 2
    assert results[3].reciprocal is False
