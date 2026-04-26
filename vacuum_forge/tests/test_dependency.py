"""Tests for dependency tracking."""

from vacuumforge.core.dependency import DependencyGraph, DerivationRecord


def test_add_dependency():
    g = DependencyGraph()
    g.add_dependency("result.gamma_v", "assumption.A_exponential")
    deps = g.of("result.gamma_v")
    assert "assumption.A_exponential" in deps


def test_tree():
    g = DependencyGraph()
    g.add_dependency("B", "A")
    g.add_dependency("C", "B")
    tree = g.tree("C")
    assert "A" in tree
    assert "B" in tree


def test_uses_assumption():
    g = DependencyGraph()
    g.add_dependency("B", "A")
    g.add_dependency("C", "B")
    assert g.uses_assumption("C", "A")
    assert not g.uses_assumption("A", "C")


def test_record_derivation():
    g = DependencyGraph()
    rec = DerivationRecord(
        id="deriv.gamma",
        operation="extract_gamma",
        inputs=["metric.gij"],
        assumptions=["A_exponential", "B_reciprocal"],
        outputs=["result.gamma_v"],
    )
    g.record_derivation(rec)
    deps = g.tree("result.gamma_v")
    assert "A_exponential" in deps
    assert "B_reciprocal" in deps
    assert "metric.gij" in deps


def test_dependents():
    g = DependencyGraph()
    g.add_dependency("B", "A")
    g.add_dependency("C", "A")
    dependents = g.dependents_of("A")
    assert "B" in dependents
    assert "C" in dependents


def test_summary():
    g = DependencyGraph()
    g.add_dependency("B", "A")
    s = g.summary()
    assert "Dependency Graph" in s
