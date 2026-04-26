"""Tests for PPN parameter extraction."""

import sympy
from vacuumforge.metric.expansion import ExpansionEngine
from vacuumforge.metric.ppn import extract_beta, extract_gamma
from vacuumforge.metric.weak_field import WeakFieldMetric


def make_engine():
    Phi = sympy.Symbol("Phi")
    c = sympy.Symbol("c", positive=True)
    return ExpansionEngine(Phi, c), Phi, c


def test_gamma_reciprocal_exponential():
    """B = exp(-Phi/c^2) => gamma_v = 1."""
    eng, Phi, c = make_engine()
    A = sympy.exp(Phi / c**2)
    B = sympy.exp(-Phi / c**2)
    metric = WeakFieldMetric(A, B)
    result = extract_gamma(metric, eng)
    assert result.value == 1


def test_beta_exponential():
    """A = exp(Phi/c^2) => beta = 1."""
    eng, Phi, c = make_engine()
    A = sympy.exp(Phi / c**2)
    B = sympy.exp(-Phi / c**2)
    metric = WeakFieldMetric(A, B)
    result = extract_beta(metric, eng)
    assert result.value == 1


def test_gamma_free():
    """B = exp(-gamma_v * Phi/c^2) => gamma_v remains symbolic."""
    eng, Phi, c = make_engine()
    gamma_v = sympy.Symbol("gamma_v")
    A = sympy.exp(Phi / c**2)
    B = sympy.exp(-gamma_v * Phi / c**2)
    metric = WeakFieldMetric(A, B)
    result = extract_gamma(metric, eng)
    assert result.value == gamma_v


def test_gamma_parallel_scaling():
    """B = exp(Phi/c^2) (same as A) => gamma_v = -1."""
    eng, Phi, c = make_engine()
    A = sympy.exp(Phi / c**2)
    B = sympy.exp(Phi / c**2)
    metric = WeakFieldMetric(A, B)
    result = extract_gamma(metric, eng)
    assert result.value == -1


def test_gamma_power_family():
    """B = A^(-p) => gamma_v = p when A = exp(Phi/c^2)."""
    eng, Phi, c = make_engine()
    p = sympy.Symbol("p")
    A = sympy.exp(Phi / c**2)
    B = A**(-p)
    metric = WeakFieldMetric(A, B)
    result = extract_gamma(metric, eng)
    assert result.value == p


def test_beta_alpha_family():
    """A = exp(alpha*Phi/c^2) => beta = alpha^2 under the standard normalization.

    Standard PPN form: -g00 = 1 + 2*(Phi/c^2) + 2*beta*(Phi/c^2)^2
    With A = exp(alpha*Phi/c^2): -g00 = A^2 = exp(2*alpha*Phi/c^2)
    First order coefficient = 2*alpha, but PPN convention normalizes to 2,
    so we'd need alpha=1 for standard PPN. When alpha=1: beta = 1.
    For general alpha: second-order coeff of A^2 = 2*alpha^2, so beta = alpha^2.
    """
    eng, Phi, c = make_engine()
    alpha = sympy.Symbol("alpha")
    A = sympy.exp(alpha * Phi / c**2)
    B = sympy.exp(-Phi / c**2)
    metric = WeakFieldMetric(A, B)
    result = extract_beta(metric, eng)
    assert sympy.simplify(result.value - alpha**2) == 0


def test_context_ppn(ctx):
    """Test PPN extraction through context proxy."""
    ms = ctx._mode_symbols
    A = sympy.exp(ms.Phi / ms.c**2)
    B = sympy.exp(-ms.Phi / ms.c**2)
    metric = ctx.metric.from_scale_factors(A, B)
    gamma = ctx.ppn.extract_gamma(metric)
    beta = ctx.ppn.extract_beta(metric)
    assert gamma.value == 1
    assert beta.value == 1
