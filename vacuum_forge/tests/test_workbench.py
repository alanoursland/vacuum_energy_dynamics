"""Tests for the equal-response workbench (M36)."""

import sympy
from vacuumforge.workbenches.equal_response import (
    classify_demos,
    demo_assumed_reciprocal,
    demo_free_gamma,
    demo_parallel_scaling,
    demo_reciprocal_exponential,
    demo_trace_free_exchange,
    equal_response,
    run_standard_comparison,
)
from vacuumforge.comparison.classification import ModelClass


def test_workbench_creation():
    ctx = equal_response()
    assert ctx.name == "equal_response_workbench"
    assert ctx._mode_symbols is not None
    assert ctx._targets is not None
    assert len(ctx.requirements.list()) > 0
    assert len(ctx.theorems.list()) > 0


def test_demo_reciprocal():
    ctx = demo_reciprocal_exponential()
    results = ctx.requirements.validate_all(ctx)
    rs = {r.requirement_id: r for r in results}
    assert rs["reciprocal_scaling"].status == "pass"
    assert rs["gamma_v_one"].status == "pass"
    assert rs["beta_one"].status == "pass"


def test_demo_parallel():
    ctx = demo_parallel_scaling()
    results = ctx.requirements.validate_all(ctx)
    rs = {r.requirement_id: r for r in results}
    assert rs["reciprocal_scaling"].status == "fail"


def test_demo_free_gamma():
    ctx = demo_free_gamma()
    results = ctx.requirements.validate_all(ctx)
    rs = {r.requirement_id: r for r in results}
    assert rs["gamma_v_one"].status == "fail"


def test_demo_trace_free_exchange():
    ctx = demo_trace_free_exchange()
    results = ctx.requirements.validate_all(ctx)
    rs = {r.requirement_id: r for r in results}
    assert rs["trace_free_exchange"].status == "assumed"
    assert rs["positive_energy"].status == "pass"


def test_demo_assumed_reciprocal():
    ctx = demo_assumed_reciprocal()
    results = ctx.requirements.validate_all(ctx)
    rs = {r.requirement_id: r for r in results}
    assert rs["reciprocal_scaling"].status == "assumed"


def test_standard_comparison():
    md = run_standard_comparison()
    assert "Model Comparison" in md
    assert "reciprocal_exponential" in md
    assert "parallel_scaling" in md


def test_classify_all_demos():
    classifications = classify_demos()

    assert classifications["reciprocal_exponential"].primary in (
        ModelClass.DERIVES_EQUAL_RESPONSE,
        ModelClass.CANDIDATE_FOR_DEVELOPMENT,
    )
    assert classifications["assumed_reciprocal"].primary == ModelClass.ASSUMES_EQUAL_RESPONSE
    assert classifications["parallel_scaling"].primary == ModelClass.PREDICTS_WRONG_WEAK_FIELD
    assert classifications["free_gamma"].primary == ModelClass.LEAVES_GAMMA_FREE
