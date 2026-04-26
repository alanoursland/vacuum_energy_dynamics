"""Tests for TheoryContext creation and basic operations."""

from vacuumforge import TheoryContext, Status


def test_create_context():
    ctx = TheoryContext("test_model")
    assert ctx.name == "test_model"


def test_context_has_registries(bare_ctx):
    assert bare_ctx.symbols is not None
    assert bare_ctx.assumptions is not None
    assert bare_ctx.expressions is not None
    assert bare_ctx.dependencies is not None
    assert bare_ctx.ledger is not None
    assert bare_ctx.sources is not None


def test_define_standard_symbols(ctx):
    assert ctx.symbols.has("A")
    assert ctx.symbols.has("B")
    assert ctx.symbols.has("kappa")
    assert ctx.symbols.has("sigma")
    assert ctx.symbols.has("c")
    assert ctx.symbols.has("Phi")
    assert ctx.symbols.has("gamma_v")
    assert ctx.symbols.has("beta")


def test_context_clone(ctx):
    import sympy as sp
    clone = ctx.clone()
    clone.assumptions.add("test_assumption", sp.Eq(sp.Symbol("x"), 1))
    assert clone.assumptions.has("test_assumption")
    assert not ctx.assumptions.has("test_assumption")


def test_context_summary(ctx):
    s = ctx.summary()
    assert "TheoryContext" in s
    assert "Symbol Registry" in s
