"""Tests for source decomposition and classification."""

import sympy
from vacuumforge.core.status import SourceClass
from vacuumforge.modes.sources import (
    SourceManager,
    classify_source,
    decompose_ab_to_modes,
    decompose_modes_to_ab,
)


def test_decompose_ab_to_modes():
    Ja, Jb = sympy.symbols("J_a J_b")
    Jk, Js = decompose_ab_to_modes(Ja, Jb)
    assert sympy.simplify(Jk - (Ja + Jb)) == 0
    assert sympy.simplify(Js - (Ja - Jb)) == 0


def test_decompose_modes_to_ab():
    Jk, Js = sympy.symbols("J_kappa J_sigma")
    Ja, Jb = decompose_modes_to_ab(Jk, Js)
    assert sympy.simplify(Ja - (Jk + Js) / 2) == 0
    assert sympy.simplify(Jb - (Jk - Js) / 2) == 0


def test_roundtrip_decomposition():
    Ja, Jb = sympy.symbols("J_a J_b")
    Jk, Js = decompose_ab_to_modes(Ja, Jb)
    Ja2, Jb2 = decompose_modes_to_ab(Jk, Js)
    assert sympy.simplify(Ja2 - Ja) == 0
    assert sympy.simplify(Jb2 - Jb) == 0


def test_classify_trace_free():
    Js = sympy.Symbol("J_sigma")
    assert classify_source(sympy.Integer(0), Js) == SourceClass.TRACE_FREE


def test_classify_pure_trace():
    Jk = sympy.Symbol("J_kappa")
    assert classify_source(Jk, sympy.Integer(0)) == SourceClass.PURE_TRACE


def test_classify_mixed():
    Jk = sympy.Symbol("J_kappa")
    Js = sympy.Symbol("J_sigma")
    assert classify_source(Jk, Js) == SourceClass.MIXED


def test_classify_zero():
    assert classify_source(sympy.Integer(0), sympy.Integer(0)) == SourceClass.ZERO


def test_manager_exchange_trace_free():
    mgr = SourceManager()
    Js = sympy.Symbol("J_sigma")
    rec = mgr.exchange_trace_free(Js)
    assert rec.classification == SourceClass.TRACE_FREE
    assert rec.source_type == "exchange"
    assert rec.assumed_trace_free is True


def test_manager_creation_uniform():
    mgr = SourceManager()
    Jc = sympy.Symbol("J_c")
    rec = mgr.creation_uniform(Jc)
    assert rec.classification == SourceClass.PURE_TRACE
    assert rec.source_type == "creation"


def test_manager_add_ab():
    mgr = SourceManager()
    Ja = sympy.Symbol("J_a")
    rec = mgr.add_ab("test", Ja, Ja)
    # Equal sources: J_kappa = 2*Ja, J_sigma = 0
    assert rec.classification == SourceClass.PURE_TRACE


def test_manager_add_ab_opposite():
    mgr = SourceManager()
    Ja = sympy.Symbol("J_a")
    rec = mgr.add_ab("test", Ja, -Ja)
    # Opposite sources: J_kappa = 0, J_sigma = 2*Ja
    assert rec.classification == SourceClass.TRACE_FREE
