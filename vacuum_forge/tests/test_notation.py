"""Tests for notation profiles (M29)."""

import sympy
from vacuumforge.core.notation import (
    FRAMEWORK_PROFILE,
    PPN_PROFILE,
    NotationProfile,
    get_profile,
)


def test_framework_profile():
    assert FRAMEWORK_PROFILE.potential_sign() == -1
    assert FRAMEWORK_PROFILE.name == "framework"


def test_ppn_profile():
    assert PPN_PROFILE.potential_sign() == 1
    assert PPN_PROFILE.name == "ppn"


def test_convert_framework_to_ppn():
    Phi = sympy.Symbol("Phi")
    U = sympy.Symbol("U")
    expr = sympy.exp(Phi)
    converted = FRAMEWORK_PROFILE.convert_potential(expr, PPN_PROFILE)
    assert converted == sympy.exp(-U)


def test_convert_ppn_to_framework():
    U = sympy.Symbol("U")
    Phi = sympy.Symbol("Phi")
    expr = sympy.exp(U)
    converted = PPN_PROFILE.convert_potential(expr, FRAMEWORK_PROFILE)
    assert converted == sympy.exp(-Phi)


def test_same_convention_no_change():
    Phi = sympy.Symbol("Phi")
    expr = sympy.exp(Phi)
    converted = FRAMEWORK_PROFILE.convert_potential(expr, FRAMEWORK_PROFILE)
    assert converted == expr


def test_get_profile():
    p = get_profile("framework")
    assert p.name == "framework"
    p2 = get_profile("ppn")
    assert p2.name == "ppn"
