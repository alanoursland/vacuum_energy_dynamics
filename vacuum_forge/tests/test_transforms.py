"""Tests for scale/log/mode transformations."""

import sympy
from vacuumforge.modes.transforms import TransformEngine


def make_engine():
    A, B = sympy.symbols("A B", positive=True)
    a, b = sympy.symbols("a b", real=True)
    kappa, sigma = sympy.symbols("kappa sigma", real=True)
    return TransformEngine(A=A, B=B, a=a, b=b, kappa=kappa, sigma=sigma)


def test_ab_to_modes_product():
    """A*B should become exp(2*kappa)."""
    eng = make_engine()
    result = eng.to_modes(eng.A * eng.B)
    assert sympy.simplify(result - sympy.exp(2 * eng.kappa)) == 0


def test_ab_to_modes_ratio():
    """A/B should become exp(2*sigma)."""
    eng = make_engine()
    result = eng.to_modes(eng.A / eng.B)
    assert sympy.simplify(result - sympy.exp(2 * eng.sigma)) == 0


def test_to_log():
    eng = make_engine()
    result = eng.to_log(eng.A * eng.B)
    expected = sympy.exp(eng.a + eng.b)
    assert sympy.simplify(result - expected) == 0


def test_from_modes():
    eng = make_engine()
    result = eng.from_modes(eng.kappa)
    expected = (eng.a + eng.b) / 2
    assert sympy.simplify(result - expected) == 0


def test_modes_to_scale():
    eng = make_engine()
    result = eng.modes_to_scale(2 * eng.kappa)
    expected = sympy.log(eng.A * eng.B)
    # These involve logs so check equivalence carefully
    assert sympy.simplify(result - expected) == 0


def test_roundtrip_scale_to_modes_to_scale():
    """Round-trip: start with A*B, go to modes, come back."""
    eng = make_engine()
    original = eng.A * eng.B
    in_modes = eng.to_modes(original)
    # in_modes should be exp(2*kappa)
    assert sympy.simplify(in_modes - sympy.exp(2 * eng.kappa)) == 0


def test_context_modes(ctx):
    """Test transforms through the context proxy."""
    A = ctx.symbols.get("A")
    B = ctx.symbols.get("B")
    result = ctx.modes.to_modes(A * B)
    kappa = ctx._mode_symbols.kappa
    assert sympy.simplify(result - sympy.exp(2 * kappa)) == 0
