"""Tests for requirement validation and assumption leak detection."""

import sympy
from vacuumforge import TheoryContext
from vacuumforge.requirements.leak_detection import detect_leaks


def test_reciprocal_scaling_derived(ctx):
    """When A and B are set via assumptions, reciprocal scaling should pass."""
    ms = ctx._mode_symbols
    ctx.assumptions.add("A_exp", sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)))
    ctx.assumptions.add("B_exp", sympy.Eq(ms.B, sympy.exp(-ms.Phi / ms.c**2)))

    results = ctx.requirements.validate_all(ctx)
    rs = {r.requirement_id: r for r in results}

    assert rs["reciprocal_scaling"].status == "pass"
    assert rs["gamma_v_one"].status == "pass"
    assert rs["beta_one"].status == "pass"


def test_reciprocal_scaling_assumed(ctx):
    """When B = 1/A is directly assumed, reciprocal scaling should be 'assumed'."""
    ms = ctx._mode_symbols
    ctx.assumptions.add("B_reciprocal", sympy.Eq(ms.B, 1 / ms.A))

    results = ctx.requirements.validate_all(ctx)
    rs = {r.requirement_id: r for r in results}

    assert rs["reciprocal_scaling"].status == "assumed"


def test_free_gamma_fails(ctx):
    """When gamma_v is left free, gamma_v = 1 should fail."""
    ms = ctx._mode_symbols
    ctx.assumptions.add("A_exp", sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)))
    gamma_v = ms.gamma_v
    ctx.assumptions.add("B_free", sympy.Eq(ms.B, sympy.exp(-gamma_v * ms.Phi / ms.c**2)))

    results = ctx.requirements.validate_all(ctx)
    rs = {r.requirement_id: r for r in results}

    # gamma_v remains symbolic, should fail unless gamma_v happens to be 1
    assert rs["gamma_v_one"].status == "fail"


def test_leak_detection_direct(ctx):
    """Direct leak: B = 1/A should be detected."""
    ms = ctx._mode_symbols
    ctx.assumptions.add("B_reciprocal", sympy.Eq(ms.B, 1 / ms.A))

    leak = detect_leaks("reciprocal_scaling", ctx.assumptions, ctx._targets)
    assert leak.leaked is True
    assert "B_reciprocal" in leak.leaked_via


def test_leak_detection_kappa_zero(ctx):
    """Leak via kappa = 0."""
    ms = ctx._mode_symbols
    ctx.assumptions.add("kappa_zero", sympy.Eq(ms.kappa, 0))

    leak = detect_leaks("kappa_zero", ctx.assumptions, ctx._targets)
    assert leak.leaked is True


def test_no_leak_when_clean(ctx):
    """No leak when only temporal ansatz is assumed."""
    ms = ctx._mode_symbols
    ctx.assumptions.add("A_exp", sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)))

    leak = detect_leaks("reciprocal_scaling", ctx.assumptions, ctx._targets)
    assert leak.leaked is False


def test_trace_free_exchange_assumed(ctx):
    """Exchange trace-free by direct declaration should be 'assumed'."""
    Js = sympy.Symbol("J_s")
    ctx.sources.exchange_trace_free(Js)

    results = ctx.requirements.validate_all(ctx)
    rs = {r.requirement_id: r for r in results}

    assert rs["trace_free_exchange"].status == "assumed"


def test_positive_energy_passes(ctx):
    """Quadratic energy with positive coefficients passes."""
    ms = ctx._mode_symbols
    ctx.energy.quadratic_modes(ms.C_kappa, ms.C_sigma, ms.kappa, ms.sigma)

    results = ctx.requirements.validate_all(ctx)
    rs = {r.requirement_id: r for r in results}

    assert rs["positive_energy"].status == "pass"


def test_validation_summary(ctx):
    """Test the summary output."""
    ms = ctx._mode_symbols
    ctx.assumptions.add("A_exp", sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)))
    ctx.assumptions.add("B_exp", sympy.Eq(ms.B, sympy.exp(-ms.Phi / ms.c**2)))

    results = ctx.requirements.validate_all(ctx)
    summary = ctx.requirements.summary(results)
    assert "reciprocal_scaling" in summary
    assert "gamma_v_one" in summary
