"""Tests for report generation."""

import sympy
from vacuumforge import TheoryContext
from vacuumforge.reports.markdown import generate_validation_report


def test_validation_report_structure(ctx):
    """Report contains expected sections."""
    ms = ctx._mode_symbols
    ctx.assumptions.add("A_exp", sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)))
    ctx.assumptions.add("B_exp", sympy.Eq(ms.B, sympy.exp(-ms.Phi / ms.c**2)))

    results = ctx.requirements.validate_all(ctx)
    report = generate_validation_report(ctx, results)

    assert "# Validation Report" in report
    assert "Active Assumptions" in report
    assert "Requirement Validation" in report
    assert "Summary" in report
    assert "PASS" in report


def test_report_shows_failures(ctx):
    """Report includes failure section when things fail."""
    ms = ctx._mode_symbols
    gamma_v = ms.gamma_v
    ctx.assumptions.add("A_exp", sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)))
    ctx.assumptions.add("B_free", sympy.Eq(ms.B, sympy.exp(-gamma_v * ms.Phi / ms.c**2)))

    results = ctx.requirements.validate_all(ctx)
    report = generate_validation_report(ctx, results)

    assert "FAIL" in report


def test_report_shows_assumed(ctx):
    """Report includes assumption warning when targets are assumed."""
    ms = ctx._mode_symbols
    ctx.assumptions.add("B_reciprocal", sympy.Eq(ms.B, 1 / ms.A))

    results = ctx.requirements.validate_all(ctx)
    report = generate_validation_report(ctx, results)

    assert "ASSUMED" in report
    assert "Assumption Warnings" in report


def test_report_manager(ctx):
    """Test the ReportManager proxy."""
    ms = ctx._mode_symbols
    ctx.assumptions.add("A_exp", sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)))
    ctx.assumptions.add("B_exp", sympy.Eq(ms.B, sympy.exp(-ms.Phi / ms.c**2)))

    handle = ctx.reports.validation()
    assert "Validation Report" in str(handle)
