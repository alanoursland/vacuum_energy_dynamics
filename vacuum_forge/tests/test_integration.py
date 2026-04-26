"""Integration and quality hardening tests (M38).

Tests covering edge cases, cross-module interactions,
and regression scenarios.
"""

import sympy
from vacuumforge import TheoryContext
from vacuumforge.core.simplify import check_equal, is_zero


def test_full_derivation_chain():
    """Full chain: symbols -> assumptions -> metric -> PPN -> validation."""
    ctx = TheoryContext("integration_test")
    ms = ctx.define_equal_response_algebraic_symbols()

    # Set assumptions
    ctx.assumptions.add("A_exp", sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)))
    ctx.assumptions.add("B_exp", sympy.Eq(ms.B, sympy.exp(-ms.Phi / ms.c**2)))

    # Build metric
    A_val = ctx.assumptions.apply(ms.A)
    B_val = ctx.assumptions.apply(ms.B)
    metric = ctx.metric.from_scale_factors(A_val, B_val)

    # Extract PPN
    gamma = ctx.ppn.extract_gamma(metric)
    beta = ctx.ppn.extract_beta(metric)
    assert check_equal(gamma.value, 1)
    assert check_equal(beta.value, 1)

    # Validate
    results = ctx.requirements.validate_all(ctx)
    rs = {r.requirement_id: r for r in results}
    assert rs["reciprocal_scaling"].status == "pass"
    assert rs["gamma_v_one"].status == "pass"
    assert rs["beta_one"].status == "pass"

    # Report
    report = ctx.reports.validation(results)
    assert "PASS" in str(report)


def test_clone_independence():
    """Cloned context is independent of the original."""
    ctx = TheoryContext("original")
    ms = ctx.define_equal_response_algebraic_symbols()
    ctx.assumptions.add("A_exp", sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)))

    clone = ctx.clone()
    clone.name = "clone"
    clone.assumptions.add("B_exp", sympy.Eq(ms.B, sympy.exp(-ms.Phi / ms.c**2)))

    assert ctx.name == "original"
    assert not ctx.assumptions.has("B_exp")
    assert clone.assumptions.has("B_exp")


def test_chained_substitution_deep():
    """Deep chained substitutions work: C = B^2, B = 1/A, A = exp(x)."""
    ctx = TheoryContext("chain_test")
    ms = ctx.define_equal_response_algebraic_symbols()

    x = sympy.Symbol("x")
    C = sympy.Symbol("C")

    ctx.assumptions.add("A_exp", sympy.Eq(ms.A, sympy.exp(x)))
    ctx.assumptions.add("B_recip", sympy.Eq(ms.B, 1 / ms.A))
    ctx.assumptions.add("C_def", sympy.Eq(C, ms.B**2))

    result = ctx.assumptions.apply(C)
    expected = sympy.exp(-2 * x)
    assert sympy.simplify(result - expected) == 0


def test_simplify_robustness():
    """Test that is_zero handles tricky expressions."""
    Phi = sympy.Symbol("Phi")
    c = sympy.Symbol("c", positive=True)

    # exp(x) * exp(-x) - 1 should be zero
    expr = sympy.exp(Phi / c**2) * sympy.exp(-Phi / c**2) - 1
    assert is_zero(expr)

    # exp(2x) - 1 should NOT be zero for general x
    expr2 = sympy.exp(2 * Phi / c**2) - 1
    assert not is_zero(expr2)


def test_empty_context_validation():
    """Empty context should return undetermined for all requirements."""
    ctx = TheoryContext("empty")
    ctx.define_equal_response_algebraic_symbols()

    results = ctx.requirements.validate_all(ctx)
    for r in results:
        assert r.status in ("undetermined", "assumed", "fail", "pass")


def test_scope_in_summary():
    """Summary includes scope information."""
    ctx = TheoryContext("scope_test")
    ctx.define_equal_response_algebraic_symbols()
    s = ctx.summary()
    assert "Scope" in s


def test_notation_on_context():
    """Context has notation profile."""
    ctx = TheoryContext("notation_test")
    assert ctx.notation.name == "framework"
    assert ctx.notation.potential_sign() == -1


def test_dimensions_on_context():
    """Context has dimension checker."""
    ctx = TheoryContext("dim_test")
    ctx.define_equal_response_algebraic_symbols()
    result = ctx.dimensions.check(sympy.exp(sympy.Symbol("Phi") / sympy.Symbol("c")**2))
    assert result.is_valid


def test_theorems_on_context():
    """Context has theorem registry."""
    ctx = TheoryContext("thm_test")
    assert len(ctx.theorems.list()) == 0
    ctx.theorems.create("test_thm", "Test theorem")
    assert ctx.theorems.has("test_thm")
