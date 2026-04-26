"""Tests for theorem candidate system (M35)."""

from vacuumforge.theorems.candidates import TheoremCandidate, TheoremRegistry


def test_create_candidate():
    tc = TheoremCandidate(
        id="trace_free_exchange",
        statement="Local exchange is trace-free.",
    )
    assert tc.status == "candidate"
    assert tc.confidence_level == "unverified"
    assert not tc.is_refuted


def test_add_support():
    tc = TheoremCandidate(
        id="test", statement="Test theorem.",
    )
    tc.add_support("reciprocal_model", "AB=1 holds")
    assert len(tc.supporting_models) == 1
    assert tc.confidence_level == "weak"


def test_add_counterexample():
    tc = TheoremCandidate(
        id="test", statement="Test theorem.",
    )
    tc.add_counterexample("mixed_source", "J_kappa != 0")
    assert tc.is_refuted
    assert tc.status == "refuted"
    assert tc.confidence_level == "refuted"


def test_registry():
    reg = TheoremRegistry()
    tc = reg.create("tc1", "Statement 1")
    assert reg.has("tc1")
    assert reg.get("tc1") is tc
    assert len(reg.list()) == 1


def test_registry_active_vs_refuted():
    reg = TheoremRegistry()
    tc1 = reg.create("tc1", "Active theorem")
    tc2 = reg.create("tc2", "Refuted theorem")
    tc2.add_counterexample("cx", "reason")

    assert len(reg.active()) == 1
    assert len(reg.refuted()) == 1


def test_theorem_markdown():
    tc = TheoremCandidate(
        id="trace_free",
        statement="Exchange is trace-free.",
        scope="algebraic_prototype",
        assumptions=["exchange-creation separation"],
    )
    tc.add_support("model_a", "passes")
    md = tc.to_markdown()
    assert "trace_free" in md
    assert "Exchange is trace-free" in md
    assert "model_a" in md


def test_registry_summary():
    reg = TheoremRegistry()
    reg.create("tc1", "First theorem")
    reg.create("tc2", "Second theorem")
    summary = reg.summary()
    assert "tc1" in summary
    assert "tc2" in summary
