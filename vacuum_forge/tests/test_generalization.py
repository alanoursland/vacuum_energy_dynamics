"""Tests for 3+1 generalization (M34)."""

import sympy
from vacuumforge.modes.generalization import (
    GeneralModeDecomposition,
    decompose_2d,
    decompose_3plus1,
    decompose_general,
)


def test_2d_decomposition():
    """Standard 2D case: kappa = (a+b)/2, sigma = (a-b)/2."""
    a, b = sympy.symbols("a b")
    result = decompose_2d(a, b)

    assert result.trace == (a + b) / 2
    assert len(result.trace_free) == 1
    assert sympy.simplify(result.trace_free[0] - (a - b) / 2) == 0  # b - b = 0, but trace_free is b - b = 0?

    # Actually trace_free is b - spatial_mean = b - b = 0 for 1 spatial var
    # Wait, no: trace_free = [b - b] = [0] for the spatial part
    # The shear (a-b)/2 is not directly the trace_free of spatial
    # Let me check: spatial_mean = b/1 = b, so trace_free = [b - b] = [0]
    # The 2D decomposition is special-cased in decompose_2d
    assert not result.is_experimental


def test_3plus1_basic():
    """3+1 decomposition with three spatial variables."""
    a, b1, b2, b3 = sympy.symbols("a b1 b2 b3")
    result = decompose_3plus1(a, b1, b2, b3)

    # Trace: (a + b1 + b2 + b3) / 4
    expected_trace = (a + b1 + b2 + b3) / 4
    assert sympy.simplify(result.trace - expected_trace) == 0

    # Should be experimental
    assert result.is_experimental
    assert len(result.warnings) > 0


def test_3plus1_trace_free_sum_zero():
    """Trace-free parts should sum to zero."""
    a, b1, b2, b3 = sympy.symbols("a b1 b2 b3")
    result = decompose_3plus1(a, b1, b2, b3)

    total = sum(result.trace_free)
    assert sympy.simplify(total) == 0


def test_general_n_spatial():
    """General decomposition with arbitrary spatial count."""
    a = sympy.Symbol("a")
    bs = sympy.symbols("b1:6")  # b1, b2, b3, b4, b5
    result = decompose_general(a, list(bs))

    assert result.n_spatial == 5
    total_tf = sum(result.trace_free)
    assert sympy.simplify(total_tf) == 0


def test_isotropic_3plus1():
    """Isotropic case: b1 = b2 = b3 = b. Trace-free should all vanish."""
    a, b = sympy.symbols("a b")
    result = decompose_3plus1(a, b, b, b)

    for tf in result.trace_free:
        assert sympy.simplify(tf) == 0

    # Trace is (a + 3b) / 4
    expected = (a + 3 * b) / 4
    assert sympy.simplify(result.trace - expected) == 0
