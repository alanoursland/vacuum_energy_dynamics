"""Tests for counterexample generation."""

import sympy
from vacuumforge.search.counterexamples import (
    density_with_nonzero_kappa,
    exchange_with_nonzero_trace,
    parallel_scaling_failure,
)


def test_density_counterexample():
    """Density is unchanged under conformal rescaling."""
    ce = density_with_nonzero_kappa()
    assert ce.verification == 0
    assert "kappa" in ce.symbols


def test_exchange_trace_counterexample():
    """Total conservation allows nonzero trace."""
    ce = exchange_with_nonzero_trace()
    # verification should be 0 (conservation holds)
    assert sympy.simplify(ce.verification) == 0


def test_parallel_scaling_counterexample():
    """Parallel scaling gives AB != 1."""
    ce = parallel_scaling_failure()
    assert ce.verification != 0
