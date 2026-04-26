"""Tests for the symbolic variable registry."""

import sympy
from vacuumforge.core.symbols import SymbolRegistry


def test_define_constant():
    reg = SymbolRegistry()
    c = reg.define_constant("c", positive=True, description="Speed of light")
    assert isinstance(c, sympy.Symbol)
    assert c.is_positive
    assert reg.record("c").kind == "constant"
    assert reg.record("c").description == "Speed of light"


def test_define_coordinate():
    reg = SymbolRegistry()
    r = reg.define_coordinate("r", positive=True)
    assert r.is_positive
    assert reg.record("r").kind == "coordinate"


def test_define_function():
    reg = SymbolRegistry()
    r = sympy.Symbol("r")
    Phi = reg.define_function("Phi", args=[r])
    assert Phi.has(r)
    assert reg.record("Phi").kind == "function"


def test_define_source():
    reg = SymbolRegistry()
    Ja = reg.define_source("J_a")
    assert isinstance(Ja, sympy.Symbol)
    assert reg.record("J_a").kind == "source"


def test_define_coefficient():
    reg = SymbolRegistry()
    Ck = reg.define_coefficient("C_kappa", positive=True)
    assert Ck.is_positive
    assert reg.record("C_kappa").kind == "coefficient"


def test_list_by_kind():
    reg = SymbolRegistry()
    reg.define_constant("c", positive=True)
    reg.define_constant("G", positive=True)
    reg.define_coordinate("r", positive=True)
    assert len(reg.list("constant")) == 2
    assert len(reg.list("coordinate")) == 1


def test_get_symbol():
    reg = SymbolRegistry()
    c = reg.define_constant("c", positive=True)
    assert reg.get("c") is c


def test_has_symbol():
    reg = SymbolRegistry()
    reg.define_constant("c")
    assert reg.has("c")
    assert not reg.has("x")


def test_summary():
    reg = SymbolRegistry()
    reg.define_constant("c", positive=True, description="Speed of light")
    s = reg.summary()
    assert "Speed of light" in s
