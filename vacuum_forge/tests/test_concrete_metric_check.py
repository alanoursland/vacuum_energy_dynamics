"""Tests for concrete metric validation classification.

Covers Milestone 48 completion criteria:
- Schwarzschild test produces ``satisfied_by_construction``.
- Failure test produces ``failed``.
- Undetermined test produces ``undetermined``.
- The function does not modify the caller's context (uses ``ctx.clone()``).
- ``underlying_validation`` field is populated.
"""

import sympy

from vacuumforge import TheoryContext
from vacuumforge.metric.concrete_check import check_concrete_metric


def test_schwarzschild_style_reciprocal_is_by_construction():
    """B = 1/A encodes AB=1 by construction."""
    ctx = TheoryContext("concrete")
    ms = ctx.define_equal_response_algebraic_symbols()

    A_value = 1 - 2 * ms.G * ms.M / (ms.r * ms.c**2)
    B_value = 1 / A_value
    results = check_concrete_metric(ctx, A_value, B_value, ["reciprocal_scaling"])

    assert results[0].status == "satisfied_by_construction"
    assert results[0].leak_report is not None
    assert results[0].leak_report.leaked is True
    assert "concrete_metric_B" in results[0].leak_report.leaked_via


def test_concrete_metric_failure():
    """A = 1 + Φ/c², B = 1 does not satisfy AB=1."""
    ctx = TheoryContext("concrete_fail")
    ms = ctx.define_equal_response_algebraic_symbols()

    results = check_concrete_metric(
        ctx, 1 + ms.Phi / ms.c**2, sympy.Integer(1), ["reciprocal_scaling"]
    )

    assert results[0].status == "failed"


def test_undetermined_without_mode_symbols():
    """If mode symbols are not defined, result should be undetermined."""
    ctx = TheoryContext("concrete_undet")
    # Do NOT call define_equal_response_algebraic_symbols.
    results = check_concrete_metric(ctx, sympy.Integer(1), sympy.Integer(1))

    assert len(results) == 1
    assert results[0].status == "undetermined"


def test_does_not_modify_caller_context():
    """check_concrete_metric should not add assumptions to the caller's context."""
    ctx = TheoryContext("concrete_clone")
    ms = ctx.define_equal_response_algebraic_symbols()
    original_assumption_ids = set(ctx.assumptions.ids())

    check_concrete_metric(ctx, sympy.Integer(1), sympy.Integer(1), ["reciprocal_scaling"])

    assert set(ctx.assumptions.ids()) == original_assumption_ids


def test_underlying_validation_populated():
    """The result should contain the underlying ValidationResult."""
    ctx = TheoryContext("concrete_val")
    ms = ctx.define_equal_response_algebraic_symbols()

    A_value = 1 - 2 * ms.G * ms.M / (ms.r * ms.c**2)
    B_value = 1 / A_value
    results = check_concrete_metric(ctx, A_value, B_value, ["reciprocal_scaling"])

    assert results[0].underlying_validation is not None
    assert hasattr(results[0].underlying_validation, "status")
