"""Tests for the research examples library (M39)."""

from vacuumforge.examples import ALL_EXAMPLES, run_example, run_all_examples


def test_all_examples_exist():
    """At least 9 examples are defined."""
    assert len(ALL_EXAMPLES) >= 9


def test_reciprocal_exponential():
    result = run_example("reciprocal_exponential")
    assert "reciprocal_exponential" in result.name
    assert "PASS" in result.report


def test_parallel_scaling_failure():
    result = run_example("parallel_scaling_failure")
    assert "FAIL" in result.report


def test_free_gamma():
    result = run_example("free_gamma")
    assert "free_gamma" in result.name


def test_trace_free_minimization():
    result = run_example("trace_free_exchange_minimization")
    assert "trace_free" in result.name


def test_counterexample_exchange():
    result = run_example("counterexample_exchange_trace")
    assert "Counterexample" in result.report


def test_counterexample_density():
    result = run_example("counterexample_density_kappa")
    assert "Counterexample" in result.report


def test_run_all_examples():
    """All examples run without error."""
    results = run_all_examples()
    assert len(results) == len(ALL_EXAMPLES)
    for name, result in results.items():
        assert result.name == name
        assert len(result.report) > 0
