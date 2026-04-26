"""Tests for notebook/terminal display (M32)."""

import sympy
from vacuumforge import TheoryContext
from vacuumforge.display import DisplayProxy


def test_display_proxy_exists(ctx):
    """Context has a display property."""
    assert ctx.display is not None
    assert isinstance(ctx.display, DisplayProxy)


def test_display_assumptions(ctx, capsys):
    """Display assumptions prints something."""
    ms = ctx._mode_symbols
    ctx.assumptions.add("A_exp", sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)))
    ctx.display.assumptions()
    captured = capsys.readouterr()
    assert "A_exp" in captured.out


def test_display_symbols(ctx, capsys):
    """Display symbols prints something."""
    ctx.display.symbols()
    captured = capsys.readouterr()
    assert len(captured.out) > 0


def test_display_validation(ctx, capsys):
    """Display validation results prints something."""
    ms = ctx._mode_symbols
    ctx.assumptions.add("A_exp", sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)))
    ctx.assumptions.add("B_exp", sympy.Eq(ms.B, sympy.exp(-ms.Phi / ms.c**2)))
    ctx.display.validation_results()
    captured = capsys.readouterr()
    assert "reciprocal_scaling" in captured.out


def test_display_sources_empty(ctx, capsys):
    """Display sources when none defined."""
    ctx.display.sources()
    captured = capsys.readouterr()
    assert "No sources" in captured.out


def test_display_energy_empty(ctx, capsys):
    """Display energy when none defined."""
    ctx.display.energy()
    captured = capsys.readouterr()
    assert "No energy" in captured.out
