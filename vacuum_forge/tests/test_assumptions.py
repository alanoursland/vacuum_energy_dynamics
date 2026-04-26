"""Tests for assumption management."""

import sympy
from vacuumforge.core.assumptions import AssumptionManager


def test_add_and_get():
    mgr = AssumptionManager()
    A, B = sympy.symbols("A B", positive=True)
    mgr.add("reciprocal", sympy.Eq(B, 1 / A))
    assert mgr.has("reciprocal")
    rec = mgr.get("reciprocal")
    assert isinstance(rec.expression, sympy.Eq)


def test_remove():
    mgr = AssumptionManager()
    mgr.add("test", sympy.Eq(sympy.Symbol("x"), 1))
    mgr.remove("test")
    assert not mgr.has("test")


def test_substitution_map():
    mgr = AssumptionManager()
    A, B = sympy.symbols("A B", positive=True)
    mgr.add("B_reciprocal", sympy.Eq(B, 1 / A))
    subs = mgr.substitution_map()
    assert B in subs
    assert subs[B] == 1 / A


def test_apply():
    mgr = AssumptionManager()
    A, B = sympy.symbols("A B", positive=True)
    mgr.add("B_reciprocal", sympy.Eq(B, 1 / A))
    result = mgr.apply(A * B)
    assert sympy.simplify(result - 1) == 0


def test_apply_specific():
    mgr = AssumptionManager()
    x, y = sympy.symbols("x y")
    mgr.add("x_val", sympy.Eq(x, 2))
    mgr.add("y_val", sympy.Eq(y, 3))
    result = mgr.apply_specific(x + y, ["x_val"])
    assert result == 2 + y


def test_active():
    mgr = AssumptionManager()
    mgr.add("a1", sympy.Eq(sympy.Symbol("x"), 1))
    mgr.add("a2", sympy.Eq(sympy.Symbol("y"), 2))
    assert len(mgr.active()) == 2


def test_inequality_detection():
    mgr = AssumptionManager()
    x = sympy.Symbol("x")
    mgr.add("x_pos", x > 0)
    rec = mgr.get("x_pos")
    assert rec.assumption_type == "inequality"
