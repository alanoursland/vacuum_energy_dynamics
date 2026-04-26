"""Shared fixtures for VacuumForge tests."""

import pytest
from vacuumforge import TheoryContext


@pytest.fixture
def ctx():
    """A fresh TheoryContext with standard algebraic symbols."""
    c = TheoryContext("test")
    c.define_equal_response_algebraic_symbols()
    return c


@pytest.fixture
def bare_ctx():
    """A bare TheoryContext with no symbols defined."""
    return TheoryContext("bare_test")
