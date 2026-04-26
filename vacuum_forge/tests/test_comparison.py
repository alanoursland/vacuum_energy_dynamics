"""Tests for model comparison and classification (M26-M27)."""

import sympy
from vacuumforge import TheoryContext
from vacuumforge.comparison.compare import (
    ModelComparison,
    ModelSummary,
    compare_models,
    summarize_model,
)
from vacuumforge.comparison.classification import (
    ModelClass,
    classify_model,
)


def _make_reciprocal_ctx() -> TheoryContext:
    ctx = TheoryContext("reciprocal_exponential")
    ms = ctx.define_equal_response_algebraic_symbols()
    ctx.assumptions.add("A_exp", sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)))
    ctx.assumptions.add("B_exp", sympy.Eq(ms.B, sympy.exp(-ms.Phi / ms.c**2)))
    return ctx


def _make_parallel_ctx() -> TheoryContext:
    ctx = TheoryContext("parallel_scaling")
    ms = ctx.define_equal_response_algebraic_symbols()
    ctx.assumptions.add("A_exp", sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)))
    ctx.assumptions.add("B_exp", sympy.Eq(ms.B, sympy.exp(ms.Phi / ms.c**2)))
    return ctx


def _make_assumed_ctx() -> TheoryContext:
    ctx = TheoryContext("assumed_reciprocal")
    ms = ctx.define_equal_response_algebraic_symbols()
    ctx.assumptions.add("B_reciprocal", sympy.Eq(ms.B, 1 / ms.A))
    return ctx


def test_summarize_reciprocal():
    ctx = _make_reciprocal_ctx()
    summary = summarize_model(ctx)
    assert summary.name == "reciprocal_exponential"
    assert summary.reciprocal_status == "pass"
    assert "reciprocal_scaling" in summary.passed_requirements


def test_summarize_parallel():
    ctx = _make_parallel_ctx()
    summary = summarize_model(ctx)
    assert summary.reciprocal_status == "fail"
    assert "reciprocal_scaling" in summary.failed_requirements


def test_compare_two_models():
    ctxs = [_make_reciprocal_ctx(), _make_parallel_ctx()]
    comparison = compare_models(ctxs)
    assert len(comparison.models) == 2
    md = comparison.to_markdown()
    assert "reciprocal_exponential" in md
    assert "parallel_scaling" in md


def test_classify_derives():
    ctx = _make_reciprocal_ctx()
    ms = ctx._mode_symbols
    ctx.energy.quadratic_modes(ms.C_kappa, ms.C_sigma, ms.kappa, ms.sigma)
    result = classify_model(ctx)
    assert result.primary == ModelClass.DERIVES_EQUAL_RESPONSE


def test_classify_assumes():
    ctx = _make_assumed_ctx()
    result = classify_model(ctx)
    assert result.primary == ModelClass.ASSUMES_EQUAL_RESPONSE


def test_classify_parallel_wrong_weak_field():
    ctx = _make_parallel_ctx()
    result = classify_model(ctx)
    assert result.primary == ModelClass.PREDICTS_WRONG_WEAK_FIELD


def test_classify_free_gamma():
    ctx = TheoryContext("free_gamma")
    ms = ctx.define_equal_response_algebraic_symbols()
    ctx.assumptions.add("A_exp", sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)))
    ctx.assumptions.add(
        "B_free_gamma",
        sympy.Eq(ms.B, sympy.exp(-ms.gamma_v * ms.Phi / ms.c**2)),
    )
    result = classify_model(ctx)
    assert result.primary == ModelClass.LEAVES_GAMMA_FREE


def test_comparison_markdown_table():
    ctxs = [_make_reciprocal_ctx(), _make_assumed_ctx()]
    comparison = compare_models(ctxs)
    md = comparison.to_markdown()
    assert "| Reciprocal Scaling |" in md
    assert "| Passed |" in md
