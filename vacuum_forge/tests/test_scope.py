"""Tests for coordinate scope annotation (M30)."""

from vacuumforge.core.scope import (
    ScopeLevel,
    ScopeManager,
    ScopeMismatch,
    check_scope_compatibility,
)


def test_compatible_scope():
    result = check_scope_compatibility(
        ScopeLevel.PPN_WEAK_FIELD, ScopeLevel.STATIC_ISOTROPIC
    )
    assert result is None  # broader result covers narrower requirement


def test_incompatible_scope():
    result = check_scope_compatibility(
        ScopeLevel.ALGEBRAIC, ScopeLevel.PPN_WEAK_FIELD
    )
    assert result is not None
    assert isinstance(result, ScopeMismatch)
    assert "may not generalize" in result.message


def test_same_scope():
    result = check_scope_compatibility(
        ScopeLevel.STATIC_ISOTROPIC, ScopeLevel.STATIC_ISOTROPIC
    )
    assert result is None


def test_scope_manager():
    mgr = ScopeManager()
    assert mgr.default == ScopeLevel.ALGEBRAIC

    mgr.annotate("result.gamma_v", ScopeLevel.PPN_WEAK_FIELD)
    rec = mgr.get("result.gamma_v")
    assert rec is not None
    assert rec.scope == ScopeLevel.PPN_WEAK_FIELD


def test_scope_manager_check_pass():
    mgr = ScopeManager()
    mgr.annotate("gamma_v", ScopeLevel.PPN_WEAK_FIELD)
    mismatch = mgr.check("gamma_v", ScopeLevel.STATIC_ISOTROPIC)
    assert mismatch is None


def test_scope_manager_check_fail():
    mgr = ScopeManager()
    mgr.annotate("gamma_v", ScopeLevel.ALGEBRAIC)
    mismatch = mgr.check("gamma_v", ScopeLevel.PPN_WEAK_FIELD)
    assert mismatch is not None


def test_scope_summary():
    mgr = ScopeManager()
    mgr.annotate("test", ScopeLevel.TWO_D_SLICE)
    s = mgr.summary()
    assert "2d_time_space_slice" in s
